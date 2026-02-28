# Lesson 53: Kolmogorov Complexity, Algorithmic Information, and Solomonoff Induction

[← Computational Complexity](lesson-52-computational-complexity.md) | [Back to TOC](../README.md) | [Next: Groups →](lesson-54-groups.md)

---

> **Why this lesson exists:** Kolmogorov complexity gives a formal definition of "simplicity" — the complexity of an object is the length of the shortest program that produces it. This connects to Occam's razor, data compression, and the deepest questions about induction. Solomonoff induction — the theoretical ideal of Bayesian learning with a universal prior — provides the gold standard for prediction, and understanding why it's uncomputable tells you exactly what practical learning algorithms are approximating.

## 🎯 Core Concepts

### Kolmogorov Complexity — The Shortest Description

- **K(x)** = the length of the shortest program that outputs x and halts, on a fixed universal Turing machine. It measures the "true" information content of x.
- **Random strings have high K:** a random 1000-bit string needs ~1000 bits to describe (you can't compress randomness). A patterned string like "0101...01" has low K — the program "print '01' 500 times" is much shorter than the string itself.
- **K is uncomputable** (by the halting problem — you can't know when you've found the shortest program). But it's the theoretical ideal that practical compression algorithms approximate.
- **Invariance theorem:** the choice of UTM changes K(x) by at most a constant. So K is well-defined up to an additive constant — the "language" doesn't matter for large x.

### Algorithmic Information Theory — Connecting to Shannon

- **Shannon entropy** measures the expected information content of a random variable (an ensemble of possible messages). **Kolmogorov complexity** measures the information content of a specific individual string.
- **For most strings from a distribution:** K(x) ≈ H(X) (Shannon entropy ≈ Kolmogorov complexity). The typical string from a source has complexity close to the entropy rate. But individual strings can deviate wildly.
- **Minimum Description Length (MDL):** choose the model that minimizes (description of model) + (description of data given model). This is the computable approximation to Kolmogorov-based model selection. It's closely related to BIC and to the free energy from Lesson 37.

### Solomonoff Induction — The Perfect Predictor

- **Solomonoff's prior:** assign probability 2^{-K(x)} to each possible future. Longer programs (more complex hypotheses) get exponentially less weight. This IS Occam's razor as a mathematical prior — the universal prior.
- **Solomonoff induction** uses this prior with Bayesian updating: observe data D, update the posterior over programs, predict the next observation by averaging over all programs weighted by posterior probability.
- **It's optimal:** Solomonoff induction converges to the true distribution faster than any other predictor (under mild assumptions). It's the theoretical ideal of learning.
- **It's uncomputable:** computing K(x) requires solving the halting problem. So Solomonoff induction can't be implemented. But it tells you what a perfect learner would do, and practical algorithms can be seen as computable approximations.

### AIXI — The Optimal Agent

- **AIXI** (Hutter, 2000) extends Solomonoff induction to the agent setting: AIXI is a reinforcement learning agent that uses the Solomonoff prior to model its environment and takes actions maximizing expected future reward.
- **AIXI is:** provably optimal (in a formal sense), incomputable, and potentially dangerous (it doesn't distinguish between "achieving the goal" and "taking control of the reward signal").
- **For alignment:** AIXI illustrates that even a *provably optimal* agent can be misaligned if the reward signal doesn't capture what you actually want. Optimization power and alignment are orthogonal.

### Practical Implications

- **Neural networks and compression:** training a neural network IS finding a compressed representation of the data. The weights encode a "program" for generating the data distribution. Better compression = better generalization (MDL principle).
- **Generalization as simplicity:** models that generalize well tend to have low description complexity relative to the data they explain. This connects to SLT (the RLCT measures effective complexity) and to the implicit bias of gradient descent (it finds "simple" solutions).

## 📺 Watch — Primary

1. **Computerphile — "Kolmogorov Complexity"**
2. **Robert Miles — "AIXI" (AI Safety series)**

## 📖 Read — Primary

- **"An Introduction to Kolmogorov Complexity and Its Applications" by Li & Vitanyi** — Chapters 1–2
- **"Universal Artificial Intelligence" by Hutter** — overview chapters

## 🔨 Do

- Estimate Kolmogorov complexity: for 5 different bit strings, find the shortest Python program that produces each. Compare with gzip compressed size.
- Implement a simple MDL model selector: given data, compare models by (code length) + (data given model length). Show it selects the correct model complexity.
- Solomonoff prediction toy example: enumerate all programs up to length 20 on a tiny language. Compute the Solomonoff prediction for the next bit of "01010101..." Show it correctly predicts "0."
- Essay: Why is AIXI both optimal and potentially dangerous? What does this tell us about the relationship between intelligence and alignment?
