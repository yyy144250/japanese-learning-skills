---
name: vocab-from-context
description: Use this skill when the user provides Japanese content (article, manga, lyrics, subtitle, etc.) and wants to extract and learn vocabulary from it. Triggers on "extract vocab from this", "what words are in this", "help me read this", pasting Japanese text.
---

# Vocabulary from Context (文脈から語彙)

Extract, analyze, and teach vocabulary from real Japanese content the user provides.

## Input

Accept any Japanese content:
- News articles
- Manga/anime dialogue
- Song lyrics
- Social media posts
- Book excerpts
- Subtitles
- Signs/menus/labels

## Ask First

1. Your JLPT level? (to filter what's worth studying)
   - Default: N4
2. What's the source? (helps with register/context)
3. Save location?
   - Default: `~/japanese-learning/context-vocab/`

## Process

1. **Parse the text** — identify all words/phrases
2. **Filter by level** — flag words above the user's current level as "new"
3. **Categorize:**
   - 🟢 Known (at or below user level) — skip unless user asks
   - 🟡 Stretch (one level above) — primary learning targets
   - 🔴 Advanced (two+ levels above) — mention but don't drill

4. **For each target word, provide:**

```markdown
### 漢字 (かな) — Meaning

- **In this context:** specific meaning/nuance as used here
- **General meaning:** broader definition
- **Register:** formal / casual / slang / literary / keigo
- **Grammar note:** (if relevant — e.g., てform of X, passive voice)
- **Original sentence:** 「...」
- **Simpler example:** (an easier sentence using same word)
- **Related:** similar words, synonyms/antonyms
```

5. **Full text breakdown** (optional, if user requests):
   - Sentence-by-sentence parsing
   - Grammar point identification
   - Cultural/contextual notes

## Special Handling

- **Slang/internet language:** Explain the standard form alongside
- **Keigo:** Note the plain-form equivalent
- **Onomatopoeia:** Explain the sound/feeling represented
- **Set phrases/idioms:** Explain literally + actual meaning

## Output Summary

```markdown
## Summary
- Source: [type of content]
- Total words identified: N
- New vocabulary (for your level): N words
- Grammar points encountered: [list]
- Difficulty assessment: [Easy/Moderate/Hard for N4]
```

## Anki Card Generation

Generate cards for all 🟡 Stretch words, with the original context as an example sentence.

## Save Rule

Save to: `<save-folder>/context-vocab-YYYY-MM-DD-[source].md`
