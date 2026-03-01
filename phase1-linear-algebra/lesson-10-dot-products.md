# Lesson 10: Dot Products, Orthogonality, and Projections

[← SVD](lesson-09-svd.md) | [Back to TOC](../README.md) | [Next: Change of Basis and Norms →](lesson-11-change-of-basis.md)

---

> **Why this lesson exists:** The dot product is the single most-used operation in transformers. Every attention score is a dot product. Every cosine similarity in embedding space is a dot product. Every projection onto a subspace uses dot products. Despite appearing mechanically in earlier lessons, it deserves its own deep treatment because the *geometric meaning* of the dot product — similarity, projection, decomposition — is what makes attention interpretable.

## 🎯 Core Concepts

- **Dot product: two views that are secretly the same thing**
  - Algebraic: a · b = a₁b₁ + a₂b₂ + ... + aₙbₙ (sum of component-wise products)
  - Geometric: a · b = |a||b|cos(θ) — it measures *how much two vectors point in the same direction*
  - The fact that these two formulas give the same number is not obvious. It's a theorem. 3B1B's duality video explains *why.*

- **Dot product as projection:** a · b = |a| × (length of b's shadow onto a). One vector "asks a question" and the other provides the answer through its shadow.

- **Sign tells you alignment:**
  - a · b > 0 → vectors point roughly the same direction (angle < 90°)
  - a · b = 0 → perpendicular (angle = 90°)
  - a · b < 0 → vectors point roughly opposite (angle > 90°)

- **Cosine similarity:** normalize both vectors first, then dot. cos(θ) = â · b̂. Strips out magnitude, measures only direction. This is THE similarity measure in embedding spaces.

- **Orthogonality:** a · b = 0 means the vectors are perpendicular. No shadow. Completely independent directions. This is the mathematical formalization of "these two things have nothing to do with each other."

- **Orthonormal basis:** a set of basis vectors that are all unit length AND mutually perpendicular. The standard basis {î, ĵ, k̂} is one, but there are infinitely many others. Orthonormal bases are "nice" because dot products with basis vectors directly give you coordinates.

- **Orthogonal matrices:** Q where QᵀQ = I (equivalently, Q⁻¹ = Qᵀ). These are *pure rotations* (and reflections). They preserve lengths and angles — no stretching, no squishing. SVD's U and V are orthogonal matrices.

- **Projection onto a vector:** proj_v(u) = (u · v / v · v) v — extracts the component of u in the v direction. The "residual" u - proj_v(u) is perpendicular to v. You've decomposed u into "the part along v" and "the part perpendicular to v."

- **Projection onto a subspace:** given a subspace W spanned by columns of A, the projection of b onto W is: proj_W(b) = A(AᵀA)⁻¹Aᵀb. The matrix P = A(AᵀA)⁻¹Aᵀ is the **projection matrix**. It's idempotent: P² = P (projecting twice does nothing new).

- **Least squares:** when Ax = b has no exact solution (more equations than unknowns), the "best" solution minimizes ||Ax - b||². This minimum occurs at x̂ = (AᵀA)⁻¹Aᵀb — which is exactly the projection formula. Least squares IS projection.

- **Gram-Schmidt process:** a recipe for converting any basis into an orthonormal one. Start with one vector, normalize it. Take the next vector, subtract its projection onto the first, normalize. Repeat. Each step removes the "already covered" directions, leaving only the new perpendicular component.

## 📺 Watch — Primary

1. **3Blue1Brown — "Dot products and duality" (Ch. 9)**
   - https://www.youtube.com/watch?v=LyGKycYT2v0
   - *The insight that a dot product is secretly a 1×n matrix transformation is stunning and ties everything back to Lesson 4. A 1×2 row vector [a, b] acting on a column vector [x, y] gives ax + by — that's a dot product AND a linear transformation from ℝ² to ℝ¹. Duality!*

## 📺 Watch — Secondary

2. **MIT OCW — Strang, Lecture 15: "Projections onto Subspaces"**
   - https://www.youtube.com/watch?v=Y_Ac6KiQ1t0
   - Strang derives the projection matrix P = A(AᵀA)⁻¹Aᵀ, which is the mathematical core of least squares regression.
3. **MIT OCW — Strang, Lecture 16: "Projection Matrices and Least Squares"**
   - https://www.youtube.com/watch?v=osh80YCg_GM
   - The least squares derivation — beautiful connection between geometry and optimization.
4. **MIT OCW — Strang, Lecture 17: "Orthogonal Matrices and Gram-Schmidt"**
   - https://www.youtube.com/watch?v=0MtwqhIwdrI
   - Gram-Schmidt → QR decomposition, another way to decompose any matrix.
   - Good for worked numerical examples

## 📖 Read — Primary

- **MML Book, Chapter 3.1–3.4** (analytic geometry: norms, inner products, lengths, angles, orthogonal projections)
  - This IS the dot product chapter of the ML bible. Formal and precise.
- **MML Book, Chapter 3.5–3.8** (orthonormal bases, orthogonal complement, projections onto general subspaces)

## 📖 Read — Secondary

- **Interactive Linear Algebra (GT), Chapter 6.3–6.4** — orthogonal projections with interactive demos
- **"Immersive Linear Algebra," Chapter 9** — dot products with 3D interactive visuals
- **BetterExplained — "Vector Calculus: Understanding the Dot Product"**
  - https://betterexplained.com/articles/vector-calculus-understanding-the-dot-product/
- **MML Book, Chapter 9.1–9.2** (linear regression as projection) — preview of how least squares connects to ML

## 🔨 Do

- **Cosine similarity in practice:** In Python, load pre-trained word vectors (GloVe or Word2Vec). Compute cosine similarity between word pairs: (king, queen), (king, banana), (cat, dog). See the dot product measuring semantic similarity.
- **Projection exercise:** Given a vector and a plane (defined by two vectors in ℝ³), project the vector onto the plane. Visualize the original vector, the projection, and the perpendicular residual.
- **Gram-Schmidt:** Implement Gram-Schmidt on 3 vectors in ℝ³. Verify the result is orthonormal: all pairwise dot products = 0, all lengths = 1.
- **Projection matrix:** For a 2D subspace in ℝ³ (defined by matrix A), compute P = A(AᵀA)⁻¹Aᵀ. Verify P² = P. Apply it to several vectors and see they all land in the plane.
- **Key exercise:** Take two non-orthogonal vectors in ℝ². Compute their dot product. Rotate one until the dot product is zero. Verify cos(θ) = 0 matches.

## 🔗 ML & Alignment Connection

The dot product is the **atomic operation of attention.** Here's exactly how:

1. Each token produces a query vector q = xW_Q and a key vector k = xW_K
2. The attention score is q · k (dot product) — "how relevant is key k to query q?"
3. Scores go through softmax to become weights (a probability distribution over positions)
4. The output is a weighted sum of value vectors — a **linear combination** (Lesson 2!) weighted by attention scores

So attention = dot products (this lesson) → softmax → linear combinations (Lesson 3). You now understand every piece.

**Cosine similarity** is how embedding search works. When you search "king - man + woman" and find "queen," you're finding the vector with highest cosine similarity to your query.

**Orthogonality and superposition:** If all feature directions in a neural network were orthogonal, there'd be no interference between features. But in a 768-dimensional residual stream, a model might want to represent 10,000+ features. You can't fit 10,000 orthogonal vectors in 768 dimensions. So features are *almost* orthogonal, and the interference between non-orthogonal directions creates superposition.

**Projections and probing:** When interpretability researchers train a "linear probe" to predict some property (e.g., part of speech) from activations, they're finding a projection direction. The probe's weight vector defines a direction in activation space, and the dot product of an activation with this direction gives the prediction.

When Anthropic's sparse autoencoder work decomposes model activations into interpretable features, they're looking for a set of *approximately orthogonal* directions in activation space. The better separated (more orthogonal) the features, the more interpretable the model. The entire research program of "finding features" is asking: what are the natural near-orthogonal directions in this high-dimensional space?

The **projection** interpretation also connects to the "residual stream" view of transformers: each attention head and MLP layer *reads* from the residual stream (via projection/dot products) and *writes* back to it (via addition). Understanding projection as "extracting the component of a vector along a direction" is literally what reading from the residual stream means.