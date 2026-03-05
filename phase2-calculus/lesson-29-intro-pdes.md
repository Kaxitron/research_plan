# Lesson 29: Introduction to PDEs -- Classification and the Heat Equation

[<- Previous](lesson-28-stokes-divergence.md) | [Back to TOC](../README.md) | [Next: Separation of Variables and Fourier Series ->](lesson-30-separation-fourier.md)

---

Partial differential equations extend the ODE framework from Phase 2 Block B to functions of multiple independent variables. Where an ODE describes how a single quantity evolves in time, a PDE describes how entire fields -- temperature distributions, probability densities, electromagnetic potentials -- evolve across both space and time. The classification of PDEs into elliptic, parabolic, and hyperbolic types mirrors a fundamental trichotomy in how information propagates: steady-state equilibrium, diffusive smoothing, and wave-like propagation.

The heat equation is the most important PDE for modern ML. It arises from two physical principles: conservation of energy and Fourier's law of heat conduction (flux proportional to the negative temperature gradient). The resulting equation, a parabolic PDE, describes how an initial temperature distribution smooths toward equilibrium. Boundary conditions -- what happens at the edges of the domain -- determine the family of possible solutions and play a role analogous to conditioning in generative models.

This lesson establishes the vocabulary and classification system you will use for every PDE encountered in this curriculum. Understanding how boundary conditions constrain solutions is essential: in diffusion models, the "boundary conditions" of the generative process are precisely what allow text prompts and other conditioning signals to guide generation.

## Core Learning

- PDEs involve partial derivatives with respect to multiple independent variables (typically space and time)
- Classification of second-order linear PDEs via the discriminant of Auxx + 2Buxy + Cuyy + ... = 0: elliptic (B^2 - AC < 0), parabolic (B^2 - AC = 0), hyperbolic (B^2 - AC > 0)
- Elliptic PDEs (e.g., Laplace) describe steady-state/equilibrium; parabolic PDEs (e.g., heat) describe diffusion; hyperbolic PDEs (e.g., wave) describe propagation
- Heat equation derivation: conservation of energy + Fourier's law yields du/dt = alpha * nabla^2 u
- The Laplacian nabla^2 u measures how much u at a point deviates from the average of its neighbors -- diffusion pushes toward local averages
- Boundary conditions: Dirichlet (prescribe u on boundary), Neumann (prescribe normal derivative on boundary), Robin (linear combination of both)
- Steady-state solutions satisfy nabla^2 u = 0 (Laplace's equation) -- the time derivative vanishes when the system reaches equilibrium
- Well-posedness (Hadamard): existence, uniqueness, and continuous dependence on data

## Watch -- Primary

- **Jason Bramburger -- PDEs Course** (Introduction and Heat Equation sections)
  - https://www.youtube.com/@jasonbramburger
  - *Covers PDE classification, derivation of the heat equation, and boundary conditions.*

## Watch -- Secondary

- **3Blue1Brown -- "But what is a partial differential equation?"**
  - https://www.youtube.com/watch?v=ly4S0oi3Yz8
  - *Beautiful visual intuition for the heat equation and how Fourier modes decay at different rates.*

## Read

- **Bramburger course notes** (if available) or Haberman, *Applied Partial Differential Equations*, Ch. 1-2
- **Strauss, *Partial Differential Equations: An Introduction***, Ch. 1: classification and the heat equation

## Key Equations

**Heat equation (general):**
$$\frac{\partial u}{\partial t} = \alpha \nabla^2 u$$

**Heat equation (1D):**
$$\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$$

**PDE classification** for $Au_{xx} + 2Bu_{xy} + Cu_{yy} + \ldots = 0$:
- Elliptic: $B^2 - AC < 0$
- Parabolic: $B^2 - AC = 0$
- Hyperbolic: $B^2 - AC > 0$

**Boundary conditions:**
- Dirichlet: $u\big|_{\partial\Omega} = g$
- Neumann: $\frac{\partial u}{\partial n}\bigg|_{\partial\Omega} = g$
- Robin: $\alpha u + \beta \frac{\partial u}{\partial n}\bigg|_{\partial\Omega} = g$

**Steady-state** (set $\partial u / \partial t = 0$):
$$\nabla^2 u = 0 \quad \text{(Laplace's equation)}$$

## ML and Alignment Connection

The heat equation IS the forward process in diffusion models (DDPM, Stable Diffusion). Adding Gaussian noise to data is equivalent to solving the heat equation: each denoising step undoes a small amount of diffusion. The thermal diffusivity alpha controls the noise schedule -- how quickly information is destroyed.

Boundary conditions determine what the model can generate. In diffusion models, conditioning signals (text prompts, class labels, image masks) act as boundary conditions that constrain the reverse process. This is why classifier-free guidance works: it modifies the "boundary conditions" of the generative PDE to steer outputs toward prompted content. Understanding how BCs shape solution spaces is directly relevant to controlling and aligning generative model outputs.

The classification of PDEs also matters: parabolic (diffusion) processes lose information over time, while hyperbolic (wave) processes preserve it. This fundamental distinction shows up in neural architecture design -- residual connections preserve information (wave-like), while layers without skip connections can diffuse and lose it (heat-like).
