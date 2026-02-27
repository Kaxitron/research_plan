# Lesson 5: Matrix Operations Deep Dive

[← Transformations](lesson-04-transformations.md) | [Back to TOC](../README.md) | [Next: Rank and Null Space →](lesson-06-rank-nullspace.md)

---

## 🎯 Core Concepts

- **Matrix-vector multiplication: two equivalent views**
  - Row view: each output entry is a dot product (pattern matching)
  - Column view: the output is a linear combination of the columns
  - Both are true simultaneously — being able to switch between them is a superpower
- **Matrix-matrix multiplication:** composition of transformations
  - AB ≠ BA in general (rotating then scaling ≠ scaling then rotating)
  - But (AB)C = A(BC) — associativity
- **Transpose:** reflection over the diagonal; rows become columns
  - (AB)ᵀ = BᵀAᵀ — the "reverse order" rule

## 📺 Watch — Primary

1. **3Blue1Brown Ch. 3–4** (review, focusing on the two views of multiplication)
2. **MIT OCW — Strang, Lecture 2 & 3**
   - Strang's four ways to see matrix multiplication is uniquely powerful
   - https://www.youtube.com/watch?v=QVKj3LADCnA

## 📺 Watch — Secondary

3. **Khan Academy — "Matrix multiplication"** series
4. **Professor Leonard — "Matrix Multiplication"**
   - https://www.youtube.com/c/ProfessorLeonard

## 📖 Read

- **MML Book, Chapter 2.2** (matrices and matrix operations)
- **"Introduction to Linear Algebra" by Strang** — Chapter 1 on matrix multiplication is the gold standard

## 🔨 Do

- Implement matrix multiplication from scratch in Python (no NumPy) — three nested loops
- Then implement it BOTH ways: (a) row-dot-product view, (b) linear-combination-of-columns view
- Verify they give the same answer
- **Speed test:** compare your implementation to NumPy's — GPUs are matrix multiplication accelerators

## 🔗 ML Connection

The forward pass through a neural network IS a sequence of matrix multiplications. When interpretability researchers decompose attention into QK and OV circuits, they're factoring matrix products. Understanding that Wₒ · Wᵥ can be treated as a single matrix (the OV circuit) — that's composition of transformations. The "Mathematical Framework for Transformer Circuits" paper leans heavily on this.
