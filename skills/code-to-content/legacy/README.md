# Legacy Scripts (Archived)

These Python scripts have been replaced with Claude-native analysis protocols.

## Archived Files

| Script | Replaced By |
|--------|-------------|
| `analyze_codebase.py` | `references/analysis-prompts.md` |
| `analyze_readability.py` | `references/readability-guide.md` |
| `generate_diagrams.py` | `references/diagram-templates.md` |

## Why Archived?

1. **Zero dependencies**: Claude-native approach requires no Python installation
2. **Inline execution**: Analysis happens during content generation, not as a separate step
3. **Flexibility**: Prompts can be adapted on-the-fly for specific needs

## Can I Still Use These?

Yes, these scripts still work if you prefer the Python approach:

```bash
python legacy/analyze_codebase.py /path/to/project --deep
python legacy/analyze_readability.py content.md --audience beginner --validate
python legacy/generate_diagrams.py --type flowchart
```

However, the skill no longer references them. Use the `references/` files instead.
