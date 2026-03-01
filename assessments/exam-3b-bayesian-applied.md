# Exam 3B: Bayesian Deep Dive & Applied Statistics — The Paradigm Shift

**The Path to AI Alignment — Lessons 35–39 Comprehensive Assessment**

---

| | |
|---|---|
| **Time Allowed** | 60 minutes |
| **Total Points** | 100 |
| **Materials** | Pencil, paper, calculator (no CAS). No code. |
| **Format** | 10 questions mixing computation and conceptual depth |

> **Advice:** The thread: **Bayesian reasoning unifies learning, regularization, and model comparison — and connects directly to SLT.**

---

## Question 1 (10 pts) — Bayesian Foundations

**(a)** Write Bayes' theorem in the form: posterior ∝ likelihood × prior. Label each term in the context of training a model with parameters θ on data D.

**(b)** You flip a coin 10 times and get 7 heads. With a uniform prior on θ (probability of heads), the posterior is Beta(8, 4). What is the posterior mean? How does this compare to the MLE?

**(c)** Now use a strong prior: Beta(100, 100) (strongly believe θ ≈ 0.5). After seeing 7/10 heads, the posterior is approximately Beta(107, 103). What is the posterior mean? Why has the prior "overwhelmed" the data?

**(d)** In one sentence: when is the Bayesian approach most different from MLE, and when do they converge?

---

## Question 2 (12 pts) — MAP and Regularization

**(a)** The MAP estimate is θ_MAP = argmax P(θ|D) = argmax [log P(D|θ) + log P(θ)]. Show that if the prior is P(θ) ∝ exp(−λ‖θ‖²), then MAP is equivalent to MLE with L2 regularization (Ridge).

**(b)** What prior corresponds to L1 regularization (Lasso)?

**(c)** Ridge works best when "everything matters a little." Lasso works best when "most things don't matter." Explain these intuitions in terms of the prior distribution shapes.

**(d)** Weight decay in neural network training is equivalent to what Bayesian prior? What does this tell you about what we implicitly believe about good weight configurations?

---

## Question 3 (10 pts) — MCMC and Variational Inference

**(a)** The posterior P(θ|D) ∝ P(D|θ)P(θ) is usually intractable. Name the two main approaches to handling this and state one advantage of each.

**(b)** Metropolis-Hastings proposes a new θ' and accepts it with probability min(1, P(θ'|D)/P(θ|D)). Why doesn't this require computing the normalizing constant P(D)?

**(c)** Variational inference approximates P(θ|D) with a simpler distribution q(θ) by minimizing KL(q ‖ P(θ|D)). This leads to maximizing the ELBO. Write the ELBO: ELBO(q) = E_q[log P(D|θ)] − KL(q ‖ P(θ)). Why is the ELBO a lower bound on log P(D)?

**(d)** The ELBO appears again in VAE training. In 2–3 sentences, explain the connection: what plays the role of θ, what plays the role of D, and what is q?

---

## Question 4 (10 pts) — Bayesian Model Comparison

**(a)** The marginal likelihood (evidence) is P(D|M) = ∫ P(D|θ,M)P(θ|M) dθ. Explain in 2–3 sentences why this automatically penalizes overly complex models (Occam's razor as a theorem).

**(b)** BIC approximates 2·log P(D|M) ≈ 2·log P(D|θ̂) − k·log(n), where k = parameter count, n = sample size. What does the −k·log(n) term do?

**(c)** BIC assumes the model is *regular* (the parameter-to-function map is locally one-to-one). Neural networks are singular (many parameters → same function). What goes wrong with BIC for neural networks?

**(d)** In SLT, the RLCT λ replaces k/2 in the free energy formula: F ≈ λ·log(n). Why is λ ≤ k/2 always, and what does this inequality mean for neural network generalization?

---

## Question 5 (10 pts) — Causal Inference

**(a)** Draw a causal DAG for: "Education → Income, Education → Health, Income → Health, Confounders → Education, Confounders → Health." Identify a backdoor path from Education to Health.

**(b)** What is a confounder? In your DAG, identify one and explain how it could bias a naive estimate of Education's effect on Health.

**(c)** An observational study finds that hospitals with more ICU beds have higher mortality rates. Explain why this doesn't mean ICU beds cause death. *(What is this an example of?)*

**(d)** Describe in 2–3 sentences how counterfactual reasoning is central to AI alignment. *(Hint: decision theory asks "what would happen if...")*

---

## Question 6 (10 pts) — Applied Statistics: Heritability and GWAS

**(a)** Heritability h² = Var(genetic)/Var(total). If h² = 0.8 for height, does this mean 80% of YOUR height is determined by genes? Explain the correct interpretation.

**(b)** GWAS finds SNPs associated with traits. A study finds 1000 SNPs each explaining 0.01% of variance in IQ. Combined they explain 10%. But twin studies suggest h² ≈ 0.5. What is this discrepancy called, and name two possible explanations.

**(c)** A study uses regression to show that after controlling for education and income, there's still a correlation between genes and a behavioral trait. Explain why "controlling for" post-treatment variables (education, income) can actually INTRODUCE bias rather than remove it.

**(d)** State one way the statistical tools from this phase (hypothesis testing, regression, causal inference) directly apply to evaluating claims about AI model capabilities.

---

## Question 7 (8 pts) — The Free Energy Principle

**(a)** Write the free energy: F = −log P(D) = −log ∫ P(D|θ)P(θ)dθ. For regular models, F ≈ nL* + (k/2)log(n). For singular models, F ≈ nL* + λ·log(n). Define each variable.

**(b)** Two models fit the same data equally well (same L*). Model A has k=100 parameters (regular). Model B is a neural network with k=10,000 parameters but RLCT λ=30. Which does Bayesian model comparison prefer, and why?

**(c)** Explain in one sentence why "neural networks have too many parameters to generalize" is wrong according to SLT.

---

## Question 8 (10 pts) — Frequentist vs. Bayesian Showdown

A medical device has a defect rate θ. You observe 0 defects in 100 tests.

**(a)** Frequentist: the MLE is θ̂ = 0. A 95% confidence interval (using the rule of three) is approximately [0, 3/100] = [0, 0.03]. Interpret this.

**(b)** Bayesian with uniform prior Beta(1,1): posterior is Beta(1, 101). The posterior mean is 1/102 ≈ 0.0098. The 95% credible interval is approximately [0.0001, 0.036]. Why is the Bayesian estimate nonzero even though no defects were observed?

**(c)** Which approach would you use to evaluate the safety of an AI system that has never exhibited dangerous behavior in testing? Justify your choice in 2–3 sentences.

---

## Question 9 (10 pts) — Synthesis: Adjudicating a Statistical Claim

A blog post claims: "Study shows that GPT-5 has emergent deceptive capabilities, p = 0.02."

Using everything from Lessons 28–39, write a 5-point critique evaluating this claim. Address: the study design, the p-value interpretation, potential confounders, Bayesian considerations, and what additional evidence you'd want.

---

## Question 10 (10 pts) — The Bayesian-SLT Bridge

**(a)** The Bayesian posterior concentrates around the MAP as n → ∞ (Bernstein-von Mises theorem) — but only for regular models. Why does this fail for singular models?

**(b)** SLT says the posterior for singular models concentrates around the set of optimal parameters K (a variety, not a point). The RLCT measures the "width" of K. Connect this to the concept of flat minima from the calculus phase.

**(c)** In your own words: how does the Bayesian framework's automatic Occam's razor (penalizing complexity via the marginal likelihood) connect to the observation that overparameterized neural networks generalize well?
