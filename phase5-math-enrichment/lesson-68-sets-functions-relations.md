# Lesson 68: Sets, Functions, and Relations — The Scaffolding of Mathematical Structure

[← Logic & Propositions](lesson-67-logic-propositions.md) | [Back to TOC](../README.md) | [Next: Combinatorics →](lesson-69-combinatorics.md)

---

> **Why this lesson exists:** Nearly every mathematical concept in machine learning — vector spaces, probability spaces, function classes, hypothesis sets — is defined in terms of sets, functions, and relations. When an alignment researcher writes about the "set of all possible reward functions" or asks whether two models are "equivalent up to some relation," they are using the exact vocabulary this lesson teaches. Mastering these foundational structures lets you read and write mathematical arguments about AI systems with precision.

> **Estimated time:** 12–18 hours

---

## Part 1: Sets — Collections with Precision

### What Is a Set?

A **set** is an unordered collection of distinct objects, called **elements** or **members**. We write "x is in S" (using the element-of symbol) to mean x is a member of set S.

Sets can be described by:
- **Roster notation:** {1, 2, 3, 4, 5}
- **Set-builder notation:** {x in Z : x > 0 and x <= 5} (read: "the set of integers x such that x is greater than 0 and at most 5")

Important standard sets:
- **N** = {0, 1, 2, 3, ...} — natural numbers (conventions vary on whether 0 is included)
- **Z** = {..., -2, -1, 0, 1, 2, ...} — integers
- **Q** = {p/q : p, q in Z, q != 0} — rationals
- **R** — real numbers
- **The empty set** (denoted with the empty-set symbol) — the set with no elements

### Set Operations

Let A and B be sets within some universal set U.

**Union:** A union B = {x : x in A or x in B}
- Contains everything in either set (or both)

**Intersection:** A intersect B = {x : x in A and x in B}
- Contains only elements in both sets

**Complement:** A^c = {x in U : x not in A}
- Everything in the universe that is NOT in A

**Set Difference:** A \ B = {x : x in A and x not in B}
- Elements in A that are not in B

**Symmetric Difference:** A triangle B = (A \ B) union (B \ A)
- Elements in exactly one of the two sets, but not both

### De Morgan's Laws for Sets

Just as we had De Morgan's laws for logic, we have them for sets:
- (A union B)^c = A^c intersect B^c
- (A intersect B)^c = A^c union B^c

This is not a coincidence. Set operations *are* logical operations applied element-by-element: "x in A union B" is the same as "x in A OR x in B." The structural parallel between logic and set theory runs deep.

### Power Set

The **power set** of A, written P(A), is the set of all subsets of A.

If A = {1, 2, 3}, then P(A) = {empty set, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}.

**Key fact:** If |A| = n, then |P(A)| = 2^n. Each element is either included or excluded — n binary choices give 2^n subsets. This exponential blowup is important: the space of possible subsets grows enormously fast, which connects to the combinatorial explosion we will study in the next lesson.

### Cartesian Product

The **Cartesian product** A x B is the set of all ordered pairs (a, b) where a is in A and b is in B.

If A = {1, 2} and B = {x, y, z}, then A x B = {(1,x), (1,y), (1,z), (2,x), (2,y), (2,z)}.

**Key fact:** |A x B| = |A| * |B|.

You already use Cartesian products constantly: R^n = R x R x ... x R is the set of n-dimensional real vectors. When you write a weight matrix's domain as R^(m x n), you are working with a Cartesian product structure. The input-output space of a neural network is a Cartesian product of the input space and output space.

### Subsets and Equality

A is a **subset** of B (written A is a subset of B) if every element of A is also in B.

A = B if and only if A is a subset of B and B is a subset of A. This "double inclusion" proof strategy is one of the most common ways to prove two sets are equal.

---

## Part 2: Functions — The Maps Between Structures

### Definition and Notation

A **function** f from set A to set B (written f: A -> B) is a rule that assigns to each element of A exactly one element of B.

- **A** is the **domain**
- **B** is the **codomain**
- For a in A, f(a) is the **image** of a
- The **range** (or image) of f is {f(a) : a in A}, which may be a proper subset of B

**Critical point:** Every element of the domain must be mapped to *exactly one* element of the codomain. "Exactly one" means the function is well-defined (no ambiguity) and total (no domain element is left unmapped).

### Injective, Surjective, Bijective

These three properties classify functions by how they "cover" their domain and codomain.

**Injective (one-to-one):** f is injective if different inputs always produce different outputs. Formally: if f(a1) = f(a2), then a1 = a2 (equivalently, if a1 != a2, then f(a1) != f(a2)).

*Intuition:* No two arrows point to the same target. No information is lost — you could in principle recover the input from the output.

*ML connection:* An injective encoder preserves all information about its input. If a representation function is injective, no two distinct inputs collapse to the same representation.

**Surjective (onto):** f is surjective if every element of the codomain is hit by at least one element of the domain. Formally: for every b in B, there exists a in A such that f(a) = b.

*Intuition:* Every target has at least one arrow pointing to it. The range equals the codomain — nothing is "missed."

**Bijective (one-to-one and onto):** f is bijective if it is both injective and surjective. Every element of B is hit by exactly one element of A.

*Intuition:* A perfect pairing. Bijections establish that two sets have the "same size" (same cardinality).

*ML connection:* Normalizing flows in generative modeling use bijective transformations — they map between a simple distribution and a complex one without losing any information, which allows exact likelihood computation.

### Composition and Inverse

**Composition:** Given f: A -> B and g: B -> C, the composition g composed with f (written g of f) maps A -> C by (g composed with f)(a) = g(f(a)).

Composition is like a pipeline: first apply f, then apply g to the result. Neural networks are fundamentally compositions of functions — layer 1 feeds into layer 2 feeds into layer 3, and so on. The entire network is a single composed function from input to output.

**Inverse:** If f: A -> B is bijective, there exists an inverse function f^(-1): B -> A such that f^(-1)(f(a)) = a for all a in A and f(f^(-1)(b)) = b for all b in B.

Only bijective functions have inverses. If f is not injective, you cannot uniquely recover the input. If f is not surjective, the inverse would have undefined points.

### Connection to Type Theory in Programming

In typed programming languages, function types are written similarly: `f :: A -> B` in Haskell declares a function from type A to type B. The concepts of injectivity, surjectivity, and composition carry over directly. Understanding functions as precise mappings between sets is the mathematical foundation of type theory, which in turn is the foundation of verified software — software that is *proven* correct, a key goal in AI safety.

---

## Part 3: Relations — Generalizing Connections

### What Is a Relation?

A (binary) **relation** R on a set A is a subset of A x A. If (a, b) is in R, we write aRb and say "a is related to b."

Functions are special cases of relations (where each a has exactly one b). But relations are more general — an element can be related to zero, one, or many elements.

**Examples:**
- "Less than" on the integers: aRb means a < b
- "Is a prerequisite of" on a set of courses
- "Has the same number of parameters as" on a set of neural networks

### Properties of Relations

A relation R on set A can have the following properties:

**Reflexive:** aRa for every a in A.
- "equals" is reflexive (a = a always)
- "less than" is NOT reflexive (a < a is false)

**Symmetric:** if aRb then bRa.
- "is a sibling of" is symmetric
- "less than" is NOT symmetric

**Antisymmetric:** if aRb and bRa, then a = b.
- "less than or equal to" is antisymmetric (if a <= b and b <= a, then a = b)
- Note: antisymmetric is NOT the negation of symmetric. A relation can be both symmetric and antisymmetric (e.g., equality), or neither.

**Transitive:** if aRb and bRc, then aRc.
- "less than" is transitive (if a < b and b < c, then a < c)
- "is a friend of" on social networks is NOT necessarily transitive

### Equivalence Relations and Equivalence Classes

An **equivalence relation** is a relation that is reflexive, symmetric, and transitive. Equivalence relations formalize the idea of "sameness" or "interchangeability" with respect to some criterion.

**Examples:**
- Equality (=) is the trivial equivalence relation
- Congruence modulo n: a is equivalent to b (mod n) if n divides (a - b). This is reflexive (a - a = 0 is divisible by n), symmetric (if n | (a-b) then n | (b-a)), and transitive (if n | (a-b) and n | (b-c), then n | (a-c)).
- "Has the same architecture as" on neural networks (if you define architecture precisely)

Given an equivalence relation ~ on A, the **equivalence class** of a (written [a]) is the set of all elements equivalent to a:

[a] = {x in A : x ~ a}

**The Fundamental Theorem:** The equivalence classes of ~ form a **partition** of A — they are disjoint, non-empty, and their union is all of A. Conversely, every partition of A defines an equivalence relation (elements are equivalent if and only if they are in the same part).

**ML connection:** In representation learning, a good representation collapses "equivalent" inputs into the same (or nearby) representations. When we say two images belong to the same class, we are defining an equivalence relation on the image space. The equivalence classes are precisely the categories the classifier must distinguish. Dimensionality reduction can be viewed as quotienting a high-dimensional space by an equivalence relation that identifies "similar enough" points.

### Partial Orders and Hasse Diagrams

A **partial order** is a relation that is reflexive, antisymmetric, and transitive. A set with a partial order is called a **partially ordered set (poset)**.

**Examples:**
- (Z, <=) — integers with the usual "less than or equal to"
- (P(S), subset-of) — the power set of S ordered by inclusion
- (N, divides) — natural numbers ordered by divisibility

The word "partial" means not every pair of elements need be comparable. In (N, divides), 3 and 5 are incomparable — neither divides the other. A **total order** (or linear order) is a partial order where every pair IS comparable (like the usual <= on integers).

A **Hasse diagram** visually represents a finite poset:
- Elements are dots
- If a < b and there is no c with a < c < b (i.e., b "covers" a), draw a line from a up to b
- Transitivity is implicit — you do not draw lines for relationships that can be deduced

Hasse diagrams make the structure of a partial order immediately visible. For instance, the Hasse diagram of (P({1,2,3}), subset-of) looks like a cube — this is the Boolean lattice, which appears throughout combinatorics and information theory.

---

## Part 4: Cardinality and Infinite Sets (Brief Introduction)

### Finite Sets

For finite sets, cardinality is just the count of elements: |{a, b, c}| = 3.

### Countable and Uncountable Infinity

Two sets have the same cardinality if there exists a bijection between them. This works even for infinite sets, leading to surprising results:

- **N and Z have the same cardinality** (you can biject them: 0 -> 0, 1 -> 1, 2 -> -1, 3 -> 2, 4 -> -2, ...)
- **N and Q have the same cardinality** (Cantor's diagonal/zigzag argument)
- **N and R do NOT have the same cardinality** (Cantor's diagonal argument shows R is "bigger" — uncountably infinite)

This means the real numbers are a fundamentally "larger" infinity than the rationals or integers. The set of all possible functions from N to {0, 1} is uncountable (it bijects with the reals). The set of all possible Turing machines is countable. Therefore, there exist functions that no Turing machine can compute — this is the foundation of uncomputability, which has deep implications for what AI systems can and cannot do in principle.

---

## Watch — Primary

1. **Trefor Bazzett — "Discrete Math" playlist (sets, functions, and relations sections)**
   - *Clear visual presentations of set operations, function properties, equivalence relations, and partial orders*

## Read — Primary

- **"Discrete Mathematics and Its Applications" by Kenneth Rosen** — Chapters 2 and 9
  - *Chapter 2 covers sets and functions; Chapter 9 covers relations. Work the exercises — they are well-calibrated.*

- **"How to Prove It" by Daniel Velleman** — Chapters 4–5
  - *Focused treatment of relations and functions with an emphasis on proof techniques involving these objects.*

## Read — Supplementary

- **"Naive Set Theory" by Paul Halmos**
  - *A classic short book on set theory. Readable and develops strong intuition for working with sets at a deeper level.*

## Exercises

1. Let A = {1, 2, 3, 4, 5} and B = {3, 4, 5, 6, 7}. Compute A union B, A intersect B, A \ B, B \ A, and A symmetric-difference B. Verify De Morgan's laws hold for these sets with U = {1, 2, ..., 10}.

2. Write out P({a, b}) (the power set). Verify it has 2^2 = 4 elements. Then describe (without listing all elements) why |P({1, 2, ..., 10})| = 1024.

3. Prove that for any sets A, B, C: A intersect (B union C) = (A intersect B) union (A intersect C). Use the element-chasing method (show that x in the LHS implies x in the RHS, and vice versa).

4. Determine whether each function is injective, surjective, both, or neither:
   - f: R -> R defined by f(x) = x^3
   - g: R -> R defined by g(x) = x^2
   - h: Z -> Z defined by h(n) = 2n + 1
   - k: R -> [0, infinity) defined by k(x) = x^2

5. Let f: A -> B and g: B -> C. Prove that:
   - If g composed with f is injective, then f is injective.
   - If g composed with f is surjective, then g is surjective.
   - Give examples showing the converses are false.

6. Determine whether each relation on Z is reflexive, symmetric, antisymmetric, and/or transitive:
   - aRb if and only if a + b is even
   - aRb if and only if a divides b
   - aRb if and only if |a - b| <= 1

7. Prove that "a is equivalent to b mod 5" is an equivalence relation on Z. List all equivalence classes.

8. Draw the Hasse diagram for (P({1, 2, 3}), subset-of). Identify all maximal chains (sequences of elements where each is a subset of the next, of maximum length).

9. Prove that if f: A -> B is a bijection, then f^(-1): B -> A is also a bijection.

10. (Challenge) Consider the set of all neural network architectures with at most n layers and at most m neurons per layer (for fixed n and m). Define an equivalence relation where two architectures are equivalent if they compute the same function. Discuss (informally) whether the number of equivalence classes is finite, countably infinite, or uncountably infinite, and what this implies about the "true diversity" of neural network behaviors in this class.
