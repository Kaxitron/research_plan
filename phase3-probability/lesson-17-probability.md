# Lesson 17: Probability Distributions and Bayes' Theorem

[← Loss Landscapes](../phase2-calculus/lesson-16-loss-landscapes.md) | [Back to TOC](../README.md) | [Next: Expectation →](lesson-18-expectation.md)

---

## 🎯 Core Learning

- Probability as measuring uncertainty (frequentist vs. Bayesian views)
- Discrete distributions: Bernoulli, categorical (what a softmax output IS)
- Continuous distributions: Gaussian/normal (appears everywhere)
- Joint, marginal, and conditional probability
- Bayes' theorem: updating beliefs with evidence
- Prior → Evidence → Posterior: the fundamental pattern of learning

## 📺 Watch

- **3Blue1Brown — "Bayes theorem, the geometry of changing beliefs"**
  - https://www.youtube.com/watch?v=HZGCoVF3YvM
- **3Blue1Brown — "The quick proof of Bayes' theorem"**
  - https://www.youtube.com/watch?v=U_85TaXbeIo

## 📖 Read

- **MML Book, Chapter 6** — probability and distributions
- **"Seeing Theory"** — https://seeing-theory.brown.edu/ — beautiful interactive probability visualizations

## 🔨 Do

- Implement Bayes' theorem for a spam filter: given word frequencies, compute P(spam | words)
- Visualize 1D and 2D Gaussians (the 2D Gaussian is a contour map — connects to gradient work)

## 🔗 ML Connection

A language model's softmax output IS a categorical probability distribution over ~50,000 tokens. Bayesian reasoning is fundamental to model uncertainty and calibration — key alignment questions like "does the model know what it doesn't know?"
