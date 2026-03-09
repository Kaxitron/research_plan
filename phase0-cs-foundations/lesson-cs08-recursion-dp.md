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

**DP requires BOTH conditions:**

1. **Overlapping subproblems** — the same sub-computation is repeated multiple times
2. **Optimal substructure** — the optimal solution is built from optimal sub-solutions

**What if you only have one?**
- **Only substructure, no overlap** → **divide and conquer** (e.g., merge sort). Subproblems don't repeat, so there's nothing to cache.
- **Only overlap, no substructure** → DP doesn't apply. E.g., longest simple path in a graph — you revisit nodes, but the best path through node A depends on which nodes you've already visited, so it can't decompose cleanly.
- **Neither** → brute force / backtracking.

**The quick test:** Can I define the answer in terms of smaller versions of the same problem? (→ substructure). Do those smaller versions get recomputed? (→ overlap). Both yes → DP.

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

### Recursion Patterns in the Wild

#### Linear Recursion
One recursive call. Reduces by one element each time. Easy to convert to iteration.
```python
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)
```
**Seen in:** linked list traversal, array processing, tail-recursive algorithms.

#### Binary/Tree Recursion
Two (or more) recursive calls. Creates a tree of calls. Often leads to DP.
```python
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)    # two branches
```
**Seen in:** fibonacci, tree traversals, divide and conquer, mergesort.

#### Divide and Conquer
Split into independent halves, solve each, combine results. NOT DP — subproblems don't overlap.
```python
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])       # independent halves
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
**Seen in:** permutations, combinations, constraint satisfaction (N-Queens, Sudoku), partition problems.

**Backtracking subtypes:**

| Subtype | Question at each step | Example |
|---------|----------------------|---------|
| Include/exclude | Do I take this element or skip it? | Subsets, Partition Equal Subset Sum |
| Choice from remaining | Which unused element goes here? | Permutations |
| Combinations with reuse | Which element from index onward? (can repeat) | Combination Sum |
| Combinations without reuse | Which element from index onward? (no repeat, skip dups) | Combination Sum II, Subsets II |
| Partitioning | Where do I cut? | Palindrome Partitioning |
| Grid exploration | Which direction? (with visited tracking) | Word Search |
| Constraint placement | Where does this piece go? | N-Queens, Sudoku Solver |
| Bucket assignment | Which group does this item join? | Partition to K Equal Sum Subsets |

#### Generate and Test
Generate candidates recursively, test validity. Simpler than backtracking (no pruning during generation).
```python
def generate_subsets(nums, i=0, current=[]):
    if i == len(nums):
        if is_valid(current): results.append(current[:])
        return
    generate_subsets(nums, i+1, current)             # skip
    generate_subsets(nums, i+1, current + [nums[i]])  # include
```
**Seen in:** brute-force subset/permutation generation. Usually upgraded to backtracking with pruning.

---

### DP Pattern Catalog

#### Pattern 1: Fibonacci / Linear Recurrence
**Shape:** `dp[i]` depends on `dp[i-1]`, `dp[i-2]`, (maybe `dp[i-3]`...).

**How to recognize:** each step has a fixed small number of previous states to consider. Often the problem says "ways to reach step i" or "cost to reach step i."

```python
# Template
dp[0] = base
dp[1] = base
for i in range(2, n+1):
    dp[i] = f(dp[i-1], dp[i-2])
```

**Space optimize:** two variables.

| Problem | Recurrence |
|---------|-----------|
| Climbing Stairs | `dp[i] = dp[i-1] + dp[i-2]` |
| Min Cost Climbing Stairs | `dp[i] = cost[i] + min(dp[i-1], dp[i-2])` |
| Decode Ways | `dp[i] = dp[i-1] (if valid single) + dp[i-2] (if valid pair)` |
| Tribonacci | `dp[i] = dp[i-1] + dp[i-2] + dp[i-3]` |

---

#### Pattern 2: Take or Skip
**Shape:** `dp[i] = max(take this item, skip this item)`.

**How to recognize:** items in a sequence, taking one affects which neighbors you can take. "Maximum/minimum value without taking adjacent elements."

```python
# Template
dp[0] = val[0]
dp[1] = max(val[0], val[1])
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + val[i])
```

**Space optimize:** two variables.

| Problem | Recurrence |
|---------|-----------|
| House Robber | `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` |
| House Robber II (circular) | Run House Robber twice: `nums[0:n-1]` and `nums[1:n]` |
| Delete and Earn | Sort + frequency count, then House Robber on values |

---

#### Pattern 3: Min/Max Cost to Reach Target
**Shape:** `dp[target]` = min/max cost. Try all ways to reach `target` from smaller values.

**How to recognize:** "minimum number of X to make Y", "fewest coins", "minimum steps."

```python
# Template
dp = [float('inf')] * (target + 1)
dp[0] = 0
for i in range(1, target + 1):
    for option in options:
        if i - option >= 0:
            dp[i] = min(dp[i], dp[i - option] + 1)
```

| Problem | Recurrence |
|---------|-----------|
| Coin Change | `dp[amount] = min(dp[amount - coin] + 1)` for each coin |
| Perfect Squares | `dp[n] = min(dp[n - k*k] + 1)` for each perfect square k*k ≤ n |

---

#### Pattern 4: Count Ways to Reach Target
**Shape:** same as Pattern 3 but summing instead of min/max.

**How to recognize:** "how many ways", "number of combinations that sum to."

```python
# Template
dp = [0] * (target + 1)
dp[0] = 1
for i in range(1, target + 1):
    for option in options:
        if i - option >= 0:
            dp[i] += dp[i - option]
```

| Problem | Recurrence |
|---------|-----------|
| Climbing Stairs | `dp[i] += dp[i-1] + dp[i-2]` |
| Coin Change II | `dp[amount] += dp[amount - coin]` (loop coins outer to avoid order-dependence) |
| Combination Sum IV | `dp[target] += dp[target - num]` for each num |

**Subtle distinction — order matters:**
- Coins outer loop, amount inner → combinations (unordered): `{1,2}` and `{2,1}` are same
- Amount outer loop, coins inner → permutations (ordered): `{1,2}` and `{2,1}` are different

---

#### Pattern 5: Longest Increasing Subsequence (LIS)
**Shape:** `dp[i]` = best answer ending at index `i`. Compare against all `j < i`.

**How to recognize:** "longest subsequence with property X", "maximum length chain."

```python
# Template: O(n^2)
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)
return max(dp)
```

Note: there's an O(n log n) solution using binary search + patience sorting.

| Problem | Variation |
|---------|----------|
| Longest Increasing Subsequence | Standard LIS |
| Number of Longest Increasing Subsequence | Track count alongside length |
| Russian Doll Envelopes | Sort + LIS on second dimension |

---

#### Pattern 6: Boolean/Reachability DP
**Shape:** `dp[i]` = True/False, can we reach state `i`?

**How to recognize:** "can you partition", "is it possible", "can you make."

```python
# Template (0/1 knapsack style)
dp = [False] * (target + 1)
dp[0] = True
for num in nums:
    for s in range(target, num - 1, -1):   # reverse to avoid reuse
        dp[s] = dp[s] or dp[s - num]
```

| Problem | Variation |
|---------|----------|
| Partition Equal Subset Sum | `dp[sum/2]` reachable? |
| Word Break | `dp[i] = any(dp[j] and s[j:i] in dict)` |
| Target Sum | `dp[offset + target]` after +/- decisions |

---

#### Pattern 7: Two-String DP
**Shape:** `dp[i][j]` = answer for `s1[:i]` vs `s2[:j]`. Fill table left-to-right, top-to-bottom.

**How to recognize:** two sequences/strings being compared, matched, or transformed.

```python
# Template (LCS)
dp = [[0] * (n+1) for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1       # chars match
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # skip one
```

| Problem | State meaning | Match case | Mismatch case |
|---------|--------------|------------|---------------|
| Longest Common Subsequence | length of LCS | `dp[i-1][j-1] + 1` | `max(dp[i-1][j], dp[i][j-1])` |
| Edit Distance | min operations | `dp[i-1][j-1]` (no op) | `1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])` |
| Distinct Subsequences | # ways t appears in s | `dp[i-1][j-1] + dp[i-1][j]` | `dp[i-1][j]` |
| Interleaving String | can interleave? | `dp[i-1][j] or dp[i][j-1]` | depends on which string matches |
| Regular Expression Matching | does s match p? | `dp[i-1][j-1]` | handle `*` with `dp[i][j-2]` or `dp[i-1][j]` |

**Space optimize:** single row (since each row only depends on the previous row).

---

#### Pattern 8: Grid DP
**Shape:** `dp[i][j]` = answer at cell (i,j). Fill top-to-bottom, left-to-right.

**How to recognize:** 2D grid, can only move right/down (or limited directions), count paths or min cost.

```python
# Template
dp = [[0] * cols for _ in range(rows)]
dp[0][0] = base
for i in range(rows):
    for j in range(cols):
        if i > 0: dp[i][j] += dp[i-1][j]   # from above
        if j > 0: dp[i][j] += dp[i][j-1]   # from left
```

| Problem | What dp[i][j] stores |
|---------|---------------------|
| Unique Paths | # ways to reach (i,j) |
| Minimum Path Sum | min cost to reach (i,j) |
| Dungeon Game | min HP needed at (i,j) — fill bottom-right to top-left |

---

#### Pattern 9: Knapsack
**Shape:** `dp[i][w]` = best value using first `i` items with weight limit `w`.

**How to recognize:** items with weight/cost and value, capacity constraint, maximize/count.

**0/1 Knapsack** (each item once):
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

The **direction of the inner loop** is the key difference: reverse for 0/1 (prevent reuse), forward for unbounded (allow reuse).

| Problem | Type |
|---------|------|
| Partition Equal Subset Sum | 0/1 knapsack (boolean) |
| Target Sum | 0/1 knapsack (count) |
| Coin Change | Unbounded knapsack (min) |
| Coin Change II | Unbounded knapsack (count) |

---

#### Pattern 10: Interval DP
**Shape:** `dp[i][j]` = answer for subarray/substring `[i..j]`. Fill by increasing length.

**How to recognize:** "optimal way to split/merge a range", result depends on how you partition an interval.

```python
# Template
for length in range(2, n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        for k in range(i, j):    # try every split point
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + cost(i, j))
```

| Problem | What you're splitting |
|---------|---------------------|
| Burst Balloons | Which balloon to burst last in range [i..j] |
| Matrix Chain Multiplication | Where to split the chain of matrices |
| Minimum Cost Tree From Leaf Values | How to pair up leaves |

---

#### Pattern 11: State Machine DP
**Shape:** `dp[i][state]` = best value at step `i` in a given state. States are a small enum (holding, not holding, cooldown, etc).

**How to recognize:** you're making sequential decisions with constraints on transitions (cooldown, limited transactions, modes).

```python
# Template (buy/sell with cooldown)
hold = -prices[0]     # holding stock
sold = 0              # just sold (cooldown next)
rest = 0              # not holding, free to buy
for price in prices[1:]:
    new_hold = max(hold, rest - price)    # buy or keep holding
    new_sold = hold + price               # sell
    new_rest = max(rest, sold)            # do nothing or come off cooldown
    hold, sold, rest = new_hold, new_sold, new_rest
```

| Problem | States |
|---------|--------|
| Buy/Sell Stock with Cooldown | hold, sold, rest |
| Buy/Sell Stock with Transaction Fee | hold, cash |
| Buy/Sell Stock with K Transactions | `dp[k][hold/cash]` |
| Best Time to Buy/Sell Stock III | `dp[transaction#][hold/cash]` |

---

#### Pattern 12: DFS + Memoization on Grid/Graph
**Shape:** `memo[i][j]` (or `memo[node]`) = answer starting from this position. Top-down only — no natural bottom-up order.

**How to recognize:** "longest path from any cell", "number of paths with constraints", DAG-like structure where you memoize from each starting point.

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
| Longest Increasing Path in a Matrix | Longest path starting from (i,j) |
| Number of Paths with Max Score | Paths from (0,0) to (m,n) with max sum |

---

### How to Identify Which DP Pattern You're Facing

```
Is it a single sequence/array?
├── Does dp[i] depend on dp[i-1], dp[i-2]?  →  Pattern 1 (Fibonacci)
├── Take current or skip it?                  →  Pattern 2 (Take/Skip)
├── Min cost to reach a target?               →  Pattern 3 (Min/Max to Reach)
├── Count ways to reach target?               →  Pattern 4 (Count Ways)
├── Longest subsequence with property?         →  Pattern 5 (LIS)
├── Can I reach / is it possible?              →  Pattern 6 (Boolean)
└── Items with weight + capacity?              →  Pattern 9 (Knapsack)

Are there two strings/sequences?               →  Pattern 7 (Two-String)

Is it a 2D grid with limited movement?         →  Pattern 8 (Grid)

Am I splitting a range optimally?              →  Pattern 10 (Interval)

Am I making sequential decisions with modes?   →  Pattern 11 (State Machine)

Is it DFS on a grid/graph with repeated visits? → Pattern 12 (DFS + Memo)
```

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
