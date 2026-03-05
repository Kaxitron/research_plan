# Lesson 21: The Chain Rule, Directional Derivatives, and Gradients

[<- Previous](lesson-20-multivariable-functions.md) | [Back to TOC](../README.md) | [Next: Optimization & Taylor ->](lesson-22-taylor-expansions.md)

---

## Core Learning

- The multivariable chain rule tells you how to differentiate composite functions when several intermediate variables each depend on several independent variables. The key idea is tree diagrams: you sum over all paths through the dependency tree, multiplying derivatives along each path. This generalizes the single-variable chain rule f'(g(x)) * g'(x) to any number of variables and any depth of composition. The Jacobian matrix J packages this into linear algebra: for F: R^n -> R^m, the Jacobian is the m x n matrix of all partial derivatives, J_{ij} = partial F_i / partial x_j. The Jacobian IS the total derivative -- the best linear approximation to F near a point. The chain rule for compositions becomes matrix multiplication: J_{g composed with f} = J_g * J_f. This single equation IS backpropagation written in the language of linear algebra.
- Directional derivatives generalize partial derivatives by asking: how fast does f change if I move in an arbitrary direction u-hat? The answer is D_{u-hat} f = nabla f . u-hat, the dot product of the gradient with the unit direction vector. This formula reveals that the gradient nabla f encodes ALL directional information. The gradient points in the direction of steepest ascent, and its magnitude |nabla f| is the maximum rate of change. Level curves are perpendicular to the gradient, which is why gradient descent trajectories cross contour lines at right angles.
- Tangent planes and linear approximation extend these ideas geometrically. The tangent plane at a point on a surface z = f(x,y) is the best local flat approximation: z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b). In higher dimensions, this becomes f(x) approximately equals f(a) + nabla f(a) . (x-a). This linear approximation is the foundation of gradient descent: near the current parameters, the loss is approximately linear, and moving opposite to the gradient decreases it.

## Watch -- Primary

- **Trefor Bazett -- Multivariable Calculus** (chain rule, gradients, and directional derivatives sections)
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxc_CvEy7xBKRQr6I214QJcd
  - Focus on the multivariable chain rule, tree diagrams, Jacobian matrix, directional derivatives, the gradient, and tangent plane videos (roughly videos 17-20 in the playlist).

## Watch -- Secondary

- **3Blue1Brown -- "Backpropagation calculus" (Deep Learning Ch. 4)**
  - https://www.youtube.com/watch?v=tIeHLnjs5U8
  - Shows how the chain rule on a computation graph produces backpropagation -- exactly the Jacobian composition from this lesson.

## Read

- **colah's blog -- "Calculus on Computational Graphs: Backpropagation"**
  - http://colah.github.io/posts/2015-08-Backprop/
  - Essential reading. Explains backprop as the chain rule applied to computation graphs -- exactly the Jacobian composition from this lesson.
- **Stewart's Calculus** -- Chapter 14, Sections 14.4-14.6 (tangent planes, chain rule, directional derivatives and gradients).
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

Directional derivative in direction u-hat:

$$D_{\hat{u}} f = \nabla f \cdot \hat{u}$$

Gradient vector:

$$\nabla f = \left(\frac{\partial f}{\partial x_1}, \ldots, \frac{\partial f}{\partial x_n}\right)$$

Tangent plane at (a, b):

$$z = f(a,b) + f_x(a,b)(x - a) + f_y(a,b)(y - b)$$

Linear approximation:

$$f(\mathbf{x}) \approx f(\mathbf{a}) + \nabla f(\mathbf{a}) \cdot (\mathbf{x} - \mathbf{a})$$

## ML and Alignment Connection

The chain rule on computation graphs IS backpropagation. A neural network is a sequence of differentiable operations composed together. The forward pass computes the output; the backward pass multiplies Jacobians in reverse order to propagate gradients from the loss back to each parameter. The equation J_{g composed with f} = J_g * J_f is exactly what happens at each layer boundary during the backward pass.

The gradient of the loss function, nabla L(theta), is THE learning signal in neural network training. Every parameter update in gradient descent moves opposite to the gradient: theta <- theta - eta * nabla L(theta). The gradient points in the direction of steepest ascent on the loss surface, so negating it gives steepest descent. Directional derivatives tell you the learning rate in any direction, which matters when you consider that optimizers like Adam effectively change the direction of descent away from the raw gradient.

For alignment, understanding the backward pass mechanistically is essential for interpretability techniques like gradient-based attribution and for understanding how different components of the loss function (helpfulness vs harmlessness) compete during training. The gradient is the mechanism by which the objective function shapes model behavior -- if the loss landscape has a geometry where deceptive alignment sits in a deeper basin than honest alignment, gradient descent will reliably find the deceptive solution. Understanding gradients geometrically -- as perpendicular to contours, with magnitude proportional to surface steepness -- builds the intuition needed to reason about whether training signals actually point toward intended behavior.
