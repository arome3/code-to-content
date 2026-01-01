# Codebase Analysis Protocol

Claude-native replacement for `analyze_codebase.py`. Use these structured prompts to analyze any codebase for technical writing content.

---

## Quick Analysis (5 minutes)

Run this for fast content ideation:

### 1. Tech Stack Detection

Read these files (if they exist):
- `package.json` → Node.js dependencies and scripts
- `requirements.txt` or `pyproject.toml` → Python dependencies
- `Cargo.toml` → Rust dependencies
- `go.mod` → Go modules
- `Gemfile` → Ruby gems
- `composer.json` → PHP dependencies

**Extract:**
- Primary language(s)
- Framework(s) used
- Key dependencies (top 5-10)

### 2. Project Purpose

Read these files:
- `README.md` → What does it claim to do?
- Main entry point (e.g., `src/index.ts`, `main.py`, `cmd/main.go`)

**Extract:**
- One-sentence description
- Primary use case
- Target audience (developers, end-users, both)

### 3. Story Hooks (Quick)

Use Grep to search for:
```
TODO|FIXME|HACK|XXX|BUG|NOTE|OPTIMIZE|SECURITY
```

**Extract:**
- 3-5 interesting comments that reveal challenges or insights
- Any patterns in what the team is working on

---

## Deep Analysis (15-20 minutes)

Run this for comprehensive blog posts, tutorials, or READMEs:

### 1. Complete Tech Stack

#### Languages
| Extension | Language |
|-----------|----------|
| `.py` | Python |
| `.js`, `.mjs` | JavaScript |
| `.ts`, `.tsx` | TypeScript |
| `.go` | Go |
| `.rs` | Rust |
| `.java`, `.kt` | Java/Kotlin |
| `.rb` | Ruby |
| `.php` | PHP |
| `.cs` | C# |
| `.swift` | Swift |

Count files per language using Glob patterns.

#### Frameworks
Check for these indicators in dependency files:

**Node.js (package.json):**
- `next` → Next.js
- `react` → React
- `vue` → Vue.js
- `express` → Express
- `fastify` → Fastify
- `nest` → NestJS
- `prisma` → Prisma ORM

**Python (requirements.txt/pyproject.toml):**
- `django` → Django
- `flask` → Flask
- `fastapi` → FastAPI
- `sqlalchemy` → SQLAlchemy
- `celery` → Celery
- `pytest` → pytest

**Go (go.mod):**
- `gin` → Gin
- `echo` → Echo
- `fiber` → Fiber
- `gorm` → GORM

### 2. Architecture Pattern Detection

Check directory structure for these patterns:

| Pattern | Indicator Directories |
|---------|----------------------|
| MVC | `models/`, `views/`, `controllers/` |
| Clean Architecture | `domain/`, `usecases/`, `infrastructure/` |
| Hexagonal | `adapters/`, `ports/`, `domain/` |
| Microservices | `services/`, `gateway/`, `docker-compose.yml` |
| Monorepo | `packages/`, `apps/`, `turbo.json`, `nx.json` |
| Serverless | `functions/`, `serverless.yml`, `vercel.json` |
| Component-based | `components/`, `features/`, `modules/` |

### 3. Key Files Identification

Locate and note:
- **Entry points:** `index.ts`, `main.py`, `main.go`, `app.py`
- **Configuration:** `config/`, `.env.example`, `settings.py`
- **Core logic:** Files with most imports, largest non-test files
- **Tests:** `test/`, `tests/`, `__tests__/`, `*_test.go`, `*_spec.rb`

### 4. API Endpoint Discovery

Search for route definitions:

**Express/Node:**
```javascript
app.get|post|put|delete('path'
router.get|post|put|delete('path'
```

**FastAPI/Flask:**
```python
@app.get|post|put|delete("path"
@router.get|post|put|delete("path"
```

**Go:**
```go
.GET|POST|PUT|DELETE("path"
HandleFunc("path"
```

### 5. Git Insights

Run these commands:
```bash
git log --oneline -20  # Recent commits
git shortlog -sn --no-merges | head -5  # Top contributors
git log --all --format='%H' | wc -l  # Total commits
```

**Extract:**
- Project age (first commit date)
- Active contributors
- Recent focus areas (from commit messages)
- Interesting commit messages for content hooks

### 6. Story Hook Patterns

Search for these comment patterns:
- `TODO:` → Planned improvements
- `FIXME:` → Known bugs
- `HACK:` → Workarounds (great for "lessons learned")
- `OPTIMIZE:` → Performance opportunities
- `SECURITY:` → Security considerations
- `DEPRECATED:` → Evolution stories

**Content angle extraction:**
- Performance story: Look for commits with "perf:", "optimize", "faster"
- Security story: Look for "security", "fix:", "vulnerability"
- Refactoring journey: Look for "refactor:", "clean up", "simplify"
- Developer experience: Look for "dx", "developer", "ergonomic"

---

## Content Angle Generator

Based on analysis, identify 3+ angles:

### Angle Templates

1. **The Performance Story**
   - "How we improved [metric] by [percentage]"
   - Look for: optimization commits, caching implementations, query improvements

2. **The Architecture Decision**
   - "Why we chose [pattern/framework] over [alternative]"
   - Look for: README justifications, ADR files, migration commits

3. **The Bug Hunt**
   - "The bug that taught us [lesson]"
   - Look for: FIXME comments, interesting fix commits

4. **The Developer Experience**
   - "Making [task] easier for developers"
   - Look for: CLI tools, dev scripts, configuration improvements

5. **The Security Journey**
   - "How we secured [component]"
   - Look for: auth implementations, security fixes, audit changes

6. **The Migration Story**
   - "Migrating from [old] to [new]"
   - Look for: deprecated code, version bumps, refactoring commits

7. **The Scale Story**
   - "Scaling [system] to handle [load]"
   - Look for: infrastructure changes, caching, load balancing

---

## Output Template

After analysis, produce this summary:

```markdown
## Project Analysis: [Name]

### Tech Stack
- **Primary Language:** [language]
- **Framework:** [framework]
- **Key Dependencies:** [list 5-7]

### Architecture
- **Pattern:** [detected pattern]
- **Notable Structure:** [key observations]

### Content Angles (3+)
1. [Angle 1 with supporting evidence]
2. [Angle 2 with supporting evidence]
3. [Angle 3 with supporting evidence]

### Story Hooks
- [Interesting TODO/FIXME/comment 1]
- [Interesting commit message 1]
- [Pattern or insight discovered]

### Recommended Content Type
Based on this analysis, the best content format would be:
[blog/tutorial/twitter thread/etc.] because [reasoning]
```
