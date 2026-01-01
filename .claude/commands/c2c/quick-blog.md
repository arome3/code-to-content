---
allowed-tools: Read, Glob, Grep
argument-hint: [topic]
description: Quick blog post - skips deep analysis for experienced users
---

# Quick Blog Post Generation

Generate a blog post quickly when you already have your topic defined.

**Quick Mode:** Skips Phase 1 (Deep Project Analysis) and Phase 4 (Optimization). Still requires audience declaration.

## When to Use Quick Mode

- Topic is already well-defined
- You don't need codebase mining for insights
- Time-sensitive content
- You know what you want to write about

## Process

1. **Declare Audience** (Required)
   Ask user: Who is this for?
   - Beginner (grade ≤ 8, jargon ≤ 2%)
   - Intermediate (grade ≤ 12, jargon ≤ 4%)
   - Expert (grade ≤ 16, jargon ≤ 8%)

2. **Load Format Reference**
   Read: `skills/code-to-content/references/formats.md` (blog section)

3. **Generate Content**
   Structure: Hook → Problem → Insight → Solution → Takeaway

   **Hook Rules:**
   - Start with surprising result or compelling problem
   - NEVER "In this article, I will..."
   - Create immediate curiosity

4. **Quick Validation**
   - [ ] Hook creates curiosity
   - [ ] Clear problem → solution arc
   - [ ] Matches declared audience complexity
   - [ ] Actionable takeaway at end

5. **Deliver**
   Present with:
   - 3 title options
   - Meta description (150-160 chars)
   - Complete content
   - Suggested header image concept

## Topic: $ARGUMENTS

Proceed with audience declaration, then generate directly.
