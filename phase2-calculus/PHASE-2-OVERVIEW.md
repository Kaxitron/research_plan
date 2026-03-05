# Phase 2 Overview: ODEs, Multivariable Calculus, Vector Calculus, PDEs & ML-Applied Calculus — Every Concept and Method

> **Purpose:** Exhaustive reference of every concept, technique, and method covered in Phase 2 (Lessons 13-36), organized into five blocks across 24 lessons. Primary sources are Trefor Bazett's ODE, Multivariable, and Vector Calculus courses, Jason Bramburger's PDE course, and ML-focused applied calculus material.
>
> **Estimated total hours:** ~235-280h

---

## Block A: Ordinary Differential Equations (Lessons 13-18) — Trefor Bazett ODE Course

### Lesson 13: Calculus Fundamentals — Rebuilding Your Intuition

**Derivatives:**
- Derivative as instantaneous rate of change — slope of the tangent line
- Limit definition: f'(x) = lim_{h->0} [f(x+h) - f(x)] / h
- Secant lines -> tangent lines as h -> 0
- "Zooming in" intuition: smooth curves look linear at sufficient magnification (local linearity)
- Differentials dx, dy as actual tiny quantities

**Differentiation Rules:**
- Power rule: d/dx x^n = nx^{n-1}
- Constant multiple and sum rules (derivative is a linear operator)
- Product rule: (fg)' = f'g + fg' (rectangle area geometric proof)
- Quotient rule: (f/g)' = (f'g - fg')/g^2
- Chain rule: d/dx f(g(x)) = f'(g(x)) g'(x) — the single most important rule for ML

**Key Functions and Their Derivatives:**
- e^x -> e^x (its own derivative; appears in softmax, log-likelihood, exponential decay)
- ln(x) -> 1/x (appears in cross-entropy, log-likelihood, information theory)
- Logarithmic derivative: d/dx ln(f(x)) = f'(x)/f(x) (relative rate of change)
- sin(x) -> cos(x), cos(x) -> -sin(x) (positional encodings, Fourier features)
- Sigmoid sigma(x) = 1/(1+e^{-x}): sigma'(x) = sigma(x)(1-sigma(x)), max derivative = 0.25 -> vanishing gradients
- tanh(x): output in (-1,1), tanh'(x) = 1 - tanh^2(x)
- ReLU(x) = max(0,x): derivative is 0 or 1 (no gradient shrinkage but dead neurons)
- Leaky ReLU, GELU, SiLU (Swish) variants
- Softplus: ln(1 + e^x) — smooth ReLU approximation

**Integration:**
- Definite integral integral_a^b f(x)dx = signed area under curve
- Riemann sums: left, right, midpoint, trapezoidal approximations
- Fundamental Theorem of Calculus Part 1: d/dx integral_a^x f(t)dt = f(x)
- Fundamental Theorem of Calculus Part 2: integral_a^b f(x)dx = F(b) - F(a) where F' = f
- Antiderivatives (indefinite integrals) + constant of integration (+C)
- Standard antiderivative table: x^n, 1/x, e^x, sin, cos, etc.

**Integration Techniques:**
- u-substitution (reverse chain rule)
- Integration by parts: integral u dv = uv - integral v du (reverse product rule)
- Partial fractions (for rational functions)
- Trigonometric substitutions and identities
- Improper integrals: convergence/divergence over unbounded domains

**Limits, Continuity, and Foundational Theorems:**
- Limits: formal epsilon-delta definition (conceptual), one-sided limits
- Continuity at a point: lim_{x->a} f(x) = f(a)
- L'Hopital's rule for 0/0 and infinity/infinity indeterminate forms
- Squeeze theorem
- Intermediate Value Theorem (IVT)
- Mean Value Theorem (MVT): there exists c in (a,b) where f'(c) = [f(b)-f(a)]/(b-a)
- Extreme Value Theorem: continuous f on closed [a,b] attains max and min

**Optimization (Single Variable):**
- Critical points: f'(x) = 0 or undefined
- Second derivative test: f'' > 0 -> local min, f'' < 0 -> local max, f'' = 0 -> inconclusive
- Concavity: f'' > 0 = concave up (bowl), f'' < 0 = concave down (hill)
- Inflection points: where concavity changes

**Sequences and Series:**
- Sequences: convergence, divergence, bounded, monotone
- Series: sum a_n, partial sums, geometric series (a/(1-r) when |r|<1)
- Convergence tests: ratio test, comparison test, integral test, root test
- Power series: sum a_n x^n, radius of convergence
- Taylor/Maclaurin series (expanded in Lesson 22)

**Newton's Method:**
- Root-finding via linearization: x_{n+1} = x_n - f(x_n)/f'(x_n)
- Geometric intuition: follow the tangent line to the x-axis, repeat
- Quadratic convergence: correct digits roughly double each iteration (when it converges)
- Failure modes: f'(x_n) ~ 0 (horizontal tangent), oscillation, divergence from bad initial guess
- Basin of attraction: set of initial points that converge to a given root
- Connection to optimization: apply Newton's method to f'(x) = 0 to find extrema -> Newton's method in optimization
- ML connection: second-order optimization methods (Newton-Raphson, natural gradient) use curvature information

**Inverse Function Derivatives:**
- If y = f(x) is invertible, then (f^{-1})'(y) = 1/f'(x) = 1/f'(f^{-1}(y))
- Geometric intuition: reflecting the curve over y = x swaps rise and run -> slope inverts
- Derivation of d/dx(arcsin x), d/dx(arccos x), d/dx(arctan x) via implicit differentiation
- Derivation of d/dx(ln x) = 1/x from inverse of e^x
- General principle: implicit differentiation is the universal tool when an explicit inverse is messy or unavailable

**Polar Coordinates:**
- Point representation: (r, theta) where r = distance from origin, theta = angle from positive x-axis
- Conversion: x = r cos theta, y = r sin theta; r^2 = x^2 + y^2, theta = arctan(y/x)
- Common polar curves: circles (r = a), cardioids (r = 1 + cos theta), roses (r = cos n*theta), spirals (r = a*theta), limacons
- Polar area: A = 1/2 integral r(theta)^2 d(theta) — derived from summing thin pie-slice sectors
- Arc length in polar: L = integral sqrt(r^2 + (dr/d(theta))^2) d(theta)
- Tangent lines: dy/dx = (r' sin theta + r cos theta)/(r' cos theta - r sin theta) via parametric chain rule
- Symmetry tests: replace theta -> -theta, theta -> pi-theta, or r -> -r to detect symmetry about x-axis, y-axis, or origin
- ML/alignment connection: polar/angular coordinates appear in phase portraits of 2D dynamical systems and in complex-valued representations

---

### Lesson 14: Introduction to ODEs — Classification and Direction Fields

**What Is an ODE:**
- An ordinary differential equation relates a function to its derivatives: F(t, y, y', y'', ...) = 0
- **Order:** the highest derivative present (first-order: y', second-order: y'', etc.)
- **Linear vs nonlinear:** linear if y and its derivatives appear only to the first power with no products between them
- **Autonomous vs non-autonomous:** autonomous if the independent variable t does not appear explicitly in f
- **Homogeneous vs nonhomogeneous:** homogeneous if every term involves y or its derivatives (no forcing function)

**Direction Fields (Slope Fields):**
- For dy/dt = f(t, y), draw a short line segment with slope f(t, y) at each point (t, y)
- Solution curves are paths that are everywhere tangent to the field
- Direction fields give qualitative behavior without solving the equation
- **Isoclines:** curves where dy/dt = constant — useful for sketching direction fields by hand

**Existence and Uniqueness:**
- **Picard-Lindelof theorem:** if f(t, y) is continuous and Lipschitz in y, then a unique solution exists through each initial condition
- When uniqueness fails: solution curves can merge (e.g., dy/dt = y^{1/3} at origin)
- Geometric consequence: solution curves of a well-posed ODE never cross

**Fixed Points and Stability (1D Autonomous):**
- Fixed point y*: where f(y*) = 0 (flow stops)
- **Stable (attracting):** f'(y*) < 0 — nearby trajectories converge toward y*
- **Unstable (repelling):** f'(y*) > 0 — nearby trajectories diverge from y*
- **Semi-stable:** stable from one side, unstable from the other
- **Phase line analysis:** arrows on a number line showing direction of flow between fixed points

**Euler's Method:**
- Numerical approximation: y_{n+1} = y_n + h f(t_n, y_n) — follow the tangent line for a small step h
- Geometric intuition: walk along the direction field in discrete steps
- Error is O(h) per step, O(h) globally (first-order method)
- Smaller h = more accurate but more computation
- Improved Euler (Heun's method), Runge-Kutta 4th order (RK4) for better accuracy

**Gradient Descent as an ODE:**
- Discrete: W_{t+1} = W_t - eta * grad L(W_t)
- Continuous limit (eta -> 0): dW/dt = -grad L(W)
- **Euler's method IS gradient descent** with step size h = eta
- Higher-order ODE solvers inspire higher-order optimization methods

**ML/alignment connection:** Viewing gradient descent as discretized gradient flow (an ODE) provides the theoretical foundation for analyzing training dynamics, convergence, and the effect of learning rate on optimization trajectories.

---

### Lesson 15: First-Order ODEs — Separable, Linear, and Exact

**Separable ODEs:**
- Form: dy/dx = g(x)h(y) — variables can be separated to opposite sides
- Method: integral dy/h(y) = integral g(x) dx, then solve for y
- Watch for lost solutions: dividing by h(y) may lose equilibrium solutions where h(y) = 0
- Example: population growth dy/dt = ky gives y = Ce^{kt}

**First-Order Linear ODEs:**
- Standard form: dy/dx + P(x)y = Q(x)
- **Integrating factor:** mu(x) = e^{integral P(x) dx}
- Multiply both sides by mu: d/dx[mu y] = mu Q, then integrate
- Superposition principle for the homogeneous part (Q = 0)
- General solution = homogeneous solution + particular solution

**Exact Equations:**
- Form: M(x,y) dx + N(x,y) dy = 0
- **Exact if** partial M/partial y = partial N/partial x
- There exists a potential function F(x,y) such that F_x = M, F_y = N, and solutions are F(x,y) = C
- Finding F: integrate M w.r.t. x, differentiate w.r.t. y, match with N
- **Integrating factors for non-exact equations:** multiply by mu to make it exact; mu may depend on x alone or y alone

**Bernoulli Equations:**
- Form: dy/dx + P(x)y = Q(x)y^n
- Substitution v = y^{1-n} reduces to a linear ODE
- Special cases: n = 0 (linear), n = 1 (separable)

**Applications of First-Order ODEs:**
- **Exponential growth/decay:** dy/dt = ky -> y = y_0 e^{kt}
- **Newton's law of cooling:** dT/dt = -k(T - T_env)
- **Mixing problems:** rate in minus rate out
- **Logistic equation:** dy/dt = ry(1 - y/K) — carrying capacity K, S-shaped growth curve
- **RC and RL circuits** as first-order linear ODEs

**Modeling with ODEs:**
- Translating word problems into differential equations
- Identifying the type (separable, linear, exact) to choose the right method
- Checking solutions by substitution back into the original equation
- Equilibrium solutions and long-term behavior from the equation itself

**ML/alignment connection:** The logistic equation is the continuous-time version of the sigmoid function central to binary classification. Exponential growth/decay dynamics appear in gradient flow analysis, and understanding how solutions depend on parameters connects to sensitivity analysis in training.

---

### Lesson 16: Higher-Order Linear ODEs, Mechanical Vibrations, and Power Series Solutions

**Second-Order Linear ODEs with Constant Coefficients:**
- General form: ay'' + by' + cy = g(t)
- **Homogeneous case** (g(t) = 0): guess y = e^{rt}, get characteristic equation ar^2 + br + c = 0
- **Two distinct real roots** r_1, r_2: y = c_1 e^{r_1 t} + c_2 e^{r_2 t}
- **Repeated real root** r: y = (c_1 + c_2 t) e^{rt}
- **Complex conjugate roots** alpha +/- beta i: y = e^{alpha t}(c_1 cos(beta t) + c_2 sin(beta t))

**Higher-Order Linear ODEs:**
- nth-order: a_n y^{(n)} + ... + a_1 y' + a_0 y = g(t)
- Characteristic polynomial of degree n -> n roots -> n linearly independent solutions
- Same methods (undetermined coefficients, variation of parameters) extend to higher order
- **Reduction of order:** if one solution is known, find a second linearly independent one

**Linear Independence and the Wronskian:**
- **Fundamental solutions and the Wronskian:** W(y_1, y_2) = y_1 y_2' - y_1' y_2; nonzero Wronskian guarantees linear independence
- For n solutions: W(y_1, ..., y_n) is the determinant of the matrix whose rows are y_i and their derivatives
- **Abel's theorem:** the Wronskian either vanishes everywhere or nowhere on an interval (for solutions of a linear ODE)

**Mechanical Vibrations (Spring-Mass-Damper):**
- **Free undamped:** my'' + ky = 0 -> y = A cos(omega_0 t - phi), omega_0 = sqrt(k/m)
- **Free damped:** my'' + by' + ky = 0 -> three regimes based on discriminant b^2 - 4mk:
  - **Overdamped** (b^2 > 4mk): slow exponential decay, no oscillation
  - **Critically damped** (b^2 = 4mk): fastest return to equilibrium without oscillation
  - **Underdamped** (b^2 < 4mk): decaying oscillation, y = e^{-bt/(2m)}[c_1 cos(omega_d t) + c_2 sin(omega_d t)]
- **Forced vibrations:** my'' + by' + ky = F_0 cos(omega t)
  - **Resonance:** when driving frequency omega matches natural frequency omega_0 (and damping is small), amplitude blows up
  - **Beats:** when omega is close to but not equal to omega_0, amplitude modulates
  - **Steady-state vs transient response:** transient dies out, steady-state persists

**Nonhomogeneous Equations:**
- **Method of undetermined coefficients:** guess the form of the particular solution based on g(t)
  - g(t) polynomial -> try polynomial of same degree
  - g(t) = e^{at} -> try Ae^{at}
  - g(t) = sin/cos -> try A cos + B sin
  - If the guess solves the homogeneous equation, multiply by t
- **Variation of parameters:** y_p = u_1 y_1 + u_2 y_2 where u_1' and u_2' are found from a 2x2 system
  - More general than undetermined coefficients — works for any g(t)
- **Superposition principle:** for linear equations, sum of solutions is a solution

**Power Series Solutions:**
- Assume y = sum a_n x^n, substitute into the ODE, match coefficients of each power of x to get a recurrence relation for the a_n
- **Ordinary point:** where the coefficient functions P(x), Q(x) in y'' + P(x)y' + Q(x)y = 0 are analytic — power series solutions guaranteed to converge
- **Singular point:** where P(x) or Q(x) blow up — standard power series method fails; need Frobenius method or other techniques
- **Airy's equation:** y'' - xy = 0 — canonical example with no closed-form elementary solution, solved exactly by power series yielding two independent series Ai(x) and Bi(x)

**Initial Value Problems vs Boundary Value Problems:**
- IVP: conditions at a single point (y(t_0) = y_0, y'(t_0) = v_0)
- BVP: conditions at two or more points (y(a) = alpha, y(b) = beta)
- BVPs can have zero, one, or infinitely many solutions

**ML/alignment connection:** The spring-mass-damper system is the exact mechanical analogy for momentum-based optimization: mass = inertia, damping = friction coefficient (momentum decay), spring force = gradient. Overdamped = slow convergence, underdamped = oscillation around the minimum, critically damped = optimal convergence. Resonance phenomena relate to sensitivity of training to hyperparameter choices.

---

### Lesson 17: The Laplace Transform

**Definition and Basic Properties:**
- L{f(t)} = F(s) = integral_0^infinity e^{-st} f(t) dt — transforms a function of time into a function of complex frequency
- Converts differential equations into algebraic equations
- **Linearity:** L{af + bg} = aF + bG
- **Existence conditions:** f must be piecewise continuous and of exponential order

**Key Transform Pairs:**
- L{1} = 1/s
- L{t^n} = n!/s^{n+1}
- L{e^{at}} = 1/(s-a)
- L{sin(bt)} = b/(s^2 + b^2)
- L{cos(bt)} = s/(s^2 + b^2)
- L{e^{at}f(t)} = F(s-a) (first shifting theorem / s-shifting)

**Operational Properties:**
- **Derivative property:** L{f'(t)} = sF(s) - f(0) — this is what converts ODEs to algebra
- L{f''(t)} = s^2 F(s) - sf(0) - f'(0)
- **t-shifting (second shifting theorem):** L{u_c(t) f(t-c)} = e^{-cs} F(s) where u_c is the unit step function
- **Convolution theorem:** L{f * g} = F(s)G(s), where (f * g)(t) = integral_0^t f(tau) g(t-tau) d(tau)
- **Differentiation of transform:** L{t f(t)} = -F'(s)

**Inverse Laplace Transform:**
- **Partial fraction decomposition:** break F(s) into simple fractions, invert each using the table
- Distinct real poles, repeated poles, complex conjugate poles
- **Completing the square** for irreducible quadratics
- Heaviside cover-up method for distinct linear factors

**Solving ODEs with the Laplace Transform:**
- Take L of both sides, using derivative property to incorporate initial conditions
- Solve the algebraic equation for Y(s)
- Invert Y(s) using partial fractions and the table
- Particularly powerful for: piecewise forcing functions, impulse inputs (Dirac delta), and systems with discontinuities

**Special Functions:**
- **Unit step function** u_c(t): models switching on/off at time c
- **Dirac delta function** delta(t-c): idealized impulse; L{delta(t-c)} = e^{-cs}
- **Periodic functions:** L{f} = 1/(1-e^{-sT}) integral_0^T e^{-st} f(t) dt

**Transfer Functions and Systems:**
- **Transfer function** H(s) = Y(s)/X(s): ratio of output to input in the s-domain
- Poles of H(s) determine system stability: all poles in left half-plane -> stable
- Zeros determine frequency response characteristics
- **Impulse response:** h(t) = L^{-1}{H(s)}, the system's response to a delta function input

**ML/alignment connection:** The Laplace transform is the continuous analog of the Z-transform used in discrete signal processing and control theory. Transfer function analysis connects to understanding how perturbations propagate through layers in a neural network. The convolution theorem underlies efficient computation in convolutional networks, and the concept of frequency-domain analysis appears in understanding what neural networks learn at different scales.

---

### Lesson 18: Systems of ODEs and Phase Portraits

**Systems of First-Order ODEs:**
- dx/dt = Ax where A is an n x n constant matrix and x is a vector
- Any nth-order ODE can be rewritten as a system of n first-order ODEs
- **Solution via eigenvalues/eigenvectors:** x(t) = c_1 e^{lambda_1 t} v_1 + c_2 e^{lambda_2 t} v_2 + ...
- **Matrix exponential:** e^{At} = I + At + (At)^2/2! + ... — the fundamental solution matrix

**Phase Portrait Classification (2D Linear Systems):**
- Both eigenvalues negative real -> **stable node** (all trajectories converge to origin)
- Both positive real -> **unstable node** (all trajectories diverge from origin)
- Opposite signs -> **saddle point** (converge along one eigendirection, diverge along other)
- Complex with Re(lambda) < 0 -> **stable spiral** (converge while rotating)
- Complex with Re(lambda) > 0 -> **unstable spiral** (diverge while rotating)
- Purely imaginary (Re(lambda) = 0) -> **center** (closed orbits, neutrally stable)
- Repeated eigenvalue, one eigenvector -> **degenerate/improper node** (star node if two independent eigenvectors)

**Nonlinear Systems and Linearization:**
- Nonlinear system: dx/dt = f(x) where f is a general vector field
- **Equilibria (fixed points):** where f(x*) = 0
- **Linearization:** near x*, approximate by dx/dt = J(x*)(x - x*) where J is the Jacobian matrix evaluated at x*
- **Hartman-Grobman theorem:** if all eigenvalues of J(x*) have nonzero real part (hyperbolic fixed point), the nonlinear phase portrait is topologically equivalent to the linearized one near x*
- Non-hyperbolic fixed points require nonlinear analysis (center manifold theory, Lyapunov methods)

**Stability Theory:**
- **Lyapunov stability:** trajectories starting near x* stay near x*
- **Asymptotic stability:** trajectories converge to x* as t -> infinity
- **Lyapunov's direct method:** find V(x) > 0 with V(x*) = 0 and dV/dt <= 0 -> stable; dV/dt < 0 -> asymptotically stable
- For gradient flow (dW/dt = -grad L), the loss L itself is a Lyapunov function: dL/dt = -||grad L||^2 <= 0
- **Basins of attraction:** regions of initial conditions that converge to a given stable fixed point
- **Separatrices:** boundaries between basins of attraction (often the stable manifolds of saddle points)

**Bifurcations:**
- Qualitative behavior changes as a parameter varies
- **Saddle-node bifurcation:** two fixed points collide and annihilate
- **Transcritical bifurcation:** two fixed points exchange stability
- **Pitchfork bifurcation:** symmetry breaking — one fixed point splits into three
- **Hopf bifurcation:** a fixed point loses stability and a limit cycle appears (or disappears)
- **Bifurcation diagrams:** plot fixed point location/stability vs parameter

**Limit Cycles and Attractors:**
- **Limit cycle:** isolated closed orbit that neighboring trajectories approach (or recede from)
- **Poincare-Bendixson theorem:** in 2D, bounded trajectories must approach a fixed point or limit cycle
- Gradient systems (dx/dt = -grad V) cannot have limit cycles
- **Strange attractors:** bounded, non-periodic, sensitive to initial conditions (chaos)

**Coupled Systems and Applications:**
- Predator-prey (Lotka-Volterra) models
- Competing species models
- Epidemiological models (SIR)
- Chemical reaction kinetics

**ML/alignment connection:** Phase portrait analysis directly applies to understanding optimization dynamics in neural networks. Eigenvalues of the Hessian at critical points determine whether training converges (stable node), oscillates (spiral), or escapes (saddle). Basins of attraction correspond to which minimum a network converges to depending on initialization. Bifurcation theory relates to phase transitions in training — grokking, emergent capabilities, and sudden loss drops can be understood as bifurcations in the training dynamical system.

---

## Block B: Multivariable Calculus (Lessons 19-23) — Trefor Bazett Multivariable Course

### Lesson 19: 3D Geometry, Curves, and Curvature

**Functions of Several Variables:**
- f: R^n -> R — scalar-valued function of a vector input
- Domain, range, level curves (2D), level surfaces (3D)
- Visualizing: surface plots z = f(x,y), contour maps, heat maps

**Partial Derivatives:**
- partial f/partial x_i: rate of change when wiggling one input, holding all others fixed
- Notation: f_x, f_y, partial f/partial x, partial_1 f
- Geometric interpretation: slope of the slice of the surface along one coordinate axis
- Higher-order partials: f_{xx}, f_{yy}, f_{xy} (mixed partials)
- **Clairaut's theorem (symmetry of mixed partials):** f_{xy} = f_{yx} when both are continuous

**Tangent Planes and Linear Approximation:**
- Tangent plane at (x_0, y_0): z - z_0 = f_x(x_0,y_0)(x-x_0) + f_y(x_0,y_0)(y-y_0)
- **Linear approximation (total differential):** f(x) ~ f(a) + grad f(a) . (x-a)
- The tangent plane IS the best linear approximation to the surface at a point
- Error bounds: the approximation is good when ||x - a|| is small relative to the curvature

**The Gradient:**
- grad f = (partial f/partial x_1, ..., partial f/partial x_n) — collects all partial derivatives into a vector
- **Points in the direction of steepest ascent** (negative gradient = steepest descent)
- **Perpendicular to level curves (contour lines)**
- Magnitude ||grad f|| = rate of steepest ascent
- Gradient field: vector field of grad f at every point

**Directional Derivatives:**
- D_u f = grad f . u_hat — rate of change in arbitrary direction u_hat (unit vector)
- Maximum when u_hat aligns with grad f; zero when u_hat is perpendicular (along contour)
- Minimum (most negative) when u_hat is antiparallel to grad f

**3D Coordinate Systems and Quadric Surfaces:**
- Cartesian coordinates in 3D, right-hand rule, distance formula
- **Quadric surfaces:** ellipsoids, paraboloids (elliptic, hyperbolic), hyperboloids (one sheet, two sheets), cones, cylinders — degree-2 equations in 3D
- Level surfaces f(x,y,z) = c as the 3D analog of level curves

**ML/alignment connection:** The gradient is the central object in all of machine learning optimization. Gradient descent follows -grad L to minimize loss. The perpendicularity of the gradient to level sets means that gradient descent always crosses contour lines at right angles, which explains why it zigzags in elongated valleys rather than heading directly toward the minimum.

---

### Lesson 20: Multivariable Functions, Limits, and Partial Derivatives

**Chain Rule Generalizations:**
- Single-variable reminder: d/dx f(g(x)) = f'(g(x)) g'(x)
- **Multivariable chain rule:** partial f/partial t = sum_i (partial f/partial x_i)(partial x_i/partial t) — sum over all paths in the dependency tree
- Chain rule with multiple intermediate and multiple independent variables
- **Tree diagrams** for tracking which variables depend on which — each path through the tree contributes one term

**The Jacobian Matrix:**
- For F: R^n -> R^m, the Jacobian J is the m x n matrix of all partial derivatives: J_{ij} = partial F_i/partial x_j
- The Jacobian IS the total derivative — the best linear approximation to F near a point
- Jacobian generalizes: scalar gradient (1 x n row vector), ordinary derivative (1 x 1), and matrix calculus
- **Composition of Jacobians:** J_{F composed G} = J_F * J_G (chain rule as matrix multiplication)
- The columns of J show how each input affects all outputs; the rows show how each output depends on all inputs

**Vector-Valued Functions and Parametric Curves:**
- r(t) = (x(t), y(t), z(t)) — parametric curves in space
- r'(t) = tangent vector = velocity vector
- ||r'(t)|| = speed; r'(t)/||r'(t)|| = unit tangent vector
- **Arc length:** L = integral ||r'(t)|| dt
- **Curvature:** kappa = ||r' x r''|| / ||r'||^3 — how sharply the curve bends
- **TNB frame:** tangent, normal, and binormal unit vectors (Frenet-Serret formulas)

**The Hessian Matrix:**
- Second-order partial derivative matrix: H_{ij} = partial^2 f / partial x_i partial x_j
- Always symmetric (by Clairaut's theorem)
- Eigenvalues of H = principal curvatures of the function surface
- Positive definite H -> local minimum; negative definite -> local maximum; indefinite -> saddle
- **Condition number** kappa = lambda_max/lambda_min — measures elongation of the level sets

**ML/alignment connection:** The Jacobian is the mathematical backbone of backpropagation. The chain rule as matrix multiplication (J_{F composed G} = J_F * J_G) is exactly what happens during the backward pass: each layer multiplies its local Jacobian. The condition number of the Hessian directly predicts how hard a loss landscape is to optimize — high condition numbers cause gradient descent to zigzag.

---

### Lesson 21: The Chain Rule, Directional Derivatives, and Gradients

**Double and Triple Integrals:**
- Double integral integral integral_D f(x,y) dA: volume under surface over region D
- Triple integral integral integral integral_E f(x,y,z) dV: integral over 3D region
- **Iterated integrals:** evaluate by integrating one variable at a time
- **Fubini's theorem:** order of integration can be swapped (when integrand is continuous)
- Setting up integration bounds for non-rectangular regions — sketching the region is essential
- Reversing the order of integration to simplify computation

**Applications of Multiple Integrals:**
- Area, volume, mass (with density function)
- Center of mass: x_bar = (1/M) integral integral x rho(x,y) dA
- Moments of inertia
- Surface area of z = f(x,y): integral integral sqrt(1 + f_x^2 + f_y^2) dA
- Probability: P(event) = integral integral_region p(x,y) dx dy for joint density p

**Coordinate Systems and Change of Variables:**
- **Polar coordinates:** (r, theta), dA = r dr d(theta)
- **Cylindrical coordinates:** (r, theta, z), dV = r dr d(theta) dz
- **Spherical coordinates:** (rho, theta, phi), dV = rho^2 sin(phi) d(rho) d(theta) d(phi)
- **General change of variables formula:** integral integral f(x,y) dA = integral integral f(g(u,v)) |det(J)| du dv
- **Jacobian determinant** |det(partial(x,y)/partial(u,v))| measures local area/volume stretching factor

**The Gaussian Integral:**
- integral_{-infinity}^{infinity} e^{-x^2} dx = sqrt(pi) (proved elegantly via polar coordinates)
- **Multivariate Gaussian normalization** involves det(Sigma) and the Jacobian
- This integral underpins all of probability theory and statistics

**ML Connection — Probability and Sampling:**
- **Monte Carlo integration:** approximate integral f(x)p(x)dx by sampling from p and averaging f
- **Importance sampling:** sample from proposal q, reweight by p/q to estimate expectations under p
- **Normalizing flows** = chain of invertible transformations with tracked Jacobian determinants
- **Reparameterization trick** in VAEs: z = mu + sigma * epsilon allows backprop through sampling
- **Change of variables for probability densities:** p(y) = p(f^{-1}(y)) |det(J_{f^{-1}})|

**ML/alignment connection:** The change of variables formula is the mathematical foundation of normalizing flows, a class of generative models that transform simple distributions into complex ones by tracking how the Jacobian determinant changes probability density. Monte Carlo integration is how we compute expectations over intractable distributions in Bayesian inference and reinforcement learning.

---

### Lesson 22: Optimization, Taylor Expansions, and the Implicit Function Theorem

**Taylor Series (Single Variable):**
- f(x) ~ f(a) + f'(a)(x-a) + (1/2)f''(a)(x-a)^2 + (1/3!)f'''(a)(x-a)^3 + ...
- Zeroth order: constant approximation
- First order: linear approximation (tangent line) — this is what gradient descent uses
- Second order: quadratic approximation — this is what Newton's method uses
- **Maclaurin series:** Taylor series centered at a = 0
- Key series: e^x = 1 + x + x^2/2! + ...; sin x = x - x^3/3! + ...; 1/(1-x) = 1 + x + x^2 + ...
- **Remainder/error bounds:** Taylor's theorem with Lagrange remainder

**Multivariate Taylor Expansion:**
- f(w) ~ f(w_0) + grad f(w_0)^T (w-w_0) + (1/2)(w-w_0)^T H(w_0)(w-w_0) + ...
- At critical points (grad f = 0): the local landscape IS the quadratic form of the Hessian
- Hessian eigenvalues completely determine local geometry at critical points
- This is why second-order methods (Newton, natural gradient) use the Hessian — they fit a local quadratic

**Implicit Function Theorem (IFT):**
- When F(x,y) = 0 defines y implicitly as a function of x
- IFT gives: dy/dx = -(partial F/partial x)/(partial F/partial y) when partial F/partial y != 0
- **Multivariable IFT:** F: R^{n+m} -> R^m, F(x,y) = 0 defines y as a function of x when det(partial F/partial y) != 0
- **Fails at singularities** (where partial F/partial y = 0 or det = 0) -> bifurcation points
- Connection to SLT: singularities in the parameter-function map are where IFT breaks down — these are exactly the degenerate critical points that SLT studies

**Big-O Notation for Approximation:**
- f(x) = O(g(x)) means |f(x)| <= C|g(x)| for sufficiently small/large x (depending on context)
- Used for truncation error bounds in Taylor approximation
- "First-order accurate" = error is O(h^2) when approximation is O(h)

**ML/alignment connection:** The Taylor expansion is the theoretical justification for gradient descent (trust the first-order approximation) and Newton's method (trust the second-order approximation). The implicit function theorem explains when smooth changes in hyperparameters lead to smooth changes in optimal parameters — and its failure points (singularities) are central to Singular Learning Theory's explanation of phase transitions in neural network training.

---

### Lesson 23: Multiple Integration and Change of Variables

**Unconstrained Optimization:**
- **Critical points:** where grad f = 0 (all partial derivatives vanish)
- **Second derivative test via Hessian:** at a critical point:
  - H positive definite (all eigenvalues > 0) -> local minimum
  - H negative definite (all eigenvalues < 0) -> local maximum
  - H indefinite (mixed eigenvalues) -> saddle point
- **2D Hessian test:** discriminant D = f_{xx} f_{yy} - f_{xy}^2; D > 0 and f_{xx} > 0 -> min; D > 0 and f_{xx} < 0 -> max; D < 0 -> saddle
- **Global extrema on closed bounded regions:** check critical points in interior AND boundary

**Constrained Optimization — Lagrange Multipliers:**
- **Problem:** minimize f(x) subject to g(x) = 0
- **Geometric insight:** at the optimum, grad f and grad g are parallel — contour lines of f are tangent to the constraint surface
- **Lagrangian:** L(x, lambda) = f(x) - lambda g(x)
- Solve the system: grad_x L = 0 and g(x) = 0 simultaneously
- lambda = the Lagrange multiplier = "shadow price" = rate of change of optimal value per unit relaxation of constraint
- **Multiple equality constraints:** one lambda per constraint; grad f = sum lambda_i grad g_i
- **Inequality constraints -> KKT conditions:** complementary slackness (lambda_i g_i = 0), lambda_i >= 0 for active constraints

**Convexity:**
- f is convex if the line segment between any two points on the graph lies above the graph
- Equivalent: H is positive semi-definite everywhere
- **For convex f: every local minimum is a global minimum** — no local traps
- Neural network loss functions are generally NON-convex; convexity theory provides lower bounds on what's achievable

**Duality:**
- **Dual problem:** max_lambda min_x L(x, lambda) — switch the order of optimization
- **Weak duality:** dual optimal value <= primal optimal value (always)
- **Strong duality:** equality holds (guaranteed under Slater's condition for convex problems)
- **Regularization as soft constraint:** L2 penalty ||w||^2 <= C is equivalent to a Lagrange multiplier lambda being the regularization strength
- SVMs are derived via the dual of a constrained quadratic program

**ML/alignment connection:** Lagrange multipliers and constrained optimization are the mathematical language for regularization, which is central to generalization in ML. L2 regularization, weight decay, and norm constraints on parameters are all instances of constrained optimization. KKT conditions appear in the derivation of support vector machines and in understanding when constraints are active during training.

---

## Block C: Vector Calculus (Lessons 24-27, 28) — Trefor Bazett Vector Calculus (8 Chapters)

### Lesson 24: Line Integrals and Curves (Ch. 1)

**Parametric Curves:**
- r(t) = (x(t), y(t), z(t)) for t in [a, b]
- Velocity r'(t), speed ||r'(t)||, acceleration r''(t)
- **Arclength parameterization:** reparameterize so that ||r'(s)|| = 1 — the parameter s is distance traveled
- Smooth vs piecewise-smooth curves

**Scalar Line Integrals:**
- integral_C f ds = integral_a^b f(r(t)) ||r'(t)|| dt
- Geometric meaning: total accumulated quantity along the curve (e.g., mass of a wire with density f)
- Independent of parameterization direction

**Vector Line Integrals (Work Integrals):**
- integral_C F . dr = integral_a^b F(r(t)) . r'(t) dt
- Physical meaning: work done by force field F along curve C
- **Depends on orientation** — reversing the curve negates the integral
- Component form: integral_C P dx + Q dy + R dz

**Properties of Line Integrals:**
- Linearity in the integrand
- Additivity over curve segments: integral_C = integral_{C_1} + integral_{C_2}
- Scalar line integrals are always positive (when f > 0); vector line integrals can be negative

**Distinguishing Types of Line Integrals:**
- Scalar line integrals (integral f ds): weighted by arc length, independent of orientation
- Component line integrals (integral P dx, Q dy, R dz): depend on orientation
- Vector line integrals (integral F . dr): work integral, depend on orientation
- Identifying which type you are computing from the notation and context

**Computing Line Integrals:**
- Step 1: Parameterize the curve
- Step 2: Compute r'(t) and ||r'(t)|| (or the dot product F . r')
- Step 3: Substitute and integrate over the parameter interval
- Common parameterizations: line segments, circles, ellipses, helices

**ML/alignment connection:** Line integrals along optimization trajectories measure cumulative quantities like total loss reduction or work done against the gradient field. The path-dependence of vector line integrals (vs path-independence for conservative fields) is analogous to how the order of gradient updates matters in non-convex optimization.

---

### Lesson 25: Vector Fields and Conservative Fields (Ch. 2-3)

**Vector Fields:**
- A vector field F assigns a vector to every point in a region: F(x,y) = (P(x,y), Q(x,y))
- Visualization: arrow at each point showing direction and magnitude
- Examples: gravitational fields, fluid velocity fields, gradient fields
- Gradient vector fields F = grad(phi) and potential functions phi

**Divergence:**
- div(F) = partial P/partial x + partial Q/partial y (+ partial R/partial z in 3D)
- Measures net outward flux per unit area — sources (+) and sinks (-)
- Positive divergence = field spreading out; negative = field converging

**Line Integral of a Vector Field (Work):**
- integral_C F . dr = integral_a^b F(r(t)) . r'(t) dt
- Physical meaning: work done by force field F along curve C
- **Component form:** integral_C P dx + Q dy + R dz

**Line Integrals with Respect to x, y, z:**
- integral_C P dx, integral_C Q dy, integral_C R dz as individual component integrals
- Relationship to the full work integral: integral_C F . dr = integral_C P dx + Q dy + R dz
- These depend on orientation — reversing the curve negates the integral

**Flux Integrals with Components:**
- Flux = integral_C F . n_hat ds: measuring outward flow through a curve
- In 2D: integral_C -Q dx + P dy (or integral_C P dy - Q dx depending on convention)
- Measures how much of the field passes through the curve rather than along it

**Curl in 2D (Scalar Curl):**
- scalar curl = partial Q/partial x - partial P/partial y
- Measures local circulation/rotation of the field at a point
- Positive curl = counterclockwise rotation; negative = clockwise

**Conservative Vector Fields:**
- F is conservative if F = grad phi for some scalar potential function phi
- **Equivalent characterizations:**
  - Line integrals are path-independent: integral_C F . dr depends only on endpoints
  - Closed loop integrals vanish: integral_C F . dr = 0 for every closed curve C
  - F = grad phi for some scalar phi
- **Fundamental Theorem for Line Integrals:** if F = grad phi, then integral_C F . dr = phi(endpoint) - phi(start)
- This is the multivariable generalization of FTC

**Testing for Conservative Fields:**
- In 2D: F = (P, Q) is conservative if and only if partial P/partial y = partial Q/partial x (on a simply connected domain)
- **Simply connected domain:** no holes — every closed curve can be continuously shrunk to a point
- On domains with holes, the test is necessary but not sufficient

**Exact and Closed Forms:**
- A differential form P dx + Q dy is **exact** if it equals d(phi) for some scalar function phi (i.e., F is conservative)
- A form is **closed** if partial P/partial y = partial Q/partial x (i.e., it passes the conservative test)
- On simply connected domains: closed implies exact
- This language generalizes to higher dimensions and connects to the 3D curl test (Lesson 27)

**Finding Potential Functions:**
- Integrate P w.r.t. x -> phi(x,y) = integral P dx + g(y)
- Differentiate w.r.t. y and match with Q to determine g(y)
- Verify by checking that grad phi = F

**Gradient Descent and Conservative Fields:**
- The loss gradient field grad L is always conservative (L is the potential)
- Gradient descent follows this conservative field downhill
- Path independence means the total loss change depends only on start and end parameters, not the path taken — but this is for the continuous gradient flow; discrete steps break exact conservativeness

**ML/alignment connection:** Neural network loss landscapes define gradient fields that are inherently conservative (the loss is the potential function). Understanding conservative fields clarifies why gradient descent converges: it's following a field with a well-defined potential that decreases along trajectories. Non-conservative perturbations (SGD noise, momentum) are what allow escape from local minima.

---

### Lesson 26: Green's Theorem — Circulation, Divergence, and Curl (Ch. 4)

**Green's Theorem (Circulation Form):**
- closed_integral_C (P dx + Q dy) = integral integral_D (partial Q/partial x - partial P/partial y) dA
- Circulation around boundary = integral of (2D curl) over interior
- Orientation convention: positive = counterclockwise, region on the left

**Green's Theorem (Flux / Divergence Form):**
- closed_integral_C F . n_hat ds = integral integral_D (partial P/partial x + partial Q/partial y) dA
- Outward flux through boundary = integral of divergence over interior

**Green's Theorem on Composite (Multiply-Connected) Regions:**
- Regions with holes (e.g., annulus): must account for both outer and inner boundary curves
- Inner boundaries traversed clockwise (opposite to outer boundary) to maintain "region on the left" convention
- Allows application of Green's theorem even when the field has singularities inside holes

**The Laplacian:**
- grad^2 f = div(grad f) = partial^2 f/partial x^2 + partial^2 f/partial y^2 + ... (sum of unmixed second partials)
- Measures how much f(x) deviates from the average of its neighbors
- grad^2 f = 0 -> harmonic function (value at center = average over surrounding sphere)
- Appears in: heat equation, diffusion models, score matching, Laplace's equation

**Vector Calculus Identities:**
- div(curl F) = 0
- curl(grad f) = 0
- grad^2 F = grad(grad . F) - grad x (grad x F)
- Product rules for div and curl with scalar/vector combinations

**ML/alignment connection:** The divergence and curl decompose any vector field into its "source/sink" and "rotational" components (Helmholtz decomposition). In training dynamics, the gradient flow is curl-free by construction, but SGD noise and momentum introduce rotational components. The Laplacian appears in diffusion models (score matching), graph neural networks (graph Laplacian), and regularization (Laplacian smoothing).

---

### Lesson 27: Surfaces, Surface Area, and Surface Integrals (Ch. 5-6)

**Parametric Surfaces:**
- r(u,v) = (x(u,v), y(u,v), z(u,v)) for (u,v) in domain D
- Examples: planes, spheres, cylinders, cones, tori, graphs z = f(x,y)
- Visualizing and understanding parametric surfaces in 3D
- **Tangent vectors:** r_u and r_v span the tangent plane at each point
- **Normal vector:** n = r_u x r_v (cross product of tangent vectors)

**Surface Area:**
- Surface area = integral integral_D ||r_u x r_v|| du dv
- For graphs z = f(x,y): SA = integral integral sqrt(1 + f_x^2 + f_y^2) dA
- Surface area of parametric surfaces: the factor ||r_u x r_v|| is the area magnification factor from parameter space to the surface

**Why Curl Is Useful and the Spider Criteria:**
- Physical interpretation of curl: local rotation, paddle wheel analogy
- The "spider criteria" mnemonic for quickly checking all three components of curl F in 3D
- Identifying conservative fields using curl: if curl F = 0 on a simply connected domain, F is conservative

**The 3D Curl Test for Conservative Fields:**
- In 3D: F = (P, Q, R) is conservative if and only if curl F = 0 (on a simply connected domain)
- This extends the 2D test (partial P/partial y = partial Q/partial x) to three dimensions
- All three component conditions: R_y = Q_z, P_z = R_x, Q_x = P_y
- On domains with holes, curl = 0 is necessary but not sufficient

**Scalar Surface Integrals:**
- integral integral_S f dS = integral integral_D f(r(u,v)) ||r_u x r_v|| du dv
- Geometric meaning: total accumulated quantity over the surface (e.g., mass of a thin shell)

**Vector Surface Integrals (Flux Integrals):**
- integral integral_S F . dS = integral integral_D F(r(u,v)) . (r_u x r_v) du dv
- Physical meaning: total flux of F through the surface S
- **Orientation matters:** choice of normal direction (outward vs inward) determines sign
- **Orientable vs non-orientable surfaces:** Mobius strip is non-orientable (no consistent "outward" direction)

**Flux Through Common Surfaces:**
- Spheres, cylinders, planes, graphs — each has standard parameterizations and normal vectors
- Closed surfaces: convention is outward-pointing normal

**ML/alignment connection:** Surface integrals generalize the notion of "measuring a quantity over a region" to curved spaces. In high-dimensional ML, the loss surface is a hypersurface in parameter space, and understanding its geometry (curvature, area elements) informs how optimization algorithms navigate it. Flux integrals through surfaces in parameter space relate to understanding how probability flows through regions during training.

---

### Lesson 28: Stokes' Theorem, Divergence Theorem, and the Unified View (Ch. 7-8)

**Stokes' Theorem:**
- closed_integral_C F . dr = integral integral_S (curl F) . dS
- Circulation of F around boundary curve C = flux of curl F through any surface S bounded by C
- Generalizes Green's theorem (circulation form) to 3D surfaces
- The surface S can be any orientable surface with boundary C — the integral is the same for all such surfaces
- Orientation: right-hand rule relates curve orientation to surface normal

**Computing Stokes' Theorem:**
- Evaluating surface integrals by converting to line integrals (and vice versa)
- Choosing the easier side: sometimes the line integral is simpler, sometimes the surface integral
- Worked examples with various surfaces and boundary curves

**The Divergence Theorem (Gauss's Theorem):**
- closed_integral integral_S F . dS = integral integral integral_E div(F) dV
- Total outward flux through closed surface S = integral of divergence over enclosed volume E
- Generalizes Green's theorem (flux form) to 3D
- Applications: Gauss's law in electrostatics, fluid flow conservation, heat flow

**Finding Sources and Sinks Using the Divergence Theorem:**
- Identifying where flux originates (sources, div > 0) or vanishes (sinks, div < 0)
- Using the divergence theorem to compute total source/sink strength in a region
- Physical applications: charge density from electric flux, fluid production/absorption rates

**The Hierarchy of Fundamental Theorems:**
- **FTC (1D):** integral_a^b f'(x) dx = f(b) - f(a)
- **Fundamental Theorem for Line Integrals:** integral_C grad phi . dr = phi(end) - phi(start)
- **Green's Theorem (2D):** relates boundary circulation/flux to interior curl/divergence
- **Stokes' Theorem (surfaces):** boundary circulation = interior curl flux
- **Divergence Theorem (volumes):** boundary flux = interior divergence
- All are instances of the **generalized Stokes' theorem:** integral_Omega d(omega) = integral_{partial Omega} omega

**The Generalized Stokes' Theorem:**
- Unifies all the above: "the integral of a derivative over a region equals the integral of the original on the boundary"
- **Differential forms** provide the language: omega is a k-form, d(omega) is its exterior derivative, Omega is a (k+1)-dimensional region, partial Omega is its boundary
- d^2 = 0 (the exterior derivative applied twice gives zero) unifies curl(grad) = 0 and div(curl) = 0
- This is the deepest structural insight of vector calculus

**Computational Methods:**
- Choosing between direct computation and using a theorem — the theorem often converts a hard integral into an easy one
- Verifying theorems by computing both sides
- Using symmetry to simplify integrals
- Choosing the right parameterization/coordinate system

**ML/alignment connection:** The generalized Stokes' theorem — "integrating a derivative over a region equals evaluating the original on the boundary" — is a fundamental principle that appears throughout ML in disguised forms. Conservation laws in physics-informed neural networks, the divergence theorem in normalizing flows (tracking probability mass), and boundary-value formulations in PDEs all rest on this unified framework. The cohomological perspective (d^2 = 0) connects to topological data analysis.

---

## Block D: Partial Differential Equations (Lessons 29-33) — Jason Bramburger PDE Course (46 videos)

### Lesson 29: Heat Equation, Separation of Variables, and Laplace's Equation (Videos: Intro, L1-L12)

**PDE Classification (Videos: Intro, L1-L2):**
- A partial differential equation involves partial derivatives of a function of multiple variables
- **Classification by order:** the highest-order derivative present
- **Linear vs nonlinear:** linear if u and its derivatives appear linearly
- **Classification of second-order linear PDEs:** Au_{xx} + Bu_{xy} + Cu_{yy} + (lower order) = 0
  - B^2 - 4AC < 0: **Elliptic** (e.g., Laplace/Poisson) — equilibrium, steady-state
  - B^2 - 4AC = 0: **Parabolic** (e.g., heat equation) — diffusion, smoothing
  - B^2 - 4AC > 0: **Hyperbolic** (e.g., wave equation) — propagation, waves

**The Heat Equation (Videos: L1-L5):**
- u_t = k grad^2 u (or u_t = k u_{xx} in 1D); derived from conservation of energy + Fourier's law
- **Boundary conditions:** Dirichlet (fixed temperature), Neumann (fixed heat flux), Robin (mixed), Periodic
- **Equilibrium temperature distributions:** steady-state solutions satisfy grad^2 u = 0; in 1D with Dirichlet BCs, the equilibrium is linear interpolation between boundary values
- **The heat equation in higher dimensions:** u_t = k(u_{xx} + u_{yy}) in 2D, u_t = k(u_{xx} + u_{yy} + u_{zz}) in 3D; separation of variables extends naturally
- **Linearity:** if u_1, u_2 are solutions, then c_1 u_1 + c_2 u_2 is also a solution — superposition makes Fourier series solutions possible
- **Key properties:** smoothing, maximum principle, irreversibility, high-frequency modes decay fastest
- **Well-posedness (Hadamard):** existence, uniqueness, continuous dependence on data

**Separation of Variables (Videos: L6-L8):**
- Ansatz u(x,t) = X(x)T(t) reduces the PDE to two ODEs linked by a separation constant
- **Dirichlet BCs** (X(0) = X(L) = 0): X_n = sin(n pi x / L), lambda_n = (n pi / L)^2
- **Neumann BCs** (X'(0) = X'(L) = 0): X_n = cos(n pi x / L); includes lambda_0 = 0 constant mode — temperature approaches uniform equilibrium (average of initial condition)
- **Periodic BCs** (u and u_x match at opposite ends): both sin(2n pi x / L) and cos(2n pi x / L); natural setting for Fourier series on a circle

**Laplace's Equation (Videos: L9-L12):**
- **On a rectangle:** separation u(x,y) = X(x)Y(y); homogeneous BCs on three sides + superposition for multiple nonhomogeneous sides
- **On a disc:** polar coordinates; Poisson integral formula gives solution from boundary data
- **Fluid flow outside a cylinder:** exterior domain; solutions involve r^{-n} terms decaying away from boundary
- **Qualitative properties:** mean value property — value at any point = average on any surrounding circle; maximum principle — max/min only on boundary; uniqueness of Dirichlet problem

**ML/alignment connection:** The heat equation IS the forward process in diffusion models. Boundary conditions correspond to conditioning signals (text prompts, class labels). Laplace's equation describes equilibrium; the mean value property explains why regularized models produce smooth predictions. The maximum principle explains why adversarial examples live at distribution boundaries.

---

### Lesson 30: Fourier Series and the Wave Equation (Videos: L13-L21)

**Fourier Series (Videos: L13-L17):**
- f(x) = a_0/2 + sum [a_n cos(n pi x / L) + b_n sin(n pi x / L)]
- **Fourier coefficients** via orthogonal projection (inner products)
- **Convergence:** pointwise, L^2, uniform; Gibbs phenomenon at discontinuities
- **Parseval's theorem:** energy in physical space = energy in frequency space
- **Sine and cosine series:** half-range expansions; sine series from Dirichlet BCs, cosine series from Neumann BCs
- **Differentiating Fourier series:** term-by-term valid when series converges uniformly; smoothness determines coefficient decay rate
- **Integrating Fourier series:** always valid for L^2-convergent series; improves convergence
- **Complex Fourier series:** f(x) = sum c_n e^{i n pi x / L}; more compact; negative frequencies encode phase; connects to Fourier transform

**The Wave Equation (Videos: L18-L21):**
- u_{tt} = c^2 u_{xx}; derived from Newton's second law on a vibrating string; hyperbolic PDE
- **Boundary conditions:** fixed ends (Dirichlet), free ends (Neumann), mixed; initial conditions specify both displacement u(x,0) and velocity u_t(x,0)
- **Solving via separation of variables:** standing waves with temporal oscillation (contrast: exponential decay in heat equation)
- **d'Alembert's solution:** u(x,t) = f(x - ct) + g(x + ct); superposition of traveling waves
- **Key properties:** finite propagation speed, energy conservation, reversibility, superposition
- **Characteristics:** x +/- ct = const; domain of dependence and range of influence
- **Higher dimensions:** 2D membranes, 3D acoustics; Bessel functions for circular geometry; Huygens' principle

**ML/alignment connection:** Fourier analysis underlies spectral methods in ML — graph Fourier transform, positional encodings, spectral bias. Complex Fourier series is the form used in ML applications. Waves preserve information (ResNets, skip connections) while heat destroys it (plain deep networks) — the mathematical reason why residual architectures work.

---

### Lesson 31: Eigenvalue Problems and Sturm-Liouville Theory (Videos: L22-L29)

**Eigenvalue Problems in PDEs (Video: L22):**
- Separation of variables always produces an eigenvalue problem L[X] = lambda X for the spatial part
- Eigenvalues determine allowed frequencies; eigenfunctions determine spatial mode shapes
- The general theory (Sturm-Liouville) guarantees real eigenvalues, orthogonal eigenfunctions, completeness

**Sturm-Liouville Theory (Videos: L23, L25):**
- -(p(x) y')' + q(x) y = lambda w(x) y on [a,b] with boundary conditions
- Real eigenvalues lambda_1 < lambda_2 < ..., orthogonal eigenfunctions with respect to weight w(x)
- Completeness: any reasonable function expandable in eigenfunctions (generalized Fourier series)
- Unifies all classical eigenvalue problems: standard Fourier modes, Bessel functions, Legendre polynomials

**Heat Flow in a Nonuniform Rod (Video: L24):**
- Variable coefficients k(x), c(x), rho(x) yield a Sturm-Liouville problem -(k(x)X')' = lambda c(x) rho(x) X
- Eigenfunctions no longer simple sines/cosines; depend on material properties

**The Rayleigh Quotient (Video: L26):**
- R[y] = (integral [p(y')^2 + qy^2] dx) / (integral w y^2 dx)
- Minimized by the first eigenfunction; min-max characterization of all eigenvalues
- Infinite-dimensional version of the matrix Rayleigh quotient from Phase 1; directly connects to PCA

**Vibrations of a Nonuniform String (Video: L27):**
- -(tau(x) X')' = lambda rho(x) X; natural frequencies omega_n = sqrt(lambda_n)
- Non-uniform mass/tension distribution changes mode shapes and frequencies

**Eigenfunction Expansions (Video: L28):**
- f(x) = sum c_n y_n(x) with coefficients via weighted inner products — generalizes Fourier series
- Used to solve PDEs with variable coefficients

**Inhomogeneous Boundary Conditions (Video: L29):**
- Decompose u(x,t) = v(x) + w(x,t): v satisfies the inhomogeneous BCs (steady-state), w satisfies homogeneous BCs
- Initial condition for w: w(x,0) = f(x) - v(x), expandable in eigenfunctions

**ML/alignment connection:** Sturm-Liouville is the infinite-dimensional spectral theorem — foundation for kernel PCA, spectral clustering, diffusion maps. The Rayleigh quotient connects to PCA and dimensionality reduction. Nonuniform problems correspond to non-uniform data distributions and variable learning rates. Inhomogeneous BC decomposition mirrors trend removal in signal processing.

---

### Lesson 32: Helmholtz Equation, Fourier Transform, and Infinite Domains (Videos: L30-L38)

**The Helmholtz Equation (Video: L30):**
- grad^2 u + k^2 u = 0; spatial eigenvalue problem from the wave equation after time separation
- Resonant frequencies of a domain — the "drum problem" (Can you hear the shape of a drum?)
- Solutions: sines/cosines (rectangular), Bessel functions (circular), spherical harmonics (spherical)

**Vibrating Circular Membranes (Video: L31):**
- Polar separation yields Bessel's equation r^2 R'' + rR' + (k^2 r^2 - m^2)R = 0
- Mode shapes J_m(k_{mn} r) cos(m theta); nodal lines as circles and diameters
- Eigenvalues NOT integer multiples of fundamental — drums less "musical" than strings

**Eigenfunction Expansions and Resonance (Video: L32):**
- Forced PDE problems: expand in eigenfunctions, each mode satisfies a forced oscillator ODE
- **Resonance:** forcing frequency matching natural frequency causes unbounded amplitude growth (undamped)
- Damping prevents blow-up but produces large amplitudes near resonance

**The Heat Equation on an Infinite Line (Video: L33):**
- No boundaries → continuous spectrum; fundamental solution is the Gaussian kernel G(x,t) = (4 pi alpha t)^{-1/2} exp(-x^2/(4 alpha t))
- Solution via convolution with initial data — Gaussian blurring with width growing as sqrt(t)

**The Fourier Transform (Videos: L34, L36):**
- F_hat(k) = integral f(x) e^{-ikx} dx; inverse: f(x) = (1/2pi) integral F_hat(k) e^{ikx} dk
- Continuous limit of complex Fourier series as period → infinity
- **Properties:** linearity, derivative property (FT[f'] = ik F_hat), convolution theorem (FT[f*g] = F_hat G_hat), Parseval's theorem, Gaussian → Gaussian

**Fourier Transform and the Heat Equation (Video: L35):**
- FT converts heat equation to U_hat_t = -alpha k^2 U_hat → each frequency decays independently
- Inverting recovers Gaussian convolution solution

**Heat Equation on a Semi-Infinite Line (Video: L37):**
- Method of images: odd extension (Dirichlet) or even extension (Neumann)
- Error function erf(x) arises from integrating Gaussian kernel over half-line

**Scattering and the Schrödinger Equation (Video: L38):**
- Time-independent: -hbar^2/(2m) psi'' + V(x) psi = E psi — a Sturm-Liouville problem
- Transmission/reflection coefficients; quantum tunneling through barriers
- Connects PDE theory to quantum mechanics and quantum computing foundations

**ML/alignment connection:** The Fourier transform is ubiquitous in ML — CNNs as convolutions, Fourier Neural Operator, spectral normalization, random Fourier features. The Gaussian fundamental solution IS the denoising kernel in diffusion models. Helmholtz eigenmodes connect to graph Laplacian spectral properties in GNNs. The Schrödinger equation provides the mathematical foundation for quantum ML.

---

### Lesson 33: Method of Characteristics, Transport Equations, and PDEs in ML (Videos: L39-L45 + ML Synthesis)

**Method of Characteristics (Video: L39):**
- Transport equation u_t + c u_x = 0: solution u(x,t) = u_0(x - ct) — profile translates at speed c
- Convert PDE to ODEs along characteristic curves dx/dt = c where u is constant
- Works for linear and quasilinear first-order PDEs

**Characteristics of the Wave Equation (Video: L40):**
- Two families: x - ct = const and x + ct = const — d'Alembert's solution follows directly
- Domain of dependence and range of influence; finite propagation speed

**Boundary Reflections in the Wave Equation (Video: L41):**
- Characteristics reflect at boundaries: inverted (Dirichlet) or same sign (Neumann)
- Method of images converts bounded to infinite-domain problems
- Multiple reflections create standing wave patterns

**Modelling Traffic with PDEs (Video: L42):**
- Conservation of cars: rho_t + (rho v(rho))_x = 0; nonlinear first-order PDE
- Characteristics depend on the solution — different densities propagate at different speeds

**Fanlike Characteristics (Video: L43):**
- Rarefaction waves: characteristics diverge, creating smooth expansion waves
- Traffic light turning green → smooth transition from high to low density

**Shock Waves (Video: L44):**
- Characteristics converge and cross → discontinuity (shock) forms
- **Rankine-Hugoniot condition:** shock speed from conservation; **entropy condition** selects physical solution
- Burgers' equation u_t + u u_x = 0 as canonical model; viscous Burgers' smooths shocks

**The Eikonal Equation (Video: L45):**
- |grad u| = 1/c(x); travel time of wavefronts; high-frequency limit of wave equation
- Characteristics are rays (Snell's law); connects to Hamilton-Jacobi equation and level set methods

**PDEs in ML — Diffusion Models and Score Matching (Block Synthesis):**
- **Forward SDE:** dx = f(x,t)dt + g(t)dW — progressive noise addition
- **Fokker-Planck equation:** describes probability density evolution under the SDE
- **Score function:** s(x,t) = grad_x log p_t(x); **score matching** trains neural network to approximate it
- **Reverse SDE:** dx = [f - g^2 s(x,t)]dt + g dW_bar; **probability flow ODE** for deterministic sampling
- **Numerical discretization:** Euler-Maruyama, DPM-Solver, DDIM — better schemes for faster generation

**Numerical Methods for PDEs:**
- **Finite differences:** forward/backward/central differences; CFL condition; von Neumann stability analysis
- **Finite elements:** basis functions on a mesh
- **Spectral methods:** Fourier mode expansion; exponential convergence for smooth solutions
- **PINNs:** embed PDE constraints in neural network loss function

**Stochastic Dynamics in Training:**
- **SGD as SDE:** gradient flow + mini-batch noise; escape from sharp minima; edge of stability

**Neural Operators:**
- **DeepONet, Fourier Neural Operator (FNO):** learn PDE solution operators in Fourier space

**ML/alignment connection:** Method of characteristics is the PDE analogue of mechanistic interpretability — tracing how inputs influence outputs. Shock formation models phase transitions in training (grokking, loss spikes). Transport equation connects to optimal transport theory and Wasserstein distance in generative models. Flow-matching models literally solve a transport equation. Diffusion models are the direct application of the entire PDE block to generative AI. Understanding the mathematics enables principled design of noise schedules, safety filters, and mechanistic interpretability of generative models.

---

## Block E: ML-Applied Calculus (Lessons 34-36)

### Lesson 34: Scalar Derivatives, Partial Derivatives, and the Gradient

**Scalar Derivative Rules (Review):**
- Constant, power, sum, product, and chain rules
- d/dx[f(g(x))] = f'(g(x)) g'(x) — the chain rule is the single most important rule for ML

**Partial Derivatives:**
- For f(x_1, ..., x_n): treat all variables except the target as constants, then differentiate normally
- Notation: ∂f/∂x_i distinguishes from df/dx

**The Gradient:**
- ∇f = [∂f/∂x_1, ..., ∂f/∂x_n] — a row vector (numerator layout) collecting all partial derivatives
- Direction of steepest ascent; magnitude = rate of change in that direction
- Every call to loss.backward() computes this vector

**ML/alignment connection:** The gradient is the fundamental object in all of deep learning. Understanding that it is just a vector of partial derivatives, assembled mechanically by the rules above, demystifies the training process.

---

### Lesson 35: Matrix Calculus — Jacobians, Element-wise Rules, and Chain Rules

**The Jacobian Matrix:**
- For f: R^n -> R^m, J has entry J_{ij} = ∂f_i/∂x_j, producing an m × n matrix (numerator layout)
- The Jacobian generalizes the gradient: gradient is a special case where m = 1
- **Numerator vs denominator layout conventions** — be consistent within a derivation

**Element-wise Operations (Diagonal Jacobians):**
- When each output depends only on corresponding inputs, the Jacobian is diagonal
- ∂(w + x)/∂w = I (identity)
- ∂(w ⊙ x)/∂w = diag(x) (Hadamard product)
- ∂(w ⊘ x)/∂w = diag(1/x_1, ..., 1/x_n) (element-wise division)

**Scalar Expansion:**
- y = zx: ∂y/∂x = zI, ∂y/∂z = x^T
- y = x + z1: ∂y/∂x = I, ∂y/∂z = 1^T

**Vector Sum Reduction:**
- ∂(Σx_i)/∂x = 1^T (row vector of ones)
- ∂(w·x)/∂x = w^T and ∂(w·x)/∂w = x^T (dot product gradient)
- For L = Σf_i(x): ∂L/∂x = Σ(∂f_i/∂x)

**The Chain Rules:**
- Single-variable: df/dx = (df/dg)(dg/dx)
- Total-derivative: ∂f/∂x = Σ_i (∂f/∂u_i)(∂u_i/∂x) — sums contributions from all paths
- **Vector chain rule:** ∂f/∂x = (∂f/∂g)(∂g/∂x) — Jacobian multiplication; the master rule that degenerates to all others

**ML/alignment connection:** The vector chain rule — Jacobian multiplication — IS backpropagation. Most layer Jacobians are diagonal (element-wise activations) or structured (linear layers give J = W), which is why backpropagation is efficient: you never materialize the full Jacobian.

---

### Lesson 36: Neural Network Gradients — From Neurons to Backpropagation

**Gradient of a Single Neuron Activation:**
- Neuron: f(w, x, b) = max(0, w·x + b) (ReLU activation)
- ∂(w·x)/∂w = x^T, ∂(w·x)/∂x = w^T, ∂(w·x + b)/∂b = 1
- ReLU derivative: 0 when inactive (u ≤ 0), 1 when active (u > 0) — piecewise gating
- Full neuron gradient by chain rule: ∂f/∂w = x^T when active, 0 when inactive

**Gradient of the Neural Network Loss Function:**
- MSE loss: C = (1/N) Σ(ŷ_i - y_i)²
- ∂C/∂w = (1/N) Σ (error_term)_i · x_i^T — summed over training examples
- ∂C/∂b = (2/N) Σ (error when active, 0 when inactive)
- Gradient descent update: w ← w - α(∂C/∂w), b ← b - α(∂C/∂b)

**Computation Graphs and Automatic Differentiation:**
- Neural networks as directed acyclic graphs (DAGs) of differentiable operations
- **Forward-mode autodiff:** propagate tangent vectors forward, one Jacobian column per pass
- **Reverse-mode autodiff (backpropagation):** propagate adjoint vectors backward, one Jacobian row per pass
- For 1 scalar loss and n parameters: reverse mode needs 1 pass, forward mode needs n passes
- Start with ∂L/∂L = 1; at each node apply chain rule; for branching paths sum contributions

**ML/alignment connection:** This lesson makes backpropagation fully transparent as the mechanical application of the chain rule and Jacobian multiplication. The ReLU's piecewise derivative acts as a gate — inactive neurons contribute zero gradient, shaping which parameters get updated and creating path-dependent training dynamics essential to understand for alignment.

---

## Assessments

- **Exam 2A: Ordinary Differential Equations** (Lessons 14-18, Block A) — 90 min, 15 questions
- **Exam 2B: Multivariable Calculus** (Lessons 19-23, Block B) — 90 min, 15 questions
- **Exam 2C: Vector Calculus** (Lessons 24-27, 28, Block C) — 90 min, 15 questions
- **Exam 2D: Partial Differential Equations** (Lessons 29-33, Block D) — 90 min, 15 questions
- **Exam 2E: ML-Applied Calculus** (Lessons 34-36, Block E) — 60 min, 8 questions
