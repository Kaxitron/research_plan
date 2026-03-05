# Lesson 26: Green's Theorem -- Circulation, Divergence, and Curl (Bazett Ch. 4)

[<- Previous](lesson-25-vector-fields.md) | [Back to TOC](../README.md) | [Next: Surface Integrals ->](lesson-27-surface-integrals.md)

---

## Core Learning

Green's theorem is the first of the "big integral theorems" that connect the behavior of a vector field on the boundary of a region to the behavior of its derivatives in the interior. In its circulation form, it says that the total circulation of a vector field around a closed curve equals the double integral of the scalar curl over the enclosed region. In its flux (divergence) form, it says the total outward flux through a closed curve equals the double integral of the divergence over the interior. Both forms express the same deep principle: boundary behavior encodes interior information.

The scalar curl (dQ/dx - dP/dy) at a point measures the local rotational tendency of the field -- how much the field "swirls" around that point. The divergence (dP/dx + dQ/dy) measures the local expansion or compression -- whether the field is "spreading out" (source) or "pulling in" (sink) at that point. Green's theorem says you can compute the total rotation or total flux by either walking around the boundary or summing up the local contributions inside. This is a 2D version of the more general integral theorems (Stokes' and Divergence) that you will see in later lessons.

The Laplacian, defined as div(grad f) = nabla^2 f, combines both operations and measures how much f at a point deviates from the average of its neighbors. It is the engine behind the heat equation (u_t = k nabla^2 u), which describes diffusion -- and diffusion is exactly the forward process in diffusion models, one of the most successful families of generative models in modern ML.

- Scalar curl in 2D: (dQ/dx - dP/dy) as circulation density
- Green's theorem (circulation form): line integral of F around boundary = double integral of curl over interior
- Divergence of a 2D vector field: dP/dx + dQ/dy
- Green's theorem (flux/divergence form): flux through boundary = double integral of divergence over interior
- The Laplacian: nabla^2 f = div(grad f) = sum of unmixed second partials
- Harmonic functions: nabla^2 f = 0 (value at center = average over surrounding circle)
- Applications: area computation via Green's theorem, fluid flow, electrostatics

## Watch -- Primary

- **Trefor Bazett -- Vector Calculus, Chapter 4 videos**
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxfW0GMqeUE1bLKaYor6kbHa
  - *Bazett covers both forms of Green's theorem with clear geometric motivation. Pay attention to how he distinguishes circulation from flux.*

## Watch -- Secondary

- **3Blue1Brown -- "Divergence and curl"**
  - https://www.youtube.com/watch?v=rB83DpBJQsE
  - *Excellent visual intuition for divergence and curl as local properties of vector fields.*

## Read

- **Bazett's Vector Calculus textbook, Chapter 4** -- Green's theorem in both forms, applications
- **Paul's Online Math Notes -- Green's Theorem**
  - https://tutorial.math.lamar.edu/Classes/CalcIII/GreensTheorem.aspx

## Key Equations

**Green's theorem (circulation form):**

$$\oint_C P \, dx + Q \, dy = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA$$

**Green's theorem (flux form):**

$$\oint_C \mathbf{F} \cdot \mathbf{n} \, ds = \iint_D \left( \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} \right) dA$$

**Laplacian:**

$$\nabla^2 f = \text{div}(\nabla f) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}$$

## ML & Alignment Connection

Divergence measures whether a vector field is "spreading out" or "compressing" -- this is the infinitesimal version of volume change, and volume change is exactly what normalizing flows need to track. The change-of-variables formula for probability densities involves the Jacobian determinant, which measures finite volume change; divergence gives the differential version. Specifically, for continuous normalizing flows, the instantaneous change in log-density is d(log p)/dt = -tr(df/dx), which is the negative divergence of the velocity field. The Laplacian appears directly in the heat equation u_t = k nabla^2 u, which IS the forward process in diffusion models: adding Gaussian noise to data is mathematically equivalent to running the heat equation. Understanding Green's theorem -- the connection between boundary integrals and interior derivatives -- builds toward the divergence theorem, which is the mathematical backbone of probability conservation in these generative models.
