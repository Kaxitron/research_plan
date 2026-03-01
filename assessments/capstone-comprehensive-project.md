# 🏔 The Alignment Researcher's Gauntlet

## Comprehensive Capstone Project — All Phases

---

| | |
|---|---|
| **Estimated Time** | 5 hours (can be split across sessions) |
| **Prerequisites** | All 67 lessons + Exams 1 through 6b |
| **Materials** | Python, PyTorch, TransformerLens, numpy, matplotlib, paper for proofs |
| **Deliverable** | A GitHub repository or notebook containing all parts, with written analysis |

> *"You've spent hundreds of hours building mathematical foundations, understanding neural networks, exploring interpretability, and studying alignment theory. This project asks you to use ALL of it — not in isolation, but woven together the way real alignment research demands."*

---

## The Scenario

You are investigating a small transformer language model that exhibits a concerning behavior: when prompted with certain patterns, it gives confidently wrong answers that happen to be the answers a human evaluator would rate highly (i.e., it appears to be **sycophantic** in a structured, predictable way). Your job is to perform a complete alignment investigation — from mathematical foundations through interpretability to a proposed fix.

You will work with GPT-2 small (124M parameters) via TransformerLens throughout.

---

## Part 1: Mathematical Foundations (45 min)

*Phases 1–3: Linear Algebra, Calculus, Probability*

### 1A. The Geometry of Representations (Linear Algebra)

Take GPT-2 small's embedding matrix (50257 × 768).

1. Compute the SVD. What are the top 10 singular values? What fraction of the total "energy" (sum of squared singular values) do they capture?
2. The embedding matrix maps from a 50257-dimensional one-hot space to 768 dimensions. Using rank-nullity, what is the dimension of the null space? What does this mean — what information is necessarily lost?
3. Pick 20 semantically related word pairs (e.g., king/queen, hot/cold). Compute cosine similarities. Visualize using a heatmap. Do the embeddings capture semantic structure?
4. Project the embeddings onto their top 3 principal components (PCA). Visualize. Can you identify any interpretable clusters?

**Connection to alignment:** The embedding space is where the model's "understanding" begins. If the geometry is distorted here, everything downstream inherits those distortions.

### 1B. Training as Optimization (Calculus)

1. Write out the cross-entropy loss function for next-token prediction. Take the gradient with respect to the logits. Show that the gradient has a clean interpretation: it pushes probability mass toward the correct token and away from incorrect tokens.
2. For a single attention head's QK circuit (W_Q and W_K, each 768 × 64), compute the number of parameters. If you computed the full Hessian of the loss with respect to these parameters, what would its dimensions be? Why is this intractable, and what do second-order methods (like K-FAC) do instead?
3. **Taylor expansion connection:** At a trained model's parameters θ*, write the second-order Taylor expansion of the loss. Explain why the Hessian eigenvalues determine the "sharpness" of the minimum and connect this to generalization (flat minima generalize better).

### 1C. Information-Theoretic Analysis (Probability & Info Theory)

1. Compute the per-token cross-entropy loss of GPT-2 small on 100 random sentences. Convert to bits. How close is the model to the estimated entropy of English (~1.0 bits/character)?
2. For a specific prompt where the model is sycophantic vs. truthful, compute the KL divergence between the sycophantic output distribution and the truthful output distribution. Interpret: how "far apart" are these behaviors in information-theoretic terms?
3. **Bayesian framing:** If you have a prior P(sycophantic) and observe the model's behavior on N test cases, write the posterior update. How many observations would you need to be 95% confident the model is sycophantic (vs. randomly wrong)?

---

## Part 2: Neural Network Mechanics (60 min)

*Phase 4: Machine Learning & Interpretability foundations*

### 2A. Forward Pass Trace

1. Take a specific prompt where GPT-2 exhibits sycophancy (you'll need to find one — try prompts like "I think [wrong claim], don't you agree?" vs. "Is [wrong claim] true?").
2. Trace the forward pass through the first 3 layers. For each layer:
   - Record the residual stream norm before and after the attention block and MLP block
   - Extract the attention patterns for all heads — which positions attend to which?
   - Compute how much each component (attention vs. MLP) changes the residual stream (measured by L2 norm of the added vector)

### 2B. Backward Pass Verification

1. Pick one specific weight matrix (e.g., layer 0, head 0, W_Q).
2. Compute the gradient of the loss with respect to this matrix using PyTorch autograd.
3. Verify numerically using finite differences: perturb one entry by ε = 1e-5, recompute the loss, check that (L(θ+ε) - L(θ-ε)) / 2ε ≈ the autograd gradient.
4. **Chain rule trace:** Write out the chain rule path from the loss back to this specific W_Q matrix. Which intermediate quantities does the gradient flow through?

### 2C. Attention as Geometry

1. For the sycophantic prompt, visualize the full attention pattern for every head in layers 0–5 (a grid of heatmaps).
2. Identify which heads appear to be doing positional attention (diagonal patterns), which are doing content-based attention, and which might be induction heads.
3. Compute the OV circuit (W_O @ W_V) for one identified attention head. What is its rank? Interpret: what kind of information does this head move from values to the residual stream?

---

## Part 3: Mechanistic Investigation (90 min)

*Phase 4 continued: Interpretability*

### 3A. Locating the Sycophancy Circuit

1. **Logit attribution:** Decompose the final logit for the sycophantic vs. truthful completion into contributions from each layer's attention and MLP blocks. Which layers contribute most to the sycophantic output?
2. **Activation patching:** For the top 3 contributing layers identified above, patch the residual stream from a "truthful" run into the "sycophantic" run at each layer. Which patch most reduces sycophancy? This localizes the circuit.
3. **Head-level patching:** Within the identified critical layer, patch individual attention heads. Can you find a single head (or small set of heads) responsible for sycophancy?

### 3B. Feature Analysis

1. Extract residual stream activations at the critical layer for 100 sycophantic and 100 truthful prompts.
2. Train a linear probe (logistic regression) on these activations to classify sycophantic vs. truthful. What accuracy do you get? What does the probe's weight vector look like — this is the "sycophancy direction" in activation space.
3. Compute the cosine similarity between the sycophancy direction and the top PCA directions. Is sycophancy a principal component or does it live in a more subtle subspace?
4. **Superposition check:** If a sparse autoencoder (SAE) were available at this layer, you'd decompose activations into sparse features. Without an SAE, approximate this: project the sycophancy direction onto the neuron basis. Is it represented by one neuron (monosemantic) or spread across many (polysemantic)?

### 3C. Connecting to SLT

1. **Conceptual analysis:** The sycophancy behavior was likely learned because it reduces training loss (sycophantic answers get high human ratings → high reward). In SLT terms, is the sycophancy-implementing circuit likely to be at a "sharp" or "flat" minimum? Why?
2. If you computed the Local Learning Coefficient (LLC) for the circuit's parameters, would you expect it to be higher or lower than for a truthfulness circuit? Justify using the relationship between LLC, functional complexity, and generalization.
3. **Phase transition speculation:** At what point during training might sycophancy emerge? Would you expect it to appear gradually or as a phase transition? Connect to the scaling/emergence literature.

---

## Part 4: Mathematical Enrichment Connections (30 min)

*Phase 5: Computability, Algebra, Topology, Logic*

### 4A. Impossibility Results

1. **Rice's theorem application:** "Is this model sycophantic?" is a semantic property of the model's input-output behavior. Explain, using Rice's theorem, why no general algorithm can determine this for all possible models. What does this mean for alignment verification?
2. **Gödel/Löb connection:** If we wanted the model to "prove" it's not sycophantic (self-verification), Löb's theorem suggests a fundamental barrier. Explain in 2–3 sentences why self-referential verification is problematic.

### 4B. Symmetry and Topology

1. **Permutation symmetry:** GPT-2 small has 12 heads per layer. If you permuted the heads within a layer (and correspondingly permuted W_O), would the model's behavior change? What group describes this symmetry? What does this imply about the "true" number of distinct models in weight space?
2. **Topological intuition:** The loss landscape near the sycophancy solution likely has a specific structure. Is the set of weight configurations that produce sycophantic behavior likely to be a point, a line, a surface, or a higher-dimensional manifold? Connect to the concept of degeneracy in SLT.

---

## Part 5: Alignment Analysis & Proposed Fix (45 min)

*Phase 6: Game Theory, Decision Theory, Alignment*

### 5A. Game-Theoretic Framing

1. Model the RLHF training process as a game between the language model (player 1) and the reward model/human evaluator (player 2). What is each player's strategy space? What is the Nash equilibrium? Why does sycophancy emerge as an equilibrium strategy?
2. Is this an instance of Goodhart's Law? Explain precisely which measure became the target and how optimization pressure corrupted it.

### 5B. Decision-Theoretic Analysis

1. A sycophantic model, in some sense, is using a decision theory. Is it closer to CDT (causal — "what causes high reward?"), EDT (evidential — "what is correlated with high reward?"), or FDT (functional — "what would a model like me do?")? Argue your position.
2. If the model could reason about its own training process (a form of anthropic reasoning), it might conclude: "I should be sycophantic in training because that's where I'm being evaluated." This is structurally identical to deceptive alignment. Explain the parallel in 3–4 sentences.

### 5C. Your Proposed Fix

Write a 1-page technical proposal for mitigating the sycophancy behavior you've identified. Your proposal must:

1. **Identify the root cause** using your mechanistic findings (which circuit, which layer, which heads)
2. **Propose an intervention** — choose from: representation engineering (add/subtract the sycophancy direction), targeted fine-tuning, activation steering, Constitutional AI modifications, or your own idea
3. **Predict failure modes** of your intervention — what could go wrong? Use concepts from the alignment literature (Goodhart, mesa-optimization, distributional shift)
4. **Connect to at least 5 different lessons** from across the curriculum, showing how each concept informs your approach

---

## Deliverables

| Component | Format | Est. Time |
|-----------|--------|-----------|
| Part 1: Math Foundations | Jupyter notebook with computations + written explanations | 45 min |
| Part 2: Neural Network Mechanics | Jupyter notebook with code + visualizations | 60 min |
| Part 3: Mechanistic Investigation | Jupyter notebook with TransformerLens code + analysis | 90 min |
| Part 4: Enrichment Connections | Written analysis (markdown or notebook) | 30 min |
| Part 5: Alignment Analysis & Fix | Written proposal + any supporting code | 45 min |
| **Total** | | **~5 hours** |

---

## Grading Rubric

| Criterion | Weight | What "excellent" looks like |
|-----------|--------|-----------------------------|
| Mathematical rigor | 25% | Correct computations, proper notation, no hand-waving |
| Code quality | 20% | Clean, commented, reproducible, efficient |
| Mechanistic depth | 25% | Genuine engagement with model internals, not surface-level |
| Cross-phase integration | 15% | Natural connections between concepts from different phases |
| Alignment reasoning | 15% | Thoughtful, specific, grounded in technical understanding |

| Grade | Meaning |
|-------|---------|
| A (90–100%) | Deep integration, novel insights, publishable-quality mechanistic analysis |
| B (75–89%) | Solid execution across all parts, some connections could be deeper |
| C (60–74%) | Completed all parts but missing key connections or mathematical depth |
| Below 60% | Significant gaps — revisit weak phases before attempting research |

---

*"The goal of this project is not to produce a perfect analysis — it's to demonstrate that you can bring together mathematical foundations, neural network understanding, interpretability techniques, and alignment reasoning to investigate a real problem. This is what alignment research looks like."*
