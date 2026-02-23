# Lesson 21: Bayesian Reasoning and Inference

[← Information Theory](lesson-20-information-theory.md) | [Back to TOC](../README.md) | [Next: Single Neuron →](../phase4-neural-networks/lesson-22-single-neuron.md)

---

> **Why this lesson exists:** Bayesian reasoning isn't just another probability technique — it's a *theory of rationality* that underpins much of alignment thinking. Solomonoff induction (the theoretical gold standard for prediction), RLHF reward modeling, and debates about AI corrigibility all use Bayesian frameworks. Many alignment researchers think in Bayesian terms by default. You need this language.

## 🎯 Core Concepts

### Bayesian Reasoning as a Way of Thinking

- **Bayes' theorem recap:** P(H|E) = P(E|H) · P(H) / P(E)
  - Prior belief P(H) + evidence P(E|H) → updated belief P(H|E)
  - You NEVER start from scratch. You always have a prior. Evidence shifts it.
- **Bayesian updating is the mathematically optimal way to change your mind.** Given certain axioms of rational belief (coherence, etc.), Bayes' theorem is the ONLY consistent update rule. This is Cox's theorem.
- **Priors matter:** your starting beliefs affect your conclusions, especially with limited evidence. Two people with different priors can rationally reach different conclusions from the same evidence. They should converge with enough evidence — but "enough" can be a lot.
- **Likelihood ratios:** a more intuitive way to do Bayesian updates. Instead of computing P(H|E) directly, ask: "How much more likely is this evidence if H is true vs. if H is false?" That ratio is the update strength.
  - Likelihood ratio = P(E|H) / P(E|¬H)
  - LR > 1: evidence supports H. LR = 10: strong evidence. LR = 100: very strong.
  - Posterior odds = Prior odds × Likelihood ratio

### Bayesian Inference in Practice

- **MAP estimation (Maximum A Posteriori):** like MLE but with a prior. Instead of maximizing P(data|θ), maximize P(θ|data) ∝ P(data|θ) · P(θ). The prior acts as regularization.
  - Gaussian prior on weights → L2 regularization (weight decay!)
  - Laplace prior on weights → L1 regularization (sparsity!)
  - **This is stunning:** regularization techniques that seem like engineering hacks are actually Bayesian inference with specific prior beliefs about what good weights look like.
- **Full Bayesian inference:** don't just find the best θ — compute the entire posterior P(θ|data). This gives you uncertainty estimates, not just point predictions.
- **Bayesian model comparison:** compare models by their marginal likelihood P(data|model) = ∫P(data|θ,model)P(θ|model)dθ. This naturally penalizes complex models (Occam's razor emerges from the math!).

### Solomonoff Induction — The Theoretical Ideal

- **Solomonoff induction:** the theoretically optimal prediction method. Your prior assigns higher probability to simpler hypotheses (shorter programs that generate the data). This is Occam's razor made mathematically precise.
- **It's uncomputable** — you can't actually run it. But it's the gold standard that practical methods try to approximate.
- **AIXI:** Hutter's extension of Solomonoff induction to agents. The theoretically optimal agent. Also uncomputable, but studying it reveals deep truths about what "optimal behavior" means.
- **Why this matters for alignment:** understanding what a "perfect reasoner" would do helps you understand how far real AI systems deviate — and whether those deviations are safe.

### Calibration and Epistemic Humility

- **Calibration:** when a model (or person) says "I'm 80% confident," are they right 80% of the time? Well-calibrated predictions are honest about uncertainty.
- **Overconfidence vs. underconfidence:** most humans are overconfident. Most neural networks are also overconfident (they output high-probability predictions even when wrong).
- **Proper scoring rules:** scoring rules that incentivize honest probability reports. Log loss (cross-entropy!) is a proper scoring rule. This connects information theory to Bayesian honesty.
- **Epistemic vs. aleatoric uncertainty:** epistemic uncertainty = uncertainty from lack of knowledge (reducible with more data). Aleatoric uncertainty = inherent randomness (irreducible). A well-calibrated model should know which is which.

## 📺 Watch — Primary

1. **3Blue1Brown — "Bayes theorem" + "The medical test paradox"**
   - https://www.youtube.com/watch?v=HZGCoVF3YvM
   - https://www.youtube.com/watch?v=lG4VkPoG3ko
   - *The base rate fallacy demonstration is the canonical example of why priors matter.*

## 📺 Watch — Secondary

2. **Arbital — "Bayes' Rule: Guide"** (by Eliezer Yudkowsky)
   - https://arbital.com/p/bayes_rule/
   - Interactive, designed for LessWrong/rationalist community. Emphasizes likelihood ratios.
3. **StatQuest — "Bayesian Inference"**
   - https://www.youtube.com/c/joshstarmer
4. **Primer (YouTube) — "Bayes theorem" series**
   - Excellent animations of sequential Bayesian updating

## 📖 Read — Primary

- **"An Intuitive Explanation of Bayes' Theorem" by Eliezer Yudkowsky**
  - https://www.yudkowsky.net/rational/bayes
  - *The definitive rationalist introduction to Bayesian thinking. Uses medical test examples to build intuition for likelihood ratios.*
- **"Probability Theory: The Logic of Science" by E.T. Jaynes** — Chapters 1–4
  - The Bayesian bible. Jaynes derives probability theory from axioms of rational belief. Dense but transformative. Free PDF available.

## 📖 Read — Secondary

- **MML Book, Chapter 8.4–8.6** — Bayesian inference, MAP estimation, Bayesian model comparison
- **"Bayesian Reasoning for Intelligent People" by Simon DeDeo**
  - https://santafe.edu/~simon/br.pdf
  - Concise, well-written introduction with good examples
- **LessWrong Sequences — "Mysterious Answers to Mysterious Questions"**
  - https://www.lesswrong.com/s/SqFbMbtxGybdS2gRs
  - Yudkowsky's treatment of how Bayesian reasoning connects to scientific thinking and epistemology

## 📖 Read — Going Deep

- **"Solomonoff Induction" on Arbital**
  - https://arbital.com/p/solomonoff_induction/
- **"Universal Artificial Intelligence" by Marcus Hutter** (technical reference for AIXI)
- **"Bayesian Brain Hypothesis"** — the idea that biological brains do approximate Bayesian inference

## 🔨 Do

- **Sequential updating:** Start with a prior on a coin's bias. Observe flips one at a time. After each flip, compute the posterior using Bayes' rule. Plot how the posterior converges to the true bias. See how the prior matters early but washes out.
- **Likelihood ratio calculator:** Build a tool that takes prior odds + likelihood ratio and outputs posterior odds. Use it on medical test examples: disease prevalence 1%, test sensitivity 95%, specificity 95%. Compute P(disease | positive test). Feel the base rate fallacy in your gut.
- **MAP vs MLE:** Fit a polynomial to noisy data using both MLE (no regularization) and MAP (with Gaussian prior = L2 regularization). See how the prior prevents overfitting.
- **Calibration exercise:** Train a simple neural network classifier. Plot a calibration curve (predicted probability vs actual frequency). Is it overconfident? Apply temperature scaling and see calibration improve.
- **Key exercise:** You're an alignment researcher. Your prior: 30% chance a model has learned deceptive behavior. You run an interpretability test (sensitivity 80%, specificity 90%). The test comes back positive. What's your posterior? Now the test comes back negative on a retest. Update again. Feel how evidence accumulates.

## 🔗 ML Connection

- **Regularization IS Bayesian inference:** L2 regularization = Gaussian prior on weights. L1 = Laplace prior. Dropout ≈ approximate Bayesian inference. Understanding this unifies "engineering tricks" under one theoretical framework.
- **LLM training is approximate MLE:** next-token prediction maximizes likelihood. But we could do MAP instead (add priors on weights) — and in practice, weight decay does exactly this.
- **RLHF and KL penalties:** when fine-tuning with RLHF, the KL divergence penalty from the base model acts like a prior — "don't deviate too far from your initial beliefs." This is Bayesian in spirit.
- **Model uncertainty:** Bayesian neural networks maintain uncertainty over weights, giving principled uncertainty estimates. Standard networks give point estimates and are often overconfident.
- **Temperature scaling** in language models is a calibration technique that adjusts the "sharpness" of the predictive distribution — directly connected to proper scoring rules.

## 🧠 Alignment Connection

Bayesian thinking permeates alignment research:

- **Solomonoff induction** is the theoretical benchmark for prediction. Understanding it helps you reason about what "intelligence" means and what limits even a perfect predictor faces.
- **Deceptive alignment detection** is fundamentally a Bayesian problem: given behavioral evidence, what's the posterior probability that the model is deceptive? The prior matters enormously — and we don't know what the right prior is.
- **Eliciting Latent Knowledge (ELK)** asks: does the model's internal representation match reality? This is connected to whether the model has good "Bayesian beliefs" about the world.
- **Corrigibility and shutdownability:** some alignment proposals use Bayesian frameworks to reason about an AI's uncertainty about human values and whether it should defer to human judgment.
- **The rationalist community** (LessWrong, Alignment Forum) thinks in Bayesian terms extensively. Fluency with Bayesian reasoning is a prerequisite for reading most alignment philosophy.
