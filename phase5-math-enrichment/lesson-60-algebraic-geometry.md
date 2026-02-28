# Lesson 60: Algebraic Geometry Essentials — Singularities and Resolution for SLT

[← Manifolds](lesson-59-manifolds.md) | [Back to TOC](../README.md) | [Next: Propositional & Predicate Logic →](lesson-61-propositional-logic.md)

---

> **Why this lesson exists:** This is the mathematical climax of the enrichment sequence. Singular Learning Theory's central result — the formula for the free energy of singular models — relies on the resolution of singularities from algebraic geometry. The RLCT (Real Log Canonical Threshold) is computed by "blowing up" the singularities in the loss landscape until they become smooth, then measuring how much the blow-up stretches the measure. This lesson gives you the algebraic geometry you need to understand that process.

## 🎯 Core Concepts

### Algebraic Varieties — Solutions of Polynomial Equations

- **An algebraic variety** V = V(f₁,...,fₖ) ⊂ ℝⁿ (or ℂⁿ) is the set of common zeros of polynomials f₁,...,fₖ. Lines, circles, hyperbolas, and neural network loss level sets are all varieties.
- **The Zariski topology:** a variety has a natural topology where closed sets are sub-varieties (solution sets of more equations). This is much coarser than the Euclidean topology — open sets are "most of the space."
- **The coordinate ring** ℝ[x₁,...,xₙ]/I(V) captures the algebraic structure of V. Functions on V are polynomials modulo the equations defining V.
- **For SLT:** the set of parameter values where the loss is minimized, K = {w : L(w) = L*}, is a variety (or analytic set). Its geometry determines the learning coefficient.

### Smooth vs Singular Points

- **A point p on V is smooth** if the Jacobian matrix of the defining equations has full rank at p. This means V looks like a manifold near p.
- **A point is singular** if the Jacobian drops rank. The variety has a "corner," "cusp," or "self-intersection" at p.
- **Examples:**
  - V = {x² + y² - 1 = 0} (circle): smooth everywhere. Jacobian (2x, 2y) never vanishes on V.
  - V = {y² - x³ = 0} (cusp): singular at the origin. Jacobian (−3x², 2y) = (0,0) there.
  - V = {xy = 0} (crossing lines): singular at origin. Jacobian (y, x) = (0,0) there.
  - V = {x² - y² = 0} (node, two crossing lines y = ±x): singular at origin.
- **For neural networks:** the set of minimizers K typically has singularities wherever neurons are "redundant" (equal weights, zero weights, etc.). These singularities are ubiquitous and structurally important.

### Blow-Ups — Resolution of Singularities

- **A blow-up** replaces a singular point with a "projective space" of directions through that point. Intuitively, you zoom in on the singularity and separate the branches.
- **Example — the node:** V = {x² - y² = 0} = {(x-y)(x+y) = 0} is two crossing lines. After blowing up the origin, the two branches separate into two parallel lines on a cylinder — the singularity is resolved.
- **The exceptional divisor** is the new set introduced by the blow-up (the "projective space of directions"). It's the price you pay for resolution.
- **Hironaka's theorem (1964):** every variety over ℝ or ℂ can be resolved by a finite sequence of blow-ups. This is one of the most important theorems of 20th-century mathematics. It guarantees that the SLT approach works — every singularity can eventually be made smooth.

### The RLCT — Real Log Canonical Threshold

- **Setup:** near a singular minimizer, the loss behaves as L(w) - L* = f(w) where f vanishes on K. The RLCT λ measures how fast f grows away from K.
- **For smooth models (regular case):** if K is a smooth point (non-degenerate Hessian), then f ≈ w₁² + ... + wₖ², and λ = k/2 (half the parameter count). This gives BIC.
- **For singular models:** after resolution of singularities, the blow-up coordinates transform f into a normal crossing form: f ∘ π = u₁^{a₁} · ... · uₘ^{aₘ}. The RLCT is λ = min_i (b_i + 1)/(2a_i) where b_i accounts for the Jacobian of the blow-up.
- **λ < k/2 always for singular models.** Neural networks are ALWAYS singular (due to permutation symmetry). So their effective complexity (measured by λ) is always less than their parameter count. This is the mathematical explanation for why deep learning works — over-parameterized networks are "less complex" than their parameter count suggests.
- **The free energy formula:** F = nL* + λ log n - (m-1) log log n + O(1), where λ is the RLCT and m is the multiplicity. Compare with BIC: F ≈ nL* + (k/2) log n. The RLCT replaces k/2.

### Computing RLCTs — Examples

- **1D: f(w) = w^{2k}.** The integral ∫ w^{-2kt} dw converges iff t < 1/(2k), so RLCT = 1/(2k). Compare with the regular case f = w² where RLCT = 1/2 = k/2 for k=1. The singularity f = w^{2k} has lower RLCT → simpler effective model.
- **2D node: f(w₁,w₂) = w₁²w₂².** After blow-up (polar-like coordinates), this resolves. The RLCT turns out to be 1/2 < 2/2 = 1 (the "regular" value for 2 parameters).
- **Neural network example:** for a single-neuron network y = a·σ(bx + c), the set of minimizers when the true function is y=0 includes both a=0 (any b,c) and the limit b→±∞ with a→0. The RLCT is 1/4 for a ReLU neuron — much less than the 3/2 that parameter counting would suggest.

## 📺 Watch — Primary

1. **Jesse Hoogland & Daniel Murfet — "Introduction to Singular Learning Theory" (YouTube)**
   - *The most accessible introduction to SLT for ML researchers.*
2. **Tadashi Tokieda — "Topology and Geometry" (African Institute lectures, YouTube)**
   - *Beautiful lectures on geometric intuition for algebraic concepts.*

## 📖 Read — Primary

- **"Algebraic Geometry and Statistical Learning Theory" by Sumio Watanabe** — Chapters 1–4
  - *The foundational SLT textbook. Dense but essential.*
- **"Invitation to Algebraic Geometry" by Smith et al.** — Chapters 1–3
  - *Gentler introduction to varieties, singularities, blow-ups.*

## 📖 Read — Secondary

- **"An Invitation to Singular Learning Theory" by Liam Carroll et al.**
  - *Recent tutorial paper bridging AG and ML. Start here if Watanabe is too dense.*

## 🔨 Do

- Classify the singularity type (smooth, node, cusp) for: y² - x² = 0, y² - x³ = 0, y² - x⁵ = 0, y² - x²(x+1) = 0. Plot each variety. Compute the Jacobian at singular points.
- Blow-up by hand: for V = {x² - y² = 0}, substitute y = tx (blow-up coordinates), show the strict transform separates the two branches. Plot the original and resolved variety.
- Compute the RLCT of f(w) = w⁴ in 1D. Compute the integral ∫₀¹ w^{-4t} dw and find the pole.
- Numerical RLCT estimation: for a 1-hidden-unit ReLU network trained to learn y=0, sample the loss near the singular minimizers and fit the power-law behavior to estimate λ. Compare with the theoretical λ = 1/4.
- Read one section of Watanabe's book or the Carroll et al. tutorial and write a one-paragraph summary of the main theorem in your own words.
