# Lesson 60: Building a Transformer from Scratch

[< Attention](lesson-59-attention.md) | [Back to TOC](../README.md) | [Next: Mechanistic Interpretability >](lesson-61-mech-interp.md)

---

> **Karpathy:** Zero to Hero #7 ("Let's build GPT") is the centerpiece -- you build a working GPT from scratch. Zero to Hero #9 ("Let's reproduce GPT-2") extends this to full-scale reproduction with distributed training.

## Core Learning

- Token embeddings: words → vectors (a learned lookup table)
- Positional encodings: giving the model a sense of order
- The full transformer block: attention → add & norm → MLP → add & norm
- Stacking blocks: depth = abstraction
- MLP layers: what they do between attention (possibly store facts)
- Causal masking: preventing the model from "seeing the future"
- The complete GPT architecture from input to next-token prediction
- **Modern variants:** Multi-head Latent Attention (MLA) as used in DeepSeek

## Watch -- Primary

1. **Karpathy -- "Let's build GPT: from scratch, in code, spelled out" (Zero to Hero #7)**
   - https://www.youtube.com/watch?v=kCc8FmEb1nY
   - *~2 hours. You build a working GPT from scratch. Transformative.*

2. **3Blue1Brown — "How might LLMs store facts" | Deep Learning Ch. 7**
   - https://www.youtube.com/watch?v=9-Jl0dxWQs8

## Watch -- Secondary

3. **Welch Labs — "How DeepSeek Rewrote the Transformer [MLA]"**
   - https://www.youtube.com/watch?v=cAxYGT4VtBo
   - *Book: Welch Labs, "The Illustrated Guide to AI," Ch. 8: Attention*
   - *18 minutes. After building a standard GPT, this shows you a real frontier modification: Multi-head Latent Attention, the architectural innovation that made DeepSeek 57× more efficient. Watch AFTER Karpathy to appreciate what's being changed and why.*

## Watch -- Optional

4. **Andrej Karpathy -- "Let's reproduce GPT-2 (124M)" (Zero to Hero #9)**
   - https://www.youtube.com/watch?v=l8pRSuU81PU
   - *~4 hours. Reproduces GPT-2 from scratch with distributed training. Optional but invaluable if you want hands-on transformer engineering experience.*

## Read

- **Welch Labs — *The Illustrated Guide to AI*, Ch. 8: Attention**
  - http://www.welchlabs.com/resources/ai-book
  - *Pairs with the Karpathy GPT build — the book covers the same architecture from a different angle.*
- **"A Mathematical Framework for Transformer Circuits" (Elhage, Nanda, et al.)**
  - https://transformer-circuits.pub/2021/framework/index.html
  - *The foundational paper of mechanistic interpretability. Uses ALL the linear algebra you learned.*
- **Neel Nanda's walkthrough of the above**
  - https://www.neelnanda.io/mechanistic-interpretability/a-walkthrough-of-a-mathematical-framework-for-transformer-circuits
  - **Video walkthrough:** https://www.youtube.com/watch?v=KV5gbOmHbjU

## Do

**1. Complete Karpathy's GPT build — follow ZtH #7 (full video)**

Continue from Lesson 59 and build the complete GPT from scratch. Karpathy adds:
- **Multi-head attention** (~0:45): split Q, K, V into `n_heads` parallel heads, concatenate outputs
- **Feed-forward network** (~1:10): two linear layers with ReLU between them, applied per-position
- **Residual connections** (~1:20): `x = x + attention(x)` and `x = x + ffn(x)` — the "residual stream"
- **Layer normalization** (~1:25): normalize before each sub-layer (pre-norm)
- **Stacking blocks** (~1:30): repeat the transformer block `n_layers` times
- **Training** (~1:40): train on Shakespeare text with cross-entropy loss

Type every line. By the end you have a working GPT that generates Shakespeare-like text.

**2. Generate text and evaluate**

Generate 500 characters from your trained model. It won't be Shakespeare, but it should produce:
- Correctly structured lines (capitalization, line breaks)
- English-like words (many real words mixed with plausible nonsense)
- Some character names and stage directions

Save a few generations — you'll compare to the makemore output from Lesson 56 to see the power of attention over fixed-context MLPs.

**3. Experiment with architecture**

Try varying one hyperparameter at a time and observe the effect on loss:
- `n_heads`: 1 vs 4 vs 8 (more heads = better, up to a point)
- `n_layers`: 1 vs 4 vs 6 (depth matters for compositional patterns)
- `d_model`: 64 vs 128 vs 256 (wider = more capacity per layer)

You don't need full training runs — just train for 2000 steps each and compare final loss.

**4. Optional: GPT-2 reproduction — Karpathy ZtH #9**

If time allows, follow Karpathy's ~4-hour GPT-2 reproduction video. This covers distributed training, weight loading from Hugging Face, and matching OpenAI's published numbers. This is optional but deeply educational if you want engineering experience.

## ML and Alignment Connection

You now understand the complete architecture of every frontier AI system, including Claude. Every interpretability technique — activation patching, logit attribution, circuit analysis — operates on this architecture. Every alignment training method — RLHF, constitutional AI, DPO — modifies these weights through backpropagation. Understanding the transformer end-to-end means you can now engage with the central question: *how do we ensure systems built on this architecture behave in accordance with human values?*
