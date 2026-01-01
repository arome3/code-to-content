---
allowed-tools: Bash(python:*), Bash(git log:*), Bash(git diff:*), Read, Glob, Grep
argument-hint: [project-path]
description: Generate a technical blog post from a codebase
---

# Generate Technical Blog Post

Generate a compelling technical blog post from the provided project.

## Process

1. **Analyze the Project**
   Run deep analysis on the codebase:
   ```bash
   python skills/code-to-content/legacy/analyze_codebase.py $ARGUMENTS --deep
   ```

2. **Load Skill Context**
   Read these files for guidance:
   - `skills/code-to-content/SKILL.md` (main skill instructions)
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
   ```bash
   python skills/code-to-content/legacy/analyze_readability.py output.md --audience [selected-audience]
   ```

7. **Deliver**
   Present the blog post with:
   - 3 suggested title options
   - Meta description for SEO (150-160 chars)
   - Suggested header image concept
   - Complete, publication-ready content
