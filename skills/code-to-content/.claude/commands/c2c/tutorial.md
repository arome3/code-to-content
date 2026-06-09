# /c2c:tutorial

Generate a step-by-step tutorial using the mandatory 6-phase process with optional agent parallelization.

**Usage:** `/c2c:tutorial [path-to-project]`

---

## Reference Loading

- `references/differentiation.md` (Phase 2 + Phase 6, always)

Load only these references for tutorials:
- `references/phase-gates.md` (always)
- `references/formats.md#tutorial`
- `references/cognitive-load.md` (progressive disclosure, chunking)
- `references/checklists.md#tutorial`
- `references/readability-guide.md` (Phase 6)

---

## Phase 1: Code Analysis

Choose execution mode based on project complexity:

### Option A: Agent-Parallel (Recommended)

Launch `content-explorer` agents with tutorial-specific focus:

```
Agent 1: "Analyze [project] for beginner-friendly tutorial opportunities"
Agent 2: "Analyze [project] for common workflows and use cases"
Agent 3: "Identify error patterns and troubleshooting needs in [project]"
```

Consolidate outputs to identify:
- ONE clear learning objective
- Prerequisites and tools
- Common errors users encounter

### Option B: Inline Analysis

Follow the protocol in `references/analysis-prompts.md`:
- Read dependency files (package.json, requirements.txt, etc.)
- Identify common user workflows
- Search for error patterns and edge cases

**Gate:** Project Brief Generated
- [ ] Learning objective defined
- [ ] Prerequisites identified
- [ ] Error patterns found

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

Tutorials are typically for **beginners** or **intermediates**.

Declare:
- Target audience
- Assumed knowledge (what they already know)
- Voice profile (typically: clear, encouraging)

**Gate:** Audience Contract Established
- [ ] Single audience selected
- [ ] Prerequisites match audience level

---

## Phase 4: Content Generation

Use template: `assets/templates/tutorial.md`

Optionally launch `format-specialist` agent: "Optimize tutorial structure for [audience] learning [objective]"

Structure:
1. **Prerequisites** — What's needed before starting
2. **Steps 1-9** — Each step:
   - One action only
   - Code example
   - Explanation
   - Checkpoint (expected output)
3. **Troubleshooting** — Common errors and fixes

**Gate:** Draft Complete with Evidence
- [ ] One action per step
- [ ] All code from actual codebase
- [ ] Checkpoints after each step

---

## Phase 5: Optimization

Apply:
- Progressive disclosure (simple → complex)
- Clear checkpoints after each step
- Troubleshooting for common errors
- Screenshots/diagrams where helpful

**Gate:** Enhancement Applied
- [ ] Complexity progression logical
- [ ] Troubleshooting included

---

## Phase 6: Verification

Also run the **distinctiveness** check from `references/differentiation.md`: the swap-the-name test ("swap in a competitor's name — does it still read fine? then it failed"), the AI-tells blocklist, and record the **Distinctiveness Score (0-5)**. REPORTED, never blocking — if 0-2, surface `AT RISK` and offer Phase 2.

Choose execution mode:

### Option A: Agent-Parallel

Launch `quality-reviewer` agents:
```
Agent 1: "Review tutorial for structure and scaffolding"
Agent 2: "Review tutorial for beginner readability"
Agent 3: "Review tutorial for code correctness and completeness"
```

### Option B: Inline Validation

Run checklist from `references/checklists.md` (Tutorial section).

Validate readability using `references/readability-guide.md`:
- Target grade: ≤8.0 for beginners, ≤12.0 for intermediate
- Define all technical terms for beginners
- Verify one action per step

**Gate:** Delivery Approved
- [ ] Checklist: 100% blocking items pass
- [ ] Readability: PASS for declared audience
- [ ] All code runs if copy-pasted

**DO NOT DELIVER until all checks pass.**

---

## Delivery Format

```markdown
## Quality Report
- **Audience:** [beginner/intermediate]
- **Learning Objective:** [objective]
- **Steps:** [count]
- **Readability Grade:** [grade] / [max]
- **Code Verified:** All examples runnable

**Verdict:** APPROVED FOR DELIVERY
```
