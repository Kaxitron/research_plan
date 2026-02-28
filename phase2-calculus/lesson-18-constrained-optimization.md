# Lesson 18: Constrained Optimization and Lagrange Multipliers

[← Optimization](lesson-17-optimization.md) | [Back to TOC](../README.md) | [Next: Loss Landscapes →](lesson-19-loss-landscapes.md)

---

> **Why this lesson exists:** Real-world optimization almost always has constraints. You don't just minimize loss — you minimize loss *subject to* a privacy budget, a compute limit, a safety requirement, a fairness criterion. Alignment IS constrained optimization: maximize capability subject to safety. Lagrange multipliers are the mathematical tool that turns constrained problems into unconstrained ones, and they underpin SVMs, KKT conditions, regularization theory, and the duality that connects many alignment frameworks.

## 🎯 Core Concepts

### Why Constraints Matter

- **Unconstrained optimization** (Lesson 16): find the lowest point on the entire landscape. Gradient descent walks downhill freely.
- **Constrained optimization**: find the lowest point *that satisfies some condition*. The optimum is usually NOT at the bottom of the landscape — it's on the boundary of the allowed region.
- **Visual example in 2D:** minimize f(x,y) = x² + y² (a bowl) subject to x + y = 1 (a line). The unconstrained minimum is (0,0), but that violates the constraint. The constrained minimum is (0.5, 0.5) — the closest point on the line to the origin.

### Lagrange Multipliers — The Core Idea

- **The geometric insight:** at the constrained optimum, the gradient of f is *parallel* to the gradient of the constraint. If they pointed in different directions, you could slide along the constraint and improve f.
- **Formally:** minimize f(x) subject to g(x) = 0. At the optimum: ∇f = λ∇g, where λ is the **Lagrange multiplier.**
- **The Lagrangian:** L(x, λ) = f(x) - λg(x). Finding a stationary point of L (∂L/∂x = 0 and ∂L/∂λ = 0) simultaneously gives the optimum AND enforces the constraint.
- **What λ means:** it measures how much the constraint "costs" you. If λ is large, relaxing the constraint slightly would improve your objective a lot. If λ ≈ 0, the constraint isn't binding — the unconstrained optimum already nearly satisfies it.

### Visual Walkthrough

Imagine a topographic map (contour lines of f) with a trail drawn on it (the constraint g(x) = 0):

1. Walk along the trail. At most points, the trail crosses contour lines at an angle — you're going uphill or downhill.
2. The constrained optimum is where the trail becomes **tangent** to a contour line — you can't go any lower without leaving the trail.
3. Tangent = gradients parallel = ∇f = λ∇g. That's the whole idea.

### Multiple Constraints

- With k constraints g₁(x) = 0, ..., gₖ(x) = 0: ∇f = λ₁∇g₁ + ... + λₖ∇gₖ
- The Lagrangian becomes: L(x, λ₁, ..., λₖ) = f(x) - Σ λᵢgᵢ(x)
- Each λᵢ measures the "price" of the corresponding constraint.

### Inequality Constraints and KKT Conditions

- **Equality constraints** (g(x) = 0): the solution must be ON the boundary.
- **Inequality constraints** (g(x) ≤ 0): the solution can be in the interior OR on the boundary.
- **Karush-Kuhn-Tucker (KKT) conditions** extend Lagrange multipliers to handle inequality constraints:
  1. ∇f = Σ λᵢ∇gᵢ (stationarity)
  2. gᵢ(x) ≤ 0 for all i (primal feasibility)
  3. λᵢ ≥ 0 for all i (dual feasibility)
  4. λᵢgᵢ(x) = 0 for all i (**complementary slackness** — either the constraint is active, or its multiplier is zero)
- Complementary slackness is the key insight: constraints that don't matter at the optimum get λ = 0. Only the "active" constraints (the ones that are tight) influence the solution.

### Convex Optimization

- **Convex function:** a function where the line segment between any two points lies above the function. The bowl f(x) = x² is convex. f(x) = sin(x) is not.
- **Convex set:** a set where the line between any two points in the set stays in the set. A disk is convex. A crescent is not.
- **Why convexity matters:** for convex problems (convex objective, convex constraint set), every local minimum is a global minimum. There are no "traps." This is when optimization is *easy*.
- **Neural network loss is NOT convex** — it has many local minima and saddle points (Lesson 18). This is why neural network training is fundamentally harder than convex optimization. But understanding convexity tells you when you CAN get guarantees.
- **Regularization as soft constraint:** L2 regularization (minimize L(w) + λ||w||²) is equivalent to minimizing L(w) subject to ||w||² ≤ C for some C. The regularization parameter λ IS a Lagrange multiplier! This directly connects regularization (engineering) to constrained optimization (math).

### Duality

- **Primal problem:** minimize f(x) subject to constraints (what we want to solve).
- **Dual problem:** maximize a lower bound on f by optimizing over the Lagrange multipliers λ.
- **Weak duality:** the dual optimal value ≤ primal optimal value (always true).
- **Strong duality:** dual optimal = primal optimal (holds for convex problems under mild conditions — Slater's condition).
- **Why duality matters:** sometimes the dual is easier to solve. SVMs are derived by solving the dual. The dual reveals structure (which constraints matter, which don't).

## 📺 Watch — Primary

1. **Khan Academy — "Lagrange multipliers, introduction"**
   - https://www.khanacademy.org/math/multivariable-calculus/applications-of-multivariable-derivatives/constrained-optimization/v/constrained-optimization-introduction
   - *Clear 2D visual walkthrough of the tangent condition.*
2. **3Blue1Brown — "Lagrange Multipliers | Multivariable Calculus"** (if available in Essence of Calculus)
   - Excellent visual of contour lines becoming tangent to the constraint

## 📺 Watch — Secondary

3. **MIT OCW 18.02 — "Lagrange Multipliers"**
   - https://www.youtube.com/results?search_query=MIT+OCW+18.02+lagrange+multipliers
4. **Steve Brunton — "Constrained Optimization: Lagrange Multipliers"**
   - Applied perspective connecting to data science
5. **StatQuest — "Regularization Part 1: Ridge (L2) Regression"**
   - https://www.youtube.com/watch?v=Q81RR3Y5oRM
   - *Shows the constraint interpretation of regularization — the "constrained region" visual*

## 📖 Read — Primary

- **MML Book, Chapter 7.2** (Constrained Optimization and Lagrange Multipliers)
  - https://mml-book.github.io/
  - *Concise treatment with good examples. Read sections 7.2.1 through 7.2.3.*
- **MML Book, Chapter 7.3** (Convex Optimization)
  - *Skim for the key definitions and the fact that convex = tractable.*

## 📖 Read — Secondary

- **Stanford CS229 — "Convex Optimization Overview"**
  - https://cs229.stanford.edu/section/cs229-cvxopt.pdf
  - *2-page summary of everything you need for ML applications.*
- **Boyd & Vandenberghe — "Convex Optimization," Chapter 5** (duality)
  - https://web.stanford.edu/~boyd/cvxbook/
  - *The definitive reference. Chapter 5 on duality is beautiful. Free PDF.*

## 🔨 Do

- **Lagrange multiplier by hand:** Minimize f(x,y) = x² + y² subject to x + y = 1. Set up the Lagrangian L = x² + y² - λ(x + y - 1). Take partial derivatives, solve. Verify the solution (0.5, 0.5) geometrically — it's the closest point on the line to the origin.
- **Visualize the tangent condition:** Plot contour lines of f(x,y) = x² + 4y² and the constraint circle x² + y² = 1. Find where they're tangent. See that ∇f and ∇g are parallel at those points.
- **Regularization as constraint:** Train a linear model with varying L2 regularization strengths. For each λ, compute the norm of the weights ||w||². Plot λ vs ||w||². See that larger λ → smaller ||w||² — you're tightening the constraint.
- **Key exercise:** You're designing an alignment objective. The AI should maximize helpfulness H(θ) subject to harmlessness score S(θ) ≥ threshold. Write this as a constrained optimization problem. Set up the Lagrangian. What does λ represent? (The "price" of safety — how much helpfulness you sacrifice per unit of harmlessness.) What happens when λ → 0? When λ → ∞?

## 🔗 ML Connection

- **L2 regularization = constrained optimization:** minimizing loss + λ||w||² is equivalent to minimizing loss subject to ||w||² ≤ C. The regularization strength λ IS the Lagrange multiplier. This unifies the "engineering trick" of weight decay with the formal math of constraints.
- **SVMs are entirely built on Lagrange multipliers:** the maximum-margin hyperplane comes from a constrained optimization problem. The dual reveals which data points are "support vectors" (the ones with non-zero λ).
- **KKT conditions appear in**: LASSO (L1 regularization), constrained policy optimization in RL, and safety-constrained training objectives.

## 🧠 Alignment Connection

**Alignment IS constrained optimization.** Almost every alignment technique can be framed this way:

- **RLHF:** maximize reward subject to KL divergence from base model ≤ budget. The KL penalty weight β is a Lagrange multiplier.
- **Constitutional AI:** maximize helpfulness subject to constitutional principles being satisfied.
- **Safety training:** maximize capability subject to harmlessness constraints.
- **Corrigibility:** optimize for the objective subject to remaining shutdownable — a constraint on the agent's own behavior.

Understanding Lagrange multipliers gives you the vocabulary for the central tradeoff in alignment: **the alignment tax** — how much capability do you sacrifice for each unit of safety? That tradeoff IS λ.

---

## 📎 Appendix: Support Vector Machines — Constrained Optimization in Action

> This section covers SVMs as the canonical *application* of everything above. It's optional but demonstrates that Lagrange multipliers aren't abstract — they're the mathematical engine behind a major ML algorithm.

### SVMs — Maximum Margin Classification

- **The idea:** given two classes of data that can be separated by a hyperplane, find the hyperplane with the *maximum margin* — the widest gap between the classes. Wider margin → more robust to noise.
- **The math:** minimize ||w||² (keep the weight vector small → wide margin) subject to yᵢ(wᵀxᵢ + b) ≥ 1 for all data points (all points correctly classified with at least margin 1). This is EXACTLY a constrained optimization problem.
- **The Lagrangian:** L = ½||w||² - Σᵢ αᵢ[yᵢ(wᵀxᵢ + b) - 1] where αᵢ ≥ 0 are Lagrange multipliers.
- **KKT conditions tell you:** most αᵢ = 0 (most data points don't matter for the decision boundary). The points with αᵢ > 0 are the **support vectors** — the critical data points closest to the boundary. The entire model depends only on these few points.
- **The dual problem** (solving for αᵢ instead of w) reveals: the solution only depends on **dot products** xᵢᵀxⱼ between data points. This opens the door to the kernel trick.

### The Kernel Trick — Implicit High-Dimensional Mapping

- **The problem:** some data isn't linearly separable in its original space (imagine two concentric circles — no line separates them).
- **The solution:** map data to a higher-dimensional space where it IS separable. Two concentric circles in 2D become separable by a plane in 3D if you add a feature z = x² + y².
- **The kernel trick:** you never actually compute the high-dimensional mapping! Since SVMs only use dot products, you replace every dot product xᵢᵀxⱼ with a kernel function K(xᵢ, xⱼ) that *implicitly* computes the dot product in the high-dimensional space.
- **Common kernels:**
  - **Linear:** K(x,y) = xᵀy (no mapping, just standard dot product)
  - **Polynomial:** K(x,y) = (xᵀy + c)^d (implicitly maps to space of all degree-d polynomial features)
  - **RBF/Gaussian:** K(x,y) = exp(-||x-y||²/2σ²) (implicitly maps to *infinite*-dimensional space!)
- **Why the kernel trick matters for alignment thinking:** it demonstrates that the right *representation* can make hard problems easy. This is exactly what neural network layers do — they learn to transform data into a space where the task becomes (nearly) linear. Understanding kernels gives you the vocabulary to talk about representation learning.
- **MML Book, Chapter 12** covers SVMs from the primal formulation through duality to kernels.

### 📺 SVM Videos

- **StatQuest — "Support Vector Machines, Main Ideas"**
  - https://www.youtube.com/watch?v=efR1C6CvhmE
  - *Clear visual explanation of maximum margin and support vectors.*
- **StatQuest — "The Polynomial Kernel" and "The RBF Kernel"**
  - Parts 2 and 3 of the SVM series. Shows how kernels transform data.

### 📖 SVM Reading

- **MML Book, Chapter 12.1–12.4** (separating hyperplanes → primal → dual → kernels)
