---
allowed-tools: Read, Glob, Grep, Bash(git log:*)
argument-hint: [project-path]
description: Quick README - skips audience phases for standard developer docs
---

# Quick README Generation

Generate a README quickly for standard developer documentation.

**Quick Mode:** Skips Phase 1 (Deep Analysis) and Phase 2 (Audience Declaration). Assumes intermediate developer audience.

## When to Use Quick Mode

- Standard open-source project README
- Developer audience is assumed
- Project structure is straightforward
- Quick documentation needed

## Process

1. **Quick Scan**
   Read these files to understand the project:
   - `package.json` or equivalent (name, description, scripts)
   - Existing `README.md` (if updating)
   - Main entry point file

2. **Load Format Reference**
   Read: `skills/code-to-content/references/documentation.md` (readme section)

3. **Generate README**
   Required sections:

   - **Title + One-liner:** What it is + key benefit
   - **Problem:** Pain point being solved
   - **Quick Start:** Working example in < 5 minutes
   - **Installation:** Copy-paste commands
   - **Usage:** Basic examples
   - **Configuration:** Options table (if applicable)
   - **License**

4. **Quick Validation**
   - [ ] One-liner describes what AND why
   - [ ] Quick start actually works
   - [ ] No jargon without explanation
   - [ ] Installation commands are copy-paste ready

5. **Deliver**
   Present the complete README.md content.

## Project Path: $ARGUMENTS

Generate the README now. Skip confirmations and deliver directly.
