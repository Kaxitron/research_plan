# Intuition Notebook

[Back to TOC](../README.md)

> **What this is:** A running collection of deep intuitions — the "aha" moments and mental models that make concepts click. Unlike the cheat sheet (formulas and facts), this notebook captures the *why* behind things. Add to it whenever something crystallizes.

---

## Linear Algebra

### Matrix-vector multiplication is BOTH row dot products AND linear combination of columns
Both are true simultaneously. The row view tells you "each output is a pattern match." The column view tells you "the output is a weighted mix of the matrix's columns, where the input vector provides the weights." Being able to flip between these perspectives is a superpower — the column view is what makes attention interpretable (the output is a weighted combination of value vectors).

### SVD means every matrix is rotate → scale → rotate
No matter how complicated a matrix looks, it's doing three simple things in sequence. Vᵀ aligns the input with natural axes, Σ stretches along those axes, U rotates the output. The singular values tell you HOW MUCH stretching happens in each direction. If some singular values are zero, dimensions get crushed — that's rank deficiency.

### Eigenvectors are the directions that "survive" a transformation
Most vectors get knocked off their line by a matrix. Eigenvectors stay on their line — they just get stretched by λ. They're the "natural axes" of the transformation. This is why PCA works: the eigenvectors of the covariance matrix ARE the directions of maximum variance.


### Miscellaneous Thoughts
1. Qᵀ = Q⁻¹ only true when columns are orthonormal and matrix is square.
2. v*v is the same things as vᵀv. This is the insight from 3B1B that the dot product of two vectors is the same as a linear transformation.  
3. The diagonal entries of XᵀX are the variance of the features, whereas the off-diagonal values are the correlation of the features.  

---

## Calculus & Optimization

### The gradient is perpendicular to contour lines and points uphill
If you're standing on a hillside, the gradient tells you the steepest uphill direction. Gradient descent goes opposite — steepest downhill. The shape of the contour lines (elongated vs. circular) determines how hard optimization is. Circular = easy (condition number ≈ 1). Elongated = hard (high condition number). This is why preconditioning and Adam optimizer help.

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

*(To be filled as you progress through Phase 5)*

---

## Alignment

*(To be filled as you progress through Phase 6)*

---

*Last updated: Feb 2026*
