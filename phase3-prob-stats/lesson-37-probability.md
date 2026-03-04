# Lesson 37: Probability Distributions and Bayes' Theorem

[← Loss Landscapes](../phase2-calculus/lesson-36-loss-landscapes.md) | [Back to TOC](../README.md) | [Next: Expectation →](lesson-38-expectation.md)

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
- **3Blue1Brown — "But what is the Central Limit Theorem?"**
  - https://www.youtube.com/watch?v=zeJD6dqJ5lo
  - *Why the normal distribution appears everywhere. Essential for understanding hypothesis testing (Lesson 35).*
- **3Blue1Brown — "Why π is in the normal distribution"**
  - https://www.youtube.com/watch?v=cy8r7WSuT1I
  - *The geometric reason π shows up in the bell curve — connects integration, circles, and probability.*
- **3Blue1Brown — "Binomial distributions"**
  - https://www.youtube.com/watch?v=8idr1WZ1A7Q
  - *Visualizes discrete probability before continuous. The binomial → normal connection is the CLT in action.*
- **StatQuest — Statistics Fundamentals playlist**
  - https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9
  - *Histograms, mean, variance, and probability distributions — Josh Starmer's clear, visual approach to foundations.*

## 📖 Read

- **MML Book, Chapter 6** — probability and distributions
- **"Seeing Theory"** — https://seeing-theory.brown.edu/ — beautiful interactive probability visualizations

## 🔨 Do

- Implement Bayes' theorem for a spam filter: given word frequencies, compute P(spam | words)
- Visualize 1D and 2D Gaussians (the 2D Gaussian is a contour map — connects to gradient work)

### 💻 Coding Mini-Project: Naive Bayes Text Classifier from Scratch (~60 lines)

Build a working text classifier with no sklearn — just Python dictionaries and basic math:

```python
class NaiveBayes:
    def fit(self, texts, labels):
        """Learn word frequencies for each class."""
        self.class_priors = {}     # P(class)
        self.word_probs = {}       # P(word | class) with Laplace smoothing
        ...

    def predict(self, text):
        """Return the most probable class for a new text."""
        # Compute log P(class) + Σ log P(word | class) for each class
        ...
```

**Your tasks:**
1. Implement `fit()`: count word frequencies per class, apply Laplace smoothing (add 1 to all counts)
2. Implement `predict()`: use **log probabilities** to avoid underflow (multiplying many small numbers → 0)
3. Create a tiny dataset of 20 sentences (10 "positive", 10 "negative" movie reviews — make them up)
4. Train on 16, test on 4. Print predictions with confidence scores
5. Add a `predict_proba()` method that returns the actual posterior probabilities (hint: softmax of log-probs)

**Why log probabilities?** This is your first encounter with a universal pattern in ML: we always work in log-space because computers can't multiply 1000 small probabilities without underflow. Cross-entropy loss, log-likelihood, logits — all the same idea.

**Programming skills practiced:** dictionaries, string processing, log-space arithmetic, class design with fit/predict pattern

## 🔗 ML & Alignment Connection

A language model's softmax output IS a categorical probability distribution over ~50,000 tokens. Bayesian reasoning is fundamental to model uncertainty and calibration — key alignment questions like "does the model know what it doesn't know?"
