# Lesson CS-08: Recursion and Dynamic Programming

[← Sorting & Searching](lesson-cs07-sorting-searching.md) | [Back to TOC](../README.md) | [Next: Discrete Math →](lesson-cs09-discrete-math.md)

---

> **Tutor Instructions:** When walking a student through this lesson, don't just explain the concepts — create a series of small, progressive coding tasks that require the student to actively use each concept covered. Explain the relevant material, then immediately give a hands-on task before moving on. Review their solutions and correct mistakes before proceeding. Tasks should escalate in complexity throughout the lesson: start with ~1-minute exercises with immediate feedback, build to ~5-minute tasks, then ~10-minute tasks, and culminate in a ~30-minute capstone that integrates multiple concepts from the lesson. Let the student control the pace. Target ~2.5 hours for guided tutoring (explanations + coding tasks), then direct the student to spend ~1.5 hours doing LeetCode problems on their own to reinforce the concepts.

> **Why this lesson exists:** Recursion is how you think about problems that have substructure — and neural networks are *full* of substructure (layers calling layers, recursive computation graphs, self-attention as a recursive operation). Dynamic programming is the art of caching repeated work, which is essentially what memoization in autograd systems does. These problem-solving skills transfer directly.

## Core Concepts

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

### Backtracking vs DP Decision

| Backtracking | DP |
|-------------|-----|
| Find ALL solutions | Find ONE optimal value (min/max/count) |
| Path/arrangement matters | Only result matters |
| No overlapping subproblems (or state too complex to cache) | Overlapping subproblems |
| Exponential is acceptable (small n) | Polynomial solution exists |

### Top-Down vs Bottom-Up

| Top-Down (Memoization) | Bottom-Up (Tabulation) |
|------------------------|----------------------|
| Recursive + cache | Iterative + table |
| Only computes needed states | Computes all states |
| Easier to write (natural recursion) | Easier to optimize space |
| Risk of stack overflow on deep recursion | No recursion limit |
| Use `@cache` (Python) or `memo[]` array (C++) | Use `dp[]` array with loops |

### Space Optimization Patterns

| Technique | When to use |
|-----------|-------------|
| Two variables | Current row depends only on previous 1-2 values (Fibonacci, House Robber) |
| Single row | 2D DP where each row depends only on previous row (grid paths, knapsack) |
| Rolling array | Keep only last 2 rows instead of full table |

### Common DP Categories

- **1D DP:** climbing stairs, house robber, coin change
- **2D DP:** longest common subsequence, edit distance, grid paths
- **Knapsack:** 0/1 knapsack, unbounded knapsack, subset sum
- **String DP:** palindromes, edit distance, regex matching

## Watch

1. **NeetCode — "Dynamic Programming" playlist**
   - Start with his 1D DP videos, then 2D DP
2. **NeetCode — "Climbing Stairs" walkthrough** — the simplest DP problem, perfectly explained
3. **Reducible — "5 Simple Steps for Solving Dynamic Programming Problems"** (optional, good framework)

## Practice Problems (NeetCode 150)

**Strategy:** start with House Robber — it makes the DP pattern click. Then Coin Change. Once 1D DP feels natural, move to 2D. Backtracking and Greedy are included here because they build on the same recursive thinking.

---

### Backtracking

**When to use:** "generate all...", "find all...", constraint satisfaction, combinatorial search. You need every valid configuration, not just a count or optimum.

**The universal pattern:**
```
def backtrack(state):
    if goal_reached: record solution; return
    for each choice:
        if valid:
            make choice
            backtrack(next state)
            undo choice      <- this is what makes it backtracking
```

#### Subsets

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 1 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | Backtrack + skip duplicates | Medium |

#### Permutations

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 2 | [Permutations](https://leetcode.com/problems/permutations/) | Swap / used-set backtracking | Medium |

#### Combinations

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 3 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | Backtrack with reuse | Medium |
| 4 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Backtrack + skip duplicates | Medium |
| 5 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Backtracking | Medium |

#### Partitioning

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 6 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Backtrack + palindrome check | Medium |

#### Constraint Placement

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 7 | [N-Queens](https://leetcode.com/problems/n-queens/) | Constraint backtracking | Hard |

---

### 1-D DP

**When to use:** problem has a single sequence/array dimension; you need one optimal value (min, max, count); `dp[i]` depends on a small number of previous entries.

**State:** `dp[i]` = answer considering first `i` elements (or up to position `i`).

#### Fibonacci Variant

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 8 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | `dp[i] = dp[i-1] + dp[i-2]` | Easy |
| 13 | [Decode Ways](https://leetcode.com/problems/decode-ways/) | `dp[i] = dp[i-1] + dp[i-2]` (conditional) | Medium |

#### Take/Skip

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 9 | [House Robber](https://leetcode.com/problems/house-robber/) | `dp[i] = max(dp[i-1], dp[i-2] + val[i])` | Medium |
| 10 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | Circular skip/take | Medium |

#### Min/Max to Reach

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 14 | [Coin Change](https://leetcode.com/problems/coin-change/) | `dp[i] = min(dp[i-c] + 1) for c in coins` | Medium |

#### Longest Increasing

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 16 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | `dp[i] = max(dp[j] + 1) for j < i` | Medium |

#### Can Partition

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 17 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | `dp[s] = dp[s] or dp[s - num]` (boolean, 0/1 knapsack) | Medium |

#### String Decomposition

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 15 | [Word Break](https://leetcode.com/problems/word-break/) | `dp[i] = any(dp[j] and s[j:i] in dict)` | Medium |

#### Expand from Center

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 11 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Expand outward from each position | Medium |
| 12 | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Expand from center | Medium |

---

### 2-D DP

**When to use:** problem is defined by two parameters (two strings, a grid, an interval, items + capacity); `dp[i][j]` captures the subproblem.

**State:** `dp[i][j]` = answer for subproblem defined by two parameters.

#### Grid Paths

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 18 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | `dp[i][j]` = ways to reach cell (i,j) | Medium |

#### Two-String Comparison

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 19 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | `dp[i][j]` = answer for `s1[:i]` and `s2[:j]` | Medium |
| 24 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | `dp[i][j]` = min ops for `s1[:i]` → `s2[:j]` | Medium |
| 22 | [Interleaving String](https://leetcode.com/problems/interleaving-string/) | `dp[i][j]` = can form target from `s1[:i]` + `s2[:j]` | Medium |
| 23 | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | `dp[i][j]` = # ways `t[:j]` appears in `s[:i]` | Hard |

#### String Matching

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 26 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | `dp[i][j]` = does `s[:i]` match `p[:j]`? | Hard |

#### Interval DP

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 25 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | `dp[i][j]` = answer for subarray `[i..j]` | Hard |

#### Knapsack 2D

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 21 | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | `dp[i][j]` = ways using first `i` items with capacity `j` | Medium |

#### State Machine

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 20 | [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | `dp[i][state]` = best value at day `i` in given state | Medium |

---

### Greedy

**When to use:** a locally optimal choice at each step leads to the globally optimal solution. No backtracking or memoization needed. Often provable by exchange argument or greedy-stays-ahead.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 27 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Greedy BFS-style reachability | Medium |
| 28 | [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | Greedy filtering | Medium |
| 29 | [Partition Labels](https://leetcode.com/problems/partition-labels/) | Greedy + last occurrence | Medium |
| 30 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | Greedy range tracking | Medium |

## ML Connection

Memoization IS caching intermediate activations during the forward pass so backprop can reuse them — PyTorch does this automatically. The Viterbi algorithm (used in sequence models like HMMs) is DP. Beam search in language models is a DP-like algorithm. Even gradient checkpointing (a memory optimization in large model training) is a time-space tradeoff that mirrors the choice between top-down memoization and bottom-up tabulation.
