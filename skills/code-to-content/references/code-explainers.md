# Code Explainers

Instructions for generating clear code explanations from the user's project.

## Core Principle

**Explain the WHY, show the WHAT, demonstrate the RESULT.**

When generating code explanations, never narrate code line-by-line. Readers can see what code does. Structure explanations to answer:
- Why this approach?
- What problem does this solve?
- What happens when it runs?

## Generating Explanations: The Explanation Stack

Layer every code explanation from concept to implementation:

```
LEVEL 4: The Result (what happens)
    ^
LEVEL 3: The Code (how it's implemented)
    ^
LEVEL 2: The Approach (why this way)
    ^
LEVEL 1: The Problem (what we're solving)
```

**Always start at Level 1, not Level 3.**

### When explaining code from the project:

1. **Identify the problem** - Extract what real-world issue this code addresses
2. **Articulate the approach** - Describe the strategy before showing implementation
3. **Present the code** - Show the implementation with strategic annotations
4. **Demonstrate the result** - Include example output or behavior

### Example output format:

```
LEVEL 1 - The Problem:
When a user types in a search box, we don't want to fire an API
request for every keystroke--typing "react" would trigger 5 requests.

LEVEL 2 - The Approach:
We wait until the user STOPS typing, then fire once. "Debouncing"
means: "wait for a pause before acting."

LEVEL 3 - The Code:
function debounce(fn, delay) {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);              // Cancel pending execution
    timeoutId = setTimeout(() => {        // Schedule new execution
      fn(...args);                        // Run after pause
    }, delay);
  };
}

LEVEL 4 - The Result:
const search = debounce(callAPI, 300);
search("r");       // Scheduled for 300ms
search("re");      // Cancels previous, schedules new
search("rea");     // Cancels previous, schedules new
search("reac");    // Cancels previous, schedules new
search("react");   // After 300ms of no typing -> API called ONCE
```

## Code Annotation Patterns

Select the appropriate annotation pattern based on code structure.

### Use the Inline Why Pattern when:
Explaining individual decisions throughout a function.

```python
def process_image(image_path):
    # JPEG compression can corrupt alpha channels
    # so we convert to PNG for processing
    img = Image.open(image_path).convert("RGBA")

    # Resize BEFORE filters--5x faster than filtering full resolution
    thumbnail = img.resize((256, 256), Image.LANCZOS)

    # Gaussian blur with sigma=2 removes noise while preserving edges
    processed = thumbnail.filter(ImageFilter.GaussianBlur(radius=2))

    return processed
```

### Use the Section Comment Pattern when:
Explaining multi-step processes with distinct phases.

```python
def authenticate_user(request):
    # ----------------------------------------------
    # STEP 1: Extract and validate token format
    # ----------------------------------------------
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise AuthError("Missing or malformed token")

    token = auth_header[7:]  # Strip "Bearer " prefix

    # ----------------------------------------------
    # STEP 2: Verify token signature and expiration
    # ----------------------------------------------
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise AuthError("Token expired")
    except jwt.InvalidTokenError:
        raise AuthError("Invalid token")

    # ----------------------------------------------
    # STEP 3: Load and return user
    # ----------------------------------------------
    user_id = payload.get("sub")
    return User.query.get(user_id)
```

### Use the Before/After Pattern when:
Demonstrating refactoring, improvements, or migrations.

```javascript
// BEFORE: Callback hell
getUser(userId, function(user) {
  getOrders(user.id, function(orders) {
    getOrderDetails(orders[0].id, function(details) {
      console.log(details);
    });
  });
});

// AFTER: Async/await
const user = await getUser(userId);
const orders = await getOrders(user.id);
const details = await getOrderDetails(orders[0].id);
console.log(details);
```

### Use the Highlighting Key Lines Pattern when:
Drawing attention to the critical insight or optimization.

```python
def optimize_query(query):
    parsed = parse_query(query)
    plan = create_plan(parsed)

    # vvv THE KEY INSIGHT vvv
    if should_use_index(plan):
        plan = rewrite_with_index_hints(plan)
    # ^^^ This reduced p99 latency by 10x ^^^

    return execute(plan)
```

## Explaining Complex Code

Choose a strategy based on the code complexity.

### Strategy 1: Build Up Incrementally

Start with the simplest implementation, then add complexity layer by layer.

```python
# Version 1: The simplest possible implementation
def find_duplicates(items):
    seen = set()
    duplicates = []
    for item in items:
        if item in seen:
            duplicates.append(item)
        seen.add(item)
    return duplicates

# Version 2: Add type hints for clarity
def find_duplicates(items: list[str]) -> list[str]:
    seen: set[str] = set()
    duplicates: list[str] = []
    for item in items:
        if item in seen:
            duplicates.append(item)
        seen.add(item)
    return duplicates

# Version 3: Handle edge cases
def find_duplicates(
    items: list[str],
    case_sensitive: bool = True
) -> list[str]:
    if not items:
        return []

    normalize = str if case_sensitive else str.lower
    seen: set[str] = set()
    duplicates: list[str] = []

    for item in items:
        key = normalize(item)
        if key in seen:
            duplicates.append(item)
        seen.add(key)

    return duplicates
```

### Strategy 2: Simplify Then Expand

Present a conceptual pseudocode version first, then show the real implementation.

```javascript
// CONCEPTUAL VERSION (not real code, shows the idea)
function virtualDOM(component) {
    oldTree = currentTree
    newTree = component.render()
    diff = compare(oldTree, newTree)
    apply(diff, realDOM)
    currentTree = newTree
}

// ACTUAL VERSION (real implementation)
function reconcile(fiber) {
    const oldFiber = fiber.alternate;
    const elements = fiber.props.children;

    let index = 0;
    let prevSibling = null;

    while (index < elements.length || oldFiber != null) {
        const element = elements[index];
        let newFiber = null;

        const sameType = oldFiber && element &&
                         element.type === oldFiber.type;

        if (sameType) {
            newFiber = {
                type: oldFiber.type,
                props: element.props,
                dom: oldFiber.dom,
                parent: fiber,
                alternate: oldFiber,
                effectTag: "UPDATE",
            };
        }
        // ... more cases
    }
}
```

### Strategy 3: Analogy First

Open with a relatable analogy, then connect it to the code.

```
ANALOGY:
A database index is like a book's index. Instead of reading every
page to find "recursion" (full table scan), you check the index,
get page 247, and go straight there (index lookup).

CODE:
-- Without index: scans 1M rows
SELECT * FROM users WHERE email = 'alice@example.com';
-- Execution time: 1200ms

-- Create index on email column
CREATE INDEX idx_users_email ON users(email);

-- With index: looks up directly
SELECT * FROM users WHERE email = 'alice@example.com';
-- Execution time: 2ms
```

## Generate Visual Aids

Include diagrams when they clarify flow, state, or data transformation.

### Generate ASCII Diagrams for:
Request flows, architecture, and component relationships.

```
Request flow through middleware:

Request -> [Auth] -> [RateLimit] -> [Logging] -> Handler -> Response
             |            |             |
             v            v             v
          Reject       Reject        Log DB
         (401/403)      (429)
```

### Generate State Transition Tables for:
State machines, event handling, and workflow logic.

```
Event Sourcing State Machine:

| Current State | Event Received  | New State  | Side Effect      |
|---------------|-----------------|------------|------------------|
| Empty         | AddItem         | HasItems   | Update total     |
| HasItems      | AddItem         | HasItems   | Update total     |
| HasItems      | RemoveItem      | HasItems   | Update total     |
| HasItems      | RemoveItem      | Empty      | Clear total      |
| HasItems      | Checkout        | Processing | Start payment    |
| Processing    | PaymentSuccess  | Complete   | Send confirmation|
| Processing    | PaymentFailed   | HasItems   | Show error       |
```

### Generate Data Flow Visualizations for:
Pipelines, transformations, and ETL processes.

```python
# Data transformation pipeline:
#
# Raw Data    ->    Clean    ->    Enrich    ->    Aggregate    ->    Output
# [1M rows]        [800K]         [800K]          [summary]         [JSON]
#
pipeline = (
    extract_from_source()          # Raw data (1M rows)
    .pipe(remove_invalid_rows)     # Clean (800K rows)
    .pipe(add_derived_fields)      # Enrich (same rows, more columns)
    .pipe(group_and_aggregate)     # Aggregate (summary stats)
    .pipe(format_as_json)          # Output (JSON report)
)
```

## Explaining Error Handling

When the project code includes error handling, explain failure modes explicitly.

```python
# What could go wrong?
# 1. Network timeout -> retry with backoff
# 2. Invalid response -> parse error, log and skip
# 3. Rate limited -> wait and retry
# 4. Unknown error -> log, alert, fail gracefully

def fetch_with_resilience(url: str, max_retries: int = 3) -> dict:
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.Timeout:
            # Network slow--exponential backoff
            wait = 2 ** attempt
            logger.warning(f"Timeout, retry in {wait}s")
            time.sleep(wait)

        except requests.HTTPError as e:
            if e.response.status_code == 429:
                # Rate limited--respect Retry-After header
                wait = int(e.response.headers.get("Retry-After", 60))
                logger.warning(f"Rate limited, waiting {wait}s")
                time.sleep(wait)
            else:
                # Other HTTP error--don't retry
                raise

        except json.JSONDecodeError:
            # Bad response body--log and fail
            logger.error(f"Invalid JSON from {url}")
            raise

    raise Exception(f"Failed after {max_retries} retries")
```

## Generation Checklist

Before delivering a code explanation, verify:

```
[] Started with the problem, not the code
[] Explained WHY this approach was chosen
[] Included runnable examples where applicable
[] Used comments for reasoning, not line narration
[] Showed expected output or result
[] Addressed failure modes and error handling
[] Built complexity incrementally for complex code
[] Added visual diagrams where they aid understanding
```
