# /c2c:blog

Generate a technical blog post using the mandatory 6-phase process with optional agent parallelization.

**Usage:** `/c2c:blog [path-to-project]`

---

## Reference Loading

- `references/differentiation.md` (Phase 2 + Phase 6, always)

Load only these references for blog posts:
- `references/phase-gates.md` (always)
- `references/formats.md#blog`
- `references/brand-voice.md` (voice calibration by tech stack)
- `references/optimization.md#seo`
- `references/optimization.md#storytelling`
- `references/checklists.md#blog`
- `references/readability-guide.md` (Phase 6)
- `references/code-snippets.md` (if post includes code visuals)

---

## Phase 1: Code Analysis

Choose execution mode based on project complexity:

### Option A: Agent-Parallel (Recommended for complex projects)

Launch 2-3 `content-explorer` agents in parallel:

```
Agent 1: "Analyze [project] for performance and optimization blog angles"
Agent 2: "Analyze [project] for architecture decision blog angles"
Agent 3: "Analyze [project] for developer experience blog angles"
```

Consolidate outputs into unified Project Brief.

### Option B: Inline Analysis

Follow the protocol in `references/analysis-prompts.md`:
- Read dependency files (package.json, requirements.txt, etc.)
- Detect architecture patterns from directory structure
- Search for story hooks (TODO, FIXME, interesting commits)
- Run git log for commit insights

Extract:
- Tech stack and key dependencies
- 3+ content angles with evidence citations
- Story-worthy commits from git history

**Gate:** Project Brief Generated
- [ ] Tech stack identified
- [ ] 3+ content angles found with evidence
- [ ] Story-worthy element identified

---

## Phase 2: Differentiation Discovery

Load `references/differentiation.md` and `references/project-analysis.md`. **Always offer this; never block on it.**

Offer the user (one message): "To make this unmistakably yours — something a competitor couldn't republish — I can (a) ask 4–5 quick questions, (b) take raw material (a Slack thread, support tickets, a voice-memo transcript, rough notes), or (c) polish a rough draft you write. Or I proceed from the code alone."

Extract into a **Differentiation Brief** (append to the Project Brief):
- **THE WHY** — the thesis/stakes to lead with, not a feature list
- **THE SPIKY CLAIM** — one defensible opinion a reader could disagree with
- **ROADS NOT TAKEN** — what you chose not to build + the trade-off
- **FOUNDER VOICE** — how they write, captured as rejections (becomes the primary voice in Phase 3)

**Gate (soft — never blocks):** Differentiation Brief produced; forecast set to ON TRACK (>=1 of WHY/opinion/roads captured) or AT RISK (code only). If declined, proceed on code alone and carry `Distinctiveness: AT RISK` to Phase 6.

---

## Phase 3: Audience Declaration

Ask user or infer from context:
- **Who** is this for? (beginner/intermediate/expert)
- **Why** are they creating this? (authority, reach, portfolio)

Declare:
- Target audience (ONE only)
- Voice profile based on tech stack
- Assumed knowledge level

**Gate:** Audience Contract Established
- [ ] Single audience selected
- [ ] Voice profile declared

---

## Phase 4: Content Generation

Use template: `assets/templates/blog_post.md`

Structure:
1. **Hook** — Surprising result, problem, or specific moment
2. **Problem** — Pain point that resonates
3. **Journey** — How you discovered the solution
4. **Solution** — The technical insight with code
5. **Results** — Metrics and outcomes

Ground ALL claims in evidence from Phase 1.

**Gate:** Draft Complete with Evidence
- [ ] All code from actual codebase
- [ ] All metrics traceable to source
- [ ] Template structure followed

---

## Phase 5: Optimization

Optionally launch `format-specialist` agent for blog optimization, or apply inline:

- SEO (keyword in title, first 100 words, subheadings)
- Voice consistency check
- Cognitive load management for audience
- Visual assets (syntax-highlighted code, diagrams)

### Code Snippet Visuals

If blog includes code examples that need hero images or shareable visuals:
- Use `references/code-snippets.md` for Carbon/Ray.so/SVG generation
- Recommended: github-light or one-dark theme (matches most blog themes)
- Generate Carbon URLs for readers to recreate images

**Gate:** Enhancement Applied
- [ ] Voice consistent
- [ ] SEO applied
- [ ] Cognitive load appropriate

---

## Phase 6: Verification

Also run the **distinctiveness** check from `references/differentiation.md`: the swap-the-name test ("swap in a competitor's name — does it still read fine? then it failed"), the AI-tells blocklist, and record the **Distinctiveness Score (0-5)**. REPORTED, never blocking — if 0-2, surface `AT RISK` and offer Phase 2.

Choose execution mode:

### Option A: Agent-Parallel (Recommended for high-stakes content)

Launch `quality-reviewer` agents:
```
Agent 1: "Review blog for structure and SEO compliance"
Agent 2: "Review blog for readability and audience fit"
Agent 3: "Review blog for evidence grounding"
```

Address all Critical and High severity issues.

### Option B: Inline Validation

Run checklist from `references/checklists.md` (Blog Post section).

Validate readability using `references/readability-guide.md`:
- Estimate grade level using Flesch-Kincaid
- Check jargon density against audience threshold
- Verify code:prose ratio

**Gate:** Delivery Approved
- [ ] Checklist: 100% blocking items pass
- [ ] Readability: PASS for declared audience
- [ ] Evidence: All claims grounded

**DO NOT DELIVER until all checks pass.**

---

## Delivery Format

Include with final blog post:

```markdown
## Quality Report
- **Audience:** [audience]
- **Readability Grade:** [grade] / [max]
- **Jargon Density:** [%] / [max %]
- **Evidence Status:** All claims grounded
- **SEO:** Title, meta, keywords applied

**Verdict:** APPROVED FOR DELIVERY
```
