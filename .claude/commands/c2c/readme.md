---
allowed-tools: Bash(python:*), Bash(git log:*), Read, Glob, Grep
argument-hint: [project-path]
description: Generate a README.md for a repository
---

# Generate Repository README

Create a comprehensive README.md for the provided project.

## Process

1. **Analyze the Project**
   ```bash
   python skills/code-to-content/legacy/analyze_codebase.py $ARGUMENTS --deep
   ```

2. **Load Skill Context**
   Read these files:
   - `skills/code-to-content/SKILL.md`
   - `skills/code-to-content/assets/templates/readme.md`
   - `skills/code-to-content/references/documentation.md`

3. **Extract Key Information**
   From analysis, identify:
   - One-line description (what + key benefit)
   - Problem being solved (pain point)
   - Target users
   - Key features (3-5)
   - Tech stack and dependencies
   - Configuration options

4. **Generate README Sections**
   Follow priority order:

   **Level 1 - Identity (always):**
   - Title with badges
   - One-line description
   - The Problem / The Solution

   **Level 2 - Usage (always):**
   - Quick Start (working in <5 minutes)
   - Basic usage examples

   **Level 3 - Details (if non-trivial):**
   - Configuration table (all options)
   - Architecture overview/diagram
   - API reference (if applicable)

   **Level 4 - Contribution (if open source):**
   - Development setup
   - Testing commands
   - Contributing link

   **Level 5 - Reference:**
   - Troubleshooting FAQ
   - Changelog link
   - License

5. **Generate Architecture Diagram**
   ```bash
   python skills/code-to-content/legacy/generate_diagrams.py $ARGUMENTS --type architecture
   ```

6. **Deliver**
   Present complete README.md ready to copy, with:
   - Suggested badges
   - ASCII or Mermaid architecture diagram
   - All sections filled with project-specific content
