# Lesson 6: Rank, Null Space, and Column Space

[← Matrix Operations](lesson-05-matrix-operations.md) | [Back to TOC](../README.md) | [Next: The Determinant →](lesson-07-determinant.md)

---

## 🎯 Core Concepts

- **Column space:** the set of all possible outputs of Ax — it's the span of the columns
- **Null space (kernel):** all inputs x where Ax = 0 — the vectors that get "crushed to nothing"
- **Rank:** the dimension of the column space — how many independent directions the output can have
- **Rank-nullity theorem:** rank + nullity = number of columns. Information preserved + information destroyed = total information.
- **When rank < n:** the transformation squishes space down. Some information is irrecoverably lost.

### Gaussian Elimination — The Computational Workhorse

- **Row echelon form:** using three operations (swap rows, scale a row, add a multiple of one row to another), reduce any matrix to upper triangular form. The number of non-zero rows = rank.
- **The algorithm:** work left-to-right, top-to-bottom. For each column, find a non-zero entry (the "pivot"), swap it to the current row, then eliminate all entries below it by subtracting multiples of the pivot row.
- **Reduced row echelon form (RREF):** go further — eliminate entries ABOVE pivots too, and scale all pivots to 1. Now you can read off the solution directly.
- **Why this matters:** this is how you *actually compute* rank, find null space vectors, solve Ax = b, and determine if a set of vectors is independent. The geometry (Lessons 2-4) tells you what these things *mean*; Gaussian elimination tells you how to *find* them.
- **Reading the result:** after row reduction, pivot columns correspond to independent columns (basis for column space). Free columns correspond to null space directions. The rank equals the number of pivots.
- **In practice:** NumPy/MATLAB do this for you (via LU decomposition, a dressed-up version of elimination). But doing it by hand on small matrices builds the intuition for when code gives unexpected results.

### MML Reference

- **MML Book, Chapter 2.1** covers systems of linear equations
- **MML Book, Chapter 2.3** covers Gaussian elimination in full detail with worked examples

## 📺 Watch — Primary

1. **3Blue1Brown — "Inverse matrices, column space, null space" (Ch. 7)**
   - https://www.youtube.com/watch?v=uQhTuRlWMxw
   - *The visualization of 3D space being squished to a 2D plane (rank 2) or a line (rank 1) is unforgettable.*
2. **3Blue1Brown — "Nonsquare matrices" (Ch. 8)**
   - https://www.youtube.com/watch?v=v8VSDg_WQlA
   - Critical for ML: weight matrices are almost always non-square

## 📺 Watch — Secondary

3. **MIT OCW — Strang, Lecture 6: "Column Space and Nullspace"**
   - https://www.youtube.com/watch?v=8o5Cmfpeo6g
4. **MIT OCW — Strang, Lecture 7: "Solving Ax = 0"**
   - https://www.youtube.com/watch?v=VqP2tREMvt0
5. **MIT OCW — Strang, Lecture 10: "The Four Fundamental Subspaces"**
   - https://www.youtube.com/watch?v=nHlE7EgMFYo

## 📖 Read

- **MML Book, Chapter 2.1–2.3** (systems of linear equations, Gaussian elimination — the computational foundation)
- **MML Book, Chapter 2.8–2.9** (affine spaces, linear mappings, image/kernel)
- **Interactive Linear Algebra (GT), Chapter 2.6–2.7**

## 🔨 Do

- **Gaussian elimination by hand:** Take A = [[1, 2, 3], [2, 4, 7], [3, 6, 10]]. Row reduce to echelon form. Read off the rank (2). Identify the free variable. Find the null space vector. Verify Av = 0.
- Compute rank and null space of several matrices by hand (via row reduction)
- In Python: generate a rank-3 matrix in ℝ³, visualize that it maps 3D space onto a 2D plane
- **Key exercise:** Create a 4×3 matrix with rank 2. Verify its null space is 1-dimensional. Find a null space vector and show Av = [0,0,0,0].
- **Implement row reduction in Python:** write a function that takes a matrix and returns its RREF. Compare your output to `numpy.linalg.matrix_rank()` and `scipy.linalg.null_space()`.

## 🔗 ML Connection

Attention matrices in transformers are deliberately **low-rank.** The QK circuit maps from 768-dimensional space through a 64-dimensional bottleneck and back. This rank constraint forces the attention head to focus on a limited number of "features." Understanding rank is crucial for reasoning about **information bottlenecks** — when does a layer lose information? When does it preserve it?
