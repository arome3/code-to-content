# /c2c:readme

Generate a comprehensive README using the mandatory 6-phase process.

**Usage:** `/c2c:readme [path-to-project]`

---

## Reference Loading

- `references/differentiation.md` (Phase 2 + Phase 6, always)

Load these references for README generation:
- `references/phase-gates.md` (always)
- `references/documentation.md` (primary reference)
- `references/checklists.md#readme`
- `references/diagram-templates.md` (if architecture diagram needed)

---

## Phase 1: Code Analysis

You MUST analyze the codebase before generating content.

Follow the Deep Analysis protocol in `references/analysis-prompts.md`:
- Read dependency files (package.json, requirements.txt, etc.)
- Detect architecture patterns from directory structure
- Identify key files and entry points
- Extract configuration options

Extract:
- What the project does (one sentence)
- Key benefit to users
- Tech stack and dependencies
- Configuration options
- Common issues/errors

**Gate:** Project Brief Generated
- [ ] Core purpose identified
- [ ] Key benefit articulated
- [ ] Dependencies mapped

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

READMEs serve multiple audiences. Declare PRIMARY:
- **New users** — Need Quick Start
- **Evaluators** — Need problem/solution framing
- **Contributors** — Need architecture overview

Voice: Match project's tech stack.

**Gate:** Audience Contract Established
- [ ] Primary audience selected
- [ ] Voice profile declared

---

## Phase 4: Content Generation

Use template: `assets/templates/readme.md`

Structure:
1. **Title + Badges** — Name, version, build status
2. **The Problem** — Pain point being solved
3. **The Solution** — What this project does
4. **Quick Start** — Working example in < 5 minutes
5. **Installation** — Step-by-step setup
6. **Usage** — Common use cases with code
7. **Configuration** — Options table
8. **API Reference** — Key methods/endpoints
9. **Architecture** — How it works (diagram if complex)
10. **Troubleshooting** — Common issues
11. **Contributing** — How to help
12. **License** — Terms

**Gate:** Draft Complete with Evidence
- [ ] Quick Start actually works
- [ ] All code from actual codebase
- [ ] Config options complete

---

## Phase 5: Optimization

Apply:
- Clear hierarchy (scannable headings)
- Code examples syntax-highlighted
- Architecture diagram (if complex)
- Badges for quick status

**Gate:** Enhancement Applied
- [ ] Scannable structure
- [ ] Visual aids added

---

## Phase 6: Verification

Also run the **distinctiveness** check from `references/differentiation.md`: the swap-the-name test ("swap in a competitor's name — does it still read fine? then it failed"), the AI-tells blocklist, and record the **Distinctiveness Score (0-5)**. REPORTED, never blocking — if 0-2, surface `AT RISK` and offer Phase 2.

Run checklist from `references/checklists.md` (README section).

Verify:
- [ ] Quick Start works end-to-end
- [ ] All links valid
- [ ] No placeholder text

**Gate:** Delivery Approved
- [ ] Checklist: 100% pass

**DO NOT DELIVER until all checks pass.**
