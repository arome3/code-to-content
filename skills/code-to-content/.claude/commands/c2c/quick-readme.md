# /c2c:quick-readme

Generate a README quickly with sensible defaults.

**Usage:** `/c2c:quick-readme [project-path or description]`

**When to use:** Fast READMEs for simple projects or updates. Skip for complex projects needing comprehensive documentation.

---

## Mode: QUICK (Reduced Verification)

**Skipped phases:** 1 (deep analysis), 2 (audience selection)

**Defaults applied:**
- Primary audience: New users who want to get started quickly
- Voice: Clear, scannable, action-oriented
- Focus: Quick Start over comprehensive docs

---

## Content Generation

Generate a README with this essential structure:

### 1. Title + One-liner
```markdown
# Project Name

Brief description of what it does and why it matters (1-2 sentences).
```

### 2. Quick Start (MOST IMPORTANT)
- Get users running in < 5 minutes
- Copy-paste ready commands
- Include expected output

```markdown
## Quick Start

\`\`\`bash
npm install project-name
\`\`\`

\`\`\`javascript
// Minimal working example
\`\`\`
```

### 3. Installation
- Step-by-step setup
- Prerequisites listed
- Common gotchas noted

### 4. Basic Usage
- 2-3 common use cases with code
- Keep examples minimal and practical

### 5. Configuration (if applicable)
- Table format for options
- Sensible defaults noted

### 6. License
- One line with license type

---

## Optional Sections

Add only if essential:
- API Reference (for libraries)
- Architecture (for complex systems)
- Contributing (for open source)
- Troubleshooting (for common issues)

---

## Lite Verification

Before delivery, verify:
- [ ] One-liner explains what + why
- [ ] Quick Start is copy-paste ready
- [ ] No placeholder text (e.g., "Add description here")
- [ ] Code examples use actual project syntax

---

## Output Format

Provide the complete README in markdown format.

Include at the end:
```
---
Sections included: [list]
Estimated read time: [X minutes]
Suggested badges: [if applicable]
```
