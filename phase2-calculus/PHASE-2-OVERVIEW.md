# Phase 2 Overview: Calculus, Multivariable Calculus & Differential Equations — Every Concept and Method

> **Purpose:** Exhaustive reference of every concept, technique, and method covered in Phase 2 (Lessons 13–30), organized by block. Includes supplementary topics from standard Calc III/IV courses (marked with ⊕) that go beyond what the lessons focus on but provide useful background, particularly from Dr. Trefor Bazett's multivariable and vector calculus playlists.

---

## Block A: Pure Calculus & Multivariable Foundations (Lessons 13–19)

### Lesson 13: Calculus Fundamentals — Rebuilding Your Intuition

**Derivatives:**
- Derivative as instantaneous rate of change — slope of the tangent line
- Limit definition: f'(x) = lim_{h→0} [f(x+h) − f(x)] / h
- Secant lines → tangent lines as h → 0
- "Zooming in" intuition: smooth curves look linear at sufficient magnification (local linearity)
- Differentials dx, dy as actual tiny quantities

**Differentiation Rules:**
- Power rule: d/dx xⁿ = nxⁿ⁻¹
- Constant multiple and sum rules (derivative is a linear operator)
- Product rule: (fg)' = f'g + fg' (rectangle area geometric proof)
- Quotient rule: (f/g)' = (f'g − fg')/g²
- Chain rule: d/dx f(g(x)) = f'(g(x))·g'(x) — the single most important rule for ML

**Key Functions and Their Derivatives:**
- eˣ → eˣ (its own derivative; appears in softmax, log-likelihood, exponential decay)
- ln(x) → 1/x (appears in cross-entropy, log-likelihood, information theory)
- Logarithmic derivative: d/dx ln(f(x)) = f'(x)/f(x) (relative rate of change)
- sin(x) → cos(x), cos(x) → −sin(x) (positional encodings, Fourier features)
- Sigmoid σ(x) = 1/(1+e⁻ˣ): σ'(x) = σ(x)(1−σ(x)), max derivative = 0.25 → vanishing gradients
- tanh(x): output in (−1,1), tanh'(x) = 1 − tanh²(x)
- ReLU(x) = max(0,x): derivative is 0 or 1 (no gradient shrinkage but dead neurons)
- Leaky ReLU, GELU, SiLU (Swish) variants
- Softplus: ln(1 + eˣ) — smooth ReLU approximation

**Integration:**
- Definite integral ∫ₐᵇ f(x)dx = signed area under curve
- Riemann sums: left, right, midpoint, trapezoidal approximations
- Fundamental Theorem of Calculus Part 1: d/dx ∫ₐˣ f(t)dt = f(x)
- Fundamental Theorem of Calculus Part 2: ∫ₐᵇ f(x)dx = F(b) − F(a) where F' = f
- Antiderivatives (indefinite integrals) + constant of integration (+C)
- Standard antiderivative table: xⁿ, 1/x, eˣ, sin, cos, etc.

**Integration Techniques:**
- u-substitution (reverse chain rule)
- Integration by parts: ∫u dv = uv − ∫v du (reverse product rule)
- Partial fractions (for rational functions)
- Trigonometric substitutions and identities
- Improper integrals: convergence/divergence over unbounded domains

**Limits, Continuity, and Foundational Theorems:**
- Limits: formal ε-δ definition (conceptual), one-sided limits
- Continuity at a point: lim_{x→a} f(x) = f(a)
- L'Hôpital's rule for 0/0 and ∞/∞ indeterminate forms
- Squeeze theorem
- Intermediate Value Theorem (IVT)
- Mean Value Theorem (MVT): ∃c ∈ (a,b) where f'(c) = [f(b)−f(a)]/(b−a)
- Extreme Value Theorem: continuous f on closed [a,b] attains max and min

**Optimization (Single Variable):**
- Critical points: f'(x) = 0 or undefined
- Second derivative test: f'' > 0 → local min, f'' < 0 → local max, f'' = 0 → inconclusive
- Concavity: f'' > 0 = concave up (bowl), f'' < 0 = concave down (hill)
- Inflection points: where concavity changes

**Sequences and Series:**
- Sequences: convergence, divergence, bounded, monotone
- Series: Σaₙ, partial sums, geometric series (a/(1−r) when |r|<1)
- Convergence tests: ratio test, comparison test, integral test, root test
- Power series: Σaₙxⁿ, radius of convergence
- Taylor/Maclaurin series (expanded in Lesson 17)

---

### Lesson 14: Partial Derivatives and Gradients

**Partial Derivatives:**
- ∂f/∂xᵢ: rate of change when wiggling one input, holding others fixed
- Notation: fₓ, f_y, ∂f/∂x, ∂₁f
- Geometric interpretation: slope of the slice of the surface along one axis
- Higher-order partials: fₓₓ, f_yy, fₓᵧ (mixed partials)
- **Clairaut's theorem (symmetry of mixed partials):** fₓᵧ = f_yₓ when both are continuous

**The Gradient:**
- ∇f = (∂f/∂x₁, ..., ∂f/∂xₙ) — collects all partial derivatives into a vector
- **Points in the direction of steepest ascent** (negative gradient = steepest descent)
- **Perpendicular to level curves (contour lines)**
- Magnitude ||∇f|| = rate of steepest ascent
- Gradient field: vector field of ∇f at every point

**Directional Derivatives:**
- D_u f = ∇f · û — rate of change in arbitrary direction û
- Maximum when û aligns with ∇f; zero when û is perpendicular (along contour)

⊕ **Supplementary — Standard Calc III Topics:**
- ⊕ **3D coordinate systems:** Cartesian, right-hand rule, distance formula in 3D
- ⊕ **Quadric surfaces:** ellipsoids, paraboloids, hyperboloids, cones, cylinders — the "zoo" of 3D shapes defined by degree-2 equations
- ⊕ **Level surfaces** (3D analog of level curves): f(x,y,z) = c
- ⊕ **Tangent planes:** z − z₀ = fₓ(x₀,y₀)(x−x₀) + f_y(x₀,y₀)(y−y₀)
- ⊕ **Linear approximation in multiple variables:** f(x) ≈ f(a) + ∇f(a)·(x−a)
- ⊕ **Optimization in several variables (no constraints):** critical points where ∇f = 0, second derivative test via the Hessian discriminant D = fₓₓf_yy − fₓᵧ²

---

### Lesson 15: The Multivariable Chain Rule and Jacobian Matrices

**Chain Rule Generalizations:**
- Single-variable chain rule: d/dx f(g(x)) = f'(g(x))·g'(x)
- **Multivariable chain rule:** ∂f/∂t = Σᵢ (∂f/∂xᵢ)(∂xᵢ/∂t) — sum over all paths in the dependency tree
- Chain rule with multiple intermediate and multiple independent variables
- **Tree diagrams** for tracking which variables depend on which

**The Jacobian Matrix:**
- For F: ℝⁿ → ℝᵐ, the Jacobian J is the m×n matrix of all partial derivatives: Jᵢⱼ = ∂Fᵢ/∂xⱼ
- The Jacobian IS the total derivative — the best linear approximation to F near a point
- Jacobian generalizes: scalar gradient (1×n), derivative (1×1), and matrix calculus
- **Composition of Jacobians:** J_{F∘G} = J_F · J_G (chain rule as matrix multiplication)

**Key Matrix Calculus Results:**
- ∂/∂x (Ax) = A
- ∂/∂x (xᵀAx) = (A + Aᵀ)x (= 2Ax when A symmetric)
- ∂/∂X tr(AX) = Aᵀ
- Numerator layout vs denominator layout conventions

**The Hessian:**
- Second-order partial derivative matrix: Hᵢⱼ = ∂²f/∂xᵢ∂xⱼ
- Always symmetric (by Clairaut's theorem)
- Eigenvalues = curvature in each eigendirection
- Positive definite H → local minimum; negative definite → local maximum; mixed → saddle
- **Condition number** κ = λ_max/λ_min — measures elongation of the loss landscape

⊕ **Supplementary — Standard Calc III Topics:**
- ⊕ **Vector-valued functions:** r(t) = (x(t), y(t), z(t)) — parametric curves in space
- ⊕ **Derivatives of vector functions:** r'(t) = tangent vector, velocity
- ⊕ **Integrals of vector functions**
- ⊕ **Arc length:** L = ∫ ||r'(t)|| dt
- ⊕ **Curvature:** κ = ||r'×r''|| / ||r'||³ — how fast the curve bends
- ⊕ **TNB frame:** tangent, normal, and binormal unit vectors (Frenet-Serret formulas)
- ⊕ **Velocity and acceleration:** tangential and normal components

---

### Lesson 16: Multiple Integration and Change of Variables

**Double and Triple Integrals:**
- Double integral ∬_D f(x,y) dA: volume under surface over region D
- Triple integral ∭_E f(x,y,z) dV: integral over 3D region
- **Iterated integrals:** evaluate by integrating one variable at a time
- **Fubini's theorem:** order of integration can be swapped (when integrand is continuous)
- Setting up integration bounds for non-rectangular regions

**Coordinate Systems and Change of Variables:**
- **Polar coordinates:** (r, θ), dA = r dr dθ
- **Cylindrical coordinates:** (r, θ, z), dV = r dr dθ dz
- **Spherical coordinates:** (ρ, θ, φ), dV = ρ² sin φ dρ dθ dφ
- **General change of variables formula:** ∬ f(x,y) dA = ∬ f(g(u,v)) |det(J)| du dv
- **Jacobian determinant** |det(∂(x,y)/∂(u,v))| measures local area/volume stretching

**Key Integrals:**
- **The Gaussian integral:** ∫_{-∞}^{∞} e^{-x²} dx = √π (proved via polar coordinates)
- **Multivariate Gaussian normalization** involves det(Σ) and the Jacobian

**ML Connection:**
- **Monte Carlo integration:** approximate ∫f(x)p(x)dx by sampling from p and averaging f
- **Importance sampling:** sample from proposal q, reweight by p/q
- **Normalizing flows** = chain of invertible transformations with tracked Jacobian determinants
- **Reparameterization trick** in VAEs: z = μ + σε allows backprop through sampling
- Change of variables for probability densities: p(y) = p(f⁻¹(y))|det(J_{f⁻¹})|

⊕ **Supplementary — Standard Calc III Topics:**
- ⊕ **Applications of double integrals:** area, volume, mass, center of mass, moments of inertia
- ⊕ **Applications of triple integrals:** volume, mass of 3D solids
- ⊕ **Surface area** of z = f(x,y): ∬√(1 + fₓ² + f_y²) dA

---

### Lesson 17: Taylor Expansions and the Implicit Function Theorem

**Taylor Series (Single Variable):**
- f(x) ≈ f(a) + f'(a)(x−a) + ½f''(a)(x−a)² + (1/3!)f'''(a)(x−a)³ + ...
- Zeroth order: constant approximation
- First order: linear approximation (tangent line) — this is what gradient descent uses
- Second order: quadratic approximation — this is what Newton's method uses
- **Maclaurin series:** Taylor series centered at a = 0
- Key series: eˣ = 1 + x + x²/2! + ...; sin x = x − x³/3! + ...; 1/(1−x) = 1 + x + x² + ...

**Multivariate Taylor Expansion:**
- f(w) ≈ f(w₀) + ∇f(w₀)ᵀ(w−w₀) + ½(w−w₀)ᵀH(w₀)(w−w₀) + ...
- At critical points (∇f = 0): the local landscape IS the quadratic form of the Hessian
- Hessian eigenvalues completely determine local geometry at critical points

**Implicit Function Theorem (IFT):**
- When F(x,y) = 0 defines y implicitly as a function of x
- IFT gives: dy/dx = −(∂F/∂x)/(∂F/∂y) when ∂F/∂y ≠ 0
- **Fails at singularities** (where ∂F/∂y = 0) → bifurcation points
- Connection to SLT: singularities in the parameter-function map are where IFT breaks down

**Big-O Notation:**
- f(x) = O(g(x)) means |f(x)| ≤ C|g(x)| for large enough x
- Used for truncation error bounds in Taylor approximation
- Scaling laws expressed in asymptotic notation

---

### Lesson 18: Vector Calculus — Fields, Divergence, Curl, and the Laplacian

**Vector Fields:**
- A vector field F assigns a vector to every point in space: F(x,y) = (P(x,y), Q(x,y))
- Visualization: arrow at each point showing direction and magnitude
- Gradient fields: ∇φ for some scalar φ — a special class of vector fields

**Conservative Vector Fields and Potential Functions:**
- F is conservative if F = ∇φ for some scalar potential φ
- Equivalent: line integrals path-independent; closed loop integrals = 0
- Test in 2D: ∂P/∂y = ∂Q/∂x (curl = 0)
- Finding the potential: integrate P w.r.t. x, match with Q
- Gradient descent follows a conservative field (loss = potential)

**Divergence:**
- div(F) = ∇ · F = ∂P/∂x + ∂Q/∂y + ∂R/∂z (scalar output)
- Measures net outward flux per unit volume — sources (+) and sinks (−)
- div(∇f) = ∇²f = the Laplacian

**Curl:**
- curl(F) = ∇ × F (vector output in 3D, scalar in 2D)
- Measures local rotation/circulation
- curl(∇φ) = 0 always — gradient fields have no rotation
- If curl(F) = 0 on simply connected domain → F is conservative

**The Laplacian:**
- ∇²f = ∂²f/∂x² + ∂²f/∂y² + ... (sum of unmixed second partials)
- Measures how much f(x) deviates from the average of its neighbors
- ∇²f = 0 → harmonic function (value at center = average over surrounding sphere)
- Appears in: heat equation, Fokker-Planck equation, diffusion models, score matching

**Vector Calculus Identities:**
- div(curl F) = 0 always
- curl(grad f) = 0 always
- ∇²F = ∇(∇·F) − ∇×(∇×F)

⊕ **Supplementary — Standard Calc III/IV Topics (Bazett's Playlists):**
- ⊕ **Parametric surfaces:** r(u,v) = (x(u,v), y(u,v), z(u,v))
- ⊕ **Surface area for parametric surfaces:** ∬ ||r_u × r_v|| du dv
- ⊕ **Orientable vs non-orientable surfaces** (Möbius strip)
- ⊕ **Flux of a vector field across a surface:** ∬_S F · dS = ∬_S F · (r_u × r_v) du dv

---

### Lesson 19: The Fundamental Theorems of Vector Calculus

**The Unifying Principle:**
- In every dimension: ∫_Ω (derivative of F) dΩ = ∮_{∂Ω} F d(∂Ω)
- Integrating a derivative over a region = evaluating the original on the boundary
- Local information (derivatives) ↔ global information (integrals)

**Line Integrals:**
- Scalar line integral: ∫_C f ds = ∫ₐᵇ f(r(t)) ||r'(t)|| dt (total along a curve)
- Vector line integral (work): ∫_C F · dr = ∫ₐᵇ F(r(t)) · r'(t) dt
- **Fundamental Theorem for Line Integrals:** if F = ∇φ, then ∫_C F · dr = φ(end) − φ(start)

**Green's Theorem (2D):**
- ∮_C (P dx + Q dy) = ∬_D (∂Q/∂x − ∂P/∂y) dA
- Circulation around boundary = integral of curl over interior
- Divergence form: ∮_C F · n̂ ds = ∬_D div(F) dA

**Stokes' Theorem (3D, Surfaces):**
- ∮_C F · dr = ∬_S (curl F) · dS
- Circulation around boundary curve = flux of curl through the surface
- Generalizes Green's theorem to 3D surfaces

**Divergence Theorem (3D, Volumes):**
- ∯_S F · dS = ∭_E div(F) dV
- Total outward flux through closed surface = integral of divergence over enclosed volume
- Generalizes Green's divergence form to 3D

**The Hierarchy:**
- FTC (1D) → Fundamental Theorem for Line Integrals → Green's (2D) → Stokes' (surfaces) → Divergence (3D volumes)
- All are instances of the generalized Stokes' theorem: ∫_Ω dω = ∫_{∂Ω} ω

⊕ **Supplementary — Computational Methods from Standard Calc IV (Bazett's Playlists):**
- ⊕ **Computing line integrals step by step:** parameterize the curve, substitute, integrate
- ⊕ **Evaluating surface integrals:** parameterize surface, compute normal vector, integrate
- ⊕ **Surface integrals for implicit and explicit surfaces**
- ⊕ **Verifying Stokes' Theorem:** compute both sides and check equality
- ⊕ **Applications of Divergence Theorem:** Gauss's Law for electric flux, fluid flow
- ⊕ **Arclength parameterization** of curves
- ⊕ **Circulation and flux integrals** as separate computations
- ⊕ **Finding scalar potential functions** for conservative fields (systematic integration method)
- ⊕ **Testing if a 3D field is conservative:** curl F = 0 + simply connected domain

---

## Block B: Differential Equations & Dynamical Systems (Lessons 20–25)

### Lesson 20: Introduction to ODEs — Rates of Change as Vector Fields

**What Is an ODE:**
- dx/dt = f(x, t) — a rule: given where you are, here's how fast and which direction you're moving
- First-order (dx/dt), second-order (d²x/dt²), systems of ODEs
- Autonomous (f doesn't depend on t explicitly) vs non-autonomous

**Geometric Picture:**
- Vector field: arrows at every point showing direction/speed of flow
- Solution curves (trajectories): paths that follow the arrows
- Phase line (1D): arrows on a number line showing direction of flow

**Fixed Points and Stability (1D):**
- Fixed point x*: where f(x*) = 0 (flow stops)
- Stable: f'(x*) < 0 (nearby trajectories converge)
- Unstable: f'(x*) > 0 (nearby trajectories diverge)

**Existence and Uniqueness:**
- If f is Lipschitz continuous, each initial condition gives exactly one trajectory
- Deterministic training trajectory (in continuous limit) from a given initialization

**Gradient Descent as an ODE:**
- Discrete: W_{t+1} = W_t − η∇L(W_t)
- Continuous limit (η → 0): dW/dt = −∇L(W)
- **Euler's method:** x_{n+1} = x_n + h·f(x_n) IS gradient descent with h = η

⊕ **Supplementary — Standard ODE Methods (Bazett's Calc IV):**
- ⊕ **Separable ODEs:** dy/dx = g(x)h(y) → ∫dy/h(y) = ∫g(x)dx
- ⊕ **First-order linear ODEs:** dy/dx + P(x)y = Q(x), integrating factor μ = e^{∫P dx}
- ⊕ **Exact equations:** M dx + N dy = 0 where ∂M/∂y = ∂N/∂x
- ⊕ **Second-order linear ODEs with constant coefficients:** ay'' + by' + cy = 0, characteristic equation ar² + br + c = 0
- ⊕ **Undetermined coefficients and variation of parameters** (particular solutions)
- ⊕ **Initial value problems vs boundary value problems**

---

### Lesson 21: Linear Systems and Phase Portraits

**Linear Systems:**
- dx/dt = Ax where A is a constant matrix
- Solution: x(t) = e^{At}x(0) = c₁e^{λ₁t}v₁ + c₂e^{λ₂t}v₂
- **Matrix exponential:** e^{At} = I + At + (At)²/2! + ...
- Behavior completely determined by eigenvalues of A

**Phase Portrait Classification:**
- Both eigenvalues negative real → **stable node** (all trajectories converge)
- Both positive real → **unstable node** (all diverge)
- Opposite signs → **saddle point** (converge along one eigendirection, diverge along other)
- Complex with Re(λ) < 0 → **stable spiral** (converge while rotating)
- Complex with Re(λ) > 0 → **unstable spiral**
- Complex with Re(λ) = 0 → **center** (closed orbits, no convergence or divergence)

**Linearization:**
- Near a fixed point, nonlinear system ≈ linear system dx/dt = Jx where J = Jacobian at x*
- **Hartman-Grobman theorem:** if eigenvalues of J have nonzero real part (hyperbolic), the nonlinear phase portrait is topologically equivalent to the linear one near x*
- **Basins of attraction:** regions of initial conditions that converge to a given stable fixed point
- **Separatrices:** boundaries between basins of attraction

**ML Connection:**
- Condition number = ratio of eigenvalue magnitudes → mismatched convergence speeds → zigzagging
- Adam/preconditioning: effectively equalize eigenvalues for uniform convergence

---

### Lesson 22: Gradient Flow and Training Dynamics

**Gradient Flow:**
- dW/dt = −∇L(W) — the continuous-time limit of gradient descent
- **Loss as Lyapunov function:** dL/dt = −||∇L||² ≤ 0 (loss always decreases along flow)
- One-line proof: dL/dt = ∇L · (dW/dt) = ∇L · (−∇L) = −||∇L||²

**Stability and Learning Rate:**
- **Euler stability criterion:** η < 2/λ_max (learning rate must be below this threshold)
- Too large → oscillation and divergence; too small → slow convergence

**Momentum:**
- Momentum as second-order ODE: d²W/dt² + γ dW/dt = −∇L (damped ball rolling on loss surface)
- Helps with ill-conditioning: cancels zigzag along elongated valleys
- Nesterov momentum: look ahead before computing gradient

**Implicit Regularization:**
- Gradient descent from small initialization → minimum-norm solution
- For deep linear networks → biases toward low-rank solutions
- **Learning rate as temperature:** larger η → more noise → escapes sharp minima, prefers flat ones
- **SGD noise:** σ² ∝ η/B (noise scales with learning rate / batch size)

---

### Lesson 23: Stability, Lyapunov Functions, and Phase Transitions

**Lyapunov Stability Theory:**
- Find V(x) > 0 with V(x*) = 0 and dV/dt ≤ 0 → x* is stable
- If dV/dt < 0 (strict) → asymptotically stable (trajectories converge)
- For gradient flow, the loss L is a "free" Lyapunov function

**Bifurcations:**
- Qualitative behavior changes as a parameter varies
- **Saddle-node bifurcation:** two fixed points collide and annihilate
- **Pitchfork bifurcation:** symmetry breaking, one fixed point → three
- **Transcritical bifurcation:** two fixed points exchange stability
- **Hopf bifurcation:** fixed point loses stability, limit cycle appears

**Phase Transitions in Training:**
- Sudden qualitative changes: loss drops, capabilities emerge
- **Grokking:** memorization phase → sudden generalization (saddle escape)
- **Emergent capabilities:** abrupt appearance of skills at certain model scales
- **SLT phase transitions:** RLCT jumps correspond to capability acquisition
- **Local Learning Coefficient (LLC):** estimable RLCT that tracks phase transitions during training

**Attractors:**
- Fixed points, limit cycles, strange attractors (chaos)
- Gradient systems can't have limit cycles (Strogatz), but SGD can oscillate

---

### Lesson 24: Neural ODEs and Stochastic Dynamics

**Neural ODEs:**
- ResNets as Euler steps: x_{l+1} = x_l + f_θ(x_l) approximates dx/dt = f_θ(x)
- Neural ODE framework: parameterize f_θ, solve with adaptive ODE solvers (Dormand-Prince, etc.)
- **Adjoint method:** O(1) memory backprop through the ODE solver (constant memory regardless of depth)
- Advantages: continuous depth, adaptive computation
- Limitations: sequential solving (no parallelism), homeomorphism constraint (can't change topology)
- **Continuous normalizing flows:** d(log p)/dt = −tr(∂f/∂x) (Hutchinson trace estimator for efficiency)

**Stochastic Dynamics:**
- **SDEs:** dW = −∇L dt + σ dB_t (gradient flow + Brownian noise)
- SGD ≈ noisy gradient flow; mini-batch noise ∝ η/B
- **Fokker-Planck equation:** describes how the probability distribution P(W) evolves over time
- Stationary distribution: P(W) ∝ exp(−L(W)/T) (Boltzmann-like)
- Large learning rate → high temperature → sharp minima destabilized → preference for flat minima

**Edge of Stability:**
- Training at η ≈ 2/λ_max: an inherently discrete-time effect
- Sharpness (top Hessian eigenvalue) self-tunes to match learning rate
- Simulated annealing connection: learning rate schedule = cooling schedule

---

### Lesson 25: PDEs — Diffusion, Heat Equation, and Generative Models

**Heat Equation:**
- u_t = k∇²u — the Laplacian drives diffusion
- Solution: convolution with Gaussian kernel (Gaussian blurring over time)
- High-frequency modes decay fastest → smoothing effect

**Diffusion Models Connection:**
- Forward process = progressive noise addition (adding Gaussian noise = running heat equation)
- Reverse process requires learning the score function ∇_x log p(x)
- **Score matching:** learn score without computing normalization constant
- **Reverse SDE:** requires learned score to denoise
- **Probability flow ODE:** deterministic version of reverse SDE
- Generation goes coarse-to-fine (large structure first, details last)

**Fokker-Planck Equation:**
- ∂p/∂t = −∂(fp)/∂x + (σ²/2)∂²p/∂x²
- Describes probability distribution over weight space during SGD
- Drift (gradient descent) + diffusion (noise)

**Other PDE Topics:**
- Separation of variables for linear PDEs
- Fourier series for periodic solutions
- Wave equation (contrast with diffusion: waves propagate, heat diffuses)

---

## Block C: ML-Applied Calculus (Lessons 26–30)

### Lesson 26: Matrix Calculus — Bridging to Backpropagation

- Partial derivatives extended to vectors and matrices
- **Gradient vector** ∇f for scalar-valued functions of vectors
- **Jacobian matrix** for vector-valued functions of vectors
- Key matrix calculus identities: ∂(Ax)/∂x = A; ∂(xᵀAx)/∂x = (A+Aᵀ)x; ∂tr(AX)/∂X = Aᵀ
- Numerator vs denominator layout conventions
- Taylor series with matrix arguments: f(x+δ) ≈ f(x) + ∇f(x)ᵀδ + ½δᵀHδ
- Linearization: why gradient descent works (trusting the first-order approximation)

---

### Lesson 27: The Chain Rule — This IS Backpropagation

- Single-variable and multivariable chain rule
- **Computation graphs:** neural networks as DAGs of simple differentiable operations
- Each node: stores value (forward) and local derivative (backward)
- **Forward pass:** compute values from inputs to loss
- **Backward pass:** compute gradients from loss to parameters
- **Reverse-mode autodiff** vs **forward-mode autodiff:** reverse is O(1) per output (perfect for many params, one loss), forward is O(1) per input
- Building a tiny autograd engine (micrograd-style)

---

### Lesson 28: Optimization and Gradient Descent

- **Vanilla gradient descent:** W ← W − η∇L(W)
- **Stochastic gradient descent (SGD):** use mini-batch gradient estimates
- **Learning rate:** too big = overshoot/diverge, too small = slow
- **Learning rate schedules:** step decay, cosine annealing, warmup
- **Momentum:** v ← βv + ∇L; W ← W − ηv (accumulate velocity)
- **Nesterov momentum:** evaluate gradient at look-ahead position
- **AdaGrad:** adaptive per-parameter learning rates (divide by sqrt of sum of squared gradients)
- **RMSProp:** fix AdaGrad's diminishing learning rates with exponential moving average
- **Adam:** momentum + RMSProp + bias correction — the default optimizer
- **AdamW:** Adam with decoupled weight decay
- **Convexity:** f convex → every local min is global min; neural networks are NON-convex
- Building micrograd (Karpathy) as a practical exercise

---

### Lesson 29: Constrained Optimization and Lagrange Multipliers

- **Constrained optimization:** minimize f(x) subject to g(x) = 0
- **Geometric insight:** at the optimum, ∇f and ∇g are parallel (contour lines tangent to constraint)
- **Lagrangian:** L(x, λ) = f(x) − λg(x); solve ∇_x L = 0 and ∇_λ L = 0
- λ = the Lagrange multiplier = "shadow price" of the constraint
- **Multiple equality constraints:** one λ per constraint
- **Inequality constraints → KKT conditions:** complementary slackness (λᵢgᵢ = 0), λᵢ ≥ 0
- **Convex optimization:** every local minimum is global; efficient algorithms exist
- **Duality:** primal problem ↔ dual problem; weak and strong duality
- **Regularization as soft constraint:** L2 penalty ||w||² ≤ C ↔ Lagrange multiplier λ is the regularization strength
- SVMs are derived via the dual of a constrained optimization problem
- Slater's condition for strong duality

---

### Lesson 30: Loss Landscapes and Local Minima

- Loss function as a surface over all parameters (very high-dimensional)
- **Local minima, saddle points, plateaus** — the landscape features
- **In high dimensions: saddle points dominate**, not local minima (random matrix theory argument)
- Hessian eigenvalue analysis: all positive → minimum, all negative → maximum, mixed → saddle
- **Bias-variance tradeoff:** total error = bias² + variance + irreducible noise
- **Double descent:** test error goes down, up, then down again as model complexity increases past interpolation threshold
- **Grokking:** delayed generalization long after memorization (phase transition in training dynamics)
- **Cross-validation:** k-fold for estimating generalization performance
- **Model selection criteria:** AIC, BIC (and their failure for singular models)
- Condition number determines gradient descent behavior (zigzagging in elongated valleys)
- **Sharp vs flat minima** and generalization (flat minima may generalize better)

---

## Assessments

- **Exam 2A: Calculus & Optimization** (Lessons 13–19, Block A + C concepts) — 90 min
- **Exam 2B: Differential Equations** (Lessons 20–25, Block B) — 60 min
