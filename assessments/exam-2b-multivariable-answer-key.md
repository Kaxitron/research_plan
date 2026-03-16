# Exam 2B: Multivariable Calculus — Answer Key

**The Path to AI Alignment — Lessons 19–23 Comprehensive Assessment**

> **Grading philosophy:** Full credit requires both correct computation and clear reasoning. Partial credit is generous for correct setup with arithmetic errors. Conceptual parts are graded on precision of language and demonstrated understanding of the ML connection — vague hand-waving earns at most half credit.

---

### Question 1 (10 pts) — Partial Derivatives and the Gradient

Let $f(x, y) = x^2 y - 3xy^3 + 2x - y$.

**(a)** Compute partial derivatives:

$$f_x = 2xy - 3y^3 + 2$$

$$f_y = x^2 - 9xy^2 - 1$$

**(b)** Second-order partial derivatives:

$$f_{xx} = 2y, \quad f_{yy} = -18xy, \quad f_{xy} = 2x - 9y^2, \quad f_{yx} = 2x - 9y^2$$

Clairaut's theorem verified: **$f_{xy} = f_{yx} = 2x - 9y^2$** ✓

**(c)** At $(1, -1)$:

$$\nabla f(1,-1) = \bigl(2(1)(-1) - 3(-1)^3 + 2,\; (1)^2 - 9(1)(-1)^2 - 1\bigr) = (-2 + 3 + 2,\; 1 - 9 - 1) = \mathbf{(3, -9)}$$

Direction of steepest increase:

$$\frac{\nabla f}{\|\nabla f\|} = \frac{(3,-9)}{\sqrt{9 + 81}} = \frac{(3,-9)}{3\sqrt{10}} = \mathbf{\frac{1}{\sqrt{10}}(1, -3)}$$

**(d)** Directional derivative $D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u}$:

$$D_{\mathbf{u}} f = (3, -9) \cdot \left(\frac{3}{5}, \frac{4}{5}\right) = \frac{9}{5} - \frac{36}{5} = \mathbf{-\frac{27}{5}}$$

**(e)** The rate of change is zero in directions **perpendicular to the gradient**. The gradient is $(3, -9)$, so the perpendicular direction is:

$$\frac{(9, 3)}{\|(9, 3)\|} = \frac{(3, 1)}{\sqrt{10}} = \mathbf{\frac{1}{\sqrt{10}}(3, 1)}$$

This direction is **tangent to the level curve** (contour line) of $f$ passing through $(1, -1)$.

---

### Question 2 (10 pts) — Tangent Planes and Linear Approximation

$z = f(x, y) = e^{x^2 + y}$

**(a)** $f(0,0) = e^0 = 1$. Partial derivatives:

$$f_x = 2x\, e^{x^2+y} \;\Rightarrow\; f_x(0,0) = 0$$

$$f_y = e^{x^2+y} \;\Rightarrow\; f_y(0,0) = 1$$

Tangent plane:

$$\boxed{z = 1 + y}$$

**(b)** Linear approximation: $f(0.1, -0.1) \approx 1 + (-0.1) = \mathbf{0.9}$.

Exact value: $e^{0.01 - 0.1} = e^{-0.09} \approx 0.9139$.

Error $\approx |0.9139 - 0.9| = \mathbf{0.014}$ (about 1.5%).

**(c)** The linear approximation is good when $\|\mathbf{x} - \mathbf{a}\|$ is small. The quantity that measures the failure of the linear approximation is the **Hessian** (matrix of second derivatives) — specifically, the remainder term in the Taylor expansion involves the Hessian quadratic form $(1/2)(\mathbf{x}-\mathbf{a})^T H (\mathbf{x}-\mathbf{a})$.

**(d)** A large learning rate steps far from the current point, where the linear approximation of the loss is poor. The actual loss function curves away from the linear prediction (due to nonzero Hessian/curvature), so the actual loss after the step can be **higher** than the linear model predicted. This causes the loss to increase rather than decrease — leading to divergence.

---

### Question 3 (12 pts) — The Multivariable Chain Rule and Backpropagation

Computation graph: $x, y \to z = x^2 + xy \to w = \sin(z) \to L = w^2$.

**(a)** Forward pass at $x = 1, y = 2$:

$$z = 1 + 2 = 3, \quad w = \sin(3) \approx 0.1411, \quad L = w^2 \approx \mathbf{0.01991}$$

**(b)** Local gradients:

$$\frac{dL}{dw} = 2w = 2\sin(3), \quad \frac{dw}{dz} = \cos(z) = \cos(3), \quad \frac{dz}{dx} = 2x + y = 4, \quad \frac{dz}{dy} = x = 1$$

**(c)** Backward pass (chain rule):

$$\frac{dL}{dx} = \frac{dL}{dw} \cdot \frac{dw}{dz} \cdot \frac{dz}{dx} = 2\sin(3) \cdot \cos(3) \cdot 4 = 8\sin(3)\cos(3) = \mathbf{4\sin(6) \approx -1.1176}$$

$$\frac{dL}{dy} = \frac{dL}{dw} \cdot \frac{dw}{dz} \cdot \frac{dz}{dy} = 2\sin(3) \cdot \cos(3) \cdot 1 = \mathbf{\sin(6) \approx -0.2794}$$

**(d)** Direct computation: $L = \sin^2(x^2 + xy)$.

$$\frac{dL}{dx} = 2\sin(x^2+xy)\cos(x^2+xy)(2x+y) = \sin(2(x^2+xy))(2x+y)$$

At $(1,2)$: $\sin(2 \cdot 3) \cdot 4 = 4\sin(6)$. ✓ Matches part (c).

**(e)** The chain rule produces a product of 100 Jacobian matrices $J_{100} \cdot J_{99} \cdots J_1$. If the eigenvalues (singular values) of these Jacobians are consistently $> 1$, the product grows exponentially — **gradients explode**. If consistently $< 1$, the product shrinks exponentially — **gradients vanish**. **Residual connections** (skip connections) mitigate this by effectively adding the identity matrix to each Jacobian, keeping eigenvalues near 1.

---

### Question 4 (10 pts) — The Jacobian Matrix

$F(x, y) = (x^2 - y,\; xy + 1)$

**(a)**

$$J = \begin{bmatrix} 2x & -1 \\ y & x \end{bmatrix}$$

**(b)** At $(1, 2)$:

$$J(1,2) = \begin{bmatrix} 2 & -1 \\ 2 & 1 \end{bmatrix}$$

Shape: **$2 \times 2$**. Each **column** represents the effect of perturbing one input variable on all outputs. Each **row** is the gradient of one output component with respect to all inputs.

**(c)** $F(1, 2) = (1 - 2,\; 2 + 1) = (-1, 3)$. Linear approximation:

$$F(1.01, 2.03) \approx \begin{pmatrix} -1 \\ 3 \end{pmatrix} + \begin{bmatrix} 2 & -1 \\ 2 & 1 \end{bmatrix} \begin{pmatrix} 0.01 \\ 0.03 \end{pmatrix} = \begin{pmatrix} -1 \\ 3 \end{pmatrix} + \begin{pmatrix} 0.02 - 0.03 \\ 0.02 + 0.03 \end{pmatrix} = \mathbf{(-1.01,\; 3.05)}$$

Exact: $(1.0201 - 2.03,\; 1.01 \cdot 2.03 + 1) = (-1.0099,\; 3.0503)$. Close! ✓

**(d)** Backpropagation computes $\mathbf{v}^T J$ (a **vector-Jacobian product**, or VJP) at each layer, which is $O(n)$ per layer. Computing the full Jacobian would be $O(n^2)$. For a scalar loss, you only need one backward pass to get all gradients, rather than computing the full Jacobian matrix at every layer.

---

### Question 5 (10 pts) — The Hessian Matrix and Curvature

$f(x, y) = x^3 - 3xy + y^3$

**(a)** Gradient:

$$\nabla f = (3x^2 - 3y,\; -3x + 3y^2) = \mathbf{0}$$

From $3x^2 = 3y$, we get $y = x^2$. Substituting into $-3x + 3y^2 = 0$: $-3x + 3x^4 = 0 \Rightarrow 3x(x^3 - 1) = 0$, giving $x = 0$ or $x = 1$.

**Critical points: $(0, 0)$ and $(1, 1)$.**

**(b)**

$$H = \begin{bmatrix} 6x & -3 \\ -3 & 6y \end{bmatrix}$$

**(c)** At $(0, 0)$: $H = \begin{bmatrix} 0 & -3 \\ -3 & 0 \end{bmatrix}$. Eigenvalues: $\lambda^2 - 9 = 0 \Rightarrow \lambda = \pm 3$. One positive, one negative → **saddle point**.

At $(1, 1)$: $H = \begin{bmatrix} 6 & -3 \\ -3 & 6 \end{bmatrix}$. Eigenvalues: $(6 - \lambda)^2 - 9 = 0 \Rightarrow \lambda = 3, 9$. Both positive → **local minimum**.

**(d)** At the saddle point $(0,0)$, the Hessian is $\begin{bmatrix} 0 & -3 \\ -3 & 0 \end{bmatrix}$.

- For $\lambda = 3$: $(0 - 3)v_1 + (-3)v_2 = 0 \Rightarrow v_1 = -v_2$. Eigenvector: $\mathbf{(1, -1)/\sqrt{2}}$ — direction of **positive curvature** (surface curves upward).
- For $\lambda = -3$: $(0 + 3)v_1 + (-3)v_2 = 0 \Rightarrow v_1 = v_2$. Eigenvector: $\mathbf{(1, 1)/\sqrt{2}}$ — direction of **negative curvature** (surface curves downward).

The surface looks like a **horse saddle**: curving up along $(1, -1)$ and down along $(1, 1)$.

**(e)** $\kappa = |100 / 0.01| = \mathbf{10{,}000}$. This is highly ill-conditioned: gradient descent takes tiny steps along the direction of large curvature (eigenvalue 100) and overshoots along the flat direction (eigenvalue 0.01), producing very slow **zigzag convergence**. Adaptive optimizers like **Adam** or second-order methods (Newton's method using the Hessian inverse) address this by rescaling the gradient in each eigendirection.

---

### Question 6 (10 pts) — Double Integrals and Fubini's Theorem

**(a)**

Inner integral: $\displaystyle\int_0^x (x + y)\, dy = \left[xy + \frac{y^2}{2}\right]_0^x = x^2 + \frac{x^2}{2} = \frac{3x^2}{2}$

Outer integral: $\displaystyle\int_0^1 \frac{3x^2}{2}\, dx = \left[\frac{x^3}{2}\right]_0^1 = \mathbf{\frac{1}{2}}$

**(b)** Reversed limits: the region is $0 \le y \le 1$, $y \le x \le 1$.

$$\int_0^1 \int_y^1 (x + y)\, dx\, dy$$

Inner: $\displaystyle\left[\frac{x^2}{2} + xy\right]_y^1 = \frac{1}{2} + y - \frac{y^2}{2} - y^2 = \frac{1}{2} + y - \frac{3y^2}{2}$

Outer: $\displaystyle\int_0^1 \left(\frac{1}{2} + y - \frac{3y^2}{2}\right) dy = \frac{1}{2} + \frac{1}{2} - \frac{1}{2} = \mathbf{\frac{1}{2}}$ ✓

**(c)** Polar coordinates: $x^2 + y^2 = r^2$, and the Jacobian factor is $\mathbf{r}$ (so $dA = r\, dr\, d\theta$). Limits: $0 \le r \le 2$, $0 \le \theta \le 2\pi$.

$$\int_0^{2\pi} \int_0^2 r^2 \cdot r\, dr\, d\theta = \int_0^{2\pi} d\theta \cdot \int_0^2 r^3\, dr = 2\pi \cdot \left[\frac{r^4}{4}\right]_0^2 = 2\pi \cdot 4 = \mathbf{8\pi}$$

**(d)** Normalization: $C \iint e^{-(x^2+y^2)/2}\, dA = 1$. Switch to polar:

$$C \int_0^{2\pi} \int_0^{\infty} r\, e^{-r^2/2}\, dr\, d\theta = C \cdot 2\pi \cdot 1 = 2\pi C = 1$$

Therefore $\mathbf{C = 1/(2\pi)}$. This is the **standard bivariate normal distribution** $N(\mathbf{0}, I)$ in 2D.

---

### Question 7 (10 pts) — Change of Variables and the Jacobian Determinant

**(a)** For $x = r\cos\theta$, $y = r\sin\theta$:

$$J = \begin{bmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{bmatrix}$$

$$\det(J) = r\cos^2\theta + r\sin^2\theta = \mathbf{r}$$

Therefore $dA = |{\det(J)}|\, dr\, d\theta = r\, dr\, d\theta$. The factor $r$ accounts for the fact that at larger radius, a small change in $\theta$ sweeps out a larger arc.

**(b)** The general change of variables formula:

$$\iint f(x,y)\, dA = \iint f\bigl(x(u,v),\, y(u,v)\bigr) \left|\det\frac{\partial(x,y)}{\partial(u,v)}\right| du\, dv$$

**(c)** $Y = 2X + 3$, so $X = (Y - 3)/2$ and $|dX/dY| = 1/2$.

$$p_Y(y) = p_X\!\left(\frac{y-3}{2}\right) \cdot \left|\frac{1}{2}\right| = \frac{1}{\sqrt{2\pi}} \cdot \frac{1}{2} \cdot e^{-(y-3)^2/8}$$

This is $\mathbf{N(3, 4)}$ — a Gaussian with mean 3 and variance 4.

**(d)** The Jacobian determinant measures how much each transformation locally **stretches or compresses volume** (area in 2D). In normalizing flows, probability mass must be conserved: if a transformation stretches a region of space by a factor $|\det J|$, the probability density in that region must be diluted by $1/|\det J|$. This is why the log-density includes $-\sum_k \log|\det(J_{f_k})|$ — it accounts for all the volume changes along the chain of transformations.

---

### Question 8 (10 pts) — The Gaussian Integral and Its Multivariate Generalization

**(a)** Let $I = \int_{-\infty}^{\infty} e^{-x^2}\, dx$. Then:

$$I^2 = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} e^{-(x^2+y^2)}\, dx\, dy$$

Switch to polar coordinates ($x^2 + y^2 = r^2$, $dA = r\, dr\, d\theta$):

$$I^2 = \int_0^{2\pi}\int_0^{\infty} r\, e^{-r^2}\, dr\, d\theta = 2\pi \cdot \left[-\frac{1}{2}e^{-r^2}\right]_0^{\infty} = 2\pi \cdot \frac{1}{2} = \pi$$

Therefore $\mathbf{I = \sqrt{\pi}}$.

**(b)** Substitution $u = \sqrt{a}\, x$, so $du = \sqrt{a}\, dx$ and $dx = du/\sqrt{a}$:

$$\int_{-\infty}^{\infty} e^{-ax^2}\, dx = \int_{-\infty}^{\infty} e^{-u^2} \frac{du}{\sqrt{a}} = \frac{1}{\sqrt{a}} \cdot \sqrt{\pi} = \mathbf{\sqrt{\frac{\pi}{a}}}$$

**(c)** Start with standard normal $\mathbf{z} \sim N(\mathbf{0}, I)$ and apply the transformation $\mathbf{x} = \Sigma^{1/2}\mathbf{z} + \boldsymbol{\mu}$. The Jacobian of this linear transformation is $\Sigma^{1/2}$, with determinant $|\det(\Sigma^{1/2})| = |\det(\Sigma)|^{1/2}$. By the change of variables formula, we divide the standard normal density by this Jacobian determinant, which introduces the factor $|\det(\Sigma)|^{-1/2}$ in the multivariate Gaussian density.

**(d)** Two reasons for Gaussian ubiquity in ML:

1. **Central Limit Theorem** — sums of many independent random variables converge to a Gaussian, regardless of their individual distributions. Neural network pre-activations are sums of many terms, so they tend to be approximately Gaussian.
2. **Computational convenience** — Gaussians are closed under linear transformations, marginalization, and conditioning, all with closed-form expressions. This makes inference, sampling, and optimization analytically tractable.

---

### Question 9 (10 pts) — Multivariate Taylor Expansion

**(a)** Second-order Taylor expansion:

$$f(\mathbf{w}) \approx f(\mathbf{w}_0) + \nabla f(\mathbf{w}_0)^T (\mathbf{w} - \mathbf{w}_0) + \frac{1}{2}(\mathbf{w} - \mathbf{w}_0)^T H(\mathbf{w}_0)(\mathbf{w} - \mathbf{w}_0)$$

Blanks: **$\nabla f(\mathbf{w}_0)$** (the gradient) and **$H(\mathbf{w}_0)$** (the Hessian).

**(b)** At a critical point ($\nabla f(\mathbf{w}_0) = \mathbf{0}$):

$$f(\mathbf{w}) \approx f(\mathbf{w}_0) + \frac{1}{2}(\mathbf{w} - \mathbf{w}_0)^T H(\mathbf{w} - \mathbf{w}_0)$$

Near a critical point, the linear term vanishes, so the loss is completely determined by the **quadratic form defined by the Hessian**. The landscape IS a paraboloid — its shape, curvatures, and principal axes are entirely encoded in $H$.

**(c)** Minimize the quadratic approximation by setting its gradient to zero:

$$\nabla_{\mathbf{w}}\left[f(\mathbf{w}_0) + \nabla f^T(\mathbf{w}-\mathbf{w}_0) + \frac{1}{2}(\mathbf{w}-\mathbf{w}_0)^T H (\mathbf{w}-\mathbf{w}_0)\right] = \nabla f + H(\mathbf{w}-\mathbf{w}_0) = \mathbf{0}$$

Solving: $\mathbf{w} - \mathbf{w}_0 = -H^{-1}\nabla f$, giving the Newton update:

$$\boxed{\mathbf{w}_{\text{new}} = \mathbf{w}_0 - H^{-1}\nabla f(\mathbf{w}_0)}$$

**(d)** Newton's method **divides the gradient by the eigenvalue** in each eigendirection, producing equal-sized steps regardless of curvature — it takes a large step along flat directions and a small step along steep ones. Gradient descent, by contrast, takes steps **proportional to the eigenvalue**, leading to slow progress along flat directions and overshooting along steep ones → zigzag convergence. Newton's method is **impractical for 10M parameters** because computing and storing the Hessian requires $O(n^2) \approx 10^{14}$ entries, and inverting it requires $O(n^3) \approx 10^{21}$ operations — impossibly expensive.

---

### Question 10 (10 pts) — The Implicit Function Theorem

**(a)** $F(x,y) = x^2 + y^2 - 1$. Partial derivatives: $F_x = 2x$, $F_y = 2y$.

At $(\sqrt{2}/2, \sqrt{2}/2)$:

$$\frac{dy}{dx} = -\frac{F_x}{F_y} = -\frac{2(\sqrt{2}/2)}{2(\sqrt{2}/2)} = \mathbf{-1}$$

**(b)** The IFT fails where $F_y = 0$, i.e., $y = 0$. The points are $\mathbf{(\pm 1, 0)}$. Geometrically, the tangent line to the circle is **vertical** at these points — $y$ cannot be expressed as a single-valued function of $x$ near them.

**(c)** $F(w, \lambda) = w^3 - \lambda w$. At $(1, 1)$: $F = 1 - 1 = 0$ ✓.

$F_w = 3w^2 - \lambda$, $F_\lambda = -w$.

$$\frac{dw}{d\lambda} = -\frac{F_\lambda}{F_w} = -\frac{-1}{3(1)^2 - 1} = \mathbf{\frac{1}{2}}$$

Interpretation: increasing $\lambda$ by a small amount $\varepsilon$ increases the optimal $w$ by approximately $\varepsilon/2$.

**(d)** At $(w, \lambda) = (0, 0)$: $F_w = 3(0)^2 - 0 = 0$. Since $F_w = 0$, the IFT **fails**. Near this point, smooth changes in $\lambda$ can cause **discontinuous jumps** in the optimal $w$ — this is a **bifurcation point**. This relates to phase transitions in neural network training: small changes in a hyperparameter (learning rate, regularization strength) can cause qualitative shifts in the learned representations, corresponding to the parameter jumping between different branches of the solution manifold.

---

### Question 11 (10 pts) — Critical Points and the Second Derivative Test

**(a)** $f(x,y) = x^2 + y^2 - 2x - 4y + 8$.

$f_x = 2x - 2 = 0 \Rightarrow x = 1$. $f_y = 2y - 4 = 0 \Rightarrow y = 2$.

Critical point: $\mathbf{(1, 2)}$. Hessian: $H = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}$. Eigenvalues: $2, 2$ (both positive).

**Local minimum.** $f(1, 2) = 1 + 4 - 2 - 8 + 8 = \mathbf{3}$.

**(b)** $g(x,y) = x^2 - y^2 + 4x - 6y$.

$g_x = 2x + 4 = 0 \Rightarrow x = -2$. $g_y = -2y - 6 = 0 \Rightarrow y = -3$.

Critical point: $\mathbf{(-2, -3)}$. Hessian: $H = \begin{bmatrix} 2 & 0 \\ 0 & -2 \end{bmatrix}$. Eigenvalues: $2, -2$.

**Saddle point.**

**(c)** $h(x,y) = x^4 + y^4 - 4xy + 1$.

$h_x = 4x^3 - 4y = 0 \Rightarrow y = x^3$. $h_y = 4y^3 - 4x = 0 \Rightarrow x = y^3$.

Substituting: $x = (x^3)^3 = x^9$, so $x^9 - x = 0 \Rightarrow x(x^8 - 1) = 0$, giving $x = 0, \pm 1$.

Critical points: $\mathbf{(0,0)}$, $\mathbf{(1,1)}$, $\mathbf{(-1,-1)}$.

Hessian: $H = \begin{bmatrix} 12x^2 & -4 \\ -4 & 12y^2 \end{bmatrix}$

- At $(0,0)$: $H = \begin{bmatrix} 0 & -4 \\ -4 & 0 \end{bmatrix}$. Eigenvalues $\pm 4$ → **saddle point**.
- At $(1,1)$: $H = \begin{bmatrix} 12 & -4 \\ -4 & 12 \end{bmatrix}$. Eigenvalues $8, 16$ → **local minimum**.
- At $(-1,-1)$: $H = \begin{bmatrix} 12 & -4 \\ -4 & 12 \end{bmatrix}$. Eigenvalues $8, 16$ → **local minimum**.

**(d)** If each eigenvalue is independently equally likely to be positive or negative, the probability that all 100 eigenvalues are positive is:

$$\left(\frac{1}{2}\right)^{100} \approx \mathbf{10^{-30}}$$

This is essentially zero. In high dimensions, **almost all critical points are saddle points**. Local minima are exponentially rare, which is why gradient descent in deep learning can typically escape critical points — they are almost always saddle points with descent directions available.

---

### Question 12 (10 pts) — Lagrange Multipliers

Minimize $f(x,y) = x^2 + 2y^2$ subject to $g(x,y) = x + y - 3 = 0$.

**(a)** Lagrangian:

$$\mathcal{L}(x, y, \lambda) = x^2 + 2y^2 - \lambda(x + y - 3)$$

**(b)** Setting partial derivatives to zero:

$$\frac{\partial \mathcal{L}}{\partial x} = 2x - \lambda = 0, \quad \frac{\partial \mathcal{L}}{\partial y} = 4y - \lambda = 0, \quad x + y = 3$$

From the first two equations: $x = \lambda/2$, $y = \lambda/4$. Substituting into the constraint:

$$\frac{\lambda}{2} + \frac{\lambda}{4} = 3 \;\Rightarrow\; \frac{3\lambda}{4} = 3 \;\Rightarrow\; \lambda = 4$$

Therefore $\mathbf{x^* = 2}$, $\mathbf{y^* = 1}$, $\mathbf{\lambda^* = 4}$. Optimal value: $f(2,1) = 4 + 2 = \mathbf{6}$.

**(c)** $\nabla f(2,1) = (2 \cdot 2,\; 4 \cdot 1) = (4, 4)$. $\nabla g(2,1) = (1, 1)$.

Check: $\nabla f = \lambda^* \nabla g \Rightarrow (4,4) = 4 \cdot (1,1)$. ✓ **Parallel.**

**(d)** $\lambda^* = 4$. If the constraint is relaxed to $x + y = 3 + \varepsilon$, the optimal value of $f$ changes by approximately:

$$\Delta f \approx \lambda^* \cdot \varepsilon = \mathbf{4\varepsilon}$$

**(e)** Increasing $\lambda$ tightens the constraint (corresponds to a smaller constraint radius $C$), forcing $\|\mathbf{w}\|^2$ to be smaller → the weights must be smaller. Smaller weights reduce the model's capacity to fit noise in the training data, thereby reducing overfitting. From the constrained optimization perspective, $\lambda$ is the **"price" of violating the constraint** — a high $\lambda$ means the penalty for large weights is steep, so the optimizer strongly prefers small-weight solutions.

---

### Question 13 (10 pts) — KKT Conditions and Inequality Constraints

Minimize $f(x,y) = (x-3)^2 + (y-3)^2$ subject to $x + y \le 4$, $x \ge 0$, $y \ge 0$.

**(a)** Unconstrained minimum: $\nabla f = (2(x-3), 2(y-3)) = \mathbf{0}$ gives $(x,y) = \mathbf{(3,3)}$.

Check $x + y \le 4$: $3 + 3 = 6 > 4$. **Violates the constraint.**

**(b)** With $x + y = 4$ active, use Lagrange multipliers:

$$\mathcal{L} = (x-3)^2 + (y-3)^2 - \lambda(x+y-4)$$

$$2(x-3) - \lambda = 0, \quad 2(y-3) - \lambda = 0 \;\Rightarrow\; x = y$$

From $x + y = 4$: $x = y = 2$. Then $\lambda = 2(2-3) = -2$.

$f(2,2) = 1 + 1 = \mathbf{2}$. Check: $x = 2 \ge 0$ ✓, $y = 2 \ge 0$ ✓.

**(c)** **Complementary slackness:** For each inequality constraint $g_i(\mathbf{x}) \le 0$:

$$\lambda_i \cdot g_i(\mathbf{x}^*) = 0$$

Either the constraint is **active** ($g_i = 0$) or the multiplier is **zero** ($\lambda_i = 0$), or both. A constraint only "costs" something ($\lambda_i > 0$) if it is binding.

**(d)** Most training points lie far from the decision boundary, so their margin constraint is **inactive** (satisfied with slack). By complementary slackness, their Lagrange multipliers $\lambda_i = 0$. Only points on or near the margin boundary have $\lambda_i > 0$ — these are the **support vectors**. Since typically only a small fraction of points land exactly on the margin, the SVM decision function depends on only these few support vectors, making prediction **memory-efficient** (no need to store the entire training set).

---

### Question 14 (8 pts) — Regularization as Constrained Optimization

**(a)** Lagrangian: $\mathcal{L} = (\mathbf{y} - X\mathbf{w})^T(\mathbf{y} - X\mathbf{w}) - \lambda(\|\mathbf{w}\|^2 - C)$.

Taking the derivative and setting to zero:

$$\frac{\partial \mathcal{L}}{\partial \mathbf{w}} = -2X^T(\mathbf{y} - X\mathbf{w}) - 2\lambda\mathbf{w} = \mathbf{0}$$

$$X^T\mathbf{y} = X^TX\mathbf{w} + \lambda\mathbf{w} = (X^TX + \lambda I)\mathbf{w}$$

$$\boxed{\mathbf{w} = (X^TX + \lambda I)^{-1} X^T\mathbf{y}}$$

**(b)** $X^TX$ is positive semi-definite with eigenvalues $\mu_i \ge 0$. Adding $\lambda I$ shifts every eigenvalue to $\mu_i + \lambda > 0$ (since $\lambda > 0$). All eigenvalues are now strictly positive, making the matrix **positive definite and therefore invertible**.

**(c)** The L2 constraint region ($\|\mathbf{w}\|_2^2 \le C$) is a **circle** (sphere); the L1 constraint region ($\|\mathbf{w}\|_1 \le C$) is a **diamond** (cross-polytope). The elliptical loss contours are more likely to first touch the diamond at a **corner**, where some coordinates are exactly zero → **sparse** solutions. The circle has no corners, so the tangency point generically has **all coordinates nonzero**.

**(d)** The Lagrange multiplier $\lambda$ is the **shadow price** of the constraint: it measures how much the optimal loss would improve if the constraint were relaxed by one unit. A **high** $\lambda$ means the constraint is expensive — the model badly wants more capacity and would benefit greatly from relaxing it. A **low** $\lambda$ means the constraint barely matters — the model is already nearly unconstrained at its optimum.

---

### Question 15 (10 pts) — Synthesis: Multivariable Calculus as the Language of Optimization

**(a)**

| Element | Concept (Lesson) |
|---------|-------------------|
| $\nabla L(\mathbf{w}_t)$ | **Gradient** — partial derivatives assembled into a vector (Q1) |
| Direction $-\nabla L$ | **Steepest descent direction** — the gradient points in the direction of greatest increase, so its negative gives greatest decrease (Q1e) |
| Choosing step size $\eta$ | **Hessian / curvature** bounds the safe range — the Taylor approximation is only accurate within a region determined by second derivatives (Q5, Q9) |
| Classifying the convergence point | **Second derivative test / Hessian eigenvalue analysis** — sign of eigenvalues determines min, max, or saddle (Q5, Q11) |
| Adding constraint $\|\mathbf{w}\| \le C$ | **Lagrange multipliers** (Q12) |

**(b)** If all Jacobians have largest singular value $> 1$: gradients **explode** exponentially through layers (each layer amplifies the gradient by a factor $> 1$, compounding over depth).

If all have largest singular value $< 1$: gradients **vanish** exponentially (each layer attenuates the gradient, and the product shrinks to zero).

**(c)** Start with $\mathbf{z} \sim N(\mathbf{0}, I)$, which has density:

$$q_0(\mathbf{z}) = (2\pi)^{-d/2} e^{-\|\mathbf{z}\|^2/2}$$

This normalization constant comes from the **multivariate Gaussian integral** (Q8). Apply $\mathbf{x} = f(\mathbf{z})$. By the **change of variables formula** (Q7):

$$\log p(\mathbf{x}) = \log q_0(\mathbf{z}) - \log|\det(J_f)|$$

$$= -\frac{d}{2}\log(2\pi) - \frac{\|\mathbf{z}\|^2}{2} - \sum_k \log|\det(J_{f_k})|$$

The **Jacobian determinant** (Q7) appears because each transformation stretches/compresses volume, and the density must be adjusted accordingly to conserve probability mass.

**(d)** Conceptual chain:

$$\text{Loss } L(\mathbf{w}) \xrightarrow{\text{Gradient}} \text{Direction to step}$$

$$\xrightarrow{\text{Hessian}} \text{Shape of landscape at critical point}$$

$$\xrightarrow{\text{Lagrange multipliers}} \text{Optimal point under constraints}$$

$$\xrightarrow{\lambda^* \text{ sensitivity}} \text{Sensitivity of optimum to constraint changes}$$

---

*End of answer key. Total: 150 points across 15 questions.*
