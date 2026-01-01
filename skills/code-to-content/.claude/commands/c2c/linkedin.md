# /c2c:linkedin

Generate a LinkedIn post using the mandatory 5-phase process.

**Usage:** `/c2c:linkedin [topic or insight]`

---

## Reference Loading

Load these references for LinkedIn posts:
- `references/phase-gates.md` (always)
- `references/formats.md#linkedin`
- `references/social-content.md`
- `references/checklists.md#linkedin`
- `references/code-snippets.md` (if post includes code)

---

## Phase 1: Project Analysis

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

## Phase 2: Audience Declaration

LinkedIn audiences:
- **Professional network** — Peers, recruiters, industry
- **Typical level:** Intermediate professionals

Voice: Professional but personal, authentic

**Gate:** Audience Contract Established
- [ ] Audience: professional network
- [ ] Voice: authentic, not corporate

---

## Phase 3: Content Generation

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

## Phase 4: Optimization

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

## Phase 5: Verification

Run checklist from `references/checklists.md` (LinkedIn section).

Verify:
- [ ] Character count: 800-1300
- [ ] Hook visible before "see more"
- [ ] Engagement question present

**Gate:** Delivery Approved
- [ ] Checklist: 100% pass

**DO NOT DELIVER until all checks pass.**
