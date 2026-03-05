# Lesson CS-09: Discrete Math Essentials — Logic, Counting, and Graphs

[← Recursion & DP](lesson-cs08-recursion-dp.md) | [Back to TOC](../README.md) | [Next: Computer Organization →](lesson-cs10-computer-organization.md)

---

> **Why this lesson exists:** Discrete math is the mathematical backbone of computer science — logic underpins formal verification, combinatorics tells you how many configurations a model can represent, graph theory describes neural network architectures, and modular arithmetic appears in hashing and cryptography. This is a theory-focused lesson, but with concrete applications throughout.

## 🎯 Core Concepts

### Propositional Logic

- **Propositions:** statements that are true or false. "It's raining" = T or F.
- **Operators:** AND (∧), OR (∨), NOT (¬), IMPLIES (→), IFF (↔)
- **Truth tables:** enumerate all combinations. Essential for verifying logical equivalences.
- **Key equivalences:**
  - De Morgan's Laws: ¬(A ∧ B) = ¬A ∨ ¬B, and ¬(A ∨ B) = ¬A ∧ ¬B
  - Contrapositive: (A → B) ≡ (¬B → ¬A) — always true
  - Converse: (A → B) does NOT imply (B → A)
- **Implication (→):** "if A then B" is only false when A is true and B is false. "If it rains, the ground is wet" — only broken if it rains and the ground is dry.

### Proof Techniques

- **Direct proof:** assume P, derive Q step by step.
- **Proof by contradiction:** assume ¬Q, derive a contradiction.
- **Proof by induction:** prove base case, prove "if true for n, then true for n+1."
  - **Why induction matters for CS:** it's how you prove algorithms are correct. "My loop invariant holds at step 0. If it holds at step k, it holds at step k+1. Therefore it holds for all steps."
- **Proof by contrapositive:** instead of proving A → B, prove ¬B → ¬A.

### Sets and Functions

- **Set operations:** union (∪), intersection (∩), difference (−), complement, Cartesian product (×)
- **Cardinality:** |A| = number of elements. |A ∪ B| = |A| + |B| − |A ∩ B| (inclusion-exclusion).
- **Functions:** injective (one-to-one), surjective (onto), bijective (both). A bijection means the sets have the same size.
- **Pigeonhole principle:** if n+1 items go into n boxes, at least one box has ≥ 2 items. Sounds trivial, proves powerful things.

### Combinatorics — Counting

- **Permutations (order matters):** P(n, k) = n! / (n−k)!
- **Combinations (order doesn't matter):** C(n, k) = n! / (k!(n−k)!)
- **With replacement:** n^k choices (each of k picks has n options independently).
- **Stars and bars:** distributing k identical items into n bins = C(n+k−1, k).
- **Binomial theorem:** (a + b)^n = Σ C(n,k) a^(n−k) b^k

#### Additional Combinatorial Identities and Techniques

- **Hockey stick identity:** C(r,r) + C(r+1,r) + C(r+2,r) + ... + C(n,r) = C(n+1,r+1). Visually, the entries along a diagonal of Pascal's triangle sum to the entry one row below and one position over (forming a "hockey stick" shape). Useful for summing binomial coefficients and counting cumulative combinations. Also known as the Christmas stocking identity.
- **Falling factorial (Pochhammer symbol):** x^{(n)} = x(x−1)(x−2)···(x−n+1), also written (x)_n. The number of permutations P(n,k) = n^{(k)} IS a falling factorial. Falling factorials connect permutations to polynomial expressions: C(x,n) = x^{(n)}/n!, and they are the natural basis for finite difference calculus (the discrete analog of Taylor series, where the falling factorial plays the role that x^n plays in continuous calculus). Falling factorial decomposition rewrites polynomials in terms of falling factorials, enabling clean closed-form summation identities.
- **Organizing a double sum by its larger index:** When you have a double sum Σ_{i=1}^{n} Σ_{j=1}^{n} f(i,j), you can rearrange by grouping terms according to max(i,j) = k, sweeping through k = 1 to n. Each "shell" at level k collects the L-shaped border of new (i,j) pairs where at least one index equals k. This reindexing technique simplifies many combinatorial sums and appears when analyzing nested loops, bounding series, or computing expectations of order statistics. The same idea generalizes to organizing by min(i,j) or other functions of the indices.

### Graph Theory

- **Graph:** vertices (nodes) + edges (connections). G = (V, E).
- **Directed vs undirected.** **Weighted vs unweighted.**
- **Degree:** number of edges touching a vertex. Sum of all degrees = 2|E|.
- **Path:** sequence of vertices connected by edges. **Cycle:** path that returns to start.
- **Connected:** every vertex reachable from every other (undirected). **Strongly connected** (directed).
- **Trees:** connected graph with no cycles. |E| = |V| − 1.
- **Bipartite:** vertices can be split into two groups where all edges go between groups (not within).
- **Planar:** can be drawn without edge crossings.
- **Euler's formula (planar graphs):** V − E + F = 2 (vertices, edges, faces).

### Modular Arithmetic

- a ≡ b (mod n) means n divides (a − b). Equivalently: a and b have the same remainder when divided by n.
- **(a + b) mod n = ((a mod n) + (b mod n)) mod n** — same for multiplication.
- **Applications:** hashing, cryptography, and the "grokking" phenomenon in ML (networks learning modular addition).

## 📺 Watch

1. **Trefor Bazett — Discrete Mathematics playlist** — clear, visual university lectures
2. **MIT OpenCourseWare — "Mathematics for Computer Science" (6.042)** — lecture videos (optional, very thorough)

## 📖 Read

- **"Discrete Mathematics and Its Applications" by Rosen** — the standard textbook. Reference chapters on logic (Ch. 1), counting (Ch. 6), and graphs (Ch. 10).
- **"Mathematics for Computer Science" (Lehman, Leighton, Meyer)** — free MIT textbook: https://courses.csail.mit.edu/6.042/spring18/mcs.pdf

## 🔨 Practice

1. **Truth tables:** build truth tables for (A → B) ∨ C and verify De Morgan's laws.
2. **Induction proof:** prove that 1 + 2 + ... + n = n(n+1)/2 by induction.
3. **Counting:** how many 4-digit PINs exist? How many with no repeated digits? How many with digits in increasing order?
4. **Graph problems:** given an adjacency list, implement and run DFS and BFS. Detect if the graph has a cycle. Check if it's bipartite ([Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)).
5. **Modular arithmetic:** compute 7^100 mod 13 using repeated squaring. Connect to how hashing works.
6. **Pigeonhole:** prove that in any group of 13 people, at least 2 share a birth month.

### Math & Geometry (NeetCode 150)

These problems test mathematical reasoning and matrix manipulation — skills that transfer directly to working with tensors in ML.

| # | Problem | Category | Pattern | Difficulty |
|---|---------|----------|---------|------------|
| 1 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Math & Geometry | Layer-by-layer traversal | Medium |
| 2 | [Plus One](https://leetcode.com/problems/plus-one/) | Math & Geometry | Carry propagation | Easy |
| 3 | [Multiply Strings](https://leetcode.com/problems/multiply-strings/) | Math & Geometry | Grade-school multiplication | Medium |
| 4 | [Detect Squares](https://leetcode.com/problems/detect-squares/) | Math & Geometry | Hash map + geometry | Medium |

## 🔗 ML Connection

Combinatorics tells you the size of a model's hypothesis space — how many possible functions a network with n parameters can represent. Graph theory describes neural architectures (layers = nodes, connections = edges) and knowledge graphs used in reasoning systems. Logic underpins formal verification approaches to alignment. Modular arithmetic connects to grokking — one of the most striking phenomena in modern ML, where networks suddenly learn modular addition after massive overfitting.

