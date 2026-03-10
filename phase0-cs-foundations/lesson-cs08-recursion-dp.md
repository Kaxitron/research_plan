# Lesson CS-08: Recursion and Dynamic Programming

[← Sorting & Searching](lesson-cs07-sorting-searching.md) | [Back to TOC](../README.md) | [Next: Discrete Math →](lesson-cs09-discrete-math.md)

---

> **Tutor Instructions:** When walking a student through this lesson, don't just explain the concepts — create a series of small, progressive coding tasks that require the student to actively use each concept covered. Explain the relevant material, then immediately give a hands-on task before moving on. Review their solutions and correct mistakes before proceeding. Tasks should escalate in complexity throughout the lesson: start with ~1-minute exercises with immediate feedback, build to ~5-minute tasks, then ~10-minute tasks, and culminate in a ~30-minute capstone that integrates multiple concepts from the lesson. Let the student control the pace. Target ~2.5 hours for guided tutoring (explanations + coding tasks), then direct the student to spend ~1.5 hours doing LeetCode problems on their own to reinforce the concepts.

> **Why this lesson exists:** Recursion is how you think about problems that have substructure — and neural networks are *full* of substructure (layers calling layers, recursive computation graphs, self-attention as a recursive operation). Dynamic programming is the art of caching repeated work, which is essentially what memoization in autograd systems does. These problem-solving skills transfer directly.

---

## Part 1: Recursion

### The Basics

Every recursive function needs:
1. **Base case:** when to stop (prevents infinite recursion)
2. **Recursive case:** break the problem into smaller versions of itself

```python
def factorial(n):
    if n <= 1: return 1          # base case
    return n * factorial(n - 1)  # recursive case
```

**The call stack:** each recursive call pushes a frame onto the stack. Too deep = `RecursionError` (Python default limit: 1000). This is why iterative solutions sometimes matter.

### Recursion Patterns

#### Linear Recursion
One recursive call per level. Reduces by one element each time. Easy to convert to iteration.
```python
def sum_list(arr, i=0):
    if i == len(arr): return 0
    return arr[i] + sum_list(arr, i + 1)
```
**Seen in:** linked list traversal, array processing, tail-recursive algorithms.

#### Binary / Tree Recursion
Two (or more) recursive calls per level. Creates a tree of calls.
```python
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)    # two branches → exponential without caching
```
**Seen in:** fibonacci, tree traversals, divide and conquer.

**Visualize the recursion tree:** `fib(5)` calls `fib(4)` and `fib(3)`. `fib(4)` calls `fib(3)` and `fib(2)`. Notice `fib(3)` is computed **twice**. This is the problem DP solves.

#### Divide and Conquer
Split into independent halves, solve each, combine results. Subproblems don't overlap, so this is NOT DP.
```python
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
```
**Seen in:** merge sort, quicksort, binary search, closest pair of points.

#### Backtracking
Try a choice, recurse, undo. Explores all valid configurations.
```python
def backtrack(state):
    if goal: record solution; return
    for choice in choices:
        if valid(choice):
            make(choice)
            backtrack(next_state)
            undo(choice)
```

**Backtracking subtypes:**

| Subtype | Question at each step | Example |
|---------|----------------------|---------|
| Include/exclude | Take this element or skip it? | Subsets |
| Choice from remaining | Which unused element goes here? | Permutations |
| Combinations with reuse | Which element from index onward? (can repeat) | Combination Sum |
| Combinations without reuse | Which element from index onward? (skip dups) | Combination Sum II |
| Partitioning | Where do I cut? | Palindrome Partitioning |
| Grid exploration | Which direction? (with visited tracking) | Word Search |
| Constraint placement | Where does this piece go? | N-Queens, Sudoku |
| Bucket assignment | Which group does this item join? | Partition to K Equal Sum Subsets |

---

## Part 2: Dynamic Programming

### When Does DP Apply?

**DP requires BOTH conditions:**

1. **Overlapping subproblems** — the same sub-computation is repeated multiple times
2. **Optimal substructure** — the optimal solution is built from optimal sub-solutions

**What if you only have one?**
- **Only substructure, no overlap** → **divide and conquer** (e.g., merge sort). Subproblems don't repeat, so there's nothing to cache.
- **Only overlap, no substructure** → DP doesn't apply. E.g., longest simple path in a graph — you revisit nodes, but the best path through node A depends on which nodes you've already visited, so it can't decompose cleanly.
- **Neither** → brute force / backtracking.

**The quick test:** Can I define the answer in terms of smaller versions of the same problem? (→ substructure). Do those smaller versions get recomputed? (→ overlap). Both yes → DP.

### Backtracking vs DP

| Backtracking | DP |
|-------------|-----|
| Find ALL solutions | Find ONE optimal value (min/max/count) |
| Path/arrangement matters | Only the result matters |
| No overlapping subproblems (or state too complex to cache) | Overlapping subproblems |
| Exponential is acceptable (small n) | Polynomial solution exists |

### Top-Down vs Bottom-Up

| Top-Down (Memoization) | Bottom-Up (Tabulation) |
|------------------------|----------------------|
| Recursive + cache | Iterative + table |
| Only computes needed states | Computes all states |
| Easier to write (natural recursion) | Easier to optimize space |
| Risk of stack overflow on deep recursion | No recursion limit |
| `@cache` (Python) or `memo[]` array (C++) | `dp[]` array with loops |

**Top-down (memoization):**
```python
from functools import cache

@cache
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)
```

**Bottom-up (tabulation):**
```python
def fibonacci(n):
    if n <= 1: return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

### Space Optimization

| Technique | When to use |
|-----------|-------------|
| Two variables | `dp[i]` depends only on previous 1–2 values (Fibonacci, House Robber) |
| Single row | 2D DP where each row depends only on previous row (grid paths, knapsack) |
| Rolling array | Keep only last 2 rows instead of full table |

```python
# Fibonacci with two variables
def fibonacci(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### The 5-Step DP Framework

1. **Define the subproblem:** what does `dp[i]` represent?
2. **Find the recurrence:** how does `dp[i]` relate to smaller subproblems?
3. **Identify base cases:** what are `dp[0]`, `dp[1]`, etc.?
4. **Determine computation order:** which subproblems must be solved first?
5. **Optimize space** if possible.

---

## Part 3: DP Pattern Catalog

### Pattern 1: Fibonacci / Linear Recurrence

**Shape:** `dp[i]` depends on `dp[i-1]`, `dp[i-2]` (maybe `dp[i-3]`).

**How to recognize:** "ways to reach step i", "cost to reach step i", fixed number of previous states.

```python
dp[0] = base
dp[1] = base
for i in range(2, n+1):
    dp[i] = f(dp[i-1], dp[i-2])
```

| Problem | Recurrence |
|---------|-----------|
| [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | `dp[i] = dp[i-1] + dp[i-2]` |
| [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | `dp[i] = cost[i] + min(dp[i-1], dp[i-2])` |
| [Decode Ways](https://leetcode.com/problems/decode-ways/) | `dp[i] = dp[i-1] (if valid single) + dp[i-2] (if valid pair)` |
| Tribonacci | `dp[i] = dp[i-1] + dp[i-2] + dp[i-3]` |

---

### Pattern 2: Take or Skip

**Shape:** `dp[i] = max(take this item, skip this item)`.

**How to recognize:** items in a sequence, taking one prevents taking neighbors. "Maximum value without adjacent elements."

```python
dp[0] = val[0]
dp[1] = max(val[0], val[1])
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + val[i])
```

| Problem | Recurrence |
|---------|-----------|
| [House Robber](https://leetcode.com/problems/house-robber/) | `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` |
| [House Robber II](https://leetcode.com/problems/house-robber-ii/) | Run twice: `nums[0:n-1]` and `nums[1:n]` |
| Delete and Earn | Frequency count, then House Robber on values |

---

### Pattern 3: Min/Max Cost to Reach Target

**Shape:** `dp[target]` = min cost. Try all ways to reach target from smaller values.

**How to recognize:** "minimum number of X to make Y", "fewest coins", "minimum steps."

```python
dp = [float('inf')] * (target + 1)
dp[0] = 0
for i in range(1, target + 1):
    for option in options:
        if i - option >= 0:
            dp[i] = min(dp[i], dp[i - option] + 1)
```

| Problem | Recurrence |
|---------|-----------|
| [Coin Change](https://leetcode.com/problems/coin-change/) | `dp[amount] = min(dp[amount - coin] + 1)` for each coin |
| Perfect Squares | `dp[n] = min(dp[n - k*k] + 1)` for each k*k <= n |

---

### Pattern 4: Count Ways to Reach Target

**Shape:** same as Pattern 3 but summing instead of min/max.

**How to recognize:** "how many ways", "number of combinations that sum to."

```python
dp = [0] * (target + 1)
dp[0] = 1
for i in range(1, target + 1):
    for option in options:
        if i - option >= 0:
            dp[i] += dp[i - option]
```

**Subtle distinction — loop order determines whether order matters:**
- Items outer, target inner → **combinations** (unordered): `{1,2}` = `{2,1}`
- Target outer, items inner → **permutations** (ordered): `{1,2}` != `{2,1}`

| Problem | Recurrence |
|---------|-----------|
| [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | `dp[amount] += dp[amount - coin]` (coins outer) |
| Combination Sum IV | `dp[target] += dp[target - num]` (target outer) |

---

### Pattern 5: Longest Increasing Subsequence (LIS)

**Shape:** `dp[i]` = best answer ending at index `i`. Compare against all `j < i`.

**How to recognize:** "longest subsequence with property X", "maximum length chain."

```python
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)
return max(dp)
```

Note: O(n log n) solution exists using binary search + patience sorting.

| Problem | Variation |
|---------|----------|
| [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Standard LIS |
| Number of Longest Increasing Subsequence | Track count alongside length |
| Russian Doll Envelopes | Sort + LIS on second dimension |

---

### Pattern 6: Boolean / Reachability DP

**Shape:** `dp[i]` = True/False, can we reach state `i`?

**How to recognize:** "can you partition", "is it possible", "can you make."

```python
dp = [False] * (target + 1)
dp[0] = True
for num in nums:
    for s in range(target, num - 1, -1):   # reverse to avoid reuse
        dp[s] = dp[s] or dp[s - num]
```

| Problem | Variation |
|---------|----------|
| [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | `dp[sum/2]` reachable? |
| [Word Break](https://leetcode.com/problems/word-break/) | `dp[i] = any(dp[j] and s[j:i] in dict)` |
| [Target Sum](https://leetcode.com/problems/target-sum/) | `dp[offset + target]` after +/- decisions |

---

### Pattern 7: Two-String DP

**Shape:** `dp[i][j]` = answer for `s1[:i]` vs `s2[:j]`. Fill left-to-right, top-to-bottom.

**How to recognize:** two sequences/strings being compared, matched, or transformed.

```python
dp = [[0] * (n+1) for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

| Problem | Match case | Mismatch case |
|---------|------------|---------------|
| [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | `dp[i-1][j-1] + 1` | `max(dp[i-1][j], dp[i][j-1])` |
| [Edit Distance](https://leetcode.com/problems/edit-distance/) | `dp[i-1][j-1]` (no op) | `1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])` |
| [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | `dp[i-1][j-1] + dp[i-1][j]` | `dp[i-1][j]` |
| [Interleaving String](https://leetcode.com/problems/interleaving-string/) | `dp[i-1][j] or dp[i][j-1]` | depends on which string matches |
| [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | `dp[i-1][j-1]` | handle `*`: `dp[i][j-2]` or `dp[i-1][j]` |

---

### Pattern 8: Grid DP

**Shape:** `dp[i][j]` = answer at cell (i,j). Fill top-to-bottom, left-to-right.

**How to recognize:** 2D grid, can only move right/down, count paths or min cost.

```python
dp = [[0] * cols for _ in range(rows)]
dp[0][0] = base
for i in range(rows):
    for j in range(cols):
        if i > 0: dp[i][j] += dp[i-1][j]
        if j > 0: dp[i][j] += dp[i][j-1]
```

| Problem | What dp[i][j] stores |
|---------|---------------------|
| [Unique Paths](https://leetcode.com/problems/unique-paths/) | # ways to reach (i,j) |
| Minimum Path Sum | min cost to reach (i,j) |
| Dungeon Game | min HP needed at (i,j) — fill bottom-right to top-left |

---

### Pattern 9: Knapsack

**Shape:** `dp[i][w]` = best value using first `i` items with weight limit `w`.

**How to recognize:** items with weight/cost and value, capacity constraint.

**0/1 Knapsack** (each item used once):
```python
for i in range(n):
    for w in range(capacity, weight[i] - 1, -1):  # reverse!
        dp[w] = max(dp[w], dp[w - weight[i]] + value[i])
```

**Unbounded Knapsack** (items reusable):
```python
for i in range(n):
    for w in range(weight[i], capacity + 1):       # forward!
        dp[w] = max(dp[w], dp[w - weight[i]] + value[i])
```

**The direction of the inner loop** is the key difference: reverse for 0/1 (prevent reuse), forward for unbounded (allow reuse).

| Problem | Type |
|---------|------|
| [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | 0/1 knapsack (boolean) |
| [Target Sum](https://leetcode.com/problems/target-sum/) | 0/1 knapsack (count) |
| [Coin Change](https://leetcode.com/problems/coin-change/) | Unbounded knapsack (min) |
| [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | Unbounded knapsack (count) |

---

### Pattern 10: Interval DP

**Shape:** `dp[i][j]` = answer for subarray `[i..j]`. Fill by increasing length.

**How to recognize:** "optimal way to split/merge a range", result depends on how you partition an interval.

```python
for length in range(2, n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + cost(i, j))
```

| Problem | What you're splitting |
|---------|---------------------|
| [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | Which balloon to burst last in [i..j] |
| Matrix Chain Multiplication | Where to split the chain |
| Minimum Cost Tree From Leaf Values | How to pair up leaves |

---

### Pattern 11: State Machine DP

**Shape:** `dp[i][state]` = best value at step `i` in a given state.

**How to recognize:** sequential decisions with constraints on transitions (cooldown, transaction limits, modes).

```python
hold = -prices[0]     # holding stock
sold = 0              # just sold (cooldown next)
rest = 0              # not holding, free to buy
for price in prices[1:]:
    new_hold = max(hold, rest - price)
    new_sold = hold + price
    new_rest = max(rest, sold)
    hold, sold, rest = new_hold, new_sold, new_rest
```

| Problem | States |
|---------|--------|
| [Buy/Sell with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | hold, sold, rest |
| Buy/Sell with Transaction Fee | hold, cash |
| Buy/Sell with K Transactions | `dp[k][hold/cash]` |
| Best Time to Buy/Sell Stock III | `dp[transaction#][hold/cash]` |

---

### Pattern 12: DFS + Memoization on Grid/Graph

**Shape:** `memo[i][j]` = answer starting from this position. Top-down only — no natural bottom-up order.

**How to recognize:** "longest path from any cell", DAG-like structure, memoize from each starting point.

```python
@cache
def dfs(i, j):
    best = 1
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if in_bounds(ni, nj) and grid[ni][nj] > grid[i][j]:
            best = max(best, 1 + dfs(ni, nj))
    return best
```

| Problem | What you're memoizing |
|---------|---------------------|
| [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | Longest path starting from (i,j) |
| Number of Paths with Max Score | Paths from (0,0) to (m,n) with max sum |

---

### Pattern Decision Tree

```
Is it a single sequence/array?
├── dp[i] depends on dp[i-1], dp[i-2]?     → Pattern 1 (Fibonacci)
├── Take current or skip it?                 → Pattern 2 (Take/Skip)
├── Min cost to reach a target?              → Pattern 3 (Min/Max to Reach)
├── Count ways to reach target?              → Pattern 4 (Count Ways)
├── Longest subsequence with property?        → Pattern 5 (LIS)
├── Can I reach / is it possible?             → Pattern 6 (Boolean)
└── Items with weight + capacity?             → Pattern 9 (Knapsack)

Are there two strings/sequences?              → Pattern 7 (Two-String)

Is it a 2D grid with limited movement?        → Pattern 8 (Grid)

Am I splitting a range optimally?             → Pattern 10 (Interval)

Am I making sequential decisions with modes?  → Pattern 11 (State Machine)

Is it DFS on a grid/graph with repeated work? → Pattern 12 (DFS + Memo)
```

---

## Part 4: Practice Problems (NeetCode 150)

**Strategy:** start with House Robber — it makes the DP pattern click. Then Coin Change. Once 1D DP feels natural, move to 2D. Backtracking and Greedy are included here because they build on the same recursive thinking.

### Backtracking

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 1 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | Combinations with reuse | Medium |
| 2 | [Permutations](https://leetcode.com/problems/permutations/) | Choice from remaining | Medium |
| 3 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | Include/exclude + skip dups | Medium |
| 4 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Combinations without reuse | Medium |
| 5 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Partitioning | Medium |
| 6 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Choice from mapped set | Medium |
| 7 | [N-Queens](https://leetcode.com/problems/n-queens/) | Constraint placement | Hard |

### 1-D DP

| # | Problem | DP Pattern | Difficulty |
|---|---------|-----------|------------|
| 8 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | P1: Fibonacci | Easy |
| 9 | [House Robber](https://leetcode.com/problems/house-robber/) | P2: Take/Skip | Medium |
| 10 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | P2: Take/Skip (circular) | Medium |
| 11 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Expand from center | Medium |
| 12 | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Expand from center | Medium |
| 13 | [Decode Ways](https://leetcode.com/problems/decode-ways/) | P1: Fibonacci (conditional) | Medium |
| 14 | [Coin Change](https://leetcode.com/problems/coin-change/) | P3: Min to reach / P9: Unbounded knapsack | Medium |
| 15 | [Word Break](https://leetcode.com/problems/word-break/) | P6: Boolean reachability | Medium |
| 16 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | P5: LIS | Medium |
| 17 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | P6: Boolean / P9: 0/1 knapsack | Medium |

### 2-D DP

| # | Problem | DP Pattern | Difficulty |
|---|---------|-----------|------------|
| 18 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | P8: Grid | Medium |
| 19 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | P7: Two-String | Medium |
| 20 | [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | P11: State Machine | Medium |
| 21 | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | P4: Count Ways / P9: Unbounded knapsack | Medium |
| 22 | [Interleaving String](https://leetcode.com/problems/interleaving-string/) | P7: Two-String | Medium |
| 23 | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | P7: Two-String | Hard |
| 24 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | P7: Two-String | Medium |
| 25 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | P10: Interval | Hard |
| 26 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | P7: Two-String (matching) | Hard |

### Greedy

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 27 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Greedy BFS-style reachability | Medium |
| 28 | [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | Greedy filtering | Medium |
| 29 | [Partition Labels](https://leetcode.com/problems/partition-labels/) | Greedy + last occurrence | Medium |
| 30 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | Greedy range tracking | Medium |

---

## Watch

1. **NeetCode — "Dynamic Programming" playlist** — start with 1D DP videos, then 2D DP
2. **NeetCode — "Climbing Stairs" walkthrough** — the simplest DP problem, perfectly explained
3. **Reducible — "5 Simple Steps for Solving Dynamic Programming Problems"** (optional, good framework)

## ML Connection

Memoization IS caching intermediate activations during the forward pass so backprop can reuse them — PyTorch does this automatically. The Viterbi algorithm (used in sequence models like HMMs) is DP. Beam search in language models is a DP-like algorithm. Even gradient checkpointing (a memory optimization in large model training) is a time-space tradeoff that mirrors the choice between top-down memoization and bottom-up tabulation.
