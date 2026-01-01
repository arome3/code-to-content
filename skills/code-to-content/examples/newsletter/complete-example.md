# Complete Newsletter Example

**Source Project:** gin-boilerplate (Go REST API starter)
**Audience:** Go developers building production APIs
**Format:** Build Log newsletter issue
**Generated Following:** 5-Phase Process with all gates passed

---

## Generated Output

---

**Subject Line Options:**
1. Why we store JWT tokens in Redis (it's not for caching)
2. The logout problem that JWT doesn't solve
3. Token revocation: what the tutorials don't tell you

**Preview Text:** JWT is stateless. Until you need to log someone out.

---

Hey there,

This week I dove into the gin-boilerplate project to understand their authentication architecture. What I found changed how I think about JWT.

## The Revelation

Every JWT tutorial says the same thing: "Tokens are self-contained! No database lookups!"

But here's what they skip: **How do you log someone out?**

JWTs can't be modified or invalidated once issued. If a user clicks "logout" or you need to revoke access, the token is still valid until it expires.

The gin-boilerplate solves this with a clever pattern.

## The Pattern

When you issue a token, store its UUID in Redis:

```go
// From models/auth.go
err = client.Set(td.AccessUuid, userID,
    time.Until(time.Unix(td.AtExpires, 0))).Err()
```

On logout, delete the UUID:

```go
// Instant revocation
deleted, err := client.Del(accessUuid).Result()
```

The middleware checks Redis on every request. No Redis entry = token revoked.

## Why This Works

- **Redis TTL matches token expiry** — Automatic cleanup
- **UUID lookup is O(1)** — Sub-millisecond latency
- **Dual tokens (access + refresh)** — Revoke either independently

It's not caching. It's a kill switch.

## What I Shipped This Week

- Deep-dived gin-boilerplate's auth layer
- Documented the Redis token pattern for my team
- Started implementing this in our internal API

## What's Next

Next week I'm looking at their request ID middleware for distributed tracing. Spoiler: it's 15 lines of code that solves a real problem.

Hit reply if you've implemented JWT revocation differently—I'd love to hear your approach.

—[Your Name]

P.S. The full gin-boilerplate is here: github.com/Massad/gin-boilerplate

---

## Metadata

**Format:** Build Log (shipped, learned, next)
**Word Count:** ~300 (newsletter sweet spot)
**Tone:** Personal, peer-to-peer
**CTA:** Reply invitation

---

## Phase Gate Verification

| Gate | Status | Evidence |
|------|--------|----------|
| Phase 1 | ✅ | Tech stack: Go, Gin, Redis, JWT |
| Phase 2 | ✅ | Audience: Go developers, Format: Newsletter |
| Phase 3 | ✅ | Code examples from models/auth.go |
| Phase 4 | ✅ | Personal voice, scannable sections |
| Phase 5 | ✅ | Conversational tone, clear value |

---

## Why This Example Works

1. **Subject line creates curiosity** — Challenges assumption
2. **Hook in first paragraph** — "What I found changed how I think"
3. **Code is minimal but complete** — Shows the key mechanism
4. **Personal reflection** — "What I Shipped" / "What's Next"
5. **Reply CTA** — Builds engagement and community
6. **P.S. with link** — High-visibility placement for resource
