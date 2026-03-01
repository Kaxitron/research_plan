# Exam 3A: Probability & Frequentist Methods — The Workhorse Toolkit

**The Path to AI Alignment — Lessons 28–34 Comprehensive Assessment**

---

| | |
|---|---|
| **Time Allowed** | 60 minutes |
| **Total Points** | 100 |
| **Materials** | Pencil, paper, calculator (no CAS). No code. |
| **Format** | 10 questions mixing computation and conceptual depth |

> **Advice:** Show all work. The integrative thread: **every ML training objective is rooted in probability and information theory.**

---

## Question 1 (10 pts) — Probability Foundations

**(a)** A language model outputs probabilities over a vocabulary of 4 tokens: P(A)=0.5, P(B)=0.3, P(C)=0.15, P(D)=0.05. Verify this is a valid probability distribution.

**(b)** Using Bayes' theorem: A classifier has 95% accuracy on spam (P(positive|spam)=0.95) and 90% accuracy on non-spam (P(negative|not spam)=0.90). If 10% of emails are spam, what is P(spam|positive)?

**(c)** Explain why the answer to (b) might surprise someone who only knows the 95% accuracy figure. What common mistake are they making?

---

## Question 2 (10 pts) — Expectation and Covariance

**(a)** A discrete random variable X takes values {−1, 0, 2} with probabilities {0.3, 0.5, 0.2}. Compute E[X] and Var(X).

**(b)** The covariance matrix of a 2D dataset is Σ = [[4, 2], [2, 3]]. Find the eigenvalues of Σ. What do the eigenvectors represent geometrically?

**(c)** PCA finds the directions of maximum variance by computing eigenvectors of Σ. The eigenvalues tell you the variance along each principal direction. What fraction of total variance is captured by the first principal component in (b)?

---

## Question 3 (12 pts) — Maximum Likelihood Estimation

You observe data: x₁ = 3, x₂ = 5, x₃ = 4, x₄ = 6, x₅ = 2, assumed drawn from N(μ, σ²).

**(a)** Write the likelihood function L(μ, σ²) for this data.

**(b)** Write the log-likelihood. Why do we prefer to work with log-likelihood?

**(c)** Derive the MLE for μ by taking ∂ℓ/∂μ = 0. Compute it for the given data.

**(d)** State (without deriving) the MLE for σ². Is it biased or unbiased?

**(e)** A neural network trained with cross-entropy loss is doing MLE. Explain in 2–3 sentences: what is the "model," what are the "parameters," and what distribution is being fit?

---

## Question 4 (12 pts) — Information Theory

**(a)** Compute the entropy H(X) for a fair coin (P(H) = P(T) = 0.5) and for a biased coin (P(H) = 0.9, P(T) = 0.1). Which has more entropy? Why does this make intuitive sense?

**(b)** Define KL divergence D_KL(P ‖ Q). Is it symmetric? What does D_KL(P ‖ Q) = 0 mean?

**(c)** Show that minimizing cross-entropy loss H(P, Q) = −Σ p(x) log q(x) between the true distribution P and model distribution Q is equivalent to minimizing KL divergence D_KL(P ‖ Q). *(Hint: write H(P,Q) = H(P) + D_KL(P‖Q).)*

**(d)** In RLHF, a KL penalty keeps the fine-tuned model Q close to the base model P. Write this penalty term. What happens if you make the KL penalty weight too small? Too large?

---

## Question 5 (10 pts) — Hypothesis Testing

A researcher claims their new model beats the baseline (accuracy 80%) on a benchmark. They test on 100 examples and get 85% accuracy.

**(a)** State H₀ and H₁ for this test.

**(b)** Under H₀, the number of correct answers follows Binomial(100, 0.8). The standard deviation is √(np(1−p)) = √(100·0.8·0.2) = 4. Compute the z-score for 85 correct.

**(c)** The p-value for z = 1.25 is approximately 0.106. At significance level α = 0.05, do you reject H₀? What does this mean in plain English?

**(d)** State what a p-value IS and what it is NOT. (One sentence each.)

**(e)** The researcher increases their test set to 10,000 examples and finds 81% accuracy. Is this result likely to be statistically significant? Is it practically significant? Explain the difference.

---

## Question 6 (10 pts) — Experimental Design and Fallacies

**(a)** Name and explain three features that make a study reliable (from Lesson 33).

**(b)** A paper reports: "Among people who exercise, cancer rates are lower. Therefore exercise prevents cancer." Identify the fallacy and explain what confounders might be at play.

**(c)** A researcher tests 20 different hypotheses and finds one with p < 0.05. Should you believe the result? Explain the multiple comparisons problem and one correction method.

**(d)** An ML paper reports: "Our model achieves state-of-the-art on benchmark X." What questions should you ask before believing this claim? Name at least three.

---

## Question 7 (10 pts) — Regression as Projection AND MLE

Consider fitting y = β₀ + β₁x to data points: (1,2), (2,4), (3,5), (4,4), (5,6).

**(a)** Set up the matrix equation y = Xβ + ε. Write out X, y, and β.

**(b)** The least-squares solution is β̂ = (XᵀX)⁻¹Xᵀy. This IS a projection from Phase 1. What is being projected onto what?

**(c)** Show that least-squares regression is also MLE under the assumption ε ~ N(0, σ²). *(Hint: maximizing the Gaussian likelihood is equivalent to minimizing what?)*

**(d)** Compute r² (coefficient of determination) if the model explains 80% of variance. What does r² = |ŷ|²/|y|² mean geometrically in terms of the projection?

---

## Question 8 (8 pts) — Connecting Cross-Entropy to Training

**(a)** A language model predicts the next token. The true distribution is one-hot: P = (0, 0, 1, 0) (the correct token is token 3). The model predicts Q = (0.1, 0.2, 0.6, 0.1). Compute the cross-entropy loss H(P, Q).

**(b)** What would the cross-entropy be if the model predicted Q = (0, 0, 1, 0)? What about Q = (0.25, 0.25, 0.25, 0.25)?

**(c)** Cross-entropy is bounded below by the entropy H(P). For a one-hot distribution, what is H(P)? What does this mean for training?

---

## Question 9 (8 pts) — Statistical Fallacies in ML

**(a)** Simpson's paradox: a treatment helps men AND helps women, but hurts the combined population. Sketch a numerical example showing how this can happen. *(Hint: unequal group sizes.)*

**(b)** A paper claims "Model A is better than Model B" because A beats B on 5 out of 7 benchmarks. Without seeing confidence intervals or effect sizes, explain why this claim might be weak.

**(c)** Base rate neglect: an AI safety test catches 99% of dangerous behaviors but has a 5% false positive rate. If only 0.1% of model behaviors are actually dangerous, what fraction of flagged behaviors are true positives?

---

## Question 10 (10 pts) — Synthesis

**(a)** Trace the connection: MLE → cross-entropy loss → KL divergence. Show how training a neural network with cross-entropy loss is minimizing the KL divergence between the data distribution and the model.

**(b)** Linear regression is simultaneously: (1) a projection (Phase 1), (2) MLE under Gaussian noise, and (3) minimizing squared error. Explain why all three perspectives give the same answer.

**(c)** The r² = |ŷ|²/|y|² connection you derived earlier bridges Phase 1 (projection lengths) and Phase 3 (explained variance). State in one sentence why you need r² (not r) to measure explained variance. *(Hint: variance involves squared lengths.)*

**(d)** A colleague says "Our model got p < 0.001, so it's definitely better." Give two reasons this could still be misleading.

---

## 🔧 Optional Mini Project (~45 minutes): Bootstrap Hypothesis Testing Lab

**Build a resampling-based statistical testing toolkit from scratch.**

1. Generate synthetic data: two groups (e.g., "control" and "treatment") drawn from slightly different distributions
2. Implement the bootstrap: resample with replacement 10,000 times, compute the mean difference each time, build a confidence interval
3. Implement a permutation test: shuffle group labels 10,000 times, compute the null distribution of mean differences, calculate the p-value
4. Compare your bootstrap CI and permutation p-value to the classical t-test result
5. Visualize: plot the bootstrap distribution, the permutation null distribution, and mark the observed statistic on each
6. Power analysis: vary the true effect size from 0 to 1 and plot the fraction of times each test correctly rejects H₀ (statistical power curve)

**Stretch:** Demonstrate Simpson's paradox with a synthetic dataset. Show that the treatment helps in every subgroup but hurts overall. Visualize why.

**Tools:** NumPy, Matplotlib, SciPy (for t-test comparison only).
