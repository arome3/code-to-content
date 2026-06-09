# /c2c:twitter

Generate a Twitter/X thread using the mandatory 6-phase process.

**Usage:** `/c2c:twitter [topic or insight]`

---

## Reference Loading

- `references/differentiation.md` (Phase 2 + Phase 6, always)

Load these references for Twitter threads:
- `references/phase-gates.md` (always)
- `references/formats.md#twitter`
- `references/social-content.md`
- `references/checklists.md#twitter`
- `references/code-snippets.md` (if thread includes code)

---

## Phase 1: Code Analysis

Identify ONE key insight worth sharing.

If analyzing a codebase, follow the protocol in `references/analysis-prompts.md`:
- Read dependency files (package.json, requirements.txt, etc.)
- Search for story hooks (TODO, FIXME, interesting commits)
- Identify content angles

Extract:
- Core insight or lesson learned
- Supporting evidence (metrics, code, results)
- Story arc potential

**Gate:** Project Brief Generated
- [ ] ONE insight identified
- [ ] Supporting evidence found
- [ ] Story arc mapped

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

Twitter threads work for:
- **Intermediate** developers (most common)
- **Expert** developers (niche topics)

Declare:
- Target audience
- Assumed context
- Voice (typically: conversational, punchy)

**Gate:** Audience Contract Established
- [ ] Audience selected
- [ ] Voice: conversational

---

## Phase 4: Content Generation

Use template: `assets/templates/twitter_thread.md`

Structure (8-12 tweets):
1. **Hook** — Most important. Creates curiosity. Scroll-stopping.
2. **Context** — Set up the situation
3. **Problem** — What went wrong or challenged you
4. **Discovery** — The turning point
5. **Insight** — The key realization
6. **Solution** — What you did
7. **Results** — Metrics, outcomes
8. **Takeaway + CTA** — Lesson learned + engagement question

Each tweet MUST have standalone value.

**Gate:** Draft Complete with Evidence
- [ ] Hook creates curiosity
- [ ] Each tweet standalone
- [ ] Evidence grounded

---

## Phase 5: Optimization

Apply:
- Hook optimization (test 3 alternatives)
- Visual suggestions (which tweets need images)
- CTA optimization (engagement question)
- Character count verification

### Code Snippet Images

If thread includes code examples, generate shareable images:
- Use `references/code-snippets.md` for Carbon/Ray.so URL generation
- Recommended: dracula or synthwave-84 theme for Twitter
- Dimensions: 1200x675 (16:9)
- Keep code to 10 lines max per image

**Gate:** Enhancement Applied
- [ ] Hook is scroll-stopping
- [ ] Visual placement identified (including code images)
- [ ] CTA drives engagement

---

## Phase 6: Verification

Also run the **distinctiveness** check from `references/differentiation.md`: the swap-the-name test ("swap in a competitor's name — does it still read fine? then it failed"), the AI-tells blocklist, and record the **Distinctiveness Score (0-5)**. REPORTED, never blocking — if 0-2, surface `AT RISK` and offer Phase 2.

Run checklist from `references/checklists.md` (Twitter Thread section).

Verify:
- [ ] Each tweet < 280 characters
- [ ] Hook is compelling
- [ ] CTA is clear

**Gate:** Delivery Approved
- [ ] Checklist: 100% pass

**DO NOT DELIVER until all checks pass.**
