# Negative Example: Generic / Swappable Launch

The hardest failure to catch — because it passes every *correctness* gate. Grounded, readable, on-brand, and completely interchangeable with a competitor's announcement.

## Gate Failed

**Phase 6 Gate** — Distinctiveness (swap-the-name test). Note: Phases 4–5 gates PASS (evidence grounded, readability fine). This is why distinctiveness is a separate check.

## Rule Violated

From `references/differentiation.md`:

> Cover the logo. Replace every product name with a competitor's. Does the piece still read fine? If yes, it has failed.

## Failing Content

```markdown
# Introducing Acme Sync 2.0

We're excited to announce Acme Sync 2.0! 🎉

Acme Sync 2.0 isn't just a sync engine — it's a whole new way to keep your
data consistent. With real-time updates, conflict resolution, and a seamless
developer experience, Acme Sync makes building collaborative apps faster than ever.

Here's what's new:
- ⚡ Real-time sync (now 2x faster)
- 🔀 Automatic conflict resolution
- 🛠️ A robust, easy-to-use API

We can't wait for you to try it. Get started today!
```

## Why It Fails

1. **Swap-the-name test: FAIL** — Replace "Acme Sync" with "Replicache" or "Liveblocks" and every sentence still reads fine. Nothing here is *theirs*.
2. **No WHY** — It lists *what* shipped, never *why* it was worth building or what the team believes about sync that competitors don't.
3. **No opinion** — There is no claim a single reader could disagree with. It is wallpaper.
4. **No road not taken** — No trade-off, no rejected approach, no story. AI could (and did) write this from the changelog alone.
5. **AI tells stacked** — "We're excited to announce", "isn't just X — it's a whole new way", "seamless", "robust", "We can't wait for you to try it." Every one is on the blocklist.
6. **Distinctiveness Score: 0/5.**

## Corrected Version

```markdown
# Sync engines lie to you about conflicts. We stopped pretending.

Every sync engine promises "automatic conflict resolution." In practice that
means last-write-wins quietly eating your users' edits — we watched it delete a
customer's 400-row spreadsheet in a demo. So we made a call most teams won't:
Acme Sync 2.0 refuses to auto-resolve a conflict it isn't sure about. It stops
and asks.

That's slower in the happy path. We considered the silent merge everyone else
ships — it demos better and it's one line of code. We didn't build it, because a
sync engine that loses data on the 1% of writes that matter isn't faster, it's
broken.

Here's how the new resolver decides when to stop and ask →
```

## Why It Passes

1. **Swap-the-name test: PASS** — A competitor cannot publish this; it names a belief ("refusing to auto-resolve") they've explicitly rejected.
2. **Leads with the WHY** — the thesis about conflicts, not the feature list.
3. **Has an opinion** — "the silent merge everyone else ships … isn't faster, it's broken." Disagreeable, defensible.
4. **Shows a road not taken** — the one-line silent merge they chose *not* to build, and the trade-off.
5. **No AI tells.** Specific, grounded ("400-row spreadsheet"), opinionated.
6. **Distinctiveness Score: 5/5.**

## Related Evaluation Question

> Q: A launch post is fully evidence-grounded and passes readability, but swapping in a competitor's name leaves it reading identically. Does it pass the Phase 6 gate?
>
> A: The BLOCKING checks pass, but **Distinctiveness is AT RISK (score 0–2)** and must be surfaced prominently. Delivery is not blocked, but the user is warned and offered Phase 2.
