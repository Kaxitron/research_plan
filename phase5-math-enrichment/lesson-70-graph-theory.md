# Lesson 70: Graph Theory — Networks, Connections, and Structure

[← Combinatorics](lesson-69-combinatorics.md) | [Back to TOC](../README.md) | [Next: Recurrences & Generating Functions →](lesson-71-recurrences-generating-functions.md)

---

> **Why this lesson exists:** Graphs are the mathematical language of connections. Neural networks are literally graphs — nodes are neurons, edges are weights. Computational graphs define how gradients flow during backpropagation. Knowledge graphs store relational information that AI systems reason over. Causal inference (critical for alignment) uses directed acyclic graphs. Understanding graph theory gives you the vocabulary and tools to analyze network architectures, reason about information flow in AI systems, and understand the structural properties that make some networks more capable or more interpretable than others.

> **Estimated time:** 15–20 hours

---

## Part 1: Fundamental Definitions

### What Is a Graph?

A **graph** G = (V, E) consists of:
- A set **V** of **vertices** (also called nodes)
- A set **E** of **edges**, where each edge connects two vertices

An edge between vertices u and v is written as {u, v} (for undirected graphs) or (u, v) (for directed graphs).

**Undirected graph:** Edges have no direction. {u, v} and {v, u} are the same edge. Think of a friendship network: if Alice is friends with Bob, Bob is friends with Alice.

**Directed graph (digraph):** Edges have direction. (u, v) means an edge FROM u TO v, which is different from (v, u). Think of Twitter follows: Alice following Bob does not mean Bob follows Alice.

### Degree

The **degree** of a vertex v (written deg(v)) is the number of edges incident to v — how many connections it has.

In a directed graph, we distinguish:
- **In-degree:** number of edges pointing INTO v
- **Out-degree:** number of edges pointing OUT of v

**The Handshaking Lemma:** The sum of all vertex degrees equals twice the number of edges.

Sum of deg(v) for all v in V = 2|E|

*Intuition:* Each edge contributes exactly 1 to the degree of each of its two endpoints, so it is counted twice in the total.

**Corollary:** The number of vertices with odd degree must be even. (Because the total degree is even.)

This seemingly trivial observation is surprisingly powerful — it constrains which graphs can exist and is the key to understanding Euler paths.

### Special Graphs

**Complete graph K_n:** Every pair of vertices is connected. Has n(n-1)/2 edges. K_5 and K_3,3 are important for planarity (covered below).

**Bipartite graph:** Vertices can be split into two groups such that every edge goes between the groups (no edges within a group). Think of a recommendation system: users on one side, items on the other, edges represent interactions.

**Complete bipartite graph K_{m,n}:** Every vertex in the first group (size m) connects to every vertex in the second group (size n). Has m*n edges.

**Cycle C_n:** n vertices arranged in a cycle, each connected to its two neighbors. The simplest "loop."

**Tree:** A connected graph with no cycles. Trees are the "minimal" connected graphs — they have exactly |V| - 1 edges.

### Weighted Graphs

A **weighted graph** assigns a numerical weight to each edge. Weights can represent distances, costs, capacities, or — in neural networks — the strength of connections between neurons.

In a neural network, the adjacency structure defines the architecture, and the edge weights are the learned parameters. Training is the process of adjusting edge weights to minimize a loss function.

---

## Part 2: Paths, Cycles, and Connectivity

### Paths and Walks

A **walk** is a sequence of vertices v0, v1, ..., vk where each consecutive pair is connected by an edge. Vertices and edges may repeat.

A **path** is a walk where no vertex repeats.

A **cycle** is a walk that starts and ends at the same vertex, with no other vertex repeated.

The **length** of a walk/path is the number of edges traversed.

### Connectivity

A graph is **connected** if there is a path between every pair of vertices. Otherwise, it breaks into **connected components** — maximal connected subgraphs.

For directed graphs, we distinguish:
- **Strongly connected:** there is a directed path from u to v AND from v to u, for every pair (u, v)
- **Weakly connected:** the graph is connected if you ignore edge directions

**ML connection:** In a neural network's computational graph, connectivity determines whether gradient signals can flow from the loss back to every parameter. If a parameter is in a disconnected component from the loss, it receives zero gradient and cannot be trained. Skip connections (as in ResNets) add edges to the computational graph, improving gradient connectivity and enabling training of very deep networks.

### Euler Paths and Circuits

An **Euler path** visits every *edge* exactly once. An **Euler circuit** is an Euler path that starts and ends at the same vertex.

**Euler's Theorem:**
- A connected graph has an Euler circuit if and only if every vertex has even degree.
- A connected graph has an Euler path (but not a circuit) if and only if it has exactly two vertices of odd degree (these must be the start and end points).

This is the theorem that solved the Konigsberg Bridge Problem — the problem that launched graph theory in 1736. The seven bridges of Konigsberg formed a graph where every vertex had odd degree, so no Euler circuit (or path) existed.

### Hamilton Paths and Circuits

A **Hamilton path** visits every *vertex* exactly once. A **Hamilton circuit** is a Hamilton path that returns to its start.

Unlike Euler paths, there is **no simple characterization** of which graphs have Hamilton paths. Determining whether a graph has a Hamilton path is NP-complete — one of the foundational hard problems in computer science. This contrast between Euler (polynomial-time) and Hamilton (NP-complete) illustrates how slight changes in problem formulation can dramatically change computational complexity.

---

## Part 3: Trees

### Properties of Trees

A **tree** is a connected acyclic graph. The following are equivalent for a graph G with n vertices:
1. G is a tree
2. G is connected and has n - 1 edges
3. G is acyclic and has n - 1 edges
4. There is exactly one path between any two vertices

Trees are "just barely connected" — removing any edge disconnects the graph. Adding any edge creates exactly one cycle.

### Rooted Trees

A **rooted tree** has a designated root vertex. This induces a parent-child hierarchy: every non-root vertex has exactly one parent (the next vertex on the path toward the root).

Rooted trees appear everywhere in CS:
- File systems
- Decision trees in machine learning
- Parse trees in natural language processing
- Search trees in game-playing AI (like Monte Carlo Tree Search used by AlphaGo)

### Spanning Trees

A **spanning tree** of a connected graph G is a subgraph that is a tree and includes all vertices of G. It is the "skeleton" of the graph — minimal connectivity.

Every connected graph has at least one spanning tree (and usually many).

### Minimum Spanning Trees

Given a weighted connected graph, a **minimum spanning tree (MST)** is a spanning tree with the smallest possible total edge weight.

**Kruskal's Algorithm:**
1. Sort all edges by weight (ascending)
2. Consider each edge in order. Add it to the MST if it does not create a cycle.
3. Stop when you have n - 1 edges.

*Greedy strategy:* Always pick the cheapest available edge that does not create a cycle.

**Prim's Algorithm:**
1. Start from any vertex. Add it to the MST.
2. Of all edges connecting MST vertices to non-MST vertices, pick the lightest.
3. Add that edge and its new vertex to the MST.
4. Repeat until all vertices are included.

*Greedy strategy:* Grow the tree one vertex at a time, always extending to the nearest neighbor.

Both algorithms produce correct MSTs (provably). The proof uses the **cut property**: for any partition of the vertices into two groups, the lightest edge crossing the partition must be in every MST.

**ML connection:** MST algorithms appear in clustering (single-linkage clustering is equivalent to an MST computation) and in constructing efficient network topologies.

---

## Part 4: Planarity

### Planar Graphs

A graph is **planar** if it can be drawn in the plane with no edges crossing.

**Euler's Formula for Planar Graphs:** For a connected planar graph with v vertices, e edges, and f faces (regions, including the outer unbounded region):

v - e + f = 2

**Example:** A triangle has v = 3, e = 3, f = 2 (the interior and the exterior). Check: 3 - 3 + 2 = 2.

### Kuratowski's Theorem

A graph is planar if and only if it does not contain a subdivision of K_5 or K_3,3 as a subgraph.

- **K_5:** the complete graph on 5 vertices (every pair connected)
- **K_3,3:** the complete bipartite graph with 3 vertices on each side

A **subdivision** means replacing edges with paths (inserting vertices of degree 2 along edges). The theorem says that K_5 and K_3,3 are the two "minimal obstructions" to planarity. If your graph contains either one (possibly with extra vertices along edges), it is not planar.

**Practical corollary from Euler's formula:** A planar graph with v >= 3 vertices has at most 3v - 6 edges. If your graph has more edges than this, it is definitely not planar.

### Why Planarity Matters for AI

Circuit board design, network layout, and visualization all benefit from planarity. More abstractly, many efficient graph algorithms run faster on planar graphs. Understanding whether a graph is planar tells you about the inherent complexity of the structure it represents.

---

## Part 5: Graph Coloring

### Vertex Coloring

A (proper) **vertex coloring** assigns a color to each vertex such that no two adjacent vertices share the same color.

The **chromatic number** chi(G) is the minimum number of colors needed to properly color G.

**Examples:**
- Any bipartite graph has chi = 2 (color the two sides differently)
- C_5 (the 5-cycle) has chi = 3
- K_n has chi = n (every vertex is adjacent to every other, so all need distinct colors)
- Any tree has chi = 2 (trees are bipartite)

### Greedy Coloring

The **greedy coloring algorithm:**
1. Order the vertices in some sequence v1, v2, ..., vn.
2. For each vertex in order, assign the smallest color number not used by any of its already-colored neighbors.

The greedy algorithm always uses at most Delta + 1 colors, where Delta is the maximum degree of any vertex. But depending on the vertex ordering, it might use more colors than necessary. Finding the optimal coloring (the chromatic number) is NP-hard in general.

**Brooks' Theorem:** For a connected graph that is neither a complete graph nor an odd cycle, chi(G) <= Delta (the maximum degree). This tightens the greedy bound by 1 for most graphs.

### The Four Color Theorem

Every planar graph can be properly colored with at most 4 colors. This was conjectured in 1852 and proved in 1976 — famously, it was one of the first major theorems proved with the help of a computer (checking many cases computationally). It remains a landmark example of computer-assisted proof, raising philosophical questions about what constitutes mathematical proof that resonate with today's debates about AI-generated proofs.

### Graph Coloring in AI and CS

- **Register allocation** in compilers: variables are vertices, edges indicate variables alive at the same time, colors are CPU registers.
- **Scheduling:** tasks are vertices, edges indicate conflicts, colors are time slots.
- **Frequency assignment** in wireless networks: transmitters are vertices, nearby transmitters are connected, colors are frequencies.

**ML connection:** Graph neural networks (GNNs) are a family of neural network architectures that operate on graph-structured data. Understanding graph properties like coloring helps in analyzing the expressive power of GNNs — the Weisfeiler-Leman graph isomorphism test, which upper-bounds standard GNN expressiveness, is intimately connected to coloring-based graph invariants.

---

## Part 6: Applications — Graphs as the Language of Neural Networks

### Computational Graphs

Every neural network computation can be represented as a **directed acyclic graph (DAG)** where:
- Nodes represent operations (matrix multiply, add bias, apply activation)
- Edges represent data flow (tensors passing between operations)

Backpropagation is a **reverse traversal** of this graph: starting from the loss node, propagating gradients backward through each edge using the chain rule at each node. Understanding this graph structure is essential for understanding gradient flow, vanishing/exploding gradients, and the effect of architectural choices.

### Knowledge Graphs

A **knowledge graph** represents factual information as a directed labeled graph:
- Nodes are entities ("Albert Einstein", "Physics", "Germany")
- Edges are relationships ("studied", "born_in", "field_of")

AI systems that reason over knowledge graphs use graph-theoretic algorithms for path finding, subgraph matching, and link prediction. Understanding graph structure helps you understand both the capabilities and limitations of these systems.

### Causal Graphs

**Directed acyclic graphs (DAGs)** are used in causal inference to represent causal relationships. Nodes are variables, and a directed edge from A to B means "A causally influences B." Reasoning about interventions, confounders, and counterfactuals all depends on the graph structure. For alignment, causal reasoning is crucial: we want to understand not just what an AI system does, but *why* — what causal mechanisms drive its behavior.

---

## Watch — Primary

1. **Trefor Bazzett — "Discrete Math" playlist (graph theory sections)**
   - *Covers graph fundamentals, Euler/Hamilton paths, trees, planarity, and coloring with visual demonstrations*

## Read — Primary

- **"Discrete Mathematics and Its Applications" by Kenneth Rosen** — Chapters 10–11
  - *Chapter 10 covers graph fundamentals; Chapter 11 covers trees. Comprehensive with many exercises.*

## Read — Supplementary

- **"Introduction to Graph Theory" by Douglas West** — Chapters 1–5
  - *A more mathematical treatment with proofs. Good reference for deeper understanding of planarity and coloring.*

## Exercises

1. For the following graph with vertices {A, B, C, D, E} and edges {AB, AC, BC, BD, CD, DE}, determine: (a) the degree of each vertex, (b) whether the graph is connected, (c) whether it has an Euler path or circuit.

2. Prove that every tree with n >= 2 vertices has at least two leaves (vertices of degree 1). (Hint: consider the longest path.)

3. Use Kruskal's algorithm to find the MST of a graph with vertices {1, 2, 3, 4, 5} and weighted edges: {1-2: 3, 1-3: 5, 2-3: 4, 2-4: 6, 3-4: 2, 3-5: 7, 4-5: 1}. Show each step.

4. Determine whether K_5 is planar. Use Euler's formula corollary (check if e <= 3v - 6).

5. Find the chromatic number of C_6 (the 6-cycle) and C_7 (the 7-cycle). Explain the pattern for even vs. odd cycles.

6. Apply the greedy coloring algorithm to a specific graph (choose your own with 6-8 vertices). Show that different vertex orderings can give different numbers of colors.

7. Prove that a graph is bipartite if and only if it contains no odd cycles. (One direction is straightforward; for the other, consider BFS from any vertex and coloring by distance parity.)

8. Consider a neural network with 3 input nodes, one hidden layer of 4 nodes (fully connected to inputs), and 2 output nodes (fully connected to hidden layer). Draw the computational graph. How many edges (parameters) does it have? What is its depth?

9. A tournament schedule for 6 teams must be arranged so that each team plays exactly one game per round. Model this as a graph coloring problem. What is the minimum number of rounds needed?

10. (Challenge) The Petersen graph is a famous graph with 10 vertices and 15 edges where every vertex has degree 3. Show that it is not planar (use Euler's formula corollary). Determine its chromatic number. Research why this graph is a frequent counterexample in graph theory.
