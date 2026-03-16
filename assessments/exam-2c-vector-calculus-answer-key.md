# Exam 2C: Vector Calculus — Answer Key

**The Path to AI Alignment — Lessons 24–28 Comprehensive Assessment**

---

> **Grading philosophy:** Partial credit is generous for correct reasoning with arithmetic errors. Clear geometric or physical intuition alongside computation earns full marks. For ML-connection questions, any thoughtful answer demonstrating genuine understanding of the bridge between vector calculus and machine learning receives credit. The goal is demonstrating understanding, not perfect computation.

---

## Part I: Curves, Fields, and Green's Theorem (70 points)

---

### Question 1 (10 pts) — Curves and Parameterization

**(a)** Given $\mathbf{r}(t) = (\cos t,\, \sin t,\, t)$ for $t \in [0, 2\pi]$:

$$\mathbf{r}'(t) = (-\sin t,\, \cos t,\, 1)$$

$$\|\mathbf{r}'(t)\| = \sqrt{\sin^2 t + \cos^2 t + 1} = \sqrt{1 + 1} = \mathbf{\sqrt{2}}$$

The speed is **constant $\sqrt{2}$** — the helix is traversed at uniform speed.

**(b)** Arc length:

$$L = \int_0^{2\pi} \|\mathbf{r}'(t)\|\, dt = \int_0^{2\pi} \sqrt{2}\, dt = \mathbf{2\pi\sqrt{2}}$$

**(c)** Consider the reparameterization $\mathbf{r}(t) = (\cos 2t,\, \sin 2t,\, 2t)$ for $t \in [0, \pi]$. This traces the same geometric curve (one full turn of the helix from height $0$ to $2\pi$), just twice as fast.

$$\mathbf{r}'(t) = (-2\sin 2t,\, 2\cos 2t,\, 2)$$

$$\|\mathbf{r}'(t)\| = \sqrt{4\sin^2 2t + 4\cos^2 2t + 4} = \sqrt{4 + 4} = 2\sqrt{2}$$

$$L = \int_0^{\pi} 2\sqrt{2}\, dt = \mathbf{2\pi\sqrt{2}}$$

**Same arc length!** Arc length depends only on the geometric curve, not on the parameterization. It is **reparameterization-invariant** — the $\|\mathbf{r}'\|$ factor in the integrand automatically compensates for how fast we traverse the curve.

**(d)** In the weight trajectory $\mathbf{w}(t)$, a large $\|\mathbf{w}'(t)\|$ early in training corresponds to rapid weight changes — large learning rate, big gradient updates. A small $\|\mathbf{w}'(t)\|$ later means fine-tuning near convergence with small adjustments. This matches **learning rate warmup-then-decay schedules**: start cautiously (warmup), ramp up for fast progress, then slow down for precision near the optimum.

---

### Question 2 (10 pts) — Line Integrals

**(a)** Parameterize the line from $(0,0)$ to $(2,4)$: $\mathbf{r}(t) = (2t, 4t)$, $t \in [0,1]$.

$$f(x,y) = xy, \quad \mathbf{r}'(t) = (2, 4), \quad \|\mathbf{r}'(t)\| = \sqrt{4 + 16} = 2\sqrt{5}$$

$$\int_C f\, ds = \int_0^1 (2t)(4t) \cdot 2\sqrt{5}\, dt = 16\sqrt{5} \int_0^1 t^2\, dt = 16\sqrt{5} \cdot \frac{1}{3} = \mathbf{\frac{16\sqrt{5}}{3}}$$

**(b)** $\mathbf{F} = (y, x)$. Along the same parameterization:

$$\mathbf{F}(\mathbf{r}(t)) = (4t, 2t), \quad \mathbf{r}'(t) = (2, 4)$$

$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_0^1 (4t, 2t) \cdot (2, 4)\, dt = \int_0^1 (8t + 8t)\, dt = \int_0^1 16t\, dt = \mathbf{8}$$

**(c)** Path along two line segments:

**Segment 1:** $(0,0) \to (2,0)$: $\mathbf{r}(t) = (2t, 0)$, $t \in [0,1]$.

$$\mathbf{F} = (0, 2t), \quad d\mathbf{r} = (2, 0)\, dt, \quad \mathbf{F} \cdot d\mathbf{r} = 0$$

$$\int_{\text{Seg 1}} \mathbf{F} \cdot d\mathbf{r} = 0$$

**Segment 2:** $(2,0) \to (2,4)$: $\mathbf{r}(t) = (2, 4t)$, $t \in [0,1]$.

$$\mathbf{F} = (4t, 2), \quad d\mathbf{r} = (0, 4)\, dt, \quad \mathbf{F} \cdot d\mathbf{r} = 8\, dt$$

$$\int_{\text{Seg 2}} \mathbf{F} \cdot d\mathbf{r} = \int_0^1 8\, dt = 8$$

**Total: $0 + 8 = \mathbf{8}$**

**(d)** Both paths give **8** — the integral is **path-independent**, which means $\mathbf{F}$ is **conservative**. Indeed, $\mathbf{F} = (y, x) = \nabla(xy)$, so the potential function is $\varphi(x,y) = xy$. By the Fundamental Theorem of Line Integrals:

$$\int_C \mathbf{F} \cdot d\mathbf{r} = \varphi(2,4) - \varphi(0,0) = 8 - 0 = \mathbf{8}$$

---

### Question 3 (10 pts) — Conservative Fields

$\mathbf{F} = (2xy + y^2,\; x^2 + 2xy + 3y^2)$

**(a)** Check the component cross-partial test:

$$\frac{\partial F_1}{\partial y} = 2x + 2y, \qquad \frac{\partial F_2}{\partial x} = 2x + 2y$$

These are **equal**, so $\mathbf{F}$ is **conservative** (on a simply connected domain).

**(b)** Find the potential $\varphi$:

$$\varphi_x = 2xy + y^2 \implies \varphi = x^2 y + xy^2 + g(y)$$

$$\varphi_y = x^2 + 2xy + g'(y) = x^2 + 2xy + 3y^2$$

$$\implies g'(y) = 3y^2 \implies g(y) = y^3$$

$$\boxed{\varphi(x,y) = x^2 y + xy^2 + y^3}$$

**(c)** By the Fundamental Theorem of Line Integrals:

$$\int_C \mathbf{F} \cdot d\mathbf{r} = \varphi(1,2) - \varphi(0,0) = (1 \cdot 2 + 1 \cdot 4 + 8) - 0 = \mathbf{14}$$

**(d)** $\nabla L$ is conservative **by definition** — it is the gradient of $L$. This means for any closed loop $C$:

$$\oint_C \nabla L \cdot d\mathbf{r} = L(\text{end}) - L(\text{start}) = 0$$

Gradient descent follows $-\nabla L$, and since the gradient field is conservative, **trajectories cannot cycle**. The line integral around any closed path is zero by the FTLI, which would require the loss to both increase and decrease by the same total amount — impossible for persistent cycling. Any apparent cycling in training must come from stochastic noise (SGD), not from the gradient field itself.

---

### Question 4 (10 pts) — Green's Theorem (Circulation)

$\mathbf{F} = (-y, x)$, $C$ = unit circle traversed counterclockwise.

**(a)** Green's theorem (circulation form):

$$\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_D \left(\frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y}\right) dA$$

**(b)** Direct computation: $\mathbf{r}(t) = (\cos t, \sin t)$, $t \in [0, 2\pi]$.

$$\mathbf{F} = (-\sin t, \cos t), \quad d\mathbf{r} = (-\sin t, \cos t)\, dt$$

$$\mathbf{F} \cdot d\mathbf{r} = \sin^2 t + \cos^2 t = 1$$

$$\oint_C \mathbf{F} \cdot d\mathbf{r} = \int_0^{2\pi} 1\, dt = \mathbf{2\pi}$$

**(c)** Via Green's theorem:

$$\text{Scalar curl} = \frac{\partial(x)}{\partial x} - \frac{\partial(-y)}{\partial y} = 1 - (-1) = 2$$

$$\iint_D 2\, dA = 2 \cdot \pi(1)^2 = \mathbf{2\pi} \quad \checkmark$$

**(d)** The scalar curl equals **2 everywhere** — uniform rotation at every point. The total circulation is curl $\times$ area $= 2 \cdot \pi = 2\pi$. Constant rotation per unit area accumulates linearly over the entire disk.

**(e)** To detect rotation in the Jacobian of a representation map $f: \mathbb{R}^n \to \mathbb{R}^n$, check whether the Jacobian $J$ has a nonzero antisymmetric (skew) component. Decompose $J = \frac{1}{2}(J + J^T) + \frac{1}{2}(J - J^T)$. If $J - J^T \neq 0$, there is a **rotational component** in how the representation transforms inputs — analogous to nonzero curl. This matters for understanding whether a learned representation preserves or introduces rotational structure.

---

### Question 5 (10 pts) — Green's Theorem (Flux) and Divergence

$\mathbf{F} = (x^2, y^2)$

**(a)** Green's theorem (flux form):

$$\oint_C \mathbf{F} \cdot \mathbf{n}\, ds = \iint_D \operatorname{div}(\mathbf{F})\, dA$$

**(b)** The divergence:

$$\operatorname{div} \mathbf{F} = \frac{\partial(x^2)}{\partial x} + \frac{\partial(y^2)}{\partial y} = 2x + 2y$$

**(c)** Over the unit square $D = [0,1] \times [0,1]$:

$$\iint_D (2x + 2y)\, dA = \int_0^1 \int_0^1 (2x + 2y)\, dx\, dy$$

Inner integral:

$$\int_0^1 (2x + 2y)\, dx = \bigl[x^2 + 2xy\bigr]_0^1 = 1 + 2y$$

Outer integral:

$$\int_0^1 (1 + 2y)\, dy = \bigl[y + y^2\bigr]_0^1 = 1 + 1 = \mathbf{2}$$

**(d)** Direct flux computation along all four sides:

- **Right** ($x=1$, upward): $\int_0^1 (1, y^2) \cdot (1, 0)\, dy = \int_0^1 1\, dy = 1$
- **Top** ($y=1$, rightward): $\int_0^1 (x^2, 1) \cdot (0, 1)\, dx = \int_0^1 1\, dx = 1$
- **Left** ($x=0$, downward): $\int_0^1 (0, y^2) \cdot (-1, 0)\, dy = 0$
- **Bottom** ($y=0$, leftward): $\int_0^1 (x^2, 0) \cdot (0, -1)\, dx = 0$

**Total: $1 + 1 + 0 + 0 = \mathbf{2}$** $\checkmark$

**(e)** Since $\operatorname{div} \mathbf{F} > 0$ everywhere in the first quadrant, probability density is being **diluted** (spread out) everywhere — the flow creates volume faster than it can be sustained. A proper **normalizing flow** must preserve total probability ($\int p = 1$). If divergence is positive everywhere, density decreases everywhere, violating normalization. A valid normalizing flow needs regions of positive divergence (expansion) balanced by regions of negative divergence (compression) so that total probability is conserved.

---

### Question 6 (10 pts) — Laplacian and Harmonic Functions

**(a)** The Laplacian in 2D:

$$\nabla^2 f = f_{xx} + f_{yy}$$

It is the sum of the unmixed second partial derivatives — measuring the total concavity in all directions.

**(b)** $f(x,y) = x^2 - y^2$:

$$f_{xx} = 2, \quad f_{yy} = -2, \quad \nabla^2 f = 2 + (-2) = 0$$

**Yes, harmonic.** (This is a saddle surface — it curves up in $x$ and down in $y$ by equal amounts.)

**(c)** $g(x,y) = e^x \sin y$:

$$g_{xx} = e^x \sin y, \quad g_{yy} = -e^x \sin y, \quad \nabla^2 g = e^x \sin y - e^x \sin y = 0$$

**Yes, harmonic.**

**(d)** **Mean value property:** The value of a harmonic function at any point equals the average of its values on any circle centered at that point.

If a point were a strict local maximum, its value would exceed the values at all nearby points, so it would exceed the average on any sufficiently small surrounding circle. This **violates** the mean value property. Therefore harmonic functions have **no local maxima or minima** in the interior of their domain.

**(e)** The Laplacian is a **local averaging operator** — it measures how much a function's value at a point differs from the average of its neighbors. The heat equation $\partial u / \partial t = \nabla^2 u$ replaces each point's value with a weighted average of its neighbors over time. This is exactly what adding Gaussian noise does to a probability distribution: convolution with a Gaussian kernel performs local averaging. In diffusion models, the forward process (adding noise) is governed by the heat equation, progressively smoothing the distribution until it becomes a Gaussian.

---

### Question 7 (10 pts) — Conceptual Checkpoint

**(a)** **Scalar line integral** $\int_C f\, ds$: weights the scalar function $f$ by arc length along the curve. Physical interpretation: total mass of a wire with density $f$, or total energy along a path.

**Vector line integral** $\int_C \mathbf{F} \cdot d\mathbf{r}$: measures the **work done** by the force field $\mathbf{F}$ along the path. It depends on the direction of traversal and decomposes $\mathbf{F}$ into the tangential component along the curve.

**(b)** Suppose $\mathbf{F}$ is conservative with $\operatorname{curl} \mathbf{F} \neq 0$. By Green's theorem, there exists some closed curve $C$ bounding a region $D$ where:

$$\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_D \operatorname{curl}(\mathbf{F})\, dA \neq 0$$

But for a conservative field, $\oint_C \mathbf{F} \cdot d\mathbf{r} = 0$ for **all** closed loops (by FTLI). **Contradiction.** Therefore $\operatorname{curl} \mathbf{F} = 0$ is necessary for conservativeness.

**(c)** The **circulation form** $\oint \mathbf{F} \cdot d\mathbf{r} = \iint \operatorname{curl}(\mathbf{F})\, dA$ measures **rotational tendency** — how much the field swirls around the boundary.

The **flux form** $\oint \mathbf{F} \cdot \mathbf{n}\, ds = \iint \operatorname{div}(\mathbf{F})\, dA$ measures **expansion/compression** — how much the field pushes outward through the boundary.

Circulation detects spinning; flux detects sources and sinks.

**(d)** Classic example:

$$\mathbf{F} = \left(\frac{-y}{x^2+y^2},\; \frac{x}{x^2+y^2}\right) \quad \text{on } \mathbb{R}^2 \setminus \bigl\lbrace (0,0) \bigr\rbrace$$

This has $\operatorname{curl} \mathbf{F} = 0$ everywhere it is defined, yet $\oint_C \mathbf{F} \cdot d\mathbf{r} = 2\pi$ around the origin. It is **not conservative** because the domain has a **hole** (the origin is removed), so it is not simply connected. Curl-free does not imply conservative on non-simply-connected domains.

**(e)** The equivalences: **conservative $\Leftrightarrow$ path-independent $\Leftrightarrow$ potential function exists.**

In ML, the existence of a loss function $L$ means $\nabla L$ is conservative, so gradient descent has a **well-defined objective**. The path taken through weight space doesn't matter — only the start and end points determine the change in loss. If the training dynamics vector field were non-conservative, no single scalar loss function could describe it, and the notion of "making progress toward a minimum" would break down.

---

## Part II: Surfaces, Stokes', and Divergence Theorem (80 points)

---

### Question 8 (10 pts) — Parametric Surfaces

$\mathbf{r}(u,v) = (u\cos v,\; u\sin v,\; u)$, $u \in [0,2]$, $v \in [0, 2\pi]$.

**(a)** Since $z = u$ and $x^2 + y^2 = u^2\cos^2 v + u^2\sin^2 v = u^2$, we have:

$$z = \sqrt{x^2 + y^2}$$

This is a **cone** opening upward with half-angle $45°$, vertex at the origin, extending to height $z = 2$.

**(b)** Partial derivatives:

$$\mathbf{r}_u = (\cos v,\; \sin v,\; 1), \qquad \mathbf{r}_v = (-u\sin v,\; u\cos v,\; 0)$$

**(c)** The cross product $\mathbf{r}_u \times \mathbf{r}_v$:

$$\mathbf{r}_u \times \mathbf{r}_v = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \cos v & \sin v & 1 \\ -u\sin v & u\cos v & 0 \end{vmatrix}$$

$$= \mathbf{i}(\sin v \cdot 0 - 1 \cdot u\cos v) - \mathbf{j}(\cos v \cdot 0 - 1 \cdot (-u\sin v)) + \mathbf{k}(\cos v \cdot u\cos v - \sin v \cdot (-u\sin v))$$

$$= \mathbf{(-u\cos v,\; -u\sin v,\; u)}$$

**(d)** Surface area:

$$\|\mathbf{r}_u \times \mathbf{r}_v\| = \sqrt{u^2\cos^2 v + u^2\sin^2 v + u^2} = \sqrt{u^2 + u^2} = u\sqrt{2}$$

$$\text{SA} = \int_0^{2\pi}\int_0^2 u\sqrt{2}\, du\, dv = \sqrt{2} \cdot 2\pi \cdot \left[\frac{u^2}{2}\right]_0^2 = \sqrt{2} \cdot 2\pi \cdot 2 = \mathbf{4\pi\sqrt{2}}$$

**(e)** $\|\mathbf{r}_u \times \mathbf{r}_v\|$ gives the area of the infinitesimal parallelogram spanned by $\mathbf{r}_u\, du$ and $\mathbf{r}_v\, dv$ — this is the **surface area element** $dS$. It is the same "cross product = parallelogram area" idea from Phase 1 linear algebra, now serving as the local scaling factor that converts a rectangle in parameter space $(u,v)$ to the actual surface patch area. It plays the role of the Jacobian for surface integration.

---

### Question 9 (10 pts) — Surface Integrals of Scalar Functions

**(a)** Upper hemisphere $z = \sqrt{1 - x^2 - y^2}$, parameterized as $\mathbf{r}(u,v) = (u\cos v,\; u\sin v,\; \sqrt{1-u^2})$, $u \in [0,1]$, $v \in [0,2\pi]$.

$$\mathbf{r}_u = \left(\cos v,\; \sin v,\; \frac{-u}{\sqrt{1-u^2}}\right), \qquad \mathbf{r}_v = (-u\sin v,\; u\cos v,\; 0)$$

$$\mathbf{r}_u \times \mathbf{r}_v = \left(\frac{u^2\cos v}{\sqrt{1-u^2}},\; \frac{u^2\sin v}{\sqrt{1-u^2}},\; u\right)$$

$$\|\mathbf{r}_u \times \mathbf{r}_v\| = \sqrt{\frac{u^4}{1-u^2} + u^2} = \sqrt{\frac{u^4 + u^2(1-u^2)}{1-u^2}} = \sqrt{\frac{u^2}{1-u^2}} = \frac{u}{\sqrt{1-u^2}}$$

Now compute $\iint_S z\, dS$:

$$\iint_S z\, dS = \int_0^{2\pi}\int_0^1 \sqrt{1-u^2} \cdot \frac{u}{\sqrt{1-u^2}}\, du\, dv = \int_0^{2\pi}\int_0^1 u\, du\, dv = 2\pi \cdot \frac{1}{2} = \mathbf{\pi}$$

**(b)** If $f$ represents mass density (mass per unit area), then $\iint_S f\, dS$ gives the **total mass** of the surface. More generally, it integrates any scalar quantity distributed over the surface, weighted by actual surface area.

**(c)** $\|\mathbf{r}_u \times \mathbf{r}_v\|$ accounts for the **distortion** between parameter space $(u,v)$ and the actual curved surface — exactly like the Jacobian determinant $|det(J)|$ in a change of variables for double integrals. A small rectangle $du \times dv$ in parameter space maps to a (generally non-rectangular) patch on the surface, and the cross product magnitude gives the area ratio.

**(d)** To measure the total curvature of a decision boundary surface $S$, set up a surface integral of a curvature measure (such as Gaussian curvature $K$ or mean curvature $H$) over the decision boundary:

$$\iint_S K\, dS \quad \text{or} \quad \iint_S H^2\, dS$$

weighted by the surface area element $dS$. This quantifies how much the decision boundary bends — highly curved boundaries suggest overfitting, while smoother (low-curvature) boundaries suggest better generalization.

---

### Question 10 (10 pts) — Orientation and Flux

$\mathbf{F} = (0, 0, z)$, $S$: the paraboloid $z = 1 - x^2 - y^2$ for $z \geq 0$, with upward-pointing normal.

**(a)** A surface is **orientable** if you can consistently choose a normal direction $\mathbf{n}$ at every point that varies continuously across the surface. This means there are exactly two choices of orientation (e.g., "outward" vs. "inward" for a closed surface, or "upward" vs. "downward").

**Non-orientable example:** The **Mobius strip** — if you try to assign a consistent normal, you return to your starting point with the normal flipped after traversing the strip once.

**(b)** Parameterize using cylindrical coordinates: $\mathbf{r}(u,v) = (u\cos v,\; u\sin v,\; 1 - u^2)$, $u \in [0,1]$, $v \in [0,2\pi]$.

$$\mathbf{r}_u = (\cos v,\; \sin v,\; -2u), \qquad \mathbf{r}_v = (-u\sin v,\; u\cos v,\; 0)$$

$$\mathbf{r}_u \times \mathbf{r}_v = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \cos v & \sin v & -2u \\ -u\sin v & u\cos v & 0 \end{vmatrix}$$

$$= (0 - (-2u)(u\cos v),\; (-2u)(-u\sin v) - 0,\; \cos v \cdot u\cos v - \sin v \cdot (-u\sin v))$$

$$= (2u^2\cos v,\; 2u^2\sin v,\; u)$$

The $z$-component is $u > 0$ for $u > 0$, confirming the normal points **upward**. $\checkmark$

**(c)** Compute the flux:

$$\mathbf{F}(\mathbf{r}(u,v)) = (0,\; 0,\; 1-u^2)$$

$$\mathbf{F} \cdot (\mathbf{r}_u \times \mathbf{r}_v) = (0, 0, 1-u^2) \cdot (2u^2\cos v,\; 2u^2\sin v,\; u) = u(1-u^2)$$

$$\text{Flux} = \int_0^{2\pi}\int_0^1 u(1-u^2)\, du\, dv = 2\pi \int_0^1 (u - u^3)\, du = 2\pi\left[\frac{u^2}{2} - \frac{u^4}{4}\right]_0^1 = 2\pi \cdot \frac{1}{4} = \mathbf{\frac{\pi}{2}}$$

**(d)** Positive flux means there is **net probability flowing upward** through the paraboloid. In the continuity equation $\frac{\partial p}{\partial t} + \operatorname{div}(\mathbf{J}) = 0$, the flux $\iint_S \mathbf{J} \cdot d\mathbf{S}$ measures the rate at which probability mass crosses the surface $S$. This tracks how the probability distribution evolves — positive flux through a surface means probability is accumulating on the side the normal points toward.

---

### Question 11 (12 pts) — Curl and Stokes' Theorem

$\mathbf{F} = (y,\; -x,\; z^2)$

**(a)** Compute the curl:

$$\nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \partial_x & \partial_y & \partial_z \\ y & -x & z^2 \end{vmatrix}$$

$$= \left(\frac{\partial(z^2)}{\partial y} - \frac{\partial(-x)}{\partial z},\; \frac{\partial(y)}{\partial z} - \frac{\partial(z^2)}{\partial x},\; \frac{\partial(-x)}{\partial x} - \frac{\partial(y)}{\partial y}\right) = (0-0,\; 0-0,\; -1-1)$$

$$\nabla \times \mathbf{F} = \mathbf{(0, 0, -2)}$$

**(b)** Let $S$ be the disk $z = 1$ over the unit circle, with $\mathbf{n} = (0, 0, 1)$:

$$\iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S} = \iint_S (0, 0, -2) \cdot (0, 0, 1)\, dA = -2 \cdot \text{Area} = -2\pi$$

$$\iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S} = \mathbf{-2\pi}$$

**(c)** Direct computation along the boundary $C$: $x^2 + y^2 = 1$, $z = 1$.

$$\mathbf{r}(t) = (\cos t,\; \sin t,\; 1), \quad \mathbf{r}'(t) = (-\sin t,\; \cos t,\; 0)$$

$$\mathbf{F}(\mathbf{r}(t)) = (\sin t,\; -\cos t,\; 1)$$

$$\mathbf{F} \cdot \mathbf{r}' = -\sin^2 t - \cos^2 t + 0 = -1$$

$$\oint_C \mathbf{F} \cdot d\mathbf{r} = \int_0^{2\pi} (-1)\, dt = \mathbf{-2\pi} \quad \checkmark$$

**(d)** **Stokes' theorem** states:

$$\iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S} = \oint_{\partial S} \mathbf{F} \cdot d\mathbf{r}$$

Both sides equal $\mathbf{-2\pi}$, confirming the theorem. $\checkmark$

**(e)** The hierarchy:

- **FTC:** $\int_a^b f'(x)\, dx = f(b) - f(a)$. The "boundary" is two endpoints.
- **Stokes':** $\iint_S \operatorname{curl} \mathbf{F} \cdot d\mathbf{S} = \oint_{\partial S} \mathbf{F} \cdot d\mathbf{r}$. The "boundary" is a closed curve.

Both follow the same pattern: **integral of a derivative over a region = integral of the function over the boundary**. The FTC is the 1D case, Stokes' is the 2D-surface-in-3D case. Green's theorem is the 2D planar special case. The Divergence theorem extends this to 3D volumes with surface boundaries. All are instances of the **generalized Stokes' theorem** $\int_\Omega d\omega = \int_{\partial\Omega} \omega$.

---

### Question 12 (10 pts) — Divergence Theorem

$\mathbf{F} = (x, y, z)$, $E$ = unit ball $x^2 + y^2 + z^2 \leq 1$.

**(a)** Divergence:

$$\operatorname{div} \mathbf{F} = \frac{\partial x}{\partial x} + \frac{\partial y}{\partial y} + \frac{\partial z}{\partial z} = 1 + 1 + 1 = \mathbf{3}$$

**(b)** Volume integral:

$$\iiint_E 3\, dV = 3 \cdot \frac{4\pi}{3} = \mathbf{4\pi}$$

**(c)** By the **Divergence Theorem**:

$$\oiint_{\partial E} \mathbf{F} \cdot d\mathbf{S} = \iiint_E \operatorname{div}(\mathbf{F})\, dV = \mathbf{4\pi}$$

**(d)** Direct verification: On the unit sphere, the outward normal is $\mathbf{n} = (x, y, z)$ (the position vector itself, since the sphere has radius 1).

$$\mathbf{F} \cdot \mathbf{n} = (x,y,z) \cdot (x,y,z) = x^2 + y^2 + z^2 = 1$$

$$\oiint_{\partial E} \mathbf{F} \cdot d\mathbf{S} = \oiint_{\partial E} 1\, dS = \text{Surface area of unit sphere} = \mathbf{4\pi} \quad \checkmark$$

**(e)** Start from the conservation principle: the rate of change of probability inside any region $E$ equals the negative of the flux out:

$$\frac{d}{dt}\iiint_E p\, dV = -\oiint_{\partial E} \mathbf{J} \cdot \mathbf{n}\, dS$$

Apply the **Divergence Theorem** to the right side:

$$\iiint_E \frac{\partial p}{\partial t}\, dV = -\iiint_E \operatorname{div}(\mathbf{J})\, dV$$

Since this holds for **every** region $E$ (no matter how small), the integrands must be equal pointwise:

$$\frac{\partial p}{\partial t} + \operatorname{div}(\mathbf{J}) = 0$$

This is the **continuity equation**. The divergence theorem is the key step that converts the global surface-flux statement into a local (pointwise) differential equation.

---

### Question 13 (10 pts) — Grand Unified Hierarchy

**(a)** The generalized Stokes' theorem hierarchy:

| Theorem | "Derivative" integrated | Domain | Boundary | Dimension |
|---|---|---|---|---|
| **FTC** | $f'(x)$ | Interval $[a,b]$ | Endpoints $\bigl\lbrace a, b \bigr\rbrace$ | 1D |
| **FTLI** | $\nabla f$ | Curve $C$ | Endpoints $\bigl\lbrace \mathbf{r}(a), \mathbf{r}(b) \bigr\rbrace$ | Curves |
| **Green's** | $\operatorname{curl} \mathbf{F}$ (scalar) | Region $R \subset \mathbb{R}^2$ | $\partial R$ (closed curve) | 2D |
| **Stokes'** | $\nabla \times \mathbf{F}$ | Surface $S \subset \mathbb{R}^3$ | $\partial S$ (closed curve) | 2D surface in 3D |
| **Divergence** | $\operatorname{div} \mathbf{F}$ | Volume $E \subset \mathbb{R}^3$ | $\partial E$ (closed surface) | 3D |

**(b)** The generalized Stokes' theorem $\int_\Omega d\omega = \int_{\partial\Omega} \omega$ is arguably the most important theorem in mathematics because it **unifies all of calculus into a single principle**: the integral of a derivative over a region equals the integral of the original quantity over the boundary. Every conservation law in physics (conservation of mass, energy, charge, probability), every relationship between local differential behavior and global integral behavior, is a special case. It says that **what happens inside is completely determined by what happens at the boundary**, and that **local rates of change (derivatives) accumulate to global differences (boundary values)**.

**(c)** **Backpropagation** as a Stokes'-type theorem: The loss is computed at the output (the "boundary" of the network), and backprop propagates this signal inward to determine gradients at every interior parameter. Just as Stokes' theorem relates boundary circulation to interior curl, backprop relates the boundary loss signal to interior parameter gradients. The **chain rule** plays the role of the exterior derivative $d$ — it is the mechanism by which the derivative at one layer connects to the derivative at the next, accumulating from boundary to interior.

**(d)** The key computational advantage: surface integrals are **(d-1)-dimensional** while volume integrals are **d-dimensional**. In 3D, a surface integral is $O(N^2)$ while the corresponding volume integral is $O(N^3)$. The boundary theorems let us **reduce dimension by 1**, which can be a dramatic computational savings. This is why boundary element methods are often preferred over finite element methods, and why computing flux through a surface can be cheaper than integrating divergence over the enclosed volume (or vice versa, depending on which is simpler).

---

### Question 14 (8 pts) — Vector Calculus Identities

**(a)** Prove $\operatorname{div}(\operatorname{curl} \mathbf{F}) = 0$:

Let $\mathbf{F} = (F_1, F_2, F_3)$. Then:

$$\operatorname{curl} \mathbf{F} = \left(\frac{\partial F_3}{\partial y} - \frac{\partial F_2}{\partial z},\; \frac{\partial F_1}{\partial z} - \frac{\partial F_3}{\partial x},\; \frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y}\right)$$

Taking the divergence:

$$\operatorname{div}(\operatorname{curl} \mathbf{F}) = \frac{\partial}{\partial x}\left(\frac{\partial F_3}{\partial y} - \frac{\partial F_2}{\partial z}\right) + \frac{\partial}{\partial y}\left(\frac{\partial F_1}{\partial z} - \frac{\partial F_3}{\partial x}\right) + \frac{\partial}{\partial z}\left(\frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y}\right)$$

$$= F_{3,xy} - F_{2,xz} + F_{1,yz} - F_{3,yx} + F_{2,zx} - F_{1,zy}$$

By **Clairaut's theorem** (equality of mixed partials), $F_{3,xy} = F_{3,yx}$, $F_{2,xz} = F_{2,zx}$, and $F_{1,yz} = F_{1,zy}$. Every term cancels with its partner:

$$\operatorname{div}(\operatorname{curl} \mathbf{F}) = \mathbf{0}$$

**(b)** Prove $\operatorname{curl}(\nabla f) = \mathbf{0}$:

$$\nabla f = (f_x, f_y, f_z)$$

$$\operatorname{curl}(\nabla f) = (f_{zy} - f_{yz},\; f_{xz} - f_{zx},\; f_{yx} - f_{xy}) = (0, 0, 0) = \mathbf{0}$$

by equality of mixed partials (Clairaut's theorem).

**(c)** Both identities express the principle **"exact forms are closed"** or equivalently $d^2 = 0$ — applying the exterior derivative twice always gives zero.

- A gradient $\nabla f$ produces an exact 1-form; its curl (the exterior derivative of a 1-form) is zero.
- A curl $\nabla \times \mathbf{F}$ produces an exact 2-form; its divergence (the exterior derivative of a 2-form) is zero.

This is the algebraic backbone of de Rham cohomology and is why the Stokes' hierarchy works: the sequence $\text{grad} \to \text{curl} \to \text{div}$ forms a **chain complex** where composing consecutive operators yields zero.

**(d)** $\operatorname{curl}(\nabla L) = \mathbf{0}$ means the gradient field of a loss function has **no rotational component**. Gradient descent follows $-\nabla L$, and since this field is curl-free, trajectories **cannot form persistent closed loops** (cycling). Any apparent cycling in training must come from stochastic noise (SGD minibatch variance) or non-gradient effects (momentum, adaptive learning rates), not from the deterministic gradient field itself. This is why pure gradient descent on a smooth loss landscape always converges to a critical point — the curl-free property guarantees no energy can be "recycled" through rotation.

---

### Question 15 (10 pts) — Synthesis: Tying It All Together

**(a)** For an infinitesimal flow $d\mathbf{x}/dt = \mathbf{f}(\mathbf{x})$, a small volume element transforms by the Jacobian. After time $dt$:

$$\det(I + J \cdot dt) \approx 1 + \operatorname{tr}(J)\, dt = 1 + \operatorname{div}(\mathbf{f})\, dt$$

Since probability is conserved ($p \cdot \text{volume} = \text{const}$ locally):

$$\frac{d}{dt}\log p = -\operatorname{div}(\mathbf{f})$$

**Divergence measures the rate at which the flow expands ($\operatorname{div} > 0$) or compresses ($\operatorname{div} < 0$) volume elements.** Since probability = density $\times$ volume, expanding volume dilutes density (decreases $\log p$) by exactly $\operatorname{div}(\mathbf{f})$. This is the **instantaneous change of variables formula** used in continuous normalizing flows.

**(b)** For $p(\mathbf{x}) = \mathcal{N}(\boldsymbol{\mu}, \Sigma)$:

$$\log p = \text{const} - \frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^T \Sigma^{-1}(\mathbf{x} - \boldsymbol{\mu})$$

$$\mathbf{s}(\mathbf{x}) = \nabla \log p = -\Sigma^{-1}(\mathbf{x} - \boldsymbol{\mu})$$

**Yes, this is conservative** — it is the gradient of $\log p(\mathbf{x})$. The **potential function is $\log p(\mathbf{x})$** itself. The score points toward the mean with magnitude proportional to the Mahalanobis distance, always derivable from a scalar potential.

**(c)** For a true score function $\mathbf{s} = \nabla \log p$ (a conservative field):

$$\oint_C \mathbf{s} \cdot d\mathbf{r} = 0 \quad \text{for any closed loop } C$$

If a learned score network $\mathbf{s}_\theta$ gives **nonzero circulation** around some closed loop, it is not a valid gradient field — it cannot be the gradient of any log-density. This serves as a **consistency/quality check** for score-based diffusion models: compute the circulation around test loops, and nonzero values indicate the network has failed to learn a valid score function. This is a direct application of the conservative field criterion.

**(d)** The **Fokker-Planck equation**:

$$\frac{\partial p}{\partial t} = -\operatorname{div}(\mathbf{f} p) + D\nabla^2 p$$

Integrate over any region $E$ and apply the **divergence theorem**:

$$\frac{d}{dt}\iiint_E p\, dV = -\oiint_{\partial E} (\mathbf{f} p) \cdot \mathbf{n}\, dS + \oiint_{\partial E} D(\nabla p) \cdot \mathbf{n}\, dS$$

The divergence theorem converts volume integrals into surface flux integrals, revealing two mechanisms:

- **Advection term** $-\operatorname{div}(\mathbf{f} p)$: the drift $\mathbf{f}$ transports probability — net flux of $\mathbf{f} p$ through the boundary measures how much probability the drift carries across.
- **Diffusion term** $D\nabla^2 p$: random motion spreads probability down concentration gradients, exactly like the **heat equation**. Flux $D\nabla p$ through the boundary measures diffusive transport.

This is the mathematical foundation of diffusion models: the forward process adds noise (diffusion dominates), and the reverse process removes noise (learned drift dominates).

**(e)** *[Open-ended — accept any thoughtful answer that connects vector calculus to ML/alignment.]*

Example strong answer: The generalized Stokes' theorem provides the mathematical guarantee that local properties (derivatives, gradients) accumulate predictably into global properties (integrals, total change). For AI alignment, this is a foundational principle: if we can verify local properties of a system (e.g., that the gradient of a reward function points in the right direction at every point), the boundary theorems guarantee that the global behavior (the trajectory the system follows) will be well-behaved. Conversely, if global behavior is problematic (misalignment), the theorems tell us that some local property must be wrong — giving us a principled place to look for the source of the problem.

---

*End of Answer Key*
