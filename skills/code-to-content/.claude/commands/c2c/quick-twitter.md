# /c2c:quick-twitter

Generate a Twitter/X thread quickly with sensible defaults.

**Usage:** `/c2c:quick-twitter [topic or insight]`

**When to use:** Fast threads from clear ideas. Skip for complex topics needing deep analysis.

---

## Mode: QUICK (Reduced Verification)

**Skipped phases:** 1 (analysis), 2 (audience), 4 (optimization)

**Defaults applied:**
- Audience: Intermediate developers
- Voice: Conversational, punchy, peer-to-peer
- Assumed knowledge: Basic programming concepts

---

## Content Generation

Generate a thread (6-10 tweets) with this structure:

1. **Hook** — Scroll-stopping first tweet
   - Start with a result, number, or surprising statement
   - Create curiosity gap
   - NO "Thread:" prefix

2. **Context** (1-2 tweets) — Set up the situation

3. **Core insight** (2-3 tweets) — The main lesson with evidence

4. **Takeaway** — What readers should do next

5. **CTA** — Engagement question or soft ask

### Constraints
- Each tweet MUST work standalone (no "as I mentioned above")
- Max 280 characters per tweet
- Include code blocks only if essential
- Suggest 1-2 image placements

---

## Lite Verification

Before delivery, verify:
- [ ] Hook creates curiosity (no preamble)
- [ ] Each tweet < 280 characters
- [ ] CTA present in final tweet
- [ ] No "Thread:" or "1/" prefixes

---

## Output Format

Provide the thread in copy-ready format:

```
---COPY BELOW FOR TWITTER---

[Tweet 1]
[Hook text here]

[Tweet 2]
[Content here]

...

[Final Tweet]
[CTA here]

---END COPY---

Character counts: [list per tweet]
Suggested images: [where to add visuals]
```
