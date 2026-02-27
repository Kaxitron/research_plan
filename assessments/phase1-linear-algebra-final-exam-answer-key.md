# Phase 1: Linear Algebra Final Examination — Answer Key

**The Path to AI Alignment — Lessons 2–10 Comprehensive Assessment**

---

> **Grading philosophy:** Partial credit is generous for correct reasoning with arithmetic errors. Geometric explanations alongside algebra earn full marks. The goal is demonstrating understanding, not perfect computation.

---

## Part A: Geometric Intuition & Conceptual Understanding (20 points)

---

### Question 1 (5 pts)

**(a)** |det(A)| = **3**, since the determinant measures the factor by which the transformation scales area, and the parallelogram has 3× the area of the unit square.

The **sign** of det(A) tells you whether the transformation **preserves or reverses orientation**. Positive means the "handedness" of space is preserved (counterclockwise stays counterclockwise). Negative means it's flipped — like a mirror reflection.

**(b)** The determinant equals the **product of eigenvalues**: det(A) = λ₁ · λ₂.

We know |det(A)| = 3 and λ₁ = 2, so:

- If det(A) = +3: λ₂ = 3/2 = **1.5**
- If det(A) = −3: λ₂ = −3/2 = **−1.5**

Either answer is acceptable since we only know |det(A)| = 3. The negative case would mean the transformation includes a reflection.

**(c)** A vector pointing in [1, 1] **stays on its line** — it just gets stretched to twice its length (scaled by λ₁ = 2). That's what being an eigenvector means. A generic vector like [1, 0] gets **both rotated and scaled** — it gets knocked off its original line, landing somewhere new in the plane. Only eigenvector directions have the special property of staying put (up to scaling).

---

### Question 2 (6 pts) — 1 point each

**(a) TRUE.** Rank 2 means the column space is 2-dimensional. A 2D subspace of ℝ³ is a plane through the origin. Every vector in ℝ³ gets mapped onto this plane — the transformation "flattens" one dimension away.

**(b) FALSE.** det(A) = 0 means Ax = b has no solution **for some** b (those outside the column space), but it does have solutions for b vectors that lie in the column space. For example, Ax = 0 always has a solution (the zero vector, plus the entire null space).

**(c) FALSE.** The null space of A and the **row space** of A are orthogonal (they're orthogonal complements in ℝⁿ). The column space lives in a different space (ℝᵐ) than the null space (ℝⁿ) when A is not square, so the statement doesn't even make sense in general. For square matrices, the null space is orthogonal to the row space, not the column space (though for symmetric matrices these coincide).

**(d) TRUE.** If u · v = 0 and both are nonzero, then neither can be a scalar multiple of the other (if v = cu, then u · v = c||u||² = 0, which forces c = 0, meaning v = 0, contradiction). So they must be linearly independent.

*Note: If either vector is the zero vector, the dot product is trivially zero but the zero vector is never linearly independent with anything. The question implicitly assumes nonzero vectors. Full credit for noting this edge case.*

**(e) FALSE.** A matrix must have n linearly independent eigenvectors to be diagonalizable. Some matrices don't — for example, the matrix [[0, 1], [0, 0]] has only eigenvalue 0 with geometric multiplicity 1, so it has only one independent eigenvector. It cannot be diagonalized. Rotation matrices in 2D also can't be diagonalized over the reals (their eigenvalues are complex).

**(f) TRUE.** Singular values are defined as the square roots of the eigenvalues of AᵀA. Since AᵀA is positive semi-definite (all eigenvalues ≥ 0), taking square roots gives σᵢ ≥ 0 always. Eigenvalues, on the other hand, can be negative (e.g., a reflection matrix has eigenvalue −1), zero, or even complex.

---

### Question 3 (5 pts)

**(a)** The unit circle maps to an **ellipse** with semi-major axis length **σ₁ = 5** and semi-minor axis length **σ₂ = 2**. The ellipse has dimensions 10 × 4 (diameter).

This is THE core geometric picture of SVD: any linear transformation turns circles into ellipses, and the singular values are the axis lengths.

**(b)** The three steps:

1. **Vᵀ (rotate/reflect the input):** Aligns the unit circle with the "natural input axes" of the transformation. The circle is still a circle — Vᵀ is an orthogonal matrix, so it preserves shapes. It just rotates the coordinate system to the one where the transformation acts most simply.

2. **Σ (scale):** Stretches the circle into an ellipse by scaling by σ₁ = 5 along one axis and σ₂ = 2 along the other. This is the only step that changes the shape. The singular values determine how much stretching happens in each direction.

3. **U (rotate/reflect the output):** Rotates the ellipse to its final orientation in the output space. Again, shape is preserved — U just positions the ellipse where it belongs.

Summary: **rotate → stretch into ellipse → rotate to final position.**

**(c)** The best rank-1 approximation is:

**A₁ = σ₁ · u₁ · v₁ᵀ**

where u₁ is the first column of U and v₁ is the first column of V. This keeps only the largest singular value and its associated directions.

Energy captured: σ₁² / (σ₁² + σ₂²) = 25 / (25 + 4) = **25/29 ≈ 86.2%**

The rank-1 approximation captures about 86% of the matrix's "energy," meaning the dominant stretching direction accounts for the vast majority of what this transformation does.

---

### Question 4 (4 pts)

**(a)** We need to find scalars c₁, c₂ such that:

c₁[1, 1] + c₂[1, −1] = [3, 1]

This gives the system:
- c₁ + c₂ = 3
- c₁ − c₂ = 1

Adding: 2c₁ = 4, so c₁ = 2. Subtracting: 2c₂ = 2, so c₂ = 1.

The coordinates of v in basis B₂ are **(2, 1)**.

Verification: 2·[1,1] + 1·[1,−1] = [2,2] + [1,−1] = [3, 1] ✓

**(b)** Coordinates are just "instructions for how to combine basis vectors to reach a point." Changing the basis is like changing measurement units — the same physical height is "6 feet" in imperial and "1.83 meters" in metric. The vector (the arrow in space) doesn't change, but the numbers describing it change because the reference frame changed. Different bases are different coordinate systems for the same space.

---

## Part B: Core Computation (30 points)

---

### Question 5 (4 pts)

**A = [[2, 1], [0, 3]], v = [4, 2]**

**(a) Row dot-product view:**

- Row 1 · v = [2, 1] · [4, 2] = 2(4) + 1(2) = 8 + 2 = **10**
- Row 2 · v = [0, 3] · [4, 2] = 0(4) + 3(2) = 0 + 6 = **6**

Result: **Av = [10, 6]**

**(b) Column linear-combination view:**

Av = 4 · [2, 0] + 2 · [1, 3] = [8, 0] + [2, 6] = **[10, 6]**

(The output is: "4 copies of column 1 plus 2 copies of column 2.")

**(c)** Both give [10, 6]. ✓

The **column view** is more useful for interpreting attention heads. When an attention head computes a weighted sum of value vectors, it's forming a linear combination of the columns of the value matrix, weighted by the attention scores. The column view directly shows you: "what directions are being combined, and with what weights?" Each column is a "thing being selected," and the weights choose how much of each thing to include.

---

### Question 6 (8 pts)

**A = [[4, 2], [1, 3]]**

**(a) Eigenvalues:**

det(A − λI) = det([[4−λ, 2], [1, 3−λ]]) = (4−λ)(3−λ) − (2)(1)

= 12 − 4λ − 3λ + λ² − 2

= λ² − 7λ + 10 = 0

Factoring: (λ − 5)(λ − 2) = 0

**λ₁ = 5, λ₂ = 2**

*Quick check via trace/det shortcut: trace = 4 + 3 = 7 = 5 + 2 ✓, det = 12 − 2 = 10 = 5 × 2 ✓*

**(b) Eigenvectors:**

**For λ₁ = 5:** Solve (A − 5I)v = 0:

```
[[-1, 2], [1, -2]] v = 0
```

Row 1: −v₁ + 2v₂ = 0 → v₁ = 2v₂

Choose v₂ = 1: **v₁ = [2, 1]**

**For λ₂ = 2:** Solve (A − 2I)v = 0:

```
[[2, 2], [1, 1]] v = 0
```

Row 1: 2v₁ + 2v₂ = 0 → v₁ = −v₂

Choose v₂ = −1: **v₂ = [1, −1]**

**(c) Verification:**

- Av₁ = [[4,2],[1,3]] · [2,1] = [8+2, 2+3] = [10, 5] = 5 · [2, 1] ✓
- Av₂ = [[4,2],[1,3]] · [1,−1] = [4−2, 1−3] = [2, −2] = 2 · [1, −1] ✓

**(d) Diagonalization:**

P = [[2, 1], [1, −1]] (eigenvectors as columns)

D = [[5, 0], [0, 2]] (eigenvalues on diagonal)

**A = PDP⁻¹**

Geometrically, P represents the **change of basis to the eigenbasis**. In the eigenbasis, the transformation is trivially simple — just scaling by 5 in one direction and 2 in the other. P⁻¹ converts a vector to eigenbasis coordinates, D scales each eigendirection independently, and P converts back to standard coordinates.

---

### Question 7 (4 pts)

**M = [[1, 2, 3], [0, k, 4], [0, 0, 2]]**

**(a)** M is upper triangular, so the determinant is the product of diagonal entries:

**det(M) = 1 · k · 2 = 2k**

**(b)** M is not invertible when det(M) = 0:

2k = 0 → **k = 0**

Geometrically, when k = 0, the matrix squishes 3D space down to a lower-dimensional subspace. Specifically, the rank drops from 3 to 2 (the second column becomes [2, 0, 0] + something dependent on the other columns), so 3D space gets flattened onto a 2D plane. One entire dimension of information is destroyed.

---

### Question 8 (6 pts)

**A = [[1, 2, 1], [2, 4, 3], [3, 6, 4]]**

**(a) Row reduction:**

R2 → R2 − 2R1: [[1, 2, 1], [0, 0, 1], [3, 6, 4]]

R3 → R3 − 3R1: [[1, 2, 1], [0, 0, 1], [0, 0, 1]]

R3 → R3 − R2: [[1, 2, 1], [0, 0, 1], [0, 0, 0]]

**Echelon form: [[1, 2, 1], [0, 0, 1], [0, 0, 0]]**

**(b) Rank = 2** (two pivots, in columns 1 and 3).

**(c) Null space:** Solve Ax = 0 using the echelon form.

From row 2: x₃ = 0

From row 1: x₁ + 2x₂ + x₃ = 0 → x₁ = −2x₂

x₂ is a free variable. Set x₂ = 1:

**Null space basis: {[−2, 1, 0]}**

This means any scalar multiple of [−2, 1, 0] gets sent to zero by A.

**(d) Rank-nullity verification:**

rank + nullity = 2 + 1 = 3 = number of columns ✓

---

### Question 9 (4 pts)

**u = [3, 4], v = [1, 0]**

**(a) Projection of u onto v:**

proj_v(u) = (u · v / v · v) · v = (3·1 + 4·0) / (1·1 + 0·0) · [1, 0] = 3/1 · [1, 0] = **[3, 0]**

Residual: u − proj_v(u) = [3, 4] − [3, 0] = **[0, 4]**

Geometric meaning: The residual is the component of u that is **perpendicular to v**. We've decomposed u into "the part along v" ([3, 0]) and "the part perpendicular to v" ([0, 4]). These two parts are orthogonal and sum back to u.

Check: [3, 0] · [0, 4] = 0 ✓ (indeed perpendicular)

**(b) Cosine similarity between u = [3, 4] and w = [2, −1]:**

u · w = 3(2) + 4(−1) = 6 − 4 = 2

||u|| = √(9 + 16) = √25 = 5

||w|| = √(4 + 1) = √5

cos(θ) = (u · w) / (||u|| · ||w||) = 2 / (5√5) = 2 / (5 · 2.236) ≈ 2 / 11.18 ≈ **0.179**

Since cos(θ) ≈ 0.179 is positive but close to zero, these vectors are **more different than similar**. They point in vaguely the same half of the plane (positive cosine → angle < 90°), but they're far from aligned. In embedding space terms, these would represent concepts with only a weak relationship.

---

### Question 10 (4 pts)

**x = [3, −4]**

**(a)**

- ||x||₁ = |3| + |−4| = 3 + 4 = **7** (Manhattan distance)
- ||x||₂ = √(3² + (−4)²) = √(9 + 16) = √25 = **5** (Euclidean distance)
- ||x||∞ = max(|3|, |−4|) = max(3, 4) = **4** (largest component)

**(b)** The general inequality is:

**||x||∞ ≤ ||x||₂ ≤ ||x||₁**

L∞ is always the smallest (it only looks at the biggest component, ignoring all others). L1 is always the largest (it sums all absolute values, giving no "discount" for combining components like L2 does with the Pythagorean theorem).

In this example: 4 ≤ 5 ≤ 7 ✓

---

## Part C: Proofs & Reasoning (20 points)

---

### Question 11 (8 pts)

**(a) Prove (AᵀA)ᵀ = AᵀA:**

Using the transpose reversal rule: (AB)ᵀ = BᵀAᵀ:

(AᵀA)ᵀ = Aᵀ(Aᵀ)ᵀ = AᵀA ∎

(Since (Aᵀ)ᵀ = A, which then reverses back.)

**(b) Prove xᵀ(AᵀA)x ≥ 0 for all x:**

The key trick is recognizing that xᵀAᵀ = (Ax)ᵀ. So:

xᵀ(AᵀA)x = (Ax)ᵀ(Ax) = ||Ax||²₂ ≥ 0 ∎

This is a squared Euclidean norm, which is always non-negative. The result is a sum of squares: if Ax = [y₁, y₂, ..., yₘ], then xᵀAᵀAx = y₁² + y₂² + ... + yₘ² ≥ 0.

**(c)** AᵀA is strictly positive definite (all eigenvalues > 0) when **A has full column rank** (i.e., the columns of A are linearly independent, equivalently rank(A) = n where A is m×n).

Reason: if A has full column rank, then Ax = 0 only for x = 0 (the null space is trivial). So ||Ax||² > 0 for all nonzero x, making xᵀAᵀAx > 0 for all nonzero x — the definition of positive definite. If A doesn't have full column rank, there exists a nonzero x in the null space where Ax = 0, giving xᵀAᵀAx = 0, so we'd only get PSD, not PD.

---

### Question 12 (6 pts)

**A is 5×4 with rank 3.**

**(a)** By rank-nullity: nullity = (# columns) − rank = 4 − 3 = **1**

The null space is 1-dimensional (a line through the origin in ℝ⁴).

**(b)** The dimension of the column space equals the rank = **3**

The column space is a 3-dimensional subspace of ℝ⁵.

**(c) No.** The column space is 3-dimensional within ℝ⁵, so Ax = b only has solutions when b lies in this 3D subspace. Since ℝ⁵ is 5-dimensional, most vectors b will not be in the column space. You would need rank = 5 (full row rank) for Ax = b to have a solution for every b ∈ ℝ⁵, but rank ≤ min(5, 4) = 4, and here rank = 3.

**(d) No, solutions are not unique.** When a solution exists, there is a 1-dimensional family of solutions. If x₀ is one solution (Ax₀ = b), then x₀ + n is also a solution for any n in the null space, since A(x₀ + n) = Ax₀ + An = b + 0 = b. Since the null space is 1-dimensional, the full solution set is a line: {x₀ + tn : t ∈ ℝ}, where n is the null space basis vector.

---

### Question 13 (6 pts)

**P = A(AᵀA)⁻¹Aᵀ**

**(a) Prove P² = P:**

P² = [A(AᵀA)⁻¹Aᵀ] · [A(AᵀA)⁻¹Aᵀ]

Group the middle terms:

= A(AᵀA)⁻¹ · [AᵀA] · (AᵀA)⁻¹Aᵀ

The [AᵀA] and (AᵀA)⁻¹ cancel:

= A(AᵀA)⁻¹ · I · Aᵀ

= A(AᵀA)⁻¹Aᵀ

= P ∎

**(b)** Projecting twice should give the same result as projecting once because the **first projection already lands you on the subspace**. Once you're already on the plane, projecting again onto the same plane doesn't move you — you're already there. It's like casting a shadow onto the floor: the shadow is already on the floor, so casting its shadow again doesn't change it.

---

## Part D: Synthesis & Connections (15 points)

---

### Question 14 (7 pts)

**S = [[5, 2], [2, 5]]**

**(a) Eigenvalues:**

det(S − λI) = (5−λ)² − 4 = λ² − 10λ + 25 − 4 = λ² − 10λ + 21 = 0

(λ − 7)(λ − 3) = 0

**λ₁ = 7, λ₂ = 3**

**(b) Determinant two ways:**

(i) Formula: det(S) = 5·5 − 2·2 = 25 − 4 = **21**

(ii) Product of eigenvalues: 7 × 3 = **21** ✓

**(c)** Because S is symmetric, its eigenvectors are **orthogonal** (perpendicular to each other).

For λ₁ = 7: (S − 7I)v = [[-2, 2], [2, -2]]v = 0 → v₁ = v₂ → **v₁ = [1, 1]**

For λ₂ = 3: (S − 3I)v = [[2, 2], [2, 2]]v = 0 → v₁ = −v₂ → **v₂ = [1, −1]**

Verification: v₁ · v₂ = 1(1) + 1(−1) = 0 ✓ (orthogonal)

This is guaranteed by the **Spectral Theorem**: symmetric matrices always have orthogonal eigenvectors and real eigenvalues.

**(d)** Normalized eigenvectors: q₁ = [1/√2, 1/√2], q₂ = [1/√2, −1/√2]

S = QΛQᵀ where:

Q = (1/√2)[[1, 1], [1, −1]], Λ = [[7, 0], [0, 3]]

For a symmetric matrix, the SVD and eigendecomposition are closely related:

- Since eigenvalues are positive (7 > 0, 3 > 0), the singular values equal the eigenvalues: σ₁ = 7, σ₂ = 3
- **U = Q, Σ = Λ, V = Q** (so Vᵀ = Qᵀ)
- S = UΣVᵀ = QΛQᵀ — they're the same decomposition!

For symmetric PSD matrices, SVD and eigendecomposition coincide. For general matrices (non-symmetric, rectangular), they differ: SVD always works but eigendecomposition may not exist or may have complex values.

**(e)** S is **positive definite** because both eigenvalues are strictly positive (7 > 0, 3 > 0).

This means the quadratic form xᵀSx > 0 for all nonzero x. Geometrically, the surface z = xᵀSx is a **bowl shape** (paraboloid opening upward) — it has a single global minimum at x = 0. This is exactly the condition you want at a minimum of a loss function: the Hessian being positive definite at a critical point confirms it's a local minimum, not a saddle point.

---

### Question 15 (8 pts)

**A = [[1, 2], [2, 4], [0, 0]]**

**(a)** The column space is spanned by the columns: [1, 2, 0] and [2, 4, 0]. But column 2 = 2 × column 1, so they're linearly dependent.

The column space is the **line** spanned by [1, 2, 0] in ℝ³. Geometrically, this is a 1-dimensional subspace — a line through the origin in the x₁-x₂ plane (the x₃ = 0 plane), pointing in the [1, 2, 0] direction.

**(b) Rank = 1** (only one independent column).

**(c)** Solve Ax = 0. Row reduce: R2 → R2 − 2R1:

[[1, 2], [0, 0], [0, 0]]

From row 1: x₁ + 2x₂ = 0 → x₁ = −2x₂

x₂ is free. Set x₂ = 1: x₁ = −2.

**Null space basis: {[−2, 1]}**

Rank-nullity check: 1 + 1 = 2 = # columns ✓

**(d)** AᵀA = [[1,2,0],[2,4,0]] · [[1,2],[2,4],[0,0]] = [[1+4+0, 2+8+0],[2+8+0, 4+16+0]] = **[[5, 10], [10, 20]]**

det(AᵀA) = 5(20) − 10(10) = 100 − 100 = **0**

Since det(AᵀA) = 0, AᵀA is **not invertible**. This makes sense: A doesn't have full column rank (rank 1 < 2 columns), so by Question 11(c), AᵀA is only PSD, not PD — it has a zero eigenvalue.

**(e)** A has **1 non-zero singular value**.

The number of non-zero singular values equals the rank of the matrix, which is 1. Geometrically, this means the transformation collapses 2D input space onto a 1D line — there's only one "stretching direction" that matters. The second singular value is zero, confirming that one entire input dimension gets crushed to nothing.

---

## Part E: ML & Alignment Applications (15 points)

---

### Question 16 (5 pts)

**(a)** A high attention score q · k means the query and key vectors **point in similar directions** in the projected space. Since q · k = ||q|| · ||k|| · cos(θ), a large value means the angle θ between them is small — they're nearly aligned. Intuitively, the query is "asking a question" and the key is "offering a match." A high dot product means the key is highly relevant to what the query is looking for. After softmax, this token will receive a large attention weight, meaning its value vector contributes strongly to the output.

**(b)** The rank bottleneck (768 → 64 → dot product) means the attention head can only compare tokens along **at most 64 dimensions** out of 768. The matrices W_Q and W_K project the full 768-dimensional representation down to a 64-dimensional subspace before computing the dot product. This forces the head to be selective: it can only "care about" information that lives in those 64 projected dimensions. Different heads learn different 64-dimensional projections, each attending to different types of relationships (syntax, semantics, position, etc.). The rank constraint is what makes each head specialized rather than trying to capture everything at once.

---

### Question 17 (5 pts)

**(a)** In ℝ³, you can have at most **3** mutually orthogonal vectors (that's the dimension). But if you relax to "almost orthogonal" (small but nonzero pairwise dot products), you can fit **many more** directions. In high dimensions this becomes even more dramatic — in ℝ⁷⁶⁸, you can fit far more than 768 approximately-orthogonal directions because the geometry of high-dimensional spaces is surprisingly "roomy." This is the mathematical basis for **superposition**: a 768-dimensional residual stream can encode thousands of features as nearly-orthogonal directions, even though there are only 768 "slots" for truly orthogonal vectors.

**(b)** When f₁ and f₂ are not perfectly orthogonal, projecting the activation vector a onto f₁ gives:

proj_{f₁}(a) = (a · f₁ / ||f₁||²) which includes a contribution from f₂'s component:

Since a might contain both features (a ≈ α₁f₁ + α₂f₂ + ...), the projection onto f₁ picks up not just α₁ but also a "cross-talk" term α₂(f₂ · f₁)/||f₁||². If f₁ ⊥ f₂, this cross-talk is zero. But if they're not orthogonal, reading f₁ gives you a "bleed" of f₂'s activation. This is **interference** — the features are entangled. The model has to tolerate this noise as the cost of encoding more features than dimensions. The more features crammed in, the less orthogonal they can be, and the more interference occurs.

---

### Question 18 (5 pts)

**(a)** The sparse autoencoder performs a **change of basis**. The "old coordinates" are the **neuron basis** — each coordinate is one neuron's activation value. The "new coordinates" are the **feature basis** — each coordinate represents the activation strength of a human-interpretable concept (like "code," "French text," "deception"). The autoencoder's encoder matrix is the change-of-basis matrix that transforms from neuron coordinates to feature coordinates, and the decoder matrix transforms back. The key insight is that the features are more interpretable than the neurons, even though they describe the exact same underlying activation vectors.

**(b)** The eigenbasis reveals axes where a matrix transformation becomes **trivially simple** — just independent scaling along each direction, with no mixing between dimensions. The feature basis is trying to find analogous axes for neural network *representations*: directions where each coordinate has a **clean, independent, interpretable meaning**. In the neuron basis, activations are dense mixtures of many concepts (polysemantic). In the feature basis, each coordinate ideally corresponds to one concept (monosemantic). Just as diagonalization reveals the "natural axes" of a transformation, sparse autoencoders seek the "natural axes" of the representation space.

**(c)** LoRA assumes that the **change in weights during fine-tuning lives in a low-rank subspace**. Instead of updating all n² entries of a weight matrix, LoRA parameterizes the update as ΔW = BA where B is n×r and A is r×n, with r << n. This is equivalent to constraining ΔW to have at most rank r.

The SVD connection: any rank-r matrix can be written as Σᵢ σᵢuᵢvᵢᵀ (the top r terms of an SVD). LoRA is implicitly assuming that fine-tuning only needs to adjust the weight matrix along a few important directions (r of them), leaving the vast majority of the matrix's structure intact. This works because fine-tuning for a specific task typically requires learning a small number of new "features" or adjustments, not rewriting the entire transformation — the knowledge from pretraining is mostly preserved.

---

## Grading Summary

| Section | Topic | Points |
|---------|-------|--------|
| Part A | Geometric Intuition & Conceptual Understanding | /20 |
| Part B | Core Computation | /30 |
| Part C | Proofs & Reasoning | /20 |
| Part D | Synthesis & Connections | /15 |
| Part E | ML & Alignment Applications | /15 |
| **Total** | | **/100** |

| Grade | Range | Meaning |
|-------|-------|---------|
| A | 90–100 | Deep geometric intuition + solid computation. Ready for calculus. |
| B | 75–89 | Good understanding with some gaps. Review weak areas, then proceed. |
| C | 60–74 | Foundations present but need strengthening. Revisit key lessons before moving on. |
| Below 60 | <60 | Significant review needed. Re-watch 3B1B, redo exercises for weak sections. |

---

*"Every matrix transformation = align input with natural directions → scale each direction independently → align output with natural directions. This is SVD. Every other concept is a window into part of this story."*
