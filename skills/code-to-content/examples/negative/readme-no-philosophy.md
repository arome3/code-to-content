# Negative Example: README With No Philosophy (The Canary)

The README is the format most likely to collapse into a swappable feature list — it has a natural "here are the features and how to use them" shape. This is the canary case the differentiation layer was built to catch.

## Gate Failed

**Phase 6 Gate** — Distinctiveness (swap-the-name test) + README "Design Philosophy" checklist item.

## Rule Violated

From `references/checklists.md` → README → Design Philosophy, and `references/differentiation.md` (Move 3):

> States WHY it exists / what it believes, not just what it does. "What this deliberately does NOT do" section present. A reader could not swap in a competing library's name and have it still read fine.

## Failing Content

```markdown
# FastAuth

A lightweight, full-featured authentication library for FastAPI.

## Features

- 🔐 JWT and session support
- 🗄️ Works with SQLAlchemy and MongoDB
- 🔁 Automatic token refresh
- 🌐 OAuth2 built-in
- ✅ Fully tested — 92% coverage

## Installation

pip install fastauth
```

## Why It Fails

1. **Swap-the-name test: FAIL** — Replace "FastAuth" with "django-allauth" or "Authlib" and ~60% of this reads identically. It's a capability matrix, not a point of view.
2. **No belief** — It lists JWT *and* sessions, SQLAlchemy *and* MongoDB, as neutral options. It never says which it thinks you should use, or why it exists.
3. **No roads not taken** — Nothing about what it deliberately *doesn't* do. Does it handle MFA? Rate limiting? The README is silent, so the library reads as "everything," which reads as nothing.
4. **Feature-list voice** — emoji bullets + "fully-featured" + coverage badge is the universal library-README costume.
5. **Distinctiveness Score: 1/5.**

## Corrected Version

```markdown
# FastAuth

Secure JWT auth for FastAPI in 3 lines. Opinionated on purpose.

## Why this exists

Every FastAPI auth tutorial hands you 50 lines of boilerplate and three security
footguns. FastAuth is the boilerplate we got tired of rewriting — with the unsafe
defaults removed and the choices already made for you.

## Design philosophy

We believe an auth library should make the *secure* path the *short* path.
So FastAuth is opinionated where most libraries stay neutral:

- **JWT with short expiry + refresh, not long-lived sessions.** Sessions are
  simpler; we chose stateless tokens so logout-everywhere is a real feature, not
  a DB sweep.

**What this deliberately does NOT do:**

- **No MFA.** It belongs at your app/identity layer; bolting it on here would
  force a database schema we don't want to own.
- **No rate limiting.** That's your gateway's job — duplicating it here just
  gives you two places to misconfigure.
- **No "bring your own everything" config.** Fewer knobs, fewer footguns.

If you want a kitchen sink, use Authlib. If you want the secure 80% with no
decisions to make, that's this.

## Install

pip install fastauth
```

## Why It Passes

1. **Swap-the-name test: PASS** — No competitor would write "no MFA, no rate limiting, fewer knobs on purpose." The omissions *are* the identity.
2. **Leads with a belief** — "make the secure path the short path."
3. **Shows roads not taken** — MFA, rate limiting, and infinite config, each with a trade-off.
4. **Takes a side** — JWT over sessions, with the reason. A reader can disagree.
5. **Distinctiveness Score: 5/5.**

## Related Evaluation Question

> Q: A README lists every feature and supported option but never states what the library believes or refuses to do. Which Phase 6 check flags it, and is delivery blocked?
>
> A: The **Distinctiveness check** (swap-the-name test) flags it `AT RISK` and the README "Design Philosophy" checklist item fails. Delivery is **not blocked** — the warning is surfaced and Phase 2 is offered.
