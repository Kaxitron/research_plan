# Lesson 21B: Vector Calculus — Fields, Divergence, Curl, and the Laplacian

[← Taylor Expansions](lesson-17-taylor-expansions.md) | [Back to TOC](../README.md) | [Next: Fundamental Theorems →](lesson-19-fundamental-theorems.md)

---

> **Why this lesson exists:** A vector field assigns a vector to every point in space — wind velocity at every location, the gradient of a loss surface at every point in parameter space, the flow of probability density. The differential operators divergence, curl, and Laplacian are the tools for analyzing these fields: where do they spread out? Where do they rotate? How do they diffuse? The Laplacian in particular is the single most important operator in the curriculum — it IS the heat equation, it appears in the Fokker-Planck equation governing SGD, and it defines the diffusion process behind generative models.

## 🎯 Core Concepts

### Vector Fields

- **Definition:** a vector field F on ℝⁿ assigns a vector F(x) ∈ ℝⁿ to each point x ∈ ℝⁿ. In 2D: F(x, y) = (P(x,y), Q(x,y)). In 3D: F(x, y, z) = (P, Q, R).
- **Visualization:** draw an arrow at each point showing the direction and magnitude. A vector field is like a map of currents — at every location, something is "flowing" in a particular direction with a particular strength.
- **Gradient fields:** given a scalar function φ(x), the gradient ∇φ is a vector field. It points in the direction of steepest increase, with magnitude equal to the rate of increase. You already know this from Lesson 14 — now we're placing it in the broader context of all vector fields.
- **The key question:** is every vector field a gradient field? No — and the distinction is one of the deepest ideas in vector calculus.

### Conservative Vector Fields and Potential Functions

- **A vector field F is conservative** if F = ∇φ for some scalar function φ (called the potential). Equivalently: the line integral of F along any path depends only on the endpoints, not the path taken. Equivalently: the integral around any closed loop is zero.
- **Why this matters:** gradient descent follows the gradient field ∇L. Loss functions define conservative fields — the loss L is the potential. But not every dynamical system follows a conservative field. Systems with momentum, or adversarial training (GANs), involve non-conservative dynamics where the "flow" rotates rather than descending a potential.
- **Test for conservativeness (in 2D):** F = (P, Q) is conservative iff ∂P/∂y = ∂Q/∂x. This "equality of mixed partials" condition is exactly the curl being zero (see below).
- **Finding the potential:** if F is conservative, you can reconstruct φ by integrating: φ(x,y) = ∫P dx + g(y), then determine g(y) by matching ∂φ/∂y = Q.

### Divergence — Sources and Sinks

- **Definition:** for F = (P, Q, R), the divergence is div(F) = ∇ · F = ∂P/∂x + ∂Q/∂y + ∂R/∂z. It's a scalar — one number at each point.
- **Geometric meaning:** divergence measures the "net outward flux per unit volume." Positive divergence = source (field flows outward, like air expanding from a heat source). Negative divergence = sink (field flows inward, like water draining). Zero divergence = incompressible flow (what flows in equals what flows out).
- **The ∇ · notation:** treat ∇ = (∂/∂x, ∂/∂y, ∂/∂z) as a "vector of operators." The dot product ∇ · F applies each partial derivative to the corresponding component and sums — exactly the dot product formula, but with derivatives instead of numbers.
- **Physical intuition:** place a tiny balloon in the flow. If div(F) > 0, the balloon expands (net outward push). If div(F) < 0, it contracts. If div(F) = 0, it deforms but keeps the same volume.
- **Connection to probability:** the continuity equation ∂ρ/∂t + ∇ · (ρv) = 0 says "probability is conserved" — the rate of change of density equals the negative divergence of the probability flux. This is the foundation of the Fokker-Planck equation.

### Curl — Rotation and Circulation

- **Definition (3D):** curl(F) = ∇ × F = (∂R/∂y − ∂Q/∂z, ∂P/∂z − ∂R/∂x, ∂Q/∂x − ∂P/∂y). It's a vector — direction gives the axis of rotation, magnitude gives the rotation rate.
- **Definition (2D):** for F = (P, Q) in the plane, curl reduces to the scalar ∂Q/∂x − ∂P/∂y.
- **Geometric meaning:** curl measures the local rotation of the field. Place a tiny paddlewheel in the flow — the curl tells you how fast and about which axis it spins.
- **The key theorem:** F is conservative (F = ∇φ) if and only if curl(F) = 0 (in a simply connected domain). Gradient fields have no rotation. This is equivalent to the "mixed partials are equal" test: ∂²φ/∂x∂y = ∂²φ/∂y∂x.
- **For optimization:** pure gradient descent has zero curl (it's a gradient field). But some optimization methods introduce rotational dynamics — Adam with momentum can have non-zero curl in its effective update field, and GAN training (where two networks compete) famously has rotational dynamics that prevent convergence to a fixed point.

### The Laplacian — Curvature of a Field

- **Definition:** for a scalar function u, the Laplacian is ∇²u = ∇ · (∇u) = ∂²u/∂x² + ∂²u/∂y² + ∂²u/∂z². It's the divergence of the gradient — a scalar.
- **Geometric meaning:** the Laplacian at a point measures how much u(x) differs from the average of u in a small ball around x. If ∇²u > 0, the point is below its neighborhood average (a pit). If ∇²u < 0, it's above (a bump). If ∇²u = 0, the function is "harmonic" — it equals its own local average everywhere.
- **The Laplacian IS the heat equation:** u_t = k∇²u says "temperature changes at a rate proportional to how far it is from its neighborhood average." Hot spots (above average → ∇²u < 0) cool. Cold spots (below average → ∇²u > 0) warm. Everything smooths toward uniformity. You will study this in depth in the PDE lesson.
- **Connection to the trace of the Hessian:** ∇²u = tr(H_u) — the Laplacian is the trace of the Hessian matrix. Since the trace equals the sum of eigenvalues (Lesson 11), the Laplacian is the sum of the curvatures in all directions. This connects to the mean curvature of level surfaces.
- **The operator hierarchy:** gradient (∇) takes a scalar to a vector. Divergence (∇·) takes a vector to a scalar. Curl (∇×) takes a vector to a vector. The Laplacian (∇²) = divergence of gradient: scalar → vector → scalar. These four operators, plus the theorems connecting them, are the complete toolkit of vector calculus.

### Identities That Matter

- **curl(∇φ) = 0** — the curl of any gradient field is zero. "Gradients don't rotate."
- **div(curl F) = 0** — the divergence of any curl field is zero. "Curls are sourceless."
- **∇²φ = div(grad φ)** — the Laplacian is divergence of gradient.
- **∇ × (∇ × F) = ∇(∇ · F) − ∇²F** — the "BAC-CAB" identity for vector fields.
- These form an exact sequence: scalar →^{grad} vector →^{curl} vector →^{div} scalar, where each composition gives zero. This algebraic structure (a "de Rham complex") is the bridge between vector calculus and the topology of Phase 5.

## 📺 Watch — Primary

1. **Khan Academy — Multivariable Calculus: Divergence and Curl**
   - https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/divergence-and-curl-articles/a/divergence
   - *Grant Sanderson (3Blue1Brown) made these for Khan Academy. Clear visual explanations of both operators.*
2. **3Blue1Brown — "Divergence and Curl" (for Khan Academy)**
   - https://www.youtube.com/watch?v=rB83DpBJQsE
   - *The animated fluid-flow visualizations make divergence and curl click immediately.*
3. **Trefor Bazett — "Vector Fields, Divergence, and Curl" series**
   - https://www.youtube.com/watch?v=sB0m-RB_JG0
   - *Systematic treatment with worked examples. Multiple videos covering each concept.*

## 📺 Watch — Secondary

4. **Khan Academy — "Laplacian intuition"**
   - https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/laplacian/v/laplacian-intuition
   - *Why the Laplacian measures "difference from neighborhood average."*
5. **Steve Brunton — "Conservative Vector Fields and Potential Functions"**
   - https://www.youtube.com/c/Eigensteve
   - *Connects conservative fields to energy and stability — the physical intuition behind gradient systems.*

## 📖 Read — Primary

- **MML Book, Chapter 5.6** (higher-order derivatives, including the Hessian and Laplacian)
- **Stewart's Calculus** or **Thomas' Calculus** — Chapter on Vector Calculus (typically Ch. 16)
  - *Any standard Calc 3 text covers vector fields, div, curl, and the Laplacian with worked examples and exercises.*

## 📖 Read — Secondary

- **"Div, Grad, Curl, and All That" by H.M. Schey**
  - *An informal, physics-oriented introduction. Short (less than 200 pages) and highly readable. Builds intuition through physical examples.*

## 🔨 Do

- Plot vector fields in Python using `matplotlib.pyplot.quiver`: (a) F = (−y, x) — pure rotation, zero divergence, nonzero curl; (b) F = (x, y) — pure expansion, nonzero divergence, zero curl; (c) ∇φ for φ = x² + y² — gradient of a paraboloid. Compute div and curl for each and verify visually.
- Verify the identity curl(∇φ) = 0 for φ = x²y + yz³ by computing the gradient and then the curl. Do it both symbolically and numerically at several points.
- Compute the Laplacian of: (a) φ = x² + y² (paraboloid), (b) φ = ln(x² + y²) (log potential), (c) φ = e^x sin y. For (b) and (c), verify that ∇²φ = 0 — these are harmonic functions.
- **Key exercise:** for the "double well" potential φ(x, y) = (x² − 1)² + y², compute the gradient field, plot it, compute the divergence, and identify the critical points. Classify each critical point using the Hessian (connecting to Lesson 17 and Phase 1 eigenvalue analysis).
- Explore the distinction between conservative and non-conservative fields: compute the line integral of F = (−y, x) around the unit circle. Then try F = (−y/(x²+y²), x/(x²+y²)) — same formula but singular at the origin. Why does one give zero and the other give 2π?

## 🔗 Connections

- **Phase 1 callback:** the gradient is a vector field built from the dot product structure (Lesson 10). The Laplacian involves the trace of the Hessian, which connects to eigenvalue sums (Lesson 8, 11).
- **Forward to PDEs:** the Laplacian IS the heat equation (Lesson 25). Understanding it here means the PDE lesson can focus on solutions rather than introducing the operator.
- **Forward to Fokker-Planck:** the continuity equation ∂ρ/∂t + ∇ · (ρv) = 0 uses divergence. The Fokker-Planck equation adds a Laplacian diffusion term. Both are natural consequences of this lesson's toolkit.
- **Forward to Phase 5 topology:** the exact sequence grad → curl → div (where each composition is zero) is a de Rham complex. It connects the differential operators of this lesson to the topological invariants of Lesson 61.
