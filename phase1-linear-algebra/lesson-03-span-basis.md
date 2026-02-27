# Lesson 3: Linear Combinations, Span, and Basis

[← Vectors](lesson-02-vectors.md) | [Back to TOC](../README.md) | [Next: Linear Transformations →](lesson-04-transformations.md)

---

## 🎯 Core Concepts

- **Linear combination:** a₁v₁ + a₂v₂ + ... + aₙvₙ — scaling vectors and adding them
- **Span:** the set of ALL vectors you can reach via linear combinations of your given vectors
  - Two non-parallel vectors in 2D span the entire plane
  - Two parallel vectors only span a line (you're "stuck" on that line)
- **Basis:** a minimal set of vectors that spans the whole space — you need exactly n vectors for ℝⁿ
- **Why this matters:** a basis is a coordinate system. Different bases = different ways of describing the same space.

## 📺 Watch — Primary

1. **3Blue1Brown — "Linear combinations, span, and basis vectors" (Ch. 2)**
   - https://www.youtube.com/watch?v=k7RM-ot2NWY
   - *The animation of î and ĵ being scaled and added to reach any point is foundational. This visual should be burned into your mind.*

## 📺 Watch — Secondary

2. **MIT OCW — Strang, Lecture 9: "Independence, Basis, and Dimension"**
   - https://www.youtube.com/watch?v=yjBerM5jWsc
   - Strang emphasizes *counting* — how many vectors do you need? When are they redundant?
3. **Khan Academy — "Linear combinations and span"**
   - Good for worked examples with specific numbers

## 📖 Read

- **MML Book, Chapter 2.5–2.6** (linear independence, basis, rank)
- **Interactive Linear Algebra, Chapter 2** — https://textbooks.math.gatech.edu/ila/systems-of-equations.html

## 🔨 Do

- In Python: generate 3 random vectors in ℝ². Show that any 2D point can be written as a linear combination of 2 of them (but you only need 2, not 3)
- **Visualization exercise:** animate scaling two basis vectors to reach a target point

## 🔗 ML Connection

Superposition in neural networks is EXACTLY about linear combinations. The superposition hypothesis says: a network with n neurons can represent MORE than n concepts by encoding each concept as a *direction* (vector) in n-dimensional space. The "features" overlap — they're non-orthogonal directions, and the network uses linear combinations to separate them. The entire foundation of Anthropic's "Toy Models of Superposition" paper rests on understanding what span and basis mean.
