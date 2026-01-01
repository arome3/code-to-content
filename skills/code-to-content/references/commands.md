# Slash Commands Reference

Complete reference for all code-to-content slash commands.

---

## Full Mode Commands (All 5 Phases)

These commands enforce the complete 5-phase process with all gates and confirmations.

| Command | Usage | Description |
|---------|-------|-------------|
| `/c2c:blog` | `/c2c:blog [path]` | Generate blog post with full analysis |
| `/c2c:tutorial` | `/c2c:tutorial [path]` | Generate step-by-step tutorial |
| `/c2c:twitter` | `/c2c:twitter [topic]` | Generate Twitter/X thread |
| `/c2c:readme` | `/c2c:readme [path]` | Generate README.md |
| `/c2c:linkedin` | `/c2c:linkedin [topic]` | Generate LinkedIn post |
| `/c2c:newsletter` | `/c2c:newsletter [path]` | Generate newsletter issue |
| `/c2c:video-script` | `/c2c:video-script [path]` | Generate video script |
| `/c2c:conference-talk` | `/c2c:conference-talk [path]` | Generate CFP + talk outline |
| `/c2c:product-launch` | `/c2c:product-launch [path]` | Generate multi-platform launch content |

---

## Quick Mode Commands (Reduced Phases)

For rapid content generation when you already know your audience and have context.

| Command | Usage | Phases Skipped | Best For |
|---------|-------|----------------|----------|
| `/c2c:quick-twitter` | `/c2c:quick-twitter [topic]` | 1, 2, 4 | Fast tweets when audience is known |
| `/c2c:quick-linkedin` | `/c2c:quick-linkedin [topic]` | 1, 2, 4 | Quick LinkedIn posts |
| `/c2c:quick-blog` | `/c2c:quick-blog [topic]` | 1, 4 | Rapid blog drafts (still validates audience) |
| `/c2c:quick-readme` | `/c2c:quick-readme [path]` | 1, 2 | Fast README updates |

### When to Use Quick Mode

**Use Quick Mode when:**
- You already know your audience well
- Content is time-sensitive
- Clear context exists (no codebase analysis needed)
- Iterating on existing content

**Use Full Mode when:**
- First-time content for a project
- High-stakes content (launches, major announcements)
- Complex technical topics requiring deep analysis
- Full verification suite needed

---

## Cascade Mode (Multi-Platform Repurposing)

| Command | Usage | Description |
|---------|-------|-------------|
| `/c2c:cascade` | `/c2c:cascade <source-file> [--formats twitter,linkedin]` | Derive multiple formats from source content |

Cascade generates Twitter thread + LinkedIn post + Newsletter section from a single blog post or tutorial.

See `references/content-cascade.md` for derivation rules and platform constraints.

---

## Command Location

All commands are located in `.claude/commands/c2c/`.

---

## Phase Flow by Command Type

### Full Mode Flow
```
Phase 1 ──[Gate + Confirm]──> Phase 2 ──[Gate + Confirm]──> Phase 3 ──[Gate]──> Phase 4 ──[Gate]──> Phase 5 ──[Gate]──> DELIVERY
```

### Quick Mode Flow (example: quick-twitter)
```
Phase 3 ──[Gate]──> Phase 5 ──[Gate]──> DELIVERY
```

### Cascade Mode Flow
```
Source Content ──[Parse]──> Platform Adaption ──[Verify per format]──> Multi-format DELIVERY
```
