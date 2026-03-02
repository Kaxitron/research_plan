# Lesson 39: Bayesian Computation — Making the Intractable Tractable

[← Bayesian Foundations](lesson-38-bayesian-foundations.md) | [Back to TOC](../README.md) | [Next: Bayesian Model Comparison →](lesson-40-bayesian-model-comparison.md)

---

> **Why this lesson exists:** The Bayesian posterior P(θ|D) ∝ P(D|θ)P(θ) is beautiful in theory but almost never computable in closed form. For neural networks with millions of parameters, the posterior is a distribution over a million-dimensional space — you can't even write it down, let alone integrate over it. This lesson covers the computational methods that make Bayesian inference practical: MCMC (sampling from the posterior), variational inference (approximating it with a simpler distribution), and the modern hybrids that power Bayesian deep learning.

## 🎯 Core Concepts

### The Computational Problem

- **The posterior** P(θ|D) = P(D|θ)P(θ)/P(D) requires computing P(D) = ∫ P(D|θ)P(θ) dθ — an integral over the entire parameter space. For anything beyond simple conjugate models, this integral is intractable.
- **Two strategies:** (1) **Sample** from the posterior without computing the integral (MCMC). (2) **Approximate** the posterior with a simpler distribution (variational inference).
- **The tradeoff:** MCMC gives exact samples (in the limit) but is slow. VI gives fast approximations but may miss important structure. Modern methods try to get the best of both.

### Markov Chain Monte Carlo (MCMC)

- **The key insight:** you can construct a Markov chain whose stationary distribution IS the posterior. Run the chain long enough, and the samples approximate the posterior — without ever computing the normalizing constant.
- **Metropolis-Hastings algorithm:** propose a new parameter θ' from a proposal distribution. Accept with probability min(1, P(θ'|D)/P(θ|D)) — note the normalizing constants cancel! You only need the unnormalized posterior P(D|θ)P(θ).
- **Gibbs sampling:** a special case where you update one parameter at a time, sampling from the conditional distribution of each parameter given all others. When these conditionals are conjugate, each step is analytical.
- **Practical issues:** burn-in (initial samples before convergence), thinning (reducing correlation between samples), diagnostics (R-hat, effective sample size), mixing (chains should explore the full posterior, not get stuck in one mode).

### Hamiltonian Monte Carlo (HMC) — Physics-Informed Sampling

- **HMC treats the posterior as a potential energy landscape** and simulates a physical system rolling on it. The "ball" explores the landscape efficiently by using gradient information.
- **Leapfrog integration:** HMC uses the gradient ∇log P(θ|D) to simulate Hamiltonian dynamics. The trajectory explores the posterior much more efficiently than random walk proposals — it can travel long distances in parameter space without losing acceptance probability.
- **This IS gradient-based exploration** of the posterior. You already know how to compute gradients (backprop). HMC uses the same gradients but for sampling instead of optimization.
- **NUTS (No-U-Turn Sampler):** automatically tunes the trajectory length, eliminating a key hyperparameter. This is what Stan and PyMC use under the hood.

### Variational Inference (VI) — Optimization Instead of Sampling

- **The idea:** choose a family of simple distributions Q = {q_φ(θ)} (e.g., Gaussians parameterized by mean and variance). Find the member that's closest to the true posterior: φ* = argmin KL(q_φ || P(θ|D)).
- **The ELBO:** since KL divergence involves the intractable P(D), we maximize the **Evidence Lower BOund**: ELBO(φ) = E_{q_φ}[log P(D|θ)] - KL(q_φ || P(θ)). This is tractable: the first term is the expected log-likelihood (estimated by sampling from q), and the second is the KL from the prior (often analytical for Gaussians).
- **ELBO = log P(D) - KL(q || posterior).** Maximizing ELBO simultaneously (a) makes q close to the posterior and (b) provides a lower bound on the evidence. The gap is the KL divergence from q to the true posterior.
- **Mean-field approximation:** assume q factors as a product of independent distributions for each parameter. This is crude — it ignores all correlations — but fast and often surprisingly effective.

### The VAE Connection — Neural Networks Meet Bayesian Inference

- **A Variational Autoencoder** is VI applied to a generative model. The encoder network outputs the variational parameters φ(x); the decoder is the likelihood P(x|z); the latent z plays the role of θ.
- **The VAE loss IS the negative ELBO:** reconstruction loss (expected log-likelihood) + KL penalty (KL from approximate posterior to prior). You've been doing variational inference every time you train a VAE.
- **The reparameterization trick** from Lesson 16 makes the ELBO differentiable with respect to the encoder parameters, enabling gradient-based optimization.

### Laplace Approximation — The Quick-and-Dirty Bayesian

- **Find the MAP estimate** θ_MAP (the posterior mode). Approximate the posterior as a Gaussian centered at θ_MAP with covariance equal to the inverse Hessian: P(θ|D) ≈ N(θ_MAP, H⁻¹). This is just the second-order Taylor expansion of the log-posterior.
- **Cheap but limited:** requires only the Hessian at the MAP (which you might already have from optimization). But it can't capture multimodality, skewness, or heavy tails.
- **For neural networks:** the Hessian is huge (d×d for d parameters), but low-rank approximations and diagonal approximations make this feasible. This connects to the Kronecker-factored approximate curvature (K-FAC) you'll see in neural network optimization.

## 📺 Watch — Primary

1. **StatQuest — "Markov Chain Monte Carlo" and "Metropolis-Hastings"**
   - *Clear step-by-step walkthrough of the algorithm.*
2. **Mutual Information — "Variational Autoencoders"**
   - *Connects VAE training to variational inference in an accessible way.*

## 📺 Watch — Secondary

3. **Michael Betancourt — "A Conceptual Introduction to Hamiltonian Monte Carlo"**
   - YouTube lecture or his excellent paper of the same name. Deep physical intuition.

## 📖 Read — Primary

- **"Bayesian Data Analysis" by Gelman et al.** — Chapters 10–12 (MCMC methods)
- **"Pattern Recognition and Machine Learning" by Bishop** — Chapter 10 (Variational inference)
- **"A Conceptual Introduction to Hamiltonian Monte Carlo" by Betancourt**
  - https://arxiv.org/abs/1701.02434

## 🔨 Do

- **Metropolis-Hastings from scratch:** sample from a bimodal distribution P(x) ∝ exp(-x²) + exp(-(x-5)²). Watch the chain jump between modes. Tune the proposal variance — too small means slow mixing, too large means low acceptance.
- **HMC from scratch:** implement leapfrog integration for the same bimodal distribution. Compare efficiency (effective samples per gradient evaluation) with random walk MH.
- **Variational inference on 2D Gaussian:** fit a diagonal Gaussian q(θ) to a correlated 2D posterior. See the mean-field approximation miss the correlation. Then fit a full-covariance Gaussian and see it capture it.
- **Bayesian neural network:** train a small BNN on a 1D regression task using either MCMC (for a tiny network) or VI (mean-field Bayes-by-Backprop). Plot the predictive uncertainty — it should widen where you have no data.
- **Probabilistic programming with NumPyro (supplementary — from Bayesian Computation book gap analysis):** take your hand-rolled Metropolis-Hastings Beta-Binomial model and rewrite it in NumPyro (JAX-based, same ecosystem you'll use for ML). Fit the same model with NUTS (NumPyro's default sampler). Compare: (a) your M-H samples vs. NUTS samples — NUTS should mix much faster, (b) wall-clock time, (c) effective sample size. Then fit a simple Gaussian model: `mu ~ Normal(0, 10); sigma ~ HalfNormal(5); y ~ Normal(mu, sigma)`. The point isn't to learn NumPyro's API exhaustively — it's to have a working tool for when you need to test Bayesian ideas quickly during your research. NumPyro over PyMC because it runs on JAX, which you'll already be using for ML.
  ```python
  # Minimal NumPyro example to get started:
  import numpyro, numpyro.distributions as dist
  from numpyro.infer import MCMC, NUTS
  import jax.random as random
  
  def model(data):
      theta = numpyro.sample("theta", dist.Beta(1, 1))
      numpyro.sample("obs", dist.Binomial(1, theta), obs=data)
  
  mcmc = MCMC(NUTS(model), num_warmup=500, num_samples=1000)
  mcmc.run(random.PRNGKey(0), data=your_data)
  mcmc.print_summary()
  ```
- **MCMC diagnostics — learn to spot bad chains (supplementary):** deliberately break your M-H sampler three ways: (1) set proposal σ = 0.001 (chains get stuck — trace plot looks like a flatline with rare jumps), (2) set proposal σ = 100 (chains reject almost everything — trace plot looks like a flatline that barely moves), (3) run only 50 iterations (not enough samples). For each, plot the trace, compute the acceptance rate, and compute R-hat across 4 chains. Then fix σ to a good value and run 4 chains — verify R-hat ≈ 1.0 and the trace plots look like "hairy caterpillars" (good mixing). Also compute effective sample size (ESS) — if ESS << total samples, you're wasting computation. ArviZ (`az.plot_trace`, `az.summary`) makes this easy. Knowing what bad chains look like prevents you from trusting garbage posteriors.
- **Hierarchical / multilevel model (supplementary):** this is the most important Bayesian concept your curriculum was missing. The setup: 10 different attention heads are tested for a specific behavior (e.g., "does this head attend to the previous token?"). Each head is tested on a different number of examples (some 5, some 500). Estimate the "success rate" for each head using three approaches:
  - **No pooling:** estimate each head independently (θ̂ᵢ = successes_i / trials_i). The heads with 5 trials have huge uncertainty.
  - **Complete pooling:** treat all heads as identical (θ̂ = total_successes / total_trials). Throws away individual variation.
  - **Hierarchical model:** each head has its own θᵢ, but they're drawn from a shared population: θᵢ ~ Beta(α, β), and you learn α, β from the data. Heads with few trials get "pulled" toward the population mean (shrinkage), while heads with lots of data keep their individual estimates.
  
  Implement in NumPyro. Plot the three sets of estimates. The hierarchical estimates should sit between no-pooling and complete-pooling, with low-data heads showing the most shrinkage. This is partial pooling, and it's the correct approach whenever you're analyzing behavior across many units (heads, layers, models, prompts).
- **Laplace approximation — watch it work, then watch it fail (supplementary — bridge to SLT):** 
  - **Part 1 (it works):** fit a Gaussian model to 1D data. Find the MAP (posterior mode). Compute the Hessian of the negative log-posterior at the MAP. The Laplace approximation says: posterior ≈ N(MAP, H⁻¹). Compare this Gaussian approximation with the true posterior (which is also Gaussian for this conjugate case). They should match perfectly.
  - **Part 2 (it fails — multimodality):** fit a 2-component Gaussian mixture: p(x) = 0.5·N(-3, 1) + 0.5·N(3, 1). The true posterior over the mixture weight is bimodal. Compute the Laplace approximation — it's a single Gaussian centered at one mode. It completely misses the other mode. Draw samples from both the Laplace approximation and the true posterior. See the Laplace approximation's catastrophic failure.
  - **Part 3 (it fails — singularity, the SLT preview):** build a tiny neural network with 2 hidden units. Train it, then permute the two hidden units' weights. You get the SAME function — this is a parameter symmetry. At the symmetry point, the Hessian has a zero eigenvalue (the direction along which permutation doesn't change the function). The Laplace approximation assumes a non-degenerate Hessian — so it breaks. Compute the Hessian, show the near-zero eigenvalue, and compute the resulting (degenerate) Laplace approximation. This is exactly what BIC gets wrong about neural networks, and exactly what Singular Learning Theory fixes. When you reach Lesson 58 (SLT), you'll already know viscerally why regular model selection fails.


## 🔗 ML & Alignment Connection

- **VAEs** = neural variational inference. **Diffusion models** = score matching (closely related to VI). Understanding this lesson means understanding the probabilistic foundations of the two most important generative model families.
- **Bayesian optimization** (for hyperparameter tuning) uses Gaussian process posteriors — these are computed using the exact formulas from this lesson.
- **Uncertainty quantification** in safety-critical applications (medical AI, autonomous driving) requires Bayesian or Bayesian-approximate methods from this lesson.

- **Honest uncertainty** requires the full posterior, not just a point estimate. An AI system that can report "I'm 70% confident" rather than just "my best guess is..." is more transparent and controllable.
- **Bayesian model averaging** (integrating over the posterior rather than using a point estimate) is more robust to model misspecification — it averages over models rather than betting on one. This is a safety property.