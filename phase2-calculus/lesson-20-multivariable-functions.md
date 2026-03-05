# Lesson 20: Multivariable Functions, Limits, and Partial Derivatives

[<- Previous](lesson-19-3d-geometry.md) | [Back to TOC](../README.md) | [Next: Chain Rule & Gradients ->](lesson-21-chain-rule-gradients.md)

---

## Core Learning

- Functions of several variables f: R^n -> R take multiple inputs and produce a scalar output. For f(x, y), the graph is a surface in 3D; for more variables, you cannot visualize the graph directly but can study it through level sets (contour plots). Level curves f(x, y) = c are the "topographic map" of the surface -- places where the function has constant height. Understanding functions through their contour structure is essential: in ML, loss contours show which parameter combinations give equal loss, and understanding their shape determines whether optimization is easy or hard.
- Multivariable limits are fundamentally harder than single-variable limits because there are infinitely many paths approaching a point. If lim f(x, y) exists as (x,y) -> (a,b), it must be the same along EVERY path. The path test exploits this: if two different paths give different limits, the limit does not exist. The squeeze theorem and algebraic techniques handle the cases where the limit does exist. Continuity in multiple dimensions means the limit equals the function value, just as in one dimension, but the richer path structure makes discontinuities easier to create and harder to detect.
- Partial derivatives measure the rate of change of f when you vary one input while holding all others fixed -- they are literally single-variable derivatives taken one coordinate at a time. The notation partial f / partial x means "differentiate with respect to x, treating y as a constant." Higher-order partials like f_xy involve differentiating twice; Clairaut's theorem guarantees f_xy = f_yx when both are continuous. The critical subtlety is the differentiability hierarchy: having all partial derivatives does NOT guarantee continuity (a function can have partials everywhere but be discontinuous), while being differentiable (having a good linear approximation) DOES guarantee continuity. This hierarchy matters because gradient-based optimization implicitly assumes differentiability, not just the existence of partials.

## Watch -- Primary

- **Trefor Bazett -- Multivariable Calculus** (functions, limits, and partial derivatives sections)
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxc_CvEy7xBKRQr6I214QJcd
  - Focus on the videos covering functions of several variables, contour plots, multivariable limits, the path test, partial derivatives, and higher-order partials (roughly videos 10-16 in the playlist).

## Watch -- Secondary

- **3Blue1Brown -- "Gradient descent, how neural networks learn" (Deep Learning Ch. 2)**
  - https://www.youtube.com/watch?v=IHZwWFHWa-w
  - Visual intuition for what partial derivatives mean geometrically -- slicing a surface along coordinate directions -- and why we collect them into gradients.

## Read

- **Stewart's Calculus** -- Chapter 14, Sections 14.1-14.3 (functions of several variables, limits and continuity, partial derivatives). Includes detailed limit examples using the path test and thorough coverage of higher-order partials.
- **MML Book (Deisenroth, Faisal, Ong)** -- Section 5.1 on partial derivatives and gradients for the ML perspective.

## Key Equations

Partial derivative definition:

$$\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}$$

Clairaut's theorem (equality of mixed partials):

$$f_{xy} = f_{yx} \quad \text{(when both are continuous)}$$

Total differential:

$$df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy$$

Differentiability hierarchy:

$$\text{differentiable} \implies \text{continuous} \implies \text{limits exist}$$
$$\text{partials exist} \;\not\!\!\!\implies \text{continuous}$$

## ML and Alignment Connection

Partial derivatives are the atomic unit of gradient computation. Every element of the gradient vector nabla L(theta) is a partial derivative partial L / partial theta_i, measuring how much the loss changes when you nudge one parameter while holding all others fixed. In a neural network with millions of parameters, backpropagation efficiently computes all these partial derivatives in one backward pass rather than computing each one separately.

The differentiability hierarchy has practical consequences: activation functions like ReLU have undefined derivatives at zero, yet gradient descent still works because these non-differentiable points form a set of measure zero. Understanding when partial derivatives exist but the function is not differentiable helps explain why some theoretical guarantees of smooth optimization break down in practice -- and why techniques like gradient clipping and careful initialization exist to handle these edge cases.

Contour plots of the loss function reveal the geometry that determines optimization difficulty. Circular contours mean all directions are equally easy to optimize (well-conditioned); elongated elliptical contours mean some directions converge much faster than others (ill-conditioned), causing gradient descent to zigzag. This geometry is controlled by the eigenvalues of the Hessian, which we will study in Lesson 22.
