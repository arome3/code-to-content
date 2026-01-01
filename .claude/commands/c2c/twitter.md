---
allowed-tools: Bash(python:*), Read, Glob, Grep
argument-hint: [topic or project-path]
description: Generate a Twitter/X thread from an insight or project
---

# Generate Twitter Thread

Create an engaging Twitter/X thread from a technical insight or project.

## Process

1. **Understand the Input**
   - If path provided: Analyze with `python skills/code-to-content/legacy/analyze_codebase.py $ARGUMENTS`
   - If topic provided: Proceed directly to insight extraction

2. **Load Skill Context**
   Read these files:
   - `skills/code-to-content/SKILL.md`
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
