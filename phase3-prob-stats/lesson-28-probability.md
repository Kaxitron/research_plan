# Lesson 28: Probability Distributions and Bayes' Theorem

[← PDEs](../phase2-calculus/lesson-27-pdes.md) | [Back to TOC](../README.md) | [Next: Expectation →](lesson-29-expectation.md)

---

## 🎯 Core Learning

- Probability as measuring uncertainty (frequentist vs. Bayesian views)
- Discrete distributions: Bernoulli, categorical (what a softmax output IS)
- Continuous distributions: Gaussian/normal (appears everywhere)
- Joint, marginal, and conditional probability
- Bayes' theorem: updating beliefs with evidence
- Prior → Evidence → Posterior: the fundamental pattern of learning

### Change of Variables — How Transformations Affect Probability

- **The problem:** if x has distribution p(x), and you apply a transformation y = f(x), what is the distribution of y?
- **The key formula (1D):** p(y) = p(x) · |dx/dy| = p(f⁻¹(y)) · |df⁻¹/dy|. The Jacobian factor accounts for how the transformation stretches or compresses space.
- **Intuition:** if f stretches a region, the probability there must decrease (same probability mass over more space = lower density). If f compresses, density increases. The |det(J)| factor measures exactly this stretching.
- **Multivariate version:** p(y) = p(f⁻¹(y)) · |det(J_f⁻¹)|, where J is the Jacobian matrix.
- **Where this matters in ML:**
  - **Normalizing flows:** neural networks that learn invertible transformations. They start with a simple distribution (Gaussian) and apply learned transformations. The change of variables formula tells you the resulting probability density — and the training uses log |det(J)| explicitly. This is why determinants (Lesson 7) matter for generative models!
  - **Reparameterization trick** in VAEs: transform a simple z ~ N(0,1) into the desired distribution by learning the right transformation.
  - **Log-normal, chi-squared, etc.:** many common distributions are just Gaussians passed through transformations.
- **MML Book, Chapter 6.7** covers this with clear worked examples.

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
