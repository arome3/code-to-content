---
allowed-tools: Read, Glob, Grep
argument-hint: [topic or project-path]
description: Generate a Twitter/X thread from an insight or project
---

# Generate Twitter Thread

Create an engaging Twitter/X thread from a technical insight or project.

> **Differentiation Discovery (offer; never blocking):** Before generating, offer to make this unmistakably theirs — ask for the WHY (the thesis/stakes), one defensible opinion, a road not taken, or a rough draft to polish ("write it ugly; I'll keep your voice"). Rank raw material (Slack threads, support tickets, a voice-memo transcript) above clean specs. If declined, proceed on code alone and flag `Distinctiveness: AT RISK`. At delivery, run the swap-the-name test + AI-tells blocklist from `references/differentiation.md`.

## Process

1. **Understand the Input**
   - If path provided: Analyze it Claude-natively (read deps, grep story hooks, mine git log; see `references/analysis-prompts.md`)
   - If topic provided: Proceed directly to insight extraction

2. **Load Skill Context**
   Read these files:
   - `skills/code-to-content/SKILL.md`
   - `skills/code-to-content/references/differentiation.md` (WHY / opinion / roads-not-taken)
   - `skills/code-to-content/references/social-content.md`
   - `skills/code-to-content/assets/templates/twitter_thread.md`

3. **Identify Core Insight**
   What's the ONE thing worth sharing? The hook must create curiosity.
   Good hooks:
   - Surprising result or metric
   - Contrarian take on common practice
   - "I was wrong about X" confession
   - Before/after transformation

4. **Generate Thread (8-12 tweets)**
   Structure:
   - Tweet 1: **HOOK** (most important - surprising claim or result)
   - Tweets 2-3: Context and problem
   - Tweets 4-6: Journey and insight
   - Tweets 7-8: Solution and results
   - Tweet 9+: Takeaway and CTA

5. **Format Rules**
   - Each tweet under 280 characters
   - Each tweet has standalone value (could be RT'd alone)
   - Include visual suggestions (code screenshots, diagrams)
   - End with engagement CTA (question, RT request, follow)

6. **Deliver**
   Present thread with:
   - Copy-paste ready format (numbered)
   - Visual suggestions for each tweet that needs one
   - Alternative hook options (2-3)
   - Best posting time recommendation
