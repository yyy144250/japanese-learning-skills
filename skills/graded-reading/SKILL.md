---
name: graded-reading
description: Use this skill when the user wants reading practice at their level — generate passages on interesting topics with vocabulary support and comprehension questions. Triggers on "reading practice", "読解", "generate a reading passage", "something to read in Japanese".
---

# Graded Reading (レベル別読解)

Generate level-appropriate Japanese reading passages on topics the user enjoys.

## Ask First

1. JLPT level?
   - Default: N4
2. Topic preference? (technology, travel, food, culture, science, daily life, history, sports)
   - Default: daily life
3. Length? (short ~100 chars / medium ~250 chars / long ~500 chars)
   - Default: medium
4. Support level? (full furigana / kanji-only furigana / no furigana)
   - Default: kanji-only furigana (furigana only on words above user's level)
5. Save location?
   - Default: `~/japanese-learning/reading/`

## Passage Guidelines by Level

| Level | Grammar | Vocabulary | Sentence length | Topics |
|-------|---------|-----------|-----------------|--------|
| N5 | です/ます, basic particles | ~800 words | 5-10 words | self, family, daily routine |
| N4 | て-form, たい, conditionals | ~1500 words | 8-15 words | hobbies, travel, shopping |
| N3 | passive, causative, よう/そう | ~3000 words | 10-20 words | news, opinions, explanations |
| N2 | formal expressions, complex clauses | ~6000 words | 12-25 words | abstracts, essays, editorials |
| N1 | literary, classical references | ~10000 words | any | academic, literary, specialized |

## Output Structure

```markdown
# [Title in Japanese]

## 本文 (Passage)

[Japanese text with appropriate furigana support]

---

## 語彙リスト (Vocabulary List)

| Word | Reading | Meaning | Note |
|------|---------|---------|------|
| 新出語 | しんしゅつご | new word | (context note) |

## 文法ポイント (Grammar Points)

1. Pattern found in line X:
   - Structure: ...
   - Meaning: ...
   - Connection to the passage: ...

## 内容確認 (Comprehension Questions)

1. [Factual question in Japanese]
   - a) ...
   - b) ...
   - c) ...

2. [Inference question in Japanese]

3. [Opinion/discussion question in Japanese]

## 答え (Answers)

1. b) — because [explanation]
2. ...

## 発展 (Extension)

- Try to summarize the passage in 2-3 sentences
- Write your opinion about the topic in Japanese
- Find one real article on the same topic (search suggestion: "[keyword] NHK Easy")
```

## Content Quality Rules

1. **Authenticity:** Passages should feel like natural Japanese, not translated English
2. **Cultural context:** Include culturally appropriate content and perspectives
3. **No artificial simplification:** Don't make sentences sound robotic — use natural connectors, sentence-final particles, and discourse markers
4. **Interest-driven:** The passage should be genuinely interesting, not a textbook exercise

## Progressive Reading Mode

If the user asks for multiple passages:
- Start with one at their level
- Next passage adds 1-2 new grammar points or slightly more complex vocabulary
- Third passage approaches the next level up

## Save Rule

Save to: `<save-folder>/reading-YYYY-MM-DD-[topic].md`
