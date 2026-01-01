# /c2c:readme

Generate a comprehensive README using the mandatory 5-phase process.

**Usage:** `/c2c:readme [path-to-project]`

---

## Reference Loading

Load these references for README generation:
- `references/phase-gates.md` (always)
- `references/documentation.md` (primary reference)
- `references/checklists.md#readme`
- `references/diagram-templates.md` (if architecture diagram needed)

---

## Phase 1: Project Analysis

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

## Phase 2: Audience Declaration

READMEs serve multiple audiences. Declare PRIMARY:
- **New users** — Need Quick Start
- **Evaluators** — Need problem/solution framing
- **Contributors** — Need architecture overview

Voice: Match project's tech stack.

**Gate:** Audience Contract Established
- [ ] Primary audience selected
- [ ] Voice profile declared

---

## Phase 3: Content Generation

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

## Phase 4: Optimization

Apply:
- Clear hierarchy (scannable headings)
- Code examples syntax-highlighted
- Architecture diagram (if complex)
- Badges for quick status

**Gate:** Enhancement Applied
- [ ] Scannable structure
- [ ] Visual aids added

---

## Phase 5: Verification

Run checklist from `references/checklists.md` (README section).

Verify:
- [ ] Quick Start works end-to-end
- [ ] All links valid
- [ ] No placeholder text

**Gate:** Delivery Approved
- [ ] Checklist: 100% pass

**DO NOT DELIVER until all checks pass.**
