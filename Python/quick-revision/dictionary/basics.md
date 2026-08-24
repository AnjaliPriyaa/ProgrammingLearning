# Level 1 — What you should remember for interviews

| Concept | Remember |
| --- | --- |
| Lookup | `dict[key]` |
| Safe lookup | `dict.get(key)` |
| Add/update | `dict[key] = value` |
| Delete | `del dict[key]` / `pop()` |
| Keys | `.keys()` |
| Values | `.values()` |
| Both | `.items()` |
| Check key | `key in dict` |
| Merge | `a \| b` |
| Modify merge | `a.update(b)` |
| Comprehension | `{k: v for ...}` |
| Sort | `sorted(dict.items())` |
| Max value key | `max(d, key=d.get)` |
| Min value key | `min(d, key=d.get)` |
| List → dict | `dict(zip(keys, values))` |
| Dict → list | `list(d.items())` |

## `data["age"]` vs `data.get("age")`

- `data["age"]` — use this when you know the key must exist (raises `KeyError` if missing)
- `data.get("age")` — use this when the key might not exist. You can also provide a default:

```python
salary = data.get("salary", 0)
print(salary)
```

## `setdefault()` — if the key exists, give me its value; otherwise create it with a default

What is `setdefault()` actually doing? This one is confusing initially.

Suppose:

```python
data = {}
```

You want to maintain a list of errors. The long way:

```python
if "errors" not in data:
    data["errors"] = []

data["errors"].append("500")
```

After that:

```python
{"errors": ["500"]}
```

`setdefault()` simply makes this shorter:

```python
data.setdefault("errors", [])
data["errors"].append("500")
```

Think of `data.setdefault("errors", [])` as: **if `errors` exists, give me its value; otherwise create `errors` with an empty list.**

## Duplicate values when reversing a dictionary

You had:

```python
data = {
    "A": 1,
    "B": 1
}
```

If you do:

```python
result = {
    value: key
    for key, value in data.items()
}
```

You get:

```python
{
    1: "B"
}
```

Why? Because dictionary keys must be unique.

The first operation is effectively:

```python
result[1] = "A"
```

Then:

```python
result[1] = "B"
```

So `"B"` replaces `"A"`.

What should we do instead? Depends on what the interviewer wants.

**Option 1 — Keep all keys**

Create:

```python
{
    1: ["A", "B"]
}
```

Use `setdefault()`:

```python
data = {
    "A": 1,
    "B": 1,
    "C": 2
}

result = {}

for key, value in data.items():
    result.setdefault(value, []).append(key)

print(result)
```

Output:

```python
{
    1: ["A", "B"],
    2: ["C"]
}
```

⭐ This is the correct solution if duplicate values need to be preserved.

## What if two lists have different lengths?

You had:

```python
keys = ["name", "age", "city"]
values = ["Anjali", 25]
```

Then:

```python
dict(zip(keys, values))
```

gives:

```python
{
    "name": "Anjali",
    "age": 25
}
```

`"city"` is silently ignored.

What should we do? Again, depends on the requirement.

**If unequal lengths should be an error**

Check first:

```python
if len(keys) != len(values):
    raise ValueError("Lists must have the same length")

result = dict(zip(keys, values))
```

This is usually the best interview answer if the data is expected to correspond one-to-one.

**If you intentionally want missing values**

Use `zip_longest()`:

```python
from itertools import zip_longest

result = dict(
    zip_longest(keys, values, fillvalue=None)
)
```

Result:

```python
{
    "name": "Anjali",
    "age": 25,
    "city": None
}
```

⭐ Interview point

- `zip()`: stops at the shortest input.
- `zip_longest()`: continues until the longest input.

## `get()` vs `setdefault()` vs `[]`

This is very important.

**`[]`**

```python
data["age"]
```

Means: *Give me the value. I expect the key to exist.*

Missing key → `KeyError`

**`get()`**

```python
data.get("age")
```

Means: *Give me the value if it exists; otherwise give me `None` or my default.*

Example: `data.get("age", 0)` — missing key → `0`.

Does **NOT** modify the dictionary.

**`setdefault()`**

```python
data.setdefault("age", 0)
```

Means: *Give me the value if it exists; otherwise INSERT `age: 0` and give me that value.*

Example:

```python
data = {}

age = data.setdefault("age", 0)

print(age)
print(data)
```

Output:

```python
0
{"age": 0}
```

## `copy()` vs `deepcopy()`

Consider:

```python
a = {
    "name": "Anjali",
    "skills": ["Python", "AWS"]
}
```

**Shallow copy**

```python
b = a.copy()
```

The outer dictionary is copied, but nested objects are shared.

```text
a ──→ dictionary
       │
       └──→ skills list ←── b
```

Therefore:

```python
b["skills"].append("Kubernetes")
```

also affects `a`.

**Deep copy**

```python
import copy

b = copy.deepcopy(a)
```

Now nested objects are copied too.

```text
a ──→ dictionary ──→ list

b ──→ dictionary ──→ separate list
```

So changing:

```python
b["skills"].append("Kubernetes")
```

doesn't affect `a`.

**Interview answer**

- `copy()` → shallow copy
- `deepcopy()` → recursively copies nested objects
