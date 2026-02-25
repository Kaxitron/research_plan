# Lesson 11: Linear Algebra Capstone

[← Change of Basis](lesson-10-change-of-basis.md) | [Back to TOC](../README.md) | [Next: Matrix Calculus →](../phase2-calculus/lesson-12-matrix-calculus.md)

---

## 🎯 Core Concepts — The Unified Picture

Everything connects:

| Lesson | Concept | Role |
|--------|---------|------|
| 1 | Vectors | Building blocks |
| 2 | Linear combinations & span | What you can reach |
| 3 | Matrices as transformations | How space moves |
| 4 | Matrix multiplication | Composing transformations |
| 5 | Rank & null space | What survives and what's lost |
| 6 | Determinant | How much area/volume changes |
| 7 | Eigenvalues | Natural axes that don't rotate |
| 8 | SVD | The complete picture: rotate → scale → rotate |
| 9 | Dot products & projections | Similarity, decomposition, attention's core |
| 10 | Change of basis & norms | Same object, different perspective; measuring size |

**The unified picture:** Any matrix transformation = align input with natural directions → scale each direction independently → align output with natural directions. This is SVD. Every other concept is a window into part of this story.

## 📺 Watch — Full Consolidation

- **3Blue1Brown — Essence of Linear Algebra (FULL playlist)** in one or two sittings
  - https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
  - Now that you've studied each concept, watching them flow as a narrative is a fundamentally different experience.

## 📺 Watch — Capstone Perspectives

- **Steve Brunton — "SVD for Data Compression, Denoising, and Data-Driven Discovery"**
- **Grant Sanderson (3B1B) on Numberphile — "Singular Value Decomposition"**

## 📖 Read — Consolidation

- **MML Book, Chapters 2 + 3 + 4 (full)** — read straight through as unified treatment
  - https://mml-book.github.io/
- **MML Book, Chapter 9** (Linear Regression) — the complete worked example tying LA to ML
- **MML Book, Chapter 10** (PCA) — eigenvalues and SVD applied to real dimensionality reduction
- **"The Matrix Cookbook"** — https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf
  - Your REFERENCE for matrix identities (not cover-to-cover reading)
- **Anthropic's "A Mathematical Framework for Transformer Circuits"** — first few pages
  - https://transformer-circuits.pub/2021/framework/index.html
  - See EXACTLY how the linear algebra you just learned is used in real interpretability research

## 🔨 Do

- **30-minute comprehensive test** covering vectors, transformations, rank, determinants, eigenvalues, SVD, dot products, projections, norms
- **Integration exercise:** Take a 3×3 matrix. Compute its rank, determinant, eigenvalues, SVD, and condition number. For each, explain the geometric meaning.
- **Capstone visualization:** Create a Python visualization showing a unit circle transformed by a matrix, with eigenvectors highlighted and SVD decomposition shown step by step (Vᵀ rotates, Σ scales, U rotates)

### Linear Regression — The Ultimate Integration Exercise

This single algorithm ties together almost everything you've learned. Derive it three ways:

1. **As projection (Lesson 9):** Given data matrix X and targets y, the prediction ŷ = Xw is a vector in the column space of X. The best w minimizes ||y - Xw||², which means the residual (y - Xw) must be perpendicular to the column space. This gives the **normal equation:** Xᵀ(y - Xw) = 0, so w = (XᵀX)⁻¹Xᵀy. This IS the projection formula from Lesson 9 — you're projecting y onto the column space of X.

2. **As optimization (Lesson 15 preview):** Minimize L(w) = ||y - Xw||². Take the gradient: ∇L = -2Xᵀ(y - Xw). Set to zero → same normal equation. You could also solve this with gradient descent instead of the closed-form solution.

3. **With regularization as constrained optimization:** Add L2 penalty: L(w) = ||y - Xw||² + λ||w||². Now w = (XᵀX + λI)⁻¹Xᵀy. The λI term makes the matrix invertible even if XᵀX is singular — regularization fixes rank deficiency! This is a preview of Lesson 15b (constrained optimization).

**Implement all three in Python.** Generate noisy 2D data, fit with each method, visualize the fit. See that regularization pulls the weights toward zero (smaller, more generalizable model).

**Read:** MML Book, Chapter 9.1–9.4 for the complete treatment. Section 9.4 ("Maximum Likelihood as Orthogonal Projection") explicitly shows the projection interpretation.

### PCA — Eigenvalues Meet Real Data

PCA (Principal Component Analysis) is the practical algorithm that unifies eigenvalues, SVD, and covariance:

1. **Start with data:** n points in d dimensions, arranged as rows of matrix X (n×d).
2. **Center the data:** subtract the mean of each column (so the data is centered at the origin).
3. **Compute the covariance matrix:** C = (1/n) XᵀX. This is a d×d symmetric PSD matrix (Lesson 10).
4. **Find eigenvectors of C:** these are the **principal components** — the directions of maximum variance.
5. **Eigenvalues = variance explained:** the eigenvalue λᵢ tells you how much variance is captured by the i-th principal component. Sorted largest to smallest.
6. **Project onto top-k components:** keep only the k eigenvectors with largest eigenvalues. This gives the best rank-k approximation (Eckart-Young theorem from Lesson 8!).

**The SVD shortcut:** you don't actually need to compute XᵀX. The right singular vectors V of X ARE the principal components. The singular values σᵢ relate to eigenvalues by λᵢ = σᵢ²/n. This is why SVD and PCA are intimately connected.

**Implement PCA from scratch:**
1. Generate 2D data shaped like a tilted ellipse (correlated Gaussian)
2. Compute covariance matrix, find eigenvectors
3. Plot the data with eigenvectors as arrows (scaled by eigenvalue)
4. Project onto the first principal component — watch 2D data become 1D
5. Verify: `np.linalg.svd(X_centered)` gives the same principal components

**Read:** MML Book, Chapter 10 for the full treatment, including the latent variable perspective (Section 10.7) which connects PCA to generative modeling.

## 🔗 ML Connection — The Complete Language

You now have the complete mathematical language for understanding neural network internals:

1. **Embedding vectors** (Lesson 1) — tokens as points in space
2. **Linear combinations** (Lesson 2) — attention weighted averages; superposition
3. **Matrix transformations** (Lesson 3) — every layer transforms representation space
4. **Rank** (Lesson 5) — attention bottlenecks, LoRA, information compression
5. **Determinant** (Lesson 6) — normalizing flows, initialization theory
6. **Eigenvalues** (Lesson 7) — PCA, Hessian analysis, loss landscape curvature
7. **SVD** (Lesson 8) — decomposing what any matrix "does"
8. **Dot products** (Lesson 9) — attention scores, cosine similarity, probing
9. **Change of basis** (Lesson 10) — neuron basis vs. feature basis in interpretability
10. **Norms** (Lesson 10) — regularization, gradient clipping, layer norm

Every mechanistic interpretability paper you'll read from here builds on these foundations.
