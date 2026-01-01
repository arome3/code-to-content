# Thread Topic

**Core Insight:** We discovered that caching at the wrong layer was making our app slower, not faster.

---

## Context

Added Redis caching to speed up API responses. Standard advice: "Cache your database queries."

We followed the advice. Response times got worse.

---

## The Problem

- Before caching: 45ms avg response
- After naive caching: 52ms avg response (7ms slower!)
- We were paying Redis network overhead for already-fast queries

---

## The Discovery

Our database queries were 5ms. Redis overhead was 3ms per call.

We were caching the wrong thing. The actual bottleneck was a permissions calculation that ran on every request—35ms of pure computation, no database involved.

---

## The Fix

New rule: Only cache operations that take longer than 2× Redis overhead.

For us: only cache things taking >10ms.

---

## Results After Fix

- 45ms → 12ms avg response
- 70% fewer Redis calls
- Cache hit rate: 34% → 91%

Less caching, better performance.

---

## Key Takeaway

"Should I cache this?" is the wrong question.

Better question: "Is this operation expensive enough to justify the caching overhead?"

Profile first. Cache second.
