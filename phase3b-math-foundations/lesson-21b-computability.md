# Lesson 21b: Computability and Complexity — The Limits of Knowledge

[← Bayesian Inference](../phase3-probability/lesson-21-bayesian-inference.md) | [Back to TOC](../README.md) | [Next: Abstract Algebra →](lesson-21c-abstract-algebra.md)

---

> **Why this lesson exists:** The curriculum references Solomonoff induction, AIXI, Rice's theorem, and Kolmogorov complexity — all of which rest on computability theory. More fundamentally, alignment asks "can we verify that an AI system is safe?" Computability theory's answer is sobering: there are formal limits on what can be verified about programs. Rice's theorem says you can't check *any* non-trivial property of a program's behavior in general. Understanding these limits isn't pessimistic — it tells you which approaches to alignment are fundamentally possible and which are chasing impossibilities.

## 🎯 Core Concepts

### Turing Machines — What Computation IS

- **A Turing machine** is the simplest mathematical model of computation: a tape (memory), a head (reads/writes), states (program), and rules (transition function). Despite its simplicity, it captures everything any computer can do. Python, C++, your brain (probably) — all equivalent in computational power to a Turing machine.
- **Church-Turing thesis:** anything "computable" in an intuitive sense is computable by a Turing machine. This isn't a theorem (you can't prove it) — it's a deeply supported empirical claim. No one has found a counterexample.
- **Universal Turing machine:** a single machine that can simulate ANY other Turing machine, given its description as input. This is the theoretical foundation of general-purpose computers — and of general-purpose AI.
- **Why this matters for alignment:** a sufficiently powerful AI is a universal computer. It can simulate any computation, including simulations of itself, its training process, and its overseers. The logical tangles this creates are studied under "embedded agency" (Lesson 33).

### The Halting Problem — The First Impossibility

- **The halting problem:** given a program and an input, will the program eventually halt (finish) or run forever? Alan Turing proved in 1936 that no algorithm can answer this for ALL program-input pairs.
- **The proof (by contradiction):** suppose a halting detector H(program, input) exists. Build a pathological program D that:
  1. Runs H on itself: H(D, D)
  2. If H says "halts," D loops forever
  3. If H says "loops," D halts
  - Now ask: does D halt on input D? If yes, H says "halts," so D loops. If no, H says "loops," so D halts. Contradiction. H cannot exist.
- **The geometric intuition:** this is a diagonal argument, the same structure as Cantor's proof that the reals are uncountable. You construct an object that differs from every item in a supposed complete list by changing the diagonal entry. It's self-reference creating paradox.
- **Why this matters:** you cannot build a general-purpose "will this AI system ever do something harmful?" detector. The halting problem is the simplest version of this impossibility.

### Rice's Theorem — The General Impossibility

- **Rice's theorem:** for ANY non-trivial property of a program's behavior (anything that's true for some programs and false for others), there is no algorithm that can decide whether an arbitrary program has that property.
  - "Does this program ever output harmful text?" — undecidable in general.
  - "Does this program always give aligned responses?" — undecidable in general.
  - "Does this program halt on all inputs?" — undecidable (the halting problem as a special case).
- **What "non-trivial" means:** the property must be about the program's *behavior* (its input-output function), not its *syntax* (its source code). "Does the code contain the string `print`?" is trivially decidable. "Does the program ever print anything?" is not.
- **What Rice's theorem does NOT say:** it doesn't say you can't check properties of *specific* programs. You can prove things about individual programs (formal verification). Rice's theorem says there's no *universal* checker that works on *all* programs.
- **Alignment implication:** this is why "just verify the AI is safe" is not a complete strategy. You can verify specific properties in specific cases, but there is no general-purpose alignment verifier. This motivates empirical, heuristic, and defense-in-depth approaches.

### Kolmogorov Complexity — The Shortest Description

- **Kolmogorov complexity K(x):** the length of the shortest program that outputs the string x. It measures the *inherent information content* of x — how compressible it is.
  - The string "01010101...01" (repeated 1000 times) has low Kolmogorov complexity: the program `print("01" * 1000)` is short.
  - A truly random string of 2000 bits has high Kolmogorov complexity: no program shorter than the string itself can produce it.
- **K(x) is uncomputable.** You cannot write a program that computes the Kolmogorov complexity of arbitrary strings. (Proof: if you could, you could solve the halting problem.)
- **But it's the foundation of Solomonoff induction** (Lesson 21). Solomonoff's prior assigns probability 2^(-K(H)) to hypothesis H — simpler hypotheses (shorter programs) get exponentially higher prior probability. This is Occam's razor formalized.
- **Why AIXI is uncomputable:** AIXI uses Solomonoff induction to predict the environment, which requires computing K(x). Since K(x) is uncomputable, so is AIXI. It's the theoretically optimal agent that can never actually be built — a Platonic ideal.
- **Minimum Description Length (MDL):** practical approximation of Kolmogorov complexity. Instead of all programs, use a specific class of models. The best model minimizes (description length of model) + (description length of data given model). This connects to regularization: simpler models are preferred.

### Complexity Theory — What's Feasibly Computable

- **P:** problems solvable in polynomial time. These are "tractable" — adding more input makes the problem harder, but manageably so.
- **NP:** problems where a proposed solution can be *verified* in polynomial time, even if *finding* the solution is hard. Example: factoring is hard, but checking a factorization is easy.
- **P vs. NP:** does every problem whose solutions can be quickly verified also have solutions that can be quickly found? Almost certainly no (P != NP), but this is unproven — the most famous open problem in math/CS.
- **NP-completeness:** the hardest problems in NP. If you could solve any one of them efficiently, you could solve ALL NP problems efficiently. Boolean satisfiability (SAT), traveling salesman, graph coloring — these are all equivalent in difficulty.
- **Why this matters for alignment:**
  - Verifying alignment might be in NP (you can check a specific alignment proof) while finding alignment might be NP-hard (no efficient general method).
  - PAC learning bounds use complexity theory to characterize when learning is feasible.
  - Adversarial robustness verification is NP-hard for neural networks.

### PAC Learning — When Can Machines Learn?

- **Probably Approximately Correct (PAC) learning:** a formal framework for asking "how much data does a learning algorithm need to achieve good generalization with high probability?"
- **The setup:** a concept class C (the things you want to learn), a distribution D over examples, a hypothesis class H. A PAC learner finds a hypothesis h in H that has low error on distribution D, using polynomially many samples.
- **VC dimension:** measures the "expressive power" of a hypothesis class. It's the largest set of points the class can shatter (classify in all 2^n possible ways). Higher VC dimension = more expressive = needs more data to learn.
  - Linear classifiers in 2D have VC dimension 3 (can shatter any 3 non-collinear points but not 4).
  - Neural networks have VC dimension roughly proportional to the number of parameters (but the exact relationship is subtle).
- **The fundamental theorem of PAC learning:** a hypothesis class is PAC-learnable if and only if it has finite VC dimension. The sample complexity is O(VC(H)/epsilon) where epsilon is the desired error.
- **Why this matters for alignment:** "how much safety testing is enough?" is a PAC-learning question. VC dimension gives lower bounds on the amount of testing needed before you can have confidence in generalization. For neural networks, these bounds are often vacuous (too loose to be useful) — which is itself an important fact.

## 📺 Watch — Primary

1. **Computerphile — "Turing Machines Explained"**
   - Search YouTube — excellent visual walkthrough of how a Turing machine operates
2. **Computerphile — "Halting Problem"**
   - The diagonal argument explained clearly with good visuals
3. **Undefined Behavior — "Rice's Theorem"**
   - Search YouTube — connects Rice's theorem to practical verification

## 📺 Watch — Secondary

4. **Art of the Problem — "Kolmogorov Complexity"**
   - Visual introduction connecting to information theory
5. **MIT OCW 6.045 — "Computability" lectures (Sipser)**
   - https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/
   - More formal treatment if you want depth
6. **Up and Atom — "P vs NP"**
   - Accessible animated explanation of the P vs NP problem

## 📖 Read — Primary

- **"Introduction to the Theory of Computation" by Michael Sipser** — Chapters 3-5
  - The gold standard textbook. Chapter 3 (Turing machines), Chapter 4 (decidability), Chapter 5 (reducibility/Rice's theorem). Clear, rigorous, well-motivated.
- **Scott Aaronson — "Who Can Name the Bigger Number?"**
  - https://www.scottaaronson.com/writings/bignumbers.html
  - *Accessible, entertaining essay that builds from computability to the Busy Beaver function. Shows the staggering scale of uncomputability.*

## 📖 Read — Secondary

- **LessWrong — "Solomonoff Induction" and "AIXI"**
  - https://www.lesswrong.com/tag/solomonoff-induction
  - The rationalist community's treatment, emphasizing alignment implications
- **Scott Aaronson — "Why Philosophers Should Care About Computational Complexity"**
  - https://www.scottaaronson.com/papers/philos.pdf
  - Connects complexity theory to philosophical questions about knowledge and verification

## 📖 Read — Going Deep

- **"Logical Induction" by Garrabrant et al. (MIRI, 2016)**
  - https://arxiv.org/abs/1609.03543
  - How do you reason under logical uncertainty? This builds a computable approximation to Solomonoff induction.
- **"An Introduction to Kolmogorov Complexity and Its Applications" by Li & Vitanyi**
  - The comprehensive reference on Kolmogorov complexity

## 🔨 Do

- **Halting problem proof exercise:** write out the diagonal argument in your own words. Draw the contradiction table. Then explain: why can't you just "try running the program and see if it halts?" (Answer: you can never distinguish "still running" from "will run forever.")
- **Kolmogorov complexity estimation:** take 5 strings (a repeated pattern, English text, random bits, a mathematical sequence, compressed data). Rank them by estimated Kolmogorov complexity. Write the shortest Python program you can for each. Your program lengths approximate K(x).
- **Rice's theorem application:** list 5 properties you'd want to verify about an AI system ("never outputs harmful content," "always gives calibrated uncertainty," "doesn't have deceptive goals," etc.). For each, explain why Rice's theorem implies there's no general verifier — and what partial verification strategies might work despite this.
- **PAC learning calculation:** given a hypothesis class with VC dimension d, compute the sample complexity needed for epsilon = 0.05 error and delta = 0.05 confidence. How does this scale with d? For a neural network with 100M parameters, what does the bound say?
- **Key exercise:** you're designing a testing protocol for an AI system. Using PAC learning theory, estimate how many test cases you need to be 95% confident the system fails on fewer than 1% of inputs. Discuss why this bound is unsatisfying and what alternatives exist (PAC-Bayes, distribution-specific bounds, interpretability-based arguments).

## 🔗 ML Connection

- **Neural networks as universal approximators** (Lesson 22) is a computability statement: any continuous function on a compact set can be approximated arbitrarily well. But universal approximation says nothing about whether gradient descent can *find* the right weights — that's a complexity question.
- **Kolmogorov complexity and compression:** language models are compressors. Cross-entropy loss measures how well the model compresses training data. A perfect model would achieve compression close to Kolmogorov complexity. Hutter's prize literally rewards text compression as a proxy for intelligence.
- **PAC-Bayes bounds** combine PAC learning with Bayesian priors and give tighter generalization bounds for neural networks than classical VC dimension. This connects directly to Lesson 21's Bayesian framework.
- **Adversarial robustness verification** has been proven NP-hard for ReLU networks — even checking whether a specific input has a nearby adversarial example is computationally intractable in general.

## 🧠 Alignment Connection

Computability theory provides the **fundamental limits** on alignment verification:

- **Rice's theorem** means there is no general "alignment checker." This doesn't mean alignment is impossible — it means alignment must be approached through specific techniques (interpretability, testing, formal verification of specific properties) rather than a universal solution.
- **Solomonoff induction** is the theoretical ideal for prediction, but it's uncomputable. Every practical alignment technique is an approximation to something that can't be done perfectly. Understanding what we're approximating helps evaluate how good the approximation is.
- **The halting problem** underlies concerns about AI systems that reason about themselves. A model trying to predict its own behavior faces halting-problem-like barriers. This is one reason "embedded agency" is so technically challenging.
- **Complexity theory** constrains what oversight is feasible. If verifying a model's output requires solving NP-hard problems, then scalable oversight can't rely on exhaustive verification — it must use heuristics, sampling, and structural guarantees.
