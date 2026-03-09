# Lesson CS-06: Trees and Graphs — Connected Structures

[← Linked Lists](lesson-cs05-linked-lists-stacks-queues.md) | [Back to TOC](../README.md) | [Next: Sorting & Searching →](lesson-cs07-sorting-searching.md)

---

> **Tutor Instructions:** When walking a student through this lesson, don't just explain the concepts — create a series of small, progressive coding tasks that require the student to actively use each concept covered. Explain the relevant material, then immediately give a hands-on task before moving on. Review their solutions and correct mistakes before proceeding. Tasks should escalate in complexity throughout the lesson: start with ~1-minute exercises with immediate feedback, build to ~5-minute tasks, then ~10-minute tasks, and culminate in a ~30-minute capstone that integrates multiple concepts from the lesson. Let the student control the pace. Target ~2.5 hours for guided tutoring (explanations + coding tasks), then direct the student to spend ~1.5 hours doing LeetCode problems on their own to reinforce the concepts.

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

### Tree Traversal — DFS (in/pre/post)

**When to use:** computing properties of a tree (height, diameter, equality), transforming tree structure, or propagating values from root to leaves or leaves to root.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 1 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | DFS (in/pre/post) — recursive swap | Easy |
| 2 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | DFS (in/pre/post) — return values up | Easy |
| 3 | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | DFS + global state — track global max | Easy |
| 4 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | DFS (in/pre/post) — height check | Easy |
| 5 | [Same Tree](https://leetcode.com/problems/same-tree/) | DFS (in/pre/post) — parallel comparison | Easy |
| 6 | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | DFS (in/pre/post) — recursive subtree check | Easy |
| 10 | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | DFS + global state — running max down path | Medium |
| 13 | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | DFS (in/pre/post) — recursion + hash map | Medium |
| 14 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | DFS + global state — return values up, update global max | Hard |
| 15 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | DFS (in/pre/post) or BFS (level-order) | Hard |

### Tree Traversal — BFS (level-order)

**When to use:** processing nodes level by level, finding the rightmost/leftmost node per level, or minimum depth.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 8 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | BFS (level-order) — queue-based, process level by level | Medium |
| 9 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | BFS (level-order) — last node per level | Medium |

### BST Property

**When to use:** the tree is a BST and you can exploit left < root < right ordering, bounds propagation, or inorder-gives-sorted-order.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 7 | [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | BST property — use bounds to choose direction | Medium |
| 11 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | BST property — DFS + bounds | Medium |
| 12 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | BST property — inorder traversal gives sorted order | Medium |

### Trie

**When to use:** prefix matching, autocomplete, dictionary lookups, or combining prefix search with DFS/backtracking.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 16 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Basic trie — insert/search/startsWith | Medium |
| 17 | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Trie + DFS — wildcard search | Medium |
| 18 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Trie + DFS — backtracking on grid | Hard |

### Graph Traversal — DFS on Grid

**When to use:** flood fill, counting connected components, measuring region sizes on a 2D grid.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 19 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | DFS on grid — flood fill, connected components | Medium |
| 21 | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | DFS on grid — flood fill + accumulate size | Medium |
| 22 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Multi-source DFS/BFS — start from multiple borders | Medium |
| 24 | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | Multi-source DFS/BFS — border-connected flood fill | Medium |
| 34 | [Word Search](https://leetcode.com/problems/word-search/) | DFS on grid — backtracking | Medium |
| 35 | [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | DFS on grid + memoization | Hard |

### Graph Traversal — BFS

**When to use:** shortest path in unweighted graphs, multi-source spread (simultaneous BFS from multiple starting points), or clone/copy with visited tracking.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 20 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | Clone/copy — BFS/DFS + hash map old-to-new | Medium |
| 23 | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Multi-source BFS — simultaneous spread | Medium |
| 28 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | BFS (unweighted) — first visit = shortest path | Hard |

### Topological Sort

**When to use:** ordering with dependencies, cycle detection in directed graphs, scheduling problems.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 25 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Topological sort — cycle detection | Medium |
| 26 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Topological sort — return ordering | Medium |
| 29 | [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | Hierholzer's algorithm / DFS — Eulerian path | Hard |

### Shortest Path Algorithms

**When to use:** finding minimum-cost paths in weighted graphs. Dijkstra's for non-negative weights, Bellman-Ford when negative weights or hop constraints exist.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 31 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Dijkstra's — priority queue, weighted non-negative edges | Medium |
| 32 | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Dijkstra's — minimize max edge on path | Hard |
| 33 | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Bellman-Ford — k-stop constraint, negative-weight capable | Medium |

### Minimum Spanning Tree (MST)

**When to use:** connecting all nodes with minimum total edge weight.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 30 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Prim's / Kruskal's — MST | Medium |

### Union-Find (Disjoint Set)

**When to use:** tracking connected components dynamically, detecting cycles in undirected graphs.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 27 | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Union-Find — cycle detection in undirected graph | Medium |

### Cross-Topic Problems

Problems that primarily belong to other lessons but involve tree/graph structures.

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 36 | [Target Sum](https://leetcode.com/problems/target-sum/) | 2-D DP — decision tree recursion | Medium |
| 37 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | Math & Geometry — recursive divide-and-conquer | Medium |

## 🔗 ML Connection

**Postorder traversal IS backpropagation.** In a computation graph, you compute values forward (preorder-ish), then compute gradients backward (postorder — process children before parent). Topological sort determines the order of gradient computation. Course Schedule (LC #207) is literally asking "can this computation graph be executed without circular dependencies?" — the same question autograd systems answer.
