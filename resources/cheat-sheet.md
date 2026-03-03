# Mathematics Cheat Sheet

[Back to TOC](../README.md)

*A living reference of formulas, identities, and key insights from the curriculum.*

*⚠️ When adding a new section, also add a corresponding link in the Table of Contents below.*

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

### [Key Identities Quick Reference](#key-identities-quick-reference)

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

| Test | Use when | Converges if |
|------|----------|-------------|
| Geometric | $\sum ar^n$ | $|r| < 1$ |
| p-series | $\sum 1/n^p$ | $p > 1$ |
| Ratio | Series with factorials or exponentials | $\lim |a_{n+1}/a_n| < 1$ |
| Comparison | Can bound against known series | Bounded by convergent series |
| Integral | $f(n) = a_n$ decreasing, positive | $\int_1^\infty f(x) \, dx$ converges |
| Alternating | $\sum (-1)^n a_n$ | $a_n \to 0$ and $a_n$ decreasing |

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

## Key Identities Quick Reference

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
| $\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$ | Gaussian integral |
| $R_n(x) = \int_a^x \frac{(x-t)^n}{n!} f^{(n+1)}(t)\,dt$ | Exact integral remainder |
| $R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$ | Lagrange remainder |
| $\|R_n(x)\| \leq \frac{M}{(n+1)!}\|x-a\|^{n+1}$ | Taylor error bound |

---

*Last updated: March 2026 — Phase 1 (Linear Algebra) + statistics preview + Phase 2 (Calculus through Lesson 21)*




