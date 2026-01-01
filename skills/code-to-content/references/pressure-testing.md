# Pressure Testing Methodology

A systematic approach to testing skill robustness under challenging conditions. Based on the "superpowers" pattern for skill validation.

---

## What is Pressure Testing?

Pressure testing validates that a skill produces quality outputs even when:
- Input is ambiguous or incomplete
- Edge cases are encountered
- Multiple constraints conflict
- The user provides minimal guidance

A skill that only works under ideal conditions is not production-ready.

---

## Testing Dimensions

### 1. Input Variety Testing

Test across diverse input types:

| Input Type | Test Case | Expected Behavior |
|------------|-----------|-------------------|
| **Minimal** | Single file with no README | Extracts what's available, asks for clarification |
| **Standard** | Typical project structure | Full 5-phase process works |
| **Complex** | Monorepo with 50+ packages | Focuses on subset, manages scope |
| **Ambiguous** | No clear "aha moment" | Generates multiple angle options |
| **Non-English** | Comments in other languages | Handles gracefully, notes limitation |

### 2. Format Stress Testing

Test each format under constraints:

| Format | Stress Test | Pass Criteria |
|--------|-------------|---------------|
| Twitter Thread | Topic with no natural breaks | Still creates coherent 5-12 tweet flow |
| Tutorial | Complex multi-step process | Breaks into digestible steps with checkpoints |
| Blog Post | Dry technical topic | Finds compelling angle anyway |
| README | Project with no clear value prop | Asks for clarification or infers best-effort |

### 3. Audience Boundary Testing

Test at audience skill boundaries:

```
Beginner content with expert topic → Should simplify or reject
Expert content for beginner audience → Should flag mismatch
Mixed audience request → Should refuse and ask for single audience
```

### 4. Gate Failure Testing

Deliberately trigger each gate failure:

| Gate | Failure Trigger | Expected Behavior |
|------|-----------------|-------------------|
| Phase 1 | Empty repository | STOP with "No content-worthy insights" |
| Phase 2 | "Write for everyone" | STOP with "Select single audience" |
| Phase 3 | Request unverifiable claim | Refuse claim or find evidence |
| Phase 4 | Conflicting optimization requests | Prioritize and explain trade-offs |
| Phase 5 | Content fails readability | Revise until passes |

---

## Testing Protocol

### Pre-Test Setup

1. **Clone test repositories** representing:
   - Different languages (Python, Go, TypeScript, Rust)
   - Different sizes (tiny, medium, large)
   - Different maturity (new, established, legacy)

2. **Prepare edge case inputs:**
   - Empty project
   - Project with only binary files
   - Project with massive files (>10MB)
   - Project with no git history

### Execution Protocol

For each test case:

```markdown
## Test Case: [Name]

**Input:** [Description of input conditions]
**Format Requested:** [Blog/Tutorial/Twitter/etc.]
**Expected Outcome:** [What should happen]

### Execution Log

1. Phase 1: [PASS/FAIL] - [Notes]
2. Phase 2: [PASS/FAIL] - [Notes]
3. Phase 3: [PASS/FAIL] - [Notes]
4. Phase 4: [PASS/FAIL] - [Notes]
5. Phase 5: [PASS/FAIL] - [Notes]

### Quality Assessment

- Hook Quality: [1-10]
- Evidence Grounding: [1-10]
- Audience Fit: [1-10]
- Structure: [1-10]
- Overall: [1-10]

### Issues Found

- [Issue description and severity]

### Verdict: [PASS/FAIL]
```

### Post-Test Analysis

After all tests complete:

1. **Calculate pass rate** per dimension
2. **Identify failure patterns** (are failures clustered?)
3. **Prioritize fixes** by severity × frequency
4. **Document edge cases** for future reference

---

## Minimum Viable Test Suite

For quick validation, run at least these 5 tests:

### Test 1: Happy Path
- **Input:** Well-structured open source project with git history
- **Format:** Blog post for intermediate developers
- **Expected:** Full 5-phase process completes with quality content

### Test 2: Minimal Input
- **Input:** Single Python script, no README
- **Format:** Twitter thread
- **Expected:** Extracts available insight, produces valid thread

### Test 3: Wrong Audience Request
- **Input:** Complex cryptography project
- **Format:** Tutorial for beginners
- **Expected:** Flags difficulty, suggests intermediate or simplifies scope

### Test 4: Gate Failure Recovery
- **Input:** Valid project, but request unverifiable performance claim
- **Format:** Blog post
- **Expected:** Refuses claim or finds alternative evidence

### Test 5: Quick Mode
- **Input:** Clear topic, no codebase
- **Format:** Quick LinkedIn post
- **Expected:** Skips analysis phases, delivers directly

---

## Scoring Rubric

### Overall Skill Score

| Score | Criteria |
|-------|----------|
| 9.5-10 | All 5 tests pass, no critical issues, graceful edge case handling |
| 9.0-9.4 | All happy paths pass, minor issues with edge cases |
| 8.0-8.9 | Most tests pass, some gate enforcement gaps |
| 7.0-7.9 | Core functionality works, multiple edge case failures |
| < 7.0 | Fundamental issues with gate enforcement or quality |

### Dimension Scores

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Input Handling | 20% | Deals with variety and edge cases |
| Format Quality | 25% | Outputs match format requirements |
| Audience Fit | 20% | Content matches declared audience |
| Gate Enforcement | 25% | Gates prevent bad outputs |
| Recovery | 10% | Graceful handling of failures |

---

## Test Repository Recommendations

### Easy (Validation)
- **RecoverPy** — Clean Python CLI, clear architecture
- **lottie-react** — Small React library, focused scope

### Medium (Stress)
- **gin-boilerplate** — Go project, multiple components
- **vanilla-calendar-pro** — TypeScript, framework-agnostic

### Hard (Edge Cases)
- **Large monorepo** — Tests scope management
- **Legacy codebase** — Tests insight extraction
- **Minimal project** — Tests minimal input handling

---

## Continuous Improvement

After each pressure testing round:

1. **Update skill based on findings**
2. **Add new test cases** for discovered issues
3. **Re-run failed tests** to verify fixes
4. **Document lessons learned**

Pressure testing is not a one-time activity—run it after every significant skill update.
