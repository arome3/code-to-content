# Automatic Quality Validation with Hooks

This skill includes Claude Code hooks that automatically validate content quality whenever you write a file.

---

## What Hooks Do

When Claude writes content (blog post, tutorial, README, etc.), the hook automatically:

1. **Runs `validate_content.py`** on the saved file
2. **Checks readability** against audience thresholds
3. **Reports issues** back to Claude
4. **Claude fixes** problems immediately

**Result:** You always receive content that meets quality standards.

---

## How It Works

```
You: "Write a beginner tutorial about Redis"
                    │
                    ▼
         Claude writes tutorial
         Uses Write tool → saves file
                    │
                    ▼
         ┌─────────────────────────┐
         │  Hook Auto-Triggers     │
         │  validate_content.py    │
         └─────────────────────────┘
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
   PASS                    FAIL
   Content delivered       Claude sees issues
                           Claude revises
                           Hook runs again
                                │
                                ▼
                           PASS
                           Content delivered
```

---

## Default Configuration

The skill ships with this hook in `.claude/settings.local.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "description": "Auto-validate content readability after writing",
        "commands": [
          "python3 files/validate_content.py \"$FILE_PATH\" --audience intermediate 2>/dev/null || true"
        ]
      }
    ]
  }
}
```

---

## Customizing the Hook

### Change Default Audience

Edit the `--audience` parameter:

```json
"commands": [
  "python3 files/validate_content.py \"$FILE_PATH\" --audience beginner"
]
```

Options:
- `beginner` — Grade ≤8.0, jargon ≤2%, sentences ≤20 words
- `intermediate` — Grade ≤12.0, jargon ≤4%, sentences ≤25 words
- `expert` — Grade ≤16.0, jargon ≤8%, sentences ≤35 words

### Validate Only Markdown Files

Add a file extension check:

```json
"commands": [
  "if [[ \"$FILE_PATH\" == *.md ]]; then python3 files/validate_content.py \"$FILE_PATH\" --audience intermediate; fi"
]
```

### Validate Only Output Directory

```json
"commands": [
  "if [[ \"$FILE_PATH\" == *output/* ]]; then python3 files/validate_content.py \"$FILE_PATH\" --audience intermediate; fi"
]
```

---

## What Gets Validated

| Check | Beginner | Intermediate | Expert |
|-------|----------|--------------|--------|
| Flesch-Kincaid Grade | ≤ 8.0 | ≤ 12.0 | ≤ 16.0 |
| Jargon Density | ≤ 2% | ≤ 4% | ≤ 8% |
| Max Sentence Length | 20 words | 25 words | 35 words |
| Weak Opening Check | Yes | Yes | No |

### Jargon Detection

The validator flags technical terms used without explanation:

- `idempotent`, `memoization`, `polymorphism`
- `middleware`, `serialization`, `callback`
- `closure`, `immutable`, `stateless`
- ... and 50+ more common terms

**To pass:** Either avoid the term or explain it:
- Bad: "The function is idempotent"
- Good: "The function is idempotent (safe to run multiple times)"

### Weak Opening Detection

For beginner/intermediate content, flags openings like:
- "In this article, I will..."
- "Today we will learn..."
- "Welcome to this tutorial..."

---

## Validation Output

### When Passing

```
PASS - Content validated for beginner audience
```

### When Failing

```
FAIL - Content needs revision for beginner audience

  Grade level: 11.2 (max for beginner: 8.0)
  Jargon density: 3.5% (max: 2%)
    Undefined terms: middleware, callback, async
  Long sentences: 4 exceed 20 words
    Sentence 12: 28 words - "The middleware function processes the..."
    Sentence 34: 25 words - "When the callback executes after the..."

Claude should revise and re-save to trigger re-validation.
```

---

## Manual Validation

You can also run the validator manually:

```bash
# Validate for beginner audience
python3 files/validate_content.py output/blog-post.md --audience beginner

# Quiet mode (just PASS/FAIL)
python3 files/validate_content.py output/tutorial.md --audience intermediate --quiet
```

---

## Disabling Hooks

To temporarily disable hooks, remove or comment out the `hooks` section in `.claude/settings.local.json`.

To disable for a single session, you can tell Claude: "Skip validation for this content."

---

## Troubleshooting

### "python3 not found"

The hook uses `python3`. If you only have `python`, edit the command:

```json
"commands": [
  "python files/validate_content.py \"$FILE_PATH\" --audience intermediate"
]
```

### Hook Not Running

1. Check that `.claude/settings.local.json` contains the hooks configuration
2. Ensure the matcher is `"Write"` (case-sensitive)
3. Verify `files/validate_content.py` exists and is executable

### False Positives

If the validator flags content incorrectly:
- Tell Claude: "The term 'X' is appropriate for this audience, ignore the warning"
- Or add the term to the "explained" patterns in `validate_content.py`

---

## Integration with 5-Phase Process

Hooks complement but don't replace the Phase 5 verification:

| Check | Hook (Automatic) | Phase 5 (Manual) |
|-------|------------------|------------------|
| Readability grade | Yes | Yes |
| Jargon density | Yes | Yes |
| Sentence length | Yes | Yes |
| Format checklist | — | Yes |
| Evidence grounding | — | Yes |
| Voice consistency | — | Yes |

Hooks catch the most common issues automatically. Phase 5 handles deeper quality checks.
