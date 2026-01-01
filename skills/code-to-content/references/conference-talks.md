# Conference Talk Generation: Implementation Instructions

Generate CFP abstracts and talk outlines from a user's project. Focus on extractable narratives and insights from the codebase.

**Scope:** This guide covers text content Claude can generate—CFP submissions and talk outlines. Presentation prep, demos, and rehearsal are the developer's responsibility.

---

## Deliverables

| Claude Generates | Developer Handles |
|------------------|-------------------|
| CFP abstract | Slide design |
| Talk outline with timing | Demo preparation |
| Core thesis/angle | Live coding practice |
| Speaker notes (brief) | Q&A rehearsal |
| Title options | Equipment/logistics |

---

## Step 1: Extract the Core Thesis

Before generating any content, identify the single memorable idea.

### Find the Insight

Scan the project for:
- Non-obvious architectural choices
- Deviations from standard patterns
- Pivotal decisions with tradeoffs
- Performance improvements with specific numbers

### Crystallize Into One Sentence

Use this template:
```
"By [doing X differently], [the project] achieved [surprising result Y]"
```

### Project Pattern → Talk Angle

| If the project has... | Generate this angle |
|-----------------------|---------------------|
| Custom solution over library | "Why We Rolled Our Own X" |
| Major refactor documented | "The Refactor That Changed Everything" |
| Performance optimization | "From Xms to Yms: The Journey" |
| Pattern adoption | "How [Pattern] Saved Our Codebase" |
| Migration story | "Migrating from A to B: Lessons Learned" |
| Unusual tech combination | "Why We Combined X and Y" |

---

## Step 2: Generate CFP Abstract

Write CFPs grounded in real project outcomes.

### Title Format

```
[Decision/Pattern]: How We [Outcome Verb] [Metric Improvement]
```

**Examples:**
- "Event Sourcing in Practice: How We Eliminated 90% of Data Bugs"
- "The Pull-Based Revolution: How We Cut Latency by 3x"
- "From Monolith to Modules: Making {{project_name}} Maintainable"

### Abstract Structure (3 paragraphs)

**Paragraph 1 - HOOK:**
```
When we started {{project_name}}, we faced {{specific_problem}}.
After {{time_period}}, we achieved {{concrete_improvement}} and learned
lessons that apply to any team facing similar challenges.
```

**Paragraph 2 - JOURNEY:**
```
In this talk, I'll walk through our journey from {{before_state}} to
{{after_state}}, including the {{key_change}} that made the difference.
You'll see real code from our production system and understand the
tradeoffs we navigated.
```

**Paragraph 3 - TAKEAWAYS:**
```
You'll leave with:
- A framework for evaluating {{decision_type}} in your own projects
- Warning signs we missed (and how to spot them earlier)
- The specific pattern that made {{outcome}} possible
```

### CFP Length Variants

**Short (100 words):** Hook + one-sentence journey + bullet takeaways
**Standard (200 words):** Full three-paragraph structure
**Extended (300 words):** Add context paragraph after hook

---

## Step 3: Generate Talk Outline

Match project scope to appropriate format.

### Lightning Talk (5-10 min)

```
[0:00] HOOK
"We were losing {{pain_metric}} until we {{key_change}}."

[0:30] PROBLEM
The before state. Core problem in one visual.

[1:30] THE INSIGHT
The architectural decision. Show the pattern (simplified).

[3:30] THE RESULT
Before/after numbers. One comparison.

[4:30] TAKEAWAY
"If you're seeing {{symptom}}, consider {{pattern}}."
Link to code/resources.
```

### Standard Talk (25-30 min)

```
OPENING (3 min)
- Hook: The moment we knew something had to change
- Context: Brief on {{project_name}} and scale
- Preview: What we'll cover

THE BEFORE (5 min)
- Early architecture
- Pain points from {{specific_issues}}
- Why standard approaches weren't working

THE DECISION (7 min)
- What we chose
- Why it was non-obvious
- Tradeoffs accepted

THE IMPLEMENTATION (10 min)
- Key code patterns
- The core refactor
- What changed architecturally

THE RESULTS (3 min)
- Concrete metrics: {{before}} → {{after}}
- What became possible
- Unexpected benefits

YOUR TURN (2 min)
- How to evaluate for your project
- First steps to try
- Resources
```

### Deep Dive (45-60 min)

Expand standard structure with:
- Multiple implementation sections
- Code walkthrough segments
- Comparison with alternatives
- Extended Q&A time built in

---

## Step 4: Generate Speaker Notes

Brief notes grounding each section in project specifics.

### Notes Format

```
SLIDE: [Title]
TIME: [Timestamp]
SAY: "[Opening line for this section]"
REFERENCE: [Specific file, commit, or metric from project]
TRANSITION: "[Bridge to next section]"
```

### Example Notes Block

```
SLIDE: The Breaking Point
TIME: 2:00
SAY: "This is the commit where everything changed."
REFERENCE: Commit {{hash}} - "Refactor auth to use {{pattern}}"
TRANSITION: "Once we saw this working, we knew we had to go further."
```

---

## Output Format

Deliver talk content as:

```markdown
# {{Talk Title}}

## CFP Abstract
[200-word abstract]

## Talk Details
- **Format:** [Lightning / Standard / Deep Dive]
- **Duration:** [X] minutes
- **Audience:** [Beginner / Intermediate / Advanced]

## Core Thesis
[One sentence]

## Outline
[Timed outline with section headers]

## Speaker Notes
[Section-by-section notes]

## Suggested Conferences
[2-3 relevant conferences based on topic/stack]
```

---

## Pre-Delivery Checklist

Before delivering talk content:

```
[ ] Thesis derived from actual project decision
[ ] CFP references specific outcomes, not hypotheticals
[ ] Outline timing adds up correctly
[ ] All {{variables}} filled with project specifics
[ ] No generic advice—everything tied to codebase
[ ] Appropriate format for content depth
```
