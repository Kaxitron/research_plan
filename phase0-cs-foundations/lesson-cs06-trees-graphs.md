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

---

## 🧩 Detailed Pattern Reference

### Tree DFS Patterns

There are three fundamental ways DFS communicates information through a tree. Every tree DFS problem uses one (or a combination) of these.

#### Pattern 1: "Return Value Up" DFS

The function returns a computed value that the parent node uses to build its own answer. Information flows from leaves upward to the root.

**How to recognize:**
- The question asks about a property of the whole tree (height, depth, is it balanced, is it symmetric).
- Each node needs information from both subtrees before it can answer.
- The words "maximum depth," "diameter," "balanced," or "same tree" appear.

**Template:**
```python
def dfs(node):
    if not node:
        return BASE_VALUE  # e.g., 0 for depth, True for balanced

    left = dfs(node.left)
    right = dfs(node.right)

    # Combine children's results to produce this node's result
    return COMBINE(left, right, node.val)
```

**Variations:**

| Problem | Base value | Combine logic |
|---------|-----------|---------------|
| Max depth | `return 0` | `return 1 + max(left, right)` |
| Balanced tree | `return 0` (height); return `-1` for unbalanced | If either child is `-1` or `abs(left - right) > 1`, return `-1`; else `1 + max(left, right)` |
| Same tree | `return True` (both None) | `return node1.val == node2.val and left and right` |
| Invert tree | `return None` | Swap `node.left, node.right = right, left`; return `node` |

#### Pattern 2: "Pass Value Down" DFS

Pass running state as a parameter from parent to child. Information flows from root downward to leaves.

**How to recognize:**
- The answer depends on the path from root to current node.
- You need to enforce constraints that tighten as you go deeper (BST bounds, running max).
- The words "path sum," "good nodes," "validate," or "root-to-leaf" appear.

**Template:**
```python
def dfs(node, state_from_parent):
    if not node:
        return BASE_VALUE

    # Use state_from_parent to make decisions at this node
    new_state = UPDATE(state_from_parent, node.val)

    left = dfs(node.left, new_state)
    right = dfs(node.right, new_state)
    return COMBINE(left, right)
```

**Variations:**

| Problem | State passed down | Update logic |
|---------|------------------|--------------|
| Path sum (root-to-leaf) | `remaining_sum` | `remaining_sum - node.val`; at leaf, check `== 0` |
| Good nodes | `max_so_far` | `max(max_so_far, node.val)`; count if `node.val >= max_so_far` |
| Validate BST | `(low, high)` bounds | Left child gets `(low, node.val)`, right gets `(node.val, high)` |
| LCA of BST | implicit — the BST property | If both targets < node, go left; both > node, go right; else found |

#### Pattern 3: "Global State" DFS

Update an external (nonlocal/class-level) variable during traversal. The DFS return value computes one thing, but the answer is tracked separately in the global variable.

**How to recognize:**
- The answer is not the root's return value but rather the best value found at *any* node.
- The problem asks for a "maximum" or "best" across all possible sub-paths.
- Classic signals: "maximum path sum," "diameter," "longest path."

**Template:**
```python
def solve(root):
    best = BASE_VALUE  # nonlocal or self.best

    def dfs(node):
        nonlocal best
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        # Update global answer (considers paths through this node)
        best = max(best, GLOBAL_COMBINE(left, right, node.val))

        # Return value to parent (single-branch contribution)
        return RETURN_COMBINE(left, right, node.val)

    dfs(root)
    return best
```

**Variations:**

| Problem | Global combine | Return to parent |
|---------|---------------|-----------------|
| Diameter | `max(best, left + right)` | `1 + max(left, right)` |
| Max path sum | `max(best, left + right + node.val)` | `max(node.val + max(left, right), 0)` (clamp negatives) |
| Longest univalue path | `max(best, left + right)` where left/right only count if same value | Matching-side length + 1, or 0 |

#### Pattern 4: Level-Order BFS

Process the tree level by level using a queue. The key trick is `for _ in range(len(queue))` to separate levels.

**How to recognize:**
- The problem explicitly asks about "levels," "depth," or "right/left side view."
- You need the minimum depth (BFS finds it first).
- You need to process all nodes at the same depth together.

**Template:**
```python
from collections import deque

def level_order(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        level_size = len(queue)  # snapshot before processing
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

**Variations:**

| Problem | What to do per level |
|---------|---------------------|
| Level order traversal | Collect all vals into `level` list |
| Right side view | Only keep `level[-1]` (last node per level) |
| Average of levels | `sum(level) / len(level)` |
| Minimum depth | Return depth when you hit the first leaf |
| Zigzag traversal | Reverse every other level |

#### Pattern 5: BST-Specific Techniques

BSTs give you a total ordering for free. Exploit it.

**How to recognize:**
- The input is explicitly a BST.
- The problem involves searching, validating, finding kth element, or finding closest value.

**Key properties to exploit:**

| Technique | When to use | Core idea |
|-----------|------------|-----------|
| Inorder = sorted | Kth smallest, convert BST to sorted list | Inorder traversal visits nodes in ascending order |
| Binary search on tree | Search/insert/delete, LCA | Compare target with `node.val` to choose left or right |
| Bounds propagation | Validate BST | Pass `(low, high)` down; left child must be `< node.val`, right must be `>` |
| Inorder with early stop | Kth smallest without full traversal | Count visits; stop at k |

**Inorder with counter template (kth smallest):**
```python
def kth_smallest(root, k):
    count = 0
    result = None

    def inorder(node):
        nonlocal count, result
        if not node or result is not None:
            return
        inorder(node.left)
        count += 1
        if count == k:
            result = node.val
            return
        inorder(node.right)

    inorder(root)
    return result
```

---

### Graph Patterns

#### Pattern 6: Grid DFS/BFS

Treat a 2D grid as an implicit graph where each cell has up to 4 neighbors.

**How to recognize:**
- Input is a 2D matrix/grid.
- The problem asks about connected regions, islands, area, or flood fill.

**Template (DFS):**
```python
def grid_dfs(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or (r, c) in visited or grid[r][c] == WALL):
            return 0
        visited.add((r, c))
        size = 1
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            size += dfs(r + dr, c + dc)
        return size

    # Example: count islands
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == LAND and (r, c) not in visited:
                dfs(r, c)
                count += 1
    return count
```

**Template (BFS):**
```python
from collections import deque

def grid_bfs(grid, start_r, start_c):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start_r, start_c)])
    visited = {(start_r, start_c)}
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and grid[nr][nc] != WALL):
                visited.add((nr, nc))
                queue.append((nr, nc))
```

**Variations:**

| Problem | Modification |
|---------|-------------|
| Number of islands | Outer loop starts DFS on each unvisited land cell; count components |
| Max area of island | DFS returns `size`; track max |
| Surrounded regions | Start DFS from border O's; mark them safe; flip remaining O's |
| Word search | DFS + backtracking; remove from visited after exploring |
| Longest increasing path | DFS + memoization; only move to strictly greater neighbors |

#### Pattern 7: Multi-Source BFS

Start BFS from multiple cells simultaneously. All sources are added to the queue at time 0, and the BFS wavefront expands outward from all of them in parallel.

**How to recognize:**
- Multiple starting points spread outward at the same time (rotting oranges, fire spreading).
- You need to find cells reachable from any of a set of border cells (pacific atlantic).
- The problem asks for the minimum time/distance from *any* source to all other cells.

**Template:**
```python
from collections import deque

def multi_source_bfs(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    visited = set()

    # Step 1: enqueue ALL sources at once
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == SOURCE:
                queue.append((r, c, 0))  # (row, col, distance/time)
                visited.add((r, c))

    # Step 2: standard BFS from all sources simultaneously
    max_dist = 0
    while queue:
        r, c, dist = queue.popleft()
        max_dist = max(max_dist, dist)
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and grid[nr][nc] != WALL):
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return max_dist
```

**Variations:**

| Problem | Sources | Direction |
|---------|---------|-----------|
| Rotting oranges | All rotten cells | Forward from sources; track time |
| Pacific atlantic | Border cells (two separate BFS runs) | Reverse: flow uphill from ocean borders; intersect reachable sets |
| Walls and gates | All gate cells | Forward from gates; first visit = shortest distance |
| 01 matrix | All 0-cells | Forward from zeros; first visit gives nearest-zero distance |

#### Pattern 8: Topological Sort

Order nodes in a directed acyclic graph (DAG) so that for every edge u -> v, u comes before v.

**How to recognize:**
- Dependencies or prerequisites ("take course A before course B").
- The problem asks "is there a valid ordering?" or "return the ordering."
- Cycle detection in a directed graph.

**Approach 1: Kahn's Algorithm (BFS-based) -- preferred for most problems:**
```python
from collections import deque, defaultdict

def topo_sort_kahn(num_nodes, edges):
    graph = defaultdict(list)
    in_degree = [0] * num_nodes

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) == num_nodes:
        return order        # valid topological order
    else:
        return []           # cycle detected — not a DAG
```

**Approach 2: DFS-based (postorder reverse):**
```python
def topo_sort_dfs(num_nodes, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * num_nodes
    order = []
    has_cycle = False

    def dfs(node):
        nonlocal has_cycle
        if has_cycle:
            return
        color[node] = GRAY
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                has_cycle = True
                return
            if color[neighbor] == WHITE:
                dfs(neighbor)
        color[node] = BLACK
        order.append(node)

    for i in range(num_nodes):
        if color[i] == WHITE:
            dfs(i)

    if has_cycle:
        return []
    return order[::-1]  # reverse postorder = topological order
```

**When to use which approach:**

| Criterion | Kahn's (BFS) | DFS-based |
|-----------|-------------|-----------|
| Need the ordering | Returns it directly | Reverse postorder |
| Cycle detection | `len(order) < num_nodes` | Gray-to-gray edge |
| Parallel scheduling (levels) | Natural: process by "rounds" of zero in-degree | Harder to extract levels |
| Simpler to implement | Usually yes | Slightly more code |

#### Pattern 9: Cycle Detection

**In directed graphs (DFS 3-coloring):**

**How to recognize:** "Can all courses be completed?" / "Is there a circular dependency?"

The 3-color approach from topological sort handles this. A cycle exists if DFS encounters a GRAY node (currently on the recursion stack).

```python
# Uses the same WHITE/GRAY/BLACK coloring as DFS topo sort above.
# Cycle exists if you ever visit a GRAY neighbor.
```

**In undirected graphs (Union-Find or parent tracking):**

**How to recognize:** "Find the redundant edge" / "Is the graph a valid tree?"

Option A -- Parent tracking in DFS:
```python
def has_cycle_undirected(graph, n):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if neighbor in visited:
                return True   # cycle found
            if dfs(neighbor, node):
                return True
        return False

    for i in range(n):
        if i not in visited:
            if dfs(i, -1):
                return True
    return False
```

Option B -- Union-Find (see Pattern 10).

#### Pattern 10: Union-Find (Disjoint Set Union)

Track connected components. Supports near-O(1) union and find with path compression + union by rank.

**How to recognize:**
- "Are these two nodes connected?"
- "How many connected components?"
- Dynamically adding edges and querying connectivity.
- Cycle detection in undirected graphs (if union returns False, the edge creates a cycle).

**Template:**
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # already connected (cycle if adding edge)
        # union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True
```

**Variations:**

| Problem | How Union-Find is used |
|---------|----------------------|
| Redundant connection | Add edges one by one; first edge where `union` returns `False` is the answer |
| Number of provinces | Union all edges; return `self.components` |
| Accounts merge | Union accounts sharing an email |
| Min cost to connect all points (Kruskal's MST) | Sort edges by weight; union greedily; stop when 1 component |

#### Pattern 11: Dijkstra's Algorithm

Shortest path in a weighted graph with non-negative edge weights. Uses a min-heap (priority queue).

**How to recognize:**
- Weighted graph with non-negative weights.
- "Shortest path," "minimum cost," "minimum time" to reach a node.
- Grid problems where movement cost varies per cell.

**Template:**
```python
import heapq
from collections import defaultdict

def dijkstra(n, edges, source):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        # graph[v].append((u, w))  # uncomment for undirected

    dist = [float('inf')] * n
    dist[source] = 0
    heap = [(0, source)]  # (distance, node)

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue  # stale entry, skip
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist
```

**Variations:**

| Problem | Modification |
|---------|-------------|
| Network delay time | Run Dijkstra from source; answer is `max(dist)` |
| Swim in rising water | Edge weight = `max(grid[r][c], grid[nr][nc])`; minimize the max along path |
| Path with minimum effort | Edge weight = abs difference in heights; minimize the max effort along path |
| Cheapest flights within k stops | Use Bellman-Ford instead (Dijkstra does not handle hop constraints well) |

#### When to Use BFS vs DFS vs Dijkstra

| Scenario | Algorithm | Why |
|----------|-----------|-----|
| Unweighted shortest path | BFS | First visit = shortest distance; O(V+E) |
| Explore all paths / backtrack | DFS | Natural recursion; easy to undo choices |
| Weighted non-negative shortest path | Dijkstra | Greedy with min-heap; O((V+E) log V) |
| Weighted with negative edges | Bellman-Ford | Relaxes all edges V-1 times; O(VE) |
| Weighted with negative edges (all pairs) | Floyd-Warshall | DP over all pairs; O(V^3) |
| Detect cycles (directed) | DFS (3-color) | Gray-to-gray = back edge = cycle |
| Detect cycles (undirected) | Union-Find or DFS with parent | Union returning False = cycle |
| Dependency ordering | Topological sort (Kahn's or DFS) | Only valid on DAGs |
| Connected components (static) | DFS or BFS | One traversal per component |
| Connected components (dynamic) | Union-Find | Efficient incremental merging |

---

### Trie Pattern

#### Pattern 12: Trie (Prefix Tree)

A tree where each node represents one character of a string. Paths from root to a node spell out prefixes.

**How to recognize:**
- Prefix matching ("find all words starting with...").
- Autocomplete / search suggestions.
- Need to check if any prefix of a word exists in a dictionary.
- Word search on a grid with a dictionary (trie + backtracking).

**Node structure and template:**
```python
class TrieNode:
    def __init__(self):
        self.children = {}      # char -> TrieNode
        self.is_end = False     # marks end of a complete word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        """Returns True if the exact word exists."""
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix):
        """Returns True if any word starts with prefix."""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
```

**When tries beat hash maps:**

| Criterion | Trie | Hash Set/Map |
|-----------|------|-------------|
| Prefix queries ("any word starts with X?") | O(len(prefix)) -- natural | O(N * avg_len) -- must check all words |
| Exact word lookup | O(len(word)) | O(len(word)) average -- tie |
| Memory for many words sharing prefixes | Shared prefixes save space | Each word stored independently |
| Wildcard search (`.` matches any char) | DFS through children at wildcard positions | Must enumerate all possibilities |
| Word Search II (grid + dictionary) | Prune entire branches when prefix not found | Cannot prune; check each word independently |

**Rule of thumb:** Use a trie when the problem involves *prefix relationships* between words or *pruning search paths* based on partial matches. Use a hash set when you only need exact lookups.

---

### Pattern Decision Tree

Use this to pick your approach when you see a new tree/graph problem:

```
Is the input a TREE or a GRAPH?
│
├── TREE
│   ├── Is it a BST?
│   │   ├── Yes → Exploit ordering: inorder = sorted, binary search to navigate,
│   │   │         bounds propagation to validate
│   │   └── No → General binary tree (continue below)
│   │
│   ├── Does the problem ask about levels/depth/views?
│   │   ├── Yes → Level-order BFS (Pattern 4)
│   │   └── No → DFS (continue below)
│   │
│   ├── Does each node need info from its children?
│   │   └── Yes → "Return value up" DFS (Pattern 1)
│   │
│   ├── Does each node need info from the root/path above it?
│   │   └── Yes → "Pass value down" DFS (Pattern 2)
│   │
│   └── Is the answer the best value found at ANY node (not just root)?
│       └── Yes → "Global state" DFS (Pattern 3)
│
├── GRAPH (or GRID)
│   ├── Is it a 2D grid?
│   │   ├── Connected components / flood fill → Grid DFS (Pattern 6)
│   │   ├── Simultaneous spread from multiple sources → Multi-source BFS (Pattern 7)
│   │   └── Weighted movement cost → Dijkstra on grid (Pattern 11)
│   │
│   ├── Are there dependencies / ordering constraints?
│   │   └── Yes → Topological sort (Pattern 8)
│   │
│   ├── Need shortest path?
│   │   ├── Unweighted → BFS
│   │   ├── Weighted, non-negative → Dijkstra (Pattern 11)
│   │   └── Weighted, negative or hop-limited → Bellman-Ford
│   │
│   ├── Need to detect cycles?
│   │   ├── Directed graph → DFS 3-coloring (Pattern 9)
│   │   └── Undirected graph → Union-Find (Pattern 10) or DFS with parent
│   │
│   ├── Need connected components dynamically?
│   │   └── Yes → Union-Find (Pattern 10)
│   │
│   └── Need minimum spanning tree?
│       └── Yes → Kruskal's (sort edges + Union-Find) or Prim's (min-heap)
│
└── STRING PREFIX problem?
    └── Yes → Trie (Pattern 12)
```

---

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
