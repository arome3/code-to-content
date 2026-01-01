---
allowed-tools: Bash(python:*), Bash(git log:*), Read, Glob, Grep
argument-hint: [project-path]
description: Generate a CFP abstract and talk outline from a codebase
---

# Generate Conference Talk

Create a CFP (Call for Papers) abstract and talk outline from the provided project.

## Process

1. **Analyze the Project**
   ```bash
   python skills/code-to-content/legacy/analyze_codebase.py $ARGUMENTS --deep
   ```
   Focus on: architectural decisions, pivots, performance improvements, lessons learned.

2. **Load Skill Context**
   Read these files:
   - `skills/code-to-content/SKILL.md`
   - `skills/code-to-content/references/conference-talks.md`

3. **Extract Core Thesis**
   Find the non-obvious insight:
   - What architectural choice surprised you?
   - What conventional wisdom did you challenge?
   - What pivotal decision changed the outcome?
   - What specific metric improvement did you achieve?

   Crystallize into one sentence:
   "By [doing X differently], [the project] achieved [surprising result Y]"

4. **Determine Talk Angle**

   | If project has... | Generate this angle |
   |-------------------|---------------------|
   | Custom solution over library | "Why We Rolled Our Own X" |
   | Major refactor documented | "The Refactor That Changed Everything" |
   | Performance optimization | "From Xms to Yms: The Journey" |
   | Pattern adoption | "How [Pattern] Saved Our Codebase" |
   | Migration story | "Migrating from A to B: Lessons" |

5. **Generate CFP Abstract (3 paragraphs)**

   **Paragraph 1 - HOOK:**
   "When we started [project], we faced [specific problem].
   After [time], we achieved [concrete improvement]."

   **Paragraph 2 - JOURNEY:**
   "In this talk, I'll walk through our journey from [before] to [after],
   including the [key change] that made the difference."

   **Paragraph 3 - TAKEAWAYS:**
   "You'll leave with:
   - A framework for evaluating [decision type]
   - Warning signs we missed
   - The specific pattern that made [outcome] possible"

6. **Generate Talk Outline**

   **For Lightning (5-10 min):**
   - 0:00 Hook
   - 0:30 Problem (before state)
   - 1:30 The Insight
   - 3:30 The Result
   - 4:30 Takeaway

   **For Standard (25-30 min):**
   - Opening (3 min)
   - The Before (5 min)
   - The Decision (7 min)
   - The Implementation (10 min)
   - The Results (3 min)
   - Your Turn (2 min)

7. **Deliver**
   Present:
   - Talk title (compelling, specific)
   - CFP abstract (submission-ready)
   - Talk outline with timing
   - Key slides to prepare
   - Demo suggestions
