---
name: pitch-accent-trainer
description: Use this skill when the user wants to practice Japanese pitch accent patterns, understand accent rules, or work with minimal pairs. Triggers on "pitch accent", "アクセント", "pronunciation sounds off", "intonation practice".
---

# Pitch Accent Trainer (アクセント練習)

Practice Japanese pitch accent with pattern rules, minimal pairs, and self-check exercises.

## Ask First

1. Current level of pitch accent awareness? (beginner / intermediate / advanced)
   - Default: beginner
2. Focus area? (basic patterns / specific word types / minimal pairs / sentence intonation)
   - Default: basic patterns
3. JLPT vocabulary level?
   - Default: N4
4. Save location?
   - Default: `~/japanese-learning/pitch-accent/`

## Lesson Structure

### For Beginners

```markdown
## What is Pitch Accent?

Japanese is NOT a "flat" language. Each word has a specific pitch pattern.
Unlike Chinese tones (which change within syllables), Japanese pitch is about
HIGH (H) and LOW (L) in a sequence.

## The 4 Pattern Types

### 1. 平板型 (Flat/Heiban) — No drop
Pattern: L-H-H-H...
Example: さくら (L-H-H) — cherry blossom
The pitch stays high and never drops.

### 2. 頭高型 (Atamadaka) — Drop after first mora
Pattern: H-L-L-L...
Example: あめ (H-L) — rain
The first mora is high, everything after drops.

### 3. 中高型 (Nakadaka) — Drop in the middle
Pattern: L-H-H-L...
Example: おとこ (L-H-L) — man
Rises then drops somewhere in the middle.

### 4. 尾高型 (Odaka) — Drop after the last mora (heard with particle)
Pattern: L-H-H + L(particle)
Example: おとうと (L-H-H-H) + が(L) — younger brother
Sounds flat in isolation, drops on the following particle.
```

### Minimal Pairs Exercise

```markdown
## Minimal Pairs (同音異義語)

These words have the same sounds but different pitch = different meaning:

| Word | Pattern A | Meaning A | Pattern B | Meaning B |
|------|-----------|-----------|-----------|-----------|
| はし | H-L (箸) | chopsticks | L-H (橋) | bridge |
| あめ | H-L (雨) | rain | L-H (飴) | candy |
| かき | H-L (牡蠣) | oyster | L-H (柿) | persimmon |

### Practice:
For each pair, say both versions out loud. Feel the difference in your mouth.
```

### Rules by Word Type

```markdown
## Common Patterns by Category

### Verb (ます form) — usually 平板
- たべます (L-H-H-H)
- のみます (L-H-H-H)
- Exception: します (H-L-L)

### い-Adjective — check dictionary, but common patterns:
- 3-mora i-adj: often 中高 (L-H-L): あかい (L-H-L)
- 4-mora i-adj: varies

### Foreign Loanwords (カタカナ) — accent on 3rd mora from end
- コンピューター (L-H-H-H-H-L-L)
- テレビ (L-H-L)
- Rule: 3-mora-from-end rule covers ~70% of loanwords
```

## Exercise Types

1. **Pattern Identification:** Given a word with pitch marked, identify the type
2. **Production:** Given a word and its type, produce the correct pattern
3. **Minimal Pair Distinction:** Identify which meaning based on described pitch
4. **Sentence Intonation:** Mark the pitch of a full sentence
5. **Rule Application:** Apply rules to predict unknown words' patterns

## Notation System

Use consistent notation:
- H/L: high/low (for simple)
- ↗/↘: pitch changes (for detail)
- [accent number]: mora after which pitch drops (0 = heiban)
  - はし[1] = H-L (chopsticks)
  - はし[0] = L-H (bridge)

## Save Rule

Save to: `<save-folder>/pitch-accent-YYYY-MM-DD.md`
