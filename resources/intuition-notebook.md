# Intuition Notebook

[Back to TOC](../README.md)

> **What this is:** A running collection of deep intuitions — the "aha" moments and mental models that make concepts click. Unlike the cheat sheet (formulas and facts), this notebook captures the *why* behind things. Add to it whenever something crystallizes.

> **📌 Maintenance rule:** When adding a new intuition entry, also add a matching link in the Table of Contents below, under the appropriate section. Keep the TOC in sync with the content.

> **⚠️ Formatting rule:** GitHub markdown can mangle LaTeX that contains characters GitHub interprets as formatting (e.g., `*` for bold/italic). Escape these with backslashes (e.g., `y\*` instead of `y*` inside LaTeX) or use plain text math when LaTeX won't render cleanly.

---

## 📑 Table of Contents

**[Linear Algebra](#linear-algebra)**
- [Matrix × Vector: Two Complementary Views](#matrix--vector-two-complementary-views)
- [SVD means every matrix is rotate → scale → rotate](#svd-means-every-matrix-is-rotate--scale--rotate)
- [Eigenvectors are the directions that "survive" a transformation](#eigenvectors-are-the-directions-that-survive-a-transformation)
- [Why symmetric matrices have orthogonal eigenvectors (via SVD)](#why-symmetric-matrices-have-orthogonal-eigenvectors-via-svd)
- [PCA's eigenvectors are just SVD's right singular vectors — and symmetry is why](#pcas-eigenvectors-are-just-svds-right-singular-vectors--and-symmetry-is-why)
- [PCA is a change of basis that diagonalizes the covariance matrix](#pca-is-a-change-of-basis-that-diagonalizes-the-covariance-matrix)
- [Matrix type taxonomy: what each type "does" to space](#matrix-type-taxonomy-what-each-type-does-to-space)
- [Every linear transformation maps the unit square to a parallelogram](#every-linear-transformation-maps-the-unit-square-to-a-parallelogram)
- [Null space lives in the INPUT space, not the output space](#null-space-lives-in-the-input-space-not-the-output-space)
- [Miscellaneous Thoughts](#miscellaneous-thoughts)

**[Calculus — Fundamentals](#calculus--fundamentals)**
- [The derivative is literally rise/run — just infinitely zoomed in](#the-derivative-is-literally-riserun--just-infinitely-zoomed-in)
- [Geometric understanding of derivatives, the product rule, and the chain rule](#geometric-understanding-of-derivatives-the-product-rule-and-the-chain-rule)
- [Riemann Sums — What they really are](#riemann-sums--what-they-really-are)
- [Trig Sub — Converting back from double angles](#trig-sub--converting-back-from-double-angles)
- [The Gaussian Integral and the Standard Normal — Why √(2π) and not √π](#the-gaussian-integral-and-the-standard-normal--why-2π-and-not-π)
- [Series convergence — the decision algorithm](#series-convergence--the-decision-algorithm)
- [The Integral Test — why comparing to an integral works](#the-integral-test--why-comparing-to-an-integral-works)
- [Which convergence test for which series — pattern matching guide](#which-convergence-test-for-which-series--pattern-matching-guide)
- [Taylor Series -- Polynomial Approximation as Derivative Matching](#taylor-series----polynomial-approximation-as-derivative-matching)
- [Taylor Remainder -- What Each Piece Means Visually](#taylor-remainder----what-each-piece-means-visually)
- [Why Taylors Theorem Is True](#why-taylors-theorem-is-true----repeated-integration-by-parts)
- [Newton's Method for Optimization — Root-Finding One Level Up](#newtons-method-for-optimization--root-finding-one-level-up)

**[Calculus — Ordinary Differential Equations](#calculus--ordinary-differential-equations)**
- [Classifying Equilibria of Autonomous ODEs — Two Methods](#classifying-equilibria-of-autonomous-odes--two-methods)
- [Repeated Roots — Where xe^(rx) Comes From](#repeated-roots--where-xerx-comes-from)
- [The Laplace Transform Is Eigendecomposition for Calculus](#the-laplace-transform-is-eigendecomposition-for-calculus)
- [Poles Tell the Whole Story — Stability From the s-Domain](#poles-tell-the-whole-story--stability-from-the-s-domain)
- [F(s) Blowing Up vs y(t) Blowing Up — Two Different Things](#fs-blowing-up-vs-yt-blowing-up--two-different-things)
- [The Derivative Property — Why Laplace Turns Calculus Into Algebra](#the-derivative-property--why-laplace-turns-calculus-into-algebra)

**[Calculus — Multivariable](#calculus--multivariable)**
- [The gradient is perpendicular to contour lines and points uphill](#the-gradient-is-perpendicular-to-contour-lines-and-points-uphill)

**[Calculus — Vector Calculus](#calculus--vector-calculus)**

**[Calculus — Partial Differential Equations](#calculus--partial-differential-equations)**

**[Calculus — Matrix Calculus & Optimization](#calculus--matrix-calculus--optimization)**

**[Statistics & Regression](#statistics--regression)**
- [Least squares IS projection — and the residuals prove it](#least-squares-is-projection--and-the-residuals-prove-it)
- [Ridge regression is for "everything matters a little"; Lasso is for "most things don't matter"](#ridge-regression-is-for-everything-matters-a-little-lasso-is-for-most-things-dont-matter)
- [P(data | H₀) ≠ P(H₀ | data)](#pdata--h₀--ph₀--data)

**[Neural Networks](#neural-networks)**

**[Interpretability](#interpretability)**

**[Alignment](#alignment)**

**[Vocabulary: Commonly Confused Terms](#vocabulary-commonly-confused-terms)**

---

## Linear Algebra

### Matrix × Vector: Two Complementary Views

**Column View (Linear Combination):**
The columns of the matrix are your new basis vectors. The entries of your input vector are *weights* — they tell you how much of each column/basis vector to combine. The first entry scales the first column, the second entry scales the second column, and you add them all up.

**Row View (Dot Product / Measurement):**
The rows of the matrix are vectors living in the same space as your input. To get each output entry, you take the dot product of that row with your input vector. The dot product captures both *directional alignment* (how much they point the same way) and *magnitude* (how large both vectors are). It's not just a "shadow" — a pure shadow would ignore the row's length. The dot product only becomes pure alignment when the row is a unit vector, which is why normalization shows up everywhere in ML.

**Why both are true simultaneously:**
These aren't different operations — they're two lenses on the exact same arithmetic. The column view asks "what am I building?" The row view asks "what am I measuring?" In ML, each row acts as a feature detector — asking "how much does this input match my pattern?"

### SVD means every matrix is rotate → scale → rotate
No matter how complicated a matrix looks, it's doing three simple things in sequence. Vᵀ aligns the input with natural axes, Σ stretches along those axes, U rotates the output. The singular values tell you HOW MUCH stretching happens in each direction. If some singular values are zero, dimensions get crushed — that's rank deficiency.

### Eigenvectors are the directions that "survive" a transformation
Most vectors get both stretched AND rotated by a matrix. Eigenvectors ONLY get stretched (by λ) — they stay on their line. They're the "natural axes" of the transformation. This is why PCA works: the eigenvectors of the covariance matrix ARE the directions of maximum variance. A generic vector like [1, 0] that isn't an eigenvector will end up pointing in a new direction after the transformation — it gets warped in both magnitude and direction.

### Why symmetric matrices have orthogonal eigenvectors (via SVD)
Start with any symmetric matrix A (so Aᵀ = A) and its SVD: A = UΣVᵀ. Take the transpose of both sides: Aᵀ = VΣUᵀ. But A = Aᵀ, so UΣVᵀ = VΣUᵀ — which forces U = V (up to sign flips on columns to handle negative eigenvalues). So the SVD collapses to A = VΣVᵀ. Since V is orthogonal (Vᵀ = V⁻¹), this is A = VΣV⁻¹ — which is exactly the eigendecomposition PDP⁻¹. The columns of V are simultaneously the right singular vectors and the eigenvectors, and they're orthogonal because SVD's V is always orthogonal. Symmetry forces the input and output rotations to be the same, which turns SVD into eigendecomposition with orthogonality guaranteed for free.

**Consequence — symmetric can't rotate:** Since U = V, the SVD is VΣVᵀ: rotate into eigenbasis (Vᵀ), scale (Σ), rotate back by the exact same amount (V). Steps 1 and 3 cancel → pure stretch, zero net rotation. For a general matrix, U ≠ V and the mismatch between input and output rotations is where rotation comes from.

**Non-uniform scaling looks like rotation on individual vectors:** A symmetric matrix like [[1,-1],[-1,1]] maps [1,0] → [1,-1] — the vector changed direction! But it's not rotation. The vector's eigenvector components got scaled by different amounts (one crushed to 0, the other doubled), warping its direction as a side effect. The test: rotation preserves the unit circle. Symmetric matrices send it to an ellipse. That's scaling, not rotation.

### PCA's eigenvectors are just SVD's right singular vectors — and symmetry is why
We have our covariance matrix C = (1/n)XᵀX, and we were going to take its eigenvectors. But if we take X = UΣVᵀ and expand XᵀX, we get (UΣVᵀ)ᵀ(UΣVᵀ) = VΣᵀUᵀUΣVᵀ = VΣ²Vᵀ (since UᵀU = I). So the eigenvectors of XᵀX are just V — the right singular vectors of X — and the eigenvalues are Σ².

The deeper reason this works so cleanly: AᵀA is always symmetric, which means its eigenvectors are orthogonal. In the eigenbasis, it's pure scaling — no rotation. So when SVD decomposes X into rotate → scale → rotate, the two rotations in AᵀA must cancel each other out, leaving only the scaling (Σ²) expressed in the V basis.

In practice, real algorithms compute SVD directly on X using iterative methods (never forming XᵀX), which avoids squaring the condition number. But for hand computation, eigendecomposing XᵀX is the right approach.

### PCA is a change of basis that diagonalizes the covariance matrix
The old coordinates are whatever basis your data was originally measured in (e.g., the neuron basis for transformer activations — each coordinate = one neuron's firing). In this basis, dimensions are typically correlated: the covariance matrix has non-zero off-diagonal entries. PCA computes the eigenvectors of the covariance matrix and uses them as a new basis. Since the covariance matrix is symmetric, these eigenvectors are orthogonal, so P is an orthogonal matrix and the change of basis is just x_new = Pᵀx. In this new coordinate system, the covariance matrix becomes diagonal (D = P⁻¹AP) — meaning every dimension is uncorrelated. Each principal component captures its own independent chunk of variance, with the eigenvalues on the diagonal telling you how much. Largest eigenvalue = direction of maximum spread. The data's structure is maximally "disentangled": each axis captures independent variation, ordered from most to least important.

### Matrix type taxonomy: what each type "does" to space
- **Symmetric** (Aᵀ = A) → stretches along perpendicular eigen-directions. No rotation. Eigenvalues real, eigenvectors orthogonal. Think: pure scaling in an orthogonal coordinate system. Example: S = [[3,0],[0,1]] stretches x by 3, leaves y alone — circle → ellipse.
- **Orthogonal** (AᵀA = I, equivalently Aᵀ = A⁻¹) → rotates or reflects without stretching. All singular values = 1, preserves lengths and angles. Its *columns* are orthonormal (that's the definition), but its *eigenvectors* can be complex. Example: Q = [[0,-1],[1,0]] is a 90° rotation — circle stays a circle, but eigenvalues are i and -i (complex), so no real direction "survives."
- **Symmetric + orthogonal** → pure reflection. Eigenvalues must be real (symmetric) AND have |λ| = 1 (orthogonal), so every eigenvalue is +1 or -1. The +1 directions stay fixed, the -1 directions flip. Rotation requires complex eigenvalues (e^(iθ)), which symmetry forbids. Special case: all +1 = identity.
- **General matrix** → does all three: rotates, scales non-uniformly, rotates again. That's SVD: A = UΣVᵀ.

**Columns of a matrix ≠ eigenvectors of a matrix.** An orthogonal matrix has orthonormal *columns* by definition — that's what QᵀQ = I means. Its *eigenvectors* are a completely different set of vectors (directions where Qv = λv). For Q = [[0,-1],[1,0]]: columns are [0,1] and [-1,0] (real, orthonormal), but eigenvectors are complex (no real direction survives a 90° rotation). Symmetric matrices are special because their eigenvectors are guaranteed real and orthonormal.

**"Symmetric" describes eigenvector geometry. "Orthogonal" describes the matrix's action on space.** The word "orthogonal" does double duty — a symmetric matrix has eigenvectors orthogonal *to each other*, while an orthogonal matrix preserves lengths and angles. These are completely different properties.

### Every linear transformation maps the unit square to a parallelogram
"Parallelogram" doesn't mean "shear." ALL matrices produce parallelograms from the unit square — that's just what "linear" means (lines stay lines, origin stays fixed). Scaling → rectangle (a special parallelogram). Rotation → rotated square (also a parallelogram). Shear → slanted parallelogram. The determinant tells you the area of that parallelogram relative to the original.

### Null space lives in the INPUT space, not the output space
The null space of an m×n matrix is a subspace of ℝⁿ (the column count = input dimension). Rank-nullity counts input dimensions: rank + nullity = n (columns). Think of it as a conservation law: every input dimension either **survives** (counted by rank) or gets **destroyed** (counted by nullity). For a 10×3 matrix with rank 2, the null space is 1-dimensional (one line in 3D input space gets crushed to zero), NOT 8-dimensional. The output lives on a 2D plane inside ℝ¹⁰ — but that plane can be tilted arbitrarily, with all 10 components nonzero. Rank tells you the dimension of the output subspace, not which coordinates are used.

### Miscellaneous Thoughts
1. v*v is the same thing as vᵀv. This is the insight from 3B1B that the dot product of two vectors is the same as a linear transformation.  
2. The diagonal entries of XᵀX are the variance of the features, whereas the off-diagonal values are the correlation of the features.  
3. Eigendecomposition works when a matrix is square and non-defective (full set of linearly independent EIGENVECTORS (not columns))

---

## Calculus — Fundamentals

### The derivative is literally rise/run — just infinitely zoomed in

![Derivative as df/dx](images/derivative-tangent-line-3b1b.png)

dx is a tiny nudge in the input. df is the resulting tiny change in the output. The derivative is their ratio — the slope of the tangent line. As dx → 0, the tangent line becomes a perfect local approximation of the curve. Rearranging gives df = f'(x) · dx: rise = slope × run at infinitesimal scale.

This fraction view is what makes the chain rule obvious: df/dg · dg/dx = df/dx because the dg's cancel — each is a real tiny quantity passed through the chain. And it's what makes backprop work: every weight's gradient dL/dw tells you "if I nudge this weight by dw, the loss changes by (dL/dw) · dw."


### Geometric understanding of derivatives, the product rule, and the chain rule

📐 [**Interactive Visualization: The Geometric Derivative**](https://kaxitron.github.io/research_plan/resources/geometric-derivative.html)

The derivative of x² comes from a square growing by dx on each side — two strips of x·dx plus a negligible corner. For 1/x, a rectangle with constant area 1 gets wider, so its height *must* shrink — the negative sign in -1/x² is geometric necessity. The product rule is two strips on a rectangle where both sides change. The chain rule is cascading nudges through a pipeline of number lines, each function scaling the nudge by its own derivative.


### Riemann Sums — What they really are

The integral is *defined* as the limit of a Riemann sum:

$$\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i) \cdot \Delta x$$

where $\Delta x = \frac{b-a}{n}$ and $x_i = a + i \cdot \frac{b-a}{n}$.

We have the sum of all the tiny rectangles under a curve. Each rectangle has width $\frac{b-a}{n}$ (where $n \to \infty$), and height $f(x_i)$ — the value of the curve at that rectangle's position. To know *which* rectangle we're on, we use $i$: the $i$-th rectangle sits at $x_i = a + i \cdot \frac{b-a}{n}$, which is just the starting point plus $i$ steps of size $\frac{b-a}{n}$. On $[0, 1]$ this simplifies to $x_i = i/n$ with width $1/n$.

To identify $f(x)$ from a sum, literally replace every $i/n$ with $x$. If you see $(i/n)^2 + i/n$, that's $f(x) = x^2 + x$. Straight substitution, nothing hidden.

**Concrete example:** $\int_2^4 x^2\,dx$ as a Riemann sum. Here $a = 2$, $b = 4$, $\Delta x = \frac{2}{n}$, and $x_i = 2 + \frac{2i}{n}$:

$$\lim_{n \to \infty} \sum_{i=1}^{n} \frac{2}{n} \cdot \left(2 + \frac{2i}{n}\right)^2 = \int_2^4 x^2\,dx = \frac{x^3}{3}\Big|_2^4 = \frac{64}{3} - \frac{8}{3} = \frac{56}{3}$$

**The integration bee trick:** Riemann sums normally define integrals, but you can run it backwards — recognize a hard sum as a Riemann sum in disguise, convert to an integral, and evaluate with the FTC. Recipe: factor out $\frac{1}{n}$ as $\Delta x$, rewrite everything else as a function of $\frac{i}{n}$, replace with $x$, integrate.

### Trig Sub — Converting back from double angles

When your trig sub answer contains sin(2θ) or cos(2θ), you **cannot** just read these off the triangle directly. The triangle gives you sinθ, cosθ, tanθ etc. — single-angle functions. There is no shortcut like "multiply the triangle ratio by 2."

Instead, use double angle identities to decompose back to single angles first:

- $\sin(2\theta) = 2\sin\theta\cos\theta$ → then read sinθ and cosθ off the triangle and multiply
- $\cos(2\theta) = 1 - 2\sin^2\theta$ or $2\cos^2\theta - 1$ → pick whichever form uses what your triangle gives you easily

**Example:** If $x = 3\sin\theta$, the triangle has opposite = $x$, hypotenuse = $3$, adjacent = $\sqrt{9-x^2}$. Then:

$$\sin(2\theta) = 2 \cdot \frac{x}{3} \cdot \frac{\sqrt{9-x^2}}{3} = \frac{2x\sqrt{9-x^2}}{9}$$

You must go through the identity — there's no way to get sin(2θ) directly from the triangle without this step.

### The Gaussian Integral and the Standard Normal — Why √(2π) and not √π

The Gaussian integral gives us:

$$\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$$

So if you wanted to turn $e^{-x^2}$ into a valid probability density (area = 1), you'd just divide by $\sqrt{\pi}$:

$$p(x) = \frac{1}{\sqrt{\pi}} e^{-x^2}$$

This *is* a perfectly valid PDF. But it has an inconvenient property: its variance is 1/2, not 1. You can verify this by computing $\text{Var}(X) = \int_{-\infty}^{\infty} x^2 \cdot \frac{1}{\sqrt{\pi}} e^{-x^2}\,dx = \frac{1}{2}$.

A variance of 1/2 is ugly to work with — it clutters every formula that builds on top of the Gaussian. So instead, we *stretch* the bell curve horizontally by substituting $x \to x/\sqrt{2}$, which widens it just enough to make the variance exactly 1. Applying this substitution:

$$e^{-x^2} \longrightarrow e^{-x^2/2}$$

But stretching changes the area under the curve. The new integral is:

$$\int_{-\infty}^{\infty} e^{-x^2/2}\,dx = \sqrt{2\pi}$$

(You can verify: substitute $u = x/\sqrt{2}$, so $dx = \sqrt{2}\,du$, and $\sqrt{2} \cdot \sqrt{\pi} = \sqrt{2\pi}$.)

So to normalize this stretched version, we divide by $\sqrt{2\pi}$:

$$p(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$$

This is the **standard normal distribution** $\mathcal{N}(0, 1)$ — mean 0, variance 1. The $\sqrt{2\pi}$ isn't some mysterious constant; it's literally $\sqrt{2} \cdot \sqrt{\pi}$, where the $\sqrt{\pi}$ comes from the Gaussian integral and the $\sqrt{2}$ comes from the horizontal stretch we chose so that the variance would be 1 instead of 1/2.

**The chain of decisions:**
1. $e^{-x^2}$ has a nice shape but its integral is $\sqrt{\pi}$ (irrational) and dividing by $\sqrt{\pi}$ gives variance 1/2 (ugly)
2. $e^{-x^2/2}$ is a horizontal stretch that makes the variance exactly 1, but now the integral is $\sqrt{2\pi}$
3. We chose convenience of variance over convenience of the normalizing constant — because variance shows up in far more formulas than the normalizing constant does

Every time you see $\sqrt{2\pi}$ in statistics, this is why it's there.

### Series convergence — the decision algorithm

When you see $\sum a_n$ and need to determine convergence, walk through this flowchart in order:

**Step 0: Does $a_n \to 0$?** If $\lim_{n\to\infty} a_n \neq 0$, the series **diverges**. Full stop. This is the divergence test — it can only prove divergence, never convergence. (The converse is false: $\sum 1/n$ diverges even though $1/n \to 0$.)

**Step 1: Is it a known form?**
- **Geometric** $\sum ar^n$: converges iff $|r| < 1$. Look for a constant ratio between consecutive terms.
- **p-series** $\sum 1/n^p$: converges iff $p > 1$. If the dominant behavior looks like $1/n^p$, jump to limit comparison.
- **Telescoping**: partial fractions give $f(n) - f(n+1)$, so the partial sums collapse.

**Step 2: Factorials or exponentials?** → **Ratio test.** Compute $\lim |a_{n+1}/a_n|$. Less than 1 → converges. Greater than 1 → diverges. Equal to 1 → inconclusive (this is the test's blind spot — it fails on all p-series, for instance). Intuition: you're asking "does each term shrink by a fixed fraction compared to the last one?"

**Step 3: Can you compare it to something known?** → **Limit comparison test.** Find a simpler series $b_n$ with the same dominant behavior. If $\lim a_n/b_n = L$ where $0 < L < \infty$, both series do the same thing. This is the workhorse test — most "messy rational function" series are handled here by comparing to a p-series. (Direct comparison also works: if $0 \leq a_n \leq b_n$ and $\sum b_n$ converges, so does $\sum a_n$.)

**Step 4: Clean decreasing function?** → **Integral test.** If $a_n = f(n)$ where $f$ is positive, continuous, and decreasing, then $\sum a_n$ converges iff $\int_1^\infty f(x)\,dx$ converges. Useful when the comparison isn't obvious but you can integrate the function.

**Step 5: Alternating signs?** → **Alternating series test.** If $a_n = (-1)^n b_n$ with $b_n > 0$, $b_n$ decreasing, and $b_n \to 0$, the series converges. Note: this only gives *conditional* convergence. If $\sum |a_n|$ also converges, you have *absolute* convergence (stronger).

**Step 6: Everything raised to $n$th power?** → **Root test.** Compute $\lim |a_n|^{1/n}$. Same threshold as ratio test (< 1 converges, > 1 diverges, = 1 inconclusive). Useful when the ratio test gives messy algebra but taking nth roots simplifies things.

**When you're stuck:** partial fractions, algebraic simplification, or rewriting the series in a different form often reveals which test to use. The goal is always to reduce to a known form or a clean comparison.


### The Integral Test — why comparing to an integral works

When $f(x)$ is positive and decreasing, the sum $\sum_{n=1}^{N} f(n)$ and the integral $\int_1^{N} f(x)\,dx$ are racing each other — and the sum always wins, because the rectangles poke above the curve.

**The 1/x example that makes this click:**

Draw $y = 1/x$ and left-endpoint rectangles at each integer. Each rectangle has width 1 and height $1/n$, so its area equals the $n$-th term of the harmonic series. Because $1/x$ is decreasing, the rectangle from $n$ to $n+1$ is taller than the curve on that interval (the left endpoint is the highest point). So the rectangles collectively overshoot the area under the curve:

$$\sum_{n=1}^{N} \frac{1}{n} > \int_1^{N+1} \frac{1}{x}\,dx = \ln(N+1)$$

Since $\ln(N+1) \to \infty$, anything bigger than it must also diverge. That proves $\sum 1/n = \infty$.

**Why this logic generalizes:** For any positive, decreasing $f(x)$:

$$\int_1^{N+1} f(x)\,dx < \sum_{n=1}^{N} f(n) < f(1) + \int_1^{N} f(x)\,dx$$

The sum is squeezed between two integrals that differ by just $f(1)$. So the sum converges if and only if the integral converges — they live or die together.

**Why it's a lower bound, not upper:** The key insight is that left-endpoint rectangles on a *decreasing* function always overshoot the curve. The integral is strictly *smaller* than the sum. So if even the smaller thing (the integral) blows up, the bigger thing (the sum) must blow up too. This is just the comparison test in disguise: $a_n > b_n$ and $\sum b_n = \infty$ implies $\sum a_n = \infty$.

**The knife edge at p = 1:** For the p-series $\sum 1/n^p$, the corresponding integral is $\int_1^{\infty} x^{-p}\,dx$. The antiderivative switches behavior at $p = 1$: for $p \neq 1$ it's $x^{1-p}/(1-p)$ (a power function), but at $p = 1$ it's $\ln(x)$ (which diverges). So $p = 1$ is the exact boundary — shrink the terms even slightly faster than $1/n$ (any $p > 1$) and the integral becomes finite.

**ML connection:** This integral-vs-sum relationship appears in learning rate theory. The conditions for SGD convergence — $\sum \eta_t = \infty$ but $\sum \eta_t^2 < \infty$ — are checked via the integral test. A schedule of $\eta_t = 1/t$ works because $\int 1/x\,dx = \ln(x) \to \infty$ (enough exploration) while $\int 1/x^2\,dx = 1$ (updates settle down).

### Which convergence test for which series — pattern matching guide

The decision algorithm above gives you the logical flowchart. This section is the complement: a pattern-matching guide organized by *what the series looks like*. Each test has a natural habitat — a family of series it's built for. The ratio test, for example, is powerful but completely blind to polynomial-rate decay (it returns $L = 1$ for *every* p-series, regardless of $p$). Matching the right test to the right series saves time and avoids inconclusive dead ends.

**Factorials or exponentials → Ratio Test.** When consecutive terms have a clean multiplicative relationship, the ratio $a_{n+1}/a_n$ simplifies beautifully. This test detects *exponential-rate* convergence or divergence.

$$\sum \frac{2^n}{n!}: \quad \frac{a_{n+1}}{a_n} = \frac{2^{n+1}}{(n+1)!} \cdot \frac{n!}{2^n} = \frac{2}{n+1} \to 0 < 1 \quad \text{(converges)}$$

**Polynomial terms (rational functions of $n$) → Limit Comparison with a p-series.** If the terms look like a ratio of polynomials in $n$, find the dominant power and compare to $1/n^p$. The ratio test *cannot* handle these — it always gives $L = 1$.

$$\sum \frac{3n + 1}{n^3 - 5}: \quad \text{Dominant behavior is } \frac{3n}{n^3} = \frac{3}{n^2}. \quad \text{Compare to } \sum \frac{1}{n^2}$$

$$\lim_{n \to \infty} \frac{(3n+1)/(n^3-5)}{1/n^2} = \lim \frac{(3n+1) \cdot n^2}{n^3 - 5} = \lim \frac{3n^3 + n^2}{n^3 - 5} = 3$$

Since $0 < 3 < \infty$ and $\sum 1/n^2$ converges ($p = 2 > 1$), the original series converges.

**Decreasing function you can integrate → Integral Test.** When the terms come from a clean, integrable function and comparison isn't obvious. Especially useful for terms involving $\ln(n)$.

$$\sum \frac{1}{n \ln(n)}: \quad \int_2^{\infty} \frac{1}{x \ln(x)}\,dx = \ln(\ln(x))\Big|_2^{\infty} = \infty \quad \text{(diverges)}$$

This series is tricky because it *looks* like it should converge (terms go to zero, and faster than $1/n$), but it doesn't. The integral test catches it cleanly. (Note: $\sum 1/(n \cdot \ln(n)^2)$ *does* converge — the extra power of $\ln$ is just enough.)

**Alternating signs → Alternating Series Test.** When terms flip sign via $(-1)^n$. Just check that the absolute values decrease and approach zero.

$$\sum \frac{(-1)^n}{n}: \quad b_n = \frac{1}{n} \text{ is decreasing and } b_n \to 0 \quad \text{(converges conditionally)}$$

This converges even though $\sum 1/n$ diverges — the alternating signs create enough cancellation. But it's only *conditional* convergence: rearranging the terms can change the sum (Riemann rearrangement theorem).

**Everything raised to the $n$-th power → Root Test.** When taking an $n$-th root simplifies things more cleanly than the ratio would.

$$\sum \left(\frac{n}{2n+1}\right)^n: \quad |a_n|^{1/n} = \frac{n}{2n+1} \to \frac{1}{2} < 1 \quad \text{(converges)}$$

The ratio test would work here too, but the algebra is messier. The root test peels off the $n$-th power immediately.

**Partial fractions reveal cancellation → Telescoping.** When the terms decompose into $f(n) - f(n+1)$, consecutive terms cancel and the partial sum collapses.

$$\sum \frac{1}{n(n+1)}: \quad \frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$$

$$S_N = \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \cdots + \left(\frac{1}{N} - \frac{1}{N+1}\right) = 1 - \frac{1}{N+1} \to 1$$

**Why the ratio test has a blind spot:** The ratio test measures whether terms decay at an *exponential* rate. Polynomial decay ($1/n^p$) is always slower than exponential decay, so the ratio $a_{n+1}/a_n$ approaches 1 from below for every p-series — the test can't distinguish $1/n$ (diverges) from $1/n^{100}$ (converges). That's why polynomial series need comparison or integration instead.

### Taylor Series -- Polynomial Approximation as Derivative Matching

The core idea: you cannot evaluate a complicated function everywhere, but you can compute its derivatives at a single point a. Taylor series builds the unique polynomial matching all derivatives at a. The n! in the denominator cancels the n! produced by differentiating (x-a)^n.

The physics analogy: x = x0 + v0*t + (1/2)a*t^2 IS a second-order Taylor expansion. f(a) = position, f'(a)*delta = velocity*time, f''(a)/2*delta^2 = half-acceleration*time-squared. Each term asks a deeper question about rates of change.

Deriving compact sum notation: (1) compute derivatives at a, (2) spot which powers survive and whether signs alternate, (3) encode with (-1)^n for alternating signs, 2n+1 for odd powers, 2n for even powers.

Why ln(1+x) has 1/n not 1/n!: its derivatives already contain factorials that cancel the Taylor formula denominator. Always simplify f^(n)(a)/n! fully.

ML connection: zeroth order = random search, first order = gradient descent, second order = Newton method via Hessian.

### Taylor Remainder -- What Each Piece Means Visually

R_n(x) = f^(n+1)(c) / (n+1)! * (x-a)^(n+1) has three factors. Visually: the pink arrow between the true function and the Taylor polynomial.

(x-a)^(n+1): how far from the expansion point. Further = bigger error. More terms make error shrink faster near a.

1/(n+1)!: how many terms already captured. Factorials grow explosively, crushing the remainder.

f^(n+1)(c): how wild the function is beyond what was captured. The mysterious c between a and x absorbs the entire infinite tail of higher derivatives.

For gradient descent (n=1): R_1 = f''(c)/2 * (x-a)^2. Error = half curvature times step size squared. Why learning rate depends on largest Hessian eigenvalue.

### Why Taylors Theorem Is True -- Repeated Integration by Parts

Start from FTC: f(x) = f(a) + integral of f'(t) dt. Apply integration by parts with v = -(x-t). Each round peels off one Taylor coefficient, pushes remainder into smaller integral. After n rounds: exact polynomial plus exact integral remainder. No approximation anywhere. Factorials accumulate from repeated integration mirroring repeated differentiation.

---

### Newton's Method for Optimization — Root-Finding One Level Up

Newton's method finds zeros. That's all it does. The optimization trick: minimizing g(x) means finding where g'(x) = 0, which is a root-finding problem. Apply Newton to f(x) = g'(x) and the second derivative g''(x) appears naturally as f'(x). You're still just finding zeros — but of the derivative, not the original function. This is the conceptual bridge to all second-order optimizers in ML: training a neural network = finding zeros of ∇L(w), which is Newton's method applied to the gradient. The Hessian appears because it's the derivative of the gradient.

---

## Calculus — Ordinary Differential Equations

### Classifying Equilibria of Autonomous ODEs — Two Methods

For dy/dt = f(y) with equilibrium f(y\*) = 0, two ways to determine stability:

**Method 1 — Sign checking:** Evaluate f(y) at test points above and below y\*. If both sides push toward y\* (positive below, negative above), it's **stable**. If both push away, it's **unstable**.

**Method 2 — Derivative shortcut:** Compute f'(y\*) (derivative of f with respect to y, not t). Negative → **stable**, positive → **unstable**. This works because f'(y\*) tells you whether the rate-of-change function is decreasing through zero (arrows converge = stable) or increasing through zero (arrows diverge = unstable). Under the hood, you're linearizing: near y\*, the displacement u = y − y\* satisfies du/dt ≈ f'(y\*) · u, which is exponential decay (stable) or growth (unstable).

**ML version:** For gradient flow dw/dt = −L'(w), the shortcut gives f'(w\*) = −L''(w\*). Stability condition f' < 0 becomes L'' > 0 — positive curvature = loss minimum = stable. This is the second derivative test repackaged as dynamical stability.

### Repeated Roots — Where xe^(rx) Comes From

When a second-order ODE ay'' + by' + cy = 0 has a repeated characteristic root r, the quadratic ar² + br + c = 0 touches zero at only one point. There is no second value s ≠ r satisfying the polynomial, so the exponential guess is exhausted after giving us just y₁ = e^(rx).

The second solution comes from a limit argument. With distinct roots r₁ and r₂, the difference (e^(r₂x) − e^(r₁x)) / (r₂ − r₁) is a valid solution (linear combination scaled by a constant). Now slide r₂ → r₁. That difference quotient is literally the definition of differentiating e^(rx) with respect to r:

d/dr [e^(rx)] = x · e^(rx)

So xe^(rx) is what the second exponential *degenerates into* when the two roots collide. It's not a lucky guess — it's the unique limit of the distinct-roots solution as the gap closes.

Why it's independent: the Wronskian of e^(rx) and xe^(rx) is e^(2rx), which is never zero. The polynomial factor x introduces growth that no constant multiple of e^(rx) can replicate.

**ML connection:** The repeated root case corresponds to critical damping in optimizer dynamics — the system decays as fast as possible without oscillating. For SGD with momentum, this is the ideal tuning point.

---

## Calculus — Multivariable

### The gradient is perpendicular to contour lines and points uphill
If you're standing on a hillside, the gradient tells you the steepest uphill direction. Gradient descent goes opposite — steepest downhill. The shape of the contour lines (elongated vs. circular) determines how hard optimization is. Circular = easy (condition number ≈ 1). Elongated = hard (high condition number). This is why preconditioning and Adam optimizer help.

---

## Calculus — Vector Calculus

*(To be filled during Block C)*

---

## Calculus — Partial Differential Equations

*(To be filled during Block D)*

---

## Calculus — Matrix Calculus & Optimization

*(To be filled during Block E)*

---

## Statistics & Regression

### Least squares IS projection — and the residuals prove it
The whole story of ordinary least squares in three lines:

- **Xw = ŷ** — the prediction lives in the column space of X
- **y = ŷ + e** — the actual value is the prediction plus the residual
- **Xᵀe = 0** — the residual is orthogonal to every column of X

That last equation is the punchline. It says the error vector is *perpendicular* to the column space — which means ŷ is the closest point in the column space to y. That's exactly what projection does (Lesson 10). The normal equations Xᵀ Xw = Xᵀy are just rearranging Xᵀ(y − Xw) = 0, i.e., "make the residual orthogonal to every predictor." Regression isn't curve fitting — it's *geometry*.

### Ridge regression is for "everything matters a little"; Lasso is for "most things don't matter"
Ridge (L2) shrinks all coefficients toward zero but never TO zero. It's best when you believe all your predictors contribute something — you just want to tame their magnitudes and handle multicollinearity. Geometrically, the L2 penalty's circular constraint surface meets the loss contours at a point where all coefficients are nonzero but smaller.

Lasso (L1) pushes coefficients all the way to exactly zero. It's best when you expect many of your predictors are irrelevant and you want the model to pick the important ones automatically. Geometrically, the L1 penalty's diamond-shaped constraint has corners on the axes, and the loss contours tend to hit those corners — which means some coefficients are exactly zero. That's automatic feature selection.

**The eigenvalue connection:** Ridge adds λ to every eigenvalue of AᵀA before inverting, which stabilizes small eigenvalues (prevents them from exploding in the inverse). Lasso doesn't have a clean matrix formula — it requires iterative soft-thresholding — but the sparsity it produces is what makes it O(mn·k) instead of O(n³), which actually makes it FASTER than ridge for very high-dimensional problems.

### P(data | H₀) ≠ P(H₀ | data)
The p-value gives you the first thing. What you actually want is the second thing. Getting from one to the other requires Bayes' theorem — specifically, you need the prior probability of H₀. This is why a "significant" result from a study testing an implausible hypothesis is much less convincing than the same p-value from a study testing a plausible one. The base rate matters.

---

## Neural Networks

*(To be filled as you progress through Phase 4)*

---

## Interpretability

*(To be filled as you progress through Phase 5, Lessons 67–94)*

---

## Alignment

*(To be filled as you progress through Phase 6)*

---

## Vocabulary: Commonly Confused Terms

**Standardize vs Normalize:** Standardize = z-score (subtract mean, divide by std → mean 0, std 1). Normalize = min-max rescaling (→ range [0,1]). For PCA, standardize — it equalizes variance across features.

**Orthogonal vs Orthonormal:** Orthogonal = perpendicular (dot product = 0). Orthonormal = perpendicular AND unit length. PCA eigenvectors should be orthonormal.

**Covariance vs Correlation:** Covariance = raw joint variation (scale-dependent). Correlation = covariance divided by both standard deviations (bounded to [-1, 1], scale-free).

**Rank vs Dimension:** Rank = property of a matrix or subspace (how many independent directions it covers). Dimension = property of the ambient space it lives in. A rank-2 matrix in ℝ⁵ maps to a 2D subspace inside 5D space.

**Eigenvalue vs Singular value:** Eigenvalues can be negative or complex; they're scaling factors of eigenvectors (Av = λv). Singular values are always ≥ 0; they're the stretching factors in SVD. Singular values of A = square roots of eigenvalues of AᵀA.

**Linear independence vs Orthogonality:** Independent = none are redundant (can't write any as a combo of the others). Orthogonal = all are perpendicular. Orthogonal implies independent, but independent does NOT imply orthogonal.

**Null space vs Kernel:** Same thing. "Null space" is standard linear algebra; "kernel" appears more in ML and functional analysis.

**Column space vs Range vs Image:** Same thing, three names. The set of all possible outputs Ax.

**Invertible vs Non-singular vs Full rank:** Same thing, three names — but the matrix must be square. det ≠ 0, null space = {0}, all columns independent. Non-square matrices can't be invertible (they map between spaces of different dimension).

**Positive definite vs Positive semi-definite:** PD = all eigenvalues > 0 (strict bowl, no flat directions). PSD = all eigenvalues ≥ 0 (bowl or flat, never saddle). Covariance matrices are always PSD. AᵀA is always PSD.

## Dynamic Programming — "Best Up To" vs "Best Ending At"

**DP subproblem definition — the key distinction:** If your decision at index $i$ depends only on position — like "skip the neighbor" in House Robber or "subtract a coin" in Coin Change — then "best up to $i$" works, because nearby dp values contain everything you need. But if your decision depends on the **actual value** of the last element you chose — like "is this number bigger than the previous one" in LIS, or "does this number divide the previous one" — then "best up to $i$" is useless because it hides which element you committed to. You need "best ending at $i$" so the subproblem exposes the last chosen value, letting you check whether the current element is compatible.

**The test:** Can I make my decision knowing only position and nearby dp values? → "up to." Does the constraint compare the current element's value against the previous chosen element's value? → "ending at."

---

## Lesson 16 — Higher-Order ODEs, Vibrations, and Power Series

**Wronskian = determinant test for functions:** The Wronskian asks "at this point x, do the state vectors (y, y')^T form linearly independent columns?" Same Phase 1 tool, applied to function-and-derivative pairs instead of plain vectors.

**Abel's theorem — all-or-nothing independence:** The Wronskian satisfies its own separable ODE: W' = -p(x)W, so W(x) = W(x_0) * exp(-∫p dx). Since the exponential is never zero, W is either always zero or never zero. Check one point, conclude everywhere. The key detail: it's p(x) (the y' coefficient), not q(x).

**Spring-mass-damper = SGD with momentum:** The continuous limit of SGD with momentum is exactly the damped oscillator ODE. Mass = inertia, damping = momentum decay (1-β), spring constant = Hessian eigenvalue. Underdamped = β too high (oscillates around minimum). Overdamped = β too low (sluggish convergence). Critically damped = optimal β. The problem: different Hessian eigenvalues want different damping, but momentum gives one global β. This is why Adam exists — per-parameter adaptive damping.

**Resonance = learning rate instability:** When the optimizer's effective frequency matches a Hessian eigenvalue direction, you get resonance — the loss explodes. The learning rate ceiling η < 2/λ_max is literally a resonance condition. Same math as a bridge shaking apart in wind.

**Undetermined coefficients — self-reproducing families:** The method works because polynomials, exponentials, and trig functions form closed families under differentiation. Differentiating never leaves the family, so a finite guess template suffices. Functions like tan(x), ln(x), 1/x break this — their derivatives generate infinitely many new forms.

**Overlap rule (multiply by x):** When your particular solution guess is already a homogeneous solution, it will produce zero on the left side. Multiplying by x bumps you out of the homogeneous solution space. For repeated roots, you may need to multiply by x twice.

**Variation of parameters — the Wronskian's practical role:** The Wronskian matrix appears as the coefficient matrix of the 2x2 system for u_1' and u_2'. Its nonzero determinant (guaranteed by independence of solutions) means the system always has a unique solution via Cramer's rule.

**Why the cancellation works in variation of parameters:** When you substitute y_p = u_1*y_1 + u_2*y_2 into the ODE, the terms without u-primes reconstruct the homogeneous equation for y_1 and y_2, which equals zero by definition. Only the u' terms survive. This is why we can use homogeneous solutions as building blocks for the particular solution.

**Power series = solving for an infinite sequence:** Instead of finding a formula, assume y = Σ a_n x^n and let the ODE force relationships between coefficients. The function is defined by its series, not by a closed-form name. Same philosophy as neural networks: represent functions through computed parameters, not symbolic formulas.

**Orphan terms in power series:** When variable coefficients like xy shift the power of x, the re-indexed sums start at different indices. Terms with no partner from the other sum are forced to zero independently of initial conditions. When sums line up (no shift), no orphans, and all coefficients depend on the free parameters a_0 and a_1.

---

---

## Lesson 17 — The Laplace Transform

### The Laplace Transform Is Eigendecomposition for Calculus

The eigenvectors of a matrix are the directions where the matrix acts by simple scaling: $Av = \lambda v$. The Laplace transform does the same thing for the operator $d/dt$. The eigenfunctions of differentiation are exponentials: $(d/dt) e^{st} = s \cdot e^{st}$. The eigenvalue is $s$.

When you compute $F(s) = \int_0^\infty e^{-st} f(t)\,dt$, you're asking "how much of each eigenfunction $e^{st}$ is present in $f(t)$?" — the exact analog of decomposing a vector into eigenvector components. This is why the Laplace transform turns differential equations into algebraic equations: you've changed to a basis where the hard operator (differentiation) is diagonal — it just multiplies by $s$.

**The gamma function connection:** The gamma function $\Gamma(n+1) = \int_0^\infty e^{-t} t^n\,dt$ is the Laplace transform of $t^n$ evaluated at $s = 1$. The $n!$ in the transform table entry $\mathcal{L}\\{t^n\\} = n!/s^{n+1}$ is literally the gamma function.

**The resonance probe interpretation:** Each value of $s$ is a probe asking "how much do you resonate with $e^{st}$?" For most $s$, the answer is finite. At the **poles** (where $F(s) \to \infty$), the probe and signal are in perfect sync — their product neither grows nor decays, so the integral accumulates without bound. The pole reveals a natural exponential rate of the system.

**Concrete example:** For $f(t) = e^{2t}$, the integrand is $e^{(2-s)t}$. When $s > 2$, the probe wins and the integral converges. When $s = 2$, perfect cancellation: the integrand is $e^0 = 1$ forever, and the integral of 1 over $[0, \infty)$ is infinite. That's the pole at $s = 2$.

### Poles Tell the Whole Story — Stability From the s-Domain

The parameter $s$ can be complex: $s = \sigma + i\omega$. The real part $\sigma$ controls growth/decay rate, the imaginary part $\omega$ controls oscillation frequency. Each basis function $e^{st}$ is a decaying or growing oscillation: $e^{st} = e^{\sigma t} \cdot e^{i\omega t}$.

The Fourier transform is the special case where $\sigma = 0$ — only pure oscillations, no growth or decay. The Laplace transform maps out the entire complex plane, which is why it can handle signals like $e^{3t}$ that the Fourier transform chokes on.

**Pole location determines solution behavior:**
- **Negative real part** (left half-plane): mode decays → stable. Example: pole at $s = -2$ gives $e^{-2t}$.
- **Zero real part** (imaginary axis): mode oscillates forever → marginally stable. Example: poles at $s = \pm 2i$ give $\sin(2t)$ and $\cos(2t)$.
- **Positive real part** (right half-plane): mode grows → unstable. Example: pole at $s = 1 + 3i$ gives $e^t \cdot e^{3it}$ — a growing oscillation.

Glance at the poles of $Y(s)$ and you immediately know whether the solution oscillates, grows, decays, or some combination — before you even invert back to the time domain.

**ML connection:** "Will training converge?" is asking "do the eigenvalues of the system have negative real parts?" The learning rate ceiling $\eta < 2/\lambda_{\max}$ is a pole-placement condition — too large and you push poles into the right half-plane, causing training to diverge. Transfer function thinking (input → black box → output) is exactly how we think about neural network layers.

### F(s) Blowing Up vs y(t) Blowing Up — Two Different Things

$F(s)$ blows up at the poles — that's what a pole *is*. But this does NOT mean $y(t)$ blows up over time. The two are different questions:

- $F(s)$ blowing up at $s = s_0$ means the transform integral diverges when probed at that specific frequency — the signal resonates perfectly with $e^{s_0 t}$.
- $y(t)$ blowing up means the time-domain solution grows without bound as $t \to \infty$.

Whether $y(t)$ blows up depends on the **real part** of the poles. Purely imaginary poles (e.g., $s = \pm 2i$) make $F(s)$ blow up at those points, but $y(t)$ just oscillates forever with constant amplitude — because $e^{2it}$ has no growth factor.

### The Derivative Property — Why Laplace Turns Calculus Into Algebra

$\mathcal{L}\\{f'(t)\\} = s\,F(s) - f(0)$. Taking a derivative in the time domain becomes multiplication by $s$, minus the initial condition.

**Why this works:** Integration by parts with $u = e^{-st}$, $dv = f'(t)\,dt$. The exponential eigenfunction interacts cleanly with differentiation — pulling down a factor of $s$ — while the boundary term at $t = 0$ captures the initial condition automatically.

**Why this is profound:** Every other ODE method handles initial conditions *after* finding the general solution. The Laplace transform absorbs them *during* the solve — they're part of the algebra from the start. The second derivative version $\mathcal{L}\\{f''(t)\\} = s^2 F(s) - s\,f(0) - f'(0)$ bakes in both $y(0)$ and $y'(0)$.

**The eigenbasis perspective:** In the eigenbasis of differentiation, the derivative operator is diagonal — it just multiplies by $s$. This is exactly what diagonalizing a matrix does: $P^{-1}AP = D$ turns the operator into multiplication by eigenvalues. The Laplace transform is the infinite-dimensional version of that diagonalization.

### When to Use Laplace vs Power Series — The Decision Tree

The Laplace transform works by decomposing into exponentials $e^{st}$, which are eigenfunctions of $d/dt$. But they're only eigenfunctions when the coefficients of the ODE are **constant**. If you have $t \cdot y''$, the Laplace transform of that product becomes a derivative of $Y(s)$ in the $s$-domain — you've traded one ODE for another, defeating the purpose.

Variable coefficients like the $x$ in $y'' + xy = 0$ break the eigenstructure. No amount of algebraic cleverness will fix this — you need a fundamentally different approach (power series), building the solution coefficient by coefficient.

**Decision rule:** Constant coefficients + IVP → Laplace (or characteristic equation). Variable coefficients → power series. Piecewise/impulsive forcing → Laplace is uniquely powerful.

**ML connection:** This mirrors a recurring theme in ML — choosing the right representation for the problem. Fourier/spectral methods work beautifully when the problem has translation symmetry (constant coefficients), but you need local methods (like finite elements, or in this analogy power series) when the structure varies across the domain.

### Power Series: Initial Conditions Are the Seeds, Recurrence Is the Growth Rule

The recurrence relation generates $a_2, a_3, a_4, \ldots$ but it cannot generate $a_0$ or $a_1$. Those **always** come from the initial conditions: $y(0) = a_0$, $y'(0) = a_1$. The recurrence propagates from those seeds — it's a machine that takes the starting values and builds every subsequent coefficient from them.

This is why power series solutions naturally have two free parameters ($a_0$ and $a_1$) when no initial conditions are given — exactly matching the two-parameter family of solutions for a second-order ODE.

### Multiplying by $x$ Shifts the Recurrence Index Backward

When $xy$ appears in an ODE, the multiplication by $x$ bumps every $x^n$ to $x^{n+1}$. Re-indexing to match powers of $x^n$ means substituting $n \to n-1$, so the coefficient of $x^n$ in the $xy$ term is $a_{n-1}$, not $a_n$.

This "reach-back" is what creates the gap in the recurrence. For the Airy equation $y'' + xy = 0$, the recurrence connects $a_{n+2}$ to $a_{n-1}$ — a gap of **three** indices. Since $a_1 = 0$ and $a_2 = 0$ (from initial conditions and the orphan term), those zeros propagate through the $a_1$-chain and $a_2$-chain forever, leaving only every third coefficient nonzero.

**Diagnostic:** If you got $a_n$ instead of $a_{n-1}$, you're solving $y'' + y = 0$ (no variable coefficient), which has the closed-form solution $\cos x$ — a completely different equation.

### Orphan Terms Exist Because Sums Have Different Starting Indices

When combining $y'' = \sum_{n=0}^{\infty} (n+2)(n+1) a_{n+2} x^n$ with $xy = \sum_{n=1}^{\infty} a_{n-1} x^n$, the first sum starts at $n = 0$ but the second starts at $n = 1$. At $n = 0$, only the $y''$ sum contributes — the $xy$ sum simply hasn't started yet. That lone $n = 0$ term is the **orphan**.

The orphan produces a separate equation ($2a_2 = 0$) that is not part of the recurrence — it lives at a different value of $n$. The recurrence only governs $n \geq 1$, where both sums overlap and can be combined.

**General principle:** Whenever you combine sums with different starting indices, check which terms have a partner and which are alone. The orphans give you extra equations; the overlap gives you the recurrence.

### Direct Table Entry vs the Shifting Theorem

$\frac{1}{s-a} \to e^{at}$ is a **fundamental table entry**, not a shifted version of something else. The first shifting theorem *extends* this base entry to handle products like $e^{at}\sin(\omega t)$ — cases where you recognize a known $s$-domain pattern that's been displaced from its usual position.

**When to use the shifting theorem:** You see something like $\frac{s+1}{(s+3)^2 + 16}$ and recognize it as the $\frac{s}{s^2+16}$ pattern (which gives $\cos(4t)$) shifted by $a = -3$. The machinery of "complete the square, rewrite numerator in terms of $(s-a)$" is the shifting theorem in action.

**When NOT to use it:** $\frac{1}{s+3}$ is already directly in the table as $e^{-3t}$. No shifting needed — you're reading the answer straight off.

**The relationship:** $\frac{1}{s-a}$ is the entry the shifting theorem is *built on*. The theorem says "if you know $F(s) \to f(t)$, then $F(s-a) \to e^{at}f(t)$." The exponential table entry is the special case where $F(s) = 1/s$ (i.e., $f(t) = 1$).

### Differentiation Is Convolution — The Laplace Transform Reveals It

The derivative property says differentiation in time becomes multiplication by $s$ in the $s$-domain: $\mathcal{L}\{f'(t)\} = sF(s)$. The convolution theorem says multiplication in the $s$-domain is convolution in the time domain: $\mathcal{L}^{-1}\{F \cdot G\} = f * g$. Chain them together and you get: **differentiation is convolution**.

Here's the proof. Start from $\mathcal{L}\{\delta(t)\} = 1$ — the sifting property evaluates $e^{-st}$ at $t = 0$, giving 1. Apply the derivative property to $\delta$ itself: $\mathcal{L}\{\delta'(t)\} = s \cdot \mathcal{L}\{\delta(t)\} = s \cdot 1 = s$. So the function whose Laplace transform is $s$ is $\delta'(t)$.

Now look at $sF(s)$. This is a product of two Laplace transforms: $s = \mathcal{L}\{\delta'\}$ and $F(s) = \mathcal{L}\{f\}$. By the convolution theorem, the inverse is a convolution: $f'(t) = (\delta' * f)(t)$.

Differentiation is convolution with $\delta'(t)$ — the derivative of the impulse. All of calculus (differentiation, integration, solving ODEs) can be reframed as convolutions with the right kernel. The Laplace transform reveals this structure because it turns every time-domain operation into multiplication, and every multiplication corresponds to a convolution.

**ML connection:** Convolutional layers in neural networks apply a learned kernel to extract features. Differentiation is the special case where the kernel is $\delta'$ — a fixed "edge detector." The network learns kernels that generalize this: some detect edges (like derivatives), some detect textures, some detect more abstract patterns. The math is the same convolution operation throughout.

### Full Convolution vs One-Sided Convolution — Why the Limits Change

There are two versions of convolution. The full version (used in signal processing, Fourier analysis, CNNs) integrates from $-\infty$ to $\infty$. The Laplace version integrates from $0$ to $t$. They're the same operation — the limits collapse because of causality.

Start with the full convolution: $(f * g)(t) = \int_{-\infty}^{\infty} f(\tau)\,g(t-\tau)\,d\tau$. Now assume both functions are **causal** — zero for negative arguments (nothing happens before $t = 0$). This kills the integrand in two regions. When $\tau < 0$: $f(\tau) = 0$ because $f$ is zero for negative inputs — this moves the lower limit from $-\infty$ to $0$. When $\tau > t$: the argument $t - \tau$ is negative, so $g(t-\tau) = 0$ — this moves the upper limit from $\infty$ to $t$. The only region where both factors are nonzero is $0 \leq \tau \leq t$, giving the one-sided form: $\int_0^t f(\tau)\,g(t-\tau)\,d\tau$.

The CNN version uses the full integral because there's no "start time" — an image extends in all directions and the filter slides across the entire thing. The Laplace version uses the one-sided form because ODEs have initial conditions at $t = 0$ and the system doesn't exist before that.

---

---

## Lesson 18 — Systems of ODEs and Phase Portraits

### Eigenvectors Decouple Systems — The Chain That Connects Everything

The entire method for solving $\frac{d\mathbf{x}}{dt} = A\mathbf{x}$ is one chain: **Coupled system** → diagonalize with eigenvectors → **decoupled system** → separate variables → **exponentials** → transform back.

Each link uses something you already know: eigenvectors from Phase 1 decouple the directions, separation of variables from Lesson 15 solves each one, and superposition (linearity) from Lesson 16 lets you add them back together. The formula $\mathbf{x}(t) = c_1 e^{\lambda_1 t}\mathbf{v}_1 + c_2 e^{\lambda_2 t}\mathbf{v}_2$ isn't a guess — it's the inevitable result of diagonalizing. Each term is one independent mode: motion along eigenvector direction $\mathbf{v}$, at the exponential rate set by eigenvalue $\lambda$.

The shortcut (write the solution directly, solve for $c_1, c_2$ from initial conditions) works because it skips the intermediate $\mathbf{z}$ coordinates and jumps to the end result. The full diagonalization route explains *why* it works; the shortcut just uses the fact.

### Phase Portraits: Time Is Not An Axis

The most common confusion with phase portraits: both axes are state variables ($x_1$ and $x_2$). Time is invisible — it's the parameter that moves you along a trajectory. Each curve is a path through state space, and the arrows show which direction $t$ is increasing. The portrait doesn't show *when* you're at each point, just *where* you go.

Every trajectory in a phase portrait is the same system (same $A$, same eigenvalues) with different initial conditions (different $c_1, c_2$). The portrait is the complete picture: "for this system, here's what happens from every starting point."

### Which Eigenvector Dominates — Fast vs Slow

In a stable node ($\lambda_1 = -1$, $\lambda_2 = -4$): as $t \to \infty$, the fast mode $e^{-4t}$ dies first, leaving only the slow mode $e^{-t}$. So trajectories **approach** along the slow eigenvector. The fast mode is gone by the time you're near the origin.

In an unstable node: the fast growing mode $e^{4t}$ dominates at large $t$, so trajectories **escape** along the fast eigenvector.

In a saddle ($\lambda_1 = 1$, $\lambda_2 = -3$): the decaying mode pulls you toward the origin along the stable eigenvector, but eventually the growing mode takes over and you escape along the unstable eigenvector. The sign of $c_1$ determines which direction you escape — positive $c_1$ means $+\mathbf{v}_1$, negative means $-\mathbf{v}_1$.

### Complex Eigenvalues = Rotation + Scaling

$e^{(\alpha + \beta i)t} = e^{\alpha t} \cdot e^{i\beta t}$. The imaginary part $\beta$ controls rotation speed. The real part $\alpha$ controls whether the radius shrinks ($\alpha < 0$, stable spiral), grows ($\alpha > 0$, unstable spiral), or stays constant ($\alpha = 0$, center). This is the same damped oscillator from Lesson 16 — complex roots there gave $e^{\alpha t}(c_1\cos\beta t + c_2\sin\beta t)$, which is exactly a spiral in disguise.

### The Matrix Exponential Is the Scalar Exponential Generalized

$\frac{dy}{dt} = ky$ → $y = e^{kt}y(0)$. $\frac{d\mathbf{x}}{dt} = A\mathbf{x}$ → $\mathbf{x} = e^{At}\mathbf{x}(0)$. Same formula, but $e^{At}$ is defined by the Taylor series of the exponential applied to a matrix. Diagonalization makes it computable: $e^{At} = Pe^{Dt}P^{-1}$, which just exponentiates each eigenvalue separately. The eigenvalue method and the matrix exponential are the same thing in different notation.

### A Unit Vector's Derivative Is Always Perpendicular To Itself

If $\hat{u}$ is any unit vector that varies (with $t$, $s$, whatever), then $\frac{d\hat{u}}{dt} \perp \hat{u}$. Proof: $\hat{u} \cdot \hat{u} = 1$, differentiate both sides, get $2\hat{u} \cdot \frac{d\hat{u}}{dt} = 0$. This is the reason $\hat{N}$ exists — $d\hat{T}/ds$ must be perpendicular to $\hat{T}$ because $\hat{T}$ is unit length. The constraint "constant magnitude" forces all change to be directional. Same principle applies to normalized weight vectors in ML: updates must be tangent to the unit sphere, never radial.

### Dotting With a Unit Vector Extracts the Scalar Coefficient

If you know $\mathbf{v} = \lambda\hat{N}$ (some scalar times a unit vector), dot both sides with $\hat{N}$: $\mathbf{v} \cdot \hat{N} = \lambda(\hat{N} \cdot \hat{N}) = \lambda$. This is how the torsion formula $\tau = -\frac{d\hat{B}}{ds} \cdot \hat{N}$ works — you prove $d\hat{B}/ds$ must be parallel to $\hat{N}$, then dot with $\hat{N}$ to extract the scalar. Same principle as projecting onto any orthonormal basis vector: the dot product "picks out" the component.

### Curvature = Bending, Torsion = Twisting — Two Independent Measurements

$\kappa = |d\hat{T}/ds|$ measures how fast the direction of travel rotates — bending within the osculating plane. $\tau = -\frac{d\hat{B}}{ds} \cdot \hat{N}$ measures how fast the osculating plane itself rotates — twisting out of that plane. A circle has $\kappa > 0$, $\tau = 0$ (bends but doesn't twist). A helix has both $\kappa > 0$ and $\tau \neq 0$ (bends AND twists). A straight line has $\kappa = 0$ (no bending at all). These are genuinely independent — you can have any combination.

### Constant Speed ≠ Zero Acceleration

Uniform circular motion: constant speed but $\mathbf{r}'' = \kappa v^2 \hat{N} \neq 0$. What's zero is $a_T = \frac{d|\mathbf{r}'|}{dt}$ (rate of change of speed), not $\mathbf{r}''$ (rate of change of velocity). Speed is a scalar, velocity is a vector. Speed can be constant while direction changes, and changing direction requires acceleration. Only a straight line at constant speed gives $\mathbf{r}'' = 0$.

### Arc Length Parameterization Strips Out Speed, Leaving Pure Geometry

The parameter $t$ mixes geometry with kinematics — "the curve turns sharply here" looks the same as "I'm moving slowly here" when you look at how fast the parameter changes. Reparameterizing by arc length $s$ forces unit speed ($|d\mathbf{r}/ds| = 1$), so everything that remains is purely geometric. That's why curvature is defined as $|d\hat{T}/ds|$ not $|d\hat{T}/dt|$ — per unit distance, not per unit time. In practice you never actually reparameterize; you use the chain rule ($dt/ds = 1/|\mathbf{r}'|$) to convert, or use the cross product formula $\kappa = |\mathbf{r}' \times \mathbf{r}''|/|\mathbf{r}'|^3$ which handles non-unit-speed parameterization automatically.

### Curvature Is a Property of the Path, Not the Traversal

Two particles moving along the same geometric curve at different speeds have the same curvature at each point. Curvature describes the shape of the road, not how fast you're driving. What differs is the normal acceleration $a_N = \kappa v^2$ — the faster you go around the same bend, the harder you're pulled sideways. This is the centripetal acceleration formula $v^2/R$ from physics, since $R = 1/\kappa$.

*Last updated: March 2026 -- through Lesson 19 (3D Geometry, Curves, and Curvature)*









