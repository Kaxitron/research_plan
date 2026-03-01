# Lesson CS-08: Recursion and Dynamic Programming

[← Sorting & Searching](lesson-cs07-sorting-searching.md) | [Back to TOC](../README.md) | [Next: Discrete Math →](lesson-cs09-discrete-math.md)

---

> **Why this lesson exists:** Recursion is how you think about problems that have substructure — and neural networks are *full* of substructure (layers calling layers, recursive computation graphs, self-attention as a recursive operation). Dynamic programming is the art of caching repeated work, which is essentially what memoization in autograd systems does. These problem-solving skills transfer directly.

## 🎯 Core Concepts

### Recursion — Functions That Call Themselves

Every recursive function needs:
1. **Base case:** when to stop (prevents infinite recursion)
2. **Recursive case:** break the problem into smaller versions of itself

```python
def factorial(n):
    if n <= 1: return 1          # base case
    return n * factorial(n - 1)  # recursive case

def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)  # two recursive calls
```

**The call stack:** each recursive call pushes a frame onto the stack. Too deep = `RecursionError` (Python default limit: 1000). This is why iterative solutions sometimes matter.

**Visualize the recursion tree:** `fibonacci(5)` calls `fibonacci(4)` and `fibonacci(3)`. `fibonacci(4)` calls `fibonacci(3)` and `fibonacci(2)`. Notice `fibonacci(3)` is computed **twice**. This is the problem DP solves.

### Dynamic Programming — Cache the Repeated Work

**The key question:** does this problem have *overlapping subproblems* (same sub-computation done multiple times) and *optimal substructure* (optimal solution built from optimal sub-solutions)?

**Top-down (memoization):** recursive, but cache results.
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)
# Now fibonacci(50) is instant instead of taking years
```

**Bottom-up (tabulation):** iterative, fill a table from small → large.
```python
def fibonacci(n):
    if n <= 1: return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

**Space optimization:** often you only need the last 1–2 values, not the whole table.
```python
def fibonacci(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### DP Problem-Solving Framework

1. **Define the subproblem:** what does `dp[i]` represent?
2. **Find the recurrence:** how does `dp[i]` relate to smaller subproblems?
3. **Identify base cases:** what are `dp[0]`, `dp[1]`, etc.?
4. **Determine computation order:** which subproblems must be solved first?
5. **Optimize space** if possible.

### Common DP Categories

- **1D DP:** climbing stairs, house robber, coin change
- **2D DP:** longest common subsequence, edit distance, grid paths
- **Knapsack:** 0/1 knapsack, unbounded knapsack, subset sum
- **String DP:** palindromes, edit distance, regex matching

## 📺 Watch

1. **NeetCode — "Dynamic Programming" playlist**
   - Start with his 1D DP videos, then 2D DP
2. **NeetCode — "Climbing Stairs" walkthrough** — the simplest DP problem, perfectly explained
3. **Reducible — "5 Simple Steps for Solving Dynamic Programming Problems"** (optional, good framework)

## 🔨 Practice Problems

| # | Problem | Category | Difficulty |
|---|---------|----------|------------|
| 1 | Climbing Stairs (LC #70) | 1D DP (fibonacci variant) | Easy |
| 2 | House Robber (LC #198) | 1D DP | Medium |
| 3 | Coin Change (LC #322) | Unbounded knapsack | Medium |
| 4 | Longest Increasing Subsequence (LC #300) | 1D DP | Medium |
| 5 | Unique Paths (LC #62) | 2D DP (grid) | Medium |
| 6 | Longest Common Subsequence (LC #1143) | 2D DP (strings) | Medium |
| 7 | Word Break (LC #139) | 1D DP + hash set | Medium |
| 8 | 0/1 Knapsack | Classic DP | Medium |
| 9 | Edit Distance (LC #72) | 2D DP | Medium |
| 10 | Decode Ways (LC #91) | 1D DP | Medium |

**Strategy:** solve Climbing Stairs and House Robber first — they make the pattern click. Then Coin Change. Once 1D DP feels natural, move to 2D.

## 🔗 ML Connection

Memoization IS caching intermediate activations during the forward pass so backprop can reuse them — PyTorch does this automatically. The Viterbi algorithm (used in sequence models like HMMs) is DP. Beam search in language models is a DP-like algorithm. Even gradient checkpointing (a memory optimization in large model training) is a time-space tradeoff that mirrors the choice between top-down memoization and bottom-up tabulation.
