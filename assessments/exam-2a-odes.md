# Exam 2A: Ordinary Differential Equations

**The Path to AI Alignment — Lessons 14–18 Comprehensive Assessment**

---

| | |
|---|---|
| **Time Allowed** | 90 minutes |
| **Total Points** | 150 |
| **Materials** | Pencil, paper, calculator (no CAS). No code. |
| **Format** | 15 questions mixing computation and conceptual depth |

> **Advice:** Show all work. Partial credit is generous for correct reasoning even with arithmetic errors. Geometric and qualitative explanations are valued alongside algebraic work.

> *"Gradient descent is a discretized ODE. Euler's method is gradient descent. Understanding the continuous system tells you about the discrete algorithm."*

---

## Q1 (8 pts) — ODE Classification

Classify each ODE by **order**, **linearity** (linear or nonlinear), and whether it is **autonomous** or non-autonomous. No solving required.

**(a)**

$$\frac{dy}{dt} = 3y - y^2$$

**(b)**

$$y'' + 4y' + 3y = \sin(t)$$

**(c)**

$$y''' = y\,y''$$

**(d)**

$$\frac{dy}{dt} = e^{-t}\,y + t^2$$

**(e)** In one sentence: why does the distinction between linear and nonlinear matter so much more than it does in algebra? *(Hint: think about the superposition principle and the tools available for each case.)*

---

## Q2 (10 pts) — Direction Fields, Fixed Points, and Existence

Consider the autonomous ODE:

$$\frac{dy}{dt} = y(2 - y)(y - 1)$$

**(a)** Find all fixed points (equilibria).

**(b)** Determine the stability of each fixed point by analyzing the sign of $\frac{dy}{dt}$ in the intervals between them. Draw a phase line with arrows.

**(c)** Sketch a rough direction field for this ODE. Then sketch solution curves starting from $y(0) = 0.5$, $y(0) = 1.5$, and $y(0) = 3$.

**(d)** The Picard–Lindelöf theorem guarantees existence and uniqueness of solutions when $f(t, y)$ and $\frac{\partial f}{\partial y}$ are continuous. For this ODE, is $f(t, y) = y(2 - y)(y - 1)$ Lipschitz in $y$ on any bounded interval? What does this guarantee about solution curves crossing?

**(e)** Consider instead $\frac{dy}{dt} = y^{1/3}$ with $y(0) = 0$. Show that both $y(t) = 0$ and $y(t) = \left(\frac{2t}{3}\right)^{3/2}$ are solutions. Why does uniqueness fail here?

---

## Q3 (10 pts) — Separable Equations

**(a)** Solve the separable ODE with initial condition:

$$\frac{dy}{dx} = xy^2, \qquad y(0) = 1$$

Show each step of the separation and integration.

**(b)** Does the solution from part (a) exist for all $x$? If not, at what value of $x$ does it blow up? Interpret this geometrically.

**(c)** Solve the logistic equation:

$$\frac{dy}{dt} = 2y\!\left(1 - \frac{y}{10}\right), \qquad y(0) = 1$$

*(Hint: use partial fractions.)*

**(d)** The logistic equation is the continuous-time version of the sigmoid function's dynamics. If $y$ represents a model's confidence during training, explain in 1–2 sentences what the carrying capacity $K = 10$ represents and why the growth slows as $y \to K$.

---

## Q4 (10 pts) — Integrating Factors and Exact Equations

**(a)** Solve the first-order linear ODE:

$$\frac{dy}{dx} + 2y = e^{-x}, \qquad y(0) = 3$$

Find the integrating factor, multiply through, and solve.

**(b)** Determine whether the equation is exact:

$$(2xy + 3)\,dx + (x^2 + 4y)\,dy = 0$$

If so, find the solution $F(x, y) = C$.

**(c)** For the non-exact equation:

$$(y + 1)\,dx - x\,dy = 0$$

Find an integrating factor that depends on $x$ alone (or $y$ alone), make the equation exact, and solve.

**(d)** The integrating factor technique transforms a hard problem into an easy one by multiplying by the right function. In one sentence, state an analogous idea in ML where multiplying or reweighting transforms a hard problem. *(Think: importance sampling, attention weights, or preconditioning.)*

---

## Q5 (12 pts) — Euler's Method IS Gradient Descent

Consider the ODE:

$$\frac{dy}{dt} = -4y, \qquad y(0) = 3$$

**(a)** Write the exact analytical solution $y(t)$.

**(b)** Apply Euler's method with step size $h = 0.25$ for 4 steps. Show $y_1, y_2, y_3, y_4$ and compare $y_4$ with the exact value at $t = 1$.

**(c)** Now try $h = 0.6$. Compute 4 steps. What happens? Explain why the approximation oscillates.

**(d)** For the general ODE $\frac{dy}{dt} = \lambda y$ (with $\lambda < 0$), the stability condition for Euler's method is $|1 + h\lambda| < 1$. For $\lambda = -4$, derive the range of step sizes $h$ that keep Euler's method stable.

**(e)** Now make the connection explicit. Gradient descent on the loss $L(w) = 2w^2$ gives the update rule $w_{t+1} = w_t - \eta \frac{dL}{dw}$. Write out this update. The corresponding continuous-time ODE (gradient flow) is $\frac{dw}{dt} = -\frac{dL}{dw}$. Write it out. Show that Euler's method applied to this gradient flow ODE with step size $h = \eta$ reproduces exactly the gradient descent update.

**(f)** Using part (d), what is the maximum learning rate $\eta$ that keeps gradient descent stable for $L(w) = 2w^2$? What happens if you exceed it?

---

## Q6 (10 pts) — The Characteristic Equation

**(a)** Solve (two distinct real roots):

$$y'' - 5y' + 6y = 0$$

Write the general solution and find the specific solution with $y(0) = 2$, $y'(0) = 1$.

**(b)** Solve (repeated root):

$$y'' + 4y' + 4y = 0$$

Write the general solution.

**(c)** Solve (complex roots):

$$y'' + 2y' + 5y = 0$$

Write the general solution in real form using sines and cosines.

**(d)** For part (c), describe the qualitative behavior of solutions as $t \to \infty$. This is a damped oscillation. In the spring-mass-damper analogy $my'' + by' + ky = 0$, identify what physical quantities correspond to $m$, $b$, and $k$.

**(e)** In momentum-based gradient descent, the update has the form:

$$w_{t+1} = w_t + \beta(w_t - w_{t-1}) - \eta \nabla L$$

This is a second-order difference equation. In the continuous limit, it becomes a second-order ODE. Explain in 2–3 sentences how the damping coefficient relates to the momentum parameter $\beta$, and why underdamped (oscillatory) dynamics correspond to too much momentum.

---

## Q7 (12 pts) — Undetermined Coefficients and Variation of Parameters

**(a)** Find a particular solution using undetermined coefficients:

$$y'' - 3y' + 2y = 4e^{3t}$$

**(b)** Find a particular solution:

$$y'' - 3y' + 2y = 5e^{2t}$$

Note that $e^{2t}$ is a solution to the homogeneous equation. What modification to your guess is needed, and why?

**(c)** Find a particular solution using variation of parameters:

$$y'' + y = \sec(t)$$

*(This is a case where undetermined coefficients fails.)* Set up the system for $u_1'$ and $u_2'$ using the fundamental solutions $y_1 = \cos(t)$, $y_2 = \sin(t)$, and solve.

**(d)** Why does undetermined coefficients only work for certain forcing functions (polynomials, exponentials, sines/cosines, and products thereof), while variation of parameters works for any continuous $g(t)$? Answer in 1–2 sentences.

---

## Q8 (10 pts) — Resonance

Consider the forced undamped oscillator:

$$y'' + 9y = F_0 \cos(\omega t)$$

**(a)** When $\omega \neq 3$, find the general solution. *(The particular solution has the form $A\cos(\omega t)$.)*

**(b)** When $\omega = 3$, the standard guess fails. Find the particular solution in this resonance case. *(Hint: try $t\cos(3t)$ or $t\sin(3t)$.)*

**(c)** Describe physically what happens at resonance: why does the amplitude grow without bound? Sketch the solution qualitatively.

**(d)** Now add damping:

$$y'' + 0.2y' + 9y = F_0 \cos(3t)$$

Does resonance still cause blow-up? Why or why not? Describe the steady-state behavior.

**(e)** In neural network training, certain learning rate and momentum combinations can cause loss oscillations that grow over time. Explain in 2–3 sentences how this is analogous to resonance in a forced oscillator. What plays the role of damping in practice?

---

## Q9 (10 pts) — Laplace Transform Fundamentals

**(a)** Using the definition:

$$\mathcal{L}\{f(t)\} = \int_0^{\infty} e^{-st}\,f(t)\,dt$$

compute the Laplace transform of $f(t) = e^{3t}$ from the definition. State for which values of $s$ the integral converges.

**(b)** Compute the Laplace transform of $f(t) = t^2 e^{-t}$. *(Use the first shifting theorem: $\mathcal{L}\{e^{at}f(t)\} = F(s - a)$.)*

**(c)** State the derivative property: $\mathcal{L}\{y'(t)\} = \;?$ Express it in terms of $Y(s) = \mathcal{L}\{y(t)\}$ and the initial condition $y(0)$. Then state $\mathcal{L}\{y''(t)\}$.

**(d)** Explain in 2–3 sentences why the derivative property is powerful: how does it convert a differential equation into an algebraic equation? What type of equation do you get in the $s$-domain?

---

## Q10 (10 pts) — Solving ODEs with the Laplace Transform

Use the Laplace transform to solve:

$$y'' + 4y = 8, \qquad y(0) = 0, \quad y'(0) = 0$$

**(a)** Take the Laplace transform of both sides. Apply the derivative property to express everything in terms of $Y(s)$.

**(b)** Solve for $Y(s)$.

**(c)** Decompose $Y(s)$ using partial fractions.

**(d)** Invert each term to find $y(t)$.

**(e)** Verify your answer by substituting $y(t)$ back into the original equation and checking the initial conditions.

---

## Q11 (10 pts) — Convolution and Impulse Response

**(a)** State the convolution theorem: if $\mathcal{L}\{f\} = F(s)$ and $\mathcal{L}\{g\} = G(s)$, then $\mathcal{L}^{-1}\{F(s)\,G(s)\} = \;?$

**(b)** Compute $\mathcal{L}^{-1}\!\left\{\frac{1}{s(s + 2)}\right\}$ by writing $\frac{1}{s(s+2)}$ as a product $F(s)\,G(s)$ and applying the convolution theorem. Verify your answer using partial fractions.

**(c)** The impulse response $h(t)$ of a system is defined as the output when the input is a Dirac delta $\delta(t)$. For the system:

$$y'' + 3y' + 2y = \delta(t), \qquad y(0) = 0, \quad y'(0) = 0$$

find the transfer function $H(s) = Y(s)$. Then find $h(t)$ by inverting $H(s)$.

**(d)** In a neural network, a perturbation to one layer's output propagates through subsequent layers. Explain in 2–3 sentences how the impulse response concept relates to understanding how a small change (an "impulse") at layer $k$ affects the network's output. What plays the role of the transfer function?

---

## Q12 (12 pts) — Systems $\frac{d\mathbf{x}}{dt} = A\mathbf{x}$: The Eigenvalue Method

Consider the system $\frac{d\mathbf{x}}{dt} = A\mathbf{x}$ where:

$$A = \begin{bmatrix} -1 & 4 \\ -1 & 3 \end{bmatrix}$$

**(a)** Find the eigenvalues of $A$.

**(b)** Find the eigenvectors corresponding to each eigenvalue.

**(c)** Write the general solution:

$$\mathbf{x}(t) = c_1\,e^{\lambda_1 t}\,\mathbf{v}_1 + c_2\,e^{\lambda_2 t}\,\mathbf{v}_2$$

**(d)** Find the specific solution with $\mathbf{x}(0) = \begin{bmatrix} 3 \\ 1 \end{bmatrix}$.

**(e)** Describe the behavior as $t \to \infty$. Along which eigendirection do solutions move? Classify this as a stable node, unstable node, saddle, spiral, or center.

**(f)** If these eigenvalues were instead eigenvalues of the Hessian of a loss function at a critical point, what would you conclude about the critical point?

---

## Q13 (12 pts) — Phase Portrait Classification

For each $2 \times 2$ matrix $A$ below, find the eigenvalues, classify the phase portrait type, and sketch the qualitative behavior of trajectories near the origin. State whether the origin is stable, unstable, or neither.

**(a)**

$$A = \begin{bmatrix} -3 & 0 \\ 0 & -1 \end{bmatrix}$$

*(diagonal matrix with both eigenvalues negative)*

**(b)**

$$A = \begin{bmatrix} 2 & 0 \\ 0 & -1 \end{bmatrix}$$

*(eigenvalues of opposite sign)*

**(c)**

$$A = \begin{bmatrix} -1 & 2 \\ -2 & -1 \end{bmatrix}$$

*(complex eigenvalues with negative real part)*

**(d)**

$$A = \begin{bmatrix} 0 & 1 \\ -4 & 0 \end{bmatrix}$$

*(purely imaginary eigenvalues)*

**(e)** Connect these to training dynamics: for each type above, describe what the corresponding training behavior would look like if $\frac{d\mathbf{x}}{dt} = A\mathbf{x}$ described the evolution of two weight parameters near a critical point of the loss.

---

## Q14 (8 pts) — Matrix Exponentials

**(a)** Write the definition of the matrix exponential:

$$e^{At} = \;?$$

*(Express as an infinite series.)*

**(b)** For $A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ (nilpotent: $A^2 = 0$), compute $e^{At}$ exactly by truncating the series.

**(c)** If $A$ is diagonalizable with $A = PDP^{-1}$, show that $e^{At} = P\,e^{Dt}\,P^{-1}$. What is $e^{Dt}$ when $D = \text{diag}(\lambda_1, \lambda_2)$?

**(d)** For the matrix $A = \begin{bmatrix} -1 & 4 \\ -1 & 3 \end{bmatrix}$ from Q12, use the eigendecomposition to write $e^{At}$ in terms of the eigenvectors and eigenvalues. Verify that $\mathbf{x}(t) = e^{At}\,\mathbf{x}(0)$ matches your solution from Q12.

---

## Q15 (6 pts) — Synthesis: ODEs and Machine Learning

**(a)** A ResNet computes $\mathbf{x}_{l+1} = \mathbf{x}_l + f_\theta(\mathbf{x}_l)$, where $l$ is the layer index. Explain in 2–3 sentences why this is Euler's method applied to the ODE $\frac{d\mathbf{x}}{dt} = f_\theta(\mathbf{x})$, and what the "step size" $h$ equals in this analogy.

**(b)** The gradient flow ODE for training is $\frac{dW}{dt} = -\nabla L(W)$. The loss $L(W)$ is a Lyapunov function for this system. State the key property that makes $L$ a Lyapunov function (compute $\frac{dL}{dt}$ along trajectories and show it is non-positive).

**(c)** Fill in the table connecting ODE concepts to ML concepts:

| ODE Concept | ML Analog |
|---|---|
| Euler's method with step size $h$ | ___ |
| Fixed points of $\frac{dy}{dt} = f(y)$ | ___ |
| Eigenvalues of the Jacobian at a fixed point | ___ |
| Stable node (all eigenvalues negative) | ___ |
| Saddle point (mixed-sign eigenvalues) | ___ |
| Resonance (driving frequency matches natural frequency) | ___ |

---

## Optional Mini-Project (~45 minutes): ODE Phase Portrait Explorer

**Build an interactive phase portrait visualizer for 2D linear systems $\frac{d\mathbf{x}}{dt} = A\mathbf{x}$.**

1. Let the user input a $2 \times 2$ matrix $A$. Compute its eigenvalues and eigenvectors.
2. Simulate trajectories from 20+ initial conditions using Euler's method (or scipy's `solve_ivp`).
3. Plot all trajectories on a single phase portrait with arrows showing direction of flow.
4. Draw the eigenvectors as lines through the origin. Color them by stability (green for stable directions, red for unstable).
5. Automatically classify and display the phase portrait type (stable node, unstable node, saddle, stable spiral, unstable spiral, center, degenerate node).
6. Test your visualizer on each case from Q13.

**Stretch:** Add a slider for a parameter in the matrix (e.g., $A = \begin{bmatrix} -1 & \mu \\ -\mu & -1 \end{bmatrix}$) and watch the phase portrait change as you slide through a bifurcation (the transition from spiral to other types as $\mu$ varies).

**Tools:** NumPy, Matplotlib, SciPy. No ML libraries needed.
