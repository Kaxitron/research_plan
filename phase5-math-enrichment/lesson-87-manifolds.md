# Lesson 87: Manifolds, Geodesics, and Lie Groups

[<- Tangent Spaces](lesson-86-tangent-spaces.md) | [Back to TOC](../README.md) | [Next: Differential Forms ->](lesson-88-differential-forms.md)

---

> **Why this lesson exists:** Neural network parameter spaces are not flat Euclidean spaces -- they are manifolds with complex geometry. Understanding manifolds, geodesics, and connections is essential for Singular Learning Theory, where the parameter space near singularities has non-trivial topology and geometry. Lie groups, which combine group structure with manifold structure, appear naturally as symmetry groups of neural networks (permutation symmetries of hidden units, for example). The exponential map and geodesics provide the right framework for understanding optimization trajectories in these curved spaces.

> **Estimated time:** 15--20 hours

---

## Part 1: Topological Manifolds

### Locally Euclidean Spaces

A **topological manifold** of dimension n is a topological space M that is:

1. **Locally Euclidean:** Every point p in M has a neighborhood homeomorphic to an open set in R^n
2. **Hausdorff:** Distinct points can be separated by open sets
3. **Second-countable:** The topology has a countable basis

The key idea: a manifold looks like R^n in small patches, even if its global structure is very different.

**Examples:**
- R^n itself (trivially)
- The circle S^1 (locally looks like R^1)
- The sphere S^2 (locally looks like R^2)
- The torus T^2 = S^1 x S^1
- The real projective space RP^n (the set of lines through the origin in R^(n+1))

**Non-examples:**
- A figure-eight (fails to be a manifold at the crossing point -- the neighborhood is not homeomorphic to R^1)
- A cone with its apex (the apex has no neighborhood homeomorphic to R^2)

### Charts and Atlases

A **chart** (or coordinate system) on M is a pair (U, phi) where U is an open subset of M and phi: U -> R^n is a homeomorphism onto an open set in R^n. The map phi assigns coordinates to points in U.

An **atlas** is a collection of charts {(U_alpha, phi_alpha)} that covers M (every point of M lies in at least one U_alpha).

**Example: The sphere S^2.** No single chart can cover S^2 (because S^2 is compact but R^2 is not). We need at least two charts. The standard choice is **stereographic projection** from the north and south poles:

- phi_N: S^2 \ {north pole} -> R^2, projecting from the north pole
- phi_S: S^2 \ {south pole} -> R^2, projecting from the south pole

Together, these two charts cover all of S^2.

### Transition Maps

Where two charts (U_alpha, phi_alpha) and (U_beta, phi_beta) overlap, the **transition map** is:

phi_beta composed with phi_alpha^{-1}: phi_alpha(U_alpha intersect U_beta) -> phi_beta(U_alpha intersect U_beta)

This is a map from an open set in R^n to another open set in R^n. The smoothness of transition maps determines the type of manifold.

---

## Part 2: Smooth Manifolds

### Smooth Structure

A **smooth manifold** is a topological manifold equipped with an atlas whose transition maps are all **smooth** (infinitely differentiable). Such an atlas is called a **smooth atlas**, and the equivalence class of compatible smooth atlases is a **smooth structure**.

A function f: M -> R is **smooth** if for every chart (U, phi), the composition f composed with phi^{-1}: R^n -> R is smooth in the usual calculus sense.

### Smooth Maps and Diffeomorphisms

A map F: M -> N between smooth manifolds is **smooth** if for every pair of charts (U, phi) on M and (V, psi) on N, the composition psi composed with F composed with phi^{-1} is smooth.

A **diffeomorphism** is a smooth bijection whose inverse is also smooth. Two manifolds are **diffeomorphic** if there exists a diffeomorphism between them -- they are "the same" as smooth manifolds.

**Warning:** A topological manifold can admit multiple non-equivalent smooth structures. The famous example: R^4 has uncountably many exotic smooth structures! (This does not happen in any other dimension.)

### Submanifolds

A **submanifold** of R^n is a subset that is locally the level set of a smooth map with full-rank Jacobian. By the **implicit function theorem**, if F: R^n -> R^k has rank k at every point of F^{-1}(0), then F^{-1}(0) is a smooth manifold of dimension n - k.

**Example:** The sphere S^(n-1) = {x in R^n : ||x||^2 - 1 = 0} is a submanifold of R^n of dimension n-1.

This is relevant to singularity theory: when the Jacobian drops rank, we get singularities. The set of singular parameter values in SLT is precisely where this condition fails.

---

## Part 3: Connections and Covariant Derivatives

### The Problem of Differentiation on Manifolds

On R^n, we can differentiate vector fields by differentiating their components. On a manifold, this breaks down because there is no canonical way to compare tangent vectors at different points -- they live in different vector spaces.

A **connection** provides the missing structure: a rule for "connecting" nearby tangent spaces, enabling differentiation of vector fields along curves.

### The Covariant Derivative

A (linear) **connection** on M assigns to each pair of vector fields (X, V) a new vector field nabla_X V (the covariant derivative of V along X) satisfying:

1. **Linearity in X:** nabla_{fX + gY} V = f * nabla_X V + g * nabla_Y V
2. **Linearity in V:** nabla_X (V + W) = nabla_X V + nabla_X W
3. **Leibniz rule:** nabla_X (fV) = X(f) * V + f * nabla_X V

In local coordinates, the connection is determined by the **Christoffel symbols** Gamma^k_{ij}:

nabla_{d/dx^i} (d/dx^j) = Gamma^k_{ij} * d/dx^k

For a vector field V = V^k * d/dx^k, the covariant derivative along d/dx^i is:

(nabla_{d/dx^i} V)^k = dV^k/dx^i + Gamma^k_{ij} * V^j

### The Levi-Civita Connection

On a Riemannian manifold (M, g), there is a unique connection that is:

1. **Torsion-free:** nabla_X Y - nabla_Y X = [X, Y] (the Lie bracket)
2. **Metric-compatible:** X(g(Y, Z)) = g(nabla_X Y, Z) + g(Y, nabla_X Z)

This is the **Levi-Civita connection**. Its Christoffel symbols are given by:

Gamma^k_{ij} = (1/2) * g^{kl} * (dg_{li}/dx^j + dg_{lj}/dx^i - dg_{ij}/dx^l)

This formula is worth memorizing -- it shows that the connection is completely determined by the metric.

---

## Part 4: Parallel Transport

### Definition

**Parallel transport** of a vector V along a curve gamma(t) means moving V along gamma while keeping nabla_{gamma'} V = 0. In components:

dV^k/dt + Gamma^k_{ij} * (dx^i/dt) * V^j = 0

This is a system of first-order ODEs -- given V at the starting point, there is a unique solution.

### Geometric Meaning

On a flat space (R^n with the standard metric), parallel transport simply keeps the vector constant. On a curved manifold, parallel transport along different paths between the same two endpoints can give different results.

**The classic example:** On the sphere S^2, parallel-transport a vector along a triangle:
1. Start at the north pole with a vector pointing along the 0-degree meridian
2. Transport south to the equator along the 0-degree meridian
3. Transport east along the equator to the 90-degree meridian
4. Transport north back to the pole

The vector has been rotated by 90 degrees! This rotation is called **holonomy** and is a direct measure of curvature.

### Holonomy and Curvature

The **Riemann curvature tensor** R measures the failure of parallel transport to commute:

R(X, Y)V = nabla_X nabla_Y V - nabla_Y nabla_X V - nabla_{[X,Y]} V

For a small parallelogram spanned by X and Y, transporting V around the boundary rotates it by approximately R(X, Y)V. The curvature tensor contains complete information about the local geometry.

---

## Part 5: Geodesics and the Exponential Map

### Geodesics

A **geodesic** is a curve gamma(t) that parallel-transports its own tangent vector:

nabla_{gamma'} gamma' = 0

In coordinates:

d^2 x^k/dt^2 + Gamma^k_{ij} * (dx^i/dt) * (dx^j/dt) = 0

These are the **geodesic equations** -- a system of second-order ODEs. Geodesics generalize straight lines to curved spaces: they are the "straightest possible" curves.

**Key examples:**
- In R^n: straight lines (Gamma = 0, so d^2x/dt^2 = 0)
- On S^2: great circles
- On a cylinder: helices (including straight lines and circles)
- On a torus: more complex, but computable

**Geodesics as length minimizers:** Locally (for short enough segments), geodesics minimize arc length between their endpoints. This is the Riemannian version of "the shortest path between two points is a straight line."

### The Exponential Map

The **exponential map** at p maps tangent vectors to points on the manifold:

exp_p: T_pM -> M

defined by exp_p(v) = gamma_v(1), where gamma_v is the geodesic starting at p with initial velocity v.

**Properties:**
- exp_p(0) = p
- exp_p(tv) = gamma_v(t) (the geodesic at time t)
- d(exp_p)_0 = identity (the exponential map is a local diffeomorphism near 0)
- **Normal coordinates:** the coordinates obtained by identifying T_pM with R^n via a basis give **geodesic normal coordinates** around p, in which Gamma^k_{ij}(p) = 0 (the Christoffel symbols vanish at p)

### Optimization Interpretation

In optimization on manifolds, the exponential map is used for:

1. **Retraction:** After computing a gradient step in T_pM, map back to M via exp_p
2. **Line search:** Search along the geodesic exp_p(t * v) for different step sizes t
3. **Riemannian gradient descent:** theta_{t+1} = exp_{theta_t}(-eta * grad L)

This is the manifold version of the update rule theta_{t+1} = theta_t - eta * grad L. On a flat space, exp_p(v) = p + v and we recover standard gradient descent.

---

## Part 6: Lie Groups

### Definition

A **Lie group** G is a group that is also a smooth manifold, where the group operations (multiplication and inversion) are smooth maps.

**Examples:**
- GL(n, R) -- the general linear group (invertible n x n matrices). This is an open subset of R^(n^2), hence a manifold of dimension n^2.
- O(n) -- the orthogonal group (A^T A = I). Dimension n(n-1)/2.
- SO(n) -- the special orthogonal group (orthogonal matrices with det = 1). Same dimension as O(n).
- SL(n, R) -- special linear group (det = 1). Dimension n^2 - 1.
- (R^n, +) -- Euclidean space with addition.
- S^1 -- the circle group (complex numbers of unit modulus under multiplication).
- S^3 -- the unit quaternions under quaternion multiplication (isomorphic to SU(2)).

### The Lie Algebra

The **Lie algebra** g of a Lie group G is the tangent space at the identity element, T_eG, equipped with the **Lie bracket** [X, Y].

For matrix Lie groups, the Lie bracket is simply the matrix commutator:

[X, Y] = XY - YX

**Examples:**
- gl(n, R) = all n x n matrices (Lie algebra of GL(n, R))
- so(n) = skew-symmetric matrices (A^T = -A) (Lie algebra of SO(n))
- sl(n, R) = traceless matrices (Lie algebra of SL(n, R))

The Lie algebra captures the "infinitesimal" structure of the group -- it encodes the local behavior near the identity.

### The Exponential Map for Lie Groups

For a matrix Lie group, the exponential map from the Lie algebra to the group is the **matrix exponential**:

exp(X) = I + X + X^2/2! + X^3/3! + ...

This connects the Lie algebra (tangent space) to the Lie group (manifold). For example:
- exp: so(3) -> SO(3) maps a skew-symmetric matrix to a rotation
- Every rotation in SO(3) can be written as exp(X) for some skew-symmetric X

This exponential map coincides with the Riemannian exponential map when G is equipped with a bi-invariant metric.

### Lie Groups in Neural Networks

Lie groups appear in deep learning through symmetries:

1. **Weight space symmetries:** Permuting hidden neurons of a layer is a discrete group action, but the continuous version (scaling symmetries) forms a Lie group.

2. **Equivariant networks:** Networks designed to respect symmetries of the input (rotations, translations) use Lie group representations.

3. **Parameter space geometry:** The parameter space of certain models has a natural Lie group structure (e.g., the Stiefel manifold for orthogonal weight matrices).

4. **SLT connection:** Singularities in the parameter space often occur at points with enhanced symmetry. Understanding the Lie group structure of the symmetry group helps classify these singularities.

---

## Watch -- Primary

**What is Math -- Manifolds section**
Provides visual intuition for charts, atlases, and the idea of "locally Euclidean." Focus on the videos that build up to the definition of a smooth manifold.

**eigenchris -- Tensor Calculus (geodesics and connections)**
The later videos in this series cover Christoffel symbols, covariant derivatives, and geodesics with excellent worked examples. Particularly valuable for understanding the geodesic equations.

Link: Search YouTube for "eigenchris Tensor Calculus geodesics"

## Watch -- Supplement

**XylyXylyX -- "What is a Manifold?" series**
A thorough and patient treatment of manifold theory starting from topological spaces. Good for filling in any gaps in the topological prerequisites.

## Read -- Primary

**Lee, "Introduction to Smooth Manifolds"**
- Chapter 1: Smooth manifolds (charts, atlases, transition maps)
- Chapter 2: Smooth maps
- Chapter 5: Submanifolds
- Chapter 7: Lie groups (definition, Lie algebra, exponential map)

**do Carmo, "Riemannian Geometry"**
- Chapter 2: Connections (covariant derivative, Christoffel symbols)
- Chapter 3: Geodesics (geodesic equations, exponential map, normal coordinates)

## Read -- Supplement

**Hall, "Lie Groups, Lie Algebras, and Representations"**
For a deeper treatment of Lie groups, particularly matrix Lie groups. Chapter 1--3 give a self-contained introduction focused on the matrix case.

---

## Exercises

### Computation Exercises

1. **Charts for S^1.** The circle S^1 cannot be covered by a single chart.
   (a) Define two charts that cover S^1 using angle coordinates. Specify the domains.
   (b) Compute the transition map where the charts overlap. Verify it is smooth.
   (c) Why is a single chart from (0, 2*pi) -> S^1 not sufficient? (What goes wrong at the identification point?)

2. **Christoffel symbols on the sphere.** Using spherical coordinates (theta, phi) with the metric g = [1, 0; 0, sin^2(theta)]:
   (a) Compute all eight Christoffel symbols Gamma^k_{ij} (many will be zero).
   (b) Write down the geodesic equations.
   (c) Verify that great circles satisfy these equations. (Hint: consider the equator theta = pi/2, phi = t.)

3. **Parallel transport on S^2.** A vector V is parallel-transported along the equator (theta = pi/2) from phi = 0 to phi = alpha.
   (a) Write the parallel transport equations.
   (b) Solve them. Show that the vector rotates by an angle that depends on alpha.
   (c) For a complete loop (alpha = 2*pi), show the vector returns to its original value. Now consider a triangle (as described in Part 4) and compute the holonomy angle.

4. **Matrix exponential.** Let X = [0, -theta; theta, 0] be a 2x2 skew-symmetric matrix.
   (a) Compute X^2, X^3, X^4.
   (b) Compute exp(X) by summing the series. Show exp(X) = [cos(theta), -sin(theta); sin(theta), cos(theta)].
   (c) Verify that exp(X) is in SO(2).
   (d) Interpret: the Lie algebra so(2) is one-dimensional (spanned by [0,-1;1,0]), and the exponential map wraps R around the circle SO(2).

5. **Geodesics on the Poincare half-plane.** The upper half-plane H = {(x,y) : y > 0} with metric g = (1/y^2) * [1, 0; 0, 1]:
   (a) Compute the Christoffel symbols.
   (b) Show that vertical lines (x = constant) are geodesics.
   (c) Show that semicircles centered on the x-axis are geodesics.

### Conceptual Exercises

6. **Why manifolds for neural networks?**
   (a) Consider a neural network with one hidden layer of width 2. Explain why permuting the two hidden neurons gives the same input-output function.
   (b) This means the parameter-to-function map is not injective. Why does this make the parameter space fail to be a manifold (in the sense of the map to function space)?
   (c) How does this connect to singularities in SLT?

7. **The exponential map and optimization.**
   (a) In Euclidean space, the exponential map at any point is exp_p(v) = p + v. Verify this satisfies the geodesic equation.
   (b) On the sphere, exp_p(v) follows a great circle. If you are at the north pole and take a gradient step, you end up at a point along a great circle. Why is this more geometrically natural than simply subtracting the gradient?
   (c) What could go wrong with naive (Euclidean) gradient descent on a manifold?

8. **Lie algebra and infinitesimal symmetries.**
   (a) The group SO(3) acts on R^3 by rotations. The Lie algebra so(3) consists of skew-symmetric 3x3 matrices. Show that each element of so(3) can be identified with a vector in R^3 (via the "hat map").
   (b) Interpret: elements of the Lie algebra are "infinitesimal rotations" -- angular velocity vectors.
   (c) The Lie bracket [X, Y] in so(3) corresponds to the cross product in R^3. Verify this for two specific elements.

### Proof Exercise

9. **Geodesics locally minimize length.** This is a foundational result. Outline the proof for the case of a Riemannian manifold:
   (a) Show that a length-minimizing curve (if it exists and is smooth) satisfies the geodesic equation. (Hint: use the calculus of variations -- the Euler-Lagrange equation for the length functional.)
   (b) Explain why the converse only holds locally: give an example of a geodesic on S^2 that is not globally length-minimizing.
   (c) State the Hopf-Rinow theorem and explain its significance for the existence of geodesics.
