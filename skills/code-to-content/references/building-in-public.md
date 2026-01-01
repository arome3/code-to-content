# Building in Public - Update Generation Instructions

Implementation guide for generating periodic project updates for building in public content.

---

## When to Use

Generate building-in-public updates when the user:
- Wants to share project progress regularly
- Is documenting their development journey
- Needs accountability posts for ongoing work
- Wants to grow an audience around their project

---

## Pre-Generation: Extract Project Status

Before generating any update, gather current project state:

```
EXTRACT FROM USER OR PROJECT:
├── What changed since last update?
│   ├── Features added
│   ├── Bugs fixed
│   ├── Decisions made
│   └── Problems encountered
├── Current metrics (if any)
│   ├── Users / downloads / stars
│   ├── Performance numbers
│   └── Revenue / signups
├── What's next?
│   ├── Immediate priorities
│   ├── Blockers
│   └── Goals for next period
└── Emotional state
    ├── Wins to celebrate
    ├── Frustrations to share
    └── Lessons learned
```

If information is missing, ask:
- "What did you work on this week?"
- "What's the biggest win since your last update?"
- "What's blocking you right now?"
- "What did you learn?"

---

## Update Types

### Daily Update (Micro)

**Use when:** Quick accountability, Twitter-native, low effort
**Length:** 1-3 tweets or short post

**Generate structure:**
```
[What I shipped today]
├── 1-2 concrete accomplishments
└── Optional: screenshot or code snippet

[What's next]
└── Tomorrow's focus (1 item)

[Optional: Metric or mood]
└── Quick number or emoji
```

**Template:**
```
Day [X] of building [Project]:

✓ [Accomplishment 1]
✓ [Accomplishment 2]

Tomorrow: [Next focus]

[Metric if available]
```

---

### Weekly Update (Standard)

**Use when:** Regular cadence, substantive progress, audience building
**Length:** 5-8 tweets or medium post

**Generate structure:**
```
[Hook: Biggest win or insight of the week]

[Progress summary]
├── 3-5 accomplishments
├── Key decision made
└── Unexpected discovery

[Challenges]
├── What was hard
└── How you solved it (or didn't)

[Metrics delta]
├── This week vs last week
└── Trend direction

[Next week focus]
├── Top 3 priorities
└── What would make it a great week

[Engagement ask]
└── Question for audience
```

**Template:**
```
Week [X] building [Project] in public:

Biggest win: [One-liner]

What shipped:
• [Feature/fix 1]
• [Feature/fix 2]
• [Feature/fix 3]

What I learned: [Insight]

Metrics:
[Before] → [After]

Hardest part: [Challenge + resolution or status]

Next week:
→ [Priority 1]
→ [Priority 2]
→ [Priority 3]

[Question for audience]
```

---

### Monthly Update (Comprehensive)

**Use when:** Milestone reflection, investor updates, major progress
**Length:** Blog post or long LinkedIn post

**Generate structure:**
```
[Opening: Month in one sentence]

## Wins
├── Major accomplishments (3-5)
├── Each with context and impact
└── Screenshots or demos if available

## Metrics
├── Key numbers with trends
├── Month-over-month comparison
└── What's driving changes

## Challenges
├── What went wrong
├── What took longer than expected
└── How you're addressing it

## Learnings
├── Technical insights
├── Product/market insights
└── Personal/process insights

## Next Month
├── Goals (specific, measurable)
├── Experiments to run
└── What success looks like

## Ask
├── Specific help needed
├── Feedback requested
└── How audience can support
```

---

### Milestone Update (Event-Driven)

**Use when:** Hitting a significant milestone, launch, pivot, or major decision
**Length:** Varies by significance

**Generate structure:**
```
[Milestone announcement with context]

[The journey to get here]
├── When you started
├── Key obstacles overcome
├── Pivotal moments

[What this means]
├── Why it matters
├── What changes now
└── What it unlocks

[Gratitude / acknowledgment]
├── Who helped
├── What you learned
└── Community thanks

[What's next]
└── Next milestone target
```

**Milestone triggers:**
- First user / First 100 / First 1000
- First revenue / $1K MRR / Profitability
- Launch day / ProductHunt / Major release
- Pivot decision / Sunset announcement
- Funding / Partnership / Major hire

---

## Platform-Specific Formatting

### Twitter/X Updates

**Daily:**
```
Day [X] of [Project]:

[1-2 line update]

#buildinpublic
```

**Weekly (thread):**
```
1/ Week [X] of building [Project] 🧵

[Biggest win headline]

2/ What shipped:
• [Item 1]
• [Item 2]
• [Item 3]

3/ [Detailed insight or learning]

4/ Metrics:
[Before] → [After]

5/ Next week:
→ [Priority]

What should I focus on? 👇
```

### LinkedIn Updates

```
[Hook line - biggest insight or win]

[3-4 paragraph narrative covering]:
- What happened
- Why it matters
- What you learned

[Bullet summary of key points]

[Forward-looking statement]

[Engagement question]

#buildinpublic #[relevant hashtags]
```

### Newsletter/Blog Updates

Use full monthly structure with additional sections:
- Behind-the-scenes details
- Revenue/growth transparency
- Longer reflection on lessons
- Resource recommendations
- Community highlights

---

## Tone Calibration

### For Wins

```
DO: Share genuine excitement, specific details, gratitude
DON'T: Humble-brag, minimize accomplishment, over-hype

GOOD: "Hit 1,000 users today. Took 6 months. The signup
      that pushed us over was from Japan at 3am. Still
      can't believe people use this thing."

BAD:  "So humbled to announce we've achieved the incredible
      milestone of 1,000 users!!!"
```

### For Challenges

```
DO: Be honest, share learning, show resilience
DON'T: Complain without insight, seek pity, blame others

GOOD: "Spent 3 days debugging a race condition. The fix
      was 2 lines. Lesson: add logging earlier."

BAD:  "Everything is broken. This sucks. Why is programming
      so hard?"
```

### For Metrics

```
DO: Show trends, provide context, be transparent
DON'T: Cherry-pick, hide bad numbers, compare unfairly

GOOD: "MRR: $1,200 → $1,450 (+21%)
      Churn: 8% (up from 5%, investigating)"

BAD:  "Revenue up 21%!!!"
```

---

## Consistency Rules

### Maintain Regular Cadence

Generate reminders for posting schedule:
- Daily: Same time each day
- Weekly: Same day each week
- Monthly: First week of month

### Track Continuity

Reference previous updates:
- "Last week I mentioned [X]. Update: [Y]"
- "Remember the bug from Day 12? Finally fixed."
- "Following up on my goal to [X]..."

### Build Narrative Arc

Connect updates into ongoing story:
- Reference origin story periodically
- Celebrate progress from early days
- Connect current work to larger vision

---

## Engagement Optimization

### End with Engagement Hooks

```
Questions that work:
- "What would you prioritize next?"
- "Anyone else dealt with [specific problem]?"
- "Should I build X or Y first?"
- "What's your experience with [technology]?"

Questions that don't work:
- "Thoughts?"
- "What do you think?"
- "Any feedback?"
```

### Respond to Comments

Generate follow-up engagement:
- Thank specific feedback
- Answer questions publicly
- Incorporate suggestions into next update

---

## Update Generation Checklist

Before delivering any update:

```
[ ] Specific accomplishments (not vague "worked on X")
[ ] At least one learning or insight
[ ] Honest about challenges (not just wins)
[ ] Metrics included if available
[ ] Forward-looking element (what's next)
[ ] Engagement hook at end
[ ] Appropriate length for platform
[ ] Consistent with previous update tone
[ ] No humble-bragging or false modesty
[ ] Authentic voice maintained
```
