# Exam 2B: Differential Equations — The Language of Dynamics — Answer Key

**The Path to AI Alignment — Lessons 22–27 Comprehensive Assessment**

---

### Question 1 (10 pts)

**(a)** x(1−x) = 0 → **x* = 0** and **x* = 1**.

**(b)** f'(x) = 1−2x. f'(0) = 1 > 0 → **unstable**. f'(1) = −1 < 0 → **stable**.

**(c)** x < 0: arrows left. 0 < x < 1: arrows right. x > 1: arrows left.

**(d)** x(0) = 0.1 → increases toward 1. x(0) = 2 → decreases toward 1. Both converge to the stable fixed point.

**(e)** For all x(0) > 0, flow always pushes toward x = 1, making (0, ∞) its basin of attraction.

---

### Question 2 (12 pts)

**(a)** Upper triangular → eigenvalues on diagonal: **λ₁ = −1, λ₂ = −3**.

**(b)** λ₁ = −1: [[0,2],[0,−2]]v = 0 → **v₁ = (1, 0)**. λ₂ = −3: [[2,2],[0,0]]v = 0 → **v₂ = (1, −1)**.

**(c)** **x(t) = c₁e^{−t}(1, 0) + c₂e^{−3t}(1, −1)**.

**(d)** Both eigenvalues negative and real → **stable node**.

**(e)** Along **v₁ = (1, 0)** (the slow eigendirection, λ = −1). The fast component e^{−3t} decays 3× faster, so trajectories first collapse onto v₁, then slowly approach the origin along it.

**(f)** Hessian eigenvalues +1, +3 → **local minimum** (bowl). Steeper in v₂ direction (curvature 3), shallower in v₁ (curvature 1). Condition number κ = 3.

---

### Question 3 (10 pts)

**(a)** **dw₁/dt = −4w₁³, dw₂/dt = −2w₂**.

**(b)** dL/dt = 4w₁³(−4w₁³) + 2w₂(−2w₂) = **−16w₁⁶ − 4w₂² ≤ 0**. Equality only at origin. ∎

**(c)** ∂²L/∂w₁² = 12w₁² → **zero at the origin**. The landscape is flat to second order in w₁. Gradient = 4w₁³ ≈ 0 for small w₁, so flow crawls. The w₂ direction has constant curvature 2 and converges exponentially.

**(d)** W_{n+1} = W_n − h∇L(W_n). This IS **gradient descent with learning rate η = h**.

---

### Question 4 (10 pts)

**(a)** (1) V(0) = 0. (2) V(x) > 0 for x ≠ 0 near 0. (3) dV/dt ≤ 0 along trajectories. (Strict inequality gives asymptotic stability.)

**(b)** V(x) = x². dV/dt = 2x(−x³) = **−2x⁴ < 0** for x ≠ 0. **Asymptotically stable.**

**(c)** dL/dt = ∇L · (−∇L) = **−‖∇L‖² ≤ 0**. Loss never increases along gradient flow.

**(d)** Hard because: formalizing "aligned behavior" as a scalar function is itself an open problem (translating values into math), and proving dV/dt ≤ 0 for all inputs requires universal guarantees. If found, it would **mathematically guarantee the system never drifts from alignment** — a stability certificate analogous to what control engineers use for physical systems.

---

### Question 5 (10 pts)

**(a)** x(r − x²) = 0: **x = 0** always; **x = ±√r** when r > 0.

**(b)** r < 0: one fixed point (x = 0, stable). r = 0: one (marginal). r > 0: three (x = 0 unstable, x = ±√r stable).

**(c)** **Supercritical pitchfork bifurcation.** One stable point loses stability and two new stable points emerge symmetrically — **symmetry breaking**.

**(d)** Example: as model size crosses a threshold, arithmetic capability suddenly emerges. The loss landscape gains new basins (the arithmetic solution becomes accessible). Bifurcation theory tells us these transitions can be **sharp and discontinuous** — capabilities appear suddenly at critical parameter values, making it dangerous to assume gradual capability growth for safety planning.

---

### Question 6 (10 pts)

**(a)** **x(t) = 4e^{−2t}**.

**(b)** x_{n+1} = x_n(1 − 2·0.5) = 0. x₁ = **0**, x₂ = **0**, x₃ = **0**.

**(c)** Exact x(1.5) = 4e^{−3} ≈ **0.199**. Euler gives 0. The step was large enough to overshoot to exactly zero, missing the gradual exponential decay.

**(d)** h = 1.5: x₁ = 4(1−3) = **−8**, x₂ = **16**, x₃ = **−32**. Oscillates and **diverges** — the direct analog of training divergence with too-high learning rate.

**(e)** |1−2h| < 1 → 0 < h < 1. **Maximum stable h = 1.**

---

### Question 7 (10 pts)

**(a)** ResNet: x_{l+1} = x_l + f_θ(x_l). Euler: x_{n+1} = x_n + h·g(x_n). Identical with h = 1, g = f_θ. Each residual layer = one Euler step of dx/dt = f_θ(x).

**(b)** (1) **Constant O(1) memory** via the adjoint method (vs O(depth) for ResNets). (2) **Adaptive computation** — solver adjusts step count to input difficulty.

**(c)** Naive backprop stores all N intermediate states → O(N) memory. The adjoint method solves a backward ODE needing only the current state, avoiding storage of the full trajectory.

**(d)** Trace = sum of d diagonal entries = O(d). Determinant = O(d³). The Hutchinson estimator approximates the trace stochastically in O(d). Trace relates to **sum of eigenvalues** (Phase 1, Lesson 8).

---

### Question 8 (10 pts)

**(a)** **dW = −∇L(W)dt + σ(W)dB_t**. Drift = −∇L (gradient descent). Diffusion = σdB_t (mini-batch noise).

**(b)** T ∝ **η/B** (learning rate / batch size). This ratio controls exploration vs. exploitation.

**(c)** Smaller batch → larger noise → higher T → broader exploration. **Small batch finds flatter minima** (noise kicks it out of sharp ones but not flat ones).

**(d)** Noise biases toward flat minima that are robust to perturbation. Flat minima generalize better because nearby parameters give similar predictions. Without noise, gradient descent converges to the nearest minimum regardless of generalization quality.

---

### Question 9 (10 pts)

**(a)** Temperature at each point changes proportionally to how much it differs from its neighbors — hot spots cool, cold spots warm, everything smooths toward average.

**(b)** Gaussian width ∝ √t → ∞ as t → ∞. Infinite-width Gaussian convolution averages everything to uniform — all structure is destroyed.

**(c)** Points toward **higher probability density** — from unlikely regions toward likely ones. It's the denoising compass.

**(d)** Data → noise: **heat equation/diffusion**. Noise convergence: **steady state**. Learn to reverse: **score function estimation** (gradients, Lesson 15). Generate: **reverse SDE** (backward dynamics).

---

### Question 10 (10 pts)

**(a)** **dW/dt = −∇L(W)**

**(b)** **Saddle point** (eigenvalues 5, 2 positive; −0.1 negative). Along λ = 5: fast convergence. λ = 2: slower convergence. λ = −0.1: slow escape (unstable direction). Training eventually leaves along the unstable direction.

**(c)** A bifurcation: the trajectory was in one basin, the landscape topology changed (new deeper basin appeared), and the system rapidly transitioned. In SLT: model moved between singularities with different RLCTs. Grokking is a prime example — memorization plateau → sudden generalization.

**(d)** Eigenvalue classification ↔ **eigenanalysis** (Lesson 8). Step size stability ↔ **condition number** (Lesson 11). Jacobian trace ↔ **trace = sum of eigenvalues / determinant = volume scaling** (Lessons 7–8).

**(e)** (i) Interpretability: phase transitions reveal when circuits form — developmental interpretability tracks these reorganizations. (ii) Safety: Lyapunov functions are the ideal for formal alignment stability proofs; bifurcation theory warns that capabilities emerge suddenly at thresholds, making gradual testing insufficient.
