# Lesson CS-04: Arrays, Strings, and Hashing — The Foundation of Everything

[← OOP](lesson-cs03-oop.md) | [Back to TOC](../README.md) | [Next: Linked Lists, Stacks & Queues →](lesson-cs05-linked-lists-stacks-queues.md)

---

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

## 🔨 Practice Problems (from NeetCode 150)

Do these in Python first. Redo favorites in C++ for practice.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 1 | Contains Duplicate (LC #217) | Hash set | Easy |
| 2 | Valid Anagram (LC #242) | Frequency count | Easy |
| 3 | Two Sum (LC #1) | Hash map | Easy |
| 4 | Group Anagrams (LC #49) | Hash map + sorting | Medium |
| 5 | Top K Frequent Elements (LC #347) | Hash map + heap or bucket sort | Medium |
| 6 | Product of Array Except Self (LC #238) | Prefix/suffix products | Medium |
| 7 | Longest Consecutive Sequence (LC #128) | Hash set | Medium |
| 8 | Best Time to Buy and Sell Stock (LC #121) | Sliding window / one pass | Easy |
| 9 | Longest Substring Without Repeating Characters (LC #3) | Sliding window + hash set | Medium |
| 10 | Minimum Window Substring (LC #76) | Sliding window + frequency count | Hard |

**Goal:** solve 1–3 without hints. For 4–7, try 15 min then watch NeetCode's walkthrough. 8–10 are stretch goals.

## 🔗 ML Connection

Tokenizer vocabularies are hash maps (token string → integer ID). Attention patterns are 2D arrays. Batch processing is array slicing. The sliding window pattern appears in convolutional neural networks (a filter sliding across an input). Frequency counting is how you compute token distributions and measure model calibration.
