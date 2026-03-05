# Lesson 36: Neural Network Gradients --- From Neurons to Backpropagation

[← Matrix Calculus](lesson-35-matrix-calculus.md) | [Back to TOC](../README.md) | [Phase 3 →](../phase3-prob-stats/lesson-37-probability.md)

---

This lesson applies everything from the previous two lessons to compute actual neural network gradients end-to-end. Following Parr & Howard, we derive the gradient of a single neuron's activation, then the gradient of a full network's loss function with respect to both weights and bias. This is backpropagation derived from first principles --- not as a mysterious algorithm but as the mechanical application of the chain rule and Jacobian multiplication from Lesson 35. The lesson culminates in building a working autodiff engine.

## Core Learning

- Derive the gradient of a single neuron activation: f(w, x, b) = max(0, w·x + b)
- Compute ∂f/∂w, ∂f/∂x, and ∂f/∂b for the ReLU neuron using the chain rule
- Derive the gradient of the MSE loss C = (1/N) Σ(y_hat_i - y_i)^2 with respect to weights w and bias b
- Understand how ReLU's piecewise derivative gates the gradient: zero when inactive, passes through when active
- See gradient descent as the direct application of these derivatives: w ← w - α(∂C/∂w)
- Understand computation graphs: neural networks as DAGs of differentiable operations
- Forward-mode autodiff: propagates tangent vectors forward, computes one Jacobian column per pass
- Reverse-mode autodiff: propagates adjoint vectors backward, computes one Jacobian row per pass (= backpropagation)
- Why reverse mode dominates: one scalar loss, millions of parameters means one backward pass suffices

## Read --- Primary

- **Parr & Howard --- "The Matrix Calculus You Need for Deep Learning"**
  - https://explained.ai/matrix-calculus/
  - *Read Sections 5--8: Gradient of Neuron Activation, Gradient of the Neural Network Loss Function, Summary, and the Matrix Calculus Reference. This is where all the theory gets applied to an actual neural network.*

## Read --- Secondary

- **Karpathy --- micrograd source code and walkthrough**
  - https://github.com/karpathy/micrograd
  - *A minimal autodiff engine in ~100 lines of Python. Read it after understanding the theory to see it implemented.*

## Watch --- Primary

- **Karpathy --- "The spelled-out intro to neural networks and backpropagation: building micrograd"**
  - https://www.youtube.com/watch?v=VMj-3S1tku0
  - *2.5-hour walkthrough building an autodiff engine from scratch. The perfect complement to the Parr & Howard text --- he builds exactly what the theory describes.*

## Watch --- Secondary

- **3Blue1Brown --- "Backpropagation calculus"**
  - https://www.youtube.com/watch?v=tIeHLnjs5U8
  - *Revisit for the visual picture of how gradients flow backward through a computation graph.*
- **Stanford CS231n --- Backpropagation lecture**
  - *More detailed treatment with worked neural network examples including multi-layer networks.*

## Key Equations

**Single neuron activation (ReLU):**

$$f(\mathbf{w}, \mathbf{x}, b) = \max(0,\; \mathbf{w} \cdot \mathbf{x} + b)$$

**Gradient of the dot product:**

$$\frac{\partial(\mathbf{w} \cdot \mathbf{x})}{\partial \mathbf{w}} = \mathbf{x}^T, \qquad \frac{\partial(\mathbf{w} \cdot \mathbf{x})}{\partial \mathbf{x}} = \mathbf{w}^T, \qquad \frac{\partial(\mathbf{w} \cdot \mathbf{x} + b)}{\partial b} = 1$$

**ReLU derivative (piecewise):**

$$\frac{\partial}{\partial u} \max(0, u) = \begin{cases} 0 & \text{if } u \leq 0 \\ 1 & \text{if } u > 0 \end{cases}$$

**Full neuron gradient (by chain rule):**

$$\frac{\partial f}{\partial \mathbf{w}} = \begin{cases} \mathbf{0} & \text{if } \mathbf{w} \cdot \mathbf{x} + b \leq 0 \\ \mathbf{x}^T & \text{if } \mathbf{w} \cdot \mathbf{x} + b > 0 \end{cases}$$

**MSE loss:**

$$C = \frac{1}{N} \sum_{i=1}^{N} (\hat{y}_i - y_i)^2$$

**Gradient of loss w.r.t. weights:**

$$\frac{\partial C}{\partial \mathbf{w}} = \frac{1}{N} \sum_i \text{(error term)}_i \cdot \mathbf{x}_i^T$$

where the error term is $(\hat{y}_i - y_i)$ when the neuron is active, 0 otherwise.

**Gradient descent update:**

$$\mathbf{w} \leftarrow \mathbf{w} - \alpha \frac{\partial C}{\partial \mathbf{w}}, \qquad b \leftarrow b - \alpha \frac{\partial C}{\partial b}$$

**Reverse-mode autodiff (backpropagation):**

Start with $\partial L / \partial L = 1$. At each node, apply the chain rule: $\partial L / \partial x = (\partial L / \partial y)(\partial y / \partial x)$. For branching paths, sum contributions.

## Block E Capstone Project --- Autodiff Engine (4h)

**Part 1: Build a reverse-mode autodiff engine (~2h)**
1. Define a `Value` class (Python) with `data`, `grad`, and a computation graph
2. Implement `forward` and `backward` for: +, -, *, /, ReLU, tanh
3. Build a 2-layer MLP on XOR using your engine
4. Verify all gradients against finite differences: |autodiff - (f(x+h) - f(x-h))/2h| < 1e-5

**Part 2: Apply the theory (~2h)**
5. Train a small network on a toy dataset, printing the gradient of each layer at each step --- confirm that ReLU zeros out gradients for inactive neurons
6. Compare forward-mode vs reverse-mode autodiff on your engine: time one forward pass per input dimension vs one backward pass for all parameters

## ML and Alignment Connection

This lesson makes backpropagation fully transparent. The gradient of the loss with respect to each weight is a chain of Jacobian multiplications from the loss back through every layer. The ReLU's piecewise derivative acts as a gate: inactive neurons contribute zero gradient, effectively disappearing from the backward pass. This gating is the mechanistic basis of feature selection in neural networks --- which neurons are "on" for a given input determines which parameters get updated. For alignment, this means a model's learned behavior is shaped not just by the loss function but by which neurons happen to activate during training, creating path-dependent training dynamics that are hard to predict but essential to understand.
