# Lesson 84: Group Actions and Representations

[<-- Rings & Fields](lesson-83-rings-fields.md) | [Back to TOC](../README.md) | [Next: Curves & Surfaces -->](lesson-85-curves-surfaces.md)

---

> **Why this lesson exists:** Group actions formalize what it means for a symmetry group to act on a mathematical object, and representations translate group elements into matrices, making abstract symmetry concrete and computable. In AI alignment research, the symmetry group of a neural network acts on the weight space by permuting neurons -- this action creates orbits of equivalent weight configurations, and understanding these orbits is essential for Singular Learning Theory's analysis of model complexity. The orbit-stabilizer theorem quantifies the redundancy in weight space, while representation theory provides tools for decomposing how symmetry affects learning dynamics. This lesson brings together the group theory of Lessons 80--82 with the geometric perspective needed for SLT.

> **Estimated time:** 15--20 hours

---

## Part 1: Group Actions

### Definition

A **(left) group action** of a group G on a set X is a function G x X --> X, written (g, x) --> g . x, satisfying:

1. **Identity:** e . x = x for all x in X.
2. **Compatibility:** (gh) . x = g . (h . x) for all g, h in G and x in X.

When such an action exists, we say G **acts on** X, or that X is a **G-set**.

### Equivalent Formulation via Homomorphisms

A group action of G on X is equivalent to a group homomorphism:

phi: G --> Sym(X)

where Sym(X) is the symmetric group of X (the group of all bijections X --> X). The element phi(g) is the permutation of X induced by g.

This reformulation is powerful: it means studying group actions is the same as studying homomorphisms from G into symmetric groups.

### Examples of Group Actions

**1. Left multiplication.** G acts on itself by left multiplication: g . x = gx. This action is always **faithful** (only the identity acts trivially). This is the action underlying Cayley's theorem: the homomorphism G --> Sym(G) is injective, embedding G into a symmetric group.

**2. Conjugation.** G acts on itself by conjugation: g . x = gxg^{-1}. The kernel of this action is the center Z(G). The orbits are **conjugacy classes**.

**3. Action on cosets.** If H is a subgroup of G, then G acts on the set of left cosets G/H by left multiplication: g . (aH) = (ga)H. This is a transitive action.

**4. Rotations of a polygon.** The dihedral group D_n acts on the set of vertices {1, 2, ..., n} of a regular n-gon by rotation and reflection. It also acts on the set of edges, the set of diagonals, and so on.

**5. S_n acts on polynomials.** S_n acts on R[x_1, ..., x_n] by permuting variables: sigma . f(x_1, ..., x_n) = f(x_{sigma(1)}, ..., x_{sigma(n)}). The polynomials fixed by this action are the **symmetric polynomials**.

**6. Matrix groups act on vectors.** GL_n(R) acts on R^n by matrix multiplication: A . v = Av. This is the prototypical example of a linear group action (i.e., a representation).

### Types of Actions

- **Faithful:** Only the identity element acts trivially (the homomorphism G --> Sym(X) is injective).
- **Transitive:** For any x, y in X, there exists g in G with g . x = y (only one orbit).
- **Free:** The only element fixing any point is the identity (every stabilizer is trivial).
- **Regular:** Both free and transitive (each pair (x, y) has exactly one g with g . x = y).

## Part 2: Orbits and Stabilizers

### Orbits

The **orbit** of an element x in X under the action of G is:

Orb(x) = G . x = {g . x : g in G}

This is the set of all elements that x can be "moved to" by the group.

**Key fact:** The orbits partition X into disjoint subsets. Every element of X belongs to exactly one orbit.

### Stabilizers

The **stabilizer** (or isotropy group) of an element x in X is:

Stab(x) = G_x = {g in G : g . x = x}

This is the subgroup of G consisting of elements that fix x.

**Key fact:** Stab(x) is always a subgroup of G (exercise: verify closure, identity, inverses).

### The Orbit-Stabilizer Theorem

**Theorem.** If G is a finite group acting on a set X, and x is any element of X, then:

|G| = |Orb(x)| * |Stab(x)|

Equivalently: |Orb(x)| = [G : Stab(x)] = |G| / |Stab(x)|.

**Proof.** There is a bijection between the orbit Orb(x) and the set of left cosets G/Stab(x), given by g . x <--> g * Stab(x). This is well-defined because g . x = h . x if and only if h^{-1}g is in Stab(x), i.e., g * Stab(x) = h * Stab(x).

### Applications of the Orbit-Stabilizer Theorem

**Counting conjugacy classes.** Under the conjugation action, the orbit of g is its conjugacy class, and the stabilizer is the centralizer C_G(g). So:

|conjugacy class of g| = [G : C_G(g)]

**Example in S_4.** The conjugacy class of (1 2) consists of all transpositions. There are C(4,2) = 6 transpositions. The centralizer of (1 2) in S_4 has order |S_4|/6 = 24/6 = 4.

### The Class Equation

Partitioning G into conjugacy classes gives the **class equation**:

|G| = |Z(G)| + sum of [G : C_G(g_i)]

where the sum runs over one representative g_i from each non-trivial conjugacy class (those with more than one element).

**Application:** If |G| = p^n for a prime p, then |Z(G)| is divisible by p. In particular, Z(G) is non-trivial. This is a powerful structural result about p-groups.

## Part 3: Burnside's Lemma

### Statement

**Burnside's Lemma** (also called the Cauchy-Frobenius lemma). If a finite group G acts on a finite set X, then the number of distinct orbits is:

|X/G| = (1/|G|) * sum over g in G of |Fix(g)|

where Fix(g) = {x in X : g . x = x} is the set of elements fixed by g.

In words: the number of orbits equals the average number of fixed points.

### Proof

Count the set S = {(g, x) : g . x = x} in two ways:
- Summing over g: |S| = sum_{g in G} |Fix(g)|.
- Summing over x: |S| = sum_{x in X} |Stab(x)|.

By the orbit-stabilizer theorem, |Stab(x)| = |G|/|Orb(x)|. Elements in the same orbit have orbits of the same size, so summing over an orbit of size k gives k * (|G|/k) = |G|. With r orbits total:

sum_{x in X} |Stab(x)| = r * |G|

Therefore sum_{g in G} |Fix(g)| = r * |G|, giving r = (1/|G|) * sum_{g in G} |Fix(g)|.

### Example: Counting Necklaces

How many distinct necklaces can be made with 4 beads, each colored red or blue, where two necklaces are "the same" if one can be rotated into the other?

The group is Z_4 = {e, r, r^2, r^3} (rotations of 4 positions). The set X is all 2^4 = 16 colorings.

- Fix(e) = all 16 colorings.
- Fix(r) = colorings unchanged by 90-degree rotation = all beads same color = 2.
- Fix(r^2) = colorings unchanged by 180-degree rotation = 2 pairs must match = 2^2 = 4.
- Fix(r^3) = same as Fix(r) = 2.

Number of distinct necklaces = (16 + 2 + 4 + 2)/4 = 24/4 = 6.

If we also allow reflections (using D_4 instead of Z_4), the count changes:
- Fix(s) = Fix(rs) = 2^2 = 4 (reflections through vertices fix 2 beads and swap 2 others in matched pairs, but the exact count depends on which reflection axis).
- The total gives (16 + 2 + 4 + 2 + 4 + 4 + 2 + 4)/8, which accounts for all 8 symmetries of the square.

Burnside's lemma is essential in combinatorics for counting "distinct objects up to symmetry," which is precisely the problem we face in neural network weight spaces.

## Part 4: Group Representations

### Definition

A **(linear) representation** of a group G is a group homomorphism:

rho: G --> GL(V)

where V is a vector space and GL(V) is the group of invertible linear transformations of V. Equivalently, it is a group action of G on V by linear maps.

If V has dimension n (over a field F), choosing a basis identifies GL(V) with GL_n(F), and the representation assigns a matrix rho(g) to each group element g.

### Why Representations?

Representations convert abstract group elements into concrete matrices. This allows us to:
- Compute with groups using linear algebra.
- Decompose group actions into simpler pieces.
- Apply Fourier analysis on groups (the representation theory of abelian groups generalizes Fourier theory).

### Examples

**1. The trivial representation.** rho(g) = I for all g. Every group has this.

**2. The sign representation of S_n.** rho(sigma) = sgn(sigma) in GL_1(R) = R*. This is a 1-dimensional representation.

**3. The permutation representation.** For G acting on {1, ..., n}, define rho(g) as the n x n permutation matrix with rho(g)_{ij} = 1 if g . j = i, and 0 otherwise.

**4. The regular representation.** G acts on the vector space C[G] (with basis indexed by group elements) by left multiplication. This representation has dimension |G| and contains every irreducible representation as a subrepresentation.

### Irreducible Representations

A representation is **irreducible** if V has no proper non-trivial G-invariant subspace. Irreducible representations are the "atoms" from which all representations are built.

**Maschke's theorem:** If G is a finite group and the characteristic of the field does not divide |G|, then every representation is a direct sum of irreducible representations. This is the group-theoretic analogue of diagonalization.

## Part 5: Character Theory Basics

### Definition

The **character** of a representation rho: G --> GL(V) is the function:

chi_rho: G --> F, chi_rho(g) = tr(rho(g))

where tr denotes the trace of the matrix.

### Key Properties

1. chi(e) = dim(V) (the trace of the identity matrix is the dimension).
2. chi(hgh^{-1}) = chi(g) (characters are **class functions** -- constant on conjugacy classes).
3. Isomorphic representations have the same character.
4. For finite groups over C, the character determines the representation up to isomorphism.

### The Character Table

For a finite group G, the character table lists the values of all irreducible characters on all conjugacy classes. It is a square matrix (the number of irreducible representations equals the number of conjugacy classes).

**Orthogonality relations:** The rows of the character table are orthogonal:

(1/|G|) * sum_{g in G} chi_i(g) * conj(chi_j(g)) = delta_{ij}

This inner product structure makes character theory a powerful computational tool.

### Example: Character Table of S_3

S_3 has 3 conjugacy classes: {e}, {(1 2), (1 3), (2 3)}, {(1 2 3), (1 3 2)}.
It has 3 irreducible representations of dimensions 1, 1, and 2 (since 1^2 + 1^2 + 2^2 = 6 = |S_3|).

|          | {e} | {transpositions} | {3-cycles} |
|----------|-----|------------------|------------|
| trivial  |  1  |        1         |     1      |
| sign     |  1  |       -1         |     1      |
| standard |  2  |        0         |    -1      |

## Part 6: Neural Network Weight Symmetry

### The Symmetry Group of a Neural Network

Consider a feedforward neural network with layers of widths n_0, n_1, ..., n_L. The symmetry group consists of all transformations of the weight space that leave the input-output function unchanged.

For a network with activation function sigma, the primary symmetry is **neuron permutation**: permuting the neurons in hidden layer l (together with their incoming and outgoing weights) preserves the computed function. This gives a symmetry group:

G = S_{n_1} x S_{n_2} x ... x S_{n_{L-1}}

For odd activation functions (like tanh), there are additional **sign-flip symmetries**: negating all incoming weights and all outgoing weights of a neuron preserves the function. This extends the group to:

G = (S_{n_1} x (Z_2)^{n_1}) x ... x (S_{n_{L-1}} x (Z_2)^{n_{L-1}})

where each factor is actually a semidirect product (wreath product) S_{n_l} wr Z_2.

### Orbits in Weight Space

Two weight configurations w_1 and w_2 are in the same orbit of G if and only if they compute the same function (assuming generic weights -- non-generic cases involve additional symmetries from parameter-function degeneracies).

By the orbit-stabilizer theorem:

|Orb(w)| = |G| / |Stab(w)|

For a generic weight configuration, Stab(w) = {e} (no nontrivial symmetry fixes a generic point), so:

|Orb(w)| = |G| = n_1! * n_2! * ... * n_{L-1}!

This means a generic function computed by the network appears |G| times in weight space.

### Non-Generic Configurations and Singularities

When neurons have equal weights (parameter degeneracies), the stabilizer Stab(w) becomes non-trivial. At such points:

- The orbit is smaller: |Orb(w)| = |G|/|Stab(w)| < |G|.
- The map from parameters to functions has a **singularity** -- it is not locally one-to-one.
- In SLT, these singularities determine the learning coefficient (RLCT), which governs how the model trades off fit against complexity.

Understanding the stabilizer structure at these singular points requires precisely the group action theory developed in this lesson.

### Example: Two-Neuron Hidden Layer

Consider a network R --> R^2 --> R with weights:
- First layer: w = (w_1, w_2) (weights from input to hidden neurons)
- Second layer: v = (v_1, v_2) (weights from hidden to output)

The symmetry group is S_2 = {e, (1 2)}, which acts by:
- e: (w_1, w_2, v_1, v_2) --> (w_1, w_2, v_1, v_2)
- (1 2): (w_1, w_2, v_1, v_2) --> (w_2, w_1, v_2, v_1)

Generic points have orbit of size 2 (two equivalent configurations). But if w_1 = w_2 and v_1 = v_2, then (1 2) fixes this point, so |Stab(w)| = 2 and |Orb(w)| = 1. This is a singularity.

At this singularity, the network effectively has only one distinct hidden neuron, but the parameterization allows two. The discrepancy between the formal dimension of the parameter space and the effective dimension creates a singular point in the parameter-to-function map. SLT quantifies this through the RLCT.

## Part 7: From Symmetries to Singularities in SLT

### The Big Picture

The chain of reasoning connecting group actions to SLT:

1. Neural networks have weight space symmetries (a group G acting on weight space W).
2. The orbits of this action correspond to equivalence classes of weights (same function).
3. Points with non-trivial stabilizers are singularities of the parameter-to-function map.
4. The geometry of these singularities (classified by algebraic geometry) determines the RLCT.
5. The RLCT controls the effective model complexity, governing generalization and learning.

Group actions thus sit at the foundation of the algebraic analysis of learning machines. Without understanding orbits, stabilizers, and the orbit-stabilizer theorem, the geometric analysis of SLT would be opaque.

### Symmetry and the Loss Landscape

The loss landscape L(w) of a neural network inherits the symmetry of the weight space: L(g . w) = L(w) for all g in G. This means:

- Critical points come in orbits: if w is a critical point, so is every g . w.
- The Hessian at symmetric critical points has a block structure determined by the representation theory of the stabilizer group.
- Saddle points associated with symmetry breaking (where the stabilizer changes) play a special role in training dynamics.

Understanding these phenomena requires combining group actions with representation theory -- exactly the tools of this lesson.

---

## Watch -- Primary

- **Matthew Macauley -- Visual Group Theory (Group Actions and Representations section)**
  Covers group actions, orbits, stabilizers, Burnside's lemma, and introduces representations with visual examples. Macauley's approach of building from concrete actions to abstract theory is particularly effective.

## Read -- Primary

- **Paolo Aluffi, "Algebra: Chapter 0," Chapter II (actions section)**
  Covers group actions, orbits, stabilizers, and the orbit-stabilizer theorem. Aluffi's categorical perspective connects actions to functors, providing a bridge to more advanced topics.

---

## Exercises

### Computational

1. The group Z_3 acts on the set of 3-bead necklaces with 2 colors by rotation. Use Burnside's lemma to count the number of distinct necklaces. Then extend to D_3 (rotations and reflections).

2. Compute all orbits and stabilizers for the action of D_4 on the vertices {1, 2, 3, 4} of a square. Verify the orbit-stabilizer theorem for each vertex.

3. Write out the permutation representation matrices for S_3 acting on R^3. Decompose this 3-dimensional representation into irreducible representations. (Hint: the trivial representation accounts for one dimension; what about the other two?)

4. For the conjugation action of S_4 on itself, compute the conjugacy classes and write down the class equation.

5. Consider 5 beads in a circle, each colored with one of 3 colors. Use Burnside's lemma (with Z_5 acting by rotation) to count the number of distinct necklaces.

### Proof-Based

6. Prove that the orbits of a group action partition the set X.

7. Prove the orbit-stabilizer theorem.

8. Prove Cayley's theorem: every group G is isomorphic to a subgroup of Sym(G).

9. Prove that if G is a group of order p^2 (p prime), then G is abelian. (Hint: use the class equation and the fact that Z(G) is non-trivial.)

10. Prove that the number of irreducible representations of a finite group (over C) equals the number of conjugacy classes.

### Conceptual

11. Explain why Burnside's lemma is the "right" counting tool for problems involving symmetry. Give an example where naive counting (without Burnside) gives the wrong answer and explain why.

12. A neural network has architecture 1-3-1 (one input, three hidden neurons, one output) with ReLU activation. Describe the symmetry group G, its order, and compute the number of generic orbits in a weight space of dimension 9 (3 + 3 + 3 bias terms... simplified for this exercise, assume 6 weight parameters: w_1, w_2, w_3, v_1, v_2, v_3).

13. Explain the connection between "a representation is irreducible" and "there is no simpler way to see the symmetry." Why is decomposing representations analogous to prime factorization?

14. Consider the action of S_3 on the polynomial ring R[x, y, z] by permuting variables. What are the symmetric polynomials? Give three examples of invariant polynomials (the elementary symmetric polynomials).

15. In the context of SLT, explain why singular points in weight space (points with non-trivial stabilizer) are more important than generic points for understanding model behavior. What does the stabilizer tell us about the "effective dimension" at that point?
