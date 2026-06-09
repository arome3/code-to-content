---
allowed-tools: Bash(git log:*), Read, Glob, Grep
argument-hint: [project-path]
description: Generate a newsletter issue about a project update
---

# Generate Newsletter Issue

Create a newsletter issue featuring updates from the provided project.

> **Differentiation Discovery (offer; never blocking):** Before generating, offer to make this unmistakably theirs — ask for the WHY (the thesis/stakes), one defensible opinion, a road not taken, or a rough draft to polish ("write it ugly; I'll keep your voice"). Rank raw material (Slack threads, support tickets, a voice-memo transcript) above clean specs. If declined, proceed on code alone and flag `Distinctiveness: AT RISK`. At delivery, run the swap-the-name test + AI-tells blocklist from `references/differentiation.md`.

## Process

1. **Analyze Recent Changes**
   Analyze the codebase **Claude-natively** (read dependency files, detect architecture, grep story hooks like TODO/FIXME, mine `git log`) — see `references/analysis-prompts.md`. No scripts required.
   Also examine recent git history for story-worthy commits.

2. **Load Skill Context**
   Read these files:
   - `skills/code-to-content/SKILL.md`
   - `skills/code-to-content/references/differentiation.md` (WHY / opinion / roads-not-taken)
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
