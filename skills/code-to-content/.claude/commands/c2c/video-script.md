# /c2c:video-script

Generate a video/screencast script using the mandatory 5-phase process.

**Usage:** `/c2c:video-script [path-to-project]`

---

## Phase 1: Project Analysis

You MUST analyze the codebase before generating content.

Follow the analysis protocol in `references/analysis-prompts.md`:
- Read dependency files and identify core functionality
- Map key user workflows to demonstrate
- Identify visual opportunities (architecture, UI, terminal)

Identify:
- What to demonstrate
- Key moments to capture
- Logical flow of demonstration
- Potential visual elements

**Gate:** Project Brief Generated
- [ ] Demo scope defined
- [ ] Key moments identified
- [ ] Visual opportunities mapped

---

## Phase 2: Audience Declaration

Video audiences:
- **Beginner** — Needs slow pace, full context
- **Intermediate** — Can skip basics, focus on insight
- **Expert** — Deep dive, fast pace acceptable

Declare:
- Target audience
- Video length target
- Voice (typically: conversational, energetic)

**Gate:** Audience Contract Established
- [ ] Audience selected
- [ ] Length target set (typically 5-15 min)

---

## Phase 3: Content Generation

Use template: `assets/templates/video_script.md`

Structure:
1. **Hook** (0:00-0:30) — Why watch this?
2. **Intro** (0:30-1:00) — What you'll learn
3. **Section 1** — First concept/demo
4. **Section 2** — Second concept/demo
5. **Section 3** — Third concept/demo (optional)
6. **Recap** — Key takeaways
7. **Outro** — CTA (subscribe, link, next video)

For each section include:
- Timestamp
- Script (what to say)
- Screen action (what to show)
- B-roll suggestions

**Gate:** Draft Complete with Evidence
- [ ] Hook grabs attention
- [ ] Timestamps logical
- [ ] Screen actions specified

---

## Phase 4: Optimization

Apply:
- Pacing appropriate for audience
- Visual variety (code, diagrams, face)
- Clear transitions between sections
- B-roll list for post-production

**Gate:** Enhancement Applied
- [ ] Pacing checked
- [ ] Visuals planned
- [ ] Transitions smooth

---

## Phase 5: Verification

Run checklist from `references/checklists.md` (Video Script section).

Verify:
- [ ] Script reads naturally aloud
- [ ] Timing realistic for content
- [ ] All demos tested

**Gate:** Delivery Approved
- [ ] Checklist: 100% pass

**DO NOT DELIVER until all checks pass.**
