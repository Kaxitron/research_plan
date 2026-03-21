# Lesson 76: Computational Complexity

[<- Kolmogorov Complexity](lesson-75-kolmogorov-complexity.md) | [Back to TOC](../README.md) | [Next: Propositional Logic ->](lesson-77-propositional-predicate-logic.md)

---

> **Why this lesson exists:** Computational complexity theory characterizes the resources (time, space, randomness) required to solve computational problems, establishing a hierarchy of difficulty that extends far beyond the decidable/undecidable boundary. For AI alignment, complexity theory matters because many natural alignment-related tasks -- verifying that a model satisfies a specification, finding optimal training configurations, checking whether a model can be adversarially attacked -- turn out to be NP-hard or worse. Understanding complexity classes helps alignment researchers set realistic expectations about what can be efficiently computed and guides the search for tractable approximations to intractable problems.

> **Estimated time:** 18--24 hours

---

## Part 1: Time Complexity Classes

### Measuring Time Complexity

The time complexity of a Turing machine M on input x is the number of steps M takes before halting. The (worst-case) time complexity of M is the function T(n) = max { steps M takes on input x : |x| = n }.

We say M runs in time O(f(n)) if T(n) <= c * f(n) for some constant c and all sufficiently large n.

A critical distinction: we care about the growth rate, not the exact count. The constants are absorbed by the O() notation because a constant-factor speedup can always be achieved by a more efficient encoding or a faster machine. What cannot be overcome by constant factors is the fundamental scaling behavior: does the running time grow polynomially, exponentially, or somewhere in between?

### The Class P

**P** is the class of languages decidable by a deterministic Turing machine in polynomial time:

P = union over k >= 0 of TIME(n^k)

Equivalently, L is in P if there exists a TM M and a constant k such that M decides L and runs in time O(n^k) for all inputs of length n.

P is widely considered the class of "efficiently solvable" problems. This identification (known as Cobham's thesis) is imperfect -- O(n^{100}) is technically polynomial but practically intractable, while 2^{0.001n} is technically exponential but practically fast for moderate n -- but it provides a robust, machine-independent dividing line.

Examples of problems in P:
- Sorting a list of numbers
- Determining if a number is prime (AKS primality test)
- Finding shortest paths in a graph (Dijkstra's algorithm)
- Linear programming (ellipsoid method, interior point methods)
- Determining if a string matches a regular expression
- 2-SAT (satisfiability of CNF formulas with at most 2 literals per clause)

### The Class NP

**NP** (nondeterministic polynomial time) is the class of languages for which membership can be *verified* in polynomial time, given a polynomial-length certificate (witness).

Formally, L is in NP if there exists a polynomial-time verifier V and a polynomial p such that:

x is in L if and only if there exists a certificate c with |c| <= p(|x|) such that V(x, c) accepts.

Equivalently, NP is the class of languages decided by a nondeterministic TM in polynomial time: the nondeterministic machine "guesses" a certificate and verifies it.

The key asymmetry: NP requires that YES-instances have short proofs, but says nothing about NO-instances. For a problem in NP, you can convince someone a YES answer is correct by showing them a certificate, but you cannot necessarily convince them a NO answer is correct.

Examples of problems in NP:
- SAT: given a boolean formula, is there a satisfying assignment? (Certificate: the satisfying assignment)
- Graph coloring: can a graph be colored with k colors? (Certificate: the coloring)
- Hamiltonian path: does a graph have a path visiting every vertex exactly once? (Certificate: the path)
- Subset sum: given a set of integers and a target, is there a subset summing to the target? (Certificate: the subset)
- Clique: does a graph have a complete subgraph of size k? (Certificate: the vertices of the clique)

### P subset of NP

Every problem in P is also in NP: if you can solve a problem in polynomial time, you can certainly verify a solution in polynomial time (just solve it from scratch and check). The certificate is not even needed.

### The P vs NP Question

The question "is P = NP?" asks whether every problem whose solution can be efficiently verified can also be efficiently solved. This is one of the most important open problems in mathematics and computer science (one of the seven Millennium Prize Problems, with a $1 million prize).

Most researchers believe P != NP, meaning there are problems where finding a solution is fundamentally harder than checking one. The evidence is circumstantial but overwhelming: decades of effort have failed to find polynomial-time algorithms for NP-complete problems, and such algorithms would have extraordinary consequences (breaking most cryptographic systems, solving optimization problems in logistics, biology, and physics, etc.).

### The coNP Class

coNP is the class of languages whose complements are in NP. Equivalently, L is in coNP if NO-instances have short certificates.

Example: TAUTOLOGY (is a boolean formula true for all assignments?) is in coNP: a NO-instance can be certified by a single falsifying assignment. But there is no known short certificate for YES-instances.

If P = NP, then P = coNP = NP. If P != NP, it is still open whether NP = coNP.

---

## Part 2: NP-Completeness

### Polynomial Reductions

A polynomial-time many-one reduction from language A to language B is a polynomial-time computable function f such that:

x is in A if and only if f(x) is in B

We write A <=_p B. If A <=_p B and B is in P, then A is in P. If A <=_p B and A is not in P, then B is not in P.

Reductions allow us to compare the difficulty of problems. If A reduces to B, then B is at least as hard as A.

### NP-Completeness: Definition

A language B is **NP-complete** if:
1. B is in NP, and
2. Every language in NP is polynomial-time reducible to B (B is NP-hard)

NP-complete problems are the "hardest" problems in NP. If any NP-complete problem has a polynomial-time algorithm, then P = NP (and all NP-complete problems have polynomial-time algorithms).

### The Cook-Levin Theorem

**Theorem (Cook 1971, Levin 1973):** SAT is NP-complete.

The proof that SAT is NP-hard involves showing that for any language L in NP with verifier V, we can construct (in polynomial time) a boolean formula phi_x such that phi_x is satisfiable if and only if V accepts (x, c) for some certificate c. The formula encodes the entire computation of V as a boolean circuit and then converts it to CNF.

This was the first NP-completeness proof and required showing that a specific problem is as hard as everything in NP. Once we have one NP-complete problem, we can prove others NP-complete by reduction.

### The Reduction Chain

Starting from SAT, a cascade of reductions establishes NP-completeness of many fundamental problems:

**SAT -> 3-SAT:** Any CNF formula can be transformed into an equivalent formula where each clause has exactly 3 literals. The reduction replaces long clauses with chains of shorter clauses using fresh variables.

**3-SAT -> CLIQUE:** Given a 3-SAT formula with k clauses, construct a graph where nodes represent literal occurrences in clauses, and edges connect nodes from different clauses whose literals are compatible (not contradictory). The formula is satisfiable iff the graph has a k-clique.

**3-SAT -> INDEPENDENT SET:** Similar to the CLIQUE reduction (CLIQUE and INDEPENDENT SET are complements under graph complementation).

**3-SAT -> VERTEX COVER:** Via the relationship: S is an independent set iff V \ S is a vertex cover.

**3-SAT -> SUBSET SUM:** A more elaborate reduction encoding the clause-variable relationship as a numeric system.

**3-SAT -> HAMILTONIAN PATH -> TRAVELING SALESMAN**

**3-SAT -> GRAPH COLORING**

Each reduction preserves polynomial-time computability and correctness (YES maps to YES, NO maps to NO).

### Key NP-Complete Problems

| Problem | Description |
|---------|-------------|
| SAT | Is a boolean formula satisfiable? |
| 3-SAT | SAT restricted to 3 literals per clause |
| CLIQUE | Does graph G have a clique of size k? |
| VERTEX COVER | Can k vertices cover all edges? |
| INDEPENDENT SET | Does G have k mutually non-adjacent vertices? |
| HAMILTONIAN PATH | Path visiting every vertex exactly once? |
| TRAVELING SALESMAN (decision) | Tour of cost at most k? |
| SUBSET SUM | Subset summing to target t? |
| GRAPH COLORING | Is G k-colorable? |
| INTEGER PROGRAMMING | Is there an integer solution to a system of linear inequalities? |
| SET COVER | Can k sets cover the universe? |

### NP-Hardness

A problem is NP-hard if every problem in NP reduces to it, but the problem need not be in NP itself. NP-hard problems are at least as hard as NP-complete problems but may be even harder (e.g., they may not even be decidable).

Example: The halting problem is NP-hard (everything reduces to it) but is not in NP (it is undecidable, hence not even decidable, let alone verifiable in polynomial time).

---

## Part 3: Space Complexity

### PSPACE

**PSPACE** is the class of languages decidable by a TM using polynomial space (polynomial number of tape cells).

Since a TM using space s(n) can have at most 2^{O(s(n))} configurations before repeating, PSPACE is contained in EXPTIME (exponential time). The containments are:

P subset of NP subset of PSPACE subset of EXPTIME

It is known that P != EXPTIME (by the time hierarchy theorem), but none of the intermediate inclusions are known to be strict.

### PSPACE-Complete Problems

A problem is PSPACE-complete if it is in PSPACE and every problem in PSPACE reduces to it. Key PSPACE-complete problems:

- **TQBF (True Quantified Boolean Formulas):** Given a fully quantified boolean formula (with alternating "for all" and "there exists" quantifiers), is it true? This is the canonical PSPACE-complete problem.
- **Generalized games:** Many two-player games (generalized chess, Go on arbitrary boards, generalized Hex) are PSPACE-complete or PSPACE-hard.
- **Regular expression equivalence:** Determining whether two regular expressions with intersection and complement describe the same language.

### Savitch's Theorem

**Theorem:** NSPACE(f(n)) subset of SPACE(f(n)^2) for f(n) >= log n.

This means nondeterministic space can be simulated with only a quadratic blowup in space. Contrast this with time complexity, where the best known simulation of nondeterministic time by deterministic time requires an exponential blowup (and most people believe this is necessary).

Corollary: NPSPACE = PSPACE. Nondeterminism does not help for polynomial-space computation.

---

## Part 4: Randomized Complexity

### BPP

**BPP** (bounded-error probabilistic polynomial time) is the class of languages decided by a probabilistic TM in polynomial time with error probability at most 1/3 on every input.

The error bound of 1/3 is arbitrary -- by repeating the algorithm O(k) times and taking a majority vote, the error probability drops to 2^{-Omega(k)}, exponentially small. So BPP captures what can be "efficiently computed with high confidence."

### RP and coRP

**RP** (randomized polynomial time): the TM always rejects NO-instances correctly, but may err on YES-instances with probability at most 1/2. One-sided error on the YES side.

**coRP:** the TM always accepts YES-instances correctly but may err on NO-instances. One-sided error on the NO side.

P subset of (RP intersect coRP) subset of BPP

### Derandomization

A major conjecture in complexity theory is that BPP = P -- that randomness does not help for polynomial-time computation. This is supported by conditional results (BPP = P if certain circuit lower bounds hold) and by the practical observation that most randomized algorithms have been derandomized.

If BPP = P, then the hierarchy simplifies to:

P subset of NP subset of PSPACE subset of EXPTIME

### Relevance to AI

Randomized algorithms are ubiquitous in machine learning: stochastic gradient descent, random initialization, dropout, data augmentation, sampling methods. Understanding BPP and randomized complexity helps frame questions about whether these random methods are fundamentally necessary or merely convenient.

---

## Part 5: Circuit Complexity

### Boolean Circuits

A boolean circuit is a directed acyclic graph where:
- Input nodes receive the input bits x_1, ..., x_n
- Internal nodes (gates) compute AND, OR, or NOT of their inputs
- One designated output node gives the final answer

The **size** of a circuit is the number of gates. The **depth** is the length of the longest path from an input to the output.

### Circuit Complexity Classes

- **P/poly:** Languages decidable by polynomial-size circuit families (one circuit for each input length). P is contained in P/poly, but P/poly also contains some undecidable languages (because the circuit for each length can be arbitrary -- there is no requirement that the circuit family be uniformly generated).

- **NC:** Languages decidable by polynomial-size, polylogarithmic-depth circuits. NC captures problems solvable in polylogarithmic parallel time with polynomially many processors. NC is contained in P.

- **AC^0:** Constant-depth, polynomial-size circuits with unbounded fan-in AND and OR gates. AC^0 cannot compute the PARITY function (this is a celebrated lower bound).

- **TC^0:** Constant-depth, polynomial-size circuits with threshold gates (outputting 1 if at least k inputs are 1). TC^0 is strictly more powerful than AC^0 and is believed to capture the computational power of fixed-precision transformers.

### Neural Networks as Circuits

A feedforward neural network is a circuit:
- Input nodes are the network inputs
- Hidden units are gates computing a nonlinear function of a weighted sum
- The output node gives the prediction

Key correspondences:
- Network depth corresponds to circuit depth
- Network width corresponds to circuit size at each level
- The activation function determines the type of gate

This connection allows circuit complexity results to inform our understanding of neural network expressiveness:

- **Depth separation:** There exist functions computable by depth-k circuits of polynomial size that require exponential size at depth k-1. Analogously, deeper neural networks can express functions that shallow networks cannot express efficiently.

- **Transformer expressiveness:** Fixed-depth, fixed-precision transformers correspond roughly to TC^0 circuits. This places an upper bound on what such transformers can compute without chain-of-thought augmentation.

---

## Part 6: Approximation Algorithms

### When Exact Solutions Are NP-Hard

Since we likely cannot solve NP-hard optimization problems exactly in polynomial time, a natural alternative is to find approximate solutions. An approximation algorithm finds a solution guaranteed to be within some factor of optimal.

### Approximation Ratios

For a minimization problem, an algorithm has approximation ratio alpha if for every instance, the algorithm's solution cost is at most alpha times the optimal cost. For maximization, the algorithm's solution value is at least (1/alpha) times the optimal value.

### Key Results

**Vertex Cover:** A simple greedy algorithm achieves a 2-approximation: repeatedly pick any uncovered edge and add both endpoints to the cover. This is remarkably hard to improve -- it is a major open problem (related to the Unique Games Conjecture) whether a better ratio is achievable in polynomial time.

**Traveling Salesman (metric):** Christofides' algorithm achieves a 3/2-approximation when the distances satisfy the triangle inequality. This stood as the best known ratio for decades until a slight improvement in 2020.

**MAX-SAT:** A random assignment satisfies at least half the clauses. A more sophisticated LP-based rounding achieves a 3/4-approximation. The celebrated result of Hastad shows that no polynomial-time algorithm can achieve a 7/8 + epsilon approximation for MAX-3-SAT (assuming P != NP).

**Set Cover:** A greedy algorithm achieves an O(log n) approximation. This is essentially optimal assuming P != NP.

### Inapproximability

Some problems cannot be efficiently approximated within any reasonable factor. The PCP theorem (Probabilistically Checkable Proofs) is the foundation of modern inapproximability results. It implies that for many problems, even finding an approximately optimal solution is NP-hard.

This has profound implications: for some optimization problems, not only is finding the exact optimum intractable, but even finding a solution within a constant factor of optimal is intractable.

---

## Part 7: Connections to AI and Alignment

### Training Neural Networks Is NP-Hard

The problem of finding the optimal weights for a neural network (even a simple two-layer network) is NP-hard. This was shown by Blum and Rivest (1988). The result holds even for simple network architectures and loss functions.

In practice, this is circumvented by:
- Using SGD, which finds local optima rather than global optima
- Overparameterization, which creates a loss landscape where local optima are nearly as good as global optima
- Accepting approximate solutions

The fact that training is NP-hard but seems "easy" in practice with overparameterized networks is one of the central mysteries of deep learning theory.

### Feature Selection and Architecture Search

Many problems in machine learning pipeline design are NP-hard:
- Selecting the optimal subset of features (equivalent to subset sum variants)
- Finding the optimal neural architecture (combinatorial search over a huge space)
- Hyperparameter optimization (in general, intractable without structure)

### Complexity of Alignment Verification

Several alignment-relevant problems have high complexity:

- **Formal verification of neural networks:** Verifying that a neural network satisfies a given specification (e.g., output is always in a safe range) is NP-complete for ReLU networks (Katz et al., 2017). This means that even checking whether a trained network meets a simple safety property is intractable in the worst case.

- **Adversarial robustness:** Finding adversarial examples (inputs close to a given input but producing a different output) is NP-hard in general for neural networks.

- **Reward hacking detection:** Determining whether a policy exploits a gap in the reward function is related to verification problems that are at least NP-hard.

### SAT Solvers in Practice

Despite NP-completeness, modern SAT solvers (using techniques like DPLL, CDCL, and random restarts) can solve many practical instances with millions of variables. This is because:

1. Real-world instances have structure that random instances lack
2. Heuristics like unit propagation and clause learning dramatically prune the search space
3. Phase transitions: random instances near the satisfiability threshold are hardest; structured instances are often far from this threshold

SAT solvers are increasingly used in formal verification of hardware and software, and there is growing interest in applying them to neural network verification.

---

## Watch -- Primary

1. **Hackerdashery -- "P vs NP and the Computational Complexity Zoo"**
   - *Outstanding visual explanation of the complexity zoo (P, NP, PSPACE, EXPTIME, BQP, etc.) with clear intuitions for what each class represents.*

2. **Neso Academy -- "Theory of Computation" (Complexity sections, if available)**
   - *Covers basic P and NP definitions, NP-completeness, and the Cook-Levin theorem.*

3. **MIT OpenCourseWare -- "Design and Analysis of Algorithms" (NP-completeness lectures)**
   - *More in-depth treatment of reductions and NP-completeness proofs with worked examples.*

---

## Read -- Primary

- **"Introduction to the Theory of Computation" by Michael Sipser** -- Chapters 7, 8, and 9
  - Chapter 7: Time Complexity (P, NP, NP-completeness, Cook-Levin theorem)
  - Chapter 8: Space Complexity (PSPACE, Savitch's theorem, PSPACE-completeness)
  - Chapter 9: Intractability (approximation, randomized computation, circuit complexity, if covered)

---

## Exercises

1. **P Membership:** Prove that the following problems are in P by describing a polynomial-time algorithm:
   - 2-SAT (hint: implication graph)
   - Determining if a graph is bipartite
   - Finding the greatest common divisor of two integers

2. **NP Verification:** For each NP-complete problem in the table above, explicitly describe the certificate and the polynomial-time verification procedure.

3. **Reduction Practice:** Prove that INDEPENDENT SET is NP-complete by reducing from VERTEX COVER. (Hint: S is an independent set if and only if V \ S is a vertex cover.)

4. **3-SAT to CLIQUE:** Carry out the reduction from 3-SAT to CLIQUE on the formula (x1 OR x2 OR NOT x3) AND (NOT x1 OR x3 OR x4) AND (x2 OR NOT x3 OR NOT x4). Draw the resulting graph and find a 3-clique corresponding to a satisfying assignment.

5. **PSPACE:** Explain intuitively why games (like generalized chess) are in PSPACE. What does the polynomial-space algorithm look like? Why does alternation of quantifiers naturally arise in game trees?

6. **Circuit Lower Bounds:** Explain why proving that a problem requires super-polynomial circuits would separate P from NP (or at least P/poly from NP). Why is proving circuit lower bounds so difficult?

7. **Approximation Algorithm:** Implement the 2-approximation algorithm for Vertex Cover. Run it on several example graphs and compare the solution size to the optimal vertex cover size (which you can find by brute force for small graphs).

8. **Neural Network Verification:** Explain why verifying that a ReLU network always outputs a value in [0, 1] is NP-complete. What makes ReLU networks particularly amenable to reduction from SAT? (Hint: think about how ReLU units can encode boolean logic.)

9. **SAT Solver Exploration:** Install a SAT solver (e.g., MiniSat or CaDiCaL) and use it to solve the following:
   - A graph coloring instance (encode 3-colorability of a given graph as a SAT formula)
   - A Sudoku puzzle (encode the constraints as SAT)
   Report the solver's performance and the structure of the encoding.

10. **Alignment Complexity Essay:** Choose one specific alignment problem (adversarial robustness verification, reward function optimization, interpretability, etc.). Analyze its computational complexity. Is it in P? NP? NP-hard? PSPACE? What does this tell us about the tractability of solving this alignment problem at scale? What approximations or restrictions might make it tractable?
