# Exam 2A: Calculus — The Language of Optimization

**The Path to AI Alignment — Lessons 13–21 Comprehensive Assessment**

---

| | |
|---|---|
| **Time Allowed** | 90 minutes |
| **Total Points** | 150 |
| **Materials** | Pencil, paper, calculator (no CAS). No code. |
| **Format** | Part I: Calculus Fundamentals (8 questions, 70 pts) — Part II: ML Calculus (7 questions, 80 pts) |

> **Advice:** Show all work. Partial credit is generous for correct reasoning even with arithmetic errors. Geometric explanations are encouraged alongside algebraic work.

> *"Every smooth curve, if you zoom in far enough, looks like a straight line. Gradient descent exploits this — it follows straight-line approximations of a curved surface, one small step at a time."*

---

# Part I: Calculus Fundamentals (70 points)

*Rebuild confidence in the core toolkit. These are the mechanical foundations that everything in Part II rests on.*

---

## Question 1 (8 pts) — Differentiation Fluency

Differentiate each function. Show your work and name the rule(s) used.

**(a)** f(x) = 5x⁴ − 3x² + 7x − 2

**(b)** f(x) = x² · ln(x)

**(c)** f(x) = (3x² + 1)⁵

**(d)** f(x) = e^(sin(x))

---

## Question 2 (10 pts) — The Chain Rule Gauntlet

The chain rule is the single most important rule for ML. Differentiate each, clearly identifying the "outer" and "inner" functions at each step.

**(a)** f(x) = ln(x³ + e^x)

**(b)** f(x) = sin²(3x) — i.e., (sin(3x))²

**(c)** f(x) = e^(−x²/2) *(This is the core of the Gaussian/normal distribution.)*

**(d)** The sigmoid function: σ(x) = 1/(1 + e^(−x)). Derive σ'(x) from scratch and show that σ'(x) = σ(x)(1 − σ(x)).

**(e)** Using your result from (d): if L = −ln(σ(x)) (this is binary cross-entropy for the positive class), compute dL/dx and simplify fully. What happens to this gradient as σ(x) → 1 (model is confident and correct)? As σ(x) → 0 (model is confident and wrong)?

---

## Question 3 (8 pts) — Critical Points and the Second Derivative Test

**(a)** Find all critical points of f(x) = x³ − 6x² + 9x + 1. Classify each as a local minimum, local maximum, or neither using the second derivative test.

**(b)** Find the critical point of g(x) = xe^(−x) for x > 0. Classify it. *(This shape appears in attention score distributions.)*

**(c)** Explain geometrically what f''(x) > 0 means in terms of the curve's shape. Then explain what f''(x) = 0 means and why the second derivative test is inconclusive there.

---

## Question 4 (10 pts) — Integration

**(a)** Compute ∫(3x² + 2x − 1) dx.

**(b)** Compute ∫₀¹ e^(2x) dx. *(Hint: u-substitution or recognize the antiderivative.)*

**(c)** Compute ∫₁ᵉ (1/x) dx. What famous number appears?

**(d)** The probability that a continuous random variable X falls between a and b is P(a ≤ X ≤ b) = ∫ₐᵇ p(x) dx. If p(x) = 2x for 0 ≤ x ≤ 1 (and 0 elsewhere), verify that ∫₀¹ p(x) dx = 1. Then find P(0.5 ≤ X ≤ 1).

**(e)** State the Fundamental Theorem of Calculus (either part) in your own words. Why does it connect derivatives and integrals?

---

## Question 5 (8 pts) — Limits and L'Hôpital's Rule

**(a)** Compute lim(x→0) sin(x)/x. *(You may state the known result.)*

**(b)** Compute lim(x→0) (e^x − 1)/x using L'Hôpital's rule. Show why it's in 0/0 form first.

**(c)** Compute lim(x→∞) x·e^(−x). *(Hint: rewrite as x/e^x and apply L'Hôpital.)*

**(d)** Why does L'Hôpital's rule matter for ML? In one sentence, explain how indeterminate forms like 0/0 arise when analyzing loss functions near critical points or when parameters approach special values (like weights going to zero).

---

## Question 6 (8 pts) — Partial Derivatives

Let f(x, y) = x²y + 3xy² − 2x + y.

**(a)** Compute ∂f/∂x (treat y as a constant).

**(b)** Compute ∂f/∂y (treat x as a constant).

**(c)** Compute ∂²f/∂x∂y and ∂²f/∂y∂x. Verify they're equal. *(This is Clairaut's theorem — mixed partials commute for smooth functions.)*

**(d)** Evaluate ∇f at the point (1, 2). In which direction does f increase most rapidly from this point?

---

## Question 7 (10 pts) — Series and Convergence

**(a)** Write the Taylor series for e^x centered at x = 0 up to the x⁴ term.

**(b)** Use your answer to approximate e^(0.1). Compare with the true value e^(0.1) ≈ 1.10517.

**(c)** Write the Taylor series for 1/(1 − x) for |x| < 1. This is a geometric series — what is the general pattern?

**(d)** The Taylor series for ln(1 + x) around x = 0 is x − x²/2 + x³/3 − x⁴/4 + ···. For what values of x does this converge? Compute ln(1.1) using the first four terms.

**(e)** Why are Taylor series the key tool in theoretical ML? Answer in 2–3 sentences. *(Hint: what happens when a paper says "to second order" or "locally quadratic"?)*

---

## Question 8 (8 pts) — Integration Techniques

**(a)** Compute ∫ x·e^x dx using integration by parts. *(Recall: ∫ u dv = uv − ∫ v du.)*

**(b)** Compute ∫ 2x/(x² + 1) dx using substitution.

**(c)** The Gaussian integral ∫_{−∞}^{∞} e^(−x²) dx = √π is one of the most important integrals in all of mathematics. You cannot compute it with single-variable techniques alone. Explain in 1–2 sentences the trick that makes it computable. *(Hint: what happens when you square the integral and switch to polar coordinates?)*

**(d)** Why does this particular integral matter so much for probability and ML?

---

# Part II: ML-Specific Calculus (80 points)

*Now apply the fundamentals to the calculus of machine learning: gradients, Hessians, optimization, and the chain rule as backpropagation.*

---

## Question 9 (12 pts) — The Chain Rule IS Backpropagation

A simple computation graph computes the loss:

```
Input: x = 2, weight: w = 3, bias: b = -1, target: y = 4
z = wx + b
a = ReLU(z) = max(0, z)
L = (a - y)²
```

**(a)** Compute the forward pass: find z, a, and L.

**(b)** Compute all backward pass gradients by tracing the chain rule in reverse: ∂L/∂a, ∂L/∂z, ∂L/∂w, ∂L/∂b.

**(c)** Verify ∂L/∂w using the "full chain" expression: ∂L/∂w = (∂L/∂a)(∂a/∂z)(∂z/∂w).

**(d)** If the input were x = −5 (so z = wx + b = 3(−5) − 1 = −16), what would ∂L/∂w be? Why? What problem does this illustrate?

**(e)** Why is reverse-mode autodiff (backpropagation) more efficient than forward-mode for neural networks? Answer in terms of the number of parameters vs. the number of outputs.

---

## Question 10 (12 pts) — The Hessian and Loss Landscape Geometry

Consider the loss function L(w₁, w₂) = w₁² + 3w₂² − 2w₁w₂.

**(a)** Compute the gradient ∇L and find the critical point.

**(b)** Compute the Hessian matrix H.

**(c)** Find the eigenvalues of H. Classify the critical point.

**(d)** The condition number κ = λ_max/λ_min. Compute it. Explain in 2–3 sentences what a high condition number means for gradient descent and why it causes "zigzag" behavior.

**(e)** Write the second-order Taylor expansion of L(w) around the critical point w₀ (where ∇L = 0). Explain why this shows that "near a critical point, the loss landscape IS a quadratic form determined by the Hessian" — connecting directly to what you learned about quadratic forms in Phase 1.

---

## Question 11 (10 pts) — Constrained Optimization and Lagrange Multipliers

Minimize L(w₁, w₂) = w₁² + w₂² subject to the constraint w₁ + 2w₂ = 5.

**(a)** Write the Lagrangian ℒ(w₁, w₂, λ).

**(b)** Solve the system of equations ∂ℒ/∂w₁ = 0, ∂ℒ/∂w₂ = 0, ∂ℒ/∂λ = 0. Find w₁*, w₂*, and λ*.

**(c)** Interpret λ* geometrically: if the constraint were relaxed to w₁ + 2w₂ = 5 + ε, approximately how much would the optimal loss change?

**(d)** Explain in 2–3 sentences how constrained optimization relates to alignment. *(Think: "maximize capability subject to ___." What does λ represent in that context?)*

---

## Question 12 (12 pts) — Taylor Expansion, IFT, and Sensitivity

**(a)** Write the multivariate second-order Taylor expansion of f(w) around a critical point w₀ where ∇f(w₀) = 0. Identify the Hessian's role.

**(b)** A loss function near a minimum has Hessian eigenvalues λ₁ = 100 and λ₂ = 0.01. Describe the shape of the loss landscape near this minimum using a geometric picture. What is the condition number?

**(c)** Newton's method uses the Hessian to take smarter steps. Write the Newton update formula. Why does it fix the zigzag problem from Q10? Why don't we use it for neural networks with millions of parameters?

**(d)** Consider the equation F(w, λ) = w³ − λw = 0. At the point (w, λ) = (1, 1), verify F = 0, then use the IFT to compute dw/dλ. At (w, λ) = (0, 0), show that the IFT fails. What does this failure mean for the loss landscape?

---

## Question 13 (10 pts) — Integration, Jacobians, and Probability Transforms

**(a)** Compute ∫∫_R (x² + y²) dA where R is the unit disk x² + y² ≤ 1, using polar coordinates. State the Jacobian and why it's needed.

**(b)** State the change of variables formula for double integrals. Connect the Jacobian determinant to the determinant's geometric meaning from Phase 1 (Lesson 7).

**(c)** If X ~ N(0, 1) and Y = 3X + 2, derive the density of Y using the change of variables formula.

**(d)** Why does the multivariate Gaussian normalization constant (2π)^(d/2)|det(Σ)|^(1/2) involve the determinant of the covariance matrix? Answer in 1–2 sentences connecting to the Jacobian.

---

## Question 14 (12 pts) — The Bias-Variance Tradeoff and Loss Landscapes

**(a)** Write the bias-variance decomposition: Error = ___² + ___ + ___.

**(b)** A 2-parameter model fits a line to data generated by a true cubic function. Is the dominant error from bias or variance? Why?

**(c)** A 1000-parameter model fits the same 20 data points. Is the dominant error from bias or variance? Why?

**(d)** Modern neural networks with millions of parameters generalize well despite classical theory. Name this phenomenon and explain in 2–3 sentences how it challenges the classical bias-variance picture.

**(e)** Why are saddle points overwhelmingly more common than local minima in high-dimensional loss landscapes? Give a probabilistic argument based on Hessian eigenvalues.

**(f)** Cross-validation splits data into train/validation/test. Why do you need THREE separate sets, not just two?

---

## Question 15 (12 pts) — Synthesis: The Complete Optimization Pipeline

You are training a small neural network with loss L(W).

**(a)** Write the gradient descent update rule with momentum. Explain using a physical analogy why momentum helps navigate ravines.

**(b)** SGD uses mini-batches instead of the full dataset. Name one advantage of SGD over full-batch gradient descent that goes beyond just computational speed. *(Hint: what does the noise do?)*

**(c)** As training converges near a critical point, you compute the Hessian and find eigenvalues {5, 3, 0.01, −0.001}. Classify this critical point. What does the near-zero positive eigenvalue tell you? What does the small negative eigenvalue imply?

**(d)** Trace the complete conceptual path: starting from a loss function, name the mathematical tool from this phase that handles each step, and the Phase 1 concept it builds upon:

| Step | Calculus Tool (Phase 2) | Linear Algebra Foundation (Phase 1) |
|------|------------------------|--------------------------------------|
| Computing direction to step | ___ | ___ |
| Propagating through layers | ___ | ___ |
| Classifying critical points | ___ | ___ |
| Understanding local shape | ___ | ___ |
| Handling constraints | ___ | ___ |

**(e)** The Jacobian determinant from Lesson 20 and the Hessian determinant both appear in this phase. State one specific role each plays in ML.
