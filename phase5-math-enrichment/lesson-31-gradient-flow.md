# Lesson 31: Gradient Flow and Training Dynamics — Training as a River

[← Linear Systems](lesson-30-linear-systems.md) | [Back to TOC](../README.md) | [Next: Stability & Phase Transitions →](lesson-32-stability.md)

---

> **Why this lesson exists:** This is where differential equations stop being abstract mathematics and become the direct language of neural network training. Gradient flow — the continuous-time limit of gradient descent — is a specific ODE whose properties tell you about convergence, the effect of learning rate, why momentum helps, and which solutions training finds. This lesson is the bridge from "I understand ODEs" to "I understand training dynamics."

## 🎯 Core Concepts

### Gradient Flow — The Fundamental Equation

- **The setup:** you have a loss function L(W) where W is the vector of all model parameters. Gradient descent updates: W_{t+1} = W_t - η∇L(W_t). In the limit η → 0, this becomes:
  
  **dW/dt = -∇L(W)**

  This is **gradient flow** — an ODE whose vector field is the negative gradient of the loss. Every trajectory follows the steepest descent direction at every instant.

- **The vector field is the negative gradient:** at every point in weight space, the arrow points downhill on the loss surface. The magnitude of the arrow is the steepness — gradient flow moves fast where the loss is steep and slow where it's flat.

- **Fixed points are critical points:** gradient flow stops where ∇L = 0. These are the minima, maxima, and saddle points of L. From Lesson 30, you know that the Hessian eigenvalues at these points determine stability — all positive eigenvalues means a minimum (stable), mixed means a saddle (unstable along some directions).

### The Loss Function as a Lyapunov Function

- **Key insight:** the loss L itself is a **Lyapunov function** for gradient flow. Along any trajectory:

  dL/dt = ∇L · (dW/dt) = ∇L · (-∇L) = -‖∇L‖² ≤ 0

  The loss **never increases** along gradient flow. It decreases whenever ∇L ≠ 0, and stays constant only at critical points. This is why gradient descent "works" — the loss is guaranteed to decrease (in continuous time).

- **This is a proof of convergence** (in a sense): gradient flow always reaches a critical point (under mild conditions). The question isn't *whether* it converges, but *where* — which critical point does it find?

- **The catch:** this guarantee is for continuous flow. Discrete gradient descent (finite η) can violate it — if the learning rate is too large, the loss can *increase* between steps. This is why learning rate matters.

### Euler's Method Stability — Learning Rate as Step Size

- **Gradient descent = Euler's method:** W_{n+1} = W_n + η · (-∇L(W_n)). The step size is η.

- **Stability criterion for Euler's method:** for the linear ODE dx/dt = λx (λ < 0), Euler's method is stable if and only if |1 + ηλ| < 1, which gives η < 2/|λ|.

- **For gradient descent on a quadratic loss** L = ½ xᵀHx where H is the Hessian: stability requires η < 2/λ_max where λ_max is the largest eigenvalue of H. **This is the fundamental learning rate bound.** If η > 2/λ_max, training diverges.

- **The practical rule:** your learning rate must be smaller than 2/(sharpest curvature of the loss). This is why learning rate schedules start small (sharp initial landscape) and why sharp minima are harder to train into.

### Why Momentum Helps — A Second-Order ODE

- **Momentum in gradient descent:** instead of W_{t+1} = W_t - η∇L, use v_{t+1} = βv_t - η∇L(W_t), W_{t+1} = W_t + v_{t+1}. This accumulates velocity.

- **In continuous time, this becomes a second-order ODE:**

  d²W/dt² + γ dW/dt = -∇L(W)

  where γ is a friction coefficient (related to 1-β). This is **literally Newton's second law** for a ball rolling on the loss landscape with friction.

- **The physical picture:** without momentum (first-order, pure gradient flow), you're a drop of honey sliding downhill — no inertia, instant response. With momentum, you're a ball — you build up speed on slopes, coast through flat regions, and can oscillate if damping is low.

- **Why this helps with conditioning:** in a badly-conditioned loss landscape (elongated valley), gradient flow zigzags back and forth across the narrow direction while crawling along the long direction. A ball with momentum smooths this out — the oscillations in the narrow direction cancel over time, while the consistent gradient along the long direction accumulates.

### Implicit Regularization — Gradient Descent Picks Solutions

- **For overparameterized models** (more parameters than data points), there are infinitely many global minima — any interpolation of the training data. Which one does gradient descent find?

- **The remarkable answer:** gradient descent from small initialization converges to the **minimum-norm solution** for linear models. It implicitly prefers "simpler" solutions without any explicit regularization.

- **This is a dynamical phenomenon:** the trajectory through weight space, determined by the ODE, selects a particular solution. Different ODEs (different optimizers, different learning rates) may select different solutions. The optimizer is not just finding *a* minimum — it's selecting *which* minimum.

- **For deep networks:** the implicit bias is more complex. Gradient descent on deep linear networks converges to low-rank solutions. For nonlinear networks, the picture is still being worked out — this is an active research frontier.

### The Role of Learning Rate and Batch Size

- **Learning rate as temperature:** larger learning rates inject more noise (in discrete-time, through overshooting). This noise helps escape sharp minima and find flatter ones. This is formally modeled by the **stochastic differential equation (SDE):**

  dW = -∇L(W)dt + σ dB_t

  where σ ~ √(η/B) (learning rate η, batch size B), and B_t is Brownian motion. SGD is not just gradient descent plus noise — the noise structure matters.

- **Large learning rate favors flat minima:** sharp minima have large Hessian eigenvalues. The Euler stability bound η < 2/λ_max means sharp minima become unstable at large η — SGD can't stay in them. It preferentially converges to flat minima, which (arguably) generalize better.

- **Batch size and noise scale:** increasing batch size B reduces the noise σ ~ 1/√B. Large batch training is "quieter" and may converge to sharper minima. This is why large-batch training sometimes generalizes worse — and why learning rate warmup helps.

## 📺 Watch — Primary

1. **3Blue1Brown — "Gradient descent, how neural networks learn" (DL Ch. 2)**
   - https://www.youtube.com/watch?v=IHZwWFHWa-w
   - *Revisit this with your new ODE vocabulary. The gradient arrows Grant draws ARE the vector field of gradient flow.*
2. **Steve Brunton — "Gradient Systems and Lyapunov Functions" (Dynamical Systems playlist)**
   - https://www.youtube.com/c/Eigensteve
   - *Brunton explicitly connects gradient flow to Lyapunov stability theory — exactly our story.*

## 📺 Watch — Secondary

3. **Yannic Kilcher — "Implicit Regularization in Deep Learning"**
   - Search YouTube — covers the remarkable finding that gradient descent selects simple solutions without explicit regularization
4. **Sander Dieleman — "Diffusion models explained" (first half)**
   - SDEs (stochastic differential equations) are the framework for diffusion models — a direct application of noisy gradient dynamics

## 📖 Read — Primary

- **"Nonlinear Dynamics and Chaos" by Steven Strogatz** — Chapter 7.1–7.2 (Limit cycles intro, gradient systems)
  - *Strogatz proves that gradient systems can't have limit cycles — they always converge to fixed points. This is a key structural property of training dynamics.*
- **"The Matrix Calculus You Need for Deep Learning" by Parr & Howard** — revisit the gradient section with dynamical systems eyes
- **colah — "Calculus on Computational Graphs: Backpropagation"**
  - https://colah.github.io/posts/2015-08-Backprop/
  - *The computation graph IS the structure that determines how gradients (and therefore the ODE's vector field) flow through the network.*

## 📖 Read — Secondary

- **"An Introduction to Optimization on Smooth Manifolds" by Boumal** — Chapter 4 (Gradient descent convergence)
  - Free PDF: https://www.nicolasboumal.net/book/
  - *Formal convergence analysis of gradient descent from the ODE perspective*
- **"Why Momentum Really Works" by Gabriel Goh**
  - https://distill.pub/2017/momentum/
  - *Beautiful interactive visualization of momentum as a damped oscillator. One of the best Distill articles.*

## 🔨 Do

- **Gradient flow on 2D losses:** implement gradient flow (using scipy's `solve_ivp` ODE solver) for:
  - L(x,y) = x² + y² (round bowl — all trajectories are straight lines to origin)
  - L(x,y) = x² + 25y² (elongated bowl, κ=25 — see the zigzag)
  - L(x,y) = (x²-1)² + y² (double well — two minima, a saddle at origin — see which basin you land in)
  Overlay on contour plots. Compare with discrete gradient descent at various learning rates.
- **Learning rate stability experiment:** for L(x) = x²/2 (a 1D quadratic), run gradient descent with η = 0.5, 1.0, 1.5, 1.9, 2.0, 2.1. Plot x vs iteration. Identify the stability boundary at η = 2/λ = 2.0. Watch the divergence at η = 2.1.
- **Momentum visualization:** for the elongated bowl L(x,y) = x² + 25y², compare:
  - Vanilla gradient descent (lots of zigzag)
  - Gradient descent with momentum β = 0.9 (zigzag suppressed)
  Plot both trajectories. Count iterations to reach within 0.01 of the minimum.
- **Implicit regularization demo:** create a linear regression problem with d=20 features and n=5 data points (underdetermined). Run gradient descent from W=0. Compare the solution to the minimum-norm solution (computed as A⁺b via pseudoinverse). They should match.

## 🔗 ML Connection

- **Everything about optimizer design** — learning rate schedules, warmup, Adam vs SGD, batch size effects — is a statement about the dynamical system of training. This lesson gives you the framework to reason about all of it.
- **Loss landscape analysis:** papers on "sharp vs flat minima," "loss of plasticity," and "learning rate as regularizer" are all about the dynamical properties of gradient flow and its stochastic approximation.
- **The landscape-dynamics duality:** the loss landscape (static) and the training dynamics (flow on that landscape) jointly determine outcomes. You can't understand training from the landscape alone — you need the dynamics.

## 🧠 Alignment Connection

- **Implicit regularization selects for simplicity** — but does "simple" = "aligned"? This is an open question. If gradient descent prefers simple solutions and aligned behavior is simpler than deceptive behavior (debatable!), implicit regularization might help alignment. If deception is a "simpler" solution to the training objective than genuine helpfulness, it hurts.
- **Optimizer choice as alignment lever:** different optimizers explore different parts of the loss landscape. If we understood basin structure, we could potentially choose optimizers that preferentially find aligned solutions.
- **Learning rate as sharpness filter:** large learning rates destabilize sharp minima. If misaligned solutions are sharper than aligned ones (or vice versa), learning rate becomes an alignment-relevant parameter.
