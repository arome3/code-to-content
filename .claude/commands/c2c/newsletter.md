---
allowed-tools: Bash(python:*), Bash(git log:*), Read, Glob, Grep
argument-hint: [project-path]
description: Generate a newsletter issue about a project update
---

# Generate Newsletter Issue

Create a newsletter issue featuring updates from the provided project.

## Process

1. **Analyze Recent Changes**
   ```bash
   python skills/code-to-content/legacy/analyze_codebase.py $ARGUMENTS --deep
   ```
   Also examine recent git history for story-worthy commits.

2. **Load Skill Context**
   Read these files:
   - `skills/code-to-content/SKILL.md`
   - `skills/code-to-content/references/newsletters.md`
   - `skills/code-to-content/assets/templates/newsletter.md`

3. **Identify Newsletter Format**
   Ask the user which format fits their update:
   - **Build Log**: Active development (shipped, learned, next)
   - **Deep Dive**: After completing significant feature
   - **Lesson Learned**: After resolving a challenge
   - **Milestone Update**: Reached a significant goal

4. **Extract Content Elements**
   - Featured item (main update or insight)
   - Quick hits (3-5 smaller updates)
   - Code snippet or visual if applicable
   - Personal reflection or lesson
   - What's next / roadmap tease

5. **Generate Newsletter**
   Include:
   - Subject line (under 50 chars, creates curiosity)
   - Preview text (120-160 chars)
   - Personal opening hook (conversational)
   - Featured section with unique commentary
   - Quick hits with your perspective (not just changelog)
   - Engaging closing with CTA

6. **Apply Voice**
   Newsletter should feel like a message from a friend, not a broadcast.
   Be specific, be personal, share the "why" behind changes.

7. **Deliver**
   Present complete newsletter with:
   - 3 subject line options
   - Preview text
   - Full newsletter content
   - Suggested send time
