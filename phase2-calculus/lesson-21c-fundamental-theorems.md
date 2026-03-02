# Lesson 21C: The Fundamental Theorems of Vector Calculus

[← Vector Calculus](lesson-21b-vector-calculus.md) | [Back to TOC](../README.md) | [Next: Introduction to ODEs →](lesson-22-odes.md)

---

> **Why this lesson exists:** The Fundamental Theorem of Calculus — ∫ₐᵇ f'(x) dx = f(b) − f(a) — says that integrating a derivative over an interval gives the boundary values. Green's theorem, Stokes' theorem, and the Divergence theorem are all higher-dimensional versions of this same idea: *integrating a derivative over a region equals integrating the original function over the boundary.* These theorems are the bridge between local information (derivatives at points) and global information (totals over regions), and they provide the mathematical foundation for conservation laws, the Fokker-Planck equation, and the deep connections between calculus and topology.

## 🎯 Core Concepts

### The Unifying Principle — Boundary ↔ Interior

- **The one idea:** in every dimension, there is a theorem of the form: ∫_Ω (derivative of F) dΩ = ∮_{∂Ω} F d(∂Ω), where Ω is a region and ∂Ω is its boundary. Differentiating on the inside is equivalent to evaluating on the outside.
- **Why this is profound:** it means local pointwise information (derivatives) completely determines global aggregate information (integrals), and vice versa. You can understand the total behavior of a system by looking at its boundary alone — or understand the boundary behavior by looking at what happens in the interior.

### Line Integrals — Integrating Along Curves

- **Scalar line integrals:** ∫_C f ds = ∫ₐᵇ f(r(t)) |r'(t)| dt. You're adding up the values of f along a curve, weighted by arc length. Physically: if f is density, this gives total mass along the wire.
- **Vector line integrals (work integrals):** ∫_C F · dr = ∫ₐᵇ F(r(t)) · r'(t) dt. You're adding up the component of F along the direction of travel. Physically: work done by force F along path C.
- **For conservative fields:** if F = ∇φ, then ∫_C F · dr = φ(end) − φ(start), regardless of the path. This is the Fundamental Theorem for Line Integrals — the direct generalization of FTC to curves in space.
- **Closed loop test:** ∮_C F · dr = 0 for all closed curves C if and only if F is conservative. Non-zero circulation around a loop means the field is not a gradient — it has "rotational" character.

### Green's Theorem — The 2D Bridge

- **Statement:** for a region D in the plane with boundary curve C (traversed counterclockwise): ∮_C (P dx + Q dy) = ∬_D (∂Q/∂x − ∂P/∂y) dA.
- **Translation:** the circulation of F = (P, Q) around the boundary of D equals the integral of the (2D) curl of F over the interior of D.
- **Geometric meaning:** the total rotation around the boundary is the sum of all the tiny local rotations inside. If the field doesn't rotate anywhere inside (curl = 0 everywhere in D), there's no net circulation around the boundary.
- **Divergence form:** ∮_C (P dy − Q dx) = ∬_D (∂P/∂x + ∂Q/∂y) dA. The total outward flux through the boundary equals the integral of divergence over the interior. This is the 2D Divergence Theorem.
- **Why Green's matters:** it converts a hard line integral (1D, along a curve) into an easy area integral (2D, over a region), or vice versa. It also proves that conservative ↔ curl-free in simply connected domains.

### Surface Integrals — Integrating Over Surfaces

- **A surface integral** ∬_S F · dS adds up the flux of F through a surface S. For each tiny patch of surface, you compute "how much F flows through it" — the dot product of F with the outward normal vector n̂, scaled by the area element: ∬_S F · n̂ dS.
- **Parameterized surfaces:** if S is given by r(u, v), the area element is dS = |r_u × r_v| du dv and the normal direction is n̂ = (r_u × r_v)/|r_u × r_v|. The cross product of the partial derivatives gives both the normal direction and the area scaling — this is the 2D analogue of the Jacobian determinant.
- **Physical meaning:** if F is fluid velocity, ∬_S F · dS is the total volume of fluid crossing S per unit time. If F is probability flux, it's the rate at which probability flows through the surface.

### Stokes' Theorem — Curl and Circulation

- **Statement:** for a surface S with boundary curve ∂S: ∮_{∂S} F · dr = ∬_S (∇ × F) · dS.
- **Translation:** the circulation of F around the boundary of a surface equals the flux of the curl through the surface.
- **This generalizes Green's theorem** to surfaces in 3D. Green's theorem is the special case where S is a flat region in the xy-plane.
- **Geometric meaning:** the total "swirling" of F around the boundary comes from adding up all the local rotations (curl) on the surface. If curl F = 0 everywhere on S, there's no net circulation around ∂S.
- **Key consequence:** if curl F = 0 everywhere, then ∮_C F · dr = 0 for every closed curve. This proves that curl-free fields are conservative (in simply connected domains).

### The Divergence Theorem (Gauss's Theorem) — The Big One

- **Statement:** for a solid region V with boundary surface ∂V: ∬_{∂V} F · dS = ∭_V (∇ · F) dV.
- **Translation:** the total outward flux of F through the boundary surface equals the integral of the divergence over the enclosed volume.
- **This is the 3D version** of the 2D divergence form of Green's theorem.
- **Geometric meaning:** the total amount of F "exiting" through the boundary = the total "creation" (source strength) inside. If div F = 0 everywhere in V, then whatever flows in must flow out — nothing is created or destroyed.
- **The connection to conservation laws:** if ρ is a conserved quantity (mass, charge, probability) and J is its flux, then ∂ρ/∂t + ∇ · J = 0 (the continuity equation). Integrating over V and applying the Divergence Theorem: d/dt ∫_V ρ dV = −∬_{∂V} J · dS. The rate of change of total ρ inside V equals the net inward flux through the boundary. This is conservation stated precisely.
- **The derivation of Fokker-Planck:** the Fokker-Planck equation (Lesson 27) is derived by applying the divergence theorem to the probability flux of a stochastic process. The probability current J = fp − (σ²/2)∇p has a drift term and a diffusion term. Conservation of probability (∂p/∂t + ∇ · J = 0) gives the Fokker-Planck PDE directly.

### The Grand Hierarchy

All of these are the same theorem at different dimensions:

| Dimension | Theorem | Interior integral | Boundary integral |
|---|---|---|---|
| 1D | Fundamental Theorem of Calculus | ∫ₐᵇ f'(x) dx | f(b) − f(a) |
| 2D (curl) | Green's / Stokes' | ∬_D curl(F) dA | ∮_{∂D} F · dr |
| 2D (div) | Green's (flux form) | ∬_D div(F) dA | ∮_{∂D} F · n̂ ds |
| 3D (curl) | Stokes' | ∬_S curl(F) · dS | ∮_{∂S} F · dr |
| 3D (div) | Divergence Theorem | ∭_V div(F) dV | ∬_{∂V} F · dS |

The pattern: differentiate inside, evaluate on the boundary. In n dimensions, an integral of a "derivative" over an n-dimensional region equals an integral of the "original" over the (n−1)-dimensional boundary. This pattern continues to arbitrary dimension and is formalized by the **generalized Stokes' theorem** in differential forms, which you'll encounter in Phase 5.

## 📺 Watch — Primary

1. **3Blue1Brown (for Khan Academy) — "Green's, Stokes', and the Divergence Theorem"**
   - *Khan Academy's multivariable calculus section. These were created by Grant Sanderson with his signature visual style.*
2. **Trefor Bazett — "Green's Theorem" series**
   - https://www.youtube.com/watch?v=a_zdFvYXX_c
   - *Step-by-step, visual, with worked examples. Covers both the circulation and flux forms.*
3. **Trefor Bazett — "Divergence Theorem" and "Stokes' Theorem" videos**
   - *Same careful visual treatment. Watch after Green's theorem.*

## 📺 Watch — Secondary

4. **Khan Academy — full "Green's, Stokes', and the Divergence Theorem" unit**
   - https://www.khanacademy.org/math/multivariable-calculus/greens-theorem-and-stokes-theorem
   - *Complete worked examples. Good for practice.*
5. **Steve Brunton — "Vector Calculus and Partial Differential Equations"**
   - https://www.youtube.com/c/Eigensteve
   - *Connects the integral theorems to PDE theory — a bridge to the ODE/PDE block.*

## 📖 Read — Primary

- **Stewart's Calculus** or **Thomas' Calculus** — Chapters on Line Integrals, Green's Theorem, Stokes' Theorem, Divergence Theorem (typically Chapters 16–17)
  - *The standard treatment with many worked examples and exercises.*
- **"Div, Grad, Curl, and All That" by H.M. Schey** — Chapters 3–5
  - *Builds from Green's to Stokes' to Divergence with physical motivation throughout.*

## 📖 Read — Secondary

- **MML Book** does NOT cover these theorems in depth — supplement with the texts above.

## 🔨 Do

- **Green's theorem verification:** compute ∮_C (xy dx + x² dy) around the unit circle both directly (parameterize the circle) and via Green's theorem (integrate the curl over the disk). Verify they match.
- **Divergence theorem verification:** for F = (x, y, z) and V = unit sphere, compute ∭_V div(F) dV and ∬_{∂V} F · dS independently. Both should give 4π.
- **Conservative field check:** given F = (2xy + z, x², x), determine if F is conservative by checking curl(F) = 0. If so, find the potential function φ.
- **Derive the continuity equation** in 1D: consider probability density ρ(x, t) and flux J(x, t). By considering the change in total probability in [a, b], show that ∂ρ/∂t + ∂J/∂x = 0. Then generalize to 3D using the divergence theorem.
- Implement a numerical verification: compute the flux of F = (x², xy, z) through the surface of the unit cube both by surface integration (6 faces) and by volume integration of div(F). Compare the numerical results.

## 🔗 Connections

- **Phase 1 callback:** the Jacobian determinant (Lesson 7) appears in surface integrals as the area scaling factor. The cross product (implicit in Lesson 10) defines surface normals.
- **Previous lesson callback:** Green's theorem proves that curl-free ↔ conservative (Lesson 21B). The Divergence theorem connects div to total flux (Lesson 21B).
- **Forward to ODEs:** fixed points of vector fields (Lesson 22) can be classified as sources, sinks, or centers using divergence and curl. The index theory of vector fields relies on line integrals around singularities.
- **Forward to PDEs:** the heat equation, Fokker-Planck equation, and conservation laws all derive from the Divergence theorem applied to probability or energy flux. This lesson provides the derivation tools.
- **Forward to Phase 5 topology:** the generalized Stokes' theorem unifies all these results into one equation: ∫_Ω dω = ∫_{∂Ω} ω. The de Rham cohomology (Lesson 58–59) measures the "gap" between curl-free and gradient fields — this gap is topological, not geometric.
