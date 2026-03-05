# Lesson 30: Fourier Series and the Wave Equation

[<- Previous](lesson-29-intro-pdes.md) | [Back to TOC](../README.md) | [Next: Eigenvalue Problems and Sturm-Liouville Theory ->](lesson-31-wave-equation.md)

---

Fourier series emerge naturally from separation of variables. When you impose boundary conditions, the spatial ODE becomes an eigenvalue problem -- only certain frequencies (eigenvalues) are allowed. The general solution is a superposition of these eigenfunctions, and the coefficients are determined by the initial condition via Fourier's formulas. This lesson develops Fourier series systematically -- the full series, sine and cosine half-range expansions, differentiation and integration of series, and the complex exponential form -- before turning to the wave equation, where these tools are applied to a fundamentally different PDE.

The wave equation is the prototypical hyperbolic PDE, governing vibrating strings, sound waves, and electromagnetic radiation. Where the heat equation diffuses and smooths, the wave equation propagates and preserves. An initial disturbance splits into pulses traveling in opposite directions at speed c -- information moves but is not destroyed. This fundamental contrast between diffusion (information loss) and wave propagation (information preservation) runs through all of physics and through neural network architecture design.

## Core Learning

### Fourier Series (Videos: L13-L17)

- **Fourier series:** any "reasonable" function on [0, L] can be written as f(x) = a_0/2 + sum_{n=1}^{infinity} [a_n cos(n*pi*x/L) + b_n sin(n*pi*x/L)]
- Fourier coefficients are computed via inner products (integrals) -- this is orthogonal projection in function space, exactly like projecting onto eigenvectors in linear algebra
- Convergence: Fourier series converge in L^2 norm; pointwise convergence at continuity points; Gibbs phenomenon at discontinuities (overshooting by ~9%)
- Parseval's theorem: energy in physical space = energy in frequency space (sum of squared coefficients)
- **Sine and cosine series:** a function on [0, L] can be expanded in a pure sine series (odd extension) or pure cosine series (even extension); sine series arise from Dirichlet BCs, cosine series from Neumann BCs; choosing the right half-range expansion depends on the boundary conditions of the PDE problem
- **Differentiating Fourier series:** term-by-term differentiation is valid when the series converges uniformly and the derivative series also converges; differentiating a cosine series yields a sine series and vice versa; smoothness of the function determines how fast Fourier coefficients decay -- smoother functions have faster-decaying coefficients, so their series can be differentiated more freely
- **Integrating Fourier series:** term-by-term integration is always valid for L^2-convergent Fourier series (more permissive than differentiation); integrating a Fourier series typically improves convergence; useful for solving ODEs and integral equations involving periodic functions
- **Complex Fourier series:** f(x) = sum_{n=-infinity}^{infinity} c_n * exp(i*n*pi*x/L), where c_n = (1/2L) * integral_{-L}^{L} f(x) * exp(-i*n*pi*x/L) dx; more compact notation using complex exponentials; negative frequencies encode phase information; connects naturally to the Fourier transform (the continuous limit as L -> infinity); this is the form used in most ML applications (positional encodings, spectral methods)

### The Wave Equation (Videos: L18-L21)

- **Wave equation derivation:** Newton's second law applied to a small element of a vibrating string yields u_{tt} = c^2 * u_{xx}, where c = sqrt(tension/density) is the wave speed; the wave equation is hyperbolic (B^2 - AC > 0 in the classification scheme)
- **Boundary conditions of the wave equation:** fixed ends (Dirichlet: u(0,t) = u(L,t) = 0), free ends (Neumann: u_x(0,t) = u_x(L,t) = 0), or mixed; the type of boundary condition determines the allowed modes -- fixed ends produce sine modes, free ends produce cosine modes; initial conditions specify both the initial displacement u(x,0) = f(x) AND the initial velocity u_t(x,0) = g(x) (two conditions because the wave equation is second-order in time)
- **Solving the wave equation** via separation of variables: u(x,t) = X(x)T(t) yields X'' + lambda*X = 0 and T'' + c^2*lambda*T = 0; the spatial equation is the same eigenvalue problem as for the heat equation; the temporal equation gives oscillatory solutions T_n(t) = A_n*cos(omega_n*t) + B_n*sin(omega_n*t) where omega_n = c*n*pi/L (contrast: exponential decay in the heat equation); standing waves: spatial modes oscillating in time
- **d'Alembert's solution (infinite domain):** u(x,t) = f(x - ct) + g(x + ct) -- superposition of right- and left-traveling waves; d'Alembert's formula with initial conditions: u(x,t) = (1/2)[phi(x-ct) + phi(x+ct)] + (1/2c)*integral_{x-ct}^{x+ct} psi(s) ds
- Characteristic lines: x - ct = const and x + ct = const; information propagates along these lines at finite speed c
- Superposition principle: linear combinations of solutions are solutions
- Energy conservation: the wave equation conserves total energy (kinetic + potential), unlike the heat equation which dissipates energy
- **The wave equation in higher dimensions:** u_{tt} = c^2*(u_{xx} + u_{yy}) in 2D (vibrating membranes), u_{tt} = c^2*(u_{xx} + u_{yy} + u_{zz}) in 3D; separation of variables in rectangular domains yields products of sine/cosine modes; circular membranes require Bessel functions; Huygens' principle -- in odd spatial dimensions (1D, 3D), sharp signals stay sharp; in even dimensions (2D), signals leave a residual wake

## Watch -- Primary

- **Jason Bramburger -- PDEs Course** (Lectures 13-21)
  - https://www.youtube.com/playlist?list=PLXsDp0z6VWFQJ6BY1O6Hz5XX2ppgGvEAu
  - L13: Fourier Series
  - L14: Sine and Cosine Series
  - L15: Differentiating Fourier Series
  - L16: Integrating Fourier Series
  - L17: Complex Fourier Series
  - L18: The Wave Equation
  - L19: Boundary Conditions of the Wave Equation
  - L20: Solving the Wave Equation
  - L21: The Wave Equation in Higher Dimensions

## Watch -- Secondary

- **3Blue1Brown -- "But what is a Fourier series?"**
  - https://www.youtube.com/watch?v=r6sGWTCMz2k
  - *The visual intuition for Fourier decomposition as "wrapping" a function around a circle and measuring the center of mass. Essential viewing.*

## Read

- **Haberman, *Applied Partial Differential Equations***, Ch. 3: Fourier series; Ch. 4: Wave equation
- **Strauss, *Partial Differential Equations: An Introduction***, Ch. 2: Waves and d'Alembert
- **Strang, *Introduction to Linear Algebra***, Section on function spaces and Fourier series (connects to Phase 1 linear algebra)

## Key Equations

**Fourier series** on $[0, L]$:
$$f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos\!\left(\frac{n\pi x}{L}\right) + b_n \sin\!\left(\frac{n\pi x}{L}\right) \right]$$

**Fourier coefficients:**
$$a_n = \frac{2}{L} \int_0^L f(x) \cos\!\left(\frac{n\pi x}{L}\right) dx, \qquad b_n = \frac{2}{L} \int_0^L f(x) \sin\!\left(\frac{n\pi x}{L}\right) dx$$

**Complex Fourier series:**
$$f(x) = \sum_{n=-\infty}^{\infty} c_n \, e^{i n \pi x / L}, \qquad c_n = \frac{1}{2L} \int_{-L}^{L} f(x) \, e^{-i n \pi x / L} \, dx$$

**Parseval's theorem:**
$$\frac{1}{L} \int_0^L |f(x)|^2 \, dx = \frac{|a_0|^2}{4} + \frac{1}{2} \sum_{n=1}^{\infty} \left( |a_n|^2 + |b_n|^2 \right)$$

**Wave equation (1D):**
$$\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}$$

**d'Alembert's solution:**
$$u(x,t) = f(x - ct) + g(x + ct)$$

**d'Alembert with initial conditions** $u(x,0) = \phi(x)$, $u_t(x,0) = \psi(x)$:
$$u(x,t) = \frac{1}{2}\big[\phi(x-ct) + \phi(x+ct)\big] + \frac{1}{2c}\int_{x-ct}^{x+ct} \psi(s)\, ds$$

**Standing waves** (Dirichlet BCs on $[0, L]$):
$$u_n(x,t) = \sin\!\left(\frac{n\pi x}{L}\right) \left[ A_n \cos\!\left(\frac{n\pi c t}{L}\right) + B_n \sin\!\left(\frac{n\pi c t}{L}\right) \right]$$

**Energy conservation:**
$$E(t) = \frac{1}{2}\int_0^L \left[ u_t^2 + c^2 u_x^2 \right] dx = \text{const}$$

## ML and Alignment Connection

Fourier analysis decomposes signals into frequency components -- this is exactly what spectral methods in ML do. Graph neural networks use the graph Fourier transform (eigenvectors of the graph Laplacian) to define convolutions on graphs. Transformer positional encodings use sinusoidal bases directly borrowed from Fourier series. The spectral bias of neural networks -- the empirical observation that networks learn low-frequency components before high-frequency ones -- mirrors the heat equation's frequency-dependent decay.

The complex Fourier series is the form most directly used in ML. The Fourier features in transformers (sin/cos positional encodings) come from the real and imaginary parts of complex exponentials. Random Fourier features for kernel approximation sample from the frequency domain. Understanding the full Fourier series -- differentiation, integration, convergence properties -- is essential for analyzing what frequency information neural networks can and cannot capture.

Waves propagate information without losing it; heat diffuses and destroys information. This distinction is directly relevant to neural network architecture design. Residual connections (y = x + f(x)) preserve the input signal like a wave -- information passes through even if f contributes nothing. Without residual connections, deep networks behave more like the heat equation: signals attenuate and gradients vanish as they propagate through layers. This is why ResNets, transformers (which are residual by construction), and other skip-connection architectures can be trained to extreme depth while plain deep networks cannot.

For alignment: understanding which frequencies a model captures first (spectral bias) tells you about the order in which it learns features. If safety-relevant features are high-frequency (subtle, context-dependent), they may be learned last -- or not at all if training stops too early. The characteristic lines of the wave equation also connect to receptive fields in neural networks: information from an input at position x can only reach outputs within a certain cone, determined by the architecture.
