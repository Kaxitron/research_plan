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

$$a \times b = \det \begin{bmatrix} \hat{i} & \hat{j} & \hat{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{bmatrix}$$

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

$$\det \begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc$$

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

---

*Last updated: February 2026 — Phase 1 (Linear Algebra) + early Lesson 9 extensions*
