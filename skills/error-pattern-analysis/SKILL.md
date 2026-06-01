---
name: error-pattern-analysis
description: Use this skill when the user wants to analyze their common Japanese mistakes across sessions, identify systematic gaps, and create targeted remediation plans. Triggers on "analyze my mistakes", "error analysis", "間違い分析", "what do I keep getting wrong", "my weak points".
---

# Error Pattern Analysis (間違いパターン分析)

Analyze systematic errors across study sessions to identify root causes and create targeted practice.

## Ask First

1. Where are your study materials?
   - Default: `~/japanese-learning/`
2. Time range to analyze? (last week / last month / all time)
   - Default: last month
3. Any specific area of concern? (grammar / vocab / particles / keigo / etc.)
   - Default: all areas
4. Save location?
   - Default: `~/japanese-learning/analysis/`

## Data Collection

Scan all available study files for error indicators:
- Corrections in journal entries
- Mistakes in grammar drills
- Wrong answers in comprehension questions
- Corrections from roleplay sessions
- Any marked ❌ or "corrected" items

## Analysis Framework

### Error Categories

1. **Particle errors** (助詞の間違い)
   - Wrong particle choice (に vs で vs を)
   - Missing particles
   - Extra particles

2. **Verb form errors** (動詞の活用)
   - Wrong conjugation
   - Tense mistakes
   - Te-form errors
   - Passive/causative confusion

3. **Adjective errors** (形容詞)
   - い/な confusion
   - Wrong negative form
   - Past tense formation

4. **Word choice errors** (語彙選択)
   - Similar words confused
   - Register mismatch
   - False friends

5. **Word order errors** (語順)
   - Modifier placement
   - Clause ordering

6. **Keigo errors** (敬語)
   - Wrong politeness level
   - Humble/honorific confusion

7. **Expression errors** (表現)
   - Unnatural phrasing
   - Direct translation from native language

## Report Format

```markdown
# Error Pattern Analysis — [Date]

## Summary
Analyzed N files over [time range].
Total errors found: N
Systematic patterns identified: N

## Top Error Patterns (ranked by frequency)

### 1. [Pattern name] — N occurrences (X%)

**The pattern:**
You tend to [description of what you do wrong].

**Examples from your work:**
1. ❌ [your version] → ✅ [correct version]
2. ❌ [...] → ✅ [...]
3. ❌ [...] → ✅ [...]

**Root cause:**
[Why this keeps happening — e.g., interference from native language, misunderstood rule, similar patterns confused]

**The rule:**
[Clear, concise rule explanation]

**Practice drill:**
Fix these sentences (all have the same error type):
1. [sentence with error]
2. [sentence with error]
3. [sentence with error]

---

### 2. [Next pattern] — N occurrences
...

## Improvement Tracking

| Pattern | Last month | This month | Trend |
|---------|-----------|-----------|-------|
| Particle に/で | 12 errors | 7 errors | ↓ Improving |
| Te-form | 8 errors | 9 errors | → Stable |
| ... | ... | ... | ... |

## Targeted Practice Plan

### This week: Focus on [top pattern]
- Day 1-2: [specific exercises]
- Day 3-4: [specific exercises]
- Day 5-7: [integration practice]

### Quick reference card:
[A compact cheat sheet for the most problematic pattern]

## Positive Patterns (getting right consistently)
- [Things you rarely make mistakes on — keep it up!]
```

## Severity Scoring

Rank errors by impact:
- 🔴 **Meaning-breaking:** native speaker can't understand you
- 🟡 **Noticeable:** native speaker notices but understands
- 🟢 **Minor:** sounds slightly off but completely understandable

Prioritize fixing 🔴 errors first.

## Save Rule

Save to: `<save-folder>/error-analysis-YYYY-MM-DD.md`
