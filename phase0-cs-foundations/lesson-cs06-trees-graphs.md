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

## 🔨 Practice Problems

| # | Problem | Type | Difficulty |
|---|---------|------|------------|
| 1 | Invert Binary Tree (LC #226) | Tree recursion | Easy |
| 2 | Maximum Depth of Binary Tree (LC #104) | Tree recursion | Easy |
| 3 | Same Tree (LC #100) | Tree comparison | Easy |
| 4 | Subtree of Another Tree (LC #572) | Tree recursion | Easy |
| 5 | Lowest Common Ancestor of a BST (LC #235) | BST property | Medium |
| 6 | Binary Tree Level Order Traversal (LC #102) | BFS | Medium |
| 7 | Validate Binary Search Tree (LC #98) | DFS + bounds | Medium |
| 8 | Number of Islands (LC #200) | Graph DFS/BFS on grid | Medium |
| 9 | Clone Graph (LC #133) | Graph BFS + hash map | Medium |
| 10 | Course Schedule (LC #207) | Topological sort / cycle detection | Medium |

## 🔗 ML Connection

**Postorder traversal IS backpropagation.** In a computation graph, you compute values forward (preorder-ish), then compute gradients backward (postorder — process children before parent). Topological sort determines the order of gradient computation. Course Schedule (LC #207) is literally asking "can this computation graph be executed without circular dependencies?" — the same question autograd systems answer.
