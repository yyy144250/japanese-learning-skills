---
name: weekly-review
description: Use this skill when the user wants to review their Japanese study progress for the week, identify weak points, and plan next week's study. Triggers on "weekly review", "週間レビュー", "how did I do this week", "study plan", "what should I focus on".
---

# Weekly Review (週間レビュー)

Analyze the week's Japanese study progress, identify patterns, and generate a focused study plan.

## Ask First

1. Where are your study materials saved?
   - Default: `~/japanese-learning/`
2. What study activities did you do this week? (or "check my files")
3. Any specific concerns or goals for next week?
4. Save location?
   - Default: `~/japanese-learning/reviews/`

## Data Sources

Scan the study folder for this week's files:
- `daily-vocab-*.md` — vocabulary sessions
- `grammar-*.md` — grammar practice
- `journal-*.md` — writing practice
- `reading-*.md` — reading sessions
- `roleplay-*.md` — conversation practice
- `shadowing-*.md` — pronunciation work
- `kanji-*.md` — kanji study
- `context-vocab-*.md` — contextual learning

## Review Report Structure

```markdown
# Weekly Review: [Date range]

## Activity Summary

| Day | Activities | Time (est.) | New items |
|-----|-----------|-------------|-----------|
| Mon | vocab, grammar | ~30min | 10 words, 1 pattern |
| Tue | journal, reading | ~25min | 5 expressions |
| ... | ... | ... | ... |
| **Total** | **N sessions** | **~Xh Ymin** | **N words, N patterns** |

## Achievements This Week 🎉

- Learned N new vocabulary words
- Practiced N grammar patterns
- Wrote N journal entries
- [Other specific accomplishments]

## Vocabulary Progress

- New words this week: N
- Cumulative vocabulary (estimated): N
- Most common topics: [...]
- Words due for review (spaced repetition): [list]

## Grammar Progress

- Patterns practiced: [list]
- Confidence level per pattern:
  - ✅ Solid: [patterns you used correctly multiple times]
  - ⚠️ Shaky: [patterns with errors]
  - 🆕 New: [just introduced, needs more practice]

## Error Patterns (弱点分析)

### Recurring mistakes:
1. [Error type] — appeared N times
   - Example: [...]
   - Root cause: [...]
   - Fix: [...]

2. ...

### Improving areas:
1. [Something that was wrong before but improved]

## Consistency Score

- Study days: N/7
- Streak: N days
- Longest gap: N days
- Trend: [Improving / Steady / Declining]

## Next Week Plan

### Priority 1: [Weakness to address]
- Action: [specific exercises]
- Target: [measurable outcome]

### Priority 2: [Skill to develop]
- Action: [...]
- Target: [...]

### Priority 3: [New territory]
- Action: [...]
- Target: [...]

### Daily minimum:
- [Smallest useful daily activity — e.g., "review 5 flashcards + write 1 sentence"]

## Long-term Progress

- Estimated weeks to next JLPT level: [based on current pace]
- Suggestion: [any course corrections needed]
```

## Insight Generation

Look for:
- **Consistency patterns:** Which days are productive? Which get skipped?
- **Skill balance:** Is reading/writing/listening/speaking balanced?
- **Difficulty curve:** Is the content getting harder over time?
- **Engagement patterns:** What topics/activities does the user enjoy most?

## Motivational Element

Always include:
- One specific "you did great this" observation
- One "this is improving" observation
- Frame next week's plan as achievable, not overwhelming

## Save Rule

Save to: `<save-folder>/review-YYYY-MM-DD.md`
