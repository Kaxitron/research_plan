# Spaced Repetition System — Research Plan Topics

> **How to use:** Each topic below is a spaced repetition candidate. Track review dates and intervals using the SM-2 algorithm or similar. Topics are extracted from the phase overviews and represent discrete, reviewable units of knowledge.
>
> **Interval schedule (SM-2 style):** 1 day → 3 days → 7 days → 14 days → 30 days → 60 days
>
> **Rating scale:** 0 (blackout) — 5 (perfect recall)

---

## Phase 0B: CS Foundations — NeetCode Roadmap (Lessons CS01–CS10)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 0B-01 | Arrays & Hashing | | | 1d | 2.5 |
| 0B-02 | Two Pointers | | | 1d | 2.5 |
| 0B-03 | Stack | | | 1d | 2.5 |
| 0B-04 | Binary Search | | | 1d | 2.5 |
| 0B-05 | Sliding Window | | | 1d | 2.5 |
| 0B-06 | Linked List | | | 1d | 2.5 |
| 0B-07 | Trees | | | 1d | 2.5 |
| 0B-08 | Tries | | | 1d | 2.5 |
| 0B-09 | Backtracking | | | 1d | 2.5 |
| 0B-10 | Heap / Priority Queue | | | 1d | 2.5 |
| 0B-11 | Graphs | | | 1d | 2.5 |
| 0B-12 | 1-D DP | | | 1d | 2.5 |
| 0B-13 | Intervals | | | 1d | 2.5 |
| 0B-14 | Greedy | | | 1d | 2.5 |
| 0B-15 | Advanced Graphs | | | 1d | 2.5 |
| 0B-16 | 2-D DP | | | 1d | 2.5 |
| 0B-17 | Bit Manipulation | | | 1d | 2.5 |
| 0B-18 | Math & Geometry | | | 1d | 2.5 |

---

## Phase 1: Linear Algebra (Lessons 02–12)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 1-01 | Vectors as arrows vs ordered lists — geometric and algebraic viewpoints | | | 1d | 2.5 |
| 1-02 | Vector operations — addition, scalar multiplication, linear combinations | | | 1d | 2.5 |
| 1-03 | Magnitude ‖v‖, unit vectors v̂ = v/‖v‖, normalization | | | 1d | 2.5 |
| 1-04 | Vectors as embeddings — words, tokens, and data points as high-dimensional vectors | | | 1d | 2.5 |
| 1-05 | Component representation — standard basis vectors e₁, e₂, …, eₙ | | | 1d | 2.5 |
| 1-06 | Linear combinations a₁v₁ + a₂v₂ + … + aₖvₖ — weights and weighted sums | | | 1d | 2.5 |
| 1-07 | Span — the set of all linear combinations, generating a subspace | | | 1d | 2.5 |
| 1-08 | Linear independence — no vector is a linear combination of the others | | | 1d | 2.5 |
| 1-09 | Basis and dimension — minimal spanning set, dim = number of basis vectors | | | 1d | 2.5 |
| 1-10 | Superposition hypothesis — neural nets encoding more features than dimensions | | | 1d | 2.5 |
| 1-11 | Subspaces — definition, closure under addition and scalar multiplication | | | 1d | 2.5 |
| 1-12 | Linear transformations — definition, L(αu + βv) = αL(u) + βL(v) | | | 1d | 2.5 |
| 1-13 | Matrix as a linear transformation — columns are images of basis vectors | | | 1d | 2.5 |
| 1-14 | Types of transforms — rotation, reflection, scaling, shear, projection | | | 1d | 2.5 |
| 1-15 | Affine vs linear — translation breaks linearity, neural network layers as affine | | | 1d | 2.5 |
| 1-16 | Non-square matrices change dimension — ℝⁿ → ℝᵐ where m ≠ n | | | 1d | 2.5 |
| 1-17 | Matrix multiplication — four views: dot product, columns, rows, outer product | | | 1d | 2.5 |
| 1-18 | Composition of transformations — AB means "apply B first, then A" | | | 1d | 2.5 |
| 1-19 | Transpose Aᵀ — (AB)ᵀ = BᵀAᵀ, symmetric matrices | | | 1d | 2.5 |
| 1-20 | Matrix inverse A⁻¹ — existence, (AB)⁻¹ = B⁻¹A⁻¹, computing via row reduction | | | 1d | 2.5 |
| 1-21 | Properties — non-commutative, associative, distributive | | | 1d | 2.5 |
| 1-22 | QK and OV circuits — attention as matrix compositions W_Q^T W_K and W_O W_V | | | 1d | 2.5 |
| 1-23 | Column space C(A) and row space C(Aᵀ) — what the matrix can reach | | | 1d | 2.5 |
| 1-24 | Null space N(A) and left null space N(Aᵀ) — what gets crushed to zero | | | 1d | 2.5 |
| 1-25 | Rank — dim(column space) = dim(row space) = number of pivots | | | 1d | 2.5 |
| 1-26 | Rank-nullity theorem — rank + nullity = n, information preserved vs destroyed | | | 1d | 2.5 |
| 1-27 | Gaussian elimination — row reduction, pivots, RREF, solving Ax = b | | | 1d | 2.5 |
| 1-28 | Low-rank structure in ML — attention heads (768→64→768), LoRA | | | 1d | 2.5 |
| 1-29 | Four fundamental subspaces — orthogonality relations, complete picture | | | 1d | 2.5 |
| 1-30 | Determinant — volume scaling factor, orientation (sign), det = 0 ↔ singular | | | 1d | 2.5 |
| 1-31 | Determinant properties — det(AB) = det(A)det(B), det(Aᵀ) = det(A), det(cA) = cⁿdet(A) | | | 1d | 2.5 |
| 1-32 | Computing determinants — cofactor expansion, row reduction to triangular form | | | 1d | 2.5 |
| 1-33 | Jacobian determinant — det(J) as local volume change, normalizing flows, VAEs | | | 1d | 2.5 |
| 1-34 | Vanishing/exploding gradients relate to Jacobian determinants near 0 or very large | | | 1d | 2.5 |
| 1-35 | Eigenvalues and eigenvectors — Av = λv, stretching along invariant directions | | | 1d | 2.5 |
| 1-36 | Characteristic equation det(A − λI) = 0, finding eigenspaces | | | 1d | 2.5 |
| 1-37 | Diagonalization A = PDP⁻¹ — matrix powers Aⁿ = PDⁿP⁻¹ | | | 1d | 2.5 |
| 1-38 | Special cases — symmetric (real eigenvalues, orthogonal eigenvectors), complex eigenvalues, repeated | | | 1d | 2.5 |
| 1-39 | Eigenvalue facts — tr(A) = Σλ, det(A) = Πλ, eigenvalues of A⁻¹ are 1/λᵢ | | | 1d | 2.5 |
| 1-40 | PCA and Hessian eigenvalues — directions of maximum variance, loss curvature | | | 1d | 2.5 |
| 1-41 | SVD decomposition A = UΣVᵀ — exists for any matrix, any shape | | | 1d | 2.5 |
| 1-42 | SVD components — V (input rotation), Σ (singular values σ₁ ≥ σ₂ ≥ …), U (output rotation) | | | 1d | 2.5 |
| 1-43 | SVD properties — rank = nonzero σᵢ, connection to eigenvalues of AᵀA and AAᵀ | | | 1d | 2.5 |
| 1-44 | Eckart-Young theorem — best rank-k approximation, truncated SVD | | | 1d | 2.5 |
| 1-45 | SVD vs eigendecomposition — any matrix vs square only, for symmetric matrices they coincide | | | 1d | 2.5 |
| 1-46 | SVD in ML — PCA, LoRA, image compression, low-rank attention | | | 1d | 2.5 |
| 1-47 | Dot product — a·b = ‖a‖‖b‖cos θ, algebraic and geometric interpretations | | | 1d | 2.5 |
| 1-48 | Cosine similarity — cos θ = a·b/(‖a‖‖b‖), similarity metric in embedding spaces | | | 1d | 2.5 |
| 1-49 | Orthogonality — a·b = 0, orthonormal sets, orthogonal matrices QᵀQ = I | | | 1d | 2.5 |
| 1-50 | Projections — proj_v(u) = (u·v/v·v)v, projection matrices P = A(AᵀA)⁻¹Aᵀ | | | 1d | 2.5 |
| 1-51 | Least squares — minimize ‖Ax − b‖², normal equations AᵀAx = Aᵀb | | | 1d | 2.5 |
| 1-52 | Linear regression as projection — ŷ = projection of y onto Col(A), R² as explained variance | | | 1d | 2.5 |
| 1-53 | Gram-Schmidt orthogonalization — producing orthonormal basis, QR factorization | | | 1d | 2.5 |
| 1-54 | Change of basis — same vector, different coordinates, conjugation P⁻¹AP | | | 1d | 2.5 |
| 1-55 | Norms — L1 (sparsity), L2 (Euclidean), L∞ (max), Frobenius, spectral (σ₁) | | | 1d | 2.5 |
| 1-56 | Special matrices — symmetric, PD, PSD, orthogonal, diagonal, triangular | | | 1d | 2.5 |
| 1-57 | Cholesky decomposition A = LLᵀ — for PD matrices, sampling from multivariate Gaussians | | | 1d | 2.5 |
| 1-58 | Trace — tr(A) = Σaᵢᵢ = Σλᵢ, cyclic property tr(AB) = tr(BA), ‖A‖²_F = tr(AᵀA) | | | 1d | 2.5 |
| 1-59 | PCA — covariance matrix, eigenvectors = principal components, dimensionality reduction | | | 1d | 2.5 |
| 1-60 | Inner product of functions — ⟨f,g⟩ = ∫f(x)g(x)dx, orthogonal functions, function spaces | | | 1d | 2.5 |
| 1-61 | Regularization connections — L1 sparsity, L2 weight decay, gradient clipping norms | | | 1d | 2.5 |
| 1-62 | Capstone: unified picture — any matrix = rotate → scale → rotate (SVD) | | | 1d | 2.5 |
| 1-63 | Concept web — eigendecomposition ↔ SVD ↔ PCA ↔ least squares ↔ projections | | | 1d | 2.5 |
| 1-64 | Neural networks as compositions of linear maps + nonlinearities | | | 1d | 2.5 |
| 1-65 | Linear algebra in attention — softmax(QKᵀ/√d)V as weighted projection | | | 1d | 2.5 |

---

## Phase 2A: ODEs (Lessons 13–18)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 2A-01 | Derivative from the limit definition | | | 1d | 2.5 |
| 2A-02 | Power rule and constant multiple/sum rules | | | 1d | 2.5 |
| 2A-03 | Product rule derivative | | | 1d | 2.5 |
| 2A-04 | Quotient rule derivative | | | 1d | 2.5 |
| 2A-05 | Chain rule — single composition f(g(x)) | | | 1d | 2.5 |
| 2A-06 | Chain rule — multi-layer nested compositions | | | 1d | 2.5 |
| 2A-07 | Implicit differentiation — find dy/dx from F(x,y) = 0 | | | 1d | 2.5 |
| 2A-08 | Logarithmic differentiation | | | 1d | 2.5 |
| 2A-09 | Derivatives of exponentials and logarithms | | | 1d | 2.5 |
| 2A-10 | Derivatives of trigonometric functions | | | 1d | 2.5 |
| 2A-11 | Derivatives of inverse trig functions (arcsin, arctan, etc.) | | | 1d | 2.5 |
| 2A-12 | ML activation function derivatives — sigmoid, tanh, ReLU, softplus | | | 1d | 2.5 |
| 2A-13 | Evaluating limits — algebraic manipulation, squeeze theorem | | | 1d | 2.5 |
| 2A-14 | L'Hôpital's rule — indeterminate forms 0/0, ∞/∞ | | | 1d | 2.5 |
| 2A-15 | Continuity analysis — removable, jump, and essential discontinuities | | | 1d | 2.5 |
| 2A-16 | Critical points, second derivative test, and concavity | | | 1d | 2.5 |
| 2A-17 | Mean Value Theorem and Extreme Value Theorem | | | 1d | 2.5 |
| 2A-18 | Basic antiderivatives — power, exponential, trigonometric | | | 1d | 2.5 |
| 2A-19 | u-substitution integrals | | | 1d | 2.5 |
| 2A-20 | Integration by parts | | | 1d | 2.5 |
| 2A-21 | Partial fraction decomposition integrals | | | 1d | 2.5 |
| 2A-22 | Trigonometric substitution integrals | | | 1d | 2.5 |
| 2A-23 | Improper integrals — convergence and divergence | | | 1d | 2.5 |
| 2A-24 | Definite integrals via FTC Part 2 | | | 1d | 2.5 |
| 2A-25 | FTC Part 1 — differentiating ∫ₐˣ f(t)dt with variable bounds | | | 1d | 2.5 |
| 2A-26 | Newton's method — root-finding via tangent line iteration | | | 1d | 2.5 |
| 2A-27 | Polar coordinates — area and arc length in polar form | | | 1d | 2.5 |
| 2A-28 | Sequences, series, and convergence tests | | | 1d | 2.5 |
| 2A-29 | Taylor/Maclaurin series expansion and remainder estimation | | | 1d | 2.5 |
| 2A-30 | ODE classification — order, linearity, autonomous; direction fields | | | 1d | 2.5 |
| 2A-31 | Existence and uniqueness — Picard-Lindelöf theorem, Lipschitz condition | | | 1d | 2.5 |
| 2A-32 | Separable equations — g(y)dy = f(x)dx | | | 1d | 2.5 |
| 2A-33 | First-order linear ODEs — integrating factor μ = e^{∫P dx}, exact equations | | | 1d | 2.5 |
| 2A-34 | Bernoulli and substitution methods — reduction to linear form | | | 1d | 2.5 |
| 2A-35 | Euler's method — numerical stepping, connection to gradient descent | | | 1d | 2.5 |
| 2A-36 | Phase line analysis — equilibria, stability (stable/unstable/semi-stable) | | | 1d | 2.5 |
| 2A-37 | Logistic growth — dy/dt = ry(1−y/K), carrying capacity, sigmoid connection | | | 1d | 2.5 |
| 2A-38 | Constant-coefficient second-order ODE — characteristic equation, three cases | | | 1d | 2.5 |
| 2A-39 | Wronskian and fundamental solution sets — linear independence of solutions | | | 1d | 2.5 |
| 2A-40 | Mechanical vibrations — free/damped/forced, underdamped/overdamped/critical | | | 1d | 2.5 |
| 2A-41 | Resonance — frequency matching, unbounded growth | | | 1d | 2.5 |
| 2A-42 | Undetermined coefficients — particular solutions for polynomial/exponential/trig forcing | | | 1d | 2.5 |
| 2A-43 | Variation of parameters — general method, Wronskian-based formula | | | 1d | 2.5 |
| 2A-44 | Power series solutions of ODEs — recurrence relations, singular points | | | 1d | 2.5 |
| 2A-45 | Laplace transform — definition and common transform pairs | | | 1d | 2.5 |
| 2A-46 | Transform of derivatives and converting ODEs to algebra | | | 1d | 2.5 |
| 2A-47 | Convolution theorem and Dirac delta impulse response | | | 1d | 2.5 |
| 2A-48 | Inverse Laplace via partial fractions and table lookup | | | 1d | 2.5 |
| 2A-49 | Systems of ODEs — x' = Ax, eigenvalue method, matrix exponential | | | 1d | 2.5 |
| 2A-50 | Phase portraits — node, spiral, saddle, center classification | | | 1d | 2.5 |
| 2A-51 | Trace-determinant plane — classifying 2×2 systems | | | 1d | 2.5 |
| 2A-52 | Stability of equilibria — asymptotically stable, unstable, marginally stable | | | 1d | 2.5 |
| 2A-53 | Nonlinear systems linearization — Jacobian at equilibrium, Hartman-Grobman | | | 1d | 2.5 |
| 2A-54 | Gradient flow — dx/dt = −∇f(x), gradient descent as discretized ODE | | | 1d | 2.5 |

---

## Phase 2B: Multivariable Calculus (Lessons 19–23)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 2B-01 | Lines and planes in 3D — parametric/symmetric forms, distance formulas | | | 1d | 2.5 |
| 2B-02 | Vector-valued functions r(t) — tangent vectors, speed, arc length | | | 1d | 2.5 |
| 2B-03 | Arc length parameterization — unit-speed curves, intrinsic vs extrinsic | | | 1d | 2.5 |
| 2B-04 | Curvature κ = |dT/ds| — osculating circle, radius of curvature | | | 1d | 2.5 |
| 2B-05 | TNB (Frenet-Serret) frame — unit tangent T, principal normal N, binormal B | | | 1d | 2.5 |
| 2B-06 | Multivariable functions — domain, range, level curves/contour plots | | | 1d | 2.5 |
| 2B-07 | Multivariable limits — path test, squeeze theorem, limit existence | | | 1d | 2.5 |
| 2B-08 | Partial derivatives — definition, computation, higher-order partials, Clairaut's theorem | | | 1d | 2.5 |
| 2B-09 | Total differential df = f_x dx + f_y dy and differentiability hierarchy | | | 1d | 2.5 |
| 2B-10 | Multivariable chain rule — tree diagrams, summing over all dependency paths | | | 1d | 2.5 |
| 2B-11 | Jacobian matrix — J_{ij} = ∂F_i/∂x_j, the total derivative as best linear approximation | | | 1d | 2.5 |
| 2B-12 | Chain rule as Jacobian multiplication: J_{g∘f} = J_g · J_f (= backpropagation) | | | 1d | 2.5 |
| 2B-13 | Directional derivatives D_û f = ∇f · û — gradient encodes all directional information | | | 1d | 2.5 |
| 2B-14 | Gradient — direction of steepest ascent, perpendicular to level curves | | | 1d | 2.5 |
| 2B-15 | Tangent planes and linear approximation f(x) ≈ f(a) + ∇f(a)·(x-a) | | | 1d | 2.5 |
| 2B-16 | Critical points — necessary condition ∇f = 0 | | | 1d | 2.5 |
| 2B-17 | Hessian matrix and second derivative test (PD → min, ND → max, indefinite → saddle) | | | 1d | 2.5 |
| 2B-18 | Saddle points dominate in high dimensions — random matrix theory prediction | | | 1d | 2.5 |
| 2B-19 | Lagrange multipliers — ∇f = λ∇g, constrained optimization geometry | | | 1d | 2.5 |
| 2B-20 | KKT conditions — inequality constraints, complementary slackness | | | 1d | 2.5 |
| 2B-21 | Regularization-constraint equivalence: min L + λ‖w‖² ↔ min L s.t. ‖w‖² ≤ C | | | 1d | 2.5 |
| 2B-22 | Multivariate Taylor expansion — 1st order (gradient), 2nd order (Hessian), Big-O notation | | | 1d | 2.5 |
| 2B-23 | Implicit Function Theorem — when F(x,y)=0 defines y=g(x), singularity when ∂F/∂y = 0 | | | 1d | 2.5 |
| 2B-24 | IFT failure and SLT — singularities where standard statistics breaks down | | | 1d | 2.5 |
| 2B-25 | Double and triple integrals — iterated integrals, Fubini's theorem, setting up bounds | | | 1d | 2.5 |
| 2B-26 | Change of variables — Jacobian determinant |det(J)|, polar/cylindrical/spherical coordinates | | | 1d | 2.5 |
| 2B-27 | Monte Carlo integration — random sampling approximation, 1/√N convergence rate | | | 1d | 2.5 |

---

## Phase 2C: Vector Calculus (Lessons 24–28)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 2C-01 | Parametric curves r(t) — velocity r'(t), speed ‖r'(t)‖, acceleration r''(t) | | | 1d | 2.5 |
| 2C-02 | Reparameterization — speed factor ds = ‖r'(t)‖ dt, invariance of geometric quantities | | | 1d | 2.5 |
| 2C-03 | Scalar line integrals — ∫_C f ds, integrating density along a curve | | | 1d | 2.5 |
| 2C-04 | Line integral of a vector field (work) — ∫_C F · dr, path dependence | | | 1d | 2.5 |
| 2C-05 | Vector fields — definition F: ℝⁿ → ℝⁿ, visualization, flow lines | | | 1d | 2.5 |
| 2C-06 | Divergence — div F = ∇·F, sources/sinks, connection to trace of Jacobian | | | 1d | 2.5 |
| 2C-07 | Curl — curl F = ∇×F, local rotation measure, 2D scalar vs 3D vector | | | 1d | 2.5 |
| 2C-08 | Conservative fields — F = ∇φ, path independence, potential functions | | | 1d | 2.5 |
| 2C-09 | Fundamental Theorem for Line Integrals — ∫_C ∇φ · dr = φ(B) − φ(A) | | | 1d | 2.5 |
| 2C-10 | Testing conservativeness — curl F = 0 on simply connected domain, ∂P/∂y = ∂Q/∂x | | | 1d | 2.5 |
| 2C-11 | Exact vs closed forms — closed (curl = 0) vs exact (has potential), topology matters | | | 1d | 2.5 |
| 2C-12 | Green's theorem (circulation form) — ∮ P dx + Q dy = ∬ (∂Q/∂x − ∂P/∂y) dA | | | 1d | 2.5 |
| 2C-13 | Green's theorem (flux/divergence form) — ∮ F·n ds = ∬ div(F) dA | | | 1d | 2.5 |
| 2C-14 | Multiply-connected domains — holes obstruct conservativeness, winding number | | | 1d | 2.5 |
| 2C-15 | The Laplacian ∇²f = div(grad f) — measures deviation from local average | | | 1d | 2.5 |
| 2C-16 | Parametric surfaces r(u,v) — tangent vectors r_u, r_v, normal vector r_u × r_v | | | 1d | 2.5 |
| 2C-17 | Surface area — ∬ ‖r_u × r_v‖ du dv, orientation and the Möbius strip | | | 1d | 2.5 |
| 2C-18 | Flux integrals — ∬_S F · dS, flow through a surface | | | 1d | 2.5 |
| 2C-19 | Stokes' theorem — ∮_C F · dr = ∬_S (∇×F) · dS | | | 1d | 2.5 |
| 2C-20 | Divergence theorem — ∯_S F · dS = ∭_E (∇·F) dV | | | 1d | 2.5 |
| 2C-21 | Unified hierarchy — FTC → FTLI → Green's → Stokes' → Divergence as ∫_{∂Ω} ω = ∫_Ω dω | | | 1d | 2.5 |
| 2C-22 | Helmholtz decomposition — any vector field = curl-free + divergence-free | | | 1d | 2.5 |
| 2C-23 | Vector calculus identities — curl(grad) = 0, div(curl) = 0, product rules | | | 1d | 2.5 |
| 2C-24 | Flux integrals in 2D — ∫_C F·n̂ ds, measuring outward flow through a curve | | | 1d | 2.5 |
| 2C-25 | Divergence and normalizing flows — d(log p)/dt = −div(f) for continuous flows | | | 1d | 2.5 |

---

## Phase 2D: PDEs (Lessons 29–33)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 2D-01 | PDE classification — elliptic (B²−AC<0), parabolic (=0), hyperbolic (>0) | | | 1d | 2.5 |
| 2D-02 | Heat equation — derivation, u_t = α∇²u | | | 1d | 2.5 |
| 2D-03 | Boundary conditions — Dirichlet, Neumann, Robin, Periodic | | | 1d | 2.5 |
| 2D-04 | Separation of variables — u(x,t) = X(x)T(t), eigenvalue problems | | | 1d | 2.5 |
| 2D-05 | Separation with different BCs — sine (Dirichlet), cosine (Neumann), both (Periodic) | | | 1d | 2.5 |
| 2D-06 | Linearity and superposition — building complex solutions from simple ones | | | 1d | 2.5 |
| 2D-07 | Well-posedness (Hadamard) — existence, uniqueness, continuous dependence | | | 1d | 2.5 |
| 2D-08 | Equilibrium/steady-state — ∇²u = 0 (Laplace's equation), rectangle and disc solutions | | | 1d | 2.5 |
| 2D-09 | Mean value property and maximum principle for harmonic functions | | | 1d | 2.5 |
| 2D-10 | Fourier series — coefficients via inner products, convergence, half-range expansions | | | 1d | 2.5 |
| 2D-11 | Complex Fourier series, Parseval's theorem, Gibbs phenomenon | | | 1d | 2.5 |
| 2D-12 | Wave equation — derivation, u_tt = c²u_xx, standing waves | | | 1d | 2.5 |
| 2D-13 | d'Alembert's solution — traveling waves f(x−ct) + g(x+ct) | | | 1d | 2.5 |
| 2D-14 | Heat vs wave — diffusion (info loss) vs propagation (info preservation) | | | 1d | 2.5 |
| 2D-15 | Sturm-Liouville eigenvalue problem — real eigenvalues, orthogonal eigenfunctions | | | 1d | 2.5 |
| 2D-16 | Sturm-Liouville as infinite-dimensional spectral theorem | | | 1d | 2.5 |
| 2D-17 | Rayleigh quotient — variational characterization, min-max principle | | | 1d | 2.5 |
| 2D-18 | Eigenfunction expansions — generalized Fourier series | | | 1d | 2.5 |
| 2D-19 | Inhomogeneous BCs — u = v + w (steady-state + transient) decomposition | | | 1d | 2.5 |
| 2D-20 | Domain of dependence, range of influence — finite propagation speed | | | 1d | 2.5 |
| 2D-21 | Energy conservation in the wave equation | | | 1d | 2.5 |
| 2D-22 | Helmholtz equation ∇²u + k²u = 0 — resonant modes, Bessel functions | | | 1d | 2.5 |
| 2D-23 | Heat equation on infinite line — Gaussian kernel, convolution with initial data | | | 1d | 2.5 |
| 2D-24 | Fourier transform — definition F̂(k), continuous frequency decomposition | | | 1d | 2.5 |
| 2D-25 | FT properties — derivative ↔ ik, convolution ↔ multiplication, shift, scaling | | | 1d | 2.5 |
| 2D-26 | FT of Gaussian is Gaussian (reciprocal width); solving PDEs via FT | | | 1d | 2.5 |
| 2D-27 | Semi-infinite domains — method of images, error function erf(x) | | | 1d | 2.5 |
| 2D-28 | Method of characteristics — converting first-order PDEs to ODEs | | | 1d | 2.5 |
| 2D-29 | Transport equation — u_t + cu_x = 0, traveling profiles | | | 1d | 2.5 |
| 2D-30 | Nonlinear conservation laws — characteristic crossing, shock waves, Rankine-Hugoniot | | | 1d | 2.5 |
| 2D-31 | Burgers' equation — canonical shock formation model | | | 1d | 2.5 |
| 2D-32 | Forward SDE in diffusion models — dx = f dt + g dW, noise schedules (VP, VE) | | | 1d | 2.5 |
| 2D-33 | Fokker-Planck, score function, score matching — probability density evolution | | | 1d | 2.5 |
| 2D-34 | Reverse SDE and probability flow ODE — running diffusion backward for generation | | | 1d | 2.5 |

---

## Phase 2E: ML-Applied Calculus (Lessons 34–36)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 2E-01 | Scalar derivatives and partial derivatives for ML — neural network framing | | | 1d | 2.5 |
| 2E-02 | Gradient vector — assembling partials, direction of steepest ascent | | | 1d | 2.5 |
| 2E-03 | Element-wise operations — diagonal Jacobians (addition → I, Hadamard → diag(x)) | | | 1d | 2.5 |
| 2E-04 | Scalar expansion ∂(zx)/∂x = zI and vector sum reduction ∂(Σx_i)/∂x = 1ᵀ | | | 1d | 2.5 |
| 2E-05 | Dot product gradient — ∂(w·x)/∂w = xᵀ, ∂(w·x)/∂x = wᵀ | | | 1d | 2.5 |
| 2E-06 | Jacobian matrix — m×n matrix for F: ℝⁿ→ℝᵐ, the total derivative | | | 1d | 2.5 |
| 2E-07 | Vector chain rule — ∂f/∂x = (∂f/∂g)(∂g/∂x), Jacobian multiplication = backpropagation | | | 1d | 2.5 |
| 2E-08 | Forward-mode vs reverse-mode autodiff — tangent vectors vs adjoint vectors | | | 1d | 2.5 |
| 2E-09 | Why reverse mode dominates — one scalar loss, millions of parameters → one backward pass | | | 1d | 2.5 |
| 2E-10 | Computation graphs — neural networks as DAGs of differentiable operations | | | 1d | 2.5 |
| 2E-11 | Gradient accumulation — fan-out nodes sum incoming gradients | | | 1d | 2.5 |
| 2E-12 | Single neuron gradient — ReLU piecewise derivative gates the gradient | | | 1d | 2.5 |
| 2E-13 | Full network loss gradient — chain of Jacobians from loss back through layers | | | 1d | 2.5 |
| 2E-14 | Softmax Jacobian — S_ij = s_i(δ_ij − s_j), cross-entropy simplification | | | 1d | 2.5 |
| 2E-15 | Batch normalization gradient — chain rule through normalization statistics | | | 1d | 2.5 |
| 2E-16 | Matrix calculus identities — ∂(xᵀAx)/∂x = (A+Aᵀ)x, ∂tr(AB)/∂A = Bᵀ | | | 1d | 2.5 |
| 2E-17 | Hessian-vector products — second-order information without full Hessian | | | 1d | 2.5 |

---

## Phase 3A: Core Probability (Lessons 37–40)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 3A-01 | Probability axioms, conditional probability, independence | | | 1d | 2.5 |
| 3A-02 | Bayes' theorem and the law of total probability | | | 1d | 2.5 |
| 3A-03 | Discrete distributions (Bernoulli, Binomial, Poisson, Geometric, Categorical) | | | 1d | 2.5 |
| 3A-04 | Continuous distributions (Uniform, Normal, Exponential, Multivariate Gaussian) | | | 1d | 2.5 |
| 3A-05 | CLT, Law of Large Numbers, change of variables for probability | | | 1d | 2.5 |
| 3A-06 | Expectation — definition, linearity, Jensen's inequality | | | 1d | 2.5 |
| 3A-07 | Variance, standard deviation, computational formula | | | 1d | 2.5 |
| 3A-08 | Covariance, correlation, covariance matrix | | | 1d | 2.5 |
| 3A-09 | Moment generating functions and moments | | | 1d | 2.5 |
| 3A-10 | MLE — likelihood, log-likelihood, cross-entropy as negative log-likelihood | | | 1d | 2.5 |
| 3A-11 | Properties of MLE (consistency, asymptotic normality, efficiency) | | | 1d | 2.5 |
| 3A-12 | EM algorithm and Gaussian Mixture Models | | | 1d | 2.5 |
| 3A-13 | Information content and entropy | | | 1d | 2.5 |
| 3A-14 | Cross-entropy and cross-entropy loss in ML | | | 1d | 2.5 |
| 3A-15 | KL divergence — properties, asymmetry | | | 1d | 2.5 |
| 3A-16 | Temperature and softmax | | | 1d | 2.5 |
| 3A-17 | Mutual information and data processing inequality | | | 1d | 2.5 |
| 3A-18 | Pointwise mutual information (PMI) and Word2Vec connection | | | 1d | 2.5 |
| 3A-19 | Information bottleneck principle — compression vs preservation tradeoff in deep learning | | | 1d | 2.5 |
| 3A-20 | Naive Bayes classifier and log-probability arithmetic — Laplace smoothing, log-space computation | | | 1d | 2.5 |

---

## Phase 3B: Frequentist Methods (Lessons 41–43)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 3B-01 | Hypothesis testing — null/alternative, p-values, significance | | | 1d | 2.5 |
| 3B-02 | Type I/II errors, statistical power, effect sizes | | | 1d | 2.5 |
| 3B-03 | Confidence intervals and multiple comparisons corrections | | | 1d | 2.5 |
| 3B-04 | P-hacking, garden of forking paths, file drawer effect | | | 1d | 2.5 |
| 3B-05 | Base rate fallacy — confusing P(data|H₀) with P(H₀|data) | | | 1d | 2.5 |
| 3B-06 | Experimental design — randomization, controls, blinding, pre-registration | | | 1d | 2.5 |
| 3B-07 | Hierarchy of evidence — case reports → RCTs → systematic reviews → meta-analyses | | | 1d | 2.5 |
| 3B-08 | Statistical fallacies — Simpson's paradox, ecological fallacy, survivor bias | | | 1d | 2.5 |
| 3B-09 | Goodhart's Law and the replication crisis | | | 1d | 2.5 |
| 3B-10 | Linear regression — OLS, R², multiple regression | | | 1d | 2.5 |
| 3B-11 | Regularization — Ridge (L2), Lasso (L1), Elastic Net | | | 1d | 2.5 |
| 3B-12 | Logistic regression and GLMs — single neuron with sigmoid = logistic regression | | | 1d | 2.5 |
| 3B-13 | Common statistical tests — t-test, chi-squared, ANOVA, Mann-Whitney U | | | 1d | 2.5 |
| 3B-14 | Regression diagnostics — linearity, homoscedasticity, multicollinearity | | | 1d | 2.5 |
| 3B-15 | Robust standard errors (Huber-White) — inference when assumptions are violated | | | 1d | 2.5 |

---

## Phase 3C: Bayesian Deep Dive (Lessons 44–46)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 3C-01 | Bayesian vs frequentist — posterior ∝ likelihood × prior | | | 1d | 2.5 |
| 3C-02 | Prior types (informative, weakly informative, Jeffreys, maximum entropy) | | | 1d | 2.5 |
| 3C-03 | Conjugate priors (Beta-Binomial, Normal-Normal, etc.) | | | 1d | 2.5 |
| 3C-04 | MAP estimation and priors as regularization | | | 1d | 2.5 |
| 3C-05 | Sequential updating — today's posterior = tomorrow's prior | | | 1d | 2.5 |
| 3C-06 | The computational problem — P(D) = ∫P(D|θ)P(θ)dθ is usually intractable | | | 1d | 2.5 |
| 3C-07 | MCMC — Metropolis-Hastings, Gibbs sampling | | | 1d | 2.5 |
| 3C-08 | MCMC diagnostics — trace plots, R-hat, effective sample size, burn-in | | | 1d | 2.5 |
| 3C-09 | Hamiltonian Monte Carlo and NUTS | | | 1d | 2.5 |
| 3C-10 | Variational inference — ELBO, mean-field approximation | | | 1d | 2.5 |
| 3C-11 | VAE connection (encoder = variational params, loss = negative ELBO) | | | 1d | 2.5 |
| 3C-12 | Laplace approximation — Gaussian at MAP with covariance = inverse Hessian | | | 1d | 2.5 |
| 3C-13 | Marginal likelihood (evidence) and automatic Occam's razor | | | 1d | 2.5 |
| 3C-14 | Bayes factors, BIC, WAIC, LOO-CV | | | 1d | 2.5 |
| 3C-15 | BIC failure for neural networks — singular models, degenerate Fisher information | | | 1d | 2.5 |
| 3C-16 | Free energy and SLT correction (RLCT replaces k/2) | | | 1d | 2.5 |
| 3C-17 | Hierarchical models — partial pooling, shrinkage | | | 1d | 2.5 |

---

## Phase 3D: Applied Statistics (Lessons 47–48)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 3D-01 | Counterfactuals and potential outcomes framework (Rubin) | | | 1d | 2.5 |
| 3D-02 | Average Treatment Effect (ATE) and causal effect definition | | | 1d | 2.5 |
| 3D-03 | DAGs — chains (mediation), forks (confounding), colliders | | | 1d | 2.5 |
| 3D-04 | d-separation rules for conditional independence | | | 1d | 2.5 |
| 3D-05 | Controlling for confounders vs mediators vs colliders | | | 1d | 2.5 |
| 3D-06 | Causal inference methods — instrumental variables, difference-in-differences | | | 1d | 2.5 |
| 3D-07 | Regression discontinuity design and propensity score matching | | | 1d | 2.5 |
| 3D-08 | Heritability (h²), twin studies, equal environments assumption | | | 1d | 2.5 |
| 3D-09 | GWAS, polygenic scores, missing heritability, population stratification | | | 1d | 2.5 |
| 3D-10 | Statistical adjudication of real-world empirical claims | | | 1d | 2.5 |
| 3D-11 | Meta-analysis and forest plots — heterogeneity (I²), funnel plots, publication bias | | | 1d | 2.5 |
| 3D-12 | Bradford Hill criteria for causation, epidemiology pitfalls | | | 1d | 2.5 |

---

## Phase 3E: ML Theory Foundations (Lessons 49–52)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 3E-01 | Markov's inequality — P(X ≥ a) ≤ E[X]/a (weakest, most general) | | | 1d | 2.5 |
| 3E-02 | Chebyshev's inequality — P(|X−μ| ≥ kσ) ≤ 1/k² | | | 1d | 2.5 |
| 3E-03 | Chernoff bounds — exponential concentration via MGFs | | | 1d | 2.5 |
| 3E-04 | Hoeffding's inequality — tight bounds for bounded random variables | | | 1d | 2.5 |
| 3E-05 | Sub-Gaussian and sub-exponential random variables | | | 1d | 2.5 |
| 3E-06 | Applications — bounding sample means, uniform convergence, generalization bounds | | | 1d | 2.5 |
| 3E-07 | Markov property — future depends only on present | | | 1d | 2.5 |
| 3E-08 | Transition matrices and stationary distribution πP = π | | | 1d | 2.5 |
| 3E-09 | Irreducibility, aperiodicity, ergodicity | | | 1d | 2.5 |
| 3E-10 | Convergence theorem — ergodic chains converge to unique stationary distribution | | | 1d | 2.5 |
| 3E-11 | Mixing time — how quickly chain approaches stationarity | | | 1d | 2.5 |
| 3E-12 | Detailed balance (reversibility) and connection to MCMC | | | 1d | 2.5 |
| 3E-13 | Fisher information I(θ) = E[(∂/∂θ log P)²] — curvature of log-likelihood | | | 1d | 2.5 |
| 3E-14 | Cramér-Rao bound — Var(θ̂) ≥ 1/I(θ), fundamental precision limit | | | 1d | 2.5 |
| 3E-15 | Fisher information matrix (multivariate) and singular Fisher info at NN symmetries | | | 1d | 2.5 |
| 3E-16 | Exponential families — P(x|θ) = h(x)exp(η·T(x) − A(θ)), sufficient statistics | | | 1d | 2.5 |
| 3E-17 | Common exponential families — Gaussian, Bernoulli, Poisson, Gamma, Beta | | | 1d | 2.5 |
| 3E-18 | Natural gradient descent — Fisher information metric, parameter space geometry | | | 1d | 2.5 |
| 3E-19 | PAC framework — Probably Approximately Correct, sample complexity | | | 1d | 2.5 |
| 3E-20 | VC dimension — largest set shattered by hypothesis class | | | 1d | 2.5 |
| 3E-21 | Fundamental theorem — finite VC dim ↔ PAC learnable | | | 1d | 2.5 |
| 3E-22 | Rademacher complexity — data-dependent capacity measure | | | 1d | 2.5 |
| 3E-23 | Generalization bounds — test error ≤ train error + complexity/√n | | | 1d | 2.5 |
| 3E-24 | Union bound and PAC-Bayes bounds — tighter bounds for neural networks, connection to SLT | | | 1d | 2.5 |

---

## Phase 4A: Neural Networks & Optimization (Lessons 53–56)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 4A-01 | Neuron computation — output = activation(wᵀx + b), the atomic unit | | | 1d | 2.5 |
| 4A-02 | Activation functions — step (original), sigmoid (smooth gate), ReLU (modern default) | | | 1d | 2.5 |
| 4A-03 | Linear decision boundary — hyperplane wᵀx + b = 0 separates classes | | | 1d | 2.5 |
| 4A-04 | Perceptron learning rule — convergence theorem for linearly separable data | | | 1d | 2.5 |
| 4A-05 | XOR problem — single neuron can't solve it, motivating multi-layer networks | | | 1d | 2.5 |
| 4A-06 | Loss functions — MSE (regression), cross-entropy (classification), loss landscape | | | 1d | 2.5 |
| 4A-07 | Gradient descent — update rule θ ← θ − η∇L, learning rate tradeoffs | | | 1d | 2.5 |
| 4A-08 | Batch, stochastic, and mini-batch SGD — noise helps escape local minima | | | 1d | 2.5 |
| 4A-09 | Momentum — accumulate velocity, smooth oscillations | | | 1d | 2.5 |
| 4A-10 | Adam optimizer — adaptive learning rates per parameter | | | 1d | 2.5 |
| 4A-11 | Learning rate schedules — warmup, cosine decay, step decay | | | 1d | 2.5 |
| 4A-12 | Micrograd — autograd engine, computation graphs, topological sort backward pass | | | 1d | 2.5 |
| 4A-13 | Backprop = reverse-mode autodiff — forward pass caches, backward pass propagates gradients | | | 1d | 2.5 |
| 4A-14 | Local gradients × upstream gradients = layer gradients | | | 1d | 2.5 |
| 4A-15 | Computation graphs — DAGs, each node knows its local derivative | | | 1d | 2.5 |
| 4A-16 | Gradient checking — finite differences to verify analytical gradients | | | 1d | 2.5 |
| 4A-17 | Vanishing gradients — sigmoid squashes; exploding gradients — large weights amplify | | | 1d | 2.5 |
| 4A-18 | Solutions — residual connections, normalization, careful initialization (Xavier/He), gradient clipping | | | 1d | 2.5 |
| 4A-19 | Multi-layer networks — composition of affine + nonlinear, ReLU folds space | | | 1d | 2.5 |
| 4A-20 | Universal approximation theorem — one hidden layer suffices but may need exponential width | | | 1d | 2.5 |
| 4A-21 | Depth = compositionality — hierarchical features (edges → textures → parts → objects) | | | 1d | 2.5 |
| 4A-22 | Embedding spaces and MLP language models (Bengio et al. 2003) | | | 1d | 2.5 |
| 4A-23 | Regularization — dropout, weight decay, early stopping, data augmentation | | | 1d | 2.5 |
| 4A-24 | Batch normalization and weight initialization — why proper scaling matters | | | 1d | 2.5 |

---

## Phase 4B: Architectures (Lessons 57–58)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 4B-01 | Convolution — kernels, feature maps, stride, padding, parameter sharing | | | 1d | 2.5 |
| 4B-02 | Pooling (max, average), receptive field, CNN architecture pattern | | | 1d | 2.5 |
| 4B-03 | AlexNet and the deep learning revolution (2012) | | | 1d | 2.5 |
| 4B-04 | Hierarchy of learned features (edges → textures → parts → objects) | | | 1d | 2.5 |
| 4B-05 | Beyond AlexNet — VGGNet, ResNet, Vision Transformers | | | 1d | 2.5 |
| 4B-06 | Kaplan scaling laws — power law in model size, data, compute | | | 1d | 2.5 |
| 4B-07 | Chinchilla scaling — compute-optimal training, 20 tokens per parameter | | | 1d | 2.5 |
| 4B-08 | Emergent capabilities and phase transitions in capability | | | 1d | 2.5 |
| 4B-09 | Emergence debate — measurement artifact hypothesis | | | 1d | 2.5 |
| 4B-10 | Grokking — delayed generalization as phase transition | | | 1d | 2.5 |
| 4B-11 | Developmental interpretability — tracking representations at transitions | | | 1d | 2.5 |

---

## Phase 4C: Transformers (Lessons 59–60)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 4C-01 | Query, Key, Value — three projections and scaled dot-product attention | | | 1d | 2.5 |
| 4C-02 | Softmax attention weights and output as weighted sum of values | | | 1d | 2.5 |
| 4C-03 | Multi-head attention — parallel heads, concatenation | | | 1d | 2.5 |
| 4C-04 | Causal masking and cross-attention | | | 1d | 2.5 |
| 4C-05 | Positional encodings — sinusoidal, learned, RoPE, ALiBi | | | 1d | 2.5 |
| 4C-06 | Transformer block — LayerNorm, attention, residual, MLP | | | 1d | 2.5 |
| 4C-07 | Residual stream as shared communication bus | | | 1d | 2.5 |
| 4C-08 | MLP layers — expansion, gated variants (SwiGLU), knowledge storage | | | 1d | 2.5 |
| 4C-09 | Embeddings, unembeddings, weight tying | | | 1d | 2.5 |
| 4C-10 | QK circuit (where to look) and OV circuit (what to copy) | | | 1d | 2.5 |
| 4C-11 | KV cache and autoregressive generation | | | 1d | 2.5 |
| 4C-12 | Byte Pair Encoding (BPE) tokenization | | | 1d | 2.5 |
| 4C-13 | Pre-norm vs post-norm transformer blocks — why pre-norm is standard | | | 1d | 2.5 |

---

## Phase 4D: Mechanistic Interpretability (Lessons 61, 65)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 4D-01 | What mechanistic interpretability is — reverse-engineering learned algorithms | | | 1d | 2.5 |
| 4D-02 | Activation patching (causal tracing) — swap activations to measure causal importance | | | 1d | 2.5 |
| 4D-03 | Direct logit attribution — trace logit contributions through residual stream | | | 1d | 2.5 |
| 4D-04 | Probing and logit lens / tuned lens — what information is encoded at each layer | | | 1d | 2.5 |
| 4D-05 | Steering vectors and activation engineering — modifying behavior at inference | | | 1d | 2.5 |
| 4D-06 | TransformerLens, hooks, ablation studies — the tools of mech interp | | | 1d | 2.5 |
| 4D-07 | Induction heads — the mechanism for in-context learning | | | 1d | 2.5 |
| 4D-08 | Monosemantic vs polysemantic neurons — why most neurons respond to multiple concepts | | | 1d | 2.5 |
| 4D-09 | Superposition hypothesis — more features than dimensions, non-orthogonal directions | | | 1d | 2.5 |
| 4D-10 | Toy models of superposition — geometry, when superposition occurs | | | 1d | 2.5 |
| 4D-11 | Sparse Autoencoders (SAEs) — overcomplete dictionary, L1 sparsity, finding interpretable features | | | 1d | 2.5 |
| 4D-12 | Scaling monosemanticity — millions of features in Claude (deception, sycophancy, etc.) | | | 1d | 2.5 |
| 4D-13 | Circuit discovery — Q/K/V-composition, attention pattern analysis | | | 1d | 2.5 |
| 4D-14 | Known circuits — IOI (indirect object identification), greater-than circuit, successor heads | | | 1d | 2.5 |

---

## Phase 4E: Additional ML Topics (Lessons 62–64)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 4E-01 | Diffusion models — forward/reverse process, denoising objective | | | 1d | 2.5 |
| 4E-02 | Noise schedule, reparameterization trick, score matching | | | 1d | 2.5 |
| 4E-03 | Conditioning and classifier-free guidance | | | 1d | 2.5 |
| 4E-04 | Key architectures — DDPM, latent diffusion, U-Net, DiT | | | 1d | 2.5 |
| 4E-05 | Video generation and temporal attention | | | 1d | 2.5 |
| 4E-06 | RL framework — agent-environment loop, MDPs, policies | | | 1d | 2.5 |
| 4E-07 | Value functions — V, Q, Bellman equations, discount factor | | | 1d | 2.5 |
| 4E-08 | Policy gradient, REINFORCE, PPO | | | 1d | 2.5 |
| 4E-09 | Actor-critic methods | | | 1d | 2.5 |
| 4E-10 | Reward hacking, specification gaming, Goodhart's Law in RL | | | 1d | 2.5 |
| 4E-11 | LLM pipeline — Stage 1: pre-training (next-token prediction, scaling) | | | 1d | 2.5 |
| 4E-12 | LLM pipeline — Stage 2: SFT (instruction tuning, LoRA) | | | 1d | 2.5 |
| 4E-13 | LLM pipeline — Stage 3: RLHF, DPO, Constitutional AI | | | 1d | 2.5 |
| 4E-14 | LLM pipeline — Stage 4: deployment, inference, evaluation | | | 1d | 2.5 |
| 4E-15 | The Bitter Lesson (Sutton) | | | 1d | 2.5 |
| 4E-16 | DDPM training objective — simplified noise prediction loss ‖ε − ε_θ(x_t, t)‖² | | | 1d | 2.5 |
| 4E-17 | Probability flow ODE and connection to neural ODEs | | | 1d | 2.5 |
| 4E-18 | KL penalty in RLHF — preventing reward model over-optimization | | | 1d | 2.5 |
| 4E-19 | Credit assignment problem — sparse rewards and attributing outcomes to actions | | | 1d | 2.5 |

---

## Phase 4F: Singular Learning Theory (Lesson 66)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 4F-01 | Why standard statistics fails — singularities, many-to-one parameter map, singular Fisher information | | | 1d | 2.5 |
| 4F-02 | Free energy F and the RLCT (Real Log Canonical Threshold) λ | | | 1d | 2.5 |
| 4F-03 | Regular vs singular models — BIC (d/2) vs SLT (λ ≤ d/2) | | | 1d | 2.5 |
| 4F-04 | Why overparameterized networks generalize — real complexity (RLCT) << parameter count | | | 1d | 2.5 |
| 4F-05 | Phase transitions in training — grokking as transition from high-RLCT to low-RLCT region | | | 1d | 2.5 |
| 4F-06 | Local Learning Coefficient (LLC) — empirical RLCT estimation, developmental interpretability | | | 1d | 2.5 |
| 4F-07 | Resolution of singularities (Hironaka), blow-ups, Watanabe's theorem and zeta function poles | | | 1d | 2.5 |

---

## Phase 5A: Computability & Complexity (Lessons 67–69)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 5A-01 | Turing machine definition — tape, head, states, transition function | | | 1d | 2.5 |
| 5A-02 | Church-Turing thesis and universal Turing machine | | | 1d | 2.5 |
| 5A-03 | Halting problem — undecidable, diagonalization proof | | | 1d | 2.5 |
| 5A-04 | Rice's theorem — every non-trivial semantic property is undecidable | | | 1d | 2.5 |
| 5A-05 | Decidability landscape — decidable, semi-decidable, undecidable | | | 1d | 2.5 |
| 5A-06 | Reductions and Busy Beaver function — grows faster than any computable function | | | 1d | 2.5 |
| 5A-07 | P (polynomial time) and NP (verifiable in polynomial time) | | | 1d | 2.5 |
| 5A-08 | NP-complete (hardest in NP) and NP-hard; Cook-Levin theorem (SAT) | | | 1d | 2.5 |
| 5A-09 | Key NP-complete problems — 3-SAT, graph coloring, TSP, subset sum, clique | | | 1d | 2.5 |
| 5A-10 | Polynomial reductions — showing one problem is at least as hard as another | | | 1d | 2.5 |
| 5A-11 | NP-hardness in ML — optimal NN training, feature selection, architecture search | | | 1d | 2.5 |
| 5A-12 | PSPACE, circuit complexity, approximation and randomized algorithms (BPP) | | | 1d | 2.5 |
| 5A-13 | Kolmogorov complexity K(x) — shortest program generating x | | | 1d | 2.5 |
| 5A-14 | K(x) is uncomputable — related to halting problem | | | 1d | 2.5 |
| 5A-15 | Invariance theorem — K independent of language up to constant | | | 1d | 2.5 |
| 5A-16 | Connection to Shannon entropy — E[K(X)] ≈ H(X) | | | 1d | 2.5 |
| 5A-17 | MDL principle and Solomonoff induction — universal prior P(x) = 2^{−K(x)} | | | 1d | 2.5 |
| 5A-18 | AIXI — Solomonoff + expected utility = optimal but incomputable agent | | | 1d | 2.5 |

---

## Phase 5B: Abstract Algebra (Lessons 70–72)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 5B-01 | Group axioms — closure, associativity, identity, inverses; abelian vs non-abelian | | | 1d | 2.5 |
| 5B-02 | Key examples — ℤ, ℝ*, permutation groups Sₙ, cyclic groups ℤₙ, matrix groups GL/SL/O/SO | | | 1d | 2.5 |
| 5B-03 | Subgroups, cosets, Lagrange's theorem (|H| divides |G|) | | | 1d | 2.5 |
| 5B-04 | Normal subgroups and quotient groups G/N | | | 1d | 2.5 |
| 5B-05 | Homomorphisms, isomorphisms, kernel | | | 1d | 2.5 |
| 5B-06 | First isomorphism theorem — G/ker(φ) ≅ im(φ) | | | 1d | 2.5 |
| 5B-07 | Cayley's theorem — every group embeds in a permutation group | | | 1d | 2.5 |
| 5B-08 | Rings — two operations (+, ×), examples (ℤ, R[x], matrices, ℤₙ) | | | 1d | 2.5 |
| 5B-09 | Fields — every nonzero element invertible; examples (ℚ, ℝ, ℂ, 𝔽ₚ) | | | 1d | 2.5 |
| 5B-10 | Ideals, quotient rings R/I, principal ideals | | | 1d | 2.5 |
| 5B-11 | Polynomial rings — foundation for algebraic geometry | | | 1d | 2.5 |
| 5B-12 | Modules, Noetherian rings, UFDs, PIDs — algebraic hierarchy | | | 1d | 2.5 |
| 5B-13 | Group actions — orbits, stabilizers, orbit-stabilizer theorem | | | 1d | 2.5 |
| 5B-14 | Burnside's lemma — counting distinct orbits via fixed points | | | 1d | 2.5 |
| 5B-15 | Neural network symmetries — neuron permutation (Sₙ), weight rescaling, zero neurons | | | 1d | 2.5 |
| 5B-16 | Symmetries create parameter space singularities — connection to SLT | | | 1d | 2.5 |
| 5B-17 | Group representations and character theory — encoding groups as matrices | | | 1d | 2.5 |
| 5B-18 | Equivariant neural networks — CNNs (translation), GNNs (permutation), steerable (rotation) | | | 1d | 2.5 |

---

## Phase 5C: Topology & Geometry (Lessons 73–76, 79)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 5C-01 | Topological spaces — open/closed sets, axioms | | | 1d | 2.5 |
| 5C-02 | Continuity as preimage of open sets; homeomorphism = topological equivalence | | | 1d | 2.5 |
| 5C-03 | Metric spaces — topology from distance, balls as open sets | | | 1d | 2.5 |
| 5C-04 | Compactness — Heine-Borel, extreme value theorem, sequential compactness | | | 1d | 2.5 |
| 5C-05 | Connectedness and path-connectedness | | | 1d | 2.5 |
| 5C-06 | Hausdorff spaces, basis for topology, subspace/product/quotient topologies | | | 1d | 2.5 |
| 5C-07 | Homotopy — continuous deformation of maps; homotopy equivalence of spaces | | | 1d | 2.5 |
| 5C-08 | Contractible spaces — homotopy equivalent to a point | | | 1d | 2.5 |
| 5C-09 | Fundamental group π₁ — loops up to deformation; π₁(S¹)=ℤ, π₁(S²)=0, π₁(T²)=ℤ×ℤ | | | 1d | 2.5 |
| 5C-10 | Simply connected spaces — π₁ = 0, no holes | | | 1d | 2.5 |
| 5C-11 | Covering spaces — unwinding topological structure, classification by subgroups of π₁ | | | 1d | 2.5 |
| 5C-12 | Loss landscape topology — holes, non-contractible loops, connected components as basins | | | 1d | 2.5 |
| 5C-13 | Smooth manifolds — locally ℝⁿ, charts and atlases, transition maps | | | 1d | 2.5 |
| 5C-14 | Examples — spheres, tori, Lie groups, weight space of neural networks | | | 1d | 2.5 |
| 5C-15 | Tangent space T_pM and tangent bundle TM | | | 1d | 2.5 |
| 5C-16 | Vector fields on manifolds — smooth assignment of tangent vectors | | | 1d | 2.5 |
| 5C-17 | Riemannian metric — measuring lengths/angles/curvature; geodesics | | | 1d | 2.5 |
| 5C-18 | Manifold hypothesis — real data lies on low-dimensional manifold; singularities = SLT | | | 1d | 2.5 |
| 5C-19 | Algebraic varieties — solution sets of polynomial equations | | | 1d | 2.5 |
| 5C-20 | Affine vs projective varieties; Hilbert's Nullstellensatz | | | 1d | 2.5 |
| 5C-21 | Coordinate ring R[x]/I(V) and local ring at a singularity | | | 1d | 2.5 |
| 5C-22 | Smooth vs singular points — Jacobian rank test | | | 1d | 2.5 |
| 5C-23 | Types of singularities — nodes, cusps, self-intersections | | | 1d | 2.5 |
| 5C-24 | Blow-ups — replacing singular points with projective spaces | | | 1d | 2.5 |
| 5C-25 | Resolution of singularities (Hironaka) and RLCT computation via blow-ups | | | 1d | 2.5 |
| 5C-26 | Differential forms — 0-forms (functions), 1-forms, 2-forms, k-forms | | | 1d | 2.5 |
| 5C-27 | Wedge product ∧ — antisymmetric (dx∧dy = −dy∧dx) | | | 1d | 2.5 |
| 5C-28 | Exterior derivative d — unifies gradient, curl, divergence; d² = 0 | | | 1d | 2.5 |
| 5C-29 | Pullbacks — how forms transform under smooth maps (rigorous change of variables) | | | 1d | 2.5 |
| 5C-30 | Generalized Stokes' theorem ∫_M dω = ∫_{∂M} ω — subsumes FTC, Green's, Stokes', Divergence | | | 1d | 2.5 |
| 5C-31 | De Rham cohomology — measuring topological holes via closed-but-not-exact forms | | | 1d | 2.5 |

---

## Phase 5D: Formal Logic (Lessons 77–78)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 5D-01 | Propositional logic — connectives, truth tables, tautologies, satisfiability | | | 1d | 2.5 |
| 5D-02 | Normal forms (CNF, DNF), logical equivalences | | | 1d | 2.5 |
| 5D-03 | Predicate logic — quantifiers, terms, formulas, models | | | 1d | 2.5 |
| 5D-04 | Soundness and completeness (Gödel's completeness theorem for FOL) | | | 1d | 2.5 |
| 5D-05 | Formal verification, SAT/SMT solvers | | | 1d | 2.5 |
| 5D-06 | Gödel numbering and self-referential sentences | | | 1d | 2.5 |
| 5D-07 | Gödel's First Incompleteness Theorem | | | 1d | 2.5 |
| 5D-08 | Gödel's Second Incompleteness Theorem | | | 1d | 2.5 |
| 5D-09 | Diagonal lemma and Löb's theorem | | | 1d | 2.5 |
| 5D-10 | Modal/provability logic (GL) and fixed-point theorem | | | 1d | 2.5 |
| 5D-11 | Implications for alignment — self-reference, trust, Vingean reflection | | | 1d | 2.5 |
| 5D-12 | Compactness theorem for FOL and nonstandard models | | | 1d | 2.5 |

---

## Phase 6A: Game Theory & Decision Theory (Lessons 80–82)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 6A-01 | Normal form games — strategies, payoff matrices, dominant strategies | | | 1d | 2.5 |
| 6A-02 | Nash equilibrium — pure and mixed strategies, Nash's theorem | | | 1d | 2.5 |
| 6A-03 | Key games — Prisoner's Dilemma, Stag Hunt, Chicken | | | 1d | 2.5 |
| 6A-04 | Iterated games, folk theorems, evolutionary game theory | | | 1d | 2.5 |
| 6A-05 | Mechanism design — incentive compatibility, revelation principle | | | 1d | 2.5 |
| 6A-06 | Auction theory (Vickrey, VCG) | | | 1d | 2.5 |
| 6A-07 | Common knowledge, signaling games, Bayesian games | | | 1d | 2.5 |
| 6A-08 | Expected utility theory — vNM axioms, risk preferences | | | 1d | 2.5 |
| 6A-09 | CDT vs EDT vs FDT — three decision theories | | | 1d | 2.5 |
| 6A-10 | Key thought experiments — Newcomb's, Smoking Lesion, Parfit's Hitchhiker | | | 1d | 2.5 |
| 6A-11 | UDT, logical uncertainty, reflective stability | | | 1d | 2.5 |
| 6A-12 | Embedded agency — agents as part of their environment | | | 1d | 2.5 |
| 6A-13 | Anthropics — SSA, SIA, Sleeping Beauty problem | | | 1d | 2.5 |
| 6A-14 | Simulation argument, Doomsday argument, Presumptuous Philosopher | | | 1d | 2.5 |
| 6A-15 | Acausal reasoning and coordination between agents | | | 1d | 2.5 |
| 6A-16 | Zero-sum vs positive-sum framing; minimax as adversarial robustness | | | 1d | 2.5 |
| 6A-17 | Cheap talk vs costly signaling — when can "I am aligned" be trusted? | | | 1d | 2.5 |
| 6A-18 | Counterfactual mugging and the Toxin Puzzle as FDT test cases | | | 1d | 2.5 |

---

## Phase 6B: Alignment (Lessons 83–84)

| # | Topic | Last Review | Next Review | Interval | Ease |
|---|-------|-------------|-------------|----------|------|
| 6B-01 | The core alignment problem — specifying and ensuring beneficial goals | | | 1d | 2.5 |
| 6B-02 | Outer alignment — reward misspecification, Goodhart's Law, specification gaming | | | 1d | 2.5 |
| 6B-03 | Inner alignment — mesa-optimization, mesa-objectives, distributional shift | | | 1d | 2.5 |
| 6B-04 | Deceptive alignment — instrumentally motivated deception during training | | | 1d | 2.5 |
| 6B-05 | Current techniques — RLHF, Constitutional AI, Debate, recursive reward modeling | | | 1d | 2.5 |
| 6B-06 | Scalable oversight and interpretability-based safety | | | 1d | 2.5 |
| 6B-07 | Threat models — power-seeking, treacherous turn, corrigibility, value lock-in | | | 1d | 2.5 |
| 6B-08 | Formal frameworks — AIXI, logical induction, infra-Bayesianism, CIRL | | | 1d | 2.5 |
| 6B-09 | Open problems — scalable oversight, ELK, deception detection, alignment tax | | | 1d | 2.5 |
| 6B-10 | SLT for alignment — RLCT, phase transitions, developmental interpretability | | | 1d | 2.5 |
| 6B-11 | Agent foundations — decision theory, embedded agency, Vingean reflection | | | 1d | 2.5 |
| 6B-12 | Interpretability frontiers — SAEs at scale, causal scrubbing, automated circuit discovery | | | 1d | 2.5 |
| 6B-13 | DPO and sleeper agents — preference optimization without reward model; safety training limitations | | | 1d | 2.5 |
| 6B-14 | Gradual disempowerment — systemic misalignment via economic/cultural displacement | | | 1d | 2.5 |

---

## Summary Statistics

| Phase | Section | Topics | Lessons | Per Lesson |
|-------|---------|--------|---------|------------|
| 0B | CS Foundations (NeetCode Roadmap) | 18 | — | — |
| 1 | Linear Algebra | 65 | 11 | 5.9 |
| 2A | ODEs (incl. Calculus Fundamentals) | 54 | 6 | 9.0 |
| 2B | Multivariable Calculus | 27 | 5 | 5.4 |
| 2C | Vector Calculus | 25 | 5 | 5.0 |
| 2D | PDEs | 34 | 5 | 6.8 |
| 2E | ML-Applied Calculus | 17 | 3 | 5.7 |
| 3A | Core Probability | 20 | 4 | 5.0 |
| 3B | Frequentist Methods | 15 | 3 | 5.0 |
| 3C | Bayesian Deep Dive | 17 | 3 | 5.7 |
| 3D | Applied Statistics | 12 | 2 | 6.0 |
| 3E | ML Theory Foundations | 24 | 4 | 6.0 |
| 4A | Neural Networks & Optimization | 24 | 4 | 6.0 |
| 4B | Architectures | 11 | 2 | 5.5 |
| 4C | Transformers | 13 | 2 | 6.5 |
| 4D | Mechanistic Interpretability | 14 | 2 | 7.0 |
| 4E | Additional ML Topics | 19 | 3 | 6.3 |
| 4F | Singular Learning Theory | 7 | 1 | 7.0 |
| 5A | Computability & Complexity | 18 | 3 | 6.0 |
| 5B | Abstract Algebra | 18 | 3 | 6.0 |
| 5C | Topology & Geometry | 31 | 5 | 6.2 |
| 5D | Formal Logic | 12 | 2 | 6.0 |
| 6A | Game Theory & Decision Theory | 18 | 3 | 6.0 |
| 6B | Alignment | 14 | 2 | 7.0 |
| | | | | |
| **Phase 2 Total** | | **157** | | |
| **Grand Total** | | **571** | | |
