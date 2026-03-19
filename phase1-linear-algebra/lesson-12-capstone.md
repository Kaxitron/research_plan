# Lesson 12: Linear Algebra Capstone

[← Change of Basis](lesson-11-change-of-basis.md) | [Back to TOC](../README.md) | [Next: Scalar Derivatives →](../phase2-calculus/lesson-34-scalar-derivatives.md)

---

## 🎯 The Unified Picture

Any matrix transformation = align input with natural directions → scale each direction independently → align output with natural directions. **This is SVD.** Every other concept is a window into part of this story.

| Lesson | Concept | Role |
|--------|---------|------|
| 2 | Vectors | Building blocks |
| 3 | Linear combinations & span | What you can reach |
| 4 | Matrices as transformations | How space moves |
| 5 | Matrix multiplication | Composing transformations |
| 6 | Rank & null space | What survives and what's lost |
| 7 | Determinant | How much area/volume changes |
| 8 | Eigenvalues | Natural axes that don't rotate |
| 9 | SVD | The complete picture: rotate → scale → rotate |
| 10 | Dot products & projections | Similarity, decomposition, attention's core |
| 11 | Change of basis & norms | Same object, different perspective; measuring size |

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
- **Capstone visualization:** See the full project spec: [capstone-linalg-visualization.pdf](capstone-linalg-visualization.pdf)

## 📝 Phase 1 Final Exam + PCA Project

**[Phase 1 Final Exam](../assessments/phase1-linear-algebra-final-exam.md)** — 60-minute, 100-point comprehensive exam covering all of Lessons 2–10, plus an ungraded take-home PCA implementation project.

The exam has five sections:
- **Part A:** Geometric intuition (can you *see* what matrices do?)
- **Part B:** Core computation (eigenvalues, rank, projections, norms by hand)
- **Part C:** Proofs & reasoning (AᵀA is PSD, projection idempotency, rank-nullity)
- **Part D:** Synthesis (connect determinants ↔ eigenvalues ↔ SVD through a single matrix)
- **Part E:** ML & alignment applications (attention as dot products, superposition, change of basis in interpretability)
- **Bonus Project:** Implement PCA from scratch on synthetic data and MNIST — ties together eigenvalues, covariance, SVD, projections, rank, and change of basis into one pipeline.

## 🔗 ML & Alignment Connection — The Complete Language

You now have the mathematical vocabulary for every mechanistic interpretability paper:

- **Embedding vectors** (L2) · **Linear combinations** (L3) · **Matrix transformations** (L4) · **Rank** (L6) · **Determinant** (L7) · **Eigenvalues** (L8) · **SVD** (L9) · **Dot products** (L10) · **Change of basis & norms** (L11)

Everything from here builds on these foundations.

---

## 📝 Time to Take the Exam

You've completed all of Phase 1. Every tool in the linear algebra toolkit is now yours. Time to prove it.

👉 **[Phase 1 Final Exam: Linear Algebra](../assessments/exam-1-linear-algebra.md)**
