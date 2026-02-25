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

## 📺 Watch — Primary

1. **Aurélien Géron — "A Short Introduction to Entropy, Cross-Entropy and KL-Divergence"**
   - https://www.youtube.com/watch?v=ErfnhcEV1O8
   - *15 minutes. Covers all three concepts with clean visuals.*
2. **Luis Serrano — "A Friendly Introduction to Cross-Entropy Loss"**
   - https://www.youtube.com/watch?v=tRsSi_sqXjI
   - *Builds up cross-entropy from information theory with great intuition.*

## 📺 Watch — Secondary

3. **StatQuest — "Entropy, Clearly Explained!"**
   - https://www.youtube.com/results?search_query=statquest+entropy+clearly+explained
   - *StatQuest's trademark style applied to information theory.*
4. **Mutual Information (YouTube channel) — "Information Theory" playlist**
   - https://www.youtube.com/results?search_query=mutual+information+information+theory+entropy
   - *Deeper mathematical treatment with ML applications.*

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
