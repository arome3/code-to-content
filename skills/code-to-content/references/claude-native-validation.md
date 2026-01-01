# Claude-Native Validation Reference

Use this validation protocol when Python scripts (`analyze_readability.py`, `validate_content.py`) are unavailable. This provides equivalent quality gates using inline analysis.

---

## When to Use This

- Python environment not available
- Scripts not installed or configured
- Quick validation needed without setup
- Running in environments without file system access

---

## Readability Validation Protocol

### Step 1: Grade Level Estimation

Analyze the content for complexity indicators:

**Grade Level Heuristics:**

| Indicator | Adds to Grade |
|-----------|---------------|
| Average sentence > 20 words | +2 |
| Passive voice > 20% | +1 |
| Technical terms without definition | +1 per 3 terms |
| Nested clauses (3+ per paragraph) | +1 |
| Abstract concepts without examples | +2 |

**Base grade:** 6 (simple prose)

**Calculate:** Base + indicators = estimated grade level

### Step 2: Jargon Density Check

Count technical terms per 100 words:

```
Jargon Density = (technical terms / total words) × 100
```

**Technical term definition:** Domain-specific words a general developer might not know.

**Thresholds:**
| Audience | Max Jargon |
|----------|------------|
| Beginner | 2% |
| Intermediate | 4% |
| Expert | 8% |

### Step 3: Code-to-Prose Ratio

Count lines of code vs. paragraphs of prose:

```
Ratio = prose paragraphs : code blocks
```

**Thresholds:**
| Audience | Target Ratio |
|----------|--------------|
| Beginner | 2:1 (more prose) |
| Intermediate | 1:1 (balanced) |
| Expert | 1:2 (more code) |

---

## Content Quality Validation

### Hook Quality Check

**PASS if first paragraph:**
- [ ] Creates curiosity or states surprising result
- [ ] Does NOT start with "In this article..."
- [ ] Establishes stakes within 2-3 sentences
- [ ] Makes reader want to continue

**FAIL indicators:**
- Generic opening ("Today we'll discuss...")
- Meta-commentary about the article itself
- No clear value proposition

### Evidence Grounding Check

For each technical claim, verify:

```
CLAIM: [statement]
EVIDENCE TYPE: [code | metric | commit | quote]
SOURCE: [file:line | commit hash | measurement]
VERIFIED: [yes/no]
```

**PASS:** 100% of claims have verified evidence
**FAIL:** Any ungrounded claim

### Structure Check

**Required elements by format:**

| Format | Must Have |
|--------|-----------|
| Blog Post | Hook, Problem, Insight, Solution, Takeaway |
| Tutorial | Objective, Prerequisites, Steps, Checkpoints, Next Steps |
| Twitter Thread | Hook tweet, Context, Insight, CTA, <280 chars each |
| README | One-liner, Problem, Solution, Quick Start, Install |
| Newsletter | Subject, Hook, Value, Personal voice, CTA |

### Voice Consistency Check

Read the first and last paragraphs aloud (mentally).

**PASS if:**
- Same tone and formality throughout
- Consistent use of "I/we/you"
- No jarring shifts in technical depth

---

## Validation Output Template

After running validation, output:

```markdown
## Validation Results

### Readability
- **Grade Level:** X.X (target: ≤Y for [audience])
- **Jargon Density:** X% (target: ≤Y%)
- **Code Ratio:** X:X (target: X:X)
- **Status:** ✅ PASS / ❌ FAIL

### Quality Gates
- **Hook Quality:** ✅/❌
- **Evidence Grounding:** ✅/❌ ([X/Y] claims verified)
- **Structure Complete:** ✅/❌
- **Voice Consistent:** ✅/❌

### Overall: ✅ APPROVED FOR DELIVERY / ❌ REVISIONS NEEDED

### Issues to Address (if any):
1. [Issue with location and fix]
2. [Issue with location and fix]
```

---

## Quick Validation Checklist

For rapid validation, run this abbreviated check:

```
QUICK VALIDATION (30 seconds):

[ ] Hook creates curiosity (not "In this article...")
[ ] All code examples from actual codebase
[ ] Single audience, consistent tone
[ ] Clear takeaway/CTA at end
[ ] No unverified performance claims

If all checked: ✅ PROCEED
If any unchecked: Run full validation above
```

---

## Comparison: Script vs. Claude-Native

| Aspect | Python Scripts | Claude-Native |
|--------|----------------|---------------|
| Speed | ~2 seconds | ~10 seconds |
| Accuracy | Precise metrics | Estimated metrics |
| Dependencies | Python + packages | None |
| Best for | Final validation | Quick checks, no-Python environments |

**Recommendation:** Use Python scripts for final delivery when available. Use Claude-native for iterative drafting and environments without Python.
