# Lesson CS-06: Trees and Graphs — Connected Structures

[← Linked Lists](lesson-cs05-linked-lists-stacks-queues.md) | [Back to TOC](../README.md) | [Next: Sorting & Searching →](lesson-cs07-sorting-searching.md)

---

> **Why this lesson exists:** Neural networks are computation *graphs*. Attention mechanisms operate on *tree*-structured data (parse trees, hierarchical features). Graph traversal algorithms (BFS, DFS) are how you trace information flow through a network. These data structures appear constantly in both ML systems and alignment research.

## 🎯 Core Concepts

### Binary Trees

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

**Traversals (know all three cold):**

```python
def inorder(node):     # Left, Root, Right — gives sorted order for BST
    if not node: return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

def preorder(node):    # Root, Left, Right — useful for copying/serializing
    if not node: return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

def postorder(node):   # Left, Right, Root — useful for deletion, backprop!
    if not node: return
    postorder(node.left)
    postorder(node.right)
    print(node.val)
```

**Level-order (BFS):**
```python
from collections import deque
def level_order(root):
    if not root: return []
    queue = deque([root])
    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

### Binary Search Trees (BST)

- **Property:** left child < parent < right child (for all nodes).
- **Search/insert/delete:** O(log n) average, O(n) worst (degenerate = linked list).
- **Inorder traversal of a BST gives sorted output.**

### Graphs

**Representations:**
```python
# Adjacency list (most common)
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': [],
    'E': []
}

# Or: list of edges
edges = [('A','B'), ('A','C'), ('B','D'), ('C','D'), ('C','E')]
```

**DFS (Depth-First Search) — uses a stack (or recursion):**
```python
def dfs(graph, start, visited=None):
    if visited is None: visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

**BFS (Breadth-First Search) — uses a queue:**
```python
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

**When to use which:**
- DFS: path finding, cycle detection, topological sort, backtracking
- BFS: shortest path (unweighted), level-by-level exploration

## 📺 Watch

1. **NeetCode — Trees playlist** — follow the NeetCode 150 roadmap
2. **NeetCode — Graphs playlist**
3. **William Fiset — "Graph Theory playlist"** — deeper theory if you want it

## 🔨 Practice Problems (NeetCode 150)

| # | Problem | Category | Pattern | Difficulty |
|---|---------|----------|---------|------------|
| 1 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Trees | Tree recursion | Easy |
| 2 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Trees | Tree recursion | Easy |
| 3 | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Trees | DFS + global max | Easy |
| 4 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Trees | DFS + height check | Easy |
| 5 | [Same Tree](https://leetcode.com/problems/same-tree/) | Trees | Tree comparison | Easy |
| 6 | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Trees | Tree recursion | Easy |
| 7 | [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Trees | BST property | Medium |
| 8 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Trees | BFS | Medium |
| 9 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Trees | BFS / DFS | Medium |
| 10 | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | Trees | DFS + running max | Medium |
| 11 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Trees | DFS + bounds | Medium |
| 12 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Trees | Inorder traversal | Medium |
| 13 | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Trees | Recursion + hash map | Medium |
| 14 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Trees | DFS + global max | Hard |
| 15 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Trees | BFS or DFS | Hard |
| 16 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Tries | Trie design | Medium |
| 17 | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Tries | Trie + DFS (wildcard) | Medium |
| 18 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Tries | Trie + backtracking on grid | Hard |
| 19 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Graphs | DFS/BFS on grid | Medium |
| 20 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | Graphs | BFS + hash map | Medium |
| 21 | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Graphs | DFS on grid | Medium |
| 22 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Graphs | Multi-source DFS/BFS | Medium |
| 23 | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Graphs | Multi-source BFS | Medium |
| 24 | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | Graphs | Border DFS/BFS | Medium |
| 25 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Graphs | Topological sort / cycle detection | Medium |
| 26 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Graphs | Topological sort (return order) | Medium |
| 27 | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Graphs | Union-Find | Medium |
| 28 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | Graphs | BFS shortest path | Hard |
| 29 | [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | Advanced Graphs | Hierholzer's / DFS | Hard |
| 30 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Advanced Graphs | Prim's / Kruskal's MST | Medium |
| 31 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Advanced Graphs | Dijkstra's shortest path | Medium |
| 32 | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Advanced Graphs | Dijkstra's / binary search + BFS | Hard |
| 33 | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Advanced Graphs | Bellman-Ford / modified Dijkstra | Medium |
| 34 | [Word Search](https://leetcode.com/problems/word-search/) | Backtracking | Grid DFS/backtracking | Medium |
| 35 | [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | 2-D DP | DFS + memoization on grid | Hard |
| 36 | [Target Sum](https://leetcode.com/problems/target-sum/) | 2-D DP | Decision tree recursion | Medium |
| 37 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | Math & Geometry | Recursive divide-and-conquer | Medium |

## 🔗 ML Connection

**Postorder traversal IS backpropagation.** In a computation graph, you compute values forward (preorder-ish), then compute gradients backward (postorder — process children before parent). Topological sort determines the order of gradient computation. Course Schedule (LC #207) is literally asking "can this computation graph be executed without circular dependencies?" — the same question autograd systems answer.
