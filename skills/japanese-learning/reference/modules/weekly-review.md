# 周回顾 (Weekly Review)

## 触发词
复习、回顾、周总结、weekly review、今周、这周学了什么

## 流程

1. **读取记忆数据**：
   - `profile.json` → 整体状态概览
   - `sessions/YYYY-MM.json` → 本周的所有会话摘要
   - `progress/vocab-mastery.jsonl` → 本周新增和状态变化的词
   - `progress/grammar-progress.json` → 本周练习的语法点
   - `progress/error-archive.json` → 错误变化趋势
   - `milestones.md` → 本周达成的里程碑

2. **生成周报**：

```
## 📊 本周学习报告（MM/DD ~ MM/DD）

### 🔥 学习节奏
- 活跃天数：X / 7 天
- 连续天数：当前 Y 天（最佳记录 Z 天）
- 总会话数：X 次

### 📚 词汇进展
- 新学：XX 个（本周）
- 累计：XXX 个（总计）
- 掌握率：XX%（mastered / total）
- 本周主题：生活(X)、科技(X)、...
- 需要加强的词：
  1. 「word」— 错了 X 次
  2. 「word」— 错了 X 次
  ...

### 📝 语法进展
- 练习过的语法点：
  1. 〜ている ✅ (mastered)
  2. 受身形 🔄 (in_progress, 练了 X 次)
  3. 使役形 ⚠️ (struggling)
- 新覆盖：X 个语法点
- 累计覆盖：XX / 该等级总数 XX

### ⚠️ 错误模式趋势
| 错误类型 | 趋势 | 本周出现 |
|---------|------|---------|
| は/が混淆 | →(stable) | 2 次 |
| て形变形 | ↓(declining) | 1 次 |
| 自他动词 | ↑(worsening) | 3 次 |

### ✨ 进步亮点
- （与上周数据对比的积极变化）
- （达成的里程碑）
- （从 struggling 变为 mastered 的词/语法）

### 📈 等级进度
当前：N4 → 目标：N3
词汇覆盖：XX%  语法覆盖：XX%  预计达成：YYYY-MM
```

3. **下周计划建议**：
   - 基于 struggling 词汇/语法推荐侧重模块
   - 基于 error-archive 中 worsening 的模式推荐专项
   - 如果 streak 要断了，给出轻量级「保 streak」建议（"哪怕只做 5 个词也行"）
   - 设定下周可量化目标

4. **综合小测**（10 题）：
   - 覆盖本周所有模块的内容
   - 题型混合（词汇/语法/翻译/填空）
   - **重点考察 struggling 项**
   - 记录得分，用于更新掌握状态

## 无数据时

如果 profile.json 不存在或 sessions/ 下本周无记录：
- 不要编造数据
- 告诉用户目前没有学习记录
- 建议从今天开始，先做一次 daily-vocab 或 lang-journal
- 引导执行初始化流程

## 会话结束时的记忆更新

本模块执行后：
- 综合小测的结果 → 更新对应词汇/语法的掌握状态
- 如果小测中发现新的错误模式 → 更新 error-archive
- 更新 sessions/YYYY-MM.json：记录本次为 weekly-review 模块
