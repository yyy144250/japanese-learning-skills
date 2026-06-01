# 错误模式分析 (Error Pattern Analysis)

## 触发词
错误分析、我总是搞错、error pattern、为什么总犯错、纠正、薄弱点

## 流程

1. **读取记忆数据**：
   - `progress/error-archive.json` → 所有活跃和已解决的错误模式
   - `progress/vocab-mastery.jsonl` → struggling 状态的词汇
   - `progress/grammar-progress.json` → struggling 状态的语法
   - `sessions/YYYY-MM.json` → 近期会话中的错误记录
   - `profile.json` → 了解用户等级和学习时长

2. **错误概览**：

```
## 🔍 错误模式分析报告

### 活跃错误模式（按严重程度排序）

#### 🔴 持续型（persistent）— 多次干预仍未解决
1. 【は/が混淆】
   - 首次出现：YYYY-MM-DD
   - 累计出现：X 次
   - 已尝试干预：X 次
   - 趋势：stable / worsening
   - 典型错误：「❌ ...」→「✅ ...」

#### 🟡 下降型（declining）— 正在改善
2. 【て形变形】
   - 首次出现：YYYY-MM-DD
   - 最近出现：YYYY-MM-DD
   - 趋势：declining（最近 2 周只出现 1 次）

#### 🟢 已解决（resolved）— 近期克服的
3. 【助数词混用】
   - 解决于：YYYY-MM-DD
   - 经过 X 次专项训练
```

3. **根因分析**（对每个 persistent 错误）：

```
### 深度分析：は/が混淆

**为什么难**：
- 中文没有对应区分，缺乏母语迁移
- 规则本身有例外和灰色地带
- 口语中界限更模糊

**你的具体弱点**：
（从历史错误例句中归纳）
- 存在句中误用は（正确应为が）
- 新信息提示时未切换到が
- 对比强调时は/が选择不稳定

**破解策略**：
1. （针对性的认知框架/口诀）
2. （3 组对比练习）
3. （日常输入时的关注点）
```

4. **专项突破练习**（可选，用户想练时提供）：
   - 针对最严重的 1 个错误模式
   - 10 道递进式专项题
   - 从最基础的规则确认开始，逐步到复杂场景
   - 每答对一题给出正反馈，错了给出规则提示而非直接答案

5. **干预记录**：
   - 在 error-archive.json 的 `interventions` 中记录本次分析日期
   - 更新趋势判断

## 错误分类体系

| 类别 | 示例 |
|------|------|
| particle（助词） | は/が、に/で、を/が |
| conjugation（活用） | て形、ない形、受身、使役 |
| vocab-confusion（词汇混淆） | 自他动词对、近义词 |
| register（语体） | 敬语/谦让/丁寧 混用 |
| word-order（语序） | 修饰语位置、倒装 |
| listening（听力） | 长音/促音/浊音混淆 |
| writing（书写） | 汉字记忆错误、送假名错误 |

## 会话结束时的记忆更新

本模块执行后：
- 更新 `error-archive.json` 中每个分析过的错误的 `interventions` 字段
- 如果专项练习全对 → 该错误 trend 更新为 `declining`
- 如果 declining 状态的错误 30 天内未再出现 → 移入 `resolved`
- 新解决的错误 → 写入 `milestones.md`
- profile.json → 更新 errors.active 列表
