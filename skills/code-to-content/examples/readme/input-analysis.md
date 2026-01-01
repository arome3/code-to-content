# Codebase Analysis: fastapi-users

**Analysis Mode:** `--deep`
**Date:** 2024-01-15

---

## Project Overview

| Metric | Value |
|--------|-------|
| Type | FastAPI authentication library |
| Primary Language | Python (95%), SQL (5%) |
| Dependencies | 18 (fastapi, pydantic, sqlalchemy, passlib, python-jose) |
| Lines of Code | 4,231 |
| Test Coverage | 92% |

---

## Core Features Detected

- User registration and authentication
- JWT and session-based auth strategies
- Password hashing with bcrypt
- OAuth2 support (Google, GitHub, Facebook)
- SQLAlchemy and MongoDB backends
- Password reset flow
- Email verification

---

## Design Patterns Detected

| Pattern | Confidence | Evidence |
|---------|------------|----------|
| Strategy | 0.91 | Multiple auth backends (JWT, Session) |
| Repository | 0.88 | UserDatabase abstraction layer |
| Factory | 0.79 | `FastAPIUsers.get_auth_router()`, `get_register_router()` |
| Dependency Injection | 0.85 | FastAPI Depends pattern throughout |

---

## Architecture

```
fastapi-users/
├── src/
│   ├── authentication/      # Auth strategy implementations
│   │   ├── base.py          # Abstract base class
│   │   ├── jwt.py           # JWT bearer tokens
│   │   └── cookie.py        # Session cookies
│   ├── backends/            # Database backends
│   │   ├── sqlalchemy.py    # SQLAlchemy (PostgreSQL, SQLite)
│   │   └── mongodb.py       # MongoDB with motor
│   ├── routers/             # FastAPI route handlers
│   │   ├── auth.py          # /login, /logout
│   │   ├── register.py      # /register
│   │   ├── users.py         # /users/me, /users/{id}
│   │   └── reset.py         # /forgot-password, /reset-password
│   └── schemas/             # Pydantic models
│       ├── user.py
│       └── auth.py
├── examples/
│   ├── simple/
│   └── oauth/
└── tests/
```

---

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | /auth/register | Create new user |
| POST | /auth/login | Authenticate user |
| POST | /auth/logout | End session |
| GET | /users/me | Get current user |
| PATCH | /users/me | Update current user |
| POST | /auth/forgot-password | Request password reset |
| POST | /auth/reset-password | Complete password reset |
| POST | /auth/verify | Verify email address |

---

## Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `secret` | str | Required | JWT signing key |
| `lifetime_seconds` | int | 3600 | Token expiration |
| `algorithm` | str | "HS256" | JWT algorithm |
| `cookie_secure` | bool | True | HTTPS-only cookies |
| `cookie_httponly` | bool | True | Prevent JS access |

---

## Suggested Content Angles

1. "Drop-in User Authentication for FastAPI in 5 Minutes"
2. "JWT vs Sessions: Which Auth Strategy for Your FastAPI App?"
3. "Building Secure Password Reset Flows with FastAPI"
