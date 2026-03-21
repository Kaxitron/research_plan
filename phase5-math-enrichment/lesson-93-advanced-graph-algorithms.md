# Lesson 93: Advanced Graph Algorithms

[<-- Combinatorial Algorithms](lesson-92-combinatorial-algorithms.md) | [Back to TOC](../README.md) | [Next: Lower Bounds and Amortized Analysis -->](lesson-94-lower-bounds-amortized.md)

---

> **Why this lesson exists:** Graphs are the natural language for describing relationships -- between neurons in a network, agents in a multi-agent system, or concepts in a knowledge graph. Advanced graph algorithms underpin many core AI techniques: spectral clustering partitions data using graph Laplacians, flow-based generative models (normalizing flows) draw on network flow theory, graph neural networks propagate information through message passing on graph structures, and matching algorithms assign tasks to agents in cooperative AI settings. Mastering these algorithms gives you the structural vocabulary to reason about alignment architectures and multi-agent coordination.

> **Estimated time:** 18--24 hours

---

## Part 1: Maximum Matching

### Bipartite Matching: Hopcroft-Karp Algorithm

A *matching* in a graph is a set of edges with no shared vertices. A *maximum matching* has the largest possible number of edges. In bipartite graphs, this problem has efficient solutions.

**Augmenting paths.** Given a matching M, an *augmenting path* is a path that alternates between unmatched and matched edges, starting and ending at unmatched vertices. By Berge's theorem, a matching M is maximum if and only if no augmenting path exists.

**The naive approach** (Hungarian algorithm variant): find augmenting paths one at a time using BFS/DFS. Each augmentation increases the matching size by 1. Finding one augmenting path takes O(E) time, and we need at most V/2 augmentations, giving O(VE) total.

**Hopcroft-Karp improvement:** Find *multiple* augmenting paths simultaneously. In each phase:

1. Use BFS from all free (unmatched) vertices in the left partition to find the shortest augmenting paths (all paths of the same minimum length).
2. Use DFS to find a maximal set of vertex-disjoint shortest augmenting paths.
3. Augment along all of them simultaneously.

The key insight: after i phases, the shortest remaining augmenting path has length >= 2i + 1. Since augmenting paths have length at most V, at most O(sqrt(V)) phases are needed. Each phase takes O(E) time.

**Total time: O(E * sqrt(V)).**

**Konig's theorem** (a beautiful duality): In a bipartite graph, the size of the maximum matching equals the size of the minimum vertex cover. This is the LP relaxation of vertex cover being integral for bipartite graphs -- a consequence of total unimodularity.

### General Matching: Edmonds' Blossom Algorithm

For non-bipartite graphs, augmenting path search is complicated by *odd cycles*. Consider a cycle of length 2k+1 in which k edges are in the matching. An augmenting path might enter the cycle at one vertex and need to exit at the one unmatched vertex, but the direction of traversal matters.

Edmonds' insight: *contract* each odd cycle (a "blossom") into a single vertex, find augmenting paths in the contracted graph, then expand blossoms to recover the actual path.

```
EDMONDS_BLOSSOM:
1. Start with any matching M (possibly empty).
2. While there exists an augmenting path:
   a. Build alternating trees from free vertices (using BFS).
   b. If an odd cycle is detected (two even-level vertices are adjacent):
      Contract the cycle into a single vertex (a blossom).
      Continue searching in the contracted graph.
   c. If an augmenting path is found, augment M along it.
   d. Expand all blossoms to recover the matching in the original graph.
```

**Time complexity:** O(V^2 * E) for the basic version; O(V^3) with careful implementation (Gabow); O(V^{1/2} * E) with the Micali-Vazirani algorithm.

**Tutte's theorem:** A graph G has a perfect matching if and only if for every subset S of vertices, the number of odd components in G - S is at most |S|. This is the non-bipartite analog of Hall's theorem.

---

## Part 2: Planarity

### Kuratowski's Theorem

A graph is *planar* if it can be drawn in the plane without edge crossings. Kuratowski's theorem (1930) characterizes planar graphs:

**Theorem:** A graph is planar if and only if it contains no subdivision of K_5 (complete graph on 5 vertices) or K_{3,3} (complete bipartite graph with parts of size 3).

Equivalently (Wagner's theorem): a graph is planar if and only if it has no K_5 or K_{3,3} *minor*.

### Euler's Formula and Consequences

For a connected planar graph with V vertices, E edges, and F faces: V - E + F = 2.

**Corollaries:**
- E <= 3V - 6 (for V >= 3). A planar graph is sparse.
- Every planar graph has a vertex of degree at most 5.
- K_5 is not planar: it has 10 edges but 3 * 5 - 6 = 9.
- K_{3,3} is not planar: it has 9 edges but (using the bipartite variant E <= 2V - 4) only allows 8.

### Planarity Testing Algorithms

Testing whether a graph is planar can be done in *linear time* O(V + E).

**Hopcroft-Tarjan algorithm (1974):** Based on depth-first search. The DFS tree divides edges into tree edges and back edges. For each back edge, there is a cycle. The algorithm checks whether these cycles can be consistently embedded on both sides of the DFS tree path.

**Boyer-Myrvold algorithm (2004):** A more practical linear-time planarity testing algorithm. It processes vertices in reverse DFS order, maintaining a representation of the partially embedded graph. When processing a vertex, it checks whether its DFS subtree can be embedded consistently with the edges going to already-processed ancestors.

**The Kuratowski subgraph extraction:** When the graph is not planar, these algorithms can output a Kuratowski subdivision (a subgraph homeomorphic to K_5 or K_{3,3}) as a certificate of non-planarity.

### Why Planarity Matters

Planar graphs admit:
- O(V)-time separator theorems: every planar graph has a separator of size O(sqrt(V)) whose removal disconnects the graph into roughly equal pieces (Lipton-Tarjan separator theorem).
- Efficient algorithms for problems that are NP-hard on general graphs (e.g., maximum independent set on planar graphs via the separator approach).
- Connections to surface topology and the graph minor theorem (Robertson-Seymour).

---

## Part 3: Network Flow

### The Maximum Flow Problem

Given a directed graph G = (V, E) with source s, sink t, and capacity function c: E -> R_+, find a flow f: E -> R_+ maximizing the total flow from s to t, subject to:
- **Capacity constraint:** 0 <= f(u, v) <= c(u, v) for all (u, v) in E.
- **Flow conservation:** For all v != s, t: sum of flow into v = sum of flow out of v.

### Residual Graph and Augmenting Paths

The *residual graph* G_f has edges:
- Forward edge (u, v) with residual capacity c(u, v) - f(u, v) if this is positive.
- Backward edge (v, u) with residual capacity f(u, v) if this is positive.

An *augmenting path* is an s-t path in the residual graph. The *bottleneck* is the minimum residual capacity along the path.

### Ford-Fulkerson Method

```
FORD_FULKERSON(G, s, t, c):
  Initialize f(u,v) = 0 for all (u,v).
  While there exists an augmenting path p in the residual graph G_f:
    Let delta = min residual capacity along p.
    For each edge (u,v) on p:
      If (u,v) is a forward edge: f(u,v) += delta.
      If (u,v) is a backward edge: f(v,u) -= delta.
  Return f.
```

**Termination:** With integer capacities, each augmentation increases the flow by at least 1, so the method terminates in at most |f*| iterations (where f* is the max flow value). With irrational capacities, Ford-Fulkerson may not terminate.

**Time complexity:** O(E * |f*|) -- pseudopolynomial in the max flow value.

### Edmonds-Karp Algorithm (BFS Augmentation)

Choose the augmenting path using BFS (shortest path in terms of number of edges).

**Key theorem:** The shortest augmenting path length is monotonically non-decreasing over successive augmentations. Moreover, each path length value is used for at most O(V * E) augmentations total.

Since the shortest path length is at most V, the total number of augmentations is O(VE), each taking O(E) time for the BFS.

**Total time: O(V * E^2).**

### Dinic's Algorithm

An improvement over Edmonds-Karp that finds *blocking flows* in layered graphs.

1. Construct the *layered graph* L from BFS in the residual graph (only edges going from layer i to layer i+1).
2. Find a *blocking flow* in L: a flow such that every s-t path in L has at least one saturated edge.
3. Add the blocking flow to the current flow.
4. Repeat until no s-t path exists in the residual graph.

**Key facts:**
- The number of phases is at most O(V) (the layered graph depth increases by at least 1 per phase).
- A blocking flow in a layered graph can be found in O(VE) time using DFS with retreat.

**Total time: O(V^2 * E).**

For unit-capacity graphs: O(E * sqrt(V)). For graphs from bipartite matching: recovers Hopcroft-Karp's O(E * sqrt(V)).

### Max-Flow Min-Cut Theorem

**Theorem (Ford-Fulkerson, 1956):** The maximum flow value from s to t equals the minimum capacity of an s-t cut.

An *s-t cut* (S, T) is a partition of V with s in S and t in T. Its capacity is sum of c(u,v) for edges (u,v) with u in S and v in T.

**Proof sketch:** (1) Any flow is at most the capacity of any cut (flow cannot exceed the bottleneck). (2) When Ford-Fulkerson terminates, define S = vertices reachable from s in the residual graph. Then (S, V-S) is a cut with capacity equal to the current flow value.

**LP duality perspective:** Max-flow is a linear program. Its dual is the minimum cut problem. The max-flow min-cut theorem is a special case of strong LP duality. The integrality of max-flow when capacities are integers follows from the total unimodularity of the constraint matrix.

### Applications of Network Flow

**Bipartite matching via flow:** Add source s connected to all left vertices, sink t connected to all right vertices, all capacities 1. Max flow = maximum matching size.

**Project selection (maximum weight closure):** Given a directed graph with weights on vertices (positive = profit, negative = cost), find the subset S of vertices maximizing total weight, subject to: if u in S and (u,v) is an edge, then v in S. This reduces to min-cut: create source s connected to positive-weight vertices, sink t connected from negative-weight vertices, original edges get infinite capacity.

**Image segmentation:** Each pixel is a vertex. Source represents "foreground," sink represents "background." Edge capacities encode pixel similarity and data-term preferences. Min-cut gives the optimal binary segmentation.

---

## Part 4: Algebraic Graph Theory

### The Adjacency Matrix and Its Spectrum

For a graph G with n vertices, the adjacency matrix A is n x n with A_{ij} = 1 if (i,j) is an edge, 0 otherwise. The eigenvalues lambda_1 >= lambda_2 >= ... >= lambda_n form the *spectrum* of G.

**Key properties:**
- sum of eigenvalues = trace(A) = 0 (no self-loops).
- sum of lambda_i^2 = trace(A^2) = 2|E| (counts walks of length 2).
- More generally, trace(A^k) = number of closed walks of length k.
- The largest eigenvalue lambda_1 satisfies d_avg <= lambda_1 <= d_max (between average and maximum degree).

### The Graph Laplacian

The *combinatorial Laplacian* is L = D - A, where D = diag(d_1, ..., d_n) is the degree matrix.

The *normalized Laplacian* is L_norm = D^{-1/2} L D^{-1/2} = I - D^{-1/2} A D^{-1/2}.

**Properties of L:**
- L is positive semidefinite: x^T L x = sum_{(i,j) in E} (x_i - x_j)^2 >= 0.
- The smallest eigenvalue is 0, with eigenvector [1, 1, ..., 1].
- The multiplicity of eigenvalue 0 equals the number of connected components.
- The second-smallest eigenvalue lambda_2 (the *algebraic connectivity* or *Fiedler value*) measures how well-connected the graph is.

### Cheeger's Inequality

Cheeger's inequality connects the spectral gap to the combinatorial notion of expansion.

The *Cheeger constant* (conductance) of G is:

h(G) = min_{S: 0 < |S| <= n/2} |E(S, V-S)| / |S|

where E(S, V-S) is the set of edges between S and V - S.

**Cheeger's inequality (discrete version):**

lambda_2 / 2 <= h(G) <= sqrt(2 * lambda_2)

This says: the graph is an expander (h(G) is large) if and only if the spectral gap (lambda_2) is large. Expanders are fundamental in theoretical computer science (derandomization, error-correcting codes, communication networks).

### Spectral Clustering

The spectral perspective leads directly to spectral clustering:

1. Construct a similarity graph (k-nearest neighbors or epsilon-neighborhood).
2. Compute the Laplacian L (or normalized Laplacian).
3. Find the k smallest eigenvectors of L.
4. Use these eigenvectors as coordinates for each vertex.
5. Apply k-means clustering in this spectral embedding.

**Why it works:** The eigenvectors of L embed the graph into R^k such that well-connected clusters are mapped to nearby points. The Fiedler vector (eigenvector of lambda_2) gives the optimal 2-way partition in a relaxed sense -- it minimizes the ratio cut (or normalized cut for the normalized Laplacian).

**The relaxation perspective:** Minimizing the normalized cut is NP-hard. The spectral relaxation replaces the discrete constraint (indicator vector) with a continuous constraint (unit eigenvector), yielding the Laplacian eigenvalue problem. This is a special case of the general technique of relaxing combinatorial optimization problems to continuous ones.

---

## Watch -- Primary

- **WilliamFiset** -- "Network Flow" playlist (Ford-Fulkerson, Edmonds-Karp, Dinic's algorithm with clear visualizations and code walkthroughs)
- **MIT 6.046J** -- "Network Flow I & II" (Erik Demaine lectures covering max-flow min-cut theorem and applications)
- **Reducible** -- "Graph Theory" videos (matching, planarity concepts)

---

## Read -- Primary

- **CLRS** -- Chapter 26 (Maximum Flow): covers Ford-Fulkerson, Edmonds-Karp, and the max-flow min-cut theorem with rigorous proofs.
- **Lovasz, "Matching Theory"** (or Schrijver, "Combinatorial Optimization") -- For deeper coverage of matching theory, including Edmonds' blossom algorithm and the Tutte matrix.
- **Chung, "Spectral Graph Theory"** -- The standard reference for graph Laplacians, Cheeger's inequality, and spectral methods. Chapters 1-3 cover the essentials.
- **von Luxburg, "A Tutorial on Spectral Clustering"** (2007) -- An excellent bridge between algebraic graph theory and machine learning applications.

---

## Exercises

1. **Hopcroft-Karp trace.** Given the bipartite graph with left vertices {a, b, c, d}, right vertices {1, 2, 3, 4}, and edges {(a,1), (a,2), (b,1), (b,3), (c,2), (c,3), (d,3), (d,4)}, trace the Hopcroft-Karp algorithm. Show the matching after each phase and the augmenting paths found.

2. **Max-flow by hand.** Consider the network: s -> a (cap 10), s -> b (cap 10), a -> b (cap 2), a -> c (cap 8), a -> d (cap 4), b -> d (cap 9), c -> t (cap 10), d -> t (cap 6). Find the maximum flow using Edmonds-Karp (BFS augmentation). Show each augmenting path and the residual graph after each augmentation. Identify the min-cut.

3. **Max-flow min-cut proof.** Prove the max-flow min-cut theorem formally: show that when Ford-Fulkerson terminates, the set S of vertices reachable from s in the residual graph defines a min-cut of capacity equal to the flow value.

4. **Project selection.** A company has five projects with profits [8, -3, 5, -2, 4] and dependencies: project 1 requires project 2, project 3 requires project 2 and project 4. Formulate as a max-flow/min-cut problem and find the optimal subset of projects to undertake.

5. **Laplacian computation.** For the Petersen graph, compute the Laplacian matrix, find its eigenvalues, and verify that the multiplicity of 0 equals 1 (since the graph is connected). Compute the Cheeger constant and verify Cheeger's inequality.

6. **Spectral clustering.** Generate a synthetic dataset with three clusters in R^2 arranged in a non-convex shape (e.g., nested crescents). Show that k-means fails but spectral clustering succeeds. Explain why in terms of the graph Laplacian eigenvectors.

7. **Flow-based generative models.** Normalizing flows in ML transform a simple distribution (Gaussian) into a complex one through a sequence of invertible transformations. Explain the connection to network flow theory: in what sense is the transformation a "flow"? What role does the change-of-variables formula (the Jacobian determinant) play, and how does it relate to capacity constraints?
