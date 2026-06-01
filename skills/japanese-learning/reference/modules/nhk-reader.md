# NHK 精读 (NHK Reader)

## 触发词
NHK、新闻、ニュース、news、今日のニュース

## 流程

1. **读取记忆**：
   - `profile.json` → level、interests
   - `progress/vocab-mastery.jsonl` → 已知词汇（只标注真正的生词）
   - `progress/grammar-progress.json` → 已掌握语法（只解释新语法点）

2. **输入**：用户提供 NHK Easy News 的文本或 URL
   - 如果是 URL，提取文章内容
   - 如果用户没提供，建议去 https://www3.nhk.or.jp/news/easy/ 选一篇
   - 可以根据 profile.interests 推荐话题方向

3. **逐段精读**：

```
## 原文 + 翻译

### 第1段
原文：（保留原文）
翻译：（中文翻译）

**词汇**：
- 〈word〉（reading）— 意思 [N?]  ← 只标注不在 vocab-mastery mastered 列表中的词

**语法**：
- 「〜について」：关于...，新闻常用表达
- 「〜ということです」：据说...，转述信息

**文体特征**：
- 这里用了「〜ました」而非「〜た」→ 新闻体的礼貌形
```

4. **新闻日语特征总结**：
   - 常用句式（〜が明らかになりました、〜と発表しました 等）
   - 数字/日期读法
   - 被动句使用（新闻体大量使用）
   - 转述表达

5. **理解题**（3-5 题）：
   - 5W1H 事实确认
   - 因果关系推断
   - 数据/时间线梳理

6. **拓展**：
   - 从这篇新闻中提取可复用的表达 3-5 个
   - 建议用户用自己的话总结这篇新闻（练习输出）

## 会话结束时的记忆更新

- 标注的新词 → 追加到 `vocab-mastery.jsonl`（status=new）
- 新出现的语法点 → 追加到 grammar-progress（status=in_progress）
- 可复用表达 → 追加到 vocab-mastery（作为短语级词汇）
- 理解题答题情况 → 更新 sessions 摘要
- 如果是第一次读 NHK → milestones.md 记录："📖 第一次精读 NHK 新闻"
