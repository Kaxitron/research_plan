# Exam 3A: Core Probability & Frequentist Methods — Answer Key

**The Path to AI Alignment — Lessons 28–34 Comprehensive Assessment**

---

### Question 1 (10 pts)

**(a)** Joint probability P(A,B) = probability both A and B occur. Marginal P(A) = Σ_B P(A,B) = probability of A regardless of B. Conditional P(A|B) = P(A,B)/P(B) = probability of A given B occurred. Relationship: **P(A,B) = P(A|B)P(B) = P(B|A)P(A)**.

**(b)** Bayes: P(disease|positive) = P(positive|disease)P(disease)/P(positive).
P(positive) = P(pos|disease)P(disease) + P(pos|no disease)P(no disease) = 0.95(0.001) + 0.01(0.999) = 0.00095 + 0.00999 = 0.01094.
P(disease|positive) = 0.00095/0.01094 ≈ **0.087 (about 8.7%)**. Despite the test being 95% sensitive and 99% specific, a positive result only means ~9% chance of disease. This is counterintuitive because the disease is so rare (1/1000) that false positives from the healthy majority outnumber true positives from the rare sick population.

**(c)** Prior = P(θ) — beliefs about parameters before seeing data (e.g., regularization). Likelihood = P(data|θ) — how well parameters explain the data (the loss function). Posterior = P(θ|data) — updated beliefs after training. Training is Bayesian updating: start with a prior, observe data, arrive at a posterior.

---

### Question 2 (10 pts)

**(a)** P(k heads) = C(10,k)(0.5)^10. E[X] = np = **5**. Var(X) = np(1−p) = **2.5**.

**(b)** μ is the **mean** (center of the bell curve). σ is the **standard deviation** (width). 68% of probability lies within **μ ± σ**.

**(c)** H = −(0.1 log₂ 0.1 + 0.6 log₂ 0.6 + 0.2 log₂ 0.2 + 0.1 log₂ 0.1) = −(0.1(−3.322) + 0.6(−0.737) + 0.2(−2.322) + 0.1(−3.322)) = 0.332 + 0.442 + 0.464 + 0.332 = **1.57 bits**.

**(d)** Maximum entropy for 4 classes (uniform [0.25, 0.25, 0.25, 0.25]) = log₂(4) = **2.0 bits**. The model's entropy (1.57) is below maximum, meaning it's moderately confident — it concentrates probability on class 2 (0.6) but retains meaningful uncertainty about the others.

---

### Question 3 (12 pts)

**(a)** L(μ) = Π (1/√(2πσ²)) exp(−(xᵢ−μ)²/(2σ²)). ℓ(μ) = −n/2 ln(2πσ²) − Σ(xᵢ−μ)²/(2σ²).

**(b)** dℓ/dμ = Σ(xᵢ−μ)/σ² = 0 → Σxᵢ = nμ → **μ̂ = (1/n)Σxᵢ = x̄** ✓

**(c)** ∂ℓ/∂(σ²) = −n/(2σ²) + Σ(xᵢ−μ̂)²/(2σ⁴) = 0 → **σ̂² = (1/n)Σ(xᵢ−x̄)²**. This is biased: E[σ̂²] = (n−1)/n · σ². It slightly underestimates variance. The unbiased estimator divides by n−1 (Bessel's correction).

**(d)** The likelihood is P(data|θ) = Π p̂(yᵢ|xᵢ;θ). Taking the log: log L = Σ log p̂(yᵢ|xᵢ;θ). Maximizing this = minimizing −Σ log p̂(yᵢ|xᵢ;θ), which is exactly the cross-entropy loss. **Cross-entropy training IS MLE.**

---

### Question 4 (10 pts)

**(a)** Entropy measures the **average information content** (or uncertainty) of a distribution. H(fair coin) = −(0.5 log₂ 0.5 + 0.5 log₂ 0.5) = **1 bit**.

**(b)** DKL(P‖Q) ≥ 0 by **Gibbs' inequality** (or Jensen's inequality applied to the convex function −log). Equality iff P = Q. It's not symmetric because DKL measures how well Q approximates P — the "cost" of using Q when the truth is P — and that cost depends on which direction you're approximating. DKL(P‖Q) penalizes Q for putting low probability where P has high probability; DKL(Q‖P) does the opposite.

**(c)** H(P,Q) = −Σ p(x) log q(x) = −Σ p(x) log p(x) + Σ p(x) log(p(x)/q(x)) = **H(P) + DKL(P‖Q)**. Since H(P) is fixed (it's the data entropy), minimizing H(P,Q) is the same as minimizing DKL(P‖Q) — finding the model Q closest to the truth P in KL sense.

**(d)** Without the KL penalty, the model can deviate arbitrarily from the reference, potentially finding pathological policies that exploit the reward model (reward hacking). The KL penalty keeps the fine-tuned model "close" to the pre-trained model, ensuring it retains general language abilities while adapting to human preferences.

---

### Question 5 (10 pts)

**(a)** H₀: no effect (the status quo). H₁: there is an effect. P-value: probability of observing data at least as extreme as what was actually observed, **assuming H₀ is true**.

**(b)** p = 0.03 **means:** if the new model were truly no better than the baseline, there is a 3% chance of seeing results this favorable (or more) by random chance alone. It does **NOT** mean: "there's a 3% chance the model is no better" or "97% probability the model is better." The p-value is about the data given H₀, not about H₀ given the data.

**(c)** Type I: rejecting H₀ when it's true (false alarm). Type II: failing to reject H₀ when H₁ is true (missed detection). At α = 0.05, P(Type I) = **0.05** (by definition — α is the threshold for rejecting H₀).

**(d)** This is the **multiple comparisons problem** (or p-hacking). P(at least one false positive) = 1 − P(no false positives) = 1 − (0.95)²⁰ ≈ 1 − 0.358 ≈ **0.64**. There's a 64% chance of finding at least one "significant" result by pure chance! The Bonferroni correction adjusts α to 0.05/20 = 0.0025 per test.

---

### Question 6 (10 pts)

**(a)** **Confounding variable / ecological fallacy.** Wealth is a confound — wealthy nations both consume more chocolate and invest more in education/research. The correlation is real but the causal conclusion is wrong.

**(b)** **Optional stopping / sequential testing without correction.** Repeatedly checking p-values inflates the false positive rate because you get many chances to cross the threshold. Must use sequential testing methods (e.g., alpha spending functions) or pre-register the sample size.

**(c)** **Data snooping / test set contamination.** The test set is no longer an unbiased estimate of performance because it was used for model selection. The reported accuracy is optimistically biased. Must use a held-out test set that is never used for any decision during development.

**(d)** **Inadequate sample size for the claimed precision.** 100 queries gives at most ~1% granularity. "99.9% blocking" means at most 0.1 failures per 1000 — you can't demonstrate this with only 100 samples. The confidence interval for the true blocking rate is very wide. Also, the test set might not be representative of real-world harmful queries.

**(e)** The large study (n=10,000) provides **much stronger evidence** despite the small study having the "surprising" p = 0.04 result. The odds ratio of 1.1 is very small — barely above 1.0 (no effect). The small study's p = 0.04 is fragile (borderline significant, likely won't replicate). The large study's p = 0.001 with the same small effect is more convincing because the narrow confidence interval pins down the true effect size. However, an OR of 1.1 means a 10% increase in risk — clinically small and possibly explained by residual confounding.

---

### Question 7 (10 pts)

**(a)** The vector y lives in ℝⁿ. The columns of X span a subspace (the column space). β̂ = (XᵀX)⁻¹Xᵀy finds the coefficients such that **ŷ = Xβ̂ is the orthogonal projection of y onto the column space of X**. This is the closest point in the column space to y, minimizing ‖y − Xβ̂‖².

**(b)** Under y ~ N(Xβ, σ²I), the log-likelihood is ℓ(β) = −n/2 ln(2πσ²) − ‖y − Xβ‖²/(2σ²). Maximizing ℓ ⟺ minimizing ‖y − Xβ‖², which is least squares. **OLS = MLE under Gaussian noise.**

**(c)** R² = ‖ŷ‖²/‖y‖² (after centering). R² = 1 means ŷ = y — the projection hits the target exactly. R² = 0 means the projection onto the model subspace has zero length in the "useful" direction — the model captures nothing beyond the mean. Geometrically, R² = cos²(θ) where θ is the angle between y and the column space.

**(d)** Binary outcomes (0/1) violate OLS assumptions: predicted values can be outside [0,1], residuals aren't normally distributed. Logistic regression uses the **cross-entropy (negative log-likelihood) loss**: L = −Σ[yᵢ log σ(xᵢᵀβ) + (1−yᵢ) log(1−σ(xᵢᵀβ))]. This is MLE for a Bernoulli model and keeps predictions in (0,1) via the sigmoid.

---

### Question 8 (8 pts)

**(a)** E[X] = ∫ x·p(x) dx. For Uniform(0,1): E[X] = ∫₀¹ x dx = **1/2**.

**(b)** E[X²] = ∫₀¹ x² dx = 1/3. Var(X) = 1/3 − (1/2)² = 1/3 − 1/4 = **1/12**.

**(c)** Eigenvectors = **principal components** — the directions of maximum variance. Eigenvalues = **variance along each principal direction**. The technique is **PCA** (Principal Component Analysis), which is the eigendecomposition of the covariance matrix from Phase 1.

**(d)** **No.** Zero covariance does not imply independence. Example: X ~ Uniform(−1,1), Y = X². Then Cov(X,Y) = E[XY] − E[X]E[Y] = E[X³] − 0 = 0 (by symmetry), but X and Y are clearly dependent (Y is a deterministic function of X). Independence is a stronger condition than zero covariance.

---

### Question 9 (10 pts)

**(a)** H(P,Q) = −Σ p(x) log q(x) = −Σ p(x) log p(x) + Σ p(x) log p(x) − Σ p(x) log q(x) = −Σ p(x) log p(x) + Σ p(x) log(p(x)/q(x)) = **H(P) + DKL(P‖Q)** ✓

**(b)** Perplexity 50 means the model is, on average, **as uncertain as if choosing uniformly among 50 options** at each token. Lower is better — a perplexity of 1 would mean perfect prediction. English has about 50,000+ possible tokens, so perplexity 50 means the model has narrowed it down dramatically from uniform.

**(c)** T → 0: the distribution collapses to a **one-hot** on the highest logit (argmax, greedy decoding). Entropy → 0. T → ∞: the distribution approaches **uniform** over all classes. Entropy → log(K). T = 1: the standard softmax. Temperature inversely controls entropy — low T = confident/deterministic, high T = uncertain/diverse.

**(d)** Problems: (1) KL divergence of 0.5 is meaningless without context — is this between two Gaussians, two categorical distributions, two language models? The scale depends on the distributions. (2) KL divergence depends on which direction (P‖Q or Q‖P). (3) There's no universal threshold for "good." You'd need: the dimensionality of the distributions, the baseline KL for random/trivial models, and comparison with other methods on the same task.

---

### Question 10 (10 pts)

**(a)** **No.** A 5% difference could be due to random variation. You'd need a paired test (McNemar's test for classification) or a statistical significance test comparing the two models' error rates, accounting for the test set size.

**(b)** **Cross-entropy** is more informative because it measures the quality of the probability predictions, not just the hard classifications. A model that gives 51% probability to the correct class gets the same accuracy credit as one giving 99%, but the cross-entropy correctly reflects that the second model is much better calibrated.

**(c)** **Model B** for safety-critical applications. Model A fails badly on class 3 (40% accuracy), which could be disastrous if class 3 represents a safety-relevant category. In alignment/safety contexts, worst-case performance matters more than average performance. A model that's uniformly reliable (85% across all classes) is preferable to one that's excellent on easy classes but fails on hard/rare ones.

**(d)** R² = r² → r = √(0.64) = **0.8**. The correlation between predictions and true values is 0.8. This connects to the Phase 1 insight: R² involves squared lengths (projection squared over original squared), and since correlation is about direction not magnitude, you need the square root.
