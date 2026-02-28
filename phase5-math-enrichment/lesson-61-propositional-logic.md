# Lesson 61: Propositional and Predicate Logic — The Syntax of Reason

[← Algebraic Geometry](lesson-60-algebraic-geometry.md) | [Back to TOC](../README.md) | [Next: Gödel & Löb →](lesson-62-godel-lob.md)

---

> **Why this lesson exists:** Logic is the formal language of proof, verification, and specification. When alignment researchers write formal specifications of what an AI system should do, they use predicate logic. When they reason about self-referential systems (AI systems reasoning about themselves), they need modal logic. When they prove impossibility results (you can't build a perfect alignment verifier), they use the tools of mathematical logic. This lesson gives you the formal syntax and semantics to read and write these arguments.

## 🎯 Core Concepts

### Propositional Logic — True/False Machines

- **Propositions** are statements that are either true or false: "it's raining" (P), "the model is aligned" (Q). Variables P, Q, R represent arbitrary propositions.
- **Connectives:** NOT (¬P), AND (P ∧ Q), OR (P ∨ Q), IMPLIES (P → Q), IFF (P ↔ Q).
- **Truth tables** define each connective exhaustively. The key non-obvious one: P → Q is false ONLY when P is true and Q is false. "If it's raining, I'll bring an umbrella" is violated only if it rains and you don't bring one.
- **Tautologies** are always true (e.g., P ∨ ¬P). **Contradictions** are always false (P ∧ ¬P). **Contingencies** depend on the values of the variables.
- **Normal forms:** any propositional formula can be written in CNF (conjunction of disjunctions) or DNF (disjunction of conjunctions). SAT — determining whether a CNF formula is satisfiable — is NP-complete (from Lesson 52).

### Predicate Logic — Quantifying Over Objects

- **Predicates** take arguments: Aligned(x) means "x is aligned." Trusts(x,y) means "x trusts y." Predicates generalize propositions by allowing variables.
- **Quantifiers:** ∀x (for all x) and ∃x (there exists an x). "For all AI systems x, if x is deployed, then x is aligned" = ∀x(Deployed(x) → Aligned(x)).
- **Free vs bound variables:** in ∀x(P(x)), x is bound. In P(x) ∧ Q(y), both are free. A formula with no free variables is a **sentence** — it has a definite truth value.
- **Logical consequence:** Σ ⊨ φ means "φ is true in every model where all sentences in Σ are true." This is the semantic notion of entailment — the conclusion follows from the premises.

### Proofs — Syntactic Reasoning

- **A proof system** gives rules for deriving new sentences from old ones: modus ponens (from P and P→Q, derive Q), universal instantiation (from ∀x P(x), derive P(a) for any a), etc.
- **Soundness:** if a proof system derives φ from Σ, then Σ ⊨ φ. Provable → True. Every proof system should be sound.
- **Completeness (Gödel's completeness theorem):** for first-order logic, if Σ ⊨ φ then there exists a proof of φ from Σ. True → Provable. This is remarkable — every true consequence is provable. (But see the INCOMPLETENESS theorem in the next lesson for arithmetic!)
- **The distinction:** soundness says proofs can't be wrong. Completeness says true things can be proved. First-order logic has both. More powerful logical systems lose completeness.

### Models and Interpretations

- **A model (interpretation)** assigns meaning to the symbols: a domain of objects, truth values for predicates, values for constants. The sentence ∀x(Dog(x) → HasTail(x)) is true in a model where every dog has a tail, false otherwise.
- **Model theory** studies the relationship between sentences and their models. A key result: the Compactness Theorem — if every finite subset of Σ has a model, then Σ has a model. This has surprising consequences (like the existence of "nonstandard" models of arithmetic).
- **For alignment:** specifying what "aligned" means formally requires choosing the right logical language and building a model of the desired behavior. The gap between the formal specification and the intended meaning is the specification problem.

### Formal Verification and Specifications

- **Formal verification** uses logic to prove properties of programs: "for all inputs, this program terminates" (∀x. Halts(P, x)) or "this system never outputs harmful content" (∀x. Input(x) → ¬Harmful(Output(P, x))).
- **Specification languages** (like temporal logic: "always," "eventually," "until") express safety and liveness properties. CTL and LTL are used for hardware and software verification.
- **For AI alignment:** you could try to formally specify alignment properties and verify them. The challenge: (1) the specification may not capture what you actually want (Goodhart's law), (2) verification of neural networks is generally intractable (Lesson 52), (3) the model space is too large for exhaustive checking.
- **Partial verification:** you can verify specific properties for specific inputs, or probabilistic properties. This is the practical path — not perfect safety, but measurable safety.

## 📺 Watch — Primary

1. **Numberphile — "Gödel's Incompleteness Theorem" (Goldrei or similar)**
2. **Computerphile — "Formal Verification" (with Tom Scott or similar)**

## 📖 Read — Primary

- **"Logic and Structure" by van Dalen** — Chapters 1–3
  - *Clear, standard introduction.*
- **"A Mathematical Introduction to Logic" by Enderton** — Chapters 1–2
  - *More thorough, excellent reference.*

## 🔨 Do

- Build a truth table evaluator in Python. Verify De Morgan's laws, the contrapositive, and the material conditional.
- Formalize in predicate logic: "Every student who studies passes the exam." "There exists a model that is both accurate and interpretable." "No alignment technique works for all possible objective functions."
- Implement resolution (a proof method for propositional logic): given a set of clauses, derive new clauses until you find a contradiction (unsatisfiable) or exhaust possibilities (satisfiable).
- Write a formal specification for a simple AI behavior: "the chatbot never reveals personal information and always responds to greetings." Discuss what the specification misses.
