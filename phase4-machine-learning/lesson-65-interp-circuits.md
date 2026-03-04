# Lesson 65: Interpretability -- Circuits, Features, and Superposition

[< LLM Pipeline](lesson-64-llm-pipeline.md) | [Back to TOC](../README.md) | [Next: Interpretability -- SLT >](lesson-66-interp-slt.md)

---

## Core Learning

- The residual stream as "shared communication channel" (a high-dimensional vector space where all components read/write)
- **Induction heads:** the first discovered "circuit" -- how models copy patterns. A two-head circuit where Head A attends to the previous occurrence of the current token, and Head B copies the token that followed. This implements in-context learning.
- **Feature circuits:** subgraphs of the network that implement specific, interpretable computations. Finding and understanding circuits is how we answer questions like "Does this model have a deception circuit?"
- **Sparse autoencoders (SAEs):** train a separate network to decompose activations into interpretable features. The encoder maps activations to a high-dimensional sparse representation; the decoder reconstructs. The sparsity constraint forces each feature to be monosemantic (one meaning).
- **Superposition:** networks encode more features than they have dimensions. A 512-dimensional residual stream might encode thousands of features using almost-orthogonal directions. This is possible because most features are rarely active simultaneously.
- **Polysemanticity:** a single neuron responds to multiple unrelated concepts (e.g., a neuron that activates for both "cat photos" and "the word 'and'"). This is the neuron-level consequence of superposition and why neurons are not the right unit of analysis.
- **Toy models of superposition:** Elhage et al. show that even simple networks learn superposition when there are more features than dimensions, and sparsity makes it efficient.

## Watch -- Primary

1. **Neel Nanda -- "Walkthrough of A Mathematical Framework for Transformer Circuits"**
   - https://www.youtube.com/@neelnanda2469
   - Key video: [Walkthrough of Transformer Circuits](https://www.youtube.com/watch?v=KV5gbOmHbjU)
   - *Stream-of-consciousness video walkthrough of the foundational Transformer Circuits paper. Neel explains every equation and connects them to real model behavior.*
2. **Neel Nanda -- YouTube channel (paper walkthroughs and research streams)**
   - https://www.youtube.com/@neelnanda2469
   - *Browse his research stream videos -- he walks through his actual research process, which is invaluable for learning how mech interp is done in practice.*

## Watch -- Secondary

3. **AXRP Episode 19 -- "Mechanistic Interpretability with Neel Nanda"**
   - https://axrp.net/episode/2023/02/04/episode-19-mechanistic-interpretability-neel-nanda.html
   - *2.5-hour deep dive into transformer circuits, induction heads, and grokking. Technical but extremely informative. Listen to the induction heads section (starts ~1:59:42) at minimum.*
4. **The Inside View -- "Neel Nanda on mechanistic interpretability, superposition and grokking"**
   - https://www.youtube.com/watch?v=cVBGjhN4-1g
   - *Covers the mindset of a mech interp researcher, the linear representation hypothesis, and superposition.*
5. **3Blue1Brown -- "How might LLMs store facts" | Deep Learning Ch. 7**
   - https://www.youtube.com/watch?v=9-Jl0dxWQs8
   - *Visualizes how MLP layers might store factual knowledge -- connects to the circuits perspective.*
6. **MLST -- Neel Nanda on Sparse Autoencoders**
   - https://open.spotify.com/episode/5XjHhNQxIb16eJZXGmbaCk
   - *How sparse autoencoders decompose superposition into interpretable features. A key modern technique.*

## Read

- **"Scaling Monosemanticity" (Anthropic, 2024)**
  - https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html
- **"Toy Models of Superposition" (Elhage et al.)**
  - https://transformer-circuits.pub/2022/toy_model/index.html
  - *The foundational paper on superposition. Shows that even simple models learn to encode more features than they have dimensions.*
- **"Circuits Updates" (latest)** -- current state of interpretability research
  - https://transformer-circuits.pub/
- **Neel Nanda -- "How to Become a Mechanistic Interpretability Researcher"**
  - https://www.neelnanda.io/mechanistic-interpretability/getting-started

## Do

- Replicate induction head finding in a 2-layer transformer using TransformerLens
- Run activation patching on a simple task (e.g., indirect object identification)
- Explore Anthropic's Neuronpedia or similar feature visualization tools
- **SAE exercise:** train a sparse autoencoder on MLP activations from a small transformer. Examine the learned features -- do they correspond to interpretable concepts?

## ML and Alignment Connection

**Circuits** are the mechanistic interpretability researcher's unit of analysis -- small subnetworks that implement specific, interpretable computations. Finding and understanding circuits is how we answer questions like: "Does this model have a deception circuit?" "Where does refusal behavior originate?" "Can we surgically remove dangerous capabilities while preserving useful ones?" The induction head circuit (this lesson's main focus) proved that transformers learn interpretable algorithms, not just statistical patterns. This is what makes the alignment research program via interpretability viable.

**Superposition** is the central obstacle: if models encode more concepts than they have dimensions, individual neurons are uninterpretable. SAEs are the leading tool for breaking through superposition -- decomposing the tangled activations into clean, monosemantic features. Anthropic's "Scaling Monosemanticity" demonstrated this works at scale, finding millions of interpretable features in Claude.
