# 记忆系统 (Memory System)

## 概述

本模块定义学习者的持久化记忆机制。目标：让 AI 在每次新对话中都能「接上上次的进度」，知道你现在在哪、要去哪、哪里薄弱。

**核心原则：只记状态变化，不记过程。**

---

## 存储结构

```
~/japanese-learning/
├── profile.json                 ← 学习者状态快照（核心！每次必读）
├── progress/
│   ├── vocab-mastery.jsonl      ← 词汇掌握度记录（增量追加）
│   ├── grammar-progress.json    ← 语法覆盖 + 掌握状态
│   ├── error-archive.json       ← 活跃错误模式档案
│   └── milestones.md            ← 成长里程碑（人类可读）
├── vocab/                       ← 每日词汇输出（已有）
├── journal/                     ← 日记输出（已有）
└── sessions/
    └── YYYY-MM.json             ← 月度会话摘要（自动压缩）
```

---

## profile.json — 学习者状态快照

这是记忆系统的**核心文件**。每次会话开始时读取，结束时更新。

```json
{
  "version": "1.0",
  "lastUpdated": "2026-06-01T14:30:00+08:00",

  "learner": {
    "level": {
      "current": "N4",
      "target": "N3",
      "startedAt": "2026-05-01",
      "estimatedReach": "2026-09-01"
    },
    "interests": ["anime", "technology", "daily-life"],
    "preferences": {
      "dailyVocabCount": 10,
      "preferAnki": true,
      "showFurigana": "auto",
      "encouragementStyle": "casual"
    }
  },

  "vocab": {
    "totalLearned": 420,
    "estimatedMastered": 310,
    "byLevel": { "N5": 180, "N4": 200, "N3": 40 },
    "recentTopics": ["food", "technology", "weather"],
    "struggling": ["紛らわしい", "曖昧", "一応", "却って", "寧ろ"],
    "recentlyMastered": ["食べ物", "天気", "便利"]
  },

  "grammar": {
    "totalCovered": 35,
    "byLevel": { "N5": 15, "N4": 18, "N3": 2 },
    "mastered": ["て形", "ない形", "た形", "〜ている", "〜たい", "〜てもいい"],
    "inProgress": ["受身形", "使役形", "〜ようにする"],
    "struggling": ["は/が使い分け", "自他動詞"]
  },

  "errors": {
    "active": [
      { "pattern": "は/が混淆", "count": 8, "firstSeen": "2026-05-10", "lastSeen": "2026-05-30", "severity": "persistent" },
      { "pattern": "て形变形（不规则）", "count": 5, "firstSeen": "2026-05-15", "lastSeen": "2026-05-28", "severity": "declining" }
    ],
    "resolved": [
      { "pattern": "助数词混用", "resolvedAt": "2026-05-25", "sessions": 4 }
    ]
  },

  "streak": {
    "current": 5,
    "best": 12,
    "totalDays": 45,
    "lastActiveDate": "2026-06-01"
  },

  "monthly": {
    "2026-05": {
      "activeDays": 22,
      "newVocab": 180,
      "grammarPoints": 8,
      "journalEntries": 12,
      "sessionsCount": 35
    }
  }
}
```

### 大小控制规则

| 字段 | 上限 | 满时策略 |
|------|------|---------|
| `vocab.struggling` | 最多 20 个词 | 替换掉最老的已改善项 |
| `vocab.recentlyMastered` | 最多 10 个 | FIFO，只保留最近掌握的 |
| `grammar.mastered` | 无限（~300 个语法点封顶） | 不清理 |
| `grammar.inProgress` | 最多 10 个 | 掌握后移到 mastered |
| `errors.active` | 最多 15 个 | 低频 + 已 30 天未出现的移到 resolved |
| `errors.resolved` | 最多 30 个 | FIFO 删最老的 |
| `monthly` | 最多 6 个月 | 删除 6 个月前的记录 |

---

## vocab-mastery.jsonl — 词汇掌握度

每行一个 JSON 对象，只在以下时刻追加：
- 新学一个词（首次出现）
- 复习一个词且结果与上次不同（从「记不住」变「记住了」，或反过来）

```jsonl
{"word":"紛らわしい","reading":"まぎらわしい","level":"N2","firstSeen":"2026-05-15","status":"struggling","quizResults":[0,0,1,0],"lastReview":"2026-05-30"}
{"word":"便利","reading":"べんり","level":"N4","firstSeen":"2026-05-01","status":"mastered","quizResults":[1,1,1,1],"lastReview":"2026-05-28"}
```

### 状态定义

| status | 含义 | 判定规则 |
|--------|------|---------|
| `new` | 刚学过，未复习 | 只出现过 1 次 |
| `learning` | 学习中 | 复习过但正确率 < 75% |
| `struggling` | 困难词 | 复习 3 次+ 且正确率 < 50% |
| `mastered` | 已掌握 | 连续 3 次复习正确 |

### 大小控制

- 文件超过 500 行时，运行压缩：
  - `mastered` 且 `lastReview` > 60 天前的词 → 删除（只保留 profile 里的统计数）
  - `struggling` 永远保留（直到状态变化）

---

## grammar-progress.json — 语法覆盖

```json
{
  "points": [
    {
      "name": "〜ている",
      "level": "N5",
      "firstStudied": "2026-05-03",
      "status": "mastered",
      "practiceCount": 8,
      "lastPractice": "2026-05-28",
      "notes": "进行/状态/结果残存三种用法都理解了"
    },
    {
      "name": "受身形",
      "level": "N4",
      "firstStudied": "2026-05-20",
      "status": "in_progress",
      "practiceCount": 3,
      "lastPractice": "2026-05-29",
      "notes": "直接受身理解，间接受身还在混"
    }
  ]
}
```

---

## error-archive.json — 错误模式档案

```json
{
  "patterns": [
    {
      "id": "err-001",
      "category": "particle",
      "description": "は/が使い分け：主题标记与主语标记混淆",
      "examples": [
        "❌ 猫は走っています（应该说：猫が走っています）",
        "❌ 私が学生です（应该说：私は学生です）"
      ],
      "rule": "新信息用が、已知话题用は；存在句/第一次提到用が",
      "occurrences": 8,
      "firstSeen": "2026-05-10",
      "lastSeen": "2026-05-30",
      "status": "active",
      "interventions": ["2026-05-15: grammar-drill 专项", "2026-05-22: 再次专项"],
      "trend": "stable"
    }
  ]
}
```

### 错误的生命周期

```
出现 → active → (干预后) → declining → (30天未复现) → resolved → (60天后) → 删除
```

---

## milestones.md — 成长里程碑

人类可读的成就记录。**只记值得纪念的节点**：

```markdown
# 🎌 学习里程碑

## 2026-06

- [2026-06-01] 🔥 连续学习 5 天
- [2026-06-01] 📚 累计词汇突破 400 个

## 2026-05

- [2026-05-25] 🎯 助数词错误模式已克服（经过 4 次专项训练）
- [2026-05-20] ✍️ 第一次独立写出 200 字日记
- [2026-05-15] 📖 第一次读完 NHK Easy 文章
- [2026-05-01] 🚀 开始 N4 → N3 学习旅程
```

### 触发里程碑的事件

| 事件 | 条件 |
|------|------|
| 连续学习 | streak 达到 7/14/30/60/100 天 |
| 词汇量 | 每突破 100 的整数关口 |
| 等级切换 | 从 N5→N4、N4→N3 等 |
| 错误克服 | 一个 active 错误变为 resolved |
| 首次成就 | 第一次完成某模块（第一篇日记、第一次角色扮演等） |
| 测试满分 | 周测 / 模块测试全对 |

---

## sessions/YYYY-MM.json — 月度会话摘要

每次学习会话结束时，追加一条摘要到当月文件：

```json
{
  "sessions": [
    {
      "date": "2026-06-01T14:30",
      "duration": "25min",
      "modules": ["daily-vocab", "grammar-drill"],
      "outcomes": {
        "newVocab": 10,
        "vocabReviewed": 6,
        "grammarPoints": ["受身形"],
        "quizScore": "8/10",
        "errorsLogged": ["は/が"]
      }
    }
  ]
}
```

### 月末压缩

每月最后一天（或下月第一次运行时），将当月 sessions 压缩为 `profile.json` 的 `monthly` 统计，然后**删除超过 3 个月的 sessions 文件**。

---

## 会话协议

### 每次对话开始时（必须执行）

```
1. 读取 ~/japanese-learning/profile.json
2. 如果文件不存在 → 进入「初始化流程」（见下方）
3. 如果存在 → 更新 streak（对比 lastActiveDate 和今天）
4. 向用户打招呼时自然地提及：
   - 当前连续天数
   - 上次学的内容（从 sessions/ 读取最近一条）
   - 如果有 struggling 的词/语法，温和提醒
```

### 每次对话结束时（必须执行）

```
1. 更新 profile.json:
   - vocab 计数
   - grammar 列表
   - streak
   - lastUpdated
   - monthly 统计
2. 如果本次有新词 → 追加到 vocab-mastery.jsonl
3. 如果本次有练习/测验 → 根据结果更新掌握状态
4. 如果发现错误模式 → 更新 error-archive.json
5. 如果触发里程碑 → 追加到 milestones.md 并告诉用户 🎉
6. 追加会话摘要到 sessions/YYYY-MM.json
```

### 初始化流程（profile 不存在时）

```
1. 问用户：
   - 你的日语水平大概是？（完全零基础 / 学过一点 / N5 / N4 / N3+）
   - 目标是什么？（JLPT考试 / 日常交流 / 看动漫 / 工作需要）
   - 已经学过哪些内容？（大致范围，不需要精确）
   - 每天大概能学多久？
2. 根据回答初始化 profile.json
3. 创建目录结构
4. 写入第一个里程碑：🚀 开始学习旅程
```

---

## 什么不记录

以下信息**明确不写入任何文件**：

| 不记 | 原因 |
|------|------|
| AI 生成的例句原文 | 下次可以重新生成更好的 |
| 练习的完整题目和选项 | 过程细节，无跨会话价值 |
| 用户的日语原文（日记除外） | 日记有单独文件存 |
| 每道题的思考时间/犹豫记录 | 太细碎 |
| AI 的解释内容 | 可重新生成 |
| 临时的对话上下文 | 会话内有用，跨会话无意义 |
| 未完成的练习 | 只记完整结果 |

---

## 数据完整性

### 防止数据损坏

- 所有 JSON 写入使用「先写临时文件再 rename」策略
- 更新前先读取完整文件，merge 后整体写回
- 不做部分更新（不用 sed 改单行）

### 手动干预

用户可以随时说：
- "重置我的学习记录" → 确认后删除 profile.json，重新初始化
- "我其实已经学过 N4 了" → 直接修改 level 和相关统计
- "把 XX 标记为已掌握" → 手动覆盖状态

AI 应当信任用户的自我评估，不要质疑。
