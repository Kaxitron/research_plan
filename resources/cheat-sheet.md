# Mathematics Cheat Sheet

[Back to TOC](../README.md)

*A living reference of formulas, identities, and key insights from the curriculum.*

*⚠️ When adding a new cheat sheet item, place it in the correct phase and block section below. Also add a corresponding link in the Table of Contents. Calculus items go into one of the six blocks (Fundamentals, ODEs, Multivariable, Vector Calculus, PDEs, Matrix Calculus). Probability items go into Phase 3, and so on.*

*⚠️ GitHub markdown can mangle LaTeX that contains characters GitHub interprets as formatting (e.g., `*` for bold/italic). Escape these with backslashes (e.g., `y\*` instead of `y*` inside LaTeX) or use plain text math when LaTeX won't render cleanly.*

---

## 📑 Table of Contents

### [Conceptual Foundations](#-key-conceptual-notes)

### Phase 1 — Linear Algebra
- [1. Vectors](#1-vectors)
- [2. Linear Combinations, Span, and Basis](#2-linear-combinations-span-and-basis)
- [3. Dot Product](#3-dot-product)
- [4. Cross Product (3D only)](#4-cross-product-3d-only)
- [5. Cosine Similarity](#5-cosine-similarity)
- [6. Matrix-Vector Multiplication](#6-matrix-vector-multiplication-two-views)
- [7. Matrix-Matrix Multiplication](#7-matrix-matrix-multiplication)
- [8. Rank, Null Space, and Column Space](#8-rank-null-space-and-column-space)
- [9. Determinant](#9-determinant)
- [10. Eigenvalues and Eigenvectors](#10-eigenvalues-and-eigenvectors)
- [11. Singular Value Decomposition (SVD)](#11-singular-value-decomposition-svd)
- [11b. PCA and the SVD Connection](#11b-pca-and-the-svd-connection)
- [12. Orthogonality and Projections](#12-orthogonality-and-projections)
- [13. Gram-Schmidt Process](#13-gram-schmidt-process)
- [14. Norms — Measuring Size](#14-norms--measuring-size)
- [15. Special Matrices](#15-special-matrices)
- [16. Change of Basis](#16-change-of-basis)
- [17. Ordinary Least Squares (OLS)](#17-ordinary-least-squares-ols)
- [18. Ridge Regression (L2 Regularization)](#18-ridge-regression-l2-regularization)
- [19. Lasso Regression (L1 Regularization)](#19-lasso-regression-l1-regularization)
- [20. Elastic Net (L1 + L2 combined)](#20-elastic-net-l1--l2-combined)
- [Quick Reference: The Regression Family](#quick-reference-the-regression-family)

### Phase 1 — Applied Statistics Preview
- [Correlation Coefficient (r)](#correlation-coefficient-r)
- [Coefficient of Determination (r²)](#coefficient-of-determination-r)

### Phase 2 — Calculus

#### [Fundamentals of Calculus](#fundamentals-of-calculus)
- [21. Derivatives and Differentials](#21-derivatives-and-differentials)
- [22. L'Hôpital's Rule](#22-lhôpitals-rule)
- [23. Limits and Continuity](#23-limits-and-continuity)
- [24. Squeeze Theorem](#24-squeeze-theorem)
- [25. Three Foundational Theorems (IVT, EVT, MVT)](#25-three-foundational-theorems-ivt-evt-mvt)
- [26. Extended Derivative Table](#26-extended-derivative-table)
- [27. Trigonometric Identities](#27-trigonometric-identities)
- [28. Integration — Fundamentals](#28-integration--fundamentals)
- [29. u-Substitution](#29-u-substitution--the-chain-rule-in-reverse)
- [30. Integration by Parts](#30-integration-by-parts--the-product-rule-in-reverse)
- [31. Trigonometric Substitution](#31-trigonometric-substitution--handling-square-roots)
- [32. Partial Fraction Decomposition](#32-partial-fraction-decomposition)
- [33. Improper Integrals](#33-improper-integrals--integrating-to-infinity)
- [34. Critical Points and Optimization](#34-critical-points-and-optimization)
- [35. Series and Convergence](#35-series-and-convergence)
- [36. Newton's Method](#36-newtons-method)
- [37. Inverse Function Derivatives](#37-inverse-function-derivatives)
- [38. Polar Coordinates](#38-polar-coordinates)
- [39. Taylor's Theorem — Remainder Forms](#39-taylors-theorem--remainder-forms)

#### [Ordinary Differential Equations](#ordinary-differential-equations)
- [40. First-Order ODEs — Solution Methods](#40-first-order-odes--solution-methods)
- [41. Exact Equations and Integrating Factors for Non-Exact Equations](#41-exact-equations-and-integrating-factors-for-non-exact-equations)
- [42. Constant-Coefficient Homogeneous Linear ODEs](#42-constant-coefficient-homogeneous-linear-odes)
- [43. The Wronskian](#43-the-wronskian)
- [44. Resonance and Forced Vibrations](#44-resonance-and-forced-vibrations)
- [45. Nonhomogeneous Equations — Undetermined Coefficients](#45-nonhomogeneous-equations--undetermined-coefficients)
- [46. Nonhomogeneous Equations — Variation of Parameters](#46-nonhomogeneous-equations--variation-of-parameters)
- [47. Power Series Solutions](#47-power-series-solutions)
- [48. The Laplace Transform](#48-the-laplace-transform)
- [49. Systems of ODEs and Phase Portraits](#49-systems-of-odes-and-phase-portraits)

#### [Multivariable Calculus](#multivariable-calculus)
*Section not yet started — items will be added during lessons 19–23.*

#### [Vector Calculus](#vector-calculus)
*Section not yet started — items will be added during lessons 24–28.*

#### [Partial Differential Equations](#partial-differential-equations)
*Section not yet started — items will be added during lessons 29–33.*

#### [Matrix Calculus & Optimization](#matrix-calculus--optimization)
*Section not yet started — items will be added during lessons 34–36.*

### Phase 3 — Probability & Statistics
*Section not yet started — items will be added during lessons 37–52.*

### Phase 4 — Machine Learning & Interpretability
*Section not yet started — items will be added during lessons 53–66.*

### Phase 5 — Extended Mathematical Foundations
*Section not yet started — items will be added during lessons 67–79.*

### Phase 6 — Alignment Theory
*Section not yet started — items will be added during lessons 80–84.*

### [Key Identities Quick Reference](#-key-identities-quick-reference)

---

## 📝 Key Conceptual Notes

**MSE is the question, regression methods are the answer:**
- **MSE (Mean Squared Error)** = (1/n) Σ(yᵢ - ŷᵢ)² — the loss function measuring prediction error
- **OLS (Ordinary Least Squares)** = the method that minimizes MSE with no constraints
- **Ridge regression** = minimizes MSE + L2 penalty (shrinks weights)
- **Lasso regression** = minimizes MSE + L1 penalty (zeros out weights)
- **L∞ regularization** = minimizes MSE + L∞ penalty (constrains max weight magnitude; rarely used — the hypercube norm ball has no corners or curvature preference, so it doesn't encourage sparsity or uniform shrinkage in a useful way)

**The norm ball determines the regression behavior:**
- L1 ball = diamond → corners on axes → sparsity (lasso)
- L2 ball = circle → smooth → uniform shrinkage (ridge)
- L∞ ball = square → flat faces → pushes weights to equal magnitude

**Regularization is secretly Bayesian inference:**
- Ridge (L2 penalty) = Gaussian prior on weights
- Lasso (L1 penalty) = Laplace prior on weights

---

## 1. Vectors

**Addition:** tip-to-tail composition

**Scalar multiplication:** stretching/shrinking

**Key insight:** coordinates only mean something relative to a basis. Change the basis, change the numbers — the arrow stays the same.

---

## 2. Linear Combinations, Span, and Basis

**Linear combination:** a₁v₁ + a₂v₂ + ... + aₙvₙ

**Span:** the set of ALL vectors reachable via linear combinations

**Basis:** a minimal set of vectors that spans the whole space. Need exactly n vectors for ℝⁿ.

**Linear independence:** no vector in the set can be written as a linear combination of the others. Equivalently, the only solution to a₁v₁ + a₂v₂ + ... = 0 is all aᵢ = 0.

---

## 3. Dot Product

**Algebraic:**

$$a \cdot b = a_1 b_1 + a_2 b_2 + \ldots + a_n b_n = \sum_i a_i b_i$$

**Geometric:**

$$a \cdot b = \|a\| \, \|b\| \cos\theta$$

**What the sign tells you:**
- a · b > 0 → angle < 90° (roughly same direction)
- a · b = 0 → angle = 90° (perpendicular / orthogonal)
- a · b < 0 → angle > 90° (roughly opposite)

**Dot product as projection:** a · b = |a| × (length of b's shadow onto a)

---

## 4. Cross Product (3D only)

$$a \times b = \|a\| \, \|b\| \sin\theta \; \hat{n}$$

where n̂ is the unit vector perpendicular to both a and b (right-hand rule).

**Determinant formula:**

$$a \times b = \det \begin{bmatrix} \hat{i} & \hat{j} & \hat{k} \\\\ a_1 & a_2 & a_3 \\\\ b_1 & b_2 & b_3 \end{bmatrix}$$

**Key property:** |a × b| = area of the parallelogram spanned by a and b

---

## 5. Cosine Similarity

$$\cos\theta = \frac{a \cdot b}{\|a\| \, \|b\|} = \hat{a} \cdot \hat{b}$$

Strips out magnitude, measures only directional similarity. THE similarity measure in embedding spaces.

---

## 6. Matrix-Vector Multiplication (Two Views)

Given Ax = y:

**Row view:** each output entry yᵢ is a dot product of row i with x (pattern matching)

**Column view:** the output y is a linear combination of the columns of A, weighted by entries of x

Both are true simultaneously. Switching between them is a superpower.

---

## 7. Matrix-Matrix Multiplication

AB means "apply B first, then A" (function composition).

**Key properties:**
- AB ≠ BA in general (not commutative)
- (AB)C = A(BC) (associative)
- (AB)ᵀ = BᵀAᵀ (reverse order for transpose)

---

## 8. Rank, Null Space, and Column Space

**Column space** of A = span of columns = {Ax : for all x} = all possible outputs

**Null space** (kernel) of A = {x : Ax = 0} = inputs that get crushed to zero

**Rank** = dimension of column space = number of linearly independent columns

### Row Echelon Form

The result of Gaussian elimination. A matrix is in **row echelon form** when:
1. All zero rows are at the bottom
2. Each row's **pivot** (first nonzero entry) is to the right of the pivot above it
3. Everything below each pivot is zero

**Example:**

```
[1  2  1]        [1  2  1]
[2  4  3]   →    [0  0  1]    ← echelon form
[3  6  4]        [0  0  0]
```

**How to get there:** subtract multiples of earlier rows from later rows to zero out entries below pivots (row reduction / Gaussian elimination).

**What it tells you:**
- **Rank** = number of pivots (nonzero rows)
- **Pivot columns** = linearly independent columns (basis for column space)
- **Free variables** = columns without pivots → these parameterize the null space
- **Null space:** set free variables to arbitrary values, solve backwards for pivot variables

**Reduced row echelon form (RREF):** additionally requires pivots = 1 and zeros above each pivot too. Gives the unique simplest form of the system.

**Rank-Nullity Theorem:**

$$\text{rank}(A) + \text{nullity}(A) = n \quad \text{(number of columns)}$$

Information preserved + information destroyed = total information.

---

## 9. Determinant

**Meaning:** the factor by which a transformation scales area/volume

$$\det(A) = \text{signed scaling factor}$$

- det > 0: preserves orientation
- det < 0: flips orientation (mirror)
- det = 0: squishes to lower dimension (singular, non-invertible)

**2×2 formula:**

$$\det \begin{bmatrix} a & b \\\\ c & d \end{bmatrix} = ad - bc$$

**Key properties:**
- det(AB) = det(A) · det(B)
- det(A⁻¹) = 1/det(A)
- det(Aᵀ) = det(A)
- det = 0 ↔ rank deficient ↔ non-invertible ↔ null space is non-trivial (all the same condition)

---

## 10. Eigenvalues and Eigenvectors

**Definition:** Av = λv — the matrix only scales v, doesn't rotate it.

**Characteristic equation:**

$$\det(A - \lambda I) = 0$$

**Diagonalization:**

$$A = PDP^{-1}$$

where P = matrix of eigenvectors (columns), D = diagonal matrix of eigenvalues. A is only diagonalizable if it is square and it has n linearly independent eigenvectors, where n = the number of columns/rows.

**Meaning:** change to eigenbasis → scale each direction → change back.

**Powers become trivial:**

$$A^n = PD^nP^{-1}$$

**Trace-determinant connection:**
- tr(A) = sum of eigenvalues
- det(A) = product of eigenvalues

---

## 11. Singular Value Decomposition (SVD)

$$A = U \Sigma V^T$$

**Works for ANY matrix** (any shape, any rank).

| Component | What it does | Properties |
|-----------|-------------|------------|
| Vᵀ | Rotate input to align with natural axes | V is orthogonal (Vᵀ = V⁻¹) |
| Σ | Scale each axis (singular values σ₁ ≥ σ₂ ≥ ... ≥ 0) | Diagonal, non-negative |
| U | Rotate output to final orientation | U is orthogonal |

**Geometric picture:** every matrix = rotate → scale → rotate. Circle becomes ellipse.

**Key facts:**
- Rank = number of nonzero singular values
- Singular values of A = square roots of eigenvalues of AᵀA
- Best rank-k approximation: keep top k singular values (Eckart-Young theorem)
- Condition number = σ₁/σₙ (measures how "elongated" the transformation is)

---

## 11b. PCA and the SVD Connection

**PCA = eigenvectors of the covariance matrix C = (1/n)XᵀX**

**Why SVD gives you PCA directly:**

$$X^T X = (U\Sigma V^T)^T (U\Sigma V^T) = V\Sigma^T U^T U \Sigma V^T = V\Sigma^2 V^T$$

UᵀU = I cancels the rotation, leaving VΣ²Vᵀ — which is already the eigendecomposition of XᵀX. So:
- **Eigenvectors of XᵀX = columns of V** (the right singular vectors of X)
- **Eigenvalues of XᵀX = σ²** (squared singular values)

**Why U disappears:** AᵀA is always symmetric → orthogonal eigenbasis → pure scaling in that basis → the two rotations in AᵀA cancel, leaving only Σ² in the V basis.

**In practice:** real algorithms compute SVD directly on X (never forming XᵀX), avoiding squaring the condition number. For hand computation, eigendecompose XᵀX directly.

---

## 12. Orthogonality and Projections

**Orthogonal:** a · b = 0 (perpendicular, completely independent directions)

**Orthonormal basis:** all vectors are unit length AND mutually perpendicular

**Orthogonal matrix Q:** QᵀQ = I, equivalently Q⁻¹ = Qᵀ. These are pure rotations (+ reflections). Preserve lengths and angles.

### Projection onto a vector

$$\text{proj}_v(u) = \frac{u \cdot v}{v \cdot v} \, v$$

### Projection onto a subspace

Given subspace spanned by columns of A:

$$\text{proj}_W(b) = A(A^T A)^{-1} A^T b$$

**Projection matrix:**

$$P = A(A^T A)^{-1} A^T$$

**Key properties:**
- P² = P (idempotent — projecting twice does nothing new)
- Pᵀ = P (symmetric)

### The Orthogonality Principle

$$A^T e = 0 \quad \text{where } e = b - A\hat{x}$$

The error vector is perpendicular to the column space. This is THE geometric insight of least squares.

### Decomposition of b

$$b = \hat{y} + e$$

where ŷ = Ax̂ (projection onto column space) and e = b - ŷ (perpendicular residual).

---

## 13. Gram-Schmidt Process

Converts any basis into an orthonormal one:

1. Take first vector, normalize it
2. Take next vector, subtract its projection onto all previous vectors, normalize
3. Repeat

Each step removes "already covered" directions, leaving only the new perpendicular component.

---

## 14. Norms — Measuring Size

| Norm | Formula | Ball shape (2D) | Encourages |
|------|---------|----------------|------------|
| L1 (Manhattan) | \|v₁\| + \|v₂\| + ... | Diamond ◇ | Sparsity |
| L2 (Euclidean) | √(v₁² + v₂² + ...) | Circle ○ | Small weights |
| L∞ (Max) | max(\|v₁\|, ..., \|vₙ\|) | Square □ | Equal magnitudes |

**For matrices:**
- **Frobenius norm:** ‖A‖_F = √(sum of all squared entries) — treats matrix as one long vector
- **Spectral norm:** ‖A‖₂ = largest singular value σ₁ — maximum stretching factor

**Ordering:** ‖v‖∞ ≤ ‖v‖₂ ≤ ‖v‖₁ (always)

---

## 15. Special Matrices

**Symmetric** (A = Aᵀ):
- Eigenvalues always real
- Eigenvectors always orthogonal
- Diagonalizable as A = QDQᵀ (Q orthogonal)

**Positive definite** (all eigenvalues > 0):
- xᵀAx > 0 for all nonzero x
- Geometrically: a "bowl" shape (no saddle directions)
- Hessian positive definite at a point → local minimum

**Positive semi-definite / PSD** (all eigenvalues ≥ 0):
- xᵀAx ≥ 0 for all x
- Covariance matrices are always PSD
- Gram matrices (AᵀA) are always PSD

**Trace properties:**
- tr(A) = sum of diagonal entries = sum of eigenvalues
- tr(AB) = tr(BA)
- ‖A‖²_F = tr(AᵀA)

---

## 16. Change of Basis

**Converting coordinates:** if B has new basis vectors as columns, then B⁻¹v converts v from standard basis to new basis.

**Same transformation, different basis:**

$$B^{-1}AB = \text{same transformation described in basis } B$$

**Eigendecomposition as change of basis:** A = PDP⁻¹ means "go to eigenbasis, scale, come back"

**SVD as two changes of basis:** A = UΣVᵀ means "go to V-basis (input), scale, go to U-basis (output)"

---

## 17. Ordinary Least Squares (OLS)

**Problem:** find x that minimizes ‖Ax - b‖² (when Ax = b has no exact solution)

**Solution:**

$$\hat{x} = (A^T A)^{-1} A^T b$$

**Equivalently:** solve the normal equations Aᵀ A x̂ = Aᵀ b

**This IS projection.** The least squares solution is the projection of b onto the column space of A.

---

## 18. Ridge Regression (L2 Regularization)

**Minimizes:** ‖Ax - b‖² + λ‖x‖₂²

**Solution:**

$$\hat{x}_{\text{ridge}} = (A^T A + \lambda I)^{-1} A^T b$$

**What λI does to eigenvalues of AᵀA:**
- Original eigenvalues: [λ₁, λ₂, ..., λₙ]
- After adding λI: [λ₁ + λ, λ₂ + λ, ..., λₙ + λ]
- Tiny eigenvalues get boosted → stable inversion
- Condition number drops → more robust solution

**Properties:**
- Shrinks all weights toward zero, never TO zero
- Larger λ → more shrinkage, smaller weights, worse training fit, often better generalization
- λ = 0 recovers OLS
- λ → ∞ sends all weights to zero
- Equivalent to Gaussian prior on weights (Bayesian interpretation)

---

## 19. Lasso Regression (L1 Regularization)

**Minimizes:** ‖Ax - b‖² + λ‖x‖₁

**No closed-form solution** — |xᵢ| has no derivative at xᵢ = 0 (the V-shaped corner). Requires iterative algorithms.

**Soft-thresholding operator** (the core building block):

$$S(z, \lambda) = \text{sign}(z) \cdot \max(|z| - \lambda, \; 0)$$

**Properties:**
- Shrinks weights AND drives some to exactly zero → automatic feature selection
- The diamond-shaped L1 norm ball has corners on axes → elliptical contours hit corners → sparse solutions
- Equivalent to Laplace prior on weights (Bayesian interpretation)
- Solved via coordinate descent: optimize one weight at a time, cycle, repeat

---

## 20. Elastic Net (L1 + L2 combined)

**Minimizes:** ‖Ax - b‖² + λ₁‖x‖₁ + λ₂‖x‖₂²

Gets sparsity from L1 AND stability from L2. Useful when features are correlated (lasso arbitrarily picks one; elastic net keeps groups together).

---

## Quick Reference: The Regression Family

| Method | Penalty | Solution | Weights → 0? | Norm ball |
|--------|---------|----------|--------------|-----------| 
| OLS | None | (AᵀA)⁻¹Aᵀb | No | — |
| Ridge | λ‖x‖₂² | (AᵀA + λI)⁻¹Aᵀb | Shrink, never zero | Circle |
| Lasso | λ‖x‖₁ | Iterative (no closed form) | Yes, exact zeros | Diamond |
| Elastic Net | λ₁‖x‖₁ + λ₂‖x‖₂² | Iterative | Yes, with grouping | Rounded diamond |

---

## Statistics — Correlation and Goodness of Fit

*Placeholder section — will be expanded in Phase 3b (Applied Statistics & Causal Reasoning).*

### Correlation Coefficient (r)

**r is cosine similarity of centered data vectors.**

Given data vectors x and y, center them by subtracting their means:

$$\tilde{x} = x - \bar{x}, \quad \tilde{y} = y - \bar{y}$$

Then:

$$r = \frac{\tilde{x} \cdot \tilde{y}}{\|\tilde{x}\| \, \|\tilde{y}\|} = \cos\theta$$

where θ is the angle between the centered data vectors in n-dimensional space.

**What r tells you:**
- r = +1 → perfect positive linear relationship (vectors perfectly aligned)
- r = -1 → perfect negative linear relationship (vectors perfectly opposite)
- r = 0 → no linear relationship (vectors perpendicular)
- r only measures **linear** relationships — a perfect parabola can have r ≈ 0

### Coefficient of Determination (r²)

**r² is the fraction of total variance explained by the model.**

From the projection decomposition (Lesson 9), the centered y vector splits into two perpendicular pieces:

$$\tilde{y} = \hat{y} + e$$

where ŷ = projection (predicted values) and e = residual (perpendicular to ŷ).

By the Pythagorean theorem (they're perpendicular!):

$$\|\tilde{y}\|^2 = \|\hat{y}\|^2 + \|e\|^2$$

$$\text{SST} = \text{SSR} + \text{SSE}$$

$$\text{Total variance} = \text{Explained variance} + \text{Unexplained variance}$$

Then:

$$r^2 = \frac{\|\hat{y}\|^2}{\|\tilde{y}\|^2} = \frac{SSR}{SST} = \frac{\text{explained variance}}{\text{total variance}}$$

**What r² tells you:**
- r² = 1 → residual has length 0, model captures everything
- r² = 0 → projection has length 0, model explains nothing (just predicts the mean)
- r² = 0.7 → 70% of variance explained, 30% unexplained

**Key connections:**
- r² is literally the ratio of squared projection length to total vector length
- Pythagorean theorem works because ŷ ⊥ e (the orthogonality principle from Lesson 9)
- Adding more predictors always increases R² (even nonsense ones) → use **adjusted R²** to penalize complexity
- Adjusted R² is conceptually similar to regularization: prefer simpler explanations

---

# Fundamentals of Calculus

---

## 21. Derivatives and Differentials

**The derivative** of f(x) is the instantaneous rate of change:

$$\frac{df}{dx} = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}$$

**Differentials — what dx and df actually mean:**
- **dx** = a tiny nudge in x (an infinitesimally small change to the input)
- **df** = the resulting tiny nudge in f (the infinitesimally small change in the output caused by dx)
- The derivative df/dx is literally a ratio of these two tiny quantities
- Rearranging: **df = f'(x) · dx** — this says "the tiny change in output = slope × tiny change in input"
- This is just **rise = slope × run** at infinitesimal scale

**Core derivative rules:**

| Function | Derivative |
|----------|-----------|
| $x^n$ | $nx^{n-1}$ |
| $e^x$ | $e^x$ |
| $\ln(x)$ | $1/x$ |
| $\sin(x)$ | $\cos(x)$ |
| $\cos(x)$ | $-\sin(x)$ |
| $\sigma(x) = \frac{1}{1+e^{-x}}$ (sigmoid) | $\sigma(x)(1 - \sigma(x))$ |
| $\tanh(x)$ | $1 - \tanh^2(x)$ |
| $\text{ReLU}(x) = \max(0,x)$ | $0$ if $x<0$, $1$ if $x>0$, undefined at $0$ |

**Product rule:** $(fg)' = f'g + fg'$

**Quotient rule:** $(f/g)' = (f'g - fg') / g^2$

---


## 22. L'Hôpital's Rule

**The problem:** Some limits give you indeterminate forms like 0/0 or ∞/∞ — the ratio could be anything, and direct substitution doesn't work.

**The rule:** If $\lim_{x \to c} \frac{f(x)}{g(x)}$ gives $\frac{0}{0}$ or $\frac{\pm\infty}{\pm\infty}$, then:

$$\lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)}$$

provided the right-hand limit exists. You differentiate the top and bottom **separately** (this is NOT the quotient rule).

**Geometric intuition:** When both f and g approach 0 at the same point, the ratio f/g depends on *how fast* each approaches 0 — which is exactly what their derivatives measure. The function that shrinks faster "wins" the race to zero, making the ratio blow up or vanish.

**Example:**

$$\lim_{x \to 0} \frac{\sin(x)}{x} = \frac{0}{0} \quad \Rightarrow \quad \lim_{x \to 0} \frac{\cos(x)}{1} = 1$$

**When to apply:**
- ✅ Only for indeterminate forms: 0/0 or ∞/∞
- ❌ NOT for cases like 1/0 or 5/∞ (those aren't indeterminate — they resolve directly)
- ✅ Can apply repeatedly if result is still indeterminate

**Common indeterminate forms reducible to L'Hôpital's:**
- $0 \cdot \infty$ → rewrite as $\frac{f}{1/g}$ to get 0/0 or ∞/∞
- $\infty - \infty$ → combine into a single fraction
- $1^\infty$, $0^0$, $\infty^0$ → take ln first, then exponentiate after

**🔗 ML Connection:** L'Hôpital's Rule shows up when analyzing loss functions near critical points — e.g., understanding how cross-entropy loss $-\log(p)$ behaves as predicted probability $p \to 0$ or $p \to 1$, or when deriving limits in softmax temperature scaling as $T \to 0$ or $T \to \infty$.

## 23. Limits and Continuity

**Limit (ε-δ definition):** $\lim_{x \to a} f(x) = L$ means: for every $\varepsilon > 0$, there exists $\delta > 0$ such that

$$0 < |x - a| < \delta \implies |f(x) - L| < \varepsilon$$

**One-sided limits:**

$$\lim_{x \to a^-} f(x) \quad \text{(from left)} \qquad \lim_{x \to a^+} f(x) \quad \text{(from right)}$$

Two-sided limit exists iff both one-sided limits exist and agree.

**Continuity at a:** $f$ is continuous at $a$ iff $\lim_{x \to a} f(x) = f(a)$.

Three requirements: (1) limit exists, (2) $f(a)$ is defined, (3) they're equal.

**Three ways to fail continuity:**
- **Jump discontinuity:** one-sided limits disagree (step function at 0)
- **Removable discontinuity (hole):** limit exists but $f(a)$ is missing or wrong
- **Blow-up:** $f(x) \to \pm\infty$ (like $1/x$ at $x = 0$)

**Hierarchy:** differentiable $\implies$ continuous $\implies$ limit exists (each arrow one-way only)

**ML connection:** ReLU is continuous but not differentiable at $x = 0$ — continuity is enough for practical optimization.

---

## 24. Squeeze Theorem

If $g(x) \leq f(x) \leq h(x)$ near $a$, and $\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L$, then:

$$\lim_{x \to a} f(x) = L$$

**Classic example:**

$$\lim_{x \to 0} x^2 \sin\!\left(\frac{1}{x}\right) = 0$$

because $-x^2 \leq x^2 \sin(1/x) \leq x^2$ and both bounds $\to 0$.

**ML connection:** The bounding strategy — when you can't compute exact generalization error, bound it above and below by computable quantities and show both converge. PAC learning is built on this.

---

## 25. Three Foundational Theorems (IVT, EVT, MVT)

All three require **continuity** as their entry ticket.

### Intermediate Value Theorem (IVT)

If $f$ is continuous on $[a, b]$ and $y$ is between $f(a)$ and $f(b)$, then:

$$\exists \; c \in (a, b) \text{ such that } f(c) = y$$

A continuous function can't skip over a value. **Why it matters:** guarantees root-finding algorithms (bisection method, Newton's method) work.

### Extreme Value Theorem (EVT)

If $f$ is continuous on a **closed** interval $[a, b]$, then $f$ attains its maximum and minimum on $[a, b]$:

$$\exists \; c, d \in [a, b] \text{ such that } f(c) \leq f(x) \leq f(d) \quad \forall x \in [a, b]$$

All three conditions matter — remove "continuous," "closed," or "bounded" and the theorem fails.

**ML connection:** Weight space $\mathbb{R}^n$ is unbounded (not compact), so EVT doesn't directly apply. **Weight decay** ($L_2$ regularization) constrains weights to a bounded region, restoring compactness so the minimum is guaranteed to exist.

### Mean Value Theorem (MVT)

If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, then:

$$\exists \; c \in (a, b) \text{ such that } f'(c) = \frac{f(b) - f(a)}{b - a}$$

Somewhere the instantaneous rate equals the average rate. The tangent line is parallel to the secant.

**ML connection:** Guarantees gradient descent makes progress — if the gradient is nonzero, the function value actually changes. Underlies convergence proofs for optimization algorithms.

---

## 26. Extended Derivative Table

| Function | Derivative |
|----------|-----------|
| $x^n$ | $nx^{n-1}$ |
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln(a)$ |
| $\ln(x)$ | $1/x$ |
| $\log_a(x)$ | $\frac{1}{x \ln a}$ |
| $\sin(x)$ | $\cos(x)$ |
| $\cos(x)$ | $-\sin(x)$ |
| $\tan(x)$ | $\sec^2(x)$ |
| $\cot(x)$ | $-\csc^2(x)$ |
| $\sec(x)$ | $\sec(x)\tan(x)$ |
| $\csc(x)$ | $-\csc(x)\cot(x)$ |
| $\arcsin(x)$ | $\frac{1}{\sqrt{1 - x^2}}$ |
| $\arccos(x)$ | $\frac{-1}{\sqrt{1 - x^2}}$ |
| $\arctan(x)$ | $\frac{1}{1 + x^2}$ |
| $\sigma(x) = \frac{1}{1+e^{-x}}$ | $\sigma(x)(1 - \sigma(x))$ |
| $\tanh(x)$ | $1 - \tanh^2(x)$ |
| $\text{ReLU}(x) = \max(0,x)$ | $0$ if $x<0$, $1$ if $x>0$, undef at $0$ |

**Differentiation rules:**

| Rule | Formula |
|------|---------|
| Constant multiple | $(cf)' = cf'$ |
| Sum | $(f + g)' = f' + g'$ |
| Product | $(fg)' = f'g + fg'$ |
| Quotient | $(f/g)' = (f'g - fg') / g^2$ |
| Chain | $\frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)$ |
| Logarithmic derivative | $\frac{d}{dx}\ln(f(x)) = \frac{f'(x)}{f(x)}$ |

---

## 27. Trigonometric Identities

### Pythagorean Identities

$$\sin^2\theta + \cos^2\theta = 1$$

$$1 + \tan^2\theta = \sec^2\theta$$

$$1 + \cot^2\theta = \csc^2\theta$$

### Double Angle Formulas

$$\sin(2\theta) = 2\sin\theta\cos\theta$$

$$\cos(2\theta) = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta$$

$$\tan(2\theta) = \frac{2\tan\theta}{1 - \tan^2\theta}$$

### Half Angle / Power Reduction (critical for trig integrals)

$$\sin^2\theta = \frac{1 - \cos(2\theta)}{2} \qquad \cos^2\theta = \frac{1 + \cos(2\theta)}{2}$$

### Sum and Difference

$$\sin(A \pm B) = \sin A \cos B \pm \cos A \sin B$$

$$\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$$

### Product-to-Sum (useful for integrating products of trig functions)

$$\sin A \cos B = \tfrac{1}{2}[\sin(A+B) + \sin(A-B)]$$

$$\cos A \cos B = \tfrac{1}{2}[\cos(A-B) + \cos(A+B)]$$

$$\sin A \sin B = \tfrac{1}{2}[\cos(A-B) - \cos(A+B)]$$

### Key Values

| $\theta$ | $\sin$ | $\cos$ | $\tan$ |
|-----------|--------|--------|--------|
| $0$ | $0$ | $1$ | $0$ |
| $\pi/6$ (30°) | $1/2$ | $\sqrt{3}/2$ | $1/\sqrt{3}$ |
| $\pi/4$ (45°) | $\sqrt{2}/2$ | $\sqrt{2}/2$ | $1$ |
| $\pi/3$ (60°) | $\sqrt{3}/2$ | $1/2$ | $\sqrt{3}$ |
| $\pi/2$ (90°) | $1$ | $0$ | undef |

---

## 28. Integration — Fundamentals

### The Definite Integral

$$\int_a^b f(x) \, dx = \text{signed area between } f(x) \text{ and the x-axis from } a \text{ to } b$$

### Riemann Sums — Building the Integral

Chop $[a,b]$ into $n$ pieces of width $\Delta x = (b-a)/n$:

| Method | Formula | Idea |
|--------|---------|------|
| Left | $L_n = \sum_{i=0}^{n-1} f(x_i) \Delta x$ | Height at left endpoint |
| Right | $R_n = \sum_{i=1}^{n} f(x_i) \Delta x$ | Height at right endpoint |
| Midpoint | $M_n = \sum_{i=0}^{n-1} f\!\left(\frac{x_i+x_{i+1}}{2}\right) \Delta x$ | Height at midpoint |
| Trapezoidal | $T_n = \frac{L_n + R_n}{2}$ | Average left and right |
| Simpson's | $S_n = \frac{\Delta x}{3}[f(x_0) + 4f(x_1) + 2f(x_2) + \cdots + f(x_n)]$ | Parabolic arcs |

As $n \to \infty$, all converge to $\int_a^b f(x)\,dx$. Monte Carlo integration (used in Bayesian ML) is a randomized Riemann sum.

### Fundamental Theorem of Calculus

**Part 1:** $\frac{d}{dx} \int_a^x f(t) \, dt = f(x)$ — the derivative of "area so far" is the original function.

**Part 2:** $\int_a^b f(x) \, dx = F(b) - F(a)$ where $F' = f$ — evaluate any antiderivative at endpoints.

### Antiderivative Table

| Function | Antiderivative |
|----------|---------------|
| $x^n$ $(n \neq -1)$ | $\frac{x^{n+1}}{n+1} + C$ |
| $1/x$ | $\ln\|x\| + C$ |
| $e^x$ | $e^x + C$ |
| $a^x$ | $\frac{a^x}{\ln a} + C$ |
| $\sin(x)$ | $-\cos(x) + C$ |
| $\cos(x)$ | $\sin(x) + C$ |
| $\sec^2(x)$ | $\tan(x) + C$ |
| $\csc^2(x)$ | $-\cot(x) + C$ |
| $\sec(x)\tan(x)$ | $\sec(x) + C$ |
| $\csc(x)\cot(x)$ | $-\csc(x) + C$ |
| $\tan(x)$ | $-\ln\|\cos(x)\| + C$ |
| $\sec(x)$ | $\ln\|\sec(x) + \tan(x)\| + C$ |
| $\frac{1}{\sqrt{1-x^2}}$ | $\arcsin(x) + C$ |
| $\frac{1}{1+x^2}$ | $\arctan(x) + C$ |
| $\frac{1}{x^2+a^2}$ | $\frac{1}{a}\arctan(x/a) + C$ |
| $\frac{1}{\sqrt{a^2-x^2}}$ | $\arcsin(x/a) + C$ |

The $+ C$ is the **constant of integration** — vertical shifts don't change slope. Different $C$ values give different antiderivatives, all equally valid.

---

## 29. u-Substitution — The Chain Rule in Reverse

**The idea:** If you see a composite function with its inner derivative nearby, collapse it.

$$\int f(g(x)) \cdot g'(x) \, dx = \int f(u) \, du \quad \text{where } u = g(x)$$

**Steps:**
1. Identify the "inner function" $u = g(x)$
2. Compute $du = g'(x) \, dx$
3. Rewrite everything in terms of $u$ and $du$ (no $x$ should remain)
4. Integrate in $u$
5. Substitute back to $x$

**Example:**

$$\int 2x \cdot e^{x^2} \, dx$$

Let $u = x^2$, so $du = 2x \, dx$. The integral becomes:

$$\int e^u \, du = e^u + C = e^{x^2} + C$$

**For definite integrals:** either convert the bounds to $u$-values, or substitute back and use original bounds.

---

## 30. Integration by Parts — The Product Rule in Reverse

$$\int u \, dv = uv - \int v \, du$$

**Choosing u and dv — LIATE rule** (pick $u$ in this priority order):

| Priority | Type | Example |
|----------|------|---------|
| 1 | **L**ogarithmic | $\ln(x)$ |
| 2 | **I**nverse trig | $\arctan(x)$ |
| 3 | **A**lgebraic | $x^2$, $x$, $3x+1$ |
| 4 | **T**rigonometric | $\sin(x)$, $\cos(x)$ |
| 5 | **E**xponential | $e^x$ |

**Example:**

$$\int x \, e^x \, dx$$

Let $u = x$ (algebraic), $dv = e^x dx$. Then $du = dx$, $v = e^x$.

$$= x e^x - \int e^x \, dx = x e^x - e^x + C = e^x(x - 1) + C$$

**Tabular method** for repeated integration by parts (when $u$ is a polynomial): alternate signs (+, −, +, −, ...), differentiate $u$ column, integrate $dv$ column, multiply diagonally.

---

## 31. Trigonometric Substitution — Handling Square Roots

Use when you see $\sqrt{a^2 - x^2}$, $\sqrt{a^2 + x^2}$, or $\sqrt{x^2 - a^2}$.

### Quick Reference: What to Substitute and What the Root Becomes

| You see | You want to kill | Set x = | Root becomes |
|---------|-----------------|---------|-------------|
| $\sqrt{a^2 - x^2}$ | the minus | $a\sin\theta$ | $a\cos\theta$ |
| $\sqrt{a^2 + x^2}$ | the plus | $a\tan\theta$ | $a\sec\theta$ |
| $\sqrt{x^2 - a^2}$ | the minus (flipped) | $a\sec\theta$ | $a\tan\theta$ |

### Full Details

| Expression | Substitution | Identity Used | Domain |
|------------|-------------|---------------|--------|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ | $1 - \sin^2\theta = \cos^2\theta$ | $-\pi/2 \leq \theta \leq \pi/2$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$ | $1 + \tan^2\theta = \sec^2\theta$ | $-\pi/2 < \theta < \pi/2$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$ | $\sec^2\theta - 1 = \tan^2\theta$ | $0 \leq \theta < \pi/2$ |

### Essential Trig Integrals for Trig Sub

- $\int \sec^2\theta\, d\theta = \tan\theta + C$
- $\int \sec\theta\tan\theta\, d\theta = \sec\theta + C$
- $\int \sec\theta\, d\theta = \ln|\sec\theta + \tan\theta| + C$

**The idea:** replace the square root with a trig identity that simplifies it completely. Draw a right triangle to convert back to x at the end.

**ML connection:** The $\sqrt{a^2 - x^2}$ form appears in the Gaussian integral $e^{-x^2}$, which is the core of the normal distribution. The $\sqrt{a^2 + x^2}$ form shows up in normalizing constants for the Student-t distribution and in kernel methods with radial basis functions.

---

## 32. Partial Fraction Decomposition

**For integrating rational functions** $\frac{P(x)}{Q(x)}$ where $\deg P < \deg Q$.

**Step 1:** Factor the denominator completely.

**Step 2:** Write the decomposition:

| Denominator factor | Partial fraction form |
|---|---|
| $(x - a)$ | $\frac{A}{x - a}$ |
| $(x - a)^n$ | $\frac{A_1}{x-a} + \frac{A_2}{(x-a)^2} + \cdots + \frac{A_n}{(x-a)^n}$ |
| $(x^2 + bx + c)$ irreducible | $\frac{Ax + B}{x^2 + bx + c}$ |
| $(x^2 + bx + c)^n$ irreducible | $\frac{A_1 x + B_1}{x^2+bx+c} + \cdots + \frac{A_n x + B_n}{(x^2+bx+c)^n}$ |

**Step 3:** Solve for constants (multiply both sides by denominator, plug in strategic $x$ values or match coefficients).

**Step 4:** Integrate each term separately — linear denominators give $\ln$, irreducible quadratics give $\arctan$.

**Example:**

$$\int \frac{1}{x^2 - 1} \, dx = \int \frac{1}{(x-1)(x+1)} \, dx = \int \left(\frac{1/2}{x-1} - \frac{1/2}{x+1}\right) dx = \frac{1}{2}\ln\left|\frac{x-1}{x+1}\right| + C$$

**If $\deg P \geq \deg Q$:** do polynomial long division first, then decompose the remainder.

---

## 33. Improper Integrals — Integrating to Infinity

**Type 1: Infinite bounds**

$$\int_a^\infty f(x) \, dx = \lim_{N \to \infty} \int_a^N f(x) \, dx$$

If the limit exists, the integral **converges**. If not, it **diverges**.

**Type 2: Integrand blows up** (e.g., $\int_0^1 \frac{1}{\sqrt{x}} dx$)

$$\int_0^b f(x) \, dx = \lim_{\varepsilon \to 0^+} \int_\varepsilon^b f(x) \, dx$$

**Key examples:**

$$\int_1^\infty \frac{1}{x^p} \, dx \quad \begin{cases} \text{converges} & \text{if } p > 1 \\ \text{diverges} & \text{if } p \leq 1 \end{cases}$$

**The Gaussian integral (most important improper integral in all of ML):**

$$\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}$$

Cannot be computed with single-variable techniques — requires squaring the integral and converting to polar coordinates.

**ML connection:** Probability densities over unbounded domains are improper integrals: $\int_{-\infty}^{\infty} p(x) \, dx = 1$. The Gaussian/normal distribution is built entirely on the Gaussian integral.

---

## 34. Critical Points and Optimization

**Critical point:** where $f'(x) = 0$ or $f'(x)$ is undefined.

**Second derivative test** at a critical point where $f'(x) = 0$:
- $f''(x) > 0$ → **local minimum** (concave up, bowl)
- $f''(x) < 0$ → **local maximum** (concave down, hill)
- $f''(x) = 0$ → **inconclusive** (could be inflection point)

**Concavity:**
- $f''(x) > 0$ on an interval → concave up (tangent line lies below curve)
- $f''(x) < 0$ on an interval → concave down (tangent line lies above curve)
- **Inflection point:** where concavity changes ($f'' = 0$ or undefined, AND sign changes)

**Applied optimization procedure:**
1. Draw a picture, define variables
2. Write the quantity to optimize as a function of one variable
3. Find critical points: set $f'(x) = 0$, solve
4. Classify via second derivative test (or check endpoints on closed interval)
5. Answer the actual question

**ML connection:** Training a neural network is setting $\partial L / \partial w = 0$ for all weights. Gradient descent iteratively approximates this. The Hessian (matrix of all second partial derivatives) generalizes the second derivative test to many dimensions.

---

## 35. Series and Convergence

### Taylor Series

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x - a)^n$$

At $a = 0$ (Maclaurin series):

| Function | Series | Radius of convergence |
|----------|--------|-----------------------|
| $e^x$ | $1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$ | $\infty$ |
| $\sin(x)$ | $x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$ | $\infty$ |
| $\cos(x)$ | $1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$ | $\infty$ |
| $\frac{1}{1-x}$ | $1 + x + x^2 + x^3 + \cdots$ | $|x| < 1$ |
| $\ln(1+x)$ | $x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots$ | $-1 < x \leq 1$ |
| $(1+x)^k$ | $1 + kx + \frac{k(k-1)}{2!}x^2 + \cdots$ | $|x| < 1$ |

### Geometric Series

$$\sum_{n=0}^{\infty} r^n = \frac{1}{1-r} \quad \text{for } |r| < 1$$

### Convergence Tests (quick reference)

| Test | Use when | Converges if | Diverges if |
|------|----------|-------------|-------------|
| **Geometric** | Series has the form $\sum ar^n$ | $\|r\| < 1$ (sum $= a/(1-r)$) | $\|r\| \geq 1$ |
| **p-series** | Series has the form $\sum 1/n^p$ | $p > 1$ | $p \leq 1$ |
| **Ratio** | Factorials ($n!$), exponentials ($k^n$), or products | $L < 1$ where $L = \lim_{n\to\infty} \|a_{n+1}/a_n\|$ | $L > 1$ (inconclusive if $L = 1$) |
| **Root** | Terms raised to the $n$th power ($c_n^{\,n}$) | $L < 1$ where $L = \lim_{n\to\infty} \|a_n\|^{1/n}$ | $L > 1$ (inconclusive if $L = 1$) |
| **Comparison** | Can bound against a known series | $0 \leq a_n \leq b_n$ and $\sum b_n$ converges | $0 \leq b_n \leq a_n$ and $\sum b_n$ diverges |
| **Limit Comparison** | Ratio to a known series approaches a constant | $\lim a_n/b_n = c > 0$ and $\sum b_n$ converges | $\lim a_n/b_n = c > 0$ and $\sum b_n$ diverges |
| **Integral** | $f(n) = a_n$, continuous, positive, decreasing for $n \geq N$ | $\int_N^\infty f(x)\,dx$ converges | $\int_N^\infty f(x)\,dx$ diverges |
| **Alternating Series** | $\sum (-1)^n b_n$ with $b_n > 0$ | $b_n$ is eventually decreasing AND $b_n \to 0$ | (test only proves convergence) |
| **Divergence (nth-term)** | Always check this first | (test cannot prove convergence) | $\lim_{n\to\infty} a_n \neq 0$ |

#### Geometric Series — details

$$\sum_{n=0}^{\infty} ar^n = \frac{a}{1-r}, \quad |r| < 1$$

**How to recognise it:** Each term is a fixed multiple of the previous one. Look for expressions like $3 \cdot (1/2)^n$, $(0.9)^n$, $5 \cdot (-1/3)^n$.

**How to apply:**
1. Identify $a$ (the first term) and $r$ (the common ratio).
2. If $|r| < 1$, the series converges to $a/(1-r)$.
3. If $|r| \geq 1$, the series diverges.

**Watch out for index shifts.** If the sum starts at $n = 1$ instead of $n = 0$:

$$\sum_{n=1}^{\infty} ar^n = \frac{ar}{1-r}$$

**Partial sum formula** (useful for finite sums):

$$\sum_{n=0}^{N} ar^n = a\,\frac{1 - r^{N+1}}{1 - r}$$

**Example:** $\sum_{n=0}^{\infty} \frac{3}{4^n} = \frac{3}{1 - 1/4} = 4$.

#### Ratio Test — details

Given $\sum a_n$ (with $a_n \neq 0$ eventually), compute:

$$L = \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right|$$

| Result | Conclusion |
|--------|-----------|
| $L < 1$ | **Absolutely convergent** |
| $L > 1$ (or $L = \infty$) | **Divergent** |
| $L = 1$ | **Inconclusive** — must use another test |

**How to recognise when to use it:** Your series has factorials ($n!$), exponentials ($k^n$), or products/ratios that simplify nicely when you form $a_{n+1}/a_n$.

**How to apply:**
1. Write out $a_{n+1}$ by replacing every $n$ with $n+1$.
2. Form the ratio $|a_{n+1}/a_n|$ and simplify — most factors cancel.
3. Take $\lim_{n \to \infty}$ of whatever remains.

**Example:** $\sum \frac{n!}{3^n}$

$$\frac{a_{n+1}}{a_n} = \frac{(n+1)!}{3^{n+1}} \cdot \frac{3^n}{n!} = \frac{n+1}{3} \to \infty$$

$L = \infty > 1$ → **diverges**.

**Example:** $\sum \frac{2^n}{n!}$

$$\frac{a_{n+1}}{a_n} = \frac{2^{n+1}}{(n+1)!} \cdot \frac{n!}{2^n} = \frac{2}{n+1} \to 0$$

$L = 0 < 1$ → **converges** (this is actually $e^2 - 1$ from the exponential series).

**When it fails ($L = 1$):** This happens for p-series ($\sum 1/n^p$), harmonic-like series, and many polynomial-ratio series. Fall back to comparison, integral, or limit comparison tests.

#### Decision flowchart — which test to try

1. **First:** Does $a_n \to 0$? If not → **diverges** (nth-term test).
2. **Geometric form?** ($ar^n$) → Use **geometric series** test.
3. **p-series form?** ($1/n^p$) → Use **p-series** test.
4. **Factorials or exponentials?** → Try the **ratio test**.
5. **$n$th powers?** ($c_n^{\,n}$) → Try the **root test**.
6. **Alternating signs?** → Try the **alternating series test**.
7. **Looks like a known series?** → Try **(limit) comparison**.
8. **Can write $a_n = f(n)$ with $f$ easy to integrate?** → Try the **integral test**.

**ML connection:** Taylor series is THE key tool in theoretical ML. When a paper says "to second order" or "locally quadratic," they're using the Taylor expansion truncated at the $x^2$ term: $f(x + h) \approx f(x) + f'(x)h + \frac{1}{2}f''(x)h^2$.

### Common Exact Sums — The "Vocabulary" of Series

Most exact series evaluations work by decomposing (often via partial fractions) into pieces that reduce to one of these known results.

| Sum | Value | Name / Origin |
|-----|-------|---------------|
| $\sum_{n=0}^{\infty} x^n$ | $\frac{1}{1-x}$, $\|x\| < 1$ | Geometric series |
| $\sum_{n=0}^{\infty} \frac{x^n}{n!}$ | $e^x$ | Exponential series |
| $\sum_{n=1}^{\infty} \frac{1}{n^2}$ | $\frac{\pi^2}{6}$ | Basel problem (Euler, 1734) |
| $\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}$ | $\ln 2$ | Alternating harmonic series |
| $\sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1}$ | $\frac{\pi}{4}$ | Leibniz formula (Gregory–Leibniz) |
| $\sum_{n=1}^{\infty} \frac{1}{n^4}$ | $\frac{\pi^4}{90}$ | Euler (generalizes Basel) |
| $\sum_{n=1}^{\infty} \frac{1}{n(n+1)}$ | $1$ | Telescoping series |

**Key asymptotic facts:**

$$H_N = \sum_{n=1}^{N}\frac{1}{n} \approx \ln N + \gamma \quad (\gamma \approx 0.5772 \text{, Euler–Mascheroni constant})$$

$$H_{2N} - H_N \to \ln 2 \quad \text{as } N \to \infty$$

**Strategy:** When you encounter a complicated rational series, use partial fractions to decompose it into pieces that match this table. The individual pieces may diverge (e.g. harmonic-like sums), but their cancellation often produces exact answers involving $\pi$, $\ln 2$, and other constants.

**ML connection:** Recognizing known forms is exactly how applied ML math works — you don't re-derive the gradient of cross-entropy loss from scratch each time, you learn to decompose unfamiliar expressions into familiar building blocks.

---

## 36. Newton's Method

**Root-finding:** Given f(x) = 0, iterate:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

**For optimization** (finding where g'(x) = 0):

$$x_{n+1} = x_n - \frac{g'(x_n)}{g''(x_n)}$$

**Convergence:** Quadratic — error roughly squares each step (doubles correct digits). Compare with gradient descent's linear convergence.

**First-order vs second-order:**
- Gradient descent: $x_{n+1} = x_n - \alpha \cdot g'(x_n)$ — you choose step size α
- Newton's method: $x_{n+1} = x_n - g'(x_n)/g''(x_n)$ — curvature sets step size automatically

**Multivariable version:** $w_{n+1} = w_n - H^{-1}\nabla L$ where H is the Hessian. Too expensive for large networks → approximations: Adam, L-BFGS, natural gradient.

**Failure modes:** diverges if f'(xₙ) ≈ 0, starting point too far from root, or near inflection points.

---

## 37. Inverse Function Derivatives

$$\frac{d}{dy}[f^{-1}(y)] = \frac{1}{f'(f^{-1}(y))} \qquad \text{equivalently,} \quad \frac{dx}{dy} = \frac{1}{dy/dx}$$

**Derivation method:** Write y = f⁻¹(x), so x = f(y). Differentiate implicitly: 1 = f'(y)·dy/dx → dy/dx = 1/f'(y). Convert back to x.

**Key results derived this way:**

| Function | Inverse | Derivative of inverse |
|----------|---------|----------------------|
| $\sin(y)$ | $\arcsin(x)$ | $1/\sqrt{1-x^2}$ |
| $\cos(y)$ | $\arccos(x)$ | $-1/\sqrt{1-x^2}$ |
| $\tan(y)$ | $\arctan(x)$ | $1/(1+x^2)$ |
| $e^y$ | $\ln(x)$ | $1/x$ |

**1D change of variables for probability:** If Y = g(X) with g invertible:

$$p_Y(y) = p_X(g^{-1}(y)) \cdot \left|\frac{d}{dy}g^{-1}(y)\right|$$

The absolute derivative is the 1D Jacobian — generalizes to the Jacobian determinant in multiple dimensions.

---

## 38. Polar Coordinates

**Conversion:**

$$x = r\cos\theta, \quad y = r\sin\theta \qquad r = \sqrt{x^2+y^2}, \quad \theta = \arctan(y/x)$$

**Key identity:** $x^2 + y^2 = r^2$

**Area in polar:** $A = \frac{1}{2}\int_\alpha^\beta [f(\theta)]^2\,d\theta$

**Double integral conversion:** $dx\,dy = r\,dr\,d\theta$ — the factor of $r$ is the Jacobian:

$$J = \det\begin{bmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{bmatrix} = r$$

**The Gaussian integral proof:**

$$I^2 = \iint e^{-(x^2+y^2)}\,dx\,dy = \int_0^{2\pi}\int_0^\infty e^{-r^2}\cdot r\,dr\,d\theta = 2\pi \cdot \frac{1}{2} = \pi$$

$$\boxed{\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}}$$

---


## 39. Taylor's Theorem — Remainder Forms

### Taylor's Theorem (Exact)

$$f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k + R_n(x)$$

This is an **exact equation**, not an approximation. $R_n(x)$ captures everything the polynomial misses.

### Deriving the Coefficients

Assume $f(x) = c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots$ and match derivatives at $a$:

- $f(a) = c_0$, so $c_0 = f(a)$
- $f'(a) = c_1$, so $c_1 = f'(a)$
- $f''(a) = 2c_2$, so $c_2 = f''(a)/2!$
- $f^{(n)}(a) = n! \cdot c_n$, so $c_n = f^{(n)}(a)/n!$

The $n!$ in the denominator cancels the $n!$ that appears when you differentiate $(x-a)^n$ exactly $n$ times.

### Integral Remainder (Exact — No Approximation)

$$R_n(x) = \int_a^x \frac{(x-t)^n}{n!} f^{(n+1)}(t) \, dt$$

Derived by repeatedly applying integration by parts to the Fundamental Theorem $f(x) = f(a) + \int_a^x f'(t)\,dt$. Each round peels off one Taylor term and leaves a smaller integral.

### Lagrange Remainder (Compressed via MVT)

$$R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$

for some $c$ between $a$ and $x$. Obtained by applying the Mean Value Theorem for Integrals to the integral remainder. The unknown $c$ absorbs the entire infinite tail of higher-order terms.

**Three factors of the remainder:**

| Factor | Meaning |
|--------|---------|
| $(x-a)^{n+1}$ | How far you are from the expansion point |
| $\frac{1}{(n+1)!}$ | How many terms the polynomial already captured |
| $f^{(n+1)}(c)$ | How "wild" the function is beyond what was captured |

### Error Bound (Practical Form)

$$|R_n(x)| \leq \frac{M}{(n+1)!}|x-a|^{n+1} \quad \text{where } M = \max_{t \in [a,x]} |f^{(n+1)}(t)|$$

Replace unknown $c$ with worst-case maximum.

### Proving a Taylor Series Converges to $f$

1. Write $f(x) = T_n(x) + R_n(x)$ (always exact)
2. Show $|R_n(x)| \to 0$ as $n \to \infty$
3. Then $f(x) = \lim_{n \to \infty} T_n(x) = \sum_{k=0}^{\infty} \frac{f^{(k)}(a)}{k!}(x-a)^k$

**Key fact:** Matching all derivatives at $a$ is necessary but not sufficient. The pathological function $f(x) = e^{-1/x^2}$ has all derivatives equal to zero at $x = 0$, so its Taylor series is identically 0 — but the function is not zero. The remainder must actually vanish.

### Compact Series Formulas — Derivation Checklist

To go from "compute derivatives" to $\sum$ notation:

1. Compute $f^{(n)}(a)$ for several $n$, plug into $\frac{f^{(n)}(a)}{n!}(x-a)^n$
2. Which powers survive? (odd → use $2n+1$; even → use $2n$; all → use $n$)
3. Do signs alternate? (yes → include $(-1)^n$ or $(-1)^{n+1}$)
4. Simplify the coefficient (factorials in $f^{(n)}(a)$ may cancel the $n!$)

| Pattern | Encoding |
|---------|----------|
| Alternating signs $+, -, +, -$ | $(-1)^n$ |
| Signs start negative $-, +, -, +$ | $(-1)^{n+1}$ |
| Only odd powers $x, x^3, x^5$ | $x^{2n+1}$ |
| Only even powers $1, x^2, x^4$ | $x^{2n}$ |

---

# Ordinary Differential Equations

---

## 40. First-Order ODEs — Solution Methods

### Separable Equations

**Form:** $g(y)\,dy = f(x)\,dx$

**Method:** Isolate all $y$-terms (including $dy$) on one side, all $x$-terms (including $dx$) on the other, then integrate both sides:

$$\int g(y)\,dy = \int f(x)\,dx + C$$

**When to use:** Whenever you can algebraically separate variables to opposite sides.

### First-Order Linear Equations (Integrating Factor)

**Standard form:** $y' + P(x)\,y = Q(x)$

**Integrating factor:** $\mu(x) = e^{\int P(x)\,dx}$

**Solution:**

$$y = \frac{1}{\mu(x)}\left[\int \mu(x)\,Q(x)\,dx + C\right]$$

**Why it works:** The condition for $\mu$ to turn the left side into $\frac{d}{dx}[\mu y]$ is $\mu' = \mu P(x)$, which is itself a separable ODE. So the method bootstraps: solve an easy separable ODE to find $\mu$, then use $\mu$ to crack the harder linear ODE.

**Key insight:** Multiplying by $\mu$ is conceptually the same as **preconditioning** in optimization — reshaping a hard problem into a well-behaved one.

### Bernoulli Equations

**Form:** $y' + P(x)\,y = Q(x)\,y^n$

The $y^n$ term on the right makes this nonlinear.

**Substitution:** $v = y^{1-n}$

This converts the Bernoulli equation into a first-order linear equation in $v$:

$$v' + (1-n)P(x)\,v = (1-n)Q(x)$$

**Critical detail:** The factor $(1-n)$ multiplies *both* $P(x)$ and $Q(x)$ in the transformed equation. The integrating factor and solution formula use these transformed coefficients:

$$\mu(x) = e^{\int (1-n)P(x)\,dx}$$

$$v = \frac{1}{\mu(x)}\left[\int \mu(x) \cdot (1-n)Q(x)\,dx + C\right]$$

Then substitute back: $y = v^{1/(1-n)}$.

**Common mistake:** Using the original $P(x)$ and $Q(x)$ from the Bernoulli equation directly in the integrating factor formula, forgetting the $(1-n)$ multiplier on both.

**Special cases:** $n = 0$ gives a standard linear equation; $n = 1$ gives a separable equation.

---

## 41. Exact Equations and Integrating Factors for Non-Exact Equations

### Exact Equations

**Form:** $M(x,y)\,dx + N(x,y)\,dy = 0$

**Exactness test:** $\dfrac{\partial M}{\partial y} = \dfrac{\partial N}{\partial x}$

If this holds, there exists a function $F(x,y)$ such that $dF = M\,dx + N\,dy$, and the solution is $F(x,y) = C$.

**Intuition:** The equation says $dF = 0$, meaning the solution curves are level curves (contours) of $F$. This is implicit differentiation in reverse — implicit differentiation goes from $F(x,y) = C$ to the ODE; solving exact equations goes from the ODE back to $F(x,y) = C$.

**Method to find $F$:**

1. Integrate $\frac{\partial F}{\partial x} = M$ with respect to $x$ → get $F = (\text{something}) + g(y)$
2. Differentiate result with respect to $y$, set equal to $N$ → solve for $g'(y)$
3. Integrate $g'(y)$ to get $g(y)$, substitute back into $F$

(You can equivalently start by integrating $N$ with respect to $y$ and using $M$ to find the leftover $h(x)$.)

### Integrating Factors for Non-Exact Equations

When $\frac{\partial M}{\partial y} \neq \frac{\partial N}{\partial x}$, multiply the equation by $\mu$ to make it exact.

**Case 1 — $\mu$ depends only on $x$:** If

$$\frac{\dfrac{\partial M}{\partial y} - \dfrac{\partial N}{\partial x}}{N} = h(x) \quad \text{(function of } x \text{ only)}$$

then $\mu(x) = e^{\int h(x)\,dx}$.

**Case 2 — $\mu$ depends only on $y$:** If

$$\frac{\dfrac{\partial N}{\partial x} - \dfrac{\partial M}{\partial y}}{M} = k(y) \quad \text{(function of } y \text{ only)}$$

then $\mu(y) = e^{\int k(y)\,dy}$.

**Derivation:** Requiring $\frac{\partial(\mu M)}{\partial y} = \frac{\partial(\mu N)}{\partial x}$ and assuming $\mu$ depends on one variable only yields a separable ODE for $\mu$. Same bootstrap pattern as the linear integrating factor.

After finding $\mu$, multiply through and solve the now-exact equation using the standard method above.

---

## 42. Constant-Coefficient Homogeneous Linear ODEs

**Form:** $ay'' + by' + cy = 0$ (extends to any order)

**Method:** Guess $y = e^{rx}$. Since $y' = re^{rx}$ and $y'' = r^2 e^{rx}$, substituting and dividing by $e^{rx} \neq 0$ gives the **characteristic equation:**

$$ar^2 + br + c = 0$$

The discriminant $\Delta = b^2 - 4ac$ determines three cases:

### Case 1: Distinct Real Roots ($\Delta > 0$)

Two real roots $r_1 \neq r_2$:

$$y = c_1 e^{r_1 x} + c_2 e^{r_2 x}$$

**Behavior:** Two exponential modes evolving at different rates. No oscillation.

### Case 2: Repeated Root ($\Delta = 0$)

One root $r = -b/(2a)$:

$$y = c_1 e^{rx} + c_2\, x\, e^{rx} = (c_1 + c_2 x)e^{rx}$$

**Why $xe^{rx}$:** The quadratic has only one root, so the exponential guess is exhausted. The second solution arises as $\lim_{r_2 \to r_1} \frac{e^{r_2 x} - e^{r_1 x}}{r_2 - r_1} = \frac{\partial}{\partial r}e^{rx} = xe^{rx}$.

### Case 3: Complex Conjugate Roots ($\Delta < 0$)

Roots $r = \alpha \pm \beta i$ where $\alpha = -b/(2a)$ and $\beta = \sqrt{4ac - b^2}/(2a)$:

$$y = e^{\alpha x}(c_1 \cos\beta x + c_2 \sin\beta x)$$

**Why sines and cosines:** Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ converts the complex exponentials into real-valued oscillating solutions. $\alpha$ controls exponential growth/decay; $\beta$ controls oscillation frequency.

### Higher-Order Extension

For an $n$th-order constant-coefficient ODE, the characteristic equation is an $n$th-degree polynomial with $n$ roots (counting multiplicity). The same three cases apply to each root:

- Each distinct real root $r$ contributes $e^{rx}$
- A root $r$ with multiplicity $m$ contributes $e^{rx}, xe^{rx}, x^2 e^{rx}, \ldots, x^{m-1}e^{rx}$
- Each complex pair $\alpha \pm \beta i$ contributes $e^{\alpha x}\cos\beta x$ and $e^{\alpha x}\sin\beta x$

The general solution always has exactly $n$ arbitrary constants.

### Physical Interpretation (Damped Oscillator)

The equation $m\ddot{x} + b\dot{x} + kx = 0$ (mass-spring-damper) has characteristic equation $mr^2 + br + k = 0$. The three cases correspond to:

| Case | Condition | Behavior |
|------|-----------|----------|
| Distinct real ($\Delta > 0$) | $b^2 > 4mk$ | **Overdamped** — slow exponential decay, no oscillation |
| Repeated real ($\Delta = 0$) | $b^2 = 4mk$ | **Critically damped** — fastest non-oscillatory decay |
| Complex ($\Delta < 0$) | $b^2 < 4mk$ | **Underdamped** — oscillates while decaying |

---

## 43. The Wronskian

**Definition:** For two solutions $y_1, y_2$:

$$W(y_1, y_2) = \begin{vmatrix} y_1 & y_2 \\ y_1' & y_2' \end{vmatrix} = y_1 y_2' - y_1' y_2$$

If $W \neq 0$, the solutions are linearly independent and form a fundamental solution set.

**What it tests:** Whether the "state vectors" $(y, y')^T$ for each solution are linearly independent — same determinant test as Phase 1, applied to functions.

**Abel's Theorem:** If $y_1, y_2$ solve $y'' + p(x)y' + q(x)y = 0$, then the Wronskian satisfies its own ODE: $W' = -p(x)W$, giving:

$$W(x) = W(x_0)\, e^{-\int_{x_0}^{x} p(t)\,dt}$$

Since the exponential is never zero, $W$ is either always zero or never zero. Check at one convenient point — if nonzero there, independent everywhere.

**Key detail:** Abel's theorem uses $p(x)$ (the $y'$ coefficient), NOT $q(x)$ (the $y$ coefficient). The ODE must be in standard form (leading coefficient 1).

**Higher order:** For $n$ solutions, the Wronskian is an $n \times n$ determinant using derivatives up to order $n-1$.

---

## 44. Resonance and Forced Vibrations

**Forced spring-mass-damper:** $m\ddot{x} + b\dot{x} + kx = F_0 \cos(\omega t)$

The full solution is $x = x_h + x_p$. The homogeneous part $x_h$ (transient) decays away if $b > 0$. The particular solution $x_p$ (steady state) persists at the driving frequency $\omega$.

**Steady-state amplitude:**

$$A(\omega) = \frac{F_0}{\sqrt{(k - m\omega^2)^2 + (b\omega)^2}}$$

**Resonance** occurs when the driving frequency matches the natural frequency $\omega_0 = \sqrt{k/m}$. The $(k - m\omega^2)$ term vanishes, leaving only $b\omega$ in the denominator. Small damping → enormous amplitude. Zero damping → amplitude goes to infinity.

**Beats:** When $\omega \approx \omega_0$ but not equal, the amplitude modulates slowly — a fast oscillation inside a slow envelope.

**ML connection:** The Hessian eigenvalues set "natural frequencies" of the loss landscape. The learning rate ceiling $\eta < 2/\lambda_{\max}$ is a resonance condition — violating it drives the largest eigenvalue direction into resonance and training diverges.

---

## 45. Nonhomogeneous Equations — Undetermined Coefficients

**Setup:** $ay'' + by' + cy = g(x)$. Solution: $y = y_h + y_p$.

**Guessing rules for $y_p$:**

| $g(x)$ | Guess |
|---------|-------|
| Polynomial degree $n$ | $A_n x^n + \cdots + A_0$ |
| $e^{\alpha x}$ | $Ae^{\alpha x}$ |
| $\sin\beta x$ or $\cos\beta x$ | $A\cos\beta x + B\sin\beta x$ (always include BOTH) |
| $e^{\alpha x}\sin\beta x$ or $e^{\alpha x}\cos\beta x$ | $e^{\alpha x}(A\cos\beta x + B\sin\beta x)$ |
| Products/sums of the above | Product/sum of corresponding guesses |

**Overlap rule:** If your guess is already a homogeneous solution, multiply by $x$. If that's also a homogeneous solution (repeated roots), multiply by $x$ again. Keep going until the guess escapes the homogeneous solution space.

**Limitations:** Only works for constant-coefficient ODEs where $g(x)$ is a polynomial, exponential, sine, cosine, or products thereof. Functions like $\tan x$, $\ln x$, $\sec x$, $1/x$ require variation of parameters instead.

---

## 46. Nonhomogeneous Equations — Variation of Parameters

**Idea:** Let the constants in $y_h = c_1 y_1 + c_2 y_2$ become functions: $y_p = u_1(x) y_1 + u_2(x) y_2$.

**The system** (ODE must be in standard form, leading coefficient 1):

$$\begin{pmatrix} y_1 & y_2 \\ y_1' & y_2' \end{pmatrix} \begin{pmatrix} u_1' \\ u_2' \end{pmatrix} = \begin{pmatrix} 0 \\ g(x) \end{pmatrix}$$

The matrix is the Wronskian matrix — its determinant $W \neq 0$ guarantees a unique solution.

**Cramer's rule solution:**

$$u_1' = \frac{-y_2\, g(x)}{W}, \qquad u_2' = \frac{y_1\, g(x)}{W}$$

Then integrate $u_1'$ and $u_2'$, and assemble $y_p = u_1 y_1 + u_2 y_2$.

**Why it works:** Substituting $y_p$ into the ODE, the terms involving $u_1$ and $u_2$ (without primes) reconstruct the homogeneous equation for $y_1$ and $y_2$, which equals zero. Only the $u_1'$ and $u_2'$ terms survive.

**Common mistake:** Forgetting to put the ODE in standard form first. If the leading coefficient is $a \neq 1$, divide through so $g(x)$ in the formula is $g(x)/a$.

**Advantage over undetermined coefficients:** Works for ANY $g(x)$, not just the "nice" families.

---

## 47. Power Series Solutions

**When to use:** Variable-coefficient ODEs where the characteristic equation method doesn't apply (e.g. $y'' - xy = 0$).

**Method:** Assume $y = \sum_{n=0}^{\infty} a_n x^n$. Compute $y'$ and $y''$ term by term, substitute into the ODE, re-index all sums to the same power of $x$, then match coefficients to get a recurrence relation for the $a_n$.

**Key steps:**

1. $y' = \sum_{n=1}^{\infty} n\, a_n x^{n-1}$, $y'' = \sum_{n=2}^{\infty} n(n-1)\, a_n x^{n-2}$
2. Substitute into the ODE
3. Re-index so all sums have the same power of $x$ (change of dummy variable)
4. If sums start at different indices, separate the "orphan" terms
5. Set each coefficient of $x^m$ to zero → recurrence relation
6. Unroll with $a_0$ and $a_1$ as free constants (for 2nd-order ODEs)

**Orphan terms:** When the ODE has variable coefficients like $xy$ or $x^2 y'$, these shift the power of $x$, causing sums to start at different indices after re-indexing. Terms with no partner are forced to zero by the equation itself, independent of initial conditions.

**Ordinary vs singular points:** A point $x_0$ is ordinary if the coefficient functions (after dividing by the leading coefficient) are analytic there. Power series solutions are valid at ordinary points. At singular points, the Frobenius method ($y = x^r \sum a_n x^n$) is needed instead.

**Canonical example — Airy's equation:** $y'' - xy = 0$ has no closed-form solution. Power series gives recurrence $a_{m+2} = a_{m-1}/((m+2)(m+1))$ with $a_2 = 0$ forced, producing two independent series (the Airy functions Ai and Bi) from chains starting at $a_0$ and $a_1$.

---

## 48. The Laplace Transform

**Definition:**

$$\mathcal{L}\\{f(t)\\} = F(s) = \int_0^{\infty} e^{-st} f(t)\, dt$$

**Core transform table:**

| $f(t)$ | $F(s)$ | Convergence |
|---|---|---|
| $1$ | $1/s$ | $s > 0$ |
| $t^n$ | $n!/s^{n+1}$ | $s > 0$ |
| $e^{at}$ | $1/(s-a)$ | $s > a$ |
| $\sin(\omega t)$ | $\omega/(s^2+\omega^2)$ | $s > 0$ |
| $\cos(\omega t)$ | $s/(s^2+\omega^2)$ | $s > 0$ |
| $u_c(t)$ (unit step) | $e^{-cs}/s$ | $s > 0$ |
| $\delta(t)$ (Dirac delta) | $1$ | all $s$ |

**Derivative property (converts ODEs to algebra):**

$$\mathcal{L}\\{f'(t)\\} = sF(s) - f(0)$$

$$\mathcal{L}\\{f''(t)\\} = s^2 F(s) - sf(0) - f'(0)$$

Pattern: each derivative adds a power of $s$; each initial condition appears with the correct power of $s$ attached.

**First shifting theorem (s-shift) — exponential modulation:**

$$\mathcal{L}\\{e^{at}f(t)\\} = F(s - a)$$

Multiplying by $e^{at}$ in time shifts the transform by $a$ in the $s$-domain. Shifts all poles horizontally by $a$.

**Extended table via first shifting theorem:**

| $f(t)$ | $F(s)$ |
|---|---|
| $e^{at}\sin(\omega t)$ | $\omega/((s-a)^2+\omega^2)$ |
| $e^{at}\cos(\omega t)$ | $(s-a)/((s-a)^2+\omega^2)$ |
| $t^n e^{at}$ | $n!/(s-a)^{n+1}$ |

**Second shifting theorem (t-shift) — time delay:**

$$\mathcal{L}\\{u_c(t) \cdot f(t-c)\\} = e^{-cs} F(s)$$

Delaying a function by $c$ and switching it on at $t = c$ multiplies its transform by $e^{-cs}$.

**Convolution theorem:**

$$\mathcal{L}\\{(f \* g)(t)\\} = F(s) \cdot G(s)$$

where $(f \* g)(t) = \int_0^t f(\tau)\, g(t - \tau)\, d\tau$.

Convolution in time = multiplication in $s$-domain.

**Solving an ODE — the four-step method:**
1. Apply $\mathcal{L}$ to both sides; derivative property absorbs initial conditions automatically
2. Solve the algebraic equation for $Y(s)$
3. Partial fraction decomposition to break $Y(s)$ into table-recognizable pieces
4. Invert each piece using the transform table: $y(t) = \mathcal{L}^{-1}\\{Y(s)\\}$

**Pole analysis and stability:** The poles of $Y(s)$ (where the denominator = 0) determine solution behavior:
- Poles with negative real part (left half-plane) → decaying modes → **stable**
- Poles with zero real part (imaginary axis) → perpetual oscillation → **marginally stable**
- Poles with positive real part (right half-plane) → growing modes → **unstable**

**Dirac delta function — sifting property:**

$$\int_{-\infty}^{\infty} f(t)\,\delta(t - c)\, dt = f(c)$$

The delta function "samples" $f$ at the spike location. $\delta(t)$ is zero everywhere except $t = 0$, where it's "infinite," with $\int \delta(t)\,dt = 1$.

**Laplace transforms of delta:**

$$\mathcal{L}\\{\delta(t)\\} = 1, \qquad \mathcal{L}\\{\delta(t - c)\\} = e^{-cs}$$

**Transfer function and impulse response:** For a system with input $G(s)$ and output $Y(s)$:

$$H(s) = \frac{Y(s)}{G(s)}, \qquad h(t) = \mathcal{L}^{-1}\\{H(s)\\}$$

$H(s)$ is the transfer function; $h(t)$ is the impulse response (output when input is $\delta(t)$). For any input $g(t)$, the output is the convolution:

$$y(t) = (h \* g)(t) = \int_0^t h(\tau)\, g(t - \tau)\, d\tau$$

Poles of $H(s)$ determine system stability.

**Laplace vs power series decision rule:**
- Constant coefficients + IVP → Laplace (or characteristic equation)
- Variable coefficients (e.g., $xy$, $x^2 y''$) → power series
- Piecewise/impulsive forcing → Laplace

---

## 49. Systems of ODEs and Phase Portraits

**Linear system in matrix form:**

$$\frac{d\mathbf{x}}{dt} = A\mathbf{x}, \quad \mathbf{x}(0) = \mathbf{x}_0$$

**Why it works:** Eigenvectors decouple the system. Substituting $\mathbf{z} = P^{-1}\mathbf{x}$ (where $P$ is the eigenvector matrix) transforms $\frac{d\mathbf{x}}{dt} = A\mathbf{x}$ into $\frac{d\mathbf{z}}{dt} = D\mathbf{z}$, a diagonal system. Each $z_i$ satisfies the separable ODE $\frac{dz_i}{dt} = \lambda_i z_i$, which gives $z_i(t) = z_i(0)\, e^{\lambda_i t}$. Transforming back: $\mathbf{x}(t) = P\mathbf{z}(t)$.

**Solution via eigenvalues/eigenvectors (the shortcut):**

If $A$ has eigenvalues $\lambda_1, \lambda_2$ with eigenvectors $\mathbf{v}_1, \mathbf{v}_2$:

$$\mathbf{x}(t) = c_1 e^{\lambda_1 t}\mathbf{v}_1 + c_2 e^{\lambda_2 t}\mathbf{v}_2$$

Find $c_1, c_2$ from initial conditions: $\mathbf{x}(0) = c_1\,\mathbf{v}_1 + c_2\,\mathbf{v}_2$.

**Matrix exponential:**

$$\mathbf{x}(t) = e^{At}\mathbf{x}_0, \quad \text{where} \quad e^{At} = I + At + \frac{(At)^2}{2!} + \frac{(At)^3}{3!} + \cdots$$

If $A = PDP^{-1}$ (diagonalizable), then $e^{At} = P\, e^{Dt}\, P^{-1}$, where $e^{Dt} = \text{diag}(e^{\lambda_1 t}, e^{\lambda_2 t})$.

**Phase portrait classification (2D):**

| Eigenvalues | Portrait type | Stability |
|---|---|---|
| Both real negative | Stable node | Stable |
| Both real positive | Unstable node | Unstable |
| Real, opposite signs | Saddle point | Unstable |
| $\alpha \pm \beta i$, $\alpha < 0$ | Stable spiral | Stable |
| $\alpha \pm \beta i$, $\alpha > 0$ | Unstable spiral | Unstable |
| $\pm \beta i$ (pure imaginary) | Center (closed orbits) | Marginally stable |

**Key behaviors:**
- Stable node: all trajectories → origin. Fast mode dies first, so trajectories align with the **slow** eigenvector on approach.
- Unstable node: all trajectories flee origin. Slow mode dominates initially, trajectories align with the **fast** eigenvector as they escape.
- Saddle: trajectories approach along the stable eigenvector, then escape along the unstable eigenvector. The stable eigenvector is the **separatrix**.
- Spirals: rotation from the imaginary part $\beta$, growth/decay from the real part $\alpha$.
- Centers: pure oscillation, no growth or decay.

**Trace-determinant classification (shortcut):** For $\tau = \text{tr}(A) = \lambda_1 + \lambda_2$ and $\Delta = \det(A) = \lambda_1 \lambda_2$:
- $\Delta < 0$ → saddle
- $\Delta > 0$, $\tau < 0$ → stable (node if $\tau^2 > 4\Delta$, spiral if $\tau^2 < 4\Delta$)
- $\Delta > 0$, $\tau > 0$ → unstable (node if $\tau^2 > 4\Delta$, spiral if $\tau^2 < 4\Delta$)
- $\tau = 0$, $\Delta > 0$ → center

---

# Multivariable Calculus

*Section not yet started — items will be added during lessons 19–23.*

---

# Vector Calculus

*Section not yet started — items will be added during lessons 24–28.*

---

# Partial Differential Equations

*Section not yet started — items will be added during lessons 29–33.*

---

# Matrix Calculus & Optimization

*Section not yet started — items will be added during lessons 34–36.*

---

# Phase 3 — Probability & Statistics

*Section not yet started — items will be added during lessons 37–52.*

---

# Phase 4 — Machine Learning & Interpretability

*Section not yet started — items will be added during lessons 53–66.*

---

# Phase 5 — Extended Mathematical Foundations

*Section not yet started — items will be added during lessons 67–79.*

---

# Phase 6 — Alignment Theory

*Section not yet started — items will be added during lessons 80–84.*

---

## 📋 Key Identities Quick Reference

| Identity | Meaning |
|----------|---------|
| Av = λv | Eigenvector definition |
| A = PDP⁻¹ | Eigendecomposition |
| A = UΣVᵀ | SVD |
| Aᵀe = 0 | Error ⊥ column space |
| b = ŷ + e | Data = projection + error |
| P² = P | Projection is idempotent |
| det(AB) = det(A)det(B) | Determinants multiply |
| tr(AB) = tr(BA) | Trace is cyclic |
| (AB)ᵀ = BᵀAᵀ | Transpose reverses order |
| QᵀQ = I | Orthogonal matrix definition |
| rank + nullity = n | Rank-nullity theorem |
| r = cos(θ) of centered data | Correlation = cosine similarity |
| r² = SSR/SST | Fraction of variance explained |
| df = f'(x) dx | Differential: rise = slope × run |
| lim f/g = lim f'/g' | L'Hôpital's Rule (for 0/0 or ∞/∞) |
| $f$ cont. on $[a,b]$, $y$ between $f(a),f(b)$ → $\exists c: f(c)=y$ | IVT |
| $f$ cont. on $[a,b]$ → $f$ attains max and min | EVT |
| $f$ cont. $[a,b]$, diff. $(a,b)$ → $\exists c: f'(c) = \frac{f(b)-f(a)}{b-a}$ | MVT |
| sin²θ + cos²θ = 1 | Pythagorean identity |
| $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$ | FTC Part 1 |
| $\int_a^b f(x)\,dx = F(b) - F(a)$ | FTC Part 2 |
| $\int f(g(x))g'(x)\,dx = \int f(u)\,du$ | u-substitution |
| $\int u\,dv = uv - \int v\,du$ | Integration by parts |
| $\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$ | Gaussian integral |
| $R_n(x) = \int_a^x \frac{(x-t)^n}{n!} f^{(n+1)}(t)\,dt$ | Exact integral remainder |
| $R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$ | Lagrange remainder |
| $\|R_n(x)\| \leq \frac{M}{(n+1)!}\|x-a\|^{n+1}$ | Taylor error bound |
| $\sum_{n=0}^{\infty} r^n = \frac{1}{1-r}$ for $\|r\|<1$ | Geometric series |
| $f(x+h) \approx f(x) + f'(x)h + \frac{1}{2}f''(x)h^2$ | Taylor (2nd order) |
| $x_{n+1} = x_n - f(x_n)/f'(x_n)$ | Newton's method (root-finding) |
| $x_{n+1} = x_n - g'(x_n)/g''(x_n)$ | Newton's method (optimization) |
| $(f^{-1})'(y) = 1/f'(f^{-1}(y))$ | Inverse function derivative |
| $p_Y(y) = p_X(g^{-1}(y)) \cdot \|(g^{-1})'(y)\|$ | 1D change of variables |
| $dx\,dy = r\,dr\,d\theta$ | Polar Jacobian |
| $W(y_1,y_2) = y_1 y_2' - y_1' y_2$ | Wronskian (independence test for solutions) |
| $W' = -p(x)W$ | Abel's theorem (Wronskian ODE) |
| $\omega_0 = \sqrt{k/m}$ | Natural frequency of spring-mass system |
| $A(\omega) = F_0/\sqrt{(k-m\omega^2)^2+(b\omega)^2}$ | Steady-state amplitude (resonance curve) |
| $u_1' = -y_2 g/W$, $u_2' = y_1 g/W$ | Variation of parameters formulas |
| $y = \sum a_n x^n$ → recurrence for $a_n$ | Power series solution method |
| $\mathcal{L}\\{f'\\} = sF(s) - f(0)$ | Laplace derivative property |
| $\mathcal{L}\\{e^{at}f(t)\\} = F(s-a)$ | First shifting theorem (s-shift) |
| $\mathcal{L}\\{u_c(t)f(t-c)\\} = e^{-cs}F(s)$ | Second shifting theorem (t-shift) |
| $\mathcal{L}\\{f \* g\\} = F(s) \cdot G(s)$ | Convolution theorem |
| $\int f(t)\,\delta(t-c)\,dt = f(c)$ | Dirac delta sifting property |
| $H(s) = Y(s)/G(s)$, $h(t) = \mathcal{L}^{-1}\\{H\\}$ | Transfer function / impulse response |
| $\frac{d\mathbf{x}}{dt} = A\mathbf{x}$ → $\mathbf{x}(t) = c_1 e^{\lambda_1 t}\mathbf{v}_1 + c_2 e^{\lambda_2 t}\mathbf{v}_2$ | Eigenvalue method for systems |
| $e^{At} = Pe^{Dt}P^{-1}$ | Matrix exponential via diagonalization |
| $\tau = \text{tr}(A)$, $\Delta = \det(A)$ → phase portrait type | Trace-determinant classification |

---

## 21. 3D Geometry, Curves, and Curvature

### Lines and Planes

**Parametric line** through point $\mathbf{P}$ in direction $\mathbf{v}$:

$$\mathbf{r}(t) = \mathbf{P} + t\mathbf{v}$$

**Plane** with normal $\mathbf{n}$ through point $\mathbf{P}$:

$$\mathbf{n} \cdot (\mathbf{r} - \mathbf{P}) = 0 \quad \Longleftrightarrow \quad ax + by + cz = d$$

where $\mathbf{n} = (a, b, c)$ and $d = \mathbf{n} \cdot \mathbf{P}$. The coefficients of $x, y, z$ are the normal vector components.

**Distance from point $\mathbf{Q}$ to plane:**

$$D = \frac{|\mathbf{n} \cdot (\mathbf{Q} - \mathbf{P})|}{|\mathbf{n}|}$$

This is the projection of $(\mathbf{Q} - \mathbf{P})$ onto $\mathbf{n}$ — same formula as vector projection magnitude from Phase 1.

**Project point $\mathbf{Q}$ onto plane:** subtract the normal component:

$$\mathbf{Q}_{\text{proj}} = \mathbf{Q} - \frac{\mathbf{n} \cdot (\mathbf{Q} - \mathbf{P})}{\mathbf{n} \cdot \mathbf{n}}\,\mathbf{n}$$

### Vector-Valued Functions

$$\mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle$$

| Quantity | Formula | What it measures |
|----------|---------|-----------------|
| Velocity | $\mathbf{v} = \mathbf{r}'(t)$ | Direction + speed (tangent to curve) |
| Speed | $\|\mathbf{v}\| = \|\mathbf{r}'(t)\|$ | How fast (scalar) |
| Acceleration | $\mathbf{a} = \mathbf{r}''(t)$ | Rate of change of velocity |
| Arc length | $L = \int_a^b \|\mathbf{r}'(t)\|\, dt$ | Distance traveled along curve |
| Arc length rate | $\frac{ds}{dt} = \|\mathbf{r}'(t)\|$ | Speed = rate distance accumulates |

### TNB Frame

$$\hat{T} = \frac{\mathbf{r}'}{|\mathbf{r}'|} = \frac{d\mathbf{r}}{ds}, \quad \hat{N} = \frac{d\hat{T}/dt}{|d\hat{T}/dt|}, \quad \hat{B} = \hat{T} \times \hat{N}$$

- $\hat{T}$: forward (direction of travel)
- $\hat{N}$: toward center of curvature (direction of turning)
- $\hat{B}$: perpendicular to osculating plane

### Curvature and Torsion

**Curvature** (how sharply the curve bends):

$$\kappa = \left|\frac{d\hat{T}}{ds}\right| = \frac{|\mathbf{r}' \times \mathbf{r}''|}{|\mathbf{r}'|^3}$$

**Torsion** (how much the curve twists out of its osculating plane):

$$\tau = -\frac{d\hat{B}}{ds} \cdot \hat{N} = \frac{(\mathbf{r}' \times \mathbf{r}'') \cdot \mathbf{r}'''}{|\mathbf{r}' \times \mathbf{r}''|^2}$$

**Osculating circle:** radius $R = 1/\kappa$. The best-fitting circle to the curve at that point.

$\kappa = 0$: straight line. $\tau = 0$: planar curve.

### Acceleration Decomposition

$$\mathbf{r}'' = a_T\,\hat{T} + a_N\,\hat{N}$$

$$a_T = \frac{\mathbf{r}' \cdot \mathbf{r}''}{|\mathbf{r}'|} \quad \text{(speeding up/slowing down)}$$

$$a_N = \frac{|\mathbf{r}' \times \mathbf{r}''|}{|\mathbf{r}'|} = \kappa|\mathbf{r}'|^2 \quad \text{(turning, = centripetal } v^2/R\text{)}$$

$a_T$ uses dot product (component along velocity). $a_N$ uses cross product (component perpendicular to velocity).

### Frenet-Serret Formulas

$$\frac{d\hat{T}}{ds} = \kappa\hat{N}, \qquad \frac{d\hat{N}}{ds} = -\kappa\hat{T} + \tau\hat{B}, \qquad \frac{d\hat{B}}{ds} = -\tau\hat{N}$$

### Quick Reference

| Formula | Name |
|---------|------|
| $\mathbf{r}(t) = \mathbf{P} + t\mathbf{v}$ | Parametric line |
| $\mathbf{n} \cdot (\mathbf{r} - \mathbf{P}) = 0$ | Plane equation |
| $D = \|\mathbf{n} \cdot (\mathbf{Q} - \mathbf{P})\| / \|\mathbf{n}\|$ | Point-to-plane distance |
| $L = \int_a^b \|\mathbf{r}'\|\, dt$ | Arc length |
| $\kappa = \|\mathbf{r}' \times \mathbf{r}''\| / \|\mathbf{r}'\|^3$ | Curvature (any parameter) |
| $\tau = (\mathbf{r}' \times \mathbf{r}'') \cdot \mathbf{r}''' / \|\mathbf{r}' \times \mathbf{r}''\|^2$ | Torsion (any parameter) |
| $a_T = \mathbf{r}' \cdot \mathbf{r}'' / \|\mathbf{r}'\|$ | Tangential acceleration |
| $a_N = \|\mathbf{r}' \times \mathbf{r}''\| / \|\mathbf{r}'\| = \kappa v^2$ | Normal acceleration |

---

*Last updated: March 2026 — Phase 1 (Linear Algebra) + statistics preview + Phase 2 (Calculus Fundamentals & ODEs through Lesson 18, 3D Geometry through Lesson 19)*









