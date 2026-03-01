# Exam 2A: Calculus — The Language of Optimization — Answer Key

**The Path to AI Alignment — Lessons 13–21 Comprehensive Assessment**

---

> **Grading philosophy:** Partial credit is generous for correct reasoning with arithmetic errors. Geometric explanations earn full marks. The goal is demonstrating understanding of the complete optimization pipeline.

---

### Question 1 (8 pts) — Gradient Computation and Geometry

**(a)** ∇L = (∂L/∂w₁, ∂L/∂w₂) = **(2w₁ − 2w₂, 6w₂ − 2w₁)**

**(b)** ∇L(2, 1) = (4 − 2, 6 − 4) = **(2, 2)**

The gradient is **perpendicular to the contour lines** and points toward steepest ascent. Contour lines are ellipses (positive definite quadratic form).

**(c)** New point = (2, 1) − 0.1·(2, 2) = **(1.8, 0.8)**

**(d)** D_u L = (2, 2) · (1/√2, 1/√2) = 4/√2 ≈ **2.83**. Since |∇L| = 2√2 ≈ 2.83, the directional derivative equals the gradient magnitude — u IS the gradient direction. So this is **equivalent** to steepest descent (up to sign).

---

### Question 2 (10 pts) — The Chain Rule IS Backpropagation

**(a)** z = 3(2) + (−1) = **5**. a = ReLU(5) = **5**. L = (5−4)² = **1**.

**(b)** ∂L/∂a = 2(a−y) = **2**. ∂a/∂z = 1 (z > 0). ∂L/∂z = **2**. ∂L/∂w = 2·2 = **4**. ∂L/∂b = 2·1 = **2**.

**(c)** (∂L/∂a)(∂a/∂z)(∂z/∂w) = 2·1·2 = **4** ✓

**(d)** Neural networks have millions of parameters but one scalar loss. Reverse-mode computes ALL partial derivatives in one backward pass. Forward-mode needs one pass per parameter — O(d) vs O(1). This makes backprop essential for neural networks.

---

### Question 3 (10 pts) — The Hessian Classifies Critical Points

**(a)** ∇f = (3x² − 3y², −6xy). Setting to zero: x² = y² and xy = 0. Only solution: **(0, 0)**.

**(b)** H = [[6x, −6y], [−6y, −6x]]

**(c)** At (0,0): H = [[0,0],[0,0]]. Both eigenvalues zero — **inconclusive**. This is a monkey saddle (degenerate saddle with three valleys). Higher-order terms needed.

**(d)** In d dimensions, all d Hessian eigenvalues must be positive for a minimum. Probability ≈ (1/2)^d, exponentially small. At d = 1000, saddle points dominate overwhelmingly. Good news: saddle points have escape directions.

---

### Question 4 (10 pts) — Constrained Optimization and Lagrange Multipliers

**(a)** ℒ = w₁² + w₂² − λ(w₁ + 2w₂ − 5)

**(b)** 2w₁ = λ, 2w₂ = 2λ, w₁ + 2w₂ = 5. So w₁ = λ/2, w₂ = λ. Then λ/2 + 2λ = 5 → **λ* = 2, w₁* = 1, w₂* = 2.** Optimal loss = **5**.

**(c)** λ* = 2: relaxing by ε changes optimal loss by ≈ 2ε. It's the "shadow price" of the constraint.

**(d)** Alignment IS constrained optimization: maximize capability subject to safety. The multiplier measures the "alignment tax" — capability cost per unit of safety.

---

### Question 5 (12 pts) — Taylor Expansion and Local Approximation

**(a)** f(w) ≈ f(w₀) + ½(w − w₀)ᵀ H(w₀)(w − w₀). The linear term vanishes at a critical point. The Hessian determines the local quadratic bowl shape.

**(b)** e^x ≈ 1 + x + x²/2 + x³/6. e^(0.1) ≈ **1.10517**.

**(c)** Elongated elliptical bowl: steep along v₁ (curvature 10), nearly flat along v₂ (curvature 0.1). Condition number κ = 10/0.1 = **100**.

**(d)** High κ → gradient points toward steep walls, not along the valley floor → zigzag bouncing. From Phase 1: Hessian eigenvalues ARE curvatures along eigenvector directions. Different eigenvalue magnitudes = different curvature rates = poor conditioning.

**(e)** Newton: **w_{new} = w − H⁻¹∇f(w)**. Rescales by H⁻¹, normalizing all directions to equal effective curvature. Not used for neural networks: O(d²) memory, O(d³) computation, and non-positive-definite Hessians.

---

### Question 6 (10 pts) — Integration and the Jacobian Determinant

**(a)** Polar: ∫₀^{2π} ∫₀^1 r²·r dr dθ = 2π · [r⁴/4]₀^1 = **π/2**

**(b)** ∬ f(x,y)dxdy = ∬ f(g⁻¹(u,v))|det(J⁻¹)|dudv. The Jacobian determinant measures local area stretching — the Phase 1 determinant meaning applied to infinitesimal coordinate patches.

**(c)** X = (Y−2)/3, |dx/dy| = 1/3. f_Y(y) = (1/√(2π))exp(−(y−2)²/18)·(1/3). This is **N(2, 9)**.

**(d)** det(Σ) measures the ellipsoidal volume where the Gaussian has significant mass. Larger volume → smaller peak height to integrate to 1.

---

### Question 7 (10 pts) — The Implicit Function Theorem and Sensitivity

**(a)** w(w² − λ) = 0. Solutions: w = 0 (all λ) and w = ±√λ (λ > 0).

**(b)** F(1,1) = 0 ✓. ∂F/∂w = 3w² − λ = 2 ≠ 0 → IFT applies. dw/dλ = w/(3w²−λ) = **1/2**.

**(c)** At (0,0): ∂F/∂w = 0. IFT fails. This is a **pitchfork bifurcation** — one solution splits into three as λ crosses 0.

**(d)** Bifurcations mean the loss landscape topology changes with hyperparameters. In SLT, singularities occur exactly where the IFT fails — the Jacobian of the gradient becomes degenerate. These singular points determine the RLCT and effective model complexity.

---

### Question 8 (10 pts) — The Bias-Variance Tradeoff

**(a)** Error = **Bias²** + **Variance** + **Irreducible Noise**

**(b)** **Bias** dominates. A parabola can't capture cubic shape — systematic error regardless of data.

**(c)** **Variance** dominates. 1000 parameters on 20 points memorizes noise — different data → wildly different model.

**(d)** **Double descent.** Error rises past the interpolation threshold then falls again for very overparameterized models. SLT explains: effective complexity (RLCT) is much less than parameter count.

**(e)** Training fits parameters. Validation selects models/hyperparameters (implicitly "training" on validation data). Test gives unbiased performance — if touched during selection, estimates are optimistic.

---

### Question 9 (10 pts) — Optimization Algorithms

**(a)** (i) w_{t+1} = w_t − η∇L(w_t). (ii) v_{t+1} = βv_t + ∇L(w_t); w_{t+1} = w_t − ηv_{t+1}.

**(b)** Heavy ball rolling downhill. Accumulates velocity from past gradients. Side-to-side bouncing cancels; along-valley speed reinforces. Can roll over small bumps through kinetic energy.

**(c)** Mini-batch noise helps **escape sharp minima** — random perturbations push away from narrow minima toward broad flat ones that generalize better.

**(d)** Adam scales each parameter's learning rate based on its gradient history — large consistent gradients get smaller rates, small/noisy gradients get larger rates.

**(e)** Finite learning rate acts as implicit regularization. Discrete steps "jump over" narrow minima that continuous flow would settle into. Finite-η SGD biases toward **flatter minima** whose width exceeds the step size.

---

### Question 10 (10 pts) — Synthesis: The Complete Path

**(a)** ∇L(W₀) points toward steepest ascent. Gradient descent moves opposite: W₁ = W₀ − η∇L(W₀), trusting the first-order Taylor approximation for one small step.

**(b)** At ∇L = 0, Hessian eigenvalues classify: all positive → minimum, all negative → maximum, mixed → saddle.

**(c)** **Saddle point** (one negative eigenvalue). The near-zero eigenvalue (0.01) indicates an almost flat direction — a near-symmetry in the model, characteristic of singularities where effective dimensionality < parameter count.

**(d)** Jacobian det: correction factor when transforming probability densities (normalizing flows, Gaussian normalization). Hessian det: classifies critical points, relates to basin volume.

**(e)** Chain rule/backprop ← **matrix multiplication** (Lesson 5). Hessian/landscape ← **eigenvalues** (Lesson 8). Jacobian/probability ← **determinants** (Lesson 7).
