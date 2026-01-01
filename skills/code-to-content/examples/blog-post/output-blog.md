# How Switching Serializers Cut Our Cache Response Time by 73%

Last Tuesday, our monitoring dashboard lit up red. Cache response times had crept from 0.3ms to 1.1ms over three months, and users were starting to notice. The culprit? Python's pickle, doing far more work than we needed.

Here's how a single dependency swap transformed our caching layer.

---

## The Problem: Pickle's Hidden Overhead

When we built fast-cache, pickle seemed like the obvious choice. It handles arbitrary Python objects and ships with the standard library. What's not to like?

Plenty, as it turns out.

```python
# Our original approach - simple but slow
def cache_set(self, key: str, value: Any) -> None:
    serialized = pickle.dumps(value)  # The bottleneck
    self.redis.set(key, serialized)
```

Profiling revealed pickle was spending 60% of its time handling type metadata we never used. We were serializing dictionaries and lists—structures that don't need Python's full object machinery.

The data told the story clearly:

| Metric | With Pickle |
|--------|-------------|
| Avg serialization time | 0.8ms |
| Memory per 1M keys | 2.1GB |
| CPU during serialization | 12% |

---

## The Insight: Match the Serializer to the Data

The realization came from examining what we were actually caching: JSON-like structures. No custom classes. No circular references. Just data.

If our data was simple, why was our serializer complex?

We ran a quick experiment. Same workload, three serializers:

```python
# Test results (1000 iterations, 10KB payload)
pickle.dumps(data)    # 0.83ms avg
json.dumps(data)      # 0.45ms avg
msgpack.packb(data)   # 0.24ms avg  # Winner
```

MessagePack was 3.5x faster than pickle. And it used less memory because binary encoding is more compact than pickle's format.

---

## The Solution: MessagePack

MessagePack is like JSON's faster cousin—binary instead of text, but supporting the same data types.

```python
# The change that mattered
import msgpack

def cache_set(self, key: str, value: Any) -> None:
    # use_bin_type ensures bytes stay as bytes
    serialized = msgpack.packb(value, use_bin_type=True)
    self.redis.set(key, serialized)

def cache_get(self, key: str) -> Any:
    data = self.redis.get(key)
    if data is None:
        return None
    return msgpack.unpackb(data, raw=False)
```

That's it. One import change, two method swaps.

For safety, we kept pickle as a fallback through our `SerializerFactory`:

```python
class SerializerFactory:
    @staticmethod
    def create(format: str = "msgpack") -> Serializer:
        serializers = {
            "msgpack": MsgPackSerializer(),
            "json": JsonSerializer(),
            "pickle": PickleSerializer(),  # Legacy support
        }
        return serializers.get(format, serializers["msgpack"])
```

---

## The Results

After deploying the change:

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Avg response time | 1.1ms | 0.3ms | **-73%** |
| Memory per 1M keys | 2.1GB | 1.3GB | **-40%** |
| Serialization CPU | 12% | 4% | **-67%** |
| Cache hit rate | 89% | 94.2% | **+5.2%** |

The cache hit rate improvement was unexpected. Faster serialization meant we could cache more aggressively without impacting response times.

---

## The Lesson

The fastest code isn't always the cleverest—sometimes it's the code that doesn't try to do too much.

Pickle is powerful because it handles everything. MessagePack is fast because it handles exactly what we need.

Before reaching for the general-purpose tool, ask: **what does my data actually look like?**

Three questions to guide serializer choice:

1. **Do you need to serialize custom classes?** If yes, you might need pickle. If no, you probably don't.
2. **Is human readability required?** JSON for yes, binary formats for no.
3. **What's your performance budget?** Profile before assuming.

---

## What's Next

We're still working on some improvements:

- **Cluster support** for horizontal scaling (the TODO we haven't tackled yet)
- **Fixing the race condition** in `batch_invalidate` (the FIXME that keeps us humble)

If you're facing similar serialization overhead, check out our implementation in the [fast-cache repository](#). The before/after is all in the git history.

---

*Have you run into unexpected performance bottlenecks from standard library choices? I'd love to hear your stories in the comments.*
