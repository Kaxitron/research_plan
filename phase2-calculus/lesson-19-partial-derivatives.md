# Lesson 19: Partial Derivatives, Gradients, and Directional Derivatives

[<- Previous](lesson-18-systems-odes.md) | [Back to TOC](../README.md) | [Next: Multivariable Chain Rule ->](lesson-20-multivariable-chain-rule.md)

---

## Core Learning

- Partial derivatives measure the rate of change of a function when you wiggle one input variable while holding all others fixed. They are the building blocks of multivariable calculus — every gradient, Jacobian, and Hessian is assembled from partial derivatives.
- The gradient vector collects all partial derivatives into a single object that points in the direction of steepest ascent. Its magnitude tells you how steep that ascent is. This is the central object in optimization: gradient descent simply moves opposite to the gradient. Level curves (contours) are always perpendicular to the gradient, which is why gradient descent trajectories cross contour lines at right angles.
- Directional derivatives generalize partials by asking: how fast does the function change if I move in an arbitrary direction? The answer is the dot product of the gradient with the unit direction vector, which means the gradient encodes ALL directional information. Tangent planes and linear approximation extend these ideas to give the best local flat approximation to a surface, while quadric surfaces and level curves/surfaces provide the geometric vocabulary for visualizing multivariable functions.

## Watch -- Primary

- **Trefor Bazett -- Multivariable Calculus** (full playlist)
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxc_CvEy7xBKRQr6I214QJcd
  - Focus on the sections covering partial derivatives, gradients, directional derivatives, tangent planes, and linear approximation.

## Watch -- Secondary

- **3Blue1Brown -- "Gradient descent, how neural networks learn" (Deep Learning Ch. 2)**
  - https://www.youtube.com/watch?v=IHZwWFHWa-w
  - Visual intuition for why the gradient is the direction of steepest ascent and how gradient descent uses it.

## Read

- **Stewart's Calculus** or **Thomas' Calculus** -- Chapters on partial derivatives, directional derivatives, and gradients (typically Chapters 14-15).
- **colah's blog -- "Calculus on Computational Graphs: Backpropagation"**
  - http://colah.github.io/posts/2015-08-Backprop/

## Key Equations

Gradient vector:

$$\nabla f = \left(\frac{\partial f}{\partial x_1}, \ldots, \frac{\partial f}{\partial x_n}\right)$$

Directional derivative in direction u-hat:

$$D_{\hat{u}} f = \nabla f \cdot \hat{u}$$

Tangent plane at (a, b):

$$z = f(a,b) + f_x(a,b)(x - a) + f_y(a,b)(y - b)$$

Linear approximation:

$$f(\mathbf{x}) \approx f(\mathbf{a}) + \nabla f(\mathbf{a}) \cdot (\mathbf{x} - \mathbf{a})$$

## ML and Alignment Connection

The gradient of the loss function, nabla L(theta), is THE learning signal in neural network training. Every parameter update in gradient descent moves opposite to the gradient: theta <- theta - eta * nabla L(theta). The gradient points in the direction of steepest ascent on the loss surface, so negating it gives steepest descent. Directional derivatives tell you the learning rate in any direction, which matters when you consider that optimizers like Adam effectively change the direction of descent away from the raw gradient.

For alignment, the gradient is the mechanism by which the objective function shapes model behavior. If the loss landscape has a geometry where deceptive alignment sits in a deeper basin than honest alignment, gradient descent will reliably find the deceptive solution. Understanding gradients geometrically -- as perpendicular to contours, with magnitude proportional to surface steepness -- builds the intuition needed to reason about whether training signals are actually pointing toward the behavior we intend.
