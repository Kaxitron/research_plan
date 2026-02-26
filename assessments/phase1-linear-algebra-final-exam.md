# Phase 1: Linear Algebra Final Examination

**The Path to AI Alignment — Lessons 1–10 Comprehensive Assessment**

---

| | |
|---|---|
| **Time Allowed** | 60 minutes |
| **Total Points** | 100 |
| **Materials** | Pencil, paper, calculator (no CAS). No code. |
| **Format** | 5 sections covering all Phase 1 concepts |

| Section | Topic | Points |
|---------|-------|--------|
| Part A | Geometric Intuition & Conceptual Understanding | 20 |
| Part B | Core Computation | 30 |
| Part C | Proofs & Reasoning | 20 |
| Part D | Synthesis & Connections | 15 |
| Part E | ML & Alignment Applications | 15 |

> **Advice:** Show all work. Partial credit is awarded generously for correct reasoning even with arithmetic errors. Geometric explanations are encouraged alongside algebraic work.

> *"Any matrix transformation = align input with natural directions → scale → align output. This is SVD. Every other concept is a window into part of this story."*

---

## Part A: Geometric Intuition & Conceptual Understanding (20 points)

*Test your ability to SEE what linear algebra does. No computation required — draw, explain, reason geometrically.*

### Question 1 (5 pts)

A 2×2 matrix A transforms the unit square into a parallelogram. You observe that:
- The area of the parallelogram is 3 times the area of the unit square.
- One eigenvector of A points along the direction [1, 1].
- The transformation is invertible.

**(a)** What is |det(A)|? What does the sign of det(A) tell you geometrically?

**(b)** The eigenvector [1, 1] gets scaled by eigenvalue λ₁ = 2 under A. If the other eigenvalue is λ₂, what must λ₂ be? *(Hint: how do determinants relate to eigenvalues?)*

**(c)** Describe in one sentence what this transformation does to a vector pointing in the [1, 1] direction vs. a generic vector pointing in the [1, 0] direction.

### Question 2 (6 pts)

**True or False with justification.** For each, state T/F and give a one-sentence geometric or algebraic reason.

**(a)** If a 3×3 matrix has rank 2, it maps all of ℝ³ onto a plane through the origin.

**(b)** If det(A) = 0, then Ax = b has no solution for any b.

**(c)** The null space of a matrix and its column space are always orthogonal to each other.

**(d)** If two vectors have a dot product of zero, they must be linearly independent.

**(e)** Every square matrix can be diagonalized.

**(f)** The singular values of a matrix are always ≥ 0, while eigenvalues can be negative.

### Question 3 (5 pts)

**SVD Geometry.** A matrix A has the SVD decomposition A = UΣVᵀ, where the singular values are σ₁ = 5 and σ₂ = 2.

**(a)** If you apply A to the unit circle in ℝ², what shape results? Give its dimensions.

**(b)** Describe the three geometric steps (Vᵀ, then Σ, then U) that the SVD performs on the unit circle. What does each step do?

**(c)** What is the best rank-1 approximation of A in terms of the SVD components? What fraction of A's "energy" (sum of squared singular values) does it capture?

### Question 4 (4 pts)

**Basis and Coordinates.** Suppose you have two different bases for ℝ²:

- Standard basis: B₁ = {î, ĵ} = {[1,0], [0,1]}
- New basis: B₂ = {[1,1], [1,−1]}

**(a)** The vector v has coordinates [3, 1] in the standard basis. What are its coordinates in B₂? (Show your reasoning.)

**(b)** Explain in one sentence why different bases give different coordinates for the same vector, using an analogy to measurement units.

---

## Part B: Core Computation (30 points)

*Show all work. Arithmetic errors with correct method receive substantial partial credit.*

### Question 5 (4 pts)

**Matrix-vector multiplication.** Let:

```
A = [[2, 1], [0, 3]]      v = [4, 2]
```

**(a)** Compute Av using the row dot-product view (each output entry is a dot product of a row of A with v).

**(b)** Compute Av using the column linear-combination view (the result is a linear combination of columns of A, weighted by entries of v).

**(c)** Verify both methods give the same answer. Then explain: which view is more useful when interpreting what an attention head does to representations, and why?

### Question 6 (8 pts)

**Eigenvalues and Eigenvectors.** Let:

```
A = [[4, 2], [1, 3]]
```

**(a)** Find the eigenvalues of A by solving det(A − λI) = 0.

**(b)** For each eigenvalue, find the corresponding eigenvector by solving (A − λI)v = 0.

**(c)** Verify your work: for each eigenvalue-eigenvector pair (λ, v), confirm that Av = λv.

**(d)** Write the diagonalization A = PDP⁻¹, identifying P and D explicitly. What does P represent geometrically?

### Question 7 (4 pts)

**Determinant and Invertibility.** Consider the matrix:

```
M = [[1, 2, 3], [0, k, 4], [0, 0, 2]]
```

**(a)** Compute det(M) as a function of k. *(Hint: this is upper triangular.)*

**(b)** For what value(s) of k is M not invertible? What happens geometrically to 3D space when this occurs?

### Question 8 (6 pts)

**Rank and Null Space.**

```
A = [[1, 2, 1], [2, 4, 3], [3, 6, 4]]
```

**(a)** Row-reduce A to echelon form.

**(b)** State the rank of A.

**(c)** Find a basis for the null space of A (solve Ax = 0).

**(d)** Verify the rank-nullity theorem: rank + nullity = number of columns.

### Question 9 (4 pts)

**Dot Products and Projection.**

Let u = [3, 4] and v = [1, 0].

**(a)** Compute the projection of u onto v: proj_v(u). What is the geometric meaning of the residual u − proj_v(u)?

**(b)** Now let w = [2, −1]. Compute cos(θ) between u and w using cosine similarity. Are these vectors more "similar" or more "different"? Justify.

### Question 10 (4 pts)

**Norms.** For the vector x = [3, −4]:

**(a)** Compute ||x||₁ (L1 norm), ||x||₂ (L2 norm), and ||x||∞ (L-infinity norm).

**(b)** Which norm is always the largest for any vector? Which is always the smallest? State the general inequality.

---

## Part C: Proofs & Reasoning (20 points)

*These require short mathematical arguments. Aim for clarity and rigor.*

### Question 11 (8 pts)

**Prove that for any matrix A, the matrix AᵀA is always symmetric and positive semi-definite.**

**(a)** Show that AᵀA is symmetric: prove (AᵀA)ᵀ = AᵀA.

**(b)** Show that AᵀA is positive semi-definite: prove xᵀ(AᵀA)x ≥ 0 for all x. *(Hint: rewrite xᵀAᵀAx as something squared.)*

**(c)** Under what condition on A is AᵀA strictly positive definite (all eigenvalues > 0)?

### Question 12 (6 pts)

**The Rank-Nullity Connection.**

Let A be a 5×4 matrix with rank 3.

**(a)** What is the dimension of the null space of A?

**(b)** What is the dimension of the column space of A?

**(c)** Can Ax = b have a solution for every b ∈ ℝ⁵? Why or why not?

**(d)** When Ax = b does have a solution, is it unique? Explain using the null space.

### Question 13 (6 pts)

**Projection and Idempotency.** Let P = A(AᵀA)⁻¹Aᵀ be the projection matrix onto the column space of A (where A has full column rank).

**(a)** Prove that P is idempotent: P² = P. (Expand P·P and simplify.)

**(b)** Give a one-sentence geometric explanation of why projecting twice should be the same as projecting once.

---

## Part D: Synthesis & Connections (15 points)

*These questions require you to connect concepts across multiple lessons.*

### Question 14 (7 pts)

**The Determinant-Eigenvalue-SVD Triangle.** Consider a 2×2 symmetric matrix:

```
S = [[5, 2], [2, 5]]
```

**(a)** Compute the eigenvalues of S.

**(b)** Compute det(S) two ways: (i) using the formula ad − bc, and (ii) as the product of eigenvalues. Verify they match.

**(c)** S is symmetric. What special property do its eigenvectors have? (State and verify.)

**(d)** For a symmetric matrix, SVD and eigendecomposition are closely related. Write S in the form S = QΛQᵀ and explain how this relates to S = UΣVᵀ.

**(e)** Is S positive definite? How do you know from the eigenvalues? What does this mean for the quadratic form xᵀSx?

### Question 15 (8 pts)

**From Span to SVD: A Journey Through a Single Matrix.** Consider:

```
A = [[1, 2], [2, 4], [0, 0]]
```

*Answer each question and explain the geometric meaning:*

**(a)** What is the column space of A? (Describe it geometrically as a subspace of ℝ³.)

**(b)** What is the rank of A?

**(c)** What is the null space of A? Find a basis.

**(d)** What is det(AᵀA)? What does this tell you about AᵀA's invertibility?

**(e)** Without computing the full SVD, how many non-zero singular values does A have? Why?

---

## Part E: ML & Alignment Applications (15 points)

*Apply your linear algebra knowledge to neural networks and AI alignment. These are conceptual — no computation needed.*

### Question 16 (5 pts)

**Attention as Dot Products.**

In a transformer, each token produces a query vector q and each other token produces a key vector k. The attention score between them is the dot product q · k.

**(a)** Using the geometric interpretation of the dot product, explain in 2–3 sentences what a high attention score means about the relationship between the query and key vectors.

**(b)** Attention heads use matrices W_Q and W_K that project tokens through a low-rank bottleneck (e.g., from 768 dimensions down to 64, then computing q · k). Using the concept of rank, explain why this bottleneck forces the head to be "selective" about what information it attends to.

### Question 17 (5 pts)

**Superposition and Orthogonality.**

The superposition hypothesis says that neural networks represent more features than they have neurons by encoding features as directions in activation space that are approximately (but not perfectly) orthogonal.

**(a)** In ℝ³, what is the maximum number of mutually orthogonal vectors you can have? Now suppose you allow vectors to be "almost orthogonal" (pairwise dot products close to zero but not exactly zero). Intuitively, can you fit more than 3 such directions? Why does this matter for a 768-dimensional residual stream?

**(b)** When features are not perfectly orthogonal, their representations "interfere." Explain this interference using the concept of projection: if feature direction f₁ and feature direction f₂ are not orthogonal, what happens when you try to read f₁'s value by projecting the activation onto f₁?

### Question 18 (5 pts)

**Change of Basis in Interpretability.**

Mechanistic interpretability researchers say neural networks are hard to interpret in the "neuron basis" (where each coordinate corresponds to one neuron) but may be interpretable in a "feature basis" (where each coordinate corresponds to a human-understandable concept). Sparse autoencoders attempt to find this feature basis.

**(a)** Using the language of change of basis, explain what the sparse autoencoder is doing. What are the "old coordinates" and "new coordinates"?

**(b)** The eigendecomposition A = PDP⁻¹ reveals axes where a transformation becomes simple (just scaling). Draw an analogy: what is the "feature basis" trying to find, in the same spirit as the eigenbasis?

**(c)** LoRA (Low-Rank Adaptation) fine-tunes a model by adding a low-rank update ΔW = BA where B is n×r and A is r×n, with r << n. In terms of SVD concepts, why does this work? What assumption about fine-tuning does it embody?

---

## Bonus Project: Implement PCA from Scratch (Ungraded)

*Take-home coding project. Ties together eigenvalues, covariance, SVD, change of basis, dot products, and rank into one unified pipeline. Complete at your own pace after the exam.*

> PCA is the single most direct application of Phase 1 linear algebra to real ML. Every concept you learned plays a role. This project proves you can wield them together.

### Background: What Is PCA?

Principal Component Analysis finds the directions of maximum variance in your data. It answers: "If I had to compress this high-dimensional data down to k dimensions, which k directions capture the most information?"

The mathematical pipeline connects nearly every lesson:

1. **Center the data** (subtract the mean) — makes the covariance matrix meaningful
2. **Compute the covariance matrix** C = (1/n) XᵀX — this is symmetric and PSD (Lesson 10)
3. **Find the eigenvalues and eigenvectors of C** — the eigenvectors ARE the principal components (Lesson 7)
4. **Sort by eigenvalue** (largest = most variance) — the eigenvalues tell you how much variance each direction captures
5. **Project data onto the top-k eigenvectors** — this is a change of basis + rank-k approximation (Lessons 9, 10, 8)

**Equivalently:** compute the SVD of the centered data matrix X = UΣVᵀ. The columns of V are the principal components, and the singular values encode the variance. SVD and eigendecomposition of the covariance matrix give the same answer. (Lesson 8)

### Part 1: PCA on 2D Synthetic Data

**Generate** 200 points from a 2D Gaussian with a non-diagonal covariance matrix, e.g.:

```
μ = [3, 7]    Σ = [[2, 1.5], [1.5, 1.5]]
```

- **Step A:** Center the data by subtracting the mean. Plot the centered data as a scatter plot.
- **Step B:** Compute the sample covariance matrix C = (1/(n−1)) XᵀX. Verify it is symmetric.
- **Step C:** Compute the eigenvalues and eigenvectors of C. These are your principal components.
- **Step D:** Plot the eigenvectors as arrows on top of the scatter plot, scaled by √(eigenvalue). These arrows should align with the "long axis" and "short axis" of the data cloud.
- **Step E:** Verify via SVD: compute the SVD of the centered data matrix X. Confirm that the right singular vectors V match the eigenvectors of the covariance matrix. Confirm that σ²/(n−1) matches the eigenvalues.

### Part 2: PCA on Real High-Dimensional Data

**Load MNIST digits** (784-dimensional images of handwritten digits). Each image is a 28×28 = 784 dimensional vector.

- **Step F:** Apply your PCA implementation to reduce from 784 dimensions to 2 dimensions. Scatter plot the result, coloring by digit label. You should see clusters forming — digits that "look similar" land near each other in PCA space.
- **Step G:** Plot the "explained variance ratio": for each k from 1 to 50, what fraction of total variance do the top k components capture? Find the "elbow" — the k where adding more components gives diminishing returns.
- **Step H:** Visualize the top 10 principal components as 28×28 images. These are the "directions of maximum variance" in pixel space. What patterns do you see? (They often look like ghostly prototypical strokes.)
- **Step I:** Reconstruct a digit using only k = 5, 20, 50, 100, 200 components. Show the reconstructions side by side with the original. Watch detail emerge as k increases.

### Part 3: Conceptual Questions (Write Up)

**Q1.** Why is PCA a change of basis? What are the old coordinates and new coordinates? In the new coordinate system, what special property does the data have? *(Hint: the covariance matrix becomes diagonal.)*

**Q2.** The rank-k PCA reconstruction is the best rank-k approximation in the Frobenius norm sense (Eckart–Young theorem). Explain this connection to SVD's low-rank approximation from Lesson 8.

**Q3.** When interpretability researchers run PCA on transformer activations, they're looking for "important directions" in the residual stream. Using your PCA intuition: what does a large eigenvalue mean for a direction in activation space? What would it mean if most variance concentrated in very few components?

**Q4.** PCA finds orthogonal directions. But the superposition hypothesis (Lesson 2) says features in neural networks are almost-orthogonal, not exactly orthogonal. Why might PCA miss features that sparse autoencoders can find?

### Constraints & Requirements

- **No `sklearn.decomposition.PCA` allowed.** Implement the algorithm yourself using only NumPy's linear algebra routines (`np.linalg.eig`, `np.linalg.svd`). The point is to see the eigenvalues and covariance matrix with your own hands.
- **Compare both paths:** eigendecomposition of the covariance matrix AND SVD of the data matrix. Verify they give the same principal components.
- **Visualize everything.** This project should produce at least 6 plots: centered data with eigenvectors, MNIST in 2D, explained variance curve, principal component images, and reconstruction comparison.
- **Write a short report** (1–2 pages) answering the conceptual questions and reflecting on what PCA taught you about the connections between eigenvalues, SVD, covariance, change of basis, and rank.

### Concept Map: Where Each Lesson Appears

| Lesson | How It Appears in PCA |
|--------|----------------------|
| **Lesson 1: Vectors** | Each data point is a vector; each image is a 784-dim vector |
| **Lesson 2: Span & Basis** | Principal components form a new basis; PCA subspace is their span |
| **Lesson 3: Transformations** | Projecting onto PCA subspace is a linear transformation |
| **Lesson 5: Rank** | Rank-k approximation discards the least important dimensions |
| **Lesson 6: Determinant** | det(covariance) = product of eigenvalues = generalized variance |
| **Lesson 7: Eigenvalues** | PCA directions ARE eigenvectors of the covariance matrix |
| **Lesson 8: SVD** | SVD of the data matrix gives PCA directly; low-rank = compression |
| **Lesson 9: Dot Products** | Projection onto components uses dot products; orthogonality of PCs |
| **Lesson 10: Change of Basis** | PCA IS a change of basis to decorrelated coordinates; norms measure reconstruction error |

---

*"Every matrix transformation = align input with natural directions → scale each direction → align output with natural directions. This is SVD. Every other concept is a window into part of this story."*

*You now have the complete mathematical language for understanding neural network internals.*
