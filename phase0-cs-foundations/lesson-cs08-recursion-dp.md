# Lesson CS-08: Recursion and Dynamic Programming

[← Sorting & Searching](lesson-cs07-sorting-searching.md) | [Back to TOC](../README.md) | [Next: Discrete Math →](lesson-cs09-discrete-math.md)

---

> **Tutor Instructions:** When walking a student through this lesson, don't just explain the concepts — create a series of small, progressive coding tasks that require the student to actively use each concept covered. Explain the relevant material, then immediately give a hands-on task before moving on. Review their solutions and correct mistakes before proceeding. Tasks should escalate in complexity throughout the lesson: start with ~1-minute exercises with immediate feedback, build to ~5-minute tasks, then ~10-minute tasks, and culminate in a ~30-minute capstone that integrates multiple concepts from the lesson. Let the student control the pace. Target ~2.5 hours for guided tutoring (explanations + coding tasks), then direct the student to spend ~1.5 hours doing LeetCode problems on their own to reinforce the concepts.

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

## 🔨 Practice Problems (NeetCode 150)

**Strategy:** start with House Robber — it makes the DP pattern click. Then Coin Change. Once 1D DP feels natural, move to 2D. Backtracking and Greedy are included here because they build on the same recursive thinking.

| # | Problem | Category | Pattern | Difficulty |
|---|---------|----------|---------|------------|
| 1 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | Backtracking | Backtrack with reuse | Medium |
| 2 | [Permutations](https://leetcode.com/problems/permutations/) | Backtracking | Swap / used-set backtracking | Medium |
| 3 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | Backtracking | Backtrack + skip duplicates | Medium |
| 4 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Backtracking | Backtrack + skip duplicates | Medium |
| 5 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Backtracking | Backtrack + palindrome check | Medium |
| 6 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Backtracking | Backtracking | Medium |
| 7 | [N-Queens](https://leetcode.com/problems/n-queens/) | Backtracking | Constraint backtracking | Hard |
| 8 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | 1-D DP | Fibonacci variant | Easy |
| 9 | [House Robber](https://leetcode.com/problems/house-robber/) | 1-D DP | Skip/take DP | Medium |
| 10 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | 1-D DP | Circular skip/take | Medium |
| 11 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | 1-D DP | Expand from center / DP | Medium |
| 12 | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | 1-D DP | Expand from center | Medium |
| 13 | [Decode Ways](https://leetcode.com/problems/decode-ways/) | 1-D DP | 1D DP | Medium |
| 14 | [Coin Change](https://leetcode.com/problems/coin-change/) | 1-D DP | Unbounded knapsack | Medium |
| 15 | [Word Break](https://leetcode.com/problems/word-break/) | 1-D DP | 1D DP + hash set | Medium |
| 16 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | 1-D DP | 1D DP or patience sort | Medium |
| 17 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | 1-D DP | 0/1 knapsack | Medium |
| 18 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | 2-D DP | Grid DP | Medium |
| 19 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | 2-D DP | String DP | Medium |
| 20 | [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | 2-D DP | State machine DP | Medium |
| 21 | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | 2-D DP | Unbounded knapsack 2D | Medium |
| 22 | [Interleaving String](https://leetcode.com/problems/interleaving-string/) | 2-D DP | 2D string DP | Medium |
| 23 | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | 2-D DP | 2D string DP | Hard |
| 24 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | 2-D DP | 2D string DP | Medium |
| 25 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | 2-D DP | Interval DP | Hard |
| 26 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | 2-D DP | 2D string DP | Hard |
| 27 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Greedy | Greedy BFS-style | Medium |
| 28 | [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | Greedy | Greedy filtering | Medium |
| 29 | [Partition Labels](https://leetcode.com/problems/partition-labels/) | Greedy | Greedy + last occurrence | Medium |
| 30 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | Greedy | Greedy range tracking | Medium |

## 🔗 ML Connection

Memoization IS caching intermediate activations during the forward pass so backprop can reuse them — PyTorch does this automatically. The Viterbi algorithm (used in sequence models like HMMs) is DP. Beam search in language models is a DP-like algorithm. Even gradient checkpointing (a memory optimization in large model training) is a time-space tradeoff that mirrors the choice between top-down memoization and bottom-up tabulation.
