# 语法训练 (Grammar Drill)

## 触发词
语法、文法、grammar、〜てform、〜ば、想学某个语法点、接续、句型

## 流程

1. **读取记忆**：
   - 从 `profile.json` 获取：level、grammar.mastered / inProgress / struggling
   - 从 `progress/grammar-progress.json` 获取：各语法点的练习次数和状态
   - 从 `progress/error-archive.json` 获取：与语法相关的活跃错误模式

2. **确认语法点**：
   - 用户指定 → 直接使用
   - 用户不指定 → 按优先级推荐（见下方推荐逻辑）

3. **讲解输出**：

```
## 〈语法点〉

**接续**：动词て形 / 名词＋の / 形容詞＋く + ...
**核心含义**：一句话总结
**使用场景**：什么情况下用这个语法
**语感**：正式 / 随意 / 书面 / 口语
**直觉类比**：用中文/英文类比帮助理解（如果有的话）

### 例文（5 句，由简到难）
1. （简单，N5 词汇）
2. （稍难）
3. （中等）
4. （接近真题难度）
5. （复杂长句）

每句标注：读音 + 翻译 + 该语法点的位置用【】标出

### 易混辨析
- 〈语法A〉 vs 〈语法B〉
  - 区别：...
  - 判断技巧：...
  - 对比例句：...
```

4. **练习**（5 题混合）：
   - 1 题判断正误（给出句子，判断语法使用是否正确）
   - 1 题填空（从选项中选择正确的接续形式）
   - 1 题选择（4 选 1，选出正确用法）
   - 1 题改错（指出并修正错误）
   - 1 题翻译造句（中→日）

5. **批改**：
   - 用户回答后逐题批改
   - 错误的给出详细解释（不只说"错"，要说为什么错、正确的思路是什么）
   - 全对的给出进阶挑战
   - **记录得分**，用于会话结束时更新 grammar-progress

## 语法推荐逻辑

如果用户不指定语法点，按以下优先级推荐：
1. `grammar.struggling` 中的语法点（需要专项突破）
2. `grammar.inProgress` 中练习次数最少的（继续巩固）
3. `error-archive.json` 中 category=grammar 的活跃错误相关语法
4. 用户等级对应的核心语法中 `grammar-progress.json` 里没有记录的（新内容）
5. 与上次练习的语法有关联的（如学了〜たら，推荐〜ば做对比）

## 会话结束时的记忆更新

本模块结束后，需要更新：
- `progress/grammar-progress.json`:
  - 语法点不存在 → 新增，status=`in_progress`，practiceCount=1
  - 语法点已存在 → practiceCount += 1，更新 lastPractice
  - 测验全对 + practiceCount >= 3 → status 升为 `mastered`
  - 测验错误率 > 50% → status 降为 `struggling`
- `profile.json`:
  - 更新 `grammar.mastered / inProgress / struggling` 列表
  - `grammar.totalCovered` 更新
  - `grammar.byLevel.NX` 更新
- 如果发现新的错误模式 → 更新 `error-archive.json`
