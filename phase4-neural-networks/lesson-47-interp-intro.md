# Lesson 47: Interpretability — What Researchers Actually Do

[← LLM Pipeline](lesson-46-llm-pipeline.md) | [Back to TOC](../README.md) | [Next: Interpretability — Circuits →](lesson-48-interp-circuits.md)

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
   - https://www.youtube.com/watch?v=UGO_Ehywuxc
   - *📖 Book: Welch Labs, "The Illustrated Guide to AI," Ch. 7: Mechanistic Interpretability*
   - *24 minutes. The best accessible introduction to mechanistic interpretability that exists. Welch uses the "dark matter" framing — we can measure the effects of internal representations without being able to see them directly — and walks through superposition and sparse autoencoders with exceptional clarity. Watch this BEFORE any papers.*

3. **Welch Labs — "The Moment We Stopped Understanding AI" (Ch. 5: AlexNet)**
   - https://www.youtube.com/watch?v=UZDiGooFs54
   - *📖 Book: Welch Labs, "The Illustrated Guide to AI," Ch. 5: AlexNet*
   - *17 minutes. Feature visualization, activation atlases, and why we stopped understanding what neural nets learn. Sets up the interpretability problem.*

2. **Neel Nanda's YouTube** — paper walkthroughs and research streams
   - Start with "Implementing GPT-3 from Scratch"
   - https://www.youtube.com/@neelnanda2469

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

## 🔗 ML & Alignment Connection

Mechanistic interpretability IS alignment research. The bet: if we can understand *what* models are computing internally — not just their input-output behavior — we can detect deceptive alignment, verify safety properties, and build more trustworthy systems. This lesson marks the transition from "learning the prerequisites" to "doing the actual work." The tools you learn here (TransformerLens, activation analysis, attention visualization) are the same tools used by researchers at Anthropic, DeepMind, and elsewhere to study whether frontier models are safe to deploy.
