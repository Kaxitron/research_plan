# Lesson 20: The Multivariable Chain Rule and Jacobian Matrices

[<- Previous](lesson-19-partial-derivatives.md) | [Back to TOC](../README.md) | [Next: Multiple Integration ->](lesson-21-multiple-integration.md)

---

## Core Learning

- The multivariable chain rule tells you how to differentiate composite functions when several intermediate variables each depend on several independent variables. The key idea is tree diagrams: you sum over all paths through the dependency tree, multiplying derivatives along each path. This generalizes the single-variable chain rule f'(g(x)) * g'(x) to any number of variables and any depth of composition.
- The Jacobian matrix packages this idea into linear algebra. For a function F: R^n -> R^m, the Jacobian J is the m x n matrix of all partial derivatives, J_{ij} = partial F_i / partial x_j. The Jacobian IS the total derivative -- the best linear approximation to F near a point. The chain rule for compositions becomes matrix multiplication: J_{g composed with f} = J_g * J_f. This single equation IS backpropagation written in the language of linear algebra.
- The Hessian matrix H_{ij} = partial^2 f / partial x_i partial x_j collects second-order partial derivatives and describes the curvature of a scalar function. Its eigenvalues are the curvatures in each eigendirection: positive definite means bowl (minimum), negative definite means dome (maximum), mixed signs mean saddle. The condition number (ratio of largest to smallest eigenvalue) controls how elongated the loss landscape is, which directly determines how badly gradient descent zigzags.

## Watch -- Primary

- **Trefor Bazett -- Multivariable Calculus** (chain rule and Jacobian sections)
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxc_CvEy7xBKRQr6I214QJcd
  - Focus on the multivariable chain rule, tree diagrams, and Jacobian matrix videos.

## Watch -- Secondary

- **3Blue1Brown -- "Backpropagation calculus" (Deep Learning Ch. 4)**
  - https://www.youtube.com/watch?v=tIeHLnjs5U8
  - Shows how the chain rule on a computation graph produces backpropagation.
- **Trefor Bazett -- Multivariable Calculus** (curvature, TNB frame sections)
  - Same playlist. The curvature and Frenet-Serret frame material connects to how curves bend in space, providing geometric intuition for the Hessian.

## Read

- **colah's blog -- "Calculus on Computational Graphs: Backpropagation"**
  - http://colah.github.io/posts/2015-08-Backprop/
  - Essential reading. Explains backprop as the chain rule applied to computation graphs -- exactly the Jacobian composition from this lesson.
- **MML Book (Deisenroth, Faisal, Ong)** -- Section 5.2 on the chain rule and Section 5.3 on gradients of compositions.

## Key Equations

Multivariable chain rule (scalar version):

$$\frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt}$$

General chain rule (sum over all paths):

$$\frac{\partial f}{\partial t_j} = \sum_{i} \frac{\partial f}{\partial x_i}\frac{\partial x_i}{\partial t_j}$$

Jacobian matrix for F: R^n -> R^m:

$$J = \begin{bmatrix} \partial F_1/\partial x_1 & \cdots & \partial F_1/\partial x_n \\ \vdots & \ddots & \vdots \\ \partial F_m/\partial x_1 & \cdots & \partial F_m/\partial x_n \end{bmatrix}$$

Chain rule as Jacobian multiplication:

$$J_{g \circ f} = J_g \cdot J_f$$

Hessian matrix:

$$H_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}$$

## Do

1. **Tree diagram practice.** Given z = f(x, y) where x = g(s, t) and y = h(s, t), draw the dependency tree and write out partial z / partial s and partial z / partial t by summing over all paths. Verify with a concrete example: z = x^2 * y, x = s + t, y = s * t.

2. **Jacobian composition as backprop.** Build a simple two-layer computation: x -> (layer 1) -> h -> (layer 2) -> y, where layer 1 is h = sigma(Wx + b) and layer 2 is y = Vh + c, with sigma = tanh. Compute J_{layer1} and J_{layer2} analytically. Verify that J_{layer2} * J_{layer1} gives the same result as computing the full Jacobian of the composition directly.

3. **Hessian eigenvalue explorer.** For f(x, y) = x^2 + k*y^2 with k = 1, 5, 25, compute the Hessian, find its eigenvalues, and compute the condition number. Run gradient descent on each and plot the trajectories. Show that higher condition number produces more zigzagging.

```python
import numpy as np

def jacobian_numerical(F, x, h=1e-5):
    """Compute Jacobian of F: R^n -> R^m numerically."""
    f0 = F(x)
    m = len(f0)
    n = len(x)
    J = np.zeros((m, n))
    for j in range(n):
        e_j = np.zeros(n)
        e_j[j] = h
        J[:, j] = (F(x + e_j) - F(x - e_j)) / (2 * h)
    return J

# Example: verify chain rule J_{g o f} = J_g * J_f
def f(x):
    return np.array([x[0]**2 + x[1], x[0]*x[1]])

def g(y):
    return np.array([np.sin(y[0] + y[1])])

def gof(x):
    return g(f(x))

x0 = np.array([1.0, 2.0])
J_f = jacobian_numerical(f, x0)
J_g = jacobian_numerical(g, f(x0))
J_gof = jacobian_numerical(gof, x0)

print("J_g @ J_f:\n", J_g @ J_f)
print("J_{g o f}:\n", J_gof)
print("Match:", np.allclose(J_g @ J_f, J_gof))
```

## ML and Alignment Connection

The chain rule on computation graphs IS backpropagation. A neural network is a sequence of differentiable operations composed together. The forward pass computes the output; the backward pass multiplies Jacobians in reverse order to propagate gradients from the loss back to each parameter. The equation J_{g composed with f} = J_g * J_f is exactly what happens at each layer boundary during the backward pass.

The Hessian measures curvature of the loss landscape. Its eigenvalues determine whether a critical point is a minimum (all positive), maximum (all negative), or saddle (mixed). In high-dimensional neural networks, saddle points vastly outnumber local minima (by random matrix theory arguments), so the Hessian spectrum tells you what kind of landscape the optimizer is navigating. The condition number lambda_max / lambda_min controls convergence speed -- poorly conditioned landscapes cause gradient descent to zigzag, which is why adaptive optimizers like Adam exist.

For alignment, understanding the backward pass mechanistically is essential for interpretability techniques like gradient-based attribution and for understanding how different components of the loss function (helpfulness vs harmlessness) compete during training.
