# Negative Example: Missing Problem Statement

## Gate Failed

**Phase 4 Gate** — Template Structure Compliance

## Rule Violated

From `assets/templates/readme.md` → Required Sections:

> ## The Problem
> [1-2 sentences describing the pain point this solves]

## Failing Content

```markdown
# FastAuth

A lightweight authentication library for FastAPI.

## Installation

```bash
pip install fastauth
```

## Quick Start

```python
from fastauth import FastAuth

auth = FastAuth(secret_key="your-secret")

@app.post("/login")
async def login(credentials: Credentials):
    return auth.create_token(credentials.username)
```

## Configuration

| Option | Default | Description |
|--------|---------|-------------|
| secret_key | None | JWT signing key |
| algorithm | HS256 | Signing algorithm |
| expiry | 3600 | Token lifetime in seconds |

## API Reference

### `FastAuth(secret_key, algorithm, expiry)`

Creates a new FastAuth instance...
```

## Why It Fails

1. **No problem statement** — Reader doesn't know *why* they need this
2. **Jumps to installation** — Assumes reader already wants the library
3. **Missing value proposition** — What pain does this solve?
4. **No comparison** — How is this different from existing solutions?

## Corrected Version

```markdown
# FastAuth

Secure JWT authentication for FastAPI in 3 lines of code.

## The Problem

Adding authentication to FastAPI requires 50+ lines of boilerplate:
token generation, validation middleware, refresh logic, and secure
defaults. Most tutorials skip security best practices entirely.

## The Solution

FastAuth handles JWT authentication with secure defaults out of the box:

```python
from fastauth import FastAuth

auth = FastAuth(secret_key="your-secret")  # That's it.
```

**What you get:**
- Automatic token refresh
- Secure cookie handling
- CSRF protection built-in
- Zero configuration required

## Installation

```bash
pip install fastauth
```

## Quick Start
...
```

## Why It Passes

1. **Clear problem** — "50+ lines of boilerplate" is a concrete pain point
2. **Value proposition first** — "3 lines of code" in the tagline
3. **Shows the contrast** — Problem → Solution flow
4. **Benefits listed** — Reader knows what they get before installing

## Related Template Section

From `assets/templates/readme.md`:

```markdown
## The Problem
[1-2 sentences describing the pain point this solves]

## The Solution
[How this project solves it - be specific]
```

## Note

This example doesn't have a direct evaluation question, but demonstrates
template compliance requirements that affect Phase 4 gate passage.
