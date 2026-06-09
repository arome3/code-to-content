# /c2c:conference-talk

Generate a CFP abstract and talk outline using the mandatory 6-phase process.

**Usage:** `/c2c:conference-talk [path-to-project]`

---

## Reference Loading

- `references/differentiation.md` (Phase 2 + Phase 6, always)

Load these references for conference talks:
- `references/phase-gates.md` (always)
- `references/conference-talks.md` (primary reference)
- `references/checklists.md#conference`
- `references/brand-voice.md` (for matching talk voice to project)

---

## Phase 1: Code Analysis

You MUST analyze the codebase before generating content.

Follow the Deep Analysis protocol in `references/analysis-prompts.md`:
- Identify unique approaches or decisions in the code
- Extract concrete metrics and results from git history
- Find the story arc (challenge → discovery → solution)

Identify:
- Unique insight or approach
- Story arc (challenge → discovery → solution)
- Concrete results or learnings
- What makes this talk-worthy

**Gate:** Project Brief Generated
- [ ] Unique angle identified
- [ ] Story arc mapped
- [ ] Concrete outcomes documented

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

Conference audiences:
- **Conference attendees** — Want actionable insights
- **CFP reviewers** — Want clear value proposition

Declare:
- Target conference type (industry, community, academic)
- Technical level expected
- Talk length (typically 20-45 min)

**Gate:** Audience Contract Established
- [ ] Conference type identified
- [ ] Technical level declared
- [ ] Length specified

---

## Phase 4: Content Generation

Generate TWO deliverables:

### 1. CFP Abstract (for submission)

Structure:
- **Title** — Compelling, specific, not clickbait
- **Abstract** (300-500 words):
  - Hook: Why this matters NOW
  - Problem: What challenge you faced
  - Solution: What you discovered
  - Takeaways: What attendees will learn (3 specific items)
- **Outline** — 3-5 main sections
- **Bio** — Speaker credentials relevant to topic

### 2. Talk Outline

Structure:
1. **Opening** (2-3 min) — Hook, establish credibility
2. **Problem** (5-7 min) — Context, why it matters
3. **Journey** (10-15 min) — What you tried, what failed
4. **Solution** (10-15 min) — The insight, the approach
5. **Results** (3-5 min) — Outcomes, metrics
6. **Takeaways** (2-3 min) — 3 actionable lessons
7. **Q&A** (if time) — Anticipated questions

**Gate:** Draft Complete with Evidence
- [ ] Abstract compelling
- [ ] Outline complete
- [ ] Takeaways specific and actionable

---

## Phase 5: Optimization

Apply:
- Title optimization (test alternatives)
- Abstract keywords for searchability
- Outline timing realistic
- Story arc engaging

**Gate:** Enhancement Applied
- [ ] Title compelling
- [ ] Timing realistic
- [ ] Story arc clear

---

## Phase 6: Verification

Also run the **distinctiveness** check from `references/differentiation.md`: the swap-the-name test ("swap in a competitor's name — does it still read fine? then it failed"), the AI-tells blocklist, and record the **Distinctiveness Score (0-5)**. REPORTED, never blocking — if 0-2, surface `AT RISK` and offer Phase 2.

Run checklist from `references/checklists.md` (Conference Talk section).

Verify:
- [ ] Abstract within word limit
- [ ] Takeaways are actionable
- [ ] Bio relevant to topic

**Gate:** Delivery Approved
- [ ] Checklist: 100% pass

**DO NOT DELIVER until all checks pass.**
