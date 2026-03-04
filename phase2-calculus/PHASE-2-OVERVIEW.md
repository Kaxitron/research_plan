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

### Lesson 16: Higher-Order Linear ODEs and Mechanical Vibrations

**Second-Order Linear ODEs with Constant Coefficients:**
- General form: ay'' + by' + cy = g(t)
- **Homogeneous case** (g(t) = 0): guess y = e^{rt}, get characteristic equation ar^2 + br + c = 0
- **Two distinct real roots** r_1, r_2: y = c_1 e^{r_1 t} + c_2 e^{r_2 t}
- **Repeated real root** r: y = (c_1 + c_2 t) e^{rt}
- **Complex conjugate roots** alpha +/- beta i: y = e^{alpha t}(c_1 cos(beta t) + c_2 sin(beta t))
- **Fundamental solutions and the Wronskian:** W(y_1, y_2) = y_1 y_2' - y_1' y_2; nonzero Wronskian guarantees linear independence

**Nonhomogeneous Equations:**
- **Method of undetermined coefficients:** guess the form of the particular solution based on g(t)
  - g(t) polynomial -> try polynomial of same degree
  - g(t) = e^{at} -> try Ae^{at}
  - g(t) = sin/cos -> try A cos + B sin
  - If the guess solves the homogeneous equation, multiply by t
- **Variation of parameters:** y_p = u_1 y_1 + u_2 y_2 where u_1' and u_2' are found from a 2x2 system
  - More general than undetermined coefficients — works for any g(t)
- **Superposition principle:** for linear equations, sum of solutions is a solution

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

**Higher-Order Linear ODEs:**
- nth-order: a_n y^{(n)} + ... + a_1 y' + a_0 y = g(t)
- Characteristic polynomial of degree n -> n roots -> n linearly independent solutions
- Same methods (undetermined coefficients, variation of parameters) extend to higher order
- **Reduction of order:** if one solution is known, find a second linearly independent one

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

### Lesson 19: Partial Derivatives, Gradients, and Directional Derivatives

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

### Lesson 20: The Multivariable Chain Rule and Jacobian Matrices

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

### Lesson 21: Multiple Integration and Change of Variables

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

### Lesson 22: Taylor Expansions and the Implicit Function Theorem

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

### Lesson 23: Optimization in Several Variables and Lagrange Multipliers

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
- In 3D: F = (P, Q, R) is conservative if and only if curl F = 0 (on a simply connected domain)
- **Simply connected domain:** no holes — every closed curve can be continuously shrunk to a point
- On domains with holes, curl = 0 is necessary but not sufficient

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

**Divergence:**
- div(F) = grad . F = partial P/partial x + partial Q/partial y (+ partial R/partial z in 3D)
- Measures net outward flux per unit area — sources (+) and sinks (-)
- Positive divergence = field spreading out; negative = field converging
- div(grad f) = grad^2 f = the Laplacian

**Curl:**
- 2D scalar curl: partial Q/partial x - partial P/partial y (measures local rotation)
- 3D vector curl: curl(F) = grad x F = (R_y - Q_z, P_z - R_x, Q_x - P_y)
- Measures local circulation/rotation of the field
- **Key identities:**
  - curl(grad phi) = 0 always — gradient fields have no rotation
  - div(curl F) = 0 always — curls have no divergence
  - If curl F = 0 on simply connected domain -> F is conservative

**The Laplacian:**
- grad^2 f = partial^2 f/partial x^2 + partial^2 f/partial y^2 + ... (sum of unmixed second partials)
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
- **Tangent vectors:** r_u and r_v span the tangent plane at each point
- **Normal vector:** n = r_u x r_v (cross product of tangent vectors)

**Surface Area:**
- Surface area = integral integral_D ||r_u x r_v|| du dv
- For graphs z = f(x,y): SA = integral integral sqrt(1 + f_x^2 + f_y^2) dA
- The factor ||r_u x r_v|| is the area magnification factor from parameter space to the surface

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

**The Divergence Theorem (Gauss's Theorem):**
- closed_integral integral_S F . dS = integral integral integral_E div(F) dV
- Total outward flux through closed surface S = integral of divergence over enclosed volume E
- Generalizes Green's theorem (flux form) to 3D
- Applications: Gauss's law in electrostatics, fluid flow conservation, heat flow

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

## Block D: Partial Differential Equations (Lessons 29-33) — Jason Bramburger PDE Course

### Lesson 29: Introduction to PDEs — Classification and the Heat Equation

**What Is a PDE:**
- A partial differential equation involves partial derivatives of a function of multiple variables
- **Classification by order:** the highest-order derivative present
- **Linear vs nonlinear:** linear if u and its derivatives appear linearly
- **Homogeneous vs nonhomogeneous:** presence of forcing terms

**Classification of Second-Order Linear PDEs:**
- **General form:** Au_{xx} + Bu_{xy} + Cu_{yy} + (lower order) = 0
- **Discriminant:** B^2 - 4AC determines type:
  - B^2 - 4AC < 0: **Elliptic** (e.g., Laplace/Poisson) — equilibrium, steady-state
  - B^2 - 4AC = 0: **Parabolic** (e.g., heat equation) — diffusion, smoothing
  - B^2 - 4AC > 0: **Hyperbolic** (e.g., wave equation) — propagation, waves
- Each type has fundamentally different behavior, solution methods, and boundary condition requirements

**The Heat Equation:**
- u_t = k grad^2 u (or u_t = k u_{xx} in 1D)
- Models diffusion of heat, chemical concentration, probability density
- **Key properties:**
  - **Smoothing:** rough initial data becomes smooth instantly
  - High-frequency modes decay fastest (exponential decay rate proportional to frequency^2)
  - **Maximum principle:** the maximum temperature occurs at t = 0 or on the boundary (no internal hot spots can form)
  - Solution via convolution with Gaussian kernel: Gaussian blurring over time
  - **Irreversible:** information is lost as time progresses (forward process is well-posed, backward is ill-posed)

**Boundary Conditions:**
- **Dirichlet:** u specified on boundary (fixed temperature)
- **Neumann:** partial u/partial n specified on boundary (fixed heat flux)
- **Robin (mixed):** linear combination of u and partial u/partial n on boundary
- **Periodic:** u and its derivatives match at opposite ends
- Well-posedness depends on matching the right boundary conditions to the PDE type

**Initial Conditions and Well-Posedness:**
- **Hadamard's conditions for well-posedness:** solution exists, is unique, and depends continuously on the data
- Heat equation needs initial condition u(x,0) = f(x) plus boundary conditions
- Ill-posed problems: small changes in data cause large changes in solution (e.g., backward heat equation)

**ML/alignment connection:** The heat equation is the mathematical foundation of the forward process in diffusion models (DDPM, score-based models). Adding noise to data is literally running the heat equation — it progressively destroys structure by diffusing information. Understanding the heat equation's smoothing and irreversibility properties explains why the reverse (denoising) process requires learning the score function.

---

### Lesson 30: Separation of Variables and Fourier Series

**Separation of Variables:**
- Ansatz: assume u(x,t) = X(x)T(t) — the solution factors into spatial and temporal parts
- Substitution into the PDE yields two ODEs (one in x, one in t) linked by a separation constant
- Boundary conditions determine the allowed values of the separation constant (eigenvalue problem)
- General solution is a (possibly infinite) superposition of separated solutions

**Eigenvalue Problems (Sturm-Liouville Theory):**
- X'' + lambda X = 0 with boundary conditions -> eigenvalues lambda_n and eigenfunctions X_n
- Common cases:
  - Dirichlet (X(0) = X(L) = 0): X_n = sin(n pi x / L), lambda_n = (n pi / L)^2
  - Neumann (X'(0) = X'(L) = 0): X_n = cos(n pi x / L), lambda_n = (n pi / L)^2
  - Periodic: X_n = sin, cos with lambda_n = (2n pi / L)^2
- Eigenfunctions form a complete orthogonal set — any reasonable function can be expanded in them

**Fourier Series:**
- f(x) = a_0/2 + sum_{n=1}^{infinity} [a_n cos(n pi x / L) + b_n sin(n pi x / L)]
- **Fourier coefficients:** a_n = (2/L) integral_0^L f(x) cos(n pi x / L) dx, similarly for b_n
- **Orthogonality** of sin and cos functions is the key property that makes Fourier series work
- **Convergence:** pointwise (at continuity points), L^2 (in mean-square), uniform (for smooth functions)
- **Gibbs phenomenon:** overshoot near discontinuities that doesn't disappear as more terms are added (but the overshoot narrows)
- **Parseval's theorem:** energy in physical space = energy in frequency space (sum of squared coefficients)

**Complex Fourier Series:**
- f(x) = sum_{n=-infinity}^{infinity} c_n e^{i n pi x / L}
- c_n = (1/2L) integral_{-L}^{L} f(x) e^{-i n pi x / L} dx
- More compact notation; connects naturally to the Fourier transform

**Solving the Heat Equation with Fourier Series:**
- Expand initial condition in eigenfunctions: f(x) = sum b_n sin(n pi x / L)
- Each mode evolves independently: u(x,t) = sum b_n e^{-k(n pi/L)^2 t} sin(n pi x / L)
- High-frequency modes (large n) decay exponentially faster — this is the mathematical basis for smoothing

**ML/alignment connection:** Fourier analysis is the mathematical foundation for understanding what neural networks learn at different scales. The spectral bias phenomenon — networks learn low-frequency components before high-frequency ones — directly mirrors how the heat equation damps high frequencies faster. Fourier features (random Fourier features, positional encodings in transformers) explicitly leverage this decomposition. Parseval's theorem connects time/spatial-domain and frequency-domain representations of signals.

---

### Lesson 31: The Wave Equation — Vibrations and d'Alembert

**The Wave Equation:**
- u_{tt} = c^2 u_{xx} (1D), u_{tt} = c^2 grad^2 u (higher dimensions)
- Models vibrating strings, membranes, sound waves, electromagnetic waves
- Second-order in time (vs first-order for heat) -> qualitatively different behavior

**d'Alembert's Solution (Infinite Domain):**
- General solution: u(x,t) = f(x - ct) + g(x + ct) — superposition of right- and left-traveling waves
- f and g determined by initial conditions u(x,0) and u_t(x,0)
- **d'Alembert's formula:** u(x,t) = (1/2)[phi(x-ct) + phi(x+ct)] + (1/2c) integral_{x-ct}^{x+ct} psi(s) ds
  - where phi = initial displacement, psi = initial velocity

**Key Properties of the Wave Equation:**
- **Finite propagation speed:** disturbances travel at speed c (contrast with heat equation's infinite speed)
- **No smoothing:** sharp features propagate indefinitely (contrast with heat equation's diffusion)
- **Energy conservation:** total energy (kinetic + potential) is conserved
- **Reversible:** time-reversal symmetry (contrast with heat equation's irreversibility)
- **Superposition principle:** waves pass through each other without interaction

**Separation of Variables for the Wave Equation:**
- u(x,t) = X(x)T(t) yields X'' + lambda X = 0 and T'' + c^2 lambda T = 0
- Standing waves: X_n(x) sin(omega_n t) or X_n(x) cos(omega_n t)
- Natural frequencies: omega_n = c n pi / L (harmonics)
- General solution as superposition of standing waves (normal modes)

**Vibrating Strings and Membranes:**
- **Boundary conditions:** fixed ends, free ends, mixed
- **Harmonics and overtones:** fundamental frequency and integer multiples
- 2D wave equation on rectangular/circular domains
- **Bessel functions** arise for circular geometry

**Characteristics:**
- **Characteristic curves** x +/- ct = const along which information propagates
- The wave equation is hyperbolic, and characteristics define the domain of dependence and range of influence
- Contrast with parabolic (heat) which has infinite speed of propagation

**ML/alignment connection:** The wave equation's finite propagation speed and energy conservation contrast sharply with the heat equation's diffusion and dissipation. This distinction appears in neural network training: some signal propagation behaves wave-like (preserving information across layers, as in ResNets and skip connections) while other phenomena are diffusion-like (gradient smoothing, noise averaging). Understanding both regimes is essential for designing architectures that preserve or transform information appropriately.

---

### Lesson 32: Helmholtz, Laplace, and Transport Equations

**Laplace's Equation and Harmonic Functions:**
- grad^2 u = 0 — the prototypical elliptic PDE
- Solutions are called harmonic functions
- **Maximum principle:** harmonic functions attain their max and min on the boundary, never in the interior
- **Mean value property:** u at any point = average of u on any surrounding sphere/circle
- **Uniqueness:** given boundary values, the solution is unique
- Solving by separation of variables on rectangles, circles (Fourier series in angular variable), spheres (spherical harmonics)
- **Poisson's equation:** grad^2 u = f — the nonhomogeneous version; Green's functions provide solutions

**The Helmholtz Equation:**
- grad^2 u + k^2 u = 0 — the spatial part of the wave equation after separating time
- Eigenvalue problem: finding frequencies and mode shapes
- Arises in acoustics, electromagnetics, quantum mechanics
- Solutions depend on geometry: rectangular -> sines/cosines, circular -> Bessel functions, spherical -> spherical harmonics

**The Transport Equation:**
- u_t + c u_x = 0 — the simplest first-order PDE
- Solution: u(x,t) = f(x - ct) — the initial profile translates at speed c
- Method of characteristics: solve along curves dx/dt = c
- Foundation for understanding more complex hyperbolic PDEs
- **Nonlinear transport (Burgers' equation):** u_t + u u_x = 0 — wave steepening and shock formation
- Adding viscosity: u_t + u u_x = nu u_{xx} (viscous Burgers') — competition between nonlinear steepening and diffusive smoothing

**Green's Functions:**
- The response to a point source (delta function forcing)
- Solution to Lu = f can be written as u(x) = integral G(x, xi) f(xi) d(xi)
- Green's function encodes the geometry and boundary conditions of the domain
- **Fundamental solutions:** Green's functions on infinite domains (no boundary)
  - Laplace: G ~ ln|x-xi| (2D), G ~ 1/|x-xi| (3D)
  - Heat: G = Gaussian kernel
  - Wave: G supported on characteristic cones

**Special Functions Arising in PDEs:**
- **Bessel functions:** J_n(x), Y_n(x) — solutions to Bessel's equation, arise in circular/cylindrical geometry
- **Legendre polynomials:** P_n(x) — arise in spherical geometry
- **Spherical harmonics:** Y_l^m(theta, phi) — eigenfunctions of the Laplacian on the sphere

**ML/alignment connection:** Laplace's equation and harmonic functions are the mathematical basis for understanding equilibrium states and steady-state solutions. The mean value property of harmonic functions is analogous to how well-generalized models produce predictions that are "averages" over local neighborhoods in input space. Green's functions provide the theoretical framework for kernel methods in ML — a kernel K(x, x') is essentially a Green's function, and Gaussian processes can be viewed through this lens.

---

### Lesson 33: PDEs in ML — Diffusion Models, Numerical Methods, and Score Matching

**Diffusion Models and the Forward Process:**
- Forward process: dx = f(x,t)dt + g(t)dB_t — progressive noise addition via an SDE
- This is equivalent to running a heat-like equation on the probability density
- Noise schedule: how quickly structure is destroyed (linear, cosine, etc.)
- At t = T: data distribution -> approximately Gaussian (all structure erased)

**The Reverse Process and Score Matching:**
- **Score function:** s(x,t) = grad_x log p_t(x) — the gradient of the log probability density
- **Anderson's reverse-time SDE:** dx = [f(x,t) - g(t)^2 s(x,t)] dt + g(t) dB_t_bar
- The reverse SDE requires knowing the score function at all times
- **Score matching:** train a neural network s_theta(x,t) to approximate the score
  - **Denoising score matching:** the score at noise level sigma equals E[-(x - x_clean)/sigma^2 | x]
  - **Sliced score matching:** project to 1D for computational efficiency
  - Training objective: minimize E[||s_theta(x,t) - grad_x log p_t(x)||^2]

**Probability Flow ODE:**
- dx/dt = f(x,t) - (1/2)g(t)^2 s(x,t) — deterministic ODE with same marginal distributions as the SDE
- Enables: exact likelihood computation, deterministic sampling, interpolation in latent space
- Solved with standard ODE solvers (Euler, RK45, adaptive methods)

**Fokker-Planck Equation:**
- partial p/partial t = -div(f p) + (1/2) g^2 grad^2 p
- Describes how the probability density p(x,t) evolves under the SDE
- Drift term (f) transports probability; diffusion term (g^2 grad^2) spreads it
- **Stationary distribution:** setting partial p/partial t = 0 gives the equilibrium density
- For gradient flow with noise: p_eq proportional to exp(-L(x)/T) (Boltzmann distribution)

**Numerical Methods for PDEs:**
- **Finite differences:** discretize derivatives on a grid
  - Forward/backward/central differences for first derivatives
  - Central difference for second derivatives
  - Stability constraints: CFL condition for wave equation, von Neumann analysis for heat equation
- **Finite elements:** approximate solution as sum of basis functions on a mesh
- **Spectral methods:** expand in Fourier modes or other global basis functions — exponential convergence for smooth solutions
- **Physics-Informed Neural Networks (PINNs):** embed PDE constraints in the loss function
  - Loss = data fitting + PDE residual + boundary condition residual
  - Mesh-free, can handle complex geometries, but training can be challenging

**Stochastic Dynamics in Training:**
- **SGD as SDE:** dW = -grad L dt + sqrt(eta/B) dB_t (gradient flow + mini-batch noise)
- **Noise covariance:** C = (eta/B) Sigma where Sigma is the gradient noise covariance
- **Escape from local minima:** noise enables exploration of the loss landscape
- **Sharp vs flat minima:** SGD noise preferentially destabilizes sharp minima -> implicit bias toward flat (generalizing) minima
- **Edge of stability:** training at eta ~ 2/lambda_max — the top Hessian eigenvalue self-tunes to match the learning rate

**Neural Operators and PDE Solvers:**
- **DeepONet, Fourier Neural Operator (FNO):** learn solution operators for families of PDEs
- Map initial/boundary conditions to solutions without re-solving from scratch
- Fourier Neural Operator: learn in Fourier space, capturing multi-scale interactions efficiently
- Potential for accelerating scientific computing by orders of magnitude

**ML/alignment connection:** Diffusion models (DDPM, score-based generative models) are the direct application of PDE theory to generative AI. The entire framework — forward diffusion as a heat equation, reverse generation as solving a learned SDE/ODE, score matching as the training objective — is built on the PDE concepts from this block. Understanding the mathematics ensures principled design choices in noise schedules, architectures, and sampling strategies. For alignment: understanding diffusion models mathematically is necessary for mechanistic interpretability of generative models and for understanding the training dynamics of these increasingly important systems.

---

## Block E: ML-Applied Calculus (Lessons 34-36)

### Lesson 34: Matrix Calculus — Bridging to Backpropagation

**Scalar-by-Vector Derivatives:**
- grad f for f: R^n -> R — the gradient is a vector of partial derivatives
- grad (a^T x) = a
- grad (x^T A x) = (A + A^T)x (= 2Ax when A is symmetric)
- grad (||x||^2) = 2x

**Vector-by-Vector Derivatives (Jacobians):**
- For F: R^n -> R^m, J_{ij} = partial F_i / partial x_j
- J(Ax) = A
- J(sigma(Wx + b)) = diag(sigma'(Wx + b)) W — the Jacobian of a neural network layer
- **Numerator vs denominator layout conventions** — be consistent within a derivation

**Matrix-by-Matrix and Trace Derivatives:**
- partial/partial X tr(AX) = A^T
- partial/partial X tr(X^T A X) = (A + A^T)X
- partial/partial X tr(AXB) = A^T (partial/partial X)^T B^T — use the trace trick
- **The trace trick:** scalar = tr(scalar); rearrange using tr(ABC) = tr(CAB) = tr(BCA)

**Computation Graphs and Automatic Differentiation:**
- Neural networks as directed acyclic graphs (DAGs) of differentiable operations
- Each node: stores value (forward pass) and local Jacobian (backward pass)
- **Forward-mode autodiff:** propagate derivatives from inputs to outputs — efficient when few inputs
- **Reverse-mode autodiff (backpropagation):** propagate derivatives from outputs to inputs — efficient when few outputs (one loss)
- **For a network with n parameters and 1 loss: reverse mode costs O(1) per parameter, forward mode costs O(n)**
- Building a tiny autograd engine (micrograd-style): define Value objects with data and grad, implement backward() for each operation

**The Backward Pass in Detail:**
- Start with dL/dL = 1
- At each node, apply chain rule: dL/dx = dL/dy * dy/dx (local Jacobian)
- For branching paths: sum the contributions (multivariate chain rule)
- Gradient accumulation: each parameter's gradient is the sum over all paths from that parameter to the loss

**Practical Considerations:**
- Gradient checkpointing: trade compute for memory by recomputing intermediate values
- Mixed precision: float16 forward, float32 gradients
- Gradient clipping: cap ||grad|| to prevent exploding gradients

**ML/alignment connection:** Matrix calculus is the language in which backpropagation is written. Every neural network training run computes exactly these derivatives, millions of times. Understanding the Jacobian structure of each layer type (linear, activation, attention) is necessary for diagnosing training pathologies (vanishing/exploding gradients) and for mechanistic interpretability — understanding what gradients tell us about what the network has learned.

---

### Lesson 35: Optimization Algorithms — SGD through Adam

**Vanilla Gradient Descent:**
- W <- W - eta grad L(W)
- Converges for convex problems with appropriate learning rate
- For non-convex: converges to a critical point (not necessarily a minimum)

**Stochastic Gradient Descent (SGD):**
- Use mini-batch gradient estimate: g_t = (1/B) sum_{i in batch} grad L_i(W)
- E[g_t] = grad L(W) — unbiased estimator of the full gradient
- Variance of g_t proportional to 1/B
- **Generalization benefits:** SGD noise acts as implicit regularization, biasing toward flat minima

**Learning Rate Schedules:**
- **Step decay:** reduce eta by a factor every N epochs
- **Cosine annealing:** eta_t = eta_min + (1/2)(eta_max - eta_min)(1 + cos(pi t / T))
- **Linear warmup:** gradually increase eta from 0 to target over first N steps
- **Warmup + cosine decay:** the standard schedule for transformer training
- **Cyclical learning rates:** oscillate eta to escape local minima
- **One-cycle policy:** warmup -> high LR -> cooldown

**Momentum Methods:**
- **Classical momentum:** v_t = beta v_{t-1} + grad L(W_t); W_{t+1} = W_t - eta v_t
  - Accumulates velocity in consistent gradient directions; damps oscillations
  - Equivalent to a damped second-order ODE: heavy ball method
- **Nesterov accelerated gradient (NAG):** evaluate gradient at the look-ahead position W - beta v
  - Provides "corrective" step — better theoretical convergence for convex problems
  - Nesterov achieves optimal convergence rate O(1/t^2) for convex problems (vs O(1/t) for vanilla GD)

**Adaptive Learning Rate Methods:**
- **AdaGrad:** divide each parameter's learning rate by sqrt(sum of squared past gradients)
  - Good for sparse features; bad for non-sparse (learning rate decays to zero)
- **RMSProp:** fix AdaGrad with exponential moving average: v_t = rho v_{t-1} + (1-rho) g_t^2
  - Keeps a running average, so learning rate doesn't vanish
- **Adam (Adaptive Moment Estimation):**
  - First moment (mean): m_t = beta_1 m_{t-1} + (1 - beta_1) g_t
  - Second moment (uncentered variance): v_t = beta_2 v_{t-1} + (1 - beta_2) g_t^2
  - **Bias correction:** m_hat = m_t / (1 - beta_1^t), v_hat = v_t / (1 - beta_2^t)
  - Update: W_{t+1} = W_t - eta m_hat / (sqrt(v_hat) + epsilon)
  - Default hyperparameters: beta_1 = 0.9, beta_2 = 0.999, epsilon = 1e-8
- **AdamW:** decouple weight decay from the adaptive learning rate
  - Adam: grad includes the L2 penalty -> adapted differently for each parameter (incorrect)
  - AdamW: apply weight decay directly to W, not through the gradient -> correct L2 regularization
  - W_{t+1} = W_t - eta (m_hat / (sqrt(v_hat) + epsilon) + lambda W_t)

**Second-Order Methods (Conceptual):**
- **Newton's method:** W <- W - H^{-1} grad L — use curvature to take better steps
  - Prohibitively expensive: H is n x n where n = number of parameters
- **Natural gradient:** use Fisher information matrix instead of Hessian
  - Accounts for geometry of the probability distribution space
- **K-FAC:** Kronecker-factored approximate curvature — practical approximation to natural gradient
- **L-BFGS:** limited-memory quasi-Newton method — approximates H^{-1} from recent gradient history; works well for small-to-medium problems

**ML/alignment connection:** The choice of optimizer profoundly affects what solution a neural network converges to, not just how fast it gets there. Adam's adaptive per-parameter learning rates effectively precondition the gradient, making optimization less sensitive to the loss landscape's condition number. For alignment research: understanding how different optimizers explore the loss landscape differently is crucial because the minimum you converge to determines the model's generalization behavior and implicit biases.

---

### Lesson 36: Loss Landscapes, Gradient Flow, and Training Dynamics

**Loss Landscapes:**
- The loss function L(W) as a surface over all parameters (typically millions/billions of dimensions)
- **Landscape features:** local minima, global minima, saddle points, plateaus, ravines
- **In high dimensions: saddle points dominate, not local minima** — random matrix theory shows that critical points with all-positive Hessian eigenvalues are exponentially rare
- Hessian eigenvalue spectrum: bulk near zero (flat directions) + a few large eigenvalues (sharp directions)
- **Loss landscape visualization:** low-dimensional projections (filter normalization, random directions) — informative but limited

**Gradient Flow Analysis:**
- dW/dt = -grad L(W) — the continuous-time limit of gradient descent
- **Loss as Lyapunov function:** dL/dt = -||grad L||^2 <= 0 — loss always decreases along gradient flow
- One-line proof: dL/dt = grad L . (dW/dt) = grad L . (-grad L) = -||grad L||^2
- **Convergence to critical points:** gradient flow converges to the set where grad L = 0
- **Stability of critical points:** determined by eigenvalues of the Hessian at that point

**Implicit Regularization:**
- Gradient descent from small initialization -> minimum-norm solution (for linear models)
- For deep linear networks -> biases toward low-rank solutions (matrix factorization)
- **Learning rate as temperature:** larger eta -> more noise -> escapes sharp minima, prefers flat ones
- **SGD noise:** variance sigma^2 proportional to eta/B (noise scales with learning rate / batch size)
- **Flat minima generalize better** (PAC-Bayes bound: flat minima are robust to weight perturbation)
- **Label noise, dropout, data augmentation** as explicit regularization complementing implicit effects

**Phase Transitions in Training:**
- Sudden qualitative changes in loss or capability during training
- **Grokking:** memorization phase -> sudden generalization long after training loss reaches zero
- **Emergent capabilities:** skills that appear abruptly at certain model scales
- **Mechanistic interpretation:** phase transitions correspond to the network discovering and committing to particular computational strategies (circuits)
- **SLT perspective:** RLCT (Real Log Canonical Threshold) governs the geometry of singularities in the loss landscape; phase transitions correspond to transitions between singular regions
- **Local Learning Coefficient (LLC):** an estimable version of the RLCT that tracks phase transitions during training in real time

**Edge of Stability:**
- Training at eta ~ 2/lambda_max: the top Hessian eigenvalue hovers near 2/eta
- **Progressive sharpening:** early in training, lambda_max grows until it hits 2/eta
- **Self-stabilization:** after reaching the edge, the network adjusts to keep lambda_max ~ 2/eta
- This is an inherently discrete-time effect — gradient flow (continuous) cannot exhibit it
- Implies gradient descent at finite learning rate explores a different set of minima than infinitesimal learning rate

**Double Descent and Interpolation:**
- **Classical bias-variance tradeoff:** increase model complexity -> train error decreases, test error U-shaped
- **Modern double descent:** test error goes down, up (interpolation threshold), then down again as complexity increases further
- **Epoch-wise double descent:** test error shows similar non-monotonic behavior over training time
- Reconciliation: overparameterized models have many interpolating solutions; optimization selects simple (generalizing) ones

**Condition Number and Optimization Geometry:**
- Condition number kappa = lambda_max / lambda_min of the Hessian
- High kappa -> elongated valleys -> gradient descent zigzags
- **Preconditioning:** multiply gradient by H^{-1} (or approximation) to equalize curvature
- Adam's per-parameter scaling is a diagonal approximation to preconditioning
- **Loss landscape shaping:** batch normalization, skip connections, careful initialization all improve conditioning

**ML/alignment connection:** Understanding loss landscapes and training dynamics is essential for alignment because the properties of the minimum a model converges to determine its behavior. Sharp minima may correspond to brittle, non-generalizing solutions, while flat minima tend to be more robust. Phase transitions (grokking, emergent capabilities) are directly relevant to alignment — sudden capability jumps could include dangerous capabilities. Singular Learning Theory provides a mathematical framework for predicting and understanding these transitions, connecting the geometry of the loss landscape to the model's learned structure.

---

## Assessments

- **Exam 2A: Ordinary Differential Equations** (Lessons 14-18, Block A) — 90 min, 15 questions
- **Exam 2B: Multivariable Calculus** (Lessons 19-23, Block B) — 90 min, 15 questions
- **Exam 2C: Vector Calculus** (Lessons 24-27, 28, Block C) — 90 min, 15 questions
- **Exam 2D: Partial Differential Equations** (Lessons 29-33, Block D) — 90 min, 15 questions
- **Exam 2E: ML-Applied Calculus** (Lessons 34-36, Block E) — 60 min, 8 questions
