# Complete Conference Talk Example

**Source Project:** RecoverPy (Python CLI for data recovery)
**Audience:** Intermediate-advanced developers at PyCon/DevOps conferences
**Format:** CFP Abstract + Talk Outline
**Generated Following:** 5-Phase Process with all gates passed

---

## Generated Output

---

### CFP Abstract

**Title:** Deleted Doesn't Mean Gone: Building a Forensic Data Recovery Tool in Python

**Duration:** 30 minutes

**Abstract:**

You've deleted critical files and panicked. Traditional recovery tools found nothing. But what if I told you your data might still exist—byte for byte—on your disk?

In this talk, I'll walk you through building RecoverPy, a terminal-based data recovery tool that scans raw disk blocks to find text that filesystem-level tools miss. You'll learn:

- Why "deleted" files often survive even after new data is written
- How to use grep at the block device level (and why the `-b` flag is your secret weapon)
- Architecting a hybrid async/threading system for responsive TUIs during massive I/O
- When Python's GIL actually helps your concurrent design

We'll examine real code from RecoverPy's 168-line search engine, see live demos of recovering "overwritten" data, and discuss the security implications of why this works.

**Takeaways:**
- Understand block-level vs. filesystem-level data operations
- Learn practical patterns for mixing asyncio with threading
- Walk away with a working mental model of disk forensics

**Target Audience:** Intermediate Python developers curious about systems programming, CLI tools, or data recovery.

---

### Talk Outline

#### Opening (3 min)
- **Hook:** Live demo—delete a file, write new data, "recover" it with RecoverPy
- **Setup the stakes:** Everyone has lost data they thought was gone forever

#### Part 1: Why Traditional Recovery Fails (5 min)
- Filesystem-level deletion: marking blocks as "available"
- Why `testdisk` and similar tools stop working after new writes
- The misconception: "overwritten = erased"

```
┌─────────────────────────────────────────┐
│ Filesystem sees: [FREE BLOCK]           │
│ Disk actually has: [YOUR DATA + NOISE]  │
└─────────────────────────────────────────┘
```

#### Part 2: Block-Level Scanning (8 min)
- The grep approach: scanning raw disk devices
- Key insight: `-b` flag returns byte offsets

```python
# The core of RecoverPy's search
def get_grep_process(partition: str, search_string: str) -> Popen:
    return Popen(
        ["grep", "-a", "-b", "-o", search_string, partition],
        stdout=PIPE,
        stderr=DEVNULL,
    )
```

- Demo: Finding a unique string in "deleted" space
- Navigating to adjacent blocks for context

#### Part 3: Architecture Deep Dive (10 min)
- The challenge: grep is blocking I/O, but we need responsive UI
- Solution: Hybrid async/threading architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌────────────────┐
│ grep (thread)   │───>│ Queue (threading)│───>│ Textual (async)│
│ Scans disk      │    │ Buffer results   │    │ Renders UI     │
└─────────────────┘    └──────────────────┘    └────────────────┘
```

- Why the GIL isn't a problem here (I/O bound, not CPU bound)
- Textual framework for modern terminal UIs
- Real-time result streaming without buffering

#### Part 4: Security Implications (3 min)
- Why secure deletion requires multiple overwrites
- What this means for sensitive data on shared systems
- Brief mention of NIST guidelines

#### Closing (1 min)
- Recap: Block-level thinking opens new possibilities
- Call to action: Try RecoverPy, explore systems programming
- Resources and links

---

## Metadata

**Talk Type:** Technical deep-dive with live demo
**Duration:** 30 minutes
**Slides Estimate:** 25-30
**Demo Requirements:** Linux VM with prepared test partition

---

## Phase Gate Verification

| Gate | Status | Evidence |
|------|--------|----------|
| Phase 1 | ✅ | Tech stack: Python, Textual, asyncio/threading |
| Phase 2 | ✅ | Audience: Intermediate+, Format: Conference talk |
| Phase 3 | ✅ | All code from recoverpy/lib/helper.py and search_engine.py |
| Phase 4 | ✅ | Clear narrative arc, timed sections |
| Phase 5 | ✅ | Appropriate technical depth for conference audience |

---

## Why This Example Works

1. **Hook is a live demo** — Immediately shows the unexpected result
2. **Clear three-act structure** — Problem → Solution → Implications
3. **Code is minimal but illuminating** — Shows the key insight
4. **Diagrams aid understanding** — ASCII art for architecture
5. **Timed sections** — Realistic pacing for 30-minute slot
6. **Takeaways are concrete** — Audience knows what they'll learn
