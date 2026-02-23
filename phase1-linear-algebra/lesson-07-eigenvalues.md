# Lesson 7: Eigenvalues and Eigenvectors

[← The Determinant](lesson-06-determinant.md) | [Back to TOC](../README.md) | [Next: SVD →](lesson-08-svd.md)

---

## 🎯 Core Concepts

- **Eigenvector:** a direction that doesn't change under the transformation — it only gets scaled
  - Av = λv — the matrix just stretches v by a factor of λ
- **Eigenvalue:** that scaling factor λ
- **Why this matters geometrically:** eigenvectors reveal the "natural axes" of a transformation. Most vectors get rotated AND scaled; eigenvectors ONLY get scaled. They're the privileged directions.
- **Characteristic equation:** det(A - λI) = 0
- **Diagonalization:** A = PDP⁻¹ where D is diagonal
  - This means: change to the eigenbasis → scale → change back
  - Powers of A become trivial: Aⁿ = PDⁿP⁻¹

## 📺 Watch — Primary

1. **3Blue1Brown — "Eigenvectors and eigenvalues" (Ch. 14)**
   - https://www.youtube.com/watch?v=PFDu9oVAE-g
   - *The visual of most vectors being knocked off their span, while eigenvectors stay on their line, is the core geometric insight.*

## 📺 Watch — Secondary

2. **3Blue1Brown — "A quick trick for computing eigenvalues"**
   - https://www.youtube.com/watch?v=e50Bj7jn9IQ
3. **MIT OCW — Strang, Lecture 21: "Eigenvalues and Eigenvectors"**
   - https://www.youtube.com/watch?v=cdZnhQjJu4I
4. **MIT OCW — Strang, Lecture 22: "Diagonalization"**
   - https://www.youtube.com/watch?v=13r9QY6cmjc
5. **Steve Brunton — "Overview of Eigenvalue Decomposition"**
   - https://www.youtube.com/c/Eigensteve

## 📖 Read — Primary

- **MML Book, Chapter 4.2–4.4** (eigenvalue decomposition)

## 📖 Read — Secondary

- **"An Intuitive Guide to Linear Algebra" by BetterExplained**
  - https://betterexplained.com/articles/linear-algebra-guide/
- **Interactive Linear Algebra (GT), Chapter 5**

## 🔨 Do

- Find eigenvalues/eigenvectors of 2×2 matrices by hand
- In Python: compute eigenvectors, visualize them as arrows that DON'T rotate under the transformation
- **Key exercise:** Take a symmetric matrix. Verify eigenvectors are orthogonal. Then take a non-symmetric matrix and show they generally aren't. This foreshadows SVD.

## 🔗 ML Connection

PCA finds the eigenvectors of the covariance matrix — the "directions of maximum variance." In interpretability, researchers use PCA on activation vectors to find important directions in the residual stream. Eigenvalues of the Hessian tell you about the curvature of the loss landscape.

## 🧠 Alignment Connection

In **Singular Learning Theory** (an emerging framework connecting to alignment), eigenvalues of certain matrices determine phase transitions in learning. The "free energy" of a model depends on the structure of its singularities, analyzed through eigenvalue-like quantities.
