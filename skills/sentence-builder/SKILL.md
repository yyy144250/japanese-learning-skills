---
name: sentence-builder
description: Use this skill when the user wants to practice constructing Japanese sentences progressively, combining grammar points and vocabulary they know. Triggers on "sentence practice", "作文練習", "help me build sentences", "combine grammar points".
---

# Sentence Builder (文作り練習)

Progressive sentence construction that builds complexity from known grammar and vocabulary.

## Ask First

1. JLPT level?
   - Default: N4
2. Which grammar points have you recently studied? (or "use my level's grammar")
3. Topic for sentences? (daily life / travel / work / hobby / etc.)
   - Default: daily life
4. Save location?
   - Default: `~/japanese-learning/sentences/`

## Method: Building Blocks Approach

Start simple, add one element at a time:

```markdown
## Round 1: Core Sentence (主語 + 述語)

Build a basic sentence:
→ 私は食べます。(I eat.)

## Round 2: Add Object (目的語)

→ 私はりんごを食べます。(I eat an apple.)

## Round 3: Add Time (時間)

→ 私は毎朝りんごを食べます。(I eat an apple every morning.)

## Round 4: Add Reason (理由)

→ 健康にいいから、私は毎朝りんごを食べます。
  (Because it's healthy, I eat an apple every morning.)

## Round 5: Add Contrast/Connection

→ 健康にいいから毎朝りんごを食べますが、実は好きじゃないです。
  (Because it's healthy I eat an apple every morning, but actually I don't like them.)
```

## Exercise Types

### Type A: Guided Expansion
- Give a simple sentence → ask user to add elements one at a time
- Provide the element to add (e.g., "now add a time expression")

### Type B: Scramble & Order
- Provide words/phrases → user arranges into correct sentence
- Example: [毎日 / 公園で / 走って / 私は / います] → ?

### Type C: Translation Build
- Give English sentence → user constructs Japanese
- Start simple, increase complexity across 5-8 sentences

### Type D: Pattern Combination
- Give two grammar patterns → user creates a sentence using both
- Example: Use ～ている AND ～たい in one sentence

## Feedback Style

For each user attempt:
1. ✅ Correct? Or needs adjustment?
2. If wrong: explain specifically what needs to change (don't just give answer)
3. Natural? Would a native say it this way? Suggest more natural alternatives
4. Offer a "level up" variation using more advanced grammar

## Session Structure

1. Warm-up: 3 simple sentences (review)
2. Main practice: 8-10 sentences with progressive difficulty
3. Challenge: 2-3 sentences combining multiple new grammar points
4. Free production: 3 sentences on user's chosen topic

## Save Rule

Save to: `<save-folder>/sentences-YYYY-MM-DD.md`
