# Lesson 35: Abstract Algebra — Groups, Symmetry, and Neural Networks

[← Computability](lesson-34-computability.md) | [Back to TOC](../README.md) | [Next: Topology →](lesson-36-topology.md)

---

> **Why this lesson exists:** Singular Learning Theory (SLT), one of the most promising mathematical frameworks for understanding deep learning, is built on the observation that neural networks have *symmetries* — you can permute neurons in a hidden layer and get the exact same function. These symmetries form mathematical structures called *groups*, and they're the reason the loss landscape has singularities rather than smooth minima. Without understanding groups, SLT stays a black box. More broadly, symmetry is the deepest organizing principle in mathematics and physics, and it's increasingly central to understanding why deep learning works.

## 🎯 Core Concepts

### What Is a Group?

- **A group (G, ·)** is a set G with an operation · satisfying four axioms:
  1. **Closure:** if a, b ∈ G, then a · b ∈ G (combining two elements gives another element)
  2. **Associativity:** (a · b) · c = a · (b · c) (parentheses don't matter)
  3. **Identity:** there exists e ∈ G such that e · a = a · e = a (there's a "do nothing" element)
  4. **Inverse:** for every a ∈ G, there exists a⁻¹ such that a · a⁻¹ = e (every action can be undone)
- **That's it.** These four simple rules generate an enormous, rich theory. The power comes from how general these axioms are — they apply to rotations, permutations, matrix multiplication, symmetries of physical objects, and much more.

### Concrete Examples — Building Intuition

- **Integers under addition (ℤ, +):** identity is 0, inverse of n is -n. This is an infinite group. It's also *abelian* (commutative: a + b = b + a). Simplest infinite group.
- **Symmetries of a square (D₄):** the 8 operations that map a square to itself — 4 rotations (0°, 90°, 180°, 270°) and 4 reflections. This is a *finite* group with 8 elements. It's *non-abelian*: rotating then reflecting ≠ reflecting then rotating. Draw this. Literally take a square, label the corners, and track where each corner goes under each operation.
- **Invertible n×n matrices under multiplication (GL(n)):** the *general linear group*. This connects directly to your linear algebra: every invertible transformation is a group element. The identity is I. The inverse is the matrix inverse. This is the group that acts on vector spaces.
- **Permutation groups (Sₙ):** all ways to rearrange n objects. S₃ has 6 elements (3! = 6 ways to rearrange 3 objects). **This is the key group for neural networks** — permuting neurons in a hidden layer rearranges the weight matrix but preserves the function.
- **Orthogonal group O(n):** matrices Q where QᵀQ = I. These are rotations and reflections — exactly the U and V matrices from SVD! The orthogonal group preserves lengths and angles.

### The Geometric Intuition: Groups as Symmetries

- **A symmetry** of an object is a transformation that leaves the object "looking the same." A square has 8 symmetries (D₄). A circle has infinitely many (any rotation). An asymmetric blob has only the identity (just 1).
- **The key principle:** the more symmetries something has, the more "redundancy" in its description. If rotating a square by 90° gives the same square, then describing the square's position needs less information than you'd think — the 4 rotated positions are all "the same."
- **Orbits and stabilizers:** if a group G acts on a set X, the *orbit* of a point x is all the points you can reach from x by applying group elements: Orb(x) = {g · x : g ∈ G}. The *stabilizer* of x is the set of group elements that fix x: Stab(x) = {g ∈ G : g · x = x}. The orbit-stabilizer theorem says |Orb(x)| × |Stab(x)| = |G|. More symmetries fixing a point → smaller orbit → more redundancy.

### Permutation Symmetries in Neural Networks

- **The critical observation for SLT:** consider a simple neural network with input → hidden layer (n neurons) → output. If you permute the hidden neurons (swap neuron 3 with neuron 7, say), AND simultaneously permute the corresponding rows in the input-to-hidden weight matrix AND columns in the hidden-to-output weight matrix, **the network computes exactly the same function.**
- **In math:** if P is a permutation matrix, then the networks with weights (W₁, W₂) and (PW₁, W₂P⁻¹) compute the same function for all inputs. The group Sₙ (permutations of n hidden neurons) acts on weight space, and every point in weight space has an orbit of size n! (at most) — all computing the same function.
- **Why this creates singularities:** the loss function L(W₁, W₂) has the same value at all n! permuted copies of any weight configuration. This means the loss landscape has vast "flat directions" (directions where loss doesn't change at all). At points where some neurons are equal or zero, the orbits collapse — multiple distinct permutations map to the same point. These are *singularities* where the geometry of the loss landscape is qualitatively different from a smooth manifold.
- **This is WHY the RLCT ≠ d/2:** in classical statistics, the leading term in model complexity is d/2 where d is the parameter count. But the symmetries mean the *effective* dimension is smaller — many parameters are redundant. The RLCT λ measures the true effective complexity, accounting for these symmetries.

### Subgroups, Quotients, and Equivalence Classes

- **Subgroup:** a subset H ⊂ G that is itself a group under the same operation. The rotations of a square form a subgroup of D₄ (4 out of 8 elements).
- **Cosets:** for a subgroup H, the left coset gH = {gh : h ∈ H} is "H shifted by g." Cosets partition G into equal-sized chunks.
- **Quotient group G/H:** when H is a *normal* subgroup (gH = Hg for all g), the cosets themselves form a group. This is "G with H collapsed to a point." The quotient group captures the structure that remains after removing the redundancy of H.
- **For neural networks:** the weight space modulo permutation symmetry is a quotient — it's the space of *distinct functions* the network can compute, with all the symmetric copies identified. This quotient space has singularities, and their geometry is what SLT studies.

### Group Actions — Groups Acting on Spaces

- **A group action** of G on a set X assigns to each group element g a transformation of X, respecting the group structure: e · x = x and (g₁g₂) · x = g₁ · (g₂ · x).
- **Examples:**
  - Sₙ acts on ℝⁿ by permuting coordinates: σ · (x₁, ..., xₙ) = (x_{σ(1)}, ..., x_{σ(n)})
  - GL(n) acts on ℝⁿ by matrix multiplication: A · v = Av
  - D₄ acts on the square by rotations and reflections
- **Fixed points:** points x where g · x = x for all g ∈ G. In neural networks, weight configurations that are invariant under all neuron permutations are special — they correspond to networks where all hidden neurons compute the same thing. These are the most degenerate singularities.

## 📺 Watch — Primary

1. **3Blue1Brown — "Groups, the monster, and topology" (or "Group Theory, Pair of Socks")**
   - Search YouTube — if available, 3B1B's visual style makes group axioms intuitive
2. **Socratica — "Abstract Algebra: What is a Group?"**
   - https://www.youtube.com/watch?v=IP7nKFiTRbI
   - Clear, concise, with good examples
3. **Visual Group Theory — Nathan Carter lectures**
   - Search YouTube — emphasis on visual/geometric understanding of groups

## 📺 Watch — Secondary

4. **Michael Penn — "Abstract Algebra" playlist (first 5-11 videos)**
   - https://www.youtube.com/c/MichaelPennMath
   - More mathematical depth while remaining accessible
5. **Mathemaniac — "The math behind neural network symmetries"**
   - If available — directly connects groups to neural network weight space

## 📖 Read — Primary

- **"Visual Group Theory" by Nathan Carter** — Chapters 1–4
  - *The most visual, intuition-first introduction to group theory available. Uses color-coded diagrams called Cayley diagrams to make abstract structures concrete. Strongly recommended for your learning style.*
- **"An Introduction to the Theory of Groups" by Rotman** — Chapter 1–3 (if you want more rigor)
- **"Symmetry and the Monster" by Mark Ronan** — popular science book, for motivation

## 📖 Read — Secondary

- **"Algebra" by Artin** — Chapter 2 (Groups)
  - Standard undergraduate textbook. More rigorous than Visual Group Theory but very clear.
- **"Why Neural Networks Have Symmetries" (blog posts / SLT introductions)**
  - Jesse Hoogland's SLT blog: https://www.lesswrong.com/s/mqwA5FcL6SrHEQzYx
  - Connects neural network symmetries directly to singular learning theory

## 📖 Read — Going Deep

- **"Singular Learning Theory" by Sumio Watanabe** — Chapter 2 (algebraic geometry of singularities)
  - The primary source. Dense but this is where the group theory meets the loss landscape.
- **"Geometric Deep Learning" by Bronstein et al.**
  - https://geometricdeeplearning.com/
  - Comprehensive treatment of how symmetries (groups) structure deep learning architectures. Covers equivariance, invariance, and gauge theory.

## 🔨 Do

- **Symmetry exploration:** take a physical square (piece of paper works). Label the corners 1-4. Perform all 8 symmetries of D₄ (4 rotations, 4 reflections). Write each as a permutation of {1,2,3,4}. Build the multiplication table. Verify it satisfies the group axioms. Find which pairs of operations don't commute.
- **Permutation group exercise:** for S₃ (permutations of 3 objects), list all 6 elements. Compute the multiplication table. Find all subgroups. Identify which subgroups are normal.
- **Neural network symmetry demo:** create a simple 2→3→1 neural network in Python. Choose random weights. Apply a permutation to the hidden layer (swap rows of W₁, corresponding columns of W₂). Verify the network produces identical output on all inputs. Count how many distinct permutations exist (3! = 6).
- **Orbit visualization:** for the permutation group S₃ acting on ℝ³ by permuting coordinates, pick a point like (1, 2, 3). Compute its full orbit (all 6 permuted versions). Plot them in 3D. Then try (1, 1, 2) — its orbit has only 3 points (some permutations give the same result). Then try (1, 1, 1) — orbit size 1. See how symmetry creates different "orbit structures" at different points.
- **Key exercise:** explain in your own words: why does the existence of permutation symmetry in neural networks mean that the loss landscape must have singularities? Why can't the loss landscape be a smooth bowl (like ordinary linear regression) when the model has hidden-layer symmetries?

## 🔗 ML Connection

- **Weight space geometry:** the parameter space of a neural network is NOT a simple Euclidean space — it's a space with symmetries. Two different weight vectors can represent the same function. This redundancy has profound consequences for optimization (SGD navigates around singularities) and for model counting (how many "distinct" models exist in a given region).
- **Equivariant neural networks:** architectures designed to respect known symmetries. A convolutional neural network is equivariant to translation (shifting the input shifts the output). Group-equivariant networks generalize this to arbitrary groups — rotations, reflections, permutations of graph nodes. The group structure constrains the weight matrices, reducing parameters and improving generalization.
- **Loss landscape topology:** the orbits of the permutation group create a complex topology in weight space. Gradient descent doesn't just descend a smooth hill — it navigates around singularities, getting stuck near degenerate critical points where multiple orbits collide. Understanding this geometry is active research.

## 🧠 Alignment Connection

- **Singular Learning Theory** is built on neural network symmetries. The RLCT λ — the quantity that replaces d/2 in Bayesian model complexity — depends on the algebraic geometry of the singularities created by these symmetries. Groups and their orbits determine WHICH singularities exist and HOW COMPLEX they are.
- **Phase transitions in learning** (sudden acquisition of new capabilities) correspond to the training trajectory crossing from one singularity type to another. Understanding the group structure tells you what kinds of phase transitions are possible.
- **Model identifiability:** the fact that many weight configurations produce the same function means you can't uniquely identify a model's internal structure from its behavior. This is a fundamental challenge for interpretability — two models might behave identically but have very different internal mechanisms, related by a symmetry transformation.
