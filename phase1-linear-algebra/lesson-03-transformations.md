# Lesson 3: Linear Transformations and Matrices

[← Span and Basis](lesson-02-span-basis.md) | [Back to TOC](../README.md) | [Next: Matrix Operations →](lesson-04-matrix-operations.md)

---

## 🎯 Core Concepts

- **THE fundamental reframe:** a matrix is not a grid of numbers — it's a *transformation* of space
- Where do the basis vectors land? That tells you EVERYTHING about the transformation
- The columns of a matrix ARE where î and ĵ end up (in 2D)
- Lines stay lines, origin stays fixed — that's what "linear" means
- Matrix-vector multiplication: "where does this vector land after the transformation?"

### Linear vs. Affine — A Crucial Distinction

- **Linear transformations** keep the origin fixed. Pure matrix multiplication y = Wx is linear.
- **Affine transformations** = linear + translation: y = Wx + b. The bias vector b shifts the origin.
- **Every neural network layer is actually *affine*, not linear.** When we say "linear layer," we mean affine — the bias term b slides the whole space over before the activation function squishes it.
- **Why this matters:** a purely linear network (no bias, no activation) can only represent functions that pass through the origin. The bias term lets each layer shift its decision boundary anywhere. Without biases, a single neuron can only separate classes with a hyperplane through the origin — a severe limitation.
- **MML Book, Chapter 2.8** covers affine spaces formally. For now, just remember: the +b in y = Wx + b is what makes neural networks *affine* transformations, and this is a feature, not a technicality.

## 📺 Watch — Primary (THE most important video in the series)

1. **3Blue1Brown — "Linear transformations and matrices" (Ch. 3)**
   - https://www.youtube.com/watch?v=kYB8IZa5AuE
   - *This is arguably the single most important video for your entire alignment journey.* The realization that matrices ARE transformations changes how you think about everything. Every neural network layer is one of these transformations.

## 📺 Watch — Secondary

2. **3Blue1Brown — "Matrix multiplication as composition" (Ch. 4)**
   - https://www.youtube.com/watch?v=XkY2DOUCWMU
   - AB means "apply B, then A." A neural network computes W₃(W₂(W₁(x))) — function composition = matrix multiplication.
3. **MIT OCW — Strang, Lecture 1: "The Geometry of Linear Equations"**
   - https://www.youtube.com/watch?v=J7DzL2_Na80
4. **MIT OCW — Strang, Lecture 3: "Multiplication and Inverse Matrices"**
   - https://www.youtube.com/watch?v=FX4C-JpTFgY

## 📖 Read — Primary

- **MML Book, Chapter 2.7** (linear mappings)
- **MML Book, Chapter 2.8** (affine spaces — skim for the distinction between linear and affine)

## 📖 Read — Secondary

- **"Immersive Linear Algebra"** — http://immersivemath.com/ila/index.html
  - 3D visualizations you can rotate. Chapters 3–4 on matrices are excellent.
- **Interactive Linear Algebra (GT)** — https://textbooks.math.gatech.edu/ila/linear-transformations.html

## 🔨 Do

- Write Python code that takes a 2×2 matrix and a grid of points, then plots the grid BEFORE and AFTER transformation
- Apply specific matrices: rotation by 90°, reflection over x-axis, shear, scaling. SEE what each one does.
- **Key exercise:** Given "rotate 45° then scale x by 2," write down the matrix WITHOUT computing — just think about where î and ĵ land. Then verify with code.

## 🔗 ML Connection

Every layer in a neural network is a matrix multiplication (linear transformation) followed by a nonlinearity. The weight matrix W literally transforms the input vector to a new position in space. An attention head's QK circuit computes a bilinear form — two matrix transformations combined with a dot product. Understanding what a matrix "does to space" is the prerequisite for understanding what an attention head "does to representations."
