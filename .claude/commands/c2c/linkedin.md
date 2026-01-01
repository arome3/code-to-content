---
allowed-tools: Bash(python:*), Read, Glob, Grep
argument-hint: [topic or project-path]
description: Generate a LinkedIn post from an insight or project
---

# Generate LinkedIn Post

Create a professional LinkedIn post from a technical insight or project experience.

## Process

1. **Understand the Input**
   - If path provided: Analyze with `python skills/code-to-content/legacy/analyze_codebase.py $ARGUMENTS`
   - If topic provided: Proceed directly to story extraction

2. **Load Skill Context**
   Read these files:
   - `skills/code-to-content/SKILL.md`
   - `skills/code-to-content/references/social-content.md` (LinkedIn section)
   - `skills/code-to-content/assets/templates/linkedin_post.md`

3. **Identify the Story**
   LinkedIn posts work best with:
   - Personal experience or lesson
   - Specific, concrete details (not abstract)
   - Professional relevance
   - Actionable takeaways

4. **Generate Post Structure**

   **HOOK (First 2 lines - visible before "See more"):**
   - First line MUST compel the click
   - Create curiosity gap or state surprising result
   - Line break after hook

   **STORY (3-4 paragraphs):**
   - Set scene with specific situation
   - Present challenge or conflict
   - Describe decision or action taken
   - Show outcome with specifics

   **LESSON (Takeaway section):**
   - Generalize what was learned
   - 3-5 bullet points for scannability
   - Make it applicable to reader

   **CTA (Engagement close):**
   - Genuine question to drive comments
   - 3-5 relevant hashtags

5. **Length and Format**
   - Target 800-1300 characters
   - Use line breaks for readability
   - Avoid walls of text
   - Professional but personable tone

6. **Deliver**
   Present post with:
   - 2-3 hook variations
   - Complete post content
   - Suggested hashtags
   - Best posting time (Tue-Thu, 8-10am or 12pm)
