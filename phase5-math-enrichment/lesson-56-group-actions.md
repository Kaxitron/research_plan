# Lesson 56: Group Actions, Representations, and Neural Network Symmetry

[← Rings & Fields](lesson-55-rings-fields.md) | [Back to TOC](../README.md) | [Next: Point-Set Topology →](lesson-57-point-set-topology.md)

---

> **Why this lesson exists:** A group acting on a set is the precise mathematical formulation of "symmetry of a structure." When S_n acts on weight space by permuting neurons, it creates orbits (sets of equivalent weights), stabilizers (symmetries fixing a point), and singularities (where stabilizers are unusually large). The orbit-stabilizer theorem tells you exactly how many equivalent weight configurations exist. Representations translate group actions into matrices, connecting symmetry to the linear algebra you already know. This is the direct bridge from abstract algebra to the singularities in neural network loss landscapes.

## 🎯 Core Concepts

### Group Actions — Symmetry in Action

- **A group action** of G on a set X is a map G × X → X, written (g,x) ↦ g·x, satisfying: (1) e·x = x, (2) (gh)·x = g·(h·x). The group "moves" elements of X while respecting the group structure.
- **The orbit** of x is Orb(x) = {g·x : g ∈ G} — all positions x can be moved to. Orbits partition X.
- **The stabilizer** of x is Stab(x) = {g ∈ G : g·x = x} — all symmetries that fix x. A large stabilizer means x has lots of symmetry.
- **Orbit-Stabilizer Theorem:** |Orb(x)| × |Stab(x)| = |G|. More symmetry at x (bigger stabilizer) means fewer distinct positions in x's orbit.

### Neural Network Symmetries

- **Permutation symmetry:** for a fully-connected network with n hidden units, the symmetric group S_n acts on weight space by permuting units. If units i and j are swapped, the incoming and outgoing weights are swapped correspondingly, but the network function is unchanged.
- **Orbit structure:** the orbit of a weight vector w under S_n consists of all n! permutations. If two units have identical weights, the stabilizer is non-trivial — some permutations don't change w. This creates singularities.
- **Sign symmetry:** for ReLU networks, flipping the sign of all incoming weights to a neuron and the sign of its outgoing weight preserves the function (because ReLU(x) behaves differently, but the composition compensates). This gives an additional (ℤ₂)ⁿ symmetry.
- **The orbit space W/G** (weight space modulo symmetry) is the "true" parameter space — distinct network functions. This space has singularities at points where the stabilizer is non-trivial (i.e., where some neurons are "equivalent").

### The Orbit-Stabilizer Theorem and SLT

- **At a generic point** in weight space (all neurons distinct), the stabilizer is trivial (just the identity). The orbit has n! elements. The loss landscape locally looks like n! copies of the same shape.
- **At a singular point** (some neurons equal or zero), the stabilizer is non-trivial. The orbit is smaller — fewer equivalent configurations. The loss landscape develops a non-generic shape — a singularity.
- **The type of singularity** (measured by the RLCT) is determined by the structure of the stabilizer at that point. Larger stabilizers → more severe singularities → smaller RLCT → lower effective complexity. This is the group-theoretic foundation of SLT.
- **Example:** in a network with 3 hidden units, if all 3 have identical weights, the stabilizer is S₃ (6 elements). The orbit has n!/6 = 1 element — the point IS fixed by the full symmetry. This is a highly singular point (the "origin" of the hidden unit space), and SLT says the RLCT here is small.

### Group Representations — Symmetry as Matrices

- **A representation** of G is a homomorphism ρ: G → GL(V) — each group element becomes an invertible matrix, and the group operation becomes matrix multiplication. This lets you study abstract symmetry using linear algebra.
- **Irreducible representations** can't be decomposed into smaller ones. Every representation breaks into irreducibles — like eigenvectors decompose a matrix.
- **Characters** χ(g) = tr(ρ(g)) are the traces of representation matrices. Characters determine the representation (up to equivalence) and are easy to compute and compare.
- **For neural networks:** the permutation action of S_n on weight space IS a representation. Decomposing it into irreducibles tells you the "independent modes" of the weight space — which combinations of weights are affected by which symmetries. This is used in equivariant neural network design.

### Equivariant Neural Networks

- **Equivariant layers** commute with group actions: f(g·x) = g·f(x). A convolutional layer is equivariant to translation: shifting the input shifts the output by the same amount.
- **Designing equivariant architectures** uses representation theory: the layer's weight matrix must commute with all representation matrices of the symmetry group. This constrains the architecture but guarantees the symmetry is respected.
- **Examples:** CNNs (translation equivariance), Spherical CNNs (rotation equivariance), Graph Neural Networks (permutation equivariance of nodes).

## 📺 Watch — Primary

1. **Visual Group Theory — "Group Actions" (Nathan Carter)**
2. **Symmetry and Spectral Graph Theory lectures (YouTube)**

## 📖 Read — Primary

- **"Visual Group Theory" by Nathan Carter** — Chapters 10–12 (actions, representations)
- **"Algebra" by Artin** — Chapters 5–6 (group actions, with excellent geometric examples)

## 🔨 Do

- Compute the orbits and stabilizers of S₃ acting on weight vectors of a 2-input, 3-hidden, 1-output network. Find a generic point (trivial stabilizer) and a singular point (non-trivial stabilizer).
- Implement the orbit-stabilizer theorem numerically: for each weight vector in a discretized space, compute its orbit size and stabilizer size. Verify they multiply to |G|.
- Show that a convolutional layer IS an equivariant layer: verify that conv(shift(x)) = shift(conv(x)) numerically in PyTorch.
- Representation decomposition: write the 6×6 permutation matrices for S₃ acting on ℝ³. Find the trivial sub-representation (the all-ones direction, invariant under all permutations) and the standard representation (the orthogonal complement).
