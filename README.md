# Japanese Learning Skills (日本語学習スキル)

AI-powered skills for learning Japanese. Each skill is a structured prompt that guides an AI agent to help you practice specific aspects of Japanese — vocabulary, grammar, reading, listening, conversation, and more.

Inspired by [mattpocock/skills](https://github.com/mattpocock/skills).

## Prerequisites

- An AI agent that supports skills (e.g., Claude Code with `npx skills@latest`)
- Basic understanding of your current JLPT level (N5–N1)

## Skills Overview

### 📝 Vocabulary & Kanji

- **daily-vocab** — Generate daily vocabulary sets with context sentences, mnemonics, and spaced-repetition Anki cards based on your JLPT level and topics of interest.

- **kanji-deep-dive** — Deep analysis of kanji: stroke order, radicals, readings (音読み/訓読み), common compounds, etymology, and visual mnemonics.

- **vocab-from-context** — Extract and learn vocabulary from Japanese content you provide (articles, manga dialogue, song lyrics, etc.).

### 📖 Grammar & Sentence Patterns

- **grammar-drill** — Targeted grammar practice with pattern explanations, example sentences, common mistakes, and transformation exercises.

- **sentence-builder** — Progressive sentence construction exercises that build complexity from your known grammar points.

### 👂 Listening & Pronunciation

- **shadowing-prep** — Prepare shadowing materials: break down audio transcripts into chunks with pitch accent marks, parsing notes, and practice schedules.

- **pitch-accent-trainer** — Practice Japanese pitch accent patterns with minimal pairs, rules by word type, and self-check exercises.

### 📚 Reading Practice

- **graded-reading** — Generate level-appropriate reading passages on topics you enjoy, with inline vocabulary help and comprehension questions.

- **nhk-reader** — Analyze NHK News Easy articles (or similar): vocabulary extraction, grammar breakdown, cultural context, and comprehension quiz.

### 💬 Conversation & Output

- **roleplay-scenario** — Immersive Japanese conversation practice with situation-based roleplay (restaurant, job interview, doctor visit, etc.).

- **lang-journal** — Guided Japanese journaling: write about your day, get corrections with explanations, and build a personal expression library.

### 🔄 Review & Progress

- **weekly-review** — Analyze your week's Japanese study: progress tracking, weak points identification, and next-week study plan generation.

- **error-pattern-analysis** — Analyze your common mistakes across sessions to identify systematic gaps and create targeted practice plans.

## Skill Structure

Each skill follows a consistent format:

```
skills/
  └── skill-name/
      ├── SKILL.md          # Main skill prompt (frontmatter + instructions)
      ├── reference/        # Reference materials (grammar tables, vocab lists, etc.)
      └── scripts/          # Helper scripts (extraction, analysis, etc.)
```

### SKILL.md Format

```markdown
---
name: skill-name
description: When to use this skill and what it does.
---

# Skill Title

Instructions for the AI agent...
```

## Installation

```bash
# Install a single skill
npx skills@latest add /path/to/japanese-learning-skills --skill daily-vocab

# Or clone and use directly
git clone <this-repo>
```

## Study Methodology

These skills are designed around evidence-based language learning principles:

1. **Comprehensible Input (i+1)** — Content always slightly above your current level
2. **Spaced Repetition** — Anki card generation for long-term retention
3. **Active Recall** — Questions and exercises, not passive reading
4. **Context-Rich Learning** — Vocabulary and grammar always in meaningful sentences
5. **Output Practice** — Writing and speaking, not just recognition
6. **Error Analysis** — Track and address systematic mistakes

## Customization

Most skills ask your JLPT level and interests on first use. You can also set defaults in a `.japanese-learning-config.json` at your home directory:

```json
{
  "level": "N3",
  "interests": ["technology", "anime", "cooking"],
  "dailyGoal": 30,
  "ankiDeck": "Japanese::Daily",
  "preferKana": false
}
```
