# Exam 2D: Partial Differential Equations — The Language of Diffusion and Dynamics

**The Path to AI Alignment — Lessons 29-33 Comprehensive Assessment**

---

| | |
|---|---|
| **Time Allowed** | 90 minutes |
| **Total Points** | 150 |
| **Materials** | Pencil, paper, calculator (no CAS). No code. |
| **Format** | Part I: Classical PDEs (7 questions, 70 pts) — Part II: PDEs Meet Machine Learning (8 questions, 80 pts) |

> **Advice:** Show all work. For Fourier series questions, set up the integrals and compute at least the first few terms. The integrative thread: **the heat equation IS the forward process of diffusion models, and understanding PDEs gives you the mathematical foundation to understand how noise is added and removed in modern generative AI.**

> *"A partial differential equation is a machine that takes a function and returns a function. The heat equation smooths, the wave equation propagates, and the reverse diffusion equation generates. The same mathematics powers physics simulations and image generation."*

---

# Part I: Classical PDEs (70 points)

*Classification, separation of variables, Fourier series, and the three canonical equations — the foundations that the ML connections build upon.*

---

## Question 1 (10 pts) — PDE Classification and Setup

**(a)** State the general form of a second-order linear PDE in two variables: Au_{xx} + Bu_{xy} + Cu_{yy} + (lower order terms) = 0. The discriminant is B^2 - 4AC. Classify each PDE as elliptic, parabolic, or hyperbolic:

- (i) u_{xx} + u_{yy} = 0
- (ii) u_t = k u_{xx}
- (iii) u_{tt} = c^2 u_{xx}
- (iv) u_{xx} + 4u_{xy} + 4u_{yy} = 0

**(b)** For each classification (elliptic, parabolic, hyperbolic), name the canonical example PDE and describe its physical meaning in one sentence.

**(c)** Explain the three types of boundary conditions:
- Dirichlet: u = g on the boundary
- Neumann: du/dn = g on the boundary
- Robin: au + b(du/dn) = g on the boundary

Give a physical interpretation of each for the heat equation on a rod.

**(d)** In ML, the choice of boundary conditions is analogous to choosing constraints on a model. A neural network with fixed output values at certain points has "Dirichlet" constraints; one with fixed gradients has "Neumann" constraints. Give an example of each in a practical ML context.

---

## Question 2 (12 pts) — The Heat Equation: Derivation and Steady State

Consider a rod of length L = pi with temperature u(x, t).

**(a)** Derive the heat equation u_t = k u_{xx} from Fourier's law (heat flux proportional to negative temperature gradient) and conservation of energy. Show each step.

**(b)** For boundary conditions u(0, t) = 0 and u(pi, t) = 0 (ends held at zero temperature), find the steady-state solution u_ss(x) by setting u_t = 0 and solving the resulting ODE.

**(c)** Now consider u(0, t) = 0 and u(pi, t) = T_0. Find the steady-state solution. Interpret geometrically.

**(d)** If the initial temperature is u(x, 0) = sin(x), and the boundary conditions are u(0, t) = u(pi, t) = 0, guess the solution. *(Hint: try u(x, t) = e^{-kt} sin(x) and verify it satisfies the PDE and all conditions.)*

**(e)** In the solution from (d), what happens as t approaches infinity? Explain physically why the exponential decay rate is k: higher thermal diffusivity means faster smoothing.

---

## Question 3 (10 pts) — Separation of Variables

Solve the heat equation u_t = u_{xx} on [0, pi] with boundary conditions u(0, t) = u(pi, t) = 0 and initial condition u(x, 0) = x(pi - x).

**(a)** Assume u(x, t) = X(x)T(t). Substitute into the PDE and separate variables. Show that you obtain X'' + lambda X = 0 and T' + lambda T = 0 for some separation constant lambda.

**(b)** Apply the boundary conditions to X. Show that the eigenvalues are lambda_n = n^2 and the eigenfunctions are X_n(x) = sin(nx) for n = 1, 2, 3, ...

**(c)** Solve the T equation for each n: T_n(t) = ?

**(d)** Write the general solution as a superposition: u(x, t) = sum of b_n T_n(t) X_n(x). Determine the Fourier sine coefficients b_n from the initial condition u(x, 0) = x(pi - x) by computing b_n = (2/pi) integral from 0 to pi of x(pi - x) sin(nx) dx. Compute b_1, b_2, and b_3. *(Hint: b_n = 0 for even n.)*

**(e)** What is the physical significance of the fact that higher-frequency modes (larger n) decay as e^{-n^2 t}, much faster than the fundamental mode e^{-t}? Relate to smoothing and low-pass filtering.

---

## Question 4 (10 pts) — Fourier Series

**(a)** Write the Fourier sine series for f(x) = 1 on [0, pi]. Compute the first four nonzero coefficients.

**(b)** The Fourier series converges to f(x) at every point of continuity. At the endpoints (where f has a jump discontinuity in the odd extension), what value does the series converge to?

**(c)** Explain the Gibbs phenomenon in 2-3 sentences: even as you add more terms, the Fourier series overshoots near discontinuities by approximately 9%. Why doesn't this violate convergence?

**(d)** Parseval's theorem states that the integral of f(x)^2 equals the sum of the squares of the Fourier coefficients (up to normalization). State the theorem precisely for Fourier sine series. Use it with f(x) = x on [0, pi] to derive the value of sum of 1/n^2 for n = 1 to infinity.

**(e)** Fourier analysis decomposes a signal into frequencies. In ML, spectral methods decompose functions on graphs into eigenvector components. In one sentence, explain the analogy: sine functions are to intervals as eigenvectors of the graph Laplacian are to graphs.

---

## Question 5 (8 pts) — Sturm-Liouville Theory

**(a)** A Sturm-Liouville problem has the form: d/dx[p(x) y'] + q(x) y + lambda w(x) y = 0 with boundary conditions. State the three key properties of Sturm-Liouville eigenvalue problems (real eigenvalues, orthogonal eigenfunctions, completeness).

**(b)** Show that the problem X'' + lambda X = 0 with X(0) = X(pi) = 0 is a Sturm-Liouville problem by identifying p(x), q(x), and w(x).

**(c)** Verify orthogonality directly: compute the integral from 0 to pi of sin(mx) sin(nx) dx for m not equal to n.

**(d)** Why is completeness crucial for separation of variables? In 2-3 sentences, explain what goes wrong if the eigenfunctions do NOT form a complete set.

---

## Question 6 (10 pts) — The Wave Equation

Consider u_{tt} = c^2 u_{xx} on [0, pi] with u(0, t) = u(pi, t) = 0.

**(a)** Using separation of variables, derive the general solution: u(x, t) = sum of [a_n cos(nct) + b_n sin(nct)] sin(nx).

**(b)** If the initial conditions are u(x, 0) = sin(2x) and u_t(x, 0) = 0, find the solution.

**(c)** D'Alembert's solution for the wave equation on the real line is u(x, t) = (1/2)[f(x - ct) + f(x + ct)]. Explain what f(x - ct) and f(x + ct) represent physically. What are the characteristic lines?

**(d)** Contrast the heat equation and wave equation: one smooths initial data and the other preserves it. Explain this difference in terms of (i) finite vs. infinite propagation speed, (ii) energy dissipation vs. energy conservation, (iii) behavior of discontinuities.

**(e)** A signal propagating through a neural network layer by layer is more like a wave (each layer transforms and passes forward) than like heat (which averages). In 1-2 sentences, explain why understanding the wave equation's characteristic lines gives insight into how information flows through deep networks — and how this relates to the concept of "receptive field" in CNNs.

---

## Question 7 (10 pts) — Laplace's Equation and the Helmholtz Equation

**(a)** Laplace's equation nabla^2 u = 0 is the steady-state of the heat equation. Solve it on the unit disk using separation of variables in polar coordinates: u(r, theta) = R(r) Theta(theta). Show that the solution involves r^n and trig functions.

**(b)** The Poisson kernel gives the solution to Laplace's equation on the disk in terms of boundary values. State the mean value property: the value at the center of a disk equals the average of the values on the boundary. Explain why this makes physical sense for steady-state temperature.

**(c)** The Helmholtz equation is nabla^2 u + k^2 u = 0. It arises from assuming time-harmonic solutions to the wave equation: u(x, t) = U(x) e^{i omega t}. Show how substituting this into the wave equation gives the Helmholtz equation and identify k in terms of omega and c.

**(d)** The transport equation u_t + c u_x = 0 has solution u(x, t) = f(x - ct) for initial condition u(x, 0) = f(x). Verify this by substitution. Explain: this PDE just "moves" the initial profile at speed c. Relate to the method of characteristics.

---

# Part II: PDEs Meet Machine Learning (80 points)

*From the classical equations to their modern incarnation: the mathematical foundation of diffusion models, score matching, and neural PDE solvers.*

---

## Question 8 (10 pts) — The Heat Equation as Forward Diffusion

**(a)** The forward process in a diffusion model is dx = -beta(t)/2 x dt + sqrt(beta(t)) dW_t. This is a stochastic differential equation. Identify the drift term and the diffusion (noise) term. What does each do to the data distribution?

**(b)** For constant beta, the marginal distribution at time t is x_t | x_0 ~ N(alpha_t x_0, sigma_t^2 I) where alpha_t = e^{-beta t/2} and sigma_t^2 = 1 - e^{-beta t}. Verify that as t approaches infinity, x_t approaches N(0, I) regardless of x_0. Why is this desirable?

**(c)** The probability density p(x, t) of the forward process satisfies the Fokker-Planck equation: dp/dt = div(beta/2 x p) + beta/2 nabla^2 p. Identify the advection term and the diffusion term. When beta = 0, this reduces to what? When the drift is zero, this reduces to what?

**(d)** Explain in 2-3 sentences why "adding Gaussian noise to data = running the heat equation on the data distribution." Be precise about what function is being "heated" — it is the probability density p(x), not the data points themselves.

---

## Question 9 (10 pts) — The Score Function

**(a)** Define the score function: s(x, t) = nabla_x log p(x, t). For a Gaussian p(x) = N(mu, sigma^2 I), compute the score explicitly. What direction does the score point?

**(b)** The score satisfies a PDE derived from the Fokker-Planck equation. For the pure heat equation dp/dt = D nabla^2 p, show that the score s = nabla log p satisfies: ds/dt = D nabla^2 s + D nabla(||s||^2). *(Hint: take the gradient of log on both sides of the Fokker-Planck equation, using the identity nabla log p = nabla p / p.)*

**(c)** Score matching trains a neural network s_theta(x, t) to approximate the true score. The denoising score matching loss is: L = E_{t, x_0, epsilon} [||s_theta(x_t, t) - (-epsilon / sigma_t)||^2] where x_t = alpha_t x_0 + sigma_t epsilon, epsilon ~ N(0, I). Explain in 2-3 sentences why the target -epsilon/sigma_t is the score of the noisy distribution q(x_t | x_0). *(Hint: what is nabla_{x_t} log q(x_t | x_0) for a Gaussian?)*

**(d)** Why can't we compute the true score nabla_x log p(x, t) directly? What would we need to know that we don't have access to?

---

## Question 10 (12 pts) — Reverse SDEs and Generation

**(a)** Anderson's theorem (1982) states that the reverse-time SDE corresponding to dx = f(x, t) dt + g(t) dW_t is: dx = [f(x, t) - g(t)^2 nabla_x log p(x, t)] dt + g(t) dW_t (reversed time). For the forward process in Q8 (f = -beta/2 x, g = sqrt(beta)), write the reverse SDE explicitly.

**(b)** The reverse SDE requires knowing the score nabla_x log p(x, t) at every noise level. This is why we train the score network. Once trained, describe the sampling algorithm in 3-4 steps: start from noise, integrate the reverse SDE, end with a sample.

**(c)** Euler-Maruyama discretization of the reverse SDE gives: x_{t-dt} = x_t + [f(x_t, t) - g(t)^2 s_theta(x_t, t)] dt + g(t) sqrt(dt) z, where z ~ N(0, I). This is one step of a diffusion model sampler. Relate this to Euler's method for ODEs — what is the additional stochastic term?

**(d)** The probability flow ODE removes the stochastic term: dx = [f(x, t) - (1/2) g(t)^2 nabla_x log p(x, t)] dt. This is a deterministic ODE that generates the SAME marginal distributions p(x, t) as the SDE. Why is the probability flow ODE useful? Name two advantages over the SDE sampler.

**(e)** The probability flow ODE is a type of neural ODE (from Lesson 18). Explain the connection: in both cases, you integrate an ODE defined by a neural network to transform one distribution into another. What is the base distribution in each case?

---

## Question 11 (10 pts) — Fokker-Planck and Probability Evolution

**(a)** The Fokker-Planck equation for a general diffusion process dx = mu(x) dt + sigma dW_t is: dp/dt = -div(mu p) + (sigma^2 / 2) nabla^2 p. Derive the first term by considering the flux of probability due to the drift mu. *(Use the continuity equation: dp/dt = -div(J) where J = mu p is the probability current.)*

**(b)** For the Ornstein-Uhlenbeck process dx = -theta x dt + sigma dW_t, write the Fokker-Planck equation. Show that the stationary solution (dp/dt = 0) is a Gaussian. Find its mean and variance.

**(c)** The Fokker-Planck equation is a PDE for the evolution of probability density. Compare it with the heat equation: what extra term does Fokker-Planck have, and what does it do physically?

**(d)** In the context of diffusion models, the forward process has a known Fokker-Planck equation (from Q8c). The reverse process also has a Fokker-Planck equation. Explain why knowing the score at all times is equivalent to knowing the full Fokker-Planck dynamics — and therefore the full time-evolution of the probability density.

---

## Question 12 (8 pts) — Finite Differences and Numerical PDE Solving

**(a)** Approximate u_{xx} using the centered difference formula: u_{xx}(x_i) approximately equals [u(x_{i+1}) - 2u(x_i) + u(x_{i-1})] / (dx)^2. Derive this by adding the Taylor expansions of u(x + dx) and u(x - dx).

**(b)** For the heat equation u_t = u_{xx}, the forward Euler time-stepping scheme is: u_i^{n+1} = u_i^n + (dt/dx^2)[u_{i+1}^n - 2u_i^n + u_{i-1}^n]. This scheme is stable only when dt/dx^2 <= 1/2. Explain intuitively why taking too large a time step causes instability. *(Connect to the learning rate stability condition from Exam 2B.)*

**(c)** The Crank-Nicolson scheme averages forward and backward Euler: u_i^{n+1} = u_i^n + (dt/2dx^2)[(u_{i+1}^{n+1} - 2u_i^{n+1} + u_{i-1}^{n+1}) + (u_{i+1}^n - 2u_i^n + u_{i-1}^n)]. This is unconditionally stable. What is the tradeoff? *(Hint: you must solve a linear system at each time step.)*

**(d)** Neural PDE solvers (like Fourier Neural Operators) learn to map initial conditions to solutions without time-stepping. State one advantage over traditional finite differences and one potential risk.

---

## Question 13 (10 pts) — The Method of Characteristics

**(a)** Solve the transport equation u_t + 2u_x = 0 with initial condition u(x, 0) = e^{-x^2} using the method of characteristics. What are the characteristic curves? Sketch a few of them in the (x, t) plane.

**(b)** Solve the equation u_t + u u_x = 0 (Burgers' equation, inviscid) with initial condition u(x, 0) = 1 - x for 0 <= x <= 1. Find the characteristic curves. At what time do they first cross? *(This crossing is called shock formation.)*

**(c)** Explain in 2-3 sentences why characteristic lines crossing corresponds to the development of a discontinuity (shock) in the solution. What goes wrong with the classical solution at that point?

**(d)** In ML, the "neural transport equation" describes how a normalizing flow moves probability density. If the flow velocity depends on the density itself (as in Burgers'), the flow can develop "shocks" — abrupt changes in the mapping. Relate this to mode collapse in generative models: what happens when many input points map to the same output region?

---

## Question 14 (10 pts) — Diffusion Models: The Full Picture

**(a)** Summarize the complete diffusion model pipeline by filling in the blanks:

- Forward process: gradually add ___ to data over T steps, transforming p_data into approximately ___
- Forward PDE: the density evolves according to the ___ equation
- Training: learn a neural network s_theta that approximates the ___ at each noise level
- Reverse process: starting from ___, integrate the reverse ___ using the learned score
- Alternative: use the probability flow ___ for deterministic sampling
- Output: a sample from approximately ___

**(b)** The noise schedule beta(t) controls how fast noise is added. A linear schedule adds noise uniformly; a cosine schedule adds noise slowly at first and quickly later. Explain in 2-3 sentences why the noise schedule matters for sample quality. *(Hint: think about how many "useful" denoising steps there are.)*

**(c)** DDPM (Denoising Diffusion Probabilistic Models) discretizes the reverse process into T steps. DDIM (Denoising Diffusion Implicit Models) uses the probability flow ODE and can skip steps. Explain why DDIM can use fewer steps than DDPM while producing comparable samples. What mathematical property of ODEs vs. SDEs makes this possible?

**(d)** Classifier-free guidance modifies the score: s_guided = s_unconditional + w (s_conditional - s_unconditional). This amplifies the conditional signal by factor w. Relate this to the temperature parameter in the Boltzmann distribution p ~ exp(-E/T): what does increasing w do to the "sharpness" of the conditional distribution?

---

## Question 15 (10 pts) — Synthesis: PDEs as the Mathematics of Generation

**(a)** The three canonical PDEs each have an ML analog. Fill in the connections:

| PDE | Physics | ML Analog |
|-----|---------|-----------|
| Heat equation u_t = k nabla^2 u | Diffusion of heat | ___ |
| Wave equation u_{tt} = c^2 nabla^2 u | Propagation of waves | ___ |
| Laplace's equation nabla^2 u = 0 | Steady-state equilibrium | ___ |

**(b)** The hierarchy: ODE -> PDE -> SDE. An ODE describes a single trajectory (one data point's evolution). A PDE describes how a density evolves (the Fokker-Planck equation). An SDE describes a single stochastic trajectory whose statistics are governed by the PDE. In diffusion models, which of these three do you simulate at inference time? Which describes the training objective? Which describes the theoretical analysis?

**(c)** The connection between PDEs and generative models goes beyond diffusion. Flow matching uses the continuity equation dp/dt + div(v p) = 0 directly, choosing v to transport one distribution to another along straight paths. In 2-3 sentences, explain why flow matching is conceptually simpler than score-based diffusion, and what PDE it relies on.

**(d)** A researcher claims: "All generative models are fundamentally about solving PDEs — they transform one distribution into another by evolving a density through a differential equation." Evaluate this claim in 3-4 sentences. Is it true for VAEs? For GANs? For autoregressive models? Where does the analogy break down?

**(e)** Looking back at the trajectory from the heat equation to diffusion models: state one mathematical insight from classical PDE theory that you now see as essential to understanding modern generative AI.

---

## Optional Mini-Project (~45 minutes): Build a 1D Diffusion Model from Scratch

**Implement the forward and reverse diffusion process for a simple 1D distribution, using only the PDE concepts from this exam.**

1. Define a target 1D distribution (e.g., a mixture of two Gaussians: p_data = 0.5 N(-3, 0.5) + 0.5 N(3, 0.5))
2. Implement the forward process: given samples from p_data, add noise according to a linear schedule beta_t for T = 100 steps. Plot the distribution at t = 0, 25, 50, 75, 100. Verify it approaches N(0, 1)
3. Train a simple MLP s_theta(x, t) to predict the score (= -epsilon/sigma_t) using the denoising score matching loss from Q9(c)
4. Implement the reverse SDE sampler: starting from N(0, 1), integrate the reverse SDE using Euler-Maruyama for T steps. Plot the generated samples and compare with the original distribution
5. Implement the probability flow ODE sampler and compare with the SDE sampler: which is more deterministic? Which produces better samples with fewer steps?

**Stretch:** Solve the Fokker-Planck equation numerically using finite differences (Q12) for the same forward process. Compare the PDE solution p(x, t) with the histogram of forward-process samples at each time step. They should match — this verifies that the SDE and PDE descriptions are consistent.

**Tools:** PyTorch (for the score network), NumPy, Matplotlib.
