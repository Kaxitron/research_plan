# Lesson 86: Tangent Spaces and Metric Tensors

[<- Curves and Surfaces](lesson-85-curves-surfaces.md) | [Back to TOC](../README.md) | [Next: Manifolds ->](lesson-87-manifolds.md)

---

> **Why this lesson exists:** The Fisher information matrix -- the central object in information geometry -- is a Riemannian metric on the parameter space of a statistical model. Natural gradient descent, which underpins many modern optimization methods, replaces the Euclidean gradient with the one defined by this metric. To understand why this works and how it connects to Singular Learning Theory, we need the abstract machinery of tangent spaces, cotangent spaces, and metric tensors. This lesson builds that machinery, moving from the concrete surfaces of Lesson 85 to the abstract framework needed for manifolds.

> **Estimated time:** 15--20 hours

---

## Part 1: Tangent Vectors as Derivations

### Moving Beyond R^n

In Lesson 85, tangent vectors were "arrows" -- velocity vectors of curves on surfaces embedded in R^3. This works fine for surfaces in Euclidean space, but breaks down when we consider:

- Parameter spaces that are not naturally embedded in any ambient space
- Spaces defined abstractly by charts and transition maps
- Infinite-dimensional spaces (function spaces)

We need an **intrinsic** definition of tangent vector that does not reference an ambient space.

### The Derivation Definition

A **tangent vector** at a point p on a smooth manifold M is a linear map:

v: C^inf(M) -> R

(where C^inf(M) is the set of smooth functions on M) satisfying the **Leibniz rule** (product rule):

v(fg) = f(p) * v(g) + g(p) * v(f)

Such a map is called a **derivation** at p. Intuitively, v is a "directional derivative operator." Given local coordinates (x^1, ..., x^n), the partial derivative operators:

d/dx^1|_p, d/dx^2|_p, ..., d/dx^n|_p

form a basis for the tangent space. Any tangent vector can be written:

v = v^1 * d/dx^1 + v^2 * d/dx^2 + ... + v^n * d/dx^n

where v^i are the **components** of v in this coordinate system.

### Why Derivations?

The derivation definition captures exactly the right amount of structure:
1. It is coordinate-independent (defined without choosing a basis)
2. It satisfies linearity and the product rule (the essential properties of differentiation)
3. The dimension of the tangent space equals the dimension of the manifold (provable from these axioms alone)

**Equivalence with curves:** Every tangent vector v at p can be realized as the velocity of some curve gamma through p:

v(f) = d/dt[f(gamma(t))]|_{t=0}

This connects the abstract derivation definition back to the geometric "velocity vector" picture.

---

## Part 2: The Tangent Space T_pM

### Structure

The **tangent space** T_pM at a point p is the vector space of all derivations at p. It is a real vector space of dimension n = dim(M).

Given local coordinates (x^1, ..., x^n) around p, the basis {d/dx^i} is called the **coordinate basis**. A tangent vector v in T_pM is written:

v = v^i * d/dx^i

(Here and throughout, we use the **Einstein summation convention**: repeated upper and lower indices are implicitly summed. So v^i * d/dx^i means the sum from i=1 to n of v^i * d/dx^i.)

### Change of Coordinates

If (y^1, ..., y^n) is another coordinate system, then:

d/dy^j = (dx^i/dy^j) * d/dx^i

and the components transform as:

v = v_new^j * d/dy^j   where   v_new^j = (dy^j/dx^i) * v^i

This is the **contravariant** transformation law. The components v^i transform "opposite" to the basis vectors -- when basis vectors get bigger, components get smaller (to keep v the same).

---

## Part 3: The Cotangent Space T*_pM

### Covectors (Linear Functionals)

The **cotangent space** T*_pM is the dual space of T_pM -- the space of all linear maps from T_pM to R:

T*_pM = {omega: T_pM -> R | omega is linear}

Elements of T*_pM are called **covectors** or **1-forms at p**.

### The Dual Basis

Given the coordinate basis {d/dx^i} for T_pM, we define the **dual basis** {dx^i} for T*_pM by:

dx^i(d/dx^j) = delta^i_j

where delta^i_j is the Kronecker delta (1 if i=j, 0 otherwise).

A general covector is written:

omega = omega_i * dx^i

Note the index position: covector components have **lower** indices. They transform **covariantly**:

omega_j_new = (dx^i/dy^j) * omega_i

This is the "same direction" as the basis -- when coordinates stretch, covector components stretch too.

### What Are Covectors Geometrically?

Think of a covector as a set of **level surfaces** with a spacing. Applying a covector omega to a vector v counts "how many level surfaces v crosses." This is the natural pairing:

omega(v) = omega_i * v^i

Gradients of functions are naturally covectors: given f in C^inf(M), the **differential** df is:

df = (df/dx^i) * dx^i

When applied to a tangent vector v:

df(v) = (df/dx^i) * v^i = v(f)

This is the directional derivative of f along v.

---

## Part 4: Metric Tensors

### From First Fundamental Form to Metric Tensor

In Lesson 85, the first fundamental form assigned an inner product to each tangent plane of a surface in R^3. A **metric tensor** generalizes this to abstract manifolds.

A **Riemannian metric** g on a manifold M is a smooth assignment of an inner product g_p to each tangent space T_pM. In coordinates:

g = g_ij * dx^i (tensor product) dx^j

where g_ij = g(d/dx^i, d/dx^j) is a symmetric, positive-definite matrix at each point.

The inner product of two tangent vectors v, w in T_pM is:

g(v, w) = g_ij * v^i * w^j

The **length** of a curve gamma(t) from t=a to t=b is:

L = integral from a to b of sqrt(g_ij * (dx^i/dt) * (dx^j/dt)) dt

This generalizes the arc length formula from Lesson 85.

### The Metric in Matrix Form

In coordinates, g is represented by the matrix:

[g] = [g_11  g_12  ...  g_1n]
      [g_21  g_22  ...  g_2n]
      [...   ...   ...  ... ]
      [g_n1  g_n2  ...  g_nn]

For a surface in R^3 with coordinates (u,v), this is exactly the matrix [E F; F G] from Lesson 85.

The **inverse metric** g^ij is defined by:

g^ij * g_jk = delta^i_k

---

## Part 5: Index Notation and Einstein Summation

### The Einstein Summation Convention

When an index appears once as a superscript and once as a subscript in a term, summation over that index is implied:

v^i * w_i   means   sum_{i=1}^{n} v^i * w_i

Rules:
- **Free indices** appear once on each side of an equation (they must match)
- **Dummy indices** appear exactly twice (once up, once down) and are summed over
- An index should never appear three or more times in a single term
- Free indices can be renamed consistently on both sides

### Raising and Lowering Indices

The metric tensor and its inverse convert between vectors (upper indices) and covectors (lower indices).

**Lowering** (vector to covector):

v_i = g_ij * v^j

This takes a tangent vector v^j and produces a covector v_i. Geometrically, the metric "flattens" a vector into a covector.

**Raising** (covector to vector):

omega^i = g^ij * omega_j

This takes a covector omega_j and produces a vector omega^i. The inverse metric "sharpens" a covector into a vector.

**Example:** The gradient of a function f. The differential df = (df/dx^i) dx^i is naturally a covector with components (df/dx^i) (lower index). The gradient vector field is obtained by raising the index:

(grad f)^i = g^ij * (df/dx^j)

In Euclidean space with the standard metric (g^ij = delta^ij), lowering/raising does nothing -- vectors and covectors look the same. On a curved manifold, they are genuinely different.

### Tensor Notation Practice

Here are key formulas written in index notation:

**Inner product:** g(v, w) = g_ij * v^i * w^j

**Norm squared:** ||v||^2 = g_ij * v^i * v^j

**Trace of a matrix:** tr(A) = A^i_i = g^ij * A_ij

**Metric determinant:** g = det(g_ij)

**Volume element:** sqrt(|g|) * dx^1 ^ dx^2 ^ ... ^ dx^n

---

## Part 6: The Fisher Information Matrix as a Riemannian Metric

### Statistical Manifolds

Consider a parametric family of probability distributions {p(x | theta) : theta in Theta}. The parameter space Theta is a manifold, and the Fisher information matrix defines a natural Riemannian metric on it:

g_ij(theta) = E[ (d log p(x|theta) / d theta^i) * (d log p(x|theta) / d theta^j) ]

This is the **Fisher-Rao metric**. It measures how much the distribution changes when we perturb the parameters.

### Why the Fisher Metric Matters

1. **It is the unique metric (up to scaling) that is invariant under sufficient statistics.** This is the Chentsov theorem -- the Fisher metric is the natural metric on statistical models.

2. **KL divergence is locally quadratic in the Fisher metric:**
   KL(p(.|theta) || p(.|theta + d_theta)) = (1/2) * g_ij * d_theta^i * d_theta^j + O(||d_theta||^3)

3. **Natural gradient descent** uses this metric:
   theta_{t+1} = theta_t - eta * g^{ij}(theta_t) * (dL/d_theta^j)

   This is gradient descent in the intrinsic geometry of the model, not the arbitrary coordinate geometry. It converges faster because it accounts for the curvature of the parameter space.

### Connection to SLT

In Singular Learning Theory, the Fisher information matrix **degenerates** at singular points -- it becomes rank-deficient. This means the Riemannian metric breaks down, and the parameter space is no longer a smooth manifold near singularities. This is precisely why we need the algebraic geometry of Lesson 89: the tools of smooth differential geometry are insufficient at singularities, and we must use resolution of singularities to analyze the geometry there.

The degeneracy of the Fisher metric at singularities is directly related to the **flatness** of the KL divergence surface -- multiple parameters map to the same distribution. Understanding this connection between metric degeneracy and model degeneracy is central to SLT.

---

## Watch -- Primary

**What is Math -- Differential Geometry playlist**
Focus on videos covering tangent spaces, dual spaces, and metric tensors. The visual presentations are invaluable for building intuition about abstract tangent vectors.

**eigenchris -- Tensor Calculus series**
This series is excellent for learning index notation, the Einstein summation convention, and the mechanics of raising/lowering indices. Start from the beginning and work through at least the first 10-15 videos.

Link: Search YouTube for "eigenchris Tensor Calculus"

## Read -- Primary

**Lee, "Introduction to Smooth Manifolds"**
- Chapter 3: Tangent Vectors (derivations, tangent space, computations in coordinates)
- Chapter 6: Covectors and Cotangent Bundle (dual spaces, differential of a function)

This is the standard graduate text. It is rigorous and thorough.

**do Carmo, "Riemannian Geometry"**
- Chapter 1: Riemannian metrics (definition, examples, the metric tensor)

A gentler introduction than Lee, focused on the geometric aspects.

## Read -- Supplement

**Amari, "Information Geometry and Its Applications"**
- Chapter 1: Manifolds of probability distributions
- Chapter 2: The Fisher metric

For the direct connection between Riemannian metrics and statistical models.

**Watanabe, "Algebraic Geometry and Statistical Learning Theory"**
- Section on the Fisher information matrix and its degeneracy at singularities

---

## Exercises

### Computation Exercises

1. **Derivations on R^2.** Let p = (1, 2) and v = 3*(d/dx) + (-1)*(d/dy) be a tangent vector at p.
   (a) Compute v(f) for f(x,y) = x^2*y.
   (b) Compute v(g) for g(x,y) = e^(xy).
   (c) Verify the Leibniz rule: v(fg) = f(p)*v(g) + g(p)*v(f).

2. **Coordinate change.** In R^2, let (x,y) be Cartesian and (r, theta) be polar coordinates.
   (a) Express d/dr and d/d(theta) in terms of d/dx and d/dy.
   (b) Express dx and dy in terms of dr and d(theta).
   (c) Compute the metric tensor g_ij in polar coordinates. Verify g = [1 0; 0 r^2].

3. **Index gymnastics.** Given a 3-dimensional Riemannian manifold with metric:
   g_ij = diag(1, r^2, r^2 * sin^2(theta))   (spherical coordinates)
   (a) Compute g^ij (the inverse metric).
   (b) For the covector omega = (1, 0, 1), compute omega^i = g^ij * omega_j.
   (c) Compute the norm ||omega||^2 = g^ij * omega_i * omega_j.

4. **Fisher information for the normal distribution.** For p(x | mu, sigma) = (1/(sigma*sqrt(2*pi))) * exp(-(x-mu)^2 / (2*sigma^2)):
   (a) Compute d(log p)/d(mu) and d(log p)/d(sigma).
   (b) Compute the 2x2 Fisher information matrix g_ij.
   (c) Show that g = [1/sigma^2, 0; 0, 2/sigma^2].
   (d) Compute the natural gradient direction for L = mu^2 + sigma^2 at the point (mu, sigma) = (1, 1). Compare with the ordinary gradient.

5. **Raising and lowering.** On R^2 with metric g = [2 1; 1 3]:
   (a) Compute g^{ij}.
   (b) For v = (1, -1) (upper indices), compute v_i = g_ij * v^j (lower indices).
   (c) For omega = (2, 0) (lower indices), compute omega^i = g^ij * omega_j (upper indices).
   (d) Verify: g(v, v) = v_i * v^i = g_ij * v^i * v^j.

### Conceptual Exercises

6. **Why covectors are not vectors.** Consider a change of units: you switch from meters to centimeters on one axis.
   (a) How do the components of a tangent vector (velocity) transform?
   (b) How do the components of a covector (gradient of a function) transform?
   (c) Explain why this shows vectors and covectors are genuinely different objects, even though in Euclidean space with Cartesian coordinates they have the same components.

7. **Metric degeneracy and singularities.**
   (a) Consider the family p(x | a) = (1/sqrt(2*pi)) * exp(-(x - a*sin(a))^2 / 2). Show that the Fisher information g_11(a) vanishes at a = 0.
   (b) What does this mean geometrically? (The metric degenerates -- distances go to zero.)
   (c) How does this connect to the idea that multiple parameter values map to the same distribution (non-identifiability)?
   (d) Why does this force us beyond smooth Riemannian geometry and into algebraic geometry?

8. **Natural gradient intuition.** Consider the Bernoulli distribution p(x | theta) = theta^x * (1-theta)^(1-x) for x in {0, 1}.
   (a) Compute the Fisher information g(theta).
   (b) Near theta = 0.5, the Fisher information is moderate. Near theta = 0.01, it is very large. Explain what this means about the "shape" of parameter space.
   (c) If you are minimizing a loss and the current parameter is theta = 0.01, why is the natural gradient step much smaller than the ordinary gradient step?

### Proof Exercise

9. **Derivations form a vector space.** Prove that the set of all derivations at a point p on a smooth manifold M forms a vector space. Specifically:
   (a) Show that if v and w are derivations, then v + w is a derivation.
   (b) Show that c*v is a derivation for any constant c in R.
   (c) Show that any derivation vanishes on constant functions. (Hint: use v(1) = v(1*1) and the Leibniz rule.)
