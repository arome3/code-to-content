# /c2c:conference-talk

Generate a CFP abstract and talk outline using the mandatory 5-phase process.

**Usage:** `/c2c:conference-talk [path-to-project]`

---

## Reference Loading

Load these references for conference talks:
- `references/phase-gates.md` (always)
- `references/conference-talks.md` (primary reference)
- `references/checklists.md#conference`
- `references/brand-voice.md` (for matching talk voice to project)

---

## Phase 1: Project Analysis

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

## Phase 2: Audience Declaration

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

## Phase 3: Content Generation

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

## Phase 4: Optimization

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

## Phase 5: Verification

Run checklist from `references/checklists.md` (Conference Talk section).

Verify:
- [ ] Abstract within word limit
- [ ] Takeaways are actionable
- [ ] Bio relevant to topic

**Gate:** Delivery Approved
- [ ] Checklist: 100% pass

**DO NOT DELIVER until all checks pass.**
