# Lesson CS-04: Arrays, Strings, and Hashing — The Foundation of Everything

[← OOP](lesson-cs03-oop.md) | [Back to TOC](../README.md) | [Next: Linked Lists, Stacks & Queues →](lesson-cs05-linked-lists-stacks-queues.md)

---

> **Tutor Instructions:** When walking a student through this lesson, don't just explain the concepts — create a series of small, progressive coding tasks that require the student to actively use each concept covered. Explain the relevant material, then immediately give a hands-on task before moving on. Review their solutions and correct mistakes before proceeding. Tasks should escalate in complexity throughout the lesson: start with ~1-minute exercises with immediate feedback, build to ~5-minute tasks, then ~10-minute tasks, and culminate in a ~30-minute capstone that integrates multiple concepts from the lesson. Let the student control the pace. Target ~2.5 hours for guided tutoring (explanations + coding tasks), then direct the student to spend ~1.5 hours doing LeetCode problems on their own to reinforce the concepts.

> **Why this lesson exists:** Arrays and hash maps are the two most important data structures in programming. Most LeetCode problems and most real-world code reduce to clever use of these two. This lesson focuses on the patterns — two pointers, sliding window, frequency counting, prefix sums, monotonic stacks — that show up over and over.

## 🎯 Core Concepts

### Arrays — Contiguous Memory

- **Access:** O(1) by index. This is why arrays are fast — the memory address is base + index × size.
- **Insert/delete at end:** O(1) amortized (dynamic arrays double when full).
- **Insert/delete at middle:** O(n) — everything after shifts.
- **Search (unsorted):** O(n). **Search (sorted):** O(log n) with binary search.

### Hash Maps — O(1) Lookup

- **How they work:** hash function maps key → bucket index. Collisions resolved by chaining (linked list at each bucket) or open addressing.
- **Average case:** O(1) for insert, lookup, delete. **Worst case:** O(n) if everything collides.
- Python: `dict`, `defaultdict`, `Counter`. C++: `unordered_map`, `unordered_set`.
- **The pattern:** whenever you need to check "have I seen this before?" or "how many times does X appear?" — reach for a hash map.

### Two Pointers

One pointer at each end, move inward. Or one slow, one fast.
- **Opposite ends:** left and right pointers moving inward (palindrome check, two-sum on sorted array, container problems).
- **Fast/slow:** one pointer advances faster than the other (remove duplicates, move zeroes).
- **Three pointers:** extension for 3-element problems (3Sum, sort colors).
- **Use when:** sorted array, finding pairs, comparing from both ends, in-place operations.

### Sliding Window

Maintain a window [left, right] over the array. Expand right, shrink left.
- **Variable-size window:** expand right, shrink left when constraint violated (longest substring, minimum window).
- **Fixed-size window:** window of size k slides across (permutation check).
- **Window + frequency map:** track character/element counts in the window (longest repeating character replacement).
- **Use when:** "find the longest/shortest subarray/substring with property X."

### Hashing (Frequency Counting & Lookup)

Hash map from element → count, or hash set for existence checks.
- **Existence check:** hash set for O(1) lookup (contains duplicate, longest consecutive sequence).
- **Frequency count:** hash map element → count (valid anagram, top K frequent).
- **Complement lookup:** store value, check if complement exists (two sum).
- **Grouping:** hash map key → list of matching items (group anagrams).
- **Use when:** "have I seen this?", "how many times?", "find complement/pair."

### Prefix Sum / Prefix Products

Precompute cumulative sums for O(1) range queries.
- `prefix[i] = sum(arr[0..i])`, then `sum(arr[l..r]) = prefix[r] - prefix[l-1]`
- **Prefix/suffix products:** left and right product arrays (product of array except self).
- **Use when:** range queries, cumulative operations, "subarray sum equals X."

```python
# Prefix sum — O(n) build, O(1) range query
def prefix_sum(nums):
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    # sum of nums[l..r] inclusive = prefix[r+1] - prefix[l]
    return prefix
```

### Monotonic Stack / Deque

A stack (or deque) that maintains increasing or decreasing order.
- **Monotonic stack:** pop elements that break the ordering invariant; useful for "next greater/smaller element" problems.
- **Monotonic deque:** maintain order within a sliding window for O(1) window max/min queries.
- **Use when:** "next greater/smaller element", "maintain a window of max/min."

```python
# Monotonic stack — next greater element in O(n)
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []  # indices, values are decreasing
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            result[stack.pop()] = num
        stack.append(i)
    return result
```

## 📺 Watch

1. **NeetCode — Arrays & Hashing playlist**
   - https://neetcode.io/roadmap — follow the "Arrays & Hashing" section
2. **NeetCode — "Sliding Window" pattern explanation**
   - Search his channel for the sliding window walkthrough

## 🔨 Practice Problems (NeetCode 150)

Do these in Python first. Redo favorites in C++ for practice.

### Hashing

**When to use:** "have I seen this?", "how many times?", "find complement/pair", anagrams, duplicates, grouping.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 1 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Hash set — existence check | Easy |
| 2 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Frequency count | Easy |
| 3 | [Two Sum](https://leetcode.com/problems/two-sum/) | Hash map — complement lookup | Easy |
| 4 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Hash map — grouping + sorting | Medium |
| 5 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Hash map — frequency count + heap or bucket sort | Medium |
| 6 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | String encoding | Medium |
| 7 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Hash set per row/col/box | Medium |
| 8 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Hash set — existence check | Medium |

### Two Pointers

**When to use:** sorted array, finding pairs, comparing from both ends, in-place operations.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 9 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Opposite ends | Easy |
| 10 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Opposite ends | Medium |
| 11 | [3Sum](https://leetcode.com/problems/3sum/) | Sort + three pointers | Medium |
| 12 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Opposite ends — greedy | Medium |
| 13 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Opposite ends / prefix max | Hard |

### Sliding Window

**When to use:** "find longest/shortest subarray/substring with property X."

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 14 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Variable-size window / one pass | Easy |
| 15 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Variable-size window + hash set | Medium |
| 16 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Variable-size window + frequency map | Medium |
| 17 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Fixed-size window | Medium |
| 18 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Variable-size window + frequency map | Hard |

### Prefix Sum

**When to use:** range queries, cumulative operations, "subarray sum equals X", prefix/suffix products.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 19 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Prefix/suffix products | Medium |

### Monotonic Stack / Deque

**When to use:** "next greater/smaller element", "maintain a window of max/min."

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 20 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Monotonic deque | Hard |

### Other Patterns (Greedy, DP, Bit Manipulation, Math & Geometry)

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 21 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Kadane's algorithm (greedy scan) | Medium |
| 22 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | 1-D DP — tracking min/max | Medium |
| 23 | [Missing Number](https://leetcode.com/problems/missing-number/) | XOR / math (bit manipulation) | Easy |
| 24 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Matrix transpose + reverse | Medium |
| 25 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | In-place marking | Medium |

**Goal:** solve Easy problems without hints. For Medium, try 15 min then watch NeetCode's walkthrough. Hard problems are stretch goals.

### Quick Reference — "What technique do I use?"

| If the problem says... | Think about... |
|------------------------|---------------|
| "sorted array" | Two pointers |
| "longest/shortest subarray" | Sliding window |
| "matching / frequency" | Hash map |
| "subarray sum" | Prefix sum + hash map |
| "next greater/smaller" | Monotonic stack |
| "palindrome" | Two pointers (expand from center or opposite ends) |
| "can you reach / is it possible" | DP (boolean) or greedy |
| "k-th largest/smallest" | Heap |

## 🔗 ML Connection

Tokenizer vocabularies are hash maps (token string → integer ID). Attention patterns are 2D arrays. Batch processing is array slicing. The sliding window pattern appears in convolutional neural networks (a filter sliding across an input). Frequency counting is how you compute token distributions and measure model calibration.
