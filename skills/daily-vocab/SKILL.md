---
name: daily-vocab
description: Use this skill when the user wants to learn new Japanese vocabulary, generate daily word lists, create Anki cards, or practice vocabulary at their JLPT level. Triggers on requests like "今日の単語", "new words", "vocabulary practice", "Anki cards".
---

# Daily Vocabulary Practice (毎日の語彙練習)

Generate a tailored daily vocabulary set with context, mnemonics, and Anki-ready output.

## Ask First

1. What is your current JLPT level? (N5/N4/N3/N2/N1)
   - Default: N4

2. How many new words today? (5/10/15/20)
   - Default: 10

3. Any topic preference? (e.g., daily life, business, travel, technology, food, anime)
   - Default: mixed

4. Where should I save the output?
   - Default: `~/japanese-learning/vocab/`

Use defaults if the user does not answer.

## Word Selection Criteria

- Match JLPT level ±0.5 (slightly above for challenge)
- Prioritize high-frequency words within the level
- Include a mix of: verbs (3), nouns (4), adjectives (2), adverbs/expressions (1) for a set of 10
- Avoid duplicates with recent sessions (check save folder for past reports)

## Output Format for Each Word

For each vocabulary item, provide:

```markdown
### N. 漢字 (かな) [pitch accent pattern]

- **Meaning:** English meaning
- **Part of speech:** noun / verb (group 1/2/3) / i-adj / na-adj / adverb
- **JLPT Level:** N4
- **Example sentence:**
  - 日本語: (natural sentence using the word)
  - Reading: (full furigana version)
  - English: (translation)
- **Common collocations:** word + particle patterns, set phrases
- **Mnemonic:** (visual/story-based memory aid)
- **Related words:** (2-3 related vocabulary)
```

## Anki Card Generation

At the end, generate Anki-importable cards in this format:

```
Front<tab>Back<tab>Tags
漢字（かな）<tab>Meaning: ...<br>Example: ...<br>Mnemonic: ...<tab>japanese::vocab::N4::topic
```

## Spaced Repetition Tracking

If previous vocab files exist in the save folder:
1. Check which words appeared before
2. Mark words due for review (Day 1, 3, 7, 14, 30 schedule)
3. Include 2-3 review words alongside new words

## Session Flow

1. Load config / ask questions
2. Check previous sessions for deduplication
3. Generate word set following criteria
4. Present words in the format above
5. Generate Anki cards
6. Create a mini-quiz (matching, fill-in-blank, or sentence completion)
7. Save the session report

## Save Rule

Save to: `<save-folder>/daily-vocab-YYYY-MM-DD.md`

## Quality Bar

- Every example sentence must sound natural to a native speaker
- Mnemonics should be vivid and memorable, not generic
- Pitch accent patterns must be accurate
- Collocations should reflect actual Japanese usage patterns
