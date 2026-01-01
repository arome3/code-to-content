# /c2c:product-launch

Generate multi-platform launch content using the mandatory 5-phase process.

**Usage:** `/c2c:product-launch [path-to-project]`

---

## Phase 1: Project Analysis

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

## Phase 2: Audience Declaration

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

## Phase 3: Content Generation

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

## Phase 4: Optimization

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

## Phase 5: Verification

Run checklist from `references/checklists.md` (Product Launch section).

Verify:
- [ ] Character limits met per platform
- [ ] No broken links
- [ ] Demo/screenshots ready

**Gate:** Delivery Approved
- [ ] Checklist: 100% pass

**DO NOT DELIVER until all checks pass.**
