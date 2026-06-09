---
allowed-tools: Bash(git log:*), Read, Glob, Grep
argument-hint: [project-path]
description: Generate a video or screencast script from a codebase
---

# Generate Video Script

Create a video or screencast script for demonstrating or explaining the provided project.

> **Differentiation Discovery (offer; never blocking):** Before generating, offer to make this unmistakably theirs — ask for the WHY (the thesis/stakes), one defensible opinion, a road not taken, or a rough draft to polish ("write it ugly; I'll keep your voice"). Rank raw material (Slack threads, support tickets, a voice-memo transcript) above clean specs. If declined, proceed on code alone and flag `Distinctiveness: AT RISK`. At delivery, run the swap-the-name test + AI-tells blocklist from `references/differentiation.md`.

## Process

1. **Analyze the Project**
   Analyze the codebase **Claude-natively** (read dependency files, detect architecture, grep story hooks like TODO/FIXME, mine `git log`) — see `references/analysis-prompts.md`. No scripts required.

2. **Load Skill Context**
   Read these files:
   - `skills/code-to-content/SKILL.md`
   - `skills/code-to-content/references/differentiation.md` (WHY / opinion / roads-not-taken)
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
