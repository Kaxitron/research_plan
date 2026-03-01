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

**(f)** If this matrix were the Hessian of a loss function at a minimum, what would the eigenvalues tell you about the shape?

---

## Question 3 (10 pts) — Gradient Flow

A loss function L(w₁, w₂) = w₁⁴ + w₂² has a minimum at the origin.

**(a)** Write the gradient flow ODE: dW/dt = −∇L(W).

**(b)** Prove that L is a Lyapunov function for this system by computing dL/dt along trajectories and showing it's ≤ 0.

**(c)** Near the origin, the w₁ direction has much weaker curvature than the w₂ direction. Explain why gradient flow converges slowly from the w₁ direction. *(Hint: what is ∂²L/∂w₁² at w₁ = 0?)*

**(d)** Connect to Euler's method: if you discretize this gradient flow with step size h, write the update rule. What IS this in ML terms?

---

## Question 4 (10 pts) — Stability and Lyapunov Functions

**(a)** State the three properties a Lyapunov function V(x) must satisfy for a fixed point x* = 0.

**(b)** For the system dx/dt = −x³, propose a Lyapunov function and verify it works. Is the origin asymptotically stable?

**(c)** Why is the loss L a "free" Lyapunov function for gradient flow? Write the one-line proof.

**(d)** An alignment researcher wants a Lyapunov function V(behavior) where V measures "distance from aligned behavior." Explain in 2–3 sentences why this is hard and what it would guarantee if found.

---

## Question 5 (10 pts) — Bifurcations and Phase Transitions

Consider dx/dt = rx − x³, where r is a parameter.

**(a)** Find all fixed points as a function of r.

**(b)** For r < 0, r = 0, and r > 0, classify each fixed point as stable or unstable.

**(c)** What type of bifurcation occurs at r = 0? What changes qualitatively?

**(d)** Relate to training: as model size increases past a threshold, a network suddenly learns a new capability (e.g., in-context learning). Explain in 2–3 sentences how this resembles a bifurcation.

---

## Question 6 (10 pts) — Euler's Method IS Gradient Descent

Consider dx/dt = −2x with x(0) = 4.

**(a)** Write the exact analytical solution x(t).

**(b)** Apply Euler's method with h = 0.5 for 3 steps. Show x₁, x₂, x₃.

**(c)** Compare Euler at t = 1.5 with the exact value.

**(d)** What happens with h = 1.5? Compute 3 steps. Relate to learning rate instability.

**(e)** For dx/dt = λx, the stability condition is |1 + hλ| < 1. For λ = −2, find the maximum stable h.

---

## Question 7 (10 pts) — Neural ODEs and ResNets

**(a)** A ResNet computes x_{l+1} = x_l + f_θ(x_l). Explain why this is Euler's method on dx/dt = f_θ(x).

**(b)** In the continuous limit (infinitely many layers, infinitesimal changes), a ResNet becomes an ODE. State one advantage and one disadvantage of neural ODEs compared to standard ResNets.

**(c)** The adjoint method computes gradients through an ODE solver in O(1) memory. Why is this important? What is it the continuous analog of?

**(d)** Neural ODE trajectories cannot cross in phase space (uniqueness theorem). Explain why this limits what a neural ODE can compute, and how augmented neural ODEs fix this.

---

## Question 8 (10 pts) — Stochastic Dynamics and SGD

**(a)** SGD adds noise to gradient descent. The corresponding SDE is dW = −∇L(W)dt + σdB_t. In this equation, identify the deterministic part and the stochastic part.

**(b)** The Fokker-Planck equation describes how the probability distribution over weights evolves during SGD training. Its steady-state solution is p(W) ∝ exp(−L(W)/T). What does the "temperature" T correspond to in SGD terms?

**(c)** A low-temperature distribution concentrates near the minimum of L. A high-temperature distribution is spread out. What does this predict about the solutions found by large vs. small batch SGD?

**(d)** Explain in 2–3 sentences why SGD noise is a *feature*, not a bug, from the perspective of finding generalizable solutions.

---

## Question 9 (10 pts) — The Heat Equation and Diffusion Models

**(a)** The heat equation is u_t = k∇²u. In one sentence, describe what this equation does to an initial temperature distribution over time.

**(b)** The solution to the heat equation is a convolution with a Gaussian whose width grows as √t. How does this connect to the forward process of a diffusion model?

**(c)** A diffusion model has two processes: forward (add noise) and reverse (remove noise). The reverse process requires knowing the "score function" ∇_x log p(x,t). Why can't we compute this directly, and what does the neural network learn instead?

**(d)** The Fokker-Planck equation from Q8 is closely related to the heat equation. State the key difference (one has drift, one doesn't) and explain why both appear in ML.

---

## Question 10 (10 pts) — Synthesis: Training as a Dynamical System

A neural network is trained with gradient descent. Think of the entire training process as a dynamical system.

**(a)** State the ODE that describes continuous-time training (gradient flow). What is the "state space"? What are the "fixed points"?

**(b)** Near a minimum w*, the linearized dynamics are dδ/dt = −H(w*)δ where δ = w − w*. What determines the convergence rate? What determines whether the system oscillates?

**(c)** A phase transition during training (like grokking) can be modeled as the system crossing a bifurcation point. Describe what "before" and "after" look like in terms of the loss and the model's internal structure.

**(d)** Connect at least THREE concepts from this exam to the training process: Lyapunov function, eigenvalue classification, Euler's method, bifurcation, stochastic noise, or the heat equation. For each, state what role it plays.

**(e)** In one sentence: why does understanding the continuous-time ODE (gradient flow) help you understand the discrete-time algorithm (gradient descent)?

---

## 🔧 Optional Mini Project (~45 minutes): Training Dynamics Phase Portrait

**Simulate gradient descent as a dynamical system and visualize its phase portrait.**

1. Define a 2D loss surface with two local minima and one saddle point (e.g., L(x,y) = (x²−1)² + y²)
2. Compute the gradient flow ODE: dw/dt = −∇L(w)
3. Using Euler's method, simulate trajectories from 20+ initial conditions spread across the 2D plane
4. Plot all trajectories on a single figure with the loss contours in the background
5. Identify and mark the fixed points (minima, saddle). Color trajectories by which minimum they converge to — visualize the basins of attraction
6. Add stochastic noise (simulating SGD) and show how noise allows escape from shallow minima

**Stretch:** Compute the Jacobian at each fixed point. Verify that the eigenvalues predict the local behavior you observe (stable node, saddle, etc.).

**Tools:** NumPy, Matplotlib. No ML libraries needed.
