---
name: code-to-content
description: |
  Use when transforming a codebase into developer content. Activates for:
  - Blog posts, tutorials, or technical documentation about code
  - README, changelog, release notes, or API docs generation
  - Twitter/X threads, LinkedIn posts about technical work
  - Conference talk proposals (CFP) or newsletter content
  - Build-in-public updates, progress threads, milestone announcements
  - Product launches on Product Hunt, Hacker News, or social platforms
  - Any request to explain, document, or share a codebase publicly
version: 1.0.1
author: Abraham Onoja
tags: [writing, content, documentation, marketing, devrel, build-in-public]
agents:
  - content-explorer
  - format-specialist
  - quality-reviewer
hooks:
  - validate_content
commands:
  - cascade
---

# Code to Content Skill

Transform codebases into compelling developer content through a mandatory 5-phase process with verification gates.

---

## Specialized Agents

This skill includes 3 specialized agents for parallel execution:

| Agent | Purpose | When to Launch |
|-------|---------|----------------|
| `content-explorer` | Discovers story angles, analyzes codebase for content opportunities | Phase 1: Launch 2-3 in parallel with different focus areas |
| `format-specialist` | Optimizes content for specific platforms and formats | Phase 3-4: Launch per format needed |
| `quality-reviewer` | Validates against checklists, readability thresholds, evidence grounding | Phase 5: Launch 2-3 in parallel with different review dimensions |

### Parallel Execution Pattern

**Phase 1 - Discovery:**
```
Launch 3 content-explorer agents in parallel:
├── Agent 1: "Find performance and optimization story angles"
├── Agent 2: "Find architecture and design decision angles"
└── Agent 3: "Find developer experience and tooling angles"

Consolidate: Merge findings, deduplicate, select top 3-5 angles
```

**Phase 5 - Quality Review:**
```
Launch 3 quality-reviewer agents in parallel:
├── Agent 1: "Review structure and format compliance"
├── Agent 2: "Review readability and audience fit"
└── Agent 3: "Review evidence grounding and technical accuracy"

Consolidate: Merge issues, prioritize by severity, address blocking items
```

---

## Reference Loading Rules (Lazy Loading)

**NEVER load all references at once.** Load only what's needed for the current format:

| Format | Load These References |
|--------|----------------------|
| Blog Post | `formats.md#blog`, `optimization.md#seo`, `optimization.md#storytelling`, `checklists.md#blog`, `code-snippets.md` |
| Tutorial | `formats.md#tutorial`, `cognitive-load.md`, `checklists.md#tutorial` |
| Twitter/X Thread | `formats.md#twitter`, `social-content.md`, `checklists.md#twitter`, `code-snippets.md` |
| LinkedIn Post | `formats.md#linkedin`, `social-content.md`, `checklists.md#linkedin`, `code-snippets.md` |
| README | `documentation.md#readme`, `checklists.md#readme` |
| API Docs | `documentation.md#api`, `checklists.md` |
| Newsletter | `newsletters.md`, `checklists.md#newsletter` |
| Video Script | `formats.md#video`, `checklists.md` |
| Conference Talk | `conference-talks.md`, `checklists.md#conference` |
| Product Launch | `product-launch.md`, `posting-plan.md` |
| Build-in-Public | `build-in-public.md`, `social-content.md` |
| Cascade | `content-cascade.md`, `social-content.md`, `code-snippets.md` |

**Always Load:**
- `phase-gates.md` — Gate verification criteria (required for all phases)
- `readability-guide.md` — Readability validation (required for Phase 5)

**Load On-Demand:**
- `analysis-prompts.md` — Only if running Claude-native analysis (Phase 1)
- `audiences.md` — Only if audience calibration needed (Phase 2)
- `brand-voice.md` — Only if voice calibration by tech stack/maturity needed (Phase 2)
- `cognitive-load.md` — Only if complex content requiring progressive disclosure (Phase 4)
- `diagram-templates.md` — Only if visual assets required (Phase 4)
- `code-snippets.md` — Only if content includes code examples for social sharing
- `conference-talks.md` — Only if generating CFP or talk outline
- `documentation.md` — Only if generating README, API docs, or architecture docs
- `mcp-integration.md` — Only if posting via MCP servers (Delivery)

---

## Mandatory 5-Phase Process

You MUST complete all 5 phases in order. Each phase has a gate that MUST pass before proceeding.

```
PHASE 1 ──[Gate + Confirm]──> PHASE 2 ──[Gate + Confirm]──> PHASE 3 ──[Gate]──> PHASE 4 ──[Gate]──> PHASE 5 ──[Gate]──> DELIVERY
```

See `references/phase-gates.md` for detailed gate verification criteria.

---

## User Confirmation Checkpoints

**Phases 1 and 2 require explicit user confirmation before proceeding.**

| After Phase | Present | Wait For |
|-------------|---------|----------|
| 1 | Project Brief (tech stack, 3+ angles, recommended angle) | "Yes" / "Use angle #" / "Add context" |
| 2 | Audience Contract (audience, format, voice, thresholds) | "Yes" / "Change audience" / "Different format" |

**Skip confirmations when:** User says "proceed without confirmations", using Quick Mode, or iterating on existing content.

---

## Phase 1: Project Analysis

**You MUST complete this phase before any content generation.**

### Execution Options

Choose based on task complexity:

| Option | When to Use | Method |
|--------|-------------|--------|
| **Agent-Parallel** | Complex projects, multiple content types | Launch 2-3 `content-explorer` agents in parallel |
| **Inline Analysis** | Simple projects, single content piece | Follow inline protocol below |

### Option A: Agent-Parallel Execution (Recommended)

Launch multiple `content-explorer` agents with different focus areas:

```
Agent 1: "Analyze [project] for performance and optimization story angles"
Agent 2: "Analyze [project] for architecture and design decision angles"
Agent 3: "Analyze [project] for developer experience and tooling angles"
```

Consolidate agent outputs into unified Project Brief.

### Option B: Inline Analysis Protocol

Follow `references/analysis-prompts.md` for Claude-native analysis:
1. Tech stack detection (read package.json, requirements.txt, etc.)
2. Architecture pattern detection from directory structure
3. Story hook discovery (grep for TODO, FIXME, HACK, etc.)
4. Git history mining for narrative elements
5. Content angle generation (3+ angles with evidence)

### Phase 1 Output: Project Brief

```markdown
## Project Brief: [Name]

### Tech Stack
- **Language:** [primary]
- **Framework:** [framework]
- **Architecture:** [pattern]
- **Voice Profile:** [precise/pragmatic/accessible/direct]

### Content Angles (3+ Required)
1. [Angle with evidence: file:line or commit]
2. [Angle with evidence]
3. [Angle with evidence]

### Story Hooks
- [Hook 1 with source reference]
- [Hook 2 with source reference]
```

### Phase 1 Gate: Project Brief Generated

You MUST verify before proceeding:
- [ ] Tech stack identified
- [ ] At least 3 content angles discovered
- [ ] Story-worthy element found (commit, pattern, or insight)
- [ ] All angles have evidence citations

**STOP if:** No content-worthy insights found after analysis.

### Phase 1 Confirmation

**Present the Project Brief to user and WAIT for confirmation.**

Display:
- Tech stack and voice profile
- 3+ content angles with evidence
- Recommended angle with reasoning

Ask: "Proceed with this analysis? [Yes / Use angle # / Add context]"

**DO NOT proceed to Phase 2 until user confirms.**

---

## Phase 2: Audience & Format Declaration

**You MUST declare audience and format before generating content.**

### Required Actions

1. **Determine target audience** (select ONE):
   | Audience | Assumed Knowledge | Jargon Tolerance |
   |----------|-------------------|------------------|
   | Beginner | Basic programming concepts | 2% max |
   | Intermediate | Language proficiency, common patterns | 4% |
   | Expert | Deep domain knowledge | 8% |
   | Hiring Manager | Technical literacy, not expertise | 2% |

2. **Select content format** (select ONE):
   - Blog post
   - Tutorial
   - Twitter/X thread
   - LinkedIn post
   - README
   - Newsletter
   - Video script
   - Conference talk

3. **Declare voice profile** based on tech stack:
   | Stack | Voice |
   |-------|-------|
   | Rust | Precise, safety-conscious |
   | JavaScript/TypeScript | Pragmatic, conversational |
   | Python | Clear, accessible |
   | Go | Direct, minimal |
   | Infrastructure | Operational, cautious |

See `references/audiences.md` for full calibration rules.

### Phase 2 Gate: Audience Contract Established

You MUST verify before proceeding:
- [ ] Single audience selected (no mixing)
- [ ] Format matches audience complexity
- [ ] Voice profile declared

**STOP if:** Audience mixing detected or format incompatible.

### Phase 2 Confirmation

**Present the Audience Contract to user and WAIT for confirmation.**

Display:
- Selected audience and what it means (grade level, jargon %)
- Selected format
- Voice profile

Ask: "Proceed with this targeting? [Yes / Change audience / Different format]"

**DO NOT proceed to Phase 3 until user confirms.**

This is the last confirmation before content generation begins.

---

## Phase 3: Content Generation

**You MUST ground all claims in project evidence.**

### Required Actions

1. **Load format template** from `assets/templates/`
2. **Apply format-specific workflow** (see below)
3. **Ground every claim** in evidence:
   - Code examples from actual codebase
   - Metrics with source citations
   - Commit hashes for historical claims

### Format-Specific Workflows

Each format has a dedicated template in `assets/templates/`:

| Format | Template | Structure |
|--------|----------|-----------|
| Blog Post | `blog_post.md` | Hook → Problem → Journey → Solution → Results |
| Tutorial | `tutorial.md` | Prerequisites → Steps (5-9) → Troubleshooting |
| Twitter/X | `twitter_thread.md` | Hook → Context → Insight → CTA |
| README | `readme.md` | Problem → Quick Start → Configuration |
| LinkedIn | `linkedin_post.md` | Hook → Story → Takeaways (800-1300 chars) |
| Newsletter | `newsletter.md` | See also `references/newsletters.md` |
| Video Script | `video_script.md` | Hook → Sections → Recap |
| Conference Talk | — | See `references/conference-talks.md` |

Load the appropriate template and follow its structure.

### Phase 3 Gate: Draft Complete with Evidence

You MUST verify before proceeding:
- [ ] All code examples from actual codebase
- [ ] All metrics/claims traceable to source
- [ ] Template structure followed

**STOP if:** Claims cannot be traced to evidence.

---

## Phase 4: Optimization

**You MUST optimize for audience and platform.**

### Required Actions

1. **Verify voice consistency** — Same tone throughout
2. **Apply cognitive load management:**
   | Complexity | Approach |
   |------------|----------|
   | Low (deps < 10) | Single-pass explanation |
   | Medium (deps 10-30) | Concept first, then implementation |
   | High (deps > 30) | Progressive disclosure with checkpoints |

3. **Apply SEO** (for web content):
   - Primary keyword in title
   - Keyword in first 100 words
   - Descriptive subheadings

4. **Prepare visual assets:**
   - Syntax-highlighted code blocks
   - Architecture diagrams (see `references/diagram-templates.md` for Mermaid templates)
   - Screenshots with annotations

See `references/optimization.md` for full optimization rules.

### Phase 4 Gate: Enhancement Applied

You MUST verify before proceeding:
- [ ] Voice consistent throughout
- [ ] Cognitive load appropriate for audience
- [ ] Visual assets enhance (not distract)

---

## Phase 5: Verification & Delivery

**You MUST NOT deliver content that fails verification.**

### Execution Options

| Option | When to Use | Method |
|--------|-------------|--------|
| **Agent-Parallel** | Complex content, high-stakes delivery | Launch 2-3 `quality-reviewer` agents |
| **Inline Validation** | Simple content, quick delivery | Follow inline protocol below |

### Option A: Agent-Parallel Review (Recommended for important content)

Launch multiple `quality-reviewer` agents with different focus areas:

```
Agent 1: "Review for structure and format compliance"
Agent 2: "Review for readability and audience fit"
Agent 3: "Review for evidence grounding and technical accuracy"
```

Consolidate findings, address all Critical and High severity issues before delivery.

### Option B: Inline Validation Protocol

1. **Format Checklist** — Load from `references/checklists.md`. Universal checks: hook, single takeaway, audience depth, voice, code syntax.
2. **Readability** — Use `references/readability-guide.md`. Thresholds: Beginner ≤8.0 grade/2% jargon, Intermediate ≤12.0/4%, Expert ≤16.0/8%.
3. **Evidence** — All claims cite actual files (path:line), commits, or measurements.

### Phase 5 Gate: Delivery Approved

You MUST verify before delivery:
- [ ] Format checklist: 100% blocking items pass
- [ ] Readability validation: PASS for declared audience
- [ ] Evidence verification: ALL claims grounded
- [ ] Voice consistency: Same tone throughout

**DO NOT DELIVER until all checks pass.**

### Delivery Output

Include with final content:
```markdown
## Quality Report

- **Audience:** [declared audience]
- **Format:** [format type]
- **Readability Grade:** [estimated grade] / [max for audience]
- **Jargon Density:** [percentage] / [max for audience]
- **Evidence Status:** All claims grounded
- **Checklist:** [X/X] items passed

**Verdict:** APPROVED FOR DELIVERY
```

---

## Stop Conditions

**STOP and inform user when:** No insights found (Phase 1), audience unclear or mixed (Phase 2), claims lack evidence (Phase 3), or readability fails (Phase 5).

---

## Constraint Propagation

Each phase output is required input for the next: Project Brief → Audience Contract → Draft → Optimized Content → Verified Deliverable. **You MUST NOT skip phases.**

---

## Reference Files

Load on-demand. **Always load:** `phase-gates.md`, `readability-guide.md`

| Phase | Key References |
|-------|----------------|
| 1 | `analysis-prompts.md` |
| 2 | `audiences.md`, `brand-voice.md` |
| 3 | `formats.md`, templates in `assets/templates/` |
| 4 | `optimization.md`, `cognitive-load.md`, `diagram-templates.md` |
| 5 | `checklists.md`, `readability-guide.md` |

**Format-specific:** `newsletters.md`, `social-content.md`, `conference-talks.md`, `documentation.md`, `product-launch.md`, `build-in-public.md`, `code-snippets.md`, `code-explainers.md`, `posting-plan.md`, `mcp-integration.md`

---

## Slash Commands

| Mode | Commands | Description |
|------|----------|-------------|
| **Full** | `/c2c:blog`, `/c2c:tutorial`, `/c2c:twitter`, `/c2c:readme`, `/c2c:linkedin`, `/c2c:newsletter`, `/c2c:video-script`, `/c2c:conference-talk`, `/c2c:product-launch` | All 5 phases |
| **Quick** | `/c2c:quick-twitter`, `/c2c:quick-linkedin`, `/c2c:quick-blog`, `/c2c:quick-readme` | Reduced phases for rapid generation |
| **Cascade** | `/c2c:cascade` | Multi-platform repurposing from source |

See `references/commands.md` for full usage details. Commands are in `.claude/commands/c2c/`.

---

## Examples

See `examples/` for input/output demonstrations:
- `blog-post/`, `twitter-thread/`, `readme/` — Positive examples with input and output
- `negative/` — Gate failures with corrections
- `workflow/` — Full 5-phase process

---

## Evaluation

Test skill with `evaluation/evaluation.xml` (18 QA pairs covering template structure, audience thresholds, voice calibration, and quality gates).

---

## Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| Generic content | Skipped Phase 1 analysis | Use `analysis-prompts.md`, cite actual files/commits |
| Confusing tutorial | Multiple actions per step | One action per step with checkpoints |
| Weak blog hook | Starting with background | Open with result/problem, NEVER "In this article..." |
| Voice mismatch | Skipped Phase 2 calibration | Match voice to tech stack table |

---

## Design Principles

1. **Evidence Over Invention** — Every claim traces to actual code, commits, or metrics. NEVER invent.
2. **Audience-First** — Determine audience in Phase 2. Depth and tone flow from this choice.
3. **Phase Gate Enforcement** — Each gate MUST pass before proceeding. NOT optional.
4. **Format Follows Function** — Use the appropriate template and checklist for each format.

---

## MCP Integration (Optional)

When MCP servers (`twitter-mcp`, `linkedin-mcp`, `buffer-mcp`) are available, this skill can post directly to platforms. See `references/mcp-integration.md` for setup. Without MCP, templates include copy-ready format with character counts.

---

## Automatic Quality Hooks (Optional)

This skill supports automatic content validation via Claude Code hooks.

See `references/hooks-guide.md` for setup and customization.

---

## Requirements

All core analysis is Claude-native with no dependencies. Optional Python 3 for automatic hooks validation.
