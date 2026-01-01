# /c2c:cascade

Automatically derive multiple content formats from a single source piece. Write once, publish everywhere.

**Usage:** `/c2c:cascade <source-file> [--formats twitter,linkedin,newsletter]`

---

## What Cascade Does

Takes your primary content (blog post, tutorial, etc.) and automatically generates platform-optimized versions:

```
Blog Post (source)
       │
       ├──► Twitter Thread (key insights, 8-12 tweets)
       ├──► LinkedIn Post (professional angle, 800-1300 chars)
       ├──► Newsletter Section (subscriber value-add)
       └──► README Section (if applicable)
```

**All derived content:**
- Maintains voice consistency with source
- Extracts the most compelling insights
- Adapts depth for each platform
- Respects platform-specific constraints

---

## Reference Loading

Load these references for cascade:
- `references/phase-gates.md` (always)
- `references/social-content.md`
- `references/formats.md` (sections for target formats)
- `references/checklists.md` (sections for target formats)

---

## Cascade Workflow

### Step 1: Analyze Source Content

Read the source file and extract:
- **Core insight** — The main takeaway
- **Key points** — 3-5 supporting ideas
- **Evidence** — Code snippets, metrics, examples
- **Voice profile** — Tone and style used
- **Audience level** — Beginner/intermediate/expert

```markdown
## Source Analysis

**Core Insight:** [One sentence summary]
**Key Points:**
1. [Point with evidence]
2. [Point with evidence]
3. [Point with evidence]

**Voice:** [detected voice profile]
**Audience:** [detected level]
```

### Step 2: User Confirmation Checkpoint

**PAUSE — Ask user to confirm before generating:**

```
I've analyzed your [format]: "[title]"

Core insight: [insight]
Key points: [3-5 points]
Voice: [voice profile]

I'll generate these formats:
- Twitter thread (8-12 tweets)
- LinkedIn post (~1000 chars)
- Newsletter section

Proceed with cascade? [Yes / Modify formats / Cancel]
```

**Wait for user confirmation before continuing.**

### Step 3: Generate Derived Formats

For each target format, launch `format-specialist` agent or generate inline:

#### Twitter Thread Derivation

```
Extract from source:
1. Hook — Most surprising/compelling point
2. Context — Why this matters (1-2 tweets)
3. Key insights — 3-5 main points (1 tweet each)
4. Evidence — Best code snippet or metric
5. Takeaway — What reader should do
6. CTA — Engagement prompt

Constraints:
- Each tweet ≤280 chars
- Each tweet has standalone value
- No "1/" or "Thread:" prefixes
```

#### LinkedIn Post Derivation

```
Extract from source:
1. Hook — Professional angle on the insight
2. Story — Personal/team journey element
3. Takeaways — 3 actionable bullet points
4. Question — Engagement prompt

Constraints:
- 800-1300 characters
- Short paragraphs (1-2 sentences)
- Professional but personal tone
```

#### Newsletter Section Derivation

```
Extract from source:
1. Intro — Why subscribers should care
2. Exclusive angle — Behind-the-scenes or deeper context
3. Key insight — The main takeaway
4. Link — To full content

Constraints:
- 150-300 words
- Adds value beyond the source
- Teases without giving everything away
```

### Step 4: Quality Validation

For each derived piece:
- Run format-specific checklist
- Verify voice consistency with source
- Check platform constraints
- Validate readability for audience

### Step 5: Delivery with Posting Schedule

```markdown
## Cascade Complete: [Source Title]

### Twitter Thread (8 tweets)
[Full thread content]

**Suggested posting:** Immediately or within 24 hours
**Best times:** 9am, 12pm, or 5pm (audience timezone)

---

### LinkedIn Post (1,150 chars)
[Full post content]

**Suggested posting:** 1-3 days after Twitter
**Best times:** Tuesday-Thursday, 8-10am

---

### Newsletter Section (220 words)
[Full section content]

**Suggested posting:** Next newsletter issue
**Note:** Link back to full blog post

---

## Posting Sequence

| Day | Platform | Content |
|-----|----------|---------|
| 0 | Twitter | Thread (immediate, raw insight) |
| 1-2 | LinkedIn | Post (refined, professional) |
| 7+ | Newsletter | Section (exclusive angle) |
```

---

## Format Options

Specify which formats to generate:

```bash
# All formats (default)
/c2c:cascade blog-post.md

# Specific formats
/c2c:cascade blog-post.md --formats twitter,linkedin

# Social only
/c2c:cascade blog-post.md --formats twitter,linkedin

# Newsletter focus
/c2c:cascade blog-post.md --formats newsletter
```

Available formats:
- `twitter` — Thread (8-12 tweets)
- `linkedin` — Post (800-1300 chars)
- `newsletter` — Section (150-300 words)
- `readme` — Documentation section
- `all` — All applicable formats (default)

---

## Voice Consistency Rules

All derived content must maintain source voice:

| Source Voice | Twitter Adaptation | LinkedIn Adaptation |
|--------------|-------------------|---------------------|
| Precise (Rust) | Technical, exact | Technical authority |
| Pragmatic (JS) | Conversational, tips | Practical insights |
| Accessible (Python) | Friendly, clear | Approachable expert |
| Direct (Go) | Minimal, punchy | Concise professional |

---

## Example Cascade

**Source:** Blog post "How We Cut API Response Time by 73%"

**Twitter Thread:**
```
Tweet 1: We cut our API response time by 73%. Here's the one change that made the biggest difference:

Tweet 2: Our p99 latency was 2.3 seconds. Users were complaining. We tried caching, query optimization, CDNs. Nothing moved the needle significantly.

Tweet 3: Then we found it: N+1 queries hiding in our user permissions check. Every API call was making 47 separate database queries.

...

Tweet 8: The fix took 2 hours. Results:
- p99: 2.3s → 620ms
- Database load: -68%
- User complaints: 0

Sometimes the biggest wins are the simplest fixes.
```

**LinkedIn Post:**
```
We were losing users to slow API responses.

After weeks of optimization attempts, we discovered something embarrassing: 47 hidden database queries on every single API call.

The fix took 2 hours. The result:
• Response time: 73% faster
• Database load: 68% lower
• Zero user complaints since

Three lessons learned:

1. Profile before optimizing (we wasted weeks on the wrong things)
2. Check your ORMs (they hide expensive operations)
3. Simple fixes often beat complex solutions

What's the simplest fix that gave you the biggest performance win?
```

**Newsletter Section:**
```
From the blog: The 2-Hour Fix That Changed Everything

Last month I shared our API performance journey. The TL;DR: we were making 47 hidden database queries per request. Embarrassing, right?

What I didn't share publicly: we almost mass-refactored our entire data layer before finding this. Three engineers, two weeks of planning—all unnecessary.

The real lesson isn't about N+1 queries. It's about profiling BEFORE optimizing.

→ Read the full story [link]
```

---

## Cascade vs. Individual Commands

| Approach | When to Use |
|----------|-------------|
| `/c2c:cascade` | You have finished content and want to repurpose it quickly |
| `/c2c:twitter` | You want a from-scratch thread with full 5-phase process |
| `/c2c:linkedin` | You want a from-scratch post with full 5-phase process |

Cascade is faster but derives from existing content.
Individual commands do deeper original analysis.

---

## Quality Gates

Each derived piece must pass:

- [ ] Voice matches source content
- [ ] Platform constraints met (chars, structure)
- [ ] Readability appropriate for platform
- [ ] Key insight preserved
- [ ] No information contradicts source
- [ ] CTA/engagement element included
