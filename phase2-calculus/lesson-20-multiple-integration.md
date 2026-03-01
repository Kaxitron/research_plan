# Lesson 20: Multiple Integration and Change of Variables — Jacobians Meet Probability

[← Loss Landscapes](lesson-19-loss-landscapes.md) | [Back to TOC](../README.md) | [Next: Taylor Expansions →](lesson-21-taylor-expansions.md)

---

> **Why this lesson exists:** Every time you compute an expectation, normalize a probability distribution, or transform random variables, you're doing a multivariable integral. The Jacobian determinant — which you already know as a volume-scaling factor from Lesson 7 — reappears as the essential correction term when you change variables in an integral. This is the mathematical engine behind normalizing flows, reparameterization tricks in VAEs, and the reason certain distributions are conjugate. Without this, the Bayesian computation in Phase 3 will feel like magic; with it, it's just calculus.

## 🎯 Core Concepts

### Double and Triple Integrals — Geometry First

- **A double integral** ∬_R f(x,y) dA computes the "volume under the surface" f over region R. Think of it as stacking infinitely many single integrals. The iterated integral ∫∫ f(x,y) dx dy works from inside out.
- **Fubini's theorem:** you can switch the order of integration (dx dy ↔ dy dx) when f is "nice enough" (continuous). This is surprisingly powerful — sometimes one order is easy and the other is nightmarish.
- **For ML:** computing E[f(X,Y)] = ∬ f(x,y) p(x,y) dx dy is a double integral over the joint density. Marginalizing out Y means ∫ p(x,y) dy — a single integral that "projects" the joint onto X.

### Change of Variables — The Jacobian Returns

- **The key formula:** if you substitute u = g(x,y), v = h(x,y), the integral transforms as:
  ∬ f(x,y) dx dy = ∬ f(g⁻¹(u,v)) |det(J⁻¹)| du dv
  where J is the Jacobian matrix of the transformation (∂(u,v)/∂(x,y)).
- **Polar coordinates** are the classic example: x = r cos θ, y = r sin θ, and the Jacobian determinant is r. That's why the area element becomes r dr dθ.
- **This IS the Lesson 7 determinant** in action: the Jacobian determinant measures how the transformation stretches or compresses volume locally. At each point, it's the factor by which infinitesimal areas change.
- **For probability:** if X has density p_X(x) and Y = g(X), then p_Y(y) = p_X(g⁻¹(y)) |det(dg⁻¹/dy)|. This is how you derive the density of a transformed random variable. Normalizing flows use this formula at every layer.

### The Gaussian Integral and Its Children

- **The foundational integral:** ∫_{-∞}^{∞} e^{-x²} dx = √π. You can't do this with single-variable techniques — the proof uses polar coordinates (change of variables!) on the 2D version ∬ e^{-(x²+y²)} dx dy = π.
- **Every Gaussian calculation** descends from this: the normalization constant of the normal distribution, multivariate Gaussian integrals, moment-generating functions, partition functions. If you understand this one integral, you understand half of probability theory.
- **Multivariate Gaussian:** for p(x) = N(μ, Σ), the normalization involves ∫ exp(-½(x-μ)ᵀΣ⁻¹(x-μ)) dx = (2π)^{d/2} |det(Σ)|^{1/2}. The determinant of the covariance matrix appears because of the change-of-variables Jacobian when diagonalizing Σ using its eigenvectors.

### Monte Carlo Integration — When Integrals Can't Be Solved

- **Most integrals in ML are intractable.** Bayesian posteriors, partition functions, marginal likelihoods — these involve integrals over high-dimensional spaces with no closed form.
- **Monte Carlo idea:** approximate ∫ f(x)p(x) dx by drawing samples x₁,...,xₙ from p and computing (1/n) Σ f(xᵢ). This converges by the law of large numbers, regardless of dimension.
- **Importance sampling:** if you can't sample from p directly, sample from a proposal distribution q and reweight: ∫ f(x)p(x)dx = ∫ f(x)(p(x)/q(x))q(x)dx ≈ (1/n) Σ f(xᵢ)p(xᵢ)/q(xᵢ). This is the foundation of particle filters and some MCMC methods.

## 📺 Watch — Primary

1. **3Blue1Brown — Essence of Calculus, Chapter 8:** "Integration and the fundamental theorem of calculus"
   - https://www.youtube.com/watch?v=rfG8ce4nNh0
   - *The visual connection between area under curves and antiderivatives — foundation for understanding integration in multiple dimensions.*
2. **3Blue1Brown — "The Gaussian integral" (if available)**
   - The polar coordinates proof is a classic visualization opportunity
   - Solid worked examples with geometric intuition

## 📺 Watch — Secondary

2. **Dr. Trefor Bazett — Multivariable Calculus (double/triple integral sections)**
   - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxc_CvEy7xBKRQr6I214QJcd
   - *Clear visual lectures on multiple integration and change of variables. Good for extra worked examples.*

## 📖 Read — Primary

- **"Mathematics for Machine Learning" (MML) by Deisenroth** — Chapter 6.5–6.7 (Change of variables, integrals)
- **Paul's Online Math Notes — Multiple Integrals**

## 🔨 Do

- Compute ∬ x²y dx dy over the unit disk using polar coordinates. Feel the Jacobian factor r appear.
- Derive the PDF of Y = X² when X ~ N(0,1) using the change-of-variables formula. Verify it's a chi-squared distribution with 1 df.
- Implement Monte Carlo estimation of π by sampling random points in [0,1]² and counting those inside the unit circle. Plot convergence vs sample size.
- Compute the normalization constant of a 2D Gaussian with covariance Σ = [[2,1],[1,3]] by diagonalizing Σ and using the change-of-variables formula.

### 💻 Coding Mini-Project: Monte Carlo Integration Library (~50 lines)

Build a reusable Monte Carlo integrator that works on arbitrary functions and dimensions:

```python
def mc_integrate(f, bounds, n_samples=100000):
    """
    Estimate ∫f(x)dx over a rectangular region.
    Args:
        f: callable that takes an (n_samples, d) array → (n_samples,) array
        bounds: list of (low, high) tuples, one per dimension
        n_samples: number of random points
    Returns: (estimate, standard_error)
    """
    ...
```

**Your tasks:**
1. Implement the function (hint: volume × mean of f over random uniform samples)
2. Return both the estimate AND the standard error (so you get confidence intervals)
3. Test on known integrals:
   - `∫₀¹ x² dx = 1/3` (1D sanity check)
   - `∫∫ over unit disk of 1 dA = π` (2D — you'll need rejection sampling or polar trick)
   - `∫₀¹ ∫₀¹ ∫₀¹ e^(xyz) dx dy dz` (3D — check against scipy)
4. Plot: estimate vs n_samples (log scale) for the π example. Verify the error shrinks as 1/√n. Add error bars using your standard error.

**Programming skills practiced:** vectorized numpy, function as argument (higher-order functions), error estimation, log-scale plotting

## 🔗 ML & Alignment Connection

- **Normalizing flows** are literally a chain of change-of-variables transformations, each with a tractable Jacobian determinant. The whole architecture is designed to make this integral formula efficient.
- **The reparameterization trick** in VAEs: instead of sampling z ~ q(z|x), write z = μ + σε where ε ~ N(0,1). This is a change of variables that makes the gradient flow through the sampling step.
- **Bayesian computation** is fundamentally about high-dimensional integrals. Questions like "how confident should we be that this model is safe?" require integrating over possible model behaviors: P(safe) = ∫ P(safe | θ) P(θ | data) dθ. Tractable approximations to these integrals (variational inference, MCMC) are the computational backbone of uncertainty quantification in AI safety.
