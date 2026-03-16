# Exam 2E: ML-Applied Calculus — Answer Key

**The Path to AI Alignment — Lessons 34–36 Assessment**

> **Grading philosophy:** Full credit requires both correct computation and clear reasoning. Partial credit is generous for correct setup with arithmetic errors. Conceptual parts are graded on precision of language and demonstrated understanding of the ML connection — vague hand-waving earns at most half credit.

---

### Question 1 (10 pts) — Matrix Calculus Identities

**(a)** Let $f(\mathbf{x}) = A\mathbf{x}$ where $A$ is $m \times n$ and $\mathbf{x} \in \mathbb{R}^n$.

The Jacobian is:

$$\frac{\partial f}{\partial \mathbf{x}} = A$$

**Dimensions: $m \times n$** (the same dimensions as $A$ itself).

This generalizes the 1D rule "the derivative of a linear function is the coefficient." In one dimension, $\frac{d}{dx}(ax) = a$. In the multivariate case, the Jacobian of a linear map **is** the matrix defining that map.

**(b)** Let $g(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$. Expand $g(\mathbf{x} + \varepsilon \mathbf{e}_i)$:

$$g(\mathbf{x} + \varepsilon \mathbf{e}_i) = (\mathbf{x} + \varepsilon \mathbf{e}_i)^T A (\mathbf{x} + \varepsilon \mathbf{e}_i) = \mathbf{x}^T A \mathbf{x} + \varepsilon \mathbf{e}_i^T A \mathbf{x} + \varepsilon \mathbf{x}^T A \mathbf{e}_i + \varepsilon^2 \mathbf{e}_i^T A \mathbf{e}_i$$

Reading off the coefficient of $\varepsilon$:

$$\frac{\partial g}{\partial x_i} = \mathbf{e}_i^T A \mathbf{x} + \mathbf{x}^T A \mathbf{e}_i = (A\mathbf{x})_i + (A^T\mathbf{x})_i = \bigl((A + A^T)\mathbf{x}\bigr)_i$$

Therefore:

$$\boxed{\frac{dg}{d\mathbf{x}} = (A + A^T)\mathbf{x}}$$

When $A$ is symmetric ($A = A^T$), this **simplifies to $2A\mathbf{x}$**.

**(c)** Backpropagation computes $\frac{\partial L}{\partial \mathbf{w}} = \frac{\partial L}{\partial \mathbf{y}} \cdot \frac{\partial \mathbf{y}}{\partial \mathbf{w}}$ — this is a **vector-Jacobian product (VJP)**, multiplying the upstream gradient (a row vector) by the Jacobian. Since the loss $L$ is scalar-valued, we only ever need one backward pass to compute all VJPs for every parameter. The layout convention (numerator vs. denominator) doesn't matter operationally because VJPs are the atomic operation that backpropagation actually executes.

---

### Question 2 (10 pts) — Computation Graphs and Autodiff

Single neuron: $z = Wx + b$, $a = \text{ReLU}(z)$, $L = \frac{1}{2}(a - y)^2$ with $W = 2$, $x = 3$, $b = -1$, $y = 4$.

**(a)** Forward pass:

$$z = 2(3) + (-1) = 5$$

$$a = \max(0, 5) = 5$$

$$L = \frac{1}{2}(5 - 4)^2 = \mathbf{0.5}$$

**(b)** Backward pass — local derivatives and chain rule:

$$\frac{\partial L}{\partial a} = a - y = 5 - 4 = 1$$

$$\frac{\partial a}{\partial z} = 1 \quad \text{(since } z = 5 > 0 \text{, ReLU derivative is 1)}$$

$$\frac{\partial z}{\partial W} = x = 3, \qquad \frac{\partial z}{\partial b} = 1$$

Applying the chain rule:

$$\boxed{\frac{\partial L}{\partial W} = \frac{\partial L}{\partial a} \cdot \frac{\partial a}{\partial z} \cdot \frac{\partial z}{\partial W} = 1 \cdot 1 \cdot 3 = \mathbf{3}}$$

$$\boxed{\frac{\partial L}{\partial b} = \frac{\partial L}{\partial a} \cdot \frac{\partial a}{\partial z} \cdot \frac{\partial z}{\partial b} = 1 \cdot 1 \cdot 1 = \mathbf{1}}$$

**(c)** Forward-mode autodiff propagates tangent vectors forward:

$$\frac{\partial z}{\partial W} = 3 \;\to\; \frac{\partial a}{\partial W} = 1 \cdot 3 = 3 \;\to\; \frac{\partial L}{\partial W} = 1 \cdot 3 = 3$$

Forward mode requires **one forward pass per parameter**. For $N$ parameters, that means $N$ forward passes. Reverse mode computes gradients with respect to **all** parameters in a single backward pass.

**(d)** With $10^8$ parameters and 1 scalar loss:

- Forward mode: $10^8$ passes (one per parameter)
- Reverse mode: **1 backward pass** for all parameters

Reverse mode is **$\sim 10^8$ times more efficient**. This is why backpropagation (reverse-mode autodiff) is used universally in deep learning — it scales with the number of outputs, not the number of parameters.

---

### Question 3 (10 pts) — The Optimization Zoo

Quadratic loss surface with eigenvalues $\lambda_1 = 100$ (steep direction) and $\lambda_2 = 1$ (flat direction).

**(a)** Vanilla SGD update rule:

$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla L(\mathbf{w}_t)$$

On the ravine landscape: gradients are **large** along the steep direction ($\lambda_1 = 100$) and **small** along the flat direction ($\lambda_2 = 1$). The learning rate must be small enough for stability in the steep direction, but this makes progress agonizingly slow in the flat direction. Result: **zigzag trajectory** — oscillating back and forth across the ravine while inching along the bottom.

**(b)** Momentum update rule:

$$\mathbf{v}_t = \beta \mathbf{v}_{t-1} + \nabla L(\mathbf{w}_t)$$

$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \mathbf{v}_t$$

**Physical analogy:** A heavy ball rolling through the ravine accumulates velocity along the consistent direction (the bottom of the ravine). The oscillations in the steep direction **cancel out** over time — the velocity averages to near zero across the ravine — while the component along the bottom **accumulates**. Momentum smooths out oscillations and accelerates progress along the consistent gradient direction.

**(c)** Adam update rules:

$$m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t \qquad \text{(first moment estimate)}$$

$$v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2 \qquad \text{(second moment estimate)}$$

$$\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \qquad \hat{v}_t = \frac{v_t}{1 - \beta_2^t} \qquad \text{(bias correction)}$$

$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \varepsilon}$$

Parameters with **sparse or noisy gradients** get **larger effective learning rates** because their $\hat{v}_t$ (the denominator) is small. Parameters with consistently large gradients get smaller effective rates because $\hat{v}_t$ is large. Adam naturally **up-weights rare but informative gradients**.

**(d)** **Adam + L2 regularization** adds $\lambda \mathbf{w}$ to the gradient before the adaptive step. The regularization term then gets divided by $\sqrt{\hat{v}_t}$, so heavily-updated parameters receive **less** regularization — the opposite of the intended effect.

**AdamW** decouples weight decay from the gradient: it applies $\mathbf{w}_t \leftarrow \mathbf{w}_t - \eta \lambda \mathbf{w}_t$ directly to the weights, **separate** from the Adam update. This ensures all parameters are regularized equally regardless of their gradient history.

BERT and other large language models use **AdamW**. The distinction matters for large models because incorrect regularization scaling can allow undertrained parameters to retain large weights, harming generalization.

---

### Question 4 (10 pts) — Learning Rate Schedules

**(a)** A function $f$ is convex if:

$$f\bigl(\lambda \mathbf{x} + (1 - \lambda)\mathbf{y}\bigr) \leq \lambda f(\mathbf{x}) + (1 - \lambda) f(\mathbf{y}) \quad \text{for all } \lambda \in [0, 1]$$

Key property: **every local minimum is a global minimum**.

Neural network loss surfaces are **not convex** — the composition of nonlinear activation functions across layers creates many local minima and, more importantly, many saddle points.

**(b)** At random initialization, gradients can be very large and unreliable (high variance, poorly directed). A **small initial learning rate prevents catastrophic updates** based on these noisy early gradients. Warmup gives the adaptive optimizer (e.g., Adam) time to **accumulate reliable gradient statistics** in $m_t$ and $v_t$ before taking large steps.

**(c)** Cosine annealing smoothly decreases the learning rate from $\eta_{\max}$ to $\eta_{\min}$ following a half-cosine curve:

$$\eta_t = \eta_{\min} + \frac{1}{2}(\eta_{\max} - \eta_{\min})\Bigl(1 + \cos\bigl(\pi t / T\bigr)\Bigr)$$

The **gradual decay near the end** allows the optimizer to settle precisely into a minimum without overshooting, unlike a sharp step-down schedule which can cause transient instability at each drop.

**(d)** Temporarily increasing the learning rate can help the optimizer **escape sharp local minima** (which tend to generalize poorly). The large-LR noise destabilizes narrow basins but not wide ones. After the learning rate decreases again, the optimizer settles into a **flatter minimum**.

This leverages the **flat minima $\leftrightarrow$ good generalization** hypothesis: flat minima are robust to perturbations in weight space, implying robustness to distribution shift at test time.

---

### Question 5 (10 pts) — Saddle Points

**(a)** If each eigenvalue is independently positive or negative with equal probability, then the probability all $n = 100$ eigenvalues are positive (i.e., the critical point is a true local minimum):

$$P = \left(\frac{1}{2}\right)^{100} = 2^{-100} \approx 10^{-30}$$

**Essentially zero.** In high dimensions, virtually all critical points are saddle points.

**(b)** Eigenvalues $\lbrace 5, 3, 1, -0.5, -2 \rbrace$: this is a **saddle point**.

- **3 positive eigenvalues** → minimum in those directions
- **2 negative eigenvalues** → maximum in those directions
- **Index = 2** (the number of negative eigenvalues)

**(c)** Near a saddle point, the gradient is approximately zero in all directions ($\nabla L \approx \mathbf{0}$), so gradient descent **stalls** — updates become tiny because $\|\nabla L\|$ is near zero.

**SGD noise rescues the trajectory.** The stochastic gradient adds random perturbations that eventually push the trajectory along the **negative curvature directions** (escape directions where the loss decreases). Deterministic gradient descent would slow to a crawl; stochasticity provides the perturbation needed to escape.

**(d)** Empirical observation (Dauphin et al.): critical points with **higher loss** tend to have **higher index** (more negative eigenvalues, more saddle-like). Critical points with **low loss** tend to be near-minima (few or no negative eigenvalues).

The practical implication: **optimization need not find a true global minimum**. Simply reaching any low-loss region of the landscape automatically avoids the worst saddle points. The loss value itself is a reliable proxy for the quality of the critical point.

---

### Question 6 (10 pts) — Gradient Flow and Stability

**(a)** For $L(w) = \frac{1}{2}(w - w^*)^2$, the gradient flow ODE is:

$$\frac{dw}{dt} = -\frac{dL}{dw} = -(w - w^*)$$

This is a first-order linear ODE with solution:

$$\boxed{w(t) = w^* + \bigl(w(0) - w^*\bigr) e^{-t}}$$

As $t \to \infty$, $w(t) \to w^*$. The trajectory **exponentially converges** to the minimum.

**(b)** Compute the time derivative of the loss along the gradient flow trajectory:

$$\frac{dL}{dt} = \nabla L \cdot \frac{d\mathbf{W}}{dt} = \nabla L \cdot (-\nabla L) = -\|\nabla L\|^2 \leq 0$$

Since $L \geq 0$ (squared error is non-negative) and $\frac{dL}{dt} \leq 0$ (always decreasing or constant), **$L$ is a Lyapunov function**. This guarantees the loss decreases monotonically along the gradient flow, ensuring convergence to a critical point.

**(c)** For $L(w) = \frac{1}{2}\lambda w^2$, the gradient descent update is:

$$w_{t+1} = w_t - \eta \lambda w_t = (1 - \eta\lambda) w_t$$

Convergence requires $|1 - \eta\lambda| < 1$:

$$-1 < 1 - \eta\lambda < 1 \;\;\Longrightarrow\;\; 0 < \eta < \frac{2}{\lambda}$$

$$\boxed{\eta_{\max} = \frac{2}{\lambda}}$$

**(d)** With $\lambda_{\max} = 100$ and $\lambda_{\min} = 0.1$:

$$\eta_{\max} = \frac{2}{\lambda_{\max}} = \frac{2}{100} = \mathbf{0.02}$$

$$\kappa = \frac{\lambda_{\max}}{\lambda_{\min}} = \frac{100}{0.1} = \mathbf{1000}$$

A large condition number means the learning rate is **constrained by the steepest direction** ($\lambda_{\max}$), but progress along the flattest direction is proportional to $\eta \cdot \lambda_{\min}$, which is extremely small ($0.02 \times 0.1 = 0.002$). Result: **extremely slow convergence** along the flat eigendirection — the optimizer barely moves in that direction while being forced to use a tiny step size to stay stable in the steep direction.

---

### Question 7 (10 pts) — Momentum and Neural ODEs

**(a)** The damped second-order ODE for optimization:

$$m \frac{d^2 \mathbf{W}}{dt^2} + \gamma \frac{d\mathbf{W}}{dt} = -\nabla L(\mathbf{W})$$

Physical interpretation of each term:

- **Mass $m$:** Inertia — resistance to changes in direction
- **Friction $\gamma$:** Damping — energy dissipation that prevents perpetual oscillation
- **Force $-\nabla L$:** The gradient drives the motion toward lower loss

**Underdamped case** (low $\gamma$): insufficient friction → the system **overshoots the minimum and oscillates** back and forth before eventually settling. This corresponds to momentum with too little damping in optimization.

**(b)** The residual network update:

$$\mathbf{h}_{t+1} = \mathbf{h}_t + f(\mathbf{h}_t, \theta_t)$$

This is **exactly Euler's method** applied to the ODE $\frac{d\mathbf{h}}{dt} = f(\mathbf{h}, t)$ with step size $\Delta t = 1$. Each residual layer corresponds to one Euler step, and **the layer index plays the role of time**. A ResNet is a discretization of a continuous dynamical system.

**(c)** Neural ODEs use the **adjoint method** for backpropagation, which does not require storing intermediate activations.

- **Standard ResNets:** Must store all intermediate $\mathbf{h}_t$ for backprop → **$O(L)$ memory** for $L$ layers
- **Neural ODEs (adjoint method):** Integrate backward in time, recomputing activations as needed → **$O(1)$ memory** (constant, independent of effective depth)

This is the key memory advantage of Neural ODEs over discrete ResNets.

**(d)** The SGD noise term scales as $\sqrt{\eta / B}$ where $\eta$ is the learning rate and $B$ is the batch size.

- **As $B$ increases:** noise decreases → more deterministic updates
- **As $\eta$ decreases:** noise also decreases

This noise acts as **implicit regularization**: it prevents the optimizer from settling into sharp minima (where high curvature amplifies the noise), pushing it toward **flat minima that generalize better**. Larger batches remove this beneficial noise, which is one reason **small-batch SGD often generalizes better** than large-batch training — the noise itself is a feature, not a bug.

---

### Question 8 (10 pts) — Edge of Stability and Grokking

**(a)** Classical theory predicts: when the sharpness (largest Hessian eigenvalue $\lambda_{\max}$) exceeds $2/\eta$, gradient descent should diverge (the learning rate exceeds the stability bound from Q6c).

**What actually happens (Edge of Stability):** The loss briefly increases (non-monotonic behavior), but then the optimization trajectory **self-corrects**. It moves to regions of lower sharpness, and the sharpness **self-regulates to hover near $2/\eta$**. The landscape and trajectory co-evolve rather than the trajectory passively descending a fixed landscape. The optimizer and the loss surface are coupled dynamically.

**(b)** Grokking training dynamics (sketch description):

- **Training loss** drops quickly to $\approx 0$ (memorization phase, early in training)
- **Training accuracy** reaches 100% early
- **Test accuracy** remains at chance level for a long time, then **suddenly jumps to near-perfect** much later (generalization phase)
- The gap between memorization and generalization can be **$10$–$100\times$** the time needed to memorize

The key signature is the **long plateau in test performance** followed by a sharp transition to generalization, well after the training loss has converged.

**(c)** The memorizing solution sits in a **sharp minimum** (high sharpness, low training loss). The SGD noise term (proportional to $\eta / B$ from Q7d) creates an effective "temperature" that makes sharp minima **unstable over long timescales**.

Eventually, the accumulated noise **kicks the model out of the sharp memorizing basin** and into a **flatter generalizing basin** — this transition is grokking. The timescale of grokking depends on how deep the sharp memorizing basin is relative to the noise magnitude: deeper basins take longer to escape.

**(d)** The "ball rolling downhill" metaphor assumes a **fixed landscape** where the optimizer passively descends. This picture fails in three critical ways:

1. **The loss landscape changes as the model learns.** The Hessian evolves throughout training — edge of stability demonstrates that the sharpness actively adapts to the learning rate rather than being a static property.

2. **The trajectory exhibits stochastic phase transitions.** Grokking shows the model fundamentally reorganizing its solution from memorization to generalization — a qualitative change that has no analog in passive ball-on-a-hill dynamics.

3. **The optimizer interacts bidirectionally with the landscape.** The trajectory reshapes the effective landscape it experiences, and the landscape constrains the trajectory. This violates the passive "ball on a fixed hill" assumption.

Both **edge of stability** (sharpness self-regulation near $2/\eta$) and **grokking** (delayed generalization through noise-driven escape from sharp minima) demonstrate that modern deep learning optimization is a **coupled dynamical system**, not passive descent on a fixed surface.
