# Lesson 34: Scalar Derivatives, Partial Derivatives, and the Gradient

[← PDEs & ML](lesson-33-pdes-ml.md) | [Back to TOC](../README.md) | [Next: Matrix Calculus →](lesson-35-matrix-calculus.md)

---

This lesson begins the matrix calculus block using Parr & Howard's *The Matrix Calculus You Need for Deep Learning* as the primary text. We start with scalar derivatives and partial derivatives, building toward the gradient --- the single most important object in all of deep learning. Everything here is review from earlier lessons, but now reframed with the explicit goal of differentiating neural network computations.

## Core Learning

- Review scalar derivative rules: constant, power, sum, product, and chain rules
- Understand functions of multiple parameters: f(x_1, ..., x_n) → R
- Compute partial derivatives by treating all variables except the target as constants
- Assemble partial derivatives into the gradient vector: ∇f = [∂f/∂x_1, ..., ∂f/∂x_n]
- Understand the gradient as the direction of steepest ascent and its magnitude as the rate of change in that direction
- Distinguish between the gradient (scalar output, vector input) and the Jacobian (vector output, vector input) --- to be developed in the next lesson

## Read --- Primary

- **Parr & Howard --- "The Matrix Calculus You Need for Deep Learning"**
  - https://explained.ai/matrix-calculus/
  - *Read Sections 1--3: Introduction, Review of Scalar Derivative Rules, and Introduction to Vector Calculus and Partial Derivatives. This establishes the notation and mindset for the rest of the block.*

## Read --- Secondary

- **MML textbook, Chapter 5.1--5.2: Gradients of Real-Valued Functions**
  - *Formal treatment that complements the Parr & Howard presentation.*

## Watch --- Primary

- **3Blue1Brown --- "Gradient descent, how neural networks learn"**
  - https://www.youtube.com/watch?v=IHZwWFHWa-w
  - *Connects the gradient to neural network training with 3B1B's signature visual style.*

## Key Equations

**Scalar derivative rules (review):**

| Rule | Formula |
|------|---------|
| Constant | $d/dx\; c = 0$ |
| Power | $d/dx\; x^n = nx^{n-1}$ |
| Sum | $d/dx\;[f + g] = f' + g'$ |
| Product | $d/dx\;[fg] = f'g + fg'$ |
| Chain | $d/dx\;f(g(x)) = f'(g(x)) \cdot g'(x)$ |

**Partial derivative:**

$$\frac{\partial f}{\partial x_i} = \lim_{h \to 0} \frac{f(x_1, \ldots, x_i + h, \ldots, x_n) - f(x_1, \ldots, x_n)}{h}$$

Treat all variables except $x_i$ as constants, then differentiate normally.

**The gradient:**

$$\nabla f = \left[\frac{\partial f}{\partial x_1},\; \frac{\partial f}{\partial x_2},\; \ldots,\; \frac{\partial f}{\partial x_n}\right]$$

A horizontal vector (row vector in numerator layout) collecting all partial derivatives.

## ML and Alignment Connection

The gradient is the fundamental object in neural network training. Every call to `loss.backward()` computes a gradient --- the vector of partial derivatives of the scalar loss with respect to every parameter. Understanding that the gradient is just a vector of partial derivatives, assembled mechanically by the rules in this lesson, demystifies the entire training process. There is no magic: backpropagation is the chain rule applied systematically.
