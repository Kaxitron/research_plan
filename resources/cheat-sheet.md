# Mathematics Cheat Sheet

[Back to TOC](../README.md)

*A living reference of formulas, identities, and key insights from the curriculum.*

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

where P = matrix of eigenvectors (columns), D = diagonal matrix of eigenvalues.

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

---

*Last updated: February 2026 — Phase 1 (Linear Algebra) + statistics preview + Phase 2 (Calculus) started*

