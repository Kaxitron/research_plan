# Lesson 77: Helmholtz, Laplace, and Transport Equations

[<- Previous](lesson-76-wave-equation.md) | [Back to TOC](../README.md) | [Next: PDEs in ML ->](lesson-78-pdes-ml.md)

---

This lesson covers three important PDEs that complete the classical toolkit: the Helmholtz equation, Laplace's equation, and the transport (advection) equation. Laplace's equation describes steady-state phenomena -- the endpoint of heat diffusion, the shape of a rubber membrane stretched over a wire frame, the electric potential in a charge-free region. Its solutions, harmonic functions, satisfy the remarkable mean value property: the value at any point equals the average over any surrounding sphere. This property connects directly to the idea that well-regularized ML models produce predictions that are smooth averages over nearby inputs.

The Helmholtz equation adds a frequency term to Laplace's equation and governs vibrating membranes, acoustic resonance, and scattering problems. It also arises when you separate variables in the wave equation and look at the spatial part only. The transport equation is the simplest hyperbolic PDE -- it moves a profile along at constant speed without distortion. Solving it via the method of characteristics introduces a powerful technique that extends to nonlinear conservation laws, where solutions can develop shockwaves (discontinuities).

The transport equation has deep connections to optimal transport theory, which has become a major tool in generative modeling. The Wasserstein distance (earth mover's distance) measures the cost of transporting one probability distribution to another, and it arises naturally from the transport PDE. Understanding how probability distributions flow under transport is essential for modern generative models, particularly flow-based and diffusion-based approaches.

## Core Learning

- Laplace's equation: nabla^2 u = 0; describes steady-state (equilibrium) solutions -- the time-independent limit of the heat equation
- Harmonic functions: solutions to Laplace's equation; satisfy the mean value property (value at center = average over any surrounding sphere/circle)
- Maximum principle: a harmonic function on a closed domain attains its max and min on the boundary, never in the interior (unless constant)
- Dirichlet problem on a disk: solved via Fourier series in polar coordinates, yielding the Poisson integral formula / Poisson kernel
- Helmholtz equation: nabla^2 u + k^2 u = 0; arises from separation of variables in the wave equation (spatial eigenvalue problem)
- Helmholtz eigenmodes are the resonant frequencies of a domain -- the "drum problem" (Can you hear the shape of a drum?)
- Transport equation: du/dt + c * du/dx = 0; the simplest hyperbolic PDE, solution is u(x,t) = u_0(x - ct)
- Method of characteristics: convert a PDE into a family of ODEs along characteristic curves; along dx/dt = c, the solution u is constant
- Nonlinear transport and shockwaves: when characteristics cross, solutions develop discontinuities (shocks) -- requires weak solutions and entropy conditions

## Watch -- Primary

- **Jason Bramburger -- PDEs Course** (Laplace equation, transport equation, method of characteristics sections)
  - https://www.youtube.com/@jasonbramburger
  - *Covers Laplace's equation, harmonic functions, and the method of characteristics for transport.*

## Watch -- Secondary

- **Steve Brunton -- Engineering Mathematics** (Laplace equation and method of characteristics)
  - https://www.youtube.com/c/Eigensteve
  - *Applied perspective on solving these equations with emphasis on physical interpretation.*

## Read

- **Haberman, *Applied Partial Differential Equations***, Ch. 2 (Laplace), Ch. 12 (Method of characteristics)
- **Evans, *Partial Differential Equations***, Ch. 2 and 3 for a more rigorous treatment of the maximum principle and characteristics

## Key Equations

**Laplace's equation:**
$$\nabla^2 u = 0$$

**Mean value property** (harmonic $u$ in 2D):
$$u(x_0, y_0) = \frac{1}{2\pi r} \oint_{|x - x_0| = r} u \, ds$$

**Poisson integral formula** (disk of radius $R$):
$$u(r, \theta) = \frac{1}{2\pi} \int_0^{2\pi} \frac{R^2 - r^2}{R^2 - 2Rr\cos(\theta - \phi) + r^2} \, g(\phi) \, d\phi$$

**Helmholtz equation:**
$$\nabla^2 u + k^2 u = 0$$

**Transport (advection) equation:**
$$\frac{\partial u}{\partial t} + c \frac{\partial u}{\partial x} = 0$$

**Method of characteristics:**
$$\frac{dx}{dt} = c, \qquad \frac{du}{dt} = 0 \quad \Longrightarrow \quad u(x,t) = u_0(x - ct)$$

**Nonlinear transport** (Burgers' equation):
$$\frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} = 0$$

## Do

1. **Laplace solver on a square.** Solve Laplace's equation nabla^2 u = 0 on the unit square [0,1] x [0,1] with boundary conditions: u = 1 on the top edge, u = 0 on the other three edges. Use the finite difference method with a grid of at least 50 x 50 points and iterate (Jacobi or Gauss-Seidel) until convergence. Plot the solution as a heatmap and contour plot.

2. **Mean value property verification.** Using your Laplace solution, pick several interior points and numerically verify the mean value property: the value at the point equals the average over a circle of points surrounding it. Try different radii. Quantify the error (it should be small, limited only by your grid resolution).

3. **Transport equation and characteristics.** Implement the method of characteristics for du/dt + c * du/dx = 0 with a Gaussian initial condition. Plot the characteristic lines in the (x,t) plane and the solution surface. Then implement the nonlinear Burgers' equation du/dt + u * du/dx = 0 with a smooth initial condition and watch characteristics converge until a shock forms. Visualize the moment of shock formation.

## ML and Alignment Connection

Laplace's equation describes equilibrium -- the state a system reaches after all transient dynamics have died out. In ML, a converged trained model is analogous to a steady-state solution: the loss landscape dynamics have settled. Harmonic functions and the mean value property connect to the idea that well-generalized models produce predictions that are smooth averages over nearby inputs -- this is precisely what regularization encourages. The maximum principle (extremes only on the boundary) is the mathematical reason why adversarial examples tend to be found at the edges of the data distribution rather than in the interior.

The transport equation governs how probability distributions flow, connecting directly to optimal transport theory used in generative models. The Wasserstein distance (earth mover's distance) measures the minimal cost of transporting one distribution to another along the transport equation. This metric has become central in ML: Wasserstein GANs use it as a training objective, and flow-matching generative models learn a velocity field that transports a simple prior distribution to the data distribution -- literally solving a transport equation.

For alignment: the method of characteristics shows that information in hyperbolic PDEs travels along specific paths. Understanding which characteristics carry which information is analogous to mechanistic interpretability -- tracing how specific inputs influence specific outputs through the network. Shockwave formation (when characteristics collide) is a model for phase transitions in training dynamics.
