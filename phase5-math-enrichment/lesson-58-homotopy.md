# Lesson 58: Homotopy and Fundamental Groups — Counting Holes in Spaces

[← Point-Set Topology](lesson-57-point-set-topology.md) | [Back to TOC](../README.md) | [Next: Manifolds →](lesson-59-manifolds.md)

---

> **Why this lesson exists:** Point-set topology tells you whether a space is connected; homotopy theory tells you HOW it's connected. The fundamental group counts the "holes" in a space — loops that can't be shrunk to a point. For loss landscapes, the topology of level sets (the set of weights with loss ≤ ε) determines whether gradient descent can find all solutions. For algebraic geometry, the topology of a variety near a singularity — measured by its fundamental group — classifies the type of singularity. This feeds directly into the resolution of singularities that SLT requires.

## 🎯 Core Concepts

### Homotopy — Continuous Deformation

- **Two paths are homotopic** if one can be continuously deformed into the other while keeping the endpoints fixed. Formally, f₀ and f₁ are homotopic if there exists a continuous F: [0,1]×[0,1] → X with F(t,0) = f₀(t) and F(t,1) = f₁(t).
- **Homotopy equivalence of spaces:** X and Y are homotopy equivalent if there exist continuous maps f: X→Y and g: Y→X such that g∘f ≃ id_X and f∘g ≃ id_Y (where ≃ means homotopic). This is weaker than homeomorphism — a solid disk is homotopy equivalent to a point (you can "squish" it down).
- **Contractible spaces** are homotopy equivalent to a point. ℝⁿ is contractible — every loop can be shrunk to a point. A donut (torus) is not — the loop around the hole can't be shrunk.

### The Fundamental Group π₁

- **π₁(X, x₀)** is the set of loops based at x₀ (paths starting and ending at x₀), up to homotopy equivalence. Two loops are "the same" if one can be continuously deformed into the other.
- **Group operation:** concatenation of loops. Walk around loop α, then walk around loop β. The identity is the constant loop (stay at x₀). The inverse of a loop is the same loop traversed backward.
- **Key examples:**
  - π₁(ℝⁿ) = {e} (trivial — every loop shrinks to a point, no holes)
  - π₁(S¹) = ℤ (the integers — loops around a circle classified by winding number)
  - π₁(T²) = ℤ × ℤ (torus — two independent loops, around each "tube")
  - π₁(S²) = {e} (trivial — every loop on a sphere can be shrunk. The sphere has a "2D hole" but no "1D hole")

### Higher Homotopy Groups πₙ

- **πₙ(X)** measures n-dimensional "holes" using n-spheres instead of loops. π₂ uses 2-spheres, detecting 2D holes. π₃ uses 3-spheres, etc.
- **π₂(S²) = ℤ** — the 2-sphere has a non-trivial 2D hole (you can't shrink a 2-sphere wrapping around S² to a point).
- **Homotopy groups are hard to compute** — this is a major open area of mathematics. But the first few are tractable and very useful.

### Covering Spaces — Unfolding Topology

- **A covering space** of X is a space X̃ that "wraps around" X, with a projection map p: X̃ → X that's a local homeomorphism. Example: ℝ covers S¹ via the map t ↦ e^{2πit}. The real line wraps around the circle infinitely many times.
- **The fundamental group classifies covering spaces.** For each subgroup H ≤ π₁(X), there's a corresponding covering space. The universal cover (H = {e}) has trivial fundamental group — it's "fully unfolded."
- **For SLT:** the resolution of singularities (Lesson 60) is analogous to passing to a covering space — it "unfolds" the singularity into a smooth space, and the structure of the covering tells you the singularity type.

### Applications to Loss Landscapes

- **Level sets** L⁻¹(c) = {w : L(w) = c} are topological spaces. Their topology changes as c varies — this is Morse theory.
- **Critical values** of c are exactly where the topology changes. At a local minimum, a new connected component appears. At a saddle point, two components merge or a hole appears/disappears.
- **Morse inequalities** relate the number of critical points of each type (minima, saddles, maxima) to the topology of the loss landscape. More saddle points → more complex topology → harder optimization.
- **For neural networks:** the loss landscape has exponentially many saddle points (related to permutation symmetry). The topology is extremely complex. But the connected components of the low-loss region seem to have simpler topology — understanding why is an active research question.

## 📺 Watch — Primary

1. **Aleph 0 — "Algebraic Topology" introduction videos**
   - https://www.youtube.com/@Aleph0
2. **Aleph 0 — "The Fundamental Theorem of Algebra"**
   - https://www.youtube.com/watch?v=shEk8sz1oOw
   - *Uses winding numbers (a homotopy concept) to prove FTA — beautiful connection between topology and algebra.*
3. **Numberphile — "Topology of a Twisted Torus" or fundamental group visualizations**

## 📖 Read — Primary

- **"Algebraic Topology" by Allen Hatcher** — Chapter 1 (fundamental group)
  - Free online: https://pi.math.cornell.edu/~hatcher/AT/ATpage.html
  - *The standard reference, beautifully written.*
- **"Topology" by Munkres** — Chapters 9, 13 (fundamental group, covering spaces)

## 🔨 Do

- Compute π₁ of the figure-eight (two circles joined at a point). It's the free group on two generators — non-abelian. Draw loops representing the generators and their product.
- Visualize covering spaces: implement the covering map ℝ → S¹ via t ↦ (cos 2πt, sin 2πt). Plot several "sheets" of the covering.
- Morse theory exercise: for f(x,y) = x² - y², trace the level sets as c goes from -1 to 1. Watch the topology change at c = 0 (the saddle point).
- For a neural network loss landscape: compute the loss at many random weight vectors. Estimate the Betti numbers (number of connected components, number of loops) of the sublevel set L ≤ c for various c using persistent homology (use the ripser or giotto-tda library).

## 🔗 ML & Alignment Connection

**Persistent homology** (computational algebraic topology) is increasingly used to study neural network loss landscapes and representation spaces. By tracking how topological features (connected components, loops, voids) appear and disappear as you vary a threshold, you get a "fingerprint" of the landscape's structure. For alignment, this could help answer: does the low-loss region for aligned behavior have the same topology as the region for misaligned behavior? Are there topological barriers between them?
