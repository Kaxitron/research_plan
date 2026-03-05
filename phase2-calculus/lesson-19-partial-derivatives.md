# Lesson 19: 3D Geometry, Curves, and Curvature

[<- Previous](lesson-18-systems-odes.md) | [Back to TOC](../README.md) | [Next: Multivariable Functions ->](lesson-20-multivariable-chain-rule.md)

---

## Core Learning

- Lines and planes are the fundamental geometric objects in 3D. A line through point P in direction v has parametric form r(t) = P + tv; eliminating the parameter gives symmetric equations. A plane through point P with normal vector n satisfies n . (r - P) = 0. The distance from a point to a plane uses the projection formula. These objects appear everywhere: the tangent line to a curve, the tangent plane to a surface, and the decision boundaries of linear classifiers are all lines and planes in the appropriate dimension.
- Vector-valued functions r(t) = <x(t), y(t), z(t)> describe curves in space. The derivative r'(t) is the tangent vector pointing in the direction of motion; its magnitude |r'(t)| is the speed. This separates geometry (the path) from kinematics (how fast you traverse it). Arc length s = integral of |r'(t)| dt measures the intrinsic length of the curve independent of parameterization, and reparameterizing by arc length produces a unit-speed curve where the parameter itself measures distance traveled.
- Curvature kappa measures how sharply a curve bends -- it is the rate at which the unit tangent vector T changes direction per unit arc length: kappa = |dT/ds|. Large curvature means tight turning; zero curvature means straight. The osculating circle at a point has radius R = 1/kappa and represents the best-fitting circle to the curve. The TNB (Frenet-Serret) frame -- unit tangent T, principal normal N, and binormal B = T x N -- provides a moving coordinate system that rides along the curve, with T pointing forward, N pointing toward the center of curvature, and B completing the right-handed frame.

## Watch -- Primary

- **Trefor Bazett -- Multivariable Calculus** (3D geometry and curves sections)
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxc_CvEy7xBKRQr6I214QJcd
  - Focus on the videos covering equations of lines and planes, vector-valued functions, arc length, curvature, and the TNB frame (roughly videos 4-9 in the playlist).

## Watch -- Secondary

- **3Blue1Brown -- "Essence of Calculus"**
  - https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr
  - The series builds intuition for derivatives as rates of change that extends naturally to vector-valued functions and curves in space.

## Read

- **Stewart's Calculus** -- Chapter 12 (vectors, lines, planes) and Chapter 13 (vector functions, arc length, curvature). These chapters cover all the 3D geometry and curve theory with worked examples.
- **MML Book (Deisenroth, Faisal, Ong)** -- Section 5.5 on linearization and tangent spaces, which connects the geometric ideas here to the differential geometry perspective used in ML.

## Key Equations

Parametric line through P in direction v:

$$\mathbf{r}(t) = \mathbf{P} + t\mathbf{v}$$

Plane with normal n through point P:

$$\mathbf{n} \cdot (\mathbf{r} - \mathbf{P}) = 0$$

Distance from point Q to plane n . r = d:

$$D = \frac{|\mathbf{n} \cdot \mathbf{Q} - d|}{|\mathbf{n}|}$$

Arc length:

$$L = \int_a^b |\mathbf{r}'(t)| \, dt$$

Curvature:

$$\kappa = \left|\frac{d\mathbf{T}}{ds}\right| = \frac{|\mathbf{r}' \times \mathbf{r}''|}{|\mathbf{r}'|^3}$$

TNB frame:

$$\mathbf{T} = \frac{\mathbf{r}'}{|\mathbf{r}'|}, \quad \mathbf{N} = \frac{\mathbf{T}'}{|\mathbf{T}'|}, \quad \mathbf{B} = \mathbf{T} \times \mathbf{N}$$

## ML and Alignment Connection

Curvature shows up in optimization through the geometry of the loss landscape. The curvature of optimization trajectories -- paths traced by gradient descent through parameter space -- determines convergence behavior. High curvature in the loss surface (large Hessian eigenvalues) causes gradient descent to overshoot and zigzag, which is why adaptive optimizers exist. The concept of geodesics (curves of zero geodesic curvature) on parameter manifolds underlies natural gradient descent, which follows the steepest descent path on the statistical manifold rather than in raw parameter space.

The TNB frame provides intuition for how coordinate systems adapt to local geometry, which is the same principle behind information geometry and the Fisher information metric. When we later study how the parameter-function map of neural networks creates curved manifolds with singularities, the Frenet-Serret machinery of this lesson -- how frames rotate as you move along a curve -- will provide concrete geometric intuition for abstract differential-geometric concepts.
