# Lesson 29: Computability and Complexity — The Limits of Knowledge

[← Applied Statistics](../phase4-statistics/lesson-28-applied-statistics.md) | [Back to TOC](../README.md) | [Next: Abstract Algebra →](lesson-30-abstract-algebra.md)

---

> **Why this lesson exists:** The curriculum references Solomonoff induction, AIXI, Rice's theorem, and Kolmogorov complexity — all of which rest on computability theory. More fundamentally, alignment asks "can we verify that an AI system is safe?" Computability theory's answer is sobering: there are formal limits on what can be verified about programs. Rice's theorem says you can't check *any* non-trivial property of a program's behavior in general. Understanding these limits isn't pessimistic — it tells you which approaches to alignment are fundamentally possible and which are chasing impossibilities.

## 🎯 Core Concepts

### Turing Machines — What Computation IS

- **A Turing machine** is the simplest mathematical model of computation: a tape (memory), a head that reads and writes symbols, a finite set of states (the program), and transition rules. Despite this simplicity, it captures everything any computer can do. Python, C++, your brain (probably) — all equivalent in computational power to a Turing machine.
- **Church-Turing thesis:** anything "computable" in an intuitive sense is computable by a Turing machine. This isn't a theorem (you can't prove it formally) — it's a deeply supported empirical claim. No one has ever found a counterexample despite nearly a century of trying.
- **Universal Turing machine:** a single machine that can simulate ANY other Turing machine, given its description as input. This is the theoretical foundation of general-purpose computers — and of general-purpose AI. Your laptop is a (finite approximation of a) universal Turing machine.
- **Why this matters for alignment:** a sufficiently powerful AI is a universal computer. It can simulate any computation, including simulations of itself, its training process, and its overseers. The logical tangles this creates are studied under "embedded agency" (Lesson 49).

### The Halting Problem — The First Impossibility

- **The halting problem:** given a program and an input, will the program eventually halt (finish) or run forever? Alan Turing proved in 1936 that no algorithm can answer this question for ALL program-input pairs.
- **The proof (by contradiction):** suppose a halting detector H(program, input) exists that always gives the correct answer. Build a pathological program D that:
  1. Runs H on itself: H(D, D)
  2. If H says "halts," D enters an infinite loop
  3. If H says "loops forever," D immediately halts
  - Now ask: does D halt on input D? If yes → H says "halts" → D loops forever (contradiction). If no → H says "loops" → D halts (contradiction). So H cannot exist.
- **The geometric intuition:** this is a *diagonal argument*, the same structure as Cantor's proof that the real numbers are uncountable. You construct an object that differs from every entry in a supposed complete list by flipping the diagonal entry. Self-reference creating paradox is a deep pattern in mathematics.
- **Why this matters:** you cannot build a general-purpose "will this AI system ever produce harmful output?" detector. The halting problem is the simplest, cleanest version of this impossibility.

### Rice's Theorem — The General Impossibility

- **Rice's theorem:** for ANY non-trivial semantic property of programs (any property that's true of some programs' behavior and false of others'), no algorithm can decide whether an arbitrary program has that property.
  - "Does this program ever output harmful text?" — undecidable in general.
  - "Does this program always give aligned responses?" — undecidable in general.
  - "Does this program implement the same function as this other program?" — undecidable.
  - The ONLY decidable semantic properties are trivial ones: "true for all programs" or "false for all programs."
- **What Rice's theorem does NOT say:** it doesn't say you can't check properties of *specific* programs. You can often verify things about particular programs with particular structures. It says there's no *universal* verifier. This distinction matters hugely for alignment — we can make progress on safety for specific architectures even though general safety verification is impossible.
- **Syntactic vs. semantic:** Rice's theorem is about *behavior* (what the program does), not *syntax* (what the code looks like). You CAN check syntactic properties: "does this code contain the string 'hack'?" That's trivially decidable. But "does this code ever do anything harmful?" — that's about behavior, and it's undecidable.

### Kolmogorov Complexity — The Shortest Description

- **Kolmogorov complexity K(x):** the length of the shortest program that outputs string x (then halts). This is the mathematical formalization of "how complex is this object?"
  - A string of 1000 zeros: low complexity (a tiny loop generates it)
  - The digits of π: low complexity (short algorithm computes them)
  - A truly random string: high complexity (no shorter description than the string itself)
- **Incompressibility:** a string is "random" (in the Kolmogorov sense) if K(x) ≈ |x| — there's no compression. Most strings of length n are incompressible (by a counting argument: there are 2ⁿ strings but fewer than 2ⁿ shorter programs).
- **K(x) is uncomputable:** you cannot write a program that computes K(x) for arbitrary x. This follows from the halting problem — you'd need to verify that no shorter program exists, which requires checking all programs for halting.
- **Why this matters for alignment:** Kolmogorov complexity is the theoretical foundation of Solomonoff induction (Lesson 23). Solomonoff's prior assigns probability 2^{-K(H)} to hypothesis H — simpler hypotheses get higher prior probability. This IS Occam's razor made mathematically precise. Understanding why K(x) is uncomputable explains why Solomonoff induction and AIXI are uncomputable — they rest on an uncomputable quantity.

### Solomonoff Induction — Revisited with Foundations

- **Now you have the vocabulary:** Solomonoff induction (from Lesson 23) assigns prior probability 2^{-K(H)} to each hypothesis H, where K(H) is the Kolmogorov complexity of the program generating H's predictions. It then does Bayesian updating as data arrives.
- **Why it's uncomputable:** computing K(H) requires solving the halting problem. So Solomonoff induction is an *ideal* that no physical system can implement. But it's the gold standard of inductive inference — any computable prediction method converges to Solomonoff's predictions (given enough data) or does worse.
- **AIXI** (Hutter) extends this to agents: use Solomonoff induction to predict the environment, then choose actions that maximize expected reward. AIXI is the theoretically optimal agent — and also uncomputable. Real AI systems are (very rough) approximations.
- **The alignment implication:** even the *theoretically optimal* agent has alignment problems. AIXI can wirehead (find ways to hack its own reward signal). The alignment problem isn't just an engineering challenge — it has deep theoretical roots.

### Computational Complexity — What's Feasible?

- **Decidable but hard:** even when a problem CAN be solved by an algorithm, it might take too long. Complexity theory asks: how do resource requirements scale with input size?
- **P (polynomial time):** problems solvable in time O(nᵏ) for some fixed k. These are "efficiently solvable." Sorting, shortest paths, matrix multiplication.
- **NP (nondeterministic polynomial):** problems where a proposed solution can be *verified* in polynomial time, even if finding the solution might be hard. Think sudoku: checking a filled grid is easy, finding the solution from scratch is hard.
- **NP-complete:** the hardest problems in NP. If you could solve any NP-complete problem efficiently, you could solve ALL NP problems efficiently (P = NP). Examples: satisfiability (SAT), traveling salesman, graph coloring.
- **P vs. NP:** the most famous open problem in computer science. Is verifying always easier than solving? Almost everyone believes P ≠ NP, but no one has proved it.
- **Why this matters for alignment:**
  - **Formal verification** of neural networks (proving safety properties) is generally NP-hard or worse. This is why we can't just "prove" an AI is safe — it's computationally infeasible even when it's theoretically possible.
  - **PAC learning theory** uses complexity bounds to characterize how much data you need to learn a concept to a given accuracy.
  - **Interpretability** can be framed as a complexity question: is finding a human-understandable explanation of a model's behavior computationally tractable?

### PAC Learning and VC Dimension (Preview)

- **PAC learning (Probably Approximately Correct):** a framework asking "how many examples do you need to learn a concept with high probability to within some error?" This makes "learning" mathematically precise.
- **VC dimension:** the largest set of points that a hypothesis class can shatter (classify in all possible ways). For linear classifiers in ℝⁿ, VC dimension = n+1. Higher VC dimension means more expressive but needs more data.
- **The bias-variance connection:** low VC dimension = high bias, low variance (underfitting). High VC dimension = low bias, high variance (overfitting). This is the formal version of the intuition from regularization.
- **Why this matters for alignment verification:** if you're trying to verify alignment from behavioral tests, PAC theory tells you how many test cases you need. The answer is often: more than you can practically run, especially if the space of possible misbehaviors is large.

## 📺 Watch — Primary

1. **Computerphile — "Turing Machines Explained"**
   - Search YouTube — good visual explanation with physical tape analogy
2. **Undefined Behavior — "The Halting Problem"**
   - Clear, step-by-step walkthrough of the diagonal argument
3. **Up and Atom — "Kolmogorov Complexity"**
   - Accessible introduction connecting to information and randomness

## 📺 Watch — Secondary

4. **MIT OCW — Michael Sipser, "Introduction to the Theory of Computation"**
   - Lectures on Turing machines and decidability. Sipser wrote THE textbook.
5. **Computerphile — "P vs NP"**
   - Accessible explanation of the most famous open problem
6. **PBS Infinite Series — "Undecidability Tangles"**
   - Good for building intuition about what "decidable" means

## 📖 Read — Primary

- **"Introduction to the Theory of Computation" by Michael Sipser** — Chapters 3–6 (Turing machines, decidability, reducibility)
  - *The gold standard textbook. Clear writing, excellent examples.*
- **"Kolmogorov Complexity" on Arbital**
  - https://arbital.com/p/kolmogorov_complexity/
  - *Short, readable, connects directly to Solomonoff induction.*
- **Scott Aaronson — "Who Can Name the Bigger Number?"**
  - https://www.scottaaronson.com/writings/bignumbers.html
  - *A delightful essay that builds intuition for uncomputability through the Busy Beaver function.*

## 📖 Read — Secondary

- **Stanford Encyclopedia of Philosophy — "Computability and Complexity"**
  - https://plato.stanford.edu/entries/computability/
- **Scott Aaronson — "Why Philosophers Should Care About Computational Complexity"**
  - https://www.scottaaronson.com/papers/philos.pdf
  - *Connects P vs NP to epistemology, free will, and mathematical truth.*

## 📖 Read — Going Deep

- **"Logical Induction" by Garrabrant et al. (MIRI)**
  - https://arxiv.org/abs/1609.03543
  - How to reason under logical uncertainty — deeply connects computability to decision theory (Lesson 46).
- **"Embedded Agency" by Demski & Garrabrant (MIRI)**
  - https://arxiv.org/abs/1902.09469
  - What happens when the agent IS a computation inside the universe it's trying to model?

## 🔨 Do

- **Halting problem intuition:** write a Python function that tries to detect infinite loops by running a program for N steps. Show that this works for many programs but fundamentally can't work for all — construct a program that loops for exactly N+1 steps, fooling your detector.
- **Kolmogorov complexity estimator:** use `gzip` compression as a rough proxy for Kolmogorov complexity. Compare the compressed sizes of: a string of zeros, the digits of pi, random bytes, English text, and Python code. Discuss why compression length approximates K(x) but can never equal it.
- **Rice's theorem exercise:** try to write a function `is_constant(f)` that determines whether a Python function always returns the same value. Show that for any finite set of test inputs it works, but construct a function that fools it (returns a constant for the first million inputs, then changes).
- **PAC learning calculator:** given VC dimension d, error ε, and confidence δ, compute the sample complexity bound: m ≥ (1/ε)(d·ln(1/ε) + ln(1/δ)). How many test cases would you need to verify alignment to 99% confidence with 1% error tolerance, for a hypothesis class with VC dimension 1000?
- **Key exercise:** you want to formally verify that an AI system never outputs harmful content. Using Rice's theorem, explain why this is impossible in the general case. Then explain why this doesn't mean alignment is hopeless — what structural properties of neural networks might make partial verification feasible?

## 🔗 ML Connection

- **Neural network expressiveness** is a complexity question. Universal approximation theorems say networks CAN approximate any function, but they don't say networks can LEARN any function efficiently. The gap between expressiveness and learnability is a complexity gap.
- **Formal verification** of neural networks (proving adversarial robustness, safety properties) is NP-hard in general. Current methods work only for small networks or restricted properties.
- **Minimum description length (MDL)** — a practical approximation of Kolmogorov complexity — is used in model selection: prefer simpler models (shorter description). Weight pruning and quantization are compression whose information-theoretic justification traces back to K(x).
- **Grokking** (delayed generalization after memorization) may relate to the network transitioning from a high-complexity lookup table to a low-complexity algorithm — a compression in Kolmogorov terms.

## 🧠 Alignment Connection

Computability theory sets the **fundamental limits** of alignment:

- **Rice's theorem** means there is no general algorithm to verify alignment. We must rely on specific properties of specific architectures, not universal solutions. This is why empirical interpretability (understanding particular models) is more promising than formal verification (proving properties of arbitrary models).
- **The Solomonoff/AIXI framework** shows that even a theoretically optimal agent has alignment problems (wireheading). Alignment isn't just about making agents smarter — it's a fundamentally different problem from capability.
- **Embedded agency** — an AI reasoning about a world that contains itself — creates self-referential tangles closely related to the halting problem.
- **MIRI's research program** is deeply rooted in computability: their work on logical uncertainty, decision theory, and agent foundations all grapple with what happens when an agent can't compute the full consequences of its own reasoning.
