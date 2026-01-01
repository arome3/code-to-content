# Content Cascade Reference

Transform one piece of content into multiple platform-optimized versions automatically.

---

## Concept

```
                    ┌─────────────────┐
                    │   Blog Post     │
                    │   (Source)      │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ Twitter Thread  │ │ LinkedIn Post   │ │ Newsletter      │
│ 8-12 tweets     │ │ 800-1300 chars  │ │ 150-300 words   │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

**One source → Multiple outputs → Consistent voice → Platform-optimized**

---

## Cascade Derivation Rules

### Twitter Thread (from Blog Post)

| Source Element | Twitter Adaptation |
|----------------|-------------------|
| Title/Hook | Tweet 1 (curiosity/result) |
| Problem section | Tweet 2-3 (context) |
| Key insights | Tweets 4-8 (one per tweet) |
| Code examples | Tweet with code block (4-6 lines max) |
| Results/metrics | Tweet 9-10 (proof) |
| Conclusion | Tweet 11-12 (takeaway + CTA) |

**Extraction priority:**
1. Most surprising statistic or result
2. Core problem that resonates
3. Key insight that's tweetable
4. Actionable takeaway

### LinkedIn Post (from Blog Post)

| Source Element | LinkedIn Adaptation |
|----------------|---------------------|
| Title | Hook (first 2 lines) |
| Personal angle | Story element |
| Key insights | 3 bullet takeaways |
| Conclusion | Engagement question |

**Tone shift:**
- More professional than Twitter
- Focus on career/business value
- Personal journey angle
- Invite discussion

### Newsletter Section (from Blog Post)

| Source Element | Newsletter Adaptation |
|----------------|----------------------|
| Title | Section header |
| Core insight | Lead paragraph |
| Unique angle | Exclusive perspective |
| Full content | Link to blog |

**Value-add requirement:**
- Must offer something not in public post
- Behind-the-scenes perspective
- Subscriber-exclusive insight
- Early access framing

---

## Platform Constraints

### Twitter

| Constraint | Limit |
|------------|-------|
| Tweet length | 280 characters |
| Thread length | 8-12 tweets optimal |
| Code blocks | 4-6 lines visible |
| Images | 1-4 per tweet |

**Formatting:**
- No "Thread:" or "1/" prefixes
- Each tweet standalone value
- Line breaks for readability
- Minimal emoji (0-2 per tweet)

### LinkedIn

| Constraint | Limit |
|------------|-------|
| Post length | 800-1300 characters optimal |
| Before fold | First 2 lines visible |
| Paragraphs | 1-2 sentences each |
| Hashtags | 3-5 at end |

**Formatting:**
- Short paragraphs with whitespace
- Bullet points for takeaways
- No links in body (comments)
- Professional but personal tone

### Newsletter

| Constraint | Limit |
|------------|-------|
| Section length | 150-300 words |
| Subject preview | 50 characters |
| CTA | One clear action |
| Links | 1-2 per section |

**Formatting:**
- Conversational opener
- Exclusive angle emphasized
- Clear link to full content
- Subscriber appreciation

---

## Voice Consistency Matrix

Maintain source voice across platforms:

| Source Voice | Twitter | LinkedIn | Newsletter |
|--------------|---------|----------|------------|
| Precise (Rust) | Technical, exact | Authority | Deep-dive |
| Pragmatic (JS) | Tips, hacks | Practical wins | Behind-scenes |
| Accessible (Python) | Friendly, clear | Approachable | Beginner-friendly |
| Direct (Go) | Punchy, minimal | Concise | Efficient |

---

## Posting Schedule Template

| Day | Platform | Content Type | Reason |
|-----|----------|--------------|--------|
| 0 | Twitter | Thread | Immediate, real-time |
| 1-2 | LinkedIn | Post | Refined, professional |
| 3-5 | Dev.to/Hashnode | Cross-post | Wider reach |
| 7+ | Newsletter | Section | Exclusive angle |

**Timing rationale:**
- Twitter first: Captures immediacy
- LinkedIn delayed: Time to refine, different audience awake
- Newsletter last: Adds exclusive value for subscribers

---

## Quality Checklist

For each derived piece:

```
VOICE CONSISTENCY:
[ ] Tone matches source
[ ] Personality consistent
[ ] Technical depth appropriate

PLATFORM FIT:
[ ] Length within limits
[ ] Format follows conventions
[ ] CTA appropriate for platform

CONTENT INTEGRITY:
[ ] Key insight preserved
[ ] No contradictions with source
[ ] Evidence/metrics accurate

VALUE DELIVERY:
[ ] Standalone value present
[ ] Not just a teaser
[ ] Actionable for reader
```

---

## Anti-Patterns

### Don't Do This

**Lazy repurposing:**
```
❌ "New blog post! [link]"
❌ First paragraph copy-pasted
❌ Same content, no adaptation
```

**Platform mismatch:**
```
❌ 2000-word LinkedIn post
❌ Thread with only 3 tweets
❌ Newsletter with no exclusive value
```

**Voice drift:**
```
❌ Formal blog → Casual tweet
❌ Technical post → Dumbed-down LinkedIn
❌ Different personality across platforms
```

### Do This Instead

**Thoughtful adaptation:**
```
✅ Extract core insight
✅ Adapt for platform norms
✅ Add platform-specific value
```

**Platform-native content:**
```
✅ Twitter: Curiosity + thread format
✅ LinkedIn: Professional + personal story
✅ Newsletter: Exclusive + subscriber value
```

**Voice consistency:**
```
✅ Same personality, different format
✅ Technical depth adjusted, not removed
✅ Recognizable as same author
```

---

## Cascade vs. Original Creation

| Approach | Best For |
|----------|----------|
| Cascade | Repurposing finished content quickly |
| Original | Platform-first content creation |

**Use Cascade when:**
- You have a finished blog post/tutorial
- You want to maximize reach
- Time is limited
- Voice is already established

**Use Original when:**
- Platform is primary (Twitter-first thread)
- Topic is platform-specific
- Need full 5-phase analysis
- No source content exists
