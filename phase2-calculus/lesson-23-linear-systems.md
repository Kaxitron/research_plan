# Lesson 23: Linear Systems and Phase Portraits — Eigenvalues Determine Everything

[← Intro to ODEs](lesson-22-intro-odes.md) | [Back to TOC](../README.md) | [Next: Gradient Flow →](lesson-24-gradient-flow.md)

---

> **Why this lesson exists:** Linear ODEs (dx/dt = Ax) are the one case where we can solve everything completely — and the answer is entirely determined by the eigenvalues of A. Since the behavior near any fixed point of a nonlinear system is governed by its linearization (the Jacobian), eigenvalue analysis is the universal tool for understanding local dynamics. You already know eigenvalues from Lesson 8. Now you'll see what they *do* — they control whether systems converge, diverge, oscillate, or spiral. This is the mathematical foundation for understanding training stability.

## 🎯 Core Concepts

### Linear Systems: dx/dt = Ax

- **The simplest 2D system:** dx/dt = ax + by, dy/dt = cx + dy, or in matrix form: d**x**/dt = A**x** where A is a 2×2 matrix. The entire behavior of this system is determined by the eigenvalues of A.
- **Why linear systems matter:** even for nonlinear systems (like gradient flow on a complicated loss), the behavior *near a fixed point* is determined by the linearization — the Jacobian matrix evaluated at that point. So understanding linear systems gives you local behavior everywhere.
- **The solution:** x(t) = e^{At}x(0), where e^{At} is the matrix exponential. You don't need to compute this directly. What matters is: if A has eigenvalues λ₁, λ₂ with eigenvectors v₁, v₂, then the solution is x(t) = c₁e^{λ₁t}v₁ + c₂e^{λ₂t}v₂. Each eigendirection evolves independently, at a rate determined by its eigenvalue.

### The Eigenvalue Classification — A Complete Map

The eigenvalues of A determine the **phase portrait** — the complete qualitative picture of all trajectories:

**Real eigenvalues, both negative (λ₁ < λ₂ < 0):** **Stable node.** All trajectories converge to the origin. They approach along the slow eigendirection (the one with the smaller |λ|). This is what a well-conditioned loss minimum looks like — gradient descent converges from all directions.

**Real eigenvalues, both positive (0 < λ₁ < λ₂):** **Unstable node.** All trajectories flee the origin. This is a local maximum of the loss — training always escapes.

**Real eigenvalues, opposite signs (λ₁ < 0 < λ₂):** **Saddle point.** Trajectories approach along the stable eigendirection (λ₁ < 0) and flee along the unstable eigendirection (λ₂ > 0). Almost all trajectories eventually escape. Saddle points are the dominant critical points in high-dimensional loss landscapes.

**Complex eigenvalues (λ = α ± βi):**
- α < 0: **Stable spiral.** Trajectories spiral inward to the origin. This happens when the loss landscape has rotational character near a minimum — the condition number and the Hessian's off-diagonal structure create oscillation.
- α > 0: **Unstable spiral.** Trajectories spiral outward.
- α = 0: **Center.** Trajectories are closed orbits — they cycle forever without converging or diverging. This is the boundary between stable and unstable.

### Condition Number Revisited

- **You learned in Lesson 11** that the condition number κ = |λ_max|/|λ_min| measures how "elongated" the transformation is. Now you see this dynamically: for a stable node with eigenvalues -1 and -100, the system converges 100x faster along one direction than another. Trajectories slam into the slow direction and then crawl along it.
- **For gradient descent on L = w₁²/2 + 50w₂²/2:** the Hessian eigenvalues are 1 and 100 (κ = 100). Gradient flow converges along w₂ in ~0.01 time units but along w₁ in ~1 time unit. The zigzag you see in gradient descent plots is exactly the mismatched eigenvalue scales causing the trajectory to bounce off the steep walls of the elongated bowl.
- **Adam and preconditioning** effectively equalize the eigenvalues, turning an elongated bowl into a round one. In phase portrait terms: they transform a badly-conditioned stable node into a well-conditioned one.

### The Jacobian and Linearization

- **For nonlinear systems dx/dt = f(x):** the behavior near a fixed point x* is determined by the **Jacobian matrix** J = ∂f/∂x evaluated at x*. The Jacobian is the matrix of all partial derivatives — it IS the linear approximation to f near x*.
- **The Hartman-Grobman theorem:** if all eigenvalues of J have nonzero real parts (no purely imaginary eigenvalues), then the nonlinear system looks qualitatively identical to the linear system dx/dt = Jx near the fixed point. The phase portrait of the linearization IS the local phase portrait of the full nonlinear system.
- **For gradient flow on a loss L:** the Jacobian of -∇L is the negative Hessian -H. So the eigenvalues of the Hessian at a critical point determine the local training dynamics. Positive Hessian eigenvalues → negative eigenvalues of the flow → stable (this is a minimum). Mixed Hessian eigenvalues → saddle. This connects your Lesson 11 knowledge directly to dynamics.

### Phase Portraits as Complete Pictures

- **A phase portrait** shows representative trajectories overlaid on the vector field. It gives you the complete qualitative story: where does the system go from any initial condition?
- **Basins of attraction:** in a nonlinear system with multiple stable fixed points, the phase portrait reveals which initial conditions flow to which equilibrium. The boundaries between basins are called **separatrices** — they often pass through saddle points.
- **For neural networks:** different random initializations place you in different basins. The structure of basins in weight space determines the distribution of trained models. Understanding phase portraits is understanding this distribution.

## 📺 Watch — Primary

1. **3Blue1Brown — "Differential equations, studying the unsolvable" (continued)**
   - Re-watch the section on phase portraits and eigenvalue classification if you haven't internalized it
2. **Steve Brunton — "Phase Portraits for 2D Systems" and "Stability and Eigenvalues" (Dynamical Systems playlist, videos 3–5)**
   - https://www.youtube.com/c/Eigensteve
   - *Brunton draws phase portraits by hand and connects eigenvalues to every type. Excellent visual treatment.*

## 📺 Watch — Secondary

3. **MIT OCW — Strogatz "Nonlinear Dynamics and Chaos" (Lectures 5–6)**
   - Strogatz's lectures on 2D linear systems and phase plane classification are the gold standard
4. **Maththebeautiful — "Systems of ODEs and Phase Portraits"**
   - More worked examples if you want additional practice

## 📖 Read — Primary

- **"Nonlinear Dynamics and Chaos" by Steven Strogatz** — Chapter 5 (Linear Systems) and Chapter 6.1–6.3 (Phase Plane)
  - *Chapter 5 is the definitive geometric treatment of the eigenvalue classification. Every case is illustrated with beautiful phase portraits. Chapter 6 extends to nonlinear systems via linearization.*

## 📖 Read — Secondary

- **Steve Brunton & Nathan Kutz — "Data-Driven Science and Engineering"** — Chapter 7.1–7.3
  - https://www.databookuw.com/
  - *Applied treatment connecting dynamical systems to data, including computational examples*

## 🔨 Do

- **Build the eigenvalue classification:** for each 2×2 matrix below, compute eigenvalues, predict the phase portrait type, then simulate and plot with Python to verify:
  - A = [[-1, 0], [0, -3]] (stable node, well-separated eigenvalues)
  - A = [[-1, 0], [0, -1]] (stable star node, repeated eigenvalue)
  - A = [[1, 0], [0, -2]] (saddle point)
  - A = [[-1, 2], [-2, -1]] (stable spiral — complex eigenvalues!)
  - A = [[0, 1], [-1, 0]] (center — pure imaginary eigenvalues)
- **Condition number visualization:** plot gradient flow trajectories for L(w₁, w₂) = w₁²/2 + κw₂²/2 with κ = 1, 10, 100. Watch the zigzagging get worse as κ increases. Then implement a "preconditioned" version that divides each gradient component by the corresponding Hessian eigenvalue — see the zigzag vanish.
- **Linearization practice:** for the nonlinear system dx/dt = x - x³, dy/dt = -y, find all fixed points. At each one, compute the Jacobian and classify the fixed point. Draw the full phase portrait.
- **Key exercise:** the loss function L(w₁, w₂) = (w₁² - 1)² + w₂² has three critical points: (0,0), (1,0), (-1,0). Compute the Hessian at each. From the eigenvalues, determine which are minima, maxima, or saddle points. Predict the gradient flow behavior near each. Then simulate gradient descent from 20 random initial conditions and overlay on a contour plot to verify.

## 🔗 ML & Alignment Connection

- **Hessian eigenvalues → training behavior:** this is the most direct application. The spectrum of the Hessian at a critical point tells you everything about local convergence: the largest eigenvalue limits your learning rate, the smallest determines how slow the slowest direction converges, and the condition number is their ratio.
- **Saddle points dominate in high dimensions:** in a d-dimensional loss landscape, a random critical point has roughly d/2 positive and d/2 negative Hessian eigenvalues — it's a saddle. True local minima become exponentially rare as d increases. This is why gradient descent works despite non-convexity: it just escapes saddles along the unstable directions.
- **Preconditioning and natural gradient:** Adam, RMSProp, and natural gradient methods all modify the dynamics to improve conditioning. They effectively change the phase portrait near critical points from elongated to round.

- **Basin structure as alignment landscape:** if aligned behavior corresponds to certain basins and misaligned behavior to others, the relative sizes and positions of basins determine alignment probability. Phase portraits visualize this directly.
- **Saddle escape determines capabilities:** when training encounters a saddle point, *which* unstable direction it escapes along determines what capability is learned. The choice of optimizer and noise level influences this selection — a lever for alignment.
- **Sensitivity to initialization:** if two basins are nearby and the separatrix between them is complex, small changes to initialization could flip between aligned and misaligned outcomes. Understanding this sensitivity is critical for safety analysis.