# Lesson 27: What Interpretability Researchers Actually Do

[← Transformer](../phase4-neural-networks/lesson-26-transformer.md) | [Back to TOC](../README.md) | [Next: Circuits →](lesson-28-circuits.md)

---

## 🎯 Core Learning

- The fundamental question: "Can we reverse-engineer neural networks into human-understandable programs?"
- Features vs. neurons: the superposition hypothesis (networks encode more concepts than they have neurons)
- Circuits: subgraphs of the network that implement specific behaviors
- Key techniques:
  - Direct logit attribution
  - Activation patching
  - Probing
  - Sparse autoencoders (SAEs) for finding features

## 📺 Watch — Primary

1. **Welch Labs — "The Dark Matter of AI [Mechanistic Interpretability]"**
   - https://www.youtube.com/@WelchLabs (search "Dark Matter of AI")
   - *24 minutes. The best accessible introduction to mechanistic interpretability that exists. Welch uses the "dark matter" framing — we can measure the effects of internal representations without being able to see them directly — and walks through superposition and sparse autoencoders with exceptional clarity. Watch this BEFORE any papers.*

2. **Neel Nanda's YouTube** — paper walkthroughs and research streams
   - Start with "Implementing GPT-2 from Scratch"
   - https://www.youtube.com/c/neaborius

## 📖 Read (core interpretability papers, in order)

1. **"A Mathematical Framework for Transformer Circuits"** (deeper re-read)
   - https://transformer-circuits.pub/2021/framework/index.html
2. **"In-context Learning and Induction Heads" (Olsson et al.)**
   - https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html
3. **"Toy Models of Superposition" (Elhage et al.)**
   - https://transformer-circuits.pub/2022/toy_model/index.html
4. **Neel Nanda's "Comprehensive Mechanistic Interpretability Explainer"**
   - https://www.neelnanda.io/mechanistic-interpretability/glossary

## 🔨 Do

- Install TransformerLens: `pip install transformer-lens`
- Load GPT-2, extract activations, visualize attention patterns
- Complete ARENA Chapter 1 mech interp tutorials on induction heads

## 🔗 ML Connection

This IS alignment work. You're learning the tools used by researchers at Anthropic, DeepMind, and elsewhere to understand what models are doing internally.
