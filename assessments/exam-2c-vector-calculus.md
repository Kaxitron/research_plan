# Exam 2C: Vector Calculus — The Language of Flow and Flux

**The Path to AI Alignment — Lessons 24–28 Comprehensive Assessment**

---

| | |
|---|---|
| **Time Allowed** | 90 minutes |
| **Total Points** | 150 |
| **Materials** | Pencil, paper, calculator (no CAS). No code. |
| **Format** | Part I: Curves, Fields, and Green's (7 questions, 70 pts) — Part II: Surfaces, Stokes', and the Big Picture (8 questions, 80 pts) |

> **Advice:** Show all work. Diagrams earn partial credit and are strongly encouraged, especially for orientation and flux questions. The integrative thread: **gradient descent lives on a surface in weight space; the theorems of vector calculus tell you how local behavior (derivatives) connects to global behavior (integrals) — the same principle that makes backpropagation work.**

> *"The divergence theorem says that what flows out of a region equals the total source strength inside. In ML, probability that flows out of one region must flow into another — conservation laws constrain what distributions can do."*

---

# Part I: Curves, Fields, and Green's Theorem (70 points)

*From parameterized curves through Green's theorem — the 2D story of how line integrals connect to double integrals.*

---

## Question 1 (10 pts) — Curves and Parameterization

Consider the helix **r**(t) = (cos t, sin t, t) for t in [0, 2pi].

**(a)** Compute **r**'(t) and ||**r**'(t)||. Interpret ||**r**'(t)|| as the speed of a particle traversing the helix.

**(b)** Compute the arc length of one full turn of the helix.

**(c)** Now consider the reparameterization **r**(t) = (cos 2t, sin 2t, 2t) for t in [0, pi]. Does this trace the same curve? Does it have the same arc length? Explain why arc length is independent of parameterization.

**(d)** A loss landscape trajectory w(t) traces a curve in weight space during training. If ||w'(t)|| is large early in training and small later, what does that tell you about the optimization dynamics? Relate to learning rate schedules.

---

## Question 2 (10 pts) — Scalar Line Integrals and Work

**(a)** Compute the scalar line integral of f(x, y) = xy along the straight line segment from (0, 0) to (2, 4). *(Use the parameterization **r**(t) = (2t, 4t), t in [0, 1].)*

**(b)** Compute the line integral of the vector field **F**(x, y) = (y, x) along the same path from (a). Interpret this as the work done by **F** on a particle traversing the path.

**(c)** Now compute the work integral of the same **F** along the path that goes from (0, 0) to (2, 0) then from (2, 0) to (2, 4) (two straight line segments).

**(d)** Compare your answers to (b) and (c). Are they equal? What does this suggest about whether **F** is conservative?

---

## Question 3 (10 pts) — Gradient Fields and Conservative Vector Fields

Let **F**(x, y) = (2xy + y², x² + 2xy + 3y²).

**(a)** Test whether **F** is conservative by checking if dF1/dy = dF2/dx.

**(b)** Find the potential function phi(x, y) such that **F** = nabla phi. *(Integrate F1 with respect to x, then determine the unknown function of y by comparing with F2.)*

**(c)** Using the Fundamental Theorem for Line Integrals, compute the integral of **F** dot d**r** along ANY path from (0, 0) to (1, 2). State the theorem before applying it.

**(d)** The gradient of a loss function nabla L(w) is always a conservative vector field. In one sentence, explain why this is immediate from the definition. Then explain: why does this guarantee that gradient descent on a smooth loss function can never "go in circles" (in the absence of noise)?

---

## Question 4 (10 pts) — Green's Theorem (Circulation Form)

Let **F**(x, y) = (-y, x) and let C be the unit circle traversed counterclockwise.

**(a)** State Green's theorem (circulation form).

**(b)** Compute the circulation integral (line integral of **F** around C) directly by parameterizing C as **r**(t) = (cos t, sin t), t in [0, 2pi].

**(c)** Compute the same integral using Green's theorem (as a double integral over the unit disk). Verify the answers match.

**(d)** The scalar curl dF2/dx - dF1/dy measures local rotation. Compute it for this **F**. Explain in one sentence why a constant scalar curl of 2 throughout the disk gives a circulation of 2pi around the boundary.

**(e)** In fluid dynamics, this measures vorticity. In a neural network's feature space, if learned representations undergo a "rotation" during training, how would you detect it from the Jacobian of the representation map?

---

## Question 5 (10 pts) — Green's Theorem (Flux Form) and Divergence

Let **F**(x, y) = (x², y²).

**(a)** State Green's theorem in flux form (relating the outward flux across a closed curve to the double integral of divergence).

**(b)** Compute div **F** = dF1/dx + dF2/dy.

**(c)** Let D be the unit square [0, 1] x [0, 1] with boundary C traversed counterclockwise. Compute the total outward flux using the divergence integral.

**(d)** Verify by computing the flux directly through each of the four sides of the square. *(Recall the outward flux through a curve is the integral of **F** dot **n** ds.)*

**(e)** The divergence of a probability flow field tells you where probability is being created or destroyed. If a normalizing flow model has div **F** > 0 everywhere, what does this mean for the probability distribution being transported? Why must a proper normalizing flow have regions where div **F** < 0 somewhere?

---

## Question 6 (10 pts) — The Laplacian and Harmonic Functions

**(a)** Define the Laplacian of a scalar function f(x, y). Write it in terms of second partial derivatives.

**(b)** Compute the Laplacian of f(x, y) = x² - y². Is f harmonic?

**(c)** Compute the Laplacian of g(x, y) = e^x sin(y). Is g harmonic?

**(d)** A function is harmonic if nabla squared f = 0. State the mean value property of harmonic functions in one sentence. Then explain: why does this guarantee that a harmonic function has no local maxima or minima in the interior of its domain?

**(e)** The Laplacian appears in the heat equation u_t = k nabla squared u. In the context of diffusion models, smoothing a data distribution with Gaussian noise is equivalent to running the heat equation forward in time. Why does the Laplacian's role as a "local averaging operator" make this connection natural?

---

## Question 7 (10 pts) — Conceptual Checkpoint: 2D Vector Calculus

This question has no computation. Answer each part in 2-3 sentences.

**(a)** Explain the difference between a scalar line integral and a vector line integral. Give a physical example of each.

**(b)** Why can't a vector field with nonzero curl be conservative? Relate to the fundamental theorem for line integrals.

**(c)** Green's theorem has two forms: circulation and flux. Both convert a line integral to a double integral. What is the difference in what they measure physically?

**(d)** A gradient field nabla f always has curl zero. The converse holds on simply connected domains. Give an example of a domain where the converse fails and explain why.

**(e)** In ML, why do we care about whether a vector field is conservative? Connect to the existence of a loss function that gradient descent can minimize.

---

# Part II: Surfaces, Stokes', Divergence, and the Unified Picture (80 points)

*Extending everything to 3D — parametric surfaces, flux through surfaces, and the grand theorems that connect derivatives to integrals across all dimensions.*

---

## Question 8 (10 pts) — Parametric Surfaces and Surface Area

Consider the parametric surface **r**(u, v) = (u cos v, u sin v, u) for u in [0, 2] and v in [0, 2pi].

**(a)** Describe what surface this is geometrically. *(Hint: what is the relationship between x, y, z?)*

**(b)** Compute **r**_u and **r**_v (the partial derivatives).

**(c)** Compute the cross product **r**_u x **r**_v.

**(d)** Compute ||**r**_u x **r**_v|| and set up the surface area integral. Evaluate it.

**(e)** Why does ||**r**_u x **r**_v|| du dv give the area element dS? Explain using the geometric meaning of the cross product magnitude from Phase 1 (parallelogram area).

---

## Question 9 (10 pts) — Surface Integrals of Scalar Functions

**(a)** Compute the surface integral of f(x, y, z) = z over the hemisphere z = sqrt(1 - x^2 - y^2), x^2 + y^2 <= 1. *(Use the parameterization **r**(u, v) = (u cos v, u sin v, sqrt(1 - u^2)) with u in [0, 1], v in [0, 2pi].)*

**(b)** Interpret your answer physically: if f represents mass density on the hemisphere, what does the surface integral represent?

**(c)** Compare a surface integral to a double integral. What role does the factor ||**r**_u x **r**_v|| play, analogous to the Jacobian in change of variables?

**(d)** In a neural network, the decision boundary is a surface in feature space. If you wanted to compute the "total curvature" of the decision boundary (to measure complexity), what kind of integral would you set up?

---

## Question 10 (10 pts) — Orientation and Flux Integrals

Let **F**(x, y, z) = (0, 0, z) and let S be the paraboloid z = 1 - x^2 - y^2 for z >= 0, oriented with upward-pointing normal.

**(a)** Explain what it means for a surface to be "orientable." Give an example of a non-orientable surface.

**(b)** Parameterize S using **r**(u, v) = (u cos v, u sin v, 1 - u^2) for u in [0, 1], v in [0, 2pi]. Compute **r**_u x **r**_v and check that it points upward (positive z-component). If not, reverse the orientation.

**(c)** Compute the flux integral: the double integral of **F** dot (**r**_u x **r**_v) du dv.

**(d)** Flux measures the rate at which a vector field flows through a surface. If **F** represents the flow of probability in a 3D latent space, what does positive flux through S mean? How does this connect to the continuity equation in probability flow?

---

## Question 11 (12 pts) — Curl and Stokes' Theorem

Let **F**(x, y, z) = (y, -x, z^2).

**(a)** Compute curl **F** = nabla x **F** using the determinant formula.

**(b)** Let S be the portion of the plane z = 1 over the unit disk x^2 + y^2 <= 1, oriented upward. Compute the surface integral of (curl **F**) dot d**S** directly.

**(c)** The boundary of S is the circle x^2 + y^2 = 1, z = 1, traversed counterclockwise when viewed from above. Compute the line integral of **F** dot d**r** around this boundary.

**(d)** Verify that Stokes' theorem holds: the surface integral of curl **F** equals the line integral around the boundary. State the theorem.

**(e)** Stokes' theorem says "the integral of a derivative over a region equals the integral of the function over the boundary." How is the Fundamental Theorem of Calculus a special case of this same principle? Write the analogy explicitly: FTC: f'(x) dx over [a,b] = ___. Stokes': curl **F** dot d**S** over S = ___.

---

## Question 12 (10 pts) — The Divergence Theorem

Let **F**(x, y, z) = (x, y, z) and let E be the unit ball x^2 + y^2 + z^2 <= 1 with boundary S (the unit sphere), oriented outward.

**(a)** Compute div **F**.

**(b)** Compute the triple integral of div **F** over the unit ball. *(Use the volume of the unit ball = 4pi/3.)*

**(c)** The divergence theorem says this equals the flux of **F** through S. Without computing the flux directly, state what it must be.

**(d)** Now verify by computing the outward flux of **F** through the unit sphere directly. *(Use the fact that on the unit sphere, the outward normal is **n** = (x, y, z) and **F** dot **n** = x^2 + y^2 + z^2 = 1.)*

**(e)** The divergence theorem is the mathematical backbone of conservation laws. In a diffusion model, probability must be conserved (it integrates to 1 at all times). Write the conservation law: d/dt (integral of p over E) = -flux of (**probability current**) through boundary of E. Explain in 1-2 sentences why the divergence theorem converts this to the continuity equation dp/dt + div(**J**) = 0.

---

## Question 13 (10 pts) — The Grand Unified Hierarchy

This question is purely conceptual. No computation required.

**(a)** Fill in the following table showing the hierarchy of integral theorems:

| Theorem | "Derivative" | Integrated over | Equals integral over | Dimension |
|---------|-------------|-----------------|---------------------|-----------|
| FTC | f'(x) | interval [a,b] | ___ | 1D |
| FTLI | nabla f | ___ | ___ | curves |
| Green's | ___ | region R | ___ | 2D |
| Stokes' | ___ | surface S | ___ | 2D surface in 3D |
| Divergence | ___ | volume E | ___ | 3D |

**(b)** All five theorems have the form: "integral of a derivative over a region = integral of the original over the boundary." The generalized Stokes' theorem unifies all of them as: integral of d(omega) over M = integral of omega over dM, where d is the exterior derivative and dM is the boundary. In your own words, explain why this is arguably the single most important theorem in all of mathematics.

**(c)** In ML, backpropagation computes "how a change at the boundary (output loss) relates to changes in the interior (weights)." In 2-3 sentences, explain the conceptual parallel to the generalized Stokes' theorem. *(This is an analogy, not a direct application — articulate what the analogy captures.)*

**(d)** Physics-informed neural networks (PINNs) use the divergence theorem to convert volume integrals in PDEs into surface integrals, reducing computational cost. Why is evaluating a surface integral cheaper than a volume integral? How does dimensionality play a role?

---

## Question 14 (8 pts) — Vector Calculus Identities and Proof

**(a)** Prove that div(curl **F**) = 0 for any smooth vector field **F**. *(Compute directly using partial derivatives and use equality of mixed partials.)*

**(b)** Prove that curl(nabla f) = **0** for any smooth scalar function f.

**(c)** These two identities say that "the boundary of a boundary is zero" — or more precisely, that applying a derivative operator twice gives zero. In the hierarchy of Part (a) of Q13, this means: the curl of a gradient is zero, and the divergence of a curl is zero. Relate this to the statement: "exact forms are closed." You may answer informally.

**(d)** In ML, the fact that nabla x (nabla f) = **0** is equivalent to saying "gradient fields are curl-free." Why does this matter for guaranteeing that gradient descent on a loss function cannot exhibit persistent rotation (cycling behavior)?

---

## Question 15 (10 pts) — Synthesis: Vector Calculus in the ML Pipeline

**(a)** A normalizing flow transforms a simple base distribution q_0 through a sequence of invertible maps. The change in log-probability is: log q_k(z_k) = log q_0(z_0) - sum of log |det(J_i)|. Connect the Jacobian determinant here to the divergence theorem: for an infinitesimal flow dx/dt = f(x), the instantaneous change in log-density is d/dt log p = -div(f). Explain in 2-3 sentences why divergence measures how a flow "stretches" or "compresses" volume (and therefore density).

**(b)** The score function nabla_x log p(x) is a vector field. For a Gaussian p(x) = N(mu, Sigma), compute the score explicitly. Is the score field conservative? What is its potential function?

**(c)** In score-based diffusion models, a neural network learns to approximate the score field at each noise level. Stokes' theorem says that the circulation of a conservative field is zero. How could you use this as a consistency check on a learned score network? *(Hint: compute the line integral of the learned score around a closed loop.)*

**(d)** The Fokker-Planck equation describes how probability density evolves under a stochastic process: dp/dt = -div(f p) + D nabla^2 p. Identify the divergence theorem's role in deriving this from conservation of probability. Name the two competing effects (advection and diffusion) and what each term contributes.

**(e)** Looking back at the entire exam: vector calculus provides the mathematical language for understanding how quantities (probability, information, gradients) flow through spaces. State one insight from this exam that changed or deepened your understanding of ML.

---

## Optional Mini-Project (~45 minutes): Visualizing Flow and Flux

**Build a vector field visualizer that demonstrates the major theorems of vector calculus.**

1. Define three 2D vector fields: (a) a gradient field **F** = nabla f for some f(x,y) of your choice, (b) a rotational field like (-y, x), (c) a field with a point source like (x, y) / (x^2 + y^2)
2. For each field, plot the vector field using quiver plots
3. Compute and overlay the divergence (as a heatmap) and the scalar curl (as a second heatmap)
4. For a chosen closed curve C, numerically compute both the circulation (line integral) and the double integral of the curl over the enclosed region. Verify Green's theorem by comparing them
5. Repeat for flux: compute the outward flux through C and compare with the integral of divergence over the enclosed region

**Stretch:** Animate a probability density being transported by one of your vector fields. At each timestep, verify that the total probability is conserved (integral of p = 1). Show that div(**F**) > 0 regions lose density and div(**F**) < 0 regions gain density — the continuity equation in action.

**Tools:** NumPy, Matplotlib, SciPy (for numerical integration). No ML libraries needed.
