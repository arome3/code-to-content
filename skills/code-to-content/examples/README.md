# Example Outputs

This directory contains before/after examples demonstrating the code-to-content skill's capabilities.

## Examples Included

### 1. Blog Post (`blog-post/`)

Transforms a codebase analysis into a compelling technical article.

| File | Description |
|------|-------------|
| `input-analysis.md` | Analysis of a CLI tool with performance optimization |
| `output-blog.md` | "How We Cut Response Time by 73%" blog post |

**Demonstrates:**
- Extracting narrative from git history
- Grounding claims in actual metrics
- Hook-Journey-Payoff structure
- Voice calibration for Python tooling

---

### 2. Twitter Thread (`twitter-thread/`)

Converts a technical insight into an engaging thread.

| File | Description |
|------|-------------|
| `input-insight.md` | Insight about caching strategy discovery |
| `output-thread.md` | 8-tweet thread with hook and CTA |

**Demonstrates:**
- Hook creation (scroll-stopping first tweet)
- Standalone value per tweet
- Progressive revelation of insight
- Engagement-driving CTA

---

### 3. README (`readme/`)

Generates comprehensive documentation from project structure.

| File | Description |
|------|-------------|
| `input-analysis.md` | FastAPI authentication library analysis |
| `output-readme.md` | Complete README with quick start, API docs, and architecture |

**Demonstrates:**
- Problem/Solution framing
- Quick Start in under 5 minutes
- Configuration tables
- Architecture diagrams

---

### 4. Negative Examples (`negative/`)

Examples of content that **fails** skill gates, with explanations and corrections.

| File | Gate Failed | Violation |
|------|-------------|-----------|
| `blog-post-weak-hook.md` | Phase 5 (Hook Quality) | Opens with "In this article, I will..." |
| `tutorial-mixed-audience.md` | Phase 5 (Readability) | Grade level 13.5 for beginners (max 8.0) |
| `readme-missing-problem.md` | Phase 4 (Template) | Skips problem statement, jumps to install |
| `twitter-thread-prefix.md` | Phase 4 (Format Rules) | Uses "Thread: 1/" prefix |
| `ungrounded-claims.md` | Phase 3 (Evidence) | "50% faster" with no data |

**Demonstrates:**
- What gate failures look like
- Specific rule violations
- Before/after corrections
- Links to evaluation questions

---

### 5. Complete Workflow (`workflow/`)

End-to-end demonstration of the **5-phase process** with actual outputs at each phase.

| File | Description |
|------|-------------|
| `blog-post-full-workflow.md` | Complete Phase 1→2→3→4→5 chain for a blog post |

**Shows:**
- Actual output from each phase (not just descriptions)
- Gate verification at each transition
- Constraint propagation (Phase N output → Phase N+1 input)
- Final quality checks with metrics

**This is the canonical reference for how the process works.**

---

### 6. Complete Generated Examples

Publication-ready content demonstrating the skill's full output quality. Each includes metadata, phase gate verification, and analysis of why it works.

| Directory | Content Type | Source Project |
|-----------|--------------|----------------|
| `newsletter/complete-example.md` | Build Log newsletter | gin-boilerplate (Go) |
| `tutorial/complete-example.md` | Step-by-step tutorial | vanilla-calendar-pro (TypeScript) |
| `linkedin-post/complete-example.md` | LinkedIn post | RecoverPy (Python) |
| `twitter-thread/complete-example.md` | Twitter/X thread | gin-boilerplate (Go) |
| `conference-talk/complete-example.md` | CFP + talk outline | RecoverPy (Python) |
| `video-script/complete-example.md` | YouTube tutorial script | lottie-react (React) |

**Each example includes:**
- Full generated content (copy-ready)
- Metadata (word count, character counts, format-specific metrics)
- Phase gate verification table
- "Why This Works" analysis

---

## Using These Examples

### Positive Examples (blog-post, readme, twitter-thread)

1. **Study the transformation**: Compare input analysis with output content
2. **Note the patterns**: Observe how raw data becomes narrative
3. **Check quality markers**: Each output demonstrates skill principles

### Negative Examples

1. **Identify the failure**: What gate does this content fail?
2. **Find the rule**: Which specific skill rule is violated?
3. **Compare corrections**: How does the fixed version differ?
4. **Connect to evaluation**: Each example links to a test question

### Workflow Example

1. **Trace the chain**: Follow output from Phase 1 through to delivery
2. **Study constraint propagation**: See how Phase N output shapes Phase N+1
3. **Verify gates**: Understand what's checked at each transition
4. **Use as template**: Copy the phase output formats for your own content

---

## Use Cases

Beyond standard technical writing, the skill's analysis and content generation capabilities support several specialized applications.

### Team Knowledge Capture

**Problem**: When senior engineers leave, institutional knowledge often disappears. Code comments go unread, and tribal knowledge about *why* decisions were made gets lost.

**Solution**: Use the blog format to generate "How This Works" documentation that's actually readable.

**Workflow**:

```bash
# Run deep analysis on the critical system
python scripts/analyze_codebase.py /path/to/payment-service --deep --json > analysis.json
```

Then prompt:

```
Using /c2c:blog, generate an internal "How Our Payment Service Works"
article for the intermediate audience. Target: new team members joining in
6 months. Focus on architectural decisions and the "why" behind patterns.
```

**Why this works**:
- `--deep` extracts design patterns, git narratives, and architectural pivots
- Blog format structures information as narrative (more engaging than wiki docs)
- Intermediate audience allows technical depth without over-explaining basics
- Evidence grounding ensures claims trace to actual code

**Limitations**: The tool analyzes *artifacts* (code, commits, comments). It cannot capture:
- Verbal discussions or Slack context
- Rejected alternatives not documented in commits
- Vendor-specific tribal knowledge
- Political/organizational context

**Pro tip**: Run this *before* someone announces departure—as part of regular documentation practice, not emergency knowledge extraction.

---

### Onboarding Accelerators

**Problem**: New hires spend weeks piecing together how systems work from scattered docs and code spelunking.

**Solution**: Generate a tutorial walking through the codebase's core flow.

```
Using /c2c:tutorial, create a "Your First Week with Our API" guide
for beginners. Cover: authentication flow, making a request, handling errors.
Target: new backend engineers.
```

The tutorial format enforces:
- Prerequisites section (what they need installed)
- 5-9 discrete steps (cognitive load managed)
- Troubleshooting section (common pitfalls)
- Verification at each step

---

### Architecture Decision Records (Informal)

**Problem**: ADRs are useful but often too formal to maintain.

**Solution**: Use blog format for lightweight "Why We Built It This Way" posts.

```
Using /c2c:blog, write "Why We Chose Event Sourcing for Orders"
for expert audience. Ground in actual implementation at src/orders/events/.
Focus on trade-offs and alternatives considered.
```

The Phase 1 analysis extracts:
- Design patterns with confidence scores
- Git narrative showing evolution
- Story-worthy commits (pivots, major refactors)

---

## Quality Markers

### Positive Examples Demonstrate:

- **Audience-appropriate language** - Matched to target readers
- **Evidence-based claims** - Grounded in actual code/metrics
- **Template structure** - Follows format guidelines
- **Voice calibration** - Matched to tech stack
- **Hook quality** - Opens with curiosity, not preamble

### Negative Examples Demonstrate:

- **Gate failures** - What causes content to fail verification
- **Rule violations** - Specific checklist items not met
- **Recovery patterns** - How to fix common mistakes
- **Evaluation alignment** - Direct links to test questions

### Workflow Example Demonstrates:

- **Constraint propagation** - How phase outputs become inputs
- **Gate verification** - What's checked at each transition
- **Process enforcement** - Why skipping phases causes failures
- **Complete reference** - The canonical 5-phase implementation
