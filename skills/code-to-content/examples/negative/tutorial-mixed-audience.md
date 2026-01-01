# Negative Example: Mixed Audience Levels

## Gate Failed

**Phase 5 Gate** — Readability Threshold

## Rule Violated

From `SKILL.md` → Readability Thresholds table:

| Audience | Flesch-Kincaid Grade | Max Jargon Density |
|----------|---------------------|-------------------|
| Beginner developers | ≤ 8.0 | 2% |

## Failing Content

```markdown
# Getting Started with React

## Prerequisites

Before we begin, ensure you have Node.js installed and understand the
fundamentals of JavaScript's event loop, closure semantics, and the
prototype chain.

## Your First Component

Let's create a simple component. First, we'll establish our component's
invariants through proper encapsulation of state mutations within the
reconciliation lifecycle.

```jsx
const Counter = () => {
  // Leveraging the useState hook's tuple destructuring pattern
  const [count, setCount] = useState(0);

  // Memoized callback to prevent unnecessary reconciliation
  const increment = useCallback(() => setCount(c => c + 1), []);

  return <button onClick={increment}>{count}</button>;
};
```

The above exemplifies React's unidirectional data flow paradigm...
```

**Measured Metrics:**
- Flesch-Kincaid Grade Level: **13.5**
- Jargon Density: **8%**

## Why It Fails

1. **Grade level too high** — 13.5 exceeds the ≤8.0 threshold for beginners
2. **Jargon overload** — "reconciliation lifecycle," "tuple destructuring pattern," "unidirectional data flow paradigm"
3. **Prerequisites mismatch** — Asking beginners to understand "closure semantics" and "prototype chain"
4. **Comments add complexity** — Code comments use expert terminology

## Corrected Version

```markdown
# Getting Started with React

## What You Need

- Node.js installed on your computer
- Basic JavaScript knowledge (variables, functions, arrays)

## Your First Component

A component is like a custom HTML tag that you create. Let's make a
button that counts clicks.

```jsx
const Counter = () => {
  // This creates a variable 'count' that React will remember
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount(count + 1)}>
      Clicked {count} times
    </button>
  );
};
```

When you click the button, `setCount` updates the number, and React
automatically refreshes what you see on screen.
```

**Corrected Metrics:**
- Flesch-Kincaid Grade Level: **6.8**
- Jargon Density: **1.5%**

## Why It Passes

1. **Grade level appropriate** — 6.8 is under the 8.0 threshold
2. **Plain language** — "React will remember" instead of "state persistence"
3. **Matched prerequisites** — Only asks for "basic JavaScript"
4. **Helpful comments** — Explain what code does, not how it works internally

## Related Evaluation Question

> Q: Content targeting beginner developers has a Flesch-Kincaid grade level of 13.5. According to the Readability Thresholds table in SKILL.md, does this PASS or FAIL the Phase 5 gate?
>
> A: **FAIL**
