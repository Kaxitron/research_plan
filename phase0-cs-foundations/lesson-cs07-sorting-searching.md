# Lesson CS-07: Sorting and Searching — Complexity in Action

[← Trees & Graphs](lesson-cs06-trees-graphs.md) | [Back to TOC](../README.md) | [Next: Recursion & DP →](lesson-cs08-recursion-dp.md)

---

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

## 🔨 Practice Problems

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 1 | Implement merge sort from scratch | Divide & conquer | — |
| 2 | Implement binary search from scratch | Binary search | — |
| 3 | Binary Search (LC #704) | Basic binary search | Easy |
| 4 | Search a 2D Matrix (LC #74) | Binary search on grid | Medium |
| 5 | Koko Eating Bananas (LC #875) | Binary search on answer | Medium |
| 6 | Find Minimum in Rotated Sorted Array (LC #153) | Modified binary search | Medium |
| 7 | Search in Rotated Sorted Array (LC #33) | Modified binary search | Medium |
| 8 | Sort Colors (LC #75) | Dutch national flag / 3-way partition | Medium |
| 9 | Merge Intervals (LC #56) | Sort + sweep | Medium |
| 10 | Median of Two Sorted Arrays (LC #4) | Binary search | Hard |

## 🔗 ML Connection

Training a neural network is an optimization problem where you're *searching* for good weights. Hyperparameter tuning often uses binary-search-like strategies (bisection on learning rate). Sorting appears in top-k sampling (select the k highest-probability tokens), beam search (sort candidates by score), and ranking model outputs. The O(n log n) vs O(n²) distinction matters when you're processing millions of tokens.
