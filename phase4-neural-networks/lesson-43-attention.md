# Lesson 43: Attention — Dot Products in Action

[← Backpropagation](lesson-42-backprop.md) | [Back to TOC](../README.md) | [Next: Transformer →](lesson-44-transformer.md)

---

## 🎯 Core Learning

- Why sequence processing needs attention (the limitation of fixed-size representations)
- Queries, Keys, Values: three projections of the same input
- Attention scores as dot products (Lesson 9!)
- Softmax over scores: probability distribution over positions
- The attention matrix: entry (i,j) = "how much position i attends to position j"
- Multi-head attention: different heads learning different relationships
- The QK circuit and OV circuit: two sub-computations inside each head

## 📺 Watch (in order)

- **3Blue1Brown — "Transformers, the tech behind LLMs" | Deep Learning Ch. 5**
  - https://www.youtube.com/watch?v=wjZofJX0v4M
- **3Blue1Brown — "Attention in transformers, step-by-step" | Deep Learning Ch. 6**
  - https://www.youtube.com/watch?v=eMlx5fFNoYc

## 📖 Read

- **"Attention is All You Need" (Vaswani et al., 2017)** — the original paper
- **Welch Labs — "How DeepSeek Rewrote the Transformer" (Ch. 8: Attention)**
  - https://www.youtube.com/watch?v=cAxYGT4VtBo
  - *📖 Book: Welch Labs, "The Illustrated Guide to AI," Ch. 8: Attention*
  - *After the 3B1B videos, watch this to see a real frontier modification: Multi-head Latent Attention.*

- **"The Illustrated Transformer" by Jay Alammar**
  - https://jalammar.github.io/illustrated-transformer/

## 🔨 Do

- Implement single-head attention from scratch in NumPy
- Compute an attention matrix for a small sequence, visualize as heatmap
- Begin Karpathy's "Let's build GPT" (Lecture 7)

## 🔗 ML & Alignment Connection

The attention mechanism is the heart of every modern LLM, including Claude. Alignment researchers at Anthropic and elsewhere analyze *what* each head learns to attend to: some heads copy tokens, some track syntax, some handle entity tracking. Crucially, some heads learn to attend to safety-relevant patterns — detecting harmful requests, tracking conversation context for consistency, or implementing "refusal circuits."

The **induction head** — a specific attention circuit that learns in-context learning — is the most important circuit discovery in mechanistic interpretability. Understanding attention mechanistically is the foundation for understanding how models implement (or fail to implement) aligned behavior.
