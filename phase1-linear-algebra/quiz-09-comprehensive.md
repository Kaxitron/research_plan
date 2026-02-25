# Quiz: Lessons 7–9 Comprehensive Exam

[← Dot Products](lesson-09-dot-products.md) | [Back to TOC](../README.md) | [Next: Change of Basis →](lesson-10-change-of-basis.md)

---

> **Topics covered:** SVD, Gram-Schmidt process, projection onto a vector, cross product, diagonalization, and projection onto a subspace. 12 questions total. Work through each problem fully — geometric intuition matters as much as getting the right number.

---

## Question 1 — SVD: Geometric Interpretation

Given the SVD decomposition A = UΣVᵀ, describe geometrically what each of the three matrices does to an input vector. A unit circle is fed into A — what shape comes out, and how does Σ determine that shape?

---

## Question 2 — SVD: Low-Rank Approximation

The matrix A has singular values σ₁ = 10, σ₂ = 3, σ₃ = 0.01.

**(a)** What is the rank of A?

**(b)** If you keep only the top 2 singular values (setting σ₃ = 0), what rank is the approximation?

**(c)** Why might this be useful in practice? Give one concrete ML example.

---

## Question 3 — SVD: Computation

Given:

```
A = | 3  0 |
    | 0  2 |
```

**(a)** Compute AᵀA and find its eigenvalues and eigenvectors (these give you V and the squared singular values).

**(b)** What are the singular values of A?

**(c)** This matrix is already diagonal — what does that tell you about U, Σ, and V?

---

## Question 4 — Diagonalization

Given:

```
A = | 4  1 |
    | 2  3 |
```

**(a)** Find the eigenvalues of A.

**(b)** Find the eigenvectors.

**(c)** Write A = PDP⁻¹. What is D?

**(d)** Using your diagonalization, what is A⁵ conceptually? (You don't need to compute the actual numbers — describe the process.)

---

## Question 5 — Projection onto a Vector

Let **u** = [3, 4] and **v** = [1, 0].

**(a)** Compute proj_v(u) — the projection of u onto v.

**(b)** Compute the residual: u − proj_v(u).

**(c)** Verify that the residual is orthogonal to v by computing their dot product.

**(d)** Draw a rough sketch of u, v, the projection, and the residual. What does the residual represent geometrically?

---

## Question 6 — Projection: Attention Connection

In a transformer, a query vector q = [2, 1] and key vector k = [1, 3] are given.

**(a)** Compute the attention score q · k.

**(b)** Compute the cosine similarity between q and k.

**(c)** If a second key k₂ = [−1, 2] exists, compute q · k₂. Which key does the query attend to more strongly?

**(d)** Why does attention use dot products rather than, say, Euclidean distance?

---

## Question 7 — Gram-Schmidt: Two Vectors

Given v₁ = [1, 1] and v₂ = [3, 1]:

**(a)** Normalize v₁ to get e₁.

**(b)** Compute the projection of v₂ onto e₁.

**(c)** Subtract the projection from v₂ to get u₂.

**(d)** Normalize u₂ to get e₂.

**(e)** Verify: e₁ · e₂ = 0, |e₁| = 1, |e₂| = 1.

---

## Question 8 — Gram-Schmidt: Three Vectors

Given v₁ = [1, 0, 1], v₂ = [1, 1, 0], v₃ = [0, 1, 1]:

**(a)** Find e₁ (normalize v₁).

**(b)** Find e₂ (project v₂ onto e₁, subtract, normalize).

**(c)** Find e₃ (project v₃ onto both e₁ and e₂ separately, subtract both, normalize).

**(d)** Verify all three pairwise dot products are zero.

---

## Question 9 — Gram-Schmidt: Why This Direction?

Explain in 2-3 sentences why, in the Gram-Schmidt process, we project the **new** vector onto the **existing** orthonormal vectors (and not the other way around). What would go wrong if you reversed the direction of projection?

---

## Question 10 — Cross Product

Given **a** = [1, 0, 0] and **b** = [0, 1, 0]:

**(a)** Compute a × b.

**(b)** Verify that the result is orthogonal to both a and b.

**(c)** What is the geometric meaning of |a × b|?

**(d)** What happens to a × b if you swap the order (compute b × a)?

---

## Question 11 — Projection onto a Subspace

Let W be the subspace of ℝ³ spanned by the columns of:

```
A = | 1  0 |
    | 1  1 |
    | 0  1 |
```

And let **b** = [1, 2, 3].

**(a)** Compute AᵀA.

**(b)** Compute Aᵀb.

**(c)** Solve the normal equations AᵀA x̂ = Aᵀb to find x̂.

**(d)** Compute the projection p = Ax̂. This is the closest point to b in the subspace W.

**(e)** Compute the error e = b − p. Verify that e is orthogonal to both columns of A (compute Aᵀe and check it equals [0, 0]).

---

## Question 12 — Projection onto a Subspace: Conceptual

**(a)** The projection matrix is P = A(AᵀA)⁻¹Aᵀ. What does the property P² = P mean geometrically?

**(b)** Why is least squares regression the same thing as projection onto a subspace? What is the "subspace" in the context of linear regression, and what is the "vector being projected"?

**(c)** In the context of interpretability, when a researcher trains a "linear probe" on model activations, how does this relate to projection?

---

## Answer Key

*Answers will be reviewed together after completing Lesson 9. Try each problem fully before checking.*

<details>
<summary>Click to reveal answers (try first!)</summary>

### Q1 — SVD Geometric
Vᵀ rotates the input to align with the "natural axes" of the transformation. Σ scales along each axis (stretches/shrinks). U rotates the output to its final orientation. A unit circle becomes an ellipse. The singular values σ₁, σ₂ are the semi-axis lengths of that ellipse.

### Q2 — SVD Low-Rank
**(a)** Rank 3 (all singular values nonzero). **(b)** Rank 2. **(c)** The tiny σ₃ = 0.01 contributes almost nothing — dropping it saves storage/computation with negligible information loss. ML example: LoRA fine-tuning uses low-rank updates ΔW = BA; image compression via truncated SVD; attention heads use rank bottlenecks.

### Q3 — SVD Computation
**(a)** AᵀA = [[9,0],[0,4]]. Eigenvalues: 9 and 4. Eigenvectors: [1,0] and [0,1]. **(b)** Singular values: σ₁ = 3, σ₂ = 2. **(c)** Since A is diagonal, U = I, Σ = A, V = I (the natural axes are already the standard axes — no rotation needed).

### Q4 — Diagonalization
**(a)** det(A − λI) = (4−λ)(3−λ) − 2 = λ² − 7λ + 10 = (λ−5)(λ−2). Eigenvalues: λ₁ = 5, λ₂ = 2. **(b)** For λ=5: [1,1]. For λ=2: [1,−2] (or any scalar multiples). **(c)** D = [[5,0],[0,2]], P = [[1,1],[1,−2]]. **(d)** A⁵ = PD⁵P⁻¹. D⁵ = [[5⁵,0],[0,2⁵]] = [[3125,0],[0,32]]. Convert to eigenbasis, raise eigenvalues to the 5th power, convert back.

### Q5 — Projection onto a Vector
**(a)** proj_v(u) = (u·v / v·v) v = (3/1)[1,0] = [3,0]. **(b)** Residual = [3,4] − [3,0] = [0,4]. **(c)** [0,4] · [1,0] = 0 ✓. **(d)** The residual is the y-component of u — the part of u that has nothing to do with the x-direction.

### Q6 — Attention Connection
**(a)** q·k = 2(1) + 1(3) = 5. **(b)** |q| = √5, |k| = √10. cos(θ) = 5/√50 = 5/(5√2) = 1/√2 ≈ 0.707. **(c)** q·k₂ = 2(−1) + 1(2) = 0. The query attends to k₁ much more (score 5 vs 0). k₂ is orthogonal to q — completely irrelevant. **(d)** Dot products measure directional alignment (similarity), scale efficiently with dimension, and naturally feed into softmax. Euclidean distance measures absolute closeness, which conflates magnitude with direction.

### Q7 — Gram-Schmidt 2D
**(a)** |v₁| = √2. e₁ = [1/√2, 1/√2]. **(b)** v₂·e₁ = 3/√2 + 1/√2 = 4/√2 = 2√2. proj = 2√2 · [1/√2, 1/√2] = [2, 2]. **(c)** u₂ = [3,1] − [2,2] = [1, −1]. **(d)** |u₂| = √2. e₂ = [1/√2, −1/√2]. **(e)** e₁·e₂ = 1/2 − 1/2 = 0 ✓. Both have length 1 ✓.

### Q8 — Gram-Schmidt 3D
**(a)** |v₁| = √2. e₁ = [1/√2, 0, 1/√2].
**(b)** v₂·e₁ = 1/√2. proj = (1/√2)[1/√2, 0, 1/√2] = [1/2, 0, 1/2]. u₂ = [1,1,0] − [1/2,0,1/2] = [1/2, 1, −1/2]. |u₂| = √(1/4+1+1/4) = √(3/2). e₂ = [1/2, 1, −1/2] / √(3/2) = [1/√6, 2/√6, −1/√6].
**(c)** v₃·e₁ = 1/√2. proj₁ = (1/√2)e₁ = [1/2, 0, 1/2]. v₃·e₂ = (0)(1/√6) + (1)(2/√6) + (1)(−1/√6) = 1/√6. proj₂ = (1/√6)e₂ = [1/6, 2/6, −1/6]. u₃ = [0,1,1] − [1/2,0,1/2] − [1/6, 1/3, −1/6] = [−2/3, 2/3, 2/3]. |u₃| = √(4/9+4/9+4/9) = 2√3/3. e₃ = [−1/√3, 1/√3, 1/√3].
**(d)** e₁·e₂ = 0, e₁·e₃ = 0, e₂·e₃ = 0. All verified ✓.

### Q9 — Why This Direction?
The residual from a projection is perpendicular to *whatever you projected onto*. We need the result perpendicular to e₁ (our existing basis), so we must project onto e₁. Reversing the direction would produce a vector perpendicular to v₂ instead, which is useless — we're building orthogonality relative to the basis we've already constructed, not relative to the messy input.

### Q10 — Cross Product
**(a)** a × b = [0·0−0·1, 0·0−1·0, 1·1−0·0] = [0, 0, 1]. **(b)** [0,0,1]·[1,0,0] = 0 ✓. [0,0,1]·[0,1,0] = 0 ✓. **(c)** |a × b| equals the area of the parallelogram formed by a and b. Here it's 1 (unit square in the xy-plane). **(d)** b × a = [0, 0, −1] — same magnitude, opposite direction. Cross product is anti-commutative: a × b = −(b × a).

### Q11 — Projection onto Subspace
**(a)** AᵀA = [[2,1],[1,2]]. **(b)** Aᵀb = [3, 5]. **(c)** Solve [[2,1],[1,2]]x̂ = [3,5]. det = 3. x̂ = (1/3)[[2,−1],[−1,2]][3,5] = (1/3)[1,7] = [1/3, 7/3]. **(d)** p = Ax̂ = [1/3, 1/3+7/3, 7/3] = [1/3, 8/3, 7/3]. **(e)** e = [1,2,3] − [1/3,8/3,7/3] = [2/3, −2/3, 2/3]. Aᵀe = [2/3−2/3, −2/3+2/3] = [0, 0] ✓.

### Q12 — Conceptual
**(a)** P² = P means projecting twice does nothing new. Once a vector is in the subspace, projecting again leaves it unchanged — it's already there. **(b)** In linear regression, the columns of the design matrix X span a subspace. The target vector y is generally not in this subspace. Least squares finds the closest point in the subspace to y — that's projection. The "subspace" is all possible predictions Xβ; the vector being projected is y. **(c)** A linear probe's weight vector defines a direction in activation space. The dot product of an activation with this direction is a projection — extracting the component of the activation along the "feature direction." The probe finds the direction where projection best predicts the property of interest.

</details>

---

*Quiz designed for Lesson 9 of the AI Alignment Research Curriculum.*
