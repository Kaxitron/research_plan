# Lesson 92: Combinatorial Algorithms

[<-- Randomized Algorithms](lesson-91-randomized-algorithms.md) | [Back to TOC](../README.md) | [Next: Advanced Graph Algorithms -->](lesson-93-advanced-graph-algorithms.md)

---

> **Why this lesson exists:** AI alignment research frequently involves searching through combinatorial spaces: the space of possible reward functions, the space of neural network architectures, the space of logical formulas representing safety specifications. Naive enumeration of these spaces is infeasible, but structured enumeration -- exploiting symmetry, ordering, and pruning -- can make intractable problems tractable. This lesson develops the algorithmic machinery for systematic generation of combinatorial objects and for navigating combinatorial search spaces efficiently, skills directly applicable to architecture search, interpretability (enumerating circuit subgraphs), and formal verification of alignment properties.

> **Estimated time:** 15--20 hours

---

## Part 1: Systematic Enumeration of Permutations

### Lexicographic Order and Knuth's Algorithm L

The most natural ordering of permutations is *lexicographic*: treat each permutation as a number and list them in increasing order. For {1, 2, 3}: 123, 132, 213, 231, 312, 321.

**Knuth's Algorithm L** generates the next permutation in lexicographic order in O(n) worst case and O(1) amortized:

```
ALGORITHM L (Next permutation in lexicographic order)
Input: permutation a[0..n-1]
Output: next permutation, or signal that current is the last

L1. [Find rightmost ascent] Find the largest index j such that a[j] < a[j+1].
    If no such j exists, the permutation is the last (fully descending). Terminate.

L2. [Find rightmost successor] Find the largest index l > j such that a[j] < a[l].

L3. [Swap] Swap a[j] and a[l].

L4. [Reverse suffix] Reverse the subsequence a[j+1..n-1].
```

**Why it works:** After position j, the suffix a[j+1..n-1] is in descending order (otherwise j would not be the rightmost ascent). To get the next permutation, we need the smallest element larger than a[j] from the suffix -- that is a[l]. After swapping, the suffix is still descending, so reversing it gives the smallest possible suffix.

**Amortized analysis:** Most calls only modify the last few elements. On average, Algorithm L performs about e - 1 ~ 1.718 element assignments per call (a result derivable via generating functions).

### Heap's Algorithm

Heap's algorithm generates all permutations by performing a single swap per permutation. It is not lexicographic but is useful when the *order* of enumeration does not matter and minimal change between successive permutations is desired.

```
HEAP(n, A):
  If n = 1:
    output A
    return
  For i = 0 to n-1:
    HEAP(n-1, A)
    If n is even:
      swap A[i] and A[n-1]
    Else:
      swap A[0] and A[n-1]
```

Each call to HEAP(n, A) generates all n! permutations of A[0..n-1]. The key property: between consecutive outputs, exactly one swap occurs. This makes Heap's algorithm a *minimal change* listing.

### Steinhaus-Johnson-Trotter Algorithm

An alternative minimal-change algorithm that generates permutations such that consecutive permutations differ by a swap of *adjacent* elements. This is related to the concept of permutation graphs and the *inversion table* representation.

Each element has a *direction* (left or right). At each step, find the largest *mobile* element (one whose neighbor in its direction is smaller) and swap it with that neighbor. Then reverse the direction of all elements larger than the one just moved.

This generates the permutations in a Hamilton path on the *permutohedron* -- the graph whose vertices are permutations and edges connect permutations differing by an adjacent transposition.

---

## Part 2: Generating Combinations and Subsets

### Binary Counting

The simplest method for generating all subsets of {1, ..., n}: iterate integers from 0 to 2^n - 1, interpreting each integer's binary representation as a characteristic vector. Bit j is 1 if element j is in the subset.

This is O(1) amortized per subset (just increment a counter).

### Revolving Door Algorithm (Combinations in Minimal Change Order)

To generate all C(n, k) combinations of k elements from n, the *revolving door* algorithm produces a listing where consecutive combinations differ by removing one element and adding another (a "one-in, one-out" change, like a revolving door).

This is a Hamilton path on the *Johnson graph* J(n, k), where vertices are k-subsets and edges connect subsets differing in exactly one element.

Knuth describes this as Algorithm R in TAOCP 4A. The key insight is a recursive construction: to list all k-subsets of {1, ..., n} in revolving-door order:
1. List all k-subsets of {1, ..., n-1} (element n absent)
2. Transition: add element n while removing one element
3. List all (k-1)-subsets of {1, ..., n-1} in *reverse* revolving-door order, each augmented with element n

The transition between phases requires careful bookkeeping to maintain the minimal-change property.

### Gray Codes for Subsets

A *Gray code* is an ordering of all 2^n binary strings such that successive strings differ in exactly one bit.

**Reflected Gray code construction:**
- For n = 1: {0, 1}
- For n = k: Take the Gray code for k-1. Write it forwards, prefixed with 0. Then write it backwards, prefixed with 1.

The n-bit reflected Gray code: G(0) = 0, and for i > 0, G(i) = i XOR (i >> 1).

**To find which bit changes between G(i) and G(i+1):** It is the position of the lowest set bit of i+1 (i.e., the ruler function / 2-adic valuation of i+1).

**Applications:**
- **Error correction in analog-to-digital converters:** Adjacent positions on a rotating encoder wheel differ by one bit, so a small misalignment causes at most a 1-bit error.
- **Karnaugh maps:** Used in digital circuit minimization.
- **Combinatorial generation:** Gray codes provide a framework for minimal-change listings of many combinatorial objects.

---

## Part 3: Generating Partitions

### Integer Partitions

A partition of n is a way to write n as a sum of positive integers, where order does not matter. For n = 5: {5}, {4+1}, {3+2}, {3+1+1}, {2+2+1}, {2+1+1+1}, {1+1+1+1+1}. There are p(5) = 7 partitions.

The partition function p(n) grows like exp(pi * sqrt(2n/3)) / (4n * sqrt(3)) (Hardy-Ramanujan asymptotic formula). This super-polynomial but sub-exponential growth means enumeration is feasible for moderate n but becomes intractable for large n.

**Algorithm for generating partitions in reverse lexicographic order:**

```
Start with the partition [n] (a single part equal to n).
Repeat:
  Let the current partition be a[1] >= a[2] >= ... >= a[k].
  Find the rightmost part a[j] > 1.
  Replace a[j] by a[j] - 1.
  Redistribute: set the remaining sum (originally a[j+1] + ... + a[k] + 1)
    into parts each equal to min(a[j] - 1, remaining).
  Output the new partition.
Until the partition is [1, 1, ..., 1].
```

### Set Partitions

A set partition of {1, ..., n} divides the set into non-empty, pairwise disjoint blocks whose union is {1, ..., n}. The number of set partitions is the Bell number B(n).

Bell numbers grow faster than partition numbers: B(n) ~ (n / (W(n)))^n * e^{n/W(n) - n - 1} / sqrt(W(n)), where W is the Lambert W function.

Set partitions can be generated via *restricted growth strings* (RGS): a string a_1 a_2 ... a_n where a_1 = 0 and a_{i+1} <= 1 + max(a_1, ..., a_i). Element i belongs to block a_i. The lexicographic ordering of RGS strings gives a natural enumeration.

---

## Part 4: De Bruijn Sequences

A *De Bruijn sequence* B(k, n) is a cyclic sequence over an alphabet of size k in which every possible string of length n appears exactly once as a contiguous substring. The sequence has length k^n.

**Example:** B(2, 3) = 00010111 (length 8). Reading windows of size 3: 000, 001, 010, 101, 011, 111, 110, 100 -- all eight binary strings of length 3.

**Construction via Eulerian circuits:** Build a De Bruijn graph where vertices are all (n-1)-length strings and there is a directed edge from string s to string t if the last n-2 characters of s equal the first n-2 characters of t. A De Bruijn sequence corresponds to an Eulerian circuit in this graph.

Since every vertex has in-degree = out-degree = k, an Eulerian circuit exists (by the BEST theorem, the number of such circuits can be computed via a determinant formula).

**Martin's algorithm** gives a simple O(1)-amortized method per symbol:

```
For i = 0 to k^n - 1:
  Output the "necklace successor" of the current string.
```

This leverages the connection between De Bruijn sequences and *necklaces* (equivalence classes of strings under cyclic rotation).

**Applications:** De Bruijn sequences appear in DNA sequencing (shotgun assembly), pseudo-random number generation, and robot localization (encoding positions on a track with a single binary sensor).

---

## Part 5: Backtracking with Pruning

### The General Framework

Backtracking explores a search tree implicitly. At each node, we have a partial solution. We extend it by one element, check feasibility, and recurse. If the partial solution cannot lead to a valid complete solution, we *prune* the branch.

```
BACKTRACK(partial_solution):
  If partial_solution is complete:
    process(partial_solution)
    return
  For each candidate extension c:
    If is_feasible(partial_solution + c):
      BACKTRACK(partial_solution + c)
```

The efficiency of backtracking depends entirely on the quality of the pruning function `is_feasible`. Good pruning can reduce exponential search spaces to polynomial effective search spaces.

### Constraint Satisfaction Problems (CSPs)

A CSP consists of variables V_1, ..., V_n, domains D_1, ..., D_n, and constraints C_1, ..., C_m. The goal is to assign values to variables satisfying all constraints.

**Pruning strategies for CSPs:**

1. **Forward checking:** When assigning a value to V_i, remove inconsistent values from the domains of unassigned variables. If any domain becomes empty, backtrack.

2. **Arc consistency (AC-3):** Maintain arc consistency: for every constraint between V_i and V_j, every value in D_i has a compatible value in D_j. Propagate constraints until a fixed point is reached.

3. **Variable ordering heuristics:** Choose the variable with the smallest remaining domain (MRV -- Minimum Remaining Values). This fails early.

4. **Value ordering heuristics:** Choose the value that rules out the fewest options for other variables (least constraining value).

### Branch and Bound

For optimization problems, branch-and-bound augments backtracking with a *bounding function* that estimates the best possible objective value achievable from a partial solution.

```
BRANCH_AND_BOUND(partial_solution, best_so_far):
  If partial_solution is complete:
    If objective(partial_solution) < best_so_far:
      best_so_far = objective(partial_solution)
    return
  If lower_bound(partial_solution) >= best_so_far:
    return  // prune: cannot improve
  For each candidate extension c:
    BRANCH_AND_BOUND(partial_solution + c, best_so_far)
```

The quality of the lower bound determines effectiveness. A tight lower bound prunes more aggressively. Common sources of lower bounds: LP relaxation, Lagrangian relaxation, combinatorial arguments.

---

## Part 6: Combinatorial Optimization

### Traveling Salesman Problem (TSP) Heuristics

The TSP asks for the shortest tour visiting all n cities exactly once. It is NP-hard, but good heuristics find near-optimal solutions.

**Nearest neighbor:** Start at a city, repeatedly visit the nearest unvisited city. Produces tours within a factor of O(log n) of optimal in the worst case, but often much better in practice. Running time: O(n^2).

**2-opt local search:** Start with any tour. Repeatedly find two edges whose removal and reconnection (in the other possible way) shortens the tour. A tour is *2-optimal* when no 2-opt improvement exists. Time per improvement check: O(n^2). Number of improvements: O(n^2) in practice, though worst-case exponential.

**Lin-Kernighan heuristic:** A sophisticated variable-depth search that generalizes 2-opt and 3-opt. At each step, it considers a sequence of edge swaps, choosing greedily at each level, and commits to the sequence that gives the best improvement. The LKH implementation by Helsgott is one of the most effective TSP heuristics known, consistently finding solutions within 1% of optimal on instances with millions of cities.

**Christofides' algorithm:** The best known polynomial-time approximation: find a minimum spanning tree, find a minimum-weight perfect matching on the odd-degree vertices, combine to form an Eulerian graph, extract a Hamiltonian tour by shortcutting. Guaranteed within factor 3/2 of optimal.

### Local Search and Neighborhoods

The general local search framework:
1. Start with a feasible solution.
2. Define a *neighborhood* N(s) for each solution s.
3. Move to a neighbor s' in N(s) with better objective value.
4. Repeat until no improving neighbor exists (local optimum).

The structure of the neighborhood determines the landscape. Larger neighborhoods give better local optima but take longer to search. The challenge is balancing neighborhood size with search efficiency.

---

## Part 7: Connections to AI Alignment

### Neural Architecture Search as Combinatorial Problem

Neural architecture search (NAS) explores a combinatorial space of architectures: choices of layer types, widths, connections, activation functions. The search space for a network with L layers and K possible operations per layer has K^L candidate architectures.

Effective NAS methods use ideas from this lesson:
- **Systematic enumeration** with pruning (early stopping of unpromising architectures)
- **Local search** in architecture space (mutating one component at a time)
- **Branch and bound** with performance predictors as bounding functions

### Interpretability and Circuit Enumeration

Mechanistic interpretability seeks to identify *circuits* -- subgraphs of a neural network responsible for specific behaviors. Enumerating candidate circuits is a combinatorial problem: for a network with n nodes and m edges, there are 2^m possible subgraphs. Systematic enumeration with pruning (e.g., only considering connected subgraphs, or subgraphs whose ablation affects output) makes this tractable.

### Formal Verification

Verifying safety properties of neural networks often reduces to constraint satisfaction: does there exist an input in some region that causes an unsafe output? SAT solvers and SMT solvers, which use sophisticated backtracking with pruning (DPLL, CDCL), are the backbone of these verification approaches.

---

## Watch -- Primary

- **Reducible** -- "Generating Permutations" (visual walkthrough of Algorithm L and Heap's algorithm)
- **Numberphile** -- "Gray Codes" (intuitive introduction to Gray codes and their applications)
- **Computerphile** -- "Backtracking" (general backtracking framework with N-Queens example)

---

## Read -- Primary

- **Knuth, "The Art of Computer Programming, Volume 4A: Combinatorial Algorithms, Part 1"** -- Sections 7.2.1.1 (generating permutations), 7.2.1.2 (generating combinations), 7.2.1.3 (generating partitions), 7.2.1.5 (Gray codes). This is the definitive reference. Dense but extraordinarily thorough.
- **Kreher and Stinson, "Combinatorial Algorithms: Generation, Enumeration, and Search"** -- A more accessible treatment covering systematic generation of permutations, combinations, partitions, and subsets with complete pseudocode.
- **Papadimitriou and Steiglitz, "Combinatorial Optimization"** -- Chapters on branch-and-bound, local search, and the TSP. Good for the optimization perspective.

---

## Exercises

1. **Algorithm L by hand.** Starting from the permutation [2, 4, 3, 1], apply Algorithm L to generate the next 5 permutations in lexicographic order. Verify your answers against the complete listing of permutations of {1, 2, 3, 4}.

2. **Gray code properties.** Prove that the reflected Gray code G(i) = i XOR (i >> 1) has the property that G(i) and G(i+1) differ in exactly one bit for all i. Identify which bit changes as a function of i.

3. **Partition enumeration.** Write pseudocode to generate all partitions of n = 8 in reverse lexicographic order. Count the number of partitions and verify against the known value p(8) = 22.

4. **De Bruijn sequence.** Construct B(2, 4) by finding an Eulerian circuit in the appropriate De Bruijn graph. Verify that all 16 binary strings of length 4 appear as substrings.

5. **Backtracking with pruning.** Implement a backtracking solver for the N-Queens problem. Measure the number of nodes explored for n = 8, 10, 12, 14 with and without forward checking. Quantify the pruning ratio.

6. **2-opt implementation.** Implement the 2-opt heuristic for TSP on random point sets of size 50, 100, 200 in the unit square. Measure the average improvement ratio over the nearest-neighbor starting tour. Compare the number of improvement steps to n^2.

7. **Alignment application.** Suppose you are searching for the minimal circuit in a neural network that implements a specific behavior. The network has 100 nodes. Describe how you would use backtracking with pruning to enumerate candidate circuits, specifying your feasibility check and pruning criterion. Estimate the effective search space size if your pruning eliminates 99% of branches at each level.
