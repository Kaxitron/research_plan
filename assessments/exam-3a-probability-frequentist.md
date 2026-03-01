# Exam 3A: Core Probability & Frequentist Methods

**The Path to AI Alignment — Lessons 28–34 Comprehensive Assessment**

---

| | |
|---|---|
| **Time Allowed** | 60 minutes |
| **Total Points** | 100 |
| **Materials** | Pencil, paper, calculator (no CAS). No code. |
| **Format** | 10 questions covering distributions, MLE, information theory, hypothesis testing, and regression |

> **Advice:** Show all work. This exam tests the "workhorse" statistical toolkit. The integrative thread: **can you derive MLE, interpret information-theoretic quantities, and critically evaluate statistical claims?**

---

## Question 1 (10 pts) — Probability Foundations

**(a)** Define joint probability P(A, B), marginal probability P(A), and conditional probability P(A|B). State the relationship between them.

**(b)** State Bayes' theorem. A medical test has 95% sensitivity (P(positive|disease) = 0.95) and 99% specificity (P(negative|no disease) = 0.99). If the disease prevalence is 1 in 1000, what is the probability a person actually has the disease given a positive test? Show your work and explain why the result is counterintuitive.

**(c)** Connect Bayes' theorem to ML: in the pattern Prior × Likelihood → Posterior, identify what each term represents when you're training a model on data.

---

## Question 2 (10 pts) — Distributions

**(a)** A coin is flipped 10 times. Write the probability of getting exactly k heads using the Binomial distribution. What is the expected number of heads? The variance?

**(b)** The Gaussian (normal) distribution has density p(x) = (1/√(2πσ²)) exp(−(x−μ)²/(2σ²)). What are the roles of μ and σ? Where does 68% of the probability mass lie?

**(c)** A neural network's softmax output produces a categorical distribution over 4 classes: [0.1, 0.6, 0.2, 0.1]. What is the entropy of this distribution? *(Use log base 2.)*

**(d)** Compare the entropy you computed with the maximum possible entropy for 4 classes (uniform distribution). What does the difference tell you about the model's confidence?

---

## Question 3 (12 pts) — Maximum Likelihood Estimation

**(a)** You observe data x₁, x₂, ..., xₙ drawn independently from a Gaussian with unknown mean μ and known variance σ². Write the likelihood function L(μ) and the log-likelihood ℓ(μ).

**(b)** Derive the MLE estimator μ̂ by taking dℓ/dμ = 0 and solving. Show that μ̂ = x̄ (the sample mean).

**(c)** Now suppose the variance σ² is also unknown. Derive the MLE for σ² by taking ∂ℓ/∂(σ²) = 0. Is this estimator biased? *(The MLE for variance divides by n, not n−1.)*

**(d)** Neural network training with cross-entropy loss is MLE in disguise. If the model outputs softmax probabilities p̂(y|x; θ), explain why minimizing −Σ log p̂(yᵢ|xᵢ; θ) is equivalent to maximizing the likelihood.

---

## Question 4 (10 pts) — Information Theory

**(a)** Define entropy H(X) = −Σ p(x) log p(x). What does it measure? What is the entropy of a fair coin flip (in bits)?

**(b)** Define KL divergence DKL(P ‖ Q) = Σ p(x) log(p(x)/q(x)). Why is it always ≥ 0? Why is it NOT symmetric — i.e., why does DKL(P‖Q) ≠ DKL(Q‖P) in general?

**(c)** Show that minimizing cross-entropy H(P, Q) = −Σ p(x) log q(x) is equivalent to minimizing KL divergence DKL(P ‖ Q) when P is fixed (the data distribution). Why does this mean cross-entropy loss = finding the model distribution closest to the data?

**(d)** In RLHF, a KL penalty DKL(π_new ‖ π_ref) prevents the fine-tuned model from drifting too far from the reference model. Explain in 2 sentences why this is necessary. What goes wrong without it?

---

## Question 5 (10 pts) — Hypothesis Testing

**(a)** Define the null hypothesis H₀, alternative hypothesis H₁, and p-value. Be precise.

**(b)** A researcher tests whether a new ML model is better than a baseline on a benchmark. They get p = 0.03. State clearly: what does this p-value mean? What does it NOT mean?

**(c)** Define Type I error (false positive) and Type II error (false negative). If α = 0.05, what is the probability of a Type I error?

**(d)** A company tests 20 different model architectures on the same dataset and reports the one with p < 0.05. Why is this problematic? Name this statistical issue and compute the approximate probability of getting at least one false positive when running 20 tests at α = 0.05.

---

## Question 6 (10 pts) — Experimental Design Fallacies

For each scenario, identify the statistical fallacy or design flaw:

**(a)** A study finds that countries with more chocolate consumption per capita have more Nobel Prize winners. Conclusion: "chocolate improves intelligence."

**(b)** A researcher runs an experiment, checks the p-value after every 10 new data points, and stops collecting data as soon as p < 0.05.

**(c)** A paper reports: "Our model achieved 95% accuracy on the test set" — but the authors tried 50 hyperparameter configurations, evaluated each on the test set, and reported the best.

**(d)** An ML safety paper claims "our safety filter blocks 99.9% of harmful queries" based on testing against a dataset of 100 harmful queries.

**(e)** A genetics study finds a significant correlation between a gene variant and a disease in a sample of 50 people, with p = 0.04 and odds ratio 1.1. A follow-up study of 10,000 people finds the same odds ratio of 1.1 but p = 0.001. Discuss which study provides stronger evidence and what the odds ratio tells you.

---

## Question 7 (10 pts) — Regression as Geometry and Statistics

**(a)** Linear regression finds ŷ = Xβ̂ where β̂ = (XᵀX)⁻¹Xᵀy. Explain this formula geometrically using the language of Phase 1: what is being projected onto what?

**(b)** Under the statistical model y = Xβ + ε with ε ~ N(0, σ²I), show that the least squares estimator is also the MLE. *(Hint: what does maximizing the Gaussian likelihood minimize?)*

**(c)** Define R² (coefficient of determination). You previously learned that R² = |ŷ|²/|y|² — the squared ratio of the projection length to the original vector length. Explain why R² = 1 means perfect fit and R² = 0 means the model predicts no better than the mean.

**(d)** Logistic regression models P(y=1|x) = σ(xᵀβ). Why can't we use ordinary least squares here? What loss function does logistic regression minimize instead, and why?

---

## Question 8 (8 pts) — Expectation and Covariance

**(a)** Define E[X] for a continuous random variable. What is E[X] for X ~ Uniform(0, 1)?

**(b)** Define Var(X) = E[(X − μ)²] = E[X²] − (E[X])². Compute Var(X) for X ~ Uniform(0, 1).

**(c)** The covariance matrix Σ of a random vector X is a matrix with eigenvalues and eigenvectors. What do the eigenvectors represent? What do the eigenvalues represent? Name the technique from Phase 1 that uses this decomposition.

**(d)** If two random variables have Cov(X, Y) = 0, are they necessarily independent? Give an example showing why or why not.

---

## Question 9 (10 pts) — Connecting the Pieces

**(a)** The cross-entropy loss for a language model predicting the next token is H(p, q) = −Σ p(x) log q(x). Show that this equals H(p) + DKL(p ‖ q), where H(p) is the entropy of the true distribution.

**(b)** Perplexity is defined as 2^H(p,q) (or e^H if using natural log). If a language model has perplexity 50 on English text, give an intuitive interpretation.

**(c)** Temperature scaling modifies the softmax: p(x) ∝ exp(logit_x / T). What happens at T → 0? T → ∞? T = 1? How does this relate to entropy?

**(d)** A mock ML paper claims: "Our model achieves a KL divergence of 0.5 from the true distribution, demonstrating good performance." Identify at least one problem with this claim. What additional information would you need to evaluate it?

---

## Question 10 (10 pts) — Synthesis

A researcher trains two models (A and B) on the same classification dataset with 3 classes. Model A achieves 90% accuracy; Model B achieves 85% accuracy.

**(a)** Can you conclude Model A is better? What statistical test could you use to determine if the difference is significant?

**(b)** Model A has average cross-entropy loss 0.3; Model B has 0.5. Which is more informative than accuracy, and why?

**(c)** You inspect the confusion matrices and discover Model A achieves 99% accuracy on classes 1 and 2 but only 40% on class 3 (which has 10% prevalence). Model B achieves 85% uniformly. Which model would you prefer for a safety-critical application? Why?

**(d)** The researcher computed R² for a regression component of the pipeline and found R² = 0.64. Using the Phase 1 connection, what is the correlation coefficient r between predictions and true values?
