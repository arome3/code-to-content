# Code Snippet Image Generation

Generate shareable code snippet images for social media, blog posts, and presentations.

---

## When to Use

Generate code snippet images when creating:
- Twitter/X threads with code examples
- LinkedIn posts showcasing technical work
- Blog post visuals
- Presentation slides
- README badges and examples

---

## Step 1: Extract the Code

### From User Request

User may specify:
- Function name: "the `processPayment` function"
- File and lines: "lines 45-60 of src/auth.ts"
- Description: "the part that handles rate limiting"

### From Project Analysis

If user is vague, identify snippet-worthy code:
- Core algorithm or logic
- Clever one-liners
- Before/after comparisons
- Key architectural patterns

### Prepare the Code

Before generating:
1. Extract the exact code block
2. Remove unnecessary imports (unless relevant)
3. Trim excessive whitespace
4. Keep it focused (5-25 lines ideal)
5. Ensure it's self-explanatory or add minimal context

---

## Step 2: Choose Output Method

```
IF user requests specific tool → Use that tool
IF user wants instant result → Generate SVG
IF user wants highest quality → Generate Carbon/Ray.so URL
IF for Twitter/LinkedIn → Generate Carbon URL (PNG export)
IF for documentation/web → Generate SVG (scalable)
IF user doesn't specify → Offer both options
```

---

## Option A: Carbon URL Generation

Generate pre-configured URLs that open Carbon with code and settings ready.

**Base URL:** `https://carbon.now.sh/`

### Parameters

| Parameter | Description | Recommended Values |
|-----------|-------------|-------------------|
| `code` | URL-encoded code | (from project) |
| `language` | Syntax highlighting | auto, javascript, typescript, python, go, rust |
| `theme` | Color theme | dracula, monokai, night-owl, one-dark, synthwave-84 |
| `bg` | Background color | rgba(0,0,0,0) for transparent, or hex |
| `fontFamily` | Code font | Fira Code, JetBrains Mono, Hack |
| `fontSize` | Font size | 14px, 16px, 18px |
| `padding` | Padding | 16, 32, 64 |
| `lineNumbers` | Show line numbers | true, false |
| `windowControls` | Show macOS buttons | true, false |

### URL Template

```
https://carbon.now.sh/?code={{url_encoded_code}}&language={{lang}}&theme={{theme}}&bg={{bg}}&fontFamily={{font}}&fontSize={{size}}&padding={{pad}}&lineNumbers={{lines}}&windowControls={{controls}}
```

---

## Option B: Ray.so URL Generation

**Base URL:** `https://ray.so/`

### Parameters

| Parameter | Description | Values |
|-----------|-------------|--------|
| `code` | Base64-encoded code | (from project) |
| `language` | Language | javascript, typescript, python, etc. |
| `theme` | Theme | candy, crimson, falcon, meadow, midnight, raindrop, sunset |
| `background` | Enable background | true, false |
| `darkMode` | Dark mode | true, false |
| `padding` | Padding | 16, 32, 64, 128 |

### URL Template

```
https://ray.so/#code={{base64_code}}&language={{lang}}&theme={{theme}}&background={{bg}}&darkMode={{dark}}&padding={{pad}}
```

---

## Option C: SVG Generation

Generate self-contained SVG with syntax highlighting. No external tools needed.

### SVG Structure

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {{width}} {{height}}">
  <!-- Background -->
  <rect width="100%" height="100%" rx="8" fill="{{bg_color}}"/>

  <!-- Window controls (optional) -->
  <circle cx="20" cy="20" r="6" fill="#ff5f56"/>
  <circle cx="40" cy="20" r="6" fill="#ffbd2e"/>
  <circle cx="60" cy="20" r="6" fill="#27c93f"/>

  <!-- Code block -->
  <text font-family="{{font}}" font-size="{{size}}" fill="{{text_color}}">
    {{highlighted_lines}}
  </text>
</svg>
```

### Syntax Highlighting Colors

**Dracula Theme:**
| Token | Color |
|-------|-------|
| Background | #282a36 |
| Default text | #f8f8f2 |
| Keywords | #ff79c6 (pink) |
| Strings | #f1fa8c (yellow) |
| Functions | #50fa7b (green) |
| Comments | #6272a4 (muted blue) |
| Numbers | #bd93f9 (purple) |

**One Dark Theme:**
| Token | Color |
|-------|-------|
| Background | #282c34 |
| Default text | #abb2bf |
| Keywords | #c678dd (purple) |
| Strings | #98c379 (green) |
| Functions | #61afef (blue) |
| Comments | #5c6370 (gray) |
| Numbers | #d19a66 (orange) |

---

## Theme Recommendations by Platform

| Platform | Recommended Theme | Background | Reason |
|----------|------------------|------------|--------|
| Twitter | dracula, synthwave-84 | Solid dark | High contrast in feed |
| LinkedIn | one-dark, night-owl | Solid dark | Professional look |
| Blog (light) | github-light | Transparent | Matches light themes |
| Blog (dark) | monokai, dracula | Transparent | Matches dark themes |
| Presentation | synthwave-84 | Gradient | Eye-catching |

---

## Dimension Guidelines

### By Platform

| Platform | Recommended Size | Aspect Ratio |
|----------|-----------------|--------------|
| Twitter | 1200x675 | 16:9 |
| LinkedIn | 1200x627 | 1.91:1 |
| Instagram | 1080x1080 | 1:1 |
| Blog embed | 800x auto | Flexible |
| Presentation | 1920x1080 | 16:9 |

### By Code Length

| Lines of Code | Recommended Width | Font Size |
|---------------|------------------|-----------|
| 1-5 | 600px | 18px |
| 6-15 | 800px | 16px |
| 16-25 | 1000px | 14px |
| 25+ | Consider splitting | 14px |

---

## Output Template

When generating code snippets, deliver as:

```markdown
## Code Snippet: {{title}}

### The Code
```{{language}}
{{extracted_code}}
```

### Carbon (Recommended for Social)
[Open in Carbon]({{carbon_url}})

Settings: {{theme}} theme, {{font}} font
Instructions: Click link → Adjust if needed → Export as PNG

### Ray.so (Alternative)
[Open in Ray.so]({{rayso_url}})

### SVG (For Web/Docs)
```svg
{{svg_code}}
```
Save as `{{filename}}.svg`

---
**Platform recommendation:** {{recommendation}}
```

---

## Language Token Patterns

Apply syntax highlighting based on language:

### JavaScript/TypeScript
```
Keywords: const, let, var, function, return, if, else, async, await, import, export, class
Strings: "...", '...', `...`
Functions: word followed by (
Comments: // or /* */
Numbers: digits, hex
```

### Python
```
Keywords: def, class, return, if, else, elif, import, from, async, await, with, as
Strings: "...", '...', """...""", '''...'''
Functions: word followed by (
Comments: #
Numbers: digits
```

### Rust
```
Keywords: fn, let, mut, pub, struct, impl, use, mod, match, if, else, return
Strings: "..."
Functions: word followed by (
Comments: // or /* */
Macros: word!
Lifetimes: 'a
```

### Go
```
Keywords: func, var, const, type, struct, interface, if, else, for, return, package, import
Strings: "...", `...`
Functions: word followed by (
Comments: // or /* */
```

---

## Integration with Content Formats

### Twitter Threads

When generating Twitter threads with code:
1. Extract key code snippet (max 10 lines for readability)
2. Generate Carbon URL with dracula theme
3. Include in thread: "Here's the code: [Carbon link]"
4. Add "(click to see full snippet)" note

### LinkedIn Posts

When generating LinkedIn posts with code:
1. Keep snippets short (5-8 lines)
2. Use one-dark theme for professional look
3. Mention "swipe for code" or include Carbon link in comments

### Blog Posts

When generating blog posts:
1. Use inline code blocks for short snippets
2. Generate Carbon/SVG for hero code images
3. Match theme to blog's color scheme

---

## Pre-Delivery Checklist

```
[ ] Code extracted accurately from project
[ ] Code is focused and readable (5-25 lines ideal)
[ ] Language correctly identified for syntax highlighting
[ ] URL properly encoded (no broken characters)
[ ] Theme appropriate for target platform
[ ] SVG validates (if generated)
[ ] Both options provided (unless user specified one)
[ ] Dimensions match target platform
[ ] Clear instructions for next steps
```

---

## Quick Reference

| User Says | Generate |
|-----------|----------|
| "snippet of X function" | Extract function, offer both options |
| "code image for Twitter" | Carbon URL with dracula theme |
| "shareable version of this code" | Both options with platform recommendations |
| "SVG of this code" | SVG only |
| "Carbon link for this" | Carbon URL only |
| "make this code pretty" | Both options, explain tradeoffs |
