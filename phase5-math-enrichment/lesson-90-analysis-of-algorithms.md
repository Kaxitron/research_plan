# Lesson 90: Analysis of Algorithms

[<-- Algebraic Geometry](lesson-89-algebraic-geometry.md) | [Back to TOC](../README.md) | [Next: Randomized Algorithms -->](lesson-91-randomized-algorithms.md)

---

> **Why this lesson exists:** Every AI alignment technique has a computational cost. When we design interpretability tools, train oversight systems, or run scalable alignment experiments, we must know *precisely* how resource consumption grows with problem size. Sloppy asymptotic reasoning leads to alignment approaches that work on toy models but collapse at frontier scale. This lesson builds the mathematical machinery -- generating functions, precise recurrence solutions, amortized cost accounting -- needed to rigorously analyze whether a proposed alignment technique is computationally viable before committing GPU-years to it.

> **Estimated time:** 18--24 hours

---

## Part 1: Asymptotic Notation Revisited

### Precise Definitions via Limits

Most introductory courses treat asymptotic notation as a shorthand for "roughly how fast a function grows." We need the full analytic definitions.

**Big-O (upper bound).** We say f(n) = O(g(n)) if there exist constants c > 0 and n_0 such that for all n >= n_0, f(n) <= c * g(n). Equivalently, lim sup_{n -> infinity} |f(n)/g(n)| < infinity.

**Big-Omega (lower bound).** We say f(n) = Omega(g(n)) if there exist constants c > 0 and n_0 such that for all n >= n_0, f(n) >= c * g(n). Equivalently, lim inf_{n -> infinity} |f(n)/g(n)| > 0.

**Big-Theta (tight bound).** f(n) = Theta(g(n)) if and only if f(n) = O(g(n)) and f(n) = Omega(g(n)). When the limit exists, this is equivalent to 0 < lim_{n -> infinity} |f(n)/g(n)| < infinity.

**Little-o (strict upper bound).** f(n) = o(g(n)) means lim_{n -> infinity} f(n)/g(n) = 0. This is strictly stronger than Big-O: f grows strictly slower than g. For example, n = o(n log n) but n log n is not o(n log n).

**Little-omega (strict lower bound).** f(n) = omega(g(n)) means lim_{n -> infinity} f(n)/g(n) = infinity. The mirror of little-o.

### The Algebra of Asymptotic Notation

These notations obey useful algebraic rules:

- **Transitivity:** If f = O(g) and g = O(h), then f = O(h). Same for Omega, Theta, o, omega.
- **Sum rule:** O(f) + O(g) = O(max(f, g)). When analyzing sequential composition, the dominant term wins.
- **Product rule:** O(f) * O(g) = O(f * g). Nested loops multiply.
- **Limit test for Big-Theta:** If lim_{n -> infinity} f(n)/g(n) = c for some 0 < c < infinity, then f = Theta(g).

### Common Pitfalls

Be careful with the following:

1. **Big-O is not symmetric.** f = O(g) does not imply g = O(f).
2. **Equality is misleading.** The "=" in f(n) = O(g(n)) is *set membership*, not equality. More precisely, f belongs to the set O(g).
3. **Constants matter in practice.** Two algorithms both O(n log n) can differ by a factor of 1000 in real performance. Asymptotic analysis tells you the *shape* of growth, not the absolute speed.
4. **Amortized vs worst-case.** An operation with O(n) worst case might be O(1) amortized. These are fundamentally different claims.

---

## Part 2: Solving Recurrences

### The Master Theorem

Many divide-and-conquer algorithms produce recurrences of the form T(n) = a * T(n/b) + f(n), where a >= 1 and b > 1.

The master theorem identifies three cases. Let c_crit = log_b(a).

**Case 1:** If f(n) = O(n^{c_crit - epsilon}) for some epsilon > 0, then T(n) = Theta(n^{c_crit}). The work at the leaves dominates.

**Case 2:** If f(n) = Theta(n^{c_crit} * (log n)^k) for some k >= 0, then T(n) = Theta(n^{c_crit} * (log n)^{k+1}). The work is evenly distributed across levels.

**Case 3:** If f(n) = Omega(n^{c_crit + epsilon}) for some epsilon > 0 and a * f(n/b) <= c * f(n) for some c < 1 (regularity condition), then T(n) = Theta(f(n)). The work at the root dominates.

**Example: Merge sort.** T(n) = 2T(n/2) + Theta(n). Here a = 2, b = 2, c_crit = 1, and f(n) = Theta(n) = Theta(n^{c_crit}). This is Case 2 with k = 0, giving T(n) = Theta(n log n).

**Example: Strassen's matrix multiplication.** T(n) = 7T(n/2) + Theta(n^2). Here a = 7, b = 2, c_crit = log_2(7) ~ 2.807. Since f(n) = Theta(n^2) = O(n^{2.807 - 0.8}), Case 1 applies: T(n) = Theta(n^{log_2 7}).

### The Akra-Bazzi Theorem

The master theorem fails when subproblems have unequal sizes. The Akra-Bazzi theorem handles recurrences of the form:

T(n) = sum_{i=1}^{k} a_i * T(b_i * n) + g(n)

where a_i > 0 and 0 < b_i < 1. Find p such that sum_{i=1}^{k} a_i * b_i^p = 1. Then:

T(n) = Theta(n^p * (1 + integral from 1 to n of g(u) / u^{p+1} du))

This is strictly more general than the master theorem. It handles cases like T(n) = T(n/3) + T(2n/3) + O(n), which arises in the analysis of randomized quicksort's worst partition. Here a_1 = a_2 = 1, b_1 = 1/3, b_2 = 2/3. We solve (1/3)^p + (2/3)^p = 1, which gives p = 1. The integral of n/u^2 from 1 to n is Theta(log n), so T(n) = Theta(n log n).

### The Recursion Tree Method

When theorems do not directly apply, draw the recursion tree:

1. The root represents the non-recursive cost f(n).
2. Each node spawns a children, each on a problem of size n/b.
3. The tree has depth log_b(n).
4. Sum the costs level by level. Level j has a^j nodes, each costing f(n/b^j).
5. Total cost = sum_{j=0}^{log_b n} a^j * f(n/b^j).

This sum is a geometric-like series. Depending on the ratio a * f(n/b) / f(n), it is dominated by the first term, the last term, or is balanced -- recovering the three cases of the master theorem.

The recursion tree is especially valuable for building intuition before attempting a formal proof. It also works for recurrences with floors and ceilings, which technically violate the master theorem's assumptions but rarely change the asymptotic answer.

---

## Part 3: Generating Functions for Algorithm Analysis

### The Flajolet-Sedgewick Approach

The *analytic combinatorics* framework treats algorithm analysis as a pipeline:

1. **Symbolic specification:** Describe the combinatorial class (data structures, inputs) using constructors (union, product, sequence, set, cycle).
2. **Translation to generating functions:** Each constructor maps to an operation on generating functions (addition, multiplication, etc.).
3. **Analytic extraction:** Use complex analysis to extract asymptotic coefficients from the generating function.

This approach transforms counting problems and average-case analyses into calculus problems.

### Ordinary Generating Functions (OGFs)

Given a sequence {a_n}, its OGF is A(z) = sum_{n >= 0} a_n * z^n.

**Key operations:**

- **Addition:** If C = A union B (disjoint), then C(z) = A(z) + B(z).
- **Product (Cartesian):** If gamma = (alpha, beta) with |gamma| = |alpha| + |beta|, then C(z) = A(z) * B(z). This is the *convolution* of sequences.
- **Sequence construction:** SEQ(A) = 1 / (1 - A(z)), provided a_0 = 0.

**Example: Binary strings.** A binary string is a sequence of bits {0, 1}. The atom class has OGF 2z (two objects of size 1). A string is SEQ({0,1}), so the OGF is 1/(1 - 2z). The coefficient of z^n is 2^n, confirming there are 2^n binary strings of length n.

### Exponential Generating Functions (EGFs)

For labelled structures (like permutations), use A(z) = sum_{n >= 0} a_n * z^n / n!.

The key operation is the *labelled product*: if C = A * B (labelled), then C(z) = A(z) * B(z). This automatically accounts for the binomial(n, k) ways to distribute labels.

**Example: Permutations.** A permutation is a set of cycles. The EGF for cycles of length >= 1 is log(1/(1 - z)). The SET construction gives EGF exp(log(1/(1-z))) = 1/(1-z). The coefficient of z^n/n! is n!, confirming n! permutations.

### Transfer Theorems: From Singularities to Asymptotics

The deepest insight of analytic combinatorics: the *location and nature of singularities* of a generating function determine the asymptotics of its coefficients.

**Basic transfer:** If A(z) ~ c * (1 - z/rho)^{-alpha} as z -> rho (the dominant singularity), then:

a_n ~ c * n^{alpha - 1} / (Gamma(alpha) * rho^n)

**Examples of singularity types and their coefficient asymptotics:**

| Singularity at z = rho | Coefficient [z^n] |
|---|---|
| (1 - z/rho)^{-1} | rho^{-n} |
| (1 - z/rho)^{-2} | (n+1) * rho^{-n} |
| (1 - z/rho)^{-1/2} | rho^{-n} / sqrt(pi * n) |
| log(1/(1 - z/rho)) | rho^{-n} / n |

### Application: Average-Case Analysis of Quicksort

Let C_n be the expected number of comparisons by quicksort on a random permutation of n elements. The recurrence is:

C_n = (n + 1) + (2/n) * sum_{k=0}^{n-1} C_k, with C_0 = C_1 = 0.

Multiply by n and subtract the equation for (n-1): n * C_n - (n-1) * C_{n-1} = 2n + 2 * C_{n-1}.

This simplifies to n * C_n = (n+1) * C_{n-1} + 2n. Dividing by n(n+1): C_n/(n+1) = C_{n-1}/n + 2/(n+1).

Let D_n = C_n/(n+1). Then D_n = D_{n-1} + 2/(n+1), so D_n = 2 * sum_{k=2}^{n+1} 1/k = 2 * H_{n+1} - 2, where H_n is the n-th harmonic number.

Therefore C_n = 2(n+1) * H_n - 4n ~ 2n ln n ~ 1.386 n log_2 n.

With generating functions, we can go further: define the EGF of {C_n} and derive a differential equation whose solution yields the same result, plus higher-order terms and distributional information.

---

## Part 4: Amortized Analysis Preview

### The Aggregate Method

Compute the total cost of n operations, then divide by n.

**Example: Dynamic array (vector/ArrayList).** Appending to a dynamic array costs O(1) normally but O(n) when the array must be resized (doubled). Over n insertions, resizing occurs at insertions 1, 2, 4, 8, ..., 2^k where 2^k <= n. Total resizing cost = 1 + 2 + 4 + ... + 2^k <= 2n. Total cost of n insertions <= n + 2n = 3n. Amortized cost per insertion = O(1).

### The Accounting Method

Assign each operation an *amortized cost* (which may differ from actual cost). The key invariant: at all times, the sum of amortized costs >= sum of actual costs. The difference is stored as "credit" in the data structure.

**Dynamic array example:** Charge each insertion an amortized cost of 3 units. The actual cost is 1 (for the insertion itself). Store the remaining 2 units as credit on the newly inserted element. When a resize occurs, the array has doubled from size m to 2m. The m elements inserted since the last resize each have 2 units of credit, totaling 2m units -- exactly enough to pay for copying m elements to the new array.

### Why Amortized Analysis Matters for AI

Training neural networks involves operations with wildly varying per-step costs: gradient checkpointing saves memory but adds recomputation; garbage collection in frameworks like PyTorch has occasional expensive pauses; dynamic batching in transformer inference creates variable-cost steps. Amortized analysis provides the correct framework for reasoning about the *average* cost per step over a training run, rather than being misled by occasional expensive operations.

---

## Watch -- Primary

- **Reducible** -- "Recurrences in Algorithm Analysis" (visual intuition for recursion trees and the master theorem)
- **MIT 6.046J** -- Lecture on Akra-Bazzi theorem (Erik Demaine)
- **Analytic Combinatorics tutorial** -- Philippe Flajolet's 2009 lecture series (available on YouTube, covers generating functions and transfer theorems)

---

## Read -- Primary

- **CLRS** (Cormen, Leiserson, Rivest, Stein) -- Chapters 3 and 4: "Growth of Functions" and "Divide-and-Conquer." These chapters provide the standard treatment of asymptotic notation and the master theorem.
- **Sedgewick and Flajolet, "Analytic Combinatorics"** -- Chapter 1: "Combinatorial Structures and Ordinary Generating Functions." This chapter introduces the symbolic method and the translation from combinatorial specifications to generating functions. Freely available at https://algo.inria.fr/flajolet/Publications/book.pdf.
- **Sedgewick and Flajolet, "An Introduction to the Analysis of Algorithms"** -- A gentler companion to Analytic Combinatorics, covering quicksort analysis, trees, and words with detailed worked examples.

---

## Exercises

1. **Asymptotic classification.** Rank the following functions in increasing order of asymptotic growth: n^2 log n, 2^{sqrt(log n)}, n^3, n^{2.5}, n^2 (log n)^3, n^2 / log n. Prove each adjacent pair's ordering using limits.

2. **Master theorem practice.** Solve T(n) = 4T(n/2) + n^2 log n. Identify which case applies (or explain why the master theorem does not directly apply) and find Theta-notation.

3. **Akra-Bazzi.** Solve the recurrence T(n) = T(n/5) + T(7n/10) + n. Find the exponent p and evaluate the integral to determine the asymptotic growth.

4. **Generating function derivation.** The Catalan numbers satisfy C_0 = 1 and C_n = sum_{k=0}^{n-1} C_k * C_{n-1-k}. Show that the OGF C(z) satisfies C(z) = 1 + z * C(z)^2, solve the quadratic, and use the transfer theorem to extract C_n ~ 4^n / (sqrt(pi) * n^{3/2}).

5. **Quicksort variance.** Using the EGF approach outlined in Flajolet-Sedgewick, show that the variance of the number of comparisons in quicksort is Theta(n^2). (Hint: compute the second moment via a similar recurrence.)

6. **Amortized analysis.** Consider a stack with an additional MULTIPOP(k) operation that pops min(k, stack_size) elements. Using the accounting method, show that any sequence of n PUSH, POP, and MULTIPOP operations has O(n) total cost.

7. **Alignment connection.** A proposed alignment technique requires O(n^2) computation per layer for n tokens (e.g., full attention), while an approximate version runs in O(n log n). If we need to process sequences of length 10^5 and have a budget of 10^{12} FLOPs per forward pass for the alignment module, which version is feasible? Quantify the difference.
