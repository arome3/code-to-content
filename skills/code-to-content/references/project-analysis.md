# Project Analysis Protocol

Before generating any content about a user's project, execute this analysis protocol to extract compelling material.

This protocol spans two phases. **Phase 1 (Code Analysis)** mines the codebase for the WHAT. **Phase 2 (Differentiation Discovery)** extracts the WHY, the opinion, and the roads not taken from the *human* — the material the code cannot contain. Section 4 (Developer Interview) is the spine of Phase 2, not an optional fallback. Pair this with `references/differentiation.md`.

> The dimensions below are not all equal. **Problem → THE WHY** and **Journey/Architecture → ROADS NOT TAKEN** are the differentiating targets — the things a competitor could not write. Treat them as required extraction goals in Phase 2, not as one content angle among many.

---

## 1. Analyze Five Dimensions

Examine each dimension systematically. Ask clarifying questions if information is missing.

### Problem Dimension → THE WHY (differentiating target)

Go past "what problem does it solve" to the strategic conviction behind it. Extract:
- The specific pain point that triggered this project
- **The belief that made this worth building *now*** — what does the builder think is changing in the world?
- **The insight or secret only they have** — a customer conversation, a number they saw, a thing they know that the market doesn't yet
- Who experiences this pain and how frequently
- What workarounds existed before this solution
- The tangible cost of the unsolved problem

Identify content angles from:
- The thesis the product is a consequence of (lead with this, not the feature)
- The frustration origin story
- Why existing solutions fell short

### Solution Dimension

Extract these elements:
- The core mechanism that makes it work
- The simplest explanation (one sentence)
- The technical explanation (full depth)
- The key differentiator from alternatives

Identify content angles from:
- The central insight driving the approach
- Simplified mental models
- Technical decision rationale

### Journey Dimension → ROADS NOT TAKEN (differentiating target)

The choices *not* made are the story an AI can never invent. Extract:
- **The obvious thing a competent team would have built — and why they didn't**
- **What was cut, deferred, or deliberately left to another layer, and the trade-off behind it**
- The hardest technical challenge encountered
- Approaches attempted but abandoned (and the deciding factor that killed them)
- Unexpected discoveries during development
- Hindsight lessons

Identify content angles from:
- "We considered X but chose Y because Z" decisions
- Debugging war stories
- Failed approaches and pivots

### Architecture Dimension

Extract these elements:
- High-level system architecture
- Technology choice rationale
- Key abstractions and their purpose
- Significant tradeoffs made

Identify content angles from:
- Design-for-constraint narratives
- Technology betting decisions
- Abstraction breakthrough moments

### Impact Dimension

Extract these elements:
- Metrics that improved (quantified if possible)
- User feedback received
- New capabilities enabled
- Future potential and roadmap

Identify content angles from:
- Before/after comparisons
- Performance improvements
- Unlocked possibilities

---

## 2. Locate the "Aha!" Moment

Find the single insight that shifts reader thinking. Probe with these questions:

1. "What's the one thing about this project worth telling a friend?"
2. "What belief changed during development?"
3. "What's counterintuitive about your solution?"
4. "What knowledge would have saved you days?"

Recognize strong "Aha!" patterns:
- Optimization insight: "The fastest code is code that never runs"
- Architecture insight: "We were caching the wrong thing"
- Perspective shift: "The bug was a feature in disguise"
- Paradox: "Simplicity required more engineering, not less"

---

## 3. Perform Code Archaeology

When the user provides a codebase, analyze these areas:

### Structure Analysis

Locate:
- Entry points (main.py, index.ts, App.jsx)
- Core logic location
- Data flow path (input -> processing -> output)
- External integrations (APIs, databases, services)
- Configuration surface

### Pattern Recognition

Identify:
- Design patterns (factory, observer, strategy, etc.)
- Architectural patterns (MVC, microservices, event-driven)
- Error handling approach
- State management strategy
- Testing methodology

### Complexity Hotspots

Find interesting content sources by locating:
- Largest files (often contain core logic)
- Most imported modules (key abstractions)
- Complex functions (where hard problems were solved)
- Heavily commented sections (explains non-obvious decisions)

---

## 4. Conduct Developer Interview (Phase 2 spine — always offered, never blocking)

This is the core of Phase 2, not a fallback. The codebase gave you the WHAT; this gets the WHY, the opinion, and the roads not taken. **Always offer it. Never block on it** — if the user declines, proceed on code alone and flag `Distinctiveness: AT RISK`.

### Open with the offer (one message, three paths + opt-out)

> "To make this unmistakably yours — something a competitor couldn't republish — I can:
> (a) ask you 4–5 quick questions,
> (b) take raw material: a Slack thread, support tickets, a 2-minute voice-memo transcript, rough notes, or
> (c) polish a rough draft you write (write it ugly; I'll keep your voice).
> Or I can proceed from the code alone. Which do you want?"

### Mess over spec
If they share raw material, rank it **above** the polished README (see `differentiation.md`). Rough Slack arguments and support tickets carry the signal; clean specs are what everyone's competitor also has.

### The questions (grouped by extraction target)

**THE WHY (Move 1):**
- "Why was this worth building *now*? What changes in the world if it works?"
- "What did a customer say, or what did you see, that made this undeniable?"

**THE SPIKY CLAIM (Move 2):**
- "What do most people in your space get *wrong* that you do differently?"
- "What's one sentence here a competitor would refuse to sign their name to?"

**ROADS NOT TAKEN (Move 3):**
- "What's the obvious thing you *could* have built — and why didn't you?"
- "What almost shipped but got killed, and what was the deciding factor?"

**Story + technical depth:**
- "What's something you tried first that didn't work?"
- "Was there a moment where everything clicked?"
- "Walk me through what happens when [core action occurs]."

**FOUNDER VOICE (capture as rejections — see `brand-voice.md`):**
- "Paste one line you've written that sounds like *you*."
- "What words, punctuation, or tone would you never use?"

---

## 5. Generate Project Brief

After completing analysis, produce this brief internally to guide content creation:

```
PROJECT BRIEF: [Name]

ONE-LINER:
[Single sentence: what it does and for whom]

PROBLEM:
[2-3 sentences: the pain point]

SOLUTION:
[2-3 sentences: the approach]

KEY INSIGHT:
[The "Aha!" moment in one sentence]

TECH STACK:
- [Component]: [Technology]
- Notable: [Interesting choices]

CHALLENGES OVERCOME:
1. [Challenge] -> [Solution]
2. [Challenge] -> [Solution]

RESULTS/IMPACT:
- [Metric or outcome]
- [Metric or outcome]

--- DIFFERENTIATION BRIEF (from Phase 2) ---

THE WHY:
[The thesis / stakes / only-you-know insight the piece should lead with]

THE SPIKY CLAIM:
[One defensible opinion a reasonable reader could disagree with. Leave blank if not captured.]

ROADS NOT TAKEN:
[What they chose not to build + the trade-off. Leave blank if not captured.]

FOUNDER VOICE:
- Sounds like: [positive anchor line]
- Never: [rejected words/punctuation/tone]
- Source: [interview / transcript / rough draft / NONE → tech-stack fallback]

RAW MATERIAL CAPTURED:
[Slack/tickets/transcript/notes, or "none"]

DISTINCTIVENESS FORECAST:
[ON TRACK — at least one of WHY/opinion/roads captured | AT RISK — code only, offer declined]

BEST CONTENT ANGLES:
1. [Angle]: [Why compelling]
2. [Angle]: [Why compelling]
3. [Angle]: [Why compelling]
```

---

## 6. Map Insights to Formats

Use this mapping to recommend content formats:

| Insight Type | Best Format | Reason |
|--------------|-------------|--------|
| "How we solved X" | Blog post | Supports technical depth |
| Quick win/tip | Twitter thread | Scannable, shareable |
| Career/decision story | LinkedIn | Professional narrative audience |
| Technical deep-dive | Blog post | Long-form explanation space |
| Announcement | Twitter + LinkedIn | Broad reach for launches |
| Teaching moment | Tutorial | Step-by-step structure |
| Conceptual clarity | Explainer | Mental model focus |

After completing this analysis, proceed to the appropriate format in `references/formats.md`.
