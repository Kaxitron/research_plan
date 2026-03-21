# Lesson 85: Curves and Surfaces

[<- Group Actions](lesson-84-group-actions.md) | [Back to TOC](../README.md) | [Next: Tangent Spaces ->](lesson-86-tangent-spaces.md)

---

> **Why this lesson exists:** Loss landscapes in deep learning are surfaces (or hypersurfaces) in high-dimensional parameter space. The curvature of these surfaces directly determines optimization difficulty -- flat directions correspond to symmetries and degeneracies, while highly curved directions create optimization bottlenecks. Differential geometry of curves and surfaces gives us the precise language to describe these phenomena. In Singular Learning Theory, the geometry of the KL divergence surface near singularities governs generalization, making this classical material a prerequisite for understanding the RLCT and related invariants.

> **Estimated time:** 15--20 hours

---

## Part 1: Parametric Curves in R^3

### Definition and Examples

A **parametric curve** is a smooth map alpha: I -> R^3, where I is an open interval in R. We write:

alpha(t) = (x(t), y(t), z(t))

The image alpha(I) is the **trace** of the curve. The same trace can be parametrized in many different ways -- the parametrization carries additional information (speed, direction of traversal).

**Key examples:**
- **Straight line:** alpha(t) = p + t*v for a point p and direction v
- **Circle:** alpha(t) = (cos t, sin t, 0)
- **Helix:** alpha(t) = (cos t, sin t, t)
- **Cusp curve:** alpha(t) = (t^2, t^3, 0) -- note: this has a singularity at t = 0

### Tangent Vectors

The **tangent vector** at alpha(t) is the derivative:

alpha'(t) = (x'(t), y'(t), z'(t))

This vector points in the direction of motion and its magnitude is the speed ||alpha'(t)||.

A curve is **regular** if alpha'(t) != 0 for all t in I. Regular curves have a well-defined tangent direction at every point. The cusp curve alpha(t) = (t^2, t^3, 0) is NOT regular at t = 0, since alpha'(0) = (0, 0, 0). Singular points of curves foreshadow the singularities we will study in algebraic geometry (Lesson 89).

### Arc Length

The **arc length** from t = a to t = b is:

L = integral from a to b of ||alpha'(t)|| dt

Arc length is independent of parametrization -- it is a geometric invariant. We can reparametrize any regular curve by arc length s, obtaining a **unit-speed** curve where ||alpha'(s)|| = 1 for all s.

### Curvature

For a unit-speed curve alpha(s), the **curvature** is:

kappa(s) = ||alpha''(s)||

Curvature measures how fast the curve is turning. A straight line has kappa = 0 everywhere; a circle of radius r has kappa = 1/r.

For a general-speed parametrization:

kappa(t) = ||alpha'(t) x alpha''(t)|| / ||alpha'(t)||^3

where x denotes the cross product.

The **Frenet-Serret frame** {T, N, B} at each point of a unit-speed curve provides a moving coordinate system:
- T = alpha'(s) (unit tangent)
- N = alpha''(s) / ||alpha''(s)|| (principal normal)
- B = T x N (binormal)

The Frenet-Serret formulas describe how this frame evolves:
- T' = kappa * N
- N' = -kappa * T + tau * B
- B' = -tau * N

where tau is the **torsion** (measuring how the curve twists out of a plane).

---

## Part 2: Regular Surfaces in R^3

### Parametric Patches

A **regular surface** S in R^3 is a subset that is locally the image of a smooth map X: U -> R^3, where U is an open set in R^2, such that:

1. X is smooth (infinitely differentiable)
2. X is a homeomorphism onto its image
3. The differential dX_q is injective for every q in U (equivalently, X_u x X_v != 0)

We write X(u, v) = (x(u,v), y(u,v), z(u,v)) and call this a **parametric patch** or **coordinate chart**.

**Key examples:**
- **Sphere:** X(theta, phi) = (sin(phi)cos(theta), sin(phi)sin(theta), cos(phi))
- **Torus:** X(u,v) = ((R + r*cos(v))cos(u), (R + r*cos(v))sin(u), r*sin(v))
- **Graph surface:** X(u,v) = (u, v, f(u,v)) for a smooth function f
- **Monkey saddle:** f(x,y) = x^3 - 3xy^2 (higher-order saddle point)

### Tangent Planes

At each point p = X(u_0, v_0), the **tangent plane** T_pS is spanned by the partial derivatives:

X_u = dX/du,   X_v = dX/dv

The **unit normal** is:

N = (X_u x X_v) / ||X_u x X_v||

The tangent plane is the best linear approximation to the surface at p -- this concept generalizes to tangent spaces of abstract manifolds (Lesson 86).

---

## Part 3: First Fundamental Form (The Metric)

### Measuring Distances on Surfaces

The **first fundamental form** I is the restriction of the dot product in R^3 to the tangent plane. If w = a*X_u + b*X_v is a tangent vector, then:

I(w, w) = E*a^2 + 2F*a*b + G*b^2

where the **metric coefficients** are:

E = X_u . X_u,   F = X_u . X_v,   G = X_v . X_v

In matrix form, the metric tensor is:

g = [E  F]
    [F  G]

This is a 2x2 symmetric positive-definite matrix at each point. It encodes ALL intrinsic geometry -- distances, angles, and areas on the surface.

**Arc length** of a curve alpha(t) = X(u(t), v(t)) on the surface:

L = integral of sqrt(E*(u')^2 + 2F*u'*v' + G*(v')^2) dt

**Area** of a region:

A = double integral of sqrt(EG - F^2) du dv

### Alignment Connection

In machine learning, the **Fisher information matrix** plays exactly the role of the first fundamental form -- it is a Riemannian metric on the parameter space of a statistical model. The metric coefficients g_ij = E[d(log p)/d(theta_i) * d(log p)/d(theta_j)] measure how distinguishable nearby parameter values are. This is the foundation of information geometry and natural gradient descent (Lesson 86).

---

## Part 4: Second Fundamental Form and Curvature

### The Shape Operator and Second Fundamental Form

The **second fundamental form** II measures how the surface curves in ambient space. For a tangent vector w = a*X_u + b*X_v:

II(w, w) = e*a^2 + 2f*a*b + g*b^2

where:

e = X_uu . N,   f = X_uv . N,   g = X_vv . N

The **shape operator** (Weingarten map) S: T_pM -> T_pM is the negative derivative of the normal:

S(w) = -dN(w)

The second fundamental form is related to the shape operator by II(v, w) = S(v) . w.

### Gauss Map

The **Gauss map** N: S -> S^2 sends each point on the surface to its unit normal vector on the unit sphere. The shape operator is precisely the differential of the Gauss map: S = -dN.

The Gauss map encodes all extrinsic curvature information. Its differential tells us how fast the normal is rotating as we move along the surface.

### Principal Curvatures

The **principal curvatures** kappa_1 and kappa_2 are the eigenvalues of the shape operator S. The corresponding eigenvectors are the **principal directions** -- the directions of maximum and minimum normal curvature.

For any unit tangent vector making angle theta with the first principal direction, the normal curvature is given by **Euler's formula**:

kappa(theta) = kappa_1 * cos^2(theta) + kappa_2 * sin^2(theta)

### Gaussian Curvature and Mean Curvature

The **Gaussian curvature** is the product of principal curvatures:

K = kappa_1 * kappa_2 = det(S) = (eg - f^2) / (EG - F^2)

The **mean curvature** is the average:

H = (kappa_1 + kappa_2) / 2 = tr(S) / 2

**Geometric meaning:**
- K > 0: elliptic point (bowl-shaped, like a sphere)
- K < 0: hyperbolic point (saddle-shaped)
- K = 0: parabolic point (one flat direction)
- H = 0: minimal surface (soap film)

### Curvature Classification of Surfaces

| Surface | K | H |
|---------|---|---|
| Plane | 0 | 0 |
| Sphere (radius r) | 1/r^2 | 1/r |
| Cylinder | 0 | 1/(2r) |
| Saddle (z = xy at origin) | -1 | 0 |
| Pseudosphere | -1 (constant) | varies |

---

## Part 5: Theorema Egregium

### Statement and Significance

**Gauss's Theorema Egregium (Remarkable Theorem):** The Gaussian curvature K is an **intrinsic** invariant -- it depends only on the first fundamental form (the metric), not on how the surface is embedded in R^3.

This means: if you can compute distances on a surface (without looking at it from outside), you can determine K. A being living on the surface could measure K by measuring triangles and comparing angle sums to pi.

**Why is this remarkable?** K is defined as the product of principal curvatures, which are extrinsic quantities (they reference the normal vector). Yet K turns out to depend only on E, F, G and their first and second partial derivatives. Mean curvature H, by contrast, is genuinely extrinsic.

### Consequences

1. **You cannot flatten a sphere** (K = 1/r^2 != 0) without distorting distances. This is why all flat maps of Earth have distortions.

2. **You can flatten a cylinder** (K = 0) without distortion. That is why a cylinder can be "unrolled."

3. **Isometric surfaces have equal Gaussian curvature.** If you bend a surface without stretching, K is preserved.

### Connection to Loss Landscapes

The Theorema Egregium tells us that certain curvature properties of loss landscapes are intrinsic to the parameter space geometry, independent of the particular coordinate system (parametrization) we choose. This is relevant because:

- Reparametrizing a neural network (e.g., permuting neurons) should not change intrinsic geometric quantities
- The intrinsic geometry near singularities determines the RLCT, which governs generalization in SLT
- Natural gradient methods work precisely because they respect the intrinsic metric (Fisher information) rather than the arbitrary coordinate metric

---

## Watch -- Primary

**What is Math -- Differential Geometry playlist (early videos)**
Focus on the videos covering curves, surfaces, and the fundamental forms. These provide strong geometric intuition with visualizations that are hard to get from textbooks alone.

Link: Search YouTube for "What is Math Differential Geometry"

## Watch -- Supplement

**eigenchris -- Tensors for Beginners**
This series introduces the tensor notation (index notation, Einstein summation) that you will need throughout the remaining geometry lessons. Start here if the notation in differential geometry texts feels opaque.

Link: Search YouTube for "eigenchris Tensors for Beginners"

**3Blue1Brown -- Differential equations and surfaces** (if available)
For building visual intuition about curvature and surface geometry.

## Read -- Primary

**do Carmo, "Differential Geometry of Curves and Surfaces"**
Chapters 1--3 cover everything in this lesson. This is the gold-standard undergraduate text.
- Chapter 1: Curves (tangent vectors, curvature, torsion, Frenet formulas)
- Chapter 2: Regular surfaces, first fundamental form
- Chapter 3: Gauss map, second fundamental form, curvature, Theorema Egregium

**Pressley, "Elementary Differential Geometry"**
A more accessible alternative to do Carmo with similar coverage.

## Read -- Supplement

**Amari, "Information Geometry and Its Applications"**
For understanding how the first fundamental form connects to the Fisher information matrix. Skim Chapter 1 to see the parallel.

---

## Exercises

### Computation Exercises

1. **Curvature of a helix.** For alpha(t) = (a*cos(t), a*sin(t), b*t):
   (a) Compute the tangent vector alpha'(t) and speed ||alpha'(t)||.
   (b) Reparametrize by arc length.
   (c) Compute the curvature kappa and torsion tau.
   (d) Verify that kappa and tau are both constant.

2. **Metric of the sphere.** For the standard parametrization X(theta, phi) = (sin(phi)cos(theta), sin(phi)sin(theta), cos(phi)):
   (a) Compute X_theta and X_phi.
   (b) Compute E, F, G. Verify F = 0 (the coordinates are orthogonal).
   (c) Write down the area element sqrt(EG - F^2) d(theta) d(phi) and integrate to get the surface area of S^2.

3. **Gaussian curvature of the torus.** For X(u,v) = ((R + r*cos(v))cos(u), (R + r*cos(v))sin(u), r*sin(v)):
   (a) Compute E, F, G and e, f, g.
   (b) Compute K = (eg - f^2) / (EG - F^2).
   (c) Show that K = cos(v) / (r(R + r*cos(v))).
   (d) Identify where K > 0 (outer rim), K < 0 (inner rim), and K = 0 (top/bottom circles).
   (e) Verify the Gauss-Bonnet theorem: the integral of K over the torus equals 2*pi*chi(T^2) = 0.

4. **Saddle surface.** For z = xy (so X(u,v) = (u, v, uv)):
   (a) Compute the first and second fundamental forms at the origin.
   (b) Compute K and H at the origin.
   (c) Find the principal curvatures and principal directions.

### Conceptual Exercises

5. **Theorema Egregium application.** Explain why a Pringles chip (K < 0) cannot be pressed flat onto a table (K = 0) without crumpling or tearing. Relate this to the Theorema Egregium.

6. **Loss landscape analogy.** Consider a loss function L(w1, w2) on two parameters. The graph surface is X(w1, w2) = (w1, w2, L(w1, w2)).
   (a) What does the first fundamental form measure in this context?
   (b) What does the Gaussian curvature tell us about the geometry near a critical point?
   (c) If K > 0 at a critical point, is it a local minimum or saddle? What if K < 0?
   (d) How does this relate to the eigenvalues of the Hessian of L?

7. **Singularity preview.** Consider the surface z^2 = x^2 + y^2 (a cone).
   (a) Why is the apex (0,0,0) singular? (Hint: try to find a smooth parametrization.)
   (b) What is the Gaussian curvature away from the apex?
   (c) This is a preview of singularity theory. In SLT, similar singularities arise in the KL divergence surface -- why might singularities in the loss landscape affect generalization?

### Proof Exercise

8. **Intrinsic nature of K.** For a surface given as a graph z = f(x,y):
   (a) Show that K = (f_xx * f_yy - f_xy^2) / (1 + f_x^2 + f_y^2)^2.
   (b) At a critical point of f (where f_x = f_y = 0), show that K equals the determinant of the Hessian.
   (c) Conclude: at critical points of a loss function, the Gaussian curvature of the graph equals det(H), where H is the Hessian matrix.
