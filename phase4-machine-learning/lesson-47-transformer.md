# Lesson 47: Building a Transformer from Scratch

[← Attention](lesson-46-attention.md) | [Back to TOC](../README.md) | [Next: RL Foundations →](lesson-48-rl-foundations.md)

---

## 🎯 Core Learning

- Token embeddings: words → vectors (a learned lookup table)
- Positional encodings: giving the model a sense of order
- The full transformer block: attention → add & norm → MLP → add & norm
- Stacking blocks: depth = abstraction
- MLP layers: what they do between attention (possibly store facts)
- Causal masking: preventing the model from "seeing the future"
- The complete GPT architecture from input to next-token prediction
- **Modern variants:** Multi-head Latent Attention (MLA) as used in DeepSeek

## 📺 Watch — Primary

1. **Karpathy — "Let's build GPT: from scratch, in code, spelled out" (Lecture 7)**
   - https://www.youtube.com/watch?v=kCc8FmEb1nY
   - *~2 hours. You build a working GPT from scratch. Transformative.*

2. **3Blue1Brown — "How might LLMs store facts" | Deep Learning Ch. 7**
   - https://www.youtube.com/watch?v=9-Jl0dxWQs8

## 📺 Watch — Secondary

3. **Welch Labs — "How DeepSeek Rewrote the Transformer [MLA]"**
   - https://www.youtube.com/watch?v=cAxYGT4VtBo
   - *📖 Book: Welch Labs, "The Illustrated Guide to AI," Ch. 8: Attention*
   - *18 minutes. After building a standard GPT, this shows you a real frontier modification: Multi-head Latent Attention, the architectural innovation that made DeepSeek 57× more efficient. Watch AFTER Karpathy to appreciate what's being changed and why.*

## 📺 Watch — Optional

4. **Andrej Karpathy — "Let's reproduce GPT-2 (124M)"**
   - https://www.youtube.com/watch?v=l8pRSuU81PU
   - *~4 hours. Reproduces GPT-2 from scratch with distributed training. Optional but invaluable if you want hands-on transformer engineering experience.*

## 📖 Read

- **Welch Labs — *The Illustrated Guide to AI*, Ch. 8: Attention**
  - http://www.welchlabs.com/resources/ai-book
  - *Pairs with the Karpathy GPT build — the book covers the same architecture from a different angle.*
- **"A Mathematical Framework for Transformer Circuits" (Elhage, Nanda, et al.)**
  - https://transformer-circuits.pub/2021/framework/index.html
  - *The foundational paper of mechanistic interpretability. Uses ALL the linear algebra you learned.*
- **Neel Nanda's walkthrough of the above**
  - https://www.neelnanda.io/mechanistic-interpretability/a-walkthrough-of-a-mathematical-framework-for-transformer-circuits
  - **Video walkthrough:** https://www.youtube.com/watch?v=KV5gbOmHbjU

## 🔨 Do

- Complete Karpathy's GPT build — type every line, run it, generate text
- Optionally: ARENA Chapter 1 exercises (building GPT-3 from scratch)
  - https://arena-ch1-transformers.streamlit.app/

## 🔗 ML & Alignment Connection

You now understand the complete architecture of every frontier AI system, including Claude. Every interpretability technique — activation patching, logit attribution, circuit analysis — operates on this architecture. Every alignment training method — RLHF, constitutional AI, DPO — modifies these weights through backpropagation. Understanding the transformer end-to-end means you can now engage with the central question: *how do we ensure systems built on this architecture behave in accordance with human values?*
