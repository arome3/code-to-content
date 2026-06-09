# Differentiation Reference

The skill's other references stop content from being **bad** (ungrounded, unreadable, badly structured). This one stops it from being **generic**.

When AI makes competent prose free, the floor drops to zero and only the ceiling matters. Grounded, readable, on-brand content that *any competitor could have published* gets the same treatment as a grocery-store cupcake: a polite shrug. The job of this reference is to manufacture the one quality AI cannot fake from a codebase alone — **information only the builder knows, written in a way only they could write it.**

Load this in Phase 2 (Differentiation Discovery) and consult its blocklist in Phase 6 (Verification).

---

## The governing principle: the swap-the-name test

> **Cover the logo. Replace every product name with a competitor's. Does the piece still read fine?**
> If yes, it has failed. Delete it and start from what only this builder knows.

This single test sits above every other rule in the skill. A piece can pass evidence grounding, hit its readability target, follow the template, and still fail this — because correctness and distinctiveness are independent axes. Most AI content is the worst quadrant: *correct and swappable.*

| | Swappable | Un-swappable |
|---|---|---|
| **Ungrounded** | Worthless slop | Confident nonsense |
| **Grounded** | **← where this skill used to land** | **← the target** |

Grounding is necessary but not sufficient. The swap-the-name test is what moves a grounded piece from the bottom-right-of-wrong into the top-right-of-right.

---

## The three moves

Every differentiated piece does at least one of these. The strongest do all three. Extract the raw material for them in Phase 2; the templates in `assets/templates/` now have explicit slots for each.

### Move 1 — Lead with the WHY, not the WHAT

Customers have tuned out the "new feature!" drumbeat. A feature list has no forward momentum; a **thesis** does. Open with the strategic claim or stakes that made the work worth doing, and let the feature read as the *consequence* of that claim.

- **Gold standard:** Linear's Agent launch opens with a thesis — *as execution accelerates, the bottleneck in product development shifts from doing to judgment about what to build.* The AI agent is presented as the consequence of that claim, not the headline. (`linear.app/changelog/2026-03-24-introducing-linear-agent`)
- **The test:** *Could anyone with your feature spec and a chatbot have written this?* If yes, you led with the WHAT. The piece must contain an insight or secret only you have — a customer conversation that sparked the build, a belief that changed, a view of where the world is going.

**Extraction prompts (Phase 2):**
- "Why was this worth building *now*? What changes in the world if it works?"
- "What did a customer say, or what did you see, that made this undeniable?"
- "Finish this sentence: *We built this because we believe ___ — and most people don't yet.*"

### Move 2 — Have a spiky, defensible opinion

Good products come from spiky opinions; good writing about them should too. Hedged, committee-softened prose ("this might help in some cases…") is the tell of writing reviewed by four people who each added a caveat. State a position the author would defend in an argument.

- **Gold standard:** HEY launched The Screener — a feature that forces every first-time sender into a holding pen the recipient controls. DHH called it "controversial to mandate internally"; it became the highest-profile feature since launch. You can *disagree* with HEY's take on email, but you cannot mistake it for anyone else's announcement. (`hey.com/features/the-screener/`)
- **The test:** *Could a reasonable, informed reader disagree with the main claim?* If no one could disagree, it isn't an opinion — it's wallpaper.
- **Caveat on AI:** LLMs are excellent at helping you *find* and sharpen an opinion, and terrible at *holding* one — they will validate whatever position you lean toward. Use AI to pressure-test the argument ("what's the strongest case against this?"), never as a source of agreement.

**Extraction prompts (Phase 2):**
- "What do most people in your space get *wrong*, that you've decided to do differently?"
- "What's a sentence in this piece that a competitor would refuse to sign their name to?"
- "If a smart skeptic read this, where would they push back — and why are they wrong?"

### Move 3 — Show what you chose NOT to build

The most underused move in the kit. Walking readers through the hard trade-offs turns a feature into a *story* with real risks and choices, and it is something an AI draft can never invent — because the AI was not in the room when you decided to ship one thing instead of another.

- **Gold standard:** Superhuman's "Blood, Sweat, and Prompts" details the AI features they *rejected* — auto-summaries, prewritten drafts — and exactly why: preemptive features run automatically, cost more, and must clear a far higher quality bar, so they shipped on-demand features first. The rejected roads are the story. (`blog.superhuman.com/how-we-built-superhuman-ai/`)
- **The test:** *Does the piece name at least one credible thing you didn't do, and the trade-off behind it?* "We considered X but chose Y because Z" is worth more than three paragraphs of what Y does.
- **Resist the Steve-Jobs pose.** Descending from the mountaintop to tell customers what they want reads as inhuman. Showing the choices you struggled with — even ones readers might disagree with — reads as a person worth trusting.

**Extraction prompts (Phase 2):**
- "What's the obvious thing a competent team would have built here — and why didn't you?"
- "What did you cut, defer, or deliberately leave to someone else's layer?"
- "What almost shipped but got killed, and what was the deciding factor?"

---

## Process: how to actually get this out of a human and into a draft

Distinctiveness lives in the builder's head, not the codebase. Code analysis (Phase 1) finds the WHAT; these techniques get the WHY/opinion/roads-not-taken. All three are offered in Phase 2 and are **never blocking** — if the user declines, proceed on code alone and flag `Distinctiveness: AT RISK`.

### Mess over spec
Do not ask for a clean summary. Clean inputs produce clean, dead outputs. Ask for the **mess** and rank it *above* polished docs:

```
INPUT PRIORITY (highest signal first):
1. Raw founder material — voice-memo transcript, the Slack thread where the decision was argued,
   the support tickets that sparked the feature, half-formed notes
2. Git history, code, comments (Phase 1 already has these)
3. The polished README / spec  ← lowest signal; everyone's looks the same
```

Concretely, offer: *"Paste the Slack thread, the support tickets, or a transcript of you rambling for two minutes about why this matters. Rough is better than tidy."*

### Use AI to find the argument
Once raw material is in hand, the model's best job is *finding the angle*, not writing the prose. Ask: **"What's the strongest case for why we built this instead of the three other things we could have built?"** Use the answer to choose the WHY and the spiky claim — then write it the way you'd say it to a smart friend, not the way you'd brief a board.

### Write ugly first
The best AI-assisted writing starts with a **terrible human draft** — half-thoughts, run-ons, real conviction — and uses AI to *clean it up*. This is the opposite of the default (clean AI draft → human adds "personality," which reads like a chatbot in a tophat). When the user offers any rough draft or transcript, **preserve their phrasing and order of thought**; edit for clarity, don't replace the voice. Offer this as an explicit Phase 2 path: *"Write it ugly and I'll polish it, keeping your voice."*

---

## AI-tells blocklist (Phase 6 scan)

These phrasings mark text as machine-generated regardless of how grounded it is. Scan the draft and rewrite every hit. None of these is forbidden by grammar — they're forbidden because they're *the tells everyone now recognizes.*

| Tell | Why it reads as AI | Rewrite toward |
|------|--------------------|----------------|
| "We're excited / thrilled to announce…" | The universal feature-update opener; zero information | Open on the thesis or the stakes |
| "Not just X — it's Y" / "It's not about A, it's about B" | The single most overused AI sentence shape | State the one thing it *is* |
| "In today's fast-paced / ever-evolving world…" | Filler throat-clearing | Cut it; start at the first real claim |
| "delve, leverage, seamless, robust, tapestry, testament, realm, foster" | Post-2023 frequency spiked ~10× in AI text | Plain verbs: dig into, use, smooth, sturdy |
| "Whether you're a X or a Y…" | Generic audience-pandering hedge | Name the one reader you're writing for |
| Rule-of-three + em-dash combo ("fast, simple, and powerful — built for you") | The signature AI cadence | Break the rhythm; one concrete claim |
| "revolutionary, game-changing, powerful, cutting-edge" | Unfalsifiable hype | A number or a comparison the reader can check |
| "We can't wait for you to try it!" | Empty enthusiasm CTA | Tell them what to do and what they'll see |

> Note: an em-dash alone is not an AI tell — good writers use them. The tell is the *combination* of vague claim + rule-of-three + em-dash. Judge by specificity, not punctuation.

This blocklist complements the hedge-word and filler-phrase lists in `readability-guide.md`; run both in Phase 6.

---

## Distinctiveness Score (Phase 6 instrument)

Score the draft 0–5. This is a **reported metric and warning, not a hard gate** — content is never blocked on it, but a low score must be surfaced prominently in the Quality Report.

```
+1  Leads with a WHY/thesis, not a feature list (Move 1)
+1  Contains at least one claim a reasonable reader could disagree with (Move 2)
+1  Names at least one road not taken + the trade-off behind it (Move 3)
+1  Carries the builder's actual voice (from Phase 2), not a tech-stack default
+1  Passes the swap-the-name test (a competitor could NOT publish it unchanged)

5/5  → SHIP. Unmistakably theirs.
3–4  → Acceptable. Note the missing move in the Quality Report.
0–2  → Distinctiveness: AT RISK. Warn loudly. Usually means Phase 2 was declined or
        skipped — offer to gather the why/opinion/roads-not-taken before delivery.
```

Report it like this in the Phase 6 Quality Report:

```markdown
- **Distinctiveness Score:** 4/5 (missing: roads not taken)
- **Swap-the-name test:** PASS
- **Founder input:** used (voice-memo transcript + 1 interview answer)
```

---

## Quick reference

```
GOVERNING TEST   Swap the name. Still reads fine? → fail.
MOVE 1           Lead with WHY (thesis), not WHAT (features).
MOVE 2           One spiky, defensible opinion. No committee hedging.
MOVE 3           Show a road not taken + its trade-off.
PROCESS          Mess over spec · AI finds the argument · write ugly first.
PHASE 6          Run the AI-tells blocklist + score 0–5 + report verdict.
NEVER            Block delivery on this. Warn, don't gate.
```

### Sources
- Evan Armstrong, "The Founder's Guide to Blogging," a16z Speedrun (`speedrun.substack.com/p/the-founders-guide-to-blogging`)
- Linear Agent launch (`linear.app/changelog/2026-03-24-introducing-linear-agent`)
- HEY — The Screener (`hey.com/features/the-screener/`)
- Superhuman, "Blood, Sweat, and Prompts" (`blog.superhuman.com/how-we-built-superhuman-ai/`)
- AI-tell frequency study, University of Helsinki, Apr 2025 (via `howtogeek.com`); voice-as-rejection (`artificialcorner.com/p/voice`)
