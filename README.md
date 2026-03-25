<p align="center">
  <img src="c2c.png" alt="Code to Content" width="600">
</p>

<p align="center">
  <a href="https://github.com/mgodfre3/code-to-content/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="Code to Content is released under the MIT license." />
  </a>
  <a href="https://github.com/mgodfre3/code-to-content/issues">
    <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions Welcome" />
  </a>
</p>

# Code to Content

> *From commits to content.*

Transform codebases into compelling developer content with a mandatory 5-phase process, verification gates, and build-in-public support. Works with **GitHub Copilot CLI**, **VS Code Copilot**, and **Claude Code**.

## Why Use This?

Most developers ship amazing code but struggle to tell the story.

* **Writer's Block:** Staring at a blank page is painful.
* **Context Switching:** Turning deep technical logic into accessible English is hard.
* **Consistency:** "Building in public" requires constant updates.

**Code to Content** solves this by using your **actual source code** as the source of truth. It analyzes your specific implementation, architectural decisions, and variable names to generate evidence-based content.

## What This Skill Does

| Feature | Description |
|---------|-------------|
| **5-Phase Process** | Mandatory workflow: Analysis → Audience → Content → Optimization → Verification |
| **Quick Mode** | Reduced-phase commands for rapid content generation |
| **Verification Gates** | Each phase has gates that MUST pass before proceeding |
| **9 Content Types** | Blog, tutorial, Twitter, LinkedIn, README, newsletter, video script, conference talk, product launch |
| **Build-in-Public** | Journey brief system for sustained narrative and voice continuity |
| **Zero Dependencies** | All analysis performed inline — no external tools required |
| **3 Parallel Agents** | Content explorer, format specialist, and quality reviewer for parallel execution |

## Installation

### GitHub Copilot CLI (Recommended)

**Option 1: Install from GitHub**
```bash
copilot plugin install mgodfre3/code-to-content
```

**Option 2: Install locally**
```bash
git clone https://github.com/mgodfre3/code-to-content.git
copilot plugin install ./code-to-content
```

After installation, verify with:
```bash
copilot
# Then in the interactive session:
/skills list
```

### VS Code Copilot

Add the marketplace to your VS Code settings:
```json
{
  "chat.plugins.marketplaces": [
    "mgodfre3/code-to-content"
  ]
}
```

Then browse **Extensions → Agent Plugins** to install.

### Claude Code

```bash
/plugin install mgodfre3/code-to-content
```

Or clone to your skills folder:
```bash
git clone https://github.com/mgodfre3/code-to-content /tmp/code-to-content
cp -r /tmp/code-to-content/skills/code-to-content ~/.claude/skills/
rm -rf /tmp/code-to-content
```

## Quick Start

The skill auto-activates when you ask the AI to create content from code:

```
You: Write a blog post about my FastAPI project at ./src

AI: [Executes 5-phase process]
  Phase 1: Analyzing codebase...
  Phase 2: Locking audience...
  Phase 3: Generating content...
  Phase 4: Optimizing...
  Phase 5: Verifying quality gates...

  [Delivers verified content]
```

### Usage Examples

| Request | What Happens |
|---------|-------------|
| "Write a blog post about this project" | Full 5-phase blog generation |
| "Create a Twitter thread about my latest feature" | Full 5-phase Twitter thread |
| "Quick linkedin post about this code" | Quick mode — skips phases 1, 2, 4 |
| "Generate a README for this codebase" | Full 5-phase README generation |
| "Quick twitter thread" | Quick mode — fast tweet generation |
| "Content cascade from this project" | Multi-platform repurposing |

## The 5-Phase Process

```
PHASE 1 ──[Gate]──> PHASE 2 ──[Gate]──> PHASE 3 ──[Gate]──> PHASE 4 ──[Gate]──> PHASE 5 ──[Gate]──> DELIVERY
```

| Phase | Purpose | Gate Requirement |
|-------|---------|------------------|
| **1. Analysis** | Understand the codebase | 3+ content angles found |
| **2. Audience** | Lock in ONE target audience | No audience mixing |
| **3. Content** | Generate evidence-based draft | All claims grounded |
| **4. Optimization** | Apply SEO, voice, visuals | Voice consistent |
| **5. Verification** | Quality gate checks | All thresholds pass |

## What's Included

```
code-to-content/
├── plugin.json                 # Copilot plugin manifest
├── .github/plugin/
│   └── marketplace.json        # Plugin marketplace manifest
├── agents/                     # 3 Copilot-compatible agents
│   ├── content-explorer.agent.md
│   ├── format-specialist.agent.md
│   └── quality-reviewer.agent.md
├── skills/
│   └── code-to-content/
│       ├── SKILL.md            # Main skill definition
│       ├── agents/             # Claude Code agent definitions
│       ├── assets/templates/   # Content templates
│       ├── references/         # Analysis guides (13 files)
│       ├── examples/           # Positive, negative, workflow
│       ├── evaluation/         # 18 QA pairs
│       └── legacy/             # Archived Python scripts (optional)
├── README.md
└── LICENSE
```

## Build-in-Public Support

For sustained content creation, the skill includes a **Journey Brief** system:

- **Persistent context** across content sessions
- **Milestone-to-content mapping** (what to post when)
- **Voice continuity** checklists
- **Content cascade timing** (Twitter → LinkedIn → Blog → Newsletter)

See `skills/code-to-content/references/build-in-public.md` for the full guide.

## Requirements

- **GitHub Copilot CLI**, **VS Code with Copilot**, or **Claude Code**
- No external dependencies — all analysis is performed inline
- Optional: MCP servers for direct social media posting

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add/update evaluation questions if adding features
4. Submit a pull request

## License

MIT License — see [LICENSE](LICENSE) file.

---

## Credits

Original project by [Abraham Onoja](https://github.com/arome3) · [@arome_dev](https://x.com/arome_dev)

Copilot skill conversion by [mgodfre3](https://github.com/mgodfre3)
