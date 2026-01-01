---
allowed-tools: Bash(python:*), Bash(git log:*), Read, Glob, Grep
argument-hint: [project-path]
description: Generate multi-platform launch content for a product
---

# Generate Product Launch Content

Create comprehensive launch content for Product Hunt, Hacker News, Twitter, and LinkedIn.

## Process

1. **Analyze the Project**
   ```bash
   python skills/code-to-content/legacy/analyze_codebase.py $ARGUMENTS --deep
   ```

2. **Load Skill Context**
   Read these files:
   - `skills/code-to-content/SKILL.md`
   - `skills/code-to-content/references/product-launch.md`
   - `skills/code-to-content/references/posting-plan.md`

3. **Build Launch Inventory**
   Extract from analysis:
   - One-line description (< 10 words)
   - Value proposition (problem → solution)
   - Target audience
   - Key features (3-5 bullets)
   - Differentiator (what makes it unique)
   - Social proof (users, stars, testimonials)

4. **Generate Product Hunt Content**

   **Tagline (60 chars max):**
   "[Action verb] [outcome] with [method]"

   **Maker Comment:**
   - Personal greeting
   - Why you built it (personal problem)
   - 1-2 sentences on the journey
   - What you're launching today (features)
   - What's coming next (roadmap)
   - "I'll be here answering questions"

5. **Generate Hacker News Post**

   **Title:** "Show HN: [Project] – [One-line description]"

   **Body:**
   - What it does (1-2 sentences)
   - Why you built it (motivation)
   - Technical approach (2-3 sentences)
   - Key features (bullets)
   - Demo + Code links
   - "Would love feedback on [specific aspect]"

6. **Generate Twitter Launch Thread**
   - Tweet 1: Hook + "Here's what it does 🧵"
   - Tweet 2-3: Problem and solution
   - Tweet 4-6: Features with screenshots
   - Tweet 7: Technical approach
   - Tweet 8: What's next
   - Tweet 9: Try it link
   - Tweet 10: RT/Star/Follow CTA

7. **Generate LinkedIn Announcement**
   - Hook about the problem
   - Personal story of building
   - What it does (clear, professional)
   - Call for feedback/support

8. **Generate 7-Day Posting Plan**
   - Day 1: Announcement (all platforms)
   - Day 2: Technical deep-dive
   - Day 3: Story/origin
   - Day 4: Use cases
   - Day 5: Lessons learned
   - Day 6: Behind-the-scenes
   - Day 7: Recap + ask

9. **Deliver**
   Present complete launch kit with:
   - All platform content ready to post
   - 7-day content calendar
   - Optimal posting times
   - Launch day checklist
