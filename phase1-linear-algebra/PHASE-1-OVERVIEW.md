# Phase 1 Overview: Linear Algebra — Every Concept and Method

> **Purpose:** Exhaustive reference of every concept, technique, and method covered in Phase 1 (Lessons 02–12). Use this to check coverage, review before the exam, or quickly locate where a topic lives.

---

## Lesson 02: Vectors — What Even Are They?

**Core Representations:**
- Vectors as arrows (geometric view: direction + magnitude)
- Vectors as ordered lists of numbers (computational view)
- Coordinates as basis-dependent instructions — change the basis, change the coordinates, same vector
- Column vectors vs row vectors; notation conventions

**Operations:**
- Vector addition (tip-to-tail geometric rule; component-wise algebraic rule)
- Scalar multiplication (stretching/shrinking/flipping arrows; multiplying each component)
- Negation (−v reverses direction)

**Key Vocabulary:**
- Magnitude (length, norm): ||v|| = √(v₁² + v₂² + ...)
- Unit vectors (magnitude 1), standard basis vectors ê₁, ê₂, ...
- Zero vector (additive identity)
- Dimension of the ambient space ℝⁿ

**ML Connection:**
- Embedding vectors in transformers (~768-dimensional representations of tokens)
- Word2Vec: similar meanings → nearby vectors
- Feature vectors as points in high-dimensional space

---

## Lesson 03: Linear Combinations, Span, and Basis

**Core Definitions:**
- **Linear combination:** c₁v₁ + c₂v₂ + ... + cₙvₙ for scalars cᵢ
- **Span:** the set of ALL linear combinations of a collection of vectors — everything reachable
- **Linear independence:** no vector in the set can be written as a linear combination of the others; equivalently, c₁v₁ + ... + cₙvₙ = 0 only when all cᵢ = 0
- **Linear dependence:** at least one vector is redundant (can be removed without shrinking the span)
- **Basis:** a set of vectors that is both linearly independent AND spans the entire space — minimal spanning set, maximal independent set
- **Dimension:** the number of vectors in any basis for the space

**Key Facts:**
- ℝⁿ always has dimension n; any basis has exactly n vectors
- Standard basis {e₁, ..., eₙ} is one choice — infinitely many others exist
- Adding a dependent vector to a basis doesn't increase span
- Removing an independent vector from a basis reduces span

**Methods:**
- Testing independence: set up c₁v₁ + ... = 0, row reduce, check for free variables
- Finding a basis for span of a set: row reduce, identify pivot columns

**ML Connection:**
- **Superposition hypothesis:** neural networks encode MORE features than they have dimensions by using non-orthogonal, nearly-independent directions
- Residual stream dimension constrains how many features a layer can represent
- Feature dictionaries (SAEs) attempt to find an overcomplete basis

---

## Lesson 04: Linear Transformations — Matrices as Functions

**Core Ideas:**
- **A matrix IS a transformation** — it moves, stretches, rotates, projects, or collapses space
- Columns of the matrix = where the basis vectors land after the transformation
- "Linear" means two things are preserved: (1) lines stay lines, (2) the origin stays fixed
- Equivalently: T(au + bv) = aT(u) + bT(v) — preserves addition and scalar multiplication
- Matrix-vector multiplication Ax = "where does x land?"
- **Affine ≠ linear:** y = Wx + b is affine (shifted); y = Wx is linear. Neural network layers are affine.

**Types of Transformations (geometric zoo):**
- Rotation matrices (preserve lengths and angles)
- Scaling matrices (stretch/compress along axes)
- Shear matrices (tilt one axis relative to another)
- Reflection matrices (flip across an axis)
- Projection matrices (collapse onto a subspace)
- Composition: doing two transformations in sequence = matrix multiplication

**Key Facts:**
- Every linear transformation ℝⁿ → ℝᵐ corresponds to a unique m×n matrix
- Non-square matrices change dimension (ℝⁿ → ℝᵐ where m ≠ n)
- Square matrices: ℝⁿ → ℝⁿ (same space, may distort it)

**ML Connection:**
- Each layer of a neural network: x ↦ σ(Wx + b) — affine transformation + nonlinearity
- Weight matrices literally transform the representation space

---

## Lesson 05: Matrix Operations — Composition and Inversion

**Matrix Multiplication:**
- **As composition:** AB means "apply B first, then A"
- **Row view:** each entry of Ax is a dot product of a row of A with x (pattern matching)
- **Column view:** Ax is a linear combination of columns of A, weighted by entries of x
- **Outer product view:** AB = sum of (column of A)(row of B) outer products
- NOT commutative: AB ≠ BA in general
- Associative: (AB)C = A(BC)
- Distributive: A(B + C) = AB + AC

**Transpose:**
- (Aᵀ)ᵢⱼ = Aⱼᵢ (flip across diagonal)
- (AB)ᵀ = BᵀAᵀ (reverse order!)
- (Aᵀ)ᵀ = A

**Inverse:**
- A⁻¹ exists iff A is square and det(A) ≠ 0 (equivalently: full rank, trivial null space)
- AA⁻¹ = A⁻¹A = I
- (AB)⁻¹ = B⁻¹A⁻¹ (reverse order!)
- Computing: row reduce [A | I] to get [I | A⁻¹]
- 2×2 formula: [[a,b],[c,d]]⁻¹ = (1/det) × [[d,−b],[−c,a]]

**ML Connection:**
- QK and OV circuits in transformers are matrix compositions (W_Q^T W_K, W_O W_V)
- Understanding the effect of composed weight matrices = understanding what a head computes

---

## Lesson 06: Rank, Null Space, and the Fundamental Theorem

**Core Subspaces:**
- **Column space** C(A): all possible outputs Ax — the span of A's columns
- **Null space** N(A): all x where Ax = 0 — inputs that get crushed to zero
- **Row space** C(Aᵀ): span of the rows of A
- **Left null space** N(Aᵀ): all y where Aᵀy = 0

**Rank:**
- rank(A) = dim(column space) = dim(row space) = number of pivots in RREF
- Rank tells you how many independent directions survive the transformation

**Rank-Nullity Theorem:**
- rank(A) + nullity(A) = n (number of columns = input dimensions)
- Conservation law: input dimensions = surviving dimensions + crushed dimensions

**Gaussian Elimination / Row Reduction:**
- Row echelon form (REF): staircase pattern of pivots
- Reduced row echelon form (RREF): pivots = 1, zeros above and below each pivot
- Three elementary row operations: swap, scale, add multiple of one row to another
- Pivot columns = independent columns; free variables = dependent columns
- Solving Ax = b: augment [A|b], row reduce, read off solutions

**Key Facts:**
- Full rank = invertible (for square matrices)
- rank(AB) ≤ min(rank A, rank B)
- Null space dimension depends on column count (input space), not row count

**ML Connection:**
- Attention heads are deliberately low-rank (768 → 64 → 768) to force compression
- LoRA exploits low-rank structure for efficient fine-tuning
- Information bottleneck = rank reduction = lossy compression

---

## Lesson 07: The Determinant — Volume, Orientation, and Invertibility

**Core Ideas:**
- **det(A) = the factor by which A scales area (2D) or volume (3D or nD)**
- |det(A)| = scaling factor; sign = orientation preserved (+) or flipped (−)
- det(A) = 0 ↔ the transformation collapses space (loses a dimension) ↔ A is singular ↔ non-invertible ↔ non-trivial null space ↔ rank < n

**Properties:**
- det(AB) = det(A) · det(B) — volume scaling composes multiplicatively
- det(A⁻¹) = 1/det(A)
- det(Aᵀ) = det(A)
- det(cA) = cⁿ det(A) for n×n matrix
- Swapping rows flips sign; adding row multiples doesn't change det; scaling a row scales det

**Computing Determinants:**
- 2×2: ad − bc
- 3×3: Sarrus' rule or cofactor expansion
- n×n: cofactor expansion along any row or column
- Via row reduction: product of pivots (tracking sign flips)

**ML Connection:**
- Vanishing/exploding gradients relate to determinants of Jacobians being near 0 or very large
- Jacobian determinant in change of variables (normalizing flows, VAEs)
- Determinant as information preservation vs destruction

---

## Lesson 08: Eigenvalues and Eigenvectors — The DNA of a Transformation

**Core Definitions:**
- **Eigenvector v:** Av = λv — a direction that doesn't rotate under A, only scales
- **Eigenvalue λ:** the scaling factor along that eigendirection
- λ > 1: stretching; 0 < λ < 1: shrinking; λ < 0: flipping; λ = 0: collapsing

**Finding Eigenvalues/Eigenvectors:**
- Characteristic equation: det(A − λI) = 0 → polynomial in λ
- For each λ: solve (A − λI)v = 0 → eigenspace = null space of (A − λI)

**Diagonalization:**
- A = PDP⁻¹ where P = [v₁ | v₂ | ... | vₙ] (eigenvectors as columns), D = diag(λ₁, ..., λₙ)
- Means: change to eigenbasis → scale each axis independently → change back
- Works when A has n linearly independent eigenvectors
- Powers: Aⁿ = PDⁿP⁻¹ (just raise eigenvalues to the nth power)

**Special Cases:**
- Symmetric matrices: always diagonalizable, real eigenvalues, orthogonal eigenvectors
- Complex eigenvalues: come in conjugate pairs, correspond to rotation
- Repeated eigenvalues: may or may not have enough eigenvectors (algebraic vs geometric multiplicity)

**Key Facts:**
- tr(A) = sum of eigenvalues
- det(A) = product of eigenvalues
- Eigenvalues of A⁻¹ are 1/λᵢ
- Eigenvalues of Aⁿ are λᵢⁿ

**ML Connection:**
- PCA: find eigenvectors of covariance matrix = directions of maximum variance
- Hessian eigenvalues = curvature of loss landscape in each direction
- Condition number κ = λ_max/λ_min predicts optimizer difficulty

---

## Lesson 09: Singular Value Decomposition — The Ultimate Factorization

**The Decomposition:**
- **A = UΣVᵀ** — every matrix, any shape, any rank
- V (right singular vectors): rotate input to align with natural axes
- Σ (singular values): scale each axis independently (σ₁ ≥ σ₂ ≥ ... ≥ 0)
- U (left singular vectors): rotate output to final orientation
- Any transformation = rotate → scale → rotate

**Key Properties:**
- Works for rectangular matrices (m×n): U is m×m, Σ is m×n, V is n×n
- Rank = number of non-zero singular values
- Singular values σᵢ = √(eigenvalues of AᵀA)
- U columns = eigenvectors of AAᵀ; V columns = eigenvectors of AᵀA

**Low-Rank Approximation:**
- **Eckart–Young theorem:** best rank-k approximation (in Frobenius or spectral norm) is obtained by keeping only the k largest singular values
- Truncated SVD: Aₖ = Σᵢ₌₁ᵏ σᵢ uᵢ vᵢᵀ

**Connection to Eigendecomposition:**
- For symmetric matrices: SVD and eigendecomposition coincide (singular values = |eigenvalues|)
- SVD generalizes eigendecomposition to non-square, non-symmetric matrices

**ML Connection:**
- PCA is SVD of the centered data matrix: principal components = V columns
- LoRA: approximate weight updates as low-rank ΔW = BA (two thin matrices)
- Image compression: keep top-k singular values
- Attention matrices: low-rank by design

---

## Lesson 10: Dot Products, Projections, and Orthogonality

**Dot Product:**
- **Algebraic:** a · b = Σ aᵢbᵢ
- **Geometric:** a · b = ||a|| ||b|| cos θ
- Sign: positive (angle < 90°), zero (perpendicular), negative (angle > 90°)
- **Cosine similarity:** (a · b)/(||a|| ||b||) = cos θ — pure direction comparison

**Orthogonality:**
- a ⊥ b ↔ a · b = 0
- **Orthogonal set:** all pairwise dot products zero
- **Orthonormal set:** orthogonal + all unit length
- **Orthogonal matrix Q:** QᵀQ = I, columns are orthonormal; Q⁻¹ = Qᵀ; preserves lengths and angles (pure rotation/reflection)

**Projections:**
- **Onto a vector:** proj_v(u) = (u · v / v · v) v — the "shadow" of u onto v
- **Onto a subspace:** P = A(AᵀA)⁻¹Aᵀ — projection matrix
- Projection matrices are idempotent: P² = P (projecting twice = projecting once)
- Projection matrices are symmetric: Pᵀ = P
- **Orthogonal complement:** everything perpendicular to the subspace; I − P projects onto it

**Least Squares:**
- When Ax = b has no exact solution, x̂ = (AᵀA)⁻¹Aᵀb minimizes ||Ax − b||²
- Least squares IS projection: Ax̂ is the projection of b onto the column space of A

**Linear Regression as Projection:**
- Setup: A = design matrix (rows = data points, columns = features), y = observed outcomes
- ŷ = Ax̂ = projection of y onto Col(A) — the best prediction living in the column space
- Error vector e = y − ŷ is perpendicular to Col(A): Aᵀ(y − Ax̂) = 0 (the normal equations)
- Geometric picture: y lives in ℝⁿ, Col(A) is a subspace; ŷ is the closest point in that subspace
- R² = ||ŷ||² / ||y||² — fraction of total variance explained by the model (when data is mean-centered)
- Equivalently: R² = 1 − ||y − ŷ||² / ||y||² — one minus the fraction of unexplained variance
- Pythagorean theorem: ||y||² = ||ŷ||² + ||e||² (because ŷ ⊥ e), so both R² formulas are consistent
- R² = 1 means y ∈ Col(A) (perfect fit, zero error); R² = 0 means ŷ = 0 (model explains nothing)
- Adding more columns to A can only increase R² (larger subspace to project onto), motivating regularization

**Gram-Schmidt Process:**
- Input: any basis {v₁, ..., vₖ}
- Output: orthonormal basis {u₁, ..., uₖ} spanning the same subspace
- Method: subtract projections onto previously computed vectors, normalize

**ML Connection:**
- **Attention IS dot products:** Q · K similarity → softmax → weighted sum of V
- Cosine similarity used in retrieval, semantic search, contrastive learning
- Layer normalization projects onto unit sphere
- Orthogonal initialization of weight matrices

---

## Lesson 11: Change of Basis, Norms, and Special Matrices

**Change of Basis:**
- Coordinates are basis-dependent; same vector, different numbers in different bases
- If B = [b₁ | ... | bₙ], then B⁻¹v converts from standard to B-basis coordinates
- **Conjugation:** B⁻¹AB = same linear transformation, expressed in basis B
- Eigendecomposition A = PDP⁻¹ IS change of basis to eigenbasis
- SVD involves TWO changes of basis (one for input, one for output)

**Norms (Measuring Size):**
- **L2 (Euclidean):** ||x||₂ = √(Σxᵢ²) — standard distance
- **L1 (Manhattan):** ||x||₁ = Σ|xᵢ| — encourages sparsity
- **L∞ (max/Chebyshev):** ||x||∞ = max|xᵢ|
- **Lp general:** ||x||ₚ = (Σ|xᵢ|ᵖ)^(1/p)
- **Frobenius norm** (for matrices): ||A||_F = √(Σᵢⱼ Aᵢⱼ²) = √(Σ σᵢ²) — treats matrix as a vector
- **Spectral norm:** ||A||₂ = σ₁ (largest singular value) — maximum stretching factor
- **Norm balls:** L2 = circle, L1 = diamond (corners touch axes → promotes sparsity), L∞ = square

**Special Matrix Types:**
- **Symmetric:** A = Aᵀ; real eigenvalues, orthogonal eigenvectors, always diagonalizable (A = QDQᵀ)
- **Positive definite (PD):** all eigenvalues > 0; xᵀAx > 0 for all x ≠ 0; "bowl shape"
- **Positive semi-definite (PSD):** eigenvalues ≥ 0; xᵀAx ≥ 0; AᵀA is always PSD
- **Orthogonal:** QᵀQ = I; pure rotation/reflection; preserves lengths
- **Diagonal:** only nonzero entries on diagonal; scales each axis independently
- **Triangular (upper/lower):** eigenvalues on diagonal; efficient for solving systems
- **Cholesky decomposition:** A = LLᵀ for PD matrices (the matrix square root)
- **Trace:** tr(A) = Σ aᵢᵢ = Σ λᵢ; tr(AB) = tr(BA) (cyclic property)
- **Inner product of functions:** ⟨f, g⟩ = ∫f(x)g(x)dx — extending dot products to function spaces; orthogonal functions

**Principal Component Analysis (PCA):**
- Goal: find the directions of maximum variance in the data
- Mean-center the data first: X̃ = X − μ (subtract column means)
- Covariance matrix: C = (1/n) X̃ᵀX̃ — symmetric PSD, entry Cᵢⱼ = covariance between features i and j
- Diagonal entries = variances; off-diagonal entries = covariances (linear dependencies between features)
- Correlation = covariance normalized by standard deviations: ρᵢⱼ = Cᵢⱼ / (σᵢ σⱼ), ρ ∈ [−1, 1]
- PCA = eigendecomposition of C: eigenvectors are principal components, eigenvalues are variances along those directions
- PCA IS a change of basis: the eigenvector basis diagonalizes C, guaranteeing uncorrelated components
- First principal component = direction of maximum variance; second = max variance orthogonal to first; etc.
- Dimensionality reduction: keep top k components, explained variance ratio = Σᵢ₌₁ᵏ λᵢ / Σ λⱼ
- Choosing k: scree plot (eigenvalue vs. component number), elbow method, or variance threshold (e.g., keep 95%)
- Connection to SVD: if X̃ = UΣVᵀ, then C = VΣ²Vᵀ/n, so V gives the principal components and σᵢ²/n = λᵢ

**ML Connection:**
- Weight decay = L2 regularization (penalizes ||w||₂²)
- L1 regularization (Lasso) = sparsity (many weights driven to exactly 0)
- Gradient clipping uses norms to bound update sizes
- Layer normalization, spectral normalization
- Covariance matrices are always symmetric PSD
- PCA used for feature preprocessing, visualization (project high-dim data to 2D/3D), and noise reduction

---

## Lesson 12: Linear Algebra Capstone

**The Unified Picture:**
- Any matrix transformation = rotate → scale → rotate (this is SVD)
- Every other concept is a window into part of this story:
  - Vectors = the things being transformed
  - Span/basis = what space you're working in
  - Rank = how many dimensions survive
  - Determinant = total volume scaling
  - Eigenvalues = scaling factors along natural axes (for symmetric/diagonalizable matrices)
  - SVD = the complete decomposition for any matrix
  - Projection = reducing to a subspace
  - Change of basis = same transformation, different coordinates

**Integration Exercise:**
- Take a single matrix; compute rank, determinant, eigenvalues, SVD, condition number
- For each: explain the geometric meaning and what it tells you about the transformation

**Assessment:**
- Phase 1 Final Exam (60 min, 100 pts): geometric intuition, computation, proof, ML applications
