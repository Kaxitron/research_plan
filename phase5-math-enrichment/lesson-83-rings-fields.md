# Lesson 83: Rings and Fields

[<-- Homomorphisms](lesson-82-homomorphisms.md) | [Back to TOC](../README.md) | [Next: Group Actions -->](lesson-84-group-actions.md)

---

> **Why this lesson exists:** Rings and fields extend group theory by introducing a second operation, giving us the algebraic framework for polynomials, modular arithmetic, and linear algebra over arbitrary fields. In AI alignment research, polynomial rings are the foundation of algebraic geometry, which is the mathematical language of Singular Learning Theory (SLT). The resolution of singularities -- a key technique in SLT for computing the real log canonical threshold (RLCT) that governs model complexity -- relies on manipulating polynomial ideals and working over various fields. Finite fields appear in error-correcting codes and cryptographic protocols relevant to AI safety infrastructure. This lesson builds the algebraic vocabulary required for the geometric and analytic tools ahead.

> **Estimated time:** 15--20 hours

---

## Part 1: Ring Definition and Examples

### What Is a Ring?

A **ring** (R, +, *) is a set R equipped with two binary operations (addition and multiplication) satisfying:

1. **(R, +) is an abelian group:** Addition is associative, commutative, has identity 0, and every element has an additive inverse.
2. **Multiplication is associative:** (a * b) * c = a * (b * c) for all a, b, c.
3. **Multiplication has an identity:** There exists 1 in R with 1 * a = a * 1 = a for all a. (Some authors omit this; we include it.)
4. **Distributive laws:** a * (b + c) = a * b + a * c and (a + b) * c = a * c + b * c for all a, b, c.

Note: Multiplication need NOT be commutative. A ring where multiplication is commutative is called a **commutative ring**.

### Comparison with Groups

A ring is considerably richer than a group: it has two interlinked operations. The additive structure forms an abelian group, and multiplication distributes over addition. The multiplicative structure need not form a group (not every nonzero element needs an inverse).

### The Integers Z

The most basic example. Z is a commutative ring with identity:
- Addition: the usual abelian group (Z, +).
- Multiplication: associative, commutative, with identity 1.
- Not every nonzero element has a multiplicative inverse (e.g., 2 has no inverse in Z).

### Modular Arithmetic Z_n

The set Z_n = {0, 1, ..., n-1} with addition and multiplication modulo n is a commutative ring. The key question: when does Z_n have "nice" multiplicative structure?

- Z_n is an **integral domain** (no zero divisors) if and only if n is prime.
- Z_n is a **field** (every nonzero element has a multiplicative inverse) if and only if n is prime.

For composite n, there are zero divisors. In Z_6, for instance, 2 * 3 = 0 even though neither 2 nor 3 is zero.

### Polynomial Rings R[x]

Given a ring R, the **polynomial ring** R[x] consists of all polynomials with coefficients in R:

a_n x^n + a_{n-1} x^{n-1} + ... + a_1 x + a_0

with the usual addition and multiplication of polynomials.

Key facts:
- If R is commutative, so is R[x].
- If R is an integral domain, so is R[x].
- R[x] is never a field (the polynomial x has no multiplicative inverse).
- We can iterate: R[x][y] = R[x, y] is the ring of polynomials in two variables.

Polynomial rings are central to algebraic geometry and therefore to SLT. The zero sets of polynomials define algebraic varieties, and the singularities of these varieties govern learning machine behavior.

### Matrix Rings M_n(R)

The set of all n x n matrices with entries from a ring R forms a ring M_n(R):
- Addition is entry-wise.
- Multiplication is matrix multiplication.
- The identity is I_n.

For n >= 2, M_n(R) is **non-commutative** even when R is commutative. This is the prototypical example of a non-commutative ring.

### Further Examples

- **Gaussian integers Z[i]** = {a + bi : a, b in Z}. A commutative ring (in fact, a Euclidean domain) that plays a role in algebraic number theory.
- **Formal power series R[[x]]**: like polynomials but allowing infinitely many terms. A power series is invertible if and only if its constant term is invertible in R.
- **Function rings:** The set of all continuous functions from R to R forms a ring under pointwise addition and multiplication.

## Part 2: Ideals

### Definition

An **ideal** I of a ring R is a subring of R (under addition) that "absorbs" multiplication:

- (I, +) is a subgroup of (R, +).
- For all r in R and a in I, both r * a and a * r are in I.

Ideals are the ring-theoretic analogue of normal subgroups. Just as normal subgroups are kernels of group homomorphisms, ideals are kernels of ring homomorphisms.

### Examples

1. **nZ is an ideal of Z** for any integer n. Every ideal of Z has this form (Z is a **principal ideal domain**).

2. **The zero ideal {0}** and the **whole ring R** are always ideals (the trivial ideals).

3. **In R[x], the ideal (x^2 + 1)** consists of all multiples of x^2 + 1. The quotient R[x]/(x^2 + 1) is isomorphic to C, the complex numbers.

4. **In Z[x], the ideal (2, x)** consists of all polynomials with even constant term. This ideal is NOT principal -- it cannot be generated by a single element.

### Types of Ideals

- **Principal ideal:** Generated by a single element. (a) = {r * a : r in R} in a commutative ring.
- **Prime ideal:** An ideal P such that if ab is in P, then a is in P or b is in P. (Analogue of prime numbers.)
- **Maximal ideal:** An ideal M that is not contained in any strictly larger proper ideal.

**Key facts:**
- Every maximal ideal is prime.
- R/P is an integral domain if and only if P is prime.
- R/M is a field if and only if M is maximal.

These characterizations are fundamental to algebraic geometry, where prime ideals correspond to irreducible algebraic varieties.

### Generating Ideals

An ideal generated by elements a_1, ..., a_k is:

(a_1, ..., a_k) = {r_1 a_1 + ... + r_k a_k : r_i in R}

This is the smallest ideal containing all the generators. Ideals generated by finitely many elements are called **finitely generated**.

## Part 3: Quotient Rings

### Construction

If I is an ideal of R, the **quotient ring** R/I consists of cosets r + I = {r + a : a in I} with operations:

(r_1 + I) + (r_2 + I) = (r_1 + r_2) + I
(r_1 + I) * (r_2 + I) = (r_1 * r_2) + I

The fact that I is an ideal (not just a subgroup) is what makes multiplication well-defined.

### Key Examples

1. **Z/nZ ≅ Z_n.** This is the formal construction of modular arithmetic.

2. **R[x]/(x^2 + 1) ≅ C.** In this quotient, x^2 + 1 = 0 (it is in the zero coset), so x^2 = -1. The element x plays the role of i. Every element can be written as a + bx (reducing higher powers using x^2 = -1), giving the complex numbers.

3. **R[x]/(x^2 - 1) ≅ R x R.** Here x^2 = 1, so x = +1 or x = -1. The quotient splits into two copies of R via the Chinese Remainder Theorem.

4. **Z[x]/(x^2 + 1) ≅ Z[i].** The Gaussian integers arise as a quotient ring.

### The Quotient as "Setting Relations"

Taking a quotient R/I is the algebraic operation of "imposing relations." We declare that all elements of I equal zero, and see what ring remains. This is exactly how algebraic geometers work: the ring of functions on a variety is a quotient ring where the defining equations of the variety are set to zero.

## Part 4: Ring Homomorphisms

### Definition

A **ring homomorphism** f: R --> S is a function preserving both operations:

- f(a + b) = f(a) + f(b)
- f(a * b) = f(a) * f(b)
- f(1_R) = 1_S

The kernel ker(f) = {r in R : f(r) = 0_S} is always an ideal of R.

### First Isomorphism Theorem for Rings

**Theorem.** If f: R --> S is a ring homomorphism, then R/ker(f) ≅ im(f).

This is the exact analogue of the group version. The proof follows the same pattern: the natural map R/ker(f) --> im(f) sending r + ker(f) to f(r) is a well-defined ring isomorphism.

### Evaluation Homomorphisms

For a polynomial ring R[x], the **evaluation homomorphism** at a point a in R is:

ev_a: R[x] --> R, ev_a(p(x)) = p(a)

This is a surjective ring homomorphism. Its kernel is the ideal of polynomials vanishing at a:

ker(ev_a) = (x - a) when R is a field

By the First Isomorphism Theorem: R[x]/(x - a) ≅ R.

## Part 5: Integral Domains

### Definition

An **integral domain** is a commutative ring with identity (where 1 is not equal to 0) that has no **zero divisors**: if ab = 0 then a = 0 or b = 0.

### Why Zero Divisors Matter

Zero divisors break the cancellation law. In an integral domain, if ab = ac and a is nonzero, then b = c. This familiar algebraic manipulation fails in rings with zero divisors.

### Examples and Non-Examples

Integral domains: Z, Z[i], R[x], any field.
Not integral domains: Z_6 (since 2 * 3 = 0), M_n(R) for n >= 2.

### Fraction Fields

Every integral domain D can be embedded in a field -- its **field of fractions** Frac(D). The construction mimics building Q from Z:

Frac(D) = {a/b : a, b in D, b nonzero} / ~

where a/b ~ c/d if ad = bc.

- Frac(Z) = Q (the rational numbers).
- Frac(Z[i]) = Q(i) = {a + bi : a, b in Q}.
- Frac(R[x]) = R(x) (rational functions in x).

## Part 6: Fields

### Definition

A **field** is a commutative ring with identity (where 1 is not equal to 0) in which every nonzero element has a multiplicative inverse. Equivalently, (F \ {0}, *) is an abelian group.

Fields are the "nicest" rings: they support division (except by zero).

### Characteristic

The **characteristic** of a field F is the smallest positive integer p such that 1 + 1 + ... + 1 (p times) = 0 in F. If no such p exists, the characteristic is 0.

- char(Q) = char(R) = char(C) = 0.
- char(Z_p) = p for prime p.
- The characteristic of a field is always 0 or prime.

### Field Extensions

A **field extension** F/K (read "F over K") is a pair of fields where K is a subfield of F.

**Examples:**
- C/R (the complex numbers over the reals).
- Q(sqrt(2))/Q = {a + b*sqrt(2) : a, b in Q}, a degree-2 extension.
- R/Q (an infinite-degree extension).

The **degree** of a field extension [F : K] is the dimension of F as a vector space over K:
- [C : R] = 2 (basis {1, i}).
- [Q(sqrt(2)) : Q] = 2 (basis {1, sqrt(2)}).

### Algebraic and Transcendental Elements

An element alpha in F is **algebraic** over K if it satisfies a polynomial equation with coefficients in K. Otherwise, it is **transcendental**.

- sqrt(2) is algebraic over Q (satisfies x^2 - 2 = 0).
- pi and e are transcendental over Q (proofs are non-trivial).
- Every element of a finite field is algebraic over its prime subfield.

## Part 7: Finite Fields

### Existence and Uniqueness

**Theorem.** For every prime p and positive integer n, there exists a field with exactly p^n elements, denoted GF(p^n) or F_{p^n}. Moreover, this field is unique up to isomorphism.

There is NO finite field of order m unless m is a prime power.

### Construction

GF(p^n) is constructed as a quotient of Z_p[x]:

GF(p^n) ≅ Z_p[x] / (f(x))

where f(x) is an irreducible polynomial of degree n over Z_p.

**Example: GF(4).**
Over Z_2, the polynomial x^2 + x + 1 is irreducible (check: 0^2 + 0 + 1 = 1 and 1^2 + 1 + 1 = 1, both nonzero in Z_2).

GF(4) = Z_2[x]/(x^2 + x + 1) = {0, 1, alpha, alpha + 1}

where alpha^2 = alpha + 1 (since x^2 + x + 1 = 0 means x^2 = x + 1 in Z_2).

### Multiplicative Structure

The nonzero elements of GF(p^n) form a cyclic group of order p^n - 1 under multiplication. This is a powerful structural result with no analogue for general rings.

**Consequence:** GF(p^n)* = <g> for some generator g (a **primitive element**). Every nonzero element is a power of g.

### Applications

- **Error-correcting codes:** Reed-Solomon codes are built over finite fields, and their algebraic structure enables efficient error detection and correction.
- **Cryptography:** Elliptic curve cryptography uses elliptic curves over finite fields. Many post-quantum cryptographic schemes rely on algebraic structures over finite fields.
- **Combinatorics:** Finite geometries (projective planes, affine planes) are built using finite fields.

## Part 8: Polynomial Rings Over Fields

### Division Algorithm

If F is a field, then F[x] has a division algorithm: for any f(x) and nonzero g(x) in F[x], there exist unique q(x) and r(x) with:

f(x) = g(x) * q(x) + r(x), where deg(r) < deg(g) or r = 0.

This makes F[x] a **Euclidean domain**, with all the good properties that entails (PID, UFD).

### Greatest Common Divisor and the Euclidean Algorithm

The Euclidean algorithm works in F[x] just as in Z:

gcd(f, g) = gcd(g, f mod g)

This gives an efficient algorithm for computing polynomial GCDs, which is used in computational algebraic geometry (Grobner basis algorithms, resultants).

### Irreducibility

A polynomial p(x) in F[x] is **irreducible** if it cannot be factored as a product of two polynomials of lower degree in F[x]. Irreducible polynomials are the "primes" of polynomial rings.

**Unique Factorization:** Every nonzero polynomial in F[x] factors uniquely (up to order and units) as a product of irreducible polynomials.

Irreducibility depends on the field:
- x^2 + 1 is irreducible over R but factors as (x + i)(x - i) over C.
- x^2 + x + 1 is irreducible over Z_2 but factors as (x - alpha)(x - alpha^2) over GF(4).

### Connection to Algebraic Geometry

The zero set of a polynomial p(x_1, ..., x_n) in F[x_1, ..., x_n] is an **algebraic variety**. The ring of polynomial functions on this variety is the quotient ring F[x_1, ..., x_n]/(p). The interplay between ideals of polynomial rings and geometric properties of varieties is the subject of algebraic geometry -- and the foundation for SLT's analysis of learning machines.

## Part 9: Connection to AI Alignment

### Polynomial Rings and Singular Learning Theory

In SLT, the parameter-to-function map w --> f_w can often be described using polynomial (or analytic) equations. The set of optimal parameters -- those minimizing the loss function -- forms a variety (or analytic set) defined by polynomial-like equations.

The **real log canonical threshold** (RLCT), which governs model complexity in SLT, is computed by resolving the singularities of this variety. The resolution process involves working with polynomial rings, ideals, and quotient rings -- precisely the tools of this lesson.

### Finite Fields in AI Safety Infrastructure

Robust AI systems require reliable communication and computation:
- Error-correcting codes (built on finite fields) ensure data integrity.
- Cryptographic protocols (relying on finite field arithmetic) secure model weights, training data, and inference results.
- Verifiable computation schemes use algebraic structures over finite fields to prove that a computation was performed correctly -- relevant for auditing AI systems.

---

## Watch -- Primary

- **Matthew Macauley -- Visual Group Theory (ring and field lectures)**
  Macauley extends his visual approach to ring theory in his later lectures. These provide geometric intuition for ideals, quotient rings, and field extensions.

- **Michael Penn -- Rings and Fields videos**
  Penn's lectures are more algebraically detailed, covering integral domains, PIDs, UFDs, and field extensions with clear proofs and examples.

## Read -- Primary

- **Paolo Aluffi, "Algebra: Chapter 0," Chapters IV--V**
  Covers rings, ideals, quotient rings, integral domains, fields, and polynomial rings. Aluffi's approach emphasizes universal properties and functorial perspectives.

---

## Exercises

### Computational

1. Construct the addition and multiplication tables for Z_5. Verify that Z_5 is a field by finding the multiplicative inverse of each nonzero element.

2. Find all zero divisors in Z_15. Which elements are units (have multiplicative inverses)?

3. Construct GF(8) = Z_2[x]/(x^3 + x + 1). List all 8 elements and build the multiplication table for the nonzero elements. Find a primitive element (generator of the multiplicative group).

4. In Q[x], use the Euclidean algorithm to compute gcd(x^4 - 1, x^3 - 1).

5. List all ideals of Z_12. Which are prime? Which are maximal?

### Proof-Based

6. Prove that every field is an integral domain.

7. Prove that every finite integral domain is a field. (Hint: consider the map x --> ax for nonzero a, and use finiteness to show it is surjective.)

8. Prove that the characteristic of a field is either 0 or prime.

9. Prove the First Isomorphism Theorem for rings.

10. Prove that in a PID (principal ideal domain), every nonzero prime ideal is maximal.

### Conceptual

11. Explain why Z_6 is not an integral domain by finding zero divisors. Then explain how the Chinese Remainder Theorem gives an isomorphism Z_6 ≅ Z_2 x Z_3, and why the direct product of two fields is never a field.

12. The construction R[x]/(x^2 + 1) ≅ C is one of the most beautiful results in algebra. Explain each step: why is (x^2 + 1) an ideal? Why is it maximal? Why does the quotient give us C?

13. Explain the analogy between "ideal in a ring" and "normal subgroup in a group." What is the common theme?

14. In the context of SLT, suppose the set of optimal parameters is defined by the equations w_1 * w_2 = 0 and w_1^2 + w_2^2 - 1 = 0. What ideal in R[w_1, w_2] defines this set? What does the quotient ring R[w_1, w_2]/I represent geometrically?

15. Why is it significant that GF(p^n)* is cyclic? What does this tell you about the structure of multiplication in a finite field?
