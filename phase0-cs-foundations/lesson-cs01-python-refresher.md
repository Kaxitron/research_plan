# Lesson CS-01: Python Refresher — Getting Your Hands Dirty Again

[Back to TOC](../README.md) | [Next: C++ Refresher →](lesson-cs02-cpp-refresher.md)

---

> **Why this lesson exists:** You have intermediate Python skills but haven't coded daily in a while. This lesson is about rebuilding muscle memory — variables, control flow, functions, I/O, string manipulation, and Pythonic idioms. By the end, you should be able to open a blank file and solve a problem without Googling basic syntax.

## 🎯 Core Skills

### Variables, Types, and Operations

- **Dynamic typing:** `x = 5` then `x = "hello"` is legal. Know the tradeoff: flexible but error-prone.
- **Core types:** `int`, `float`, `str`, `bool`, `None`
- **Type checking:** `type(x)`, `isinstance(x, int)`
- **String operations you'll use constantly:**
  ```python
  s = "hello world"
  s.split()          # ['hello', 'world']
  s.strip()          # remove whitespace
  s.replace("o", "0")
  s.find("world")    # 6 (index) or -1
  f"value is {x}"    # f-strings — use these always
  s[::-1]            # reverse a string
  ```

### Control Flow

- `if/elif/else`, `for`, `while`, `break`, `continue`
- **`for` with `enumerate`:** `for i, val in enumerate(lst):`
- **`for` with `zip`:** `for a, b in zip(list1, list2):`
- **Ternary:** `result = x if condition else y`

### Functions

- `def`, `return`, default arguments, `*args`, `**kwargs`
- **Lambda functions:** `f = lambda x: x**2` — useful for `sorted(lst, key=lambda x: x[1])`
- **Scope:** local vs global. Avoid `global` — pass arguments and return values instead.

### Data Structures (Built-In)

- **Lists:** `append`, `pop`, `insert`, `sort`, `reverse`, slicing `lst[start:end:step]`
- **List comprehensions:** `[x**2 for x in range(10) if x % 2 == 0]`
- **Dictionaries:** `d[key]`, `d.get(key, default)`, `d.keys()`, `d.values()`, `d.items()`
- **Dict comprehensions:** `{k: v for k, v in pairs}`
- **Sets:** `add`, `remove`, `union`, `intersection`, `difference` — O(1) lookup
- **Tuples:** immutable, can be dict keys, used for multiple return values

### File I/O

```python
# Reading
with open("file.txt", "r") as f:
    content = f.read()       # whole file as string
    lines = f.readlines()    # list of lines

# Writing
with open("output.txt", "w") as f:
    f.write("hello\n")

# CSV
import csv
with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### Standard Library Highlights

- `collections`: `Counter`, `defaultdict`, `deque`
- `itertools`: `combinations`, `permutations`, `product`
- `functools`: `lru_cache` (memoization for free!)
- `math`: `sqrt`, `log`, `ceil`, `floor`, `gcd`
- `heapq`: `heappush`, `heappop` — min-heap by default

## 📺 Watch

1. **NeetCode — "Python for Coding Interviews"**
   - https://www.youtube.com/watch?v=0K_eZGS5NsU
   - *Compact overview of everything you need for LeetCode-style problems in Python.*

## 🔨 Practice Problems

Solve these in a blank file (no IDE autocomplete). The goal is rebuilding fluency.

1. **FizzBuzz** — print 1–100, replacing multiples of 3 with "Fizz", 5 with "Buzz", both with "FizzBuzz"
2. **Two Sum** (LeetCode #1) — given an array and target, return indices of two numbers that add to target. Use a hash map.
3. **Valid Anagram** (LeetCode #242) — are two strings anagrams? Use `Counter`.
4. **Reverse a linked list** — define a `ListNode` class, build a list, reverse it iteratively.
5. **Read a CSV, compute column averages** — practice file I/O + list processing.
6. **Implement a stack using a list** — `push`, `pop`, `peek`, `is_empty`. Then use it to check balanced parentheses (LeetCode #20).

## 🔗 ML Connection

Python is the language of ML research. Every paper's code, every PyTorch model, every interpretability tool is Python. The built-in data structures (dicts, sets, list comprehensions) show up constantly when processing model outputs, tokenizer vocabularies, and attention patterns.
