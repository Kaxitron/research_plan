# Final Project: The Alignment Observatory

**A Comprehensive Integration Across All Phases — Build, Train, Interpret, and Align a Language Model**

---

| | |
|---|---|
| **Estimated Time** | 5 hours (can be split across sessions) |
| **Prerequisites** | All lessons (0–67) and all exams completed |
| **Materials** | Python, PyTorch, NumPy, Matplotlib. GPU recommended but not required. |
| **Deliverable** | A GitHub repository with code, visualizations, and a written report |

> *"The goal was never to learn linear algebra, calculus, probability, or neural networks in isolation. It was to build the unified mathematical language needed to work on the most important problem in human history."*
>
> This project is the proof that you built it.

---

## Overview

You will build a small transformer language model from scratch, train it, analyze its training dynamics, interpret its internals, attempt to align it, and write a rigorous analysis connecting each step to the mathematics you've learned. Every phase of the curriculum will be used.

The project has 7 stages. Each stage tells you what to build AND which lessons it draws from.

---

## Stage 1: Architecture (45 min)
**Phases used: 1 (Linear Algebra), 4 (Neural Networks)**

Build a small transformer from scratch in PyTorch. No `nn.TransformerEncoder` — implement every component by hand.

### Requirements
- **Token embedding layer** — a learned matrix E ∈ ℝ^{vocab × d_model}. (Lesson 2: vectors, Lesson 11: change of basis)
- **Positional encoding** — sinusoidal. Implement the formula and visualize the encoding matrix as a heatmap. (Lesson 21: Taylor/Fourier connection)
- **Single-head attention** — implement Q, K, V projections and scaled dot-product attention. (Lesson 10: dot products, Lesson 43: attention)
- **Multi-head attention** — split into h heads, concatenate, project. (Lesson 4: linear transformations, Lesson 11: change of basis)
- **Feed-forward network** — two linear layers with ReLU. (Lesson 40: single neuron, Lesson 41: forward pass)
- **Layer norm** — implement manually. (Lesson 11: norms)
- **Full transformer block** — attention → add & norm → FFN → add & norm. Stack 2–4 blocks.

### Deliverable
- Complete model code with every matrix dimension annotated in comments
- A diagram (hand-drawn or code-generated) showing the full architecture with tensor shapes at every stage
- Parameter count breakdown: how many parameters in each component?

### Analysis Questions
1. Compute the rank of your embedding matrix at initialization (before training). What do you expect it to be? (Lesson 6)
2. What is the computational complexity of attention as a function of sequence length n and dimension d? Where does the bottleneck come from? (Lesson 52: computational complexity)

---

## Stage 2: Training (45 min)
**Phases used: 2 (Calculus), 3 (Probability), 4 (Neural Networks)**

Train your transformer on a dataset that has learnable structure.

### Dataset Options (pick one)
- **Shakespeare character-level** — predict the next character
- **Simple arithmetic** — sequences like "12+34=46" (enables studying grokking)
- **Tiny Stories** — a small subset of synthetic stories

### Requirements
- **Loss function:** cross-entropy (derive it from MLE — Lesson 30). Show that minimizing cross-entropy = maximizing log-likelihood = minimizing KL divergence from the data distribution. (Lesson 31: information theory)
- **Optimizer:** implement SGD with momentum from scratch first. Then switch to Adam. (Lesson 17: optimization, Lesson 19: loss landscapes)
- **Learning rate schedule:** implement cosine annealing. Plot the schedule.
- **Training loop:** track loss, gradient norms, and parameter norms per layer at every step

### Deliverable
- Training loss curve (log scale) over all steps
- Gradient norm plot per layer — look for vanishing/exploding gradients (Lesson 42: backprop)
- Parameter norm plot per layer — is anything growing unbounded?

### Analysis Questions
1. Compute the Jacobian of the loss with respect to the attention weights for a single input. What are its dimensions? (Lesson 14: matrix calculus, Lesson 16: chain rule)
2. At the end of training, estimate the Hessian's top eigenvalue using the power method. What does this tell you about the local curvature? (Lesson 8: eigenvalues, Lesson 19: loss landscapes)
3. If you chose the arithmetic dataset: does grokking occur? At what step? (Lesson 25: stability, Lesson 50: SLT phase transitions)

---

## Stage 3: Training Dynamics as a Dynamical System (30 min)
**Phases used: 2 (Calculus — ODEs), 5 (Topology)**

Analyze the training process through the lens of dynamical systems theory.

### Requirements
- **Gradient flow view:** write the continuous-time ODE that your training approximates: dw/dt = −∇L(w). (Lesson 24: gradient flow)
- **Phase portrait:** pick 2 parameters (e.g., two weights in the attention layer). Plot their trajectory through training as a 2D path overlaid on a contour plot of the loss (estimated by evaluating the loss on a grid around the trajectory). (Lesson 22: intro ODEs)
- **Lyapunov analysis:** verify that the training loss is a Lyapunov function — it should decrease monotonically (approximately) along the trajectory. (Lesson 25: stability)
- **Learning rate as discretization:** compare the training dynamics with learning rate η vs. η/2. Show that smaller η more closely approximates the continuous ODE. (Lesson 22: Euler's method)

### Deliverable
- 2D phase portrait with training trajectory and loss contours
- Loss-as-Lyapunov-function plot
- Learning rate comparison showing convergence to the continuous limit

### Analysis Questions
1. At convergence, the system reaches a fixed point of the ODE. What are the eigenvalues of the Jacobian at this point? (Lesson 23: linear systems, Lesson 25: stability)
2. If you observe oscillation near convergence, what does this tell you about the Hessian eigenvalues? (Lesson 25: stability)

---

## Stage 4: Mechanistic Interpretability (60 min)
**Phases used: 1 (Linear Algebra), 4 (Interpretability)**

Open the black box and find out what your model learned.

### Requirements
- **Embedding analysis:** compute the SVD of the learned embedding matrix. Plot the singular values. How many dimensions does the model actually use? (Lesson 9: SVD, Lesson 6: rank)
- **Attention pattern visualization:** for 10 representative inputs, plot the attention weights as heatmaps. Can you identify any interpretable patterns? (Lesson 43: attention, Lesson 47: interp intro)
- **Activation patching:** for a specific prediction the model gets right, patch activations from a different input at each layer. Find which layer is most critical for this prediction. (Lesson 48: interp circuits)
- **Probing:** train a logistic regression (Lesson 34: regression) on the residual stream activations to predict a simple feature (e.g., "is the next token a vowel?" or "is the arithmetic result > 50?"). At which layer does the probe achieve highest accuracy?
- **Direction analysis:** using the probe weights as a "feature direction," project all token embeddings onto this direction. Visualize: do tokens cluster by the feature? (Lesson 10: dot products, Lesson 11: change of basis)

### Deliverable
- SVD spectrum of embedding matrix with interpretation
- Attention heatmaps for 10 inputs with annotations
- Activation patching results: bar chart of effect size by layer
- Probing accuracy by layer
- 2D visualization of embeddings colored by the probed feature

### Analysis Questions
1. The embedding space has d_model dimensions but the SVD reveals an effective rank of r < d_model. What does this mean in terms of superposition? (Lesson 49: interp scaling)
2. If you find an attention head that implements a simple pattern (e.g., "attend to the previous token"), express this as a matrix equation: what must W_Q and W_K satisfy? (Lesson 5: matrix operations)

---

## Stage 5: Alignment Attempt (60 min)
**Phases used: 3 (Probability/Statistics), 4 (Neural Networks), 6 (Alignment)**

Attempt to steer the model's behavior toward a specified goal.

### Requirements
- **Define an alignment criterion:** choose a measurable property. Examples: "the model should never output [specific token]," "arithmetic answers should be correct," or "generated text should not contain [pattern]."
- **Reward model:** train a simple reward model (logistic regression or small MLP) that scores outputs on your criterion. (Lesson 34: regression, Lesson 40: single neuron)
- **DPO or simple RLHF:** implement a simplified version of Direct Preference Optimization.
  - Generate pairs of outputs for each prompt
  - Label which output is "preferred" according to your criterion
  - Fine-tune the model using the DPO loss: L_DPO = −log σ(β(log π_θ(y_w|x) − log π_ref(y_w|x) − log π_θ(y_l|x) + log π_ref(y_l|x)))
  - (Lesson 46: LLM pipeline, Lesson 66: alignment problem)
- **Evaluate:** measure the alignment criterion before and after DPO. Compute a confidence interval on the improvement. (Lesson 32: hypothesis testing)
- **Failure analysis:** find cases where the aligned model still fails. Categorize the failure modes.

### Deliverable
- Reward model accuracy on held-out data
- Before/after comparison on the alignment metric with confidence intervals
- 5 examples of successful alignment, 5 examples of failure
- Written analysis: why does the model still fail in some cases?

### Analysis Questions
1. The DPO loss contains a KL divergence penalty (via the reference model). What happens if you remove it (set β → ∞)? Why is the constraint necessary? (Lesson 18: constrained optimization, Lesson 31: information theory)
2. Your reward model has finite accuracy. Using concepts from Lesson 33 (experimental design) and Lesson 32 (hypothesis testing), how confident are you that the observed improvement is real and not a reward model artifact?
3. Could your model have learned to game the reward model rather than genuinely satisfy the criterion? Describe what this would look like and how you'd detect it. (Lesson 66: alignment problem — Goodhart's Law)

---

## Stage 6: Mathematical Analysis (45 min)
**Phases used: 5 (Abstract Algebra, Topology, Logic), 4 (SLT)**

Apply the deeper mathematical frameworks to understand your model.

### Requirements
- **Symmetry analysis:** your model has permutation symmetry in the hidden neurons. Compute the size of the symmetry group for your architecture. Show that permuted weight configurations produce identical outputs. (Lesson 54: groups, Lesson 56: group actions)
- **SLT estimation (if feasible):** estimate the local learning coefficient (LLC) using the trace of the Hessian or a sampling-based method. How does the LLC compare to the naive parameter count? (Lesson 50: SLT)
- **Topological analysis:** compute the persistent homology of the learned representations (activation vectors for a batch of inputs). Compare the topology before and after alignment training (Stage 5). Did alignment change the shape of the representation space? (Lesson 57: point-set topology, Lesson 58: homotopy)
- **Logical limits reflection:** your alignment attempt in Stage 5 tried to verify a behavioral property. Using Rice's theorem (Lesson 51), explain why perfect verification is impossible. Using Löb's theorem (Lesson 62), explain why the model cannot self-certify its own alignment.

### Deliverable
- Symmetry group computation with numerical verification
- LLC estimate (or explanation of why estimation is difficult for your architecture)
- Persistence diagrams before/after alignment
- Written reflection on logical limits (1 page)

---

## Stage 7: The Report (45 min)
**All phases**

Write a research-style report that connects everything.

### Structure
1. **Abstract** (100 words): what you built, what you found
2. **Architecture** (half page): describe your model with the linear algebra and transformation language from Phase 1
3. **Training** (half page): describe training as optimization (Phase 2) and maximum likelihood (Phase 3)
4. **Dynamics** (half page): what the dynamical systems analysis revealed (Phase 2 ODEs)
5. **Interpretability** (1 page): what you found inside the model (Phase 4)
6. **Alignment** (1 page): what worked, what didn't, and why (Phase 6)
7. **Mathematical Foundations** (half page): symmetry, SLT, topology, logical limits (Phase 5)
8. **Reflection** (half page): what this project taught you about the alignment problem that you couldn't have understood before this curriculum

### Grading Rubric

| Criterion | Points |
|-----------|--------|
| Working code that trains a transformer from scratch | 20 |
| Correct training pipeline with proper loss and optimizer | 15 |
| Dynamical systems analysis with visualizations | 10 |
| Interpretability analysis (SVD, attention, patching, probing) | 20 |
| Alignment attempt with quantitative evaluation | 15 |
| Mathematical analysis (symmetry, SLT, topology, logic) | 10 |
| Written report connecting to curriculum concepts | 10 |
| **Total** | **100** |

---

## Phase-by-Lesson Coverage Map

Every lesson in the curriculum appears at least once in this project:

| Phase | Lessons | Where They Appear |
|-------|---------|-------------------|
| **Phase 0** | 0–1 | Python/PyTorch used throughout |
| **Phase 1** | 2–12 | Stage 1 (architecture), Stage 4 (interpretability) |
| **Phase 2** | 13–21 | Stage 2 (training), Stage 3 (dynamics) |
| **Phase 2** | 22–27 | Stage 3 (dynamical systems analysis) |
| **Phase 3** | 28–34 | Stage 2 (loss function), Stage 5 (evaluation) |
| **Phase 3** | 35–39 | Stage 5 (Bayesian reward modeling, statistical evaluation) |
| **Phase 4** | 40–46 | Stages 1–2 (build and train the model) |
| **Phase 4** | 47–50 | Stage 4 (interpretability), Stage 6 (SLT) |
| **Phase 5** | 51–56 | Stage 6 (symmetry, computability limits) |
| **Phase 5** | 57–62 | Stage 6 (topology, logical limits) |
| **Phase 6** | 63–67 | Stage 5 (alignment), Stage 6 (reflection) |

---

*This is the culmination of your mathematical journey toward alignment research. The skills you demonstrate here — building, analyzing, interpreting, aligning, and reasoning about the limits of each approach — are the exact skills the field needs.*

*Welcome to the frontier.*
