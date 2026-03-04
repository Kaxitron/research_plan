# Exam 2B: Multivariable Calculus

**The Path to AI Alignment -- Lessons 19-23 Comprehensive Assessment**

---

| | |
|---|---|
| **Time Allowed** | 90 minutes |
| **Total Points** | 150 |
| **Materials** | Pencil, paper, calculator (no CAS). No code. |
| **Format** | 15 questions mixing computation and conceptual depth |

> **Advice:** Show all work. Partial credit is generous for correct reasoning even with arithmetic errors. Geometric explanations are encouraged alongside algebraic work.

> *"The gradient tells you which way is up. The Hessian tells you the shape of the ground beneath your feet. Together they determine everything about how gradient descent behaves."*

---

## Q1 (10 pts) -- Partial Derivatives and the Gradient

Let f(x, y) = x^2 y - 3xy^3 + 2x - y.

**(a)** Compute the partial derivatives f_x and f_y.

**(b)** Compute the second-order partial derivatives f_{xx}, f_{yy}, f_{xy}, and f_{yx}. Verify that f_{xy} = f_{yx} (Clairaut's theorem).

**(c)** Compute the gradient vector grad f at the point (1, -1). In what direction does f increase most steeply from this point?

**(d)** Find the rate of change of f at (1, -1) in the direction u = (3/5, 4/5). *(This is the directional derivative D_u f.)*

**(e)** In what direction from (1, -1) is the rate of change of f equal to zero? What geometric object does this direction define on the contour map?

---

## Q2 (10 pts) -- Tangent Planes and Linear Approximation

Consider the surface z = f(x, y) = e^(x^2 + y).

**(a)** Find the equation of the tangent plane to this surface at the point (0, 0, 1).

**(b)** Use the tangent plane (linear approximation) to estimate f(0.1, -0.1). Compare with the exact value.

**(c)** The linear approximation is f(x) ~ f(a) + grad f(a) . (x - a). State the condition under which this approximation is "good." What quantity measures how badly the linear approximation fails?

**(d)** In neural network training, each gradient descent step implicitly trusts a linear approximation of the loss. The learning rate controls how far you step within this trusted region. Explain in 2-3 sentences why a learning rate that is too large causes divergence, using the language of linear approximation quality.

---

## Q3 (12 pts) -- The Multivariable Chain Rule and Backpropagation

Consider the computation graph:
```
x, y -> z = x^2 + xy -> w = sin(z) -> L = w^2
```

**(a)** Compute the forward pass: if x = 1, y = 2, find z, w, and L.

**(b)** Compute dL/dw, dw/dz, dz/dx, and dz/dy individually (the "local gradients" at each node).

**(c)** Using the chain rule, compute dL/dx and dL/dy by tracing backward through the graph.

**(d)** Verify dL/dx by computing it directly as d/dx[(sin(x^2 + xy))^2] evaluated at x = 1, y = 2.

**(e)** In a deep network with 100 layers, the chain rule produces a product of 100 Jacobian matrices. Explain in 2-3 sentences why this product can cause gradients to either vanish or explode, and name one architectural technique designed to mitigate this. *(Connect to eigenvalues of the Jacobians.)*

---

## Q4 (10 pts) -- The Jacobian Matrix

**(a)** For the function F(x, y) = (x^2 - y, xy + 1), compute the Jacobian matrix J.

**(b)** Evaluate J at the point (1, 2). What are the dimensions of J? What does each column represent? What does each row represent?

**(c)** The Jacobian is the best linear approximation to F near a point: F(a + h) ~ F(a) + J(a) h. Use this to approximate F(1.01, 2.03). Compare with the exact value.

**(d)** For two composed functions F: R^2 -> R^2 and G: R^2 -> R^2, the chain rule states J_{F o G} = J_F * J_G. This is a matrix multiplication. Explain in 2-3 sentences why backpropagation through a neural network is fundamentally a sequence of Jacobian-times-vector multiplications, and why this is more efficient than computing full Jacobians.

---

## Q5 (10 pts) -- The Hessian Matrix and Curvature

Consider f(x, y) = x^3 - 3xy + y^3.

**(a)** Compute the gradient grad f and find all critical points (where grad f = 0).

**(b)** Compute the Hessian matrix H(x, y).

**(c)** Evaluate H at each critical point. Compute the eigenvalues of H at each critical point. Classify each as a local minimum, local maximum, or saddle point.

**(d)** At the saddle point, find the eigenvectors of H. These are the directions along which the curvature is purely positive and purely negative. Describe what the surface looks like near this point.

**(e)** The condition number kappa = |lambda_max / lambda_min| of the Hessian measures how elongated the loss landscape is. If a Hessian has eigenvalues 100 and 0.01, compute kappa and explain in 1-2 sentences what this means for gradient descent convergence. What optimizer feature addresses this?

---

## Q6 (10 pts) -- Double Integrals and Fubini's Theorem

**(a)** Compute integral_0^1 integral_0^x (x + y) dy dx. Show the inner integral first, then the outer.

**(b)** Reverse the order of integration in part (a): rewrite the integral as integral integral (x + y) dx dy with the correct new limits. Verify you get the same answer.

**(c)** Compute integral integral_D (x^2 + y^2) dA where D is the disk x^2 + y^2 <= 4, by converting to polar coordinates. State the Jacobian factor and the new limits.

**(d)** In probability, the joint density p(x, y) integrates to 1 over all of R^2. If p(x, y) = Ce^(-(x^2 + y^2)/2) for some constant C, use polar coordinates and the Gaussian integral (integral_0^infinity r e^(-r^2/2) dr = 1) to find C. What famous distribution is this?

---

## Q7 (10 pts) -- Change of Variables and the Jacobian Determinant

**(a)** For the polar coordinate transformation x = r cos(theta), y = r sin(theta), compute the Jacobian matrix of the transformation and its determinant. Explain why the area element becomes dA = r dr d(theta).

**(b)** State the general change of variables formula for double integrals: integral integral f(x,y) dA = ? in terms of new variables (u, v) and the Jacobian determinant.

**(c)** If X is a random variable with density p_X(x) and Y = g(X) where g is invertible, then the density of Y is p_Y(y) = p_X(g^(-1)(y)) |d(g^(-1))/dy|. This is the change of variables formula for probability densities. If X ~ N(0, 1) and Y = 2X + 3, derive the density of Y.

**(d)** Normalizing flows are generative models that transform a simple distribution z ~ N(0, I) through a chain of invertible functions to produce complex data x = f_K o ... o f_1(z). The log-density of x involves the sum of log|det(J_{f_k})|. Explain in 2-3 sentences why the Jacobian determinant is needed and what it measures about how each transformation stretches or compresses probability density.

---

## Q8 (10 pts) -- The Gaussian Integral and Its Multivariate Generalization

**(a)** The Gaussian integral states that integral_{-infinity}^{infinity} e^(-x^2) dx = sqrt(pi). Outline the key steps of the polar coordinates proof: square the integral, convert to a double integral, switch to polar coordinates, and evaluate. *(You may sketch the steps rather than compute every detail.)*

**(b)** The general univariate Gaussian integral is integral_{-infinity}^{infinity} e^(-ax^2) dx = sqrt(pi/a) for a > 0. Use a substitution u = sqrt(a) x to derive this from part (a).

**(c)** The multivariate Gaussian density in R^d is p(x) = (2pi)^(-d/2) |det(Sigma)|^(-1/2) exp(-1/2 (x - mu)^T Sigma^(-1) (x - mu)). The normalization constant involves |det(Sigma)|^(-1/2). Explain in 2-3 sentences why the determinant of the covariance matrix appears, using the Jacobian determinant and the change of variables from a standard normal z ~ N(0, I) to x = Sigma^(1/2) z + mu.

**(d)** In variational autoencoders (VAEs), the encoder outputs mu and Sigma (or just the diagonal) and the KL divergence between two Gaussians appears in the loss. Why is the Gaussian distribution so ubiquitous in ML? Give two reasons, one from probability theory (a theorem) and one from computational convenience.

---

## Q9 (10 pts) -- Multivariate Taylor Expansion

**(a)** Write the second-order Taylor expansion of f(w) around a point w_0 in vector form:

f(w) ~ f(w_0) + ___^T (w - w_0) + 1/2 (w - w_0)^T ___ (w - w_0)

Fill in the two blanks.

**(b)** At a critical point where grad f(w_0) = 0, the expansion simplifies. Write the simplified form. Explain why "near a critical point, the loss landscape IS a quadratic form determined by the Hessian."

**(c)** Newton's method uses the second-order Taylor expansion to find the minimum of the local quadratic. Derive the Newton update step: w_{new} = w_0 - H^(-1) grad f(w_0). *(Hint: minimize the quadratic approximation by setting its gradient to zero.)*

**(d)** For a loss function with Hessian eigenvalues {100, 50, 1, 0.5, 0.01}, Newton's method takes equally-sized steps in all eigendirections (because it divides by the eigenvalue). Gradient descent, by contrast, takes steps proportional to the eigenvalue. Explain in 2-3 sentences why Newton's method converges faster, and why it is impractical for a neural network with 10 million parameters.

---

## Q10 (10 pts) -- The Implicit Function Theorem

**(a)** Consider the equation F(x, y) = x^2 + y^2 - 1 = 0 (the unit circle). At the point (sqrt(2)/2, sqrt(2)/2), use the IFT to compute dy/dx without solving for y explicitly. Recall: dy/dx = -(F_x / F_y).

**(b)** At which points on the unit circle does the IFT fail to express y as a function of x? What happens geometrically at those points?

**(c)** Consider F(w, lambda) = w^3 - lambda w = 0, where w is a model parameter and lambda is a hyperparameter. At (w, lambda) = (1, 1), verify F = 0. Compute dw/d(lambda) using the IFT. Interpret: if you increase lambda slightly, how does the optimal w change?

**(d)** At (w, lambda) = (0, 0), verify that the IFT fails (check the condition). Explain in 2-3 sentences what this means: near this point, smooth changes in the hyperparameter lambda can cause discontinuous changes in the optimal parameter w. How does this relate to phase transitions in neural network training?

---

## Q11 (10 pts) -- Critical Points and the Second Derivative Test

**(a)** Find all critical points of f(x, y) = x^2 + y^2 - 2x - 4y + 8. Classify each using the Hessian.

**(b)** Find all critical points of g(x, y) = x^2 - y^2 + 4x - 6y. Classify each using the Hessian.

**(c)** Find all critical points of h(x, y) = x^4 + y^4 - 4xy + 1. *(Hint: set h_x = 4x^3 - 4y = 0 and h_y = 4y^3 - 4x = 0, then substitute.)* Classify each.

**(d)** In high-dimensional loss landscapes (d >> 1), a critical point is a saddle point if even one Hessian eigenvalue is negative. If each eigenvalue is equally likely to be positive or negative, what fraction of critical points are local minima in dimension d = 100? What does this imply about the relative abundance of saddle points vs. local minima in neural network loss landscapes?

---

## Q12 (10 pts) -- Lagrange Multipliers

Minimize f(x, y) = x^2 + 2y^2 subject to the constraint g(x, y) = x + y - 3 = 0.

**(a)** Write the Lagrangian L(x, y, lambda) = f(x, y) - lambda g(x, y).

**(b)** Solve the system of equations: partial L/partial x = 0, partial L/partial y = 0, g(x, y) = 0. Find x*, y*, and lambda*.

**(c)** Verify that at the optimum, grad f is parallel to grad g. Compute both and check.

**(d)** Interpret lambda*: if the constraint is relaxed to x + y = 3 + epsilon, by approximately how much does the optimal value of f change?

**(e)** In ML, L2 regularization adds a penalty lambda ||w||^2 to the loss. This is equivalent to minimizing the original loss subject to ||w||^2 <= C for some constraint C. The regularization strength lambda is a Lagrange multiplier. Explain in 2-3 sentences why increasing lambda leads to smaller weights, and why this helps prevent overfitting. *(Use the constrained optimization perspective.)*

---

## Q13 (10 pts) -- KKT Conditions and Inequality Constraints

Minimize f(x, y) = (x - 3)^2 + (y - 3)^2 subject to x + y <= 4 and x >= 0, y >= 0.

**(a)** Without any constraints, what is the unconstrained minimum? Does it satisfy all constraints?

**(b)** Since the unconstrained minimum violates x + y <= 4, the constraint must be active at the optimum. Treat x + y = 4 as an equality constraint and use Lagrange multipliers to find the constrained minimum. Verify that x >= 0 and y >= 0 are satisfied.

**(c)** State the complementary slackness condition of KKT: for each inequality constraint g_i(x) <= 0, what must be true about lambda_i and g_i(x*)?

**(d)** In support vector machines (SVMs), the KKT conditions determine which data points are "support vectors." A support vector is a point where the margin constraint is active (complementary slackness: lambda_i > 0 implies g_i = 0). Explain in 2-3 sentences why only a small fraction of training points typically end up as support vectors, and why this makes SVMs memory-efficient at prediction time.

---

## Q14 (8 pts) -- Regularization as Constrained Optimization

**(a)** Consider minimizing L(w) = (y - Xw)^T (y - Xw) subject to ||w||^2 <= C (this is ridge regression). Write the Lagrangian. Show that the optimal w satisfies (X^T X + lambda I) w = X^T y, where lambda is the Lagrange multiplier.

**(b)** The matrix X^T X may be singular (non-invertible) when the data is rank-deficient. Why does adding lambda I guarantee that (X^T X + lambda I) is invertible for lambda > 0? *(Hint: what does adding lambda I do to the eigenvalues of X^T X?)*

**(c)** L1 regularization (||w||_1 <= C) tends to produce sparse solutions (many w_i = 0), while L2 regularization (||w||_2^2 <= C) tends to produce small but non-zero weights. Give a geometric explanation using the shapes of the L1 and L2 constraint regions and how they intersect with the elliptical contours of the loss.

**(d)** In alignment research, regularization is sometimes analogized to "constraining" a model's behavior. Explain in 1-2 sentences how the Lagrange multiplier lambda represents the "price" of the constraint, and what it means for the price to be high vs. low.

---

## Q15 (10 pts) -- Synthesis: Multivariable Calculus as the Language of Optimization

**(a)** Gradient descent on a loss L(w) for w in R^d uses the update w_{t+1} = w_t - eta * grad L(w_t). Name the concept from this exam that each element relies on:

| Element | Concept |
|---------|---------|
| grad L(w_t) | ___ (from which lesson?) |
| The direction -grad L | ___ (why this direction?) |
| Choosing the step size eta | ___ (what determines the safe range?) |
| Classifying the convergence point | ___ (what tool?) |
| Adding a constraint ||w|| <= C | ___ (what method?) |

**(b)** A neural network computes f = f_K o f_{K-1} o ... o f_1. The Jacobian of the full network is J = J_K * J_{K-1} * ... * J_1. State one consequence if all the Jacobians have largest singular value > 1. State one consequence if they all have largest singular value < 1.

**(c)** The multivariate Gaussian normalization, the change of variables formula, and the Jacobian determinant all appear when computing the likelihood in normalizing flows. Trace the connections: start with z ~ N(0, I), apply x = f(z), and write the log-density of x. Identify where each of these three concepts appears.

**(d)** Complete this conceptual chain by filling in each arrow with the mathematical tool that connects them:

```
Loss function L(w)
    --[___]--> Direction to step
    --[___]--> Shape of landscape at critical point
    --[___]--> Optimal point under constraints
    --[___]--> Sensitivity of optimum to constraint changes
```

---

## Optional Mini-Project (~45 minutes): Gradient Descent on a Constrained Loss Landscape

**Build a visualizer that compares unconstrained and constrained optimization on a 2D loss surface.**

1. Define a 2D loss surface L(w_1, w_2) = (w_1 - 2)^2 + 5(w_2 - 1)^2 (an elongated bowl).
2. Implement vanilla gradient descent and plot the trajectory on a contour plot. Observe the zigzag behavior caused by the condition number (kappa = 10).
3. Add an L2 constraint ||w||^2 <= R^2 for various values of R. Use projected gradient descent: after each gradient step, project back onto the constraint region. Plot the constrained trajectories for R = 1, 2, 3, 5.
4. Implement the Lagrange multiplier approach: for each R, solve the KKT conditions analytically and mark the constrained optimum on the plot.
5. Plot the optimal loss value as a function of R. Verify that the slope of this curve at each R matches the Lagrange multiplier lambda*.

**Stretch:** Replace L2 with L1 constraint (||w||_1 <= R) and observe that the constrained optimum tends to sit on a corner of the diamond-shaped constraint region (producing sparse solutions). Compare with the L2 case visually.

**Tools:** NumPy, Matplotlib. No ML libraries needed.
