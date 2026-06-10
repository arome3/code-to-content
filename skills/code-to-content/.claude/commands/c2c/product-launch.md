# /c2c:product-launch

Generate multi-platform launch content using the mandatory 6-phase process.

**Usage:** `/c2c:product-launch [path-to-project]`

---

## Phase 1: Code Analysis

You MUST analyze the codebase before generating content.

Follow the analysis protocol in `references/analysis-prompts.md`:
- Identify core value proposition from README and code
- Extract differentiators from architecture and dependencies
- Find metrics or social proof from git history

Extract:
- What the product does (one sentence)
- Key differentiator (why this, why now)
- Target user and their pain point
- Metrics or social proof (if available)

**Gate:** Project Brief Generated
- [ ] Value proposition clear
- [ ] Differentiator identified
- [ ] Target user defined

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

Launch platforms have different audiences:
- **Product Hunt** — Early adopters, makers
- **Hacker News** — Technical, skeptical, value substance
- **Twitter/X** — Broad tech audience
- **LinkedIn** — Professional network
- **Reddit** — Community-specific, authentic

Declare:
- Primary platform(s)
- Audience technical level
- Voice per platform

**Gate:** Audience Contract Established
- [ ] Platforms selected
- [ ] Voice adapted per platform

---

## Phase 4: Content Generation

See `references/product-launch.md` for full templates.

Generate content for selected platforms:

### Product Hunt
- **Tagline** (60 chars max)
- **Description** (260 chars)
- **First Comment** — Personal story, why you built it
- **Maker's Comment** — Technical details, roadmap

### Hacker News
- **Title** — Descriptive, not clickbait (Show HN: ...)
- **Comment** — Technical details, honest limitations

### Twitter/X Thread
- **Launch tweet** — Announcement + key benefit
- **Thread** — Features, story, demo, CTA

### LinkedIn
- **Launch post** — Professional angle, story

### Blog Post
- **Launch announcement** — Full story, details

**Gate:** Draft Complete with Evidence
- [ ] Each platform content complete
- [ ] Messaging consistent across platforms
- [ ] All claims evidence-based

---

## Phase 5: Optimization

Apply:
- Platform-specific formatting
- Timing strategy (best launch times)
- Visual assets (screenshots, demo GIFs)
- Response templates for comments

**Gate:** Enhancement Applied
- [ ] Platform formatting correct
- [ ] Visuals prepared
- [ ] Response templates ready

---

## Phase 6: Verification

Also run the **distinctiveness** check from `references/differentiation.md`: the swap-the-name test ("swap in a competitor's name — does it still read fine? then it failed"), the AI-tells blocklist, and record the **Distinctiveness Score (0-5)**. REPORTED, never blocking — if 0-2, surface `AT RISK` and offer Phase 2.

Run checklist from `references/checklists.md` (Product Launch section).

Verify:
- [ ] Character limits met per platform
- [ ] No broken links
- [ ] Demo/screenshots ready

**Gate:** Delivery Approved
- [ ] Checklist: 100% pass

**DO NOT DELIVER until all checks pass.**
