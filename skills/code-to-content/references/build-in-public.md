# Build in Public Guide

This guide transforms the code-to-content skill from a **content creation toolkit** into a **build-in-public system** with narrative continuity, milestone mapping, and audience relationship building.

---

## The Build-in-Public Problem

Individual content pieces are easy. Sustained narrative is hard.

| One-Off Content | Build-in-Public |
|-----------------|-----------------|
| Write a blog post | Tell a story over months |
| Create a Twitter thread | Build audience relationships |
| Publish a README | Maintain consistent voice |
| Announce a feature | Connect updates to a journey |

This guide solves the second column.

---

## Part 1: The Journey Brief

Before creating any content, establish a **persistent context** that carries across all posts.

### Journey Brief Template

```yaml
journey_brief:
  # Core Identity
  project_name: ""
  one_liner: ""  # 10 words max
  why_it_matters: ""  # The problem you're solving

  # Your Story
  origin_story: |
    # Why you started building this
    # What frustrated you / inspired you
    # The moment you decided to build

  current_stage: ""  # idea | building | launched | scaling
  started_date: ""

  # Milestones
  milestones:
    completed:
      - date: ""
        what: ""
        lesson: ""

    upcoming:
      - target_date: ""
        what: ""
        why_share_worthy: ""

  # Voice Consistency
  voice:
    personality: ""  # e.g., "pragmatic optimist", "skeptical engineer"
    recurring_themes: []  # Topics you return to
    phrases_to_use: []  # Signature expressions
    phrases_to_avoid: []  # Things that don't sound like you

  # Audience Relationship
  audience:
    who: ""  # Primary audience
    what_they_care_about: []
    what_they_struggle_with: []
    how_you_help: ""

  # Content History
  previous_posts:
    - date: ""
      type: ""  # blog, twitter, linkedin, etc.
      title: ""
      key_point: ""
      url: ""
```

### Example Journey Brief

```yaml
journey_brief:
  project_name: "FastCache"
  one_liner: "Redis caching for FastAPI in one decorator"
  why_it_matters: "Production caching shouldn't require 200 lines of boilerplate"

  origin_story: |
    I was building my third FastAPI project and copy-pasting the same
    caching code for the third time. 200 lines of Redis connection handling,
    serialization, cache invalidation. Every. Single. Time.

    I thought: "This should be @cached(ttl=300) and done."
    So I built it.

  current_stage: "building"
  started_date: "2024-10-01"

  milestones:
    completed:
      - date: "2024-10-15"
        what: "First working prototype"
        lesson: "Decorators + async = tricky edge cases"

      - date: "2024-11-01"
        what: "Cache stampede fix shipped"
        lesson: "Probabilistic early expiration is elegant"

      - date: "2024-11-15"
        what: "73% latency reduction in production"
        lesson: "The boring optimization wins"

    upcoming:
      - target_date: "2024-12-01"
        what: "Public beta launch"
        why_share_worthy: "First external users, real feedback"

      - target_date: "2024-12-15"
        what: "100 GitHub stars"
        why_share_worthy: "Social proof milestone"

  voice:
    personality: "Pragmatic engineer who's been burned before"
    recurring_themes:
      - "Boring tech wins"
      - "Copy-paste is a code smell"
      - "Production lessons > tutorial examples"
    phrases_to_use:
      - "Here's what actually happened"
      - "The boring truth"
      - "What I wish I'd known"
    phrases_to_avoid:
      - "Game-changer"
      - "Revolutionary"
      - "10x"

  audience:
    who: "Backend developers building APIs"
    what_they_care_about:
      - "Performance without complexity"
      - "Production-ready, not tutorial-ready"
      - "Real metrics, not hype"
    what_they_struggle_with:
      - "Caching feels like black magic"
      - "Too many cache invalidation footguns"
      - "Redis boilerplate everywhere"
    how_you_help: "One decorator, sensible defaults, production patterns included"

  previous_posts:
    - date: "2024-10-20"
      type: "twitter"
      title: "Why I'm building FastCache"
      key_point: "200 lines of boilerplate, every project"
      url: "https://x.com/..."

    - date: "2024-11-05"
      type: "blog"
      title: "How We Solved Cache Stampede"
      key_point: "Probabilistic early expiration"
      url: "https://blog.example.com/..."
```

---

## Part 2: Milestone → Content Mapping

Not every milestone deserves the same content. Use this mapping:

### The Milestone Matrix

| Milestone Type | Primary Content | Secondary Content | Skip |
|----------------|-----------------|-------------------|------|
| **Idea validation** | Twitter thread | LinkedIn post | Blog (too early) |
| **First prototype** | Twitter thread | — | Blog (nothing to teach yet) |
| **Technical breakthrough** | Blog post | Twitter thread | LinkedIn (too technical) |
| **First user/customer** | Twitter thread | LinkedIn | Blog (save for 10 users) |
| **Metrics milestone** | Blog post | Twitter + LinkedIn | — |
| **Public launch** | All formats | Product Hunt | Newsletter |
| **Lesson learned** | Blog post | Twitter thread | LinkedIn (unless professional lesson) |
| **Failure/pivot** | Twitter thread | Blog (if deep) | LinkedIn (too vulnerable) |

### Content Cascade Pattern

For major milestones, cascade content across platforms:

```
Day 0: Twitter thread (immediate, raw)
       └── Captures the moment, authentic reaction

Day 1-3: LinkedIn post (refined, professional)
         └── Same story, business angle

Day 7: Blog post (comprehensive, evergreen)
       └── Full technical details, lessons learned

Day 14: Newsletter (relationship, exclusive)
        └── Behind-the-scenes, what's next
```

---

## Part 3: Cross-Content Continuity

### Referencing Previous Posts

Every post after your first should connect to your journey.

**Pattern: The Callback Open**

```markdown
# Bad (no continuity)
"Today I'm sharing how we implemented caching."

# Good (callbacks to previous post)
"Two weeks ago, I shared that our API was losing users to slow response times.
Today: we fixed it. Here's how."

# Better (callbacks + metrics)
"In October, I posted about our 890ms latency problem.
This week we hit 145ms. Here's the 50 lines of code that got us there."
```

**Pattern: The Journey Anchor**

Start major posts by anchoring to your origin story:

```markdown
"When I started FastCache, I had one goal: never copy-paste Redis
boilerplate again. Three months later, here's what I've learned..."
```

**Pattern: The Series Connector**

For multi-part content:

```markdown
"This is Part 2 of my build-in-public journey with FastCache.
Part 1 covered why I started. Today: the first technical breakthrough."
```

### Maintaining Voice Consistency

Before publishing, check against your journey brief:

```
[ ] Does this sound like my voice personality?
[ ] Did I use my signature phrases naturally?
[ ] Did I avoid my "phrases to avoid"?
[ ] Does this connect to my recurring themes?
[ ] Would my audience recognize this as "me"?
```

---

## Part 4: Content Cadence

### Sustainable Rhythms

| Stage | Recommended Cadence |
|-------|---------------------|
| **Pre-launch** | 1-2 tweets/week, 1 blog/month |
| **Building actively** | 2-3 tweets/week, 2 blogs/month |
| **Post-launch** | 3-4 tweets/week, 1 blog/week |
| **Maintenance mode** | 1 tweet/week, 1 blog/month |

### The Content Calendar Pattern

```
Week 1: Progress update (Twitter)
Week 2: Technical deep-dive (Blog) → excerpt (Twitter) → angle (LinkedIn)
Week 3: Lesson learned (Twitter)
Week 4: Milestone celebration or user story (Twitter + LinkedIn)

Monthly: Newsletter summarizing the month
Quarterly: "State of the project" blog post
```

### Avoiding Burnout

Rules for sustainable build-in-public:

1. **Batch content creation** — Write 2-3 Twitter threads in one session
2. **Repurpose aggressively** — Every blog post = 3 tweets + 1 LinkedIn post
3. **Lower the bar on Twitter** — Not every tweet needs to be profound
4. **Skip weeks, not months** — Consistency > frequency
5. **Automate the boring parts** — Schedule posts, use templates

---

## Part 5: The Build-in-Public Workflow

### Modified Phase 1: Reconnaissance + Journey Context

When creating content, Phase 1 now includes:

```yaml
phase_1_output:
  # Standard project brief
  project_brief: { ... }

  # NEW: Journey context
  journey_context:
    journey_brief_loaded: true
    previous_posts_relevant:
      - title: "Why I'm building FastCache"
        key_point: "200 lines of boilerplate"
        callback_opportunity: "Reference the origin problem"

    current_milestone: "73% latency reduction"
    milestone_type: "metrics"
    recommended_content: ["blog", "twitter", "linkedin"]

    voice_reminders:
      - "Use 'boring tech wins' theme"
      - "Avoid 'game-changer' language"
      - "Connect to origin story"
```

### Modified Phase 4: Draft with Continuity

When writing the draft, include:

```yaml
phase_4_checklist:
  # Standard checks
  - template_structure: true
  - hook_quality: true

  # NEW: Continuity checks
  - references_previous_post: true  # If not first post
  - connects_to_origin_story: true  # For major milestones
  - voice_consistent: true
  - milestone_clearly_stated: true
```

### Modified Phase 5: Quality + Journey Verification

Add these checks:

```yaml
phase_5_additional:
  journey_checks:
    - voice_matches_brief: true
    - avoids_banned_phrases: true
    - audience_appropriate: true
    - adds_to_narrative: true  # Not just standalone content

  continuity_checks:
    - callbacks_natural: true  # References don't feel forced
    - standalone_value: true  # New readers can still understand
    - journey_brief_updated: true  # Add this post to history
```

---

## Part 6: Quick Reference

### Before ANY Build-in-Public Content

```
1. Load journey brief
2. Check previous posts for callback opportunities
3. Identify milestone type → content mapping
4. Verify voice reminders
```

### After Publishing

```
1. Update journey_brief.previous_posts
2. Note any lessons learned
3. Plan cascade content (if major milestone)
4. Schedule follow-up engagement
```

### Voice Consistency Checklist

```
[ ] Personality matches brief
[ ] Recurring themes present (at least one)
[ ] Signature phrases used naturally
[ ] Banned phrases avoided
[ ] Audience would recognize this as "me"
```

### Continuity Checklist

```
[ ] References at least one previous post (if not first)
[ ] Connects to origin story (for major milestones)
[ ] Advances the narrative (not just standalone)
[ ] New readers can still follow
```

---

## Integration with Existing Skill

This guide **extends** the 5-phase process:

| Phase | Standard | + Build-in-Public |
|-------|----------|-------------------|
| Phase 1 | Project brief | + Journey context loaded |
| Phase 2 | Audience lock-in | + Voice consistency check |
| Phase 3 | Evidence collection | + Previous post callbacks |
| Phase 4 | Structured draft | + Continuity verification |
| Phase 5 | Quality gate | + Journey checks added |

The workflow example in `examples/workflow/` shows standalone content creation.
This guide adds the **continuity layer** for sustained build-in-public.
