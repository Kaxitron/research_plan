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
- **"The Matrix Cookbook"** — https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf
  - Your REFERENCE for matrix identities (not cover-to-cover reading)
- **Anthropic's "A Mathematical Framework for Transformer Circuits"** — first few pages
  - https://transformer-circuits.pub/2021/framework/index.html
  - See EXACTLY how the linear algebra you just learned is used in real interpretability research

## 🔨 Do

- **30-minute comprehensive test** covering vectors, transformations, rank, determinants, eigenvalues, SVD, dot products, projections, norms
- **Integration exercise:** Take a 3×3 matrix. Compute its rank, determinant, eigenvalues, SVD, and condition number. For each, explain the geometric meaning.
- **Capstone visualization:** Create a Python visualization showing a unit circle transformed by a matrix, with eigenvectors highlighted and SVD decomposition shown step by step (Vᵀ rotates, Σ scales, U rotates)

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
