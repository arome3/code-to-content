# /c2c:linkedin

Generate a LinkedIn post using the mandatory 6-phase process.

**Usage:** `/c2c:linkedin [topic or insight]`

---

## Reference Loading

- `references/differentiation.md` (Phase 2 + Phase 6, always)

Load these references for LinkedIn posts:
- `references/phase-gates.md` (always)
- `references/formats.md#linkedin`
- `references/social-content.md`
- `references/checklists.md#linkedin`
- `references/code-snippets.md` (if post includes code)

---

## Phase 1: Code Analysis

Identify the core insight or story:

If from codebase, follow the protocol in `references/analysis-prompts.md`:
- Read dependency files (package.json, requirements.txt, etc.)
- Search for story hooks (TODO, FIXME, interesting commits)
- Identify content angles

Extract:
- ONE key lesson or insight
- Personal angle (your experience)
- Specific details (numbers, names, dates)

**Gate:** Project Brief Generated
- [ ] Core insight identified
- [ ] Personal angle found
- [ ] Specific details gathered

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

LinkedIn audiences:
- **Professional network** — Peers, recruiters, industry
- **Typical level:** Intermediate professionals

Voice: Professional but personal, authentic

**Gate:** Audience Contract Established
- [ ] Audience: professional network
- [ ] Voice: authentic, not corporate

---

## Phase 4: Content Generation

Use template: `assets/templates/linkedin_post.md`

Structure:
1. **Hook** (first 2 lines) — MUST create curiosity
   - These lines appear before "see more"
   - Make them count
2. **Story** (3-4 paragraphs) — Personal narrative
   - Specific situation
   - Challenge faced
   - What you learned
3. **Takeaways** (3 bullets) — Actionable lessons
4. **Engagement question** — Invite responses

Length: 800-1300 characters optimal

**Gate:** Draft Complete with Evidence
- [ ] Hook in first 2 lines
- [ ] Story is personal and specific
- [ ] 3 actionable takeaways

---

## Phase 5: Optimization

Apply:
- Hook optimization (test alternatives)
- Line breaks for readability
- Remove corporate jargon
- Add relevant hashtags (3-5 max)

**Gate:** Enhancement Applied
- [ ] Hook is compelling
- [ ] No corporate speak
- [ ] Hashtags relevant

---

## Phase 6: Verification

Also run the **distinctiveness** check from `references/differentiation.md`: the swap-the-name test ("swap in a competitor's name — does it still read fine? then it failed"), the AI-tells blocklist, and record the **Distinctiveness Score (0-5)**. REPORTED, never blocking — if 0-2, surface `AT RISK` and offer Phase 2.

Run checklist from `references/checklists.md` (LinkedIn section).

Verify:
- [ ] Character count: 800-1300
- [ ] Hook visible before "see more"
- [ ] Engagement question present

**Gate:** Delivery Approved
- [ ] Checklist: 100% pass

**DO NOT DELIVER until all checks pass.**
