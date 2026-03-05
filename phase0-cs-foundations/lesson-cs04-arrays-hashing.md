# Lesson CS-04: Arrays, Strings, and Hashing — The Foundation of Everything

[← OOP](lesson-cs03-oop.md) | [Back to TOC](../README.md) | [Next: Linked Lists, Stacks & Queues →](lesson-cs05-linked-lists-stacks-queues.md)

---

> **Tutor Instructions:** When walking a student through this lesson, don't just explain the concepts — create a series of small, progressive coding tasks that require the student to actively use each concept covered. Explain the relevant material, then immediately give a hands-on task before moving on. Review their solutions and correct mistakes before proceeding. Tasks should escalate in complexity throughout the lesson: start with ~1-minute exercises with immediate feedback, build to ~5-minute tasks, then ~10-minute tasks, and culminate in a ~30-minute capstone that integrates multiple concepts from the lesson. Let the student control the pace. Target ~2.5 hours for guided tutoring (explanations + coding tasks), then direct the student to spend ~1.5 hours doing LeetCode problems on their own to reinforce the concepts.

> **Why this lesson exists:** Arrays and hash maps are the two most important data structures in programming. Most LeetCode problems and most real-world code reduce to clever use of these two. This lesson focuses on the patterns — two pointers, sliding window, frequency counting — that show up over and over.

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

### Key Patterns

**Two Pointers:** one pointer at each end, move inward. Or one slow, one fast.
- Use when: sorted array, finding pairs, removing duplicates in-place.

**Sliding Window:** maintain a window [left, right] over the array. Expand right, shrink left.
- Use when: "find the longest/shortest subarray with property X."

**Frequency Counting:** hash map from element → count.
- Use when: anagrams, duplicates, "most common," matching.

**Prefix Sum:** precompute cumulative sums for O(1) range queries.
- `prefix[i] = sum(arr[0..i])`, then `sum(arr[l..r]) = prefix[r] - prefix[l-1]`

## 📺 Watch

1. **NeetCode — Arrays & Hashing playlist**
   - https://neetcode.io/roadmap — follow the "Arrays & Hashing" section
2. **NeetCode — "Sliding Window" pattern explanation**
   - Search his channel for the sliding window walkthrough

## 🔨 Practice Problems (NeetCode 150)

Do these in Python first. Redo favorites in C++ for practice.

| # | Problem | Category | Pattern | Difficulty |
|---|---------|----------|---------|------------|
| 1 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Arrays & Hashing | Hash set | Easy |
| 2 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Arrays & Hashing | Frequency count | Easy |
| 3 | [Two Sum](https://leetcode.com/problems/two-sum/) | Arrays & Hashing | Hash map | Easy |
| 4 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Arrays & Hashing | Hash map + sorting | Medium |
| 5 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Arrays & Hashing | Hash map + heap or bucket sort | Medium |
| 6 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | Arrays & Hashing | String encoding | Medium |
| 7 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Arrays & Hashing | Prefix/suffix products | Medium |
| 8 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Arrays & Hashing | Hash set per row/col/box | Medium |
| 9 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Arrays & Hashing | Hash set | Medium |
| 10 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Two Pointers | Two pointers inward | Easy |
| 11 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two Pointers | Two pointers inward | Medium |
| 12 | [3Sum](https://leetcode.com/problems/3sum/) | Two Pointers | Sort + two pointers | Medium |
| 13 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Two Pointers | Two pointers greedy | Medium |
| 14 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Two Pointers | Two pointers / prefix max | Hard |
| 15 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Sliding Window | Sliding window / one pass | Easy |
| 16 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Sliding Window | Sliding window + hash set | Medium |
| 17 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Sliding Window | Sliding window + frequency count | Medium |
| 18 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Sliding Window | Fixed-size sliding window | Medium |
| 19 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Sliding Window | Sliding window + frequency count | Hard |
| 20 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Sliding Window | Monotonic deque | Hard |
| 21 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Greedy | Kadane's algorithm | Medium |
| 22 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | 1-D DP | Array scan tracking min/max | Medium |
| 23 | [Missing Number](https://leetcode.com/problems/missing-number/) | Bit Manipulation | XOR / math | Easy |
| 24 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Math & Geometry | Matrix transpose + reverse | Medium |
| 25 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Math & Geometry | In-place marking | Medium |

**Goal:** solve Easy problems without hints. For Medium, try 15 min then watch NeetCode's walkthrough. Hard problems are stretch goals.

## 🔗 ML Connection

Tokenizer vocabularies are hash maps (token string → integer ID). Attention patterns are 2D arrays. Batch processing is array slicing. The sliding window pattern appears in convolutional neural networks (a filter sliding across an input). Frequency counting is how you compute token distributions and measure model calibration.
