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

#### Pattern: Dummy Head Technique

> **How to recognize:** The head node itself might be removed or changed (e.g., merge two lists, remove duplicates, partition list). Any time you would otherwise need special-case logic for the head.

**Why it works:** A dummy node before the real head means every real node — including the original head — has a predecessor. You never need `if head is None` or `if curr == head` branches. At the end, `dummy.next` is your answer.

```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
```

| Variation | When to use | Example problems |
|-----------|-------------|-----------------|
| Dummy head + merge | Merging two or more sorted lists | Merge Two Sorted Lists, Merge k Sorted Lists |
| Dummy head + traversal with carry | Digit-by-digit arithmetic on lists | Add Two Numbers |
| Dummy head + filter | Removing nodes by condition | Remove Duplicates, Remove Elements |
| Dummy head + partition | Splitting list around a pivot | Partition List |

#### Pattern: Fast/Slow Pointers

> **How to recognize:** You need to find the middle of a list, detect a cycle, or find the k-th node from the end — all without knowing the list length in advance.

**Cycle detection (Floyd's algorithm):** Slow moves 1 step, fast moves 2. If they meet, there is a cycle. To find the cycle entry, reset one pointer to head and advance both by 1 until they meet again.

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

def find_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            # Reset one pointer to head
            slow = head
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow  # cycle entry
    return None
```

**Find middle of list:**

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # middle node (second middle if even length)
```

**Find n-th node from end:** Advance fast by n steps first, then move both. When fast reaches the end, slow is at the target.

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next  # skip the target node
    return dummy.next
```

| Variation | Speed ratio | What it finds |
|-----------|-------------|---------------|
| Slow 1, Fast 2 | 1:2 | Middle node, cycle detection |
| Slow 1, Fast 2 + reset phase | 1:2 then 1:1 | Cycle entry point |
| Offset start by n | 1:1 with head start | n-th from end |

#### Pattern: In-Place Reversal

> **How to recognize:** You need to reverse all or part of a linked list. Look for words like "reverse," "reorder," or problems where the output list has a different traversal order than the input.

**The prev/curr/next dance:** At each step you save the next node, point current backward, and advance. Three variables, three lines in the loop.

```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next   # 1. save next
        curr.next = prev   # 2. reverse pointer
        prev = curr        # 3. advance prev
        curr = nxt         # 4. advance curr
    return prev  # new head
```

**Reverse a sub-section (between positions left and right):**

```python
def reverse_between(head, left, right):
    dummy = ListNode(0, head)
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next
    curr = prev.next
    for _ in range(right - left):
        nxt = curr.next
        curr.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt
    return dummy.next
```

| Variation | Description | Example problems |
|-----------|-------------|-----------------|
| Full reversal | Reverse entire list | Reverse Linked List |
| Partial reversal | Reverse between positions left and right | Reverse Linked List II |
| K-group reversal | Reverse every k nodes | Reverse Nodes in k-Group |
| Alternating reversal | Reverse every other group | — |

#### Pattern: Merge Technique

> **How to recognize:** You have two or more sorted linked lists and need to produce a single sorted result, or you need to interleave nodes from multiple lists.

The template is the dummy-head merge shown above. For k lists, you either merge pairwise (divide and conquer, O(N log k)) or use a min-heap to always pick the smallest head (also O(N log k)).

```python
import heapq

def merge_k_lists(lists):
    dummy = ListNode(0)
    tail = dummy
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
```

#### Pattern: Composite — Find Middle + Reverse + Merge

> **How to recognize:** The problem asks you to rearrange nodes in a way that depends on position from both ends (e.g., "first, last, second, second-to-last, ..."). Classic example: Reorder List.

**Steps:**
1. Find the middle using fast/slow pointers.
2. Reverse the second half in-place.
3. Merge/interleave the two halves.

```python
def reorder_list(head):
    # Step 1: find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None  # cut

    # Step 2: reverse second half
    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    second = prev

    # Step 3: interleave
    first = head
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
```

### Stacks — Last In, First Out (LIFO)

- **Operations:** `push` (add to top), `pop` (remove from top), `peek` (look at top). All O(1).
- **Implementation:** just use a Python list or C++ `stack<T>`.
- **When to use:** matching parentheses, undo operations, DFS, expression evaluation, monotonic stack problems.

#### Pattern: Matching / Balancing

> **How to recognize:** The problem involves nested or paired symbols — parentheses, brackets, braces, HTML tags, or any "open/close" structure.

**Template:**

```python
def is_valid(s):
    stack = []
    match = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in match:
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return len(stack) == 0
```

| Variation | Description | Example problems |
|-----------|-------------|-----------------|
| Simple matching | Check if brackets are balanced | Valid Parentheses |
| Generate valid sequences | Backtrack with open/close counts | Generate Parentheses |
| Minimum removals | Track indices of unmatched brackets | Minimum Remove to Make Valid Parentheses |
| Nested depth | Track max stack size | Maximum Nesting Depth of Parentheses |

#### Pattern: Expression Evaluation

> **How to recognize:** The problem asks you to evaluate a mathematical expression given as a string, or the input is already in postfix (Reverse Polish) notation.

**RPN evaluation template:**

```python
def eval_rpn(tokens):
    stack = []
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b),  # truncate toward zero
    }
    for token in tokens:
        if token in ops:
            b, a = stack.pop(), stack.pop()  # order matters
            stack.append(ops[token](a, b))
        else:
            stack.append(int(token))
    return stack[0]
```

For infix expressions (Basic Calculator problems), use two stacks (one for values, one for operators) or convert to postfix first. Parentheses trigger recursive sub-evaluation or push/pop of partial results.

| Variation | Approach | Example problems |
|-----------|----------|-----------------|
| Postfix (RPN) | Single stack, push numbers, pop-operate-push | Evaluate Reverse Polish Notation |
| Infix, no precedence | Stack of partial results, handle `(` and `)` | Basic Calculator |
| Infix with precedence | Two stacks or Shunting Yard | Basic Calculator II |

#### Pattern: Monotonic Stack

> **How to recognize:** The problem asks for the "next greater element," "next smaller element," "days until warmer temperature," or anything that compares each element to future/past elements in a nearest-match fashion. Also appears in histogram and rectangle area problems.

**Why it works:** A monotonic stack maintains elements in sorted order (either increasing or decreasing). When a new element violates the order, you pop elements that are "resolved" by this new element. Each element is pushed and popped at most once, giving O(n) overall.

**Next greater element template (decreasing stack):**

```python
def next_greater_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices; values at these indices are decreasing
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result
```

**Largest rectangle in histogram template (increasing stack):**

```python
def largest_rectangle(heights):
    stack = []  # increasing stack of indices
    max_area = 0
    heights.append(0)  # sentinel to flush remaining bars
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area
```

| Variation | Stack order | What it finds | Example problems |
|-----------|------------|---------------|-----------------|
| Decreasing stack | Top is smallest | Next greater element | Daily Temperatures, Next Greater Element |
| Increasing stack | Top is largest | Next smaller element | Largest Rectangle in Histogram |
| Circular variant | Process array twice (mod n) | Next greater in circular array | Next Greater Element II |

#### Pattern: Stack for DFS Simulation

> **How to recognize:** You need DFS traversal but want to avoid recursion (to prevent stack overflow on deep inputs, or the problem explicitly asks for iterative traversal).

Replace the call stack with an explicit stack. Push neighbors in reverse order so they are processed in the correct order.

```python
def iterative_dfs(root):
    if not root:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)  # left is popped first
    return result
```

### Queues — First In, First Out (FIFO)

- **Operations:** `enqueue` (add to back), `dequeue` (remove from front). All O(1) with proper implementation.
- **Implementation:** Python `collections.deque` (NOT a list — `list.pop(0)` is O(n)). C++ `queue<T>`.
- **When to use:** BFS, scheduling, buffering, level-order traversal.

### Deque — Double-Ended Queue

- Insert/remove from both ends in O(1). Python `collections.deque`. C++ `deque<T>`.
- Powers the sliding window maximum problem.

### Heaps / Priority Queues

> Python's `heapq` module provides a **min-heap**. For a max-heap, negate values on push/pop.

```python
import heapq

# Min-heap usage
heap = []
heapq.heappush(heap, val)
smallest = heapq.heappop(heap)

# Max-heap trick
heapq.heappush(heap, -val)
largest = -heapq.heappop(heap)
```

#### Pattern: Top-K Elements

> **How to recognize:** The problem asks for the k largest, k smallest, k most frequent, or k closest elements. Any time you need to maintain a "best k" out of a stream or array.

**Strategy:** Maintain a min-heap of size k. For each element, push it. If the heap exceeds size k, pop the smallest. At the end, the heap contains the k largest elements. (For k smallest, use a max-heap of size k instead.)

**Time complexity:** O(n log k) — much better than sorting O(n log n) when k is small.

```python
def k_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # remove smallest
    return heap  # contains k largest
```

| Variation | Heap type | Size | Example problems |
|-----------|-----------|------|-----------------|
| K largest | Min-heap | k | Kth Largest Element in a Stream |
| K closest | Min-heap (negate distance) or max-heap | k | K Closest Points to Origin |
| K most frequent | Min-heap on frequency | k | Top K Frequent Elements |

#### Pattern: Two Heaps (Running Median)

> **How to recognize:** You need to maintain a running median or balanced partition of a data stream. More generally, any time you need quick access to both the "lower half max" and the "upper half min."

**Strategy:** Keep a max-heap for the lower half and a min-heap for the upper half. Balance their sizes so they differ by at most 1. The median is the top of the larger heap (odd count) or the average of both tops (even count).

```python
class MedianFinder:
    def __init__(self):
        self.lo = []  # max-heap (negate values)
        self.hi = []  # min-heap

    def addNum(self, num):
        heapq.heappush(self.lo, -num)
        # Ensure max of lo <= min of hi
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        # Balance sizes: lo can be larger by at most 1
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
```

#### Pattern: Greedy Scheduling with Heap

> **How to recognize:** You repeatedly need to process the highest-priority (or largest/smallest) item, possibly with cooldowns, deadlines, or constraints on ordering. "Simulate a process that always picks the best available option."

**Template (Task Scheduler style):**

```python
def least_interval(tasks, n):
    counts = Counter(tasks)
    heap = [-cnt for cnt in counts.values()]
    heapq.heapify(heap)
    time = 0
    cooldown = deque()  # (available_time, remaining_count)
    while heap or cooldown:
        time += 1
        if heap:
            cnt = 1 + heapq.heappop(heap)  # cnt is negative, adding 1 moves toward 0
            if cnt:
                cooldown.append((time + n, cnt))
        if cooldown and cooldown[0][0] == time:
            heapq.heappush(heap, cooldown.popleft()[1])
    return time
```

| Variation | Description | Example problems |
|-----------|-------------|-----------------|
| Max-heap greedy | Always process highest-priority item | Last Stone Weight |
| Heap + cooldown queue | Process with mandatory gaps | Task Scheduler |
| Heap + time simulation | Simulate event-driven scheduling | Process Tasks Using Servers |

#### Pattern: K-Way Merge

> **How to recognize:** You have k sorted sequences (lists, arrays, streams) and need to produce a single sorted output. This is the multi-list generalization of Merge Two Sorted Lists.

**Strategy:** Push the head of each list into a min-heap. Pop the smallest, then push that element's successor. Repeat until the heap is empty.

```python
def merge_k_sorted(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # (value, list_index, element_index)
    result = []
    while heap:
        val, li, ei = heapq.heappop(heap)
        result.append(val)
        if ei + 1 < len(lists[li]):
            heapq.heappush(heap, (lists[li][ei + 1], li, ei + 1))
    return result
```

**Time complexity:** O(N log k) where N is total elements across all lists.

### Pattern Decision Tree

Use this to pick the right data structure based on what the problem is asking:

```
What does the problem need?
│
├─ Frequent insert/delete, no random access needed?
│  └─ LINKED LIST
│     ├─ Head might change? → Use dummy head
│     ├─ Find middle / detect cycle / k-th from end? → Fast/slow pointers
│     ├─ Reverse order? → In-place reversal (prev/curr/next)
│     ├─ Merge sorted sequences? → Dummy head + merge (or heap for k-way)
│     └─ Rearrange by position from both ends? → Composite: find middle + reverse + merge
│
├─ Matching/nesting/undo, or "most recent first" access?
│  └─ STACK
│     ├─ Paired symbols (open/close)? → Matching/balancing
│     ├─ Evaluate expression? → Expression evaluation (one or two stacks)
│     ├─ Next greater/smaller element? → Monotonic stack
│     └─ DFS without recursion? → Explicit stack for DFS simulation
│
├─ Process in arrival order, level-by-level, or scheduling?
│  └─ QUEUE / DEQUE
│     ├─ BFS / level-order traversal? → Queue
│     ├─ Sliding window min/max? → Monotonic deque
│     └─ Need both ends? → Deque
│
└─ Need repeated access to min/max, or top-k, or sorted merge of streams?
   └─ HEAP (Priority Queue)
      ├─ K largest/smallest/closest? → Min-heap of size k (top-k)
      ├─ Running median or balanced partition? → Two heaps (max-heap + min-heap)
      ├─ Greedy "always pick best available"? → Max-heap (possibly + cooldown queue)
      └─ Merge k sorted sequences? → Min-heap with k entries (k-way merge)
```

## 📺 Watch

1. **NeetCode — Linked List playlist** — follow the NeetCode 150 roadmap
2. **NeetCode — Stack playlist**

## 🔨 Practice Problems (NeetCode 150)

**Build from scratch first:** before solving LeetCode problems, implement a singly linked list class with `insert_head`, `insert_tail`, `delete`, `search`, `reverse`, and `print_list`. Do the same for a stack and queue class. Then move to the problems below.

### Linked List Patterns

**When to use:** problems involving pointer manipulation, merging sorted sequences, cycle detection, or restructuring node order in-place.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 1 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | In-place reversal | Easy |
| 2 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Dummy head + merge | Easy |
| 3 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Fast/slow pointers | Easy |
| 4 | [Reorder List](https://leetcode.com/problems/reorder-list/) | Composite: find middle + reverse + merge | Medium |
| 5 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Fast/slow pointers with offset | Medium |
| 6 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Hash map or interleave | Medium |
| 7 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Dummy head + traversal with carry | Medium |
| 8 | [Find The Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Fast/slow pointers (Floyd's cycle detection) | Medium |
| 9 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Hash map + doubly linked list | Medium |
| 10 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Dummy head + merge (heap or divide & conquer) | Hard |
| 11 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | In-place reversal + counting | Hard |

### Stack Patterns

**When to use:** problems requiring matching/balancing (parentheses, tags), evaluating expressions, tracking "next greater/smaller" via monotonic stacks, or designing data structures with O(1) auxiliary queries.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 12 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Matching/balancing | Easy |
| 13 | [Min Stack](https://leetcode.com/problems/min-stack/) | Design: stack with extra capability | Medium |
| 14 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Expression evaluation | Medium |
| 15 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Matching/balancing + backtracking | Medium |
| 16 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Monotonic stack | Medium |
| 17 | [Car Fleet](https://leetcode.com/problems/car-fleet/) | Sort + monotonic stack | Medium |
| 18 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Monotonic stack | Hard |

### Heap / Priority Queue Patterns

**When to use:** problems asking for the k-th largest/smallest, maintaining a running median, or greedy scheduling where you always process the highest-priority item next.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 19 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Top-k (min-heap of size k) | Easy |
| 20 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Greedy scheduling (max-heap) | Easy |
| 21 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Top-k (min/max heap) | Medium |
| 22 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Greedy scheduling (max-heap + greedy) | Medium |
| 23 | [Design Twitter](https://leetcode.com/problems/design-twitter/) | Top-k (heap + hash map + OOP) | Medium |
| 24 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Two heaps (min + max) | Hard |

### Cross-Topic Problems

| # | Problem | Category | Pattern | Difficulty |
|---|---------|----------|---------|------------|
| 25 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | 1-D DP | Fibonacci variant | Easy |
| 26 | [Happy Number](https://leetcode.com/problems/happy-number/) | Math & Geometry | Cycle detection (Floyd's) | Easy |
| 27 | [Subsets](https://leetcode.com/problems/subsets/) | Backtracking | Include/exclude recursion | Medium |

## 🔗 ML Connection

Computation graphs in PyTorch are essentially linked structures — each tensor knows which operation created it and what its inputs were. Backpropagation traverses this graph backward (like reversing a linked list of operations). Stacks appear in recursive computations and DFS-based graph analysis. Queues power BFS, which is used in some interpretability work to trace activation paths through networks layer by layer.
