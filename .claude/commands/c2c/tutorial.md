---
allowed-tools: Bash(git log:*), Read, Glob, Grep
argument-hint: [project-path]
description: Generate a step-by-step tutorial from a codebase
---

# Generate Technical Tutorial

Create a step-by-step tutorial that teaches developers how to use or build something from the provided project.

> **Differentiation Discovery (offer; never blocking):** Before generating, offer to make this unmistakably theirs — ask for the WHY (the thesis/stakes), one defensible opinion, a road not taken, or a rough draft to polish ("write it ugly; I'll keep your voice"). Rank raw material (Slack threads, support tickets, a voice-memo transcript) above clean specs. If declined, proceed on code alone and flag `Distinctiveness: AT RISK`. At delivery, run the swap-the-name test + AI-tells blocklist from `references/differentiation.md`.

## Process

1. **Analyze the Project**
   Analyze the codebase **Claude-natively** (read dependency files, detect architecture, grep story hooks like TODO/FIXME, mine `git log`) — see `references/analysis-prompts.md`. No scripts required.

2. **Load Skill Context**
   Read these files:
   - `skills/code-to-content/SKILL.md`
   - `skills/code-to-content/references/differentiation.md` (WHY / opinion / roads-not-taken)
   - `skills/code-to-content/references/formats.md` (tutorials section)
   - `skills/code-to-content/assets/templates/tutorial.md`

3. **Identify Learning Objective**
   Ask the user: What single skill should readers gain from this tutorial?

4. **Structure the Tutorial**
   Follow the 6-section structure:
   - Hook & Outcome (what they'll build)
   - Prerequisites (required knowledge, tools, time)
   - Foundation (first 5 minutes - get something working)
   - Build (one concept per section)
   - Polish (error handling, production considerations)
   - Next Steps (extensions, related topics)

5. **Apply Progressive Disclosure**
   - Start with simplest working version
   - Add complexity incrementally
   - 5-9 numbered steps (one action per step)
   - Checkpoint after each step
   - Troubleshooting blocks for common errors

6. **Validate**
   Ensure content matches audience level using:
   Estimate readability **Claude-natively** against the audience thresholds in `references/readability-guide.md` (grade level, jargon %, code:prose ratio).

7. **Deliver**
   Present complete tutorial with:
   - Clear title: "[Action Verb] a [Result] with [Technology]"
   - Time estimate
   - Difficulty level (Beginner/Intermediate/Advanced)
   - Complete, tested code examples
