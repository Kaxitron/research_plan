# Lesson 59: Attention — Dot Products in Action

[< Scaling Laws](lesson-58-scaling-laws.md) | [Back to TOC](../README.md) | [Next: Transformer >](lesson-60-transformer.md)

---

> **Welch Labs:** Ch. 8 (Attention) covers how DeepSeek's Multi-head Latent Attention modifies the original transformer.

> **Karpathy:** Zero to Hero #7 ("Let's build GPT") -- you build attention from scratch as part of the full GPT implementation.

## Core Learning

- Why sequence processing needs attention (the limitation of fixed-size representations)
- Queries, Keys, Values: three projections of the same input
- Attention scores as dot products (Lesson 9!)
- Softmax over scores: probability distribution over positions
- The attention matrix: entry (i,j) = "how much position i attends to position j"
- Multi-head attention: different heads learning different relationships
- The QK circuit and OV circuit: two sub-computations inside each head

## Watch (in order)

- **3Blue1Brown — "Transformers, the tech behind LLMs" | Deep Learning Ch. 5**
  - https://www.youtube.com/watch?v=wjZofJX0v4M
- **3Blue1Brown — "Attention in transformers, step-by-step" | Deep Learning Ch. 6**
  - https://www.youtube.com/watch?v=eMlx5fFNoYc

## Read

- **Welch Labs — *The Illustrated Guide to AI*, Ch. 8: Attention**
  - http://www.welchlabs.com/resources/ai-book
  - *How DeepSeek's Multi-head Latent Attention modifies the original transformer. Code and exercises included.*
- **"Attention is All You Need" (Vaswani et al., 2017)** — the original paper
- **Welch Labs — "How DeepSeek Rewrote the Transformer" (Ch. 8: Attention)**
  - https://www.youtube.com/watch?v=cAxYGT4VtBo
  - *Book: Welch Labs, "The Illustrated Guide to AI," Ch. 8: Attention*
  - *After the 3B1B videos, watch this to see a real frontier modification: Multi-head Latent Attention.*

- **"The Illustrated Transformer" by Jay Alammar**
  - https://jalammar.github.io/illustrated-transformer/

## Do

**1. Implement single-head attention from scratch (NumPy)**

Given an input matrix `X` of shape `(seq_len, d_model)`:

```python
Q = X @ W_Q  # (seq_len, d_k)
K = X @ W_K  # (seq_len, d_k)
V = X @ W_V  # (seq_len, d_v)
scores = Q @ K.T / sqrt(d_k)  # (seq_len, seq_len)
weights = softmax(scores, axis=-1)
output = weights @ V  # (seq_len, d_v)
```

Initialize `W_Q, W_K, W_V` randomly. Run on a toy sequence of 5 vectors of dimension 8.

**2. Visualize the attention matrix**

Plot `weights` as a heatmap using `matplotlib.imshow`. Label axes with token positions. Each row shows where that position "looks" — the distribution should sum to 1 across columns.

**3. Add causal masking**

Before softmax, set all entries above the diagonal to `-inf`:
```python
mask = np.triu(np.ones((seq_len, seq_len)), k=1) * -1e9
scores = scores + mask
```

Re-visualize. Now each position can only attend to itself and earlier positions — this is how GPT prevents "seeing the future."

**4. Begin Karpathy's GPT build — follow ZtH #7 (0:00–0:45)**

Start Karpathy's "Let's build GPT" video. In the first 45 minutes he sets up:
- Character-level tokenization on Shakespeare
- Bigram baseline model
- Self-attention from scratch

Type every line. Stop when he starts multi-head attention — that's Lesson 60.

## ML and Alignment Connection

The attention mechanism is the heart of every modern LLM, including Claude. Alignment researchers at Anthropic and elsewhere analyze *what* each head learns to attend to: some heads copy tokens, some track syntax, some handle entity tracking. Crucially, some heads learn to attend to safety-relevant patterns — detecting harmful requests, tracking conversation context for consistency, or implementing "refusal circuits."

The **induction head** — a specific attention circuit that learns in-context learning — is the most important circuit discovery in mechanistic interpretability. Understanding attention mechanistically is the foundation for understanding how models implement (or fail to implement) aligned behavior.
