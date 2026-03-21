# Lesson 82: Group Homomorphisms and the Isomorphism Theorems

[<-- Cosets & Lagrange](lesson-81-cosets-lagrange.md) | [Back to TOC](../README.md) | [Next: Rings & Fields -->](lesson-83-rings-fields.md)

---

> **Why this lesson exists:** Homomorphisms are the maps that respect algebraic structure, and the isomorphism theorems reveal the deep architecture of how groups decompose. In AI alignment research, the concept of "structure-preserving transformation" is central: neural network layers transform representations while (ideally) preserving task-relevant structure. The First Isomorphism Theorem -- which says that the image of a homomorphism is isomorphic to the domain modulo the kernel -- provides a template for understanding how information is compressed, what is preserved, and what is lost when data flows through a network. These ideas underpin the algebraic perspective on feature learning and representation in alignment-relevant interpretability work.

> **Estimated time:** 15--20 hours

---

## Part 1: Group Homomorphisms

### Definition

A **group homomorphism** is a function f: G --> H between groups that preserves the group operation:

f(g_1 * g_2) = f(g_1) * f(g_2) for all g_1, g_2 in G

The operation on the left is G's operation; on the right is H's. The homomorphism "translates" one group's structure into another's.

### Basic Properties

If f: G --> H is a homomorphism, then:

1. **f maps identity to identity:** f(e_G) = e_H.
   Proof: f(e_G) = f(e_G * e_G) = f(e_G) * f(e_G). Multiplying both sides by f(e_G)^{-1} gives e_H = f(e_G).

2. **f maps inverses to inverses:** f(g^{-1}) = f(g)^{-1}.
   Proof: f(g) * f(g^{-1}) = f(g * g^{-1}) = f(e_G) = e_H, so f(g^{-1}) is the inverse of f(g).

3. **f preserves order (up to division):** The order of f(g) divides the order of g.

4. **The image of a subgroup is a subgroup:** If K <= G, then f(K) <= H.

5. **The preimage of a subgroup is a subgroup:** If L <= H, then f^{-1}(L) <= G.

### Important Examples

**1. The determinant map det: GL_n(R) --> R*.**
This is a homomorphism from the general linear group to the multiplicative group of nonzero reals: det(AB) = det(A) * det(B). Its kernel is SL_n(R), the matrices with determinant 1.

**2. The sign map sgn: S_n --> {+1, -1}.**
Each permutation is either even (sign +1) or odd (sign -1), and sgn(sigma * tau) = sgn(sigma) * sgn(tau). The kernel is A_n, the alternating group.

**3. The exponential map exp: (R, +) --> (R_{>0}, *).**
exp(a + b) = exp(a) * exp(b). This is an isomorphism, with inverse log.

**4. The mod-n map Z --> Z_n.**
Sends each integer to its residue class modulo n. The kernel is nZ = {..., -2n, -n, 0, n, 2n, ...}.

**5. Evaluation of polynomials.** The map R[x] --> R sending p(x) to p(a) for fixed a is a ring homomorphism (we will revisit this in Lesson 83, but it illustrates the ubiquity of the concept).

## Part 2: Kernel and Image

### Definitions

For a homomorphism f: G --> H:

- The **kernel** of f is ker(f) = {g in G : f(g) = e_H}. This is the set of elements that f "kills" (sends to the identity).
- The **image** of f is im(f) = {f(g) : g in G}. This is the set of elements in H that are "hit" by f.

### Kernel Is Always Normal

**Theorem.** ker(f) is a normal subgroup of G.

**Proof.** First, ker(f) is a subgroup: if f(a) = e_H and f(b) = e_H, then f(ab^{-1}) = f(a)f(b)^{-1} = e_H * e_H = e_H.

For normality: if n is in ker(f) and g is any element of G, then f(gng^{-1}) = f(g)f(n)f(g)^{-1} = f(g) * e_H * f(g)^{-1} = e_H. So gng^{-1} is in ker(f).

This result is profoundly important: it tells us that normal subgroups are exactly the kernels of homomorphisms. Every normal subgroup N of G is the kernel of the natural projection G --> G/N.

### Injectivity and the Kernel

**Theorem.** A homomorphism f is injective (one-to-one) if and only if ker(f) = {e_G}.

This gives a clean algebraic criterion for injectivity: instead of checking that f(a) = f(b) implies a = b for all pairs, we just need to check that only the identity maps to the identity.

### Image Is Always a Subgroup

im(f) is always a subgroup of H (but not necessarily normal).

## Part 3: Isomorphisms

### Definition

An **isomorphism** is a bijective homomorphism. If an isomorphism exists between G and H, we write G ≅ H and say the groups are **isomorphic**.

Isomorphic groups are "the same group with different labels." They have identical algebraic structure: the same order, the same number of elements of each order, the same subgroup lattice structure, and so on.

### Examples of Isomorphisms

1. Z_2 ≅ {+1, -1} under multiplication.
2. Z ≅ nZ for any nonzero n (via the map k --> nk).
3. (R, +) ≅ (R_{>0}, *) via the exponential map.
4. Z_2 x Z_3 ≅ Z_6 (since gcd(2,3) = 1).
5. Z_2 x Z_2 is NOT isomorphic to Z_4 (the former has no element of order 4).

### Automorphisms

An **automorphism** is an isomorphism from a group to itself. The set of all automorphisms of G forms a group Aut(G) under composition.

**Inner automorphisms:** For each g in G, the map phi_g(x) = gxg^{-1} is an automorphism (conjugation by g). The set of inner automorphisms Inn(G) is a normal subgroup of Aut(G), and Inn(G) ≅ G/Z(G).

## Part 4: The First Isomorphism Theorem

### Statement

**First Isomorphism Theorem.** If f: G --> H is a homomorphism, then:

G / ker(f) ≅ im(f)

In other words, the quotient of the domain by what the map kills is isomorphic to what the map hits.

### Unpacking the Statement

This theorem has three components working together:

1. ker(f) is a normal subgroup of G (so G/ker(f) makes sense as a quotient group).
2. im(f) is a subgroup of H.
3. The map G/ker(f) --> im(f) given by g*ker(f) --> f(g) is a well-defined isomorphism.

### Proof Sketch

Define phi: G/ker(f) --> im(f) by phi(g*ker(f)) = f(g).

- **Well-defined:** If g_1*ker(f) = g_2*ker(f), then g_1^{-1} g_2 is in ker(f), so f(g_1^{-1} g_2) = e_H, giving f(g_1) = f(g_2).
- **Homomorphism:** phi(g_1*ker(f) * g_2*ker(f)) = phi(g_1 g_2*ker(f)) = f(g_1 g_2) = f(g_1)f(g_2) = phi(g_1*ker(f)) * phi(g_2*ker(f)).
- **Injective:** If phi(g*ker(f)) = e_H, then f(g) = e_H, so g is in ker(f), meaning g*ker(f) = ker(f) (the identity in the quotient).
- **Surjective:** Every element of im(f) is f(g) for some g, which equals phi(g*ker(f)).

### Applications

**Example 1.** The determinant det: GL_n(R) --> R* has kernel SL_n(R) and image R*. By the First Isomorphism Theorem: GL_n(R) / SL_n(R) ≅ R*.

**Example 2.** The sign map sgn: S_n --> {+1, -1} has kernel A_n and is surjective. So: S_n / A_n ≅ Z_2.

**Example 3.** The mod-n map Z --> Z_n has kernel nZ and is surjective. So: Z / nZ ≅ Z_n. (This is the formal justification for modular arithmetic.)

### The Diamond Diagram

The First Isomorphism Theorem is often visualized as a commutative diagram:

```
    G ---f---> H
    |          ^
  pi|        / i (inclusion)
    v      /
  G/ker(f) --phi--> im(f)
```

where pi is the natural projection and phi is the isomorphism. This "factoring" of f through the quotient is a universal construction that will reappear in category theory.

## Part 5: Second and Third Isomorphism Theorems

### Second Isomorphism Theorem (Diamond Isomorphism Theorem)

Let H be a subgroup of G and N be a normal subgroup of G. Then:

1. HN = {hn : h in H, n in N} is a subgroup of G.
2. H intersect N is a normal subgroup of H.
3. **HN/N ≅ H/(H intersect N).**

Visual: draw the subgroup lattice with HN at top, H and N below it, H intersect N below both, and {e} at the bottom. The diamond shape gives this theorem its name.

### Third Isomorphism Theorem

Let N and M be normal subgroups of G with N contained in M. Then:

1. M/N is a normal subgroup of G/N.
2. **(G/N) / (M/N) ≅ G/M.**

Intuition: "canceling" N's in the double quotient. If you first mod out by N and then mod out by M/N, the result is the same as modding out by M directly.

### Correspondence Theorem (Fourth Isomorphism Theorem)

If N is a normal subgroup of G, there is a bijection between:
- Subgroups of G containing N
- Subgroups of G/N

This bijection preserves normality, indices, and containment. It tells you that the subgroup structure of a quotient group G/N is a "coarsened" version of the subgroup structure of G.

## Part 6: Quotient Groups

### Construction

If N is a normal subgroup of G, the **quotient group** (or factor group) G/N is the set of all cosets {gN : g in G} with the operation:

(g_1 N)(g_2 N) = (g_1 g_2)N

Normality of N is precisely what makes this operation well-defined (independent of coset representative choice).

### Examples

1. **Z/nZ ≅ Z_n.** The quotient of the integers by multiples of n gives modular arithmetic.

2. **R/Z.** The quotient of the reals by the integers. Each coset is a set {x + n : n in Z} for x in [0,1). This quotient group is isomorphic to the circle group S^1 (the unit circle in the complex plane under multiplication), since adding real numbers modulo 1 is the same as rotating around the circle.

3. **S_n/A_n ≅ Z_2.** Quotienting the symmetric group by even permutations gives a group of order 2: "even or odd."

4. **GL_n(R)/SL_n(R) ≅ R*.** Quotienting by unit-determinant matrices gives the multiplicative reals (the determinant).

### Quotient Groups as "Simplified Versions"

A quotient G/N captures the structure of G with the "detail" provided by N collapsed. Elements that differ only by an element of N become identified. This is precisely the mechanism used in SLT when collapsing equivalent weight configurations: the quotient space W/G identifies weights that differ only by symmetry.

## Part 7: Classification of Finite Abelian Groups

### The Fundamental Theorem

**Fundamental Theorem of Finite Abelian Groups.** Every finite abelian group G is isomorphic to a direct product of cyclic groups:

G ≅ Z_{n_1} x Z_{n_2} x ... x Z_{n_k}

This decomposition can be expressed in two canonical forms:

**Invariant factor form:** n_1 | n_2 | ... | n_k (each divides the next). This is unique.

**Elementary divisor form:** Each n_i is a prime power. This is also unique (up to reordering).

### Example

All abelian groups of order 12:
- Z_12 ≅ Z_4 x Z_3 (invariant factor: 12)
- Z_2 x Z_6 ≅ Z_2 x Z_2 x Z_3 (invariant factors: 2, 6)

These are the only two, and they are not isomorphic (Z_12 has an element of order 12; Z_2 x Z_6 does not).

### Example: Abelian Groups of Order 36

36 = 2^2 * 3^2. The elementary divisors can be:
- 4, 9: giving Z_4 x Z_9 ≅ Z_36
- 4, 3, 3: giving Z_4 x Z_3 x Z_3 ≅ Z_12 x Z_3
- 2, 2, 9: giving Z_2 x Z_2 x Z_9 ≅ Z_2 x Z_18
- 2, 2, 3, 3: giving Z_2 x Z_2 x Z_3 x Z_3 ≅ Z_6 x Z_6

So there are exactly 4 abelian groups of order 36, up to isomorphism.

## Part 8: Direct Products

### External Direct Product

Given groups G_1, G_2, ..., G_n, the **direct product** G_1 x G_2 x ... x G_n is the set of tuples (g_1, g_2, ..., g_n) with component-wise operation:

(g_1, ..., g_n) * (h_1, ..., h_n) = (g_1 * h_1, ..., g_n * h_n)

The order is |G_1| * |G_2| * ... * |G_n|.

### Internal Direct Product

If G has normal subgroups N_1 and N_2 such that G = N_1 N_2 and N_1 intersect N_2 = {e}, then G is the **internal direct product** of N_1 and N_2, and G ≅ N_1 x N_2.

### When Is Z_m x Z_n Cyclic?

Z_m x Z_n is cyclic (isomorphic to Z_{mn}) if and only if gcd(m, n) = 1. This is because (1, 1) has order lcm(m, n) in Z_m x Z_n, and lcm(m, n) = mn exactly when gcd(m, n) = 1.

## Part 9: Connection to AI Alignment

### Structure-Preserving Maps in Neural Networks

Each layer of a neural network computes a transformation of its input. Ideally, these transformations preserve task-relevant structure while discarding irrelevant information. This is precisely the idea of a homomorphism: preserve structure (the kernel captures what is lost, the image captures what is retained).

The First Isomorphism Theorem provides a conceptual framework: a neural network layer f maps input representations G to output representations im(f), and the "equivalence classes" of inputs that produce the same output correspond to cosets of ker(f). The network has learned to quotient the input space by task-irrelevant distinctions.

### Representation Equivalence

Two neural network weight configurations are **equivalent** if they compute the same function. The equivalence classes are orbits of the symmetry group action (Lesson 84). The quotient space of weight configurations modulo symmetry is a fundamental object in SLT, and its structure depends on the group theory developed in this lesson and the previous one.

---

## Watch -- Primary

- **Matthew Macauley -- Visual Group Theory, Lectures 21--30 (approx.)**
  Covers homomorphisms, kernels, quotient groups, and the isomorphism theorems with visual examples. The progression from Cayley diagrams to quotient diagrams is particularly effective.

## Read -- Primary

- **Paolo Aluffi, "Algebra: Chapter 0," Chapter III**
  Covers homomorphisms, isomorphism theorems, direct products, and the classification of finite abelian groups. Aluffi's approach via universal properties begins to show its power here.

---

## Exercises

### Computational

1. Define f: Z_12 --> Z_4 by f(x) = x mod 4. Verify this is a homomorphism. Find ker(f) and im(f). Verify the First Isomorphism Theorem.

2. Define f: S_3 --> Z_2 by f(sigma) = sgn(sigma). Find ker(f) and verify S_3/A_3 ≅ Z_2.

3. List all group homomorphisms from Z_6 to Z_3. (Hint: a homomorphism is determined by where it sends a generator, and the image of a generator must have order dividing the order of the generator.)

4. Classify all abelian groups of order 72 = 2^3 * 3^2 up to isomorphism. How many are there?

5. Find Aut(Z_10). What familiar group is it isomorphic to?

### Proof-Based

6. Prove that if f: G --> H is a homomorphism, then the order of f(g) divides the order of g.

7. Prove the Second Isomorphism Theorem.

8. Prove that if G is a finite group and f: G --> G is a homomorphism, then |ker(f)| * |im(f)| = |G|.

9. Prove that Z_m x Z_n ≅ Z_{mn} if and only if gcd(m, n) = 1.

10. Prove that Inn(G) ≅ G/Z(G).

### Conceptual

11. The First Isomorphism Theorem says G/ker(f) ≅ im(f). Explain what this means intuitively in terms of "what the homomorphism forgets" versus "what it sees."

12. Consider a neural network layer f: R^n --> R^m defined by f(x) = sigma(Wx + b) where sigma is an activation function. In what sense is this analogous to a group homomorphism? In what sense is the analogy imperfect?

13. Explain why the Correspondence Theorem is useful: if you know the subgroups of a quotient G/N, what does that tell you about G?

14. The group Z_2 x Z_2 x Z_2 has order 8. How many distinct homomorphisms are there from this group to Z_2? How many to Z_4?

15. Two groups of order 8 are Q_8 (quaternion group) and D_4. Both are non-abelian. List one structural property that distinguishes them. (Hint: count elements of order 4.)
