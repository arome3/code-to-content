# Readability Validation Guide

Claude-native replacement for `analyze_readability.py`. Use these protocols to validate content meets audience requirements.

---

## Audience Thresholds (MUST PASS)

| Audience | Max Grade Level | Max Jargon Density | Prose:Code Ratio |
|----------|-----------------|-------------------|------------------|
| Beginner | 8.0 | 2% | 2:1 (more prose) |
| Intermediate | 12.0 | 4% | 1:1 (balanced) |
| Expert | 16.0 | 8% | 0.5:1 (code-heavy OK) |

---

## Quick Validation Checklist

Run this for fast verification:

### Sentence Check
- [ ] No sentence exceeds 30 words
- [ ] Average sentence length: 15-20 words
- [ ] Varied sentence lengths (not all same length)

### Paragraph Check
- [ ] No paragraph exceeds 150 words
- [ ] Each paragraph has ONE main idea
- [ ] Visual breaks every 3-4 paragraphs

### Jargon Check (for beginners)
- [ ] All technical terms defined on first use
- [ ] Jargon linked to documentation when possible
- [ ] Acronyms spelled out on first use

### Structure Check
- [ ] Clear heading hierarchy (H2 > H3 > H4)
- [ ] Lists used for 3+ related items
- [ ] Code blocks have language specified

---

## Detailed Validation Protocol

### Step 1: Grade Level Estimation

Use the **Flesch-Kincaid formula** on a sample paragraph (100+ words):

```
Grade Level = 0.39 × (total words / total sentences) + 11.8 × (total syllables / total words) - 15.59
```

**Quick estimation method:**
1. Take a 100-word sample
2. Count sentences → divide 100 by this number = words per sentence
3. Count syllables in 10 random words → multiply by 10 for estimate
4. Apply formula

**Syllable counting rules:**
- Count vowel sounds (a, e, i, o, u, sometimes y)
- Silent 'e' at end doesn't count
- Diphthongs (ea, ou, ai) count as one
- Examples: "de-vel-op-er" = 4, "code" = 1, "im-ple-ment" = 3

### Step 2: Jargon Density Check

Count occurrences of these technical terms in your content:

**General Tech Jargon:**
- API, REST, GraphQL, SDK, CLI, CRUD, ORM, MVC
- DOM, CSS, HTML, JSON, XML, YAML, SQL
- async, callback, promise, observable
- immutable, stateless, idempotent, atomic

**DevOps Jargon:**
- CI/CD, Docker, Kubernetes, terraform
- microservices, container, pipeline, deployment

**Database Jargon:**
- index, schema, migration, query, join
- normalization, sharding, replication

**Architecture Jargon:**
- singleton, factory, facade, proxy
- observer, strategy, decorator, adapter

**Calculate density:**
```
Jargon Density = (jargon term count / total word count) × 100
```

### Step 3: Passive Voice Detection

Search for these patterns:
- "is/are/was/were + [verb]ed"
- "has been", "have been", "had been"
- "will be", "would be", "should be"

**Examples of passive voice to revise:**
| Passive | Active |
|---------|--------|
| "The function was called by the handler" | "The handler called the function" |
| "The error is thrown when..." | "The system throws an error when..." |
| "Data is stored in the cache" | "The cache stores data" |

**Target:** Less than 10% of sentences should use passive voice.

### Step 4: Weak Language Check

Flag and consider removing:

**Hedge words:**
- maybe, perhaps, possibly, probably
- somewhat, slightly, kind of, sort of
- a bit, a little, fairly, rather
- quite, basically, essentially, just

**Filler phrases:**
- "in order to" → "to"
- "due to the fact that" → "because"
- "it is important to note that" → [delete, just state it]
- "in terms of" → [rephrase directly]
- "at the end of the day" → [delete]
- "in this article" → [delete]
- "as previously mentioned" → [delete or link directly]

### Step 5: Code-to-Prose Ratio

For technical content:
1. Count lines of code (inside code blocks)
2. Count lines of prose (outside code blocks)
3. Calculate ratio

**Guidelines:**
- Tutorials: More prose than code (explain each step)
- Reference docs: More code than prose (examples first)
- Blog posts: Balanced (code supports narrative)

---

## Improvement Suggestions Generator

After analysis, provide actionable improvements:

### If Grade Level Too High

1. **Break long sentences:**
   - Split at conjunctions (and, but, or)
   - One idea per sentence

2. **Simplify vocabulary:**
   - "utilize" → "use"
   - "implement" → "build" or "add"
   - "facilitate" → "help" or "make easier"

3. **Add transitions:**
   - "First...", "Next...", "Finally..."
   - "Because of this...", "As a result..."

### If Jargon Density Too High

1. **Define on first use:**
   - "An API (Application Programming Interface) lets..."

2. **Link to resources:**
   - "Using [REST](link-to-explainer) endpoints..."

3. **Use analogies:**
   - "Think of an API as a waiter taking your order..."

### If Structure Issues

1. **Add subheadings** every 300-400 words
2. **Convert paragraphs to lists** when listing features/steps
3. **Add code comments** for complex examples
4. **Use bold** for key terms and actions

---

## Validation Output Template

After validation, produce this report:

```markdown
## Readability Report

### Metrics
- **Grade Level:** [X] (Target: [Y] for [audience])
- **Jargon Density:** [X]% (Target: ≤[Y]%)
- **Code:Prose Ratio:** [X:Y]

### Pass/Fail
- [ ] Grade level: [PASS/FAIL]
- [ ] Jargon density: [PASS/FAIL]
- [ ] Sentence length: [PASS/FAIL]
- [ ] Paragraph length: [PASS/FAIL]

### Issues Found
1. [Issue with location and suggestion]
2. [Issue with location and suggestion]

### Verdict
[PASS - Ready for delivery] OR [FAIL - Needs revision: specific issues]
```
