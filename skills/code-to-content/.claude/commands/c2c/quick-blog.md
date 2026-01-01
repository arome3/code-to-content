# /c2c:quick-blog

Generate a technical blog post draft quickly.

**Usage:** `/c2c:quick-blog [topic]`

**When to use:** Fast first drafts when you have a clear topic. Skip for posts requiring deep codebase analysis or complex evidence gathering.

---

## Mode: QUICK (Reduced Verification)

**Skipped phases:** 1 (codebase analysis), 4 (SEO/optimization)

**Still required:** Audience selection (Phase 2) — you must specify who this is for.

**Defaults applied:**
- Voice: Clear, accessible technical writing
- Structure: Problem → Journey → Solution
- Evidence: Based on user-provided context (no automated analysis)

---

## Phase 2: Audience (Required)

Before generating, confirm the audience:

| Audience | Writing Style |
|----------|---------------|
| Beginner | Define all jargon, step-by-step, encouraging tone |
| Intermediate | Standard jargon OK, focus on the "why" |
| Expert | Dense, jump to insights, assume deep knowledge |

Ask: "Who is this post for?" if not specified.

---

## Content Generation

Generate a blog post (800-1500 words) with this structure:

### 1. Hook (2-3 sentences)
- Start with a result, problem, or surprising insight
- NO "In this article, I will..."
- Create immediate interest

### 2. The Problem (1 paragraph)
- Pain point your readers experience
- Why existing solutions fall short

### 3. The Journey (2-3 paragraphs)
- What you tried first
- Why it didn't work
- The turning point

### 4. The Solution (2-4 paragraphs)
- Your approach with code examples
- Key implementation details
- Why this works

### 5. Results (1 paragraph)
- Specific outcomes (metrics if available)
- Before → After comparison

### 6. Conclusion (2-3 sentences)
- Key takeaway
- What to try next

---

## Lite Verification

Before delivery, verify:
- [ ] Hook is engaging (no preamble)
- [ ] Structure follows problem → journey → solution
- [ ] Code examples are relevant and explained
- [ ] Conclusion has clear takeaway
- [ ] Appropriate for declared audience

---

## Output Format

Provide the complete blog post in markdown format, ready for publication.

Include at the end:
```
---
Word count: [count]
Audience: [selected audience]
Suggested title alternatives: [2-3 options]
```
