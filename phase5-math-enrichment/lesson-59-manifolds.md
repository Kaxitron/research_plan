# Lesson 59: Manifolds and Tangent Spaces — The Stage for Optimization

[← Homotopy](lesson-58-homotopy.md) | [Back to TOC](../README.md) | [Next: Algebraic Geometry →](lesson-60-algebraic-geometry.md)

---

> **Why this lesson exists:** A manifold is a space that looks locally like ℝⁿ — it's curved globally but flat locally. The surface of the Earth is a 2-manifold: locally flat (you can use a flat map), globally curved (no flat map covers it all). Loss landscapes, weight spaces modulo symmetry, and data manifolds are all manifolds (or nearly so). The tangent space at each point gives you a linear approximation — and optimization on manifolds (Riemannian gradient descent) generalizes everything you know about flat-space optimization.

## 🎯 Core Concepts

### Smooth Manifolds — Locally Euclidean

- **An n-dimensional manifold M** is a topological space that's locally homeomorphic to ℝⁿ. Each point has a neighborhood that looks like a patch of ℝⁿ — a coordinate chart.
- **An atlas** is a collection of charts covering M, with smooth transition maps between overlapping charts. This makes M a smooth manifold — you can do calculus on it.
- **Examples:** the circle S¹ (1-manifold), the sphere S² (2-manifold), the torus T² (2-manifold), the group of rotations SO(3) (3-manifold), the space of positive definite matrices (an open cone in matrix space).
- **Non-examples:** a figure-eight is NOT a manifold (the crossing point has no Euclidean neighborhood). Varieties with singularities are not manifolds at the singular points — this is precisely the issue SLT addresses.

### Tangent Spaces and Tangent Bundles

- **The tangent space T_p M** at a point p is the set of all "velocity vectors" of curves through p. It's a vector space of the same dimension as M.
- **Geometric picture:** for a surface in ℝ³, the tangent space at p is literally the tangent plane. For an abstract manifold, you define it intrinsically using equivalence classes of curves or derivations.
- **The tangent bundle TM** = ⋃_p T_p M is the collection of all tangent spaces. It's itself a manifold of dimension 2n (each tangent vector needs n coordinates for the base point + n for the direction).
- **Gradients live in tangent spaces.** The gradient ∇L at a point w is an element of T_w M (or more precisely, the cotangent space). Gradient descent moves along the manifold in the direction of steepest descent.

### Riemannian Metrics — Measuring on Curved Spaces

- **A Riemannian metric** assigns an inner product to each tangent space: g_p: T_p M × T_p M → ℝ. This lets you measure lengths, angles, and distances on the manifold.
- **Geodesics** are the shortest paths between points on a Riemannian manifold — the "straight lines" of curved space. On a sphere, geodesics are great circles.
- **The natural gradient** (Amari) uses the Fisher information matrix as a Riemannian metric on the space of probability distributions. The natural gradient direction is different from the Euclidean gradient direction — it accounts for the curvature of the statistical manifold.
- **For neural networks:** the space of distributions parameterized by a network has a natural Riemannian structure. The natural gradient is theoretically optimal but computationally expensive. K-FAC and other methods approximate it.

### The Manifold Hypothesis for Data

- **The manifold hypothesis:** high-dimensional data (images, text, audio) lies on or near a low-dimensional manifold embedded in the ambient space. A 256×256 image lives in ℝ^{65536}, but natural images occupy a much smaller manifold.
- **Dimensionality reduction** (PCA, t-SNE, autoencoders) approximates this manifold. The intrinsic dimension of the data manifold determines how many parameters you actually need.
- **Neural networks as manifold learners:** the hidden layers learn a coordinate system on the data manifold. The representation at each layer is a chart mapping data to a latent space where the task is simpler.

### Singularities — Where Manifold Structure Breaks Down

- **A singular point** is where the manifold structure fails. The variety V = {(x,y) : xy = 0} (two crossing lines) is a manifold everywhere except the origin, where the two branches meet.
- **SLT studies these singularities** in the loss landscape. At singular points, the Hessian is degenerate — the tangent space description breaks down. You need algebraic geometry (next lesson) to understand the local structure.
- **The key question:** how does the loss landscape behave near a singularity? The RLCT measures this. Near a smooth critical point, loss grows quadratically (∝ w²). Near a singularity, it can grow as w^{2/λ} for some rational λ < 1 — this is the RLCT.

## 📺 Watch — Primary

1. **Eigenchris — "Tensor Calculus" playlist (YouTube)**
   - *Excellent visual introduction to manifolds and tangent spaces for physicists/engineers.*
2. **3Blue1Brown — differential forms or manifold content (if available)**

## 📖 Read — Primary

- **"An Introduction to Manifolds" by Loring Tu** — Chapters 1–5
  - *Very clear, aimed at advanced undergrads.*
- **"Mathematics for Machine Learning" (MML)** — Chapter 7 (optimization on manifolds)

## 🔨 Do

- Parameterize the sphere S² using spherical coordinates. Compute the tangent vectors at a point. Verify the Riemannian metric is g = dθ² + sin²θ dφ².
- Implement Riemannian gradient descent on the sphere: minimize f(x,y,z) = z (find the south pole) constrained to x²+y²+z² = 1. Compare with projected gradient descent and see they give different trajectories but the same answer.
- The manifold of positive-definite 2×2 matrices: parameterize it, compute the Fisher metric, and visualize geodesics. Compare with straight lines in matrix space.
- Find the singular points of V = {(x,y,z) : x² + y² - z² = 0} (a cone). Show that V is a manifold everywhere except the origin. Compute the tangent space at a smooth point.
