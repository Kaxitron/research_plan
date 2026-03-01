# Exam 3B: Bayesian Deep Dive & Applied Statistics — Answer Key

**The Path to AI Alignment — Lessons 35–39 Comprehensive Assessment**

---

### Question 1 (10 pts)
**(a)** Frequentist: probability is long-run frequency of repeated experiments. Bayesian: probability is degree of belief. "P(this model generalizes to new data) = 0.9" is meaningful to a Bayesian (it quantifies uncertainty about one specific model) but meaningless to a strict frequentist (the model either generalizes or it doesn't — there's no repeatable experiment).

**(b)** MLE: p̂ = 7/10 = **0.7**. Bayesian with Beta(2,2) prior → posterior Beta(2+7, 2+3) = Beta(9, 5). Posterior mean = 9/(9+5) = **9/14 ≈ 0.643**.

**(c)** The Bayesian estimate is pulled toward 0.5 (the prior mean of Beta(2,2)). This is **shrinkage** — the prior regularizes the estimate. As n → ∞, both converge to the true value: the prior gets "overwhelmed" by data.

---

### Question 2 (12 pts)
**(a)** A conjugate prior means the posterior has the same distributional form as the prior. Convenient because you get a closed-form posterior without numerical integration.

**(b)** P(θ|data) ∝ P(data|θ)P(θ) = [C(n,k)θᵏ(1−θ)^(n−k)] · [θ^(α−1)(1−θ)^(β−1)/B(α,β)] ∝ **θ^(α+k−1)(1−θ)^(β+n−k−1)**. This is the kernel of **Beta(α+k, β+n−k)**. ∎

**(c)** Prior Beta(1,1), 8 heads in 10: Posterior = Beta(9, 3). Mean = 9/12 = **0.75**. MLE = 8/10 = 0.80. The uniform prior barely pulls the estimate (toward 0.5).

**(d)** Prior Beta(10,10), same data: Posterior = Beta(18, 12). Mean = 18/30 = **0.6**. The strong prior pulls the estimate significantly toward 0.5 because the prior "contributes" 20 pseudo-observations (10 heads, 10 tails), comparable to the 10 real observations.

---

### Question 3 (10 pts)
**(a)** MAP: θ̂_MAP = argmax_θ P(θ|D) = argmax_θ [P(D|θ)P(θ)] = argmax_θ [log P(D|θ) + log P(θ)].

**(b)** log P(θ) for θ ~ N(0, σ²I) is −‖θ‖²/(2σ²) + const. So MAP = argmax [log P(D|θ) − ‖θ‖²/(2σ²)] = argmin [−log P(D|θ) + ‖θ‖²/(2σ²)]. This is MLE loss + λ‖θ‖² with **λ = 1/(2σ²)**. Larger prior variance σ² → weaker regularization λ.

**(c)** **Laplace prior** P(θ) ∝ exp(−|θ|/b). The log-prior is −|θ|/b, giving L1 penalty. The Laplace distribution has a sharp peak at zero, putting substantial prior probability on θ = 0. This encourages sparsity because the MAP solution can set parameters exactly to zero. The Gaussian prior is smooth at zero, so it shrinks toward zero but never reaches it.

**(d)** Every regularizer implicitly assumes a prior. When you add a penalty to your loss function, you're making a Bayesian assumption about which parameter values are more plausible before seeing data. Understanding this means you can choose regularization principled by asking "what do I believe about my parameters?" rather than blindly tuning hyperparameters.

---

### Question 4 (10 pts)
**(a)** MCMC: draw samples from the posterior by constructing a Markov chain whose stationary distribution is P(θ|D). VI: approximate the posterior with a simpler distribution q(θ) by minimizing KL divergence.

**(b)** The acceptance ratio is P(θ'|D)/P(θ|D) = [P(D|θ')P(θ')/P(D)] / [P(D|θ)P(θ)/P(D)]. **P(D) cancels** in the ratio. You only need the unnormalized posterior ∝ likelihood × prior.

**(c)** ELBO = E_q[log P(D|θ)] − KL(q(θ) ‖ P(θ)). First term: expected log-likelihood under q (data fit). Second term: KL divergence from q to the prior (complexity penalty). Maximizing ELBO finds q that explains the data well while staying close to the prior.

**(d)** VI is used for VAEs because MCMC is too slow for the inner loop of training (you'd need to run a full sampling procedure for every gradient step). VI gives a differentiable objective (the ELBO) that can be optimized with standard gradient descent, enabling end-to-end training.

---

### Question 5 (10 pts)
**(a)** A complex model spreads its prior probability thinly over many possible datasets. For any specific dataset, most of that prior mass is "wasted" on patterns that didn't occur. A simple model concentrates prior mass on fewer patterns — if the data matches, the marginal likelihood is high. Integration automatically trades fit vs. complexity.

**(b)** log P(D|θ̂): maximum log-likelihood (data fit). −(d/2)log(n): complexity penalty (d = parameters, n = samples). BIC says: models are penalized proportionally to their parameter count, with the penalty growing logarithmically with sample size.

**(c)** BIC assumes the model is **regular** — the Fisher information matrix is invertible and the posterior is approximately Gaussian. Neural networks are **singular**: many parameter settings give the same function (symmetries), the Fisher information is singular, and the posterior is NOT Gaussian. BIC's penalty d/2 overcounts complexity.

**(d)** λ = RLCT (Real Log Canonical Threshold), m = multiplicity. λ replaces d/2 as the effective complexity measure. λ ≤ d/2 always for singular models because the singularities create flat directions that reduce effective dimensionality. Neural networks are always singular (permutation symmetry), so λ < d/2, meaning their effective complexity is less than their parameter count — explaining why overparameterized networks generalize.

---

### Question 6 (10 pts)
**(a)** We can only observe one potential outcome per unit. For patient i, we see either the outcome with treatment or without, never both. The individual causal effect (difference between the two potential outcomes) is fundamentally unobservable.

**(b)** Temperature is a **confounder** — it causes both ice cream sales and drowning. Conditioning on temperature blocks this backdoor path, revealing that ice cream has no direct causal effect on drowning. [DAG: Temperature → Ice cream, Temperature → Drowning, with no arrow between Ice cream and Drowning.]

**(c)** Confounder: common cause of X and Y (Z → X, Z → Y). **Control for it** to block the backdoor path. Mediator: on the causal path from X to Y (X → Z → Y). **Don't control** if you want the total effect; **control** only for direct effect. Collider: common effect of X and Y (X → Z ← Y). **Don't control** — conditioning on a collider creates a spurious association.

**(d)** DAG: Model quality (confound) → RLHF training (more resources spent on better models) and Model quality → Safety. Companies that invest in RLHF may also invest more in safety evaluation, pre-training data quality, etc. A proper causal analysis would require randomizing RLHF training (or finding a natural experiment), controlling for model scale and training resources, and measuring safety outcomes on standardized benchmarks.

---

### Question 7 (8 pts)
**(a)** h² = Var(genetic component)/Var(total phenotype) in a specific population in a specific environment. It's the fraction of trait **variation** attributable to genetic **variation** in that population.

**(b)** Misinterpretation 1: h² = 0.8 does NOT mean "80% of an individual's intelligence is determined by genes." Heritability is about population-level variation, not individual causation. Misinterpretation 2: high heritability does NOT mean the trait is immutable to environmental intervention. A trait can be 100% heritable and still respond dramatically to environmental change (example: height is highly heritable, but average height increased dramatically with better nutrition).

**(c)** Heritability measures how much of the variation is genetic given the current range of environments. In a population where everyone has identical environments, ALL variation is genetic → h² ≈ 1. In a population with wildly different environments, more variation is environmental → h² is lower. Example: plant height in a uniform greenhouse (h² ≈ 1) vs. across varied soils (h² < 1).

---

### Question 8 (10 pts)
**(a)** log P(x) = log ∫ P(x,z)dz = log ∫ [P(x|z)P(z)/q(z|x)]q(z|x)dz = log E_q[P(x|z)P(z)/q(z|x)]. By Jensen's inequality: log P(x) ≥ E_q[log P(x|z)P(z)/q(z|x)] = E_q[log P(x|z)] − KL(q(z|x)‖P(z)) = ELBO. The gap is KL(q(z|x)‖P(z|x)).

**(b)** Since ELBO ≤ log P(x), maximizing ELBO pushes log P(x) up (generates better data) while simultaneously minimizing the KL gap (making q a better approximation to the true posterior).

**(c)** E_q[log P(x|z)]: **reconstruction term** — encourages latent codes z to contain enough information to reconstruct x. KL(q(z|x)‖P(z)): **regularization term** — prevents the encoder from producing latent codes too different from the prior (usually N(0,I)), ensuring a smooth, interpolatable latent space.

**(d)** The ELBO = log-likelihood − KL(posterior from prior). This mirrors MAP = log-likelihood − regularizer. The KL term IS the regularizer, and the prior P(z) determines its form. A standard Gaussian prior corresponds to L2 regularization on the latent space. The VAE is doing approximate Bayesian inference with a specific choice of prior and approximate posterior family.

---

### Question 9 (10 pts)
**(a)** Difference = 0.10. p̂ = (30+20)/200 = 0.25. SE ≈ √(0.25·0.75/100 + 0.25·0.75/100) = √(0.00375) ≈ **0.0612**. 95% CI: 0.10 ± 1.96(0.0612) = **0.10 ± 0.12 = (−0.02, 0.22)**. The CI includes zero, so the result is not significant at α = 0.05.

**(b)** Drug group: Beta(1+30, 1+70) = Beta(31, 71). Mean = 31/102 ≈ **0.304**. Placebo: Beta(1+20, 1+80) = Beta(21, 81). Mean = 21/102 ≈ **0.206**.

**(c)** Sample many pairs (p_drug, p_placebo) from their respective posterior distributions. Count the fraction where p_drug > p_placebo. This gives P(drug better | data) directly — a number like "there's a 92% probability the drug is better," which is far more intuitive than a p-value.

**(d)** The frequentist says: "The 95% CI includes zero, so we cannot reject the null hypothesis of no effect." This is a yes/no answer that says nothing about how likely the drug works. The Bayesian says: "There's a ~92% probability the drug is better, with the most likely effect size around 10 percentage points." This directly answers the agency's question with a probability and quantifies uncertainty about the effect size.

---

### Question 10 (10 pts)
**(a)** A GWAS tests ~10⁶ variants simultaneously. At α = 0.05, you'd expect 50,000 false positives by chance alone. **Bonferroni threshold: 0.05/10⁶ = 5 × 10⁻⁸** (genome-wide significance).

**(b)** p = 0.0001 = 10⁻⁴. Bonferroni for 10⁶ tests: 5 × 10⁻⁸. **Does not survive.** For 500,000 tests: 10⁻⁷. Still **does not survive.** The finding is not genome-wide significant.

**(c)** Using a simplified approach: prior odds = 1/999 ≈ 0.001. With a BF ≈ 1000 (approximate for p = 0.0001), posterior odds ≈ 0.001 × 1000 = 1. So posterior probability ≈ **50%**. The skeptical prior dramatically reduces confidence — even strong p-values translate to modest posterior probabilities when most hypotheses are false a priori.

**(d)** GWAS findings often fail to replicate because: (1) the winner's curse — the effect size is overestimated in the discovery sample (variants are "selected" partly because noise inflated their apparent effect), (2) population stratification, and (3) multiple comparisons inflate false positives. Replication in an independent cohort confirms the signal is real and provides unbiased effect size estimates. The winner's curse means the reported OR of 1.2 is likely an overestimate — the true OR may be smaller.
