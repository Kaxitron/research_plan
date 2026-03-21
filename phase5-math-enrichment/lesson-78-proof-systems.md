# Lesson 78: Proof Systems

[<- Propositional and Predicate Logic](lesson-77-propositional-predicate-logic.md) | [Back to TOC](../README.md) | [Next: Godel Incompleteness ->](lesson-79-godel-incompleteness.md)

---

> **Why this lesson exists:** A logic without a proof system is a language without grammar -- you can make statements, but you cannot reason from premises to conclusions in a mechanically checkable way. For AI alignment, proof systems are the engine behind formal verification: tools like Lean, Coq, and Isabelle implement proof systems that can certify that a piece of code (or a mathematical theorem about an AI system) is correct. Understanding soundness and completeness tells you exactly what guarantees these tools can and cannot provide. Godel's completeness theorem for first-order logic says that if something is true in all models, a proof exists -- and automated theorem provers can, in principle, find it. This lesson equips you to read the formal verification literature and understand both the power and the limits of proof-based approaches to AI safety.

> **Estimated time:** 10--15 hours

---

## Part 1: What Is a Proof?

### Informal vs. Formal Proofs

In everyday mathematics, a "proof" is an argument that convinces a competent reader. But convincing arguments can contain hidden gaps, rely on unstated assumptions, or even be wrong in subtle ways.

A **formal proof** is a finite sequence of formulas, each of which is either an axiom or follows from previous formulas by an explicitly stated inference rule. A computer can check a formal proof mechanically -- no intuition, no trust, no ambiguity. This is exactly what we want for AI verification: a certificate of correctness that anyone (or any machine) can check.

### Proof Systems

A **proof system** (also called a **deductive system** or **formal system**) consists of:

1. A **language** (the well-formed formulas from the previous lesson)
2. A set of **axioms** (formulas assumed to be true without proof)
3. A set of **inference rules** (mechanical procedures for deriving new formulas from existing ones)

Different proof systems may use different axioms and rules but prove the same theorems. The choice of proof system affects how natural or efficient proofs are, but not what is provable (assuming the systems are sound and complete for the same logic).

---

## Part 2: Natural Deduction

### The Idea

Natural deduction, introduced by Gerhard Gentzen in 1934, is designed to mimic how mathematicians actually reason. Instead of starting from a large set of axioms, it provides **introduction** and **elimination** rules for each connective. You introduce a connective when you want to conclude a formula involving that connective, and you eliminate a connective when you want to extract information from a formula involving it.

### Inference Rules for Propositional Logic

Each rule is written with premises above a horizontal line and the conclusion below.

**AND Introduction (^I):**
If you have proved A and you have proved B, you may conclude A ^ B.

```
  A    B
  ------  (^I)
  A ^ B
```

**AND Elimination (^E):**
If you have proved A ^ B, you may conclude A (or B).

```
  A ^ B         A ^ B
  -----  (^E1)  -----  (^E2)
    A              B
```

**OR Introduction (vI):**
If you have proved A, you may conclude A v B (for any B).

```
    A               B
  ------  (vI1)   ------  (vI2)
  A v B            A v B
```

**OR Elimination (vE) -- Proof by Cases:**
If you have proved A v B, and from the assumption A you can prove C, and from the assumption B you can prove C, then you may conclude C.

```
          [A]    [B]
           .      .
           .      .
  A v B    C      C
  -----------------  (vE)
          C
```

The square brackets indicate that A and B are temporary assumptions that are "discharged" by the rule.

**IMPLIES Introduction (->I) -- Conditional Proof:**
If by assuming A you can prove B, then you may conclude A -> B, discharging the assumption A.

```
   [A]
    .
    .
    B
  ------  (->I)
  A -> B
```

This is one of the most important rules. To prove "if A then B," you assume A and derive B. The assumption is then discharged -- it is no longer in force.

**IMPLIES Elimination (->E) -- Modus Ponens:**
If you have proved A -> B and you have proved A, you may conclude B.

```
  A -> B    A
  -----------  (->E)
       B
```

This is the most fundamental rule of deductive reasoning. It appears everywhere.

**Negation Introduction (~I) -- Proof by Contradiction:**
If by assuming A you can derive a contradiction (often written as the falsum symbol, a bottom symbol representing absurdity), then you may conclude ~A.

```
   [A]
    .
    .
    _|_ (contradiction)
  ------  (~I)
    ~A
```

**Negation Elimination (~E):**
If you have proved A and ~A, you may conclude a contradiction.

```
  A    ~A
  ------  (~E)
   _|_
```

**Double Negation Elimination (DNE):**
From ~~A, conclude A. (This rule is what makes the system classical rather than intuitionistic.)

```
   ~~A
  -----  (DNE)
    A
```

### Modus Tollens as a Derived Rule

**Modus Tollens** is not typically a primitive rule in natural deduction, but it is easily derived:

If A -> B and ~B, then ~A.

Proof: Assume A (for contradiction). By modus ponens with A -> B, we get B. But we have ~B. Contradiction. Therefore ~A.

This pattern -- "the contrapositive argument" -- is used constantly in mathematical reasoning and in safety proofs for AI systems ("if the system were unsafe, it would violate property X; but we have verified property X; therefore the system is safe").

### Inference Rules for Predicate Logic

**Universal Introduction (for-all-I):**
If you have proved P(a) for an arbitrary element a (i.e., a does not appear in any undischarged assumptions), you may conclude (for all x) P(x).

```
    P(a)   [a is arbitrary]
  --------  (for-all-I)
  (for all x) P(x)
```

The restriction that a is arbitrary is crucial. You cannot generalize from a specific example.

**Universal Elimination / Universal Instantiation (for-all-E):**
From (for all x) P(x), you may conclude P(t) for any term t.

```
  (for all x) P(x)
  -----------------  (for-all-E)
       P(t)
```

**Existential Introduction / Existential Generalization (exists-I):**
From P(t), you may conclude (there exists x) P(x).

```
       P(t)
  ----------------  (exists-I)
  (there exists x) P(x)
```

**Existential Elimination (exists-E):**
If you have (there exists x) P(x), and from the assumption P(a) (for a fresh variable a) you can prove C (where a does not appear in C or in any other undischarged assumptions), then you may conclude C.

```
                    [P(a)]
                      .
                      .
  (exists x) P(x)    C      [a fresh]
  ----------------------------  (exists-E)
              C
```

### Example Proof in Natural Deduction

**Claim:** From the premises (for all x)(P(x) -> Q(x)) and P(a), prove Q(a).

```
1. (for all x)(P(x) -> Q(x))     [premise]
2. P(a)                            [premise]
3. P(a) -> Q(a)                    [for-all-E on line 1]
4. Q(a)                            [->E on lines 3, 2]
```

This is a tiny proof, but it illustrates the interaction between quantifier elimination and modus ponens -- a pattern that appears in every formal verification argument.

---

## Part 3: Sequent Calculus

### Sequents

Sequent calculus, also introduced by Gentzen, uses a different notation. A **sequent** has the form:

A1, A2, ..., An |- B1, B2, ..., Bm

This means: if all of A1 through An are true, then at least one of B1 through Bm is true.

The left side (before |-) is the **antecedent**. The right side is the **succedent**. The turnstile |- represents derivability.

A sequent with an empty antecedent (|- B) means B is provable from no assumptions -- i.e., B is a theorem. A sequent with an empty succedent (A |-) means A leads to a contradiction -- i.e., A is unsatisfiable.

### Structural Rules

These rules manipulate the structure of sequents without introducing or eliminating connectives:

**Weakening:** You can add extra formulas to either side of a sequent.
```
  G |- D
  ----------  (Weakening Left)
  G, A |- D

  G |- D
  ----------  (Weakening Right)
  G |- D, A
```

**Contraction:** You can merge duplicate formulas.
```
  G, A, A |- D
  -------------  (Contraction Left)
   G, A |- D
```

**Exchange:** You can reorder formulas (the comma is essentially unordered).

### Logical Rules

Each connective gets a left rule and a right rule. For example:

**Implication Right:**
```
  G, A |- B, D
  --------------  (->R)
  G |- A -> B, D
```

To prove A -> B (on the right), move A to the left (as an assumption) and prove B.

**Implication Left:**
```
  G |- A, D    G, B |- D
  -----------------------  (->L)
     G, A -> B |- D
```

To use A -> B (on the left), you need to prove A and then can use B.

### Cut Elimination

The **cut rule** allows you to use a "lemma":

```
  G |- A, D    G, A |- D
  -----------------------  (Cut)
         G |- D
```

You prove A as an intermediate result, then use it. This seems essential, but Gentzen proved a remarkable theorem:

**Cut Elimination Theorem (Gentzen's Hauptsatz):** Any proof that uses the cut rule can be transformed into a proof that does not use the cut rule.

This has profound consequences. Cut-free proofs have the **subformula property:** every formula appearing in the proof is a subformula of the conclusion. This means proof search can be done by analyzing the structure of the goal formula alone, which is what makes automated theorem proving possible.

For AI alignment, cut elimination is important because it guarantees that automated proof search strategies are complete -- they do not need to guess at intermediate lemmas.

---

## Part 4: Soundness

### The Soundness Theorem

A proof system is **sound** if every provable formula is valid (true in all models).

More precisely: if G |- A (A is provable from assumptions G), then G |= A (A is a logical consequence of G).

In symbols: provability implies truth.

**Why soundness matters for AI:** If you use a proof assistant to verify that an AI system satisfies a specification, soundness guarantees that the verification is correct -- the system really does satisfy the specification (relative to the model). A proof system that is not sound would be useless for verification, because it could "prove" false statements.

### Proving Soundness

Soundness is proved by induction on the length (or structure) of proofs:

1. **Base case:** Every axiom is valid. (You check each axiom against the semantics.)
2. **Inductive step:** Every inference rule preserves validity. (If the premises are valid, the conclusion is valid.)

This is a straightforward but essential verification. When a new proof assistant is built, establishing the soundness of its core inference rules is the first priority.

---

## Part 5: Completeness

### Godel's Completeness Theorem (1929)

The **completeness theorem** for first-order logic states:

If a first-order sentence is valid (true in every structure), then it is provable.

Equivalently: if a sentence is not provable, then there exists a structure in which it is false (a countermodel).

In symbols: truth implies provability. Combined with soundness, we get:

**A first-order sentence is provable if and only if it is valid.**

This is a stunning result. It says that first-order proof systems are perfectly calibrated to first-order semantics -- they prove exactly the valid sentences, no more and no less.

### Proof Sketch

The proof (due to Henkin, 1949, simplifying Godel's original) proceeds by contrapositive: assume A is not provable. Then:

1. The set {~A} is consistent (does not derive a contradiction).
2. Extend {~A} to a maximally consistent set using Lindenbaum's lemma.
3. Construct a model from the maximally consistent set (using the terms of the language as domain elements).
4. Show that ~A is true in this model, so A is not valid.

### What Completeness Does NOT Say

Completeness does not say proofs are easy to find. First-order validity is undecidable (Church and Turing, 1936) -- there is no algorithm that, given an arbitrary first-order sentence, always terminates and correctly decides whether the sentence is valid.

Completeness says: if a sentence is valid, a proof exists. It does not say you can always find it in finite time. This is a crucial distinction for AI verification. The existence of a proof does not mean an automated tool can find it.

### The Compactness Theorem

A consequence of completeness (or provable directly):

**Compactness Theorem:** A set of first-order sentences has a model if and only if every finite subset has a model.

Equivalently: if a set of sentences is unsatisfiable, then some finite subset is already unsatisfiable.

This has applications in model theory and in understanding the limits of first-order logic. For AI: it means that if a specification is inconsistent, the inconsistency is witnessed by finitely many constraints -- you can always localize the problem.

---

## Part 6: Automated Theorem Proving

### Resolution

**Resolution** is an inference rule used in automated theorem provers. It works on formulas in CNF (from the previous lesson):

```
  p v A    ~p v B
  ----------------  (Resolution)
       A v B
```

If one clause contains p and another contains ~p, you can "resolve" them to eliminate p, producing a new clause.

A formula (in CNF) is unsatisfiable if and only if the empty clause (a contradiction) can be derived by repeated resolution. This is the basis of resolution-based theorem provers.

### Unification

When working with predicate logic, resolution requires **unification**: finding a substitution that makes two terms identical.

Example: To resolve P(x, f(y)) with ~P(a, z), we need a substitution that makes x = a, f(y) = z. The substitution {x -> a, z -> f(y)} works.

The **unification algorithm** (Robinson, 1965) finds the most general unifier (MGU) -- the simplest substitution that works. Unification is the key operation in Prolog, a logic programming language where programs are logical formulas and execution is proof search.

### Prolog-Style Logic Programming

In Prolog, you write:

```
parent(tom, bob).
parent(bob, alice).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
```

The query `?- grandparent(tom, alice)` triggers a proof search using resolution and unification. Prolog demonstrates that proofs and computation are two sides of the same coin -- a deep insight that connects logic to AI.

---

## Part 7: Proof Assistants and AI Alignment

### Modern Proof Assistants

**Lean**, **Coq**, **Isabelle**, and **Agda** are interactive proof assistants that implement rich type theories (which extend first-order logic). In these systems:

- You state a theorem as a type.
- You construct a proof as a term of that type (the Curry-Howard correspondence: proofs are programs).
- The kernel (a small, trusted piece of code) checks that the term has the correct type.

Because the kernel is small, the entire system's correctness depends on a small, auditable piece of code. This is the gold standard for trust in formal verification.

### AI-Assisted Theorem Proving

Recent work uses machine learning to guide proof search in these assistants:

- **AlphaProof** (DeepMind, 2024): Used reinforcement learning to solve International Mathematical Olympiad problems in Lean.
- **LeanDojo** and **ReProver**: Train language models to suggest proof steps in Lean.

This creates a feedback loop: AI helps prove theorems, and those theorems can in principle be about AI systems. The dream of alignment researchers is to use AI-assisted formal verification to prove properties of AI systems themselves.

### Limits

Proof assistants can verify that a mathematical model of an AI system satisfies a property. But:

1. The model must faithfully represent the actual system (the "specification gap").
2. The property must faithfully capture what we actually want (the "alignment gap").
3. Godel's incompleteness theorems (next lesson) place fundamental limits on what can be proved within any formal system.

---

## Watch -- Primary

- **Trefor Bazzett -- Logic playlist** (YouTube): Focus on videos covering proof methods, inference rules, and deduction. Look for content on modus ponens, proof by contradiction, and universal/existential reasoning.

## Read -- Primary

- Rosen, "Discrete Mathematics and Its Applications," sections on proof methods and inference rules
- For sequent calculus and cut elimination: Troelstra and Schwichtenberg, "Basic Proof Theory" (more advanced, consult selectively)
- For proof assistants: the Lean 4 tutorial (leanprover.github.io) is an excellent hands-on introduction

---

## Exercises

1. **Natural deduction proof:** Prove the following using natural deduction rules (write out each step with the rule used):
   - From p -> q and q -> r, prove p -> r (hypothetical syllogism)
   - From p v q and ~p, prove q (disjunctive syllogism)
   - From (for all x)(P(x) -> Q(x)) and (there exists x) P(x), prove (there exists x) Q(x)

2. **Sequent calculus:** Write a sequent calculus proof (without cut) of:
   - |- (p -> q) -> (~q -> ~p) (contrapositive as a theorem)

3. **Soundness verification:** Take the modus ponens rule (A -> B and A, therefore B). Prove that it is sound: if A -> B is true in a model M and A is true in M, then B must be true in M. (Use the truth table definition of implication.)

4. **Resolution refutation:** Use resolution to show that the following set of clauses is unsatisfiable:
   - {p v q, ~p v q, p v ~q, ~p v ~q}
   Show the resolution steps leading to the empty clause.

5. **Unification:** Find the most general unifier for each pair, or explain why no unifier exists:
   - P(x, f(y)) and P(g(z), f(z))
   - P(x, x) and P(a, b)
   - P(f(x), y) and P(y, f(x))

6. **Prolog-style reasoning:** Given the following facts and rules:
   ```
   safe(system_a).
   verified(system_a).
   aligned(X) :- safe(X), verified(X).
   deployable(X) :- aligned(X).
   ```
   Trace the proof search for the query `deployable(system_a)`. What inference rules from natural deduction correspond to each step?

7. **Completeness reflection:** Explain in your own words why the completeness theorem for first-order logic does NOT mean that all mathematical truths are provable. (Hint: think about what "valid" means in the completeness theorem versus what "true" means in a fixed structure like the natural numbers.)

8. **AI alignment application:** Suppose you want to formally verify that a reward function R never assigns positive reward to an unsafe action. Write this as a first-order sentence. Then describe what a proof of this sentence in a proof assistant would look like at a high level -- what would the key steps be? What are the assumptions you would need?
