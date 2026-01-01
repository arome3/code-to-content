# Content Format Guides

Consolidated reference for generating technical content across different formats. Each section contains implementation instructions for a specific content type.

---

## Table of Contents

1. [Blog Posts](#blog-posts) - Technical articles and feature announcements
2. [Tutorials](#tutorials) - Step-by-step learning guides
3. [Code Explainers](#code-explainers) - Clear code explanations
4. [Social Content](#social-content) - Twitter/X threads, LinkedIn posts
5. [Documentation](#documentation) - READMEs, API docs, architecture docs
6. [Conference Talks](#conference-talks) - CFP abstracts and talk outlines
7. [Newsletters](#newsletters) - Project update editions
8. [Building in Public](#building-in-public) - Progress updates and accountability posts
9. [Code Snippets](#code-snippets) - Shareable code images
10. [Product Launch](#product-launch) - Multi-platform launch content
11. [Posting Plan](#posting-plan) - Multi-day content schedules

---

## Blog Posts

Generate blog posts and technical articles from a user's project.

### Pre-Generation: Extract from Project

Before generating any blog post, extract these elements:

```
FROM PROJECT ANALYSIS, IDENTIFY:
├── Core problem the project solves
├── Key technical decisions and their rationale
├── Notable implementation patterns
├── Performance characteristics or metrics
├── Challenges encountered and solutions applied
├── Dependencies and technology choices
└── Target audience (developers, ops, data scientists, etc.)
```

### Title Formulas

**For outcome-focused projects (has metrics/results):**
- "How [Project] Achieves [Specific Result]"
- "[Number] Patterns Behind [Project's] [Impressive Attribute]"
- "Building [Project Type] That [Measurable Achievement]"

**For problem-solving projects:**
- "Why [Common Approach] Fails (And How [Project] Solves It)"
- "The [Problem] That Led to [Project]"
- "[Surprising Insight]: How [Project] [Unexpected Approach]"

**For utility/tool projects:**
- "A Practical Guide to [Project's Core Function]"
- "[Project Domain] From First Principles"
- "The Missing Tool for [Problem Space]"

**Title rules:**
- Keep to 5-10 words
- Include specific outcome or insight from the project
- Use concrete numbers when the project has metrics
- Never: "My Thoughts on...", "Introduction to...", "A Discussion of..."

### Opening Hook Patterns

**In-Media-Res** (project has compelling origin story):
Start mid-action in the problem that created the project.

**Results-First** (project has quantifiable achievements):
Lead with the most impressive metric or outcome.

**Counterintuitive Claim** (project challenges conventional approaches):
State the surprising truth the project demonstrates.

**Relatable Problem** (project addresses widespread developer pain):
Describe the universal experience the project addresses.

**Opening rules:**
- First sentence must hook immediately
- Establish stakes by paragraph 2
- Preview the insight without spoiling details
- Never: "In this post, I will...", "Hello everyone...", "Let me define..."

### Body Structures

**Problem-Solution Posts:**
```
## The Problem [Project Name] Addresses
## What Traditional Approaches Miss
## How [Project] Works
## Results and Insights
```

**Before/After Posts:**
```
## The Old Way
## Where It Breaks Down
## The [Project] Approach
## The Impact
```

**Deep-Dive Posts:**
```
## The Simple Version
## Adding Real-World Complexity
## The Full Implementation
## Advanced Considerations
```

### Code Block Rules

1. Extract the most illustrative code section, not the most complex
2. Add "why" comments explaining rationale, not mechanics
3. Strip boilerplate that doesn't illuminate the concept
4. Include type hints if the project uses them
5. Mark key insight lines with highlight comments

**Progressive revelation:** Simple version (5-10 lines) → With error handling → Production version

### Length Guidelines

| Content Type | Target Length |
|--------------|---------------|
| Feature announcement | 500-800 words |
| Technical walkthrough | 1500-2500 words |
| Architecture deep-dive | 3000-5000 words |
| Comprehensive guide | 5000+ words |

### SEO Elements

```
Title tag: [Generated title] (50-60 chars)
URL slug: [3-5 keywords from title, hyphenated]
Meta description: [Problem solved] + [Key insight] (150-160 chars)
```

---

## Tutorials

Generate step-by-step tutorials from a user's project.

### Generation Approach

```
FOUNDATION: Generate working code immediately (first win)
    ↓
BUILD: Add one concept per section (manageable chunks)
    ↓
COMPLETE: End with production-ready result (real accomplishment)
```

### Required Structure (6 Sections)

**1. Hook & Outcome:**
```markdown
# [Action Verb] a [Result] with [Technology]

[Description of what reader will build]

**What you'll learn:**
- [Concept 1]
- [Concept 2]
- [Concept 3]

**Prerequisites:**
- [Required knowledge]
- [Required tools]
- [Time estimate]

**Final code:** [Link placeholder]
```

**2. Prerequisites:**
```markdown
## Prerequisites

**Required Knowledge:**
- [Skill with specificity]

**Not Required (covered in tutorial):**
- [Concept this tutorial teaches]

**Tools Needed:**
- [Tool with version]

**Estimated Time:** [X] minutes
**Difficulty:** [Beginner/Intermediate/Advanced]
```

**3. Foundation (First 5 minutes):**
```markdown
## Step 1: [Action] ([Time] minutes)

[One-sentence goal]

```[language]
[Minimal setup commands]
```

[Expected result]

**Checkpoint:** [Specific verification]
```

**4. Build (One concept per section):**
```markdown
## Step [N]: [Feature Name]

[Context connecting to previous step]

**Add this code:**
```[language]
[New/changed code with context]  // ← ADD THIS
```

**What's happening:**
1. [Explanation of block 1]
2. [Explanation of block 2]

**Checkpoint:** [Verification step]
```

**5. Polish (Production considerations):**
```markdown
## Step [N]: Error Handling

[Context: why this matters]

```[language]
[Error handling code]
```

**Why this matters:**
[Real-world scenario]
```

**6. Next Steps:**
```markdown
## What's Next?

**You built:** [Summary]

**Extend this project:**
- [ ] [Extension 1]
- [ ] [Extension 2]

**Related topics:**
- [Topic 1] - [Brief description]

**Full code:** [Repository link]
```

### Checkpoint Types

- Terminal output: "Terminal shows 'Server running on port 3000'"
- Visual result: "Page displays the form with three fields"
- Console log: "Browser console shows the API response"
- Behavior: "Clicking the button triggers the animation"

### Troubleshooting Blocks

```markdown
<details>
<summary>Not working? Common issues</summary>

**Error: "[Likely error message]"**
[Solution]

**Still stuck?**
Compare your code with [checkpoint reference]
</details>
```

---

## Code Explainers

> **Full reference:** `references/code-explainers.md` - Complete templates and depth strategies

Generate clear code explanations from a user's project.

### Core Principle

**Explain the WHY, show the WHAT, demonstrate the RESULT.**

Never narrate code line-by-line. Structure explanations to answer:
- Why this approach?
- What problem does this solve?
- What happens when it runs?

### The Explanation Stack

```
LEVEL 4: The Result (what happens)
    ^
LEVEL 3: The Code (how it's implemented)
    ^
LEVEL 2: The Approach (why this way)
    ^
LEVEL 1: The Problem (what we're solving)
```

**Always start at Level 1, not Level 3.**

### Annotation Patterns

**Inline Why Pattern** (individual decisions throughout a function):
```python
def process_image(image_path):
    # JPEG compression can corrupt alpha channels
    # so we convert to PNG for processing
    img = Image.open(image_path).convert("RGBA")
```

**Section Comment Pattern** (multi-step processes with distinct phases):
```python
def authenticate_user(request):
    # ----------------------------------------------
    # STEP 1: Extract and validate token format
    # ----------------------------------------------
    auth_header = request.headers.get("Authorization")
```

**Before/After Pattern** (refactoring, improvements, migrations):
```javascript
// BEFORE: Callback hell
getUser(userId, function(user) { ... });

// AFTER: Async/await
const user = await getUser(userId);
```

**Highlighting Key Lines Pattern** (critical insight or optimization):
```python
    # vvv THE KEY INSIGHT vvv
    if should_use_index(plan):
        plan = rewrite_with_index_hints(plan)
    # ^^^ This reduced p99 latency by 10x ^^^
```

### Complexity Strategies

**Strategy 1: Build Up Incrementally**
Version 1 (simplest) → Version 2 (type hints) → Version 3 (edge cases)

**Strategy 2: Simplify Then Expand**
Conceptual pseudocode first → Real implementation

**Strategy 3: Analogy First**
Relatable analogy → Connect to code

### Visual Aids

**ASCII Diagrams** (request flows, architecture):
```
Request -> [Auth] -> [RateLimit] -> [Logging] -> Handler -> Response
```

**State Transition Tables** (state machines, event handling):
```
| Current State | Event Received | New State | Side Effect |
```

**Data Flow Visualizations** (pipelines, transformations):
```python
# Raw Data -> Clean -> Enrich -> Aggregate -> Output
```

---

## Social Content

> **Full reference:** `references/social-content.md` - Complete hook formulas, thread structures, LinkedIn templates

Generate Twitter/X threads, LinkedIn posts, and social content from technical projects.

### Platform Selection

| Platform | When to Use | Tone | Constraints |
|----------|-------------|------|-------------|
| Twitter/X | Quick insights, announcements | Casual, punchy | 280 chars/tweet, 8-15 tweets |
| LinkedIn | Career narratives, business impact | Professional, story-driven | 1300-3000 chars |
| Dev.to | Tutorial snippets, announcements | Technical, detailed | Medium-length |
| Reddit | Discussion prompts, feedback | Authentic, no self-promotion | Variable |

### Twitter Thread Structure

```
TWEET 1: HOOK
- Stop the scroll with surprising fact, result, or question
- Promise value immediately
- Never use "thread incoming" or similar preamble

TWEETS 2-N: BODY
- One idea per tweet
- Each tweet comprehensible standalone
- Visual placeholders for code screenshots

FINAL TWEET: CTA
- Summarize key takeaway
- Call to action (question, link, follow)
```

### Hook Formulas

**Surprising Statement:**
```
[Unexpected action or result]
[Positive outcome 1/2/3]
Here's what I learned:
```

**Contrarian Take:**
```
Hot take: [Challenge conventional wisdom]
I've been [credential]. Here are [N] practices I've stopped:
```

**Results-First:**
```
We [achieved specific result].
No [expected approach]. Just [simple explanation].
Here's exactly what we changed:
```

**Curiosity Gap:**
```
The most useful [concept] isn't:
- [Expected thing]
It's something [surprising contrast].
```

### Thread Length

| Content Type | Target Length |
|--------------|---------------|
| Quick tip | 3-5 tweets |
| Story/lesson | 7-10 tweets |
| Tutorial/guide | 10-15 tweets |
| Deep dive | 15-20 tweets |

### LinkedIn Post Structure

```
HOOK (First 2 lines - visible before "See more")
- First line must compel the click
- Line break after hook

STORY (3-4 paragraphs)
- Set scene with specific situation
- Present challenge or conflict
- Describe decision or action
- Show outcome with specifics

LESSON (Takeaway section)
- Generalize what was learned
- Bullet points for scannability

CTA (Engagement close)
- Genuine question
- 3-5 relevant hashtags
```

### LinkedIn Hook Formulas

**The Confession:**
```
I [surprising action].
[Stakeholder reaction].
Here's why I did it anyway:
```

**The Numbers Hook:**
```
[Impressive metric from project].
We didn't [expected approach].
We changed one thing:
```

---

## Documentation

Generate README files, API documentation, and technical docs from user projects.

### README Structure (Priority Order)

**Level 1 - Identity (always include):**
- Project name with one-line description
- The problem it solves (2-3 sentences)
- Who should use it

**Level 2 - Usage (always include):**
- Installation command
- Quick start with minimal working example
- Basic usage patterns

**Level 3 - Details (non-trivial projects):**
- Key concepts
- Architecture overview
- Configuration options (table format)

**Level 4 - Contribution (open source):**
- Development setup
- Link to CONTRIBUTING.md
- Testing commands

**Level 5 - Reference (as needed):**
- Advanced usage
- Troubleshooting
- Changelog link

### Configuration Tables

```markdown
| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `optionName` | type | `defaultValue` | What it controls |
```

### API Documentation Structure

```markdown
## [Action Description]

`[METHOD] [path]`

[One sentence description]

### Authentication
[Required/Optional, method]

### Request
**Headers:** [table]
**Path Parameters:** [table]
**Query Parameters:** [table]
**Body:** [JSON example + field table]

### Response
**Success ([status code]):** [JSON example]
**Errors:** [code table]

### Example
**Request:** [curl example]
**Response:** [JSON example]
```

### Architecture Documentation

**Component descriptions:**
```markdown
### [Component Name]

**Purpose:** [One sentence]
**Responsibilities:** [bullet list]
**Technologies:** [key libraries]
**Interfaces:**
- Exposes: [APIs, ports]
- Consumes: [dependencies]
```

**ASCII diagrams:**
```
┌─────────────┐     ┌─────────────┐
│  Component  │────▶│  Component  │
└─────────────┘     └─────────────┘
```

### Changelog Format (Keep a Changelog)

```markdown
## [Version] - YYYY-MM-DD

### Added
### Changed
### Fixed
### Removed
### Security
```

---

## Conference Talks

Generate CFP abstracts and talk outlines from a user's project.

### Deliverables

| Claude Generates | Developer Handles |
|------------------|-------------------|
| CFP abstract | Slide design |
| Talk outline with timing | Demo preparation |
| Core thesis/angle | Live coding practice |
| Speaker notes (brief) | Q&A rehearsal |

### Extract Core Thesis

**Find the insight:**
- Non-obvious architectural choices
- Deviations from standard patterns
- Pivotal decisions with tradeoffs
- Performance improvements with specific numbers

**Crystallize into one sentence:**
```
"By [doing X differently], [the project] achieved [surprising result Y]"
```

### Talk Angles

| If the project has... | Generate this angle |
|-----------------------|---------------------|
| Custom solution over library | "Why We Rolled Our Own X" |
| Major refactor documented | "The Refactor That Changed Everything" |
| Performance optimization | "From Xms to Yms: The Journey" |
| Pattern adoption | "How [Pattern] Saved Our Codebase" |
| Migration story | "Migrating from A to B: Lessons Learned" |

### CFP Abstract Structure (3 paragraphs)

**Paragraph 1 - HOOK:**
```
When we started {{project_name}}, we faced {{specific_problem}}.
After {{time_period}}, we achieved {{concrete_improvement}}.
```

**Paragraph 2 - JOURNEY:**
```
In this talk, I'll walk through our journey from {{before_state}} to
{{after_state}}, including the {{key_change}} that made the difference.
```

**Paragraph 3 - TAKEAWAYS:**
```
You'll leave with:
- A framework for evaluating {{decision_type}}
- Warning signs we missed
- The specific pattern that made {{outcome}} possible
```

### Talk Outline Formats

**Lightning Talk (5-10 min):**
```
[0:00] HOOK - "We were losing {{pain_metric}} until we {{key_change}}."
[0:30] PROBLEM - The before state
[1:30] THE INSIGHT - The architectural decision
[3:30] THE RESULT - Before/after numbers
[4:30] TAKEAWAY - "If you're seeing {{symptom}}, consider {{pattern}}."
```

**Standard Talk (25-30 min):**
```
OPENING (3 min) - Hook, context, preview
THE BEFORE (5 min) - Early architecture, pain points
THE DECISION (7 min) - What we chose, why non-obvious
THE IMPLEMENTATION (10 min) - Key code patterns
THE RESULTS (3 min) - Concrete metrics
YOUR TURN (2 min) - How to evaluate, first steps
```

### Speaker Notes Format

```
SLIDE: [Title]
TIME: [Timestamp]
SAY: "[Opening line]"
REFERENCE: [Specific file, commit, or metric]
TRANSITION: "[Bridge to next section]"
```

---

## Newsletters

> **Full reference:** `references/newsletters.md` - 9 complete newsletter templates (shipping update, post-mortem, origin story, etc.)

Generate newsletter editions from project updates, code changes, and development journey.

### Content Extraction Pipeline

```
PROJECT SOURCE                    NEWSLETTER CONTENT
├── recent_changes              → "What I Built This Week"
├── git_history                 → "Behind the Scenes" stories
├── tech_stack                  → Stack deep-dives
├── patterns_found              → Tips & techniques
├── challenges_solved           → Problem-solving narratives
├── lessons_learned             → "What I Learned" reflections
└── upcoming_work               → Roadmap teasers
```

### Newsletter Formats

**Format 1: Build Log** (active development)
```
├── TLDR (3 bullets: shipped, learned, next)
├── What I Built
├── What Broke
├── Code Snippet
├── Metrics
└── What's Next
```

**Format 2: Deep Dive** (after completing significant feature)
```
├── The Problem
├── Approaches Considered
├── The Solution
├── Code Walkthrough
├── Trade-offs
├── Results
└── Retrospective
```

**Format 3: Lesson Learned** (after resolving challenge)
```
├── The Situation
├── The Mistake
├── The Investigation
├── The Fix
├── The Lesson
├── The Prevention
└── Reader Takeaway
```

### Subject Line Formulas

```
FROM recent_changes:
"I mass-deleted from {{project_name}}. Here's why."
"{{number}} commits later: what I learned"

FROM challenges_solved:
"The bug that took {{time}} to find"
"I broke prod. Here's the post-mortem."

FROM lessons_learned:
"What {{technology}} taught me about {{broader_topic}}"
"I was wrong about {{assumption}}"
```

### Cadence by Project Phase

| Phase | Focus | Frequency |
|-------|-------|-----------|
| Starting | Origin story, stack choices | Once, then weekly |
| Active Development | Build logs, progress | Weekly |
| Major Feature | Deep dive on approach | Per feature |
| Bug Fix/Incident | Post-mortem, lessons | As they happen |
| Milestone/Launch | Retrospective, metrics | Per milestone |

---

## Building in Public

> **Full reference:** `references/building-in-public.md` - Monthly update templates, milestone announcements, metrics tracking

Generate periodic project updates for building in public content.

### Update Types

**Daily Update (Micro):**
```
Day [X] of building [Project]:

✓ [Accomplishment 1]
✓ [Accomplishment 2]

Tomorrow: [Next focus]

[Metric if available]
```

**Weekly Update (Standard):**
```
Week [X] building [Project] in public:

Biggest win: [One-liner]

What shipped:
• [Feature/fix 1]
• [Feature/fix 2]
• [Feature/fix 3]

What I learned: [Insight]

Metrics:
[Before] → [After]

Hardest part: [Challenge + resolution]

Next week:
→ [Priority 1]
→ [Priority 2]

[Question for audience]
```

**Monthly Update (Comprehensive):**
```markdown
## Wins
[Major accomplishments with context and impact]

## Metrics
[Key numbers with trends and month-over-month comparison]

## Challenges
[What went wrong, what took longer, how addressing it]

## Learnings
[Technical, product/market, personal/process insights]

## Next Month
[Specific goals, experiments to run]

## Ask
[Specific help needed, feedback requested]
```

**Milestone Update (Event-Driven):**
```
[Milestone announcement with context]
[The journey to get here]
[What this means]
[Gratitude / acknowledgment]
[What's next]
```

### Tone Calibration

**For Wins:**
```
DO: Share genuine excitement, specific details, gratitude
DON'T: Humble-brag, minimize, over-hype

GOOD: "Hit 1,000 users today. Took 6 months. Still can't believe people use this."
BAD: "So humbled to announce we've achieved the incredible milestone..."
```

**For Challenges:**
```
DO: Be honest, share learning, show resilience
DON'T: Complain without insight, seek pity

GOOD: "Spent 3 days debugging a race condition. The fix was 2 lines."
BAD: "Everything is broken. This sucks."
```

**For Metrics:**
```
DO: Show trends, provide context, be transparent
DON'T: Cherry-pick, hide bad numbers

GOOD: "MRR: $1,200 → $1,450 (+21%). Churn: 8% (up from 5%, investigating)"
BAD: "Revenue up 21%!!!"
```

---

## Code Snippets

Generate shareable code snippet images from a user's project. Support both URL-based tools (Carbon, Ray.so) and direct SVG generation.

### When to Use

Generate code snippet images when the user:
- Wants to share code on social media (Twitter, LinkedIn)
- Needs code visuals for blog posts or articles
- Is creating slides or presentations
- Wants to highlight a specific function or pattern

### Decision Logic

```
IF user requests specific tool → Use that tool
IF user wants instant result → Generate SVG
IF user wants highest quality → Generate Carbon/Ray.so URL
IF for Twitter/LinkedIn → Carbon URL (PNG export)
IF for documentation/web → SVG (scalable)
IF user doesn't specify → Offer both options
```

### Carbon URL Generation

**Base URL:** `https://carbon.now.sh/`

**Parameters:**

| Parameter | Description | Recommended Values |
|-----------|-------------|-------------------|
| `code` | URL-encoded code | (from project) |
| `language` | Syntax highlighting | auto, javascript, typescript, python, go, rust |
| `theme` | Color theme | dracula, monokai, night-owl, one-dark, synthwave-84 |
| `bg` | Background color | rgba(0,0,0,0) for transparent, or hex |
| `fontFamily` | Code font | Fira Code, JetBrains Mono, Hack |
| `fontSize` | Font size | 14px, 16px, 18px |
| `padding` | Padding options | 16, 32, 64 |
| `lineNumbers` | Show line numbers | true, false |
| `windowControls` | Show macOS buttons | true, false |

**Generate URL:**
```
https://carbon.now.sh/?code={{url_encoded_code}}&language={{lang}}&theme={{theme}}&bg={{bg}}&fontFamily={{font}}&fontSize={{size}}&padding={{pad}}&lineNumbers={{lines}}&windowControls={{controls}}
```

**Theme by Platform:**
| Platform | Theme | Background | Why |
|----------|-------|------------|-----|
| Twitter | dracula, synthwave-84 | Solid dark | High contrast in feed |
| LinkedIn | one-dark, night-owl | Solid dark | Professional look |
| Blog (light) | github-light | Transparent | Matches light themes |
| Blog (dark) | monokai, dracula | Transparent | Matches dark themes |
| Presentation | synthwave-84 | Gradient | Eye-catching |

### Ray.so URL Generation

**Base URL:** `https://ray.so/`

**Parameters:**

| Parameter | Description | Values |
|-----------|-------------|--------|
| `code` | Base64-encoded code | (from project) |
| `language` | Language | javascript, typescript, python, etc. |
| `theme` | Theme | candy, crimson, falcon, meadow, midnight, raindrop, sunset |
| `background` | Enable background | true, false |
| `darkMode` | Dark mode | true, false |
| `padding` | Padding | 16, 32, 64, 128 |

**Generate URL:**
```
https://ray.so/#code={{base64_code}}&language={{lang}}&theme={{theme}}&background={{bg}}&darkMode={{dark}}&padding={{pad}}
```

### SVG Generation

Generate self-contained SVG with syntax highlighting. No external tools needed.

**SVG Structure:**
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {{width}} {{height}}">
  <!-- Background -->
  <rect width="100%" height="100%" rx="8" fill="{{bg_color}}"/>

  <!-- Window controls (optional) -->
  <circle cx="20" cy="20" r="6" fill="#ff5f56"/>
  <circle cx="40" cy="20" r="6" fill="#ffbd2e"/>
  <circle cx="60" cy="20" r="6" fill="#27c93f"/>

  <!-- Code block -->
  <text font-family="{{font}}" font-size="{{size}}" fill="{{text_color}}">
    {{highlighted_lines}}
  </text>
</svg>
```

**Dracula Theme Colors:**
```
Background: #282a36
Default text: #f8f8f2
Keywords: #ff79c6 (pink)
Strings: #f1fa8c (yellow)
Functions: #50fa7b (green)
Comments: #6272a4 (muted blue)
Numbers: #bd93f9 (purple)
Operators: #ff79c6 (pink)
```

**One Dark Theme Colors:**
```
Background: #282c34
Default text: #abb2bf
Keywords: #c678dd (purple)
Strings: #98c379 (green)
Functions: #61afef (blue)
Comments: #5c6370 (gray)
Numbers: #d19a66 (orange)
Operators: #56b6c2 (cyan)
```

**Language Token Patterns:**

*JavaScript/TypeScript:*
```
Keywords: const, let, var, function, return, if, else, async, await, import, export, class
Strings: "...", '...', `...`
Functions: word followed by (
Comments: // or /* */
Numbers: digits, hex
```

*Python:*
```
Keywords: def, class, return, if, else, elif, import, from, async, await, with, as
Strings: "...", '...', """...""", '''...'''
Functions: word followed by (
Comments: #
Numbers: digits
```

**SVG Line Generation:**
```svg
<tspan x="{{padding}}" dy="{{line_height}}">
  <tspan fill="{{keyword_color}}">const</tspan>
  <tspan fill="{{default_color}}"> </tspan>
  <tspan fill="{{variable_color}}">result</tspan>
  <tspan fill="{{operator_color}}"> = </tspan>
  <tspan fill="{{function_color}}">processData</tspan>
  <tspan fill="{{default_color}}">(</tspan>
  <tspan fill="{{string_color}}">"input"</tspan>
  <tspan fill="{{default_color}}">);</tspan>
</tspan>
```

### Dimension Guidelines

| Platform | Recommended Size | Aspect Ratio |
|----------|-----------------|--------------|
| Twitter | 1200x675 | 16:9 |
| LinkedIn | 1200x627 | 1.91:1 |
| Instagram | 1080x1080 | 1:1 |
| Blog embed | 800x auto | Flexible |
| Presentation | 1920x1080 | 16:9 |

| Lines of Code | Width | Font Size |
|---------------|-------|-----------|
| 1-5 | 600px | 18px |
| 6-15 | 800px | 16px |
| 16-25 | 1000px | 14px |
| 25+ | Consider splitting | 14px |

---

## Product Launch

> **Full reference:** `references/product-launch.md` - Complete Product Hunt, Hacker News, Twitter/LinkedIn launch templates

Generate launch content and strategy for a user's project across multiple platforms.

### Pre-Generation: Launch Inventory

```
PROJECT ESSENTIALS:
├── One-line description (< 10 words)
├── Value proposition (problem → solution)
├── Target audience
├── Key features (3-5 bullet points)
├── Differentiator
├── Social proof (users, stars, testimonials)
└── Call to action

LAUNCH SPECIFICS:
├── Launch platforms
├── Launch date/time
├── Demo/video available?
├── Pricing
└── Available for support on launch day?
```

### Product Hunt Launch

**Tagline (60 chars max):**
```
{{action_verb}} {{outcome}} with {{method}}
```
Examples: "Give AI agents a wallet—with guardrails"

**Maker Comment Structure:**
```
Hey Product Hunt!

I'm {{name}}, and I built {{project_name}} because {{personal_problem}}.

{{1-2 sentences on the journey}}

What you're getting today:
• {{Feature 1}}
• {{Feature 2}}

What's coming next:
• {{Roadmap item}}

I'll be here all day answering questions.
```

### Hacker News Launch

**Title Format:**
```
Show HN: {{Project}} – {{One-line description}}
```

**Post Body:**
```
{{What it does in 1-2 sentences}}
{{Why I built it - personal motivation}}
{{Technical approach in 2-3 sentences}}

Key features:
- {{Feature 1}}
- {{Feature 2}}

Demo: {{link}}
Code: {{github_link}}

Would love feedback on {{specific_aspect}}.
```

**HN Guidelines:**
- Post between 8-10am ET weekdays
- No marketing language
- Be technical and honest
- Respond to every comment

### Twitter Launch Thread

```
1/ {{Project_name}} is live.
{{Hook: surprising statement or result}}
Here's what it does and why I built it: 🧵

2/ The problem:
{{Pain point}}

3/ The solution:
{{What your project does}}

4-6/ Feature highlights with screenshots

7/ The technical approach

8/ What's next (roadmap)

9/ Try it: {{link}}

10/ RT the first tweet / Star the repo / Follow for updates
```

### Launch Day Checklist

**Pre-Launch (1 week before):**
- [ ] All content written and reviewed
- [ ] Product Hunt draft saved
- [ ] Twitter thread drafted
- [ ] GitHub README polished
- [ ] Demo/screenshots ready

**Launch Day (Morning):**
- [ ] Product Hunt goes live at 12:01am PT
- [ ] Maker comment posted immediately
- [ ] Twitter thread posted (8-9am)
- [ ] Hacker News submitted (8-10am ET)

**Launch Day (Ongoing):**
- [ ] Respond to every PH comment
- [ ] Respond to every HN comment
- [ ] Monitor for bugs/issues

### Platform Timing

| Platform | Best Time | Best Days |
|----------|-----------|-----------|
| Product Hunt | 12:01am PT | Weekdays |
| Hacker News | 8-10am ET | Tue-Thu |
| Twitter | 9-11am, 1-3pm | Tue-Thu |
| LinkedIn | 8-10am, 12pm | Tue-Thu |

---

## Posting Plan

> **Full reference:** `references/posting-plan.md` - Complete 7-day launch plan with daily content templates

Generate multi-day content schedules with ready-to-post content for each day.

### 7-Day Launch Plan Structure

```
DAY 1: The Announcement (Maximum reach)
DAY 2: The Technical Deep-Dive (Credibility)
DAY 3: The Story (Emotional connection)
DAY 4: The Use Cases (Practical value)
DAY 5: The Lessons (Wisdom sharing)
DAY 6: The Behind-the-Scenes (Authenticity)
DAY 7: The Recap + Ask (Engagement)
```

### Day 1: The Announcement

**Purpose:** Maximum visibility, clear value proposition
**Platforms:** All platforms simultaneously
**Timing:** Optimal hours (Tue-Thu, 9-11am)

Content elements:
- Clear project name and what it does
- Primary value proposition
- 3 key features or benefits
- Direct link to try/use

### Day 2: The Technical Deep-Dive

**Purpose:** Establish credibility, attract technical audience
**Platforms:** Twitter thread, Dev.to, Hacker News

Content elements:
- One interesting architectural decision
- Code snippets from actual project
- Performance characteristics
- Trade-offs considered

### Day 3: The Story

**Purpose:** Emotional connection, shareability
**Platforms:** LinkedIn (primary), Twitter

Content elements:
- Personal motivation / origin moment
- Specific obstacle or challenge
- Turning point or breakthrough
- Connection to larger theme

### Day 4: The Use Cases

**Purpose:** Practical value, help users see themselves using it
**Platforms:** Twitter, LinkedIn, relevant communities

Content elements:
- 3-5 distinct use cases
- Specific scenarios (not abstract)
- Clear outcomes for each
- Invitation to self-identify

### Day 5: The Lessons

**Purpose:** Wisdom sharing, thought leadership
**Platforms:** LinkedIn (primary), Twitter

Content elements:
- 3-5 specific lessons tied to project experience
- At least one counterintuitive insight
- Generalizable beyond this project
- Engagement question

### Day 6: The Behind-the-Scenes

**Purpose:** Authenticity, humanization
**Platforms:** Twitter, Instagram

Content elements:
- Visual element (screenshot, photo)
- Honest imperfection
- Relatable struggle
- Community invitation

### Day 7: The Recap + Ask

**Purpose:** Summary for newcomers, specific engagement ask
**Platforms:** All platforms

Content elements:
- Summary for newcomers
- Social proof (metrics, quotes, feedback)
- Forward-looking roadmap tease
- Specific feedback request
- Gratitude

### Alternative Plan Templates

**5-Day Quick Launch:**
```
Day 1: Announcement + Technical Overview
Day 2: Story + Origin
Day 3: Use Cases + Examples
Day 4: Lessons + Behind-the-Scenes
Day 5: Recap + What's Next
```

**14-Day Extended Launch:**
```
Week 1: Announcement → Technical #1 → Story → Use case #1 → Use case #2 → BTS → Recap
Week 2: Technical #2 → Lessons → User spotlight → Use case #3 → Vision → Gratitude → Full recap
```

**Ongoing Weekly Cadence:**
```
Monday: Progress update (what shipped)
Wednesday: Insight or lesson
Friday: Behind-the-scenes or community
```

### Cross-Platform Adaptation

**Twitter → LinkedIn:**
- Expand thread into flowing paragraphs
- Add professional context
- Soften casual language

**LinkedIn → Twitter:**
- Extract key points into thread
- Punch up language
- Add thread emoji (🧵)

**Twitter → Blog:**
- Expand each tweet into paragraph
- Add code examples and details
- Add SEO elements

---

## Verification Checklist (All Formats)

Before delivering any content:

```
CONTENT QUALITY:
□ Clear angle/hook in first paragraph
□ "So what?" question answered
□ Single main idea present
□ Depth matches stated audience level

STRUCTURE:
□ Hook-Journey-Payoff arc present
□ Logical flow from start to finish
□ Headers guide the reader

CODE (if applicable):
□ All examples syntactically correct
□ Imports and dependencies shown
□ Comments explain "why" not "what"

READABILITY:
□ Sentences average <25 words
□ Paragraphs contain <5 sentences
□ Technical terms explained on first use
```
