# Lesson 51: Fisher Information and Exponential Families

[← MLE (L39)](lesson-39-mle.md) | [Back to TOC](../README.md) | [Next: Information Theory (L40) →](lesson-40-information-theory.md)

---

> **Why this lesson exists:** Fisher information is the curvature of the log-likelihood — it tells you how much information each data point carries about the parameters. It's the foundation of the natural gradient (which outperforms vanilla gradient descent by respecting the geometry of probability distributions), the Cramér-Rao bound (the fundamental limit on estimation accuracy), and information geometry (treating the space of distributions as a Riemannian manifold). Exponential families are the class of distributions where Fisher information and sufficient statistics have their cleanest form — and they include nearly every distribution you'll use in ML: Gaussian, Bernoulli, Poisson, categorical, and more. These concepts bridge statistics, optimization, and differential geometry.

## 🎯 Core Concepts

### Fisher Information — Curvature of Log-Likelihood

- **The score function:** For a parametric model p(x|θ), the score is:

$$s(\theta) = \frac{\partial}{\partial \theta} \log p(x|\theta)$$

- The score has a key property: E[s(θ)] = 0. The expected direction of steepest ascent of log-likelihood is zero — at the true parameter, the likelihood isn't systematically pulling in any direction.

- **Fisher information** is the variance of the score:

$$I(\theta) = E\left[\left(\frac{\partial}{\partial \theta} \log p(x|\theta)\right)^2\right] = -E\left[\frac{\partial^2}{\partial \theta^2} \log p(x|\theta)\right]$$

- **Geometric meaning:** Fisher information measures the **curvature** of the log-likelihood function. High curvature → the likelihood is sharply peaked → data is very informative about θ. Low curvature → the likelihood is flat → data tells you little about θ.

- **Connection to Lesson 19:** The Hessian of the loss landscape determines local curvature (eigenvalues of H). Fisher information IS the expected Hessian of the negative log-likelihood. The loss landscape geometry you studied is Fisher information geometry.

### The Fisher Information Matrix (Multivariate)

- For parameter vector θ ∈ ℝᵈ, the Fisher information matrix is:

$$I(\theta)_{ij} = E\left[\frac{\partial \log p(x|\theta)}{\partial \theta_i} \frac{\partial \log p(x|\theta)}{\partial \theta_j}\right]$$

- This is a d × d positive semidefinite matrix. It defines a **Riemannian metric** on the parameter space — the Fisher metric.
- **Invariance:** The Fisher metric is the unique (up to scaling) metric on distributions that is invariant under reparameterization. If you change coordinates from θ to φ(θ), the Fisher metric transforms correctly. This is why it's the "natural" geometry for probability distributions.

### The Cramér-Rao Lower Bound

- **Statement:** For any unbiased estimator θ̂ of θ:

$$\text{Var}(\hat{\theta}) \geq \frac{1}{nI(\theta)}$$

- **In words:** No unbiased estimator can have variance smaller than 1/(nI). Fisher information sets a fundamental **speed limit** on learning.
- **ML connection:** This tells you the best possible sample efficiency. If a model needs n samples to learn something, the Cramér-Rao bound explains whether that's inherent (because Fisher information is low) or because the estimator is suboptimal.
- **For n i.i.d. observations:** total information = nI(θ). More data → more information → tighter bound → better estimation. The √n convergence rate of MLE comes from this.

### The Natural Gradient — Geometry-Aware Optimization

- **The problem with vanilla gradient descent:** In parameter space, the Euclidean distance |θ − θ'| doesn't capture how different the distributions p(x|θ) and p(x|θ') are. A small change in one parameter might dramatically change the distribution, while a large change in another barely matters.
- **The natural gradient** fixes this by using the Fisher metric:

$$\tilde{\nabla}L(\theta) = I(\theta)^{-1} \nabla L(\theta)$$

- This rescales the gradient by the inverse Fisher information, making the step size appropriate for the geometry of the distribution space.
- **Connection to Lesson 17:** Adam and other adaptive optimizers approximate the natural gradient. Adam's per-parameter learning rate is a diagonal approximation to I(θ)⁻¹. The natural gradient explains *why* Adam works better than vanilla SGD.
- **Connection to Lesson 59:** The Fisher information matrix IS a Riemannian metric tensor on the manifold of distributions. Natural gradient descent IS Riemannian gradient descent. This is the deep connection between statistics and differential geometry.

### Exponential Families — The Universal Framework

- A distribution is in the **exponential family** if it can be written as:

$$p(x|\theta) = h(x) \exp(\eta(\theta)^T T(x) - A(\eta))$$

- **η(θ):** natural parameters
- **T(x):** sufficient statistics — the "summary" of data that captures ALL information about θ
- **A(η):** log-partition function (normalizing constant)
- **h(x):** base measure

- **Almost everything is exponential family:**
  - Gaussian: T(x) = (x, x²), η = (μ/σ², −1/(2σ²))
  - Bernoulli: T(x) = x, η = log(p/(1−p)) (the log-odds!)
  - Poisson: T(x) = x, η = log(λ)
  - Categorical: T(x) = one-hot vector, η = log probabilities

- **Why this matters:**
  - MLE has a beautiful form: just match E[T(x)] to the sample average of T(x)
  - Fisher information = ∇²A(η) — the Hessian of the log-partition function
  - Sufficient statistics T(x) capture ALL information. You can throw away the raw data and keep only T(x) without losing anything for estimation.
  - Conjugate priors (Lesson 35) exist precisely for exponential families

### Sufficient Statistics — What Data Actually Matters

- A statistic T(X) is **sufficient** for θ if P(X|T(X), θ) doesn't depend on θ. In words: once you know T(X), the rest of the data tells you nothing more about θ.
- **For Gaussians:** (sample mean, sample variance) is sufficient for (μ, σ²). The order of the data, which specific values appeared — none of that matters beyond the mean and variance.
- **For ML:** The gradient ∇L(θ; batch) is a sufficient statistic for the batch's contribution to learning. This is why stochastic gradient descent works — each mini-batch's gradient captures all the batch's information about the parameter update.

## 📺 Watch

1. **Mutual Information (YouTube) — "Fisher Information"**
   - Search for "Fisher Information explained" — several good visual explanations
2. **StatQuest — "Maximum Likelihood, clearly explained"** (review with Fisher eyes)
   - Rewatch the MLE explanation and now see the curvature of the log-likelihood as Fisher information
3. **Amari — "Natural Gradient" lectures**
   - Search for Shun-ichi Amari's talks on information geometry and natural gradient

## 📖 Read — Primary

- **MML textbook — Chapter 8.3 (Exponential Families)**
  - Concise treatment with ML applications
- **"Natural Gradient Works Efficiently in Learning" by Amari (1998)**
  - https://ieeexplore.ieee.org/document/6790500
  - *The foundational paper on natural gradient. Short and readable.*

## 📖 Read — Secondary

- **"Information Geometry and Its Applications" by Amari** — Chapter 1
  - The definitive treatment of how Fisher information creates a Riemannian geometry on probability distributions
- **"Pattern Recognition and Machine Learning" by Bishop** — Section 2.4 (Exponential Family)
  - Clear, standard treatment with examples

## 🔨 Do

- **Fisher information for a coin:** for Bernoulli(p), compute I(p) analytically. Plot I(p) vs p. Notice it's highest near p=0 and p=1 (extreme probabilities are hard to estimate precisely) and lowest at p=0.5. Explain intuitively why.
- **Fisher information for a Gaussian:** compute the 2×2 Fisher information matrix for N(μ, σ²). Show that μ and σ² are "orthogonal" in the Fisher metric (the off-diagonal entries are zero). What does this mean for estimation?
- **Natural gradient experiment:** implement natural gradient descent for logistic regression. Compare convergence speed with vanilla gradient descent and Adam on a simple dataset. Show that natural gradient handles different parameterizations equally well.
- **Exponential family toolkit:** for Bernoulli, Gaussian, and Poisson, write each in exponential family form. Identify η, T(x), A(η), and h(x). Verify that ∂A/∂η = E[T(x)] and ∂²A/∂η² = Var[T(x)] = I(η).
- **Key exercise:** the Cramér-Rao bound for a Bernoulli(p) coin is Var(p̂) ≥ p(1−p)/n. For p = 0.5 and n = 100, what's the minimum variance? Compute the actual variance of the MLE (sample proportion). Verify that MLE achieves the bound (it's *efficient*).

## 🔗 ML & Alignment Connection

- **The natural gradient** explains why Adam outperforms vanilla SGD: Adam approximately inverts the Fisher information, performing geometry-aware optimization. K-FAC (Kronecker-factored approximate curvature) is an explicit Fisher information approximation used in large-scale training.
- **Singular Learning Theory (Lesson 50)** begins where classical Fisher information breaks down. In singular models (like neural networks), the Fisher information matrix is degenerate (not full rank) at certain parameter values. The RLCT replaces the role of parameter count (which assumes non-degenerate Fisher information). Understanding where Fisher information works and where it fails is essential for SLT.
- **Information geometry and alignment:** the space of all possible reward functions, or all possible policies, forms a manifold with Fisher metric. "How different are two reward functions?" is naturally measured by Fisher distance, not Euclidean distance in parameter space.
- **Sufficient statistics and interpretability:** when a neural network compresses its input, it's computing an approximate sufficient statistic — keeping the information relevant to the task and discarding the rest. Understanding sufficiency helps formalize what a network "knows" and what it ignores.
