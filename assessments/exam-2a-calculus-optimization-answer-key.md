# Exam 2A: Calculus — The Language of Optimization — Answer Key

**The Path to AI Alignment — Lessons 13–21 Comprehensive Assessment**

---

> **Grading philosophy:** Partial credit is generous for correct reasoning with arithmetic errors. Geometric explanations alongside algebra earn full marks. The goal is demonstrating understanding of the complete optimization pipeline.

---

# Part I: Calculus Fundamentals (70 points)

---

### Question 1 (8 pts) — Differentiation Fluency

**(a)** Power rule: f'(x) = **20x³ − 6x + 7**

**(b)** Product rule: f'(x) = 2x·ln(x) + x²·(1/x) = **2x·ln(x) + x**

**(c)** Chain rule: f'(x) = 5(3x² + 1)⁴ · 6x = **30x(3x² + 1)⁴**

**(d)** Chain rule: f'(x) = e^(sin(x)) · cos(x) = **cos(x)·e^(sin(x))**

*Scoring: 2 pts each. 1 pt for correct method even with arithmetic error.*

---

### Question 2 (10 pts) — The Chain Rule Gauntlet

**(a)** Outer: ln(u), inner: u = x³ + eˣ.

f'(x) = (1/(x³ + eˣ)) · (3x² + eˣ) = **(3x² + eˣ)/(x³ + eˣ)**

**(b)** Outer: u², middle: sin(v), inner: v = 3x.

f'(x) = 2sin(3x) · cos(3x) · 3 = **6sin(3x)cos(3x)** = 3sin(6x)

**(c)** Outer: eᵘ, inner: u = −x²/2.

f'(x) = e^(−x²/2) · (−x) = **−x·e^(−x²/2)**

This is (up to a constant) the derivative of the Gaussian density — it appears everywhere in probability.

**(d)** σ(x) = (1 + e^(−x))^(−1).

σ'(x) = −(1 + e^(−x))^(−2) · (−e^(−x)) = e^(−x)/(1 + e^(−x))²

Now factor: e^(−x)/(1 + e^(−x))² = [1/(1 + e^(−x))] · [e^(−x)/(1 + e^(−x))]

Note: e^(−x)/(1 + e^(−x)) = 1 − 1/(1 + e^(−x)) = 1 − σ(x)

So: **σ'(x) = σ(x)(1 − σ(x))** ✓

**(e)** L = −ln(σ(x)). By chain rule:

dL/dx = −(1/σ(x)) · σ'(x) = −(1/σ(x)) · σ(x)(1−σ(x)) = **−(1 − σ(x)) = σ(x) − 1**

As σ(x) → 1 (confident and correct): dL/dx → **0**. The gradient vanishes — the model barely updates because it's already right. This is correct behavior.

As σ(x) → 0 (confident and wrong): dL/dx → **−1**. Strong gradient signal pushing the model to fix its confident mistake. Cross-entropy's great property: it punishes confident wrong answers hard.

---

### Question 3 (8 pts) — Critical Points and the Second Derivative Test

**(a)** f'(x) = 3x² − 12x + 9 = 3(x² − 4x + 3) = 3(x − 1)(x − 3) = 0

Critical points: **x = 1** and **x = 3**.

f''(x) = 6x − 12. At x = 1: f''(1) = −6 < 0 → **local maximum**, f(1) = 1 − 6 + 9 + 1 = 5.
At x = 3: f''(3) = 6 > 0 → **local minimum**, f(3) = 27 − 54 + 27 + 1 = 1.

**(b)** g(x) = xe^(−x). g'(x) = e^(−x) − xe^(−x) = e^(−x)(1 − x) = 0 → **x = 1**.

g''(x) = −e^(−x)(1 − x) − e^(−x) = e^(−x)(x − 2). At x = 1: g''(1) = e^(−1)(−1) < 0 → **local maximum**, g(1) = 1/e ≈ 0.368.

**(c)** f''(x) > 0 means the curve is **concave up** — shaped like a bowl, curving upward. The tangent line lies below the curve. f''(x) = 0 means the curvature is zero — the curve is instantaneously flat (an inflection point). The second derivative test is inconclusive because zero curvature could mean a minimum, maximum, or inflection point — you can't tell without higher-order information.

---

### Question 4 (10 pts) — Integration

**(a)** ∫(3x² + 2x − 1) dx = **x³ + x² − x + C**

**(b)** ∫₀¹ e^(2x) dx = [e^(2x)/2]₀¹ = e²/2 − 1/2 = **(e² − 1)/2 ≈ 3.195**

**(c)** ∫₁ᵉ (1/x) dx = [ln(x)]₁ᵉ = ln(e) − ln(1) = **1 − 0 = 1**. The famous number is **e** (the base of the natural log, appearing as the upper limit).

**(d)** ∫₀¹ 2x dx = [x²]₀¹ = 1 ✓. P(0.5 ≤ X ≤ 1) = ∫₀.₅¹ 2x dx = [x²]₀.₅¹ = 1 − 0.25 = **0.75**.

**(e)** The FTC says that differentiation and integration are inverse operations. Specifically: if F(x) = ∫ₐˣ f(t) dt, then F'(x) = f(x). The total accumulation (integral) can be computed by finding any antiderivative and evaluating at the endpoints. This connects "rate of change" (derivative) with "total change" (integral).

---

### Question 5 (8 pts) — Limits and L'Hôpital's Rule

**(a)** lim(x→0) sin(x)/x = **1**. (Known fundamental limit.)

**(b)** At x = 0: numerator = e⁰ − 1 = 0, denominator = 0. Indeterminate 0/0 form. L'Hôpital: lim = (eˣ)/1 evaluated at x = 0 = **1**.

**(c)** Rewrite as lim(x→∞) x/eˣ. Form ∞/∞. L'Hôpital: lim = 1/eˣ → **0** as x → ∞. Exponential growth dominates polynomial growth.

**(d)** Indeterminate forms arise in ML when analyzing loss functions near critical points where both the gradient and certain denominators approach zero simultaneously. For example, analyzing the KL divergence D_KL(P‖Q) when P and Q become similar (0·log(0/0) terms), or understanding learning dynamics as weights approach symmetry-creating values like zero.

---

### Question 6 (8 pts) — Partial Derivatives

**(a)** ∂f/∂x = **2xy + 3y² − 2**

**(b)** ∂f/∂y = **x² + 6xy + 1**

**(c)** ∂²f/∂x∂y = ∂/∂x(x² + 6xy + 1) = 2x + 6y.
∂²f/∂y∂x = ∂/∂y(2xy + 3y² − 2) = 2x + 6y. **Equal** ✓ (Clairaut's theorem).

**(d)** ∇f(1, 2) = (2(1)(2) + 3(4) − 2, 1 + 6(1)(2) + 1) = (4 + 12 − 2, 1 + 12 + 1) = **(14, 14)**.

f increases most rapidly in the direction of the gradient: **(14, 14)**, or normalized: **(1/√2, 1/√2)** — along the 45° line.

---

### Question 7 (10 pts) — Series and Convergence

**(a)** eˣ = 1 + x + x²/2! + x³/3! + x⁴/4! = **1 + x + x²/2 + x³/6 + x⁴/24**

**(b)** e^(0.1) ≈ 1 + 0.1 + 0.005 + 0.000167 + 0.0000042 ≈ **1.10517**. True value: 1.10517... Excellent match even at 4 terms!

**(c)** 1/(1−x) = 1 + x + x² + x³ + ··· = **Σₙ₌₀^∞ xⁿ** for |x| < 1. Each term is the previous times x.

**(d)** Converges for −1 < x ≤ 1. ln(1.1) = ln(1 + 0.1) ≈ 0.1 − 0.005 + 0.000333 − 0.000025 ≈ **0.09531**. True value: 0.09531... Again excellent.

**(e)** Taylor series let us approximate complicated functions with polynomials near a point. In ML, when a paper says "to second order" or "locally quadratic," they're using the second-order Taylor expansion: the loss near any critical point is approximately a quadratic form determined by the Hessian. This is why everything you learned about quadratic forms, eigenvalues, and condition numbers in Phase 1 directly describes local training dynamics.

---

### Question 8 (8 pts) — Integration Techniques

**(a)** Let u = x, dv = eˣdx. Then du = dx, v = eˣ.

∫xeˣ dx = xeˣ − ∫eˣ dx = **xeˣ − eˣ + C = eˣ(x − 1) + C**

**(b)** Let u = x² + 1, du = 2x dx.

∫ 2x/(x² + 1) dx = ∫ du/u = ln|u| + C = **ln(x² + 1) + C**

**(c)** Square the integral: (∫e^(−x²)dx)² = ∫∫e^(−x²−y²) dx dy. In polar coordinates, x² + y² = r² and dx dy = r dr dθ. The integral becomes ∫₀^{2π} ∫₀^∞ e^(−r²) r dr dθ = 2π · [−e^(−r²)/2]₀^∞ = 2π · ½ = π. Taking the square root: √π.

**(d)** This integral is the foundation of the **normal distribution's normalization**. Every Gaussian probability calculation, every multivariate normal, every partition function in statistical mechanics traces back to it. In ML, it appears whenever we work with Gaussian priors, likelihoods, or noise models — which is essentially always.

---

# Part II: ML-Specific Calculus (80 points)

---

### Question 9 (12 pts) — The Chain Rule IS Backpropagation

**(a)** z = 3(2) + (−1) = **5**. a = ReLU(5) = **5**. L = (5 − 4)² = **1**.

**(b)** Backward:
- ∂L/∂a = 2(a − y) = 2(5 − 4) = **2**
- ∂a/∂z = 1 (since z = 5 > 0, ReLU' = 1), so ∂L/∂z = 2 · 1 = **2**
- ∂z/∂w = x = 2, so ∂L/∂w = 2 · 2 = **4**
- ∂z/∂b = 1, so ∂L/∂b = 2 · 1 = **2**

**(c)** (∂L/∂a)(∂a/∂z)(∂z/∂w) = 2 · 1 · 2 = **4** ✓

**(d)** z = −16 < 0, so ReLU(z) = 0 and ReLU'(z) = 0. Therefore ∂L/∂z = (∂L/∂a) · 0 = 0, and ∂L/∂w = 0. **The gradient is completely zero.** This is the **dying ReLU problem**: once a neuron's pre-activation goes negative, it produces zero gradient and can never recover. The neuron is "dead."

**(e)** A neural network has millions of parameters but **one scalar output** (the loss). Reverse-mode computes ALL partial derivatives of one output w.r.t. all inputs in a single backward pass — O(1) passes. Forward-mode computes all output derivatives w.r.t. ONE input — requiring O(d) passes for d parameters. For neural networks where d >> 1, reverse-mode wins massively.

---

### Question 10 (12 pts) — The Hessian and Loss Landscape Geometry

**(a)** ∇L = (2w₁ − 2w₂, 6w₂ − 2w₁). Setting to zero: 2w₁ − 2w₂ = 0 → w₁ = w₂, and 6w₂ − 2w₁ = 0 → 6w₂ = 2w₁ → w₁ = 3w₂. Combined: w₁ = w₂ and w₁ = 3w₂ → w₂ = 0, w₁ = 0. Critical point: **(0, 0)**.

**(b)** H = [[2, −2], [−2, 6]]

**(c)** det(H − λI) = (2−λ)(6−λ) − 4 = λ² − 8λ + 8 = 0.

λ = (8 ± √(64−32))/2 = (8 ± √32)/2 = 4 ± 2√2.

**λ₁ = 4 + 2√2 ≈ 6.83, λ₂ = 4 − 2√2 ≈ 1.17.** Both positive → **local minimum** (and global minimum, since L is a quadratic that goes to +∞).

**(d)** κ = λ_max/λ_min = (4 + 2√2)/(4 − 2√2) ≈ 6.83/1.17 ≈ **5.83**.

A high condition number means the curvature differs greatly between the steepest and shallowest directions. Gradient descent follows the gradient, which points mostly toward the steep walls. The optimizer bounces between the walls (steep direction) while crawling along the valley floor (shallow direction). The result is zigzag behavior. The step size must be small enough for the steep direction, which makes progress painfully slow along the shallow direction.

**(e)** At w₀ = (0,0) with ∇L = 0: **L(w) ≈ L(0) + ½wᵀHw** = ½wᵀ[[2,−2],[−2,6]]w.

This shows the loss near the critical point IS a quadratic form in the Hessian — exactly the objects you studied in Phase 1. The Hessian eigenvalues are the curvatures along the principal (eigenvector) directions. The Hessian eigenvectors define the "natural" coordinate axes of the local landscape. Everything about quadratic forms — positive definiteness, condition number, principal axes — directly describes the local loss surface.

---

### Question 11 (10 pts) — Constrained Optimization and Lagrange Multipliers

**(a)** ℒ(w₁, w₂, λ) = w₁² + w₂² − λ(w₁ + 2w₂ − 5)

**(b)** ∂ℒ/∂w₁ = 2w₁ − λ = 0 → w₁ = λ/2
∂ℒ/∂w₂ = 2w₂ − 2λ = 0 → w₂ = λ
Constraint: λ/2 + 2λ = 5 → 5λ/2 = 5 → **λ* = 2**

**w₁* = 1, w₂* = 2.** Optimal loss = 1 + 4 = **5**.

**(c)** λ* = 2 means relaxing by ε changes the optimal loss by ≈ **2ε**. The Lagrange multiplier is the "shadow price" — the rate at which the objective improves per unit of constraint relaxation.

**(d)** Alignment IS constrained optimization: maximize capability (task performance) **subject to safety constraints** (don't produce harmful outputs, follow instructions, be honest). The multiplier λ measures the **"alignment tax"** — how much capability you sacrifice per unit of safety. A large λ means safety is expensive; a small λ means capability and safety are nearly compatible. The dream of alignment research is to make λ as small as possible.

---

### Question 12 (12 pts) — Taylor Expansion, IFT, and Sensitivity

**(a)** f(w) ≈ f(w₀) + ½(w − w₀)ᵀ H(w₀)(w − w₀)

The linear term ∇f(w₀)ᵀ(w−w₀) vanishes because ∇f = 0 at a critical point. The Hessian H determines the **local quadratic shape** — it IS the loss landscape near the critical point.

**(b)** An extremely **elongated elliptical bowl**: steep along the eigenvector for λ₁ = 100 (curvature 100), and nearly flat along the eigenvector for λ₂ = 0.01 (curvature 0.01). Like a narrow canyon — very steep walls but nearly flat floor. Condition number: κ = 100/0.01 = **10,000**.

**(c)** Newton's update: **w_new = w − H⁻¹∇f(w)**

H⁻¹ rescales the gradient by the inverse curvature: steep directions (large eigenvalues) get their gradients shrunk; shallow directions (small eigenvalues) get their gradients amplified. This normalizes all directions to equal "effective curvature," eliminating zigzag.

Not used for large networks because: (1) H is d×d — for d = 10⁸ parameters, storing it requires ~10¹⁶ bytes, (2) inverting it costs O(d³), and (3) the Hessian may be indefinite at non-minimum critical points, making the step direction wrong.

**(d)** At (1,1): F(1,1) = 1 − 1 = 0 ✓.

∂F/∂w = 3w² − λ. At (1,1): ∂F/∂w = 3 − 1 = **2 ≠ 0** → IFT applies.

dw/dλ = −(∂F/∂λ)/(∂F/∂w) = −(−w)/(3w²−λ) = 1/2 = **0.5**.

At (0,0): ∂F/∂w = 0 − 0 = **0** → IFT fails.

When the IFT fails, the critical point structure changes qualitatively — this is a **bifurcation**. At (0,0), three solution branches (w = 0, w = ±√λ) meet. The loss landscape topology changes as λ crosses zero: one critical point becomes three. In SLT, singularities occur precisely where the IFT fails — these are the points where the RLCT is computed.

---

### Question 13 (10 pts) — Integration, Jacobians, and Probability Transforms

**(a)** Polar coordinates: x² + y² = r², dA = **r dr dθ** (the r is the Jacobian determinant |∂(x,y)/∂(r,θ)| = r).

∫₀^{2π} ∫₀^1 r² · r dr dθ = 2π · [r⁴/4]₀^1 = 2π/4 = **π/2**

**(b)** ∬f(x,y) dx dy = ∬ f(g⁻¹(u,v)) · |det J⁻¹| du dv, where J is the Jacobian matrix of the transformation.

The Jacobian determinant measures **local area scaling** — how much the transformation stretches or compresses infinitesimal area patches at each point. This is the same geometric meaning as the determinant from Lesson 7: det measures volume change under a linear map. The Jacobian applies this locally (at each point) rather than globally.

**(c)** Y = 3X + 2 → X = (Y−2)/3 → dx/dy = 1/3.

f_Y(y) = f_X((y−2)/3) · |1/3| = (1/√(2π)) exp(−(y−2)²/18) · (1/3)

This is **N(2, 9)** — mean 2, variance 3² = 9.

**(d)** The normalization integral of a multivariate Gaussian involves a change of variables that diagonalizes the covariance matrix using its eigenvectors. The Jacobian of this transformation involves det(Σ), which measures the "volume" of the ellipsoidal region where the Gaussian concentrates. Larger det(Σ) → more spread → lower peak to integrate to 1.

---

### Question 14 (12 pts) — The Bias-Variance Tradeoff and Loss Landscapes

**(a)** Error = **Bias²** + **Variance** + **Irreducible Noise**

**(b)** **Bias** dominates. A line (2 parameters) can't capture cubic curvature — it systematically underestimates the bends, regardless of how much data. Like a dartboard where all darts cluster around the wrong spot.

**(c)** **Variance** dominates. 1000 parameters on 20 points → extreme overfitting. Train on a different 20 points and you'd get a wildly different model. Like darts scattered all over the board.

**(d)** **Double descent.** Classical theory predicts monotonically increasing error past the interpolation threshold. But for very overparameterized models, error decreases again. Modern networks live in this regime where vastly more parameters than data improves generalization. SLT explains: the RLCT (effective complexity) is much smaller than parameter count, so the model isn't as complex as it appears.

**(e)** In d dimensions, for a local minimum ALL d Hessian eigenvalues must be positive. If each eigenvalue is independently positive or negative with equal probability, the chance is (1/2)^d. For d = 1000, that's ~10^{−301}. Essentially all critical points are **saddle points** with a mix of positive and negative eigenvalues.

**(f)** Three sets serve distinct purposes: **Training** fits parameters. **Validation** selects among models/hyperparameters (implicitly "training" on validation data). **Test** gives an unbiased performance estimate untouched by any decision. Without a separate test set, your reported performance is optimistically biased by the model selection process.

---

### Question 15 (12 pts) — Synthesis: The Complete Optimization Pipeline

**(a)** Momentum update:
- v_{t+1} = βv_t + ∇L(w_t) (accumulate gradient with decay)
- w_{t+1} = w_t − ηv_{t+1} (step using accumulated momentum)

Analogy: a **heavy ball rolling downhill**. In a ravine, the ball averages out side-to-side bouncing (which cancels over time) while accumulating speed along the valley floor (which reinforces). The ball's inertia also carries it past small bumps (shallow local minima).

**(b)** SGD noise helps **escape sharp minima**. The random perturbations from mini-batch sampling make sharp, narrow minima unstable (noise kicks the optimizer out), while broad, flat minima are stable (robust to perturbation). Since flat minima generalize better, SGD noise acts as **implicit regularization** — free regularization from the stochasticity.

**(c)** **Saddle point** (one negative eigenvalue: −0.001). It's nearly a minimum — the negative eigenvalue is tiny, so the escape direction is very gentle. The near-zero positive eigenvalue (0.01) indicates a **nearly flat direction** — characteristic of a loss landscape near a singularity. In SLT terms, this flat direction corresponds to a near-symmetry where different parameters produce nearly identical functions.

**(d)**

| Step | Calculus Tool (Phase 2) | Linear Algebra Foundation (Phase 1) |
|------|------------------------|--------------------------------------|
| Computing direction to step | **Gradient** (∇L) | **Vectors** (gradient is a vector in parameter space) |
| Propagating through layers | **Chain rule** (backprop) | **Matrix multiplication** (each layer's Jacobian) |
| Classifying critical points | **Hessian eigenvalues** | **Eigenvalue decomposition** (Lesson 8) |
| Understanding local shape | **Taylor expansion** (2nd order) | **Quadratic forms** (wᵀHw from Phase 1) |
| Handling constraints | **Lagrange multipliers** | **Projections** (constraint = projecting onto feasible set) |

**(e)** **Jacobian determinant** (Lesson 20): the correction factor when transforming probability densities. Appears in normalizing flows, Gaussian normalization, and change of variables. It's the local volume-scaling factor.

**Hessian determinant** (Lessons 19, 21): its sign (via eigenvalue products) helps classify critical points. det(H) > 0 means eigenvalues share a sign; det(H) < 0 means saddle point. Its magnitude relates to the "tightness" of the local basin.
