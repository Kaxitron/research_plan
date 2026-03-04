# Exam 4B: Mechanistic Interpretability

**The Path to AI Alignment -- Lessons 61, 65–66 Comprehensive Assessment**

---

| | |
|---|---|
| **Part I** | 10 short questions -- 30 minutes |
| **Part II** | Interpretability project -- 3-4 hours |
| **Materials** | Part I: pencil and paper. Part II: Python, TransformerLens, PyTorch |
| **Format** | Conceptual fluency (Part I) + hands-on research (Part II) |

> **Advice:** Part I tests whether you have internalized the core ideas well enough to explain them quickly and reason about counterfactuals. Part II tests whether you can do interpretability research. The thread: **can you explain what mechanistic interpretability reveals, why singular learning theory provides its mathematical foundation, and then actually investigate a model's internals?**

---

# Part I: Core Concepts (30 minutes)

Answer each question in 2-4 sentences unless otherwise specified. These are meant to be quick -- test your intuition, not your ability to write essays.

---

## Question 1 -- Mechanistic vs. Behavioral

What is mechanistic interpretability, and how does it differ from behavioral testing (i.e., just running inputs and checking outputs)? Give one concrete example where behavioral testing would miss something that mechanistic interpretability could catch.

---

## Question 2 -- Activation Patching

You run activation patching on a language model: you replace the activation at a specific layer and position with the activation from a different input, then observe how the output changes. What does a large change in output tell you about that activation? What does no change tell you?

---

## Question 3 -- Superposition

A transformer's residual stream has 512 dimensions, yet the model appears to represent thousands of distinct features. Explain how this is possible. Why does superposition make individual neurons hard to interpret?

---

## Question 4 -- Sparse Autoencoders

A Sparse Autoencoder (SAE) is trained to decompose model activations into interpretable features using the objective: minimize ||x - Decode(Encode(x))||^2 + lambda * ||Encode(x)||_1. In one sentence each: what does the reconstruction term do, what does the sparsity term do, and why does the combination help us find monosemantic features?

---

## Question 5 -- Induction Heads

Describe the induction head circuit in 2-3 sentences: what pattern does it detect, and how do the two heads (the previous-token head and the induction head) work together? Why was this discovery significant for the claim that transformers learn interpretable algorithms?

---

## Question 6 -- QK vs. OV Circuits

In a transformer attention head, the QK circuit and the OV circuit serve different roles. What does each one compute? (One sentence each is sufficient.)

---

## Question 7 -- Why Standard Statistics Fails

BIC approximates model complexity using k/2, where k is the parameter count. Why does this fail for neural networks? Name two specific properties of neural networks that violate the "regularity" assumption BIC requires.

---

## Question 8 -- The RLCT

The Real Log Canonical Threshold (lambda) replaces d/2 as the measure of model complexity in Singular Learning Theory. What does lambda measure intuitively? Why is the fact that lambda <= d/2 important for explaining why overparameterized networks generalize?

---

## Question 9 -- Phase Transitions

During training, a model's loss sometimes drops sharply after a long plateau (as in grokking). What is happening internally at such a phase transition, according to SLT? What would you expect to see in a plot of the Local Learning Coefficient at the moment of the transition?

---

## Question 10 -- Local Learning Coefficient

A researcher tracks the Local Learning Coefficient (LLC) during training and observes it sitting at approximately 2.0 for 5000 steps, then dropping sharply to approximately 0.8. What does the LLC track, and what can you infer happened at the transition? Why is a lower LLC value associated with better generalization?

---

# Part II: Mechanistic Interpretability Investigation (3-4 hours)

## Project: Investigating Induction Heads in GPT-2 Small

Use TransformerLens to investigate how GPT-2 small implements in-context learning through induction heads. This project has three phases: replicate a known finding, extend it with your own analysis, and write up results.

### Setup

```bash
pip install transformer-lens torch numpy matplotlib plotly
```

```python
import transformer_lens
from transformer_lens import HookedTransformer
import torch
import numpy as np

model = HookedTransformer.from_pretrained("gpt2-small")
```

### Phase 1: Replicate (60-90 minutes)

**Goal:** Confirm that GPT-2 small contains induction heads and identify which heads they are.

1. **Construct an induction-style prompt.** Create a sequence with a repeated pattern, e.g., a sequence of random tokens where a subsequence appears twice: `[A B C D ... A B C D ...]`. The model should predict the token after `A B C` on the second occurrence by copying what followed `A B C` on the first occurrence.

2. **Run the model and cache all activations.** Use `model.run_with_cache()` to capture attention patterns at every layer and head.

3. **Identify induction heads.** For each attention head, compute an "induction score": on the repeated subsequence, how strongly does the head at position `i` attend to position `j` where token `j+1` matches what should come next? Heads with high induction scores are induction heads.

4. **Visualize the attention patterns** of the top 2-3 induction heads. The attention pattern should show a clear diagonal stripe offset by the length of the repeated subsequence.

**Deliverable:** A ranked list of heads by induction score, with attention pattern visualizations for the top candidates. Identify which (layer, head) pairs are induction heads.

### Phase 2: Extend (60-90 minutes)

Choose ONE of the following extensions:

**Option A -- Activation Patching.** Use activation patching to confirm that the induction heads you identified are causally important for in-context copying. Patch the output of each head (replace it with the output from a corrupted input that breaks the repeated pattern) and measure the change in the model's ability to predict the next token in the repeated sequence. Rank all heads by their causal effect. Compare this causal ranking to your induction score ranking from Phase 1.

**Option B -- Previous-Token Heads.** Induction heads need a "previous-token head" in an earlier layer to compose with. Identify which earlier-layer heads attend primarily to the previous token position. Then demonstrate the composition: show that the previous-token head's output is used by the induction head's QK circuit to look up the right source position. Visualize the two-step circuit.

**Option C -- Varying the Pattern.** Test the robustness of induction heads by varying the task:
- Does the induction behavior work with natural language (repeated phrases in English text) or only with random token sequences?
- What happens with longer gaps between the first and second occurrence of the pattern?
- At what sequence length does induction head performance degrade?

Plot your findings and interpret what they reveal about the generality of the induction mechanism.

**Deliverable:** Results from your chosen extension with supporting visualizations and a 1-2 paragraph interpretation.

### Phase 3: Write-Up (30-60 minutes)

Write a short report (1-2 pages) covering:

1. **Question:** What did you investigate and why does it matter for interpretability?
2. **Method:** What tools did you use, and how did you set up the experiment?
3. **Replication results:** Which heads are induction heads in GPT-2 small? Include your key visualization.
4. **Extension results:** What did your extension reveal? Include your key finding and what it adds beyond the replication.
5. **Reflection:** What surprised you? What would you investigate next with more time? How does this connect to the broader goal of understanding whether models are safe?

**Deliverable:** A written report with embedded figures, submitted as a PDF or Jupyter notebook.

### Grading Criteria

| Component | Weight | What we look for |
|---|---|---|
| Replication correctness | 30% | Correctly identified induction heads, clean visualizations |
| Extension depth | 30% | Genuine investigation beyond replication, not just re-running code |
| Write-up clarity | 20% | Clear writing, results properly interpreted, figures labeled |
| Code quality | 10% | Readable, commented, reproducible |
| Connection to alignment | 10% | Demonstrates understanding of why this work matters |

### Alternative Project (if TransformerLens setup is not feasible)

**Train a small transformer on a synthetic task and analyze it.**

1. Train a 2-layer transformer on a simple algorithmic task (modular addition, sequence copying, or parenthesis matching) using PyTorch.
2. After training, extract and visualize all attention patterns.
3. Use activation patching to identify which components are causally responsible for the task.
4. Write up: what circuit did the model learn? Does it match what you would expect from a hand-designed solution?

Same deliverables and grading criteria apply.
