# Lesson 21e: Formal Logic — Self-Reference, Limits, and AI Reasoning

[← Topology](lesson-21d-topology.md) | [Back to TOC](../README.md) | [Next: Single Neuron →](../phase4-neural-networks/lesson-22-single-neuron.md)

---

> **Why this lesson exists:** MIRI's agent foundations research — arguably the most theoretically ambitious alignment program — is built on formal logic. Logical uncertainty (referenced in Lesson 30), Löb's theorem (why agents can't reason about their own trustworthiness in certain ways), and Gödel's incompleteness theorems (fundamental limits on self-knowledge) all require formal logic vocabulary. When alignment researchers worry about "an AI system reasoning about its own reasoning," the obstacles they identify are logical in nature. This lesson gives you enough logic to read those arguments and understand what they're proving.

## 🎯 Core Concepts

### Propositional and Predicate Logic

- **Propositional logic** deals with statements that are true or false, connected by AND (∧), OR (∨), NOT (¬), IMPLIES (→), and IF AND ONLY IF (↔).
  - A **tautology** is true regardless of the truth values of its components: P ∨ ¬P is always true.
  - **Modus ponens:** from P and P → Q, conclude Q. The fundamental rule of inference.
  - **Contrapositive:** P → Q is equivalent to ¬Q → ¬P. Essential for reasoning about AI: "if the AI is safe, it passes the test" is equivalent to "if it fails the test, it's not safe."

- **Predicate logic (first-order logic)** adds quantifiers:
  - ∀x (for all x): "for every possible input, the model is safe"
  - ∃x (there exists x): "there exists an input that makes the model unsafe"
  - The negation of ∀x P(x) is ∃x ¬P(x). To disprove "the model is always safe," you need just ONE counterexample.

- **Why this matters for alignment:** safety properties are logical statements. "The model never produces harmful output" is ∀x ¬Harmful(Output(model, x)). Proving this is a universal statement — you need it to hold for ALL inputs. Finding a violation is an existential statement — you need just ONE bad input. This asymmetry is fundamental to why safety is harder than capability.

### Formal Systems and Provability

- **A formal system** consists of axioms (starting truths), rules of inference (how to derive new truths), and theorems (everything derivable). First-order arithmetic (Peano Arithmetic, or PA) is the standard formal system for reasoning about numbers.
- **Provability vs. truth:** in a formal system, a statement is *provable* if it can be derived from the axioms. It's *true* (in the intended model) if it holds in the standard natural numbers. These are NOT the same — the gap between them is Gödel's discovery.
- **Consistency:** a system is consistent if it never proves both P and ¬P. Inconsistent systems are useless (they prove everything). We hope our formal systems are consistent, but proving consistency is itself subject to fundamental limits.

### Gödel's Incompleteness Theorems

- **First incompleteness theorem:** any consistent formal system strong enough to describe basic arithmetic contains statements that are true but unprovable within the system. There are mathematical truths that the system can state but never prove or disprove.
  - **The Gödel sentence G says, roughly: "this statement is not provable in this system."** If G is provable, the system proves something false (G says it's unprovable). If G is unprovable, it's true (it correctly says it's unprovable). So G is true but unprovable.
  - This is a diagonal argument again — the same self-referential trick as the halting problem (Lesson 21b). Gödel essentially built a "program" (formal statement) that talks about its own provability.

- **Second incompleteness theorem:** a consistent formal system cannot prove its own consistency. If a system proves "I am consistent," then it is actually inconsistent.
  - **Alignment implication:** an AI system using formal reasoning cannot prove, within its own reasoning system, that its reasoning system is consistent. There will always be a gap between what the AI can verify about itself and what is actually true about itself.

### Löb's Theorem — The Obstacle to Self-Trust

- **Löb's theorem:** in any formal system containing basic arithmetic, if the system can prove "if I can prove P, then P is true," then the system can actually prove P.
  - Formally: if PA ⊢ (Prov(⌈P⌉) → P), then PA ⊢ P.
  - In English: a formal system cannot assert "everything I prove is true" unless it can prove literally everything (making it inconsistent or trivial).

- **Why this matters for AI:** suppose you want an AI system that reasons: "If my reasoning process concludes that action X is safe, then X is actually safe." Löb's theorem says this kind of self-trust is impossible within a consistent formal system — unless the conclusion is already independently provable.

- **The AI self-trust problem:** we want AI systems that can verify their own reasoning. But Löb's theorem creates obstacles: the AI cannot, within its own logic, establish that its own proofs are reliable in general. This is one reason MIRI researchers believe alignment requires going beyond standard formal reasoning frameworks.

### Self-Reference and Fixed Points

- **Self-reference** is the common thread: Gödel sentences refer to their own provability. The halting problem involves programs analyzing themselves. Löb's theorem concerns systems asserting their own reliability.
- **The diagonal lemma (Gödel's fixed point theorem):** for any property P, there exists a sentence that says "I have property P." This is the formal mechanism that makes self-reference possible and creates the incompleteness phenomena.
- **Quining:** in programming, a quine is a program that outputs its own source code. This is self-reference made computational. The connection to Gödel: a Gödel sentence is essentially a logical quine — a formula that "quotes" itself.
- **Relevance to embedded agency:** an AI system embedded in the world it's reasoning about must deal with self-reference constantly. It's a physical system reasoning about physical systems (including itself). The formal logic tells us this creates inescapable limitations.

### Logical Uncertainty — Reasoning About What You Can't Compute

- **Logical uncertainty** (referenced in Lesson 30) is uncertainty about the consequences of your own deductive system. You know the axioms, you know the rules, but you haven't computed all the theorems yet. What probability should you assign to an unproven mathematical conjecture?
- **Why standard probability theory doesn't cover this:** Bayesian probability handles *empirical* uncertainty (uncertainty about facts). Logical uncertainty is different — the facts are determined by the axioms, but you don't know them yet because computing them takes too long.
- **MIRI's "Logical Induction" paper** (Garrabrant et al., 2016) proposes a framework for logical uncertainty that satisfies desirable rationality properties. It uses a market metaphor: beliefs are priced like assets, and a "logical inductor" is a belief system that can't be exploited by any computationally bounded trader.
- **Connection to AI alignment:** a sufficiently powerful AI faces massive logical uncertainty. It can't compute all consequences of its training objective, it can't fully simulate its own future behavior, and it can't verify all properties of its own code. How it handles this uncertainty affects whether it behaves safely.

## 📺 Watch — Primary

1. **Veritasium — "Math Has a Fatal Flaw" (Gödel's Incompleteness)**
   - https://www.youtube.com/watch?v=HeQX2HjkcNo
   - *Excellent accessible treatment of incompleteness with visual explanations*
2. **Numberphile — "Gödel's Incompleteness Theorem"**
   - Multiple videos available — Prof. Marcus du Sautoy's version is good
3. **Robert Miles — "Embedded Agency"** (if available)
   - Connects logical limitations to AI alignment

## 📺 Watch — Secondary

4. **Computerphile — "Gödel's Incompleteness Theorem"**
   - More technical treatment with computer science flavor
5. **PBS Infinite Series — "Löb's Theorem and Gödel"**
   - Connects Löb's theorem to game theory and cooperation

## 📖 Read — Primary

- **"Gödel, Escher, Bach" by Douglas Hofstadter** — Chapters 1-9
  - The classic treatment of self-reference, formal systems, and incompleteness. Dense but deeply rewarding. The dialogues between chapters build intuition before the formal chapters deliver the proofs.
- **"Gödel's Proof" by Ernest Nagel and James Newman**
  - Short (100 pages), clear, self-contained explanation of the first incompleteness theorem. If GEB is too long, read this instead.

## 📖 Read — Secondary

- **MIRI's "Logical Induction" by Garrabrant et al. (2016)**
  - https://arxiv.org/abs/1609.03543
  - The technical paper on logical uncertainty. Read the introduction and Section 1 for the motivation; the full technical details are very dense.
- **"Embedded Agency" by Demski & Garrabrant (MIRI)**
  - https://arxiv.org/abs/1902.09469
  - Section on "reasoning about reasoning" uses the logic from this lesson directly.
- **LessWrong — "Löb's Theorem" posts**
  - https://www.lesswrong.com/tag/lob-s-theorem
  - The rationalist community's treatment with alignment applications

## 📖 Read — Going Deep

- **"Computability and Logic" by Boolos, Burgess, and Jeffrey**
  - The standard textbook for the mathematical logic underlying computability and incompleteness
- **"The Logic of Provability" by George Boolos**
  - Advanced treatment of provability logic, Löb's theorem, and self-referential reasoning

## 🔨 Do

- **Gödel sentence construction:** write out (informally) a Gödel sentence for a simple formal system. Walk through the diagonal argument step by step. Convince yourself it's true but unprovable.
- **Propositional logic warmup:** prove that (P → Q) is equivalent to (¬Q → ¬P) using a truth table. Then prove that ¬(∀x P(x)) is equivalent to ∃x ¬P(x). Apply these to alignment: rephrase "if the model is aligned, it passes the evaluation" and its contrapositive.
- **Quine exercise:** write a Python quine (a program that prints its own source code) without reading the source file. This is self-reference made concrete. Appreciate how the trick works — it's the same fixed-point mechanism as Gödel's construction.
- **Löb's theorem thought exercise:** suppose an AI uses a formal proof system and reasons: "I've proven that action X is safe, and everything I prove is true, so X is safe." Explain, using Löb's theorem, why this chain of reasoning is problematic. What would the AI need to do differently?
- **Key exercise:** an AI alignment researcher proposes: "we'll make the AI prove, within its own formal system, that it is aligned." Using Gödel's second incompleteness theorem, explain the fundamental obstacle. Then discuss: what *can* the AI prove about itself, and what must be verified externally?

## 🔗 ML Connection

- **Neural networks as proof search:** some recent work frames neural network computation as a form of bounded proof search in a logical system. The network "looks for" arguments that the output should be a particular token. This perspective connects deep learning to logic.
- **Chain-of-thought reasoning** in LLMs is a form of explicit logical derivation. Understanding what formal logic can and can't do helps evaluate the reliability of chain-of-thought.
- **Formal verification of neural networks** (proving that outputs stay within bounds for all inputs in a domain) uses the logic from this lesson. The limitations (Rice's theorem from 21b) and the possibilities (verification of specific properties) are both logical.

## 🧠 Alignment Connection

- **Embedded agency** (one of MIRI's core research areas) is about agents reasoning about themselves while being part of the world they reason about. Gödel's incompleteness theorems and Löb's theorem are the formal obstacles that make this hard.
- **Logical uncertainty** is how AI systems should handle the gap between what they can prove and what is true. Getting this wrong can lead to overconfidence (the AI acts on unverified beliefs) or paralysis (the AI refuses to act because it can't prove safety). MIRI's logical induction is one proposed solution.
- **The AI self-improvement problem:** if an AI system modifies its own code, can it verify that the modification preserves safety? Gödel's second theorem suggests fundamental limits: the system can't prove its own consistency, let alone prove that a modified version remains consistent. This is a formal argument for external oversight.
- **Cooperation between AI systems:** Löb's theorem has been connected to cooperation in the Prisoner's Dilemma. If two AI systems can read each other's source code, they can achieve mutual cooperation by reasoning about their mutual reasoning — but only with careful handling of the self-referential logic.
