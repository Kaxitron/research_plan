# Lesson 9: Singular Value Decomposition (SVD)

[← Eigenvalues](lesson-08-eigenvalues.md) | [Back to TOC](../README.md) | [Next: Dot Products and Projections →](lesson-10-dot-products.md)

---

## 🎯 Core Concepts

- **SVD: every matrix can be decomposed as A = UΣVᵀ**
  - V: rotate (align input with "natural axes")
  - Σ: scale (stretch/shrink — these are the singular values)
  - U: rotate again (align output with "natural axes" of output space)
- **SVD works for ANY matrix** — rectangular, rank-deficient, any shape. Unlike eigendecomposition, SVD is universal.
- **Singular values σ₁ ≥ σ₂ ≥ ... ≥ 0** are always non-negative and ordered
- **Rank = number of non-zero singular values**
- **Low-rank approximation:** keep only top-k singular values → best rank-k approximation (Eckart–Young theorem)
- **Connection to eigendecomposition:** singular values of A are square roots of eigenvalues of AᵀA

## 📺 Watch — Primary

1. **Steve Brunton — "SVD: Overview"**
   - https://www.youtube.com/watch?v=nbBvuuNVfco
   - Brunton's SVD series (5-7 videos) is outstanding: intuition, computation, applications.
2. **Steve Brunton — "SVD: Matrix Approximation"**
   - https://www.youtube.com/watch?v=xy3QyzhiuY4

## 📺 Watch — Secondary

3. **Visual Kernel — "SVD Visualized"**
   - https://www.youtube.com/watch?v=vSczTbgc8Rc
4. **MIT OCW — Strang, Lecture 29: "Singular Value Decomposition"**
   - https://www.youtube.com/watch?v=TX_vooSnhm8
5. **Maththebeautiful — "SVD Part 1"**

## 📖 Read — Primary

- **MML Book, Chapter 4.5** (SVD) — https://mml-book.github.io/
- **"We Recommend a Singular Value Decomposition" by Kalman (2002)** — freely available PDF

## 📖 Read — Secondary

- **Interactive Linear Algebra (GT), Chapter 6**
- **Gregory Gundersen — "SVD as Simply as Possible"**
  - https://gregorygundersen.com/blog/2018/12/10/svd/

## 🔨 Do

- Implement SVD on a small matrix by hand (compute AᵀA, find eigenvalues/eigenvectors for V, then get U and Σ)
- **Image compression project:** Load a grayscale image as a matrix. Compute SVD. Reconstruct with k = 1, 5, 10, 50, 100 singular values. Watch detail emerge.
- **Compute compression ratio:** original = m×n numbers. Rank-k SVD = m×k + k + k×n numbers. When does this save space?

## 🔗 ML Connection

SVD is *everywhere* in ML and alignment research:

- **Attention heads are low-rank:** W_Q and W_K project through a rank bottleneck. SVD reveals what information survives.
- **LoRA (Low-Rank Adaptation):** Fine-tuning via low-rank updates ΔW = BA. This IS the SVD insight.
- **Probing in interpretability:** Finding directions that predict labels is SVD-adjacent.
- **"Mathematical Framework for Transformer Circuits"** uses SVD-like decompositions extensively.

### SVD and PCA: The Same Coin

PCA asks you to find the eigenvectors of the covariance matrix C = (1/n)XᵀX. You could eigendecompose XᵀX directly — but notice what happens if you take the SVD of the data matrix X = UΣVᵀ instead:

XᵀX = (UΣVᵀ)ᵀ(UΣVᵀ) = VΣᵀUᵀUΣVᵀ = VΣ²Vᵀ

Since UᵀU = I (U is orthogonal), the U drops out entirely. What remains is the eigendecomposition of XᵀX — with V as the eigenvectors and Σ² as the eigenvalues. So **the right singular vectors (V) from SVD of your data ARE the principal components**, and the squared singular values are proportional to the variance along each direction. You don't need to form XᵀX at all — SVD on X gives you PCA for free, and is more numerically stable because it avoids squaring the singular values.
