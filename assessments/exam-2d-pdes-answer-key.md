# Exam 2D: Partial Differential Equations — Answer Key

**The Path to AI Alignment — Lessons 29–33 Comprehensive Assessment**

---

> **Grading philosophy:** Partial credit is generous for correct reasoning with arithmetic errors. Conceptual insight matters as much as mechanical computation. The ML-connection parts reward thoughtful analogies — there is no single "right" phrasing, so any answer demonstrating genuine understanding earns full marks. For Fourier coefficient computations, full setup of the integral with correct limits and integrand earns most of the credit even if arithmetic slips occur.

---

# Part I: Classical PDEs (70 points)

---

### Question 1 (10 pts) — PDE Classification and Setup

**(a)** The general second-order linear PDE is $Au_{xx} + Bu_{xy} + Cu_{yy} + \text{(lower order)} = 0$, classified by the discriminant $B^2 - 4AC$.

**(i)** $u_{xx} + u_{yy} = 0$

$A = 1,\; B = 0,\; C = 1$. Discriminant: $B^2 - 4AC = 0 - 4 = -4 < 0$.

**Classification: Elliptic.**

**(ii)** $u_t = ku_{xx}$

Rewrite as $ku_{xx} - u_t = 0$. Here $A = k,\; B = 0,\; C = 0$. Discriminant: $B^2 - 4AC = 0 - 0 = 0$.

**Classification: Parabolic.**

**(iii)** $u_{tt} = c^2 u_{xx}$

Rewrite as $c^2 u_{xx} - u_{tt} = 0$. Here $A = c^2,\; B = 0,\; C = -1$. Discriminant: $B^2 - 4AC = 0 + 4c^2 = 4c^2 > 0$.

**Classification: Hyperbolic.**

**(iv)** $u_{xx} + 4u_{xy} + 4u_{yy} = 0$

$A = 1,\; B = 4,\; C = 4$. Discriminant: $B^2 - 4AC = 16 - 16 = 0$.

**Classification: Parabolic.**

**(b)**

- **Elliptic** — Laplace's equation $\nabla^2 u = 0$: describes steady-state temperature distributions and equilibrium configurations.
- **Parabolic** — Heat equation $u_t = k u_{xx}$: describes diffusion of heat (or any substance) and the smoothing of temperature profiles over time.
- **Hyperbolic** — Wave equation $u_{tt} = c^2 u_{xx}$: describes propagation of disturbances (sound waves, vibrating strings) at finite speed.

**(c)**

- **Dirichlet** ($u = g$ on boundary): Fix the temperature at the endpoints. *Example:* a rod with its ends immersed in ice baths at $0°$C — the temperature is prescribed at each end.
- **Neumann** ($\partial u / \partial n = g$ on boundary): Fix the heat flux at the endpoints. *Example:* an insulated end has zero flux ($\partial u / \partial x = 0$), meaning no heat escapes through that boundary.
- **Robin** ($au + b\,\partial u/\partial n = g$ on boundary): A mixed condition combining temperature and flux. *Example:* Newton's law of cooling at an endpoint — the heat flux is proportional to the difference between the rod's temperature and the ambient temperature.

**(d)**

- **ML Dirichlet constraints:** Fixing output values at certain inputs — for example, in Physics-Informed Neural Networks (PINNs), enforcing that the network output satisfies $u = g$ on the domain boundary, or interpolation constraints where the model must pass through specific data points.
- **ML Neumann constraints:** Fixing gradients at certain points — for example, gradient penalties in WGAN-GP that enforce a Lipschitz constraint by penalizing the norm of $\nabla_x D(x)$, or smoothness regularization that constrains the derivative of the learned function.

---

### Question 2 (12 pts) — The Heat Equation: Derivation and Steady State

**(a)** **Derivation from Fourier's law and conservation of energy.**

*Step 1 — Fourier's law:* The heat flux $q$ (energy per unit area per unit time) is proportional to the negative temperature gradient:

$$q = -k\,\frac{\partial u}{\partial x}$$

where $k > 0$ is the thermal diffusivity. Heat flows from hot to cold.

*Step 2 — Energy balance on a thin slab:* Consider a thin slab $[x, x + \Delta x]$. The rate of heat energy entering from the left is $q(x)$, and the rate leaving from the right is $q(x + \Delta x)$. The net rate of heat gain is:

$$\text{Rate in} - \text{Rate out} = q(x) - q(x + \Delta x) \approx -\frac{\partial q}{\partial x}\,\Delta x$$

This must equal the rate of temperature increase in the slab (with appropriate constants absorbed into $k$):

$$\frac{\partial u}{\partial t}\,\Delta x = -\frac{\partial q}{\partial x}\,\Delta x$$

*Step 3 — Combine:* Substituting Fourier's law:

$$\frac{\partial u}{\partial t} = -\frac{\partial q}{\partial x} = -\frac{\partial}{\partial x}\!\bigl(-k\,u_x\bigr) = k\,\frac{\partial^2 u}{\partial x^2}$$

$$\boxed{u_t = k\,u_{xx}}$$

**(b)** Set $u_t = 0$: the PDE becomes $u_{xx} = 0$, whose general solution is $u = ax + b$.

Apply boundary conditions: $u(0) = 0 \Rightarrow b = 0$. $u(\pi) = 0 \Rightarrow a\pi = 0 \Rightarrow a = 0$.

$$\boxed{u_{ss}(x) = 0}$$

The steady state is identically zero — with both ends held at zero, all heat eventually drains out.

**(c)** Again $u_{xx} = 0 \Rightarrow u = ax + b$.

Apply boundary conditions: $u(0) = 0 \Rightarrow b = 0$. $u(\pi) = T_0 \Rightarrow a = T_0/\pi$.

$$\boxed{u_{ss}(x) = \frac{T_0}{\pi}\,x}$$

**Geometric interpretation:** The steady-state temperature profile is a **straight line** from $0$ at the left end to $T_0$ at the right end. Heat flows at a constant rate from the hot end to the cold end.

**(d)** Try $u(x,t) = e^{-kt}\sin(x)$.

- PDE check: $u_t = -k e^{-kt}\sin(x)$ and $u_{xx} = -e^{-kt}\sin(x)$. So $k\,u_{xx} = -k e^{-kt}\sin(x) = u_t$. **PDE satisfied.**
- IC check: $u(x,0) = e^0 \sin(x) = \sin(x)$. **Initial condition satisfied.**
- BC check: $u(0,t) = e^{-kt}\sin(0) = 0$ and $u(\pi,t) = e^{-kt}\sin(\pi) = 0$. **Boundary conditions satisfied.**

$$\boxed{u(x,t) = e^{-kt}\sin(x)}$$

**(e)** As $t \to \infty$, $e^{-kt} \to 0$, so **$u(x,t) \to 0$** — the solution decays to the steady state found in part (b).

**Physical interpretation:** The exponential decay rate is $k$ (the thermal diffusivity). Higher $k$ means heat spreads faster through the material, so temperature variations are smoothed out more quickly. The rod equilibrates to its boundary conditions at a rate proportional to $k$. This is the fundamental smoothing property of the heat equation.

---

### Question 3 (10 pts) — Separation of Variables

**(a)** Assume $u(x,t) = X(x)\,T(t)$. Substitute into $u_t = u_{xx}$:

$$X(x)\,T'(t) = X''(x)\,T(t)$$

Divide both sides by $X(x)\,T(t)$:

$$\frac{T'(t)}{T(t)} = \frac{X''(x)}{X(x)}$$

The left side depends only on $t$ and the right side only on $x$, so both must equal a constant $-\lambda$:

$$\frac{T'}{T} = \frac{X''}{X} = -\lambda$$

This gives two ODEs:

$$X'' + \lambda X = 0, \qquad T' + \lambda T = 0$$

**(b)** Apply boundary conditions $u(0,t) = u(\pi,t) = 0$, which require $X(0) = 0$ and $X(\pi) = 0$.

The ODE $X'' + \lambda X = 0$ with $X(0) = X(\pi) = 0$ has nontrivial solutions only when $\lambda > 0$. Writing $\lambda = \mu^2$, the general solution is $X = A\cos(\mu x) + B\sin(\mu x)$.

$X(0) = 0 \Rightarrow A = 0$, so $X = B\sin(\mu x)$.

$X(\pi) = 0 \Rightarrow B\sin(\mu\pi) = 0$. For nontrivial solutions, $\sin(\mu\pi) = 0$, so $\mu = n$ for $n = 1, 2, 3, \ldots$

$$\boxed{\lambda_n = n^2, \qquad X_n(x) = \sin(nx), \quad n = 1, 2, 3, \ldots}$$

**(c)** For each $n$, the $T$ equation is $T' + n^2 T = 0$, which has solution:

$$\boxed{T_n(t) = e^{-n^2 t}}$$

**(d)** The general solution is:

$$u(x,t) = \sum_{n=1}^{\infty} b_n\, e^{-n^2 t}\,\sin(nx)$$

At $t = 0$: $u(x,0) = x(\pi - x) = \sum_{n=1}^{\infty} b_n \sin(nx)$.

The Fourier sine coefficients are:

$$b_n = \frac{2}{\pi}\int_0^{\pi} x(\pi - x)\sin(nx)\,dx$$

Expand $x(\pi - x) = \pi x - x^2$ and integrate by parts twice. The result is:

$$b_n = \frac{4}{n^3 \pi}\bigl[1 - (-1)^n\bigr]$$

For **even** $n$: $1 - (-1)^n = 1 - 1 = 0$, so $b_n = 0$.

For **odd** $n$: $1 - (-1)^n = 2$, so $b_n = \dfrac{8}{n^3 \pi}$.

Computing the first three:

$$\boxed{b_1 = \frac{8}{\pi}, \qquad b_2 = 0, \qquad b_3 = \frac{8}{27\pi}}$$

**(e)** The mode with index $n$ decays as $e^{-n^2 t}$. Since $n^2$ grows quadratically, **higher-frequency modes decay exponentially faster** than the fundamental mode.

**Physical significance:** The heat equation acts as a **low-pass filter**. High-frequency oscillations (fine-grained temperature variations) are smoothed out first, leaving only the slowly-decaying low-frequency components. For large $t$, the solution is dominated by the fundamental mode $b_1 e^{-t}\sin(x)$ — all the fine structure has been erased. This is exactly why diffusion processes destroy information: they preferentially eliminate high-frequency detail.

---

### Question 4 (10 pts) — Fourier Series

**(a)** The Fourier sine series of $f(x) = 1$ on $[0, \pi]$ has coefficients:

$$b_n = \frac{2}{\pi}\int_0^{\pi} \sin(nx)\,dx = \frac{2}{\pi}\biggl[-\frac{\cos(nx)}{n}\biggr]_0^{\pi} = \frac{2}{n\pi}\bigl(1 - \cos(n\pi)\bigr) = \frac{2}{n\pi}\bigl(1 - (-1)^n\bigr)$$

For even $n$: $b_n = 0$. For odd $n$: $b_n = \dfrac{4}{n\pi}$.

$$\boxed{b_1 = \frac{4}{\pi},\quad b_3 = \frac{4}{3\pi},\quad b_5 = \frac{4}{5\pi},\quad b_7 = \frac{4}{7\pi}}$$

**(b)** The function $f(x) = 1$ on $[0,\pi]$, when extended as an odd function (which the sine series implicitly does), has jump discontinuities at $x = 0$ and $x = \pi$ (jumping between $+1$ and $-1$).

At these discontinuities, **the Fourier series converges to the average of the left and right limits**:

$$\frac{1 + (-1)}{2} = \boxed{0} \quad\text{(at } x = 0 \text{ and } x = \pi\text{)}$$

More precisely, at $x = 0^+$ the function is $1$ and at $x = 0^-$ (from the odd extension) it is $-1$, so the series converges to $1/2$ from the right perspective. The midpoint of the jump is $\mathbf{1/2}$.

**(c)** **Gibbs phenomenon:** Near discontinuities, the Fourier partial sums overshoot the function value by approximately **9%** of the jump size. This overshoot does **not** diminish as more terms are added — it merely becomes narrower and moves closer to the discontinuity.

This does not violate convergence because the Fourier series converges in the **$L^2$ (mean-square) sense**: $\int |f - S_N|^2\,dx \to 0$ as $N \to \infty$. The pointwise overshoot occupies a vanishingly narrow interval, so its contribution to the integrated error goes to zero. Convergence is in the energy norm, not pointwise uniform.

**(d)** **Parseval's identity** states that for the Fourier sine series on $[0,\pi]$:

$$\frac{2}{\pi}\int_0^{\pi} [f(x)]^2\,dx = \sum_{n=1}^{\infty} b_n^2$$

Apply to $f(x) = x$ on $[0,\pi]$. The sine coefficients are $b_n = \dfrac{2}{n\pi}\displaystyle\int_0^{\pi} x\sin(nx)\,dx$. Integration by parts gives $b_n = (-1)^{n+1}\cdot\dfrac{2}{n}$.

Left side:

$$\frac{2}{\pi}\int_0^{\pi} x^2\,dx = \frac{2}{\pi}\cdot\frac{\pi^3}{3} = \frac{2\pi^2}{3}$$

Right side:

$$\sum_{n=1}^{\infty} b_n^2 = \sum_{n=1}^{\infty} \frac{4}{n^2}$$

Setting them equal:

$$\frac{2\pi^2}{3} = 4\sum_{n=1}^{\infty}\frac{1}{n^2}$$

$$\boxed{\sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6}}$$

This is the **Basel problem**, first solved by Euler in 1734.

**(e)** The sine functions $\sin(nx)$ are **eigenfunctions of the operator $d^2/dx^2$** on $[0,\pi]$ with homogeneous Dirichlet boundary conditions. They form an orthogonal basis that decomposes any (square-integrable) function into frequency components.

On a graph, the **graph Laplacian** plays the role of $d^2/dx^2$. Its eigenvectors are the "graph Fourier modes" — they form an orthogonal basis for functions defined on the graph's vertices. Low-eigenvalue eigenvectors vary slowly across the graph (analogous to low-frequency sines), while high-eigenvalue eigenvectors oscillate rapidly.

**Both provide an orthogonal decomposition into frequency components** — sines for functions on continuous intervals, graph Laplacian eigenvectors for functions on discrete graph structures. This is the foundation of **spectral graph theory** and **graph neural networks**.

---

### Question 5 (8 pts) — Sturm-Liouville Theory

**(a)** Three key properties of Sturm-Liouville eigenvalue problems:

1. **All eigenvalues are real.** This ensures the separation constants in PDEs are real numbers, giving physically meaningful solutions.
2. **Eigenfunctions corresponding to distinct eigenvalues are orthogonal** with respect to the weight function $w(x)$: $\int_a^b X_m(x)\,X_n(x)\,w(x)\,dx = 0$ for $m \neq n$.
3. **The eigenfunctions form a complete set** — any sufficiently well-behaved function can be expanded as a (possibly infinite) series in these eigenfunctions.

**(b)** The equation $X'' + \lambda X = 0$ is a Sturm-Liouville problem with:

$$p(x) = 1, \qquad q(x) = 0, \qquad w(x) = 1$$

written in the standard form $-(pX')' + qX = \lambda\,w\,X$, which becomes $-X'' = \lambda X$, i.e., $X'' + \lambda X = 0$.

**(c)** **Direct orthogonality verification.** For $m \neq n$:

$$\int_0^{\pi} \sin(mx)\sin(nx)\,dx = \frac{1}{2}\int_0^{\pi}\bigl[\cos((m-n)x) - \cos((m+n)x)\bigr]\,dx$$

$$= \frac{1}{2}\biggl[\frac{\sin((m-n)x)}{m-n} - \frac{\sin((m+n)x)}{m+n}\biggr]_0^{\pi}$$

Since $m-n$ and $m+n$ are both nonzero integers, $\sin((m-n)\pi) = 0$ and $\sin((m+n)\pi) = 0$, and both terms vanish at $x = 0$ as well.

$$\boxed{\int_0^{\pi}\sin(mx)\sin(nx)\,dx = 0 \quad\text{for } m \neq n}$$

**(d)** Without **completeness**, there would exist initial conditions $u(x,0)$ that cannot be represented as a sum of eigenfunctions $\sum b_n \sin(nx)$. The separation of variables method would break down — we could solve the PDE for some initial conditions but not all.

Completeness guarantees that the Fourier sine coefficients $b_n$ can always be computed and that the resulting series converges to the desired initial condition. Without it, the entire machinery of eigenfunction expansions would have gaps, leaving certain physically reasonable problems unsolvable by this method.

---

### Question 6 (10 pts) — The Wave Equation

**(a)** Assume $u(x,t) = X(x)T(t)$ in $u_{tt} = c^2 u_{xx}$:

$$XT'' = c^2 X''T \implies \frac{T''}{c^2 T} = \frac{X''}{X} = -\lambda$$

This gives $X'' + \lambda X = 0$ and $T'' + \lambda c^2 T = 0$.

With boundary conditions $X(0) = X(\pi) = 0$: eigenvalues $\lambda_n = n^2$, eigenfunctions $X_n = \sin(nx)$.

The $T$ equation becomes $T'' + n^2 c^2 T = 0$, with solution:

$$T_n(t) = a_n\cos(nct) + b_n\sin(nct)$$

**General solution:**

$$\boxed{u(x,t) = \sum_{n=1}^{\infty}\bigl[a_n\cos(nct) + b_n\sin(nct)\bigr]\sin(nx)}$$

**(b)** Apply initial conditions:

$u(x,0) = \sin(2x)$: comparing with $\sum a_n \sin(nx)$, we get $a_2 = 1$ and all other $a_n = 0$.

$u_t(x,0) = 0$: $\sum b_n\,(nc)\sin(nx) = 0$, so $b_n = 0$ for all $n$.

$$\boxed{u(x,t) = \cos(2ct)\sin(2x)}$$

This is a **standing wave** — the spatial shape $\sin(2x)$ oscillates in amplitude with frequency $2c$.

**(c)** **d'Alembert's solution:** The general solution of $u_{tt} = c^2 u_{xx}$ on the whole line is:

$$u(x,t) = f(x - ct) + g(x + ct)$$

- $f(x - ct)$: a **right-traveling wave** moving at speed $c$.
- $g(x + ct)$: a **left-traveling wave** moving at speed $c$.
- **Characteristics:** The lines $x - ct = \text{const}$ and $x + ct = \text{const}$ in the $(x,t)$-plane. Information propagates along these lines. The solution at any point $(x_0, t_0)$ depends only on the initial data within the interval $[x_0 - ct_0,\; x_0 + ct_0]$ (the domain of dependence).

**(d)** Key differences between heat and wave equations:

| Property | Heat equation | Wave equation |
|---|---|---|
| **Propagation speed** | Infinite (effect felt instantly everywhere) | Finite speed $c$ |
| **Energy** | Dissipated over time | Conserved (no dissipation) |
| **Smoothing** | Discontinuities immediately smoothed | Discontinuities propagate along characteristics |
| **Reversibility** | Irreversible (information destroyed) | Reversible (time-symmetric) |

**(e)** In a CNN, information propagates **layer by layer** at a finite "speed." Each convolutional layer has a finite kernel size, so after $k$ layers, a pixel's information can influence outputs within a radius of approximately $k \times (\text{kernel size}/2)$ pixels. This is the **receptive field**.

This is directly analogous to the **characteristic cone** of the wave equation: a disturbance at point $x_0$ at time $t = 0$ can only influence the region $|x - x_0| \leq ct$ by time $t$. The receptive field of a CNN is the discrete analog of this finite-speed propagation. Deeper networks (more layers) have larger receptive fields, just as longer times allow waves to reach farther.

---

### Question 7 (10 pts) — Laplace's Equation and the Helmholtz Equation

**(a)** In polar coordinates $(r,\theta)$, Laplace's equation on a disk of radius $R$ is:

$$r^2 R'' + r R' + \Theta'' = 0 \quad\text{(after separation } u = R(r)\Theta(\theta)\text{)}$$

$$\frac{r^2 R'' + r R'}{R} = -\frac{\Theta''}{\Theta} = n^2$$

- **Angular equation:** $\Theta'' + n^2\Theta = 0 \Rightarrow \Theta_n(\theta) = A_n\cos(n\theta) + B_n\sin(n\theta)$, with $\Theta$ periodic ($2\pi$-periodic), so $n = 0, 1, 2, \ldots$
- **Radial equation:** $r^2 R'' + rR' - n^2 R = 0$ (Euler equation). Solutions: $R = r^n$ and $R = r^{-n}$. **Boundedness at the origin** requires discarding $r^{-n}$, so $R_n(r) = r^n$.

**General solution on the disk:**

$$\boxed{u(r,\theta) = \frac{A_0}{2} + \sum_{n=1}^{\infty} r^n\bigl(A_n\cos(n\theta) + B_n\sin(n\theta)\bigr)}$$

The coefficients $A_n, B_n$ are determined by the boundary data $u(R,\theta)$.

**(b)** **Mean value property:** If $u$ is harmonic (satisfies Laplace's equation) in a domain, then its value at any interior point equals the average of $u$ over any circle centered at that point:

$$u(\text{center}) = \frac{1}{2\pi}\int_0^{2\pi} u(R,\theta)\,d\theta$$

**Physical interpretation:** In steady-state heat conduction, the temperature at any point is the average of the surrounding temperatures. No point can be a local maximum or minimum of temperature (maximum principle) — if it were hotter than its neighbors, heat would flow out, contradicting the steady state. Heat has finished flowing, so the temperature at every point is in perfect balance with its surroundings.

**(c)** Look for time-harmonic solutions: $u(x,t) = U(x)e^{i\omega t}$.

Substitute into the wave equation $u_{tt} = c^2 u_{xx}$:

$$-\omega^2 U e^{i\omega t} = c^2 U'' e^{i\omega t}$$

Cancel $e^{i\omega t}$:

$$U'' + \frac{\omega^2}{c^2}U = 0$$

This is the **Helmholtz equation** $U'' + k^2 U = 0$ with $k = \omega/c$ (the wavenumber). It arises whenever we seek steady-state oscillatory solutions to the wave equation — the spatial structure of a vibration at a fixed frequency.

**(d)** Consider $u_t + cu_x = 0$ (the transport equation). If $u(x,t) = f(x - ct)$, then:

$$u_t = -c\,f'(x - ct), \qquad u_x = f'(x - ct)$$

$$u_t + c\,u_x = -cf' + cf' = 0 \quad\checkmark$$

The transport equation simply **translates the initial profile** $f(x)$ to the right at constant speed $c$ without changing its shape. The **characteristic curves** are the lines $x - ct = \text{const}$, along which the solution is constant. Every point on the initial profile rides along its characteristic line at speed $c$.

---

# Part II: PDEs Meet Machine Learning (80 points)

---

### Question 8 (10 pts) — Heat Equation as Forward Diffusion

**(a)** In the forward SDE $dx_t = -\frac{\beta(t)}{2}\,x_t\,dt + \sqrt{\beta(t)}\,dW_t$:

- **Drift term** $-\frac{\beta(t)}{2}\,x_t$: pushes $x_t$ toward the origin, **shrinking the signal** by a factor that depends on the current position. This systematically contracts the data distribution.
- **Diffusion term** $\sqrt{\beta(t)}\,dW_t$: adds **Gaussian noise** at rate $\beta(t)$. This spreads out the distribution, injecting randomness.

Together, the drift contracts the data distribution while the noise spreads it, gradually transforming structured data into unstructured noise.

**(b)** As $t \to \infty$:

$$\alpha_t = e^{-\int_0^t \beta(s)/2\,ds} \to 0, \qquad \sigma_t^2 = 1 - e^{-\int_0^t \beta(s)\,ds} \to 1$$

So $x_t \to \mathcal{N}(0, I)$. **This is desirable** because the endpoint distribution is a known, easy-to-sample prior. We can draw $x_T \sim \mathcal{N}(0,I)$ trivially, then run the reverse process to generate data. If the endpoint were some complicated unknown distribution, we couldn't start the reverse process.

**(c)** The **Fokker-Planck equation** for the forward SDE is:

$$\frac{\partial p}{\partial t} = \underbrace{\nabla \cdot\!\Bigl(\frac{\beta}{2}\,x\,p\Bigr)}_{\text{advection}} + \underbrace{\frac{\beta}{2}\,\nabla^2 p}_{\text{diffusion}}$$

- **Advection term** $\nabla \cdot(\frac{\beta}{2}\,xp)$: transports probability mass toward the origin (contraction).
- **Diffusion term** $\frac{\beta}{2}\,\nabla^2 p$: spreads probability mass outward (smoothing).

**Special cases:**
- If $\beta = 0$: $\partial p/\partial t = 0$ — the distribution is **frozen**, nothing happens.
- If the drift is zero (no contraction): $\partial p/\partial t = \frac{\beta}{2}\nabla^2 p$ — this is the **pure heat equation**, and the density simply diffuses outward without contraction.

**(d)** Adding Gaussian noise to each data point is equivalent to **convolving the data distribution** $p(x)$ with a Gaussian kernel $G_\sigma(x)$:

$$p_{\text{noisy}}(x) = (p * G_\sigma)(x)$$

The heat equation evolves a function by exactly this convolution — the solution at time $t$ is the initial condition convolved with the heat kernel. **The function being "heated" is the probability density** $p(x,t)$, not the individual data points. The PDE describes how the entire distribution smooths out over time, with the noise level $\sigma(t)$ playing the role of $\sqrt{2kt}$ in the heat kernel.

---

### Question 9 (10 pts) — The Score Function

**(a)** The **score function** is defined as:

$$s(x,t) = \nabla_x \log p(x,t)$$

For a Gaussian $p = \mathcal{N}(\mu, \sigma^2 I)$:

$$\log p(x) = \text{const} - \frac{\|x - \mu\|^2}{2\sigma^2}$$

$$\boxed{s(x) = \nabla_x \log p = -\frac{x - \mu}{\sigma^2} = \frac{\mu - x}{\sigma^2}}$$

The score **points toward the mean** $\mu$. Its magnitude is proportional to the distance from the mean and inversely proportional to the variance. At the mean, the score is zero.

**(b)** Starting from the Fokker-Planck equation $\partial p/\partial t = D\,\nabla^2 p$:

Taking $\nabla \log$ of both sides and using $\nabla \log p = \nabla p / p$, we obtain:

$$\frac{\partial s}{\partial t} = D\,\nabla\!\left(\frac{\nabla^2 p}{p}\right)$$

Using the identity $\nabla(\nabla^2 p / p) = \nabla^2 s + \nabla(\|s\|^2)$, the score satisfies:

$$\boxed{\frac{\partial s}{\partial t} = D\,\nabla^2 s + D\,\nabla\bigl(\|s\|^2\bigr)}$$

This is a **nonlinear PDE** for the score — the $\nabla(\|s\|^2)$ term makes it nonlinear, unlike the linear Fokker-Planck equation for $p$.

**(c)** The forward transition kernel is $q(x_t \mid x_0) = \mathcal{N}(\alpha_t\,x_0,\;\sigma_t^2\,I)$.

$$\log q(x_t \mid x_0) = \text{const} - \frac{\|x_t - \alpha_t x_0\|^2}{2\sigma_t^2}$$

$$\nabla_{x_t}\log q(x_t \mid x_0) = -\frac{x_t - \alpha_t x_0}{\sigma_t^2}$$

Since $x_t = \alpha_t x_0 + \sigma_t\,\varepsilon$ where $\varepsilon \sim \mathcal{N}(0,I)$, we have $x_t - \alpha_t x_0 = \sigma_t\,\varepsilon$. Therefore:

$$\boxed{\nabla_{x_t}\log q(x_t \mid x_0) = -\frac{\varepsilon}{\sigma_t}}$$

This is why the neural network is trained to **predict the noise** $\varepsilon$: the score is simply $-\varepsilon/\sigma_t$, so predicting $\varepsilon$ is equivalent to predicting the score (up to a known scaling factor).

**(d)** Computing $\nabla_x \log p(x,t)$ requires knowing $p(x,t)$, the **true marginal density of the data** at noise level $t$. But $p(x,t)$ is the unknown quantity we are trying to model — we only have **samples** from $p$, not the density function itself. The density involves an intractable integral over all possible $x_0$:

$$p(x_t, t) = \int q(x_t \mid x_0)\,p_{\text{data}}(x_0)\,dx_0$$

which requires knowing $p_{\text{data}}$ in closed form. This is why we train a neural network $s_\theta(x,t)$ to approximate the score, using the denoising score matching objective that cleverly avoids needing $p$ directly.

---

### Question 10 (12 pts) — Reverse-Time SDEs and Sampling

**(a)** The forward SDE has drift $f(x,t) = -\frac{\beta}{2}\,x$ and diffusion coefficient $g(t) = \sqrt{\beta}$.

The **Anderson reverse-time SDE** is:

$$dx = \biggl[-\frac{\beta}{2}\,x - \beta\,\nabla_x \log p(x,t)\biggr]dt + \sqrt{\beta}\,d\bar{W}_t$$

where $d\bar{W}_t$ is a reverse-time Brownian motion. Simplifying:

$$\boxed{dx = -\frac{\beta}{2}\bigl[x + 2\,\nabla_x \log p(x,t)\bigr]\,dt + \sqrt{\beta}\,d\bar{W}_t}$$

The score term $\nabla_x \log p$ is the crucial addition that "undoes" the forward diffusion. It steers the trajectory toward regions of high probability density.

**(b)** **Sampling algorithm:**

1. **Initialize:** Draw $x_T \sim \mathcal{N}(0, I)$ (sample from the prior).
2. **Iterate** from $t = T$ down to $t = 0$ in small steps $\Delta t$:
   - Compute the learned score $s_\theta(x_t, t) \approx \nabla_x \log p(x_t, t)$.
   - Draw $z \sim \mathcal{N}(0, I)$.
   - Update: $x_{t - \Delta t} = x_t + \bigl[\frac{\beta}{2}\,x_t + \beta\,s_\theta(x_t, t)\bigr]\Delta t + \sqrt{\beta\,\Delta t}\,z$.
3. **Return** $x_0$ as the generated sample.

**(c)** **Euler-Maruyama** is the SDE analog of Euler's method for ODEs.

- The **deterministic part** $\bigl[-f(x,t) + g^2\,s_\theta(x,t)\bigr]\,\Delta t$ is updated exactly like the Euler step for an ODE — multiply the right-hand side by the time step.
- The **stochastic correction** $g\,\sqrt{\Delta t}\,z$ adds random Gaussian noise scaled by $\sqrt{\Delta t}$, **not** $\Delta t$. The $\sqrt{\Delta t}$ scaling is the signature of Brownian motion (whose increments have standard deviation $\sqrt{\Delta t}$). This is why SDE discretization requires smaller steps than ODE discretization for comparable accuracy — the noise introduces $O(\sqrt{\Delta t})$ error per step rather than $O(\Delta t)$.

**(d)** The **probability flow ODE** replaces the stochastic reverse SDE with a deterministic ODE that produces the same marginal distributions:

$$\frac{dx}{dt} = f(x,t) - \frac{1}{2}g(t)^2\,\nabla_x \log p(x,t)$$

**Advantages over the SDE:**

1. **Deterministic:** The same initial noise $x_T$ always produces the same output $x_0$. This enables **interpolation in latent space** (smoothly blending between two noise inputs) and **exact likelihood computation** via the change-of-variables formula.
2. **Adaptive solvers:** One can use higher-order ODE solvers (RK45, adaptive step-size methods) that take larger steps where the trajectory is smooth. This requires **fewer function evaluations** (fewer neural network forward passes), making sampling significantly faster.

**(e)** Both **neural ODEs** and the **probability flow ODE** integrate a differential equation $dx/dt = f_\theta(x,t)$ with a learned velocity field to transport one distribution into another.

- In **neural ODEs** (normalizing flows): the base distribution is typically $\mathcal{N}(0,I)$, and the ODE transforms it into the data distribution.
- In **diffusion models**: the base distribution is also $\mathcal{N}(0,I)$ (the noise prior), and the probability flow ODE transforms it into (approximately) the data distribution.

The key conceptual link is that both use a **learned vector field** to define a continuous, invertible mapping between distributions. The difference is in training: neural ODEs optimize likelihood directly, while diffusion models train the score function via denoising and derive the ODE from it.

---

### Question 11 (10 pts) — The Fokker-Planck Equation

**(a)** Define the **probability current** (flux) as $J = \mu\,p$, where $\mu$ is the drift velocity and $p$ is the probability density.

**Conservation of probability** (the continuity equation): probability is neither created nor destroyed, so:

$$\frac{\partial p}{\partial t} = -\text{div}(J) = -\text{div}(\mu\,p)$$

This is the advection term — it describes how probability is **transported** by the drift velocity $\mu$. If $\mu > 0$ at some point, probability flows to the right there.

**(b)** The **Ornstein-Uhlenbeck (OU) process** $dx = -\theta x\,dt + \sigma\,dW_t$ has the Fokker-Planck equation:

$$\frac{\partial p}{\partial t} = \frac{\partial}{\partial x}(\theta x\,p) + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial x^2}$$

For the **stationary distribution**, set $\partial p/\partial t = 0$:

$$0 = \frac{\partial}{\partial x}(\theta x\,p) + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial x^2}$$

Try a Gaussian $p = \mathcal{N}(0, \sigma_{\infty}^2)$. The drift term pushes probability toward the origin while diffusion spreads it. In equilibrium, these balance when:

$$\boxed{\sigma_{\infty}^2 = \frac{\sigma^2}{2\theta}}$$

The stationary distribution is $p_\infty(x) = \mathcal{N}\!\bigl(0,\;\sigma^2/(2\theta)\bigr)$. Larger noise $\sigma$ gives a wider distribution; stronger mean reversion $\theta$ gives a narrower one.

**(c)** The Fokker-Planck equation differs from the pure heat equation by the **advection/drift term** $-\text{div}(\mu\,p)$:

$$\underbrace{\frac{\partial p}{\partial t}}_{\text{time evolution}} = \underbrace{-\text{div}(\mu\,p)}_{\text{drift (transport)}} + \underbrace{D\,\nabla^2 p}_{\text{diffusion (smoothing)}}$$

- The **drift** transports the distribution bodily — it moves the "center of mass" of probability without changing its shape.
- The **diffusion** spreads the distribution — it increases variance and smooths out sharp features.
- The **heat equation** is the special case with **zero drift** ($\mu = 0$): only diffusion occurs.

**(d)** The score $\nabla_x \log p$ appears in the reverse SDE as the term that steers the reverse trajectory. It encodes **all the information about $p$ needed to reverse the diffusion** — specifically, the direction toward higher density at each point in space and time.

Knowing $\nabla_x \log p(x,t)$ for all $(x,t)$ is equivalent to knowing $p(x,t)$ up to a normalizing constant (since $\log p$ can be recovered by integration, up to a constant). Since $p$ satisfies the Fokker-Planck equation, knowing the score at all points is equivalent to knowing the full PDE dynamics of the density. The score is the bridge between the PDE perspective (Fokker-Planck for densities) and the SDE perspective (stochastic trajectories of individual samples).

---

### Question 12 (8 pts) — Finite Differences and Numerical PDE Methods

**(a)** **Taylor expansion derivation of the second-derivative approximation.**

$$u(x + \Delta x) = u(x) + u'(x)\,\Delta x + \frac{u''(x)}{2}\,\Delta x^2 + \frac{u'''(x)}{6}\,\Delta x^3 + O(\Delta x^4)$$

$$u(x - \Delta x) = u(x) - u'(x)\,\Delta x + \frac{u''(x)}{2}\,\Delta x^2 - \frac{u'''(x)}{6}\,\Delta x^3 + O(\Delta x^4)$$

Adding these two expressions:

$$u(x+\Delta x) + u(x-\Delta x) = 2u(x) + u''(x)\,\Delta x^2 + O(\Delta x^4)$$

Solving for $u''$:

$$\boxed{u''(x) = \frac{u(x+\Delta x) - 2u(x) + u(x-\Delta x)}{\Delta x^2} + O(\Delta x^2)}$$

This is the **central difference** approximation, accurate to second order.

**(b)** The **CFL (Courant-Friedrichs-Lewy) condition** for the explicit forward-Euler discretization of the heat equation requires:

$$\frac{k\,\Delta t}{\Delta x^2} \leq \frac{1}{2}$$

If $\Delta t$ is too large, the numerical scheme becomes **unstable** — small errors are amplified at each time step instead of being damped, and the solution blows up.

**ML analogy:** This is identical to the **learning rate stability condition** in gradient descent. If the learning rate $\eta$ is too large relative to the curvature of the loss landscape (the largest eigenvalue $\lambda_{\max}$ of the Hessian), the updates overshoot and diverge. The condition $\eta < 2/\lambda_{\max}$ is the continuous analog of the CFL condition. Both come from requiring the amplification factor $|1 + h\lambda| < 1$ for all eigenvalues.

**(c)** **Crank-Nicolson** is an implicit method (averages forward and backward Euler). The tradeoff:

- **Cost per step:** Higher — requires solving a **tridiagonal linear system** at each time step (though this is efficient, $O(N)$ with the Thomas algorithm).
- **Stability:** **Unconditionally stable** — there is no restriction on $\Delta t / \Delta x^2$. One can take much larger time steps without blowing up.
- **Net efficiency:** Often more efficient overall, because the larger permissible time steps more than compensate for the extra per-step cost.

**(d)**

- **Advantage of learned solvers (e.g., Fourier Neural Operators):** Once trained, they solve PDEs in a **single forward pass** — orders of magnitude faster than iterative classical methods. This is especially powerful when solving the same PDE with many different initial/boundary conditions (amortized cost).
- **Risk:** They may fail to **generalize** to initial conditions far from the training distribution, and they provide **no guaranteed accuracy bounds**. A classical finite-difference solver may be slow but gives controllable error. A neural solver is fast but can silently produce incorrect results on out-of-distribution inputs.

---

### Question 13 (10 pts) — The Method of Characteristics

**(a)** For $u_t + 2u_x = 0$ with $u(x,0) = e^{-x^2}$:

The **characteristic equations** are $\dfrac{dx}{dt} = 2$, giving $x = 2t + x_0$ (lines of slope $1/2$ in the $(x,t)$-plane).

Along characteristics: $\dfrac{du}{dt} = u_t + 2u_x = 0$, so **$u$ is constant along each characteristic**.

The characteristic through $(x, t)$ originated at $x_0 = x - 2t$, so:

$$\boxed{u(x,t) = u(x - 2t, 0) = e^{-(x-2t)^2}}$$

The initial Gaussian profile translates to the right at speed $2$ without changing shape. The characteristics are **parallel lines** $x = 2t + x_0$.

**(b)** For $u_t + u\,u_x = 0$ with $u(x,0) = 1 - x$ on $[0,1]$:

The characteristics satisfy $\dfrac{dx}{dt} = u$, and $u$ is constant along each characteristic, so $\dfrac{dx}{dt} = u(x_0, 0) = 1 - x_0$.

$$x = x_0 + (1 - x_0)\,t$$

- At $x_0 = 0$: $x = t$ (speed $1$, fastest).
- At $x_0 = 1$: $x = 1$ (speed $0$, stationary).

The characteristics **converge** because faster waves (from the left, where $u$ is larger) catch up to slower ones (on the right). Solving for when characteristics cross: from $x = x_0 + (1-x_0)t = x_0(1-t) + t$, we get $\partial x/\partial x_0 = 1-t = 0$ at **$t = 1$**.

**A shock forms at $t = 1$.**

**(c)** When characteristics cross, two different values of $u$ are assigned to the same point — the **classical (smooth) solution becomes multi-valued**, which is physically impossible. The solution develops a **discontinuity (shock wave)** at the crossing point.

After shock formation, one needs the theory of **weak solutions** and **entropy conditions** (e.g., the Rankine-Hugoniot jump condition) to select the physically relevant solution. The classical solution ceases to exist, but the physics continues — shock waves are real phenomena (e.g., sonic booms, traffic jams).

**(d)** In **normalizing flows**, mode collapse occurs when many input points from the latent space get mapped to the same output region — the flow "compresses" probability mass into a small area. This is the generative model analog of **shock formation**: the mapping becomes nearly non-invertible, and the **Jacobian determinant approaches zero** in the collapsed region.

Just as shock formation means the characteristic map $x_0 \mapsto x(t)$ loses invertibility (multiple $x_0$ values map to the same $x$), mode collapse means the flow map $z \mapsto x = g_\theta(z)$ loses effective invertibility (many latent codes $z$ produce nearly identical outputs $x$). Both represent a breakdown of the smooth, one-to-one correspondence between input and output.

---

### Question 14 (10 pts) — Diffusion Models: The Full Picture

**(a)** Fill in the blanks for the diffusion model pipeline:

| Stage | Description |
|---|---|
| **Forward process** | Add Gaussian noise progressively, transforming $p_{\text{data}}$ into approximately $\mathcal{N}(0, I)$ |
| **Forward PDE** | The density evolution is governed by the **Fokker-Planck equation** |
| **Training target** | The neural network learns the **score function** $\nabla_x \log p(x,t)$ |
| **Reverse process** | Starting from $\mathcal{N}(0, I)$, integrate the **reverse-time SDE** backward |
| **Deterministic alternative** | The **probability flow ODE** gives the same marginals without stochasticity |
| **Output** | Samples from (approximately) $p_{\text{data}}$ |

**(b)** The **noise schedule** $\beta(t)$ determines how noise is distributed across time steps.

A **linear schedule** increases $\beta$ uniformly, which wastes many steps at high noise levels where the distribution is already nearly Gaussian — these steps are uninformative because the model is just learning "it's all noise."

A **cosine schedule** (proposed by Nichol & Dhariwal) allocates more steps at **intermediate noise levels** where the model is actually learning meaningful structure — the transition region between "clearly data" and "clearly noise." This improves sample quality and training efficiency by focusing model capacity where it matters most.

**(c)** **DDIM** (Denoising Diffusion Implicit Models) uses the **probability flow ODE** rather than the stochastic SDE.

- **ODE trajectories are smooth, deterministic curves** that can be accurately approximated with larger step sizes or adaptive solvers.
- **SDE trajectories** include a $\sqrt{\Delta t}$ noise term that requires many small steps for accuracy — the stochastic component introduces $O(\sqrt{\Delta t})$ error per step.
- The deterministic nature means **intermediate steps can be skipped** without accumulating stochastic error. DDIM can produce good samples in 10-50 steps versus the 1000 steps typically needed for DDPM's SDE.

**(d)** Increasing the **classifier-free guidance weight** $w$ is analogous to **lowering the temperature** $T$ in a Boltzmann distribution $p(x) \propto e^{-E(x)/T}$.

Higher $w$ **sharpens the conditional distribution**, concentrating probability on the samples most consistent with the conditioning signal (text prompt, class label). The effect:

- **Higher $w$:** More confident, higher-fidelity, more "stereotypical" samples — but less diversity. Risk of **mode collapse** and artifacts.
- **Lower $w$:** More diverse, more creative samples — but potentially less faithful to the conditioning.

This is the **quality-diversity tradeoff**, directly analogous to the temperature-entropy tradeoff in statistical mechanics.

---

### Question 15 (10 pts) — Synthesis: The PDE Landscape of Generative AI

**(a)** PDE-to-ML correspondence table:

| PDE | ML Analog | Connection |
|---|---|---|
| **Heat equation** $u_t = k\,u_{xx}$ | Forward diffusion process | Adding noise = smoothing the probability density. The heat equation governs how $p(x,t)$ evolves as noise is added. |
| **Wave equation** $u_{tt} = c^2 u_{xx}$ | Signal propagation through network layers | Information travels at finite speed (bounded receptive field), layer by layer, analogous to waves propagating along characteristics. |
| **Laplace's equation** $\nabla^2 u = 0$ | Converged training (steady state) | A trained network at equilibrium satisfies $\nabla_\theta L = 0$ — the gradient flow has reached its steady state, analogous to the time-independent solution of the heat equation. |

**(b)** When to use SDE vs. PDE perspectives:

- **At inference (sampling):** Use the **SDE** (or ODE) — simulate a single stochastic (or deterministic) trajectory from noise to a data sample. The SDE perspective works with individual samples.
- **For the training objective:** The **PDE** (Fokker-Planck) perspective is natural — it describes how the entire distribution $p(x,t)$ evolves, which is what the score matching loss is derived from.
- **For theoretical analysis:** The **PDE** perspective is essential for analyzing convergence properties, understanding how distributions evolve, and proving that the forward and reverse processes are inverses of each other.

**(c)** **Flow matching** directly uses the **continuity equation**:

$$\frac{\partial p}{\partial t} + \text{div}(v\,p) = 0$$

Rather than defining a noising process and learning its score, flow matching **directly specifies a velocity field** $v(x,t)$ that transports the data distribution along straight (or simple) paths to the noise distribution.

This is **simpler** than score-based diffusion because:
- It avoids the SDE/reverse-SDE machinery entirely.
- It does not require the score function — instead, it learns $v$ directly.
- The underlying PDE is the **transport/continuity equation**, not the Fokker-Planck equation.
- Straight transport paths are easier for neural networks to learn than the curved paths induced by diffusion.

**(d)** **Critical evaluation** of the claim "all generative models are solving PDEs":

- **Diffusion models:** The claim is **strongest** here. The forward process is literally governed by the Fokker-Planck equation, and sampling solves the reverse SDE/ODE. The PDE connection is exact, not metaphorical.
- **Normalizing flows:** **Strong** connection. The continuous normalizing flow ODE $dx/dt = f_\theta(x,t)$ induces a density evolution via the continuity equation. The change-of-variables formula is the PDE at work.
- **VAEs:** **Partial** truth. The encoder/decoder define a mapping between distributions, but the ELBO objective doesn't directly involve a PDE. The connection is more structural (transport between distributions) than mathematical (solving a differential equation).
- **GANs:** The analogy is **weaker**. The generator implicitly transports noise to data, but the adversarial training procedure is not a differential equation. The Wasserstein GAN has connections to optimal transport, which does involve PDEs (the Monge-Ampere equation), but standard GANs don't directly solve PDEs.
- **Autoregressive models:** The analogy **breaks down**. These factorize the joint distribution into a chain of conditionals $p(x_1)p(x_2|x_1)\cdots$ — this is a probabilistic chain, not a differential equation. There is no continuous transformation between distributions, no PDE to solve.

**Conclusion:** The PDE perspective captures continuous transformations between distributions powerfully and precisely, but it misses discrete and sequential generation paradigms. It is a lens, not the whole picture.

**(e)** *Sample full-credit response:*

"The heat equation's smoothing property is exactly what makes the forward process work — it is not just 'adding noise,' it is **systematically destroying information at different frequencies**. High-frequency details (fine textures, sharp edges) are erased first (the $e^{-n^2 t}$ decay of Fourier modes), and low-frequency structure (overall composition, color palette) persists longest. Reversing this process — the generative step — means **reconstructing information from coarse to fine**, first establishing the global structure, then progressively adding detail. This is why diffusion model samples look blurry at early reverse steps and gain sharpness as $t \to 0$. The mathematics of Fourier analysis and the heat equation do not merely describe what diffusion models do — they explain *why* the multi-scale, coarse-to-fine generation process is natural and effective."

*Any thoughtful insight connecting PDE theory to generative modeling, demonstrating genuine synthesis of the material, earns full marks.*

---

**End of Answer Key — Total: 150 points**
