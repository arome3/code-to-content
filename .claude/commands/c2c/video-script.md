---
allowed-tools: Bash(python:*), Bash(git log:*), Read, Glob, Grep
argument-hint: [project-path]
description: Generate a video or screencast script from a codebase
---

# Generate Video Script

Create a video or screencast script for demonstrating or explaining the provided project.

## Process

1. **Analyze the Project**
   ```bash
   python skills/code-to-content/legacy/analyze_codebase.py $ARGUMENTS --full
   ```

2. **Load Skill Context**
   Read these files:
   - `skills/code-to-content/SKILL.md`
   - `skills/code-to-content/assets/templates/video_script.md`
   - `skills/code-to-content/references/formats.md` (video scripts section)

3. **Determine Video Type**
   Ask the user:
   - **Demo** (3-5 min): Show the tool in action
   - **Tutorial** (10-20 min): Teach how to build something
   - **Explainer** (5-10 min): Explain architecture or concept
   - **Walkthrough** (5-15 min): Tour of codebase

4. **Structure the Script**

   **INTRO (10-15% of runtime):**
   - Hook: What will they learn/see?
   - Context: Why does this matter?
   - Preview: What's coming?

   **BODY (70-80% of runtime):**
   - For demos: Feature → Action → Result
   - For tutorials: Step → Code → Explanation → Checkpoint
   - For explainers: Concept → Visualization → Example
   - For walkthroughs: Area → Purpose → Key Files → Connections

   **OUTRO (10-15% of runtime):**
   - Summary: Key takeaways
   - CTA: What to do next
   - Resources: Links, docs, community

5. **Add Production Notes**
   For each section, include:
   - [SCREEN]: What to show (code editor, terminal, browser, slides)
   - [SAY]: Exact narration script
   - [DO]: Actions to perform on screen
   - [NOTE]: Timing or transition notes

6. **Deliver**
   Present script with:
   - Estimated runtime
   - Scene-by-scene breakdown
   - Production notes
   - Required assets/setup list
   - Thumbnail concept
