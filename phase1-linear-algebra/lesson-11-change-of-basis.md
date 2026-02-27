# Lesson 11: Change of Basis, Norms, and Special Matrices

[← Dot Products](lesson-10-dot-products.md) | [Back to TOC](../README.md) | [Next: Linear Algebra Capstone →](lesson-12-capstone.md)

---

> **Why this lesson exists:** When interpretability researchers say "let's look at this in the feature basis instead of the neuron basis," they mean a change of basis. When training uses weight decay, gradient clipping, or layer normalization, those involve norms. When analyzing loss landscapes, you need positive definite matrices. This lesson collects the "connective tissue" concepts that glue everything together.

## 🎯 Core Concepts

### Change of Basis

- **The same vector has different coordinates in different bases.** A vector doesn't change — its description does. Just like "5 feet" and "1.524 meters" describe the same height in different units.
- **If B is a matrix whose columns are the new basis vectors**, then B⁻¹v converts v's coordinates from the standard basis to the new basis. B converts back.
- **A transformation in a new basis:** If A is a transformation in the standard basis, then B⁻¹AB is the *same transformation* described in the basis B. The matrix looks different, but it does the same thing to space.
- **Eigendecomposition AS change of basis:** A = PDP⁻¹ means "convert to the eigenbasis (P⁻¹), scale each eigenvector direction (D), convert back (P)." The matrix looks *diagonal* — trivially simple! — in its eigenbasis.
- **SVD AS two changes of basis:** A = UΣVᵀ means "convert input to V-basis, scale by Σ, convert output to U-basis." Every matrix is just scaling in the right coordinate systems.

### Norms — Measuring Size

- **L2 norm (Euclidean):** ||v||₂ = √(v₁² + v₂² + ... + vₙ²) — straight-line distance from origin. The "default" norm.
- **L1 norm (Manhattan):** ||v||₁ = |v₁| + |v₂| + ... + |vₙ| — taxicab distance. Encourages sparsity (many components = 0).
- **L∞ norm (max):** ||v||∞ = max(|v₁|, ..., |vₙ|) — largest component. Used in adversarial robustness.
- **Frobenius norm (for matrices):** ||A||_F = √(sum of all squared entries) — treats the matrix as one long vector.
- **Spectral norm:** ||A||₂ = largest singular value σ₁ — the maximum stretching factor of the transformation.
- **Norm balls:** the set of all vectors with ||v|| ≤ 1. L2 ball = circle. L1 ball = diamond. L∞ ball = square. The *shape* of the norm ball determines what "closeness" means.

### Special Matrices

- **Symmetric matrices** (A = Aᵀ):
  - Eigenvalues are always real (never complex)
  - Eigenvectors are always orthogonal
  - Can always be diagonalized: A = QDQᵀ where Q is orthogonal
  - **Where they appear:** covariance matrices, Hessians, kernel matrices, attention score matrices (before masking)
  
- **Positive definite matrices:** all eigenvalues > 0
  - The quadratic form xᵀAx > 0 for all nonzero x — geometrically, this is a "bowl" shape
  - Hessian being positive definite at a point = local minimum
  - **Where they appear:** loss landscape curvature, covariance matrices, Fisher information matrix

- **Positive semi-definite (PSD):** all eigenvalues ≥ 0
  - xᵀAx ≥ 0 for all x — bowl or flat, never a saddle
  - Covariance matrices are always PSD
  - Gram matrices (AᵀA) are always PSD

- **Trace:** tr(A) = sum of diagonal entries = sum of eigenvalues
  - tr(AB) = tr(BA) — cyclic property
  - ||A||²_F = tr(AᵀA) — Frobenius norm via trace
  - Shows up constantly in ML loss functions and gradient computations

### Cholesky Decomposition

- **For positive definite matrices:** A = LLᵀ, where L is lower triangular. Think of it as "taking the square root" of a matrix.
- **Why it exists:** if A is positive definite (all eigenvalues > 0), it can always be factored this way. The factorization is unique.
- **Why it matters:** Cholesky is ~2x faster than general matrix decomposition. It's the standard way to:
  - Sample from multivariate Gaussians: if you want x ~ N(μ, Σ), compute L where Σ = LLᵀ, then x = μ + Lz where z ~ N(0, I). The matrix L "shapes" standard normal noise into the correct covariance structure.
  - Solve systems involving covariance matrices efficiently (Bayesian inference, Gaussian processes).
  - Test positive definiteness: if Cholesky succeeds, the matrix is positive definite. If it fails, it's not.
- **MML Book, Chapter 4.3** covers this in one page — worth a quick read.

### Inner Product of Functions

- **Functions can be vectors too.** The 3B1B video on abstract vector spaces (Ch. 15) introduces this idea. Formally: the set of all continuous functions on [a, b] forms a vector space. You can add functions, scale them, and take linear combinations — just like regular vectors.
- **The inner product of two functions:** ⟨f, g⟩ = ∫ₐᵇ f(x)g(x) dx — analogous to the dot product for finite vectors. It measures "how similar" two functions are.
- **Orthogonal functions:** ⟨f, g⟩ = 0 means the functions are "perpendicular" — they have nothing in common. sin(x) and cos(x) are orthogonal on [0, 2π]. This is the basis of Fourier analysis.
- **Why this matters for ML:** neural networks live in *function space* — the space of all possible input-output mappings. When researchers say "the loss landscape in function space," they mean this infinite-dimensional vector space where each "point" is a function. Inner products of functions let you measure distances and angles between different neural networks' behaviors.
- **MML Book, Chapter 3.7** covers this briefly but clearly.

### Matrix Phylogeny — The Family Tree

How matrix types relate to each other:

```
All Matrices
├── Square Matrices
│   ├── Symmetric (A = Aᵀ)
│   │   ├── Positive Semi-Definite (eigenvalues ≥ 0)
│   │   │   └── Positive Definite (eigenvalues > 0)
│   │   │       → Cholesky decomposition exists
│   │   └── Indefinite (mixed eigenvalues)
│   │       → Saddle points in loss landscape
│   ├── Orthogonal (QᵀQ = I)
│   │   → Pure rotations/reflections, preserve lengths
│   │   → SVD's U and V are orthogonal
│   ├── Diagonal
│   │   → Eigendecomposition's D, SVD's Σ
│   ├── Triangular (upper or lower)
│   │   → Cholesky's L, Gaussian elimination result
│   └── Invertible (det ≠ 0, full rank)
├── Non-Square Matrices
│   → Most weight matrices in neural networks
│   → SVD works on these; eigendecomposition doesn't
└── Special Products
    ├── AᵀA → always symmetric PSD (Gram matrix)
    └── AAᵀ → always symmetric PSD
```

This hierarchy matters because knowing what TYPE a matrix is tells you what tools you can use and what properties are guaranteed.

## 📺 Watch — Primary

1. **3Blue1Brown — "Change of basis" (Ch. 13)**
   - https://www.youtube.com/watch?v=P2LTAUO1TdA
   - *The visual of the same transformation looking complicated in one basis and simple in another is THE key insight. This is WHY we diagonalize.*

## 📺 Watch — Secondary

2. **3Blue1Brown — "Abstract vector spaces" (Ch. 15)**
   - https://www.youtube.com/watch?v=TgKwz5Ikpc8
   - Functions as vectors, polynomials as vectors. The abstraction that lets you apply linear algebra to activation spaces and function spaces.
3. **MIT OCW — Strang, Lecture 25: "Symmetric Matrices and Positive Definiteness"**
   - https://www.youtube.com/watch?v=UCc9q_cAhho
4. **MIT OCW — Strang, Lecture 5: "Transposes, Permutations, Spaces"**
   - https://www.youtube.com/watch?v=JibVXBElKL0
5. **Steve Brunton — "Matrix Norms"**
   - Applied treatment of norms with data science context

## 📖 Read — Primary

- **MML Book, Chapter 3.1–3.3** (norms, inner products, distances)
- **MML Book, Chapter 3.7** (inner product of functions — brief but important bridge to function spaces)
- **MML Book, Chapter 4.1** (determinant and trace)
- **MML Book, Chapter 4.3** (Cholesky decomposition — one-page treatment, quick read)
- **MML Book, Chapter 4.7** (matrix phylogeny — the family tree of matrix types, beautiful reference diagram)
- **MML Book, Chapter 2.7.2** (basis change)

## 📖 Read — Secondary

- **Interactive Linear Algebra (GT), Chapter 5.3** — change of basis with interactive visualizations
- **Stanford CS229 Math Review** — https://cs229.stanford.edu/section/cs229-linalg.pdf
  - Concise summary of LA concepts most used in ML: norms, positive definiteness, matrix calculus

## 🔨 Do

- **Change of basis exercise:** Take A = [[2, 1], [1, 2]]. Compute eigenvectors. Construct P. Verify P⁻¹AP = D is diagonal. Reconstruct A from PDP⁻¹. See the same transformation from two perspectives.
- **Norm comparison:** Generate 1000 random vectors in ℝ¹⁰. Compute L1, L2, L∞ norms. Plot histograms. Notice L1 ≥ L2 ≥ L∞ always — why?
- **Norm ball visualization:** Plot the unit ball for L1, L2, and L∞ norms in 2D. See the diamond, circle, and square. Understand why L1 encourages sparsity (the diamond's corners are on the axes — sparse solutions!).
- **Positive definiteness:** Create a symmetric matrix. Compute eigenvalues. If all positive, verify xᵀAx > 0 for random x. If some negative, find x where xᵀAx < 0.
- **Key exercise:** Take the covariance matrix of 2D data. Show it's symmetric. Show it's PSD. Find eigenvalues and eigenvectors — these are the PCA directions and variances.

## 🔗 ML Connection

**Change of basis** is fundamental to interpretability. When researchers say "analyze this in the feature basis instead of the neuron basis," they mean a change of basis. Sparse autoencoders find a new basis (feature directions) where activations look sparse and interpretable, rather than dense and opaque in the neuron basis.

**Norms** show up everywhere in training:
- **Weight decay** = L2 regularization = adding λ||W||² to the loss = penalizing large weights
- **L1 regularization** encourages sparsity — many weights become exactly zero
- **Gradient clipping** = if ||∇L|| > threshold, scale it down. Prevents exploding gradients.
- **Layer normalization** = dividing activations by their norm. Used in every transformer layer.
- **Spectral norm** of weight matrices bounds how much a layer amplifies signals

**Positive definiteness** of the Hessian tells you about loss landscape curvature. The ratio of largest to smallest Hessian eigenvalue (the **condition number**) measures how "elongated" the landscape is — high condition numbers make optimization slow (steep in one direction, flat in another).

## 🧠 Alignment Connection

**Singular Learning Theory** (SLT) cares deeply about the Hessian and its spectral properties at singularities in the loss landscape. Phase transitions — when a model suddenly "learns" a new capability — correspond to changes in effective dimensionality, measured through eigenvalue analysis. Understanding norms and positive definiteness gives you the vocabulary for this cutting-edge alignment theory.

The **neuron basis vs. feature basis** distinction is arguably the central insight of modern interpretability. Individual neurons don't correspond to clean concepts (they're "polysemantic"). But in a different basis — the feature basis found by sparse autoencoders — activations decompose into interpretable features. This is literally a change of basis making the representation interpretable.
