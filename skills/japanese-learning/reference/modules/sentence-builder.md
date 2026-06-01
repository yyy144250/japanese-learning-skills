# 造句阶梯 (Sentence Builder)

## 触发词
造句、练习写句子、sentence practice、用这个词造句

## 流程

1. **读取记忆**：
   - `profile.json` → level、grammar.mastered/inProgress
   - `progress/vocab-mastery.jsonl` → 最近学的词（优先用这些词做素材）
   - `progress/grammar-progress.json` → 最近练的语法（结合练习）
   - `progress/error-archive.json` → 活跃错误（批改时重点关注）

2. **给定素材**：2-3 个词汇 + 1 个语法点
   - 用户指定 → 直接使用
   - 用户不指定 → 从记忆中选取：
     - 词汇：优先从 `vocab-mastery` 中 status=learning 或 new 的词中选
     - 语法：优先从 `grammar.inProgress` 中选

3. **5 级难度递进**：

### L1：替换练习
- 给一个模板句，用户只需替换其中一个词
- 例：「私は＿＿が好きです」→ 填入任何名词

### L2：连接两个短句
- 给两个简单句，用指定的接续词连接
- 例：「雨が降る」+「出かけない」→ 用〜から连接

### L3：加入修饰成分
- 在基础句上添加时间/原因/条件/程度
- 例：在「本を読む」基础上加入时间和地点

### L4：表达观点
- 用指定语法表达个人看法/对比/推测
- 例：用〜と思う表达对某话题的看法

### L5：自由段落
- 用今天的全部素材写 3-5 句连贯的段落
- 可以是描述一个场景、讲一件事、发表一个观点

4. **批改规则**：
   - 先肯定正确的部分
   - 指出错误并解释
   - **特别关注 error-archive 中活跃错误模式是否出现**
   - 给出「自然版」改写（母语者会怎么说）
   - 如果有更高级的表达方式，额外提供「进阶版」

## 素材选择逻辑

如果用户不指定素材：
- 优先从今天的 daily-vocab 中抽取（如果同一会话刚做过）
- 其次从 vocab-mastery 中 status=learning/new 的词中选
- 语法从 grammar.inProgress 中选
- 如果都没有，从用户等级的常用词和核心语法中随机选取

## 会话结束时的记忆更新

- 用户在 L4/L5 中的造句表现 → 如果语法使用正确，该语法 practiceCount += 1
- 如果造句中反复出现某类错误 → 更新 error-archive
- 更新 sessions 摘要
