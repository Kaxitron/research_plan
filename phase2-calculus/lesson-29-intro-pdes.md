# Lesson 29: Heat Equation, Separation of Variables, and Laplace's Equation

[<- Previous](lesson-28-stokes-divergence.md) | [Back to TOC](../README.md) | [Next: Fourier Series and the Wave Equation ->](lesson-30-separation-fourier.md)

---

Partial differential equations extend the ODE framework from Phase 2 Block B to functions of multiple independent variables. Where an ODE describes how a single quantity evolves in time, a PDE describes how entire fields -- temperature distributions, probability densities, electromagnetic potentials -- evolve across both space and time. The classification of PDEs into elliptic, parabolic, and hyperbolic types mirrors a fundamental trichotomy in how information propagates: steady-state equilibrium, diffusive smoothing, and wave-like propagation.

This lesson covers the first three major topic groups in the PDE course: the heat equation and its properties, the method of separation of variables applied to different boundary conditions, and Laplace's equation on various domains. The heat equation is the most important PDE for modern ML -- it arises from conservation of energy and Fourier's law, and its forward process IS the noise-addition step in diffusion models. Separation of variables is the fundamental analytical technique that reduces a PDE to a pair of ODEs. Laplace's equation describes steady-state phenomena -- the endpoint of heat diffusion, the electric potential in a charge-free region -- and its solutions (harmonic functions) have remarkable properties that connect directly to regularization in ML.

## Core Learning

### PDE Classification and the Heat Equation (Videos: Intro, L1-L5)

- PDEs involve partial derivatives with respect to multiple independent variables (typically space and time)
- Classification of second-order linear PDEs via the discriminant of Au_{xx} + 2Bu_{xy} + Cu_{yy} + ... = 0: elliptic (B^2 - AC < 0), parabolic (B^2 - AC = 0), hyperbolic (B^2 - AC > 0)
- Elliptic PDEs (e.g., Laplace) describe steady-state/equilibrium; parabolic PDEs (e.g., heat) describe diffusion; hyperbolic PDEs (e.g., wave) describe propagation
- **Derivation of the heat equation:** conservation of energy + Fourier's law (flux proportional to negative temperature gradient) yields du/dt = alpha * nabla^2 u
- The Laplacian nabla^2 u measures how much u at a point deviates from the average of its neighbors -- diffusion pushes toward local averages
- **Boundary conditions of the heat equation:** Dirichlet (prescribe u on boundary), Neumann (prescribe normal derivative / heat flux on boundary), Robin (linear combination of both), Periodic (u and derivatives match at opposite ends)
- Well-posedness depends on matching the right boundary conditions to the PDE type
- **Equilibrium temperature distributions:** steady-state solutions satisfy nabla^2 u = 0 (Laplace's equation) -- the time derivative vanishes when the system reaches equilibrium; for 1D with Dirichlet BCs, the equilibrium is a linear interpolation between boundary values; for nonhomogeneous BCs, solve Laplace's equation directly
- **The heat equation in higher dimensions:** u_t = alpha * (u_{xx} + u_{yy}) in 2D, u_t = alpha * (u_{xx} + u_{yy} + u_{zz}) in 3D; the Laplacian generalizes to multiple spatial dimensions; separation of variables extends naturally but yields multiple spatial eigenvalue problems
- **Linearity of the heat equation:** the heat equation is linear -- if u_1 and u_2 are solutions, then c_1*u_1 + c_2*u_2 is also a solution; this superposition principle allows building complex solutions from simple ones; linearity is what makes Fourier series solutions possible
- Well-posedness (Hadamard): existence, uniqueness, and continuous dependence on data

### Separation of Variables (Videos: L6-L8)

- **Separation of variables technique:** assume u(x,t) = X(x)T(t), substitute into the PDE, separate variables to get two ODEs linked by a separation constant (eigenvalue)
- For the heat equation: T'(t) = -alpha * lambda * T(t) and X''(x) = -lambda * X(x), where lambda is the separation constant
- **Separation of Variables I -- Dirichlet boundaries:** X(0) = X(L) = 0 selects eigenvalues lambda_n = (n*pi/L)^2 and eigenfunctions X_n(x) = sin(n*pi*x/L); each temporal mode decays as T_n(t) = exp(-alpha * lambda_n * t); general solution is u(x,t) = sum b_n * sin(n*pi*x/L) * exp(-alpha*(n*pi/L)^2*t)
- **Separation of Variables II -- Neumann boundaries:** X'(0) = X'(L) = 0 (insulated ends / zero heat flux) selects eigenfunctions X_n(x) = cos(n*pi*x/L) with eigenvalues lambda_n = (n*pi/L)^2; includes the lambda_0 = 0 mode (constant), reflecting that with insulated boundaries, temperature approaches a uniform equilibrium (the average of the initial condition)
- **Separation of Variables III -- Periodic boundaries:** u(0,t) = u(L,t) and u_x(0,t) = u_x(L,t); eigenfunctions are both sin(2*n*pi*x/L) and cos(2*n*pi*x/L) with eigenvalues lambda_n = (2*n*pi/L)^2; this is the natural setting for Fourier series on a circle; arises in problems with no physical boundary (e.g., temperature around a ring)

### Laplace's Equation (Videos: L9-L12)

- **Laplace's equation on a rectangle:** nabla^2 u = 0 on a rectangular domain; solved by separation of variables u(x,y) = X(x)Y(y); homogeneous BCs on three sides reduce to an eigenvalue problem in one direction and hyperbolic functions in the other; for nonhomogeneous BCs on multiple sides, use superposition -- solve four subproblems, each with one nonhomogeneous side
- **Laplace's equation on a disc:** use polar coordinates (r, theta); separation u(r,theta) = R(r)*Theta(theta) yields Euler-Cauchy equation for R and eigenvalue problem for Theta; solutions involve r^n*cos(n*theta) and r^n*sin(n*theta); the Poisson integral formula gives the solution directly from boundary data g(theta)
- **Fluid flow outside a cylinder:** Laplace's equation in the exterior of a disc; boundary conditions at the cylinder surface and at infinity; solutions involve r^{-n} terms (decaying away from the boundary) rather than r^n terms; demonstrates how the same PDE with different domain geometry produces qualitatively different solutions
- **Qualitative properties of Laplace's equation:** harmonic functions (solutions to nabla^2 u = 0) satisfy the mean value property -- the value at any interior point equals the average over any surrounding circle/sphere; the maximum principle -- harmonic functions attain their maximum and minimum only on the boundary, never in the interior (unless constant); uniqueness of solutions to the Dirichlet problem follows from the maximum principle

## Watch -- Primary

- **Jason Bramburger -- PDEs Course** (Videos: Intro, Lectures 1-12)
  - https://www.youtube.com/playlist?list=PLXsDp0z6VWFQJ6BY1O6Hz5XX2ppgGvEAu
  - Intro: Welcome
  - L1: Derivation of the Heat Equation
  - L2: Boundary Conditions of the Heat Equation
  - L3: Equilibrium Temperature Distributions
  - L4: The Heat Equation in Higher Dimensions
  - L5: Linearity of the Heat Equation
  - L6: Separation of Variables I: Dirichlet Boundaries
  - L7: Separation of Variables II: Neumann Boundaries
  - L8: Separation of Variables III: Periodic Boundaries
  - L9: Laplace's Equation on a Rectangle
  - L10: Laplace's Equation on a Disc
  - L11: Fluid Flow Outside a Cylinder
  - L12: Qualitative Properties of Laplace's Equation

## Watch -- Secondary

- **3Blue1Brown -- "But what is a partial differential equation?"**
  - https://www.youtube.com/watch?v=ly4S0oi3Yz8
  - *Beautiful visual intuition for the heat equation and how Fourier modes decay at different rates.*

## Read

- **Haberman, *Applied Partial Differential Equations***, Ch. 1-2: heat equation derivation, boundary conditions, equilibrium, separation of variables, Laplace's equation
- **Strauss, *Partial Differential Equations: An Introduction***, Ch. 1: classification and the heat equation

## Key Equations

**Heat equation (1D):**
$$\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$$

**Heat equation (general):**
$$\frac{\partial u}{\partial t} = \alpha \nabla^2 u$$

**PDE classification** for $Au_{xx} + 2Bu_{xy} + Cu_{yy} + \ldots = 0$:
- Elliptic: $B^2 - AC < 0$
- Parabolic: $B^2 - AC = 0$
- Hyperbolic: $B^2 - AC > 0$

**Boundary conditions:**
- Dirichlet: $u\big|_{\partial\Omega} = g$
- Neumann: $\frac{\partial u}{\partial n}\bigg|_{\partial\Omega} = g$
- Robin: $\alpha u + \beta \frac{\partial u}{\partial n}\bigg|_{\partial\Omega} = g$

**Separation of variables (heat equation, Dirichlet BCs on [0, L]):**
$$u(x,t) = \sum_{n=1}^{\infty} b_n \sin\!\left(\frac{n\pi x}{L}\right) e^{-\alpha (n\pi/L)^2 t}$$

**Separation of variables (heat equation, Neumann BCs on [0, L]):**
$$u(x,t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos\!\left(\frac{n\pi x}{L}\right) e^{-\alpha (n\pi/L)^2 t}$$

**Laplace's equation:**
$$\nabla^2 u = 0$$

**Poisson integral formula** (disk of radius $R$):
$$u(r, \theta) = \frac{1}{2\pi} \int_0^{2\pi} \frac{R^2 - r^2}{R^2 - 2Rr\cos(\theta - \phi) + r^2} \, g(\phi) \, d\phi$$

**Mean value property** (harmonic $u$ in 2D):
$$u(x_0, y_0) = \frac{1}{2\pi r} \oint_{|x - x_0| = r} u \, ds$$

## ML and Alignment Connection

The heat equation IS the forward process in diffusion models (DDPM, Stable Diffusion). Adding Gaussian noise to data is equivalent to solving the heat equation: each denoising step undoes a small amount of diffusion. The thermal diffusivity alpha controls the noise schedule -- how quickly information is destroyed. Linearity is what allows the superposition of noise at different scales, which is the foundation of the multi-scale denoising approach used in modern diffusion models.

Boundary conditions determine what the model can generate. In diffusion models, conditioning signals (text prompts, class labels, image masks) act as boundary conditions that constrain the reverse process. This is why classifier-free guidance works: it modifies the "boundary conditions" of the generative PDE to steer outputs toward prompted content.

Laplace's equation describes equilibrium -- the state a system reaches after all transient dynamics have died out. In ML, a converged trained model is analogous to a steady-state solution. The mean value property of harmonic functions connects to the idea that well-generalized models produce predictions that are smooth averages over nearby inputs -- this is precisely what regularization encourages. The maximum principle (extremes only on the boundary) is the mathematical reason why adversarial examples tend to be found at the edges of the data distribution rather than in the interior.

The separation of variables with different boundary conditions (Dirichlet, Neumann, Periodic) previews the different "modes" of information flow in architectures: fixed-value boundaries correspond to hard constraints, zero-flux (Neumann) boundaries model conservation, and periodic boundaries arise in positional encoding schemes.
