# /c2c:twitter

Generate a Twitter/X thread using the mandatory 5-phase process.

**Usage:** `/c2c:twitter [topic or insight]`

---

## Reference Loading

Load these references for Twitter threads:
- `references/phase-gates.md` (always)
- `references/formats.md#twitter`
- `references/social-content.md`
- `references/checklists.md#twitter`
- `references/code-snippets.md` (if thread includes code)

---

## Phase 1: Project Analysis

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

## Phase 2: Audience Declaration

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

## Phase 3: Content Generation

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

## Phase 4: Optimization

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

## Phase 5: Verification

Run checklist from `references/checklists.md` (Twitter Thread section).

Verify:
- [ ] Each tweet < 280 characters
- [ ] Hook is compelling
- [ ] CTA is clear

**Gate:** Delivery Approved
- [ ] Checklist: 100% pass

**DO NOT DELIVER until all checks pass.**
