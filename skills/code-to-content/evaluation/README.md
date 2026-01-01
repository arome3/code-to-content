# Evaluation Guide

This directory contains evaluation questions for testing the code-to-content skill.

## Overview

The evaluation suite tests whether Claude can effectively use this skill's guidance files to answer questions about technical writing best practices.

**Approach:** Self-contained — all questions can be answered by reading the skill's own files (SKILL.md, templates, scripts, references). No external repositories required.

---

## Question Categories

| Category | Count | Tests |
|----------|-------|-------|
| Template structure knowledge | 2 | Understanding of blog_post.md, readme.md patterns |
| Audience profile thresholds | 2 | Readability levels and jargon tolerance |
| Voice calibration rules | 2 | Tech stack to voice style mapping |
| Script capabilities | 2 | analyze_codebase.py and analyze_readability.py flags |
| Reference file content | 2 | Cognitive load management, storytelling sources |
| Content quality gates | 5 | Gate pass/fail decision-making |
| Build-in-public workflow | 3 | Journey continuity, milestone mapping |

**Total:** 18 questions

### Content Quality Gates (New)

The content quality gates category tests **enforcement decisions**, not just comprehension. These questions present scenarios and ask whether the content passes or fails specific gates:

- Hook quality checks (blog post openings)
- Readability threshold enforcement (grade levels)
- Jargon density limits (audience-specific)
- Format-specific rules (Twitter thread prefixes)
- Evidence grounding requirements (Phase 3 gate)

### Build-in-Public Workflow

The build-in-public category tests understanding of **sustained content creation**:

- Journey Brief as persistent context
- Milestone-to-content-type mapping
- Content cascade timing (Twitter → LinkedIn → Blog → Newsletter)

---

## Running Evaluations

### Manual Testing

1. Load the code-to-content skill
2. For each question in `evaluation.xml`:
   - Ask Claude the question
   - Compare the response to the expected answer
   - Score 1 for exact match, 0 for mismatch

### Verification Method

Answers are verified using **exact string comparison**:

```python
score = 1 if response.strip() == expected_answer.strip() else 0
```

---

## XML Format

Questions are stored in `evaluation.xml` with this structure:

```xml
<evaluation>
  <qa_pair>
    <question>Your question text here</question>
    <answer>Single verifiable answer</answer>
  </qa_pair>
</evaluation>
```

---

## Answer Requirements

All answers are designed to be:

- **Verifiable** — Single, clear answer via string comparison
- **Stable** — Based on skill file content that doesn't change
- **Specific** — Exact phrases, numbers, or flag names
- **Independent** — No question depends on another's answer

---

## Files Referenced

Questions reference these skill files:

| File | Questions |
|------|-----------|
| `SKILL.md` | 9 questions (voice, audience, cognitive load, storytelling, gates) |
| `assets/templates/blog_post.md` | 1 question |
| `assets/templates/readme.md` | 1 question |
| `scripts/analyze_codebase.py` | 1 question |
| `scripts/analyze_readability.py` | 1 question |
| `references/checklists.md` | 2 questions (format-specific rules) |
| `references/build-in-public.md` | 3 questions (journey brief, milestones, cascade) |

---

## Expected Scores

A properly functioning skill should achieve:

| Score | Interpretation |
|-------|----------------|
| 18/18 | Skill files are correctly read and all logic understood |
| 15-17/18 | Minor issues with exact phrasing or enforcement decisions |
| <15/18 | Skill may not be loading files or enforcing gates correctly |

**Note:** 8 of 18 questions test decision-making or workflow understanding, not just recall. A model must correctly apply thresholds, rules, and journey patterns to pass these questions.

---

## Adding New Questions

When adding questions:

1. Ensure the answer exists verbatim in a skill file
2. Make the question specific enough for exact matching
3. Test the question yourself before adding
4. Add to appropriate category in the XML
