# Lesson 18: Systems of ODEs and Phase Portraits

[<- Previous](lesson-17-laplace-transform.md) | [Back to TOC](../README.md) | [Next: 3D Geometry ->](lesson-19-3d-geometry.md)

---

## Core Learning

- Formulate systems of ODEs as matrix equations: dx/dt = Ax
- Solve linear systems using the eigenvalue method: find eigenvalues and eigenvectors of A, build the general solution
- Classify 2D phase portraits by eigenvalue type: stable/unstable nodes, saddle points, stable/unstable spirals, and centers
- Understand the matrix exponential e^{At} as the formal solution and its connection to diagonalization
- Solve nonhomogeneous systems dx/dt = Ax + g(t) using variation of parameters or undetermined coefficients
- Read phase portraits to predict qualitative long-term behavior without solving

## Watch --- Primary

- **Trefor Bazett --- ODE Course (Systems of ODEs, Phase Portraits, Matrix Exponential)**
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxde-SlgmWlCmNHroIWtujBw
  - *The systems section of the playlist. Bazett's visual treatment of phase portraits is particularly strong --- he draws the trajectories and explains how eigenvalues determine the portrait type. This connects directly back to the eigenvalue work from Phase 1 linear algebra.*

## Watch --- Secondary

- **Steve Brunton --- "Linearizing Around Fixed Points" and "Phase Portraits"**
  - https://www.youtube.com/c/Eigensteve
  - *Brunton's dynamical systems playlist covers linearization and phase portrait classification with an applied/data-driven perspective.*
- **3Blue1Brown --- "Differential equations, studying the unsolvable"**
  - https://www.youtube.com/watch?v=p_di4Zn4wz4
  - *The phase portrait section near the end of this video provides beautiful visual intuition for how systems of ODEs create flow patterns.*

## Read

- **Strogatz, "Nonlinear Dynamics and Chaos"** --- Chapter 5 (Linear Systems) and Chapter 6.1-6.3 (Phase Plane)
  - *The definitive treatment of 2D phase portrait classification. Strogatz organizes everything by the trace-determinant plane, giving a complete map of all possible behaviors.*
- **Paul's Online Math Notes --- Systems of Differential Equations**
  - https://tutorial.math.lamar.edu/Classes/DE/SystemsDE.aspx
  - *Mechanical walkthrough of the eigenvalue method with worked examples for each case.*

## Key Equations

**Linear system in matrix form:**

$$\frac{d\mathbf{x}}{dt} = A\mathbf{x}, \quad \mathbf{x}(0) = \mathbf{x}_0$$

**Solution via eigenvalues/eigenvectors:**

If $A$ has eigenvalues $\lambda_1, \lambda_2$ with eigenvectors $\mathbf{v}_1, \mathbf{v}_2$:

$$\mathbf{x}(t) = c_1 e^{\lambda_1 t}\mathbf{v}_1 + c_2 e^{\lambda_2 t}\mathbf{v}_2$$

**Matrix exponential:**

$$\mathbf{x}(t) = e^{At}\mathbf{x}_0, \quad \text{where} \quad e^{At} = I + At + \frac{(At)^2}{2!} + \frac{(At)^3}{3!} + \cdots$$

If $A = PDP^{-1}$ (diagonalizable), then $e^{At} = P\, e^{Dt}\, P^{-1}$.

**Phase portrait classification (2D):**

| Eigenvalues | Portrait Type |
|-------------|---------------|
| $\lambda_1, \lambda_2 < 0$ (both real negative) | Stable node |
| $\lambda_1, \lambda_2 > 0$ (both real positive) | Unstable node |
| $\lambda_1 < 0 < \lambda_2$ (real, opposite sign) | Saddle point |
| $\alpha \pm \beta i$, $\alpha < 0$ | Stable spiral |
| $\alpha \pm \beta i$, $\alpha > 0$ | Unstable spiral |
| $\pm \beta i$ (pure imaginary) | Center (closed orbits) |

**Trace-determinant classification:**

For $A$ with trace $\tau = \lambda_1 + \lambda_2$ and determinant $\Delta = \lambda_1 \lambda_2$:
- $\Delta < 0$: saddle
- $\Delta > 0$, $\tau < 0$: stable (node if $\tau^2 > 4\Delta$, spiral if $\tau^2 < 4\Delta$)
- $\Delta > 0$, $\tau > 0$: unstable
- $\Delta > 0$, $\tau = 0$: center

## Block A Capstone Project — ODE System Solver & Training Dynamics (~6h)

Build a C++ numerical solver that generates trajectory data, then use Python to classify, visualize, and connect the dynamics to gradient-based optimization.

---

### Part 1 — C++ Numerical Solvers (~2.5h)

**Goal:** Implement two ODE integrators from scratch and generate trajectory data for six canonical 2x2 systems.

**1a. Implement Euler and RK4 as generic solvers**

Write two solver functions that accept any ODE of any dimension (not hardcoded to 2D). Each takes: a right-hand-side function `f(t, x)`, an initial condition `x0`, a time interval `[t0, tf]`, and a step size `dt`. Returns the full trajectory as a list of states.

**1b. Solve six canonical systems**

For each matrix below, solve dx/dt = Ax from **6 initial conditions** evenly spaced on a circle of radius 2. Use RK4 with dt = 0.01, t in [0, 10]. Write each trajectory to CSV with columns: `t, x1, x2, ic_index`.

**Stable node** — A = [[-2, 0], [0, -1]]. All trajectories converge to origin, faster along x1.

**Unstable node** — A = [[1, 0], [0, 2]]. All trajectories flee origin.

**Saddle** — A = [[1, 0], [0, -2]]. Trajectories approach along x2-axis, flee along x1.

**Stable spiral** — A = [[-0.2, 1], [-1, -0.2]]. Inward-spiraling orbits.

**Unstable spiral** — A = [[0.2, 1], [-1, 0.2]]. Outward-spiraling orbits.

**Center** — A = [[0, 1], [-1, 0]]. Closed elliptical orbits.

**1c. Convergence check**

Pick the stable spiral system. Run from one initial condition with both Euler and RK4 at dt = 0.1, 0.01, 0.001. Use the dt = 0.0001 RK4 result as ground truth. Output a CSV of `method, dt, error`. You should see Euler's error drop linearly with dt (order 1) and RK4's error drop as dt^4 (order 4).

---

### Part 2 — Phase Portrait Gallery (Python, ~1.5h)

**Goal:** Read the C++ output, auto-classify each system, and produce a 2x3 gallery.

**2a. Trace-determinant classifier**

Write a function that classifies a 2x2 matrix using trace (tau) and determinant (Delta):

- Delta < 0 → **saddle**
- Delta > 0, tau < 0, tau^2 > 4\*Delta → **stable node**
- Delta > 0, tau < 0, tau^2 < 4\*Delta → **stable spiral**
- Delta > 0, tau > 0, tau^2 > 4\*Delta → **unstable node**
- Delta > 0, tau > 0, tau^2 < 4\*Delta → **unstable spiral**
- Delta > 0, tau = 0 → **center**

Verify it correctly labels all six matrices.

**2b. Phase portrait gallery**

Plot all 6 trajectories per system on one subplot. Include arrowheads for flow direction, mark the origin (filled = stable, open = unstable), and title each subplot with the classification and eigenvalues. Arrange as a 2x3 grid.

**2c. Convergence plot**

Plot log(error) vs log(dt) for Euler and RK4 from the convergence CSV. The slopes should be ~1 and ~4 respectively — annotate them.

---

### Part 3 — Gradient Descent as a Dynamical System (Python, ~2h)

**Goal:** Show that gradient descent is just Euler's method on a continuous ODE, and that momentum turns it into a second-order system.

**3a. Gradient flow vs gradient descent**

Define a 2D quadratic loss with condition number 50:

$$\mathcal{L}(\mathbf{x}) = \tfrac{1}{2}\mathbf{x}^T H \mathbf{x}, \quad H = \text{diag}(50, 1)$$

The continuous gradient flow is dx/dt = -Hx. Solve it with RK4 (reimplement in NumPy) from x0 = (8, 8).

Now run discrete gradient descent — x\_{k+1} = x\_k - eta \* H \* x\_k — which is literally Euler's method with step size eta. Run three learning rates on the same contour plot:

- **eta = 0.005** — slow but smooth convergence
- **eta = 0.035** — visible zigzagging along the steep eigenvalue direction
- **eta = 0.041** — diverges (because eta > 2/lambda\_max = 0.04)

Overlay all three discrete paths plus the continuous flow on loss-contour ellipses. This single figure should make the Euler-GD connection viscerally obvious.

**3b. Momentum comparison**

Gradient descent with momentum (mu = 0.9):

- v\_{k+1} = mu \* v\_k - eta \* H \* x\_k
- x\_{k+1} = x\_k + v\_{k+1}

Produce a **side-by-side figure**: left panel shows the (x1, x2) trajectory for no-momentum vs momentum, right panel shows loss vs iteration for both. Use eta = 0.035. Momentum should converge significantly faster despite the ill-conditioning.

---

### Deliverables

- [ ] C++ solver compiles and produces trajectory + convergence CSVs
- [ ] 2x3 phase portrait gallery with auto-classification labels
- [ ] Convergence plot confirming solver accuracy orders
- [ ] Gradient flow vs GD contour plot (3 learning rates + continuous)
- [ ] Momentum vs no-momentum comparison figure

## ML and Alignment Connection

The training dynamics of linear networks are literally linear ODE systems. For a linear model minimizing squared loss, the gradient flow reduces to dW/dt = AW + b for some matrix A determined by the data covariance. The eigenvalues of A (equivalently, of the Hessian of the loss) completely determine whether training converges, how fast it converges, and what path it takes. A stable node means all parameter directions converge, at rates set by the eigenvalues. A saddle means some directions converge while others diverge --- this is what happens at saddle points in the loss landscape, and understanding saddle escape dynamics is critical for deep learning theory. The condition number (ratio of largest to smallest eigenvalue magnitude) determines how much the convergence speeds differ across directions, which directly explains the zigzagging behavior of vanilla gradient descent on ill-conditioned problems.

Phase portraits visualize how different initializations lead to different training outcomes, which is directly relevant to alignment. If the loss landscape has multiple stable equilibria (trained models), the phase portrait shows the basins of attraction --- which initializations lead to which final models. The separatrices (boundaries between basins) are the critical structures: a tiny change in initialization near a separatrix can lead to a qualitatively different trained model. For alignment, this means understanding whether the basin of "aligned behavior" is large and robust or small and fragile. The eigenvalue structure of the Hessian at each equilibrium tells you about the local geometry --- whether the basin is wide and flat (robust alignment) or narrow and sharp (fragile alignment that could be lost with small perturbations).
