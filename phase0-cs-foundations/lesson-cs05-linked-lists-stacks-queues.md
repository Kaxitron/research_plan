# Lesson CS-05: Linked Lists, Stacks, and Queues

[← Arrays & Hashing](lesson-cs04-arrays-hashing.md) | [Back to TOC](../README.md) | [Next: Trees & Graphs →](lesson-cs06-trees-graphs.md)

---

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

## 🔨 Practice Problems

| # | Problem | Structure | Difficulty |
|---|---------|-----------|------------|
| 1 | Reverse Linked List (LC #206) | Linked list | Easy |
| 2 | Merge Two Sorted Lists (LC #21) | Linked list | Easy |
| 3 | Linked List Cycle (LC #141) | Fast/slow pointers | Easy |
| 4 | Reorder List (LC #143) | Find middle + reverse + merge | Medium |
| 5 | Remove Nth Node From End (LC #19) | Two pointers with offset | Medium |
| 6 | Valid Parentheses (LC #20) | Stack | Easy |
| 7 | Min Stack (LC #155) | Stack design | Medium |
| 8 | Evaluate Reverse Polish Notation (LC #150) | Stack | Medium |
| 9 | Daily Temperatures (LC #739) | Monotonic stack | Medium |
| 10 | Implement Queue using Stacks (LC #232) | Stack/Queue | Easy |

**Build from scratch first:** before solving LeetCode problems, implement a singly linked list class with `insert_head`, `insert_tail`, `delete`, `search`, `reverse`, and `print_list`. Do the same for a stack and queue class. Then move to the problems above.

## 🔗 ML Connection

Computation graphs in PyTorch are essentially linked structures — each tensor knows which operation created it and what its inputs were. Backpropagation traverses this graph backward (like reversing a linked list of operations). Stacks appear in recursive computations and DFS-based graph analysis. Queues power BFS, which is used in some interpretability work to trace activation paths through networks layer by layer.
