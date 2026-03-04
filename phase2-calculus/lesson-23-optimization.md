# Lesson 23: Optimization in Several Variables and Lagrange Multipliers

[<- Previous](lesson-22-taylor-expansions.md) | [Back to TOC](../README.md) | [Next: Line Integrals ->](lesson-24-line-integrals.md)

---

## Core Learning

- Finding minima and maxima of multivariable functions starts with setting the gradient to zero to find critical points. But not all critical points are minima -- you need the second derivative test via the Hessian to classify them. A positive definite Hessian (all eigenvalues positive) means local minimum; negative definite means local maximum; mixed eigenvalues mean saddle point. In high-dimensional neural network loss landscapes, saddle points vastly outnumber local minima, which is why understanding the Hessian spectrum matters for ML.
- Lagrange multipliers solve constrained optimization: minimize f(x) subject to g(x) = 0. The key geometric insight is that at the optimum, the gradient of f must be parallel to the gradient of g -- otherwise you could move along the constraint surface and still decrease f. This gives the Lagrangian condition nabla f = lambda * nabla g, where lambda (the Lagrange multiplier) is the "shadow price" of the constraint. Multiple constraints require one multiplier per constraint.
- KKT (Karush-Kuhn-Tucker) conditions extend Lagrange multipliers to inequality constraints g(x) <= 0. The crucial new feature is complementary slackness: either the constraint is active (g = 0 and lambda > 0) or it is inactive (g < 0 and lambda = 0). Duality theory provides an alternative formulation of the optimization problem that is sometimes easier to solve. The deep connection to ML is that L2 regularization (adding lambda * ||w||^2 to the loss) is exactly equivalent to constraining ||w||^2 <= C for some C determined by lambda -- Lagrange multipliers make this equivalence precise.

## Watch -- Primary

- **Trefor Bazett -- Multivariable Calculus** (optimization and Lagrange multiplier sections)
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxc_CvEy7xBKRQr6I214QJcd
  - Focus on critical point classification, second derivative test, and the Lagrange multiplier videos.

## Watch -- Secondary

- **Khan Academy -- "Lagrange multipliers"**
  - https://www.khanacademy.org/math/multivariable-calculus/applications-of-multivariable-derivatives/constrained-optimization/a/lagrange-multipliers-single-constraint
  - Step-by-step visual walkthrough with worked examples.
- **Steve Brunton -- "Constrained Optimization" (Data-Driven Science)**
  - https://www.youtube.com/c/Eigensteve
  - Connects constrained optimization to engineering and ML applications.

## Read

- **Stewart's Calculus** -- Sections on local extrema, second derivative test, and Lagrange multipliers (typically Chapter 14).
- **Boyd and Vandenberghe -- "Convex Optimization"** -- Chapter 5 on duality. Available free at https://web.stanford.edu/~boyd/cvxbook/. This is the standard reference for KKT conditions and duality in optimization.
- **MML Book (Deisenroth, Faisal, Ong)** -- Section 7.2 on constrained optimization and Lagrange multipliers.

## Key Equations

Critical points (necessary condition for extremum):

$$\nabla f = \mathbf{0}$$

Second derivative test via Hessian:
- H positive definite (all eigenvalues > 0) implies local minimum
- H negative definite (all eigenvalues < 0) implies local maximum
- H indefinite (mixed eigenvalues) implies saddle point

Lagrange multiplier condition (single equality constraint g(x) = 0):

$$\nabla f = \lambda \nabla g$$

The Lagrangian:

$$\mathcal{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) - \lambda \, g(\mathbf{x})$$

KKT conditions (inequality constraints g_i(x) <= 0):

$$\nabla f = \sum_i \lambda_i \nabla g_i, \quad \lambda_i \geq 0, \quad \lambda_i g_i(\mathbf{x}) = 0 \text{ (complementary slackness)}$$

Regularization-constraint equivalence:

$$\min_{\mathbf{w}} L(\mathbf{w}) + \lambda \|\mathbf{w}\|^2 \quad \Longleftrightarrow \quad \min_{\mathbf{w}} L(\mathbf{w}) \text{ subject to } \|\mathbf{w}\|^2 \leq C$$

## Do

1. **Critical point classification.** For f(x, y) = x^4 + y^4 - 4xy + 1, find all critical points (set nabla f = 0 and solve). Compute the Hessian at each critical point and classify as minimum, maximum, or saddle using the eigenvalue test. Verify by plotting the surface.

2. **Lagrange multipliers by hand and code.** Maximize f(x, y) = xy subject to x^2 + y^2 = 1 (find the rectangle of maximum area inscribed in the unit circle). Solve analytically using nabla f = lambda * nabla g. Then solve numerically using scipy.optimize.minimize with a constraint. Verify the solutions match.

3. **Regularization = constraint.** Consider a simple linear regression problem: minimize ||Ax - b||^2. Solve it three ways: (a) unconstrained (normal equations), (b) with L2 regularization (ridge regression: minimize ||Ax - b||^2 + lambda * ||x||^2), and (c) with an explicit constraint ||x||^2 <= C using scipy.optimize.minimize with a constraint. Show that for each lambda, there exists a C such that solutions (b) and (c) are identical. Plot the solution norm ||x|| as a function of lambda and as a function of C.

```python
import numpy as np
from scipy.optimize import minimize

# Lagrange multipliers: maximize f(x,y) = xy on the unit circle
# Equivalent to minimizing -xy subject to x^2 + y^2 - 1 = 0

def objective(x):
    return -x[0] * x[1]

def constraint(x):
    return x[0]**2 + x[1]**2 - 1.0

from scipy.optimize import minimize

result = minimize(objective, x0=[0.5, 0.5],
                  constraints={'type': 'eq', 'fun': constraint})
print(f"Optimal point: ({result.x[0]:.4f}, {result.x[1]:.4f})")
print(f"Max xy = {-result.fun:.4f}")
print(f"Analytical: (1/sqrt(2), 1/sqrt(2)), max xy = 0.5")

# Regularization vs constraint equivalence
np.random.seed(42)
A = np.random.randn(20, 5)
b = np.random.randn(20)

# Ridge regression for various lambda
lambdas = np.logspace(-3, 3, 50)
norms_ridge = []
for lam in lambdas:
    x_ridge = np.linalg.solve(A.T @ A + lam * np.eye(5), A.T @ b)
    norms_ridge.append(np.linalg.norm(x_ridge)**2)

print(f"\nRidge: lambda=0.001 -> ||x||^2 = {norms_ridge[0]:.4f}")
print(f"Ridge: lambda=1000  -> ||x||^2 = {norms_ridge[-1]:.6f}")
```

## ML and Alignment Connection

ALL of neural network training is optimization: minimize a loss function over millions of parameters. The Hessian eigenvalue spectrum at a critical point tells you whether you have found a minimum (all positive -- good) or a saddle point (mixed signs -- common in high dimensions). Random matrix theory predicts that in a function of n variables, a random critical point has roughly half positive and half negative Hessian eigenvalues, so saddle points exponentially outnumber local minima as dimension increases. This explains why gradient descent in neural networks rarely gets trapped in bad local minima -- it gets stuck at saddle points instead, and momentum/noise help escape them.

Lagrange multipliers explain WHY regularization works. L2 regularization (weight decay) adds lambda * ||w||^2 to the loss. This is mathematically equivalent to optimizing the original loss subject to the constraint ||w||^2 <= C. The multiplier lambda IS the regularization strength. Larger lambda means tighter constraint means smaller weights means simpler model. This equivalence is not just theoretical -- it is the foundation of support vector machines, where the dual of a constrained optimization problem gives the kernel trick.

For alignment, constrained optimization is directly relevant: we want to maximize helpfulness SUBJECT TO safety constraints. The Lagrangian formulation suggests that safety constraints can be converted to penalty terms in the loss (and vice versa), but the KKT conditions reveal subtleties -- complementary slackness means some constraints may be "slack" (inactive) at the optimum, which has implications for how robustly safety constraints bind during training.
