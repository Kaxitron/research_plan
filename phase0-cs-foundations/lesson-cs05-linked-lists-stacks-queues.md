# Lesson CS-05: Linked Lists, Stacks, and Queues

[← Arrays & Hashing](lesson-cs04-arrays-hashing.md) | [Back to TOC](../README.md) | [Next: Trees & Graphs →](lesson-cs06-trees-graphs.md)

---

> **Tutor Instructions:** When walking a student through this lesson, don't just explain the concepts — create a series of small, progressive coding tasks that require the student to actively use each concept covered. Explain the relevant material, then immediately give a hands-on task before moving on. Review their solutions and correct mistakes before proceeding. Tasks should escalate in complexity throughout the lesson: start with ~1-minute exercises with immediate feedback, build to ~5-minute tasks, then ~10-minute tasks, and culminate in a ~30-minute capstone that integrates multiple concepts from the lesson. Let the student control the pace. Target ~2.5 hours for guided tutoring (explanations + coding tasks), then direct the student to spend ~1.5 hours doing LeetCode problems on their own to reinforce the concepts.

> **Why this lesson exists:** These data structures teach you to think about *pointers* — one thing referencing another. Linked lists are the simplest version of this idea, and it scales up to trees, graphs, and ultimately computation graphs (the backbone of backpropagation). Building these from scratch also forces you to handle edge cases carefully.

## 🎯 Core Concepts

### Linked Lists

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

- **Access:** O(n) — must traverse from head. No random access.
- **Insert/delete at known position:** O(1) — just rewire pointers.
- **When to use:** when you need frequent insertion/deletion and don't need random access.
- **Dummy head trick:** create a `dummy = ListNode(0)` before the real head. Simplifies edge cases where the head itself changes.

**Key patterns:**
- **Two pointers (slow/fast):** slow moves 1 step, fast moves 2. When fast hits the end, slow is at the middle. If there's a cycle, they'll meet.
- **Reverse in-place:** maintain `prev`, `curr`, `next`. Rewire `curr.next = prev` and advance.

### Stacks — Last In, First Out (LIFO)

- **Operations:** `push` (add to top), `pop` (remove from top), `peek` (look at top). All O(1).
- **Implementation:** just use a Python list or C++ `stack<T>`.
- **When to use:** matching parentheses, undo operations, DFS, expression evaluation, monotonic stack problems.

### Queues — First In, First Out (FIFO)

- **Operations:** `enqueue` (add to back), `dequeue` (remove from front). All O(1) with proper implementation.
- **Implementation:** Python `collections.deque` (NOT a list — `list.pop(0)` is O(n)). C++ `queue<T>`.
- **When to use:** BFS, scheduling, buffering, level-order traversal.

### Deque — Double-Ended Queue

- Insert/remove from both ends in O(1). Python `collections.deque`. C++ `deque<T>`.
- Powers the sliding window maximum problem.

## 📺 Watch

1. **NeetCode — Linked List playlist** — follow the NeetCode 150 roadmap
2. **NeetCode — Stack playlist**

## 🔨 Practice Problems (NeetCode 150)

**Build from scratch first:** before solving LeetCode problems, implement a singly linked list class with `insert_head`, `insert_tail`, `delete`, `search`, `reverse`, and `print_list`. Do the same for a stack and queue class. Then move to the problems below.

| # | Problem | Category | Pattern | Difficulty |
|---|---------|----------|---------|------------|
| 1 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Linked List | In-place reversal | Easy |
| 2 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Linked List | Dummy head + merge | Easy |
| 3 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Linked List | Fast/slow pointers | Easy |
| 4 | [Reorder List](https://leetcode.com/problems/reorder-list/) | Linked List | Find middle + reverse + merge | Medium |
| 5 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Linked List | Two pointers with offset | Medium |
| 6 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Linked List | Hash map or interleave | Medium |
| 7 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Linked List | Linked list traversal + carry | Medium |
| 8 | [Find The Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Linked List | Floyd's cycle detection | Medium |
| 9 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Linked List | Hash map + doubly linked list | Medium |
| 10 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Linked List | Heap or divide & conquer | Hard |
| 11 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Linked List | In-place reversal + counting | Hard |
| 12 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Stack | Stack matching | Easy |
| 13 | [Min Stack](https://leetcode.com/problems/min-stack/) | Stack | Stack design | Medium |
| 14 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Stack | Stack evaluation | Medium |
| 15 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Stack | Stack / backtracking | Medium |
| 16 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Stack | Monotonic stack | Medium |
| 17 | [Car Fleet](https://leetcode.com/problems/car-fleet/) | Stack | Sort + monotonic stack | Medium |
| 18 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Stack | Monotonic stack | Hard |
| 19 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Heap / Priority Queue | Min heap of size k | Easy |
| 20 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Heap / Priority Queue | Max heap | Easy |
| 21 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Heap / Priority Queue | Min/max heap | Medium |
| 22 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Heap / Priority Queue | Max heap + greedy | Medium |
| 23 | [Design Twitter](https://leetcode.com/problems/design-twitter/) | Heap / Priority Queue | Heap + hash map + OOP | Medium |
| 24 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Heap / Priority Queue | Two heaps (min + max) | Hard |
| 25 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | 1-D DP | Fibonacci variant | Easy |
| 26 | [Happy Number](https://leetcode.com/problems/happy-number/) | Math & Geometry | Cycle detection (Floyd's) | Easy |
| 27 | [Subsets](https://leetcode.com/problems/subsets/) | Backtracking | Include/exclude recursion | Medium |

## 🔗 ML Connection

Computation graphs in PyTorch are essentially linked structures — each tensor knows which operation created it and what its inputs were. Backpropagation traverses this graph backward (like reversing a linked list of operations). Stacks appear in recursive computations and DFS-based graph analysis. Queues power BFS, which is used in some interpretability work to trace activation paths through networks layer by layer.
