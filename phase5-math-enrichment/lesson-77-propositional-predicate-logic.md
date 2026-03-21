# Lesson 77: Propositional and Predicate Logic

[<- Computational Complexity](lesson-76-computational-complexity.md) | [Back to TOC](../README.md) | [Next: Proof Systems ->](lesson-78-proof-systems.md)

---

> **Why this lesson exists:** Logic is the bedrock of formal reasoning about AI systems. When we want to specify what an AI should or should not do, we need a precise language -- not English, which is riddled with ambiguity, but formal logic. Propositional and predicate logic give us that language. SAT solvers (which decide propositional satisfiability) are workhorses inside modern AI verification pipelines. Predicate logic extends the reach to statements about all possible inputs, all possible states, all possible futures -- exactly the kind of universal guarantees alignment researchers need. Without fluency in these systems, you cannot read or write formal specifications of AI behavior, and you cannot engage with the verification literature that attempts to prove AI systems safe.

> **Estimated time:** 10--15 hours

---

## Part 1: Propositional Logic -- Syntax

### The Alphabet

Propositional logic starts with a surprisingly small toolkit:

- **Propositional variables:** p, q, r, s, ... (each represents a statement that is either true or false)
- **Logical connectives:** NOT (negation), AND (conjunction), OR (disjunction), IMPLIES (conditional), IFF (biconditional)
- **Parentheses:** ( and ) for grouping

Common notation varies across textbooks. Here is a reference table:

| English     | Symbol  | Alternative | Precedence (lower = binds tighter) |
|-------------|---------|-------------|-------------------------------------|
| NOT         | ~p      | -p          | 1 (tightest)                        |
| AND         | p ^ q   | p & q       | 2                                   |
| OR          | p v q   | p \| q      | 3                                   |
| IMPLIES     | p -> q  |             | 4                                   |
| IFF         | p <-> q |             | 5 (loosest)                         |

### Well-Formed Formulas (WFFs)

Not every string of symbols is a valid formula. A **well-formed formula** is defined recursively:

1. Every propositional variable standing alone is a WFF. (Base case.)
2. If A is a WFF, then ~A is a WFF.
3. If A and B are WFFs, then (A ^ B), (A v B), (A -> B), and (A <-> B) are WFFs.
4. Nothing else is a WFF.

This recursive definition is your first taste of **structural induction** -- a proof technique where you prove something about all WFFs by proving it for the base case (variables) and then proving that each connective rule preserves the property.

**Example:** Is `p -> (q ^ ~r)` a WFF?
- r is a WFF (rule 1)
- ~r is a WFF (rule 2, applied to r)
- q is a WFF (rule 1)
- q ^ ~r is a WFF (rule 3, applied to q and ~r)
- p is a WFF (rule 1)
- p -> (q ^ ~r) is a WFF (rule 3, applied to p and q ^ ~r)

Yes. Every step follows the rules. This kind of pedantic checking matters when you build automated tools that parse logical formulas -- which is exactly what happens inside formal verification systems for AI.

### Parse Trees

Every WFF can be represented as a tree. The root is the main connective (the one with the widest scope), and the leaves are propositional variables. For `p -> (q ^ ~r)`:

```
       ->
      /  \
     p    ^
         / \
        q   ~
            |
            r
```

Parse trees eliminate all ambiguity. When you write code for a SAT solver or a theorem prover, you are working with parse trees (or their equivalent data structures), not strings.

---

## Part 2: Propositional Logic -- Semantics

### Truth Assignments

A **truth assignment** (also called a **valuation** or **interpretation**) is a function that maps every propositional variable to either True (T) or False (F).

Given a truth assignment, you can compute the truth value of any WFF by working up from the leaves of the parse tree, applying the truth table for each connective.

### Truth Tables for Connectives

| p | q | ~p | p ^ q | p v q | p -> q | p <-> q |
|---|---|----|-------|-------|--------|---------|
| T | T | F  | T     | T     | T      | T       |
| T | F | F  | F     | T     | F      | F       |
| F | T | T  | F     | T     | T      | F       |
| F | F | T  | F     | F     | T      | T       |

The one that trips people up most is **implication**. "p -> q" is false ONLY when p is true and q is false. When p is false, the implication is vacuously true regardless of q. This is not a quirk -- it is the definition that makes the connective maximally useful in mathematics. If an AI's specification says "if the user requests X, the system does Y," that specification is satisfied whenever the user does not request X.

### Tautologies, Contradictions, and Contingencies

- A **tautology** is a WFF that is true under every possible truth assignment. Example: p v ~p.
- A **contradiction** is a WFF that is false under every possible truth assignment. Example: p ^ ~p.
- A **contingency** is a WFF that is true under some assignments and false under others. Example: p -> q.

### Logical Equivalence

Two WFFs A and B are **logically equivalent** (written A === B or A <=> B) if they have the same truth value under every truth assignment. Equivalently, A <-> B is a tautology.

Key equivalences you should internalize:

- **Double negation:** ~~p === p
- **De Morgan's Laws:** ~(p ^ q) === ~p v ~q and ~(p v q) === ~p ^ ~q
- **Commutativity:** p ^ q === q ^ p and p v q === q v p
- **Associativity:** (p ^ q) ^ r === p ^ (q ^ r)
- **Distributivity:** p ^ (q v r) === (p ^ q) v (p ^ r) and p v (q ^ r) === (p v q) ^ (p v r)
- **Implication elimination:** p -> q === ~p v q
- **Contrapositive:** p -> q === ~q -> ~p

These are not just abstract facts. SAT solvers repeatedly apply equivalences like these to simplify formulas before attempting to solve them. The efficiency of modern SAT solving -- which underlies much AI verification -- depends on clever use of these identities.

---

## Part 3: Normal Forms

### Literals and Clauses

A **literal** is a propositional variable or its negation: p, ~p, q, ~q, etc.

A **clause** is a disjunction (OR) of literals: p v ~q v r.

### Conjunctive Normal Form (CNF)

A formula is in **CNF** if it is a conjunction (AND) of clauses:

(p v ~q) ^ (~p v r) ^ (q v r v ~s)

Every propositional formula can be converted to an equivalent formula in CNF.

**Why CNF matters:** Virtually every modern SAT solver takes its input in CNF. The DIMACS format, which is the standard file format for SAT solver input, represents CNF formulas. If you want to use a SAT solver to verify a property of an AI system, you must first express that property in CNF.

### Disjunctive Normal Form (DNF)

A formula is in **DNF** if it is a disjunction (OR) of conjunctions (AND) of literals:

(p ^ ~q) v (~p ^ r) v (q ^ r ^ ~s)

DNF is useful in some contexts (e.g., representing the "winning conditions" of a game), but less central to modern AI verification than CNF.

### Conversion Algorithm (to CNF)

1. Eliminate implications: replace A -> B with ~A v B, and A <-> B with (A -> B) ^ (B -> A).
2. Push negations inward using De Morgan's laws until negations apply only to variables.
3. Distribute OR over AND repeatedly until you have a conjunction of disjunctions.

The worst case for step 3 is an exponential blowup in formula size. This is one reason SAT solving is hard in general (it is NP-complete), but modern solvers use clever tricks like the Tseitin transformation to avoid the worst-case blowup by introducing auxiliary variables.

---

## Part 4: Satisfiability

### The SAT Problem

Given a propositional formula F, is there any truth assignment that makes F true?

- If yes, F is **satisfiable**.
- If no, F is **unsatisfiable** (i.e., a contradiction).

**The Cook-Levin Theorem** (which you may have seen in the complexity lesson) establishes that SAT is NP-complete. This means it is among the hardest problems in NP -- every problem in NP can be reduced to SAT.

### SAT Solvers and AI

Despite NP-completeness, modern SAT solvers (MiniSat, CaDiCaL, Kissat) can solve instances with millions of variables in practice. They use techniques including:

- **Unit propagation:** If a clause has only one unassigned literal, that literal must be true.
- **Boolean constraint propagation:** Chain unit propagation across the formula.
- **Conflict-Driven Clause Learning (CDCL):** When a contradiction is reached, analyze the conflict and learn a new clause that prevents the same mistake.
- **Backjumping:** Instead of backtracking one step, jump back to the decision that caused the conflict.

In AI alignment, SAT solvers and their extensions (SMT solvers, which handle richer theories) are used for:

- Verifying properties of neural networks (e.g., robustness to small input perturbations)
- Checking that a planning system's output satisfies safety constraints
- Model checking temporal properties of AI systems

---

## Part 5: Predicate Logic -- Syntax

### Why Predicate Logic?

Propositional logic cannot express statements like "every AI system that passes test X is safe" or "there exists an input that causes the system to fail." For that, we need **predicate logic** (also called **first-order logic** or **FOL**).

### New Ingredients

Predicate logic adds to propositional logic:

- **Variables** (ranging over a domain of objects): x, y, z, ...
- **Constants** (naming specific objects): a, b, c, ...
- **Predicates** (properties and relations): P(x), Q(x, y), Safe(s), Aligned(a), ...
- **Functions** (mapping objects to objects): f(x), g(x, y), ...
- **Quantifiers:**
  - Universal quantifier: "for all x" (written with the symbol that looks like an upside-down A)
  - Existential quantifier: "there exists an x" (written with a backwards E)

### Terms and Formulas

A **term** is a variable, a constant, or a function applied to terms. Terms name objects.

An **atomic formula** is a predicate applied to terms: P(a), Q(x, f(y)), Equal(x, y).

Well-formed formulas are built from atomic formulas using connectives (as before) and quantifiers.

### Free and Bound Variables

A variable x is **bound** if it falls within the scope of a quantifier over x. Otherwise it is **free**.

In the formula: (for all x)(P(x) -> Q(x, y))
- x is bound (it is quantified)
- y is free (no quantifier binds it)

A **sentence** (or **closed formula**) is a formula with no free variables. Sentences have definite truth values in a given interpretation; formulas with free variables do not -- they are like functions waiting for arguments.

### Scope and Parentheses

The scope of a quantifier extends as far to the right as possible, or until closed by a parenthesis. Be precise about scope:

- (for all x)(P(x) -> Q(x)) means: for every x, if P(x) then Q(x)
- (for all x)(P(x)) -> Q(x) means: (if every x has property P) then Q(x) -- but here x in Q(x) is free, which is likely a mistake

Sloppy scoping is a common source of errors in formal specifications. When writing specifications for AI systems, getting quantifier scope wrong can be the difference between "the system is safe for all inputs" and something much weaker.

---

## Part 6: Predicate Logic -- Semantics

### Structures and Interpretations

A **structure** (or **model**) for a first-order language consists of:

1. A **domain** (or **universe**) D -- a nonempty set of objects
2. An interpretation of each constant as an element of D
3. An interpretation of each function symbol as a function on D
4. An interpretation of each predicate symbol as a relation on D

**Example:** Let the language have a constant a, a unary predicate P, and a binary predicate R.

A structure might be:
- D = {1, 2, 3}
- a = 1
- P = {1, 3} (i.e., P is true of 1 and 3)
- R = {(1,2), (2,3)} (i.e., R holds between 1 and 2, and between 2 and 3)

### Evaluating Formulas

Given a structure and an assignment of free variables to domain elements:

- P(a) is true iff the interpretation of a is in the interpretation of P
- (for all x) F(x) is true iff F(d) is true for every d in the domain
- (there exists x) F(x) is true iff F(d) is true for at least one d in the domain

### Validity vs. Satisfiability

- A sentence is **satisfiable** if there exists some structure in which it is true.
- A sentence is **valid** if it is true in every structure.
- A sentence is **unsatisfiable** if there is no structure in which it is true.

Validity in predicate logic is the analog of tautology in propositional logic. The relationship between validity and satisfiability is: A is valid if and only if ~A is unsatisfiable.

---

## Part 7: Prenex Normal Form

A formula is in **prenex normal form** if all quantifiers are at the front:

(for all x)(there exists y)(for all z) [quantifier-free part]

The quantifier-free part is called the **matrix**. Any first-order formula can be converted to prenex normal form using equivalences like:

- ~(for all x) F(x) === (there exists x) ~F(x)
- ~(there exists x) F(x) === (for all x) ~F(x)
- (for all x) F(x) ^ G === (for all x)(F(x) ^ G) [when x is not free in G]

Prenex normal form is important in automated theorem proving and in understanding the complexity of logical theories (the prenex quantifier prefix determines which decision procedures apply).

---

## Part 8: Connecting to AI Alignment

### Formal Specifications

When alignment researchers write "the AI should never take action A in state S," they are implicitly writing a first-order sentence:

(for all s)(for all a)(State(s) ^ Action(a) ^ InState(s) -> ~Takes(system, a))

Making these specifications formal and precise is the first step toward verifying them. Ambiguity in natural-language specifications is a major source of alignment failures -- the system optimizes for what was literally specified, not what was intended.

### SAT/SMT Solving for Neural Network Verification

Tools like Marabou and alpha-beta-CROWN encode neural network verification problems as SAT/SMT instances. For example, to verify that a neural network classifier is robust (small input perturbations do not change the output), the problem is encoded as: "does there exist an input within epsilon of the original input such that the network's output differs?" This is a satisfiability question.

### Logic-Based AI Safety

Some approaches to AI safety use logical frameworks directly. For instance, logical induction (Garrabrant et al., 2016) uses logical sentences as the objects that an AI reasons about. Understanding predicate logic is a prerequisite for engaging with this literature.

---

## Watch -- Primary

- **Trefor Bazzett -- Logic playlist** (YouTube): Covers propositional logic, truth tables, quantifiers, and predicate logic with clear visual explanations. Work through the videos on connectives, truth tables, quantifiers, and validity.

## Read -- Primary

- Any standard discrete mathematics or mathematical logic textbook, such as:
  - Rosen, "Discrete Mathematics and Its Applications," Chapters 1.1--1.5
  - Enderton, "A Mathematical Introduction to Logic," Chapters 1--2 (more rigorous)

---

## Exercises

1. **Truth table construction:** Build complete truth tables for the following formulas and classify each as a tautology, contradiction, or contingency:
   - (p -> q) <-> (~q -> ~p)
   - (p -> q) ^ (q -> r) -> (p -> r)
   - p ^ ~p
   - (p v q) ^ (~p v r) -> (q v r)

2. **CNF conversion:** Convert the following formula to CNF, showing each step:
   - (p -> q) ^ (q -> r) -> (p -> r)
   First eliminate implications, then push negations inward, then distribute.

3. **Logical equivalence:** Prove using truth tables that p -> (q -> r) is logically equivalent to (p ^ q) -> r. Then prove it algebraically using the equivalences listed above.

4. **Predicate logic translation:** Translate the following English sentences into predicate logic:
   - "Every safe AI system has been formally verified."
   - "There exists an input that causes the system to produce an unsafe output."
   - "For every specification, either the system satisfies it or there is a counterexample."

5. **Free and bound variables:** For each formula, identify the free and bound variables:
   - (for all x)(P(x, y) -> (there exists z) Q(z, x))
   - (there exists x)(R(x) ^ (for all y) S(x, y)) -> T(x)
   - (for all x)(there exists y)(P(x, y) -> (for all x) Q(x))

6. **Satisfiability check:** Consider the set of clauses {p v q, ~p v r, ~q v ~r, ~p v ~q}. Is this set satisfiable? Find a satisfying assignment or prove unsatisfiability by resolution.

7. **AI alignment formalization:** Write a first-order specification for the following informal requirement: "The system never takes an action that it predicts will reduce human well-being, unless the human has explicitly authorized that action." Identify the predicates, quantifiers, and potential ambiguities in your formalization.

8. **Prenex normal form:** Convert the following to prenex normal form:
   - ~(for all x)(P(x) -> (there exists y) Q(x, y))
   Show each step and verify your answer is equivalent to the original.
