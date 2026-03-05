# Lesson 35: Matrix Calculus --- Jacobians, Element-wise Rules, and Chain Rules

[← Scalar Derivatives & Gradients](lesson-34-scalar-derivatives.md) | [Back to TOC](../README.md) | [Next: Neural Network Gradients →](lesson-36-neural-network-gradients.md)

---

This is the core of matrix calculus. When a function maps a vector to a vector, its derivative is no longer a single number or even a single vector --- it is a matrix called the Jacobian. Most neural network layers are vector-to-vector functions, so Jacobians are the native language of backpropagation. The key insight from Parr & Howard is that most Jacobians in deep learning are diagonal or near-diagonal because neural network operations are element-wise, and the chain rule for vectors is just matrix multiplication of Jacobians.

## Core Learning

- The Jacobian matrix: for f: R^n → R^m, J has entry (i,j) = ∂f_i/∂x_j, producing an m × n matrix (numerator layout)
- Derivatives of element-wise binary operations: when each output depends only on the corresponding inputs, the Jacobian is diagonal
- Key element-wise Jacobians: addition (identity), Hadamard product (diag(x)), element-wise division
- Scalar expansion: when a scalar interacts with a vector (e.g., y = zx), differentiate w.r.t. both the vector and the scalar
- Vector sum reduction: for L = Σf_i(x), the gradient is ∂L/∂x = Σ(∂f_i/∂x); for a simple sum, ∂(Σx_i)/∂x = 1^T
- The dot product gradient: ∂(w·x)/∂w = x^T and ∂(w·x)/∂x = w^T
- Single-variable chain rule: df/dx = (df/dg)(dg/dx)
- Total-derivative chain rule: ∂f/∂x = Σ_i (∂f/∂u_i)(∂u_i/∂x), summing contributions from all paths
- Vector chain rule: ∂f/∂x = (∂f/∂g)(∂g/∂x) --- Jacobian multiplication; this is the master rule that degenerates to all other chain rules as special cases

## Read --- Primary

- **Parr & Howard --- "The Matrix Calculus You Need for Deep Learning"**
  - https://explained.ai/matrix-calculus/
  - *Read Section 4 (all subsections 4.1--4.5): Matrix Calculus. This is the heart of the resource --- Jacobian generalization, element-wise operations, scalar expansion, vector sum reduction, and all three chain rules.*

## Read --- Secondary

- **The Matrix Cookbook** (Petersen & Pedersen)
  - *Comprehensive reference of matrix derivative identities. Bookmark permanently.*
- **MML textbook, Chapter 5.3--5.4: Gradients of Vector-Valued Functions**
  - *Formal Jacobian treatment that complements the Parr & Howard presentation.*

## Watch --- Primary

- **3Blue1Brown --- "Backpropagation calculus"**
  - https://www.youtube.com/watch?v=tIeHLnjs5U8
  - *The clearest visual explanation of how the chain rule flows backward through a computation graph. This IS Jacobian multiplication in action.*

## Watch --- Secondary

- **Ari Seff --- "What is Automatic Differentiation?"**
  - *Covers forward vs reverse mode autodiff with clear computation graph examples.*

## Key Equations

**Jacobian (vector-by-vector derivative, numerator layout):**

$$J = \frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n} \end{bmatrix} \quad (m \times n)$$

**Element-wise operations (diagonal Jacobians):**

$$\frac{\partial(\mathbf{w} + \mathbf{x})}{\partial \mathbf{w}} = I, \qquad \frac{\partial(\mathbf{w} \circ \mathbf{x})}{\partial \mathbf{w}} = \text{diag}(\mathbf{x})$$

**Scalar expansion:**

$$\mathbf{y} = z\mathbf{x}: \quad \frac{\partial \mathbf{y}}{\partial \mathbf{x}} = zI, \quad \frac{\partial \mathbf{y}}{\partial z} = \mathbf{x}^T$$

**Vector sum reduction:**

$$\frac{\partial}{\partial \mathbf{x}} \sum_i x_i = \mathbf{1}^T, \qquad \frac{\partial(\mathbf{w} \cdot \mathbf{x})}{\partial \mathbf{x}} = \mathbf{w}^T$$

**Vector chain rule:**

$$\frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \frac{\partial \mathbf{f}}{\partial \mathbf{g}} \cdot \frac{\partial \mathbf{g}}{\partial \mathbf{x}}$$

Jacobian of the composition = product of Jacobians.

**Total-derivative chain rule (scalar case with multiple paths):**

$$\frac{\partial f}{\partial x} = \sum_i \frac{\partial f}{\partial u_i} \frac{\partial u_i}{\partial x}$$

## ML and Alignment Connection

The vector chain rule --- Jacobian multiplication --- is backpropagation. When you call `.backward()` in PyTorch, the framework multiplies Jacobians layer by layer from the loss back to the parameters. Understanding that most layer Jacobians are diagonal (element-wise activations like ReLU) or structured (linear layers give $J = W$) explains why backpropagation is efficient: you never materialize the full Jacobian, you just multiply by it. This is also why certain architectures cause vanishing or exploding gradients --- the product of many Jacobians can shrink or grow exponentially, and the structure of each layer's Jacobian determines which happens.
