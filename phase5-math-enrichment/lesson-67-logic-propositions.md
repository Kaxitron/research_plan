# Lesson 67: Logic and Propositions — The Language of Rigorous Reasoning

[← Interpretability — SLT](../phase4-machine-learning/lesson-66-interp-slt.md) | [Back to TOC](../README.md) | [Next: Sets & Functions →](lesson-68-sets-functions-relations.md)

---

> **Why this lesson exists:** AI alignment research rests on making precise claims about what AI systems can and cannot do, and then *proving* those claims rigorously. Every safety proof, every formal verification of a program, every argument about reward hacking or specification gaming ultimately depends on propositional and predicate logic. If you want to move from intuitions about alignment to actual theorems — or even to read papers that contain such theorems — you need fluency in the language of logic and the toolkit of proof techniques. This lesson builds that fluency from the ground up.

> **Estimated time:** 15–20 hours

---

## Part 1: Propositional Logic — Building Blocks of Reasoning

### What Is a Proposition?

A **proposition** is a declarative statement that is either true or false — never both, never neither. This is the bedrock of all formal reasoning.

**These are propositions:**
- "2 + 3 = 5" (true)
- "Every neural network converges to a global minimum" (false, in general)
- "The model's output is harmful" (has a definite truth value in any specific instance)

**These are NOT propositions:**
- "Train the model" (a command)
- "Is this safe?" (a question)
- "x + 1 = 5" (truth value depends on x — this becomes a proposition once x is specified)

The last example is critical. Open sentences with free variables are called **predicates**, and we will get to them when we discuss quantifiers. For now, we work with statements whose truth value is settled.

### Logical Connectives

We build complex propositions from simple ones using **logical connectives**. Let p and q be propositions.

| Connective | Symbol | Name | English |
|---|---|---|---|
| NOT | ~p (or -p) | Negation | "not p" |
| AND | p /\ q | Conjunction | "p and q" |
| OR | p \/ q | Disjunction | "p or q" |
| IF...THEN | p -> q | Conditional (implication) | "if p then q" |
| IF AND ONLY IF | p <-> q | Biconditional | "p if and only if q" |

**A crucial subtlety about OR:** In logic, "or" is **inclusive** by default. "p or q" is true when p is true, when q is true, or when both are true. This differs from everyday English, where "or" often implies exclusivity ("Would you like coffee or tea?"). The exclusive or (XOR) is a separate operation.

**A crucial subtlety about IF-THEN:** The conditional p -> q is false *only* when p is true and q is false. If p is false, then p -> q is **vacuously true** regardless of q. This feels strange at first: "If the moon is made of cheese, then 2 + 2 = 7" is technically true in classical logic. But this convention makes the conditional useful: if someone promises "If it rains, I will bring an umbrella," they have only broken their promise if it rains and they fail to bring the umbrella. If it does not rain, the promise is automatically kept.

### Truth Tables

A **truth table** exhaustively lists all possible truth value assignments and the resulting compound proposition values. For n atomic propositions, you have 2^n rows.

**Truth table for p -> q:**

| p | q | p -> q |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

**Truth table for p <-> q:**

| p | q | p <-> q |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

The biconditional is true exactly when both sides have the same truth value. You can think of it as "p and q agree."

**Practice:** Build the truth table for (p -> q) /\ (q -> p) and verify it matches p <-> q. This is your first taste of proving logical equivalence.

### Logical Equivalences

Two compound propositions are **logically equivalent** (written with a triple-bar symbol, or informally as "equivalent") if they have the same truth value in every possible assignment. This is the logical analogue of algebraic identities.

**The fundamental equivalences you must internalize:**

**De Morgan's Laws:**
- ~(p /\ q) is equivalent to (~p) \/ (~q)
- ~(p \/ q) is equivalent to (~p) /\ (~q)

In words: the negation of "and" becomes "or" with negated parts, and vice versa. These laws appear constantly in proof writing and in programming (think about negating complex boolean conditions).

**Conditional equivalences:**
- p -> q is equivalent to (~p) \/ q
- p -> q is equivalent to ~q -> ~p (the **contrapositive**)
- p -> q is NOT equivalent to q -> p (the **converse** — a common fallacy)
- p -> q is NOT equivalent to ~p -> ~q (the **inverse** — another common fallacy)

**The contrapositive** is enormously important. "If it rains, then the ground is wet" is logically identical to "If the ground is not wet, then it did not rain." Many proofs work by proving the contrapositive because it is often easier to start from the negation of the conclusion.

**Double negation:** ~(~p) is equivalent to p.

**Absorption, distribution, and more:**
- p /\ (p \/ q) is equivalent to p (absorption)
- p /\ (q \/ r) is equivalent to (p /\ q) \/ (p /\ r) (distribution of AND over OR)
- p \/ (q /\ r) is equivalent to (p \/ q) /\ (p \/ r) (distribution of OR over AND)

### Connection to AI: Boolean Circuits and Formal Verification

Every digital computer is built from logic gates implementing AND, OR, and NOT. When we formally verify that a piece of software (or an AI system's decision procedure) behaves correctly, we are essentially checking logical equivalences at massive scale. SAT solvers — programs that determine whether a propositional formula can be made true — are the workhorses of modern formal verification. Understanding propositional logic is understanding the language these tools speak.

---

## Part 2: Predicate Logic and Quantifiers

### From Propositions to Predicates

A **predicate** is a statement containing one or more variables that becomes a proposition once you assign values to those variables.

- P(x): "x is a prime number" — becomes true or false once you specify x
- Q(x, y): "x is greater than y" — needs both x and y specified
- Safe(m): "model m is safe" — becomes a proposition once you specify the model

The set of values a variable can take is called the **domain** (or universe of discourse). The domain matters enormously: "for every x, x^2 >= 0" is true if the domain is real numbers, but the statement does not even make sense if the domain is, say, the set of colors.

### Universal Quantifier

The symbol "for all" (an upside-down A) means "for every element in the domain."

**"For all x, P(x)"** asserts that P(x) is true for every x in the domain.

To **prove** a universally quantified statement, you must show it holds for an *arbitrary* element — you pick a generic x and prove P(x) without assuming anything special about x.

To **disprove** it, you need just one **counterexample** — a single x where P(x) is false.

### Existential Quantifier

The symbol "there exists" (a backwards E) means "there is at least one element in the domain."

**"There exists x such that P(x)"** asserts that P(x) is true for at least one x.

To **prove** an existential statement, you can either exhibit a specific witness or give an indirect argument that one must exist.

To **disprove** it, you must show P(x) is false for *every* x — which is equivalent to proving the universal statement "for all x, not P(x)."

### Negating Quantified Statements

This is where De Morgan's laws generalize beautifully:

- NOT (for all x, P(x)) is equivalent to: there exists x such that NOT P(x)
- NOT (there exists x, P(x)) is equivalent to: for all x, NOT P(x)

In words: "not everything has property P" means "something lacks property P." And "nothing has property P" means "everything lacks property P."

### Nested Quantifiers

Real mathematical (and alignment) statements often involve multiple quantifiers. **Order matters.**

- "For all x, there exists y such that x + y = 0" — TRUE (for real numbers: y = -x works for any x)
- "There exists y such that for all x, x + y = 0" — FALSE (no single y works for every x)

The first says: "given any x, I can find a y that depends on x." The second says: "there is one magic y that works for all x simultaneously." These are very different claims.

**Alignment example:** Consider the statement "For every input prompt p, there exists a response r such that r is safe." This says the model *can* produce a safe response for any input. Contrast with "There exists a response r such that for every input prompt p, r is safe" — this says there is a single universal safe response (much stronger and likely false for any useful model).

### Translating English to Logic

This is a skill you will use constantly when reading and writing alignment research. Practice with these:

- "Every model that is trained with RLHF is aligned" becomes: For all m, (RLHF_trained(m) -> Aligned(m))
- "Some aligned models are not robust" becomes: There exists m such that (Aligned(m) /\ NOT Robust(m))
- "No model is both perfectly aligned and maximally capable" becomes: For all m, NOT (PerfectlyAligned(m) /\ MaxCapable(m))

Note the pattern: "every A is B" translates to the universal with an implication (->), while "some A is B" translates to the existential with a conjunction (/\). Mixing these up is a common error.

---

## Part 3: Proof Techniques

### Why Proofs Matter

A proof is a logically airtight argument that establishes a statement's truth beyond any doubt. In alignment research, we do not just want to *believe* that a system is safe — we want to *prove* it when possible, and understand the limits of what can be proven when it is not.

### Direct Proof

**Structure:** To prove "if P then Q," assume P is true and derive Q through a chain of logical steps.

**Example:** Prove that the sum of two even integers is even.

*Proof.* Let m and n be even integers. By definition, m = 2a and n = 2b for some integers a and b. Then m + n = 2a + 2b = 2(a + b). Since a + b is an integer, m + n is even by definition.

This is the most straightforward proof strategy: start from what you know, apply definitions and known results, arrive at what you want.

### Proof by Contrapositive

**Structure:** To prove "if P then Q," instead prove "if NOT Q then NOT P" (which is logically equivalent).

**Example:** Prove that if n^2 is odd, then n is odd.

*Proof.* We prove the contrapositive: if n is even, then n^2 is even. Suppose n is even, so n = 2k for some integer k. Then n^2 = (2k)^2 = 4k^2 = 2(2k^2). Since 2k^2 is an integer, n^2 is even.

Use the contrapositive when the conclusion Q is hard to work with directly, but NOT Q gives you something concrete to start from.

### Proof by Contradiction

**Structure:** To prove statement S, assume NOT S and derive a logical impossibility (a contradiction).

**Example:** Prove that the square root of 2 is irrational.

*Proof.* Suppose, for contradiction, that sqrt(2) is rational. Then sqrt(2) = a/b where a and b are integers with no common factors (the fraction is in lowest terms). Squaring both sides: 2 = a^2/b^2, so a^2 = 2b^2. This means a^2 is even, so a is even (by the result above). Write a = 2k. Then (2k)^2 = 2b^2, so 4k^2 = 2b^2, so b^2 = 2k^2, so b^2 is even, so b is even. But then both a and b are even, contradicting our assumption that they share no common factors.

Proof by contradiction is powerful but can be harder to follow. Use it when direct approaches and the contrapositive both seem stuck.

### Mathematical Induction

**Structure:** To prove that P(n) holds for all natural numbers n >= n_0:
1. **Base case:** Prove P(n_0).
2. **Inductive step:** Prove that for any k >= n_0, if P(k) is true (the *inductive hypothesis*), then P(k+1) is true.

**Why it works:** The base case gives you P(n_0). The inductive step then gives you P(n_0 + 1), which gives you P(n_0 + 2), and so on — like an infinite chain of dominoes.

**Example:** Prove that 1 + 2 + 3 + ... + n = n(n+1)/2 for all n >= 1.

*Proof.*
- *Base case:* n = 1. LHS = 1. RHS = 1(2)/2 = 1. Check.
- *Inductive step:* Assume the formula holds for some k >= 1 (i.e., 1 + 2 + ... + k = k(k+1)/2). We must show it holds for k+1:

  1 + 2 + ... + k + (k+1) = k(k+1)/2 + (k+1) = (k+1)(k/2 + 1) = (k+1)(k+2)/2.

  This is exactly the formula with n = k+1.

By induction, the formula holds for all n >= 1.

### Strong Induction

**Structure:** Same as ordinary induction, but in the inductive step you may assume P(n_0), P(n_0 + 1), ..., P(k) are ALL true (not just P(k)) to prove P(k+1).

Strong induction is logically equivalent to ordinary induction, but it is often more natural when the value at k+1 depends on values earlier than k.

**Example:** Every integer n >= 2 can be written as a product of primes.

*Proof.*
- *Base case:* n = 2 is itself prime, so it is a product of primes (a product with one factor).
- *Strong inductive step:* Assume every integer from 2 to k can be written as a product of primes. Consider k+1. If k+1 is prime, we are done. If not, then k+1 = a * b where 2 <= a, b <= k. By the inductive hypothesis, both a and b can be written as products of primes. Multiplying those products together gives a prime factorization of k+1.

### Connection to AI: Induction and Recursive Reasoning

Mathematical induction is the formal backbone of reasoning about recursive algorithms, recursive neural network architectures, and any system that processes inputs step by step. When you prove that an alignment property holds at step 0 and is preserved at each subsequent step, you are doing induction. For instance, proving that a reward model maintains a certain safety property throughout training is an inductive argument: the property holds initially, and each gradient step preserves it (under certain conditions).

---

## Part 4: Building Intuition Through Practice

### Common Proof Pitfalls

1. **Assuming what you want to prove.** This is circular reasoning. In the inductive step, you assume P(k) and prove P(k+1) — you do NOT assume P(k+1).

2. **Confusing the conditional with the biconditional.** "If P then Q" does not mean "If Q then P." When you see "the following are equivalent," you need to prove implications in both directions.

3. **Existential proofs require a witness (or indirect argument).** You cannot prove "there exists x with property P" by saying "let x have property P." You must exhibit a specific x or derive existence indirectly.

4. **Domain matters.** "For all x, x^2 > x" is false over the reals (try x = 0.5) but true over the integers greater than 1. Always be explicit about your domain.

### Proof Strategy Guide

When faced with a statement to prove, ask yourself:

1. What is the logical form? (Universal? Existential? Conditional? Biconditional?)
2. For a universal statement: start with "let x be an arbitrary element..."
3. For a conditional (if P then Q): try direct proof first. If stuck, try contrapositive. If still stuck, try contradiction.
4. For statements involving natural numbers: consider induction.
5. For an existential statement: can you construct a witness? If not, try contradiction (assume nothing works and derive a contradiction).

### Connecting Logic to Formal Verification in AI

Formal verification of AI systems is an active research area. The basic approach is:

1. **Specify** the desired property in formal logic (e.g., "for all inputs x in the valid range, the output f(x) is within safe bounds").
2. **Encode** the AI system's computation as logical constraints.
3. **Use automated reasoning** (SAT/SMT solvers) to check whether the property holds or find a counterexample.

This pipeline is exactly propositional and predicate logic in action. The specification uses quantifiers; the encoding uses logical connectives; the solver performs systematic truth-value search. Understanding this lesson's material is the first step toward understanding (and contributing to) formal AI safety verification.

---

## Watch — Primary

1. **Trefor Bazzett — "Discrete Math" playlist (logic and proof sections)**
   - *Covers propositional logic, truth tables, logical equivalences, quantifiers, and all major proof techniques with clear visual explanations*

## Read — Primary

- **"Discrete Mathematics and Its Applications" by Kenneth Rosen** — Chapters 1 and 2
  - *The standard reference for propositional logic, predicate logic, and proof methods. Work through the examples, not just the exposition.*

- **"How to Prove It" by Daniel Velleman** — Chapters 1–3
  - *Focused specifically on building proof skills. Excellent if you find proofs intimidating — Velleman breaks down the process of constructing proofs into systematic strategies.*

## Read — Supplementary

- **"Mathematical Logic for Computer Science" by Mordechai Ben-Ari** — Chapter 1
  - *Connects logic directly to computer science applications, including formal verification.*

## Exercises

1. Build complete truth tables for (a) p -> (q -> p), (b) (p -> q) -> (~q -> ~p), (c) (p \/ q) /\ (~p \/ r) -> (q \/ r). Identify which are tautologies.

2. Using only logical equivalences (not truth tables), show that p -> (q -> r) is equivalent to (p /\ q) -> r.

3. Negate the following statements and simplify using De Morgan's laws and quantifier negation rules:
   - "All models trained for more than 100 epochs are overfitted."
   - "There exists a learning rate such that the model converges and the loss is below 0.01."
   - "For every input, if the input is adversarial, then the output is incorrect."

4. Prove by direct proof: if n is odd, then n^2 is odd.

5. Prove by contrapositive: if n^2 + 2n + 1 is even, then n is odd.

6. Prove by contradiction: there is no largest prime number. (Hint: consider the product of all primes up to some assumed largest prime, plus 1.)

7. Prove by induction: for all n >= 1, the sum 1^2 + 2^2 + ... + n^2 = n(n+1)(2n+1)/6.

8. Prove by strong induction: every integer amount of postage >= 12 cents can be formed using 4-cent and 5-cent stamps.

9. Translate the following into predicate logic and determine truth values (domain: all neural networks):
   - "Every recurrent network can approximate any continuous function."
   - "Some transformer models are both large and efficient."
   - "No model with fewer than 1000 parameters can solve this task."

10. (Challenge) Write a formal specification in predicate logic for the property: "An AI assistant never produces harmful output in response to any input." Then discuss what makes this specification difficult to verify in practice — what are the challenges in defining "harmful" formally?
