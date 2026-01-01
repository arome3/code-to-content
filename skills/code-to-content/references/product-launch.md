# Product Launch Generation: Implementation Instructions

Generate launch content and strategy for a user's project across multiple platforms. Cover pre-launch, launch day, and post-launch phases.

---

## When to Use

Generate launch content when the user:
- Is releasing a project publicly for the first time
- Is launching on Product Hunt, Hacker News, or similar platforms
- Wants a coordinated multi-platform launch strategy
- Needs launch day content ready in advance

---

## Pre-Generation: Launch Inventory

Before generating launch content, extract from the project:

```
PROJECT ESSENTIALS:
├── One-line description (< 10 words)
├── Value proposition (problem → solution)
├── Target audience (who is this for)
├── Key features (3-5 bullet points)
├── Differentiator (what makes it unique)
├── Social proof (if any: users, stars, testimonials)
└── Call to action (try it, star it, sign up)

LAUNCH SPECIFICS:
├── Launch platforms (Product Hunt, HN, Twitter, etc.)
├── Launch date/time
├── Demo/video available?
├── Pricing (free, freemium, paid)
└── Available for support on launch day?
```

---

## Platform-Specific Launch Content

### Product Hunt Launch

**Tagline (60 chars max):**
```
{{action_verb}} {{outcome}} with {{method}}
```

Examples:
- "Give AI agents a wallet—with guardrails"
- "Ship docs that developers actually read"
- "Turn screenshots into code in seconds"

**Description (260 chars max):**
```
{{Problem in one sentence}}. {{Project_name}} {{solution}}.

{{Key feature 1}}
{{Key feature 2}}
{{Key feature 3}}

{{Differentiator or social proof}}
```

**First Comment (Maker Comment):**
```
Hey Product Hunt!

I'm {{name}}, and I built {{project_name}} because {{personal_problem}}.

{{1-2 sentences on the journey}}

What you're getting today:
• {{Feature 1}}
• {{Feature 2}}
• {{Feature 3}}

What's coming next:
• {{Roadmap item 1}}
• {{Roadmap item 2}}

I'll be here all day answering questions. Would love to hear:
- {{Specific question for community}}

Thanks for checking it out!
```

**Gallery Assets Checklist:**
- [ ] Logo (240x240)
- [ ] Hero image (1270x760)
- [ ] 3-5 product screenshots
- [ ] Demo GIF or video (optional but recommended)

---

### Hacker News Launch

**Title Format:**
```
{{Action}}: {{Project}} – {{One-line description}}
```

Title types:
- **Show HN:** For projects you built
- **Launch HN:** For startup launches (YC companies)

Examples:
- "Show HN: Tempo-MCP – Let AI agents send payments with spending limits"
- "Show HN: I built a tool that generates docs from code comments"

**HN Post Body:**
```
{{What it does in 1-2 sentences}}

{{Why I built it - personal motivation}}

{{Technical approach in 2-3 sentences}}

Key features:
- {{Feature 1}}
- {{Feature 2}}
- {{Feature 3}}

{{What's unique about the approach}}

Demo: {{link}}
Code: {{github_link}}

Would love feedback on {{specific_aspect}}.
```

**HN Guidelines:**
- Post between 8-10am ET weekdays
- No marketing language ("revolutionary", "game-changing")
- Be technical and honest
- Respond to every comment
- Don't ask for upvotes

---

### Twitter/X Launch

**Launch Tweet:**
```
{{Project_name}} is live.

{{One-sentence value prop}}

{{Feature 1}}
{{Feature 2}}
{{Feature 3}}

{{CTA}}: {{link}}

🧵 Thread with the full story:
```

**Launch Thread (8-12 tweets):**
```
1/ {{Project_name}} is live.

{{Hook: surprising statement or result}}

Here's what it does and why I built it: 🧵

2/ The problem:

{{Pain point your audience feels}}

{{Why existing solutions don't work}}

3/ The solution:

{{What your project does}}

{{Key insight or approach}}

4/ Feature 1: {{Name}}

{{What it does}}
{{Why it matters}}

[Screenshot or code snippet]

5/ Feature 2: {{Name}}

{{What it does}}
{{Why it matters}}

6/ Feature 3: {{Name}}

{{What it does}}
{{Why it matters}}

7/ The technical approach:

{{Brief architecture or key decision}}

{{Why this approach works}}

8/ What's next:

{{Roadmap item 1}}
{{Roadmap item 2}}
{{Roadmap item 3}}

9/ Try it:

{{Primary CTA + link}}

{{Secondary CTA if applicable}}

10/ If you found this useful:

• RT the first tweet to spread the word
• Star the repo: {{github}}
• Follow for updates on {{topic}}

Questions? Ask below 👇
```

---

### LinkedIn Launch

**Launch Post:**
```
{{Hook: What you shipped + why it matters}}

{{2-3 paragraphs covering:}}
- The problem you solved
- Your approach
- What makes it different

Key features:
• {{Feature 1}}
• {{Feature 2}}
• {{Feature 3}}

{{Personal reflection: what you learned or why this matters to you}}

{{CTA}}

Link: {{url}}

#launch #{{relevant_tags}}
```

---

### GitHub Launch

**Release Notes Format:**
```markdown
# {{Project_name}} v1.0.0

{{One-line description}}

## Highlights

- **{{Feature 1}}**: {{Brief description}}
- **{{Feature 2}}**: {{Brief description}}
- **{{Feature 3}}**: {{Brief description}}

## Getting Started

```bash
{{installation_command}}
```

## Quick Example

```{{language}}
{{minimal_working_example}}
```

## Documentation

- [Getting Started]({{docs_link}})
- [API Reference]({{api_link}})
- [Examples]({{examples_link}})

## What's Next

- [ ] {{Roadmap item 1}}
- [ ] {{Roadmap item 2}}
- [ ] {{Roadmap item 3}}

## Feedback

We'd love to hear from you:
- {{Issue tracker}}
- {{Discussion forum}}
- {{Social handle}}
```

---

### Dev.to / Blog Launch Post

**Structure:**
```markdown
# {{Title: How I Built X / Introducing X / X is Live}}

{{Hook paragraph - the problem or story}}

## The Problem

{{What pain point you're solving}}
{{Why existing solutions don't work}}

## What I Built

{{Project description}}
{{Key features}}

## How It Works

{{Technical overview}}
{{Architecture diagram or code snippets}}

## Key Features

### {{Feature 1}}
{{Description with code example}}

### {{Feature 2}}
{{Description with code example}}

### {{Feature 3}}
{{Description with code example}}

## The Journey

{{Brief build story - challenges, decisions, timeline}}

## What's Next

{{Roadmap}}

## Try It

{{CTA with links}}

---

{{Bio line + social links}}
```

---

## Launch Day Checklist

### Pre-Launch (1 week before)

```
[ ] All content written and reviewed
[ ] Product Hunt draft saved
[ ] Twitter thread drafted
[ ] LinkedIn post drafted
[ ] GitHub README polished
[ ] Demo/screenshots ready
[ ] Landing page live
[ ] Analytics tracking set up
[ ] Support channels ready (email, Discord, Twitter DMs)
```

### Launch Day (Morning)

```
[ ] Product Hunt goes live at 12:01am PT
[ ] Maker comment posted immediately
[ ] Twitter thread posted (8-9am your time)
[ ] LinkedIn post published
[ ] Hacker News submitted (8-10am ET)
[ ] Email list notified (if applicable)
[ ] Cross-post to relevant communities
```

### Launch Day (Ongoing)

```
[ ] Respond to every PH comment
[ ] Respond to every HN comment
[ ] Engage with Twitter replies
[ ] Monitor for bugs/issues
[ ] Share user feedback/testimonials
[ ] Post updates if milestones hit
```

### Post-Launch (Day 2-7)

```
[ ] Thank you post to supporters
[ ] Compile feedback/feature requests
[ ] Fix critical bugs surfaced
[ ] Share metrics/learnings
[ ] Follow up with engaged users
[ ] Plan next iteration
```

---

## Launch Timing Guide

**Product Hunt:**
- Ships at 12:01am PT
- Peak activity: 9am-12pm PT
- Post maker comment immediately
- Be available all day

**Hacker News:**
- Best times: 8-10am ET weekdays
- Tuesday-Thursday optimal
- Avoid weekends, holidays
- First hour critical for momentum

**Twitter:**
- Best times: 9-11am, 1-3pm your audience's timezone
- Tuesday-Thursday optimal
- Thread in morning, engagement throughout day

**LinkedIn:**
- Best times: 8-10am, 12pm
- Tuesday-Thursday optimal
- Respond to comments within first hour

---

## Launch Metrics to Track

```
AWARENESS:
├── Impressions across platforms
├── Product Hunt ranking (final position)
├── Hacker News points + comments
└── Social shares/retweets

ENGAGEMENT:
├── Comments and replies
├── Time on site
├── Demo completions
└── GitHub stars/forks

CONVERSION:
├── Signups/downloads
├── Email subscribers
├── Active users (Day 1, Day 7)
└── Conversion rate by source
```

---

## Platform-Specific Tips

### Product Hunt Success Factors

```
DO:
- Have a compelling tagline (this is 50% of clicks)
- Lead with demo GIF/video
- Respond to every comment quickly
- Be genuine in maker comment
- Share on social with gratitude, not desperation

DON'T:
- Ask for upvotes explicitly
- Post and disappear
- Use marketing buzzwords
- Launch on weekends
- Ignore critical feedback
```

### Hacker News Success Factors

```
DO:
- Be technical and specific
- Show genuine craft/effort
- Respond thoughtfully to criticism
- Share what you learned
- Be humble about limitations

DON'T:
- Use marketing language
- Astroturf with fake accounts
- Argue with critics
- Spam your link
- Delete and repost
```

---

## Output Format

Deliver launch content as:

```markdown
# {{Project_name}} Launch Package

## Overview
- **Launch date:** {{date}}
- **Primary platforms:** {{list}}
- **Target:** {{goal}}

---

## Product Hunt

### Tagline
{{tagline}}

### Description
{{description}}

### Maker Comment
{{comment}}

---

## Hacker News

### Title
{{title}}

### Post Body
{{body}}

---

## Twitter

### Launch Tweet
{{tweet}}

### Thread
{{thread}}

---

## LinkedIn

### Launch Post
{{post}}

---

## Launch Day Checklist
{{customized_checklist}}

---

## Timing Plan
{{schedule}}
```

---

## Pre-Delivery Checklist

```
[ ] All platform content within character limits
[ ] Consistent messaging across platforms
[ ] All links verified working
[ ] Screenshots/assets listed
[ ] Maker comment personal and genuine
[ ] HN post avoids marketing language
[ ] Clear CTAs on each platform
[ ] Timing recommendations included
[ ] Launch day checklist customized
[ ] Post-launch follow-up planned
```
