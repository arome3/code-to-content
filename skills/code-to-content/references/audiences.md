# Audience Determination and Content Calibration

Instructions for determining target audience and calibrating content accordingly.

---

## Determine Content Audience

When the user requests content about their project, establish the target audience through this sequence:

### Step 1: Gather Context

Ask or infer:
- What is the project? (complexity, tech stack, domain)
- Who uses the project? (their skill level, roles)
- What is the content goal? (authority, reach, hiring, community)
- What format is intended? (blog, tutorial, talk, social)

### Step 2: Apply Goal-to-Audience Mapping

| User's Goal | Recommend This Audience |
|-------------|------------------------|
| Build authority / personal brand | Peers at same expertise level |
| Grow following / maximize reach | One level below user's expertise |
| Portfolio / get hired | Hiring managers and senior engineers |
| Help project community | Project's actual users |
| Quick social content | Broad developer audience |
| Deep technical content | Domain specialists |
| Conference presentation | Self-selecting attendees |

### Step 3: Validate Against Project Complexity

Assess project complexity and confirm audience is realistic:

**Simple projects** (few dependencies, clear API):
- Can target: complete beginners, broad audiences, non-technical stakeholders
- Tutorial-style content works well
- Wide reach is achievable

**Moderate projects** (standard stack, common patterns):
- Can target: intermediate developers (sweet spot), beginners with guidance
- Balance explanation with depth
- Good for practical how-to content

**Complex projects** (advanced patterns, specialized domain):
- Best for: experienced developers, domain specialists
- Difficult to reach: general audiences, complete beginners
- Focus on depth over breadth

If user requests an audience that mismatches project complexity, flag this:
- "Your project's complexity may require more scaffolding for beginners"
- "A specialized project like this will resonate most with experienced developers"

---

## Calibrate Explanation Depth

Once audience is established, apply these calibration rules throughout content generation:

### For Beginner Audiences

**Explain:**
- What the problem is and why it matters
- Every tool, library, and concept used
- Why each step is necessary
- Common mistakes and how to avoid them
- How to verify success at each stage

**Assume only:**
- Basic programming ability
- Ability to follow instructions
- Motivation to learn

**Tone directives:**
- Use encouraging language
- Be thorough without being condescending
- Acknowledge progress points
- Include analogies to familiar concepts

### For Intermediate Audiences

**Explain:**
- The specific approach and rationale
- Trade-offs considered
- Non-obvious gotchas and edge cases
- Connections to patterns they likely know

**Assume:**
- Comfort with stack basics
- Familiarity with common patterns
- Can read code without line-by-line walkthrough
- Will research unfamiliar terms independently

**Tone directives:**
- Write peer-to-peer
- Be practical and efficient
- Respect their time
- Skip obvious boilerplate

### For Expert/Peer Audiences

**Explain:**
- What is novel or different about this approach
- Edge cases and failure modes
- Performance characteristics and benchmarks
- Contrarian positions and their justification

**Assume:**
- Deep domain familiarity
- Can infer implementation from description
- Will evaluate approach critically
- Interested in nuance and trade-offs

**Tone directives:**
- Write densely
- State opinions directly
- Maintain technical precision
- Engage with complexity

### For Hiring Manager Audiences

**Explain:**
- The business problem and measurable impact
- Decision-making process and alternatives considered
- Metrics and outcomes achieved
- Retrospective insights (what would change)
- Collaboration and team dynamics

**Assume:**
- Technical background but not specialist depth
- Evaluating judgment, not just skills
- Limited time, scanning for signal
- Comparing against other candidates

**Tone directives:**
- Lead with results
- Show clear ownership
- Project confidence
- Quantify where possible

---

## Apply Audience-Specific Tone

Match writing characteristics to the determined audience:

| Audience | Sentence Structure | Vocabulary | Examples | Pacing |
|----------|-------------------|------------|----------|--------|
| Beginners | Short, clear sentences | Define jargon | Complete, runnable | Step-by-step |
| Intermediate | Moderate complexity | Standard jargon OK | Show interesting parts | Brisk but thorough |
| Experts | Dense, compound | Technical terminology | Edge cases, failures | Jump to insights |
| Hiring managers | Clear, outcome-focused | Business + technical | Impact metrics | Scannable sections |

---

## Enforce Audience Consistency

Throughout content generation, maintain these constraints:

### Single Audience Rule
Generate content for ONE audience per piece. If user requests mixed audiences:
- Recommend separate pieces for each audience
- Or identify primary audience and note secondary adaptations

### Assumption Consistency
Track what has been assumed vs. explained. Do not:
- Explain basics then assume advanced concepts
- Switch between beginner explanations and expert shorthand
- Mix encouraging tone with dense technical prose

### Format-Audience Alignment
Verify format matches audience expectations:

| Format | Best Audiences | Poor Fit |
|--------|---------------|----------|
| Tutorial | Beginners, Intermediates | Experts |
| Deep-dive blog | Intermediates, Experts | Beginners |
| Quick tips / social | Broad audiences | Specialists |
| Case study | Hiring managers, Peers | Beginners |
| Reference docs | Project users at any level | General audiences |

---

## Handle Ambiguous Audience Requests

When user does not specify audience clearly:

1. **Infer from goal**: If user states a goal, map to recommended audience
2. **Infer from format**: Tutorial implies learners; case study implies evaluators
3. **Ask directly**: "Who should this content be for? Options: [contextual suggestions]"
4. **Default intelligently**: For general content requests, default to one level below user's apparent expertise

### Clarifying Questions

Use when audience is unclear:
- "Is this for developers new to [domain] or those already working in it?"
- "Should this showcase your decision-making (portfolio) or teach the technique (tutorial)?"
- "Are you targeting your project's existing users or a broader developer audience?"

---

## Output: Audience Declaration

When generating content, internally establish and maintain:

```
TARGET AUDIENCE: [specific group]
ASSUMED KNOWLEDGE: [list]
WILL EXPLAIN: [list]
TONE: [descriptor]
```

Reference this declaration when making content decisions about:
- What to explain vs. skip
- How much context to provide
- Level of technical detail
- Voice and encouragement level
- Example complexity
