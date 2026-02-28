# Lesson 14: Matrix Calculus — Bridging to Backpropagation

[← Calculus Fundamentals](lesson-13-calculus-fundamentals.md) | [Back to TOC](../README.md) | [Next: Gradients →](lesson-15-gradients.md)

---

## 🎯 Core Learning

- Derivatives of scalar functions (quick refresh)
- Partial derivatives: how a function changes when you wiggle *one* input
- The gradient vector: collecting all partial derivatives into one object that points "uphill"
- Jacobian matrices: when your function maps vectors to vectors, the derivative is a *matrix*
- Key matrix calculus results: derivatives of **Ax**, **xᵀAx**, and why these matter

### Taylor Series and Linearization — Why Gradient Descent Works

- **The key idea:** near any point, a smooth function looks like a straight line (1D) or a flat plane (nD). Taylor expansion makes this precise:
  - **1D:** f(x + δ) ≈ f(x) + f'(x)·δ + ½f''(x)·δ² + ...
  - **nD:** f(x + δ) ≈ f(x) + ∇f(x)ᵀδ + ½δᵀHδ + ...  (where H is the Hessian)
- **First-order approximation:** f(x + δ) ≈ f(x) + ∇f(x)ᵀδ. This is the tangent plane. Gradient descent trusts this approximation for one small step (learning rate controls how far), then recomputes.
- **Why learning rate matters geometrically:** the linear approximation is only accurate near x. Step too far and you're following a tangent line that no longer matches the actual surface. Step too small and you waste time on tiny improvements.
- **Second-order approximation** uses the Hessian (see below) for curvature. Newton's method uses this to take smarter steps — but computing the Hessian is expensive for large networks.
- **MML Book, Chapter 5.8** covers multivariate Taylor series in detail.

### Gradients of Matrices — Computing ∂L/∂W

When your variable is a *matrix* (like a weight matrix W), you need matrix calculus:

- **∂/∂x (Ax) = A** — the gradient of a linear function is just the matrix itself
- **∂/∂x (xᵀAx) = (A + Aᵀ)x** — for symmetric A, this simplifies to 2Ax
- **∂/∂X tr(AX) = Aᵀ** — trace derivatives appear constantly in ML loss functions
- **∂/∂X tr(XᵀAX) = (A + Aᵀ)X** — used in deriving weight gradients
- **∂/∂X ||Y - XW||²_F = -2(Y - XW)Wᵀ** — the gradient for linear regression with matrix inputs

These identities are what you'd use to derive gradient updates by hand. In practice, autograd computes them for you — but understanding them lets you verify correctness and build intuition for what the gradient "looks like."

**MML Book, Chapter 5.4–5.5** provides a systematic treatment with worked examples.

### The Hessian Matrix — Second-Order Curvature

- **The Hessian** H is the matrix of all second partial derivatives: H_ij = ∂²f/∂xᵢ∂xⱼ
- It's always **symmetric** (if f is twice differentiable) — so everything from Lesson 11 about symmetric matrices applies.
- **Hessian eigenvalues = curvature in each direction:**
  - All positive → local minimum (bowl shape) — the function curves upward in every direction
  - All negative → local maximum (upside-down bowl)
  - Mixed → saddle point (curves up in some directions, down in others)
  - Some zero → flat direction (the function doesn't curve — plateau or ridge)
- **Condition number** = λ_max / λ_min of the Hessian. If large, the landscape is "elongated" — steep in one direction, flat in another. This makes gradient descent slow (it zig-zags). This is why Adam optimizer adapts the learning rate per-parameter.
- **MML Book, Chapter 5.7** covers higher-order derivatives including the Hessian.

## 📺 Watch

- **3Blue1Brown — Essence of Calculus, Chapter 1:** "The essence of calculus"
  - https://www.youtube.com/watch?v=WUvTyaaNkzM
- **3Blue1Brown — Essence of Calculus, Chapter 10:** "Taylor series"

## 📖 Read

- **"The Matrix Calculus You Need for Deep Learning" by Parr & Howard**
  - https://arxiv.org/abs/1802.01528
  - Designed specifically for ML practitioners. Essential reading.
- **MML Book, Chapter 5** — vector calculus (full chapter)
  - Pay special attention to: 5.4 (gradients of matrices), 5.5 (useful identities), 5.7 (higher-order derivatives / Hessian), 5.8 (Taylor series)
- **"The Matrix Cookbook"** — https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf
  - Section 2 (derivatives) — a reference sheet of every matrix calculus identity you might need

## 🔨 Do

- Compute the gradient of f(x,y) = x²y + sin(xy) by hand
- Compute the Jacobian of a simple 2→2 function
- Write Python code that numerically approximates gradients and compares to analytical results
- **Taylor approximation visualization:** Plot f(x) = sin(x) alongside its 1st, 3rd, and 5th order Taylor approximations. See how each term adds precision. Then do the same for f(x,y) = sin(x)cos(y) — visualize the tangent plane (1st order) vs the original surface.
- **Matrix gradient exercise:** For the linear regression loss L(w) = ||Xw - y||², derive ∂L/∂w by hand using the matrix identities above. Verify: ∂L/∂w = 2Xᵀ(Xw - y). Then verify numerically in Python.
- **Hessian exercise:** Compute the Hessian of f(x,y) = x³ - 3xy² (monkey saddle). Find eigenvalues at the origin. Verify it's a saddle point (mixed eigenvalue signs). Visualize the surface and see the saddle.
- **Key exercise:** For a 2-parameter neural network loss, compute the Hessian numerically (finite differences). Find its eigenvalues. Interpret: which direction has steep curvature? Which is flat? How does the condition number relate to training difficulty?

## 🔗 ML Connection

Every parameter in a neural network gets updated by its gradient. The Jacobian tells you how a layer's output changes with its input — exactly what backpropagation multiplies through. The gradient of the loss is literally the "direction to adjust weights."

## 🧠 Alignment Connection

The Hessian's eigenvalue structure directly impacts alignment. If the loss landscape has sharp, narrow minima for aligned behavior but broad, flat minima for misaligned behavior, gradient descent will preferentially find misaligned solutions (the "simplicity bias" problem). Understanding the Hessian — curvature in every direction — lets you reason about whether alignment objectives create favorable loss geometry. This connects directly to Singular Learning Theory (Phase 5), where the geometry of critical points determines generalization behavior.
