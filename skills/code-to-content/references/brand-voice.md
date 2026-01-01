# Voice Implementation Instructions

Instructions for determining and applying voice when generating project content.

---

## Voice Calibration Sequence

Execute this sequence before generating any content.

### Step 1: Extract Voice Signals

Identify these signals from the codebase:

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

## Apply Tech Stack Voice Rules

Set base voice characteristics from detected stack:

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

## Calibrate Confidence by Maturity

Adjust prescriptiveness based on project version:

```
v0.x (EXPERIMENTAL):
├── Hedge appropriately: "This approach works for now"
├── Invite feedback: "We're exploring patterns here"
├── Warn of instability: "Expect changes in future versions"
└── Apply: Low prescriptiveness, exploratory tone

v1.0 (INITIAL STABLE):
├── Balance confidence: "This is the recommended approach"
├── Acknowledge gaps: "Advanced cases still being documented"
├── Use "should" over "must"
└── Apply: Moderate prescriptiveness

v2.x-3.x (MATURE):
├── Be authoritative: "Use this pattern for production"
├── Reference established practices
├── Prescribe directly: "Do X, then Y"
└── Apply: High prescriptiveness

v4.0+ (LEGACY):
├── Acknowledge existing implementations
├── Prioritize migration clarity
├── Address backward compatibility
└── Apply: Authoritative but careful
```

### Select Confidence Language

| Maturity | Use | Avoid |
|----------|-----|-------|
| v0.x | "might", "consider", "currently" | "always", "must", "the right way" |
| v1.x | "should", "recommended", "typically" | "must", "only way" |
| v2.x+ | "use", "do", "the pattern for" | excessive hedging |

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
└── Project type determines position
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
| Generic voice for all projects | Ignores community norms | Derive from tech stack |
| Same confidence for v0.1 and v3.0 | Misleads about stability | Match to maturity |
| Library voice for infrastructure | Wrong operational focus | Match project type |
| Ignoring code comment style | Disconnects from codebase | Mirror existing patterns |
| Over-casual for enterprise | Loses credibility | Match domain expectations |
| Over-formal for JS ecosystem | Feels foreign | Match community norms |
