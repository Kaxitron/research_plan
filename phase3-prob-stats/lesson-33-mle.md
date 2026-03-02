# Lesson 33: Maximum Likelihood Estimation

[← Expectation](lesson-32-expectation.md) | [Back to TOC](../README.md) | [Next: Information Theory →](lesson-34-information-theory.md)

---

> **Why this lesson exists:** MLE is the bridge between probability theory and learning. When a neural network trains on data, it's doing MLE (or a close relative). Understanding MLE means understanding *what training is actually optimizing* — and understanding its limitations tells you why models can learn the wrong thing, which is the starting point of alignment concerns.

## 🎯 Core Learning

- The central question: given data, what parameters best explain it?
- Likelihood function: probability of the data given the parameters
- MLE: find parameters that maximize likelihood
- Log-likelihood: turns products into sums (numerical stability + easier calculus)
- MLE for Gaussians: the mean and variance formulas you know ARE MLE solutions
- **Connection to neural network training: minimizing cross-entropy loss = maximizing likelihood**

### The EM Algorithm — MLE When There's Hidden Structure

- **The problem:** sometimes your data has hidden (latent) variables you can't observe. You see the exam scores but not which study group each student was in. You see pixel colors but not which object each pixel belongs to. You can't directly maximize likelihood because the likelihood involves summing over all possible values of the hidden variables.
- **The Expectation-Maximization (EM) solution:** alternate between two steps:
  1. **E-step (Expectation):** given current parameter estimates, compute the *expected* values of the hidden variables. "Given what I currently believe about the clusters, which cluster does each data point probably belong to?"
  2. **M-step (Maximization):** given those expected hidden values, update parameters via standard MLE. "Given these cluster assignments, what are the best cluster centers and shapes?"
  3. Repeat until convergence. Each iteration is guaranteed to increase (or maintain) the likelihood — you'll never go backward.
- **Visual intuition:** imagine you're fitting two overlapping Gaussian bells to data, but you don't know which bell generated each point. E-step: color each point by how likely it came from each bell (soft assignment). M-step: re-fit each bell using the colored points. The bells gradually separate and sharpen.
- **Gaussian Mixture Models (GMMs)** are the canonical EM application: model data as coming from k different Gaussians with unknown means, variances, and mixing proportions. EM learns all of these.
- **Why EM matters beyond GMMs:**
  - **The pattern is universal:** many learning algorithms alternate between "infer hidden structure" and "update parameters given structure." This includes some formulations of RLHF (infer reward model → update policy) and Bayesian methods.
  - **Latent variable models** are how we formalize "the data has hidden structure." VAEs, topic models, and hidden Markov models all use EM or EM-like inference.
  - **K-means clustering** is a special case of EM where the E-step makes hard assignments instead of soft ones.
- **Limitations:** EM finds local maxima, not global ones. Different initializations give different results. It can be slow for complex models. But the conceptual framework — iterate between inference and optimization — is profoundly useful.
- **MML Book, Chapter 11.3** covers EM for GMMs. Chapter 11.1–11.2 set up GMMs and their likelihood.

## 📺 Watch — Primary

1. **StatQuest — "Maximum Likelihood, clearly explained!!!"**
   - https://www.youtube.com/watch?v=XepXtl9YKwc
   - *Josh Starmer's signature style. Builds MLE from scratch with clear visuals. Start here.*
2. **StatQuest — "Maximum Likelihood For the Normal Distribution, step-by-step!"**
   - https://www.youtube.com/watch?v=Dn6b9fCIUpM
   - *Walks through the Gaussian MLE derivation — shows you get the sample mean and variance.*

## 📺 Watch — Secondary

3. **StatQuest — "Probability vs Likelihood"**
   - https://www.youtube.com/watch?v=pYxNSUDSFH4
   - *Critical distinction: probability fixes parameters and asks about data. Likelihood fixes data and asks about parameters. This confusion trips up many people.*
4. **Serrano.Academy — "A friendly introduction to Maximum Likelihood Estimation"**
   - Search YouTube for "Serrano Academy maximum likelihood"
5. **StatQuest — "Gaussian Mixture Models and EM"**
   - Search YouTube for "StatQuest Gaussian mixture models"
   - *Visual walkthrough of the E-step and M-step on real data.*

## 📖 Read

- **MML Book, Chapter 8.3** — maximum likelihood estimation (the core framework)
- **MML Book, Chapter 11.1–11.3** — Gaussian Mixture Models and the EM algorithm
- **MML Book, Chapter 11.4** — the latent variable perspective (connects EM to generative models)

## 🔨 Do

- Implement MLE for a Gaussian: given data points, find best μ and σ
- Show that minimizing mean squared error = maximizing likelihood under Gaussian noise
- **EM from scratch:** Generate data from 2 Gaussians (you know the true parameters). Implement EM: E-step computes responsibilities, M-step updates means/variances/mixing weights. Watch the estimated parameters converge to the true ones. Plot the evolution over 20 iterations.
- **K-means as hard EM:** Implement k-means on the same data. Compare to soft EM. See that k-means makes hard cluster assignments while EM gives probabilities.

## 🔗 ML & Alignment Connection

When we train a language model to predict the next token, we are literally doing maximum likelihood estimation. The loss function (cross-entropy) IS the negative log-likelihood. This connection means you understand the fundamental training objective of every modern LLM.

The EM pattern appears throughout ML:
- **VAEs** use a variant of EM (the ELBO objective)
- **Self-training / pseudo-labeling** is EM-like: infer labels (E-step), retrain on pseudo-labels (M-step)
- **Some RLHF formulations** alternate between inferring human preferences (reward model) and optimizing policy — an EM-like loop

MLE optimizes the model to match the *training distribution*. But alignment requires the model to generalize beyond training data in the right way. MLE on "predict the next token" doesn't inherently teach the model to be helpful, honest, or harmless — it teaches it to be a good next-token predictor. The gap between "good at MLE" and "aligned" is the entire reason RLHF and Constitutional AI exist.