---
name: lang-journal
description: Use this skill when the user wants to practice writing Japanese through journaling — write about their day, get corrections with explanations, and build a personal expression library. Triggers on "日記", "journal", "write about my day", "Japanese writing practice", "correct my Japanese".
---

# Language Journal (日本語日記)

Guided Japanese journaling with corrections, explanations, and personal expression building.

## Ask First

1. What do you want to write about? (today / a specific topic / free choice)
   - Default: today
2. JLPT level?
   - Default: N4
3. Length goal? (3 sentences / 5 sentences / 1 paragraph / free)
   - Default: 5 sentences
4. Correction style? (gentle / thorough / native-level)
   - Gentle: only fix errors that break meaning
   - Thorough: fix all errors, suggest improvements
   - Native-level: rewrite to sound completely natural
   - Default: thorough
5. Save location?
   - Default: `~/japanese-learning/journal/`

## If User Needs Help Starting

Provide a prompt:

```markdown
## Today's Writing Prompt (今日のテーマ)

Choose one, or write about anything:
1. 今日何をしましたか？ (What did you do today?)
2. 最近面白いと思ったこと (Something interesting recently)
3. 週末の予定 (Weekend plans)
4. 好きな食べ物について (About your favorite food)
5. 最近見た映画/読んだ本 (A recent movie/book)

### Helpful structures for today:
- ～ました (past tense)
- ～と思います (I think...)
- ～たいです (I want to...)
- ～てから、～ (after doing X, Y)
```

## After User Writes

Provide feedback in this format:

```markdown
## Corrections (添削)

### Your text:
[User's original text, numbered by sentence]

### Corrected version:
[Full corrected text]

### Detailed feedback:

#### Sentence 1:
- **Original:** [...]
- **Corrected:** [...]
- **Changes:**
  - [specific change] — [why: grammar rule / natural expression / word choice]
- **Native alternative:** [how a native might express the same idea differently]

#### Sentence 2:
...

## Expression Library (表現ライブラリー)

New useful expressions from today's session:

| Expression | Meaning | Context | Example |
|-----------|---------|---------|---------|
| ～てしまった | (regret/completion) | When something happened that you didn't intend | 寝坊してしまった |

## Stats
- Sentences written: N
- Errors found: N
- New expressions learned: N
- Accuracy rate: N%

## Challenge for next time:
Try using [specific grammar point or expression] in your next entry.
```

## Progressive Tracking

If previous journal entries exist:
1. Note improvement over time
2. Flag recurring errors (user keeps making the same mistake)
3. Track vocabulary growth
4. Suggest new structures to try based on what's already mastered

## Encouragement Style

- Celebrate what the user got right first
- Frame corrections as learning opportunities, not failures
- Highlight when the user successfully uses something new
- Keep it motivating — journaling should feel good

## Save Rule

Save to: `<save-folder>/journal-YYYY-MM-DD.md`
