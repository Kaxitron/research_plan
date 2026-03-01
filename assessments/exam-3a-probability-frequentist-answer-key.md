# Exam 3A: Probability & Frequentist Methods — Answer Key

**The Path to AI Alignment — Lessons 28–34 Comprehensive Assessment**

---

### Question 1 (10 pts)

**(a)** 0.5 + 0.3 + 0.15 + 0.05 = 1.0. All probabilities ≥ 0. ✓ Valid distribution.

**(b)** P(spam|+) = P(+|spam)P(spam) / P(+) = (0.95)(0.1) / [(0.95)(0.1) + (0.10)(0.9)] = 0.095 / (0.095 + 0.09) = 0.095/0.185 ≈ **0.514** (about 51%).

**(c)** Despite 95% accuracy, only ~51% of positive results are actually spam because spam is rare (10% base rate). The mistake is ignoring the **base rate** (prior probability) — P(positive|spam) is not P(spam|positive). This is base rate neglect, one of the most common errors in probabilistic reasoning.

---

### Question 2 (10 pts)

**(a)** E[X] = (−1)(0.3) + (0)(0.5) + (2)(0.2) = −0.3 + 0 + 0.4 = **0.1**. E[X²] = (1)(0.3) + (0)(0.5) + (4)(0.2) = 0.3 + 0.8 = 1.1. Var(X) = E[X²] − (E[X])² = 1.1 − 0.01 = **1.09**.

**(b)** det(Σ−λI) = (4−λ)(3−λ)−4 = λ²−7λ+8 = 0. λ = (7±√(49−32))/2 = (7±√17)/2. λ₁ ≈ **5.56**, λ₂ ≈ **1.44**. The eigenvectors represent the **principal axes of the data ellipse** — directions of maximum and minimum variance.

**(c)** Total variance = tr(Σ) = 4+3 = 7 (or equivalently λ₁+λ₂ ≈ 7). First PC captures λ₁/7 ≈ 5.56/7 ≈ **79.4%** of total variance.

---

### Question 3 (12 pts)

**(a)** L(μ,σ²) = ∏ᵢ (1/√(2πσ²)) exp(−(xᵢ−μ)²/(2σ²))

**(b)** ℓ = −(n/2)log(2πσ²) − (1/(2σ²))Σ(xᵢ−μ)². Prefer log-likelihood because: products → sums (numerically stable), and sums are easier to differentiate.

**(c)** ∂ℓ/∂μ = (1/σ²)Σ(xᵢ−μ) = 0 → μ̂ = (1/n)Σxᵢ = (3+5+4+6+2)/5 = **4**.

**(d)** σ̂² = (1/n)Σ(xᵢ−μ̂)² = (1+1+0+4+4)/5 = **2**. This is **biased** (divides by n not n−1). The unbiased estimator uses n−1.

**(e)** The "model" is a categorical distribution over the vocabulary (parameterized by the neural network). The "parameters" are all the network weights. The distribution being fit is the conditional distribution P(next_token | context). Cross-entropy loss = negative log-likelihood, so minimizing it IS maximum likelihood estimation of the network parameters.

---

### Question 4 (12 pts)

**(a)** Fair: H = −2(0.5 log₂ 0.5) = **1 bit**. Biased: H = −0.9 log₂ 0.9 − 0.1 log₂ 0.1 ≈ 0.137 + 0.332 = **0.469 bits**. Fair coin has more entropy — maximum uncertainty. The biased coin is more predictable, so there's less surprise/information in each flip.

**(b)** D_KL(P‖Q) = Σ p(x) log(p(x)/q(x)). Not symmetric: D_KL(P‖Q) ≠ D_KL(Q‖P) in general. D_KL = 0 iff P = Q (the distributions are identical).

**(c)** H(P,Q) = −Σp(x)log q(x) = −Σp(x)log p(x) + Σp(x)log(p(x)/q(x)) = H(P) + D_KL(P‖Q). Since H(P) is constant w.r.t. Q, minimizing H(P,Q) over Q is equivalent to minimizing D_KL(P‖Q).

**(d)** KL penalty: β · D_KL(π_new ‖ π_base). Too small β → reward hacking (model diverges far from base, exploiting reward model quirks). Too large β → model barely changes from base (underfitting human preferences, too conservative).

---

### Question 5 (10 pts)

**(a)** H₀: p = 0.80 (model is no better than baseline). H₁: p > 0.80 (model is better).

**(b)** z = (85 − 80)/4 = **1.25**.

**(c)** p-value 0.106 > 0.05. **Do not reject H₀.** In plain English: there is not enough evidence to conclude the new model is better. The observed improvement could plausibly be due to chance.

**(d)** A p-value IS: the probability of observing data this extreme (or more) if H₀ were true. A p-value is NOT: the probability that H₀ is true, nor the probability the result is due to chance.

**(e)** With n=10,000, the standard error shrinks to √(10000·0.8·0.2) = 40. z = (8100−8000)/40 = 2.5, p ≈ 0.006 — **statistically significant**. But 81% vs 80% is a tiny improvement — likely **not practically significant**. Statistical significance just means "probably not random noise"; practical significance means "large enough to matter."

---

### Question 6 (10 pts)

**(a)** (1) **Randomization** — randomly assign subjects to treatment/control, balancing all confounders. (2) **Control group** — provides a comparison baseline. (3) **Blinding** — subjects/researchers don't know assignments, preventing expectation bias.

**(b)** **Correlation ≠ causation.** Confounders: people who exercise may also eat better, be wealthier, have better healthcare access, smoke less, etc. The exercise-cancer correlation might be driven entirely by these confounding variables.

**(c)** With 20 tests at α=0.05, you expect ~1 false positive by chance alone (20 × 0.05 = 1). This is the **multiple comparisons problem**. Correction: **Bonferroni correction** — use α/20 = 0.0025 per test. Only reject if p < 0.0025.

**(d)** Questions: (1) Was the test set truly held out, or was it tuned on? (2) How many models/hyperparameters were tried? (multiple comparisons) (3) Are confidence intervals reported? (4) Is the improvement practically meaningful or just statistically significant? (5) Does it replicate on other benchmarks?

---

### Question 7 (10 pts)

**(a)** X = [[1,1],[1,2],[1,3],[1,4],[1,5]], y = [2,4,5,4,6]ᵀ, β = [β₀, β₁]ᵀ.

**(b)** The observation vector y is being **projected onto the column space of X**. The fitted values ŷ = Xβ̂ are the projection, and the residuals ε̂ = y − ŷ are orthogonal to the column space. This is exactly the projection from Lesson 10.

**(c)** Under ε ~ N(0,σ²), the likelihood is ∝ exp(−‖y−Xβ‖²/(2σ²)). Maximizing this is equivalent to minimizing ‖y−Xβ‖² — the sum of squared residuals. So least squares = MLE under Gaussian noise.

**(d)** r² = 0.80 means 80% of variance explained. Geometrically, r² = |ŷ|²/|y|² = cos²θ where θ is the angle between y and the column space. It's the squared ratio of the projection length to the original vector length.

---

### Question 8 (8 pts)

**(a)** H(P,Q) = −(0·log0.1 + 0·log0.2 + 1·log0.6 + 0·log0.1) = −log(0.6) ≈ **0.511 nats** (or 0.737 bits).

**(b)** Perfect: H(P,Q) = −log(1) = **0**. Uniform: H(P,Q) = −log(0.25) = log(4) ≈ **1.386 nats**. Perfect prediction gives zero loss; uniform prediction gives maximum loss.

**(c)** H(P) = 0 for a one-hot distribution (no uncertainty in the "true" answer). This means the cross-entropy can reach zero — a model can in principle achieve zero training loss by predicting the correct token with probability 1.

---

### Question 9 (8 pts)

**(a)** Example: Treatment helps 80/100 men (80%) vs 70/100 untreated men (70%) — helps men. Treatment helps 30/50 women (60%) vs 20/50 untreated women (40%) — helps women. Combined treated: 110/150 = 73%. Combined untreated: 90/150 = 60%. Wait, that shows treatment helps overall too. Better example: 1/10 men treated (10%) vs 3/100 untreated men (3%); 9/90 women treated (10%) vs 5/100 untreated women (5%). Combined treated: 10/100 = 10%. Combined untreated: 8/200 = 4%. Treatment "hurts" combined (10% vs 4%) but helps within each group. The key is unequal group sizes and different baseline rates.

**(b)** Without confidence intervals, we don't know if the differences are within noise. Without effect sizes, we don't know if the improvements are meaningful. 5/7 could easily happen by chance (binomial probability ≈ 0.16 even with no real difference). The claim lacks statistical rigor.

**(c)** P(dangerous|flagged) = P(flagged|dangerous)P(dangerous) / P(flagged) = (0.99)(0.001) / [(0.99)(0.001) + (0.05)(0.999)] = 0.00099 / (0.00099 + 0.04995) ≈ 0.00099/0.05094 ≈ **1.94%**. Over 98% of flagged behaviors are false positives! This illustrates why AI safety testing is hard when dangerous behaviors are rare.

---

### Question 10 (10 pts)

**(a)** MLE maximizes P(data|θ), which equals maximizing log P(data|θ) = −H(P_data, P_model) (up to constants). Since H(P_data, P_model) = H(P_data) + D_KL(P_data ‖ P_model), and H(P_data) is fixed, MLE minimizes D_KL(P_data ‖ P_model). Training with cross-entropy = MLE = minimizing KL divergence from data to model.

**(b)** All three give the same answer because the Gaussian likelihood turns MLE into minimizing squared error (the exponent of the Gaussian), and minimizing squared error is equivalent to finding the closest point in the column space (projection). The geometry (projection), the statistics (MLE), and the optimization (least squares) are three views of one mathematical object.

**(c)** Variance is the expected squared deviation — it involves squared lengths. The correlation r measures the cosine of the angle between vectors, but explained variance requires cos²θ = r² because squaring is needed to convert from "length ratios" to "squared-length ratios" (which is what variance is).

**(d)** (1) Statistical significance doesn't imply practical significance — the effect might be tiny. (2) If many models were tested, this could be a multiple comparisons artifact — the winner among 100 random models will "look" significant.
