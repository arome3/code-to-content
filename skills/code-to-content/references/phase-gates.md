# Phase Gates Reference

This document defines the mandatory verification gates between phases. You MUST pass each gate before proceeding to the next phase. NO exceptions.

---

## Overview

```
Phase 1 ──[Gate 1]──> Phase 2 ──[Gate 2*]──> Phase 3 ──[Gate 3]──> Phase 4 ──[Gate 4]──> Phase 5 ──[Gate 5]──> Phase 6 ──[Gate 6]──> DELIVERY
 Code                Differentiation         Audience &           Content             Optimization        Verification
 Analysis            Discovery               Format               Generation                              & Delivery
```

Each gate is BLOCKING **except Gate 2** (marked `*`), which is a soft forecast — it never stops delivery. If any required item on a blocking gate fails, you MUST:
1. Address the failure
2. Re-verify the gate
3. Only then proceed

---

## Phase 1 Gate: Code Brief Generated

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
- No content-worthy insights found after Claude-native analysis (see `analysis-prompts.md`)
- Project is too small or trivial for meaningful content
- Cannot access the codebase or required files

### Gate Verification
Analysis is Claude-native (read deps, grep for hooks, mine git log) — no scripts required. The legacy helper `legacy/analyze_codebase.py --deep` is optional and opt-in only.

---

## Phase 2 Gate: Differentiation Forecast Set (SOFT — never blocks)

**Verify before proceeding to Phase 3. This gate NEVER stops delivery.**

The founder interview is **always offered, never blocking**. This gate confirms the offer happened and a forecast was recorded — not that the user engaged.

### Required Outputs
- [ ] **Offer made** — the Phase 2 invitation was presented (questions / raw material / ugly-draft / opt-out), regardless of response
- [ ] **Differentiation Brief produced** — WHY, spiky claim, roads-not-taken, founder voice fields filled OR explicitly marked "none captured"
- [ ] **Forecast set** — `ON TRACK` (≥1 of WHY / opinion / roads-not-taken captured) or `AT RISK` (code only)

### NOT a STOP condition
`AT RISK` is permitted. Do **not** block on declined founder input — proceed on code alone and propagate the `AT RISK` flag to Gate 6's Quality Report. See `differentiation.md`.

---

## Phase 3 Gate: Audience Contract Established

**Verify before proceeding to Phase 4:**

### Required Outputs
- [ ] **Single audience selected** — One of: beginner, intermediate, expert, or hiring manager
- [ ] **Format selected** — One specific format (blog, tutorial, thread, README, etc.)
- [ ] **Voice profile declared** — Use the captured **FOUNDER VOICE** (from the Phase 2 Differentiation Brief) as primary. Fall back to the tech-stack table ONLY if no founder voice was captured:
  | Stack | Voice (fallback only) |
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

## Phase 4 Gate: Draft Complete with Evidence

**Verify before proceeding to Phase 5:**

### Required Outputs
- [ ] **Leads with the WHY** — opens on the thesis/stakes, not a feature list
- [ ] **Captured differentiation present** — spiky claim and/or road-not-taken from the Differentiation Brief are in the draft (skip only if the brief marked them "none captured")
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

## Phase 5 Gate: Optimization Applied

**Verify before proceeding to Phase 6:**

### Required Outputs
- [ ] **Voice consistency verified** — Same tone throughout, matching the captured founder voice (including its rejections)
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

## Phase 6 Gate: Delivery Approved

**Verify before delivering to user:**

### Required Outputs (BLOCKING)
- [ ] **Format checklist passed** — 100% of items from `references/checklists.md`
- [ ] **Readability validation passed** — Claude-native estimate against the thresholds below (optional helper: `legacy/analyze_readability.py --validate`)
- [ ] **Evidence verification complete** — All claims verified in Phase 4
- [ ] **No blockers remain** — All STOP conditions resolved

### Reported, NOT blocking
- [ ] **Distinctiveness recorded** — run the swap-the-name test + AI-tells blocklist from `differentiation.md`; record the **Distinctiveness Score (0–5)**, the swap-the-name verdict, and whether founder input was used or declined. A score of 0–2 → surface the `AT RISK` warning prominently and offer to run Phase 2 before publishing. **Never block delivery on this.**

### Readability Thresholds (MUST pass)
| Audience | Max Grade | Max Jargon | Code Ratio |
|----------|-----------|------------|------------|
| Beginner | 8.0 | 2% | 2:1 prose:code |
| Intermediate | 12.0 | 4% | 1:1 |
| Expert | 16.0 | 8% | 0.5:1 |

### STOP Conditions
**DO NOT DELIVER if:**
- Any format checklist item fails
- Readability validation returns FAIL
- Unverified claims remain
- User has not approved final draft (if requested)

**Distinctiveness `AT RISK` is NOT a STOP condition** — warn loudly, deliver anyway.

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
| Gate 1 (Code Brief) | Re-analyze project or request different project |
| Gate 2 (Differentiation) | Soft — never fails; re-offer the interview if user wants more distinctiveness |
| Gate 3 (Audience) | Re-clarify with user |
| Gate 4 (Evidence) | Phase 4 — find evidence or revise claims |
| Gate 5 (Optimization) | Phase 5 — apply missing optimizations |
| Gate 6 (Delivery) | Phase that caused the failure |

---

## Quick Reference Card

```
PHASE 1: CODE ANALYSIS
├── Claude-native: read deps, grep hooks, mine git log
├── Output: Tech stack, 3+ angles, story element
└── Gate: Code Brief Generated

PHASE 2: DIFFERENTIATION DISCOVERY  (offer; never blocks)
├── Offer: questions / raw material / ugly-draft / opt-out
├── Extract: THE WHY · SPIKY CLAIM · ROADS NOT TAKEN · FOUNDER VOICE
└── Gate*: Forecast set (ON TRACK | AT RISK) — soft

PHASE 3: AUDIENCE & FORMAT
├── Select: ONE audience, ONE format
├── Declare: Founder voice (primary) / tech-stack fallback
└── Gate: Audience Contract Established

PHASE 4: CONTENT GENERATION
├── Lead with the WHY; place spiky claim + road-not-taken
├── Use: Format template · Ground: ALL claims in evidence
└── Gate: Draft Complete with Evidence

PHASE 5: OPTIMIZATION
├── Apply: Voice, SEO, cognitive load
├── Add: Visual assets
└── Gate: Enhancement Applied

PHASE 6: VERIFICATION
├── Run: Format checklist · Readability (Claude-native)
├── Report: Swap-the-name test + Distinctiveness Score (0–5)
└── Gate: Blocking checks pass → DELIVER (distinctiveness reported, not gated)
```
