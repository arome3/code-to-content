# /c2c:newsletter

Generate a newsletter issue using the mandatory 6-phase process.

**Usage:** `/c2c:newsletter [path-to-project or topic]`

---

## Phase 1: Code Analysis

Gather content sources.

If analyzing a codebase, follow `references/analysis-prompts.md`:
- Extract key updates and changes
- Identify story hooks (TODO, FIXME, interesting commits)
- Find teachable moments or insights

Or gather from provided topics:
- Featured story/update
- Quick hits (3-5 brief items)
- Tool/resource of the week
- Community highlights

**Gate:** Project Brief Generated
- [ ] Featured content identified
- [ ] 3+ quick hits gathered
- [ ] Tool recommendation ready

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

Newsletter audiences:
- **Subscribers** — Opted in, expect value
- **Community members** — Want updates + insights

Declare:
- Newsletter type (see `references/newsletters.md` for 9 types)
- Audience technical level
- Voice (typically: friendly, informative)

**Gate:** Audience Contract Established
- [ ] Newsletter type selected
- [ ] Audience level declared

---

## Phase 4: Content Generation

Use template: `assets/templates/newsletter.md`

Structure:
1. **Subject Line** — Compelling, specific
2. **Intro** — Personal, sets context (2-3 sentences)
3. **Featured** — Main story with depth
4. **Quick Hits** — 3-5 brief items with links
5. **Tool of the Week** — One recommendation
6. **Community** — Highlights, shoutouts
7. **CTA** — What to do next

See `references/newsletters.md` for 9 specialized templates.

**Gate:** Draft Complete with Evidence
- [ ] Subject line compelling
- [ ] Featured story has substance
- [ ] Quick hits are scannable

---

## Phase 5: Optimization

Apply:
- Subject line optimization (test 3 alternatives)
- Scannable formatting (bold key points)
- Clear section breaks
- Mobile-friendly length

**Gate:** Enhancement Applied
- [ ] Subject line tested
- [ ] Formatting scannable

---

## Phase 6: Verification

Also run the **distinctiveness** check from `references/differentiation.md`: the swap-the-name test ("swap in a competitor's name — does it still read fine? then it failed"), the AI-tells blocklist, and record the **Distinctiveness Score (0-5)**. REPORTED, never blocking — if 0-2, surface `AT RISK` and offer Phase 2.

Run checklist from `references/checklists.md` (Newsletter section).

Verify:
- [ ] All links work
- [ ] No placeholder text
- [ ] Appropriate length

**Gate:** Delivery Approved
- [ ] Checklist: 100% pass

**DO NOT DELIVER until all checks pass.**
