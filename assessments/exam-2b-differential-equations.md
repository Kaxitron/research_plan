# Exam 2B: Differential Equations — The Language of Dynamics

**The Path to AI Alignment — Lessons 22–27 Comprehensive Assessment**

---

| | |
|---|---|
| **Time Allowed** | 60 minutes |
| **Total Points** | 100 |
| **Materials** | Pencil, paper, calculator (no CAS). No code. |
| **Format** | 10 questions mixing computation and conceptual depth |

> **Advice:** Show all work. The integrative thread: **gradient descent is a discretized ODE, and understanding the ODE tells you about training.**

---

## Question 1 (10 pts) — ODEs as Vector Fields

Consider the 1D ODE: dx/dt = x(1 − x).

**(a)** Find all fixed points (where dx/dt = 0).

**(b)** For each fixed point, determine stability by analyzing the sign of dx/dt on either side.

**(c)** Sketch the vector field on a number line: draw arrows showing the direction of flow for x < 0, 0 < x < 1, and x > 1.

**(d)** If x(0) = 0.1, describe qualitatively what happens as t → ∞. What about x(0) = 2?

**(e)** This is the logistic equation. Explain in one sentence why the fixed point x = 1 acts as a "basin of attraction" for most initial conditions.

---

## Question 2 (12 pts) — Linear Systems and Phase Portraits

Consider the linear system dx/dt = Ax where A = [[−1, 2], [0, −3]].

**(a)** Find the eigenvalues of A.

**(b)** Find the eigenvectors of A.

**(c)** Write the general solution x(t) = c₁e^{λ₁t}v₁ + c₂e^{λ₂t}v₂.

**(d)** Classify the phase portrait (stable node, unstable node, saddle, spiral, center).

**(e)** As t → ∞, along which eigendirection do trajectories approach the origin? Why?

**(f)** If this matrix were the negative Hessian −H of a loss function at a critical point (so the Hessian eigenvalues are +1 and +3), what would this tell you about the loss landscape there?

---

## Question 3 (10 pts) — Gradient Flow

A loss function L(w₁, w₂) = w₁⁴ + w₂² has a minimum at the origin.

**(a)** Write the gradient flow ODE: dW/dt = −∇L(W).

**(b)** Prove that L is a Lyapunov function for this system by computing dL/dt along trajectories and showing it's ≤ 0.

**(c)** Near the origin, the w₁ direction has much weaker curvature than the w₂ direction. Explain why gradient flow converges slowly from the w₁ direction. *(Hint: what is ∂²L/∂w₁² at w₁ = 0?)*

**(d)** Connect to Euler's method: if you discretize this gradient flow with step size h, write the update rule. What IS this update rule in ML terminology?

---

## Question 4 (10 pts) — Stability and Lyapunov Functions

**(a)** State the three properties a Lyapunov function V(x) must satisfy to prove a fixed point x* = 0 is stable.

**(b)** For the system dx/dt = −x³, propose a Lyapunov function and verify it works. Is the origin asymptotically stable?

**(c)** Why is the loss function L a "free" Lyapunov function for gradient flow? Write the one-line proof that dL/dt ≤ 0.

**(d)** An alignment researcher dreams of finding a Lyapunov function V(behavior) for an AI system, where V measures "distance from aligned behavior." Explain in 2–3 sentences why this is hard and what it would guarantee if found.

---

## Question 5 (10 pts) — Bifurcations and Phase Transitions

Consider the parameterized system: dx/dt = rx − x³, where r is a parameter.

**(a)** Find all fixed points as a function of r.

**(b)** For r < 0, r = 0, and r > 0, describe the number and stability of fixed points.

**(c)** What type of bifurcation occurs at r = 0? What happens geometrically?

**(d)** Relate this to neural network training: when a hyperparameter crosses a threshold, the loss landscape can change qualitatively. Give one concrete example of this and explain why understanding bifurcations matters for predicting emergent capabilities.

---

## Question 6 (10 pts) — Euler's Method IS Gradient Descent

Consider the ODE dx/dt = −2x with x(0) = 4.

**(a)** Write the exact analytical solution x(t).

**(b)** Apply Euler's method with step size h = 0.5 for 3 steps. Show the values x₁, x₂, x₃.

**(c)** Compare your Euler approximation at t = 1.5 with the exact solution. Why is there a discrepancy?

**(d)** What happens if h = 1.5? Compute a few steps and relate this to learning rate instability in gradient descent.

**(e)** The stability condition for Euler's method on dx/dt = λx is |1 + hλ| < 1. For λ = −2, what is the maximum stable step size h?

---

## Question 7 (10 pts) — Neural ODEs and ResNets

**(a)** A residual network computes x_{l+1} = x_l + f_θ(x_l) at each layer. Explain why this is Euler's method applied to the ODE dx/dt = f_θ(x).

**(b)** In the continuous limit of infinitely many layers with infinitesimal changes, the ResNet becomes the ODE dx/dt = f_θ(x(t)). Name two advantages of this Neural ODE formulation over a standard fixed-depth ResNet.

**(c)** The adjoint method computes gradients through the ODE solver in O(1) memory. Why is naive backpropagation through all solver steps expensive in memory, and how does the adjoint method avoid this?

**(d)** A continuous normalizing flow uses the identity d(log p)/dt = −tr(∂f/∂x). Why is the trace of the Jacobian easier to compute than the full Jacobian determinant? What Phase 1 concept is the trace related to?

---

## Question 8 (10 pts) — Stochastic Dynamics and SGD

**(a)** Write the stochastic differential equation (SDE) that models SGD: dW = ___dt + ___dB_t. Identify the drift and diffusion terms.

**(b)** The Fokker-Planck equation describes how the probability density of weights evolves during SGD. In steady state, the distribution approaches p(W) ∝ exp(−L(W)/T). What plays the role of "temperature" T in SGD?

**(c)** High temperature explores widely; low temperature concentrates near minima. How does batch size affect the effective temperature of SGD? Which finds flatter minima — small or large batch?

**(d)** Explain in 2–3 sentences why the noise in SGD is a feature, not a bug, from the perspective of finding solutions that generalize well.

---

## Question 9 (10 pts) — The Heat Equation and Diffusion Models

**(a)** The heat equation is u_t = k∇²u. In one sentence, explain what this equation says physically.

**(b)** The solution to the heat equation is a convolution with a Gaussian whose width grows as √t. Explain why this means the forward process of a diffusion model (adding noise progressively) eventually destroys all structure in the data.

**(c)** The reverse process of a diffusion model requires learning the score function ∇_x log p(x,t). What does the score function point toward geometrically?

**(d)** The full diffusion model pipeline is: data → progressively add noise → pure noise → learn to reverse → generate. Identify which mathematical concepts from this phase underpin each arrow.

---

## Question 10 (10 pts) — Synthesis: Training as a Dynamical System

A neural network is being trained with gradient descent on loss L(W).

**(a)** Model training as a continuous-time system. Write the gradient flow ODE.

**(b)** At a critical point W*, the Hessian H has eigenvalues {5, 2, −0.1}. Classify this critical point. Using the linear system dx/dt = −Hx near this point, describe the behavior along each eigendirection.

**(c)** A phase transition during training causes the loss to suddenly drop. Describe this event using the language of bifurcations and dynamical systems.

**(d)** Connect three concepts from this phase to three concepts from Phase 1:
- Gradient flow eigenvalue classification ↔ ___
- Euler's method step size stability ↔ ___
- Jacobian trace in normalizing flows ↔ ___

**(e)** In one sentence each, explain how this phase's concepts connect to (i) mechanistic interpretability and (ii) alignment safety.
