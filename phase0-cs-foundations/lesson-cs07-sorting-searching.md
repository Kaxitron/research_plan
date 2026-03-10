# Lesson CS-07: Sorting and Searching — Complexity in Action

[← Trees & Graphs](lesson-cs06-trees-graphs.md) | [Back to TOC](../README.md) | [Next: Recursion & DP →](lesson-cs08-recursion-dp.md)

---

> **Tutor Instructions:** When walking a student through this lesson, don't just explain the concepts — create a series of small, progressive coding tasks that require the student to actively use each concept covered. Explain the relevant material, then immediately give a hands-on task before moving on. Review their solutions and correct mistakes before proceeding. Tasks should escalate in complexity throughout the lesson: start with ~1-minute exercises with immediate feedback, build to ~5-minute tasks, then ~10-minute tasks, and culminate in a ~30-minute capstone that integrates multiple concepts from the lesson. Let the student control the pace. Target ~2.5 hours for guided tutoring (explanations + coding tasks), then direct the student to spend ~1.5 hours doing LeetCode problems on their own to reinforce the concepts.

> **Why this lesson exists:** Sorting and searching are where you internalize Big-O — not as an abstract concept but as something you can *feel* in runtime differences. This lesson also introduces divide-and-conquer, the strategy behind merge sort, quicksort, and binary search. Understanding these deeply prepares you for algorithm analysis throughout the curriculum.

## 🎯 Core Concepts

### Big-O — What It Actually Means

Not "how many seconds" but "how does runtime scale as input grows?"

| Complexity | Name | Example | 1K items | 1M items |
|-----------|------|---------|----------|----------|
| O(1) | Constant | Hash map lookup | instant | instant |
| O(log n) | Logarithmic | Binary search | ~10 ops | ~20 ops |
| O(n) | Linear | Single pass | 1K ops | 1M ops |
| O(n log n) | Linearithmic | Merge sort | ~10K ops | ~20M ops |
| O(n²) | Quadratic | Nested loops | 1M ops | 1T ops 💀 |
| O(2ⁿ) | Exponential | Brute-force subsets | heat death | heat death |

**Rule of thumb:** ~10⁸ operations per second in Python. If n = 10⁵, O(n²) = 10¹⁰ → too slow. O(n log n) = ~10⁶ → fine.

### Sorting Algorithms You Should Know

**Merge Sort** — O(n log n), stable, divide-and-conquer:
```python
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Quick Sort** — O(n log n) average, O(n²) worst, in-place:
- Pick a pivot, partition: elements < pivot go left, > pivot go right. Recurse on each half.
- Faster in practice than merge sort (better cache behavior).

**Counting/Bucket Sort** — O(n) when the range of values is bounded. Not comparison-based.

**Python built-in:** `sorted()` and `.sort()` use Timsort (hybrid merge + insertion sort). O(n log n). Just use it unless the problem requires a specific algorithm.

#### When to Use Which Sorting Algorithm

| Algorithm | Time (avg) | Time (worst) | Space | Stable? | Best when... |
|-----------|-----------|-------------|-------|---------|--------------|
| Merge sort | O(n log n) | O(n log n) | O(n) | Yes | You need stable sort, guaranteed worst-case, or are sorting linked lists |
| Quicksort | O(n log n) | O(n²) | O(log n) | No | In-place is required, cache performance matters, average case is fine |
| Counting sort | O(n + k) | O(n + k) | O(k) | Yes | Values are integers in a bounded range k (e.g., ages, ASCII chars) |
| Timsort (Python built-in) | O(n log n) | O(n log n) | O(n) | Yes | You have no reason to write your own — use this by default |

**How to recognize "sorting is part of the solution":**
- The problem asks about ordering, ranking, or relative position.
- You need to process items "smallest first" or "largest first."
- A brute-force nested loop could be replaced by sorting + a single pass.
- The problem involves intervals, events, or deadlines.

#### The Partition Function (Quickselect / Kth Element)

The partition subroutine from quicksort is a tool in its own right. It places a pivot in its final sorted position and rearranges elements around it — all in O(n) time with O(1) extra space.

**How to recognize:** "Find the kth largest/smallest element," "find the median," or any problem where you need a partial ordering without fully sorting.

```python
import random

def partition(nums, lo, hi):
    """Lomuto partition: returns the final index of the pivot."""
    pivot_idx = random.randint(lo, hi)          # random pivot avoids O(n^2) worst case
    nums[pivot_idx], nums[hi] = nums[hi], nums[pivot_idx]
    pivot = nums[hi]
    store = lo
    for i in range(lo, hi):
        if nums[i] < pivot:
            nums[store], nums[i] = nums[i], nums[store]
            store += 1
    nums[store], nums[hi] = nums[hi], nums[store]
    return store

def quickselect(nums, k):
    """Find the kth smallest element (0-indexed). Average O(n), worst O(n^2)."""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        p = partition(nums, lo, hi)
        if p == k:
            return nums[p]
        elif p < k:
            lo = p + 1
        else:
            hi = p - 1
    return nums[lo]
```

| Variation | Description |
|-----------|-------------|
| Kth largest | Call `quickselect(nums, len(nums) - k)` or negate values |
| Hoare partition | Two pointers from both ends — fewer swaps, but pivot not in final position |
| 3-way partition (Dutch National Flag) | Handles many duplicates; partitions into `< pivot`, `== pivot`, `> pivot` |
| Median of medians | Guarantees O(n) worst case by choosing a good pivot deterministically |

### Binary Search — The O(log n) Workhorse

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1  # not found
```

**The generalized pattern:** binary search works on any monotonic function. "Find the smallest x where f(x) is True" — search over the condition, not just over an array.

#### Binary Search Variants — Detailed Patterns

##### Variant 1: Standard Binary Search (Find Exact Target)

**How to recognize:** Sorted array + "find this value" or "does this value exist?"

This is the basic template shown above. Key details:
- Use `lo <= hi` (both inclusive).
- Return `mid` on match, -1 on miss.
- `lo` and `hi` converge to the same index and then cross — the loop ends when `lo > hi`.

##### Variant 2: Bisect Left / Bisect Right (First or Last Occurrence)

**How to recognize:** "Find the first position where..." or "find the last position where..." or "count occurrences of target in sorted array" (answer = bisect_right - bisect_left).

```python
def bisect_left(arr, target):
    """Index of the first element >= target (insertion point for left side)."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid          # mid could be the answer; keep it in range
    return lo

def bisect_right(arr, target):
    """Index of the first element > target (insertion point for right side)."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

| Use case | Call | Interpretation of result |
|----------|------|--------------------------|
| First occurrence of `target` | `bisect_left(arr, target)` | Check `arr[result] == target` |
| Last occurrence of `target` | `bisect_right(arr, target) - 1` | Check `arr[result] == target` |
| Count of `target` | `bisect_right(arr, target) - bisect_left(arr, target)` | 0 means not found |
| Insert position (maintain sort) | `bisect_left(arr, target)` | Insert before any existing copies |

**Key difference from standard binary search:** the loop condition is `lo < hi` (not `lo <= hi`), and `hi` starts at `len(arr)` (not `len(arr) - 1`). The loop finds a boundary, not a specific element.

##### Variant 3: Binary Search on Answer ("Minimum/Maximum That Satisfies Condition")

**How to recognize:** The problem does not give you a sorted array. Instead, it asks "what is the minimum speed / capacity / time / value such that some condition is met?" The answer space is a range of integers, and there is a monotonic relationship: if `x` works, then `x + 1` also works (or vice versa).

Classic examples: Koko Eating Bananas, Capacity to Ship Packages, Split Array Largest Sum, Magnetic Force Between Two Balls.

```python
def binary_search_on_answer(lo, hi, condition):
    """Find the minimum value in [lo, hi] where condition(value) is True.
    Assumes: condition is monotonic — once True, stays True for all larger values.
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if condition(mid):
            hi = mid          # mid might be the answer
        else:
            lo = mid + 1      # mid is too small
    return lo                 # lo == hi == smallest valid answer

# Example: Koko Eating Bananas
def min_eating_speed(piles, h):
    def can_finish(speed):
        hours = sum((p + speed - 1) // speed for p in piles)  # math.ceil(p/speed)
        return hours <= h

    lo, hi = 1, max(piles)
    return binary_search_on_answer(lo, hi, can_finish)
```

**Template for "maximum value that satisfies condition":** flip the logic — search for the *last* True:
```python
def binary_search_on_answer_max(lo, hi, condition):
    """Find the maximum value in [lo, hi] where condition(value) is True.
    Assumes: condition is True for small values, then becomes False.
    """
    while lo < hi:
        mid = (lo + hi + 1) // 2   # round UP to avoid infinite loop
        if condition(mid):
            lo = mid              # mid might be the answer
        else:
            hi = mid - 1          # mid is too large
    return lo
```

##### Variant 4: Binary Search on Rotated Array

**How to recognize:** "Rotated sorted array" is stated directly, or the array is "almost sorted" with a single breakpoint where values wrap around.

The key insight: after computing `mid`, at least one half (`lo..mid` or `mid..hi`) is guaranteed to be properly sorted. Determine which half is sorted, then decide if the target could be in that sorted half.

```python
def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        if nums[lo] <= nums[mid]:          # LEFT half is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1              # target is in the sorted left half
            else:
                lo = mid + 1              # target is in the other half
        else:                              # RIGHT half is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1              # target is in the sorted right half
            else:
                hi = mid - 1
    return -1

def find_min_rotated(nums):
    """Find the minimum element in a rotated sorted array (no duplicates)."""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1          # min is in the right half
        else:
            hi = mid              # mid could be the min
    return nums[lo]
```

| Scenario | How to handle |
|----------|---------------|
| No duplicates | Standard approach above |
| With duplicates | When `nums[lo] == nums[mid] == nums[hi]`, shrink both ends: `lo += 1; hi -= 1`. Worst case becomes O(n). |
| Find minimum | Compare `nums[mid]` with `nums[hi]` to decide direction |
| Find target | Check which half is sorted, then check if target is in that half |

##### Variant 5: Binary Search on Matrix

**How to recognize:** 2D matrix where rows and/or columns are sorted.

There are two common matrix layouts:

**Layout A — Fully sorted matrix** (each row sorted, first element of next row > last of previous row): Treat it as a 1D sorted array of length `rows * cols`.

```python
def search_matrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    lo, hi = 0, rows * cols - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // cols][mid % cols]   # convert 1D index to 2D
        if val == target:
            return True
        elif val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
```

**Layout B — Row-sorted and column-sorted** (each row sorted left-to-right, each column sorted top-to-bottom, but no global ordering): Use the staircase search starting from top-right (or bottom-left).

```python
def search_matrix_240(matrix, target):
    """O(m + n) staircase search for Search a 2D Matrix II."""
    row, col = 0, len(matrix[0]) - 1     # start at top-right corner
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1          # need bigger, go down
        else:
            col -= 1          # need smaller, go left
    return False
```

| Matrix type | Strategy | Time |
|-------------|----------|------|
| Fully sorted (row-major) | Flatten to 1D, standard binary search | O(log(m*n)) |
| Row-sorted + col-sorted | Staircase from top-right or bottom-left | O(m + n) |
| Only rows sorted | Binary search each row | O(m log n) |

---

### Interval Problems — Detailed Patterns

#### How to Recognize Interval Problems

- The input is a list of `[start, end]` pairs (meetings, ranges, jobs, etc.).
- The problem asks about overlaps, merges, gaps, or scheduling.
- Keywords: "overlapping," "merge," "insert," "minimum rooms," "non-overlapping."

#### Sort by Start vs Sort by End

| Sort order | When to use | Why |
|------------|-------------|-----|
| Sort by start | Merging overlapping intervals, inserting intervals | You process intervals left to right and extend/merge as you go |
| Sort by end | Greedy activity selection / maximizing non-overlapping count | Finishing earliest leaves maximum room for future intervals |
| Sort by start, break ties by end | Sweep-line problems, nested intervals | Consistent ordering when starts are equal |

#### Merge Overlapping Intervals — Template

```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])      # sort by start
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:           # overlaps with previous
            merged[-1][1] = max(merged[-1][1], end)   # extend
        else:
            merged.append([start, end])      # no overlap, new interval
    return merged
```

**Variations:**

| Variation | Change to template |
|-----------|-------------------|
| Count overlapping intervals removed | Track `len(intervals) - len(merged)` |
| Insert a new interval then merge | Append the new interval to the list, then run merge |
| Find gaps between intervals | After merge, gaps are `[merged[i-1][1], merged[i][0]]` where the difference > 0 |

#### Sweep Line / Event-Based Approach

**How to recognize:** "How many intervals are active at any point?" or "maximum concurrent meetings." Instead of thinking about intervals as wholes, decompose each interval into two events: a start event (+1) and an end event (-1).

```python
def max_concurrent(intervals):
    """Maximum number of overlapping intervals at any point."""
    events = []
    for start, end in intervals:
        events.append((start, 1))     # interval begins
        events.append((end, -1))      # interval ends
    events.sort()                     # process in chronological order

    active = 0
    max_active = 0
    for _, delta in events:
        active += delta
        max_active = max(max_active, active)
    return max_active
```

**Tie-breaking note:** If an interval ending at time `t` and another starting at time `t` do not count as overlapping, sort end events before start events by using `(time, -1)` for ends and `(time, 1)` for starts (since -1 < 1).

#### Meeting Rooms Pattern (Min Heap for Active Intervals)

**How to recognize:** "Minimum number of rooms / resources needed" or "assign intervals to the fewest groups."

```python
import heapq

def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])    # sort by start time
    heap = []                               # min-heap of end times of active meetings

    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)             # reuse the room that frees up earliest
        heapq.heappush(heap, end)

    return len(heap)                        # heap size = rooms in use
```

**Why a heap?** You always want to free the room that ends earliest. A min-heap gives you that in O(log n). The final heap size is the peak concurrency.

---

### Greedy — Detailed Patterns

#### How to Recognize Greedy Problems

- There is a natural ordering (sort by deadline, profit, weight, etc.) that lets you make a locally optimal choice.
- The problem has "optimal substructure" and the "greedy choice property": making the best local choice never blocks a better global outcome.
- You never need to revisit or undo a choice (no backtracking).
- Common keywords: "minimum number of," "maximum number of," "earliest," "latest," "most efficient."

#### The Exchange Argument — How to Prove Greedy Is Correct

The exchange argument is the standard way to prove a greedy algorithm works:

1. **Assume** an optimal solution OPT exists that differs from your greedy solution G.
2. **Find** the first point where OPT and G make different choices.
3. **Show** that swapping OPT's choice for G's choice at that point produces a solution that is at least as good as OPT.
4. **Conclude** that G must be optimal (or tied with optimal).

**Practical heuristic:** If you can articulate *why* choosing the locally best option never blocks a globally better outcome, greedy probably works. If you can construct a counterexample where the locally best choice leads to a worse total, you need DP.

#### Greedy vs DP — When Each Applies

| Property | Greedy | DP |
|----------|--------|----|
| Choice revisited? | No — commit and move on | Yes — try all options, pick best |
| Subproblems overlap? | Irrelevant | Yes, memoize them |
| Proof technique | Exchange argument | Bellman equation / induction |
| Typical complexity | O(n log n) or O(n) | O(n * state_size) |
| When to suspect greedy | Sorting + single pass solves it | You keep needing "the best of all previous decisions" |

**Rule of thumb:** Try greedy first (it is simpler). If you find a counterexample where the greedy choice leads to a suboptimal result, switch to DP.

#### Common Greedy Patterns

##### Activity Selection (Maximize Non-overlapping Intervals)

**How to recognize:** "Select the maximum number of non-overlapping intervals."

Sort by end time. Always pick the interval that finishes earliest and is compatible with the last one you picked.

```python
def max_non_overlapping(intervals):
    intervals.sort(key=lambda x: x[1])    # sort by END time
    count = 0
    last_end = float('-inf')
    for start, end in intervals:
        if start >= last_end:              # no overlap with last picked
            count += 1
            last_end = end
    return count
```

**Why sort by end?** Finishing earliest leaves maximum room for remaining intervals. This is the canonical example of the exchange argument: any other choice either picks the same interval or one that ends later, leaving less room.

##### Fractional Knapsack

**How to recognize:** "Maximize value given a weight constraint" and you can take fractions of items (unlike 0/1 knapsack which requires DP).

Sort by value-to-weight ratio (descending). Take items greedily until the capacity runs out.

```python
def fractional_knapsack(items, capacity):
    """items = [(value, weight), ...]. Returns maximum total value."""
    items.sort(key=lambda x: x[0] / x[1], reverse=True)  # best ratio first
    total_value = 0.0
    for value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)   # take a fraction
            break
    return total_value
```

**When greedy fails (and you need DP):** If you *cannot* take fractions (0/1 knapsack), the greedy ratio approach does not work. Example: items = [(60, 10), (100, 20), (120, 30)], capacity = 50. Greedy by ratio picks item 1 + item 2 = 160, but the optimal is item 2 + item 3 = 220.

##### Huffman-Like / Priority Queue Greedy

**How to recognize:** "Combine items repeatedly, minimizing total cost" or "build something optimally by always picking the two smallest/cheapest items."

```python
import heapq

def min_cost_to_connect(sticks):
    """Minimum cost to connect all sticks (each merge costs sum of two sticks)."""
    heapq.heapify(sticks)
    total_cost = 0
    while len(sticks) > 1:
        a = heapq.heappop(sticks)
        b = heapq.heappop(sticks)
        cost = a + b
        total_cost += cost
        heapq.heappush(sticks, cost)
    return total_cost
```

**Why it works:** Merging the two cheapest items first minimizes the total cost because cheaper items get "charged" more times (they appear in more merges). This is the same logic behind Huffman coding.

##### Summary of Common Greedy Strategies

| Pattern | Sort/choose by | Classic problem |
|---------|---------------|-----------------|
| Activity selection | Earliest end time | Non-overlapping Intervals |
| Deadline scheduling | Earliest deadline | Task Scheduler |
| Fractional knapsack | Best value/weight ratio | Fractional Knapsack |
| Huffman merge | Smallest items first (heap) | Connect Sticks / Huffman Coding |
| Jump game | Farthest reachable index | Jump Game |
| Gas station | Cumulative surplus scan | Gas Station |

---

### Pattern Decision Tree

Use this decision tree when you encounter a sorting/searching/interval/greedy problem and are not sure which technique to apply:

```
START: What does the problem give you?
│
├── A sorted array (or something that should be sorted)
│   ├── "Find a specific value" ──────────────> Standard binary search
│   ├── "Find first/last occurrence" ─────────> Bisect left / bisect right
│   ├── Array is rotated ─────────────────────> Rotated binary search (find which half is sorted)
│   └── 2D matrix, rows/cols sorted ─────────> Flatten to 1D binary search OR staircase search
│
├── NOT a sorted array, but asks "minimum X such that condition is met"
│   └── Is the condition monotonic (once true, stays true)?
│       ├── Yes ──────────────────────────────> Binary search on answer
│       └── No ───────────────────────────────> DP or brute force
│
├── A list of intervals / ranges
│   ├── "Merge overlapping" ──────────────────> Sort by start, merge template
│   ├── "Max non-overlapping" ────────────────> Sort by end, greedy activity selection
│   ├── "How many concurrent / min rooms" ───> Sweep line (events) or min-heap
│   └── "Insert interval" ───────────────────> Sort by start, merge template
│
├── An optimization problem ("maximize / minimize ...")
│   ├── Can you prove a greedy choice is always safe?
│   │   ├── Yes ──────────────────────────────> Greedy (sort + single pass)
│   │   └── No / counterexample exists ──────> DP (see lesson CS-08)
│   ├── "Kth largest / smallest" ────────────> Quickselect (partition) or heap
│   └── "Top-k" or "k most frequent" ───────> Heap or bucket sort
│
└── None of the above
    └── Consider: Is there a way to sort the input that simplifies the problem?
        ├── Yes ──────────────────────────────> Sort + two pointers / sliding window / greedy
        └── No ───────────────────────────────> Hash map, brute force, or different pattern
```

---

## 📺 Watch

1. **NeetCode — "Binary Search" playlist**
2. **NeetCode — "Sorting" problems from the roadmap**
3. **Back to Back SWE — "Merge Sort" and "Quick Sort" visualizations** (optional, for visual learners)

## 🔨 Practice Problems (NeetCode 150)

### Implementation Warm-ups

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 1 | Implement merge sort from scratch | Divide & conquer | — |
| 2 | Implement binary search from scratch | Standard binary search | — |
| 3 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Dutch national flag / 3-way partition | Medium |

### Binary Search Variants

**When to use:** sorted data, rotated/shifted sorted data, or any monotonic condition where you can binary search on the answer rather than on an array index.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 4 | [Binary Search](https://leetcode.com/problems/binary-search/) | Standard binary search | Easy |
| 5 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Binary search on matrix | Medium |
| 6 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Binary search on answer | Medium |
| 7 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Modified binary search | Medium |
| 8 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Modified binary search | Medium |
| 9 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Binary search on answer | Medium |
| 10 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Binary search on partition | Hard |

### Intervals

**When to use:** problems involving ranges, overlaps, or scheduling. Almost always start by sorting by start (or end) time.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 11 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Sort + merge | Medium |
| 12 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Sort + merge | Medium |
| 13 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Greedy scheduling | Medium |
| 14 | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | Sort + merge | Easy |
| 15 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Sweep line / heap | Medium |
| 16 | [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | Sweep line / heap | Hard |

### Greedy

**When to use:** locally optimal choice leads to globally optimal. No backtracking needed. Look for single-pass solutions with a running state.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 17 | [Jump Game](https://leetcode.com/problems/jump-game/) | Greedy reachability | Medium |
| 18 | [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | Greedy filtering | Medium |
| 19 | [Gas Station](https://leetcode.com/problems/gas-station/) | Greedy scan | Medium |

### Sorting + Selection

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 20 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Quickselect / partition | Medium |

## 🔗 ML Connection

Training a neural network is an optimization problem where you're *searching* for good weights. Hyperparameter tuning often uses binary-search-like strategies (bisection on learning rate). Sorting appears in top-k sampling (select the k highest-probability tokens), beam search (sort candidates by score), and ranking model outputs. The O(n log n) vs O(n²) distinction matters when you're processing millions of tokens.
