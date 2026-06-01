---
name: shadowing-prep
description: Use this skill when the user wants to prepare shadowing materials, practice pronunciation, or work with audio transcripts for listening/speaking practice. Triggers on "shadowing", "シャドーイング", "pronunciation practice", "prepare audio for practice".
---

# Shadowing Preparation (シャドーイング準備)

Prepare optimized shadowing materials from Japanese audio/text content with pitch accent marking, chunking, and practice schedules.

## Ask First

1. What content do you want to shadow? (provide transcript, URL, or ask for a recommendation)
2. JLPT level?
   - Default: N4
3. What's your goal? (general fluency / pitch accent / speed / specific sounds)
   - Default: general fluency
4. Practice session length? (5min / 10min / 15min)
   - Default: 10min
5. Save location?
   - Default: `~/japanese-learning/shadowing/`

## Material Preparation

### Step 1: Text Analysis

```markdown
## Source Information
- Content: [title/description]
- Length: ~N seconds / N sentences
- Difficulty: [Easy/Medium/Hard for level]
- Speech speed: [Slow/Normal/Fast] (~N mora per second)
- Register: [casual/polite/formal/news/anime]
```

### Step 2: Chunked Breakdown

Break the text into shadowing chunks (breath groups):

```markdown
### Chunk 1
**Text:** 今日はいい天気ですね。
**Reading:** きょう↗は↘ いい↗てんき↘ですね↘。
**Pitch:** [accent marks using ↗↘ notation]
**Speed note:** Normal pace, slight pause after は
**Key sounds:** Long vowel in きょう, nasal ん in てんき

### Chunk 2
...
```

### Step 3: Difficulty Notes

For each chunk, flag:
- 🔴 Hard sounds (つ/ず, りゃ/りゅ/りょ, long vowels, double consonants)
- 🟡 Pitch accent traps (common words with unexpected patterns)
- 🟢 Natural pause points

### Step 4: Practice Schedule

```markdown
## Practice Plan

### Day 1: Listen & Parse
- Listen 3x without text (get overall rhythm)
- Listen 2x with text (match sounds to characters)
- Mark unclear spots

### Day 2: Slow Shadow
- Shadow at 0.75x speed (if using app)
- Focus on Chunks 1-5
- Record yourself, compare

### Day 3: Normal Speed
- Shadow at 1.0x speed, Chunks 1-5
- Begin Chunks 6-10 at 0.75x

### Day 4-5: Full Speed + Polish
- Full passage at normal speed
- Focus on flagged difficult spots
- Record final version
```

## Pitch Accent Notation

Use this system:
- ↗ = pitch rises
- ↘ = pitch drops
- Underline = high pitch sustained
- Example: あ↗め↘ (rain, 頭高型) vs あめ↗ (candy, 平板型)

## Output Format

Full document includes:
1. Source info
2. Full text (clean, for reference)
3. Chunked breakdown with annotations
4. Vocabulary list (new words from the passage)
5. Grammar points used
6. Practice schedule
7. Self-evaluation checklist

## Quality Bar

- Pitch accent must be verified against standard Tokyo dialect
- Chunks should be natural breath groups, not arbitrary splits
- Practice schedule should be realistic for the stated session length
- Difficulty assessment should be honest — don't label N2 content as "easy for N4"

## Save Rule

Save to: `<save-folder>/shadowing-YYYY-MM-DD-[content-name].md`
