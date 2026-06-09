---
allowed-tools: Bash(git log:*), Bash(git diff:*), Read, Glob, Grep
argument-hint: [project-path]
description: Generate a technical blog post from a codebase
---

# Generate Technical Blog Post

Generate a compelling technical blog post from the provided project.

> **Differentiation Discovery (offer; never blocking):** Before generating, offer to make this unmistakably theirs — ask for the WHY (the thesis/stakes), one defensible opinion, a road not taken, or a rough draft to polish ("write it ugly; I'll keep your voice"). Rank raw material (Slack threads, support tickets, a voice-memo transcript) above clean specs. If declined, proceed on code alone and flag `Distinctiveness: AT RISK`. At delivery, run the swap-the-name test + AI-tells blocklist from `references/differentiation.md`.

## Process

1. **Analyze the Project**
   Analyze the codebase **Claude-natively** (read dependency files, detect architecture, grep story hooks like TODO/FIXME, mine `git log`) — see `references/analysis-prompts.md`. No scripts required.

2. **Load Skill Context**
   Read these files for guidance:
   - `skills/code-to-content/SKILL.md` (main skill instructions)
   - `skills/code-to-content/references/differentiation.md` (WHY / opinion / roads-not-taken)
   - `skills/code-to-content/references/formats.md` (blog section)
   - `skills/code-to-content/references/project-analysis.md`
   - `skills/code-to-content/assets/templates/blog_post.md`

3. **Determine Audience**
   Ask the user: Who is this blog post for? (beginners, peers, hiring managers, general developers)

4. **Identify the "Aha Moment"**
   From the analysis, find the single most compelling insight worth sharing:
   - Surprising technical decision
   - Performance improvement with metrics
   - Problem-solving journey
   - Architectural pivot

5. **Generate Content**
   Follow the blog post template structure:
   - Hook that creates immediate curiosity (no "In this article...")
   - Problem → Journey → Solution → Results arc
   - Ground all examples in actual code from the project
   - Extract before/after examples from git history if available
   - Apply voice calibration based on tech stack

6. **Validate Readability**
   Run readability analysis on the generated content:
   Estimate readability **Claude-natively** against the audience thresholds in `references/readability-guide.md` (grade level, jargon %, code:prose ratio).

7. **Deliver**
   Present the blog post with:
   - 3 suggested title options
   - Meta description for SEO (150-160 chars)
   - Suggested header image concept
   - Complete, publication-ready content
