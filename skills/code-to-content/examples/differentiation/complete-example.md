# Positive Example: Differentiation Discovery → Output

Shows Phase 2 (Differentiation Discovery) in action and the un-swappable post it produces. Contrast with `examples/negative/generic-swappable-launch.md`, which had the same feature and shipped a 0/5.

---

## Input: Phase 1 Code Brief (the WHAT)

```
PROJECT: queue-lite — a tiny background-job library for Python
CODE FINDINGS:
- Single-file, ~600 LOC, zero dependencies beyond stdlib
- Commit 9c21a0f: "drop the broker, use SQLite as the queue"
- No Redis/RabbitMQ; jobs table in the app's existing SQLite/Postgres
- 3 public functions: enqueue(), worker(), schedule()
```

A code-only post would now write: *"Introducing queue-lite — a simple, powerful background-job library with zero dependencies. We're excited to share it!"* (Swap-the-name: FAIL.)

## Phase 2: Differentiation Discovery (the offer)

> "Your commits show you deleted the message broker and put the queue *in the app's own database*. That's an unusual call — worth making the post about. Want me to ask 3 questions, take a Slack thread, or polish a rough draft?"

User picked **3 questions.** Captured:

```
DIFFERENTIATION BRIEF

THE WHY:
  Every job library starts by telling you to run Redis. For 90% of apps that's a
  second piece of always-on infrastructure to babysit for work the database could
  already do. We think the broker is premature for most teams.

THE SPIKY CLAIM:
  "Reach for Redis/RabbitMQ when you have the scale to justify a broker — not
  before. Most background jobs are low-volume and would be happier as rows in the
  database you already run."

ROADS NOT TAKEN:
  - Considered a Redis backend for parity with Celery. Rejected: it reintroduces the
    exact dependency we're arguing against. We'll add it only when a real user hits
    the throughput ceiling (~thousands of jobs/sec).
  - Considered async workers. Rejected for v1: a polling loop on an indexed table is
    boring, debuggable, and good enough below the ceiling.

FOUNDER VOICE:
  sounds like: dry, confident, a little contrarian; "boring on purpose"
  never: "we're excited to", emoji bullets, "blazing fast"
  source: interview

DISTINCTIVENESS FORECAST: ON TRACK
```

## Output: the post (Distinctiveness 5/5)

```markdown
# Your background jobs don't need Redis yet

Every job library opens the same way: step one, run Redis. So before you've shipped
a single task, you own a second always-on service to monitor, secure, and pay for —
to do work the database you already run could handle.

queue-lite makes the opposite bet. The queue is a table. `enqueue()` inserts a row;
`worker()` polls an indexed column. No broker, no new infrastructure, ~600 lines of
standard-library Python.

## The opinion we're shipping

Reach for a real broker when you have the scale to justify one — not before. Most
apps run low-volume jobs (welcome emails, nightly rollups, the occasional export)
that would be perfectly happy as rows in Postgres. The broker is premature
optimization wearing an ops uniform.

## What we chose not to build

We almost shipped a Redis backend, for Celery parity. We cut it — adding Redis to a
library whose whole argument is "you don't need Redis yet" is incoherent. It goes in
the day a real user hits the throughput ceiling (thousands of jobs/sec), and not a
commit sooner.

We also skipped async workers for v1. A polling loop on an indexed table is boring
and debuggable, and boring is the feature. When the ceiling moves, so will this.

## When you SHOULD reach for the broker

If you're doing thousands of jobs a second, fan-out to many workers, or sub-second
latency — this isn't your tool, and we'll tell you so in the README. queue-lite is
for the 90% who were about to install Redis out of habit.
```

## Why it passes

| Check | Result |
|-------|--------|
| Swap-the-name test | **PASS** — a competitor can't publish "you don't need Redis yet" |
| Move 1: leads with WHY | ✓ the broker is premature for most teams |
| Move 2: defensible opinion | ✓ "the broker is premature optimization wearing an ops uniform" |
| Move 3: road not taken | ✓ rejected Redis backend + async workers, with trade-offs |
| Founder voice | ✓ dry, contrarian, "boring is the feature"; no AI tells |
| **Distinctiveness Score** | **5/5** |

## Related Evaluation Question

> Q: In Phase 2, the user shares that they deliberately rejected a Redis backend to stay dependency-free. Which of the three differentiation moves does that map to, and where should it appear in a blog post?
>
> A: **Move 3 (Roads Not Taken).** It belongs in the template's "Roads Not Taken — what we chose not to build" slot, with the trade-off stated.
