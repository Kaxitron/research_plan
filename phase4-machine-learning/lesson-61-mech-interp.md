# Lesson 61: Mechanistic Interpretability -- The Dark Matter of AI

[< Transformer](lesson-60-transformer.md) | [Back to TOC](../README.md) | [Next: Diffusion Models >](lesson-62-diffusion-models.md)

---

> **Welch Labs framing:** Welch uses the "dark matter" analogy -- we can measure the effects of internal representations without being able to see them directly. Sparse autoencoders are the telescope that lets us peer into the dark matter of neural networks. Watch Ch. 7 BEFORE any papers.

## Core Learning

- The fundamental question: "Can we reverse-engineer neural networks into human-understandable programs?"
- Activation patching: intervene on a specific activation and measure the downstream effect on output
- Probing: train a small classifier on internal activations to test whether a representation encodes a concept
- Logit lens / tuned lens: read off the model's "current best guess" at intermediate layers by projecting to the vocabulary
- Steering vectors: add a direction in activation space to steer model behavior (e.g., add a "truthfulness" direction)
- Direct logit attribution: decompose the final logit into contributions from each component (head, MLP, embedding)
- TransformerLens: the primary Python library for mechanistic interpretability research
- Hooks: inserting custom functions at specific points in the forward pass to read or modify activations

## Watch -- Primary

1. **Welch Labs -- "The Dark Matter of AI [Mechanistic Interpretability]"**
   - https://www.youtube.com/watch?v=UGO_Ehywuxc
   - *Book: Welch Labs, "The Illustrated Guide to AI," Ch. 7: Mechanistic Interpretability*
   - *24 minutes. The best accessible introduction to mechanistic interpretability that exists. Welch uses the "dark matter" framing and walks through superposition and sparse autoencoders with exceptional clarity. Watch this BEFORE any papers.*

2. **Welch Labs -- "The Moment We Stopped Understanding AI" (Ch. 5: AlexNet)**
   - https://www.youtube.com/watch?v=UZDiGooFs54
   - *Book: Welch Labs, "The Illustrated Guide to AI," Ch. 5: AlexNet*
   - *17 minutes. Feature visualization, activation atlases, and why we stopped understanding what neural nets learn. Sets up the interpretability problem.*

3. **Neel Nanda's YouTube** -- paper walkthroughs and research streams
   - Start with "Implementing GPT-3 from Scratch"
   - https://www.youtube.com/@neelnanda2469
   - **Getting Started Guide:** https://www.neelnanda.io/mechanistic-interpretability/getting-started
   - *Neel's curated roadmap for entering mech interp research. Read this early for orientation.*

## Read

- **Welch Labs -- *The Illustrated Guide to AI*, Ch. 5: AlexNet + Ch. 7: Mechanistic Interpretability**
  - http://www.welchlabs.com/resources/ai-book
  - *Ch. 5 covers the moment neural nets became too complex to understand. Ch. 7 introduces mech interp as a response.*
- **"A Mathematical Framework for Transformer Circuits"** (deeper re-read)
  - https://transformer-circuits.pub/2021/framework/index.html
- **"In-context Learning and Induction Heads" (Olsson et al.)**
  - https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html
- **"Toy Models of Superposition" (Elhage et al.)**
  - https://transformer-circuits.pub/2022/toy_model/index.html
- **Neel Nanda's "Comprehensive Mechanistic Interpretability Explainer"**
  - https://www.neelnanda.io/mechanistic-interpretability/glossary

## Do

**1. Set up TransformerLens**

```python
pip install transformer-lens
from transformer_lens import HookedTransformer
model = HookedTransformer.from_pretrained("gpt2-small")
```

Run a simple prompt through the model and extract the logits. Verify you get reasonable next-token predictions.

**2. Visualize attention patterns**

For the prompt `"When Mary and John went to the store, John gave a drink to"`:
- Extract attention patterns from all heads in all layers using `model.run_with_cache`
- Plot attention heatmaps for 2-3 interesting heads (use `cv.attention.attention_patterns`)
- Look for: heads that attend to the previous token, heads that attend to specific names, heads that attend to commas/periods

**3. Direct logit attribution**

Decompose the model's prediction into contributions from each component:
- For a given prompt, compute the residual stream contribution of each attention head and MLP layer to the final logit
- Identify which heads contribute most to the correct prediction
- This tells you WHERE in the network the prediction is being made

**4. Activation patching (if time allows)**

On the "indirect object identification" task (`"When Mary and John went to the store, John gave a drink to"` → should predict `"Mary"`):
- Run the clean prompt and a corrupted version (swap names)
- Patch activations from the clean run into the corrupted run, one component at a time
- Identify which heads are critical for the task — these form the "circuit"

**5. ARENA tutorials**

Complete the ARENA Chapter 1 mechanistic interpretability exercises on induction heads:
- https://arena-ch1-transformers.streamlit.app/
- These walk you through finding induction heads, the two-head induction circuit, and verification via ablation

## ML and Alignment Connection

Mechanistic interpretability IS alignment research. The bet: if we can understand *what* models are computing internally -- not just their input-output behavior -- we can detect deceptive alignment, verify safety properties, and build more trustworthy systems. This lesson marks the transition from "learning the prerequisites" to "doing the actual work." The tools you learn here (TransformerLens, activation analysis, attention visualization) are the same tools used by researchers at Anthropic, DeepMind, and elsewhere to study whether frontier models are safe to deploy.
