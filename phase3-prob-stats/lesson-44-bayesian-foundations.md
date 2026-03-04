# Lesson 44: Bayesian Reasoning and Foundations — The Prior Art

[← Regression](lesson-43-regression.md) | [Back to TOC](../README.md) | [Next: Bayesian Computation →](lesson-45-bayesian-computation.md)

---

> **Why this lesson exists:** The Bayesian framework treats probability as a measure of belief, not just frequency. This single shift transforms how you think about learning, uncertainty, and model comparison. Every neural network's training can be viewed as approximate Bayesian inference; every regularization technique is an implicit prior. Going deep into Bayesianism gives you the conceptual vocabulary to understand why models generalize (or don't), why Occam's razor emerges naturally from the math, and why Singular Learning Theory works.

## 🎯 Core Concepts

### The Bayesian Paradigm — Belief as Probability

- **Frequentist view:** probability is long-run frequency. "This coin has P(heads) = 0.5" means if you flip it infinitely many times, half will be heads.
- **Bayesian view:** probability is degree of belief. "P(this model is correct) = 0.7" is a meaningful statement — it quantifies your uncertainty about a specific hypothesis, not a repeatable experiment.
- **Why this matters for ML:** you have ONE trained model. It doesn't have a "frequency" — it either generalizes or it doesn't. The Bayesian framework lets you reason about the probability that your specific model will perform well on unseen data.

### Bayes' Theorem — The Update Rule

- **P(θ|D) = P(D|θ)P(θ) / P(D)** where:
  - P(θ) is the **prior** — your belief about parameters before seeing data
  - P(D|θ) is the **likelihood** — how probable the data is given the parameters
  - P(θ|D) is the **posterior** — your updated belief after seeing data
  - P(D) = ∫P(D|θ)P(θ)dθ is the **evidence** (marginal likelihood) — a normalizing constant
- **The posterior is proportional to likelihood × prior:** P(θ|D) ∝ P(D|θ)P(θ). The evidence P(D) just normalizes. This is the update rule — new belief = data evidence × old belief, renormalized.

### Priors — Encoding What You Know (and Don't)

- **Informative priors:** you know something about θ. A physicist measuring a constant might use a Gaussian prior centered on the current best estimate.
- **Weakly informative priors:** you know the rough scale but not the value. P(σ) ~ HalfCauchy(0, 10) says "the noise level is probably between 0 and ~30 but could be larger."
- **"Uninformative" priors:** trying to say "I know nothing." Uniform priors, Jeffreys priors. But truly uninformative priors don't exist — the choice of parameterization matters. This is a deep philosophical issue.
- **Priors as regularization:** L2 regularization (weight decay) IS a Gaussian prior on the weights. L1 regularization IS a Laplace prior. Dropout IS an approximate prior. Every regularization technique in ML has a Bayesian interpretation as a prior belief about model structure. Ridge regression = MAP with Gaussian prior. Lasso = MAP with Laplace prior.
- **The role of the prior in alignment:** what prior beliefs are we encoding in our training setup? RLHF encodes a prior via human preferences. Constitutional AI encodes a prior via constitutional principles. Understanding priors = understanding what we're implicitly assuming about aligned behavior.

### Conjugate Priors — When the Math Is Clean

- **A conjugate prior** for a likelihood is a prior distribution such that the posterior has the same functional form. This makes updating analytical (no integrals needed).
- **Beta-Binomial:** prior Beta(α,β) + binomial data with k successes in n trials → posterior Beta(α+k, β+n-k). The hyperparameters α, β act as "pseudo-counts" — prior successes and failures.
- **Normal-Normal:** prior N(μ₀, σ₀²) + normal data with mean x̄ → posterior with mean that's a weighted average of prior mean and data mean, weighted by relative precision. More data → posterior shrinks toward the data.
- **Dirichlet-Multinomial:** prior over probability vectors + categorical data. This is the foundation of Latent Dirichlet Allocation (topic models) and Bayesian language models.
- **Why conjugacy matters:** it gives you exact posteriors without computation. In practice, most models aren't conjugate — but conjugate examples build intuition for what "updating beliefs" looks like.

### MAP Estimation — The Bridge Between Bayesian and Frequentist

- **Maximum A Posteriori:** instead of computing the full posterior, just find its mode: θ_MAP = argmax P(θ|D) = argmax [log P(D|θ) + log P(θ)].
- **This is MLE + regularization:** log P(D|θ) is the log-likelihood, log P(θ) is the regularizer. MAP with Gaussian prior = MLE + L2 penalty. MAP with Laplace prior = MLE + L1 penalty.
- **MAP loses uncertainty:** it gives a point estimate, throwing away the posterior's shape. The full Bayesian approach keeps the whole distribution — which matters for safety, because knowing "I'm 95% confident this model works" is different from "my best guess is that this model works."

### Sequential Updating — Bayes as Online Learning

- **Today's posterior is tomorrow's prior.** As new data arrives, you update: P(θ|D₁,D₂) ∝ P(D₂|θ) P(θ|D₁). The posterior after the first batch becomes the prior for the second.
- **This is how beliefs should evolve:** each new piece of evidence refines your estimate. The Bayesian agent is the normative model of rational belief updating — the standard against which human and AI reasoning can be compared.
- **For alignment:** a Bayesian agent that correctly updates on evidence about whether its actions are aligned would naturally become better calibrated over time. The failure modes of real AI systems can be understood as violations of proper Bayesian updating.

## 📺 Watch — Primary

1. **3Blue1Brown — "Bayes theorem, the geometry of changing beliefs"**
   - https://www.youtube.com/watch?v=HZGCoVF3YvM
2. **StatQuest — "Bayesian Inference, Clearly Explained"**
   - https://www.youtube.com/watch?v=O2L2Uv9pdDA
   - *Clear, slow, with good examples of priors and posteriors.*

## 📖 Read — Primary

- **"Bayesian Data Analysis" by Gelman et al.** — Chapters 1–3 (Foundations, single-parameter models)
  - The gold standard Bayesian textbook
- **McElreath — "Statistical Rethinking"** — Chapters 1–4
  - More intuitive, focuses on scientific reasoning

## 🔨 Do

- **Beta-Binomial updating:** start with Beta(1,1) (uniform). Observe 7 heads in 10 flips. Plot prior, likelihood, and posterior. Then observe 30 more flips (20 heads). Update again. Watch the posterior sharpen.
- **Bayesian linear regression:** implement by hand for 1D data. Place a Gaussian prior on the slope and intercept. Compute the posterior analytically (it's conjugate). Compare with MLE. Add an outlier — see how the prior provides robustness.
- **MAP = regularized MLE:** show numerically that MAP estimation with a Gaussian prior N(0, λ⁻¹I) gives the same answer as ridge regression with penalty λ.
- **Demonstrate prior sensitivity:** for the same dataset, compute posteriors with different priors (strong, weak, misspecified). When does the prior matter? When does the data overwhelm it?
- **Prior predictive check — build the habit (supplementary — from Bayesian Computation book gap analysis):** before fitting ANY model, sample from the prior predictive: (1) draw parameter values from your prior, (2) simulate data from the likelihood using those parameters, (3) plot the simulated data. For a model of human heights: if your prior on the mean is N(0, 100), you'll generate "humans" that are −200cm or +300cm tall. The prior predictive immediately reveals this is insane. Tighten to N(170, 20) and the simulated data looks reasonable. Do this for: (a) a Gaussian model of heights, (b) a Binomial model of coin flips, (c) a Poisson model of daily website visits. Train yourself to ALWAYS simulate before fitting — this catches more modeling errors than any diagnostic.
- **Full Bayesian regression end-to-end (supplementary):** take a small 1D dataset (10 points, linear trend with noise). (1) Fit OLS — get point estimates and confidence intervals. (2) Now do it Bayesian: place Gaussian priors on slope and intercept, compute the posterior analytically (conjugate case for known σ), plot posterior distributions for both parameters. (3) Draw 50 lines from the posterior — this is the posterior predictive, showing model uncertainty. Compare with the single OLS line. (4) Tighten the prior variance — watch the posterior shrink toward the prior mean (regularization). (5) Use a Laplace prior instead of Gaussian — show that some posterior mass concentrates at exactly zero (Lasso/sparsity). The key insight: you already know "Ridge = Gaussian prior, Lasso = Laplace prior" from the Core Concepts section. This exercise makes that claim viscerally real rather than just stated.


## 🔗 ML & Alignment Connection

- **Every regularized neural network** is implicitly performing MAP estimation under some prior. Weight decay = Gaussian prior. Understanding this reframes regularization from "engineering trick" to "principled belief."
- **Transfer learning as prior:** a pretrained model provides an informed prior for fine-tuning. The pretrained weights encode beliefs learned from the pretraining data.
- **Bayesian neural networks** maintain a distribution over weights instead of point estimates. This gives principled uncertainty quantification — critical for safety applications.

- **Calibrated uncertainty is safety-critical.** An aligned AI should know what it doesn't know. Bayesian reasoning provides the normative standard for calibration.
- **Prior specification is value specification.** The prior encodes what you believe before seeing data. For alignment, the prior encodes what you value before observing behavior. Getting the prior right IS the alignment problem in Bayesian dress.