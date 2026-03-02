# Lesson 57: Groups — Symmetry as Mathematics

[← Kolmogorov Complexity](lesson-56-kolmogorov-complexity.md) | [Back to TOC](../README.md) | [Next: Rings & Fields →](lesson-58-rings-fields.md)

---

> **Why this lesson exists:** A group is the mathematical formalization of symmetry — the set of all ways to transform something while preserving its structure. Groups appear throughout ML: the permutation symmetry of neural network neurons, the rotation/translation invariance of convolutions, the gauge symmetries of weight space. Understanding groups gives you the language to describe these symmetries precisely, and symmetry is the key to understanding the singularities that SLT studies.

## 🎯 Core Concepts

### What Is a Group?

- **A group (G, ·)** is a set G with a binary operation · satisfying four axioms:
  1. **Closure:** a · b ∈ G for all a, b ∈ G
  2. **Associativity:** (a · b) · c = a · (b · c)
  3. **Identity:** there exists e ∈ G such that e · a = a · e = a for all a
  4. **Inverse:** for each a ∈ G there exists a⁻¹ such that a · a⁻¹ = a⁻¹ · a = e
- **Groups capture symmetry:** the set of all symmetries of any object forms a group. The operation is composition (do one symmetry, then another). The identity is "do nothing." The inverse undoes a symmetry.

### Essential Examples

- **ℤ_n (integers mod n):** {0, 1, ..., n-1} under addition mod n. The symmetries of a clock face. ℤ_2 = {0,1} is the simplest non-trivial group.
- **S_n (symmetric group on n elements):** all permutations of {1,...,n}. This group has n! elements. S_3 has 6 elements and is the first non-abelian group you'll encounter (ab ≠ ba in general).
- **GL(n,ℝ) (general linear group):** all invertible n×n real matrices under multiplication. You've been working with this group since Phase 1 — every invertible matrix is a symmetry of ℝⁿ.
- **O(n) and SO(n):** orthogonal and special orthogonal groups — rotations and reflections. These are the symmetries that preserve distances (isometries). They appear in data augmentation and equivariant neural networks.

### Subgroups, Cosets, and Quotients

- **A subgroup H ≤ G** is a subset that's itself a group under the same operation. Example: even permutations form a subgroup A_n ≤ S_n.
- **Lagrange's theorem:** the order of a subgroup divides the order of the group: |H| divides |G|. This is a powerful counting tool.
- **Cosets:** gH = {gh : h ∈ H} is a left coset of H. Cosets partition G into equal-sized pieces. The number of cosets is |G|/|H| (the index).
- **Normal subgroups and quotient groups:** if H is normal in G (gHg⁻¹ = H for all g), you can form the quotient group G/H, whose elements are the cosets. This is "collapsing" the symmetry of H — treating everything related by H as identical.
- **For neural networks:** neurons that are permutations of each other are related by the symmetric group S_n acting on hidden units. The "true" weight space is the quotient W/S_n — weight space modulo permutation symmetry. This quotient structure creates the singularities that SLT studies.

### Homomorphisms and Isomorphisms

- **A homomorphism** φ: G → H is a map that preserves the group operation: φ(ab) = φ(a)φ(b). It's a "structure-preserving translation" between groups.
- **An isomorphism** is a bijective homomorphism — two groups are "the same" if isomorphic.
- **The kernel** ker(φ) = {g ∈ G : φ(g) = e_H} is a normal subgroup of G. **The first isomorphism theorem:** G/ker(φ) ≅ im(φ). The quotient by the kernel equals the image.
- **For ML:** the map from weight space to function space is a homomorphism (under appropriate operations). Its kernel — the set of weight configurations that compute the same function — is the symmetry group of the network. The first isomorphism theorem says: function space ≅ weight space / symmetry group.

### Abelian vs Non-Abelian Groups

- **Abelian (commutative):** ab = ba for all a, b. Examples: ℤ, ℤ_n, (ℝⁿ, +).
- **Non-abelian:** ab ≠ ba in general. Examples: S_n for n ≥ 3, GL(n) for n ≥ 2, rotation group SO(3).
- **Most symmetry groups in ML are non-abelian:** permuting neuron 1 and 2, then permuting 2 and 3, gives a different result than the reverse order. Non-commutativity creates richer structure (and more complex singularities).

## 📺 Watch — Primary

1. **3Blue1Brown — groups and symmetry (if available)**
2. **Visual Group Theory — "What is a Group?" (Nathan Carter lectures)**
3. **Aleph 0 — "Group Theory, Pair of Pants"**
   - https://www.youtube.com/watch?v=IK3VcATCkuY
   - *Beautifully produced short video connecting group theory to topology. Perfect for geometric intuition.*
4. **Socratica — "Abstract Algebra" playlist (Groups episodes)**
   - https://www.youtube.com/playlist?list=PLi01XoE8jYoi3SgnnGorR_XOW3IcK-TP6
   - *Short (~10 min), clear introductions. Good on-ramp before the heavier material.*

## 📖 Read — Primary

- **"Visual Group Theory" by Nathan Carter** — Chapters 1–6
  - *The most visual and intuitive introduction to group theory available.*
- **"Algebra: Chapter 0" by Aluffi** — Chapter 1–2 (if you want more rigor)

## 🔨 Do

- Write out the full multiplication table for S₃ (6 elements). Find all subgroups. Verify Lagrange's theorem.
- Prove that the set of n×n orthogonal matrices forms a group under multiplication. What's the identity? What's the inverse of an element?
- Implement a permutation group in Python: represent permutations as lists, implement composition and inversion. Verify the group axioms computationally for S₄.
- Show that for a 2-hidden-unit neural network, swapping the two hidden units (a specific element of S₂) gives the same function. Write this as a group action on weight space.

## 🔗 ML & Alignment Connection

**Permutation symmetries** in neural networks (swapping neurons gives the same function) create degenerate regions in the loss landscape. These symmetries mean many different weight configurations compute the same function — making it harder to verify whether a model has learned "safe" vs "unsafe" behavior by inspecting weights alone. In Singular Learning Theory, these symmetries create the singularities that determine generalization. Understanding group theory is prerequisite to understanding *why* neural networks generalize the way they do.
