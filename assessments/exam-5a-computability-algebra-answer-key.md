# Exam 5A: Computability and Abstract Algebra — Answer Key

**The Path to AI Alignment — Lessons 51–56 Comprehensive Assessment**

---

### Question 1 (10 pts)

**(a)** A Turing machine has: a tape (infinite memory divided into cells), a head (reads/writes one cell at a time and moves left/right), a finite set of states, and a transition function (given current state and symbol under the head, determines what to write, which direction to move, and which state to enter). It formalizes the notion of "mechanical computation" — anything a computer can compute, a Turing machine can compute.

**(b)** The halting problem asks: given a program P and input I, will P(I) eventually halt (finish running) or run forever? Turing proved this is **undecidable** — no algorithm can correctly answer this question for ALL program-input pairs.

**(c)** Assume H(P, I) exists and correctly outputs "halts" or "loops" for any program P and input I. Construct D(P): run H(P, P). If H says "halts," loop forever. If H says "loops," halt. Now run D(D): If H(D, D) says "halts" → D(D) loops forever → H was wrong. If H(D, D) says "loops" → D(D) halts → H was wrong. Contradiction in both cases. Therefore H cannot exist.

**(d)** No — by Rice's theorem (a generalization), any non-trivial property of a program's behavior is undecidable. "Will this AI system ever produce harmful output?" is a non-trivial behavioral property, so it's undecidable in general. We cannot build a universal safety verifier that works for arbitrary AI systems. However, partial verification (for specific properties, specific architectures, specific inputs) IS possible.

---

### Question 2 (10 pts)

**(a)** No algorithm can decide any non-trivial property of the function computed by an arbitrary program.

**(b)** (i) "Computes the same function as Q" is a property of the program's input-output behavior → non-trivial → **undecidable** by Rice's theorem. (ii) "Implements a deceptive strategy" is a property of the program's behavior (it behaves differently in some contexts vs. others) → non-trivial → **undecidable** by Rice's theorem.

**(c)** The escape hatch is: practical tools are **conservative approximations** that sacrifice completeness for soundness. A type checker might reject some valid programs (false positives) but never accepts an invalid one. These tools decide a SUBSET of instances, not all instances. Similarly, a linter might flag potential issues without guaranteeing it catches all of them. Rice's theorem says you can't do both perfectly — but you can do one side perfectly at the cost of the other.

**(d)** Even though complete verification is impossible, partial verification can still be valuable. We can prove safety properties for restricted classes of models, specific types of inputs, or bounded computation. The strategy is: build many partial guarantees that overlap sufficiently, like overlapping shields, rather than seeking one universal proof. In practice, defense in depth with multiple partial verification methods may achieve adequate safety.

---

### Question 3 (10 pts)

**(a)** **P:** problems solvable in polynomial time by a deterministic algorithm. **NP:** problems where a proposed solution can be VERIFIED in polynomial time (but finding the solution might take exponential time). Known: P ⊆ NP. Conjectured: P ≠ NP (there exist problems that are easy to verify but hard to solve).

**(b)** (i) Sorting: **P** — O(n log n) algorithms exist (mergesort). (ii) SAT: **NP-complete** — no known polynomial algorithm; verifying a satisfying assignment is easy. (iii) Matrix multiplication: **P** — O(n^{2.37}) currently (Strassen and improvements).

**(c)** To verify the network never outputs harmful text for ANY input, you'd need to check an exponentially large input space (all possible token sequences up to some length). This is essentially searching for an adversarial input — finding whether any input triggers harmful output. This is at least as hard as SAT-like problems (can I find an input x such that f(x) = harmful?). For networks with ReLU activations, exact verification is known to be **NP-hard**. The network's size makes exhaustive search impossible.

**(d)** If P = NP, we could efficiently find adversarial inputs (or prove none exist), efficiently verify behavioral properties, and efficiently solve constraint satisfaction for safety specifications. Most computer scientists believe P ≠ NP because decades of effort haven't found polynomial algorithms for NP-complete problems, many independent NP-complete problems share the same hardness, and efficient solutions would break cryptography (which empirically works).

---

### Question 4 (10 pts)

**(a)** K(x) is the length of the shortest program (in some fixed programming language) that outputs x and halts. It measures the inherent "complexity" or "compressibility" of x. Low K = highly compressible/patterned. High K = random/incompressible.

**(b)** Suppose K were computable. Consider strings of length n. There are 2^n such strings but fewer than 2^n programs of length < n. So some string s of length n has K(s) ≥ n (it's incompressible). But the program "find the first string of length n with K ≥ n and output it" has length O(log n) << n, giving K(s) ≤ O(log n) — contradiction. Therefore K is uncomputable.

**(c)** Solomonoff induction assigns higher probability to simpler hypotheses (shorter programs → higher 2^{−K} probability). This IS Occam's razor: prefer the simplest explanation compatible with the data. It's "ideal" because: (1) it converges to the true distribution for any computable data source, (2) it makes optimal predictions in a precise information-theoretic sense. It's the theoretical gold standard that practical learning algorithms (MLE, Bayesian inference with specific priors) approximate.

**(d)** MDL says: choose the model that gives the shortest total description (model description + data given model). This directly approximates K(data) ≈ K(model) + K(data|model). BIC is a further approximation where K(model) ≈ (d/2)log(n). The RLCT from SLT replaces d/2 with λ — it's a more refined measure of model complexity that accounts for singularities. So: Kolmogorov → MDL → BIC → SLT's free energy. Each is a more practical (but less general) version of the preceding one.

---

### Question 5 (10 pts)

**(a)** (1) Closure: for all a, b in G, a·b is in G. (2) Associativity: (a·b)·c = a·(b·c). (3) Identity: there exists e in G such that e·a = a·e = a for all a. (4) Inverse: for each a, there exists a⁻¹ such that a·a⁻¹ = a⁻¹·a = e.

**(b)** Closure: sum of two integers is an integer ✓. Associativity: (a+b)+c = a+(b+c) ✓. Identity: 0 + a = a + 0 = a, so e = 0 ✓. Inverse: a + (−a) = 0 for all a ∈ ℤ ✓. All four axioms hold, so (ℤ, +) is a group.

**(c)** The **inverse axiom fails**. For example, 2 has no multiplicative inverse in ℤ (1/2 ∉ ℤ). More generally, only ±1 have inverses in ℤ under multiplication.

**(d)** The 6 elements: e = (1)(2)(3) (identity), (1 2), (1 3), (2 3), (1 2 3), (1 3 2).
Identity: e = (1)(2)(3).
Composition (1 2 3)(1 2): Apply (1 2) first: 1→2, 2→1, 3→3. Then (1 2 3): 2→3, 1→2, 3→1. Combined: 1→2→3, 2→1→2, 3→3→1. Result: **(1 3)** — swaps 1 and 3.

---

### Question 6 (10 pts)

**(a)** **S₃** — the symmetric group on 3 elements, i.e., all permutations of {1, 2, 3}.

**(b)** |S₃| = 3! = **6** distinct permutations. Each functional solution has **6 equivalent weight configurations** (one for each way to relabel the 3 hidden neurons).

**(c)** When S₃ acts on weight space, each functional solution corresponds to an **orbit of 6 points**. Where these orbits shrink (at weight configurations with extra symmetry, like all neurons identical), the parameter-to-function map becomes many-to-one in a degenerate way — the Jacobian of this map drops rank. These degenerate points are **singularities** where the loss landscape has flat directions (moving within the orbit doesn't change the function).

**(d)** More symmetry (larger S_n) means more flat directions in the loss landscape at singular points. More flat directions = the effective volume of meaningful parameter space is smaller = lower RLCT relative to d/2. For n hidden neurons, n! symmetries create extensive flat structure, making λ << d/2. This is why larger networks can have disproportionately small effective complexity.

---

### Question 7 (10 pts)

**(a)** A ring has two operations (addition and multiplication) where addition forms an abelian group and multiplication is associative and distributes over addition. A field additionally requires: every nonzero element has a multiplicative inverse (division is always possible except by zero).

**(b)** **ℤ** (integers) under standard +, ×. It's a ring (closure, associativity, distributivity all hold). It's NOT a field because 2 has no multiplicative inverse in ℤ (1/2 is not an integer).

**(c)** Elements: polynomials with real coefficients (e.g., 3x² − x + 5). It's a ring because polynomials can be added and multiplied with all ring axioms satisfied. It's NOT a field because not every nonzero polynomial has a polynomial inverse — 1/x is not a polynomial.

**(d)** Near a singularity, the loss function can be expressed as a polynomial in local coordinates, and the ideal generated by its partial derivatives in the polynomial ring defines the singular set. The algebraic structure of this ideal (via algebraic geometry) determines the RLCT.

---

### Question 8 (10 pts)

**(a)** A group action of G on X is a map G × X → X (written g·x) satisfying: (1) e·x = x (identity acts trivially), (2) (gh)·x = g·(h·x) (compatible with group operation). **Orbit** of x: Orb(x) = {g·x : g ∈ G} — all points reachable from x by the action. **Stabilizer** of x: Stab(x) = {g ∈ G : g·x = x} — elements that fix x.

**(b)** |G| = |Orb(x)| × |Stab(x)|.

**(c)** If all 3 neurons have identical weights, then ANY permutation of neurons leaves the configuration unchanged. So:
- Orbit: only **1 element** (the configuration itself — all permutations give the same point)
- Stabilizer: **all of S₃** → |Stab| = 6
- Orbit-stabilizer: |S₃| = 6 = 1 × 6 ✓

**(d)** Large stabilizer means many symmetry transformations fix the point — many "different" parameter directions lead to the same function. These directions are flat in the loss landscape (zero gradient, zero curvature). More flat directions = more degenerate singularity = lower RLCT. The orbit-stabilizer theorem quantifies exactly how degenerate: if |Stab| is large, |Orb| is small, meaning more of the symmetry group is "wasted" at this point — creating a more singular, lower-complexity configuration.

---

### Question 9 (10 pts)

**(a)** It translates abstract group elements into concrete linear algebra — matrices you can multiply, diagonalize, and compute with. Instead of reasoning about abstract symmetry, you can use eigenvalues, traces, determinants, and all the Phase 1 tools.

**(b)** (1 2) swaps positions 1 and 2:
```
ρ((1 2)) = [[0, 1, 0],
             [1, 0, 0],
             [0, 0, 1]]
```

**(c)** Irreducible subspaces transform independently under the group action. The loss function can be analyzed separately on each subspace — one subspace might have steep curvature, another might be flat. This decomposition identifies which directions in weight space are "equivalent under symmetry" and which are "independent," dramatically simplifying the analysis of the loss landscape near singularities.

**(d)** For a matrix M that commutes with all elements of a group representation (M commutes with ρ(g) for all g), Schur's lemma says M acts as a scalar on each irreducible subspace. This means the eigenspaces of M align with the irreducible decomposition. So irreducible representations ARE the "natural basis" in which the symmetry structure is diagonal — exactly like eigenvectors are the basis in which a matrix is diagonal. Eigendecomposition is representation theory for the group generated by one matrix.

---

### Question 10 (8 pts)

**(a)** Halting problem → can't decide if arbitrary programs halt → Rice's theorem → can't decide ANY non-trivial behavioral property → alignment verification for arbitrary AI systems is undecidable. This tells us: there is no universal algorithm that can certify safety for all possible AI architectures and inputs. We must accept that complete formal verification is impossible in the strongest sense, and instead pursue defense-in-depth with partial verification, interpretability, and empirical testing.

**(b)** Groups formalize symmetry → neural networks have permutation symmetry (S_n) → this symmetry creates singularities in the loss landscape (where the parameter-to-function map degenerates) → the RLCT measures the geometry of these singularities → lower RLCT = lower effective complexity → overparameterized networks generalize because their true complexity (RLCT) is much less than their parameter count. Abstract algebra provides the precise language to describe the symmetries that make neural network loss landscapes singular, which SLT then uses to explain generalization.

**(c)** Absolutely not. Undecidability means we can't build a UNIVERSAL verifier, not that we can't verify ANYTHING. Similarly, computational hardness of RLCT doesn't mean we can't estimate it usefully. Mathematics gives us the map of what's possible and what's not — knowing the boundaries lets us focus effort where it can succeed (partial verification, approximate computation, specific architectures) rather than pursuing impossible universal solutions.
