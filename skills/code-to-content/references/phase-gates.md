# Phase Gates Reference

This document defines the mandatory verification gates between phases. You MUST pass each gate before proceeding to the next phase. NO exceptions.

---

## Overview

```
Phase 1 ──[Gate 1]──> Phase 2 ──[Gate 2]──> Phase 3 ──[Gate 3]──> Phase 4 ──[Gate 4]──> Phase 5 ──[Gate 5]──> DELIVERY
```

Each gate is BLOCKING. If any required item fails, you MUST:
1. Address the failure
2. Re-verify the gate
3. Only then proceed

---

## Phase 1 Gate: Project Brief Generated

**Verify before proceeding to Phase 2:**

### Required Outputs
- [ ] **Tech stack identified** — Primary language, frameworks, and key dependencies documented
- [ ] **Content angles discovered** — At least 3 potential story angles identified
- [ ] **Story-worthy element found** — At least one of:
  - Interesting commit (refactor, optimization, pivot)
  - Design pattern or architectural decision
  - TODO/FIXME with narrative potential
  - Performance metric or improvement

### STOP Conditions
**STOP and inform the user if:**
- No content-worthy insights found after running `analyze_codebase.py --deep`
- Project is too small or trivial for meaningful content
- Cannot access the codebase or required files

### Gate Verification Command
```bash
# Run analysis and verify outputs exist
python scripts/analyze_codebase.py /path/to/project --deep
```

---

## Phase 2 Gate: Audience Contract Established

**Verify before proceeding to Phase 3:**

### Required Outputs
- [ ] **Single audience selected** — One of: beginner, intermediate, expert, or hiring manager
- [ ] **Format selected** — One specific format (blog, tutorial, thread, README, etc.)
- [ ] **Voice profile declared** — Based on tech stack:
  | Stack | Voice |
  |-------|-------|
  | Rust | Precise, safety-conscious |
  | JavaScript/TypeScript | Pragmatic, conversational |
  | Python | Clear, accessible |
  | Go | Direct, minimal |
  | Infrastructure | Operational, cautious |
- [ ] **Assumed knowledge documented** — What the audience already knows

### STOP Conditions
**STOP and inform the user if:**
- Audience mixing detected (e.g., "beginners and experts")
- Format doesn't match audience complexity (e.g., expert-level tutorial for beginners)
- Unable to determine audience after asking user

### Audience-Format Compatibility Matrix
| Audience | Compatible Formats |
|----------|-------------------|
| Beginner | Tutorial, README with examples, explainer blog |
| Intermediate | Blog post, detailed tutorial, architecture overview |
| Expert | Deep dive, technical RFC, performance analysis |
| Hiring Manager | README, portfolio piece, case study |

---

## Phase 3 Gate: Draft Complete with Evidence

**Verify before proceeding to Phase 4:**

### Required Outputs
- [ ] **All code examples from actual codebase** — No invented code
- [ ] **All metrics traceable to source** — Every number has a citation
- [ ] **Template structure followed** — Using format from `assets/templates/`
- [ ] **Claims grounded in evidence** — Every technical claim maps to:
  - Git commit hash
  - File path and line number
  - Actual measurement or metric

### Evidence Verification Checklist
For each claim in the draft:
| Claim | Evidence Type | Source Location | Verified |
|-------|--------------|-----------------|----------|
| [claim 1] | [code/metric/commit] | [file:line or hash] | [ ] |
| [claim 2] | ... | ... | [ ] |

### STOP Conditions
**STOP and revise if:**
- Any claim cannot be traced to evidence
- Code examples are invented or hypothetical
- Metrics lack source citations
- Template structure not followed

---

## Phase 4 Gate: Optimization Applied

**Verify before proceeding to Phase 5:**

### Required Outputs
- [ ] **Voice consistency verified** — Same tone throughout
- [ ] **Cognitive load appropriate** — Based on audience:
  | Complexity | Approach |
  |------------|----------|
  | Low (deps < 10) | Single-pass explanation |
  | Medium (deps 10-30) | Concept first, then implementation |
  | High (deps > 30) | Progressive disclosure with checkpoints |
- [ ] **SEO applied** (if blog/web content):
  - [ ] Primary keyword in title
  - [ ] Keyword in first 100 words
  - [ ] Descriptive subheadings
  - [ ] Meta description (if applicable)
- [ ] **Visual assets prepared** (if applicable):
  - [ ] Code blocks syntax highlighted
  - [ ] Diagrams/charts created
  - [ ] Screenshots annotated

### Voice Consistency Check
Read the opening and closing paragraphs aloud. Do they sound like the same author?
- [ ] Yes — proceed
- [ ] No — revise for consistency

---

## Phase 5 Gate: Delivery Approved

**Verify before delivering to user:**

### Required Outputs
- [ ] **Format checklist passed** — 100% of items from `references/checklists.md`
- [ ] **Readability validation passed** — Using:
  ```bash
  python scripts/analyze_readability.py content.md --audience <type> --validate
  ```
- [ ] **Evidence verification complete** — All claims verified in Phase 3
- [ ] **No blockers remain** — All STOP conditions resolved

### Readability Thresholds (MUST pass)
| Audience | Max Grade | Max Jargon | Code Ratio |
|----------|-----------|------------|------------|
| Beginner | 8.0 | 2% | 2:1 prose:code |
| Intermediate | 12.0 | 4% | 1:1 |
| Expert | 16.0 | 8% | 0.5:1 |

### Final Verification Command
```bash
python scripts/analyze_readability.py output.md --audience beginner --validate
# Expected: PASS
```

### STOP Conditions
**DO NOT DELIVER if:**
- Any format checklist item fails
- Readability validation returns FAIL
- Unverified claims remain
- User has not approved final draft (if requested)

---

## Gate Failure Recovery

When a gate fails:

1. **Identify the failure** — Which specific check failed?
2. **Return to appropriate phase** — Fix at the source
3. **Re-run verification** — Don't assume fixes worked
4. **Document the fix** — Note what was changed

### Backtrack Rules
| Failed Gate | Return To |
|-------------|-----------|
| Gate 1 (Project Brief) | Re-analyze project or request different project |
| Gate 2 (Audience) | Re-clarify with user |
| Gate 3 (Evidence) | Phase 3 — find evidence or revise claims |
| Gate 4 (Optimization) | Phase 4 — apply missing optimizations |
| Gate 5 (Delivery) | Phase that caused the failure |

---

## Quick Reference Card

```
PHASE 1: PROJECT ANALYSIS
├── Run: analyze_codebase.py --deep
├── Output: Tech stack, 3+ angles, story element
└── Gate: Project Brief Generated

PHASE 2: AUDIENCE & FORMAT
├── Select: ONE audience, ONE format
├── Declare: Voice profile, assumed knowledge
└── Gate: Audience Contract Established

PHASE 3: CONTENT GENERATION
├── Use: Format template
├── Ground: ALL claims in evidence
└── Gate: Draft Complete with Evidence

PHASE 4: OPTIMIZATION
├── Apply: Voice, SEO, cognitive load
├── Add: Visual assets
└── Gate: Enhancement Applied

PHASE 5: VERIFICATION
├── Run: Format checklist
├── Run: analyze_readability.py --validate
└── Gate: All Checks Pass → DELIVER
```
