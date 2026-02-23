# Lesson 5: Rank, Null Space, and Column Space

[← Matrix Operations](lesson-04-matrix-operations.md) | [Back to TOC](../README.md) | [Next: The Determinant →](lesson-06-determinant.md)

---

## 🎯 Core Concepts

- **Column space:** the set of all possible outputs of Ax — it's the span of the columns
- **Null space (kernel):** all inputs x where Ax = 0 — the vectors that get "crushed to nothing"
- **Rank:** the dimension of the column space — how many independent directions the output can have
- **Rank-nullity theorem:** rank + nullity = number of columns. Information preserved + information destroyed = total information.
- **When rank < n:** the transformation squishes space down. Some information is irrecoverably lost.

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

- **MML Book, Chapter 2.8–2.9** (affine spaces, linear mappings, image/kernel)
- **Interactive Linear Algebra (GT), Chapter 2.6–2.7**

## 🔨 Do

- Compute rank and null space of several matrices by hand (via row reduction)
- In Python: generate a rank-2 matrix in ℝ³, visualize that it maps 3D space onto a 2D plane
- **Key exercise:** Create a 4×3 matrix with rank 2. Verify its null space is 1-dimensional. Find a null space vector and show Av = [0,0,0,0].

## 🔗 ML Connection

Attention matrices in transformers are deliberately **low-rank.** The QK circuit maps from 768-dimensional space through a 64-dimensional bottleneck and back. This rank constraint forces the attention head to focus on a limited number of "features." Understanding rank is crucial for reasoning about **information bottlenecks** — when does a layer lose information? When does it preserve it?
