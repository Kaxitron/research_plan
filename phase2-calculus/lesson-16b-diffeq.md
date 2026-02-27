# Lesson 16b: Differential Equations and Dynamical Systems

[← Loss Landscapes](lesson-16-loss-landscapes.md) | [Back to TOC](../README.md) | [Next: Probability →](../phase3-probability/lesson-17-probability.md)

---

> **Why this lesson exists:** Training a neural network is solving a differential equation. Gradient descent with infinitesimal learning rate becomes gradient flow — an ODE in parameter space. Understanding this connection lets you reason about training dynamics: why does the network converge where it does? When do phase transitions happen? Why does training sometimes get stuck? Dynamical systems also underpin neural ODEs, diffusion models, and SLT's analysis of how learning trajectories pass through singularities.

## 🎯 Core Concepts

### ODEs — Functions that Describe Change

- **An ordinary differential equation (ODE)** relates a function to its derivatives: dy/dt = f(y, t). It says "the rate of change of y depends on the current value of y and the current time."
- **The geometric picture:** at every point (y, t) in the plane, the ODE assigns a direction arrow (a slope). The collection of all these arrows is the **vector field.** A solution to the ODE is a curve that follows the arrows everywhere — it's always tangent to the field.
  - **Simple example:** dy/dt = -y. The solution is y(t) = y₀ e^(-t) — exponential decay. Every arrow points toward zero. All solutions converge to the origin. This is a "stable equilibrium."
  - **Another example:** dy/dt = y. The solution is y(t) = y₀ e^(t) — exponential growth. Arrows point away from zero. The origin is an "unstable equilibrium."
- **Systems of ODEs:** when you have multiple interacting quantities (x, y, z...), you get a system: dx/dt = f(x, y), dy/dt = g(x, y). The vector field now lives in higher dimensions. Solutions are trajectories through this space.

### Gradient Flow — Training as a Differential Equation

- **Gradient descent:** θ_{t+1} = θ_t - η ∇L(θ_t). Each step moves the parameters in the direction that decreases loss the fastest, scaled by learning rate η.
- **Gradient flow:** take the limit as η → 0 and steps become continuous. You get the ODE: dθ/dt = -∇L(θ). The parameters flow continuously "downhill" on the loss landscape.
- **Why this matters:** gradient flow is the idealized version of gradient descent. Its mathematical properties (convergence guarantees, invariant manifolds, basin structure) tell you about the qualitative behavior of actual discrete training. When practitioners say "the optimizer finds a basin of attraction," they're speaking the language of dynamical systems.
- **Equilibria of gradient flow** are exactly the critical points of the loss function: ∇L(θ*) = 0. Stable equilibria (where flow converges) are local minima. Unstable equilibria are saddle points or maxima. The "basin of attraction" of a minimum is the set of all initial conditions from which gradient flow converges to that minimum.

### Stability and Phase Portraits

- **Fixed points (equilibria):** where the vector field is zero. The system doesn't change. These are the critical points of the loss function.
- **Stability analysis (linearization):** near a fixed point, approximate the vector field by its linear part (the Jacobian matrix). The eigenvalues of the Jacobian determine stability:
  - All eigenvalues have negative real part → stable (attracting) → local minimum in gradient flow
  - Some eigenvalues positive → unstable (saddle point or maximum)
  - Eigenvalues close to zero → slow dynamics, possible phase transition
- **Phase portrait:** the picture of all solution trajectories in state space. For gradient flow on a loss landscape, the phase portrait shows which initial conditions flow to which minima — the basins of attraction.
- **Bifurcations:** when a parameter changes and the qualitative structure of the phase portrait changes — equilibria appear, disappear, or change stability. In neural network training, hyperparameter changes (learning rate, data distribution) can trigger bifurcations. SLT's phase transitions during training are bifurcation-like events.

### Dynamical Systems Concepts for ML

- **Attractors:** sets toward which trajectories converge. Point attractors (fixed points), limit cycles (periodic orbits), and strange attractors (chaotic). Loss function minima are point attractors of gradient flow.
- **Lyapunov functions:** functions that decrease along trajectories, guaranteeing convergence. For gradient flow, the loss function L itself is a Lyapunov function (its time derivative is -||∇L||² ≤ 0). This is WHY gradient descent decreases the loss — it's not just a heuristic.
- **Invariant manifolds:** surfaces in parameter space that are preserved by the dynamics. If the trajectory starts on the manifold, it stays on it. In neural networks, the weight space symmetries (Lesson 21c) create invariant manifolds — gradient flow respects the symmetry structure.
- **Time scales and slow manifolds:** in high-dimensional systems, some directions change fast and some change slow. The system quickly relaxes onto a "slow manifold" where the interesting dynamics happen. In training, this explains why some features are learned quickly (fast directions of the loss landscape) and others take much longer (slow directions).

### Neural ODEs — Networks as Continuous Dynamics

- **Neural ODE:** instead of discrete layers f₁, f₂, ..., fₙ, model the transformation as a continuous ODE: dh/dt = f(h(t), t; θ). The "depth" becomes continuous. The output is h(T) for some final time T.
- **Advantages:** memory-efficient (don't need to store intermediate activations), adaptive computation (the ODE solver chooses how many function evaluations to use), continuous-depth models.
- **Connection to ResNets:** a residual network computes h_{l+1} = h_l + f_l(h_l). With small step size, this approximates the Euler discretization of dh/dt = f(h, t). ResNets are discrete approximations to neural ODEs.
- **Diffusion models** (DALL-E, Stable Diffusion, etc.) are based on stochastic differential equations (SDEs) — ODEs with added noise. The forward process adds noise (simple SDE), the reverse process removes it (learned reverse SDE). Understanding this requires the language of differential equations.

## 📺 Watch — Primary

1. **3Blue1Brown — "Differential equations, a tourist's guide"**
   - https://www.youtube.com/watch?v=p_di4Zn4wz4
   - *Beautiful visual treatment of ODEs as vector fields. The phase portrait visualizations are exactly the right intuition.*
2. **Steve Brunton — "Dynamical Systems" playlist (first 3-4 videos)**
   - https://www.youtube.com/c/Eigensteve
   - Applied treatment with data science connections. Stability analysis and phase portraits.

## 📺 Watch — Secondary

3. **3Blue1Brown — "But what is a partial differential equation?"**
   - https://www.youtube.com/watch?v=ly4S0oi3Yz8
   - Not directly needed for ML but builds intuition for continuous systems
4. **Yannic Kilcher — "Neural Ordinary Differential Equations" (paper review)**
   - Search YouTube — explains the neural ODE paper with ML context
5. **MIT OCW 18.03 — "First-order ODEs" (first few lectures)**
   - Formal treatment if you want more rigor

## 📖 Read — Primary

- **"Neural Ordinary Differential Equations" by Chen et al. (2018)**
  - https://arxiv.org/abs/1806.07366
  - *The foundational neural ODE paper. Read after understanding the ODE basics.*
- **Steve Brunton's "Data-Driven Science and Engineering" — Chapter 7 (available online)**
  - Applied dynamical systems with a data science perspective

## 📖 Read — Secondary

- **"Nonlinear Dynamics and Chaos" by Steven Strogatz** — Chapters 1-4
  - The classic textbook. Incredibly well-written and visual. Chapters 1-4 cover everything you need for the ML connection.
- **Stanford CS229 — "Optimization and Gradient Descent" notes**
  - https://cs229.stanford.edu/
  - Treats gradient descent from the dynamical systems perspective

## 📖 Read — Going Deep

- **"Gradient Descent Dynamics in the Mean-Field Limit" (recent papers)**
  - The mathematical theory of training dynamics in the infinite-width limit
- **"Deep Learning and Dynamical Systems" (Weinan E)**
  - The research program connecting ResNets to ODEs rigorously

## 🔨 Do

- **Vector field visualization:** write Python code that plots the vector field for simple ODEs: dy/dt = -y, dy/dt = y(1-y) (logistic growth), and the 2D system dx/dt = y, dy/dt = -x (rotation). Overlay solution trajectories.
- **Gradient flow on a simple loss:** create a 2-parameter loss function L(a, b) = (a² + b² - 1)² + ab. Plot the loss surface. Compute the gradient flow ODE. Use scipy.integrate.solve_ivp to trace trajectories from various starting points. See them converge to minima.
- **Euler method vs. true ODE:** implement Euler's method for dy/dt = -y with different step sizes. Show that small step sizes give accurate solutions while large step sizes diverge — this is exactly the learning rate instability problem.
- **ResNet as discrete ODE:** build a simple ResNet (3-4 blocks) and a simple neural ODE on the same task. Compare their behavior and the smoothness of their learned transformations.
- **Key exercise:** consider gradient descent on L(w) = w⁴ - 2w². This loss has two minima (at w = ±1) and a saddle point (at w = 0). Write the gradient flow ODE. Find the fixed points and their stability. Sketch the phase portrait. Identify the basins of attraction for each minimum. Then run discrete gradient descent with various learning rates and initial conditions and compare to the continuous prediction.

## 🔗 ML Connection

- **Gradient descent IS a dynamical system.** The loss function is the potential, the gradient is the force, and the learning rate is the time step. Stability analysis of the Jacobian at critical points tells you whether training will converge or diverge near that point.
- **Learning rate warmup and decay** are dynamical systems interventions: warmup starts with gentle dynamics to avoid divergence; decay reduces the step size to converge to a sharper minimum.
- **Adam and other adaptive optimizers** change the dynamical system by preconditioning the gradient. Adam approximately follows the natural gradient, which is gradient flow on a different (Riemannian) manifold.
- **Neural ODEs** enable diffusion models, continuous normalizing flows, and other architectures where the continuous dynamics perspective is essential.

## 🧠 Alignment Connection

- **Phase transitions in training** (sudden emergence of capabilities) correspond to the training trajectory passing through a bifurcation or singularity in the loss landscape. SLT analyzes this using the dynamical systems framework: the RLCT determines the geometry near singularities, which determines the qualitative behavior of gradient flow nearby.
- **Training instabilities** — when models suddenly develop unwanted behaviors during fine-tuning — can be understood as the training trajectory entering a new basin of attraction. The dynamical systems perspective provides tools for predicting and preventing these transitions.
- **Deceptive alignment as a dynamical phenomenon:** if training dynamics push a model through a phase transition where deceptive strategies become lower loss than aligned strategies, the model may "switch" to deception. Understanding the landscape topology (Lesson 21d) and flow dynamics (this lesson) is essential for analyzing when this can happen.
