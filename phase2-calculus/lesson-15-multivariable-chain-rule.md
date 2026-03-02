# Lesson 15B: The Multivariable Chain Rule and Jacobian Matrices

[← Gradients](lesson-14-gradients.md) | [Back to TOC](../README.md) | [Next: Multiple Integration →](lesson-16-multiple-integration.md)

---

> **Why this lesson exists:** The single-variable chain rule says "multiply the derivatives." The multivariable chain rule says "multiply the *Jacobian matrices*." This is one of the most beautiful unifications in calculus — the derivative of a composition of vector-valued functions is the product of their Jacobian matrices. Every use of the chain rule in ML (backpropagation, normalizing flows, reparameterization) is a special case of this one general principle. We study it here as pure mathematics before seeing its applications.

## 🎯 Core Concepts

### From Single-Variable to Multi-Variable Composition

- **Single-variable review:** if y = f(g(x)), then dy/dx = f'(g(x)) · g'(x). The derivative of a composition is the product of derivatives, evaluated at the right points.
- **The question:** what if g: ℝⁿ → ℝᵐ and f: ℝᵐ → ℝᵖ? The composition f ∘ g maps ℝⁿ → ℝᵖ. What is its derivative?
- **The answer is matrix multiplication.** The derivative of g at a point x is the Jacobian matrix J_g(x), an m×n matrix. The derivative of f at the point g(x) is J_f(g(x)), a p×m matrix. The derivative of the composition is: J_{f∘g}(x) = J_f(g(x)) · J_g(x), a p×n matrix.
- **This is the multivariable chain rule.** It says: *the Jacobian of a composition is the product of the Jacobians.* The single-variable chain rule is the 1×1 special case.

### The Jacobian Matrix — The Total Derivative

- **Definition:** for a function f: ℝⁿ → ℝᵐ, the Jacobian at a point x is the m×n matrix of all partial derivatives: (J_f)ᵢⱼ = ∂fᵢ/∂xⱼ. Row i contains the gradient of the i-th output. Column j contains how all outputs change when you wiggle the j-th input.
- **The Jacobian IS the best linear approximation:** f(x + δ) ≈ f(x) + J_f(x) · δ. This is the multivariable version of f(x + h) ≈ f(x) + f'(x)h. The Jacobian plays the role of the derivative.
- **Special cases you already know:**
  - f: ℝⁿ → ℝ (scalar output): the Jacobian is a 1×n row vector — the gradient ∇f transposed.
  - f: ℝ → ℝⁿ (curve in space): the Jacobian is an n×1 column vector — the tangent vector.
  - f: ℝⁿ → ℝⁿ (same dimension): the Jacobian is a square matrix, and |det J| measures local volume scaling (this is why the Jacobian determinant appears in change of variables).
- **Geometric meaning:** the Jacobian at a point describes how the function locally stretches, rotates, and distorts space near that point. It IS a linear transformation — the best linear approximation to the function at that point. This connects directly to Lesson 4: every smooth function locally looks like a matrix.

### The Chain Rule in Multiple Dimensions

- **Theorem:** if g: ℝⁿ → ℝᵐ is differentiable at x and f: ℝᵐ → ℝᵖ is differentiable at g(x), then f ∘ g is differentiable at x and: J_{f∘g}(x) = J_f(g(x)) · J_g(x).
- **Dimensions check:** J_f is p×m, J_g is m×n, their product is p×n. ✓ The composition maps ℝⁿ → ℝᵖ, so its Jacobian should be p×n.
- **Why matrix multiplication?** Because composition of linear maps IS matrix multiplication (Lesson 5). The chain rule says "derivatives of compositions = compositions of derivatives," and composition of linear maps = matrix product.
- **Multiple compositions:** for h = f₃ ∘ f₂ ∘ f₁, the chain rule gives J_h = J_{f₃} · J_{f₂} · J_{f₁}. This is a product of matrices — one for each "link" in the chain. The more links, the longer the product.
- **Tree diagrams for complex dependencies:** when a variable z depends on x through multiple intermediate paths (say z depends on u and v, which both depend on x), the chain rule becomes: ∂z/∂x = (∂z/∂u)(∂u/∂x) + (∂z/∂v)(∂v/∂x). You sum over all paths from x to z. This "sum over paths" structure is the mathematical backbone of backpropagation, though we won't study that application until later.

### Implicit Differentiation — When You Can't Solve Explicitly

- **The setup:** given F(x, y) = 0, can you find dy/dx without solving for y?
- **Yes:** differentiate both sides with respect to x using the chain rule. F_x + F_y · (dy/dx) = 0, so dy/dx = −F_x/F_y (provided F_y ≠ 0).
- **Multivariable version:** given F(x, y) = 0 where x ∈ ℝⁿ and y ∈ ℝᵐ, the Jacobian of y with respect to x is: ∂y/∂x = −(∂F/∂y)⁻¹ · (∂F/∂x). This requires the m×m matrix ∂F/∂y to be invertible — which connects to the Implicit Function Theorem in Lesson 17.
- **Geometric meaning:** implicit differentiation finds the slope of a curve defined by a constraint, without parameterizing the curve. The constraint surface F = 0 is a manifold, and we're finding tangent directions on it.

### The Jacobian Determinant — Volume Scaling Revisited

- **For f: ℝⁿ → ℝⁿ** (square Jacobian), det(J_f) measures how f locally scales volumes near a point. This is the direct generalization of the determinant's geometric meaning from Lesson 7.
- **Sign matters:** positive determinant preserves orientation, negative reverses it (like a reflection).
- **Zero determinant:** the function locally collapses a dimension — it's not locally invertible at that point. This connects to rank: if rank(J) < n, some directions are destroyed.
- **Preview of change of variables (Lesson 16):** when you change coordinates in an integral, the factor |det J| corrects for the volume distortion. You'll see this in action soon.

## 📺 Watch — Primary

1. **3Blue1Brown — "Visualizing the chain rule and product rule" (Essence of Calculus, Ch. 4)**
   - https://www.youtube.com/watch?v=YG15m2VwSjA
   - *Single-variable visualization. Watch this first as a warmup before generalizing.*
2. **Khan Academy — "Multivariable chain rule and directional derivatives"**
   - https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/differentiating-vector-valued-functions/a/multivariable-chain-rule-simple-version
   - *Clear worked examples of the chain rule with multiple variables.*
3. **Trefor Bazett — "The Multivariable Chain Rule"**
   - https://www.youtube.com/watch?v=NO3AqAaAE6o
   - *Visual and careful treatment, exactly the right pace.*

## 📺 Watch — Secondary

4. **Khan Academy — "Jacobian" (full Jacobian series)**
   - https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/jacobian/v/jacobian-prerequisite-knowledge
   - *Multiple videos walking through the Jacobian matrix and its geometric meaning.*
5. **Trefor Bazett — "Jacobians and Change of Variables"**
   - *Connects the Jacobian determinant to area/volume scaling — bridges this lesson to Lesson 16.*

## 📖 Read — Primary

- **MML Book, Chapter 5.2–5.4** (gradients, chain rule, higher-order derivatives)
  - *The matrix formulation of the chain rule. Equation 5.48 is the key: J = J_f · J_g.*
- **Thomas' Calculus or Stewart's Calculus** — Chapter on the Multivariable Chain Rule
  - *Any standard Calc 3 textbook covers this. The worked examples are valuable.*

## 📖 Read — Secondary

- **"The Matrix Calculus You Need for Deep Learning" by Parr & Howard**
  - https://arxiv.org/abs/1802.01528
  - *Sections on Jacobians and the chain rule. Written for ML but the math is general. Save the ML applications for later — focus on the pure chain rule content.*

## 🔨 Do

- Compute the Jacobian of the polar-to-Cartesian transformation: (r, θ) → (r cos θ, r sin θ). Verify that |det J| = r. Draw a picture of a small rectangle in (r, θ) space and its distorted image in (x, y) space to see the area scaling.
- Given f(u, v) = (u², uv, v³) and g(x, y) = (x + y, xy), compute J_f, J_g, and their product J_{f∘g} both directly and by composing the Jacobians. Verify they match.
- Implement a function in Python that numerically estimates the Jacobian of any function f: ℝⁿ → ℝᵐ using finite differences, and verify your hand computations.
- **Implicit differentiation exercise:** for the curve x³ + y³ = 6xy, find dy/dx at the point (3, 3) using implicit differentiation. Plot the curve to see what's happening geometrically.
- For a composition of three functions ℝ² → ℝ³ → ℝ² → ℝ, draw the tree diagram showing all intermediate dependencies. Write out the chain rule as a matrix product and verify the dimensions at each step.

## 🔗 Connections

- **Phase 1 callback:** the Jacobian IS a linear transformation (Lesson 4). Its determinant scales volume (Lesson 7). Its rank determines which dimensions survive (Lesson 6). Its singular values describe the stretching factors (Lesson 9).
- **Forward connection to ODEs:** when you linearize a nonlinear ODE system near a fixed point (Lesson 21), you compute the Jacobian of the vector field. The eigenvalues of this Jacobian determine stability — everything in Phase 1 comes alive.
- **Forward connection to change of variables:** the Jacobian determinant in Lesson 16 exists because of everything in this lesson. You'll see |det J| as the natural "correction factor" for volume distortion under coordinate changes.
