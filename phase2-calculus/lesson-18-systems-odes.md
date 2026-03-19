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

## Block A Capstone Project — ODE System Solver & Training Dynamics (~4h)

Build a complete pipeline: a C++ numerical solver that generates trajectory data, and a Python analysis layer that classifies, visualizes, and connects the dynamics to gradient-based optimization.

---

### Part 1 — C++ Numerical Solvers (1–1.5h)

**Goal:** Implement two ODE integrators from scratch and generate trajectory data for six canonical 2×2 systems.

**1a. Implement Euler and RK4 as generic solvers**

Write two functions with the signature:

```
std::vector<State> solve(
    std::function<State(double, State)> f,   // the ODE: dx/dt = f(t, x)
    State x0,                                 // initial condition
    double t0, double tf,                     // time interval
    double dt                                 // step size
);
```

where `State` is a `std::vector<double>` (or a small fixed-size vector). Both Euler and RK4 should work for *any* dimension, not just 2D.

**Recall — the RK4 update:**

$$k_1 = f(t_n,\, \mathbf{x}_n)$$
$$k_2 = f\!\left(t_n + \tfrac{h}{2},\, \mathbf{x}_n + \tfrac{h}{2}k_1\right)$$
$$k_3 = f\!\left(t_n + \tfrac{h}{2},\, \mathbf{x}_n + \tfrac{h}{2}k_2\right)$$
$$k_4 = f(t_n + h,\, \mathbf{x}_n + h\,k_3)$$
$$\mathbf{x}_{n+1} = \mathbf{x}_n + \tfrac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

**1b. Solve six canonical systems**

For each of the following matrices $A$, solve $d\mathbf{x}/dt = A\mathbf{x}$ from **8 initial conditions** evenly spaced on a circle of radius 2 (i.e., $\mathbf{x}_0 = 2(\cos\theta,\, \sin\theta)$ for $\theta = 0, \pi/4, \pi/2, \ldots, 7\pi/4$):

| Label | Matrix $A$ | Expected behavior |
|-------|-----------|-------------------|
| Stable node | $\begin{pmatrix} -2 & 0 \\ 0 & -1 \end{pmatrix}$ | All trajectories → origin, faster along $x_1$ |
| Unstable node | $\begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$ | All trajectories flee origin |
| Saddle | $\begin{pmatrix} 1 & 0 \\ 0 & -2 \end{pmatrix}$ | Approach along $x_2$-axis, flee along $x_1$ |
| Stable spiral | $\begin{pmatrix} -0.2 & 1 \\ -1 & -0.2 \end{pmatrix}$ | Inward-spiraling orbits |
| Unstable spiral | $\begin{pmatrix} 0.2 & 1 \\ -1 & 0.2 \end{pmatrix}$ | Outward-spiraling orbits |
| Center | $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ | Closed elliptical orbits |

Use RK4 with $dt = 0.01$, $t \in [0, 10]$. Write each trajectory to CSV with columns: `t, x1, x2`.

**1c. Convergence validation**

For the stable spiral system, run from a single initial condition with Euler at $dt = 0.1, 0.01, 0.001$ and RK4 at the same step sizes. Output a CSV of final-state error vs $dt$ (use the $dt = 0.0001$ RK4 solution as ground truth). This should show Euler's $O(h)$ convergence vs RK4's $O(h^4)$.

**Output structure:**

```
output/
├── trajectories/
│   ├── stable_node.csv       # columns: t, x1, x2, ic_index
│   ├── unstable_node.csv
│   ├── saddle.csv
│   ├── stable_spiral.csv
│   ├── unstable_spiral.csv
│   └── center.csv
└── convergence.csv            # columns: method, dt, error
```

---

### Part 2 — Phase Portrait Gallery & Auto-Classification (1h)

**Goal:** Read the C++ output, classify each system automatically, and produce a publication-quality 2×3 figure.

**2a. Eigenvalue-based auto-classifier**

Write a function that takes a 2×2 matrix $A$ and returns a classification string by computing $\text{tr}(A)$ and $\det(A)$:

```
               ┌─────────────────────────────────────────────┐
               │           Trace-Determinant Plane            │
               │                                             │
         det   │              τ² = 4Δ                        │
          ▲    │             ╱       ╲                        │
          │    │   Stable   ╱ Stable  ╲  Unstable             │
          │    │   Spiral  ╱  Node     ╲  Spiral              │
          │    │          ╱             ╲                      │
          │    │─────────╱───────────────╲────── Δ > 0        │
          │    │        ╱    Centers      ╲                   │
          │    │───────────────┬───────────────── Δ = 0       │
          │    │               │                              │
          │    │    Saddles    │    Saddles        Δ < 0       │
          │    │               │                              │
          └────┼───────────────┼────────────────▶ trace       │
               │            τ = 0                             │
               └─────────────────────────────────────────────┘
```

The function should return one of: `"stable node"`, `"unstable node"`, `"saddle"`, `"stable spiral"`, `"unstable spiral"`, `"center"`. Verify it correctly classifies all six matrices from Part 1.

**2b. Phase portrait gallery**

For each system, plot all 8 trajectories on one axis with:
- Arrowheads along trajectories showing flow direction (use `quiver` or `annotate`)
- Eigenvector lines overlaid as dashed lines for real-eigenvalue cases (nodes and saddles)
- The origin marked, with a filled dot (stable) or open dot (unstable)
- Title showing the matrix, eigenvalues, and your classifier's label
- Consistent axis limits across all six plots

Arrange as a **2×3 grid** (top row: node types + saddle; bottom row: spirals + center).

**2c. Convergence plot**

From the convergence CSV, plot log(error) vs log(dt) for both methods. Fit lines and annotate the slopes — you should see slope ≈ 1 for Euler and slope ≈ 4 for RK4. This is a visual proof that your solvers have the correct order of accuracy.

---

### Part 3 — Gradient Descent as Dynamical System (1–1.5h)

**Goal:** Show that gradient descent is a discretization of a continuous ODE, and that momentum is a second-order system.

**3a. Gradient flow on a quadratic loss**

Define a 2D quadratic loss with an ill-conditioned Hessian:

$$\mathcal{L}(\mathbf{x}) = \frac{1}{2}\mathbf{x}^T H \mathbf{x}, \quad H = \begin{pmatrix} 50 & 0 \\ 0 & 1 \end{pmatrix}$$

This has condition number $\kappa = 50$, meaning one direction is 50× steeper than the other.

The continuous gradient flow ODE is:

$$\frac{d\mathbf{x}}{dt} = -\nabla\mathcal{L} = -H\mathbf{x}$$

Use your RK4 solver (via Python's `subprocess` calling the C++ binary, or reimplement in NumPy) to solve this ODE from $\mathbf{x}_0 = (8, 8)$. Plot the trajectory overlaid on loss contours (use `plt.contour`). The trajectory should flow smoothly toward the origin, initially diving along the steep direction.

**3b. Euler's method ≈ gradient descent**

Now run discrete gradient descent with a fixed learning rate:

$$\mathbf{x}_{k+1} = \mathbf{x}_k - \eta\, H\mathbf{x}_k$$

This is literally Euler's method on the gradient flow ODE with step size $\eta$.

Run three learning rates: $\eta = 0.005$ (slow, stable), $\eta = 0.035$ (zigzagging), $\eta = 0.041$ (divergent — why?). Plot all three on the same contour plot alongside the continuous flow. The critical learning rate for stability is $\eta < 2/\lambda_{\max} = 2/50 = 0.04$.

**Expected output — a figure showing:**

```
    x₂ ▲
       │   ╭─── continuous flow (smooth curve to origin)
       │  ╱
       │ ╱   ╱╲╱╲  ← η=0.035 zigzags along steep direction
       │╱   ╱
       ●───╱────────── η=0.005 (slow but smooth)
       │
       │        η=0.041 spirals outward and diverges
       └──────────────────▶ x₁
              (loss contours as ellipses)
```

**3c. Momentum as a damped oscillator**

Gradient descent with momentum is:

$$\mathbf{v}_{k+1} = \mu\,\mathbf{v}_k - \eta\,\nabla\mathcal{L}(\mathbf{x}_k)$$
$$\mathbf{x}_{k+1} = \mathbf{x}_k + \mathbf{v}_{k+1}$$

This discretizes the second-order ODE (a damped oscillator):

$$\ddot{\mathbf{x}} + (1-\mu)\,\dot{\mathbf{x}} + \eta\, H\mathbf{x} = 0$$

Rewrite this as a first-order system by introducing $\mathbf{y} = (\mathbf{x}, \dot{\mathbf{x}})$ — this is a 4D linear ODE.

Produce a **2×2 comparison figure**:

| | No Momentum ($\mu = 0$) | With Momentum ($\mu = 0.9$) |
|---|---|---|
| **Phase portrait** $(x_1, x_2)$ | Zigzagging path | Smoother, faster convergence |
| **Loss vs iteration** | Slow, possibly oscillating | Faster decay |

Use $\eta = 0.035$ for both. The momentum version should reach the minimum in significantly fewer steps despite the ill-conditioning.

**3d. Learning rate stability region (bonus)**

For the 2D system with Hessian $H$, the discrete update matrix is $M = I - \eta H$. Gradient descent converges iff all eigenvalues of $M$ satisfy $|\lambda| < 1$.

Plot the spectral radius $\rho(M) = \max|\lambda_i(M)|$ as a function of $\eta$ for $\eta \in [0, 0.05]$. Mark the critical value $\eta^* = 2/\lambda_{\max}$ where stability is lost. Then do the same plot for the momentum update — show how momentum shifts the stability boundary.

---

### Deliverables Checklist

- [ ] C++ solver compiles and runs, producing all CSV files
- [ ] Convergence plot confirms $O(h)$ for Euler, $O(h^4)$ for RK4
- [ ] 2×3 phase portrait gallery with correct classifications
- [ ] Gradient flow + GD comparison plot showing stability/instability
- [ ] Momentum vs no-momentum comparison (phase portrait + loss curve)
- [ ] All figures saved as PNG at 200+ DPI

## ML and Alignment Connection

The training dynamics of linear networks are literally linear ODE systems. For a linear model minimizing squared loss, the gradient flow reduces to dW/dt = AW + b for some matrix A determined by the data covariance. The eigenvalues of A (equivalently, of the Hessian of the loss) completely determine whether training converges, how fast it converges, and what path it takes. A stable node means all parameter directions converge, at rates set by the eigenvalues. A saddle means some directions converge while others diverge --- this is what happens at saddle points in the loss landscape, and understanding saddle escape dynamics is critical for deep learning theory. The condition number (ratio of largest to smallest eigenvalue magnitude) determines how much the convergence speeds differ across directions, which directly explains the zigzagging behavior of vanilla gradient descent on ill-conditioned problems.

Phase portraits visualize how different initializations lead to different training outcomes, which is directly relevant to alignment. If the loss landscape has multiple stable equilibria (trained models), the phase portrait shows the basins of attraction --- which initializations lead to which final models. The separatrices (boundaries between basins) are the critical structures: a tiny change in initialization near a separatrix can lead to a qualitatively different trained model. For alignment, this means understanding whether the basin of "aligned behavior" is large and robust or small and fragile. The eigenvalue structure of the Hessian at each equilibrium tells you about the local geometry --- whether the basin is wide and flat (robust alignment) or narrow and sharp (fragile alignment that could be lost with small perturbations).
