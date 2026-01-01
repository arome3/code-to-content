# Project Analysis Protocol

Before generating any content about a user's project, execute this analysis protocol to extract compelling material.

---

## 1. Analyze Five Dimensions

Examine each dimension systematically. Ask clarifying questions if information is missing.

### Problem Dimension

Extract these elements:
- The specific pain point that triggered this project
- Who experiences this pain and how frequently
- What workarounds existed before this solution
- The tangible cost of the unsolved problem

Identify content angles from:
- The frustration origin story
- Why existing solutions fell short
- Quantified developer/user pain

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

### Journey Dimension

Extract these elements:
- The hardest technical challenge encountered
- Approaches attempted but abandoned
- Unexpected discoveries during development
- Hindsight lessons

Identify content angles from:
- Debugging war stories
- Failed approaches and pivots
- Hard-won knowledge

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

## 4. Conduct Developer Interview

When information gaps exist, ask the user directly. Use these question categories:

**Opening (establish scope):**
- "In one sentence, what does this project do?"
- "Who is this for and what were they doing before?"

**Technical depth (mine implementation details):**
- "Walk me through what happens when [core action occurs]"
- "What was the trickiest part to get right?"
- "What would break if we removed [component]?"

**Story mining (extract narrative):**
- "What's something you tried first that didn't work?"
- "Was there a moment where everything clicked?"
- "What would you tell someone starting a similar project?"

**Differentiation (find unique angles):**
- "Why this approach vs [common alternative]?"
- "What's unusual about your implementation?"
- "What are you most proud of technically?"

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
