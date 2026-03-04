# Lesson 18: Systems of ODEs and Phase Portraits

[<- Previous](lesson-17-laplace-transform.md) | [Back to TOC](../README.md) | [Next: Partial Derivatives ->](lesson-19-partial-derivatives.md)

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

## Do

**Phase Portrait Plotter with Eigenvalue Classification**

Build a phase portrait plotter for 2D linear systems dx/dt = Ax. Classify the origin automatically based on the eigenvalues, and color trajectories by type.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def classify_fixed_point(A):
    """
    Compute eigenvalues of 2x2 matrix A and classify the origin.
    Returns: (eigenvalues, classification_string)

    Classifications: 'stable node', 'unstable node', 'saddle',
                     'stable spiral', 'unstable spiral', 'center'
    """
    eigenvalues = np.linalg.eigvals(A)
    # TODO: classify based on real/imaginary parts
    pass

def plot_phase_portrait(A, x_range=(-3, 3), y_range=(-3, 3),
                         n_trajectories=12, t_span=(0, 10)):
    """
    Plot the phase portrait for dx/dt = Ax.

    1. Draw the vector field using quiver
    2. Compute and plot trajectories from initial conditions
       arranged in a circle around the origin
    3. Plot eigenvectors as dashed lines (for real eigenvalues)
    4. Title the plot with the classification and eigenvalues
    """
    eigvals, classification = classify_fixed_point(A)

    # TODO: Create meshgrid for vector field
    # TODO: Compute dx/dt = Ax at each grid point
    # TODO: Plot with plt.streamplot or plt.quiver

    # TODO: Generate initial conditions on a circle
    # TODO: Solve ODE forward (and backward for saddles)
    #       using solve_ivp
    # TODO: Plot trajectories, colored by type

    # TODO: If eigenvalues are real, plot eigenvector directions

    plt.title(f"{classification}\neigenvalues: {eigvals}")
    pass

# --- Test on these matrices (one of each type) ---

matrices = {
    'Stable node':    np.array([[-2, 0], [0, -1]]),
    'Unstable node':  np.array([[1, 0], [0, 2]]),
    'Saddle':         np.array([[1, 0], [0, -2]]),
    'Stable spiral':  np.array([[-0.5, 2], [-2, -0.5]]),
    'Unstable spiral':np.array([[0.5, 2], [-2, 0.5]]),
    'Center':         np.array([[0, 1], [-1, 0]]),
}

# Tasks:
# 1. Create a 2x3 grid of subplots, one phase portrait per matrix
# 2. Verify your classifier labels each one correctly
# 3. For the saddle: plot the stable and unstable manifolds
#    (eigenvector directions) as dashed lines
# 4. For spirals: observe the rotation direction (clockwise vs
#    counterclockwise) and relate to the sign of the off-diagonal
# 5. Create one more plot: A = [[-1, 5], [0, -1]] (a defective
#    node with repeated eigenvalue). Observe the behavior.

# --- Bonus: Training Dynamics Visualization ---
# Consider gradient descent on L(w1, w2) = 0.5*(a*w1^2 + b*w2^2)
# The gradient flow is dw/dt = -(a*w1, b*w2), so A = diag(-a, -b).
# Plot phase portraits for:
#   a=1, b=1   (isotropic: perfect circle contours, straight paths)
#   a=10, b=1  (anisotropic: elongated contours, curved paths)
#   a=1, b=-1  (saddle point in loss: unstable direction exists)
# Overlay loss contours on the phase portrait.
```

**Tasks:**
1. Implement the classifier and verify on all six matrix types
2. Produce a 2x3 gallery of phase portraits, one per type
3. Add eigenvector lines for real-eigenvalue cases
4. Create the training dynamics visualization showing how eigenvalue ratio affects convergence paths

## ML and Alignment Connection

The training dynamics of linear networks are literally linear ODE systems. For a linear model minimizing squared loss, the gradient flow reduces to dW/dt = AW + b for some matrix A determined by the data covariance. The eigenvalues of A (equivalently, of the Hessian of the loss) completely determine whether training converges, how fast it converges, and what path it takes. A stable node means all parameter directions converge, at rates set by the eigenvalues. A saddle means some directions converge while others diverge --- this is what happens at saddle points in the loss landscape, and understanding saddle escape dynamics is critical for deep learning theory. The condition number (ratio of largest to smallest eigenvalue magnitude) determines how much the convergence speeds differ across directions, which directly explains the zigzagging behavior of vanilla gradient descent on ill-conditioned problems.

Phase portraits visualize how different initializations lead to different training outcomes, which is directly relevant to alignment. If the loss landscape has multiple stable equilibria (trained models), the phase portrait shows the basins of attraction --- which initializations lead to which final models. The separatrices (boundaries between basins) are the critical structures: a tiny change in initialization near a separatrix can lead to a qualitatively different trained model. For alignment, this means understanding whether the basin of "aligned behavior" is large and robust or small and fragile. The eigenvalue structure of the Hessian at each equilibrium tells you about the local geometry --- whether the basin is wide and flat (robust alignment) or narrow and sharp (fragile alignment that could be lost with small perturbations).
