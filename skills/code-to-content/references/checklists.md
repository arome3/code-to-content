# Content Verification Checklists

Pre-delivery verification steps. You MUST run these checks before delivering content.

---

## Phase Gate Verification [BLOCKING]

**You MUST verify each phase gate before proceeding. These checks are BLOCKING.**

### Phase 1 Gate: Code Brief Generated
```
[BLOCKING] Tech stack identified
[BLOCKING] At least 3 content angles discovered
[BLOCKING] Story-worthy element found (commit, pattern, or insight)

STOP CONDITION: No content-worthy insights after analysis
→ Action: Request different project or narrow scope
```

### Phase 2 Gate: Differentiation Forecast Set (SOFT — never blocks)
```
[ ] Offer made (questions / raw material / ugly-draft / opt-out)
[ ] Differentiation Brief produced (fields filled OR "none captured")
[ ] Forecast set: ON TRACK or AT RISK

NOT A STOP CONDITION: AT RISK (declined founder input) is allowed.
→ Action: Proceed on code alone; carry AT RISK flag to Phase 6 report.
```

### Phase 3 Gate: Audience Contract Established
```
[BLOCKING] Single audience selected (beginner/intermediate/expert)
[BLOCKING] Format matches audience complexity
[BLOCKING] Voice profile declared (founder voice primary; tech-stack fallback)

STOP CONDITION: Audience mixing detected
→ Action: Request single audience from user
```

### Phase 4 Gate: Draft Complete with Evidence
```
[BLOCKING] Leads with the WHY, not a feature list
[BLOCKING] Captured spiky claim / road-not-taken present (unless brief said "none captured")
[BLOCKING] All code examples from actual codebase
[BLOCKING] All metrics/claims traceable to source
[BLOCKING] Template structure followed

STOP CONDITION: Claims cannot be traced to evidence
→ Action: Remove claim or find supporting evidence
```

### Phase 5 Gate: Enhancement Applied
```
[BLOCKING] Voice consistent throughout (matches captured founder voice + rejections)
[BLOCKING] Cognitive load appropriate for declared audience
[ ] SEO applied (if web content)
[ ] Visual assets prepared (if applicable)
```

### Phase 6 Gate: Delivery Approved
```
[BLOCKING] Format-specific checklist: 100% BLOCKING items pass
[BLOCKING] Readability validation: PASS
[BLOCKING] Evidence verification: all claims grounded
[REPORTED] Distinctiveness: swap-the-name verdict + score (0–5) recorded — NOT blocking

FINAL CHECK: Claude-native readability estimate vs thresholds (optional: legacy/analyze_readability.py)
→ Expected: PASS
→ If FAIL: Revise content and re-check

DO NOT DELIVER until all [BLOCKING] items pass. Distinctiveness AT RISK → warn loudly, deliver anyway.
```

---

## Readability Thresholds [BLOCKING]

Content MUST pass these thresholds for the declared audience:

| Audience | Max Grade | Max Jargon | Code Ratio |
|----------|-----------|------------|------------|
| Beginner | 8.0 | 2% | 2:1 prose:code |
| Intermediate | 12.0 | 4% | 1:1 |
| Expert | 16.0 | 8% | 0.5:1 |

**Validation:** Claude-native estimate against the thresholds above. Optional opt-in helper:
```bash
python skills/code-to-content/legacy/analyze_readability.py content.md --audience <type> --validate
```

---

## Universal Pre-Delivery Verification

Run these checks on ALL generated content:

```
CONTENT QUALITY:
[ ] Clear angle/hook exists in first paragraph
[ ] "So what?" question is answered
[ ] Single main idea/takeaway is present
[ ] Depth matches stated audience level
[ ] No unnecessary tangents

STRUCTURE:
[ ] Hook-Journey-Payoff arc is present
[ ] Logical flow from start to finish
[ ] Headers guide reader through content
[ ] Transitions exist between sections

CODE (if applicable):
[ ] All code examples are syntactically correct
[ ] Imports and dependencies are shown
[ ] Comments explain "why" not "what"
[ ] Expected output/result is shown

READABILITY:
[ ] Sentences average <25 words
[ ] Paragraphs contain <5 sentences
[ ] No walls of text
[ ] Technical terms explained on first use

VOICE:
[ ] Consistent tone throughout
[ ] Active voice is used
[ ] No apologetic language
[ ] Formality level matches request

POLISH:
[ ] Spelling and grammar correct
[ ] No placeholder text remains
[ ] No sensitive information exposed
[ ] Content sounds natural when read aloud
```

---

## Distinctiveness Checklist [REPORTED — never blocking]

Run on ALL content. This is the swap-the-name layer; see `references/differentiation.md`. Record results in the Quality Report — do NOT block delivery on them.

```
SWAP-THE-NAME TEST:
[ ] Cover the logo, replace the product name with a competitor's — does it STILL read fine?
    → If yes: FAIL. Content is swappable. Surface AT RISK and offer to run Phase 2.

THE THREE MOVES (≥1 required to clear AT RISK):
[ ] WHY leads — opens on a thesis/stakes, not "We're excited to announce [feature]"
[ ] One defensible OPINION — a claim a reasonable reader could disagree with
[ ] One ROAD NOT TAKEN — something they chose not to build + the trade-off

AI-TELLS SCAN (rewrite every hit):
[ ] No "We're excited / thrilled to announce…"
[ ] No "not just X — it's Y" / "it's not about A, it's about B"
[ ] No "in today's fast-paced / ever-evolving world…"
[ ] No delve / leverage / seamless / robust / tapestry / testament / realm / foster
[ ] No rule-of-three + em-dash hype cadence ("fast, simple, and powerful — built for you")

HEDGE SCAN (opinions only — facts about stability may stay honest):
[ ] No softened thesis ("this might possibly be a slightly better approach for some")
[ ] Conviction intact regardless of version (epistemic vs rhetorical, see brand-voice.md)

VOICE:
[ ] Carries the captured founder voice, not a tech-stack default
[ ] Honors the founder's rejections (words/punctuation/tone they said never to use)

SCORE: ___/5  ·  SWAP-THE-NAME: PASS / AT RISK  ·  FOUNDER INPUT: used / declined
```

---

## Blog Post Checklist

```
TITLE:
[ ] Under 60 characters
[ ] Specific (not generic)
[ ] Benefit or outcome is clear
[ ] Would compel a click

OPENING (first 100 words):
[ ] Hook captures reader immediately
[ ] Leads with the WHY/thesis, not a feature list or "We're excited to announce…"
[ ] Problem or outcome is stated
[ ] No "In this post, I will..." phrasing
[ ] Reader knows what they will learn

BODY:
[ ] H2s and H3s use correct hierarchy
[ ] Code examples progress logically
[ ] Examples appear before abstractions
[ ] Common objections addressed
[ ] Each section earns its place

CLOSING:
[ ] Clear takeaway/action exists
[ ] No "In conclusion..." phrasing
[ ] Door opened for further exploration
[ ] Call to action if appropriate

SEO:
[ ] Meta description (<155 chars)
[ ] Clean URL slug suggested
[ ] Internal link opportunities noted
[ ] Images have descriptive alt text
```

---

## Tutorial Checklist

```
STRUCTURE:
[ ] Learning objective stated upfront
[ ] Prerequisites listed
[ ] End result described
[ ] Steps numbered (5-9 optimal)

EACH STEP:
[ ] One clear action per step
[ ] "Why this step matters" explained
[ ] Complete code shown
[ ] Expected result/output included
[ ] Common errors addressed

CODE:
[ ] Code runs if copy-pasted
[ ] Version numbers specified
[ ] All dependencies documented
[ ] Working final version provided

SCAFFOLDING:
[ ] New concepts introduced one at a time
[ ] Prior knowledge requirements stated
[ ] Difficulty ramps gradually
[ ] Rest points in longer tutorials
[ ] Progress celebrated at milestones

COMPLETENESS:
[ ] No assumed knowledge unexplained
[ ] All tools/setup steps covered
[ ] Troubleshooting section included
[ ] Next steps suggested
[ ] Resources for deeper exploration
```

---

## Twitter Thread Checklist

```
FIRST TWEET:
[ ] Hook is in first line
[ ] Tweet provides standalone value
[ ] Curiosity is created
[ ] Under 280 characters
[ ] No "Thread:" or "1/" prefixes

THREAD STRUCTURE:
[ ] 8-12 tweets total (optimal)
[ ] Each tweet has standalone value
[ ] Logical progression exists
[ ] No tweets that only say "Now..."
[ ] Natural flow between tweets

CONTENT:
[ ] One key insight per tweet
[ ] Concrete examples included
[ ] Code formatted correctly for Twitter
[ ] Jargon minimized

FINAL TWEET:
[ ] Clear summary/takeaway exists
[ ] Call to action included
[ ] Engagement invited
```

---

## LinkedIn Post Checklist

```
HOOK (first 2 lines):
[ ] Attention grabbed immediately
[ ] Reader will click "see more"
[ ] No clickbait tactics
[ ] Professional but interesting tone

STRUCTURE:
[ ] Short paragraphs (1-2 sentences each)
[ ] One idea per paragraph
[ ] White space for readability
[ ] Total length 800-1300 chars optimal

CONTENT:
[ ] Business/career value is clear
[ ] Personal insight included
[ ] Not pure self-promotion
[ ] Actionable advice if applicable
[ ] Story or lesson present

FORMATTING:
[ ] Line breaks for readability
[ ] Emoji usage minimal (if any)
[ ] No hashtag overload
[ ] Links noted for comments

ENGAGEMENT:
[ ] Question or call for discussion
[ ] Content easy to comment on
[ ] Relevant to professional audience
```

---

## README Checklist

```
ESSENTIALS:
[ ] Project name is clear
[ ] One-line description exists
[ ] Problem being solved stated
[ ] Screenshot/demo placement noted

INSTALLATION:
[ ] Prerequisites listed
[ ] Step-by-step commands provided
[ ] Instructions work on fresh machine
[ ] Multiple OS covered if applicable
[ ] Common issues addressed

QUICK START:
[ ] Minimal example provided
[ ] Example is copy-paste ready
[ ] Value shown immediately
[ ] Under 5 minutes to try

DOCUMENTATION:
[ ] API/usage documented
[ ] Configuration options listed
[ ] Environment variables explained
[ ] Links to full docs if extensive

PROJECT INFO:
[ ] Tech stack mentioned
[ ] Architecture overview if complex
[ ] Contributing guidelines if applicable
[ ] License specified

DESIGN PHILOSOPHY (the differentiator — avoids the swappable feature-list README):
[ ] States WHY it exists / what it believes, not just what it does
[ ] "What this deliberately does NOT do" section present (roads not taken + trade-off)
[ ] A reader could not swap in a competing library's name and have it still read fine
```

---

## Conference Talk Checklist

### CFP/Proposal

```
TITLE:
[ ] Clear and intriguing
[ ] Specific benefit or outcome stated
[ ] Works as standalone hook
[ ] Appropriate for target conference

ABSTRACT:
[ ] Problem is stated
[ ] Approach is explained
[ ] What audience learns is clear
[ ] Under word limit
[ ] No jargon without context
```

### Presentation

```
STRUCTURE:
[ ] One Big Idea defined
[ ] 3 main points maximum
[ ] Opening hooks audience
[ ] Closing is memorable
[ ] Timing estimated

SLIDES:
[ ] 1 idea per slide
[ ] Minimal text on slides
[ ] Readable from back of room
[ ] Code size sufficient
[ ] Consistent visual style

CONTENT:
[ ] Examples are relatable
[ ] Complex concepts simplified
[ ] Story arc present
[ ] Audience interaction opportunities noted
```

---

## Newsletter Checklist

```
SUBJECT LINE:
[ ] Specific and intriguing
[ ] Under 50 characters
[ ] No spam trigger words
[ ] Creates urgency or curiosity

OPENING:
[ ] Personal and warm tone
[ ] Context is set
[ ] Quick hook exists
[ ] Mobile-friendly length

CONTENT:
[ ] Value delivered early
[ ] Original insight included
[ ] All links functional
[ ] CTAs are clear
[ ] Appropriate length

CURATION (if applicable):
[ ] Quality over quantity
[ ] Commentary adds value
[ ] Sources credited
[ ] Variety of content types

CLOSING:
[ ] Personal sign-off exists
[ ] Replies encouraged
[ ] Next issue teased if appropriate
```

---

## API Documentation Checklist

```
OVERVIEW:
[ ] What API does is explained
[ ] Authentication documented
[ ] Base URL included
[ ] Rate limits specified if known

EACH ENDPOINT:
[ ] Method and path clear
[ ] All parameters documented
[ ] Request body examples included
[ ] Response examples provided
[ ] Error codes documented

EXAMPLES:
[ ] Multiple language examples
[ ] Examples copy-paste ready
[ ] Examples actually work
[ ] Common use cases covered

QUALITY:
[ ] Consistent formatting
[ ] Content searchable/scannable
[ ] Version number noted
[ ] Changelog if applicable
```

---

## Technical Accuracy Checklist

```
CODE:
[ ] All examples syntactically correct
[ ] Imports and dependencies complete
[ ] Variable names consistent throughout
[ ] Error handling present where needed
[ ] Security best practices followed
[ ] No hardcoded credentials or secrets
[ ] Platform/version compatibility noted

CLAIMS:
[ ] Performance claims qualified
[ ] Statistics sourced/cited
[ ] Version compatibility stated
[ ] Breaking changes noted
[ ] Deprecation warnings included

EXTERNAL REFERENCES:
[ ] Links point to official documentation
[ ] Third-party tool versions specified
[ ] License implications noted if relevant
[ ] Alternative tools acknowledged
[ ] API signatures match current versions
```

---

## Accessibility Checklist

```
CONTENT:
[ ] Language is clear and simple
[ ] Reading level matches audience
[ ] Acronyms and jargon explained
[ ] Instructions don't rely solely on color
[ ] Alternatives for time-sensitive content

IMAGES:
[ ] All images have alt text suggestions
[ ] Alt text is descriptive (not "image")
[ ] Decorative images marked appropriately
[ ] Long descriptions for complex images
[ ] Text alternative for text in images

CODE:
[ ] Code blocks have language specified
[ ] Syntax highlighting not sole indicator
[ ] Code described in surrounding text

STRUCTURE:
[ ] Headings create logical outline
[ ] Links have descriptive text (not "click here")
[ ] Tables have proper headers
[ ] Lists used for list content
```

---

## SEO Checklist

```
KEYWORDS:
[ ] Primary keyword in title (front-loaded)
[ ] Primary keyword in H1
[ ] Primary keyword in first 100 words
[ ] Secondary keywords in subheadings
[ ] Keyword suggested for URL slug
[ ] Natural keyword density (not stuffed)

META INFORMATION:
[ ] Meta title under 60 characters
[ ] Meta description under 155 characters
[ ] Meta description includes keyword
[ ] Call to action in meta description
[ ] Open Graph tag needs noted
[ ] Twitter card configuration noted

CONTENT STRUCTURE:
[ ] Proper heading hierarchy (H1-H2-H3)
[ ] Table of contents for >1500 words
[ ] FAQ section with question headers
[ ] Lists and tables for scannable info
[ ] Short paragraphs (3-4 sentences max)

LINKING:
[ ] Internal link opportunities (2-5)
[ ] External authoritative sources (1-3)
[ ] Descriptive anchor text (not "click here")
```

---

## Quick Verification Reference

Run these minimum checks on ALL content:

```
EVERY PIECE:
[ ] Clear hook exists
[ ] Single main idea present
[ ] Appropriate for stated audience
[ ] Proofread for errors

EVERY CODE EXAMPLE:
[ ] Syntactically correct
[ ] Minimal and focused
[ ] Comments explain why

EVERY LINK/REFERENCE:
[ ] Accurately described
[ ] Points to real resource

EVERY IMAGE REFERENCE:
[ ] Alt text suggested
[ ] Adds clear value
```

---

Before delivering any content, run through applicable checklists above. Address any failures before presenting content to user. If a check cannot be satisfied, note the limitation explicitly in delivery.
