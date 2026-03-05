# Lesson 30: Separation of Variables and Fourier Series

[<- Previous](lesson-29-intro-pdes.md) | [Back to TOC](../README.md) | [Next: The Wave Equation ->](lesson-31-wave-equation.md)

---

Separation of variables is the fundamental analytical technique for solving linear PDEs. The core idea is beautifully simple: assume the solution factors as a product of single-variable functions, u(x,t) = X(x)T(t), and substitute into the PDE. Because the left side depends only on t and the right side only on x, both must equal the same constant -- the separation constant. One PDE becomes two ODEs, each solvable with standard techniques from Phase 2 Block B.

Fourier series emerge naturally from this process. When you impose boundary conditions, the spatial ODE becomes an eigenvalue problem -- only certain frequencies (eigenvalues) are allowed. The general solution is a superposition of these eigenfunctions, and the coefficients are determined by the initial condition via Fourier's formulas. The Fourier series of the initial condition decomposes it into sinusoidal modes, and each mode evolves independently: in the heat equation, high-frequency modes decay exponentially faster than low-frequency ones. This frequency-dependent decay is why diffusion blurs fine details first.

The deeper mathematical structure here is the Sturm-Liouville eigenvalue problem, which generalizes the matrix eigendecomposition from Phase 1 to function spaces. Just as a symmetric matrix has orthogonal eigenvectors that form a basis for R^n, a Sturm-Liouville operator has orthogonal eigenfunctions that form a basis for a function space. This is the bridge between finite-dimensional linear algebra and the infinite-dimensional analysis that underpins PDE theory, spectral methods, and functional analysis in ML.

## Core Learning

- Separation of variables: assume u(x,t) = X(x)T(t), substitute into the PDE, separate variables to get two ODEs linked by a separation constant
- For the heat equation: T'(t) = -alpha * lambda * T(t) and X''(x) = -lambda * X(x), where lambda is the separation constant (eigenvalue)
- Boundary conditions on u translate to boundary conditions on X, which select the allowed eigenvalues lambda_n = (n*pi/L)^2 and eigenfunctions X_n(x) = sin(n*pi*x/L)
- Fourier series: any "reasonable" function on [0, L] can be written as a sum of sines and cosines with computable coefficients
- Fourier coefficients are computed via inner products (integrals) -- this is orthogonal projection in function space, exactly like projecting onto eigenvectors in linear algebra
- Convergence: Fourier series converge in L^2 norm; pointwise convergence at continuity points; Gibbs phenomenon at discontinuities (overshooting by ~9%)
- Sturm-Liouville theory: -(p(x)y')' + q(x)y = lambda * w(x)y generalizes the eigenvalue equation; eigenfunctions are orthogonal with respect to weight w(x)
- The heat equation solution: each Fourier mode decays as exp(-alpha * (n*pi/L)^2 * t) -- high frequencies decay fastest

## Watch -- Primary

- **Jason Bramburger -- PDEs Course** (Separation of variables and Fourier series sections)
  - https://www.youtube.com/@jasonbramburger
  - *Systematic treatment of the separation technique applied to the heat equation.*

## Watch -- Secondary

- **3Blue1Brown -- "But what is a Fourier series?"**
  - https://www.youtube.com/watch?v=r6sGWTCMz2k
  - *The visual intuition for Fourier decomposition as "wrapping" a function around a circle and measuring the center of mass. Essential viewing.*

## Read

- **Haberman, *Applied Partial Differential Equations***, Ch. 2-3: separation of variables, Fourier series
- **Strang, *Introduction to Linear Algebra***, Section on function spaces and Fourier series (connects to Phase 1 linear algebra)

## Key Equations

**Separation ansatz:**
$$u(x,t) = X(x) \cdot T(t)$$

**Fourier series** on $[0, L]$:
$$f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos\!\left(\frac{n\pi x}{L}\right) + b_n \sin\!\left(\frac{n\pi x}{L}\right) \right]$$

**Fourier coefficients:**
$$a_n = \frac{2}{L} \int_0^L f(x) \cos\!\left(\frac{n\pi x}{L}\right) dx, \qquad b_n = \frac{2}{L} \int_0^L f(x) \sin\!\left(\frac{n\pi x}{L}\right) dx$$

**Heat equation solution (Dirichlet BCs on [0, L]):**
$$u(x,t) = \sum_{n=1}^{\infty} b_n \sin\!\left(\frac{n\pi x}{L}\right) e^{-\alpha (n\pi/L)^2 t}$$

**Sturm-Liouville eigenvalue problem:**
$$-\big(p(x)\, y'\big)' + q(x)\, y = \lambda\, w(x)\, y$$

**Orthogonality of eigenfunctions:**
$$\int_a^b y_m(x)\, y_n(x)\, w(x)\, dx = 0 \quad \text{for } m \neq n$$

## ML and Alignment Connection

Fourier analysis decomposes signals into frequency components -- this is exactly what spectral methods in ML do. Graph neural networks use the graph Fourier transform (eigenvectors of the graph Laplacian) to define convolutions on graphs. Transformer positional encodings use sinusoidal bases directly borrowed from Fourier series. The spectral bias of neural networks -- the empirical observation that networks learn low-frequency components before high-frequency ones -- mirrors the heat equation's frequency-dependent decay.

Sturm-Liouville eigenvalue problems generalize the matrix eigendecomposition from Phase 1 to function spaces. Just as PCA finds the principal eigenvectors of a covariance matrix, kernel PCA and spectral methods find eigenfunctions of integral operators. The orthogonality and completeness of Sturm-Liouville eigenfunctions is the infinite-dimensional version of the spectral theorem -- the mathematical foundation for all spectral methods in ML, from kernel methods to diffusion maps to spectral clustering.

For alignment: understanding which frequencies a model captures first (spectral bias) tells you about the order in which it learns features. If safety-relevant features are high-frequency (subtle, context-dependent), they may be learned last -- or not at all if training stops too early.
