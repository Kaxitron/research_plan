# Lesson 36: Loss Landscapes, Gradient Flow, and Training Dynamics

[← Optimization Algorithms](lesson-35-optimization-algorithms.md) | [Back to TOC](../README.md) | [Phase 3 →](../phase3-prob-stats/lesson-37-probability.md)

**Prerequisites:** Also depends on Lesson 18 (Systems of ODEs)

---

Training a neural network is solving an ODE in parameter space. The continuous-time limit of gradient descent, dW/dt = -grad_L(W), is a gradient flow -- a dynamical system whose trajectories are paths of steepest descent on the loss surface. The Lyapunov proof that loss decreases under this flow is immediate: dL/dt = grad_L dot dW/dt = -||grad_L||^2, which is always non-positive. This single line of mathematics explains why gradient descent works at all.

But we do not run continuous gradient flow. We take discrete steps, and this discretization changes everything. The stability condition eta < 2/lambda_max(H) sets the maximum learning rate before training diverges, and the "edge of stability" phenomenon shows that real training operates right at this boundary -- the sharpness of the loss landscape self-tunes to match the learning rate. Momentum transforms the first-order ODE into a second-order one (a damped oscillator), and the connection between ResNets and Euler's method reveals that depth in a neural network is literally a discretization of continuous dynamics.

This lesson is the capstone that unifies calculus, differential equations, and dynamical systems into a single framework for understanding training. Grokking, phase transitions, edge of stability, and neural ODEs are all manifestations of the same underlying mathematics: the behavior of dynamical systems near critical transitions. For alignment, this perspective offers the possibility of predicting when a model will undergo sudden capability jumps -- the most dangerous events from a safety standpoint.

## Core Learning

- Loss as a high-dimensional surface: parameters are coordinates, loss is elevation
- In high dimensions, saddle points dominate -- local minima are exponentially rare (random matrix theory argument)
- Gradient flow ODE: dW/dt = -grad_L(W) as the continuous limit of gradient descent
- Lyapunov proof of convergence: dL/dt = -||grad_L||^2 <= 0, so loss monotonically decreases under continuous flow
- Learning rate stability condition: eta < 2/lambda_max(H) where H is the Hessian
- Momentum as second-order ODE: X_ddot + gamma * X_dot + grad_L = 0 (damped ball on loss surface)
- Neural ODEs: ResNet skip connections x_{l+1} = x_l + f(x_l) are Euler steps of dx/dt = f(x)
- SGD as a stochastic differential equation: discrete noise from mini-batching approximates Brownian motion
- Edge of stability: sharpness (top Hessian eigenvalue) self-tunes to 2/eta during training
- Grokking as a phase transition/bifurcation: sudden generalization long after memorization
- Bifurcations in training dynamics: qualitative changes in behavior at critical hyperparameter values

## Watch -- Primary

1. **3Blue1Brown -- Differential Equations series (Chapters 1-3)**
   - *The visual foundation for understanding gradient flow as a dynamical system. Focus on the phase portrait and stability intuitions.*

## Watch -- Secondary

2. **Yannic Kilcher -- "Neural Ordinary Differential Equations" (paper review)**
   - *Clear walkthrough of the Neural ODE framework and the adjoint method.*
3. **Welch Labs -- "The most complex model we actually understand [Grokking]"**
   - https://www.youtube.com/watch?v=D8GOeCFFby4
   - *Grokking as a phase transition -- connects dynamical systems theory to a real training phenomenon.*

## Read

- **Cohen et al. -- "Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability"**
  - *The paper that identified the edge-of-stability phenomenon. Focus on Sections 1-3 and the experimental results.*
- **Chen et al. -- "Neural Ordinary Differential Equations" (NeurIPS 2018)**
  - *The foundational Neural ODE paper. Read the introduction and Section 2 (ODE solvers as network layers).*
- **Strogatz -- "Nonlinear Dynamics and Chaos" (Chapter 2, Flows on the Line)**
  - *Background on fixed points, stability, and bifurcations -- the dynamical systems language used throughout this lesson.*

## Key Equations

**Gradient flow (continuous GD):**

dW/dt = -grad_L(W)

**Lyapunov proof (loss always decreases under flow):**

dL/dt = grad_L dot (dW/dt) = grad_L dot (-grad_L) = -||grad_L||^2 <= 0

**Learning rate stability condition:**

eta < 2 / lambda_max(H)

where H is the Hessian of the loss and lambda_max is its largest eigenvalue.

**Momentum as second-order ODE:**

X_ddot + gamma * X_dot + grad_L = 0

Equivalent to a damped harmonic oscillator rolling on the loss surface.

**ResNet as Euler discretization:**

x_{l+1} = x_l + f(x_l)  approx  x(t) + f(x(t)) * dt

The residual block IS one step of Euler's method applied to dx/dt = f(x).

**SGD as SDE (stochastic differential equation):**

dW = -grad_L(W) dt + sigma dB_t

where sigma^2 is proportional to eta/B (learning rate / batch size).

## Block E Capstone Project — Autodiff Engine & Optimizer Suite (4h)

**C++ Component (~1.5h):**
1. Build a reverse-mode automatic differentiation engine from scratch in C++ — define a `Value` class with a computation graph, implement forward and backward passes for +, -, *, /, tanh, and ReLU
2. Build SGD, momentum, and Adam optimizers on top of your engine
3. Train a 2-layer MLP on XOR using your engine — verify all gradients against finite differences

**Python Component (~2.5h):**
4. Compare continuous gradient flow (solve the ODE dx/dt = −∇L via RK4 using scipy) vs discrete optimizer steps on a quadratic loss — show they converge to the same minimum but discrete steps can oscillate
5. Train a small network on MNIST and track the top Hessian eigenvalue (use power iteration) over training. Verify the edge of stability: sharpness rises to approximately 2/η and hovers there

## ML & Alignment Connection

This is the capstone connection for all of calculus applied to ML. Training a neural network is solving an ODE in parameter space. The Lyapunov proof shows loss must decrease under gradient flow -- but discrete steps can violate this, leading to the edge of stability where the training process self-organizes at the boundary of convergence. Grokking (sudden generalization long after memorization) is a phase transition in training dynamics, analogous to a bifurcation in a dynamical system. Neural ODEs (ResNets as continuous dynamics) unify deep learning with dynamical systems theory, making the entire toolkit of ODE analysis available for understanding networks.

For alignment, the dynamical systems perspective on training is critical. If training dynamics undergo bifurcations -- sudden qualitative changes in behavior -- then a model might acquire dangerous capabilities abruptly rather than gradually. Understanding the conditions that trigger these transitions (learning rate, data distribution, model scale) is essential for predicting and preventing sudden capability jumps. The edge of stability phenomenon shows that training already operates at a critical boundary, and the connection between SGD noise and exploration of the loss landscape suggests that the specific minima a model finds (and therefore its behaviors) depend sensitively on hyperparameters that practitioners often treat as arbitrary tuning knobs.
