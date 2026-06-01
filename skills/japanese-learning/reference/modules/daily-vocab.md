# 每日词汇 (Daily Vocabulary)

## 触发词
单词、词汇、vocabulary、今日の単語、Anki、new words

## 流程

1. **读取记忆**：
   - 从 `profile.json` 获取：level、interests、dailyVocabCount、preferAnki
   - 从 `vocab-mastery.jsonl` 获取：所有 `struggling` 状态的词（需要复习）
   - 从 `vocab-mastery.jsonl` 获取：所有已学过的词（避免重复）

2. **确认参数**（仅首次或用户主动指定时才问）：
   - 等级：默认从 profile.level 读取
   - 数量：默认从 profile.preferences.dailyVocabCount 读取
   - 主题：默认从 profile.learner.interests 中轮换

3. **选词规则**：
   - 优先高频词（参考 `reference/data/jlpt-level-guide.md`）
   - **排除 vocab-mastery.jsonl 中 status 为 mastered 的词**
   - **优先安排 struggling 词汇的复习（最多占 30%）**
   - 同一课中混合词性（名/动/形/副）
   - 包含至少 2 个有汉字的词
   - 相关词优先放一组（如食物主题的词放在一起）
   - 基于 profile.level 决定难度范围

4. **每个词的输出格式**：

```
### 〈word〉 【reading】 — meaning

- **词性**：名詞/動詞/形容詞/副詞
- **例文**：（自然的例句，根据 level 决定是否标注读音）
- **搭配**：常见搭配 2-3 个
- **助记**：（字源/联想/谐音，任选最有效的）
- **音高**：用 ↑↓ 标注 pitch pattern
- **JLPT**：N?
```

5. **Anki 卡片**（如果 profile.preferences.preferAnki = true）：
   - 格式：TSV
   - 列：`正面\t背面\t例句\t标签`
   - 标签格式：`japanese::vocab::N3::YYYY-MM-DD`

6. **小测验**（5 题）：
   - 2 题配对（日→中）
   - 2 题填空（句子中填入正确的词）
   - 1 题造句（用今天的 2 个词造一个句子）
   - **记录得分**：用于会话结束时更新 vocab-mastery

7. **保存**：`~/japanese-learning/vocab/daily-vocab-YYYY-MM-DD.md`

## 间隔复习机制

基于 `vocab-mastery.jsonl` 的智能复习：

| 状态 | 复习间隔 |
|------|---------|
| new | 1 天后 |
| learning | 3 天后 |
| struggling | 每次都复习（直到连续对 2 次） |
| mastered | 不主动复习 |

每次运行时：
- 从 vocab-mastery.jsonl 中筛选需要复习的词（基于 lastReview + 上表间隔）
- 复习词放在开头的「复习区」，与新词分开展示
- 复习区的词不计入新词数量

## 会话结束时的记忆更新

本模块结束后，需要更新：
- `profile.json`: `vocab.totalLearned += 新词数`, `vocab.byLevel.NX += 对应数量`
- `vocab-mastery.jsonl`: 为每个新词追加一行（status=new），复习词更新 quizResults
- 测验中答错的词 → 如果已在 struggling 则 count+1，否则从 learning 降为 struggling
- 复习全对的词 → 检查是否满足 mastered 条件（连续 3 次正确）
