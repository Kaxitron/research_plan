# Exam 2B: Differential Equations — The Language of Dynamics — Answer Key

**The Path to AI Alignment — Lessons 22–27 Comprehensive Assessment**

---

### Question 1 (10 pts)

**(a)** x* = 0 and x* = 1.

**(b)** f'(x) = 1 − 2x. At x=0: f'(0)=1>0 → **unstable**. At x=1: f'(1)=−1<0 → **stable**.

**(c)** x<0: arrows left. 0<x<1: arrows right. x>1: arrows left. Flow converges toward x=1 from both sides.

**(d)** x(0)=0.1 → increases to 1. x(0)=2 → decreases to 1.

**(e)** All x>0 are attracted to x=1 because the vector field always points toward it from both sides.

---

### Question 2 (12 pts)

**(a)** Upper triangular → λ₁ = −1, λ₂ = −3.

**(b)** λ₁=−1: v₁ = (1,0). λ₂=−3: v₂ = (1,−1).

**(c)** x(t) = c₁e^{−t}(1,0) + c₂e^{−3t}(1,−1).

**(d)** Both eigenvalues negative → **stable node**.

**(e)** Along v₁ = (1,0), the slow direction (|λ₁|<|λ₂|). The e^{−3t} decays faster, so trajectories align with v₁ at late times.

**(f)** Curvatures 1 and 3; steeper along v₂. Condition number = 3. GD converges 3× faster along v₂.

---

### Question 3 (10 pts)

**(a)** dw₁/dt = −4w₁³, dw₂/dt = −2w₂.

**(b)** dL/dt = 4w₁³(−4w₁³) + 2w₂(−2w₂) = −16w₁⁶ − 4w₂² ≤ 0. ✓

**(c)** ∂²L/∂w₁² = 12w₁² = 0 at origin. Zero curvature → gradient ∝ w₁³ is tiny near 0 → plateau.

**(d)** w(t+h) = w(t) − h·∇L(w(t)). This IS gradient descent with η = h.

---

### Question 4 (10 pts)

**(a)** (1) V(0)=0, (2) V(x)>0 for x≠0, (3) dV/dt ≤ 0 along trajectories.

**(b)** V = x²/2. dV/dt = x(−x³) = −x⁴ < 0 for x≠0. Asymptotically stable.

**(c)** dL/dt = ∇L·(−∇L) = −‖∇L‖² ≤ 0.

**(d)** Hard because: defining "aligned" formally is open, and proving dV/dt ≤ 0 for all inputs requires reasoning about the entire input space. If found, it guarantees alignment never degrades — any perturbation corrects itself.

---

### Question 5 (10 pts)

**(a)** x = 0 always; x = ±√r for r > 0.

**(b)** r<0: x=0 stable. r>0: x=0 unstable, ±√r stable.

**(c)** Supercritical pitchfork bifurcation. One stable point splits into two stable + one unstable.

**(d)** Increasing model size creates a new minimum representing the capability. Before the threshold, the minimum doesn't exist. After, training finds it — a sudden qualitative change analogous to the pitchfork's new fixed points appearing.

---

### Question 6 (10 pts)

**(a)** x(t) = 4e^{−2t}.

**(b)** x₁ = 4 − 0.5·8 = 0. x₂ = 0. x₃ = 0.

**(c)** Euler: 0. Exact: 4e^{−3} ≈ 0.199. Euler overshoots to 0 immediately.

**(d)** h=1.5: x₁=−8, x₂=16, x₃=−32. Oscillates and diverges — learning rate instability.

**(e)** |1−2h|<1 → 0<h<1. Max stable h = **1**.

---

### Question 7 (10 pts)

**(a)** x_{l+1}−x_l = f_θ(x_l) is Δx = f(x)·1, Euler's method with Δt=1.

**(b)** Advantage: O(1) memory + adaptive computation. Disadvantage: sequential (not parallelizable), and continuous flows are homeomorphisms limiting representational power.

**(c)** Avoids storing all intermediate activations. Continuous analog of backpropagation.

**(d)** Non-crossing trajectories → homeomorphism → can't change input topology. Augmenting with extra dimensions lets trajectories "go around" each other.

---

### Question 8 (10 pts)

**(a)** Deterministic: −∇L(W)dt. Stochastic: σdB_t.

**(b)** T ∝ learning_rate / batch_size. More noise = higher temperature.

**(c)** Large batch (low T) → sharp minima. Small batch (high T) → flat, generalizable minima.

**(d)** Noise makes sharp minima unstable, biasing toward flat minima that generalize. Free implicit regularization.

---

### Question 9 (10 pts)

**(a)** Smooths any distribution toward uniformity — diffuses toward the average.

**(b)** Forward process = adding Gaussian noise of increasing width = convolution with growing Gaussians. Data → noise, like heat → equilibrium.

**(c)** p(x,t) is intractable. The network learns to approximate the score by denoising: predict the noise added to noisy samples.

**(d)** Heat equation: diffusion only. Fokker-Planck: drift + diffusion. Heat equation → diffusion model forward process. Fokker-Planck → SGD weight distribution evolution.

---

### Question 10 (10 pts)

**(a)** dW/dt = −∇L(W). State space: ℝ^d (all weight configurations). Fixed points: critical points where ∇L = 0.

**(b)** Convergence rate: smallest eigenvalue of H (slowest direction). Oscillation: in discrete time, when hλ_max > 1. Continuous gradient flow doesn't oscillate (symmetric Hessian → real eigenvalues).

**(c)** Before: high loss basin, unstructured representations, memorization. After: low-RLCT basin, organized circuits implementing a generalizable algorithm. Sudden because it's crossing a bifurcation.

**(d)** (1) Lyapunov/loss: guarantees training makes progress. (2) Eigenvalues: classify critical points and set convergence rates. (3) Noise: implicit regularization toward flat minima.

**(e)** The continuous flow reveals qualitative structure (fixed points, stability, bifurcations) that discrete gradient descent inherits as approximations.
