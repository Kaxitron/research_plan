# Lesson 11: Linear Algebra Capstone

[← Change of Basis](lesson-10-change-of-basis.md) | [Back to TOC](../README.md) | [Next: Matrix Calculus →](../phase2-calculus/lesson-12-matrix-calculus.md)

---

## 🎯 The Unified Picture

Any matrix transformation = align input with natural directions → scale each direction independently → align output with natural directions. **This is SVD.** Every other concept is a window into part of this story.

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

## 📺 Watch

- **3Blue1Brown — Essence of Linear Algebra (FULL playlist)** — rewatch as a single narrative
  - https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
- **Anthropic's "A Mathematical Framework for Transformer Circuits"** — skim the first few pages
  - https://transformer-circuits.pub/2021/framework/index.html
  - See EXACTLY how the LA you just learned is used in real interpretability research

## 📖 Read

- **MML Book, Chapters 2 + 3 + 4 (full)** — read straight through as unified treatment
  - https://mml-book.github.io/
- **"The Matrix Cookbook"** — https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf
  - Your REFERENCE for matrix identities going forward (not cover-to-cover reading)

## 🔨 Do

- **Integration exercise:** Take a 3×3 matrix. Compute its rank, determinant, eigenvalues, SVD, and condition number. For each, explain the geometric meaning.
- **Capstone visualization:** Create a Python visualization showing a unit circle transformed by a matrix, with eigenvectors highlighted and SVD decomposition shown step by step (Vᵀ rotates, Σ scales, U rotates).

## 📝 Phase 1 Final Exam + PCA Project

**[Phase 1 Final Exam](../assessments/phase1-linear-algebra-final-exam.md)** — 60-minute, 100-point comprehensive exam covering all of Lessons 1–10, plus an ungraded take-home PCA implementation project.

The exam has five sections:
- **Part A:** Geometric intuition (can you *see* what matrices do?)
- **Part B:** Core computation (eigenvalues, rank, projections, norms by hand)
- **Part C:** Proofs & reasoning (AᵀA is PSD, projection idempotency, rank-nullity)
- **Part D:** Synthesis (connect determinants ↔ eigenvalues ↔ SVD through a single matrix)
- **Part E:** ML & alignment applications (attention as dot products, superposition, change of basis in interpretability)
- **Bonus Project:** Implement PCA from scratch on synthetic data and MNIST — ties together eigenvalues, covariance, SVD, projections, rank, and change of basis into one pipeline.

## 🔗 ML Connection — The Complete Language

You now have the mathematical vocabulary for every mechanistic interpretability paper:

- **Embedding vectors** (L1) · **Linear combinations** (L2) · **Matrix transformations** (L3) · **Rank** (L5) · **Determinant** (L6) · **Eigenvalues** (L7) · **SVD** (L8) · **Dot products** (L9) · **Change of basis & norms** (L10)

Everything from here builds on these foundations.
