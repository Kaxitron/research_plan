# Lesson 28: Stokes' Theorem, Divergence Theorem, and the Unified View (Bazett Ch. 7-8)

[<- Previous](lesson-27-surface-integrals.md) | [Back to TOC](../README.md) | [Next: Intro to PDEs ->](lesson-29-intro-pdes.md)

---

## Core Learning

Stokes' theorem and the divergence theorem are the culminating results of vector calculus, and together with the Fundamental Theorem of Calculus and Green's theorem, they form a single unified hierarchy. Stokes' theorem says that the circulation of a vector field around a closed curve equals the flux of its curl through any surface bounded by that curve. The divergence theorem says that the total outward flux of a vector field through a closed surface equals the triple integral of its divergence over the enclosed volume. Both are instances of the same principle: integrating a derivative over a region equals evaluating the original quantity on the boundary.

The 3D curl, nabla x F, is a vector field that measures the local rotational tendency of F around each axis. Unlike the 2D scalar curl from Green's theorem, the 3D curl has both magnitude (how much rotation) and direction (the axis of rotation). Stokes' theorem generalizes Green's circulation form from flat 2D regions to arbitrary surfaces in 3D. The divergence theorem generalizes Green's flux form from 2D regions to 3D volumes. Both reduce to Green's theorem when the surface is flat and the region is planar.

The deepest insight is the unified view. Every major integral theorem in calculus is the same statement: the integral of a derivative over a domain equals the integral of the original over the boundary. The generalized Stokes' theorem, written as integral over the boundary of Omega of omega equals integral over Omega of d-omega, encapsulates all of them: FTC, FTLI, Green's, Stokes', and the divergence theorem. This is not just mathematical elegance -- it is the reason why boundary behavior constrains interior behavior, a principle that resonates throughout physics and, as we will see, throughout the theory of probability flows in generative models.

- 3D curl: nabla x F as a vector measuring local rotation
- Stokes' theorem: circulation around boundary = flux of curl through surface
- Divergence theorem: flux through closed surface = integral of divergence over volume
- Gauss' Law as a consequence of the divergence theorem
- Regions with multiple boundary components (e.g., a shell with inner and outer surfaces)
- The hierarchy: FTC -> FTLI -> Green's -> Stokes' -> Divergence theorem
- Generalized Stokes' theorem: integral of omega over boundary of Omega = integral of d-omega over Omega

## Watch -- Primary

- **Trefor Bazett -- Vector Calculus, Chapter 7-8 videos**
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxfW0GMqeUE1bLKaYor6kbHa
  - *Bazett builds from Stokes' theorem through the divergence theorem to the unified picture. His final summary video connecting all the theorems is particularly valuable.*

## Watch -- Secondary

- **3Blue1Brown -- "But what is a curl?"**
  - Covers the geometric meaning of 3D curl with the characteristic 3B1B visual style.
- **Khan Academy -- Stokes' theorem and the divergence theorem**
  - https://www.khanacademy.org/math/multivariable-calculus/greens-theorem-and-stokes-theorem
  - *Worked examples and step-by-step computations for both theorems.*

## Read

- **Bazett's Vector Calculus textbook, Chapters 7-8** -- Stokes' theorem, divergence theorem, unified view
- **Paul's Online Math Notes -- Stokes' Theorem and Divergence Theorem**
  - https://tutorial.math.lamar.edu/Classes/CalcIII/StokesTheorem.aspx
  - https://tutorial.math.lamar.edu/Classes/CalcIII/DivergenceTheorem.aspx

## Key Equations

**Stokes' theorem:**

$$\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}$$

**Divergence theorem:**

$$\oiint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_E (\nabla \cdot \mathbf{F}) \, dV$$

**Generalized Stokes' theorem (the unified view):**

$$\int_{\partial \Omega} \omega = \int_{\Omega} d\omega$$

**3D curl:**

$$\nabla \times \mathbf{F} = \left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \right) \mathbf{i} + \left( \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} \right) \mathbf{j} + \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) \mathbf{k}$$

## Block C Capstone Project — Vector Calculus Theorem Verifier (3h)

**C++ Component (~1h):**
1. Implement numerical line integral, surface integral, and volume integral routines in C++ using quadrature rules
2. Output computed values to CSV for verification against Python implementations

**Python Component (~2h):**
3. Verify Green's theorem (both circulation and flux forms) on specific 2D vector fields — compute both sides independently and confirm equality
4. Verify Stokes' theorem: compute the circulation around a curve and the flux of curl through the bounded surface. Verify the divergence theorem on the unit cube
5. Visualize 2D and 3D vector fields with matplotlib showing curl, divergence, and gradient fields. Create a diagram showing the unified hierarchy: FTC → FTLI → Green's → Stokes' → Divergence theorem

## ML & Alignment Connection

The unified view (generalized Stokes' theorem) is one of the deepest results in mathematics: boundary behavior determines interior behavior, and vice versa. In ML, this principle echoes in multiple ways. Test set performance (a "boundary" measurement) constrains what the model has learned internally. The divergence theorem connects directly to probability flow: if probability is conserved (as it must be for a valid probability distribution evolving over time), then the total flux through any closed boundary must equal the rate of change of probability inside. This is the continuity equation, and it is the mathematical foundation of the Fokker-Planck equation that governs how probability distributions evolve under stochastic dynamics -- including the dynamics of SGD over weight space. For diffusion models, the forward process (adding noise) and reverse process (denoising) both obey this conservation law, and the divergence theorem is what ensures that probability is neither created nor destroyed as data flows through the generative process. Understanding these integral theorems is understanding the plumbing of modern generative AI.
