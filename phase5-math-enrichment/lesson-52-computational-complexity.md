# Lesson 52: Computational Complexity — P, NP, and the Landscape of Feasibility

[← Turing Machines](lesson-51-turing-machines.md) | [Back to TOC](../README.md) | [Next: Kolmogorov Complexity →](lesson-53-kolmogorov-complexity.md)

---

> **Why this lesson exists:** Decidability asks "can a computer solve this at all?" Complexity asks "can a computer solve this *efficiently*?" Many alignment-relevant problems (verifying model behavior, searching for adversarial inputs, optimizing reward functions) are computationally hard — meaning the best known algorithms scale exponentially. Understanding WHY these problems are hard, and which aspects of them might be tractable, tells you which alignment strategies are computationally feasible and which are pipe dreams.

## 🎯 Core Concepts

### Time Complexity and Big-O

- **Time complexity** measures how an algorithm's running time scales with input size n. O(n) is linear, O(n²) is quadratic, O(2ⁿ) is exponential.
- **Polynomial time** (O(n^k) for some fixed k) is considered "efficient" or "tractable." Exponential time (O(2^n), O(n!)) is "intractable" — even small inputs become prohibitive.
- **This distinction matters in practice:** an O(n³) algorithm on a billion parameters takes ~10²⁷ operations. An O(2ⁿ) algorithm on 100 parameters takes ~10³⁰ operations. The polynomial/exponential boundary is where problems go from "hard but doable" to "physically impossible."

### P, NP, and NP-Completeness

- **P** = problems solvable in polynomial time. Matrix multiplication, shortest paths, linear programming. These are the "easy" problems.
- **NP** = problems where a solution can be *verified* in polynomial time, even if finding one might be hard. "Is there a set of weights that achieves loss < ε?" — if someone hands you the weights, you can check. But finding them might be hard.
- **NP-Complete** = the hardest problems in NP. If you could solve any one of them in polynomial time, you could solve ALL NP problems in polynomial time (P = NP). SAT (boolean satisfiability) was the first proved NP-complete (Cook-Levin theorem).
- **P vs NP:** does P = NP? This is the most important open problem in computer science. Most experts believe P ≠ NP — that some problems are fundamentally harder to solve than to verify. This is unproven.

### NP-Hardness in ML and Alignment

- **Training a neural network** to global optimality is NP-hard. Gradient descent finds local optima, not global ones. The fact that this works well in practice is surprising and not fully understood.
- **Adversarial robustness verification** (proving a network is robust to all perturbations within a ball) is NP-hard. This means you can't efficiently prove a model is safe against all adversarial inputs.
- **Reward hacking detection:** determining whether a model has found an unintended way to achieve high reward is, in general, as hard as solving the halting problem. Approximate versions are likely NP-hard.
- **The lesson for alignment:** many "verify everything" approaches to safety hit computational walls. Practical alignment likely requires approximate methods, domain-specific shortcuts, or accepting probabilistic guarantees instead of absolute ones.

### Space Complexity and PSPACE

- **PSPACE** = problems solvable using polynomial space (memory), regardless of time. PSPACE contains NP (you can try all solutions one at a time, reusing space). PSPACE-complete problems include game-playing (chess with an n×n board, Go with an n×n board).
- **For AI:** the computational complexity of planning and strategic reasoning is typically PSPACE-complete or harder. This means even a superintelligent AI faces fundamental computational limits on how far ahead it can plan.

### Circuit Complexity and Neural Networks

- **A Boolean circuit** is a network of AND, OR, NOT gates — it's the hardware analog of a Turing machine. Circuit complexity asks: how many gates do you need to compute a given function?
- **Neural networks ARE circuits** (with threshold gates instead of Boolean gates). Circuit complexity results directly bound what networks of a given size can compute.
- **Depth vs width:** depth-d polynomial-width circuits can be more powerful than depth-(d-1) circuits. Similarly, deeper neural networks can express functions that would require exponentially wider shallow networks. Depth matters — and this has been made rigorous through circuit complexity.

## 📺 Watch — Primary

1. **MIT OCW — "P vs NP and the Computational Complexity Zoo"** (or Sipser lectures)
2. **Scott Aaronson — "P vs NP" public lectures** (YouTube)
   - *Aaronson is the best expositor of complexity theory alive.*

## 📖 Read — Primary

- **"Introduction to the Theory of Computation" by Sipser** — Chapters 7–8 (Time complexity, NP-completeness)
- **Scott Aaronson — "Quantum Computing Since Democritus"** — Chapters on complexity
  - *Readable, opinionated, brilliant.*

## 🔨 Do

- Implement a SAT solver (brute force, then DPLL with backtracking). Test on random 3-SAT instances. See the phase transition at the clause-to-variable ratio ~4.27.
- Show NP-hardness of training: construct a simple network where finding global optimum requires solving a known NP-hard problem.
- Benchmark: for a specific function, compare the network size needed at depth 2 vs depth 5 vs depth 10. See depth efficiency empirically.
- Research exercise: for 3 alignment-relevant tasks (adversarial robustness, reward verification, behavior prediction), find the known complexity results. Which are NP-hard? PSPACE-hard? Undecidable?
