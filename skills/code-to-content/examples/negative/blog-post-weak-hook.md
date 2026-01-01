# Negative Example: Weak Hook

## Gate Failed

**Phase 5 Gate** — Hook Quality Check

## Rule Violated

From `SKILL.md` → Common Issues → "In this article, I will...":

> Never open with meta-commentary about the article itself. Open with the insight, problem, or hook.

## Failing Content

```markdown
# Building a REST API with FastAPI

In this article, I will explain how we built our REST API using FastAPI.
First, I'll cover the project setup, then I'll discuss the routing structure,
and finally, I'll show you how we handled authentication.

## Introduction

FastAPI is a modern Python framework for building APIs. It's fast and easy to use.
In the following sections, we will explore how to set up a basic API...
```

## Why It Fails

1. **Opens with meta-commentary** — "In this article, I will explain" describes the article, not the insight
2. **Buries the hook** — The interesting part (what problem they solved) never appears
3. **Generic introduction** — "FastAPI is a modern Python framework" adds no value
4. **Passive structure** — "we will explore" delays the payoff

## Corrected Version

```markdown
# How We Cut API Response Time from 2.3s to 180ms

Our checkout API was hemorrhaging users. A 2.3-second response time meant
40% of mobile users abandoned their carts before the spinner stopped.

Three weeks later, we hit 180ms. Here's the FastAPI architecture that got us there.

## The Problem: Database Round-Trips

Every checkout request was making 14 separate database calls...
```

## Why It Passes

1. **Opens with outcome** — The title itself is the hook (specific numbers)
2. **Immediate stakes** — Reader knows why this matters (user abandonment)
3. **Concrete transformation** — 2.3s → 180ms is verifiable
4. **Forward momentum** — "Here's what got us there" promises payoff

## Related Evaluation Question

> Q: A blog post opens with "In this article, I will explain how we built our API." According to SKILL.md's Common Issues section, does this opening pass the hook quality check?
>
> A: **NO**
