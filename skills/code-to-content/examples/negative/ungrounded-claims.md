# Negative Example: Ungrounded Performance Claims

## Gate Failed

**Phase 3 Gate** — Evidence Grounding

## Rule Violated

From `SKILL.md` → Phase 3 (Deep-Dive Research) gate requirement:

> Every claim grounded in evidence (code, commits, metrics)

And from `SKILL.md` → Design Principles → Evidence-Based Claims:

> Every performance claim must trace to: specific commit hashes, benchmark runs, or measurable code changes.

## Failing Content

```markdown
# Optimizing Our GraphQL API

## Performance Improvements

After implementing these optimizations, our API became significantly faster
and more efficient. Users reported much better experiences, and our
infrastructure costs decreased substantially.

### Query Batching

We added query batching, which dramatically improved performance. The
response times were much better after this change.

### Caching Layer

Implementing a caching layer made our API blazingly fast. Database load
dropped considerably, and the overall system became more responsive.

### Results

The optimizations were highly successful. Our API is now one of the
fastest in the industry, handling requests with minimal latency.
```

## Why It Fails

1. **"significantly faster"** — How much faster? No number.
2. **"much better experiences"** — Unmeasurable claim
3. **"dramatically improved"** — Vague intensifier, no data
4. **"blazingly fast"** — Marketing speak, not evidence
5. **"one of the fastest in the industry"** — Unverifiable superlative

## Corrected Version

```markdown
# Optimizing Our GraphQL API

## Performance Improvements

These three changes reduced our p95 latency from 890ms to 145ms
(commit: `a3f7c2d`). Here's what we measured.

### Query Batching

Before: 12 separate database round-trips per request
After: 3 batched queries

Measured impact: 340ms → 95ms average response time
PR: #847 (includes benchmark suite)

### Caching Layer

We added Redis caching for user permission lookups.

- Cache hit rate: 94%
- Database queries reduced: 12,000/min → 720/min
- Monthly RDS cost: $890 → $340

Commit: `b8e4f1a` — "Add Redis caching for permission checks"

### Results

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| p50 latency | 320ms | 89ms | -72% |
| p95 latency | 890ms | 145ms | -84% |
| p99 latency | 2.1s | 380ms | -82% |
| Requests/sec | 450 | 1,200 | +167% |

Benchmark methodology: 10,000 requests over 5 minutes using `wrk`,
measured on production traffic patterns.
```

## Why It Passes

1. **Specific numbers** — 890ms → 145ms, not "significantly faster"
2. **Commit references** — `a3f7c2d`, `b8e4f1a` are verifiable
3. **Methodology stated** — Reader knows how measurements were taken
4. **Before/after tables** — Clear, comparable data
5. **No superlatives** — Facts speak for themselves

## Related Evaluation Question

> Q: A blog post claims "our caching layer made the API 50% faster" but provides no commit hash, benchmark, or measurement methodology. According to SKILL.md's Phase 3 gate, does this claim pass the evidence grounding requirement? Answer YES or NO.
>
> A: **NO**
