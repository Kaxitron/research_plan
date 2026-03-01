# Exam 3B: Bayesian Deep Dive & Applied Statistics — Answer Key

**The Path to AI Alignment — Lessons 35–39 Comprehensive Assessment**

---

### Question 1 (10 pts)

**(a)** P(θ|D) ∝ P(D|θ) · P(θ). Posterior (updated belief about parameters after seeing data) ∝ Likelihood (probability of data given parameters) × Prior (initial belief about parameters before data).

**(b)** Posterior mean = α/(α+β) = 8/12 = **0.667**. MLE = 7/10 = 0.70. The Bayesian estimate is pulled toward 0.5 by the uniform prior — a mild shrinkage effect.

**(c)** Posterior mean = 107/210 ≈ **0.510**. The strong prior (effectively 200 "virtual" observations) overwhelms the 10 actual observations. The posterior barely moves from 0.5.

**(d)** Most different with small data and strong priors; they converge as n → ∞ because the likelihood dominates the prior.

---

### Question 2 (12 pts)

**(a)** log P(θ|D) = log P(D|θ) + log P(θ) + const = log P(D|θ) − λ‖θ‖² + const. Maximizing this = maximizing log-likelihood minus λ‖θ‖² = MLE + L2 penalty = **Ridge regression**.

**(b)** P(θ) ∝ exp(−λ‖θ‖₁) — a **Laplace prior** (double exponential).

**(c)** The Gaussian prior (Ridge) is smooth and dome-shaped — it penalizes all parameters equally, shrinking them toward zero but never to exactly zero. The Laplace prior (Lasso) has a sharp peak at zero — it strongly favors parameters being exactly zero, enforcing sparsity. "Everything matters a little" = Gaussian (all parameters small). "Most things don't matter" = Laplace (most parameters zero).

**(d)** Weight decay = L2 regularization = Gaussian prior on weights. We implicitly believe good neural networks have **small weights** — large weights are unlikely a priori. This encodes a preference for smooth, non-extreme functions.

---

### Question 3 (10 pts)

**(a)** MCMC: asymptotically exact samples. Advantage: no approximation error given enough samples. VI: fast optimization-based approximation. Advantage: scales to large datasets/models.

**(b)** The acceptance ratio P(θ'|D)/P(θ|D) = [P(D|θ')P(θ')/P(D)] / [P(D|θ)P(θ)/P(D)] — the P(D) terms cancel. You only need the unnormalized posterior.

**(c)** ELBO = E_q[log P(D|θ)] − KL(q‖P(θ)) = log P(D) − KL(q‖P(θ|D)). Since KL ≥ 0, ELBO ≤ log P(D). It's a lower bound because the gap is exactly the KL divergence between q and the true posterior.

**(d)** In a VAE, θ → latent variables z, D → observed data x, q → the encoder q(z|x) that approximates the true posterior P(z|x). The ELBO becomes: E_q[log P(x|z)] − KL(q(z|x)‖P(z)). The first term is reconstruction quality; the second keeps the encoder close to the prior.

---

### Question 4 (10 pts)

**(a)** A complex model spreads its prior over many possible datasets. For any specific dataset, most of that probability mass is "wasted." A simple model concentrates its prior on fewer patterns — if the data matches, the marginal likelihood is high. The integral automatically trades fit vs. complexity without any explicit penalty term.

**(b)** The −k·log(n) term penalizes parameter count. More parameters → lower BIC score → less preferred, all else equal. It's the information-theoretic "cost" of flexibility.

**(c)** BIC assumes the Fisher information matrix is invertible at the MLE (regularity). For neural networks, the parameter-to-function map is many-to-one (permutation symmetry, etc.), making the Fisher information singular. BIC overstates the effective complexity by using k/2 instead of the true RLCT λ, which can be much smaller.

**(d)** λ ≤ k/2 because singularities reduce effective complexity below parameter count. The symmetries and redundancies in neural networks mean many parameters don't independently contribute to model flexibility. This is why networks with millions of parameters can generalize — their true complexity (measured by λ) is far smaller than their parameter count suggests.

---

### Question 5 (10 pts)

**(a)** DAG: Confounders → Education, Confounders → Health, Education → Income → Health, Education → Health. Backdoor path: Education ← Confounders → Health (a non-causal path from Education to Health through the confounder).

**(b)** A confounder influences both the treatment and the outcome, creating a spurious association. Example: socioeconomic background affects both education level and health outcomes. Without controlling for it, the naive Education→Health effect is biased (includes the confounded path).

**(c)** **Collider bias** (or selection bias). Sicker patients go to hospitals with more ICU beds. The severity of illness confounds the relationship — ICU beds → allocated to sicker patients → higher mortality. The ICU beds don't cause death; they're selected by the very factor that causes death.

**(d)** Alignment requires counterfactual reasoning: "If the AI had been given a different prompt, would it still behave safely?" or "If we hadn't included this safety training, would the model be deceptive?" Decision theory (Lesson 64) asks agents to evaluate counterfactual consequences of actions. Causal inference provides the mathematical framework for making such counterfactual claims rigorous.

---

### Question 6 (10 pts)

**(a)** No — h² is a **population-level** statistic. It means 80% of the variation in height *across the population* is associated with genetic variation. For any individual, genes and environment interact in complex ways. In a different environment, h² could be different.

**(b)** The **missing heritability problem**. Possible explanations: (1) many more SNPs with even smaller effects haven't reached significance threshold, (2) gene-gene interactions (epistasis) aren't captured by additive GWAS, (3) rare variants not well-tagged by common SNPs, (4) structural variants not captured by SNP arrays.

**(c)** Education and income are **mediators** (on the causal path from genes → education → outcome). Controlling for mediators blocks part of the causal effect you're trying to measure, and can open collider paths. This is "bad control" — it introduces bias rather than removing it.

**(d)** When a paper claims "Model X has capability Y based on benchmark Z," we can apply: hypothesis testing (is the improvement statistically significant?), experimental design (was the benchmark properly held out? multiple comparisons?), regression (do results hold after controlling for model size/data?), causal inference (does the training cause the capability, or is it a confounded correlation?).

---

### Question 7 (8 pts)

**(a)** n = number of data points, L* = minimum training loss, k = parameter count, λ = RLCT (real log canonical threshold — effective complexity), log = natural log.

**(b)** Model A: F ≈ nL* + (100/2)log(n) = nL* + 50·log(n). Model B: F ≈ nL* + 30·log(n). Model B has **lower free energy** despite 100× more parameters, because its RLCT (30) is less than A's effective complexity (50). Bayesian model comparison prefers Model B.

**(c)** The effective complexity of a neural network (measured by RLCT λ) is much less than its parameter count k/2, due to symmetries and redundancies — so "too many parameters" overstates the actual model complexity.

---

### Question 8 (10 pts)

**(a)** MLE says defect rate is exactly 0. The CI [0, 0.03] means: if the true rate were 0.03 or higher, seeing 0/100 would be unlikely (< 5%). It does NOT mean we're 95% sure the rate is below 3%.

**(b)** The Bayesian estimate is nonzero because the prior (uniform) assigns some belief to θ > 0 before seeing data. Even 100 perfect tests don't completely eliminate the possibility of defects — they just make it very unlikely. The posterior mean 0.0098 reflects the residual uncertainty.

**(c)** **Bayesian**, because: (1) "no dangerous behavior observed" is exactly the 0/n situation where MLE gives the dangerously overconfident answer θ̂ = 0, (2) we need to quantify residual risk even with no failures, and (3) we have prior knowledge about what kinds of failures are possible. A Bayesian credible interval like [0.0001, 0.036] honestly represents our uncertainty, while the frequentist MLE of 0 could create false confidence in safety.

---

### Question 9 (10 pts)

Five-point critique:

1. **Study design:** How was "deception" operationalized? What's the control condition? Without a clear definition and control, "deceptive capabilities" could mean many things.

2. **P-value interpretation:** p = 0.02 means there's a 2% chance of seeing results this extreme under the null. It does NOT mean there's a 98% chance GPT-5 is deceptive. With the extraordinary nature of the claim, the prior probability of true deception is low, so even p = 0.02 might not move the posterior much (Bayesian reasoning).

3. **Confounders:** Could the observed behavior be explained by prompt sensitivity, pattern matching, or training data contamination rather than genuine deception? Without controlling for these, the causal claim is unsupported.

4. **Bayesian consideration:** The prior probability of genuine deception should be low. By Bayes' theorem, even a low p-value produces a modest posterior when the prior is very small. We need a likelihood ratio large enough to overcome the low prior.

5. **Additional evidence needed:** Replication by independent labs, robustness across different prompts, mechanistic evidence (interpretability showing deception circuits), and ruling out simpler explanations. One p = 0.02 result is insufficient for a claim this consequential.

---

### Question 10 (10 pts)

**(a)** The Bernstein-von Mises theorem assumes the Fisher information matrix is invertible at the true parameter. For singular models, the Fisher information is singular — the posterior doesn't concentrate around a single point but around a set (variety) of optimal parameters. The normal approximation that BvM provides simply doesn't apply.

**(b)** The set K of optimal parameters is a variety with flat directions — directions where you can move without changing the loss. The RLCT λ measures how quickly the loss grows as you move away from K. A smaller λ means the landscape is flatter near K, which is analogous to the "flat minima generalize better" intuition: models near K are robust to perturbation because the loss barely changes.

**(c)** The marginal likelihood integral naturally counts the "volume" of parameter space that achieves good fit. Neural networks, despite having many parameters, have huge symmetry groups that collapse this volume. The RLCT captures this collapse: the effective model complexity is λ, not k/2. So the Bayesian penalty for complexity is much smaller than the raw parameter count suggests, explaining why overparameterized networks aren't penalized as much as classical theory would predict.
