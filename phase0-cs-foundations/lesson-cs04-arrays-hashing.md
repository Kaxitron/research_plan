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

**How to recognize:** the input is sorted (or you can sort it), you need to find pairs/triplets satisfying a condition, or you need to do in-place operations on an array without extra space.

**General template:**

```python
# Opposite ends
def two_pointer_opposite(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]  # or some comparison
        if current == target:
            return (left, right)
        elif current < target:
            left += 1       # need larger value
        else:
            right -= 1      # need smaller value

# Fast / slow
def two_pointer_fast_slow(arr):
    slow = 0
    for fast in range(len(arr)):
        if some_condition(arr[fast]):
            arr[slow] = arr[fast]
            slow += 1
    return slow  # new length of processed portion
```

**Two Pointer subtypes:**

| Subtype | Description | Example Problems |
|---------|-------------|-----------------|
| Opposite ends | Left and right converge inward; works on sorted arrays or when comparing extremes | Two Sum II, Container With Most Water, Valid Palindrome, Trapping Rain Water |
| Fast / slow | Slow pointer marks "write position", fast scans ahead; used for in-place dedup and partitioning | Remove Duplicates, Move Zeroes, Remove Element |
| Three pointers | Fix one pointer, two-pointer scan the rest; or three-way partition (Dutch national flag) | 3Sum, Sort Colors (Dutch National Flag) |
| Merge two sorted | One pointer per sorted input, advance the smaller; used for merging and intersection | Merge Sorted Arrays, Intersection of Two Arrays |

### Sliding Window

Maintain a window [left, right] over the array. Expand right, shrink left.
- **Variable-size window:** expand right, shrink left when constraint violated (longest substring, minimum window).
- **Fixed-size window:** window of size k slides across (permutation check).
- **Window + frequency map:** track character/element counts in the window (longest repeating character replacement).
- **Use when:** "find the longest/shortest subarray/substring with property X."

**How to recognize:** the problem asks for a contiguous subarray or substring, and you need to optimize its length (longest/shortest) subject to some constraint. Keywords: "subarray", "substring", "contiguous", "at most k", "window."

**General template:**

```python
# Variable-size sliding window
def sliding_window_variable(arr):
    left = 0
    best = 0
    window_state = {}  # frequency map, sum, etc.
    for right in range(len(arr)):
        # 1. Expand: add arr[right] to window state
        update_state(window_state, arr[right])

        # 2. Shrink: while window is invalid, remove from left
        while not is_valid(window_state):
            remove_from_state(window_state, arr[left])
            left += 1

        # 3. Update answer with current valid window
        best = max(best, right - left + 1)
    return best

# Fixed-size sliding window
def sliding_window_fixed(arr, k):
    window_state = {}
    for right in range(len(arr)):
        update_state(window_state, arr[right])

        if right >= k:
            remove_from_state(window_state, arr[right - k])

        if right >= k - 1:
            check_answer(window_state)
```

**Sliding Window subtypes:**

| Subtype | Description | Example Problems |
|---------|-------------|-----------------|
| Variable-size (maximize) | Expand right always, shrink left when invalid; track longest valid window | Longest Substring Without Repeating Characters, Longest Repeating Character Replacement |
| Variable-size (minimize) | Expand right until valid, then shrink left to find shortest valid window | Minimum Window Substring |
| Fixed-size | Window always has exactly k elements; slide by adding right and removing left | Permutation in String, Find All Anagrams in a String |
| Window + frequency map | Maintain a character/element count inside the window; compare against a target frequency map | Minimum Window Substring, Permutation in String, Longest Repeating Character Replacement |
| Window + distinct count | Track number of distinct elements; shrink when exceeding k distinct | Fruits Into Baskets, Longest Substring with At Most K Distinct Characters |

### Hashing (Frequency Counting & Lookup)

Hash map from element → count, or hash set for existence checks.
- **Existence check:** hash set for O(1) lookup (contains duplicate, longest consecutive sequence).
- **Frequency count:** hash map element → count (valid anagram, top K frequent).
- **Complement lookup:** store value, check if complement exists (two sum).
- **Grouping:** hash map key → list of matching items (group anagrams).
- **Use when:** "have I seen this?", "how many times?", "find complement/pair."

**How to recognize:** you need O(1) lookup or counting. The problem involves finding pairs, checking membership, counting frequencies, or grouping items by some derived key. Any time brute force uses a nested loop to "search for something," a hash map can likely eliminate the inner loop.

**General templates:**

```python
# Complement lookup (Two Sum pattern)
def complement_lookup(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# Frequency counting
from collections import Counter
def frequency_pattern(items):
    freq = Counter(items)
    # Now use freq for comparisons, top-k, etc.

# Grouping by key
from collections import defaultdict
def group_by_key(items):
    groups = defaultdict(list)
    for item in items:
        key = derive_key(item)  # e.g., sorted(item), tuple of char counts
        groups[key].append(item)
    return list(groups.values())
```

**Hashing subtypes:**

| Subtype | Description | Example Problems |
|---------|-------------|-----------------|
| Complement lookup | Store seen values; for each new value, check if its complement (target - value) exists | Two Sum, Two Sum II (also solvable with two pointers), 4Sum II |
| Frequency counting | Count occurrences of each element; compare counts, find top-k, or verify anagrams | Valid Anagram, Top K Frequent Elements, Sort Characters By Frequency |
| Grouping by key | Map a derived key to a list of items sharing that key; the key is often a sorted string or count tuple | Group Anagrams, Isomorphic Strings |
| Existence check (set) | Use a hash set for O(1) "have I seen this?" checks; often replaces an O(n) inner loop | Contains Duplicate, Longest Consecutive Sequence, Happy Number |
| Prefix sum + hash map | Store prefix sums in a map; check if `prefix[j] - target` was seen to find subarrays summing to target | Subarray Sum Equals K, Contiguous Array |

### Prefix Sum / Prefix Products

Precompute cumulative sums for O(1) range queries.
- `prefix[i] = sum(arr[0..i])`, then `sum(arr[l..r]) = prefix[r] - prefix[l-1]`
- **Prefix/suffix products:** left and right product arrays (product of array except self).
- **Use when:** range queries, cumulative operations, "subarray sum equals X."

**How to recognize:** the problem involves range sums, subarray sums, or asks "how many subarrays sum to X." Also useful when you need both a left-to-right and right-to-left accumulation (prefix/suffix products). Keywords: "sum of subarray", "range query", "product except self."

**General templates:**

```python
# Prefix sum — O(n) build, O(1) range query
def prefix_sum(nums):
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    # sum of nums[l..r] inclusive = prefix[r+1] - prefix[l]
    return prefix

# Prefix sum + hash map — count subarrays summing to target
def subarray_sum(nums, target):
    prefix_counts = {0: 1}  # prefix_sum -> count of times seen
    current_sum = 0
    result = 0
    for num in nums:
        current_sum += num
        # If (current_sum - target) was a previous prefix sum,
        # then the subarray between them sums to target
        result += prefix_counts.get(current_sum - target, 0)
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
    return result

# Prefix / suffix products
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]
    return result
```

**Prefix Sum subtypes:**

| Subtype | Description | Example Problems |
|---------|-------------|-----------------|
| Basic prefix sum | Build cumulative sum array; answer range sum queries in O(1) | Range Sum Query, Running Sum of 1D Array |
| Prefix sum + hash map | Store prefix sums in a map; find subarrays summing to a target by checking if `current - target` was seen | Subarray Sum Equals K, Contiguous Array |
| Prefix / suffix products | Build left-product and right-product arrays; multiply them for "product except self" | Product of Array Except Self |
| Prefix max / min | Track running max/min from left and right; useful for water-trapping or boundary problems | Trapping Rain Water (prefix max approach) |

### Monotonic Stack / Deque

A stack (or deque) that maintains increasing or decreasing order.
- **Monotonic stack:** pop elements that break the ordering invariant; useful for "next greater/smaller element" problems.
- **Monotonic deque:** maintain order within a sliding window for O(1) window max/min queries.
- **Use when:** "next greater/smaller element", "maintain a window of max/min."

**How to recognize:** the problem asks "for each element, find the next/previous greater/smaller element" or requires maintaining a max/min over a sliding window in O(n). Also applies to histogram-area problems and stock span calculations.

**General templates:**

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

# Monotonic deque — sliding window maximum in O(n)
from collections import deque
def sliding_window_max(nums, k):
    dq = deque()  # indices, values are decreasing
    result = []
    for i, num in enumerate(nums):
        # Remove elements outside the window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # Maintain decreasing order
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

**Monotonic Stack subtypes:**

| Subtype | Description | Example Problems |
|---------|-------------|-----------------|
| Next greater element | Decreasing stack; pop when current > top to assign next-greater | Next Greater Element I/II, Daily Temperatures |
| Next smaller element | Increasing stack; pop when current < top to assign next-smaller | Stock Span Problem (inverted) |
| Histogram area | For each bar, find nearest shorter bar on left and right; area = height * width | Largest Rectangle in Histogram, Maximal Rectangle |
| Monotonic deque (window max/min) | Deque maintains decreasing order; front is always the window max; popleft when out of range | Sliding Window Maximum |

---

### Pattern Decision Tree

Use this to quickly identify which array/string technique to apply:

```
What does the problem ask for?
│
├── Pairs/triplets satisfying a condition?
│   ├── Input sorted (or can sort)?           → Two Pointers (opposite ends)
│   └── Input unsorted, can't sort?           → Hashing (complement lookup)
│
├── Longest/shortest contiguous subarray/substring?
│   ├── Constraint on window contents?         → Sliding Window (variable-size)
│   └── Window of fixed size k?                → Sliding Window (fixed-size)
│
├── Subarray sum equals / divisible by X?
│   └── Use prefix sum + hash map              → Prefix Sum + Hashing
│
├── Range sum queries on a static array?
│   └── Precompute cumulative sums             → Prefix Sum
│
├── "Have I seen this before?" / frequency / grouping?
│   ├── Existence check                        → Hash Set
│   ├── Count occurrences                      → Hash Map (Counter)
│   └── Group by derived key                   → Hash Map (defaultdict(list))
│
├── Next/previous greater or smaller element?
│   └── Monotonic Stack
│
├── Max/min over a sliding window?
│   └── Monotonic Deque
│
├── In-place removal / partitioning?
│   └── Two Pointers (fast/slow)
│
├── Product of array except self?
│   └── Prefix / Suffix Products
│
└── Not sure?
    ├── Try hashing first — it solves the most problems
    └── If contiguous subarray → sliding window or prefix sum
```

---

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
