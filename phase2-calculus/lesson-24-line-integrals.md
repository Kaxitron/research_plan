# Lesson 24: Line Integrals and Curves (Bazett Ch. 1)

[<- Previous](lesson-23-multiple-integration.md) | [Back to TOC](../README.md) | [Next: Vector Fields ->](lesson-25-vector-fields.md)

---

## Core Learning

Before integrating over vector fields, you need to understand curves themselves. A parametric curve r(t) = (x(t), y(t), z(t)) traces a path through space as t varies over an interval [a, b]. The same geometric curve can have many different parameterizations -- a circle can be traversed at constant speed, accelerating speed, or even backward -- and the choice of parameterization affects how we compute integrals along the curve but not the geometric quantity (like arc length) itself. Understanding when a result depends on parameterization versus when it is intrinsic to the curve is a recurring theme.

A scalar line integral takes a function f defined along a curve and accumulates its values weighted by arc length. Think of it as computing the mass of a wire whose density varies along its length. The key formula integrates f(r(t)) multiplied by the speed factor ||r'(t)||, which accounts for how fast the parameterization moves through space. This speed factor is what makes the result independent of parameterization: if you traverse the curve faster, dt shrinks but ||r'(t)|| grows, and the product ds = ||r'(t)|| dt stays the same.

These ideas are not abstract for ML. Every training run traces a curve through parameter space -- the sequence of weight vectors W(0), W(1), W(2), ... forms a discrete path, and in the continuous-time limit (gradient flow) it becomes a smooth curve W(t). The arc length of this training trajectory measures how far the weights actually travel, which connects to implicit bias: gradient descent tends to find solutions via short paths, and shorter paths correspond to simpler models.

- Parametric curves r(t) = (x(t), y(t), z(t)) on [a, b]
- Tangent vector r'(t) and speed ||r'(t)||
- Reparameterization: same curve, different speed; arc length parameterization (unit speed)
- Arc length as the integral of speed
- Scalar line integrals: accumulating a scalar field along a curve
- Line integrals in 2D and 3D
- Distinguishing types of line integrals: scalar (ds) vs component (dx, dy, dz) — identifying which type you are computing
- Piecewise-smooth curves and how to handle corners

## Watch -- Primary

- **Trefor Bazett -- Vector Calculus, Chapter 1 videos**
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxfW0GMqeUE1bLKaYor6kbHa
  - *Bazett covers parameterizations, arc length, and scalar line integrals with clear visual examples. Work through the Chapter 1 videos in order.*

## Watch -- Secondary

- **3Blue1Brown -- "Essence of Calculus" (review as needed)**
  - https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr
  - *If parameterization feels shaky, revisit the relevant segments on curves and integrals.*

## Read

- **Bazett's Vector Calculus textbook, Chapter 1** -- parametric curves, arc length, scalar line integrals
- **Paul's Online Math Notes -- Line Integrals Part I**
  - https://tutorial.math.lamar.edu/Classes/CalcIII/LineIntegrals.aspx

## Key Equations

**Arc length:**

$$L = \int_a^b \|r'(t)\| \, dt$$

**Scalar line integral:**

$$\int_C f \, ds = \int_a^b f(r(t)) \, \|r'(t)\| \, dt$$

**Speed factor (why parameterization cancels):**

$$ds = \|r'(t)\| \, dt$$

## ML & Alignment Connection

Paths through parameter space during training ARE curves. The arc length of a training trajectory -- how far the weights travel from initialization to convergence -- measures the geometric complexity of the optimization path. Research on the implicit bias of gradient descent shows that among all models fitting the data, gradient descent finds solutions reachable by short paths from initialization. This "short path" preference is a form of implicit regularization: shorter paths correspond to simpler, more generalizable models. Understanding line integrals along training curves also connects to computing quantities like "total gradient norm traveled," which practitioners use to diagnose training health.
