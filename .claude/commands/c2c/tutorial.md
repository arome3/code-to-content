---
allowed-tools: Bash(python:*), Bash(git log:*), Read, Glob, Grep
argument-hint: [project-path]
description: Generate a step-by-step tutorial from a codebase
---

# Generate Technical Tutorial

Create a step-by-step tutorial that teaches developers how to use or build something from the provided project.

## Process

1. **Analyze the Project**
   ```bash
   python skills/code-to-content/legacy/analyze_codebase.py $ARGUMENTS --full
   ```

2. **Load Skill Context**
   Read these files:
   - `skills/code-to-content/SKILL.md`
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
   ```bash
   python skills/code-to-content/legacy/analyze_readability.py output.md --audience [level]
   ```

7. **Deliver**
   Present complete tutorial with:
   - Clear title: "[Action Verb] a [Result] with [Technology]"
   - Time estimate
   - Difficulty level (Beginner/Intermediate/Advanced)
   - Complete, tested code examples
