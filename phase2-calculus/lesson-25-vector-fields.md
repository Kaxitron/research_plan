# Lesson 25: Vector Fields and Conservative Fields (Bazett Ch. 2-3)

[<- Previous](lesson-24-line-integrals.md) | [Back to TOC](../README.md) | [Next: Green's Theorem ->](lesson-26-greens-theorem.md)

---

## Core Learning

A vector field assigns a vector to every point in space. In 2D, F(x, y) = (P(x, y), Q(x, y)) gives an arrow at each point; in 3D, F(x, y, z) = (P, Q, R). The gradient of any scalar function is a vector field -- the gradient field of the loss function is the vector field that gradient descent follows. But not every vector field is a gradient field, and the distinction between those that are (conservative fields) and those that are not is one of the most important ideas in vector calculus.

Two key local properties of vector fields are divergence and curl. The divergence dP/dx + dQ/dy measures expansion or compression at a point -- whether the field is "spreading out" (source) or "pulling in" (sink). The 2D scalar curl dQ/dx - dP/dy measures the local rotational tendency -- how much the field "swirls" around a point. These quantities become the integrand in Green's theorem (next lesson), but you need to understand them as standalone properties of the field first.

The line integral of a vector field along a curve measures "work" -- how much the field pushes along the path. This can also be written in component form as integral of P dx + Q dy + R dz. The flux integral measures how much of the field passes through a curve (2D) or surface (3D) rather than along it. For a conservative field F = grad(phi), the Fundamental Theorem for Line Integrals says the work depends only on the endpoints: integral of F dot dr = phi(B) - phi(A). This is path-independence, and it is equivalent to saying every closed loop integral is zero. The test for conservativeness in 2D is simple: dP/dy = dQ/dx (the mixed partials of the potential must agree). When this fails, the field has nonzero curl -- it pushes things around in loops, and the work done depends on which path you take. The language of exact and closed differential forms captures this same idea: a form is exact if it is the differential of some function (conservative), and closed if it satisfies the curl-free condition. In simply connected domains, closed implies exact.

This distinction is directly relevant to understanding gradient descent. The gradient field of a loss function is conservative by definition -- the loss itself is the potential function. But when you account for stochasticity (mini-batch gradients), the effective vector field that SGD follows is NOT exactly conservative. The noise introduces a non-conservative component, which means the path you take through parameter space matters -- this is why data ordering and curriculum learning affect final performance.

- Vector fields in 2D and 3D: visualization, interpretation as force fields or velocity fields
- Gradient vector fields F = grad(phi) and potential functions phi
- Divergence of a vector field: dP/dx + dQ/dy as expansion/compression density
- Line integral of a vector field (work): integral of F dot dr
- Line integrals with respect to x, y, z: integral of P dx, Q dy, R dz and their relationship to the work integral
- Flux integrals with components: measuring outward flow through a curve
- Curl in 2D (scalar curl): dQ/dx - dP/dy as circulation density
- The Fundamental Theorem for Line Integrals (FTLI)
- Path-independence, equivalent conditions for conservative fields
- Testing conservativeness: dP/dy = dQ/dx in 2D
- Exact and closed forms: the relationship between exact differentials, closed forms, and conservative fields
- Finding potential functions by systematic integration
- Simply connected domains: why topology matters for conservativeness

## Watch -- Primary

- **Trefor Bazett -- Vector Calculus, Chapter 2-3 videos**
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxfW0GMqeUE1bLKaYor6kbHa
  - *Bazett covers vector fields, work integrals, conservative fields, and the FTLI. The visualizations of path-independence are particularly helpful.*

## Watch -- Secondary

- **Khan Academy -- Line integrals and vector fields**
  - https://www.khanacademy.org/math/multivariable-calculus/integrating-multivariable-functions
  - *Good supplementary worked examples if you want more practice with computation.*

## Read

- **Bazett's Vector Calculus textbook, Chapters 2-3** -- vector fields, line integrals of vector fields, conservative fields, FTLI
- **Paul's Online Math Notes -- Conservative Vector Fields**
  - https://tutorial.math.lamar.edu/Classes/CalcIII/ConservativeVectorField.aspx

## Key Equations

**Divergence (2D):**

$$\text{div}(\mathbf{F}) = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y}$$

**Scalar curl (2D):**

$$\text{curl}(\mathbf{F}) = \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}$$

**Work (line integral of a vector field):**

$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t) \, dt = \int_C P \, dx + Q \, dy + R \, dz$$

**Fundamental Theorem for Line Integrals:**

$$\int_C \nabla f \cdot d\mathbf{r} = f(B) - f(A)$$

**Conservative field test (2D):**

$$\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}$$

## ML & Alignment Connection

The gradient field -grad(L) IS a vector field on parameter space, and gradient descent follows it. Because the loss L serves as a potential function, this field is conservative: the work done along any closed loop is zero, and the integral depends only on endpoints. But real training uses stochastic gradients, not true gradients. The mini-batch gradient is the true gradient plus noise, and this noise component is generally NOT conservative -- it introduces path-dependence. This is why curriculum learning works: the order in which you present training data changes the effective path through parameter space, and for a non-conservative field, different paths lead to different endpoints. Understanding when and how the stochastic component breaks conservativeness helps explain why training details that "shouldn't matter" (data ordering, batch composition) actually affect the final model -- a fact with direct implications for alignment, since it means the training process itself, not just the loss function, shapes what the model learns.
