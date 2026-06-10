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
version: 1.1.0
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

Transform codebases into compelling developer content through a mandatory 6-phase process with verification gates.

**Core premise:** when AI makes competent prose free, grounded-but-generic content gets ignored. The thing that wins is information only the builder knows, written the way only they would write it. This skill's evidence and readability machinery stops content from being *bad*; Phase 2 (Differentiation Discovery) and `references/differentiation.md` stop it from being *generic*. The governing test, applied at delivery: **cover the logo, swap in a competitor's name — if it still reads fine, it failed.**

---

## Specialized Agents

This skill includes 3 specialized agents for parallel execution:

| Agent | Purpose | When to Launch |
|-------|---------|----------------|
| `content-explorer` | Discovers story angles, analyzes codebase for content opportunities | Phase 1: Launch 2-3 in parallel with different focus areas |
| `format-specialist` | Optimizes content for specific platforms and formats | Phase 4-5: Launch per format needed |
| `quality-reviewer` | Validates against checklists, readability thresholds, evidence grounding, distinctiveness | Phase 6: Launch 2-3 in parallel with different review dimensions |

### Parallel Execution Pattern

**Phase 1 - Code Analysis:**
```
Launch 3 content-explorer agents in parallel:
├── Agent 1: "Find performance and optimization story angles"
├── Agent 2: "Find architecture and design decision angles"
└── Agent 3: "Find developer experience and tooling angles"

Consolidate: Merge findings, deduplicate, select top 3-5 angles
```

**Phase 6 - Quality Review:**
```
Launch 4 quality-reviewer agents in parallel:
├── Agent 1: "Review structure and format compliance"
├── Agent 2: "Review readability and audience fit"
├── Agent 3: "Review evidence grounding and technical accuracy"
└── Agent 4: "Review distinctiveness — swap-the-name test + AI-tells blocklist"

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
- `differentiation.md` — Swap-the-name test, the three moves, AI-tells blocklist (required for Phase 2 and Phase 6)
- `readability-guide.md` — Readability validation (required for Phase 6)

**Load On-Demand:**
- `analysis-prompts.md` — Only if running Claude-native analysis (Phase 1)
- `project-analysis.md` — Differentiation Discovery protocol + developer interview (Phase 2)
- `audiences.md` — Only if audience calibration needed (Phase 3)
- `brand-voice.md` — Founder-voice application; tech-stack fallback (Phase 3)
- `cognitive-load.md` — Only if complex content requiring progressive disclosure (Phase 5)
- `diagram-templates.md` — Only if visual assets required (Phase 5)
- `code-snippets.md` — Only if content includes code examples for social sharing
- `conference-talks.md` — Only if generating CFP or talk outline
- `documentation.md` — Only if generating README, API docs, or architecture docs
- `mcp-integration.md` — Only if posting via MCP servers (Delivery)

---

## Mandatory 6-Phase Process

You MUST complete all 6 phases in order. Each phase has a gate that MUST pass before proceeding.

```
PHASE 1 ──[Gate]──> PHASE 2 ──[Gate + Confirm]──> PHASE 3 ──[Gate + Confirm]──> PHASE 4 ──[Gate]──> PHASE 5 ──[Gate]──> PHASE 6 ──[Gate]──> DELIVERY
  Code              Differentiation               Audience &                   Content          Optimization      Verification
  Analysis          Discovery                     Format                       Generation                         & Delivery
```

Phase 2's founder interview is **always offered, never blocking**: if the user declines, proceed on code alone and carry a `Distinctiveness: AT RISK` flag to the Phase 6 report. See `references/phase-gates.md` for detailed gate verification criteria.

---

## User Confirmation Checkpoints

**Phases 2 and 3 require explicit user confirmation before proceeding.**

| After Phase | Present | Wait For |
|-------------|---------|----------|
| 2 | Project Brief + Differentiation Brief (WHY, spiky claim, roads not taken, voice, angles) | "Yes" / "Use angle #" / "Add context" |
| 3 | Audience Contract (audience, format, voice, thresholds) | "Yes" / "Change audience" / "Different format" |

The Phase 2 confirmation is also where the differentiation interview is offered. **Skip confirmations when:** User says "proceed without confirmations", using Quick Mode, or iterating on existing content. (Skipping confirmation does not skip the Phase 2 *offer* — it just doesn't wait; the offer can still be declined.)

---

## Phase 1: Code Analysis

**You MUST complete this phase before any content generation.** This phase mines the codebase for the WHAT — tech stack, architecture, story hooks. The WHY, opinion, and roads-not-taken come from the human in Phase 2.

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

### Phase 1 Output: Project Brief (code-derived half)

```markdown
## Project Brief: [Name]

### Tech Stack
- **Language:** [primary]
- **Framework:** [framework]
- **Architecture:** [pattern]
- **Voice Profile (fallback):** [precise/pragmatic/accessible/direct — replaced by founder voice if Phase 2 captures one]

### Content Angles (3+ Required)
1. [Angle with evidence: file:line or commit]
2. [Angle with evidence]
3. [Angle with evidence]

### Story Hooks
- [Hook 1 with source reference]
- [Hook 2 with source reference]
```

### Phase 1 Gate: Code Brief Generated

You MUST verify before proceeding:
- [ ] Tech stack identified
- [ ] At least 3 content angles discovered
- [ ] Story-worthy element found (commit, pattern, or insight)
- [ ] All angles have evidence citations

**STOP if:** No content-worthy insights found after analysis.

Proceed directly to Phase 2 (no user wait yet — confirmation happens after the Differentiation Brief is assembled).

---

## Phase 2: Differentiation Discovery

**The code told you WHAT. This phase gets the WHY, the opinion, and the roads not taken — the material a competitor could not republish.** Load `references/differentiation.md` and `references/project-analysis.md`.

**This phase always runs. Its founder interview is ALWAYS OFFERED and NEVER BLOCKING.** If the user declines, proceed on code alone and set `Distinctiveness: AT RISK`.

### Required Actions

1. **Make the offer** (one message, three paths + opt-out):
   > "To make this unmistakably yours — something a competitor couldn't republish — I can (a) ask you 4–5 quick questions, (b) take raw material (a Slack thread, support tickets, a 2-minute voice-memo transcript, rough notes), or (c) polish a rough draft you write (write it ugly; I'll keep your voice). Or I can proceed from the code alone. Which do you want?"

2. **Mess over spec** — if raw material is offered, rank it ABOVE the polished README. Rough Slack/tickets/transcripts carry the signal.

3. **Extract the three moves** (see `project-analysis.md` §4 for the full question set):
   - **THE WHY** — the thesis/stakes; the only-you-know insight to lead with
   - **THE SPIKY CLAIM** — one defensible opinion a reader could disagree with
   - **ROADS NOT TAKEN** — what they chose not to build + the trade-off

4. **Capture founder voice as rejections** ("never use semicolons", "never corporate") — this becomes the primary voice in Phase 3, displacing the tech-stack fallback.

### Phase 2 Output: Differentiation Brief

Append to the Project Brief:

```markdown
### Differentiation Brief
- **THE WHY:** [thesis to lead with]
- **THE SPIKY CLAIM:** [defensible opinion — or "none captured"]
- **ROADS NOT TAKEN:** [what they didn't build + trade-off — or "none captured"]
- **FOUNDER VOICE:** sounds like [anchor] · never [rejections] · source: [interview/transcript/draft/NONE]
- **RAW MATERIAL:** [slack/tickets/transcript/notes — or "none"]
- **DISTINCTIVENESS FORECAST:** [ON TRACK | AT RISK]
```

### Phase 2 Gate: Differentiation Forecast Set (soft)

You MUST verify before proceeding:
- [ ] The offer was made (regardless of response)
- [ ] Differentiation Brief produced (fields filled or explicitly "none captured")
- [ ] Forecast set: ON TRACK (≥1 of WHY/opinion/roads captured) or AT RISK (code only)

**This gate never STOPS delivery.** AT RISK is allowed — it just propagates a loud warning to Phase 6. Do not block on missing founder input.

### Phase 2 Confirmation

**Present the combined Project Brief + Differentiation Brief and WAIT for confirmation.**

Display: tech stack, 3+ angles, the WHY, the spiky claim, roads not taken, recommended angle.

Ask: "Proceed with this analysis? [Yes / Use angle # / Add context]"

**DO NOT proceed to Phase 3 until user confirms** (unless confirmations are skipped).

---

## Phase 3: Audience & Format Declaration

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

3. **Declare voice profile.** Use the **FOUNDER VOICE** from the Phase 2 Differentiation Brief as the primary voice. Only if it is `NONE` (offer declined), fall back to the tech-stack heuristic — which is safe but swappable:
   | Stack | Voice (fallback only) |
   |-------|-------|
   | Rust | Precise, safety-conscious |
   | JavaScript/TypeScript | Pragmatic, conversational |
   | Python | Clear, accessible |
   | Go | Direct, minimal |
   | Infrastructure | Operational, cautious |

See `references/audiences.md` for full calibration rules and `references/brand-voice.md` for applying a captured founder voice.

### Phase 3 Gate: Audience Contract Established

You MUST verify before proceeding:
- [ ] Single audience selected (no mixing)
- [ ] Format matches audience complexity
- [ ] Voice profile declared (founder voice if captured, else tech-stack fallback)

**STOP if:** Audience mixing detected or format incompatible.

### Phase 3 Confirmation

**Present the Audience Contract to user and WAIT for confirmation.**

Display:
- Selected audience and what it means (grade level, jargon %)
- Selected format
- Voice profile (and whether it's the founder's or the fallback)

Ask: "Proceed with this targeting? [Yes / Change audience / Different format]"

**DO NOT proceed to Phase 4 until user confirms.**

This is the last confirmation before content generation begins.

---

## Phase 4: Content Generation

**You MUST ground all claims in project evidence — and lead with the Differentiation Brief.**

### Required Actions

1. **Load format template** from `assets/templates/`
2. **Apply format-specific workflow** (see below)
3. **Lead with the WHY**, not the feature list. Place the spiky claim and at least one road-not-taken into the draft using the template's differentiation slots (WHY/thesis lead · YOUR TAKE · ROADS NOT TAKEN). If the Differentiation Brief says `none captured` for these, do not invent them — generate honestly and let Phase 6 flag `AT RISK`.
4. **If a rough founder draft was provided** (write-ugly-first path), polish *it* — preserve their phrasing and order of thought; do not replace the voice.
5. **Ground every claim** in evidence:
   - Code examples from actual codebase
   - Metrics with source citations
   - Commit hashes for historical claims

### Format-Specific Workflows

Each format has a dedicated template in `assets/templates/`:

| Format | Template | Structure |
|--------|----------|-----------|
| Blog Post | `blog_post.md` | WHY/Thesis → Problem → Journey → Roads Not Taken → Solution → Results |
| Tutorial | `tutorial.md` | Prerequisites → Steps (5-9) → Troubleshooting |
| Twitter/X | `twitter_thread.md` | Hook → Context → Insight → CTA |
| README | `readme.md` | Problem → Quick Start → Design Philosophy → Configuration |
| LinkedIn | `linkedin_post.md` | Hook → Story → Takeaways (800-1300 chars) |
| Newsletter | `newsletter.md` | See also `references/newsletters.md` |
| Video Script | `video_script.md` | Hook → Sections → Recap |
| Conference Talk | — | See `references/conference-talks.md` |

Load the appropriate template and follow its structure.

### Phase 4 Gate: Draft Complete with Evidence

You MUST verify before proceeding:
- [ ] All code examples from actual codebase
- [ ] All metrics/claims traceable to source
- [ ] Template structure followed
- [ ] WHY leads (not a feature list); captured spiky claim / roads-not-taken are present if the brief had them

**STOP if:** Claims cannot be traced to evidence.

---

## Phase 5: Optimization

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

### Phase 5 Gate: Enhancement Applied

You MUST verify before proceeding:
- [ ] Voice consistent throughout (and matches the captured founder voice, including its rejections)
- [ ] Cognitive load appropriate for audience
- [ ] Visual assets enhance (not distract)

---

## Phase 6: Verification & Delivery

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
Agent 4: "Review for distinctiveness: run the swap-the-name test and AI-tells blocklist"
```

Consolidate findings, address all Critical and High severity issues before delivery.

### Option B: Inline Validation Protocol

1. **Format Checklist** — Load from `references/checklists.md`. Universal checks: hook, single takeaway, audience depth, voice, code syntax.
2. **Readability** — Use `references/readability-guide.md`. Thresholds: Beginner ≤8.0 grade/2% jargon, Intermediate ≤12.0/4%, Expert ≤16.0/8%.
3. **Evidence** — All claims cite actual files (path:line), commits, or measurements.
4. **Distinctiveness** — Use `references/differentiation.md`. Run the **swap-the-name test**, the **AI-tells blocklist**, and score the **Distinctiveness Score (0–5)**.

### Phase 6 Gate: Delivery Approved

You MUST verify before delivery:
- [ ] Format checklist: 100% blocking items pass
- [ ] Readability validation: PASS for declared audience
- [ ] Evidence verification: ALL claims grounded
- [ ] Voice consistency: Same tone throughout
- [ ] Distinctiveness reported: swap-the-name verdict + score recorded (this is REPORTED, never blocking)

**DO NOT DELIVER until the first four checks pass.** Distinctiveness is reported, not gated — but if the Distinctiveness Score is 0–2, surface the `AT RISK` warning prominently and offer to run Phase 2 before publishing.

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
- **Distinctiveness Score:** [N]/5 [(missing: ...)]
- **Swap-the-name test:** [PASS | AT RISK]
- **Founder input:** [used (source) | declined → AT RISK]

**Verdict:** APPROVED FOR DELIVERY
```

---

## Stop Conditions

**STOP and inform user when:** No insights found (Phase 1), audience unclear or mixed (Phase 3), claims lack evidence (Phase 4), or readability fails (Phase 6). **Do NOT stop** when founder input is declined in Phase 2 — proceed on code alone and flag `AT RISK`.

---

## Constraint Propagation

Each phase output is required input for the next: Code Brief → Differentiation Brief → Audience Contract → Draft → Optimized Content → Verified Deliverable. **You MUST NOT skip phases.**

---

## Reference Files

Load on-demand. **Always load:** `phase-gates.md`, `differentiation.md`, `readability-guide.md`

| Phase | Key References |
|-------|----------------|
| 1 | `analysis-prompts.md` |
| 2 | `differentiation.md`, `project-analysis.md` |
| 3 | `audiences.md`, `brand-voice.md` |
| 4 | `formats.md`, templates in `assets/templates/` |
| 5 | `optimization.md`, `cognitive-load.md`, `diagram-templates.md` |
| 6 | `checklists.md`, `readability-guide.md`, `differentiation.md` |

**Format-specific:** `newsletters.md`, `social-content.md`, `conference-talks.md`, `documentation.md`, `product-launch.md`, `build-in-public.md`, `code-snippets.md`, `code-explainers.md`, `posting-plan.md`, `mcp-integration.md`

---

## Slash Commands

| Mode | Commands | Description |
|------|----------|-------------|
| **Full** | `/c2c:blog`, `/c2c:tutorial`, `/c2c:twitter`, `/c2c:readme`, `/c2c:linkedin`, `/c2c:newsletter`, `/c2c:video-script`, `/c2c:conference-talk`, `/c2c:product-launch` | All 6 phases |
| **Quick** | `/c2c:quick-twitter`, `/c2c:quick-linkedin`, `/c2c:quick-blog`, `/c2c:quick-readme` | Reduced phases for rapid generation |
| **Cascade** | `/c2c:cascade` | Multi-platform repurposing from source |

See `references/commands.md` for full usage details. Commands are in `.claude/commands/c2c/`.

---

## Examples

See `examples/` for input/output demonstrations:
- `blog-post/`, `twitter-thread/`, `readme/` — Positive examples with input and output
- `negative/` — Gate failures with corrections
- `workflow/` — Full 6-phase process

---

## Evaluation

Test skill with `evaluation/evaluation.xml` (18 QA pairs covering template structure, audience thresholds, voice calibration, and quality gates).

---

## Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| Generic / swappable content | No WHY/opinion/roads — Phase 2 skipped or declined | Run Phase 2; apply `differentiation.md` swap-the-name test; lead with the thesis |
| Reads like AI | "We're excited to announce…", "not just X, it's Y", delve/seamless | Run the AI-tells blocklist in `differentiation.md` |
| Confusing tutorial | Multiple actions per step | One action per step with checkpoints |
| Weak blog hook | Starting with background | Open with the WHY/thesis, NEVER "In this article..." |
| Voice mismatch | Used tech-stack fallback when a founder voice existed | Apply captured FOUNDER VOICE from the Differentiation Brief; tech-stack table is fallback only |

---

## Design Principles

1. **Evidence Over Invention** — Every claim traces to actual code, commits, or metrics. NEVER invent. (This is the floor — it stops *bad* content.)
2. **Distinctiveness Over Competence** — Grounded-but-generic loses. Lead with the WHY, hold one defensible opinion, show a road not taken. The swap-the-name test is the ceiling — it stops *generic* content. NEVER block delivery on it; warn instead.
3. **Voice Is a Person** — Capture the founder's actual voice (especially what they reject). The tech-stack table is a fallback, not a target.
4. **Audience-First** — Determine audience in Phase 3. Depth and tone flow from this choice.
5. **Phase Gate Enforcement** — Each gate MUST pass before proceeding (except the soft Phase 2 forecast). NOT optional.
6. **Format Follows Function** — Use the appropriate template and checklist for each format.

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
