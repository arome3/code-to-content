# Complete Workflow Example: Blog Post

This document shows the **complete 5-phase workflow** for creating a blog post,
with actual outputs at each phase and gate verification at each transition.

**Scenario:** User requests a blog post about their FastAPI caching implementation.

---

## Phase 1: Codebase Reconnaissance

### Task

Analyze the codebase to understand what exists and identify story-worthy elements.

### Actions Taken

1. Ran `analyze_codebase.py --output json`
2. Examined git history for significant commits
3. Identified patterns and architectural decisions

### Phase 1 Output: Project Brief

```yaml
project_brief:
  name: "fastapi-cache-layer"

  tech_stack:
    primary_language: "Python 3.11"
    framework: "FastAPI 0.104"
    key_dependencies:
      - "Redis 7.2"
      - "Pydantic 2.5"
      - "SQLAlchemy 2.0"

  architecture:
    pattern: "Repository pattern with caching decorator"
    layers:
      - "API routes (routes/)"
      - "Service layer (services/)"
      - "Cache layer (cache/)"
      - "Repository layer (repositories/)"

  story_worthy_elements:
    commits:
      - hash: "a3f7c2d"
        message: "Add Redis caching layer - 73% latency reduction"
        date: "2024-11-15"
        files_changed: 12

      - hash: "b8e4f1a"
        message: "Fix cache stampede with probabilistic early expiration"
        date: "2024-11-18"
        files_changed: 3

      - hash: "c9d2e3f"
        message: "Add cache warming on startup"
        date: "2024-11-20"
        files_changed: 5

    patterns_discovered:
      - "Decorator-based caching (@cached)"
      - "Probabilistic early expiration (stampede prevention)"
      - "Cache warming strategy"

    metrics_found:
      - "p95 latency: 890ms → 145ms (commit a3f7c2d)"
      - "Cache hit rate: 94%"
      - "Database queries reduced: 12,000/min → 720/min"

  content_angles:
    1: "Performance optimization story (before/after)"
    2: "Cache stampede problem and solution"
    3: "Decorator pattern for cross-cutting concerns"
    4: "Production lessons learned"
```

### Gate 1 Verification

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Tech stack identified | ✓ PASS | Python 3.11, FastAPI, Redis, SQLAlchemy |
| At least 3 content angles | ✓ PASS | 4 angles identified |
| Story-worthy element found | ✓ PASS | Commit a3f7c2d with 73% latency reduction |

**Gate 1: PASSED** → Proceed to Phase 2

---

## Phase 2: Audience Lock-In

### Task

Define exactly ONE audience with specific parameters.

### Input

Project brief from Phase 1 (tech stack, content angles, story elements)

### Decision Process

Given the tech stack (FastAPI, Redis, SQLAlchemy) and story (performance optimization):

- **Not beginners:** Requires understanding of async Python, caching concepts
- **Not experts:** The patterns are established, not cutting-edge
- **Best fit:** Intermediate backend developers who know Python but haven't implemented production caching

### Phase 2 Output: Audience Profile

```yaml
audience_profile:
  level: "intermediate"
  role: "Backend developer"

  description: |
    Python developers who have built APIs but haven't implemented
    production caching. They understand async/await, know what Redis
    is, but haven't dealt with cache stampedes or warming strategies.

  assumptions:
    knows:
      - "Python async/await syntax"
      - "Basic FastAPI routing"
      - "What Redis is (conceptually)"
      - "Why caching improves performance"
    does_not_know:
      - "Cache stampede problem"
      - "Probabilistic early expiration"
      - "Cache warming strategies"
      - "Decorator patterns for caching"

  voice_parameters:
    tone: "Pragmatic and direct"
    formality: "Conversational but technical"
    jargon_tolerance: "4% maximum"
    explanation_depth: "Show code, explain why"

  readability_targets:
    flesch_kincaid_grade: "≤ 12.0"
    sentence_length_avg: "≤ 20 words"

  content_angle_selected: "Performance optimization story (angle #1)"

  why_this_angle: |
    The 73% latency reduction is concrete and compelling.
    Intermediate developers want practical results, not theory.
    The before/after structure matches their learning style.
```

### Gate 2 Verification

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Single audience defined | ✓ PASS | "Intermediate backend developers" |
| No audience mixing | ✓ PASS | Clear knows/doesn't-know boundaries |
| Voice parameters set | ✓ PASS | Tone, jargon tolerance, readability targets |
| Content angle selected | ✓ PASS | Angle #1 (performance story) |

**Gate 2: PASSED** → Proceed to Phase 3

---

## Phase 3: Deep-Dive Research

### Task

Gather evidence to support every claim in the upcoming draft.

### Input

- Project brief from Phase 1 (commits, metrics, patterns)
- Audience profile from Phase 2 (what they know, what to explain)

### Actions Taken

1. Extracted code snippets for each pattern
2. Pulled exact metrics from commits
3. Identified the "why" behind each decision

### Phase 3 Output: Evidence Collection

```yaml
evidence_collection:

  claim_1:
    statement: "We reduced p95 latency from 890ms to 145ms"
    evidence:
      type: "commit + metrics"
      commit_hash: "a3f7c2d"
      benchmark_file: "benchmarks/latency_comparison.py"
      methodology: "10,000 requests over 5 minutes using wrk"
    grounded: true

  claim_2:
    statement: "Cache hit rate of 94%"
    evidence:
      type: "monitoring data"
      source: "Redis INFO stats, averaged over 7 days"
      file: "docs/performance_report.md"
    grounded: true

  claim_3:
    statement: "Database queries reduced by 94%"
    evidence:
      type: "calculated"
      before: "12,000 queries/min"
      after: "720 queries/min"
      reduction: "(12000 - 720) / 12000 = 94%"
      source: "PostgreSQL pg_stat_statements"
    grounded: true

  code_snippets:

    snippet_1:
      name: "Cache decorator"
      file: "cache/decorators.py"
      lines: "15-32"
      code: |
        def cached(ttl: int = 300, prefix: str = ""):
            def decorator(func):
                @wraps(func)
                async def wrapper(*args, **kwargs):
                    key = f"{prefix}:{func.__name__}:{hash(args)}"

                    # Check cache first
                    cached_value = await redis.get(key)
                    if cached_value:
                        return json.loads(cached_value)

                    # Cache miss - call function
                    result = await func(*args, **kwargs)
                    await redis.setex(key, ttl, json.dumps(result))
                    return result
                return wrapper
            return decorator
      why_included: "Shows the core pattern, simple enough for intermediates"

    snippet_2:
      name: "Probabilistic early expiration"
      file: "cache/decorators.py"
      lines: "45-58"
      code: |
        def should_refresh_early(ttl_remaining: int, total_ttl: int) -> bool:
            """
            Probabilistically refresh cache before expiration
            to prevent stampede. Uses exponential decay.
            """
            if ttl_remaining > total_ttl * 0.5:
                return False  # More than 50% TTL remaining

            # Probability increases as TTL decreases
            probability = 1 - (ttl_remaining / total_ttl)
            return random.random() < probability
      why_included: "This is the 'aha' moment - solves stampede elegantly"

    snippet_3:
      name: "Cache warming on startup"
      file: "cache/warming.py"
      lines: "10-25"
      code: |
        async def warm_cache_on_startup(app: FastAPI):
            """Pre-populate cache with frequently accessed data."""

            popular_items = await get_popular_item_ids(limit=1000)

            async with asyncio.TaskGroup() as tg:
                for item_id in popular_items:
                    tg.create_task(fetch_and_cache_item(item_id))

            logger.info(f"Warmed cache with {len(popular_items)} items")
      why_included: "Practical pattern they can copy directly"

  narrative_arc:
    hook: "73% latency reduction with three changes"
    problem: "Cache stampede causing periodic latency spikes"
    journey: "Decorator → Early expiration → Warming"
    payoff: "Production-ready caching in 50 lines"
```

### Gate 3 Verification

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Every claim grounded | ✓ PASS | 3/3 claims have commit hashes or data sources |
| Code snippets extracted | ✓ PASS | 3 snippets with file paths and line numbers |
| Narrative arc defined | ✓ PASS | Hook → Problem → Journey → Payoff |

**Gate 3: PASSED** → Proceed to Phase 4

---

## Phase 4: Structured Draft

### Task

Write the full draft using the blog_post.md template.

### Input

- Audience profile from Phase 2 (voice, jargon tolerance)
- Evidence collection from Phase 3 (claims, snippets, arc)

### Template Applied

Using `assets/templates/blog_post.md` structure:
- Hook (curiosity gap)
- Problem (relatable pain)
- Journey (3 key insights)
- Payoff (transformation achieved)

### Phase 4 Output: Full Draft

```markdown
# How We Cut API Response Time from 890ms to 145ms

Our checkout API was losing users. A 890ms p95 latency meant one in twenty
requests took almost a full second—long enough for mobile users to tap
the back button.

Three weeks and 50 lines of code later, we hit 145ms. Here's the caching
architecture that got us there.

## The Problem: Death by a Thousand Queries

Every checkout request was a database massacre:

- Fetch user profile (1 query)
- Fetch cart items (1 query)
- Fetch product details for each item (N queries)
- Fetch shipping options (1 query)
- Fetch tax calculations (1 query)
- Fetch payment methods (1 query)

For a cart with 8 items? That's 14 database round-trips. Every. Single. Request.

PostgreSQL was handling 12,000 queries per minute. Our RDS bill was crying.

## Solution 1: The Caching Decorator

We started with a simple decorator pattern:

```python
def cached(ttl: int = 300, prefix: str = ""):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            key = f"{prefix}:{func.__name__}:{hash(args)}"

            cached_value = await redis.get(key)
            if cached_value:
                return json.loads(cached_value)

            result = await func(*args, **kwargs)
            await redis.setex(key, ttl, json.dumps(result))
            return result
        return wrapper
    return decorator
```

Usage is clean:

```python
@cached(ttl=3600, prefix="products")
async def get_product(product_id: int) -> Product:
    return await db.fetch_product(product_id)
```

This alone dropped our p95 from 890ms to 320ms. Cache hit rate: 94%.

But we had a new problem.

## Solution 2: Defeating the Cache Stampede

Every hour, on the hour, our latency spiked to 2+ seconds.

Why? Cache stampede. When a popular item's cache expired, hundreds of
concurrent requests would all miss the cache simultaneously—and all
hit the database at once.

The fix is elegant: probabilistic early expiration.

```python
def should_refresh_early(ttl_remaining: int, total_ttl: int) -> bool:
    """
    Probabilistically refresh cache before expiration.
    Probability increases as TTL approaches zero.
    """
    if ttl_remaining > total_ttl * 0.5:
        return False

    probability = 1 - (ttl_remaining / total_ttl)
    return random.random() < probability
```

Instead of everyone refreshing at expiration, random requests refresh
*before* expiration. The cache never actually expires for popular items.

Latency spikes: gone.

## Solution 3: Cache Warming

Cold starts still hurt. After a deployment, the first few thousand
requests hit an empty cache.

We added startup warming:

```python
async def warm_cache_on_startup(app: FastAPI):
    popular_items = await get_popular_item_ids(limit=1000)

    async with asyncio.TaskGroup() as tg:
        for item_id in popular_items:
            tg.create_task(fetch_and_cache_item(item_id))

    logger.info(f"Warmed cache with {len(popular_items)} items")
```

Now deploys are invisible to users.

## The Results

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| p50 latency | 320ms | 89ms | -72% |
| p95 latency | 890ms | 145ms | -84% |
| Database queries/min | 12,000 | 720 | -94% |
| Monthly RDS cost | $890 | $340 | -62% |

Three patterns. 50 lines of code. 84% latency reduction.

## Key Takeaways

1. **Start with the decorator pattern.** It's simple, composable, and
   handles 90% of caching needs.

2. **Probabilistic early expiration prevents stampedes.** Don't let
   popular items expire—refresh them randomly before TTL.

3. **Warm your cache on startup.** Cold caches cause cold sweats.

The code is available at `github.com/example/fastapi-cache-layer`.
Commit `a3f7c2d` is where the magic happens.

---

*Benchmarked using wrk: 10,000 requests over 5 minutes against production
traffic patterns. Metrics from PostgreSQL pg_stat_statements and Redis INFO.*
```

### Gate 4 Verification

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Template structure followed | ✓ PASS | Hook → Problem → Journey → Payoff |
| All code snippets from Phase 3 | ✓ PASS | 3/3 snippets included |
| Claims match evidence | ✓ PASS | All metrics traceable to Phase 3 |
| Hook present (not meta) | ✓ PASS | Opens with outcome, not "In this article" |

**Gate 4: PASSED** → Proceed to Phase 5

---

## Phase 5: Quality Gate

### Task

Verify the draft meets all quality thresholds before delivery.

### Input

- Full draft from Phase 4
- Audience profile from Phase 2 (readability targets)

### Quality Checks Performed

#### 1. Readability Analysis

Ran `analyze_readability.py` on the draft:

```
Flesch-Kincaid Grade Level: 9.2
Average Sentence Length: 14.3 words
Passive Voice Percentage: 8%
```

**Target for intermediate audience:** ≤ 12.0 grade level

**Result:** ✓ PASS (9.2 < 12.0)

#### 2. Jargon Density

Identified technical terms:
- "p95 latency" (used 3 times)
- "cache stampede" (used 2 times)
- "TTL" (used 4 times)
- "decorator" (used 3 times)
- "async" (used 2 times)

Total words: ~850
Jargon instances: 28
Jargon density: 3.3%

**Target for intermediate audience:** ≤ 4%

**Result:** ✓ PASS (3.3% < 4%)

#### 3. Hook Quality

Opening line: "Our checkout API was losing users."

- Starts with outcome/problem: ✓
- No "In this article": ✓
- Creates curiosity: ✓

**Result:** ✓ PASS

#### 4. Evidence Grounding

| Claim in Draft | Evidence Source | Grounded? |
|----------------|-----------------|-----------|
| "890ms to 145ms" | Commit a3f7c2d | ✓ |
| "12,000 queries per minute" | pg_stat_statements | ✓ |
| "Cache hit rate: 94%" | Redis INFO stats | ✓ |
| "Monthly RDS cost" | Cost report | ✓ |

**Result:** ✓ PASS (4/4 claims grounded)

#### 5. Template Compliance

| Required Section | Present? |
|------------------|----------|
| Hook | ✓ |
| Problem statement | ✓ |
| Solution/Journey | ✓ |
| Results/Payoff | ✓ |
| Takeaways | ✓ |

**Result:** ✓ PASS

### Gate 5 Verification

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Readability threshold met | ✓ PASS | Grade 9.2 ≤ 12.0 |
| Jargon density acceptable | ✓ PASS | 3.3% ≤ 4% |
| Hook quality verified | ✓ PASS | Opens with outcome |
| All claims grounded | ✓ PASS | 4/4 traceable |
| Template complete | ✓ PASS | All sections present |

**Gate 5: PASSED** → Ready for Delivery

---

## Workflow Summary

```
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 1: Codebase Reconnaissance                                │
│ Output: Project brief (tech stack, commits, content angles)     │
│ Gate: ✓ 3+ angles, ✓ story element found                       │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 2: Audience Lock-In                                       │
│ Input: Project brief                                            │
│ Output: Audience profile (intermediate, 4% jargon, grade ≤12)   │
│ Gate: ✓ Single audience, ✓ voice params set                    │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 3: Deep-Dive Research                                     │
│ Input: Project brief + Audience profile                         │
│ Output: Evidence collection (claims, snippets, arc)             │
│ Gate: ✓ All claims grounded, ✓ code extracted                  │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 4: Structured Draft                                       │
│ Input: Audience profile + Evidence collection                   │
│ Output: Full draft (blog_post.md template)                      │
│ Gate: ✓ Template followed, ✓ hook present                      │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 5: Quality Gate                                           │
│ Input: Full draft + Audience profile                            │
│ Checks: Readability, jargon, hook, evidence, template           │
│ Gate: ✓ All thresholds met                                     │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
                 ┌─────────┐
                 │DELIVERED│
                 └─────────┘
```

---

## Key Observations

### Constraint Propagation in Action

Notice how each phase's output becomes the next phase's input:

1. **Phase 1 → Phase 2:** Tech stack (FastAPI, Redis) informed audience selection
   (not beginners—they wouldn't know async/await)

2. **Phase 2 → Phase 3:** Audience profile (4% jargon max) guided which code
   snippets to include (simple decorator, not the full implementation)

3. **Phase 3 → Phase 4:** Evidence collection structured the narrative
   (3 solutions matching 3 code snippets)

4. **Phase 4 → Phase 5:** Draft checked against Phase 2's readability targets
   (grade 9.2 vs. target ≤12.0)

### Gate Verification Prevents Drift

Without gates, Phase 4 might have:
- Mixed beginner and expert content (Gate 2 prevents)
- Made ungrounded performance claims (Gate 3 prevents)
- Opened with "In this article..." (Gate 5 catches)

### The 5-Phase Process is Non-Negotiable

Skipping phases causes failures:

| Skip | Consequence |
|------|-------------|
| Phase 1 | No story-worthy elements → generic content |
| Phase 2 | Audience mixing → inconsistent jargon levels |
| Phase 3 | Ungrounded claims → credibility loss |
| Phase 4 | No template → missing structure |
| Phase 5 | Quality violations → unprofessional output |

---

## Checklist for This Workflow

```
[✓] Phase 1 completed - Project brief generated
[✓] Gate 1 passed - 3+ angles, story element found
[✓] Phase 2 completed - Audience profile locked
[✓] Gate 2 passed - Single audience, voice params set
[✓] Phase 3 completed - Evidence collected
[✓] Gate 3 passed - All claims grounded
[✓] Phase 4 completed - Draft written
[✓] Gate 4 passed - Template followed, hook present
[✓] Phase 5 completed - Quality verified
[✓] Gate 5 passed - All thresholds met
[✓] DELIVERED
```
