# Lesson 89: Algebraic Geometry and Singularities for SLT

[<- Differential Forms](lesson-88-differential-forms.md) | [Back to TOC](../README.md) | [Next: Analysis of Algorithms ->](lesson-90-analysis-of-algorithms.md)

---

> **Why this lesson exists:** This is the mathematical heart of Singular Learning Theory. The real log canonical threshold (RLCT), which governs how singular statistical models generalize, is defined using resolution of singularities from algebraic geometry. Neural networks are singular models -- their parameter-to-function maps have degenerate fibers, and the KL divergence has non-isolated critical points. Classical statistics (which assumes smooth, identifiable models) breaks down at these singularities. Algebraic geometry provides the tools to analyze what happens instead: the RLCT replaces the parameter count in the BIC/MDL formula, giving a geometrically meaningful measure of model complexity. Understanding this lesson is essential for anyone serious about the mathematical foundations of deep learning theory.

> **Estimated time:** 18--24 hours

---

## Part 1: Affine Varieties

### Polynomial Equations Define Geometry

An **affine variety** V(I) in R^n (or C^n) is the set of common zeros of a collection of polynomials:

V(f_1, ..., f_k) = {x in R^n : f_1(x) = 0, f_2(x) = 0, ..., f_k(x) = 0}

**Examples:**
- V(x^2 + y^2 - 1) = the unit circle in R^2
- V(x*y) = the union of the x-axis and y-axis in R^2
- V(x^2 - y^3) = a cuspidal cubic curve in R^2
- V(x^2 + y^2 + z^2 - 1) = the unit sphere in R^3
- V(x*y, x*z, y*z) = the three coordinate axes in R^3

Affine varieties are the geometric objects of algebraic geometry. Unlike the smooth manifolds of differential geometry, varieties can have **singularities** -- points where the geometry degenerates.

### Polynomial Ideals

The set of ALL polynomials that vanish on a variety V forms an **ideal** I(V) in the polynomial ring R[x_1, ..., x_n]:

I(V) = {f in R[x_1, ..., x_n] : f(p) = 0 for all p in V}

Recall from algebra: an ideal I in a ring R is a subset closed under addition and under multiplication by any ring element.

**The algebra-geometry dictionary:**

| Algebra (Ideals) | Geometry (Varieties) |
|-------------------|---------------------|
| Ideal I | Variety V(I) |
| Sum I + J | Intersection V(I) intersect V(J) |
| Product I*J | Union V(I) union V(J) (approximately) |
| Prime ideal | Irreducible variety |
| Maximal ideal | Point |
| Radical of I | Same variety, minimal ideal |

This dictionary is the foundation of algebraic geometry: geometric questions become algebraic questions, and vice versa.

### Hilbert's Nullstellensatz

The **Nullstellensatz** ("zero-locus theorem") makes the algebra-geometry dictionary precise. Over an algebraically closed field (like C):

**Weak form:** The only maximal ideals in C[x_1, ..., x_n] are of the form (x_1 - a_1, ..., x_n - a_n) for points (a_1, ..., a_n) in C^n.

**Strong form:** I(V(J)) = sqrt(J), where sqrt(J) = {f : f^k in J for some k} is the radical of J.

In plain language: a polynomial vanishes on V(J) if and only if some power of it belongs to J. The radical "captures" exactly the right ideal for a given variety.

Over R (which is not algebraically closed), the Nullstellensatz requires modification, but the spirit is the same.

---

## Part 2: Singularities

### What Is a Singularity?

A point p on a variety V is **singular** if the tangent space at p has dimension larger than expected (larger than the dimension of V).

For a variety V(f) defined by a single equation f = 0 in R^n, the point p is singular if:

df/dx_1(p) = df/dx_2(p) = ... = df/dx_n(p) = 0

That is, the gradient vanishes at p.

More generally, for V(f_1, ..., f_k), the point p is singular if the **Jacobian matrix**:

J = [df_i/dx_j]

has rank less than the codimension of V (i.e., less than n - dim(V)).

A point that is not singular is called **smooth** or **regular**.

### The Jacobian Criterion

**Jacobian criterion:** A point p on V(f_1, ..., f_k) is smooth if and only if the Jacobian matrix J at p has the expected rank.

**Examples of singularities:**

1. **Node:** V(y^2 - x^2(x+1)) at the origin. The curve crosses itself -- two branches meet. The tangent space at (0,0) is all of R^2 (dimension 2 instead of 1).

2. **Cusp:** V(y^2 - x^3) at the origin. The curve has a sharp point. The gradient (df/dx, df/dy) = (-3x^2, 2y) vanishes at (0,0).

3. **Whitney umbrella:** V(x^2 - y^2*z) in R^3. The singular locus is the z-axis (x = y = 0).

4. **Cone:** V(x^2 + y^2 - z^2). The apex (0,0,0) is singular.

### Classification of Singularities

Singularities are classified by their **multiplicity** and local structure:

- **Multiplicity:** The order of vanishing of the defining equations at the singular point. A node has multiplicity 2, a cusp has multiplicity 2 (but different local structure).
- **Isolated vs non-isolated:** An isolated singularity has a neighborhood where no other singular points exist. A non-isolated singularity sits on a locus of singular points.
- **Normal crossings:** A variety has **normal crossings** at a point if, in suitable coordinates, it locally looks like a union of coordinate hyperplanes (e.g., x*y = 0 in R^2). This is the "simplest" type of singularity.

---

## Part 3: Resolution of Singularities

### The Goal

**Resolution of singularities** is the process of replacing a singular variety with a smooth variety that is isomorphic to the original away from the singularities.

Formally: given a singular variety X, find a smooth variety Y and a proper birational map pi: Y -> X such that pi is an isomorphism over the smooth locus of X.

### Blowups: The Key Tool

A **blowup** replaces a point (or subvariety) with a projective space, "spreading out" the singularity.

**Blowup of R^2 at the origin:** Consider R^2 with coordinates (x, y). The blowup is the set:

Bl_0(R^2) = {((x, y), [s : t]) in R^2 x RP^1 : x*t = y*s}

The map pi: Bl_0(R^2) -> R^2 is the projection ((x,y), [s:t]) -> (x,y).

**What this does:**
- Away from the origin, pi is a bijection (nothing changes)
- The origin is replaced by a copy of RP^1 (the **exceptional divisor** E)
- Lines through the origin in R^2 are "separated" in the blowup -- they arrive at E at different points

In the chart s = 1 (so [s:t] = [1:t] and y = t*x):

Bl_0(R^2) is parametrized by (x, t) where y = t*x.

### Blowup of the Cusp

Consider V(y^2 - x^3) -- the cuspidal cubic. Substituting y = t*x in the chart s = 1:

(t*x)^2 - x^3 = x^2(t^2 - x) = 0

This factors as x^2 = 0 (the exceptional divisor, with multiplicity 2) and t^2 = x (the **strict transform**).

The strict transform t^2 = x is a smooth parabola! The singularity has been resolved.

The factor x^2 tells us that the exceptional divisor appears with multiplicity 2 -- this multiplicity is crucial for computing the RLCT.

### Blowup of the Node

For V(y^2 - x^2(x+1)), substituting y = t*x:

t^2*x^2 - x^2(x+1) = x^2(t^2 - x - 1) = 0

The strict transform t^2 - x - 1 = 0 is smooth, and at x = 0 we get t = +/- 1 -- the two branches of the node have been separated.

### Hironaka's Theorem

**Theorem (Hironaka, 1964):** Every algebraic variety over a field of characteristic zero admits a resolution of singularities by a sequence of blowups.

This is one of the monumental achievements of 20th-century mathematics (Fields Medal, 1970). For our purposes, the key point is:

**Any singularity can be resolved into normal crossings** by iterated blowups. After resolution, the variety locally looks like a product of coordinate hyperplanes, which is amenable to explicit computation.

---

## Part 4: The Real Log Canonical Threshold (RLCT)

### Setup: Statistical Learning Theory

Consider a statistical model p(x | w) parametrized by w in W (a compact subset of R^d). The **true distribution** is q(x) = p(x | w_0) for some (unknown) true parameter w_0.

The **KL divergence** from the model to the truth is:

K(w) = integral of q(x) * log(q(x) / p(x|w)) dx

K(w) >= 0 with equality if and only if p(x|w) = q(x) almost everywhere.

The set of true parameters is:

W_0 = {w in W : K(w) = 0} = {w : p(x|w) = q(x) a.e.}

### The Problem with Singular Models

In classical (regular) statistics, W_0 = {w_0} is a single point, and K(w) behaves like a non-degenerate quadratic near w_0:

K(w) ~ (w - w_0)^T * I(w_0) * (w - w_0) / 2

where I(w_0) is the Fisher information matrix (assumed positive definite).

For **singular models** (like neural networks), W_0 can be a complicated set (not just a point), and the Fisher information matrix degenerates. The KL divergence K(w) is not a non-degenerate quadratic -- it vanishes on a variety with singularities.

### Definition of the RLCT

The **real log canonical threshold** (RLCT), denoted lambda, is defined via resolution of singularities of K(w).

Let pi: Y -> W be a resolution of the zero set of K(w). By Hironaka's theorem, we can choose pi so that:

K(pi(u)) = u_1^{2k_1} * u_2^{2k_2} * ... * u_d^{2k_d} * c(u)

where c(u) > 0 is smooth and positive, and the k_i are non-negative integers (the **multiplicities**).

Similarly, the Jacobian of pi is:

|det(d_pi)| = |u_1^{h_1} * u_2^{h_2} * ... * u_d^{h_d}| * b(u)

where b(u) > 0 is smooth and positive, and h_i are non-negative integers.

The RLCT is:

lambda = min_j {(h_j + 1) / (2 * k_j)}

where the minimum is taken over all j with k_j > 0, and over all coordinate charts of the resolution.

### Watanabe's Free Energy Formula

The central result of SLT is:

**Free energy:** F_n = -log Z_n = lambda * log(n) - (m - 1) * log(log(n)) + O(1)

where:
- Z_n = integral of exp(-n * K(w)) * phi(w) dw (the partition function)
- n is the sample size
- lambda is the RLCT
- m is the multiplicity of lambda (how many components achieve the minimum)
- phi(w) is the prior

**Comparison with regular models:** For a regular model with d parameters, lambda = d/2 and m = 1, recovering the BIC: F_n = (d/2) * log(n) + O(1).

For singular models, lambda < d/2 in general -- the effective complexity is LESS than the parameter count. This is why neural networks generalize better than the parameter count suggests.

### Computing the RLCT: Examples

**Example 1: Regular model.** K(w) = w_1^2 + w_2^2. No singularity to resolve. We can read off k_1 = k_2 = 1, h_1 = h_2 = 0. So lambda = min{(0+1)/(2*1), (0+1)/(2*1)} = 1/2 per parameter. Total: lambda = d/2 = 1.

**Example 2: Redundant parameter.** K(w) = w_1^2 * w_2^2. The zero set is the cross {w_1 = 0} union {w_2 = 0}, which is singular at the origin.

Blowing up at the origin (in the chart w_2 = t * w_1): K = w_1^2 * t^2 * w_1^2 = w_1^4 * t^2. The Jacobian is |w_1|. So:
- From the w_1 factor: k = 2, h = 1, ratio = (1+1)/(2*2) = 1/2
- From the t factor: k = 1, h = 0, ratio = (0+1)/(2*1) = 1/2

lambda = 1/2. But d/2 = 1, so lambda < d/2. The model is "less complex" than parameter counting suggests.

**Example 3: The key SLT example.** K(w) = (w_1 * w_2)^2 where w_1, w_2 are parameters of a reduced rank model. This is exactly Example 2. The singularity at the origin corresponds to parameter degeneracy (both parameters zero gives the same function), and the RLCT captures the effective dimension.

### The RLCT as a Measure of Singularity

The RLCT measures how "singular" the model is at the true parameters:

- lambda = d/2: regular (no singularity), equivalent to parameter counting
- lambda < d/2: singular, the model has symmetries/degeneracies that reduce effective complexity
- Smaller lambda: more singular, lower effective complexity, better generalization (up to a point)

The RLCT depends on:
1. The **structure** of the model (its parameterization)
2. The **true distribution** (which determines where on the parameter space we are)
3. NOT on the sample size or the data (it is a geometric invariant)

---

## Part 5: SLT in Practice

### RLCT for Neural Networks

For neural networks, exact RLCT computation is extremely difficult. Known results include:

- **Reduced-rank regression** (a simple model with matrix factorization): RLCT is known exactly and is strictly less than d/2
- **Two-layer networks with tanh activation:** Partial results exist for small widths
- **General deep networks:** The RLCT is known to be less than d/2, but exact values are open problems

The RLCT depends on the **true function** being learned. A network learning a simple function (realizable by a smaller network) has a smaller RLCT than one learning a complex function.

### Phase Transitions in Learning

As the sample size n grows, the Bayesian posterior concentrates around the set W_0. The RLCT governs this concentration:

- The posterior volume scales as n^{-lambda}
- Model selection via free energy prefers models with smaller lambda (for the same fit)
- This creates **phase transitions**: as n increases, simpler (more singular) representations are preferred

This connects to the phenomenology of deep learning:
- Neural networks often learn simple features first, then complex ones
- Generalization improves despite increasing parameter count (the RLCT stays small)
- Pruning and compression work because the effective dimension is small

### Watanabe's Formula vs. Classical BIC

| | Classical BIC | Watanabe's Formula |
|---|---|---|
| Assumes | Regular model | Any (possibly singular) model |
| Complexity term | (d/2) * log(n) | lambda * log(n) |
| d = | parameter count | RLCT (geometric invariant) |
| Second-order term | O(1) | -(m-1) * log(log(n)) |
| Applies to neural nets? | No (singular) | Yes |

---

## Watch -- Primary

**Aleph 0 -- "What is Algebraic Geometry?"**
An excellent 20-minute overview that builds intuition for varieties, ideals, and the algebra-geometry correspondence. Watch this first.

Link: Search YouTube for "Aleph 0 What is Algebraic Geometry"

## Watch -- Supplement

**3Blue1Brown -- "But what is a convolution?"** (for intuition about algebraic operations, if helpful)

**Seminars and lectures on SLT:**
- Search for "Watanabe Singular Learning Theory lecture" for presentations by Watanabe himself
- Search for "RLCT tutorial" for applied introductions

## Read -- Primary (Textbook)

**Shafarevich, "Basic Algebraic Geometry 1"**
Chapters 1--2 cover affine and projective varieties, singularities, and blowups. This is a standard graduate text -- readable but demanding.

**Watanabe, "Algebraic Geometry and Statistical Learning Theory"**
THE reference for the RLCT and its applications. Read Chapters 1--4 for the theory, Chapter 6 for examples. This book directly connects algebraic geometry to statistical learning.

## Read -- Supplement

**Sumio Watanabe, "Mathematical Theory of Bayesian Statistics"**
A more accessible introduction to SLT with less algebraic geometry prerequisites. Good for understanding the statistical motivation.

**Reid, "Undergraduate Algebraic Geometry"**
A gentle introduction to varieties and singularities, suitable as a warm-up for Shafarevich.

---

## Go Deeper

For those who want to develop serious facility with algebraic geometry beyond what this lesson covers:

**NPTEL Algebraic Geometry course**
A full university-level course available on YouTube via NPTEL (National Programme on Technology Enhanced Learning, India). Covers varieties, schemes, sheaves, and cohomology systematically.

**Harpreet Bedi -- Algebraic Geometry (68 lectures)**
A comprehensive YouTube lecture series covering algebraic geometry from the ground up. Suitable for self-study, with a pace that allows careful note-taking.

Link: Search YouTube for "Harpreet Bedi Algebraic Geometry"

Both of these are substantial commitments (50+ hours each) but will build deep understanding of the algebraic geometry underlying SLT.

---

## Exercises

### Computation Exercises

1. **Varieties and ideals.** For each of the following, sketch the variety and determine whether the origin is singular:
   (a) V(x^2 + y^2 - 1) in R^2
   (b) V(x*y) in R^2
   (c) V(y^2 - x^3) in R^2
   (d) V(y^2 - x^2 - x^3) in R^2 (the nodal cubic)
   (e) V(x^2 + y^2 - z^2) in R^3 (the cone)

2. **Jacobian criterion practice.** For V(f) where f(x,y) = y^2 - x^3 - x^2:
   (a) Compute the gradient (df/dx, df/dy).
   (b) Find all singular points.
   (c) At the singular point, what is the dimension of the tangent "space" (the zero set of the linearized equation)?
   (d) Factor f near the origin to understand the local structure (two branches crossing).

3. **Blowup of the cusp.** For the cusp V(y^2 - x^3):
   (a) Perform the blowup at the origin. In the chart y = t*x, substitute and factor.
   (b) Identify the strict transform and the exceptional divisor.
   (c) Verify the strict transform is smooth.
   (d) Determine the multiplicity of the exceptional divisor.

4. **Blowup of y^2 = x^4.** This is a "worse" singularity than the cusp.
   (a) Perform one blowup at the origin (chart y = t*x). Is the result smooth?
   (b) If not, perform a second blowup. Continue until the strict transform is smooth.
   (c) Record the multiplicities at each step.

5. **RLCT computation.** For K(w) = w_1^2 + w_2^4:
   (a) The zero set is just {(0,0)}. Is this a singularity of K?
   (b) In polar-like coordinates w_1 = r*cos(theta), w_2 = r*sin(theta), express K.
   (c) Compute the RLCT. (Hint: you need to find the minimum of (h+1)/(2k) over appropriate blowup charts. For this simple case, direct computation via the integral Z_n suffices.)
   (d) Compare lambda with d/2 = 1. Is this model singular?

6. **RLCT for a product singularity.** For K(w) = w_1^2 * w_2^2 (the classic SLT example):
   (a) Describe the zero set W_0.
   (b) Perform a blowup at the origin.
   (c) Compute the RLCT (as worked in Part 4).
   (d) Explain why lambda = 1/2 < d/2 = 1 in terms of model redundancy.

### Conceptual Exercises

7. **The algebra-geometry dictionary.**
   (a) What is the ideal I(V) for V = {(1,0), (0,1)} in R^2? (Find polynomials vanishing at both points.)
   (b) Is this ideal prime? Is V irreducible?
   (c) Decompose V into irreducible components and relate to the prime decomposition of I(V).

8. **Singularities in neural networks.**
   (a) Consider a one-hidden-layer network f(x; a, b) = a * tanh(b * x). At (a, b) = (0, b_0) for any b_0, the network outputs zero. Why does this create a singularity?
   (b) At (a, b) = (a_0, 0) for any a_0, the network outputs a_0 * tanh(0) = 0 as well. What does the set W_0 look like when the true function is identically zero?
   (c) Explain intuitively why the RLCT for this model is less than d/2 = 1.

9. **Why resolution of singularities matters for integration.**
   (a) Consider the integral I(n) = integral of exp(-n * w^2) dw over R. Compute it (Gaussian integral).
   (b) Now consider I(n) = integral of exp(-n * w^4) dw over R. Compute the leading behavior as n -> infinity. (Hint: substitute u = n^{1/4} * w.)
   (c) Compare the rates of decay. The exponent in w^4 corresponds to a "more singular" setting. How does this connect to the RLCT?
   (d) For I(n) = integral of exp(-n * w_1^2 * w_2^2) dw_1 dw_2 over [-1,1]^2, explain why direct computation is hard and resolution of singularities (blowup) helps.

### Proof Exercise

10. **RLCT bounds.** Prove: for any analytic function K(w) with K(w) >= 0 and K(0) = 0 on R^d:
    (a) lambda <= d/2 (the RLCT is at most half the dimension).
    (b) lambda >= 1/(2 * ord(K)) where ord(K) is the order of the lowest-degree nonzero term in the Taylor expansion of K at 0.
    (c) Interpret: (a) says singular models are no worse than regular ones; (b) says the RLCT is bounded below by the vanishing order.
