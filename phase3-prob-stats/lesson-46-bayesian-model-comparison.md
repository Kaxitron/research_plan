# Lesson 46: Bayesian Model Comparison and the Free Energy Principle — Occam's Razor from Math

[← Bayesian Computation](lesson-45-bayesian-computation.md) | [Back to TOC](../README.md) | [Next: Causal Inference →](lesson-47-causal-inference.md)

---

> **Why this lesson exists:** How do you decide which model is better — a simple one that might underfit, or a complex one that might overfit? Bayesian model comparison gives a principled answer: the **marginal likelihood** P(D) automatically penalizes complexity. This is Occam's razor as a theorem, not a heuristic. It's also the mathematical foundation of Singular Learning Theory, which you'll study later — the RLCT (the key quantity in SLT) is precisely the correction term that the marginal likelihood applies to singular models like neural networks.

## 🎯 Core Concepts

### The Marginal Likelihood — Nature's Regularizer

- **P(D|M) = ∫ P(D|θ,M)P(θ|M) dθ** is the **marginal likelihood** (or evidence) for model M. It integrates the likelihood over all possible parameter values, weighted by the prior.
- **Why this penalizes complexity:** a complex model spreads its prior probability over many possible data patterns. For any specific dataset, most of that probability is "wasted" on patterns that didn't occur. A simple model concentrates its prior on fewer patterns — if the data matches one of them, the marginal likelihood is high.
- **Occam's razor as integration:** the integral automatically trades off fit (likelihood) against complexity (how much the prior is "diluted" by unnecessary parameters). This is not a heuristic — it's a mathematical consequence of probability theory.

### Bayes Factors — Comparing Models

- **The Bayes factor** for model M₁ vs M₂ is: BF₁₂ = P(D|M₁)/P(D|M₂). If BF > 1, the data favors M₁.
- **The posterior odds** are: P(M₁|D)/P(M₂|D) = BF₁₂ × P(M₁)/P(M₂). The Bayes factor updates the prior odds to posterior odds.
- **Interpretation scale (Kass & Raftery):** BF 1–3 = barely worth mentioning, 3–20 = positive evidence, 20–150 = strong, >150 = very strong.
- **Unlike p-values,** Bayes factors can support the null hypothesis: BF < 1 means evidence for the simpler model. This is a crucial advantage — frequentist tests can only reject, never confirm.

### The BIC Approximation — Quick Model Comparison

- **BIC = -2 log P(D|θ̂) + k log n** where θ̂ is the MLE, k is the number of parameters, n is the sample size.
- **BIC ≈ -2 log P(D|M)** — the BIC approximates the log marginal likelihood using the Laplace approximation. The k log n term is the complexity penalty.
- **For regular models** (where the Fisher information matrix is non-degenerate), BIC is asymptotically correct. It tells you the effective dimension is k (the parameter count).
- **For neural networks, BIC is WRONG.** Neural networks are singular models — the Fisher information matrix is degenerate at many points. The effective dimension is NOT the parameter count. This is exactly what SLT fixes.

### The WAIC and Cross-Validation — Practical Alternatives

- **WAIC (Watanabe-Akaike Information Criterion):** a Bayesian generalization of AIC that uses the full posterior (not just the MAP). It works for singular models where BIC fails.
- **LOO-CV (Leave-One-Out Cross-Validation):** the gold standard for predictive model comparison. Computationally expensive but can be efficiently approximated using Pareto-smoothed importance sampling (PSIS-LOO).
- **The deep connection:** WAIC and LOO-CV are asymptotically equivalent. Both estimate the model's out-of-sample predictive accuracy — which is what you actually care about.

### Free Energy — The Unifying Concept

- **The free energy** F = -log P(D|M) = -log ∫ P(D|θ)P(θ) dθ. This is the negative log marginal likelihood. Minimizing free energy = maximizing evidence = selecting the model that best explains the data with the least complexity.
- **The variational free energy** (from Lesson 39): F_var = -ELBO = -E_q[log P(D|θ)] + KL(q||prior). This is an upper bound on the true free energy. VI minimizes this bound.
- **BIC approximates the free energy** for regular models: F ≈ nL(θ̂) + (k/2)log n where L is the negative log-likelihood per data point.
- **SLT corrects the free energy** for singular models: F ≈ nL(θ̂) + λ log n - (m-1) log log n where λ is the RLCT (Real Log Canonical Threshold) and m is the multiplicity. The RLCT replaces k/2 — it's the TRUE effective dimension. For neural networks, λ < k/2, meaning they're simpler than their parameter count suggests.

### The SLT Preview — Why This Matters for Neural Networks

- **Regular models:** the loss landscape near the optimum looks like a bowl (non-degenerate Hessian). BIC works. Effective dimension = parameter count.
- **Singular models (neural networks):** the loss landscape near the optimum has flat directions, ridges, and singularities. BIC fails. Effective dimension < parameter count, determined by the geometry of the singularities.
- **The RLCT** measures the effective dimension by looking at how the loss landscape's singularities resolve under "blow-up" (a technique from algebraic geometry). You'll learn this properly in Lesson 53 (SLT) and Lesson 63 (Algebraic Geometry). For now, know that the free energy framework gives the right vocabulary: model comparison for singular models requires going beyond parameter counting.

## 📺 Watch — Primary

1. **Neel Nanda / Jesse Hoogland — SLT introductory talks** (YouTube)
   - *For the SLT motivation. You won't understand all the details yet, but see where this is heading.*
2. **Statistical Rethinking — "Model Comparison" lectures by McElreath**
   - *Practical Bayesian model comparison with worked examples.*

## 📖 Read — Primary

- **"Statistical Rethinking" by McElreath** — Chapter 7 (Model comparison, WAIC)
- **"Bayesian Data Analysis" by Gelman et al.** — Chapter 7 (Model checking and comparison)
- **"Algebraic Geometry and Statistical Learning Theory" by Watanabe** — Chapter 1 (Introduction only)
  - *Dense but essential. Read the introduction to understand what the free energy formula is trying to correct.*

## 📖 Read — Secondary

- **"Practical Bayesian Model Evaluation Using Leave-One-Out Cross-Validation and WAIC" by Vehtari et al.**
  - https://arxiv.org/abs/1507.04544

## 🔨 Do

- **Bayesian model comparison:** generate data from a cubic polynomial. Fit linear, quadratic, and cubic models. Compute marginal likelihoods (using conjugate priors or numerical integration). Show that the Bayes factor correctly selects the cubic model — and correctly penalizes a 10th-degree polynomial even though it fits better.
- **BIC vs true marginal likelihood:** for the same models, compare BIC with the actual marginal likelihood (computed numerically). They should approximately agree for regular models.
- **WAIC implementation:** compute WAIC for a Bayesian regression model. Compare with LOO-CV.
- **Parameter counting fails:** build a neural network with redundant parameters (e.g., two hidden units that are copies of each other). Show that the parameter count doubles but the effective complexity doesn't. This is why BIC fails for neural networks.
- **Free energy decomposition:** for a simple model, decompose the log marginal likelihood into goodness-of-fit and complexity terms. Show the complexity penalty growing with model size.

## 🔗 ML & Alignment Connection

- **The training loss is not a good model comparison metric** — it always favors more complex models. The marginal likelihood (or its approximations like WAIC) is the principled alternative.
- **SLT will give you the correct complexity measure** for neural networks. This lesson provides the Bayesian framework; SLT provides the geometric correction.
- **The free energy principle** in neuroscience (Karl Friston) proposes that the brain minimizes variational free energy. Whether or not this is correct about brains, it's mathematically equivalent to Bayesian model selection.

- **Model selection as alignment selection:** if you can compute the marginal likelihood for different training objectives, you can select the objective that best explains desired behavior with the least complexity. This is a principled approach to reward modeling.
- **Complexity and deception:** if deceptive alignment requires more "effective parameters" than genuine alignment (i.e., higher RLCT), then Bayesian model comparison would automatically penalize it. Understanding whether this is true is an open alignment question — and it requires the SLT framework.