# Algorithm & Data Structure Classification — Systematic Audit

[Back to TOC](../README.md)

---

## 1. Arrays, Strings & Hashing (CS-04)

### Two Pointers

**When to use:** sorted array, finding pairs, comparing from both ends, in-place operations.

| Technique | Description | Problems |
|-----------|-------------|----------|
| Opposite ends | Left and right pointers moving inward | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/), [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/), [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) |
| Fast/slow | One pointer advances faster than the other | [Remove Duplicates](https://leetcode.com/problems/remove-duplicates-from-sorted-array/), [Move Zeroes](https://leetcode.com/problems/move-zeroes/) |
| Three pointers | Extension for 3-element problems | [3Sum](https://leetcode.com/problems/3sum/), [Sort Colors](https://leetcode.com/problems/sort-colors/) |

### Sliding Window

**When to use:** "find longest/shortest subarray/substring with property X."

| Technique | Description | Problems |
|-----------|-------------|----------|
| Variable-size window | Expand right, shrink left when constraint violated | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/), [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) |
| Fixed-size window | Window of size k slides across | [Permutation in String](https://leetcode.com/problems/permutation-in-string/), [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) |
| Window + frequency map | Track character/element counts in window | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) |

### Hashing

**When to use:** "have I seen this?", "how many times?", "find complement/pair."

| Technique | Description | Problems |
|-----------|-------------|----------|
| Existence check | Hash set for O(1) lookup | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/), [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) |
| Frequency count | Hash map element → count | [Valid Anagram](https://leetcode.com/problems/valid-anagram/), [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) |
| Complement lookup | Store value, check if complement exists | [Two Sum](https://leetcode.com/problems/two-sum/) |
| Grouping | Hash map key → list of matching items | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) |

### Prefix Sum / Prefix Products

**When to use:** range queries, cumulative operations, "subarray sum equals X."

| Technique | Description | Problems |
|-----------|-------------|----------|
| Prefix sum | `prefix[i] = sum(arr[0..i])` for O(1) range sum | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) |
| Prefix/suffix products | Left and right product arrays | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) |

### Monotonic Stack/Deque

**When to use:** "next greater/smaller element", "maintain a window of max/min."

| Technique | Description | Problems |
|-----------|-------------|----------|
| Monotonic stack | Stack that maintains increasing/decreasing order | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/), [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) |
| Monotonic deque | Deque maintaining order for sliding window | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) |

---

## 2. Linked Lists, Stacks & Queues (CS-05)

### Linked List Patterns

| Technique | Description | Problems |
|-----------|-------------|----------|
| Dummy head | Fake node before real head to simplify edge cases | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/), [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) |
| Fast/slow pointers | Cycle detection, find middle | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/), [Find The Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) |
| In-place reversal | prev/curr/next pointer dance | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/), [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) |
| Merge | Combine sorted lists using pointers | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/), [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) |
| Composite | Find middle + reverse + merge | [Reorder List](https://leetcode.com/problems/reorder-list/) |

### Stack Patterns

| Technique | Description | Problems |
|-----------|-------------|----------|
| Matching/balancing | Push openers, pop on closers | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) |
| Expression evaluation | Operands on stack, apply operators | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) |
| Design | Stack with extra capability | [Min Stack](https://leetcode.com/problems/min-stack/) |

### Heap / Priority Queue Patterns

| Technique | Description | Problems |
|-----------|-------------|----------|
| Top-k | Min-heap of size k for k largest | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/), [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) |
| Two heaps | Max-heap + min-heap for running median | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) |
| Greedy scheduling | Max-heap to always process highest priority | [Task Scheduler](https://leetcode.com/problems/task-scheduler/), [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) |

---

## 3. Trees & Graphs (CS-06)

### Tree Traversal

| Technique | Description | Problems |
|-----------|-------------|----------|
| DFS (in/pre/post) | Recursive traversal, return values up | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/), [Maximum Depth](https://leetcode.com/problems/maximum-depth-of-binary-tree/), [Diameter](https://leetcode.com/problems/diameter-of-binary-tree/) |
| BFS (level-order) | Queue-based, process level by level | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/), [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) |
| DFS + global state | Track a running value, update global answer | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/), [Count Good Nodes](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) |
| BST property | Left < root < right, use bounds | [Validate BST](https://leetcode.com/problems/validate-binary-search-tree/), [Lowest Common Ancestor of BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) |
| Inorder traversal | Gives sorted order on BST | [Kth Smallest in BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) |

### Trie (Prefix Tree)

| Technique | Description | Problems |
|-----------|-------------|----------|
| Basic trie | Insert/search/startsWith | [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) |
| Trie + DFS | Wildcard search or backtracking | [Design Add and Search Words](https://leetcode.com/problems/design-add-and-search-words-data-structure/), [Word Search II](https://leetcode.com/problems/word-search-ii/) |

### Graph Traversal

| Technique | Description | Problems |
|-----------|-------------|----------|
| DFS on grid | Flood fill, connected components | [Number of Islands](https://leetcode.com/problems/number-of-islands/), [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) |
| BFS on grid | Shortest path, multi-source spread | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) |
| Multi-source BFS/DFS | Start from multiple points simultaneously | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/), [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) |
| Topological sort | Ordering with dependencies, cycle detection | [Course Schedule](https://leetcode.com/problems/course-schedule/), [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) |
| Clone/copy | BFS/DFS + hash map old→new | [Clone Graph](https://leetcode.com/problems/clone-graph/) |

### Shortest Path Algorithms

| Technique | Description | Problems |
|-----------|-------------|----------|
| BFS (unweighted) | Queue, first visit = shortest | [Word Ladder](https://leetcode.com/problems/word-ladder/) |
| Dijkstra's | Priority queue, weighted non-negative edges | [Network Delay Time](https://leetcode.com/problems/network-delay-time/), [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) |
| Bellman-Ford | Handles negative weights, k-stop constraints | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) |

### Minimum Spanning Tree

| Technique | Description | Problems |
|-----------|-------------|----------|
| Prim's / Kruskal's | Connect all nodes with minimum total edge weight | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) |

### Union-Find (Disjoint Set)

| Technique | Description | Problems |
|-----------|-------------|----------|
| Union-Find | Track connected components, detect cycles | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) |

---

## 4. Sorting & Searching (CS-07)

### Binary Search

**When to use:** sorted data, or any monotonic condition where you can binary search on the answer.

| Technique | Description | Problems |
|-----------|-------------|----------|
| Standard binary search | Find target in sorted array | [Binary Search](https://leetcode.com/problems/binary-search/) |
| Binary search on answer | Search over possible answers, check feasibility | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) |
| Modified binary search | Handle rotated/shifted arrays | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/), [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) |
| Binary search on matrix | Treat 2D as 1D, or row+col search | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) |
| Binary search on partition | Find optimal split point | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) |

### Intervals

| Technique | Description | Problems |
|-----------|-------------|----------|
| Sort + merge | Sort by start, merge overlaps | [Merge Intervals](https://leetcode.com/problems/merge-intervals/), [Insert Interval](https://leetcode.com/problems/insert-interval/) |
| Greedy scheduling | Minimize removals / maximize non-overlapping | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) |
| Sweep line / heap | Track active intervals | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) |

### Greedy

**When to use:** locally optimal choice leads to globally optimal. No backtracking needed.

| Technique | Description | Problems |
|-----------|-------------|----------|
| Greedy reachability | Track farthest reachable position | [Jump Game](https://leetcode.com/problems/jump-game/), [Jump Game II](https://leetcode.com/problems/jump-game-ii/) |
| Greedy scan | Single pass with running state | [Gas Station](https://leetcode.com/problems/gas-station/), [Maximum Subarray (Kadane's)](https://leetcode.com/problems/maximum-subarray/) |
| Greedy filtering | Filter candidates by condition | [Merge Triplets](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) |
| Greedy partitioning | Use last occurrence to determine cuts | [Partition Labels](https://leetcode.com/problems/partition-labels/) |

---

## 5. Backtracking (CS-08)

**The universal pattern:**
```
def backtrack(state):
    if goal_reached: record solution; return
    for each choice:
        if valid:
            make choice
            backtrack(next state)
            undo choice      ← this is what makes it backtracking
```

**When to use:** "generate all...", "find all...", constraint satisfaction, combinatorial search.

### Classification by Structure

| Type | Question at each step | Problems |
|------|----------------------|----------|
| Subsets | Include this element or skip it? | [Subsets](https://leetcode.com/problems/subsets/), [Subsets II](https://leetcode.com/problems/subsets-ii/) |
| Permutations | Which unused element goes next? | [Permutations](https://leetcode.com/problems/permutations/) |
| Combinations | Which element from remaining goes next? (order doesn't matter) | [Combination Sum](https://leetcode.com/problems/combination-sum/), [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) |
| Partitioning | Where do I cut? | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) |
| Grid search | Which direction do I go? | [Word Search](https://leetcode.com/problems/word-search/) |
| Constraint placement | Where do I place the next piece? | [N-Queens](https://leetcode.com/problems/n-queens/), [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) |
| Bucket assignment | Which bucket does this item go in? | [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) |

### Key Pruning Techniques

| Technique | Description |
|-----------|-------------|
| Skip duplicates | Sort first, skip `nums[i] == nums[i-1]` when both unused |
| Constraint check | Don't recurse if current state already violates constraints |
| Sort descending | Fail faster on large elements |
| Identical bucket pruning | If an empty bucket failed, don't try other empty buckets |
| Early termination | Return immediately when solution found (if only need one) |

### Backtracking vs DP Decision

| Backtracking | DP |
|-------------|-----|
| Find ALL solutions | Find ONE optimal value (min/max/count) |
| Path/arrangement matters | Only result matters |
| No overlapping subproblems (or state too complex to cache) | Overlapping subproblems |
| Exponential is acceptable (small n) | Polynomial solution exists |

---

## 6. Dynamic Programming (CS-08)

**The two requirements:**
1. **Overlapping subproblems** — same sub-computation repeated
2. **Optimal substructure** — optimal solution built from optimal sub-solutions

**Decision framework:**
1. What is `dp[i]` (or `dp[i][j]`)? ← most important step
2. What's the recurrence?
3. What are the base cases?
4. What order do I fill the table?
5. Can I optimize space?

### 1-D DP

**State:** `dp[i]` = answer considering first `i` elements (or up to position `i`).

| Pattern | Recurrence Shape | Problems |
|---------|-----------------|----------|
| Fibonacci variant | `dp[i] = dp[i-1] + dp[i-2]` | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/), [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) |
| Take/skip | `dp[i] = max(dp[i-1], dp[i-2] + val[i])` | [House Robber](https://leetcode.com/problems/house-robber/), [House Robber II](https://leetcode.com/problems/house-robber-ii/) |
| Best ending here | `dp[i] = max(nums[i], dp[i-1] + nums[i])` | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) |
| Min/max to reach | `dp[i] = min(dp[i-c] + 1) for c in coins` | [Coin Change](https://leetcode.com/problems/coin-change/) |
| Longest increasing | `dp[i] = max(dp[j] + 1) for j < i where nums[j] < nums[i]` | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) |
| Can partition? | `dp[s] = dp[s] or dp[s - num]` (boolean) | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) |
| String decomposition | `dp[i] = any(dp[j] and s[j:i] in dict)` | [Word Break](https://leetcode.com/problems/word-break/) |
| Decode/count | `dp[i] = dp[i-1] + dp[i-2]` (conditional) | [Decode Ways](https://leetcode.com/problems/decode-ways/) |
| Expand from center | Not table-based; expand outward from each position | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/), [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) |

### 2-D DP

**State:** `dp[i][j]` = answer for subproblem defined by two parameters (two strings, grid position, interval).

| Pattern | State Meaning | Problems |
|---------|--------------|----------|
| Grid paths | `dp[i][j]` = ways/cost to reach cell (i,j) | [Unique Paths](https://leetcode.com/problems/unique-paths/) |
| Two-string comparison | `dp[i][j]` = answer for `s1[:i]` and `s2[:j]` | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/), [Edit Distance](https://leetcode.com/problems/edit-distance/) |
| String matching | `dp[i][j]` = does `s[:i]` match `p[:j]`? | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) |
| String interleaving | `dp[i][j]` = can we form target from `s1[:i]` + `s2[:j]`? | [Interleaving String](https://leetcode.com/problems/interleaving-string/) |
| Subsequence counting | `dp[i][j]` = # ways `t[:j]` appears in `s[:i]` | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) |
| Interval DP | `dp[i][j]` = answer for subarray/substring `[i..j]` | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) |
| Knapsack 2D | `dp[i][j]` = answer using first `i` items with capacity `j` | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) |
| State machine | `dp[i][state]` = best value at day `i` in given state | [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) |
| DFS + memo on grid | `memo[i][j]` = answer starting from cell (i,j) | [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) |
| Decision tree with state | `dp[i][first][last]` = min length at index i | [Decremental String Concatenation](https://leetcode.com/problems/decremental-string-concatenation/) |

### Knapsack Variants

| Type | Description | Problems |
|------|-------------|----------|
| 0/1 Knapsack | Each item used at most once | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/), [Target Sum](https://leetcode.com/problems/target-sum/) |
| Unbounded Knapsack | Items can be reused | [Coin Change](https://leetcode.com/problems/coin-change/), [Coin Change II](https://leetcode.com/problems/coin-change-ii/) |

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

---

## 7. Quick Reference: "What technique do I use?"

| If the problem says... | Think about... |
|------------------------|---------------|
| "sorted array" | Binary search, two pointers |
| "longest/shortest subarray" | Sliding window |
| "all permutations/combinations/subsets" | Backtracking |
| "minimum/maximum cost/ways" | DP |
| "can you reach / is it possible" | DP (boolean), BFS, or greedy |
| "connected components" | DFS/BFS, Union-Find |
| "shortest path" | BFS (unweighted), Dijkstra (weighted) |
| "dependencies / ordering" | Topological sort |
| "next greater/smaller" | Monotonic stack |
| "k-th largest/smallest" | Heap |
| "matching / frequency" | Hash map |
| "palindrome" | Two pointers, expand from center, or DP |
| "subarray sum" | Prefix sum + hash map |
| "tree" | DFS recursion (usually), BFS for level-order |
| "interval overlap" | Sort + sweep/merge |

---

## 8. NeetCode Roadmap Mapping

All problems above are from or aligned with the [NeetCode 150](https://neetcode.io/roadmap). The roadmap categories map to lessons as follows:

| NeetCode Category | Lesson |
|-------------------|--------|
| Arrays & Hashing | CS-04 |
| Two Pointers | CS-04 |
| Sliding Window | CS-04 |
| Stack | CS-05 |
| Linked List | CS-05 |
| Binary Search | CS-07 |
| Trees | CS-06 |
| Tries | CS-06 |
| Backtracking | CS-08 |
| Graphs | CS-06 |
| Advanced Graphs | CS-06 |
| 1-D DP | CS-08 |
| 2-D DP | CS-08 |
| Greedy | CS-07 / CS-08 |
| Intervals | CS-07 |
| Heap / Priority Queue | CS-05 |
| Math & Geometry | CS-04 |
| Bit Manipulation | CS-04 |
