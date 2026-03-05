# Full Concept & Technique Overview

> **Purpose:** A searchable reference of every concept, technique, and tool covered across all 68+ lessons. If you need to check whether a topic is in the curriculum, search this document first.

---

## Phase 0: CS Foundations (Lessons CS-01 through CS-10)

### CS-01: Python Refresher
- Dynamic typing, core types (`int`, `float`, `str`, `bool`, `None`)
- Type checking (`type()`, `isinstance()`)
- String operations: `split`, `strip`, `replace`, `find`, f-strings, slicing
- Control flow: `if/elif/else`, `for`, `while`, `break`, `continue`
- `enumerate()`, `zip()`, ternary expressions
- Functions: `def`, `return`, default arguments, `*args`, `**kwargs`
- Lambda functions, scope (local vs global)
- Lists: `append`, `pop`, `insert`, `sort`, slicing, list comprehensions
- Dictionaries: `.get()`, `.keys()`, `.values()`, `.items()`, dict comprehensions
- Sets: `add`, `remove`, `union`, `intersection`, `difference` — O(1) lookup
- Tuples: immutability, as dict keys, multiple return values
- File I/O: `open()`, `read()`, `readlines()`, `write()`, CSV reading
- Standard library: `collections` (`Counter`, `defaultdict`, `deque`), `itertools`, `functools` (`lru_cache`), `math`, `heapq`

### CS-02: C++ Refresher
- Variables, types, I/O (`cout`, `cin`), strings
- **Pointers** (`int* p = &x`) and **references** (`int& r = x`)
- Dereferencing (`*p`), pass-by-reference, `nullptr`
- **Stack vs heap** memory: stack = local/auto, heap = `new`/`malloc`
- STL containers: `vector`, `unordered_map`, `unordered_set`, `stack`, `queue`, `priority_queue`
- Range-based for loops, iterator-based loops
- Sorting with custom comparators (lambdas)
- **Memory layout**: contiguous arrays (fast, cache-friendly) vs pointer chasing (slow, cache misses)

### CS-03: Object-Oriented Programming
- Classes in Python and C++: `__init__`, `self`, constructors, destructors
- Inheritance, `super()`, method overriding
- Dunder methods: `__repr__`, `__str__`, `__len__`, `__eq__`, `__lt__`, `__add__`
- `@property` decorator
- C++ specifics: `public/private/protected`, `virtual` keyword, initializer lists, `this` pointer
- **Four pillars:** encapsulation, inheritance, polymorphism, abstraction
- **PyTorch pattern:** `nn.Module` subclassing, `__init__` + `forward`

### CS-04: Arrays, Strings, and Hashing
- Array operations: O(1) access, O(1) amortized append, O(n) insert/delete middle
- Hash maps: hash function → bucket index, collision resolution (chaining, open addressing)
- **Two pointers pattern:** one at each end or slow/fast
- **Sliding window pattern:** maintain [left, right] window
- **Frequency counting:** element → count via hash map
- **Prefix sum:** precompute cumulative sums for O(1) range queries

### CS-05: Linked Lists, Stacks, and Queues
- Singly linked lists: `ListNode` with `val` and `next`
- **Dummy head trick** for edge case simplification
- Two-pointer slow/fast (find middle, detect cycles)
- Reverse linked list in-place (prev/curr/next rewiring)
- **Stacks (LIFO):** push, pop, peek — used for DFS, expression evaluation, monotonic stack
- **Queues (FIFO):** enqueue, dequeue — used for BFS, scheduling
- **Deque:** double-ended queue, O(1) operations on both ends (`collections.deque`)

### CS-06: Trees and Graphs
- Binary trees: `TreeNode` with `val`, `left`, `right`
- **Traversals:** inorder (L-Root-R, sorted for BST), preorder (Root-L-R), postorder (L-R-Root, used in backprop)
- **Level-order (BFS)** using queue
- Binary Search Trees: left < parent < right, O(log n) average operations
- Graph representations: adjacency list, edge list
- **DFS** (stack/recursion): path finding, cycle detection, topological sort
- **BFS** (queue): shortest path (unweighted), level-by-level exploration
- Directed vs undirected, weighted vs unweighted graphs

### CS-07: Sorting and Searching
- **Big-O notation:** O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ) — with practical intuitions
- **Merge sort:** O(n log n), stable, divide-and-conquer
- **Quick sort:** O(n log n) average, in-place, better cache behavior
- **Counting/bucket sort:** O(n) for bounded range
- Timsort (Python's built-in)
- **Binary search:** O(log n), works on any monotonic function
- Generalized binary search: "find smallest x where f(x) is True"

### CS-08: Recursion and Dynamic Programming
- Recursion: base case + recursive case, call stack, recursion tree visualization
- **Dynamic Programming:** overlapping subproblems + optimal substructure
- **Top-down (memoization):** recursive + cache (`@lru_cache`)
- **Bottom-up (tabulation):** iterative, fill table small → large
- **Space optimization:** only keep last 1-2 values
- DP framework: define subproblem → recurrence → base cases → computation order → optimize space
- Categories: 1D DP, 2D DP, knapsack (0/1 and unbounded), string DP

### CS-09: Discrete Math Essentials
- **Propositional logic:** AND (∧), OR (∨), NOT (¬), IMPLIES (→), IFF (↔)
- Truth tables, De Morgan's Laws, contrapositive vs converse
- **Proof techniques:** direct proof, contradiction, induction, contrapositive
- **Mathematical induction** and loop invariant proofs
- **Set theory:** union, intersection, difference, complement, Cartesian product
- **Inclusion-exclusion principle:** |A ∪ B| = |A| + |B| − |A ∩ B|
- **Functions:** injective, surjective, bijective
- **Pigeonhole principle**
- **Combinatorics:** permutations P(n,k), combinations C(n,k), with replacement (n^k), stars and bars
- **Binomial theorem:** (a+b)^n = Σ C(n,k) a^(n-k) b^k
- **Hockey stick identity:** C(r,r) + C(r+1,r) + ... + C(n,r) = C(n+1,r+1) — diagonal sums in Pascal's triangle
- **Falling factorial:** x^{(n)} = x(x−1)(x−2)···(x−n+1); P(n,k) = n^{(k)}; C(x,n) = x^{(n)}/n!; natural basis for finite difference calculus and falling factorial decomposition of polynomials
- **Organizing a double sum by its larger index:** reindex Σ_i Σ_j f(i,j) by grouping on max(i,j) = k; L-shaped shells; simplifies nested-loop analysis and combinatorial sum evaluation
- **Graph theory:** vertices, edges, degree, paths, cycles, connected/strongly connected, trees (|E| = |V| − 1), bipartite, planar, Euler's formula V − E + F = 2
- **Modular arithmetic:** congruence, operations mod n, connection to grokking

### CS-10: Computer Organization
- **Binary representation:** base-2, converting decimal ↔ binary, hexadecimal
- **Two's complement** for signed integers
- **IEEE 754 floating point:** sign + exponent + mantissa, float32 vs float16 precision
- Overflow, underflow, loss scaling for float16
- **Bitwise operations:** AND, OR, XOR, NOT, left/right shift
- **Memory hierarchy:** registers → L1/L2/L3 cache → RAM → SSD → HDD (with access times)
- Sequential vs random memory access, cache misses
- **CPU execution:** fetch-decode-execute cycle, registers, stack frames, heap allocation
- Assembly basics: `mov`, `add`, `cmp`, `jl`
- **CPU vs GPU:** few fast cores vs thousands of slow cores, embarrassingly parallel operations
- Memory bandwidth as bottleneck, batching to amortize transfer costs

---

## Phase 0: Setup (Lessons 0–1)

### Lesson 0: Python & NumPy
- NumPy array creation: `np.array`, `np.eye`, `np.zeros`, `np.random.randn`
- Linear algebra operations: `@` (matmul), `np.linalg.inv`, `np.linalg.det`, `np.linalg.eig`, `np.linalg.svd`, `np.linalg.norm`, `.T`
- **Broadcasting** rules
- Matplotlib: `plt.plot`, `plt.scatter`, `plt.quiver` (vectors), `plt.contour`, `plt.imshow` (heatmaps)
- Jupyter notebooks and Google Colab

### Lesson 1: PyTorch
- **Tensors:** NumPy arrays with autograd and GPU support
- Device management (CPU/GPU), `dtype` (float32 default, float16/bfloat16 for large models)
- Converting: `torch.from_numpy()`, `.numpy()`
- **Autograd:** `requires_grad=True`, computation graphs, `loss.backward()`, `.grad`
- `torch.no_grad()`, `.detach()` — disabling gradient tracking
- Dynamic computation graphs (rebuilt each forward pass)
- **Training loop pattern:** `zero_grad()` → forward → loss → `backward()` → `step()`
- Gradient accumulation (PyTorch accumulates by default)
- `model.eval()` vs `model.train()` — toggling dropout/batchnorm
- **nn.Module:** `__init__` + `forward`, `nn.Linear`, `nn.Sequential`
- **Hooks:** `register_forward_hook()` — the atomic operation of interpretability
- **Einops:** `rearrange` for readable tensor reshaping
- **Einsum:** `torch.einsum` for arbitrary tensor contractions
- **DataLoaders:** `Dataset`, `DataLoader`, batching, collate functions, attention masks

---

## Phase 1: Linear Algebra (Lessons 2–12)

### Lesson 2: Vectors
- Vectors as arrows (geometric) AND lists of numbers (computational)
- Vector addition (tip-to-tail), scalar multiplication
- Coordinates are basis-dependent instructions
- Embedding vectors in transformers (~768-dimensional)

### Lesson 3: Linear Combinations, Span, and Basis
- **Linear combination:** a₁v₁ + a₂v₂ + ... + aₙvₙ
- **Span:** all reachable vectors via linear combinations
- **Linear independence** vs dependence
- **Basis:** minimal spanning set, exactly n vectors for ℝⁿ
- **Superposition hypothesis:** networks encode more features than dimensions using non-orthogonal directions

### Lesson 4: Linear Transformations and Matrices
- **Matrices as transformations** of space (not just grids of numbers)
- Columns of a matrix = where basis vectors land
- "Linear" means: lines stay lines, origin stays fixed
- **Linear vs affine:** y = Wx (linear) vs y = Wx + b (affine, what neural network layers actually are)
- Matrix-vector multiplication = "where does this vector land?"
- **Matrix multiplication as composition:** AB means "apply B, then A"
- Non-commutativity: AB ≠ BA in general

### Lesson 5: Matrix Operations
- **Two views of matrix-vector multiplication:**
  - Row view: dot products (pattern matching)
  - Column view: linear combination of columns
- Matrix-matrix multiplication = composition of transformations
- Transpose: (AB)ᵀ = BᵀAᵀ (reverse order rule)
- Associativity: (AB)C = A(BC)
- **QK and OV circuits** in transformers as matrix compositions

### Lesson 6: Rank, Null Space, and Column Space
- **Column space:** all possible outputs of Ax (span of columns)
- **Null space (kernel):** all x where Ax = 0 (vectors crushed to zero)
- **Rank:** dimension of column space = number of independent directions in output
- **Rank-nullity theorem:** rank + nullity = number of columns
- **Gaussian elimination / row reduction:** row echelon form, reduced row echelon form (RREF)
- Pivot columns, free variables, reading solutions from RREF
- Attention matrices are deliberately **low-rank** (e.g., 768 → 64 → 768)

### Lesson 7: The Determinant
- **Determinant = scaling factor for area/volume** under transformation
- det = 0 ↔ rank deficient ↔ non-invertible ↔ non-trivial null space
- det < 0 ↔ orientation flip
- det(AB) = det(A)·det(B)
- Computing 2×2 and 3×3 determinants
- Cofactor expansion
- Vanishing/exploding gradients and determinant magnitudes

### Lesson 8: Eigenvalues and Eigenvectors
- **Eigenvector:** direction unchanged by transformation (Av = λv)
- **Eigenvalue λ:** the scaling factor
- **Characteristic equation:** det(A − λI) = 0
- **Diagonalization:** A = PDP⁻¹ (change to eigenbasis → scale → change back)
- Powers: Aⁿ = PDⁿP⁻¹
- PCA finds eigenvectors of covariance matrix
- Hessian eigenvalues = loss landscape curvature

### Lesson 9: Singular Value Decomposition (SVD)
- **A = UΣVᵀ** — rotate (V) → scale (Σ) → rotate (U)
- Works for ANY matrix (rectangular, rank-deficient)
- Singular values σ₁ ≥ σ₂ ≥ ... ≥ 0
- Rank = number of non-zero singular values
- **Low-rank approximation:** Eckart–Young theorem (best rank-k approx)
- Connection to eigendecomposition: singular values = √(eigenvalues of AᵀA)
- **SVD and PCA:** AᵀA = VΣ²Vᵀ, so PCA directions = V columns
- LoRA (Low-Rank Adaptation) for efficient fine-tuning

### Lesson 10: Dot Products, Orthogonality, and Projections
- **Dot product:** algebraic (sum of products) = geometric (|a||b|cos θ)
- Dot product as **projection** (shadow of one vector onto another)
- Sign: positive (same direction), zero (perpendicular), negative (opposite)
- **Cosine similarity:** â · b̂ — direction-only similarity measure
- **Orthogonality:** a · b = 0 (completely independent directions)
- **Orthonormal basis:** unit length + mutually perpendicular vectors
- **Orthogonal matrices:** QᵀQ = I, pure rotations/reflections, preserve lengths
- **Projection onto a vector:** proj_v(u) = (u·v / v·v)v
- **Projection onto a subspace:** P = A(AᵀA)⁻¹Aᵀ, idempotent (P² = P)
- **Least squares:** x̂ = (AᵀA)⁻¹Aᵀb (least squares IS projection)
- **Gram-Schmidt process:** converting any basis to orthonormal
- **Attention IS dot products** → softmax → linear combinations

### Lesson 11: Change of Basis, Norms, and Special Matrices
- **Change of basis:** B⁻¹v converts coordinates; B⁻¹AB = same transformation in new basis
- Eigendecomposition AS change of basis: A = PDP⁻¹
- SVD AS two changes of basis
- **Norms:**
  - L2 (Euclidean), L1 (Manhattan, encourages sparsity), L∞ (max)
  - Frobenius norm (matrix as vector), spectral norm (largest singular value)
  - **Norm balls:** L2 = circle, L1 = diamond (corners → sparsity), L∞ = square
- **Symmetric matrices:** real eigenvalues, orthogonal eigenvectors, always diagonalizable (A = QDQᵀ)
- **Positive definite:** all eigenvalues > 0, xᵀAx > 0, "bowl shape"
- **Positive semi-definite (PSD):** eigenvalues ≥ 0, AᵀA always PSD
- **Trace:** tr(A) = sum of diagonal = sum of eigenvalues, tr(AB) = tr(BA)
- **Cholesky decomposition:** A = LLᵀ for positive definite matrices (matrix square root)
  - Used for sampling multivariate Gaussians, solving covariance systems
- **Inner product of functions:** ⟨f,g⟩ = ∫f(x)g(x)dx, orthogonal functions, function spaces
- **Matrix phylogeny:** family tree of matrix types and their relationships
- Weight decay = L2 regularization, gradient clipping, layer normalization, spectral norm

### Lesson 12: Linear Algebra Capstone
- **Unified picture:** any matrix = rotate → scale → rotate (SVD)
- Integration exercise connecting all Phase 1 concepts through a single matrix
- SVD decomposition visualization

---

## Phase 2: Calculus (Lessons 13–23, 28–81)

### Block A: ODEs (Lessons 13–18)

### Lesson 13: Calculus Fundamentals
- Derivative as rate of change, limit definition, local linearity
- Differentiation rules: power, product, quotient, chain rule
- Key derivatives: eˣ, ln(x), sigmoid, ReLU, tanh
- Integration: FTC, u-substitution, integration by parts, improper integrals
- Limits, L'Hopital's rule, MVT, IVT, sequences and series foundations

### Lesson 14: Introduction to ODEs
- ODE as vector field: dx/dt = f(x,t)
- Gradient descent as Euler's method on gradient flow ODE
- Solution curves, existence/uniqueness, fixed points
- 1D stability analysis: f'(x*) < 0 stable, f'(x*) > 0 unstable

### Lesson 15: First-Order ODEs
- Separable equations, integrating factors, exact equations
- Linear first-order ODEs and solution methods
- Phase line analysis and qualitative behavior
- Applications: exponential growth/decay, logistic equation

### Lesson 16: Higher-Order ODEs, Mechanical Vibrations, and Power Series Solutions
- Characteristic equation for constant-coefficient ODEs: three cases (distinct real, repeated, complex)
- Higher-order constant-coefficient ODEs via higher-degree characteristic polynomials
- Wronskian and linear independence of solutions; Abel's theorem
- Mechanical vibrations: undamped, overdamped, critically damped, underdamped, forced, resonance
- Undetermined coefficients and variation of parameters for nonhomogeneous equations
- Power series solutions: assume y = sum a_n x^n, find recurrence relations
- Ordinary vs singular points; Airy's equation as canonical example

### Lesson 17: Laplace Transform
- Definition, linearity, transforms of common functions
- Solving ODEs via Laplace transform (algebraic method)
- Transfer functions and system analysis
- Inverse Laplace transform, convolution theorem

### Lesson 18: Systems of ODEs
- Coupled systems, state-space representation
- Gradient flow: dW/dt = -nabla L(W), loss as Lyapunov function
- Euler stability criterion, momentum as second-order ODE
- Lyapunov stability, bifurcations (saddle-node, pitchfork), phase transitions in training

### Block B: Multivariable Calculus (Lessons 19–23)

### Lesson 19: 3D Geometry, Curves, and Curvature
- Lines and planes in 3D, parametric and symmetric equations
- Vector-valued functions r(t), tangent vectors, arc length
- Curvature kappa, osculating circle, TNB (Frenet-Serret) frame
- Reparameterization by arc length, geometry vs kinematics

### Lesson 20: Multivariable Functions, Limits, and Partial Derivatives
- Functions f: R^n -> R, domain, range, level curves and surfaces
- Limits and continuity in several variables
- Partial derivatives, gradient vector, higher-order partials
- Gradients perpendicular to contour lines, steepest ascent

### Lesson 21: The Chain Rule, Directional Derivatives, and Gradients
- Single-variable and multivariable chain rule
- Jacobian matrix: derivative of vector-to-vector functions
- Directional derivatives, gradient field visualization
- Computation graphs, forward pass vs backward pass

### Lesson 22: Optimization, Taylor Expansions, and the Implicit Function Theorem
- Critical points, Hessian matrix, second derivative test
- Lagrange multipliers, the Lagrangian, KKT conditions
- Taylor expansion: zeroth, first, second order approximations
- Multivariate Taylor: local landscape as quadratic form of the Hessian
- Implicit function theorem, failure at singularities (bifurcation points, SLT)
- Loss landscapes, saddle points, convex optimization

### Lesson 23: Multiple Integration and Change of Variables
- Double/triple integrals, iterated integration, Fubini's theorem
- Change of variables, Jacobian determinant as local stretching
- Polar/spherical coordinates, the Gaussian integral via polar coordinates
- Monte Carlo integration, importance sampling, reparameterization trick

### Block C: Vector Calculus (Lessons 24–27, 28)

### Lesson 24: Line Integrals
- Parametric curves, tangent vectors, reparameterization, arc length parameterization
- Scalar line integrals: accumulating a scalar field along a curve
- Line integrals in 2D and 3D
- Distinguishing types of line integrals: scalar (ds) vs component (dx, dy, dz)
- Piecewise-smooth curves

### Lesson 25: Vector Fields
- Vector fields in 2D and 3D, gradient vector fields and potential functions
- Divergence: sources and sinks, div(F) = nabla . F
- Curl in 2D (scalar curl): circulation density
- Line integral of a vector field (work), line integrals w.r.t. x, y, z
- Flux integrals with components
- Fundamental theorem for line integrals, path independence
- Conservative field test, exact and closed forms
- Finding potential functions, simply connected domains

### Lesson 26: Green's Theorem
- Green's theorem (circulation form): boundary circulation = interior curl integral
- Green's theorem (flux/divergence form): boundary flux = interior divergence integral
- Composite (multiply-connected) regions: domains with holes, boundary orientations
- The Laplacian, harmonic functions
- Applications: area computation, fluid flow, electrostatics

### Lesson 27: Surface Integrals
- Parametric surfaces, visualizing and understanding surfaces in 3D
- Surface area element, normal vectors via cross product
- Why curl is useful: spider criteria for conservative fields
- The 3D curl test for conservative fields (curl F = 0)
- Scalar and vector surface integrals (flux)
- Orientation of surfaces, orientability (Mobius strip)

### Lesson 28: Stokes' Theorem and the Divergence Theorem
- Stokes' theorem: circulation integral = curl flux through surface
- Computing Stokes' theorem: converting between surface and line integrals
- Divergence theorem: flux through closed surface = divergence integral over volume
- Finding sources and sinks using the divergence theorem
- Generalized Stokes' theorem unifying FTC, Green's, classical Stokes', divergence
- Differential forms (conceptual), connections to topology and gauge theory

### Block D: PDEs (Lessons 29–33)

### Lesson 29: Heat Equation, Separation of Variables, and Laplace's Equation
- u_t = k nabla^2 u, diffusion as Gaussian blurring
- Separation of variables, boundary conditions (Dirichlet, Neumann)
- Laplace equation (steady-state heat), maximum principle
- Forward process of diffusion models as progressive noise addition

### Lesson 30: Fourier Series and the Wave Equation
- Fourier series: representing functions as sums of sinusoids
- Fourier coefficients, convergence, Gibbs phenomenon
- u_tt = c^2 nabla^2 u, traveling wave solutions, d'Alembert's formula
- Standing waves, normal modes, superposition

### Lesson 31: Eigenvalue Problems and Sturm-Liouville Theory
- Sturm-Liouville eigenvalue problems, orthogonal eigenfunctions
- Regular and singular Sturm-Liouville problems
- Eigenfunction expansions, completeness
- Connections to spectral methods in ML

### Lesson 32: Helmholtz Equation, Fourier Transform, and Infinite Domains
- Helmholtz equation (frequency-domain wave), eigenvalue problems
- Fourier transform for PDEs on infinite domains
- Laplace equation in polar/spherical coordinates
- Connections to spectral methods and graph Laplacians in ML

### Lesson 33: Method of Characteristics, Transport Equations, and PDEs in ML
- Transport equation, method of characteristics
- Fokker-Planck equation: probability evolution during SGD
- Score function, score matching, reverse SDE for diffusion models
- Probability flow ODE, continuous normalizing flows
- Neural operators and physics-informed neural networks (PINNs)

### Block E: ML Calculus (Lessons 34–36)

### Lesson 34: Scalar Derivatives, Partial Derivatives, and the Gradient
- Scalar derivative rules review: constant, power, sum, product, chain
- Partial derivatives: treat all variables except target as constants
- The gradient: nabla f = [df/dx_1, ..., df/dx_n] — row vector of all partials
- Gradient as direction of steepest ascent

### Lesson 35: Matrix Calculus — Jacobians, Element-wise Rules, and Chain Rules
- Jacobian matrix: J_{ij} = df_i/dx_j for f: R^n -> R^m (m x n, numerator layout)
- Element-wise operations yield diagonal Jacobians: d(w circ x)/dw = diag(x)
- Scalar expansion and vector sum reduction rules
- Dot product gradient: d(w . x)/dw = x^T, d(w . x)/dx = w^T
- Vector chain rule: df/dx = (df/dg)(dg/dx) — Jacobian multiplication IS backpropagation

### Lesson 36: Neural Network Gradients — From Neurons to Backpropagation
- Gradient of neuron activation: f = max(0, w . x + b), chain rule through ReLU
- Gradient of MSE loss w.r.t. weights and bias
- ReLU gating: zero gradient when inactive, pass-through when active
- Computation graphs, forward-mode vs reverse-mode autodiff
- Reverse mode = backpropagation: 1 backward pass for all parameters

---

## Phase 3: Probability & Statistics (Lessons 37–52)

### Lesson 37: Probability Distributions and Bayes' Theorem
- Probability axioms, conditional probability, independence
- **Bayes' theorem:** P(A|B) = P(B|A)P(A)/P(B)
- Common distributions: Bernoulli, binomial, Gaussian/normal, Poisson, uniform, exponential
- **Central Limit Theorem:** averages of random variables → Gaussian
- **Change of variables for probability:** p(y) = p(f⁻¹(y))·|det(J_f⁻¹)| (Jacobian factor)
- Joint, marginal, conditional distributions
- **Law of total probability**

### Lesson 38: Expectation, Variance, and Covariance
- **Expected value:** E[X] = Σ xP(x) (weighted average)
- **Variance:** Var(X) = E[(X−μ)²] = E[X²] − (E[X])²
- **Standard deviation:** σ = √Var
- **Covariance:** Cov(X,Y) = E[(X−μ_X)(Y−μ_Y)]
- **Correlation:** ρ = Cov(X,Y)/(σ_X σ_Y), normalized to [−1, 1]
- **Covariance matrix:** symmetric, PSD
- Linearity of expectation
- Law of large numbers, moment generating functions

### Lesson 39: Maximum Likelihood Estimation
- **Likelihood:** L(θ) = P(data | θ) — probability of data given parameters
- **MLE:** θ̂ = argmax P(data | θ), equivalently minimize −log likelihood
- **Cross-entropy loss = negative log-likelihood** for classification
- **Properties of MLE:** consistent, asymptotically normal, asymptotically efficient
- **EM Algorithm (Expectation-Maximization):**
  - E-step: compute expected assignments given current parameters
  - M-step: update parameters given expected assignments
- **Gaussian Mixture Models (GMMs):** EM for fitting multiple Gaussians
- **K-means as hard EM** (hard vs soft assignments)

### Lesson 40: Information Theory
- **Information content:** I(x) = −log₂ P(x) — rare events carry more info
- **Entropy:** H(X) = −Σ P(x) log P(x) — average surprise
  - Maximum entropy = uniform distribution
- **Cross-entropy:** H(P,Q) = −Σ P(x) log Q(x) — encoding cost using wrong distribution
- **KL divergence:** D_KL(P‖Q) = H(P,Q) − H(P) ≥ 0 — "extra bits wasted"
- **Temperature in softmax:** T controls entropy of output distribution
- **Mutual information:** I(X;Y) = H(X) − H(X|Y) — what X tells you about Y
- **Conditional mutual information:** I(X;Y|Z)
- **Data Processing Inequality:** X→Y→Z implies I(X;Z) ≤ I(X;Y)
- **Information Bottleneck principle:** compress input, preserve output information
- Two-phase learning: fitting then compressing
- **Pointwise Mutual Information (PMI):** log[P(x,y)/(P(x)P(y))], connection to Word2Vec

### Lesson 41: Hypothesis Testing
- **Null hypothesis (H₀)** vs **alternative hypothesis (H₁)**
- **P-value:** P(data ≥ this extreme | H₀ true) — NOT P(H₀ | data)
- **Base rate fallacy:** P(data|H₀) ≠ P(H₀|data)
- **p < 0.05 threshold** and its problems
- **Multiple comparisons:** Bonferroni correction, False Discovery Rate (FDR), Benjamini-Hochberg
- **P-hacking, garden of forking paths**
- **Type I error** (false positive, α), **Type II error** (false negative, β)
- **Statistical power** = 1 − β
- **Effect sizes:** Cohen's d, Pearson's r, odds ratio — what p-values don't tell you
- **Confidence intervals:** repeated-experiment interpretation (not probability of containing truth)

### Lesson 42: Experimental Design and Statistical Fallacies
- **Randomization, control groups, blinding** (single, double), **pre-registration**
- **Hierarchy of evidence:** case reports → observational → RCTs → meta-analyses
- **Correlation ≠ causation** (confounders)
- **Simpson's paradox:** trend reverses when groups combined
- **Survivorship bias**
- **Base rate neglect / prosecutor's fallacy**
- **Ecological fallacy:** group-level ≠ individual-level relationships
- **Regression to the mean**

### Lesson 43: Regression
- **Linear regression:** y = β₀ + β₁x₁ + ... + ε, ε ~ N(0,σ²)
- Standard errors, t-tests on coefficients, confidence intervals
- **R² (coefficient of determination)**
- **Multiple regression:** "controlling for" variables, partial effects
- **Multicollinearity:** correlated predictors → unreliable individual coefficients
- Adjusted R²
- **Logistic regression:** P(y=1|x) = σ(β₀ + β₁x₁ + ...), sigmoid function
- Coefficients in log-odds, odds ratios (OR = e^β)
- Single neuron with sigmoid = logistic regression
- **Generalized Linear Models (GLMs):** unified framework with link functions
- Assumptions: linearity, independence, homoscedasticity
- **Robust standard errors** (Huber-White)

### Lesson 44: Bayesian Foundations
- **Bayesian vs frequentist:** probability as degree of belief vs long-run frequency
- **Bayes' theorem as update rule:** posterior ∝ likelihood × prior
- **Priors:** informative, weakly informative, "uninformative" (Jeffreys)
- **Priors as regularization:** L2 = Gaussian prior, L1 = Laplace prior, dropout = approximate prior
- **Conjugate priors:** posterior same form as prior
  - Beta-Binomial, Normal-Normal, Dirichlet-Multinomial
- **MAP estimation:** argmax [log likelihood + log prior] = MLE + regularization
- MAP loses uncertainty information
- **Sequential updating:** today's posterior = tomorrow's prior
- Bayesian agent as normative model of rational belief updating

### Lesson 45: Bayesian Computation
- **The computational problem:** P(D) = ∫P(D|θ)P(θ)dθ is intractable
- **MCMC (Markov Chain Monte Carlo):** construct chain whose stationary distribution = posterior
  - **Metropolis-Hastings:** propose → accept/reject (normalizing constants cancel)
  - **Gibbs sampling:** update one parameter at a time from conditional
  - Diagnostics: burn-in, thinning, R-hat, effective sample size
- **Hamiltonian Monte Carlo (HMC):** physics-inspired gradient-based sampling
  - Leapfrog integration, NUTS (No-U-Turn Sampler)
- **Variational Inference (VI):** approximate posterior with simple distribution
  - Minimize KL(q_φ ‖ P(θ|D)) by maximizing **ELBO**
  - **ELBO** = E_q[log P(D|θ)] − KL(q‖prior) = log P(D) − KL(q‖posterior)
  - **Mean-field approximation:** assume q factors as product of independent distributions
- **VAE connection:** encoder = variational params, decoder = likelihood, VAE loss = negative ELBO
- **Laplace approximation:** Gaussian at MAP with covariance = inverse Hessian

### Lesson 46: Bayesian Model Comparison
- **Marginal likelihood (evidence):** P(D|M) = ∫P(D|θ,M)P(θ|M)dθ
- **Automatic Occam's razor:** complex models spread prior over more patterns → lower evidence for specific data
- **Bayes factors:** BF₁₂ = P(D|M₁)/P(D|M₂), can support null hypothesis (unlike p-values)
- **BIC approximation:** −2log P(D|θ̂) + k log n
- BIC ≈ log marginal likelihood for regular models
- **BIC fails for neural networks** (singular models, Fisher information degenerate)
- **WAIC:** Bayesian generalization of AIC, works for singular models
- **LOO-CV (PSIS-LOO):** gold standard predictive model comparison
- **Free energy:** F = −log P(D|M) — minimizing = maximizing evidence
- **SLT correction:** F ≈ nL(θ̂) + λ log n − (m−1)log log n
  - **RLCT (λ)** replaces k/2 as true effective dimension
  - For neural networks: λ ≤ d/2 (simpler than parameter count suggests)

### Lesson 47: Causal Inference
- **Counterfactuals:** what would have happened differently?
- **Potential outcomes framework (Rubin):** Y₁ᵢ, Y₀ᵢ, causal effect = Y₁ − Y₀
- **Average Treatment Effect (ATE)**
- **Directed Acyclic Graphs (DAGs):** causal diagrams
- **Three fundamental patterns:**
  - **Chains** (mediation): X → M → Y
  - **Forks** (confounding): X ← Z → Y
  - **Colliders:** X → Z ← Y (conditioning on Z creates spurious association)
- **d-separation** rules
- Controlling for confounders (good) vs mediators (sometimes bad) vs colliders (always bad)
- **Causal inference methods:**
  - **Instrumental variables (IV):** find Z that affects X but not Y directly
  - **Difference-in-differences**
  - **Regression discontinuity**
  - **Propensity score matching**
- **Mendelian randomization:** genetic variants as natural instruments

### Lesson 48: Applied Statistics
- **Heritability (h²):** fraction of trait variation from genetic variation (population-level, NOT individual)
- Between-group heritability ≠ between-group genetic causation
- **Twin studies:** identical vs fraternal twins, assumptions and violations
- **GWAS:** genome-wide association, p < 5×10⁻⁸ threshold, tiny effect sizes
- **Polygenic scores (PRS)**
- **Population stratification:** ancestry as confounder, PCA correction
- **Missing heritability problem**
- **Nature-nurture debate:** high within-group heritability ≠ between-group genetic cause
- **Epidemiology:** observational study evaluation, Bradford Hill criteria
- **Nutrition science:** confounders everywhere, healthy user bias
- Statistical adjudication of empirical claims

### Lesson 49: Concentration Inequalities — From Markov to Chernoff
- **The tightening ladder:** Markov → Chebyshev → Hoeffding → Chernoff (more assumptions → tighter bounds)
- **Markov's inequality:** P(X ≥ t) ≤ μ/t (uses only the mean, very general but weak)
- **Chebyshev's inequality:** P(|X−μ| ≥ t) ≤ σ²/t² (adds variance, polynomial decay)
- **Hoeffding's inequality:** P(|S̄−μ| ≥ t) ≤ 2exp(−2nt²/(b−a)²) (exponential decay for bounded averages)
- **Chernoff bounds:** optimize over t in P(X ≥ a) ≤ E[e^{tX}]/e^{ta} — uses MGF, tightest possible
- **Sub-Gaussian variables:** MGF bounded by Gaussian MGF → automatic Hoeffding-type tails
- **Union bound:** P(∪Aᵢ) ≤ ΣP(Aᵢ) — needed for simultaneous guarantees over multiple parameters
- **ML connection:** generalization guarantees, RLHF reward estimation reliability, safety evaluation sample sizes

### Lesson 50: Markov Chains and Mixing
- **Markov property:** P(X_{n+1} | X_n, ..., X_0) = P(X_{n+1} | X_n) — future depends only on present
- **Transition matrix P:** Pᵢⱼ = P(X_{n+1}=j | Xₙ=i), each row sums to 1 (stochastic matrix)
- **n-step transitions:** (i,j) entry of Pⁿ — matrix powers from linear algebra
- **Stationary distribution:** πP = π — left eigenvector of P with eigenvalue 1
- **Ergodicity:** irreducible + aperiodic → converges to unique π from any start
- **Mixing time:** τ_mix ≈ 1/(1−λ₂) — eigenvalue gap determines convergence speed
- **Detailed balance:** π(i)P(i→j) = π(j)P(j→i) — reversibility, basis of Metropolis-Hastings
- **PageRank:** stationary distribution of random web surfer = dominant eigenvector
- **ML connection:** RL as MDP, MCMC convergence, SGD as Markov chain on parameter space

### Lesson 51: Fisher Information and Exponential Families
- **Score function:** s(θ) = ∂/∂θ log p(x|θ), E[s(θ)] = 0
- **Fisher information:** I(θ) = Var(score) = −E[∂²/∂θ² log p(x|θ)] — curvature of log-likelihood
- **Fisher information matrix:** I(θ)ᵢⱼ = E[∂ᵢ log p · ∂ⱼ log p] — defines Riemannian metric on parameter space
- **Cramér-Rao bound:** Var(θ̂) ≥ 1/(nI(θ)) — fundamental speed limit on estimation
- **Natural gradient:** Ĩ∇L = I(θ)⁻¹∇L — geometry-aware optimization (explains why Adam works)
- **Exponential families:** p(x|θ) = h(x)exp(ηᵀT(x) − A(η)) — Gaussian, Bernoulli, Poisson, categorical
- **Sufficient statistics:** T(X) captures ALL information about θ — compress without losing anything
- **ML connection:** natural gradient ≈ Adam, singular Fisher matrix → SLT, information geometry

### Lesson 52: PAC Learning and Generalization Bounds
- **Generalization gap:** |L(h) − L̂(h)| — difference between true and empirical risk
- **PAC framework:** with probability ≥ 1−δ, true error ≤ empirical error + ε, given n ≥ n₀(ε, δ, H)
- **Finite classes:** n ≥ (1/2ε²)log(2|H|/δ) — only logarithmic in hypothesis count
- **VC dimension:** largest number of points H can shatter; VC(linear in ℝᵈ) = d+1
- **VC bound:** sample complexity n = O(d/ε² · log(d/ε))
- **Rademacher complexity:** data-dependent measure — how well can H fit random noise?
- **PAC-Bayes:** E_Q[L(h)] ≤ E_Q[L̂(h)] + √(D_KL(Q‖P) + log(n/δ))/(2n) — tightest practical bounds
- **Why classical bounds fail for deep learning:** implicit regularization, compression, SLT (RLCT < parameter count)
- **ML connection:** safety evaluation guarantees, alignment tax quantification, distributional shift

---

## Phase 4: Machine Learning (Lessons 53–66)

### Block A: Core ML (Lessons 53–62)

### Lesson 53: Perceptron
- Perceptron model: weighted sum + bias + activation
- Linear decision boundary (hyperplane)
- Step function, sigmoid, ReLU activations
- Perceptron learning rule
- XOR problem: single neurons can't solve non-linear problems

### Lesson 54: Gradient Descent
- Gradient descent: W <- W - eta nabla L(W)
- SGD: mini-batch gradient estimates, learning rate tuning
- Momentum, Nesterov acceleration
- Convexity vs non-convexity of neural network loss

### Lesson 55: Backpropagation
- Full network gradient computation via chain rule
- Backprop = reverse-mode autodiff on computation graph
- Gradient flow through layers, vanishing/exploding gradients
- Residual connections, batch/layer normalization, gradient checking

### Lesson 56: Deep Learning
- Multi-layer networks: stacking linear transformations + nonlinearities
- Forward pass = sequence of matrix multiplications + activations
- ReLU folds space, universal approximation theorem
- Width vs depth tradeoffs, representation learning

### Lesson 57: AlexNet and CNNs
- Convolutional layers: local receptive fields, weight sharing
- Pooling, stride, feature hierarchies (edges -> textures -> objects)
- AlexNet as the deep learning watershed moment
- Modern CNN architectures, transfer learning

### Lesson 58: Scaling Laws
- Kaplan scaling laws: L(N) proportional to N^(-alpha)
- Chinchilla scaling: optimal data/params ratio ~20:1
- The bitter lesson (Rich Sutton): scale wins over cleverness
- Emergent capabilities, measurement artifact debate, grokking as phase transition

### Lesson 59: Attention — Dot Products in Action
- Query, Key, Value vectors: Q = xW_Q, K = xW_K, V = xW_V
- Attention scores: QK^T/sqrt(d_k), softmax as probability distribution
- Multi-head attention, causal/autoregressive masking
- Multi-head Latent Attention (MLA, DeepSeek variant)

### Lesson 60: Transformer Architecture
- Full transformer block: LayerNorm -> MHA -> Residual -> LayerNorm -> MLP -> Residual
- Residual stream view, positional encoding (sinusoidal or learned)
- QK circuit and OV circuit analysis
- "Mathematical Framework for Transformer Circuits" (Elhage, Nanda et al.)

### Lesson 61: Mechanistic Interpretability
- Mechanistic interpretability: reverse-engineering model internals
- Activation patching, direct logit attribution, probing
- Induction heads, feature circuits, steering vectors
- Sparse autoencoders (SAEs), superposition, monosemantic vs polysemantic neurons

### Lesson 62: Diffusion Models
- Forward process: progressive noise addition (heat equation connection)
- Reverse process: learned denoising, score function estimation
- Score matching, reverse SDE, probability flow ODE
- DDPM, classifier-free guidance, connections to Fokker-Planck

### Block B: Applied ML (Lessons 50, 82)

### Lesson 63: RL Foundations
- Agent, Environment, State, Action, Reward framework
- MDP, policy pi(a|s), value function V(s), Q-function Q(s,a)
- Policy gradient methods, PPO, value-based methods (Q-learning, DQN)
- Reward shaping, specification gaming, Goodhart's Law, reward hacking

### Lesson 64: LLM Pipeline
- Pre-training: next-token prediction (MLE), scaling laws
- SFT: supervised fine-tuning on demonstrations
- RLHF / DPO / Constitutional AI: preference optimization
- KL penalty, credit assignment, deployment and monitoring

### Block C: Interpretability Theory (Lessons 65–66)

### Lesson 65: Circuits and Superposition
- Superposition hypothesis: more features than dimensions via near-orthogonality
- SAE training and feature dictionaries for auditing model internals
- Induction head circuit: previous token head + induction head composition
- IOI circuit in GPT-2, developmental interpretability

### Lesson 66: Singular Learning Theory (SLT)
- Neural networks are singular: many-to-one parameter-to-function map
- Symmetries create singularities, Fisher information is singular
- RLCT (Real Log Canonical Threshold): true effective complexity, lambda <= d/2
- Free energy formula, LLC tracking, phase transitions as bifurcations in training

---

## Phase 5: Mathematical Enrichment (Lessons 67–79)

### Lesson 67: Turing Machines and Decidability
- **Turing machine:** tape + head + states + transition function — formal definition of computation
- Church-Turing thesis: anything computable is Turing-computable
- **Halting problem:** no algorithm can determine if arbitrary programs halt — **undecidable**
- Proof by contradiction using diagonalization
- **Rice's theorem:** every non-trivial semantic property of programs is undecidable
- Decidability landscape: decidable, semi-decidable, undecidable

### Lesson 68: Computational Complexity
- **P:** problems solvable in polynomial time
- **NP:** solutions verifiable in polynomial time
- **NP-complete:** hardest problems in NP (via polynomial reductions)
- **P vs NP** — open problem
- Cook-Levin theorem (SAT is NP-complete)
- NP-hardness in ML: training neural networks, feature selection
- **Space complexity:** PSPACE
- **Circuit complexity:** neural networks as Boolean circuits

### Lesson 69: Kolmogorov Complexity and Algorithmic Information
- **Kolmogorov complexity K(x):** length of shortest program generating x
- Incompressible strings (random)
- K(x) is **uncomputable** (related to halting problem)
- Connection to Shannon entropy: E[K(x)] ≈ H(X)
- **Solomonoff induction:** universal prior P(x) = 2^{-K(x)}, optimal prediction
- **AIXI:** Solomonoff induction + expected utility maximization = theoretically optimal agent
- Incomputable but provides theoretical ideal for agent design
- Minimum Description Length (MDL) principle

### Lesson 70: Group Theory
- **Group:** set + operation satisfying closure, associativity, identity, inverses
- Examples: integers under addition, permutation groups S_n, cyclic groups Z_n, matrix groups GL(n), SO(n), dihedral groups
- **Subgroups, cosets, quotient groups** G/N
- **Lagrange's theorem:** |H| divides |G|
- **Homomorphisms and isomorphisms**
- **First isomorphism theorem**
- Abelian vs non-abelian groups
- **Normal subgroups**

### Lesson 71: Rings, Fields, and Algebraic Structures
- **Rings:** set with + and ×, additive group + multiplicative monoid
- Examples: integers Z, polynomials R[x], matrix rings
- **Fields:** rings where every nonzero element has multiplicative inverse (Q, R, C, F_p)
- **Ideals and quotient rings**
- **Modules and vector spaces** (vector space = module over a field)
- **Noetherian rings, Hilbert Basis Theorem**
- **Polynomial rings** — foundation for algebraic geometry

### Lesson 72: Group Actions, Representations, and Neural Network Symmetry
- **Group actions:** group acts on a set (orbits, stabilizers)
- **Neural network symmetries:** neuron permutation symmetry in hidden layers
- **Orbit-stabilizer theorem** and connection to SLT (parameter symmetries create singularities)
- **Group representations:** encoding symmetries as matrices
- Character theory basics
- **Equivariant neural networks:** architectures preserving symmetries (CNNs = translation equivariance)

### Lesson 73: Point-Set Topology
- **Topological spaces:** defined by open sets satisfying axioms
- **Continuity:** topological definition (preimage of open is open)
- **Compactness:** every open cover has finite subcover
  - Heine-Borel: closed + bounded ⊂ ℝⁿ ↔ compact
  - Extreme value theorem requires compactness
- **Connectedness:** cannot be split into two disjoint open sets
- **Path-connectedness** (stronger than connectedness)
- **Hausdorff spaces:** points can be separated by open sets
- Homeomorphisms (topological equivalence)

### Lesson 74: Homotopy and Fundamental Groups
- **Homotopy:** continuous deformation of one map into another
- Homotopy equivalence of spaces
- **Fundamental group π₁:** loops up to continuous deformation
  - π₁(circle) = Z, π₁(sphere) = 0, π₁(torus) = Z×Z
- **Higher homotopy groups πₙ**
- **Covering spaces:** unwinding topology
- Loss landscape topology: holes and non-contractible loops

### Lesson 75: Manifolds and Tangent Spaces
- **Smooth manifolds:** locally Euclidean spaces with smooth transition maps
- Examples: spheres, tori, weight space as manifold
- **Tangent spaces and tangent bundles**
- **Riemannian metrics:** inner product on tangent spaces (measuring on curved spaces)
- **Manifold hypothesis:** real-world data lies on low-dimensional manifold in high-dimensional space
- **Singularities:** where manifold structure breaks down (key for SLT)

### Lesson 79: Differential Forms and Stokes' Theorem
- **k-forms:** 0-forms = functions, 1-forms = integrable along curves, 2-forms = over surfaces, 3-forms = volumes
- **Wedge product ∧:** antisymmetric (dx∧dy = −dy∧dx, dx∧dx = 0) — captures oriented area/volume
- **Connection to determinants:** (dx∧dy)(u,v) = det[u|v] — wedge product IS the determinant
- **Exterior derivative d:** unifies grad (d on 0-forms), curl (d on 1-forms), div (d on 2-forms)
- **d² = 0:** curl(grad f) = 0 and div(curl F) = 0 are both consequences of this single fact
- **Generalized Stokes' theorem:** ∫_∂M ω = ∫_M dω — unifies FTC, Green's, Stokes', Divergence theorems
- **Pullbacks φ*:** how forms transform under maps — the change of variables formula IS a pullback
- **De Rham cohomology:** Hᵏ(M) = {closed k-forms}/{exact k-forms} — detects topological holes via calculus
- **ML connection:** normalizing flows (change of variables = pullback), Fisher metric as 2-tensor, SLT blow-up pullbacks

### Lesson 76: Algebraic Geometry Essentials
- **Algebraic varieties:** solution sets of polynomial equations
- Affine varieties, projective varieties
- **Smooth vs singular points:** Jacobian rank condition
- **Blow-ups:** resolution of singularities
  - Replace a point with the space of directions through it
- **The RLCT (Real Log Canonical Threshold):** computed via resolution of singularities
  - Blow up the singularity → compute how the volume form transforms → extract λ
- **Computing RLCTs for examples:** linear regression, reduced rank regression, neural networks
- Direct connection to SLT: algebraic geometry provides the computational tools

### Lesson 77: Propositional and Predicate Logic
- **Propositional logic:** connectives (∧, ∨, ¬, →, ↔), truth tables
- Tautologies, contradictions, satisfiability
- Normal forms (CNF, DNF)
- **Predicate logic:** quantifiers (∀, ∃), predicates, terms
- **Formal proofs:** natural deduction, sequent calculus
- **Soundness** (provable → true) and **completeness** (true → provable)
- **Models and interpretations** (semantic side)
- **Formal verification** of software/AI systems

### Lesson 78: Gödel's Incompleteness and Löb's Theorem
- **Gödel's First Incompleteness Theorem:** any consistent formal system strong enough to express arithmetic contains true but unprovable statements
- **Gödel numbering:** encoding statements as numbers (self-reference)
- **Gödel's Second Incompleteness Theorem:** such a system cannot prove its own consistency
- **Löb's Theorem:** if PA proves "if PA proves P then P," then PA proves P
  - Prevents naive self-trust in formal systems
- **Diagonal lemma:** construction of self-referential sentences
- **Modal logic and provability logic (GL)**
- **Implications for alignment:** self-referential agents, trust between AI systems, limitations on self-verification

---

## Phase 6: Alignment Theory (Lessons 80–84)

### Lesson 80: Game Theory
- **Normal form games, extensive form games**
- **Nash equilibrium:** no player can unilaterally improve
- **Dominant strategies, mixed strategies**
- **Key games:** Prisoner's Dilemma, Stag Hunt, Chicken, Battle of the Sexes
- **Iterated games and folk theorems**
- **Mechanism design:** designing incentive-compatible systems (reverse game theory)
- **Common knowledge, signaling, information asymmetry**
- **Auction theory** (Vickrey, etc.)

### Lesson 81: Decision Theory
- **Expected utility theory:** maximize E[u(outcome)]
- **Von Neumann-Morgenstern axioms**
- **Three decision theories:**
  - **CDT (Causal Decision Theory):** evaluate actions by causal consequences
  - **EDT (Evidential Decision Theory):** evaluate actions by what they're evidence for
  - **FDT (Functional Decision Theory):** evaluate the policy/algorithm itself
- **Key thought experiments:** Newcomb's Problem, Smoking Lesion, Prisoner's Dilemma
- **Updateless Decision Theory (UDT)**
- **Logical uncertainty**
- Implications for AI agent design

### Lesson 82: Anthropics and Self-Locating Beliefs
- **Observation selection effects**
- **Sleeping Beauty Problem**
- **Self-Sampling Assumption (SSA)** vs **Self-Indication Assumption (SIA)**
- **Simulation arguments** (Bostrom)
- **Anthropics and AI doom probability estimates**
- **Doomsday argument**
- **Embedded agency:** agents reasoning about themselves as part of the environment

### Lesson 83: The Alignment Problem
- **Core problem:** ensuring AI systems pursue goals beneficial to humanity
- **Outer alignment:** specifying the right objective
- **Inner alignment:** ensuring the model optimizes for the specified objective
- **Mesa-optimization:** learned optimizers within the model (mesa-objectives vs base objectives)
- **Deceptive alignment:** model appears aligned during training but isn't
- **Current alignment techniques:**
  - RLHF, Constitutional AI, debate, recursive reward modeling
  - Scalable oversight, interpretability-based safety
- **Goodhart's Law:** when a measure becomes a target, it ceases to be a good measure

### Lesson 84: Open Problems and Research Frontiers
- **Technical open problems:** scalable oversight, interpretability gaps, robustness
- **Emerging theoretical frameworks:** SLT for understanding learning, agent foundations
- **Research frontiers in interpretability:** sparse autoencoders at scale, developmental interpretability, causal scrubbing
- **The Alignment Observatory** (capstone project)
- **The Alignment Researcher's Gauntlet** (capstone project)

---

## Phase 7: Research (Research Guide)

### Research Guide
- Recommended research path (from Neel Nanda's guide)
- **Key tools:** TransformerLens, PyTorch, einops
- **Research communities:** Alignment Forum, LessWrong, MATS, EleutherAI

---

## Resources (Not Lessons)

### Cheat Sheet
- Quick reference for formulas, identities, key results

### Intuition Notebook
- Personal insights and geometric intuitions accumulated during learning

### Practice Problems
- Additional exercises across all phases

### Video Index, Blog Index, Paper Index, Book Rankings, Course Listings
- Curated references organized by topic

---

## Assessments

- **Exam 1:** Linear Algebra (Phase 1)
- **Exam 2a:** Calculus & Optimization
- **Exam 2b:** Differential Equations
- **Exam 3a:** Probability (Frequentist)
- **Exam 3b:** Bayesian & Applied
- **Exam 4a:** Neural Network Foundations
- **Exam 4b:** Mechanistic Interpretability
- **Exam 5a:** Computability & Algebra
- **Exam 5b:** Topology & Logic
- **Exam 6a:** Rational Agency
- **Exam 6b:** Alignment Capstone
- **Final Project:** The Alignment Observatory (build transformers from scratch)
- **Capstone:** Comprehensive cross-phase project

---

## Quick-Search Index of Key Techniques

| Technique | Lesson(s) |
|-----------|-----------|
| Activation patching | 47 |
| Adam optimizer | 17, 23, 24 |
| Adjoint method | 26 |
| Algebraic varieties | 60 |
| Antiderivatives / indefinite integrals | 13 |
| Attention (dot-product) | 10, 43 |
| Backpropagation | 16, 42 |
| Bayes factors | 37 |
| Bayes' theorem | 28, 35 |
| BFS/DFS | CS-06 |
| Bias-variance tradeoff | 19 |
| Bifurcations | 25 |
| Binary search | CS-07 |
| Binomial theorem | CS-09 |
| Blow-ups (resolution of singularities) | 60 |
| Boolean/propositional logic | CS-09, 61 |
| Broadcasting (NumPy) | 00 |
| Causal inference (DAGs) | 38 |
| Chain rule | 13, 16 |
| Change of basis | 11 |
| Change of variables (integrals) | 20 |
| Cholesky decomposition | 11 |
| Combinatorics (P, C, stars & bars) | CS-09 |
| Computation graphs | 16 |
| Condition number | 14, 23, 24 |
| Confidence intervals | 32 |
| Conjugate priors | 35 |
| Constitutional AI | 46 |
| Contour plots / gradient fields | 15 |
| Convex optimization | 18 |
| Cosine similarity | 10 |
| Cross-entropy loss | 30, 31 |
| Cross-validation (k-fold) | 19 |
| DAGs (causal) | 38 |
| Decision theory (CDT/EDT/FDT) | 64 |
| Determinants | 7, 20 |
| Diagonalization | 8 |
| Diffusion models | 27 |
| Directional derivatives | 15 |
| Double descent | 19 |
| Double sum reindexing (by larger index) | CS-09 |
| DPO (Direct Preference Optimization) | 46 |
| Duality (optimization) | 18 |
| Dynamic programming | CS-08 |
| Effect sizes (Cohen's d) | 32 |
| Eigenvalues / eigenvectors | 8 |
| Einops / einsum | 01 |
| ELBO (Evidence Lower Bound) | 36 |
| EM algorithm | 30 |
| Emergent capabilities | 49 |
| Entropy | 31 |
| Epsilon-delta definition | 13, 57 |
| Equivariant networks | 56 |
| Euler's method | 22, 24 |
| Expected utility | 64 |
| Extreme Value Theorem | 13 |
| Falling factorial / Pochhammer symbol | CS-09 |
| False Discovery Rate (FDR) | 32 |
| Fixed points (ODE) | 22 |
| Fokker-Planck equation | 27 |
| Forward/backward pass | 16, 41, 42 |
| Fourier series | 27 |
| Free energy | 37, 50 |
| Frobenius norm | 11 |
| Fundamental group π₁ | 58 |
| Fundamental Theorem of Calculus | 13 |
| Game theory (Nash equilibrium) | 63 |
| Gaussian elimination | 6 |
| Gaussian integral | 20 |
| Gaussian Mixture Models | 30 |
| Gödel's incompleteness | 62 |
| Gradient descent | 17 |
| Gradient flow (ODE) | 24 |
| Gram-Schmidt process | 10 |
| Grokking | 19, 25, 49 |
| Group actions | 56 |
| Group theory | 54 |
| GWAS | 39 |
| Halting problem | 51 |
| Hamiltonian Monte Carlo | 36 |
| Hartman-Grobman theorem | 23 |
| Hash maps / hash tables | CS-04 |
| Heat equation | 27 |
| Heritability | 39 |
| Hessian matrix | 14, 21, 23 |
| Hockey stick identity | CS-09 |
| Homotopy | 58 |
| Hooks (PyTorch) | 01, 47 |
| Hypothesis testing | 32 |
| Implicit function theorem | 21 |
| Importance sampling | 20 |
| Improper integrals | 13, 20 |
| Inclusion-exclusion | CS-09 |
| Induction heads | 48 |
| Information bottleneck | 31 |
| Inner product of functions | 11 |
| Instrumental variables | 38 |
| Integration by parts | 13 |
| Intermediate Value Theorem | 13 |
| Jacobian matrix | 14, 20 |
| KKT conditions | 18 |
| KL divergence | 31 |
| Kolmogorov complexity | 53 |
| L'Hôpital's rule | 13 |
| Lagrange multipliers | 18 |
| Laplace approximation | 36 |
| Least squares (as projection) | 10 |
| Linked lists | CS-05 |
| LLC (Local Learning Coefficient) | 25, 50 |
| Löb's theorem | 62 |
| Logistic regression | 34 |
| LoRA | 9 |
| Loss landscapes | 19 |
| Low-rank approximation | 9 |
| Lyapunov functions / stability | 24, 25 |
| Manifolds | 59 |
| MAP estimation | 35 |
| Matrix calculus | 14 |
| Matrix exponential | 23 |
| Maximum Likelihood Estimation | 30 |
| MCMC (Metropolis-Hastings, Gibbs) | 36 |
| Mean Value Theorem | 13 |
| Mechanism design | 63 |
| Mendelian randomization | 38 |
| Mesa-optimization | 66 |
| MLP / neural network layers | 40, 41 |
| Modular arithmetic | CS-09 |
| Momentum (optimization) | 17, 24 |
| Monte Carlo integration | 20 |
| Multi-head attention | 43 |
| Mutual information | 31 |
| Nash equilibrium | 63 |
| Neural ODEs | 26 |
| Newcomb's problem | 64 |
| Norm balls (L1 diamond, L2 circle, L∞ square) | 11 |
| Norms (L1, L2, L∞, Frobenius, spectral) | 11 |
| Normalizing flows | 20, 26 |
| NP-completeness | 52 |
| Null space / kernel | 6 |
| Occam's razor (Bayesian) | 37 |
| ODE: linear systems / phase portraits | 23 |
| Orbit-stabilizer theorem | 56 |
| Orthogonal matrices | 10 |
| Orthogonality / orthonormal basis | 10 |
| OV / QK circuits | 5, 44 |
| P-values | 32 |
| P vs NP | 52 |
| PCA (via SVD / eigendecomposition) | 8, 9 |
| Phase portraits | 23 |
| Phase transitions | 25, 49, 50 |
| Pigeonhole principle | CS-09 |
| PMI (pointwise mutual information) | 31 |
| Policy gradient / PPO | 45 |
| Polygenic scores | 39 |
| Positive definite / PSD matrices | 11 |
| Potential outcomes framework | 38 |
| Power (statistical) | 32 |
| PPO (Proximal Policy Optimization) | 45 |
| Prefix sum | CS-04 |
| Probing (linear probes) | 47 |
| Product rule | 13 |
| Projection matrix (P = A(AᵀA)⁻¹Aᵀ) | 10 |
| Proof by induction | CS-09 |
| Quotient groups | 54 |
| R² (coefficient of determination) | 34 |
| Rank | 6 |
| Rank-nullity theorem | 6 |
| ReLU (and geometric folding) | 41 |
| Reparameterization trick | 20, 36 |
| Representations (group) | 56 |
| Residual stream | 44 |
| Riemann sums | 13 |
| RLCT (Real Log Canonical Threshold) | 37, 50, 60 |
| RLHF pipeline | 45, 46 |
| Rings and fields | 55 |
| Scaling laws (Kaplan, Chinchilla) | 49 |
| Score function / score matching | 27 |
| SDEs (stochastic differential equations) | 26 |
| SGD (stochastic gradient descent) | 17 |
| Sigmoid / logistic function | 34 |
| Simpson's paradox | 33 |
| Simulation arguments | 65 |
| Singular Learning Theory (SLT) | 37, 50, 60 |
| Singular values / SVD | 9 |
| Sleeping Beauty problem | 65 |
| Sliding window pattern | CS-04 |
| Softmax | 13, 43 |
| Solomonoff induction / AIXI | 53 |
| Sparse autoencoders (SAEs) | 48 |
| Spectral norm | 11 |
| Stacks and queues | CS-05 |
| Steering vectors | 47 |
| Stochastic gradient descent | 17 |
| Superposition hypothesis | 3, 48 |
| Survivorship bias | 33 |
| SVMs (via dual) | 18 |
| Symmetric matrices | 11 |
| Taylor expansions | 14, 21 |
| Temperature (softmax) | 31 |
| Topological spaces | 57 |
| Topological sort | CS-06 |
| Trace | 11 |
| Transformer architecture | 44 |
| TransformerLens | 01, 47, 48 |
| Tree traversals (in/pre/post order) | CS-06 |
| Turing machines | 51 |
| Two-pointer pattern | CS-04 |
| u-substitution (reverse chain rule) | 13 |
| Universal approximation | 41 |
| VAE (Variational Autoencoder) | 36 |
| Vanishing/exploding gradients | 7, 42 |
| Variational inference | 36 |
| Vector fields | 22 |
| Vectors (geometric + computational) | 2 |
| WAIC | 37 |
| Weight decay (= L2 reg = Gaussian prior) | 11, 18, 35 |

---

*Last updated: March 2026*
*Total lessons: 68+ across 8 phases (including CS foundations)*
