# /c2c:newsletter

Generate a newsletter issue using the mandatory 5-phase process.

**Usage:** `/c2c:newsletter [path-to-project or topic]`

---

## Phase 1: Project Analysis

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

## Phase 2: Audience Declaration

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

## Phase 3: Content Generation

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

## Phase 4: Optimization

Apply:
- Subject line optimization (test 3 alternatives)
- Scannable formatting (bold key points)
- Clear section breaks
- Mobile-friendly length

**Gate:** Enhancement Applied
- [ ] Subject line tested
- [ ] Formatting scannable

---

## Phase 5: Verification

Run checklist from `references/checklists.md` (Newsletter section).

Verify:
- [ ] All links work
- [ ] No placeholder text
- [ ] Appropriate length

**Gate:** Delivery Approved
- [ ] Checklist: 100% pass

**DO NOT DELIVER until all checks pass.**
