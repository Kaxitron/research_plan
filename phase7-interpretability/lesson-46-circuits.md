# Lesson 46: Circuits and Features in Practice

[← Intro to Interp](lesson-45-intro-interp.md) | [Back to TOC](../README.md) | [Next: Scaling Laws & Emergence →](lesson-47-scaling-emergence.md)

---

## 🎯 Core Learning

- The residual stream as "shared communication channel" (a high-dimensional vector space where all components read/write)
- Induction heads: the first discovered "circuit" — how models copy patterns
- Indirect Object Identification: a complex real-world circuit in GPT-2
- Sparse autoencoders: training a separate network to decompose activations into interpretable features
- Anthropic's "Scaling Monosemanticity" — finding millions of features in Claude

## 📺 Watch — Primary

1. **Neel Nanda — "Walkthrough of A Mathematical Framework for Transformer Circuits"**
   - https://www.youtube.com/@neelnanda2469
   - *Stream-of-consciousness video walkthrough of the foundational Transformer Circuits paper. Neel explains every equation and connects them to real model behavior.*
2. **Neel Nanda — YouTube channel (paper walkthroughs and research streams)**
   - https://www.youtube.com/@neelnanda2469
   - *Browse his research stream videos — he walks through his actual research process, which is invaluable for learning how mech interp is done in practice.*

## 📺 Watch — Secondary

3. **AXRP Episode 19 — "Mechanistic Interpretability with Neel Nanda"**
   - https://axrp.net/episode/2023/02/04/episode-19-mechanistic-interpretability-neel-nanda.html
   - *2.5-hour deep dive into transformer circuits, induction heads, and grokking. Technical but extremely informative. Listen to the induction heads section (starts ~1:59:42) at minimum.*
4. **The Inside View — "Neel Nanda on mechanistic interpretability, superposition and grokking"**
   - Search YouTube for "The Inside View Neel Nanda"
   - *Covers the mindset of a mech interp researcher, the linear representation hypothesis, and superposition.*
5. **3Blue1Brown — "How might LLMs store facts" | Deep Learning Ch. 7**
   - https://www.youtube.com/watch?v=9-Jl0dxWQs8
   - *Visualizes how MLP layers might store factual knowledge — connects to the circuits perspective.*

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
