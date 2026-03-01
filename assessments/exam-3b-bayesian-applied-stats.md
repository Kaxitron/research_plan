# Exam 3B: Bayesian Deep Dive & Applied Statistics

**The Path to AI Alignment — Lessons 35–39 Comprehensive Assessment**

---

| | |
|---|---|
| **Time Allowed** | 60 minutes |
| **Total Points** | 100 |
| **Materials** | Pencil, paper, calculator (no CAS). No code. |
| **Format** | 10 questions covering Bayesian inference, computation, model comparison, causal reasoning |

> **Advice:** This is the "paradigm shift" exam. Show all work. The integrative thread: **can you think like a Bayesian, connect it to frequentist methods, and adjudicate real statistical claims?**

---

## Question 1 (10 pts) — Bayesian Foundations

**(a)** State the key philosophical difference between frequentist and Bayesian probability. Give an example of a statement that is meaningful under the Bayesian view but meaningless under the frequentist view.

**(b)** You flip a coin 10 times and get 7 heads. A frequentist would compute the MLE for the bias. A Bayesian with a Beta(2,2) prior would compute the posterior. Compute both estimates.

**(c)** How does the Bayesian estimate differ from the MLE? What happens to this difference as n → ∞?

---

## Question 2 (12 pts) — Conjugate Priors and Posterior Computation

**(a)** Define "conjugate prior." Why are conjugate priors computationally convenient?

**(b)** For a Binomial likelihood with Beta(α, β) prior: if you observe k successes in n trials, the posterior is Beta(α + k, β + n − k). Derive this using Bayes' theorem. *(Show the key steps — you don't need to normalize explicitly, just identify the kernel.)*

**(c)** With prior Beta(1, 1) (uniform), compute the posterior mean after observing 8 heads in 10 flips. Compare with the MLE.

**(d)** With prior Beta(10, 10) (strong prior toward 0.5), compute the posterior mean after the same 8/10 observation. Why is the posterior pulled more toward 0.5?

---

## Question 3 (10 pts) — MAP and Regularization

**(a)** Define MAP (Maximum A Posteriori) estimation. Write the formula being maximized.

**(b)** Show that MAP with a Gaussian prior on parameters N(0, σ²I) is equivalent to MLE with L2 regularization (Ridge regression). What is the relationship between the prior variance σ² and the regularization strength λ?

**(c)** What prior corresponds to L1 regularization (Lasso)? Why does it produce sparse solutions while L2 does not?

**(d)** In your own words: why is "regularization = prior" one of the most important insights in all of ML?

---

## Question 4 (10 pts) — MCMC and Variational Inference

**(a)** The core problem: we need to compute P(θ|D) = P(D|θ)P(θ)/P(D), but P(D) = ∫ P(D|θ)P(θ)dθ is intractable. Name two approaches and describe each in one sentence.

**(b)** The Metropolis-Hastings algorithm proposes a new θ' and accepts with probability min(1, P(θ'|D)/P(θ|D)). Why don't you need to compute P(D) for this? *(Hint: what cancels in the ratio?)*

**(c)** Variational inference approximates P(θ|D) with a simpler distribution q(θ) by minimizing KL(q ‖ P(θ|D)). This leads to maximizing the ELBO (Evidence Lower BOund). State the ELBO and explain each term.

**(d)** MCMC is exact but slow. VI is fast but approximate. For training a VAE (Variational Autoencoder), which is used and why?

---

## Question 5 (10 pts) — Bayesian Model Comparison and Free Energy

**(a)** The marginal likelihood P(D|M) = ∫ P(D|θ,M)P(θ|M)dθ is used to compare models. Explain the "Bayesian Occam's razor": why does the marginal likelihood automatically penalize overly complex models?

**(b)** For regular models, the marginal likelihood is approximated by BIC: log P(D|M) ≈ log P(D|θ̂) − (d/2)log(n). Interpret each term.

**(c)** BIC fails for neural networks because they are *singular* models. What goes wrong? What quantity replaces d/2 in Singular Learning Theory, and why is it always ≤ d/2?

**(d)** State the SLT free energy formula: F ≈ λ·log(n) − (m−1)·log(log(n)) + constant. What are λ and m? Why does λ < d/2 explain why overparameterized neural networks can generalize?

---

## Question 6 (10 pts) — Causal Inference

**(a)** State the fundamental problem of causal inference. Why can't we observe individual causal effects?

**(b)** Draw a causal DAG for: "Ice cream sales → (nothing)" ← "Temperature" → "Drowning deaths." Ice cream sales and drowning deaths are correlated. Why would controlling for temperature remove the correlation?

**(c)** Define a confounder, a mediator, and a collider using DAG terminology. For each, state whether you should or should not control for it when estimating the causal effect of X on Y.

**(d)** An AI safety researcher claims: "Models trained with RLHF are safer because RLHF training reduces harmful outputs." Construct a causal DAG that includes at least one potential confounder. What would a proper causal analysis require?

---

## Question 7 (8 pts) — Applied Statistics: Evaluating Claims

A paper claims: "Heritability of intelligence is 0.8, therefore intelligence is 80% genetic."

**(a)** Define heritability precisely. What does h² = 0.8 actually mean?

**(b)** Explain two common misinterpretations of heritability that the claim above commits.

**(c)** Why does heritability depend on the population and environment being studied? Give a concrete example showing how the same trait can have different heritability in different environments.

---

## Question 8 (10 pts) — The ELBO and VAEs

**(a)** For a generative model with latent variables z, write the marginal likelihood log P(x) and show that it equals ELBO + KL(q(z|x) ‖ P(z|x)).

**(b)** Since KL ≥ 0, this means ELBO ≤ log P(x). Why is maximizing the ELBO a useful objective?

**(c)** The ELBO for a VAE is: ELBO = E_q[log P(x|z)] − KL(q(z|x) ‖ P(z)). Interpret each term: what does the first term encourage? What does the second?

**(d)** Connect to Lessons 35–37: the ELBO involves a reconstruction term (likelihood) and a regularization term (KL from prior). This is MAP estimation in disguise. Explain this connection.

---

## Question 9 (10 pts) — Synthesis: Frequentist vs. Bayesian on a Real Problem

A clinical trial tests a new drug. 100 patients receive the drug, 100 receive placebo. Results: 30/100 improved on drug, 20/100 improved on placebo.

**(a)** Frequentist approach: compute the difference in proportions (0.30 − 0.20 = 0.10). Compute an approximate 95% confidence interval. *(Use SE ≈ √(p̂(1−p̂)/n₁ + p̂(1−p̂)/n₂) with p̂ = 0.25.)*

**(b)** Bayesian approach: with a uniform Beta(1,1) prior on each group's success rate, what are the posterior distributions? Compute the posterior means.

**(c)** How could a Bayesian directly compute P(drug is better than placebo | data)? *(Describe the approach, you don't need to compute the exact number.)*

**(d)** A regulatory agency asks: "Is this drug effective?" Describe how the frequentist answer (confidence interval) and Bayesian answer (posterior probability) address this question differently.

---

## Question 10 (10 pts) — Capstone: Adjudicating a Statistical Debate

A controversial paper claims a specific gene variant increases risk of a disease by 20% (odds ratio 1.2), based on a GWAS with 10,000 participants and p = 0.0001.

**(a)** What is the multiple comparisons problem in GWAS? If 1 million gene variants are tested, what Bonferroni-corrected significance threshold should be used?

**(b)** Does p = 0.0001 survive this correction? What if 500,000 variants were tested?

**(c)** A Bayesian re-analysis uses a skeptical prior that most gene variants have no effect. The prior probability of a true association is 1/1000. Using a simplified Bayes factor analysis, estimate the posterior probability of a true association. *(You may approximate.)*

**(d)** The paper does not include a replication cohort. Why is replication essential for GWAS findings? What is the "winner's curse" and how does it affect reported effect sizes?
