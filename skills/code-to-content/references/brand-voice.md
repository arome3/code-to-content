# Voice Implementation Instructions

Instructions for determining and applying voice when generating project content.

---

## Voice Source Priority

Voice is a person, not a programming language. A real voice is captured from the builder in Phase 2 (Differentiation Discovery); the tech-stack and domain tables below are **fallback heuristics**, used only when no founder voice was captured.

```
VOICE SOURCE PRIORITY (highest fidelity first):
1. FOUNDER VOICE (primary)   → captured in Phase 2: how they actually write,
                               especially what they REJECT (see next section).
                               A rough draft or voice-memo transcript outranks everything.
2. CODE COMMENT STYLE         → the voice already present in their own comments.
3. TECH-STACK / DOMAIN TABLES → community-norm fallback ONLY when 1 and 2 are absent.
                               These produce a competent, swappable default — never a
                               distinctive one. Treat as a floor, not a target.
```

If the Differentiation Brief contains a FOUNDER VOICE section, use it as the base voice and skip straight to "Adjust for Audience." Use the tables below to fill gaps, not to override a captured voice.

---

## Voice = What You Reject

The sharpest part of anyone's voice is what they refuse to do. A voice profile built from likes ("I like direct writing") is vague; one built from **rejections** is specific and enforceable.

Weak: *"Write in a clear, professional voice."*
Strong: *"Never use semicolons — they make it sound like a college essay. Never open with a definition. Never hedge a claim I actually believe. Contractions always."*

When capturing founder voice in Phase 2, prefer to record the anti-patterns:

```
FOUNDER VOICE — capture as rejections:
├── Words/phrases they would never use:  ___
├── Punctuation/structure they avoid:     ___  (e.g., "no semicolons", "no rule-of-three")
├── Formality they refuse:                ___  (e.g., "never corporate", "never cutesy")
├── Sentences they'd never sign:          ___  (paste one a competitor would write)
└── A line they HAVE written that sounds like them:  ___  (the positive anchor)
```

Apply the rejections as hard constraints during generation, and check them again in Phase 6 alongside the AI-tells blocklist in `differentiation.md`.

---

## Voice Calibration Sequence

Execute this sequence before generating any content.

### Step 1: Extract Voice Signals

If a captured FOUNDER VOICE exists, it is the base voice — these codebase signals only fill gaps. Identify from the codebase:

```
REQUIRED INPUTS:
├── tech_stack       → Languages, frameworks, tools detected
├── code_style       → Naming conventions, structure patterns
├── comment_style    → Documentation voice present in code
├── project_type     → Library, application, infrastructure, CLI, SDK
├── maturity         → Version number, API stability indicators
├── domain           → Problem space (fintech, healthcare, devtools)
└── target_users     → Inferred from complexity and context
```

### Step 2: Analyze Code Comments

Scan comments and match patterns to voice traits:

| Comment Pattern | Voice Trait to Apply |
|-----------------|----------------------|
| `// TODO: fix this hack` | Conversational, acknowledge imperfection |
| `/** @param {string} id */` | Technical, structured, precise |
| `# This is cursed but it works` | Personality permitted, pragmatic |
| `// See RFC 7231 section 6.5.1` | Authoritative, reference specifications |
| `/* Implements visitor pattern */` | Design-focused, assume pattern knowledge |
| Minimal or absent comments | Dense content, example-heavy, minimal narration |

---

## Apply Tech Stack Voice Rules (Fallback)

**Use only when no founder voice was captured.** These encode community norms, which makes them safe but swappable — every Rust project sounds "precise," every JS project sounds "conversational." They prevent a *wrong* voice, not a *generic* one. Set base voice characteristics from detected stack:

```
RUST:
├── Use precise, correctness-focused language
├── Address memory safety and performance explicitly
├── Maintain rigorous technical accuracy
└── OUTPUT: Authoritative, exact, safety-conscious

JAVASCRIPT/TYPESCRIPT:
├── Use pragmatic, ship-oriented framing
├── Emphasize developer experience
├── Allow casual phrasing
└── OUTPUT: Conversational, practical, inclusive

PYTHON:
├── Prioritize readability in explanations
├── Assume educational context welcome
├── Use clear, accessible language
└── OUTPUT: Clear, accessible, explanatory

GO:
├── Apply simplicity as primary value
├── Prefer explicit over clever explanations
├── Minimize unnecessary elaboration
└── OUTPUT: Direct, minimal, no-nonsense

JAVA/KOTLIN:
├── Use enterprise-appropriate formality
├── Reference patterns by name
├── Address maintenance concerns
└── OUTPUT: Formal, thorough, pattern-aware

ELIXIR/ERLANG:
├── Emphasize concurrency concepts
├── Frame around fault-tolerance
├── Allow enthusiasm for paradigm
└── OUTPUT: Enthusiastic, conceptual, resilient

INFRASTRUCTURE (Terraform, K8s, Docker):
├── Ground in operational reality
├── Address failure scenarios explicitly
├── Include safety warnings
└── OUTPUT: Practical, cautious, experienced
```

---

## Infer Audience and Calibrate

Determine audience from project characteristics:

### Map Complexity to Audience

```
MINIMAL DEPENDENCIES + CLEAR API:
└── Treat as: Broad audience, possibly beginners
└── Apply: Accessible language, define terms, step-by-step structure

COMPLEX TYPE SYSTEM + ADVANCED PATTERNS:
└── Treat as: Experienced developers
└── Apply: Assume fundamentals, focus on nuance

DOMAIN-SPECIFIC LOGIC + JARGON IN CODE:
└── Treat as: Domain experts
└── Apply: Domain terms permitted, explain only technical concepts

FRAMEWORK INTERNALS + METAPROGRAMMING:
└── Treat as: Power users, contributors
└── Apply: Deep technical detail, internal architecture permitted
```

### Apply Domain Adjustments

| Detected Domain | Adjustments to Apply |
|-----------------|---------------------|
| Fintech | Use precise language, acknowledge compliance considerations |
| Healthcare | Be thorough, document edge cases, no shortcuts |
| Gaming | Include performance context, reference benchmarks |
| Developer Tools | Show empathy for pain points, prioritize practical solutions |
| Education | Use progressive disclosure, patience in explanations |
| Enterprise | Address organizational concerns, maintain formality |
| Open Source | Welcome contribution, use inclusive framing |

---

## Calibrate Confidence: Two Kinds, Don't Confuse Them

A common mistake is to soften *everything* for early-stage projects. That is backward — early projects often hold the most contrarian, interesting conviction. Separate the two kinds of confidence:

```
EPISTEMIC confidence  → claims about STABILITY and facts.
                        Governed by maturity. Be honest. A v0.x API may change.
                        "This API is still settling" is truthful, not hedging.

RHETORICAL confidence → your THESIS and your OPINION (the WHY, the spiky claim).
                        NOT governed by maturity. Be bold at every version.
                        "We think most teams cache the wrong layer" is a v0.1 founder's
                        right and obligation to say.
```

The essay's point: hold conviction about *what you believe and why you built it*, regardless of how mature the code is. Hedge only the factual claim that could mislead someone about stability.

```
v0.x (EXPERIMENTAL):
├── Epistemic: be honest about churn — "expect this to change"
├── Rhetorical: state the thesis with full conviction — do NOT hedge the opinion
└── Result: stable about humility, spiky about belief

v1.0+ (STABLE → MATURE):
├── Epistemic: prescribe production use as it earns it
├── Rhetorical: same conviction; now backed by a track record
└── Result: authoritative on both axes
```

### Select Confidence Language

Apply hedges to **stability claims only**. Never hedge the thesis or opinion.

| About… | v0.x | v1.x+ |
|--------|------|-------|
| **Stability / facts** (epistemic) | "still settling", "expect changes", "early" | "stable", "production-ready", "battle-tested" |
| **Thesis / opinion** (rhetorical) | Bold at any version — "we believe", "most teams get this wrong", "the right move is" | Bold — same |

> Anti-pattern (do not do this): softening the *opinion* because the version is low — "this might possibly be a slightly better approach for some users, perhaps." That is the committee voice the swap-the-name test is built to catch.

---

## Apply Project Type Voice

Shape content based on project type:

```
LIBRARY:
├── Prioritize API clarity
├── Lead with examples
├── Focus on integration scenarios
├── Address versioning implications
└── OUTPUT: Precise, example-rich, integration-focused

APPLICATION:
├── Frame around user tasks
├── Emphasize benefits over mechanics
├── Use workflow language
└── OUTPUT: Task-oriented, benefit-focused, empathetic

INFRASTRUCTURE:
├── Address operational concerns
├── Document failure modes
├── Include monitoring/configuration context
└── OUTPUT: Operational, thorough, safety-conscious

FRAMEWORK:
├── Establish conventions clearly
├── Explain pattern rationale
├── Maintain ecosystem coherence
└── OUTPUT: Opinionated, pattern-focused, cohesive

CLI TOOL:
├── Optimize for scannability
├── Document flags/options densely
├── Show composition with other tools
└── OUTPUT: Terse, scannable, reference-style

SDK:
├── Lead with authentication
├── Cover error handling patterns
├── Show multi-language examples when applicable
└── OUTPUT: Integration-focused, error-aware
```

---

## Voice Application Order

Apply voice in this sequence:

1. **Establish Base Voice** - Set initial formality and community tone from tech stack
2. **Adjust for Audience** - Modify assumed knowledge level and explanation depth
3. **Calibrate Confidence** - Set prescriptiveness level from project maturity
4. **Apply Project Type Focus** - Shape content structure and emphasis
5. **Layer Domain Modifiers** - Add domain-specific concerns and terminology rules

---

## Position on Voice Spectrums

For each content piece, determine position:

```
FORMALITY:
Formal ←————————→ Casual
└── Tech stack + domain determine position

DENSITY:
Dense ←————————→ Accessible
└── Audience expertise determines position

PRESCRIPTIVENESS:
Hedging ←————————→ Prescriptive
└── Maturity determines position

OPINION:
Reserved ←————————→ Opinionated
└── Default to Opinionated. The WHY and the spiky claim are the point of the piece.
    Dial back ONLY for reference material (API docs) where the reader wants facts, not a thesis.
```

---

## Apply Content-Type Modifiers

Adjust voice based on content type being generated:

### README
- Increase accessibility
- Front-load value proposition
- Maintain project voice but lower barrier

### API Reference
- Increase precision
- Maximize scannability
- Minimize prose

### Tutorial
- Increase patience
- Use progressive disclosure
- Add encouragement at milestones

### Conceptual Guide
- Allow more depth
- Explain "why" thoroughly
- Connect to broader patterns

---

## Quick Voice Determination

When rapid voice selection needed:

```
1. WHO reads this?           → Set complexity level
2. WHAT do they need to do?  → Set content focus
3. HOW certain can I be?     → Set prescriptiveness
```

---

## Voice Anti-Patterns

| Avoid | Reason | Instead |
|-------|--------|---------|
| Generic voice for all projects | Swappable; no one's voice | Capture founder voice in Phase 2; tech-stack table is fallback only |
| Hedging the opinion because the version is low | Kills conviction; reads as committee | Hedge stability claims only; keep the thesis bold (epistemic vs rhetorical) |
| Same *stability* claims for v0.1 and v3.0 | Misleads about maturity | Match epistemic confidence to maturity |
| Library voice for infrastructure | Wrong operational focus | Match project type |
| Ignoring code comment style | Disconnects from codebase | Mirror existing patterns |
| Over-casual for enterprise | Loses credibility | Match domain expectations |
| Over-formal for JS ecosystem | Feels foreign | Match community norms |
