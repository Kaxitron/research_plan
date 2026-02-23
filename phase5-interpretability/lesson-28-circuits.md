# Lesson 28: Circuits and Features in Practice

[← Intro to Interp](lesson-27-intro-interp.md) | [Back to TOC](../README.md) | [Next: Game Theory →](../phase6-alignment-theory/lesson-29-game-theory.md)

---

## 🎯 Core Learning

- The residual stream as "shared communication channel" (a high-dimensional vector space where all components read/write)
- Induction heads: the first discovered "circuit" — how models copy patterns
- Indirect Object Identification: a complex real-world circuit in GPT-2
- Sparse autoencoders: training a separate network to decompose activations into interpretable features
- Anthropic's "Scaling Monosemanticity" — finding millions of features in Claude

## 📖 Read

- **"Scaling Monosemanticity" (Anthropic, 2024)**
  - https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html
- **"Circuits Updates" (latest)** — current state of interpretability research
  - https://transformer-circuits.pub/
- **Neel Nanda — "How to Become a Mechanistic Interpretability Researcher"**
  - https://www.neelnanda.io/mechanistic-interpretability/getting-started

## 🔨 Do

- Replicate induction head finding in a 2-layer transformer using TransformerLens
- Run activation patching on a simple task
- Explore Anthropic's Neuronpedia or similar feature visualization tools
