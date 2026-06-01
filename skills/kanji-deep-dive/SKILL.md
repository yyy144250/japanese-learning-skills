---
name: kanji-deep-dive
description: Use this skill when the user wants to deeply study a specific kanji or set of kanji — radicals, readings, stroke order, etymology, compounds, and visual mnemonics. Triggers on "漢字を勉強", "kanji study", "explain this kanji", "radical breakdown".
---

# Kanji Deep Dive (漢字深掘り)

Provide comprehensive analysis of kanji for deep understanding and long-term retention.

## Ask First

1. Which kanji do you want to study? (single kanji, a word, or "give me today's kanji")
   - If "today's kanji": select one appropriate for user's level
2. Current JLPT level?
   - Default: N4
3. Save location?
   - Default: `~/japanese-learning/kanji/`

## Analysis Structure

For each kanji, provide:

```markdown
# 漢 — [meaning]

## Basic Info
- **Strokes:** N strokes
- **JLPT:** N3
- **Frequency rank:** #XXX (out of 2136 jōyō kanji)
- **Grade:** Taught in grade X

## Radical Breakdown
- **Main radical:** 部首 (meaning) — position: left/right/top/bottom/enclosure
- **Components:**
  - Top: 〇 (meaning)
  - Bottom: 〇 (meaning)
- **Visual decomposition:** Draw ASCII art or describe spatial layout

## Readings
| Type | Reading | Common usage |
|------|---------|-------------|
| 音読み (on) | カン | 漢字、漢方 |
| 訓読み (kun) | — | — |

## Etymology & Mnemonic
- **Origin:** (oracle bone → bronze → seal script evolution, if notable)
- **Story mnemonic:** (vivid visual story connecting components to meaning)
- **Association:** (connect to something the learner already knows)

## Key Compounds (熟語)
| Compound | Reading | Meaning | JLPT |
|----------|---------|---------|------|
| 漢字 | かんじ | kanji | N5 |
| 漢方 | かんぽう | Chinese medicine | N2 |

(List 8-12 compounds, sorted by frequency/JLPT level)

## Common Confusions
- **Looks similar to:** 〇 (differences highlighted)
- **Sounds similar to:** 〇 (different meaning)

## Practice
1. Write the kanji 5 times, paying attention to stroke order
2. Cover the readings and recall from memory
3. Make one original sentence using a compound
```

## Multi-Kanji Mode

When the user provides a word (e.g., 勉強):
- Analyze each kanji separately
- Then explain how they combine semantically
- Show other words sharing each kanji

## Anki Output

Generate cards for:
1. Kanji → Readings + Meaning
2. Compound → Reading + Meaning (one card per key compound)

## Save Rule

Save to: `<save-folder>/kanji-YYYY-MM-DD-[kanji].md`
