# Lesson 33: Method of Characteristics, Transport Equations, and PDEs in ML

[<- Previous](lesson-32-helmholtz-laplace.md) | [Back to TOC](../README.md) | [Next: Scalar Derivatives ->](lesson-34-scalar-derivatives.md)

---

This lesson covers the method of characteristics -- a powerful technique for solving first-order PDEs and understanding information propagation in hyperbolic systems -- and then brings the entire PDE block full circle by showing how every equation from Lessons 29-32 converges in the mathematical framework behind diffusion generative models. The method of characteristics converts a PDE into a family of ODEs along curves in the x-t plane. For linear problems, these characteristics are straight lines along which the solution is constant. For nonlinear problems, characteristics can collide, forming shock waves -- discontinuities that require weak solutions and entropy conditions.

The transport equation is the simplest first-order PDE and the foundation for optimal transport theory, which has become a major tool in generative modeling. The Wasserstein distance measures the cost of transporting one probability distribution to another, and it arises naturally from the transport PDE. The lesson culminates with diffusion models, where the forward process is the heat equation, the reverse process requires the score function, and the entire framework connects to Fokker-Planck, SDEs, and the transport equation.

## Core Learning

### Method of Characteristics (Video: L39)

- **The transport equation:** du/dt + c * du/dx = 0 -- the simplest first-order PDE; solution is u(x,t) = u_0(x - ct), meaning the initial profile translates at speed c without distortion
- **Method of characteristics:** convert a PDE into a family of ODEs along characteristic curves; for du/dt + c*du/dx = 0, the characteristics are lines dx/dt = c along which du/dt = 0 (u is constant)
- **General first-order PDE** a(x,t)*u_x + b(x,t)*u_t = c(x,t,u): characteristics are curves (x(s), t(s)) satisfying dx/ds = a, dt/ds = b, and along these curves du/ds = c
- The method reduces a PDE problem to solving a system of ODEs -- each characteristic carries a value of u from the initial data into the interior of the domain
- Works for both linear and quasilinear first-order PDEs

### Characteristics of the Wave Equation (Video: L40)

- The 1D wave equation u_{tt} = c^2*u_{xx} can be rewritten as a system of first-order equations, revealing two families of characteristics: x - ct = const (right-traveling) and x + ct = const (left-traveling)
- d'Alembert's solution u(x,t) = f(x-ct) + g(x+ct) is a direct consequence: the general solution is the sum of functions constant along each family of characteristics
- **Domain of dependence:** the solution u(x_0, t_0) depends only on initial data in the interval [x_0 - ct_0, x_0 + ct_0] -- the "past light cone"
- **Range of influence:** initial data at a point x_0 influences the solution only within the cone |x - x_0| <= ct -- information cannot travel faster than speed c
- This finite propagation speed contrasts sharply with the heat equation, where any perturbation instantly (though exponentially weakly) affects the entire domain

### Boundary Reflections in the Wave Equation (Video: L41)

- When a characteristic reaches a boundary (e.g., a fixed end where u = 0), it reflects: an incoming right-traveling wave reflects as a left-traveling wave with inverted sign (for Dirichlet BCs) or same sign (for Neumann BCs)
- Method of images: extend the domain and initial data by odd reflection (Dirichlet) or even reflection (Neumann) to convert a bounded-domain problem into an infinite-domain problem with d'Alembert's solution
- Multiple reflections create standing wave patterns -- the same standing waves obtained by separation of variables, providing an alternative physical interpretation
- Understanding reflections is essential for wave propagation in bounded media (strings, acoustic cavities, waveguides)

### Modelling Traffic with PDEs (Video: L42)

- **Traffic flow model:** conservation of cars gives rho_t + q_x = 0, where rho(x,t) is car density and q = rho*v(rho) is the flux (density times velocity)
- Velocity depends on density: v(rho) = v_max*(1 - rho/rho_max) -- cars slow down in dense traffic
- This gives a nonlinear first-order PDE: rho_t + f'(rho)*rho_x = 0 where f(rho) = rho*v(rho) is the flux function
- Characteristics now depend on the solution itself: dx/dt = f'(rho) -- different densities propagate at different speeds
- This is the simplest example of a conservation law and serves as a model for more complex nonlinear hyperbolic systems

### Fanlike Characteristics (Video: L43)

- **Rarefaction waves:** when characteristics diverge (fan out), the solution develops a smooth expansion wave connecting two constant states
- For the traffic model: when a traffic light turns green, a rarefaction wave propagates backward as cars accelerate -- the transition from high to low density is smooth and spreads over time
- The fan of characteristics fills the gap smoothly; the solution is found by solving x/t = f'(rho) for rho
- Rarefaction waves are the "easy" case of nonlinear wave interactions -- they always produce smooth, single-valued solutions

### Shock Waves (Video: L44)

- **Shock formation:** when characteristics converge and cross, the solution becomes multi-valued -- physically impossible, so a discontinuity (shock) forms
- For traffic: a sudden slowdown (e.g., an accident) creates converging characteristics and a shock wave of braking that propagates backward through traffic
- **Rankine-Hugoniot condition:** the shock speed s is determined by conservation: s = [f(rho)]_jump / [rho]_jump = (f(rho_R) - f(rho_L)) / (rho_R - rho_L)
- **Entropy condition:** when multiple weak solutions exist, the physically correct one is selected by requiring that characteristics run INTO the shock (not out of it) -- the Lax entropy condition
- Burgers' equation u_t + u*u_x = 0 is the canonical model for shock formation; adding viscosity (u_t + u*u_x = nu*u_{xx}) smooths shocks into thin transition layers

### The Eikonal Equation (Video: L45)

- **Eikonal equation:** |nabla u|^2 = 1/c(x)^2 (or |nabla u| = n(x) in optics), where u(x) represents the travel time of a wavefront and c(x) is the local wave speed
- Arises as the high-frequency limit of the wave equation (geometric optics approximation); also governs shortest-path/distance problems
- Characteristics of the eikonal equation are the rays along which waves propagate -- Snell's law of refraction follows from the eikonal equation with a discontinuous speed function
- Level sets of u (wavefronts) are everywhere perpendicular to the characteristics (rays)
- Connects to the Hamilton-Jacobi equation from classical mechanics and to level set methods in image processing and computational geometry

### PDEs in ML: Diffusion Models, Score Matching, and Numerical Methods (Block D Synthesis)

- **Forward diffusion process:** dx = f(x,t)dt + g(t)dW (an SDE that progressively adds noise to data); common schedules: variance-preserving (VP), variance-exploding (VE), sub-VP
- **Fokker-Planck equation:** dp/dt = -nabla . (f*p) + (1/2) nabla . (g^2 nabla p) describes how the probability density p(x,t) evolves under the forward SDE
- **Score function:** s(x,t) = nabla_x log p_t(x) -- the gradient of log-probability, pointing toward high-density regions
- **Score matching:** train a neural network s_theta(x,t) to approximate the true score by minimizing E[||s_theta - nabla_x log p_t||^2]; denoising score matching makes this tractable
- **Reverse SDE:** dx = [f - g^2 * s(x,t)]dt + g*dW_bar -- requires the learned score to run backward in time
- **Probability flow ODE:** dx/dt = f - (1/2)g^2 * nabla_x log p_t(x) -- a deterministic ODE that generates the same marginal distributions as the reverse SDE; enables exact likelihood computation
- **Connection between score and denoising:** the optimal denoiser at noise level sigma is related to the score by s(x,t) = (D(x,t) - x) / sigma^2
- **Numerical discretization:** Euler-Maruyama for SDEs, predictor-corrector methods, exponential integrators; fewer steps = faster generation but lower quality; DDIM, DPM-Solver, and other advanced samplers use better numerical schemes for the underlying ODE/SDE

## Watch -- Primary

- **Jason Bramburger -- PDEs Course** (Lectures 39-45)
  - https://www.youtube.com/playlist?list=PLXsDp0z6VWFQJ6BY1O6Hz5XX2ppgGvEAu
  - L39: Method of Characteristics
  - L40: Characteristics of the Wave Equation
  - L41: Boundary Reflections in the Wave Equation
  - L42: Modelling Traffic with PDEs
  - L43: Fanlike Characteristics
  - L44: Shock Waves
  - L45: The Eikonal Equation

## Watch -- Secondary

- **Yang Song -- "Score-Based Generative Modeling" lectures/talks**
  - *The creator of score-based diffusion models explains the SDE framework, score matching, and the connection to PDEs. Essential for understanding the full mathematical picture.*

## Read

- **Haberman, *Applied Partial Differential Equations***, Ch. 12: Method of characteristics
- **Evans, *Partial Differential Equations***, Ch. 3: characteristics and conservation laws
- **Yang Song et al., "Score-Based Generative Modeling through Stochastic Differential Equations" (2021)** -- https://arxiv.org/abs/2011.13456
- **Calvin Luo, "Understanding Diffusion Models: A Unified Perspective" (2022)** -- https://arxiv.org/abs/2208.11970

## Key Equations

**Transport equation:**
$$\frac{\partial u}{\partial t} + c \frac{\partial u}{\partial x} = 0$$

**Method of characteristics:**
$$\frac{dx}{dt} = c, \qquad \frac{du}{dt} = 0 \quad \Longrightarrow \quad u(x,t) = u_0(x - ct)$$

**Nonlinear conservation law:**
$$\frac{\partial \rho}{\partial t} + \frac{\partial f(\rho)}{\partial x} = 0$$

**Rankine-Hugoniot shock speed:**
$$s = \frac{f(\rho_R) - f(\rho_L)}{\rho_R - \rho_L}$$

**Burgers' equation:**
$$\frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} = 0$$

**Eikonal equation:**
$$|\nabla u| = \frac{1}{c(x)}$$

**Forward SDE:**
$$dx = f(x,t)\, dt + g(t)\, dW$$

**Score function:**
$$s(x,t) = \nabla_x \log p_t(x)$$

**Reverse SDE:**
$$dx = \big[f(x,t) - g(t)^2\, \nabla_x \log p_t(x)\big]\, dt + g(t)\, d\bar{W}$$

**Fokker-Planck equation:**
$$\frac{\partial p}{\partial t} = -\nabla \cdot (f\, p) + \frac{1}{2} \nabla \cdot \big(g^2 \nabla p\big)$$

**Probability flow ODE:**
$$\frac{dx}{dt} = f(x,t) - \frac{1}{2} g(t)^2\, \nabla_x \log p_t(x)$$

**Denoising score matching objective:**
$$\mathcal{L}(\theta) = \mathbb{E}_{t, x_0, \epsilon}\!\left[\big\| s_\theta(x_t, t) - \nabla_{x_t} \log p(x_t | x_0) \big\|^2\right]$$

## Block D Capstone Project — PDE Solver & Mini Diffusion Model (~4h)

See the full project spec with rendered math and diagrams: [lesson-33-capstone-project.pdf](lesson-33-capstone-project.pdf)

## ML and Alignment Connection

The method of characteristics reveals how information flows through first-order PDEs -- each characteristic carries a piece of the initial data forward in time. This is analogous to mechanistic interpretability: tracing how specific inputs influence specific outputs through the network. Understanding which characteristics carry which information is the PDE version of understanding which pathways in a neural network carry which features.

Shock formation in nonlinear conservation laws -- where smooth solutions develop discontinuities -- is a model for phase transitions in training dynamics. Grokking (sudden generalization after prolonged memorization) and loss spikes during training may be understood as "shocks" in the landscape of model parameters, where different training regimes collide. The entropy condition for selecting the correct weak solution has analogues in implicit regularization: SGD's noise selects the "physically correct" solution among many possibilities.

The transport equation governs how probability distributions flow, connecting directly to optimal transport theory used in generative models. The Wasserstein distance (earth mover's distance) measures the minimal cost of transporting one distribution to another. Flow-matching generative models learn a velocity field that transports a simple prior distribution to the data distribution -- literally solving a transport equation. The eikonal equation connects to level set methods and distance computations used in image segmentation and computational geometry.

Diffusion models -- DALL-E 3, Stable Diffusion, Midjourney, Sora -- are the most successful generative models as of 2024-2026. They work by running the heat equation forward (adding noise) and learning to reverse it (denoising). The score function is what the neural network learns: a vector field pointing toward higher-probability regions of data space. Conditioning (text prompts, safety classifiers) modifies the score function via classifier-free guidance: s(x,t) + w * [s(x,t|c) - s(x,t)]. Understanding this mathematically is essential for building reliable safety filters for generative models and for mechanistic interpretability of what these models "know" about the data distribution.
