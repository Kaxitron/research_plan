# Exam 5A: Computability and Abstract Algebra

**The Path to AI Alignment — Lessons 51–56 Comprehensive Assessment**

---

| | |
|---|---|
| **Time Allowed** | 60 minutes |
| **Total Points** | 100 |
| **Materials** | Pencil, paper. No calculator needed. |
| **Format** | 10 questions mixing proofs, computation, and conceptual depth |

> **Advice:** This exam splits between two worlds: the discrete/logical (computability) and the algebraic (groups, symmetry). The connecting thread: **what can be computed, and how does symmetry structure the landscape of learning?**

---

## Question 1 (10 pts) — Turing Machines and the Halting Problem

**(a)** Define a Turing machine informally: what are its components and what does it do?

**(b)** State the halting problem: what does it ask, and what did Turing prove about it?

**(c)** Walk through the core of the halting problem proof by contradiction. Assume a halting decider H(P, I) exists. Construct the "adversary" program D(P) and explain why D(D) leads to a contradiction.

**(d)** What does the halting problem imply for AI alignment verification? Can we build a program that takes an arbitrary AI system as input and determines whether it will ever produce harmful output?

---

## Question 2 (10 pts) — Rice's Theorem and Decidability

**(a)** State Rice's theorem in one sentence.

**(b)** Using Rice's theorem, argue that the following are undecidable: (i) "Does this program always output the same thing as program Q?" (ii) "Does this neural network implement a deceptive strategy?"

**(c)** Rice's theorem says we can't decide ANY non-trivial property of program behavior. But in practice, we DO analyze programs (compilers, linters, type checkers). How is this possible? What's the escape hatch?

**(d)** For alignment, why does "partial verification is possible even though complete verification is not" represent a hopeful message?

---

## Question 3 (10 pts) — Computational Complexity

**(a)** Define the complexity classes P and NP. What is the relationship between them (known and conjectured)?

**(b)** Classify the following problems: (i) sorting a list of n numbers, (ii) finding whether a Boolean formula has a satisfying assignment (SAT), (iii) multiplying two n×n matrices.

**(c)** An alignment researcher wants to verify that a neural network never outputs harmful text for ANY possible input. Explain why this "adversarial robustness verification" problem is likely computationally intractable for large networks.

**(d)** If P = NP were proven true, what would this mean for alignment verification? Why do most computer scientists believe P ≠ NP?

---

## Question 4 (10 pts) — Kolmogorov Complexity and Occam's Razor

**(a)** Define Kolmogorov complexity K(x) of a string x.

**(b)** Why is Kolmogorov complexity uncomputable? *(Hint: if it were computable, you could generate a short description of the first "incompressible" string — contradiction.)*

**(c)** Solomonoff induction assigns prior probability 2^{−K(H)} to hypothesis H. Explain why this is the "ideal Bayesian prior" and why it implements Occam's razor.

**(d)** What is the relationship between Kolmogorov complexity, the minimum description length (MDL) principle, and model selection? How does this connect to the RLCT from SLT?

---

## Question 5 (10 pts) — Groups: Axioms and Examples

**(a)** State the four group axioms (closure, associativity, identity, inverse).

**(b)** Prove that the integers under addition (ℤ, +) form a group by verifying all four axioms.

**(c)** Show that the integers under multiplication (ℤ, ×) do NOT form a group. Which axiom fails?

**(d)** The symmetric group S₃ consists of all permutations of {1, 2, 3}. List its 6 elements. What is the identity element? Compute the composition (1 2 3)(1 2) — apply (1 2) first, then (1 2 3).

---

## Question 6 (10 pts) — Groups in Neural Networks

**(a)** A neural network with 3 hidden neurons has a symmetry: permuting the neurons (reordering rows of the weight matrix and corresponding columns of the next matrix) doesn't change the network's function. Which group describes this symmetry?

**(b)** How many distinct permutations of 3 hidden neurons exist? If each permutation gives a "different" point in weight space that computes the same function, how many equivalent weight configurations exist for each functional solution?

**(c)** For a network with n hidden neurons, the permutation group S_n acts on weight space. Explain in 2–3 sentences why this symmetry creates singularities in the loss landscape.

**(d)** Connect to SLT: the singularities created by permutation symmetry are exactly the singularities that the RLCT measures. Why does more symmetry (larger n) generally lead to a lower RLCT relative to parameter count?

---

## Question 7 (10 pts) — Rings and Fields

**(a)** What distinguishes a ring from a group? What extra structure does a field add beyond a ring?

**(b)** Give an example of a ring that is NOT a field, and explain which field axiom fails.

**(c)** The polynomial ring ℝ[x] is central to algebraic geometry. What are its elements? Why is it a ring but not a field?

**(d)** In one sentence, explain why polynomial rings matter for SLT. *(Hint: the loss function near a singularity can be expressed as a polynomial, and the ideal generated by its partial derivatives defines the singular set.)*

---

## Question 8 (10 pts) — Group Actions and Orbits

**(a)** Define a group action of G on a set X. What are the orbit and stabilizer of a point x ∈ X?

**(b)** State the orbit-stabilizer theorem: |G| = |Orb(x)| × |Stab(x)|.

**(c)** S₃ acts on weight space of a 3-hidden-unit network by permuting neurons. Consider a weight configuration where all 3 hidden neurons have identical weights.
- What is the orbit of this configuration? (How many distinct weight vectors are in the orbit?)
- What is the stabilizer? (How large is it?)
- Verify the orbit-stabilizer theorem for this case.

**(d)** A weight configuration where all neurons are identical has a large stabilizer (the full group). Explain why large stabilizers correspond to "more singular" points in the loss landscape, and how this connects to the RLCT.

---

## Question 9 (10 pts) — Representations

**(a)** A group representation maps group elements to invertible matrices: ρ: G → GL(V). Why is this useful — what does it let you do with abstract symmetry?

**(b)** The permutation representation of S₃ maps each permutation to a 3×3 permutation matrix. Write the matrix for the transposition (1 2) (which swaps elements 1 and 2).

**(c)** When a group acts on weight space, the weight space decomposes into subspaces that transform independently under the group action (irreducible representations). Why is this decomposition useful for understanding the loss landscape?

**(d)** Connect representations to Phase 1: how are irreducible representations related to the eigenvalue decomposition of a matrix?

---

## Question 10 (8 pts) — Synthesis

**(a)** Draw a conceptual map connecting: halting problem → Rice's theorem → alignment verification limits. In 2–3 sentences, explain what these results tell us about the *theoretical* limits of proving AI safety.

**(b)** Draw a conceptual map connecting: groups → permutation symmetry → singularities → RLCT → generalization. In 2–3 sentences, explain how abstract algebra provides the mathematical foundation for understanding why neural networks generalize.

**(c)** A colleague asks: "If alignment verification is undecidable (Rice's theorem) and the RLCT is hard to compute (algebraic geometry), should we give up on mathematical approaches to alignment?" Write a 2–3 sentence response.

---

## 🔧 Optional Mini Project (~45 minutes): Turing Machine Simulator & Symmetry Explorer

**Part 1: Build a Turing machine simulator (25 min)**
1. Implement a Turing machine: tape (infinite in both directions), head position, state, transition table
2. Program three machines: (a) a binary incrementer, (b) a palindrome detector, (c) a busy beaver (3-state)
3. Visualize the tape at each step — show the head position and current state
4. Run the busy beaver and count the steps. Verify it matches the known BB(3) value

**Part 2: Weight space symmetry visualizer (20 min)**
1. Create a tiny neural network: 2 inputs, 3 hidden (ReLU), 1 output
2. Train it on a simple task (e.g., XOR or a nonlinear boundary)
3. For the 3 hidden neurons, there are 3! = 6 permutations. Apply each permutation to the weight matrices (swap rows of W₁ and corresponding columns of W₂)
4. Verify all 6 networks produce identical outputs on test data
5. Visualize: plot all 6 weight configurations in a 2D projection (PCA of the weight vectors). Show they form a symmetric pattern

**Tools:** Python. NumPy for Part 1, PyTorch + Matplotlib for Part 2.
