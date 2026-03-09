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
