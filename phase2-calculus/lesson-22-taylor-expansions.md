# Lesson 22: Taylor Expansions and the Implicit Function Theorem

[<- Previous](lesson-21-multiple-integration.md) | [Back to TOC](../README.md) | [Next: Optimization ->](lesson-23-optimization.md)

---

## Core Learning

- The multivariate Taylor expansion approximates a function near a point using its derivatives. The first-order term involves the gradient (linear approximation), the second-order term involves the Hessian (quadratic approximation), and higher-order terms add progressively finer corrections. At a critical point where the gradient vanishes, the local shape of the function IS the quadratic form of the Hessian -- its eigenvalues completely determine whether you are at a bowl, a dome, or a saddle.
- Big-O notation provides the language for truncation errors. Writing f(x+h) = f(x) + f'(x)h + O(h^2) means the error of the linear approximation shrinks quadratically as h shrinks. This notation is essential for analyzing the accuracy of numerical methods (Euler's method is O(h), Runge-Kutta is O(h^4)) and for understanding scaling laws in ML.
- The Implicit Function Theorem (IFT) tells you when an equation F(x, y) = 0 implicitly defines y as a smooth function of x. The condition is simple: partial F / partial y must be nonzero. Where this condition FAILS -- where the derivative vanishes -- you get singularities: points where the implicit function branches, folds, or ceases to exist. These singularities are exactly where Singular Learning Theory (SLT) becomes necessary, because neural network parameter-function maps have abundant singularities where standard statistical theory (which assumes the IFT holds) breaks down.

## Watch -- Primary

- **Trefor Bazett -- Multivariable Calculus** (Taylor expansion and approximation sections)
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxc_CvEy7xBKRQr6I214QJcd
  - Focus on multivariate Taylor series, quadratic approximation, and the Hessian's role in local geometry.

## Watch -- Secondary

- **3Blue1Brown -- "Taylor series"**
  - https://www.youtube.com/watch?v=3d6DsjIBzJ4
  - Beautiful visual explanation of Taylor series as polynomial approximations. Single-variable, but the intuition transfers directly.
- **Trefor Bazett -- Multivariable Calculus** (implicit differentiation and IFT sections)
  - Same playlist. Covers implicit differentiation and the conditions under which implicit functions exist.

## Read

- **Stewart's Calculus** -- Sections on Taylor and Maclaurin series (single variable) and the second-order approximation for multivariable functions.
- **MML Book (Deisenroth, Faisal, Ong)** -- Section 5.4 on Taylor series and linearization.
- **Watanabe, "Algebraic Geometry and Statistical Learning Theory"** -- Chapter 1, for a preview of why singularities in the parameter-function map (where IFT fails) require new mathematical tools beyond classical statistics.

## Key Equations

Multivariate Taylor expansion (2nd order):

$$f(\mathbf{x} + \mathbf{h}) \approx f(\mathbf{x}) + \nabla f(\mathbf{x})^T \mathbf{h} + \frac{1}{2} \mathbf{h}^T H(\mathbf{x}) \mathbf{h} + O(\|\mathbf{h}\|^3)$$

At a critical point (where nabla f = 0), the local shape is:

$$f(\mathbf{x}^* + \mathbf{h}) \approx f(\mathbf{x}^*) + \frac{1}{2} \mathbf{h}^T H(\mathbf{x}^*) \mathbf{h}$$

Implicit Function Theorem: if F(x_0, y_0) = 0 and partial F / partial y is nonzero at (x_0, y_0), then near that point y = g(x) for some smooth function g, with:

$$\frac{dy}{dx} = -\frac{\partial F / \partial x}{\partial F / \partial y}$$

IFT fails (singularity) when:

$$\frac{\partial F}{\partial y} = 0$$

## Do

1. **Taylor approximation comparison.** For f(x, y) = sin(x) * e^y, compute the 1st-order (linear) and 2nd-order (quadratic) Taylor approximations centered at (0, 0). Plot all three surfaces (true function, linear approx, quadratic approx) over [-1, 1] x [-1, 1]. Compute the max absolute error of each approximation over this region.

2. **Hessian at critical points.** For f(x, y) = x^3 - 3xy^2 (monkey saddle), find the critical point at the origin, compute the Hessian there, and find its eigenvalues. What does the second-order test say? Plot the function near the origin to see the monkey saddle shape that the Hessian's zero eigenvalues fail to capture.

3. **IFT failure visualization.** Consider the curve F(x, y) = y^2 - x^3 = 0 (a cusp). Plot the curve. At the origin, verify that partial F / partial y = 0 (IFT fails). Show that the curve is NOT the graph of a smooth function y = g(x) near the origin -- it has a cusp where two branches meet. Contrast with a nearby non-singular point where the IFT holds and the curve is locally a smooth graph.

```python
import numpy as np
import matplotlib.pyplot as plt

def taylor_2nd_order(f, grad_f, hessian_f, x0):
    """Return a function that evaluates the 2nd-order Taylor approx at x0."""
    f0 = f(x0)
    g0 = grad_f(x0)
    H0 = hessian_f(x0)
    def approx(x):
        h = x - x0
        return f0 + g0 @ h + 0.5 * h @ H0 @ h
    return approx

# Example: f(x,y) = sin(x) * exp(y)
f = lambda x: np.sin(x[0]) * np.exp(x[1])
grad_f = lambda x: np.array([np.cos(x[0]) * np.exp(x[1]),
                              np.sin(x[0]) * np.exp(x[1])])
hessian_f = lambda x: np.array([[-np.sin(x[0]) * np.exp(x[1]),
                                   np.cos(x[0]) * np.exp(x[1])],
                                  [np.cos(x[0]) * np.exp(x[1]),
                                   np.sin(x[0]) * np.exp(x[1])]])

x0 = np.array([0.0, 0.0])
approx = taylor_2nd_order(f, grad_f, hessian_f, x0)

# Test: compare true value vs approximation at a nearby point
x_test = np.array([0.1, 0.1])
print(f"True:   {f(x_test):.6f}")
print(f"Taylor: {approx(x_test):.6f}")
print(f"Error:  {abs(f(x_test) - approx(x_test)):.6f}")
```

## ML and Alignment Connection

Taylor expansion IS how we analyze optimization algorithms. The first-order expansion justifies gradient descent: near the current point, the loss is approximately linear, and moving opposite the gradient decreases it. The second-order expansion justifies Newton's method: using curvature information (the Hessian) gives a better approximation and can converge much faster, but at the cost of computing and inverting the Hessian (O(n^2) storage, O(n^3) inversion for n parameters).

Where the Implicit Function Theorem fails is exactly where Singular Learning Theory (SLT) becomes necessary. Standard statistical learning theory (e.g., the BIC for model selection) assumes that the map from parameters to distributions is locally one-to-one, which requires the IFT to hold. But neural networks have massive symmetries (permuting neurons, rescaling weights) that create singularities where multiple parameter values map to the same function. At these singular points, partial F / partial y = 0, the IFT fails, and the Fisher information matrix is degenerate. SLT replaces the assumptions that fail at singularities with tools from algebraic geometry, producing the RLCT (Real Log Canonical Threshold) as the correct complexity measure. Understanding where and why the IFT fails is the gateway to understanding why SLT is needed for deep learning theory.
