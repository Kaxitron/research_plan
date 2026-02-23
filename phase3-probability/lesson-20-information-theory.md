# Lesson 20: Information Theory — Entropy, KL Divergence, Cross-Entropy

[← MLE](lesson-19-mle.md) | [Back to TOC](../README.md) | [Next: Bayesian Inference →](lesson-21-bayesian-inference.md)

---

## 🎯 Core Learning

- Information content: "surprising" events carry more information (−log p)
- Entropy: the average surprise of a distribution (measures uncertainty)
- Cross-entropy: average surprise when using distribution Q to encode events from P
- KL divergence: how "far apart" two distributions are (not a true distance!)
- **Cross-entropy loss = entropy + KL divergence:** minimizing cross-entropy pushes model toward truth
- Temperature in softmax: controlling "sharpness" of predictions

## 📺 Watch

- **Aurélien Géron — "A Short Introduction to Entropy, Cross-Entropy and KL-Divergence"** (YouTube)
- **Luis Serrano — "A Friendly Introduction to Cross-Entropy Loss"** (YouTube)

## 📖 Read

- **"Deep Learning" by Goodfellow et al., Chapter 3** — information theory section
  - https://www.deeplearningbook.org/
- **colah's blog — "Visual Information Theory"**
  - http://colah.github.io/posts/2015-09-Visual-Information/
  - *Gorgeous visual explanations*

## 🔨 Do

- Compute entropy of various distributions (uniform, peaked, bimodal)
- Implement cross-entropy loss from scratch
- Show that as model predictions approach true distribution, cross-entropy decreases

## 🔗 ML Connection

Cross-entropy is THE loss function for language modeling. KL divergence appears in RLHF training for alignment (the KL penalty keeps the model from drifting too far from the base model), in variational autoencoders, and in information-theoretic analyses of what networks learn. Temperature controls creative vs. focused outputs.
