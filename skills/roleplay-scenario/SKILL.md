---
name: roleplay-scenario
description: Use this skill when the user wants conversational Japanese practice through situational roleplay — ordering food, job interviews, doctor visits, shopping, etc. Triggers on "会話練習", "roleplay", "conversation practice", "let's practice talking", "restaurant scenario".
---

# Roleplay Scenario (ロールプレイ会話)

Immersive Japanese conversation practice through realistic situational roleplay.

## Ask First

1. Which scenario? Choose or suggest:
   - 🍽️ Restaurant (レストラン)
   - 🏪 Convenience store / shopping (買い物)
   - 🏥 Doctor / pharmacy (病院)
   - 💼 Job interview (面接)
   - 🏠 Real estate / apartment viewing (部屋探し)
   - 🚉 Asking directions / transportation (道を聞く)
   - 📞 Phone call (電話)
   - 🏢 Business meeting (会議)
   - 👋 Meeting someone new / self-introduction (自己紹介)
   - 🎉 Party / social event (パーティー)
   - Custom scenario: [user specifies]

2. JLPT level?
   - Default: N4

3. Formality level? (casual / polite / keigo)
   - Default: polite (ます/です)

4. Mode? (guided / free / challenge)
   - Guided: AI provides hints and options
   - Free: Pure conversation, corrections after
   - Challenge: AI introduces unexpected situations
   - Default: guided

## Setup

```markdown
## Scenario: [Name]

### Situation
[Clear description of where you are, who you're talking to, what you need to accomplish]

### Your role
You are: [description]
Your goal: [what you need to achieve in this conversation]

### My role
I am: [description — e.g., the waiter, the doctor, the interviewer]
I will: [how I'll behave — friendly, formal, speak fast, etc.]

### Useful phrases for this scenario
Before we start, here are key phrases you might need:
1. [phrase] — [meaning] — [when to use]
2. ...
(5-8 phrases relevant to the scenario)

### Cultural note
[Relevant cultural context — e.g., in Japan you say いただきます before eating]

---
Ready? Let's begin. I'll start the conversation.
```

## During Roleplay

### Guided Mode
- After each user turn, provide:
  - Natural response (continuing the conversation)
  - [Optional hint] if the user seems stuck
  - Brief correction only if there's a meaning-breaking error
- Save detailed corrections for the end

### Free Mode
- Respond naturally as the character
- No interruptions for corrections
- Full feedback after the conversation ends

### Challenge Mode
- Introduce unexpected elements:
  - "Sorry, we're out of that item"
  - "Could you explain that in more detail?"
  - Switch topics unexpectedly
  - Ask a question the user might not expect

## Post-Roleplay Feedback

```markdown
## Conversation Review

### Overall Performance
- Communication success: ✅/⚠️/❌ Did you achieve your goal?
- Naturalness: [rating] /5
- Grammar accuracy: [rating] /5
- Vocabulary range: [rating] /5
- Cultural appropriateness: [rating] /5

### Corrections
| What you said | Issue | Better version | Why |
|--------------|-------|---------------|-----|
| ... | grammar/vocab/register | ... | ... |

### Great Moments
- [Quote something the user said well and explain why]

### Key Takeaways
1. Learn these 3 phrases from this conversation: ...
2. Grammar point to review: ...
3. Next time, try: ...

### Want to try again?
- Same scenario, harder difficulty?
- Same scenario, different role?
- New scenario?
```

## Scenario Database (Reference)

Each scenario has:
- Common vocabulary list
- Expected conversation flow
- Cultural notes
- Typical complications
- Keigo requirements (if applicable)

## Save Rule

Save transcript to: `<save-folder>/roleplay-YYYY-MM-DD-[scenario].md`
