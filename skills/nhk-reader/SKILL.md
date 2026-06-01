---
name: nhk-reader
description: Use this skill when the user wants to study from a real Japanese news article (NHK Easy News or similar), with full vocabulary extraction, grammar analysis, and comprehension support. Triggers on "NHK", "news article", "ニュース", "read this article".
---

# NHK News Reader (ニュース読解)

Analyze real Japanese news articles for language learning — vocabulary, grammar, cultural context, and comprehension.

## Ask First

1. Provide the article (paste text, provide URL, or "find one for me")
   - If "find one for me": suggest searching NHK News Easy (https://www3.nhk.or.jp/news/easy/)
2. JLPT level?
   - Default: N4
3. Depth of analysis? (quick / standard / deep)
   - Default: standard
4. Save location?
   - Default: `~/japanese-learning/nhk/`

## Analysis Structure

```markdown
# Article: [Title]
Source: [URL/Source]
Date: [Publication date]
Topic: [Category — politics/economy/society/culture/science/sports]

## Summary (要約)
2-3 sentences in simple Japanese summarizing the main point.
English translation of summary.

## Full Text with Annotations

[Original text, broken into paragraphs]

### Paragraph 1
**Text:** [Japanese]
**Translation:** [English]
**Key grammar:** [patterns used]

### Paragraph 2
...

## Vocabulary Table

### New Words (above your level)
| Word | Reading | Meaning | Usage note |
|------|---------|---------|-----------|
| ... | ... | ... | (formal/news-specific/etc.) |

### News-Specific Vocabulary
| Word | Reading | Meaning | Frequency in news |
|------|---------|---------|-------------------|
| 政府 | せいふ | government | Very common |
| 発表 | はっぴょう | announcement | Very common |

## Grammar Breakdown

### Pattern 1: ～によると (according to ~)
- Usage in article: 「...」
- General meaning: Citing a source
- Level: N3
- More examples: ...

### Pattern 2: ...

## Cultural/Background Context

- What background knowledge does a Japanese reader bring to this?
- Any cultural references or institutions mentioned?
- How does this connect to broader Japanese society?

## Comprehension Check

1. 誰が何をしましたか？ (Who did what?)
2. いつ、どこで？ (When, where?)
3. なぜ？ (Why?)
4. 結果はどうなりましたか？ (What was the result?)
5. あなたはどう思いますか？ (What do you think?)

## Study Tasks

1. **Read aloud:** Read the full article at least twice
2. **Summarize:** Explain the article in 3 sentences (Japanese)
3. **Vocabulary:** Create flashcards for the 5 most useful new words
4. **Grammar:** Find one grammar point to study further
5. **Discuss:** Form an opinion about the topic in Japanese
```

## Difficulty Assessment

At the end, provide:
```
Difficulty for [level]: ★★★☆☆ (3/5)
- Vocabulary: ★★★ (several N2+ words)
- Grammar: ★★☆ (mostly N3 patterns)
- Content complexity: ★★★ (requires background knowledge)
Recommended: Good stretch for N4, comfortable for N3
```

## Save Rule

Save to: `<save-folder>/nhk-YYYY-MM-DD-[topic-slug].md`
