# Lesson 31: Eigenvalue Problems and Sturm-Liouville Theory

[<- Previous](lesson-30-separation-fourier.md) | [Back to TOC](../README.md) | [Next: Helmholtz Equation, Fourier Transform, and Infinite Domains ->](lesson-32-helmholtz-laplace.md)

---

Every time you apply separation of variables to a PDE, the spatial part becomes an eigenvalue problem: find the values of lambda for which a nontrivial solution exists satisfying the boundary conditions. In Lessons 29-30, these were simple cases -- X'' + lambda*X = 0 on uniform domains with constant coefficients. This lesson generalizes to the full Sturm-Liouville framework, which handles variable coefficients, non-uniform media, and weighted inner products. The theory guarantees that eigenvalues are real, eigenfunctions are orthogonal, and any reasonable function can be expanded in the eigenfunctions -- exactly the properties needed for separation of variables to work on more complex problems.

Sturm-Liouville theory is the infinite-dimensional version of the spectral theorem from Phase 1 linear algebra. Just as a symmetric matrix has real eigenvalues and orthogonal eigenvectors forming a basis for R^n, a Sturm-Liouville operator has real eigenvalues and orthogonal eigenfunctions forming a basis for a function space. This bridge between finite-dimensional linear algebra and infinite-dimensional analysis underpins all spectral methods in ML, from kernel methods to diffusion maps to spectral clustering.

## Core Learning

### Eigenvalue Problems in PDEs (Video: L22)

- When separation of variables is applied to any linear PDE, the spatial part becomes an eigenvalue problem of the form L[X] = lambda * X, where L is a differential operator and lambda is the separation constant
- The eigenvalues lambda determine the allowed frequencies/modes; the eigenfunctions X_n determine the spatial shapes of those modes
- Different PDEs and different boundary conditions produce different eigenvalue problems, but the underlying structure is always the same: find lambda and X_n such that L[X_n] = lambda_n * X_n with X_n satisfying the BCs
- The general theory (Sturm-Liouville) guarantees key properties: real eigenvalues, orthogonal eigenfunctions, completeness -- these are not accidents of simple examples but structural features of self-adjoint operators

### Sturm-Liouville Theory (Videos: L23, L25)

- **Sturm-Liouville eigenvalue problem:** -(p(x)*y')' + q(x)*y = lambda * w(x) * y on [a, b] with boundary conditions at x = a and x = b
- p(x) > 0, w(x) > 0 (weight function), q(x) >= 0; these are the conditions for a regular Sturm-Liouville problem
- **Key properties** (analogous to the spectral theorem for symmetric matrices):
  - All eigenvalues are real: lambda_1 < lambda_2 < lambda_3 < ...
  - Eigenvalues form an increasing sequence tending to infinity
  - Eigenfunctions corresponding to distinct eigenvalues are orthogonal with respect to the weight function w(x): integral_a^b y_m(x) * y_n(x) * w(x) dx = 0 for m != n
  - The eigenfunctions form a complete set -- any "reasonable" function can be expanded as f(x) = sum c_n * y_n(x) (generalized Fourier series)
- **Sturm-Liouville eigenvalues and eigenfunctions:** for specific choices of p, q, w, and BCs, one recovers all the classical eigenvalue problems -- the standard Fourier modes (p=1, q=0, w=1), Bessel functions (cylindrical geometry), Legendre polynomials (spherical geometry), and many others
- The simple eigenvalue problems from Lessons 29-30 (X'' + lambda*X = 0 with Dirichlet/Neumann/Periodic BCs) are all special cases of Sturm-Liouville with p(x) = 1, q(x) = 0, w(x) = 1

### Heat Flow in a Nonuniform Rod (Video: L24)

- A rod with spatially varying thermal conductivity k(x) and heat capacity c(x) leads to the heat equation c(x)*rho(x)*u_t = (k(x)*u_x)_x -- the coefficients are no longer constant
- Separation of variables u(x,t) = X(x)*T(t) yields -(k(x)*X')' = lambda * c(x)*rho(x) * X -- a Sturm-Liouville problem with p(x) = k(x) and w(x) = c(x)*rho(x)
- The eigenvalues and eigenfunctions depend on the material properties; temperature modes decay at rates proportional to their eigenvalues, just as in the uniform case, but the spatial shapes are no longer simple sines and cosines
- This is the PDE analogue of how variable step sizes or layer-dependent learning rates modify the modes of gradient descent

### The Rayleigh Quotient (Video: L26)

- **Rayleigh quotient:** R[y] = (integral_a^b [p(x)*(y')^2 + q(x)*y^2] dx) / (integral_a^b w(x)*y^2 dx) -- a functional that takes a trial function and returns a scalar
- The Rayleigh quotient is minimized by the first eigenfunction y_1, and R[y_1] = lambda_1 (the smallest eigenvalue)
- Among all functions orthogonal to y_1, R is minimized by y_2 with R[y_2] = lambda_2, and so on -- this is the min-max characterization of eigenvalues
- Provides upper bounds on eigenvalues: plugging any trial function into R gives an upper bound on lambda_1 (variational principle)
- This is the infinite-dimensional version of the Rayleigh quotient for matrices from Phase 1: R(x) = x^T*A*x / x^T*x
- Directly connects to PCA (finding directions of maximum variance), spectral clustering, and variational methods in ML

### Vibrations of a Nonuniform String (Video: L27)

- A vibrating string with spatially varying density rho(x) and tension tau(x) leads to rho(x)*u_{tt} = (tau(x)*u_x)_x
- Separation of variables yields -(tau(x)*X')' = lambda * rho(x) * X -- a Sturm-Liouville problem for the spatial modes
- Natural frequencies are omega_n = sqrt(lambda_n); the mode shapes depend on how mass and tension are distributed along the string
- A string with more mass in one region vibrates differently from a uniform string -- the heavy section moves less, the light section moves more
- This physical problem provides intuition for how non-uniform scaling affects the spectral decomposition of operators

### Eigenfunction Expansions (Video: L28)

- **Eigenfunction expansion:** given a Sturm-Liouville problem with eigenfunctions y_n(x), any function f(x) can be written as f(x) = sum c_n * y_n(x), where c_n = integral_a^b f(x) * y_n(x) * w(x) dx / integral_a^b y_n(x)^2 * w(x) dx
- This generalizes Fourier series (which is the special case where eigenfunctions are sines/cosines) to arbitrary Sturm-Liouville eigenfunctions
- Used to solve PDEs on non-uniform domains or with variable coefficients: expand the initial/boundary data in eigenfunctions, then each mode evolves independently according to its eigenvalue
- Convergence properties parallel Fourier series: L^2 convergence is guaranteed; pointwise and uniform convergence depend on smoothness

### Inhomogeneous Boundary Conditions (Video: L29)

- **Inhomogeneous boundary conditions** (e.g., u(0,t) = A, u(L,t) = B where A, B are nonzero) cannot be directly handled by eigenfunction expansion, because eigenfunctions satisfy homogeneous BCs
- **Strategy:** decompose u(x,t) = v(x) + w(x,t), where v(x) is the steady-state solution satisfying the inhomogeneous BCs (i.e., nabla^2 v = 0 with v(0) = A, v(L) = B), and w(x,t) satisfies the PDE with homogeneous BCs
- The initial condition for w is w(x,0) = f(x) - v(x), which can be expanded in eigenfunctions as usual
- Time-dependent inhomogeneous BCs require more sophisticated techniques (e.g., subtracting a function of both x and t that satisfies the BCs)
- This decomposition strategy -- splitting a problem into an easier part (steady-state) and a remainder (transient) -- is a general problem-solving pattern that appears throughout applied mathematics and ML

## Watch -- Primary

- **Jason Bramburger -- PDEs Course** (Lectures 22-29)
  - https://www.youtube.com/playlist?list=PLXsDp0z6VWFQJ6BY1O6Hz5XX2ppgGvEAu
  - L22: Eigenvalue Problems in PDEs
  - L23: Sturm-Liouville Theory
  - L24: Heat Flow in a Nonuniform Rod
  - L25: Sturm-Liouville Eigenvalues and Eigenfunctions
  - L26: The Rayleigh Quotient
  - L27: Vibrations of a Nonuniform String
  - L28: Eigenfunction Expansions
  - L29: Inhomogeneous Boundary Conditions

## Read

- **Haberman, *Applied Partial Differential Equations***, Ch. 5: Sturm-Liouville eigenvalue problems
- **Strang, *Introduction to Linear Algebra***, Section on function spaces (connects to Phase 1 spectral theorem)

## Key Equations

**Sturm-Liouville eigenvalue problem:**
$$-\big(p(x)\, y'\big)' + q(x)\, y = \lambda\, w(x)\, y$$

**Orthogonality of eigenfunctions:**
$$\int_a^b y_m(x)\, y_n(x)\, w(x)\, dx = 0 \quad \text{for } m \neq n$$

**Rayleigh quotient:**
$$R[y] = \frac{\int_a^b \left[ p(x)\, (y')^2 + q(x)\, y^2 \right] dx}{\int_a^b w(x)\, y^2 \, dx}$$

**Eigenfunction expansion:**
$$f(x) = \sum_{n=1}^{\infty} c_n \, y_n(x), \qquad c_n = \frac{\int_a^b f(x)\, y_n(x)\, w(x)\, dx}{\int_a^b y_n(x)^2\, w(x)\, dx}$$

**Inhomogeneous BC decomposition:**
$$u(x,t) = v(x) + w(x,t)$$
where $\nabla^2 v = 0$ with the inhomogeneous BCs, and $w$ satisfies homogeneous BCs.

## ML and Alignment Connection

Sturm-Liouville eigenvalue problems generalize the matrix eigendecomposition from Phase 1 to function spaces. Just as PCA finds the principal eigenvectors of a covariance matrix, kernel PCA and spectral methods find eigenfunctions of integral operators. The orthogonality and completeness of Sturm-Liouville eigenfunctions is the infinite-dimensional version of the spectral theorem -- the mathematical foundation for all spectral methods in ML, from kernel methods to diffusion maps to spectral clustering.

The Rayleigh quotient is directly connected to PCA and dimensionality reduction. In PCA, the first principal component maximizes x^T*Sigma*x / x^T*x (the matrix Rayleigh quotient). The Sturm-Liouville Rayleigh quotient extends this to infinite-dimensional function spaces, which is exactly what kernel PCA does. Variational methods in deep learning (e.g., variational autoencoders) also rely on optimizing functionals over function spaces.

The nonuniform rod and string problems show what happens when the "geometry" of the problem is not uniform -- the eigenfunctions and eigenvalues change. In ML, this corresponds to non-uniform data distributions, variable learning rates across parameters, or architectures with different widths at different layers. Understanding how non-uniformity affects spectral properties helps in designing architectures and training procedures that work well across diverse data distributions.

Inhomogeneous boundary conditions and the decomposition u = v + w mirrors the practice of removing a trend or baseline before applying spectral analysis -- common in signal processing and time series analysis in ML.
