# Negative Example: Thread Numbering Prefix

## Gate Failed

**Phase 4 Gate** — Format-Specific Rules

## Rule Violated

From `references/checklists.md` → Twitter/X Thread section:

> [BLOCKING] First tweet must NOT start with "Thread:" or "1/"

## Failing Content

```
Thread: How we reduced our AWS bill by 60% (1/8)

1/ First, let me give you some context about our infrastructure...

2/ We were running 12 t3.large instances across three regions

3/ The problem was our auto-scaling was too aggressive

4/ Here's what we changed:
- Switched to spot instances
- Implemented better caching
- Reduced cross-region calls

5/ The spot instances alone saved us 40%

6/ Caching reduced our database queries by 70%

7/ Cross-region optimization cut another 15% off

8/ Total savings: $4,200/month

Like and retweet if this was helpful!
```

## Why It Fails

1. **"Thread:" prefix** — Explicitly blocked in checklist
2. **"1/" numbering** — Also explicitly blocked
3. **Weak hook** — "Let me give you some context" is meta-commentary
4. **Generic CTA** — "Like and retweet if helpful" is low-value

## Corrected Version

```
We cut our AWS bill from $7,000 to $2,800/month.

No architectural overhaul. No new services. Just three changes we should have made years ago.

Here's exactly what we did:

---

Our setup: 12 t3.large instances across 3 regions.

Sounds reasonable, right?

But our auto-scaling was panic-scaling. Traffic spike? SPIN UP EVERYTHING.

We were paying for capacity we used for 6 minutes a day.

---

Change #1: Spot instances for non-critical workloads.

Our batch processing didn't need guaranteed uptime.

Spot instances = same compute, 60-70% cheaper.

Savings: $1,680/month

---

Change #2: Redis caching layer.

We were hitting Postgres for the same 50 queries. Every. Single. Request.

Added a $50/month Redis instance.

Database queries dropped 70%.

Savings: $890/month

---

Change #3: Consolidated regions.

We had instances in eu-west-1 "just in case."

Our EU traffic? 2% of total.

Killed it. Routed through us-east-1.

Savings: $630/month

---

Total monthly savings: $4,200

Time to implement: 2 days

The lesson?

Audit your infrastructure like you audit your code.

The waste is hiding in plain sight.

---

Want the full breakdown with screenshots?

I wrote up our exact process: [link]

Drop a comment if you want me to cover auto-scaling configs next.
```

## Why It Passes

1. **No prefix** — Opens directly with the hook (the outcome)
2. **Standalone tweets** — Each section works independently
3. **Specific numbers** — $7,000 → $2,800, not "significant savings"
4. **Value-add CTA** — Offers additional resource, asks specific question

## Related Evaluation Question

> Q: A Twitter thread's first tweet begins with "Thread: How we reduced our AWS bill by 60% (1/8)". According to references/checklists.md, does this violate format-specific rules? Answer YES or NO.
>
> A: **YES**
