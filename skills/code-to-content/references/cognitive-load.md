# Cognitive Load Optimization

Apply these rules when generating content to minimize reader cognitive load and maximize comprehension.

---

## Calibrate Explanation Depth

Assess project complexity and adjust output accordingly:

**Low complexity** (complexity score 1-3, dependencies < 10):
- Combine concept and implementation in single-pass explanations
- Skip scaffolding analogies
- Proceed directly to practical usage

**Medium complexity** (complexity score 4-6, dependencies 10-30):
- Present concept first, then implementation (two-layer approach)
- Group related ideas into concept clusters
- Include analogies for unfamiliar patterns only

**High complexity** (complexity score 7-10, dependencies > 30):
- Implement multi-layer progressive disclosure
- Decompose topics into prerequisite chains
- Insert checkpoint summaries after each major topic
- Build mental models before showing implementation

---

## Analyze Prerequisites

When the project has dependencies, generate prerequisite context:

**Step 1: Classify each dependency**
- Runtime frameworks (React, Express, Django) = Require conceptual familiarity
- Build tools (Webpack, Vite) = Require awareness only
- Type systems (TypeScript) = Affects code example presentation
- Domain libraries (Prisma, TensorFlow) = Often core prerequisite knowledge
- Utility libraries (lodash, date-fns) = No prerequisite needed

**Step 2: Extract prerequisite concepts**
For each major dependency, determine:
- What mental model does this require?
- Is it standard (assume known) or specialized (explain)?
- Does the project use it idiomatically or unusually?

**Step 3: Produce three prerequisite lists**
- "Must understand" = Blocking prerequisites readers cannot proceed without
- "Helpful to know" = Concepts that accelerate understanding
- "Will be explained" = Concepts covered in generated content

---

## Sequence by Architecture Type

Order explanations based on detected architecture:

**Layered architecture** (Controllers, Services, Repositories):
1. Start with data models (what flows through layers)
2. Explain repository layer (data access)
3. Cover service layer (business logic)
4. End with controller layer (HTTP interface)

**Microservices architecture:**
1. Start with service boundaries (what each service owns)
2. Explain communication patterns (how services talk)
3. Deep-dive into one representative service
4. Cover cross-cutting concerns (auth, logging)

**Event-driven architecture:**
1. Start with event catalog (what events exist)
2. Explain producer patterns (what triggers events)
3. Cover consumer patterns (what reacts to events)
4. Trace event flow for one complete use case

**Monolithic/MVC architecture:**
1. Start with request lifecycle overview
2. Explain model layer (data and business rules)
3. Cover controller layer (request handling)
4. End with view layer (response rendering)

**Plugin/extension architecture:**
1. Start with core system behavior
2. Explain extension points (where plugins hook in)
3. Cover plugin lifecycle (load, execute, unload)
4. Walk through one example plugin

---

## Apply Progressive Disclosure

Map directory structure to disclosure layers and expose content accordingly:

**Layer 1 - Foundation:** Core utilities, shared types, base classes
- Introduce first
- Explain fully

**Layer 2 - Domain:** Models, domain logic, business entities
- Explain when needed for understanding subsequent content

**Layer 3 - Application:** Services, API handlers, main functionality
- Provide full explanation with examples
- This is the primary content layer

**Layer 4 - Advanced:** Middleware, plugins, extensions, optimizations
- Mark as optional or advanced
- Explain only when explicitly relevant

**Reference:** Configuration, tests, scripts
- Point to but do not explain in detail
- Use tests as usage examples when helpful

---

## Chunk by Concept Clusters

Group explanations by files that work together:

**Chunking rules to follow:**
- One concept cluster = one major section
- Explain the cluster's purpose before individual files
- Show how files in the cluster interact
- Use the same cluster as consistent example throughout related sections
- Never split a cluster's explanation across multiple sections

**Working memory constraints to enforce:**
- Maximum 4 files or concepts per cluster explanation
- If cluster exceeds 4 files, identify "core" vs "supporting" files
- Explain core files fully; reference supporting files briefly
- Provide cluster diagram as quick reference when helpful

---

## Scaffold Unfamiliar Abstractions

When generating explanations of key abstractions, apply scaffolding based on type:

**Standard patterns** (Repository, Factory, Observer):
- State the pattern name
- Provide one-sentence reminder
- Explain project-specific usage

**Custom implementations of known patterns:**
- Name the base pattern
- Explain how this version differs
- State design rationale for differences

**Project-specific abstractions:**
- Provide analogy to something familiar
- Give concrete example with code
- Extract the abstract pattern
- Show multiple instances if available

**Emergent patterns** (unnamed but repeated):
- Name the pattern explicitly
- Explain its purpose
- Show two or three instances

---

## Signal Complexity

Mark each generated section with complexity indicators:

**Simple sections** (small files, few imports, straightforward logic):
- Label as "Quick concept" with ~5 minute read time

**Moderate sections** (medium files, standard patterns, some interconnection):
- Label as "Core concept" with ~15 minute read time
- List prerequisite sections

**Complex sections** (large files, many imports, high cyclomatic complexity):
- Label as "Deep dive" with ~30+ minute read time
- List prerequisite sections
- Recommend prior reading if applicable

**Translate metrics to reader signals:**
- High connectivity = "This module is central to the system"
- Low complexity = "Good starting point for understanding"
- High complexity + low centrality = "Advanced topic, return to later"
- Utility code = "Reference only, not for primary learning"

---

## Insert Comprehension Checkpoints

Place checkpoints at these boundaries:
- After explaining each concept cluster
- After covering each architecture layer
- Before transitioning to new directory or subsystem
- After any section marked as complex
- Before optional or advanced content

**Each checkpoint must include:**
1. Summary of concepts just covered
2. Connection to what comes next
3. One or two verification questions readers should be able to answer
4. Suggested exploration task in actual codebase

---

## Pre-Output Verification

Before finalizing content, verify these requirements:

**Structure verification:**
- Complexity score determined explanation depth
- Dependencies mapped to prerequisite categories
- Architecture type determined topic sequence
- File structure mapped to progressive disclosure layers
- Module organization informed concept clusters
- Key abstractions classified by scaffolding needs

**Section-level verification:**
- Complexity signal displayed (quick/core/deep dive)
- Prerequisites listed for non-trivial sections
- One concept cluster per major section maximum
- Examples use consistent files from same cluster
- Checkpoint present at section end

**Reader experience verification:**
- New concepts introduced one at a time
- Each concept builds on previously explained material
- Working memory not overloaded (4 items maximum per explanation)
- Clear signals distinguish optional from required reading
