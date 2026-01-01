# Newsletter Generation Instructions

Generate newsletter editions from the user's project updates, code changes, and development journey.

---

## Content Extraction Pipeline

When generating newsletter content, extract material from project data:

```
PROJECT SOURCE                    NEWSLETTER CONTENT
├── {{recent_changes}}          → "What I Built This Week"
├── {{git_history}}             → "Behind the Scenes" stories
├── {{tech_stack}}              → Stack deep-dives & comparisons
├── {{patterns_found}}          → Tips & techniques series
├── {{challenges_solved}}       → Problem-solving narratives
├── {{lessons_learned}}         → "What I Learned" reflections
└── {{upcoming_work}}           → Roadmap teasers & previews
```

---

## Generating from Commit History

Transform commit messages into newsletter angles:

```
COMMIT TYPE                    NEWSLETTER ANGLE
──────────────────────────────────────────────────────────────
"Fix: race condition in..."  → "The Bug That Took 3 Days to Find"
"Refactor: extract..."       → "Why I Rewrote 500 Lines of Code"
"Add: caching layer..."      → "How We Cut Response Time by 80%"
"Update: migrate to..."      → "Lessons from Our [X] Migration"
"Chore: upgrade deps..."     → "What Breaking Changes Taught Me"
```

### Generate: Weekly Shipping Update

Structure the edition as:

```markdown
Subject: What I actually shipped this week (and what broke)

---

Hey {{subscriber_name}},

This week I pushed {{commit_count}} commits to {{project_name}}.
Here's what actually happened.

## The Win: {{primary_feature}}

{{recent_changes}} included [describe the main accomplishment].

The interesting part wasn't the code—it was [unexpected insight].

## The Struggle: {{challenge_faced}}

I spent [time] debugging [problem] before realizing [root cause].

The fix was [solution], but the lesson was [takeaway].

## The Numbers

- Lines added: {{lines_added}}
- Lines deleted: {{lines_deleted}}
- Tests written: {{test_count}}
- Coffee consumed: [joke number]

## What's Next

{{upcoming_work}} focuses on [next milestone]. I'm particularly
curious about [open question you're exploring].

---

What's the last thing you shipped that surprised you?

[Your name]
```

---

## Generating from Problem-Solving Stories

Identify newsletter-worthy challenges by scanning for:

```
LOOK FOR IN PROJECT DATA:
├── Files with extensive git blame history (lots of iterations)
├── Commits with long messages (complex decisions documented)
├── PRs with significant discussion
├── Code comments that explain "why" not "what"
├── Areas where multiple approaches were considered
└── Bugs that took longer than expected to fix
```

### Generate: Problem-Solving Narrative

Structure the edition as:

```markdown
Subject: I mass-deleted 2,000 lines. Here's why.

---

Hey {{subscriber_name}},

Last week I stared at {{file_or_module}} for three hours before
deleting most of it.

## The Setup

{{project_name}} had grown to [scope]. The {{problem_area}} worked,
but every change felt like playing Jenga with my production server.

## What I Tried First

My initial approach was [first attempt]. It failed because
[reason].

Then I tried [second attempt]. Better, but [limitation].

## The Breakthrough

The insight came from {{lessons_learned}}: [key realization].

Here's the before:

```{{tech_stack.primary_language}}
// The old approach
{{code_snippet_before}}
```

And the after:

```{{tech_stack.primary_language}}
// The new approach
{{code_snippet_after}}
```

## What This Taught Me

{{lessons_learned}} boiled down to one principle: [distilled insight].

If you're working on something similar, the question to ask is:
[actionable question for readers].

---

[Your name]
```

---

## Generating Project Chronicle Series

Create episodic newsletter series from ongoing project development:

```
EPISODE STRUCTURE:
├── Episode 0: "Why I'm Building This" (origin story)
├── Episode 1-N: "Building [Feature]" (progress updates)
├── Milestone Episodes: "Launching [Version]" (celebrations)
├── Crisis Episodes: "When Everything Broke" (recovery stories)
└── Retrospective: "What I'd Do Differently" (lessons compiled)
```

### Generate: Origin Story Episode

Structure the edition as:

```markdown
Subject: I'm building {{project_name}} in public. Here's why.

---

Hey {{subscriber_name}},

I'm starting something new, and I want to bring you along.

## The Problem

[Describe the problem your project solves, from personal experience]

## Why Build It

I looked at existing solutions:
- {{existing_tool_1}}: [limitation]
- {{existing_tool_2}}: [limitation]

None of them [key differentiator you're pursuing].

## The Plan

Tech stack: {{tech_stack}}

Timeline:
- Week 1-2: {{milestone_1}}
- Week 3-4: {{milestone_2}}
- Week 5+: {{milestone_3}}

## What I'll Share

Every [frequency], you'll get:
- What I shipped
- What went wrong
- What I learned
- Real code snippets

## The Ask

Reply and tell me: what would make this valuable for you?

---

Let's build.

[Your name]
```

### Generate: Progress Update Episode

Structure the edition as:

```markdown
Subject: {{project_name}} Week {{week_number}}: {{headline}}

---

Hey {{subscriber_name}},

## TLDR

- Shipped: {{primary_deliverable}}
- Learned: {{key_lesson}}
- Blocked by: {{current_challenge}}

## What I Built

{{recent_changes}}

The most interesting part was [specific technical detail].

Here's how it works:

```{{tech_stack.primary_language}}
{{code_snippet}}
```

## What Broke

[Be honest about failures—readers love authenticity]

The fix taught me: {{lessons_learned}}

## By the Numbers

| Metric | Last Week | This Week |
|--------|-----------|-----------|
| Test coverage | X% | Y% |
| API endpoints | N | N+M |
| Open issues | A | B |

## Next Week

{{upcoming_work}}

I'm most uncertain about [open question]. If you have experience
with this, I'd love to hear your approach.

---

[Your name]
```

### Generate: Crisis Post-Mortem Episode

Structure the edition as:

```markdown
Subject: We broke prod. Here's the full story.

---

Hey {{subscriber_name}},

[Day/time], {{project_name}} went down for [duration].

I'm sharing the full post-mortem because I think there are
lessons here for anyone building [type of system].

## Timeline

- **[Time]**: {{trigger_event}}
- **[Time]**: First alert fired
- **[Time]**: Identified root cause
- **[Time]**: Fix deployed
- **[Time]**: Full recovery confirmed

## Root Cause

{{challenge_description}}

The specific failure was:

```{{tech_stack.primary_language}}
// This line caused the issue
{{problematic_code}}
```

## What We Missed

Looking at {{git_history}}, the warning signs were there:
- [Sign 1]
- [Sign 2]

## The Fix

{{solution_implemented}}

```{{tech_stack.primary_language}}
// The corrected approach
{{fixed_code}}
```

## What We Changed

1. [Process change 1]
2. [Technical change 2]
3. [Monitoring change 3]

## Lessons for You

If you're building something similar, add these checks now:
- [ ] [Actionable item 1]
- [ ] [Actionable item 2]
- [ ] [Actionable item 3]

---

Have you had a similar experience? Reply—I read everything.

[Your name]
```

---

## Generating from Code Patterns

Scan the project for shareable techniques:

```
EXTRACT FROM PROJECT:
├── {{patterns_found}} - Recurring structures in the code
├── Utility functions used everywhere
├── Error handling approaches
├── Testing strategies
├── Performance optimizations
├── Configuration patterns
└── Abstractions worth explaining
```

### Generate: Technique of the Week

Structure the edition as:

```markdown
Subject: The [pattern] that simplified everything

---

Hey {{subscriber_name}},

Quick tip from {{project_name}} this week.

## The Problem

[Describe the repetitive/complex situation]

## The Pattern

In {{file_path}}, I use this approach:

```{{tech_stack.primary_language}}
{{pattern_code}}
```

## Why It Works

1. [Benefit 1]
2. [Benefit 2]
3. [Benefit 3]

## When to Use It

This pattern shines when:
- [Condition 1]
- [Condition 2]

Skip it if:
- [Anti-condition 1]
- [Anti-condition 2]

## Real Usage

Here's how it appears in production:

```{{tech_stack.primary_language}}
{{real_usage_example}}
```

---

Steal this for your own projects.

[Your name]
```

### Generate: Code Self-Review

Structure the edition as:

```markdown
Subject: I code-reviewed my 6-month-old code. Yikes.

---

Hey {{subscriber_name}},

I revisited {{module_name}} from {{time_ago}}. Here's what I found.

## What Past Me Wrote

```{{tech_stack.primary_language}}
{{old_code}}
```

## What I'd Write Today

```{{tech_stack.primary_language}}
{{improved_code}}
```

## The Differences

| Then | Now | Why |
|------|-----|-----|
| {{old_approach_1}} | {{new_approach_1}} | {{reason_1}} |
| {{old_approach_2}} | {{new_approach_2}} | {{reason_2}} |
| {{old_approach_3}} | {{new_approach_3}} | {{reason_3}} |

## What Changed My Thinking

{{lessons_learned}}

The biggest shift was understanding [key insight].

## Should You Refactor Old Code?

My rule: [your personal heuristic for when to refactor]

---

What would you change about your code from 6 months ago?

[Your name]
```

---

## Generating Refactoring Diaries

### Generate: Refactoring Journey

Structure the edition as:

```markdown
Subject: Day 3 of refactoring {{module}}. Send help.

---

Hey {{subscriber_name}},

I'm mid-refactor on {{project_name}}'s {{module_name}}, and I'm
documenting the journey.

## Why Refactor Now

{{refactoring_trigger}}

The code worked, but:
- [Pain point 1]
- [Pain point 2]
- [Pain point 3]

## The Approach

I'm using [refactoring strategy]:

```
BEFORE:
{{architecture_before}}

AFTER:
{{architecture_after}}
```

## Day-by-Day Log

**Day 1**: [What happened]
**Day 2**: [What happened]
**Day 3**: [Where I am now]

## Current Blockers

[Honest about what's hard]

## What I've Learned So Far

{{lessons_learned}}

The surprise insight: [unexpected discovery]

## What's Left

{{upcoming_work}}

I'll share the final results next week.

---

[Your name]
```

---

## Newsletter Format Selection

Select the appropriate format based on project context:

### Format 1: Build Log
Use during active development phases.

```
STRUCTURE:
├── TLDR (3 bullets: shipped, learned, next)
├── What I Built ({{recent_changes}} with context)
├── What Broke (challenges + solutions)
├── Code Snippet (one technique worth sharing)
├── Metrics (if relevant)
└── What's Next ({{upcoming_work}})
```

### Format 2: Deep Dive
Use after completing a significant feature.

```
STRUCTURE:
├── The Problem (why this feature exists)
├── Approaches Considered (what was evaluated)
├── The Solution (what was built)
├── Code Walkthrough (annotated snippets)
├── Trade-offs (what was sacrificed for what)
├── Results (metrics, feedback)
└── Retrospective ({{lessons_learned}})
```

### Format 3: Lesson Learned
Use after resolving a significant challenge.

```
STRUCTURE:
├── The Situation (what happened)
├── The Mistake (what went wrong)
├── The Investigation (how it was diagnosed)
├── The Fix (what solved it)
├── The Lesson ({{lessons_learned}})
├── The Prevention (how to avoid this)
└── Reader Takeaway (actionable advice)
```

### Format 4: Stack Review
Use for periodic reflection on technical choices.

```
STRUCTURE:
├── Current Stack ({{tech_stack}} overview)
├── What's Working (tools earning their place)
├── What's Not (tools causing friction)
├── What I'd Change (if starting over)
├── Recent Changes (migrations, additions)
├── Upcoming Evaluation (what's being considered)
└── Recommendations (for similar projects)
```

---

## Subject Line Generation

Generate subject lines from project events:

```
FROM {{recent_changes}}:
"I mass-deleted from {{project_name}}. Here's why."
"The {{feature}} is finally done. Here's how."
"{{number}} commits later: what I learned"

FROM {{challenges_solved}}:
"The bug that took {{time}} to find"
"Why {{obvious_solution}} didn't work"
"I broke prod. Here's the post-mortem."

FROM {{lessons_learned}}:
"What {{technology}} taught me about {{broader_topic}}"
"I was wrong about {{assumption}}"
"The refactor that changed how I think"

FROM {{upcoming_work}}:
"What I'm building next (and why)"
"{{project_name}} roadmap: what's coming"
"The feature I'm most nervous about"
```

---

## Generate: Complete Newsletter Edition

Structure the full edition as:

```markdown
Subject: {{project_name}} #{{issue_number}}: {{compelling_hook}}

---

Hey {{subscriber_name}},

[1-2 sentences connecting to last issue or recent work]

This week: {{brief_preview}}

---

## What I Shipped

{{recent_changes}}

[Expand on the most interesting part]

The non-obvious insight was [something readers can apply].

---

## The Code

Here's the approach I took:

```{{tech_stack.primary_language}}
{{relevant_code_snippet}}
```

**Why this works:** [brief explanation]

**The trade-off:** [what was given up for this approach]

---

## What I Learned

{{lessons_learned}}

The bigger principle: [generalized insight]

If you're working on something similar, ask yourself:
[question that helps readers apply this]

---

## What's Next

{{upcoming_work}}

I'm most uncertain about [open question].

---

## Quick Hits

- **Tool I'm trying**: [tool + why]
- **Article that helped**: [link + why]
- **Problem I'm stuck on**: [invitation for reader input]

---

Reply and tell me: [specific question related to this issue].

Until next week,
[Your name]

---

Building {{project_name}} in public | [Archive](link) | [Repo](link)
```

---

## Generation Checklist

Before generating, extract:
- [ ] Review {{recent_changes}} for newsletter-worthy items
- [ ] Identify {{lessons_learned}} from this period
- [ ] Check {{challenges_solved}} for story potential
- [ ] Note {{upcoming_work}} for teasers
- [ ] Select {{patterns_found}} worth explaining

While generating, ensure:
- [ ] Lead with what readers can learn/apply
- [ ] Include real code from the project
- [ ] Be specific about what didn't work
- [ ] Connect to previous episodes if serializing
- [ ] Add one actionable takeaway

Before finalizing, verify:
- [ ] Code snippets are accurate
- [ ] Story is honest about challenges
- [ ] Subject line reflects actual content
- [ ] CTA invites relevant reader engagement

---

## Cadence Recommendations by Project Phase

| Project Phase | Newsletter Focus | Frequency |
|---------------|------------------|-----------|
| **Starting** | Origin story, goals, stack choices | Once, then weekly |
| **Active Development** | Build logs, progress updates | Weekly |
| **Major Feature** | Deep dive on approach + results | Per feature |
| **Bug Fix/Incident** | Post-mortem, lessons learned | As they happen |
| **Refactoring** | Before/after, decision rationale | When complete |
| **Milestone/Launch** | Retrospective, metrics, next phase | Per milestone |
| **Maintenance Mode** | Lessons compiled, occasional updates | Monthly |
