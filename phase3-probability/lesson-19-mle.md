# Lesson 19: Maximum Likelihood Estimation

[← Expectation](lesson-18-expectation.md) | [Back to TOC](../README.md) | [Next: Information Theory →](lesson-20-information-theory.md)

---

## 🎯 Core Learning

- The central question: given data, what parameters best explain it?
- Likelihood function: probability of the data given the parameters
- MLE: find parameters that maximize likelihood
- Log-likelihood: turns products into sums
- MLE for Gaussians: the mean and variance formulas you know ARE MLE solutions
- **Connection to neural network training: minimizing cross-entropy loss = maximizing likelihood**

## 📖 Read

- **MML Book, Chapter 8.3** — maximum likelihood estimation

## 🔨 Do

- Implement MLE for a Gaussian: given data points, find best μ and σ
- Show that minimizing mean squared error = maximizing likelihood under Gaussian noise

## 🔗 ML Connection

When we train a language model to predict the next token, we are literally doing maximum likelihood estimation. The loss function (cross-entropy) IS the negative log-likelihood. This connection means you understand the fundamental training objective of every modern LLM.
