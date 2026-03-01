# Exam 5B: Topology and Formal Logic

**The Path to AI Alignment — Lessons 57–62 Comprehensive Assessment**

---

| | |
|---|---|
| **Time Allowed** | 60 minutes |
| **Total Points** | 100 |
| **Materials** | Pencil, paper. No calculator needed. |
| **Format** | 10 questions mixing proofs, computation, and conceptual depth |

> **Advice:** This exam covers the most abstract material in the curriculum. The thread: **topology gives structure to spaces where optimization lives, algebraic geometry resolves the singularities SLT studies, and logic reveals fundamental limits on self-referential reasoning about safety.**

---

## Question 1 (10 pts) — Point-Set Topology

**(a)** In the standard topology on ℝ, is the set (0, 1) open, closed, both, or neither? What about [0, 1]? What about [0, 1)?

**(b)** Define compactness. State (without proof) the Heine-Borel theorem for ℝⁿ.

**(c)** Why does compactness matter for optimization? Specifically: if f is a continuous function on a compact set K, what can you guarantee about f's maximum and minimum? (State the extreme value theorem.)

**(d)** A loss function L: W → ℝ is continuous and W is all of ℝᵈ (not compact). Why doesn't the extreme value theorem apply directly? What practical trick do we use to recover compactness? *(Hint: weight decay / regularization.)*

---

## Question 2 (10 pts) — Connectedness and Continuity

**(a)** Define what it means for a topological space to be connected.

**(b)** Is the set {x ∈ ℝ : x² < 4} connected? Is the set {x ∈ ℝ : x² > 4} connected? Explain.

**(c)** In the context of loss landscapes: if the set of global minima {W : L(W) = L*} is connected, what does this mean for training? What if it's disconnected?

**(d)** If two loss minima are in the same connected component, can gradient descent always find a path between them? Why or why not?

---

## Question 3 (10 pts) — Homotopy and Fundamental Groups

**(a)** Define a homotopy between two continuous maps. When are two paths "homotopic"?

**(b)** The fundamental group π₁(X, x₀) captures "loops that can't be shrunk." Compute (or state) π₁ for: (i) ℝ², (ii) the circle S¹, (iii) the torus T².

**(c)** A loss landscape sublevel set S_ε = {W : L(W) ≤ ε} might have "holes" (non-trivial fundamental group). What would the presence of a hole mean for gradient-based optimization?

**(d)** The topology of level sets can change as ε varies — this is the essence of Morse theory. How does this connect to critical points of the loss function?

---

## Question 4 (10 pts) — Manifolds and Tangent Spaces

**(a)** Define a smooth manifold informally. Give two examples from everyday experience.

**(b)** What is the tangent space T_pM at a point p on a manifold M? Why is it useful for optimization?

**(c)** Weight space modulo the permutation symmetry S_n (i.e., identifying equivalent weight configurations) is NOT a manifold everywhere — it has singular points. Where do these singularities occur? *(Hint: think about the orbit-stabilizer theorem from Lesson 56.)*

**(d)** Riemannian gradient descent generalizes gradient descent to manifolds. In one sentence, explain the key idea: how is the gradient adapted to a curved space?

---

## Question 5 (12 pts) — Algebraic Geometry and Singularities

**(a)** Define an algebraic variety. Give two examples: one smooth, one singular.

**(b)** How do you determine if a point on a variety is smooth or singular? State the Jacobian criterion.

**(c)** Classify the singularity type for each variety at the origin: (i) V = {y² − x² = 0}, (ii) V = {y² − x³ = 0}.

**(d)** Describe what a blow-up does geometrically to the node V = {y² − x² = 0} at the origin. After the blow-up, is the singularity resolved?

**(e)** Compute the RLCT for f(w) = w⁶ in 1D. *(Hint: the integral ∫₀¹ w^{−6t} dw converges iff...)*

---

## Question 6 (10 pts) — The RLCT: Full Chain

**(a)** State the chain connecting permutation symmetry to the RLCT:
permutation symmetry → ___ → ___ → ___ → RLCT

**(b)** For a simple model f(w₁, w₂) = w₁²w₂² (the product-of-squares singularity), the set {f = 0} is two crossing lines. After blowing up, the singularity resolves. The RLCT is λ = 1/2. Compare with the "regular" value d/2 = 2/2 = 1 for 2 parameters. What does the 2× reduction mean?

**(c)** Hironaka's theorem guarantees that ANY variety can be resolved by a finite sequence of blow-ups. Why is this theorem essential for SLT?

---

## Question 7 (10 pts) — Propositional and Predicate Logic

**(a)** Translate into propositional logic: "If the model is deceptive and passes behavioral tests, then interpretability is necessary for detecting misalignment." Define your variables clearly.

**(b)** Construct a truth table for (P → Q) ∧ (¬Q). What does this compound statement simplify to?

**(c)** Translate into predicate logic: "For every input, if the model produces a harmful output, then the safety filter catches it." Use ∀, →, and appropriate predicates.

**(d)** Formalize the following safety property in predicate logic: "There exists no input for which the model produces harmful output and the safety filter fails to catch it."

---

## Question 8 (10 pts) — Gödel's Incompleteness Theorems

**(a)** State Gödel's first incompleteness theorem informally.

**(b)** The Gödel sentence G says "this sentence is not provable." Explain why G is TRUE but UNPROVABLE in the system.

**(c)** State Gödel's second incompleteness theorem. What does it say about a system proving its own consistency?

**(d)** For alignment: if an AI system uses a formal logical system for reasoning, what do Gödel's theorems imply about the system's ability to prove its own safety? Be specific.

---

## Question 9 (10 pts) — Löb's Theorem and Self-Reference

**(a)** State Löb's theorem: if a system can prove "if I can prove P, then P," what follows?

**(b)** Explain the "Löbian obstacle" to AI self-trust: why can't an AI system simply prove "if I can prove I'm safe, then I am safe" and use this to bootstrap a safety guarantee?

**(c)** Two AI systems, A and B, want to cooperate but each needs to trust the other's safety proofs. Explain how Löb's theorem constrains this mutual verification.

**(d)** Despite these limits, some researchers propose "Löbian handshakes" or alternative logical frameworks. In 1–2 sentences, explain why finding workarounds to Löb's theorem matters for AI coordination.

---

## Question 10 (8 pts) — Capstone Synthesis

Trace the complete chain from permutation symmetry to Löb's theorem:

**(a)** Permutation symmetry (Lesson 56) → singularity in weight space → blow-up resolution (Lesson 60) → RLCT computation → free energy formula.
For each arrow, write one sentence explaining the mathematical mechanism.

**(b)** In 3–4 sentences, explain why BOTH the algebraic geometry thread (singularities, RLCT) AND the logic thread (Gödel, Löb) are necessary for a complete mathematical approach to alignment. What does each contribute that the other cannot?
