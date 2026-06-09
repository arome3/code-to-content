# Negative Example: Hedged, No Opinion (Committee Voice)

## Gate Failed

**Phase 6 Gate** — Distinctiveness (the three moves: missing a defensible opinion). Also trips the hedge scan.

## Rule Violated

From `references/differentiation.md` (Move 2) and `references/brand-voice.md` (epistemic vs rhetorical confidence):

> Great writing has a point of view the author is willing to defend. Cheap writing reads like it was reviewed by four people who each added a caveat. Hedge stability claims only — never the thesis.

## Failing Content

```markdown
## Choosing a Caching Strategy

Caching can sometimes be a useful tool for improving performance in certain
situations. There are several approaches you might consider, and the right one
often depends on your specific use case. In-memory caching may potentially offer
benefits, though it could also introduce some trade-offs in certain scenarios.

We generally found that caching was, in many cases, somewhat helpful, although
results may vary. Some teams might prefer a different approach, and that's
perfectly valid too. Ultimately, it's worth considering what works best for you.
```

## Why It Fails

1. **No defensible claim** — Nothing here could be disagreed with, because nothing is actually asserted. "Results may vary" is not a position.
2. **Hedge pile-up** — "can sometimes", "in certain situations", "may potentially", "somewhat", "in many cases", "might prefer". The `readability-guide.md` hedge list and the `differentiation.md` hedge scan both flag this.
3. **Committee tell** — Every sentence is softened as if four reviewers each added a caveat. This is the exact voice the swap-the-name test exists to catch.
4. **Wrong axis hedged** — It hedges the *opinion* (rhetorical), which must stay bold, instead of only hedging genuine *stability* facts (epistemic).
5. **Distinctiveness Score: 1/5** (carries a faint voice at best).

## Corrected Version

```markdown
## Choosing a Caching Strategy

Most teams cache too early and at the wrong layer. We did too — we added Redis in
front of queries that already ran in 5ms and made the whole endpoint slower,
because the 3ms of network hop cost more than the work it "saved."

Our rule now: cache nothing under 2× your cache overhead. For us that's a hard
floor of 10ms. Below it, caching is a tax you pay to feel productive.

Is that too blunt? Maybe for a read-heavy CDN workload. For an app database it's
the rule we'd defend in any review.
```

## Why It Passes

1. **States a position** — "Most teams cache too early and at the wrong layer" is a claim a reasonable engineer could fight about.
2. **Defensible, not reckless** — It concedes the one real exception (CDN workloads) without dissolving the thesis. That's epistemic honesty, not rhetorical hedging.
3. **Grounded specificity** — 5ms / 3ms / 10ms anchor the opinion in fact.
4. **One voice, no committee** — reads like a person who decided something.
5. **Distinctiveness Score: 5/5.**

## Related Evaluation Question

> Q: Per brand-voice.md, should an opinion be softened because the project is v0.x?
>
> A: **NO.** Maturity governs *epistemic* confidence (claims about stability), not *rhetorical* confidence (the thesis/opinion). Hedge "this API may change"; never hedge "most teams cache the wrong layer."
