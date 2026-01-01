# fastapi-users

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/example/fastapi-users/actions)
[![PyPI version](https://img.shields.io/badge/pypi-v1.0.0-blue)](https://pypi.org/project/fastapi-users/)
[![Coverage](https://img.shields.io/badge/coverage-92%25-green)](https://github.com/example/fastapi-users)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> Drop-in user authentication for FastAPI applications.

---

## The Problem

Every FastAPI project needs user authentication. Every time, you rewrite:

- Registration with email verification
- Login with JWT or sessions
- Password reset emails
- OAuth2 integrations

It's boring, error-prone, and takes days away from building your actual product.

## The Solution

**fastapi-users** provides production-ready authentication in under 5 minutes.

- **JWT or sessions** — Your choice, same API
- **SQLAlchemy or MongoDB** — Bring your own database
- **OAuth2 built-in** — Google, GitHub, Facebook ready
- **Fully tested** — 92% coverage, battle-tested in production

---

## Quick Start

### Installation

```bash
pip install fastapi-users[sqlalchemy]
```

### Basic Setup

```python
from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy

app = FastAPI()

# Configure authentication
jwt_backend = JWTStrategy(secret="your-secret-key", lifetime_seconds=3600)

# Initialize FastAPI Users
fastapi_users = FastAPIUsers(
    user_db,
    [jwt_backend],
)

# Add routes
app.include_router(fastapi_users.get_auth_router(jwt_backend), prefix="/auth")
app.include_router(fastapi_users.get_register_router(), prefix="/auth")
app.include_router(fastapi_users.get_users_router(), prefix="/users")
```

Your API now has `/auth/login`, `/auth/register`, and `/users/me`.

### Protect a Route

```python
@app.get("/protected")
async def protected_route(user: User = Depends(fastapi_users.current_user())):
    return {"message": f"Hello, {user.email}!"}
```

---

## API Reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/auth/register` | POST | Create new user account |
| `/auth/login` | POST | Authenticate and receive token |
| `/auth/logout` | POST | Invalidate current session |
| `/users/me` | GET | Get current user profile |
| `/users/me` | PATCH | Update current user profile |
| `/auth/forgot-password` | POST | Request password reset email |
| `/auth/reset-password` | POST | Complete password reset |
| `/auth/verify` | POST | Verify email address |

---

## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `secret` | `str` | **Required** | Secret key for JWT signing |
| `lifetime_seconds` | `int` | `3600` | Token expiration in seconds |
| `algorithm` | `str` | `"HS256"` | JWT signing algorithm |
| `cookie_secure` | `bool` | `True` | Require HTTPS for cookies |
| `cookie_httponly` | `bool` | `True` | Prevent JavaScript access to cookies |

---

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   FastAPI   │────▶│  fastapi-    │────▶│  Database   │
│   Routes    │     │    users     │     │  Backend    │
└─────────────┘     └──────────────┘     └─────────────┘
                           │
                    ┌──────┴──────┐
                    ▼             ▼
              ┌─────────┐   ┌──────────┐
              │   JWT   │   │ Sessions │
              │ Backend │   │ Backend  │
              └─────────┘   └──────────┘
```

**Components:**

- **Routers** — Pre-built FastAPI routers for auth endpoints
- **Backends** — Pluggable database adapters (SQLAlchemy, MongoDB)
- **Strategies** — Authentication methods (JWT, Cookie sessions)
- **Schemas** — Pydantic models for request/response validation

---

## Examples

### OAuth2 with Google

```python
from fastapi_users.oauth import GoogleOAuth2

google_oauth = GoogleOAuth2(
    client_id="your-client-id",
    client_secret="your-client-secret",
)

app.include_router(
    fastapi_users.get_oauth_router(google_oauth),
    prefix="/auth/google",
)
```

### MongoDB Backend

```bash
pip install fastapi-users[mongodb]
```

```python
from fastapi_users.db import MongoDBUserDatabase

user_db = MongoDBUserDatabase(User, database["users"])
```

---

## Troubleshooting

<details>
<summary>Token expired errors</summary>

Increase `lifetime_seconds` in your JWT configuration. Default is 1 hour (3600 seconds).

```python
jwt_backend = JWTStrategy(secret="...", lifetime_seconds=86400)  # 24 hours
```

</details>

<details>
<summary>CORS issues with cookies</summary>

For local development over HTTP, disable secure cookies:

```python
cookie_backend = CookieStrategy(cookie_secure=False)  # Dev only!
```

</details>

<details>
<summary>Password validation failing</summary>

Implement custom password validation:

```python
async def validate_password(password: str, user: User) -> None:
    if len(password) < 8:
        raise InvalidPasswordException("Password must be 8+ characters")
```

</details>

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:

- Development setup
- Testing guidelines
- Pull request process

```bash
# Development setup
git clone https://github.com/example/fastapi-users
cd fastapi-users
pip install -e ".[dev]"
pytest
```

---

## License

MIT — See [LICENSE](LICENSE) for details.

---

<p align="center">
  Built for the FastAPI community
  <br>
  <a href="https://github.com/example/fastapi-users">GitHub</a> •
  <a href="https://fastapi-users.readthedocs.io">Docs</a> •
  <a href="https://pypi.org/project/fastapi-users/">PyPI</a>
</p>
