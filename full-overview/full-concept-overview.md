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

## Phase 0: Setup (Lessons 00–01)

### Lesson 00: Python & NumPy
- NumPy array creation: `np.array`, `np.eye`, `np.zeros`, `np.random.randn`
- Linear algebra operations: `@` (matmul), `np.linalg.inv`, `np.linalg.det`, `np.linalg.eig`, `np.linalg.svd`, `np.linalg.norm`, `.T`
- **Broadcasting** rules
- Matplotlib: `plt.plot`, `plt.scatter`, `plt.quiver` (vectors), `plt.contour`, `plt.imshow` (heatmaps)
- Jupyter notebooks and Google Colab

### Lesson 01: PyTorch
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

## Phase 1: Linear Algebra (Lessons 02–12)

### Lesson 02: Vectors
- Vectors as arrows (geometric) AND lists of numbers (computational)
- Vector addition (tip-to-tail), scalar multiplication
- Coordinates are basis-dependent instructions
- Embedding vectors in transformers (~768-dimensional)

### Lesson 03: Linear Combinations, Span, and Basis
- **Linear combination:** a₁v₁ + a₂v₂ + ... + aₙvₙ
- **Span:** all reachable vectors via linear combinations
- **Linear independence** vs dependence
- **Basis:** minimal spanning set, exactly n vectors for ℝⁿ
- **Superposition hypothesis:** networks encode more features than dimensions using non-orthogonal directions

### Lesson 04: Linear Transformations and Matrices
- **Matrices as transformations** of space (not just grids of numbers)
- Columns of a matrix = where basis vectors land
- "Linear" means: lines stay lines, origin stays fixed
- **Linear vs affine:** y = Wx (linear) vs y = Wx + b (affine, what neural network layers actually are)
- Matrix-vector multiplication = "where does this vector land?"
- **Matrix multiplication as composition:** AB means "apply B, then A"
- Non-commutativity: AB ≠ BA in general

### Lesson 05: Matrix Operations
- **Two views of matrix-vector multiplication:**
  - Row view: dot products (pattern matching)
  - Column view: linear combination of columns
- Matrix-matrix multiplication = composition of transformations
- Transpose: (AB)ᵀ = BᵀAᵀ (reverse order rule)
- Associativity: (AB)C = A(BC)
- **QK and OV circuits** in transformers as matrix compositions

### Lesson 06: Rank, Null Space, and Column Space
- **Column space:** all possible outputs of Ax (span of columns)
- **Null space (kernel):** all x where Ax = 0 (vectors crushed to zero)
- **Rank:** dimension of column space = number of independent directions in output
- **Rank-nullity theorem:** rank + nullity = number of columns
- **Gaussian elimination / row reduction:** row echelon form, reduced row echelon form (RREF)
- Pivot columns, free variables, reading solutions from RREF
- Attention matrices are deliberately **low-rank** (e.g., 768 → 64 → 768)

### Lesson 07: The Determinant
- **Determinant = scaling factor for area/volume** under transformation
- det = 0 ↔ rank deficient ↔ non-invertible ↔ non-trivial null space
- det < 0 ↔ orientation flip
- det(AB) = det(A)·det(B)
- Computing 2×2 and 3×3 determinants
- Cofactor expansion
- Vanishing/exploding gradients and determinant magnitudes

### Lesson 08: Eigenvalues and Eigenvectors
- **Eigenvector:** direction unchanged by transformation (Av = λv)
- **Eigenvalue λ:** the scaling factor
- **Characteristic equation:** det(A − λI) = 0
- **Diagonalization:** A = PDP⁻¹ (change to eigenbasis → scale → change back)
- Powers: Aⁿ = PDⁿP⁻¹
- PCA finds eigenvectors of covariance matrix
- Hessian eigenvalues = loss landscape curvature

### Lesson 09: Singular Value Decomposition (SVD)
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

## Phase 2: Calculus (Lessons 13–27)

### Lesson 13: Calculus Fundamentals
**Derivatives:**
- **Derivative as rate of change** at an instant — slope of tangent line
- **Limit definition:** f'(x) = lim_{h→0} [f(x+h) − f(x)] / h
- Secant lines → tangent lines via limits
- "Zooming in" intuition: smooth curves look linear at sufficient magnification (local linearity)
- **Differentials** (dx, dy) as actual tiny quantities, not just notation
- **Differentiation rules:**
  - **Power rule:** d/dx xⁿ = nxⁿ⁻¹
  - **Constant multiple and sum rules** (derivative is a linear operator)
  - **Product rule:** (fg)' = f'g + fg' (rectangle area analogy)
  - **Quotient rule:** (f/g)' = (f'g − fg') / g²
  - **Chain rule:** d/dx f(g(x)) = f'(g(x))·g'(x) — THE most important rule for ML (backpropagation IS the chain rule)
- **Key functions and their derivatives:**
  - eˣ → eˣ (its own derivative; softmax, log-likelihood, exponential decay)
  - ln(x) → 1/x (cross-entropy loss, log-likelihood, information theory)
  - **Logarithmic derivative:** d/dx ln(f(x)) = f'(x)/f(x) (relative rate of change)
  - sin(x) → cos(x), cos(x) → −sin(x) (positional encodings, Fourier features)
  - **Sigmoid σ(x) = 1/(1+e⁻ˣ):** σ'(x) = σ(x)(1−σ(x)), max derivative = 0.25 → vanishing gradients
  - **tanh(x):** output in (−1,1), tanh'(x) = 1 − tanh²(x)
  - **ReLU(x) = max(0,x):** derivative is 0 or 1 (no gradient shrinkage), dead neuron problem
  - Leaky ReLU, GELU (variants)

**Integration:**
- **Definite integral** ∫ₐᵇ f(x) dx = signed area under curve
- **Riemann sums:** approximating area with rectangles (left, right, midpoint, trapezoidal)
- **Fundamental Theorem of Calculus:**
  - Part 1: d/dx ∫ₐˣ f(t) dt = f(x) (derivative of "area so far" = original function)
  - Part 2: ∫ₐᵇ f(x) dx = F(b) − F(a) where F' = f (evaluate antiderivative at endpoints)
- **Antiderivatives** (indefinite integrals): reverse the derivative table
  - xⁿ → xⁿ⁺¹/(n+1) + C, 1/x → ln|x| + C, eˣ → eˣ + C, sin → −cos + C, cos → sin + C
  - **Constant of integration** (+C) — vertical shifts don't change slope
- **Integration techniques:**
  - **u-substitution:** reverse chain rule, ∫f(g(x))g'(x)dx = ∫f(u)du
  - **Integration by parts:** ∫u dv = uv − ∫v du (reverse product rule)
  - Partial fractions (for rational functions)
  - Trigonometric substitutions and identities
- **Improper integrals:** ∫₀^∞ f(x) dx as limit of ∫₀ᴺ f(x)dx as N→∞ (convergence/divergence)
  - Essential for probability densities over unbounded domains (Gaussian, exponential)

**Limits, Continuity, and Foundational Theorems:**
- **Limits:** lim_{x→a} f(x) — formal ε-δ definition (conceptual understanding, not daily use)
- **Continuity:** f continuous at a ↔ lim_{x→a} f(x) = f(a)
- **L'Hôpital's rule:** lim f/g in 0/0 or ∞/∞ form → lim f'/g'
- **Squeeze theorem:** bound function between two converging functions
- **Intermediate Value Theorem (IVT):** continuous f on [a,b] hits every value between f(a) and f(b)
- **Mean Value Theorem (MVT):** there exists c in (a,b) where f'(c) = [f(b)−f(a)]/(b−a) (instantaneous rate = average rate somewhere)
- **Extreme Value Theorem:** continuous f on closed [a,b] attains its max and min

**Optimization (Critical Points):**
- **Critical points:** where f'(x) = 0 or undefined — candidates for max/min
- **Second derivative test:** f''(x₀) > 0 → local min (concave up), f''(x₀) < 0 → local max (concave down), f''(x₀) = 0 → inconclusive
- **Concavity:** f'' > 0 = concave up (bowl), f'' < 0 = concave down (hill)
- **Inflection points:** where concavity changes (f'' = 0 and changes sign)
- Training a neural network = iteratively approximating where ∇L = 0

**Sequences and Series (foundations for Taylor, Lesson 21):**
- **Sequences:** convergence, divergence, bounded, monotone
- **Series:** Σaₙ, partial sums, geometric series (a/(1−r) when |r|<1)
- **Convergence tests:** ratio test, comparison test, integral test (conceptual)
- **Power series:** Σ aₙxⁿ, radius of convergence
- Taylor/Maclaurin series covered in depth in Lesson 21

### Lesson 14: Matrix Calculus
- Partial derivatives: change when wiggling one input
- **Gradient vector:** ∇f collects all partial derivatives, points "uphill"
- **Jacobian matrix:** derivative of vector-to-vector function (a matrix)
- **Key matrix calculus results:**
  - ∂/∂x(Ax) = A
  - ∂/∂x(xᵀAx) = (A + Aᵀ)x
  - ∂/∂X tr(AX) = Aᵀ
- **Taylor series and linearization:** f(x+δ) ≈ f(x) + ∇f(x)ᵀδ (why gradient descent works)
- Learning rate controls how far to trust the linear approximation
- **Hessian matrix:** second-order partial derivatives, always symmetric
  - Eigenvalues = curvature in each direction
  - **Condition number** κ = λ_max/λ_min (elongated landscapes → zigzag SGD)

### Lesson 15: Partial Derivatives and Gradients
- Gradients perpendicular to contour lines
- Gradient = direction of steepest ascent
- **Directional derivatives:** rate of change in arbitrary direction
- **Multivariable chain rule:** the key identity for backpropagation
- Gradient field visualization (contour plots with arrows)

### Lesson 16: The Chain Rule and Backpropagation
- Single-variable and multivariable chain rule
- **Computation graphs:** neural networks as directed graphs of simple operations
- **Forward pass** (compute values) vs **backward pass** (compute gradients)
- **Reverse-mode autodiff** vs forward-mode: reverse is O(1) per output, forward is O(1) per input — reverse wins for neural nets (many inputs, one loss)
- Building a tiny backprop engine (micrograd-style)

### Lesson 17: Optimization and Gradient Descent
- **Gradient descent:** W ← W − η∇L(W)
- **SGD:** mini-batch gradient estimates instead of full dataset
- Learning rate: too big = overshoot, too small = slow
- **Momentum:** accumulate velocity, coast through flat regions
- **Adam optimizer:** adaptive per-parameter learning rates
- **Convexity vs non-convexity:** neural network loss is non-convex
- Building micrograd (Karpathy)

### Lesson 18: Constrained Optimization and Lagrange Multipliers
- **Lagrange multipliers:** at constrained optimum, ∇f ∥ ∇g (gradients parallel)
- **The Lagrangian:** L(x, λ) = f(x) − λg(x)
- λ measures the "cost" of the constraint
- **Multiple constraints and KKT conditions** (inequality constraints)
- **Complementary slackness:** inactive constraints get λ = 0
- **Convex optimization:** every local minimum is global
- **Regularization as soft constraint:** L2 penalty ↔ constrained ||w||² ≤ C, λ IS the Lagrange multiplier
- **Duality:** primal vs dual problems, weak and strong duality
- SVMs derived via the dual problem

### Lesson 19: Loss Landscapes and Local Minima
- Loss as function of all parameters in high-dimensional space
- Local minima, saddle points, plateaus
- **In high dimensions:** saddle points dominate (not local minima)
- **Bias-variance tradeoff:** error = bias² + variance + noise
- **Double descent:** error curve goes down, up, then down again for overparameterized models
- **Grokking:** sudden generalization after apparent overfitting
- **Cross-validation:** k-fold for estimating generalization
- **Model selection:** AIC, BIC
- Hessian analysis: positive eigenvalues = minimum, mixed = saddle
- Condition number determines gradient descent zigzagging

### Lesson 20: Multiple Integration and Change of Variables
- **Double/triple integrals:** volume under surface, iterated integration
- **Fubini's theorem:** can switch integration order
- **Change of variables formula:** Jacobian determinant measures local stretching
- Polar coordinates (Jacobian = r)
- **The Gaussian integral:** ∫e^(-x²)dx = √π (proved via polar coordinates)
- **Multivariate Gaussian** normalization involves det(Σ)
- **Monte Carlo integration:** approximate ∫f(x)p(x)dx by sampling
- **Importance sampling:** sample from proposal q, reweight by p/q
- Normalizing flows = chain of change-of-variables transformations
- **Reparameterization trick** in VAEs

### Lesson 21: Taylor Expansions and the Implicit Function Theorem
- **Taylor expansion:** f(x) ≈ f(a) + f'(a)(x−a) + ½f''(a)(x−a)² + ...
- Zeroth order (constant), first order (gradient descent), second order (Newton's method)
- **Multivariate Taylor:** f(w) ≈ f(w₀) + ∇f(w₀)ᵀ(w−w₀) + ½(w−w₀)ᵀH(w−w₀)
- At critical points: local landscape IS the quadratic form of the Hessian
- **Implicit function theorem:** when F(x,y)=0 can be solved for y=g(x), and g'(x) = −(∂F/∂x)/(∂F/∂y)
- Fails at singularities → bifurcation points (key for SLT)
- **Big-O notation:** f(x) = O(g(x)) — asymptotic bounds for truncation errors
- Scaling laws expressed in asymptotic notation

### Lesson 22: Introduction to ODEs
- **ODE:** dx/dt = f(x,t) — rates of change as vector fields
- **Vector field visualization:** arrows at every point showing direction/speed of flow
- **Gradient descent as Euler's method on an ODE:** dW/dt = −∇L(W)
- Step size h = learning rate η
- **Solution curves / trajectories:** paths following the vector field
- **Existence and uniqueness theorem** (Lipschitz continuity)
- **Fixed points:** where f(x*) = 0 (critical points of loss for gradient flow)
- **1D stability:** f'(x*) < 0 → stable, f'(x*) > 0 → unstable

### Lesson 23: Linear Systems and Phase Portraits
- **Linear systems:** dx/dt = Ax — behavior determined entirely by eigenvalues of A
- **Solution:** x(t) = e^{At}x(0) = c₁e^{λ₁t}v₁ + c₂e^{λ₂t}v₂
- **Matrix exponential**
- **Phase portrait classification by eigenvalues:**
  - Both negative real → **stable node** (convergence)
  - Both positive real → **unstable node**
  - Opposite signs → **saddle point**
  - Complex with α < 0 → **stable spiral**
  - Complex with α > 0 → **unstable spiral**
  - Complex with α = 0 → **center** (closed orbits)
- **Condition number revisited dynamically:** mismatched eigenvalues → zigzagging convergence
- Adam/preconditioning equalize eigenvalues
- **Jacobian linearization:** behavior near fixed point ≈ behavior of dx/dt = Jx
- **Hartman-Grobman theorem:** nonlinear ≈ linear near hyperbolic fixed points
- **Basins of attraction, separatrices**

### Lesson 24: Gradient Flow and Training Dynamics
- **Gradient flow equation:** dW/dt = −∇L(W)
- **Loss as Lyapunov function:** dL/dt = −‖∇L‖² ≤ 0 (loss always decreases along flow)
- **Euler stability criterion:** η < 2/λ_max (fundamental learning rate bound)
- **Momentum as second-order ODE:** damped ball rolling on loss surface
- Momentum helps with ill-conditioning (cancels zigzag)
- **Implicit regularization:** gradient descent from small init → minimum-norm solution
- For deep linear networks → low-rank solutions
- **Learning rate as temperature:** larger η → more noise → escapes sharp minima
- **SGD noise:** σ² ∝ η/B (learning rate / batch size)
- Batch size and generalization tradeoff

### Lesson 25: Stability, Lyapunov Functions, and Phase Transitions
- **Lyapunov stability:** find V(x) > 0 with dV/dt ≤ 0 → fixed point is stable
- **Lyapunov functions for AI safety:** dream of proving alignment stability
- **Bifurcations:** qualitative behavior changes as parameter varies
  - **Saddle-node bifurcation:** two fixed points collide and annihilate
  - **Pitchfork bifurcation:** symmetry breaking, one → three fixed points
- **Phase transitions in training:** sudden qualitative changes (loss drops, capabilities emerge)
- **Grokking** as saddle escape from memorization to generalization
- **Emergent capabilities** as phase transitions in model size
- **SLT phase transitions:** RLCT jumps correspond to capability acquisition
- **Local Learning Coefficient (LLC):** tracks RLCT during training
- **Attractors:** fixed points, limit cycles, strange attractors/chaos
- Gradient systems can't have limit cycles (Strogatz), but SGD can oscillate

### Lesson 26: Neural ODEs and Stochastic Dynamics
- **ResNets as Euler steps:** x_{l+1} = x_l + f_θ(x_l) ≈ ODE
- **Neural ODE framework:** dx/dt = f_θ(x), solved with adaptive ODE solvers
- **Adjoint method:** O(1) memory backprop through ODE solver
- Advantages: constant memory, adaptive computation
- Limitations: sequential solving, homeomorphism constraint
- **Continuous normalizing flows:** d(log p)/dt = −tr(∂f/∂x) (Hutchinson trace estimator)
- **Stochastic Differential Equations (SDEs):** dW = −∇L dt + σ dB_t
- **SGD as noisy gradient flow**
- **Fokker-Planck perspective:** P(W) ∝ exp(−L(W)/T) at steady state
- Large learning rate → preference for flat minima (sharp minima destabilized)
- **Edge of stability:** training at η ≈ 2/λ_max (inherently discrete effect)
- Simulated annealing connection (LR schedule = cooling)

### Lesson 27: Partial Differential Equations
- **Heat equation:** u_t = k∇²u (diffusion = Gaussian blurring)
- Solution via convolution with Gaussian kernel
- **Forward process of diffusion models** = progressive noise addition
- **Fokker-Planck equation:** ∂p/∂t = −∂(fp)/∂x + (σ²/2)∂²p/∂x²
- Describes probability distribution over weight space during SGD
- **Score function:** ∇_x log p(x) — gradient of log-probability
- **Score matching:** learn score without normalization constant
- **Reverse SDE for diffusion models:** requires learned score function
- **Probability flow ODE** (deterministic version of reverse SDE)
- **Separation of variables, Fourier series** for solving linear PDEs
- High-frequency modes decay fastest → diffusion models generate coarse-to-fine

---

## Phase 3: Probability & Statistics (Lessons 28–39)

### Lesson 28: Probability Distributions and Bayes' Theorem
- Probability axioms, conditional probability, independence
- **Bayes' theorem:** P(A|B) = P(B|A)P(A)/P(B)
- Common distributions: Bernoulli, binomial, Gaussian/normal, Poisson, uniform, exponential
- **Central Limit Theorem:** averages of random variables → Gaussian
- **Change of variables for probability:** p(y) = p(f⁻¹(y))·|det(J_f⁻¹)| (Jacobian factor)
- Joint, marginal, conditional distributions
- **Law of total probability**

### Lesson 29: Expectation, Variance, and Covariance
- **Expected value:** E[X] = Σ xP(x) (weighted average)
- **Variance:** Var(X) = E[(X−μ)²] = E[X²] − (E[X])²
- **Standard deviation:** σ = √Var
- **Covariance:** Cov(X,Y) = E[(X−μ_X)(Y−μ_Y)]
- **Correlation:** ρ = Cov(X,Y)/(σ_X σ_Y), normalized to [−1, 1]
- **Covariance matrix:** symmetric, PSD
- Linearity of expectation
- Law of large numbers, moment generating functions

### Lesson 30: Maximum Likelihood Estimation
- **Likelihood:** L(θ) = P(data | θ) — probability of data given parameters
- **MLE:** θ̂ = argmax P(data | θ), equivalently minimize −log likelihood
- **Cross-entropy loss = negative log-likelihood** for classification
- **Properties of MLE:** consistent, asymptotically normal, asymptotically efficient
- **EM Algorithm (Expectation-Maximization):**
  - E-step: compute expected assignments given current parameters
  - M-step: update parameters given expected assignments
- **Gaussian Mixture Models (GMMs):** EM for fitting multiple Gaussians
- **K-means as hard EM** (hard vs soft assignments)

### Lesson 31: Information Theory
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

### Lesson 32: Hypothesis Testing
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

### Lesson 33: Experimental Design and Statistical Fallacies
- **Randomization, control groups, blinding** (single, double), **pre-registration**
- **Hierarchy of evidence:** case reports → observational → RCTs → meta-analyses
- **Correlation ≠ causation** (confounders)
- **Simpson's paradox:** trend reverses when groups combined
- **Survivorship bias**
- **Base rate neglect / prosecutor's fallacy**
- **Ecological fallacy:** group-level ≠ individual-level relationships
- **Regression to the mean**

### Lesson 34: Regression
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

### Lesson 35: Bayesian Foundations
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

### Lesson 36: Bayesian Computation
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

### Lesson 37: Bayesian Model Comparison
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

### Lesson 38: Causal Inference
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

### Lesson 39: Applied Statistics
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

---

## Phase 4: Machine Learning (Lessons 40–50)

### Lesson 40: Single Neuron
- Perceptron model: weighted sum + bias + activation
- Linear decision boundary (hyperplane)
- Step function, sigmoid, ReLU activations
- Perceptron learning rule
- **XOR problem:** single neurons can't solve non-linear problems

### Lesson 41: Forward Pass
- **Multi-layer networks:** stacking linear transformations + nonlinearities
- Forward pass = sequence of matrix multiplications + activations
- **ReLU folds space** — geometric view of piecewise-linear decision boundaries
- Universal approximation theorem
- Width vs depth tradeoffs

### Lesson 42: Backpropagation
- Full network gradient computation via chain rule
- **Backprop = reverse-mode autodiff on computation graph**
- Gradient flow through layers
- Vanishing/exploding gradients
- **Residual connections** help gradient flow
- Batch normalization, layer normalization
- Gradient checking (numerical vs analytical)

### Lesson 43: Attention Mechanism
- **Query, Key, Value** vectors: Q = xW_Q, K = xW_K, V = xW_V
- **Attention scores:** QKᵀ/√d_k (scaled dot-product attention)
- **Softmax** → attention weights (probability distribution over positions)
- Weighted sum of values
- **Multi-head attention:** multiple attention patterns in parallel
- **Causal/autoregressive masking:** prevent attending to future tokens
- Multi-head Latent Attention (MLA, DeepSeek variant)

### Lesson 44: Transformer Architecture
- **Full transformer block:** LayerNorm → Multi-Head Attention → Residual → LayerNorm → MLP → Residual
- **Residual stream** view: attention heads and MLPs read/write to shared stream
- **Positional encoding:** sinusoidal or learned
- **QK circuit** (W_Qᵀ W_K): determines what a head attends to
- **OV circuit** (W_O W_V): determines what information moves
- **"Mathematical Framework for Transformer Circuits"** (Elhage, Nanda et al.)
- Building a transformer from scratch

### Lesson 45: Reinforcement Learning Foundations
- **Agent, Environment, State, Action, Reward** framework
- **Markov Decision Process (MDP):** states, actions, transition probabilities, rewards
- **Policy π(a|s):** strategy mapping states to action probabilities
- **Value function V(s)** and **Q-function Q(s,a)**
- **Discount factor γ:** future reward weighting
- **Policy gradient methods:** ∇J(θ) = E[∇log π(a|s)·Q(s,a)]
- **PPO (Proximal Policy Optimization):** clipped updates, trust region
- **Value-based methods:** Q-learning, DQN
- **Reward shaping, specification gaming, Goodhart's Law**
- **Sparse vs dense rewards, credit assignment problem**
- **Reward hacking:** the alignment problem in miniature
- **RLHF pipeline:** SFT → reward model from comparisons → PPO fine-tuning

### Lesson 46: LLM Training Pipeline
- **Stage 1: Pre-training** — next-token prediction on internet text (MLE)
- Scaling laws: loss ∝ N^(-α)
- **Stage 2: SFT** — supervised fine-tuning on (instruction, response) demonstrations
- Format learning, not judgment
- **Stage 3: RLHF / DPO / Constitutional AI** — preference optimization
- Reward model, PPO, KL penalty from base model
- **DPO:** direct preference optimization (skip reward model)
- **Constitutional AI:** principle-based self-critique (Anthropic's approach)
- **Stage 4: Deployment and monitoring**

### Lesson 47: Interpretability Introduction
- **Mechanistic interpretability:** understanding model internals at circuit level
- **Activation patching:** swap activations to measure causal importance
- **Direct logit attribution:** which components contribute to final token prediction
- **Probing:** train linear classifiers on intermediate representations
- **Steering vectors:** add directions to residual stream to modify behavior

### Lesson 48: Circuits and Features
- **Induction heads:** attention pattern that copies previous occurrences
- **Feature circuits:** networks of components that implement specific computations
- **Sparse autoencoders (SAEs):** decompose activations into interpretable features
- **Superposition:** models represent more features than dimensions
- **Monosemantic vs polysemantic neurons**
- **Scaling monosemanticity** (Anthropic)

### Lesson 49: Scaling Laws and Emergent Capabilities
- **Kaplan scaling laws:** L(N) ∝ N^(-α) — loss as power law in model size
- **Chinchilla scaling:** optimal data/params ratio ~20:1
- **The bitter lesson** (Rich Sutton): scale wins over cleverness
- **Emergent capabilities:** abrupt appearance at certain scales
  - In-context learning, chain-of-thought, theory of mind
- **Measurement artifact debate** (Schaeffer et al.): smooth in log-space, sharp in accuracy
- **Practical danger threshold** may still be sharp
- **Grokking as phase transition** in time (not scale)
- **Developmental interpretability:** tracking internal changes at capability transitions

### Lesson 50: Singular Learning Theory (SLT)
- **Standard statistics fails for neural networks:** many-to-one parameter-to-function map
- **Symmetries create singularities:** neuron permutation, weight rescaling, zero neurons
- Fisher information matrix is singular at singularities
- **Free energy:** F = −log ∫ P(D|θ)P(θ)dθ
  - Regular models: F ≈ (d/2)log n (= BIC)
  - **Singular models: F ≈ λ·log n − (m−1)·log log n**
- **RLCT (Real Log Canonical Threshold) λ:** true effective dimension, λ ≤ d/2
- Measured via singularity geometry (blow-ups from algebraic geometry)
- **Why overparameterized networks generalize:** real complexity (RLCT) << parameter count
- **Phase transitions:** model moves between basins with different RLCTs
- **Local Learning Coefficient (LLC):** estimable RLCT, tracks phase transitions during training
- Connection to: eigenvalues (flat Hessian directions), rank (degenerate Fisher information), algebraic geometry (resolution of singularities)

---

## Phase 5: Mathematical Enrichment (Lessons 51–62)

### Lesson 51: Turing Machines and Decidability
- **Turing machine:** tape + head + states + transition function — formal definition of computation
- Church-Turing thesis: anything computable is Turing-computable
- **Halting problem:** no algorithm can determine if arbitrary programs halt — **undecidable**
- Proof by contradiction using diagonalization
- **Rice's theorem:** every non-trivial semantic property of programs is undecidable
- Decidability landscape: decidable, semi-decidable, undecidable

### Lesson 52: Computational Complexity
- **P:** problems solvable in polynomial time
- **NP:** solutions verifiable in polynomial time
- **NP-complete:** hardest problems in NP (via polynomial reductions)
- **P vs NP** — open problem
- Cook-Levin theorem (SAT is NP-complete)
- NP-hardness in ML: training neural networks, feature selection
- **Space complexity:** PSPACE
- **Circuit complexity:** neural networks as Boolean circuits

### Lesson 53: Kolmogorov Complexity and Algorithmic Information
- **Kolmogorov complexity K(x):** length of shortest program generating x
- Incompressible strings (random)
- K(x) is **uncomputable** (related to halting problem)
- Connection to Shannon entropy: E[K(x)] ≈ H(X)
- **Solomonoff induction:** universal prior P(x) = 2^{-K(x)}, optimal prediction
- **AIXI:** Solomonoff induction + expected utility maximization = theoretically optimal agent
- Incomputable but provides theoretical ideal for agent design
- Minimum Description Length (MDL) principle

### Lesson 54: Group Theory
- **Group:** set + operation satisfying closure, associativity, identity, inverses
- Examples: integers under addition, permutation groups S_n, cyclic groups Z_n, matrix groups GL(n), SO(n), dihedral groups
- **Subgroups, cosets, quotient groups** G/N
- **Lagrange's theorem:** |H| divides |G|
- **Homomorphisms and isomorphisms**
- **First isomorphism theorem**
- Abelian vs non-abelian groups
- **Normal subgroups**

### Lesson 55: Rings, Fields, and Algebraic Structures
- **Rings:** set with + and ×, additive group + multiplicative monoid
- Examples: integers Z, polynomials R[x], matrix rings
- **Fields:** rings where every nonzero element has multiplicative inverse (Q, R, C, F_p)
- **Ideals and quotient rings**
- **Modules and vector spaces** (vector space = module over a field)
- **Noetherian rings, Hilbert Basis Theorem**
- **Polynomial rings** — foundation for algebraic geometry

### Lesson 56: Group Actions, Representations, and Neural Network Symmetry
- **Group actions:** group acts on a set (orbits, stabilizers)
- **Neural network symmetries:** neuron permutation symmetry in hidden layers
- **Orbit-stabilizer theorem** and connection to SLT (parameter symmetries create singularities)
- **Group representations:** encoding symmetries as matrices
- Character theory basics
- **Equivariant neural networks:** architectures preserving symmetries (CNNs = translation equivariance)

### Lesson 57: Point-Set Topology
- **Topological spaces:** defined by open sets satisfying axioms
- **Continuity:** topological definition (preimage of open is open)
- **Compactness:** every open cover has finite subcover
  - Heine-Borel: closed + bounded ⊂ ℝⁿ ↔ compact
  - Extreme value theorem requires compactness
- **Connectedness:** cannot be split into two disjoint open sets
- **Path-connectedness** (stronger than connectedness)
- **Hausdorff spaces:** points can be separated by open sets
- Homeomorphisms (topological equivalence)

### Lesson 58: Homotopy and Fundamental Groups
- **Homotopy:** continuous deformation of one map into another
- Homotopy equivalence of spaces
- **Fundamental group π₁:** loops up to continuous deformation
  - π₁(circle) = Z, π₁(sphere) = 0, π₁(torus) = Z×Z
- **Higher homotopy groups πₙ**
- **Covering spaces:** unwinding topology
- Loss landscape topology: holes and non-contractible loops

### Lesson 59: Manifolds and Tangent Spaces
- **Smooth manifolds:** locally Euclidean spaces with smooth transition maps
- Examples: spheres, tori, weight space as manifold
- **Tangent spaces and tangent bundles**
- **Riemannian metrics:** inner product on tangent spaces (measuring on curved spaces)
- **Manifold hypothesis:** real-world data lies on low-dimensional manifold in high-dimensional space
- **Singularities:** where manifold structure breaks down (key for SLT)

### Lesson 60: Algebraic Geometry Essentials
- **Algebraic varieties:** solution sets of polynomial equations
- Affine varieties, projective varieties
- **Smooth vs singular points:** Jacobian rank condition
- **Blow-ups:** resolution of singularities
  - Replace a point with the space of directions through it
- **The RLCT (Real Log Canonical Threshold):** computed via resolution of singularities
  - Blow up the singularity → compute how the volume form transforms → extract λ
- **Computing RLCTs for examples:** linear regression, reduced rank regression, neural networks
- Direct connection to SLT: algebraic geometry provides the computational tools

### Lesson 61: Propositional and Predicate Logic
- **Propositional logic:** connectives (∧, ∨, ¬, →, ↔), truth tables
- Tautologies, contradictions, satisfiability
- Normal forms (CNF, DNF)
- **Predicate logic:** quantifiers (∀, ∃), predicates, terms
- **Formal proofs:** natural deduction, sequent calculus
- **Soundness** (provable → true) and **completeness** (true → provable)
- **Models and interpretations** (semantic side)
- **Formal verification** of software/AI systems

### Lesson 62: Gödel's Incompleteness and Löb's Theorem
- **Gödel's First Incompleteness Theorem:** any consistent formal system strong enough to express arithmetic contains true but unprovable statements
- **Gödel numbering:** encoding statements as numbers (self-reference)
- **Gödel's Second Incompleteness Theorem:** such a system cannot prove its own consistency
- **Löb's Theorem:** if PA proves "if PA proves P then P," then PA proves P
  - Prevents naive self-trust in formal systems
- **Diagonal lemma:** construction of self-referential sentences
- **Modal logic and provability logic (GL)**
- **Implications for alignment:** self-referential agents, trust between AI systems, limitations on self-verification

---

## Phase 6: Alignment Theory (Lessons 63–67)

### Lesson 63: Game Theory
- **Normal form games, extensive form games**
- **Nash equilibrium:** no player can unilaterally improve
- **Dominant strategies, mixed strategies**
- **Key games:** Prisoner's Dilemma, Stag Hunt, Chicken, Battle of the Sexes
- **Iterated games and folk theorems**
- **Mechanism design:** designing incentive-compatible systems (reverse game theory)
- **Common knowledge, signaling, information asymmetry**
- **Auction theory** (Vickrey, etc.)

### Lesson 64: Decision Theory
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

### Lesson 65: Anthropics and Self-Locating Beliefs
- **Observation selection effects**
- **Sleeping Beauty Problem**
- **Self-Sampling Assumption (SSA)** vs **Self-Indication Assumption (SIA)**
- **Simulation arguments** (Bostrom)
- **Anthropics and AI doom probability estimates**
- **Doomsday argument**
- **Embedded agency:** agents reasoning about themselves as part of the environment

### Lesson 66: The Alignment Problem
- **Core problem:** ensuring AI systems pursue goals beneficial to humanity
- **Outer alignment:** specifying the right objective
- **Inner alignment:** ensuring the model optimizes for the specified objective
- **Mesa-optimization:** learned optimizers within the model (mesa-objectives vs base objectives)
- **Deceptive alignment:** model appears aligned during training but isn't
- **Current alignment techniques:**
  - RLHF, Constitutional AI, debate, recursive reward modeling
  - Scalable oversight, interpretability-based safety
- **Goodhart's Law:** when a measure becomes a target, it ceases to be a good measure

### Lesson 67: Open Problems and Research Frontiers
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
