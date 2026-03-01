# Exam 4B: Mechanistic Interpretability

**The Path to AI Alignment — Lessons 47–50 Comprehensive Assessment**

---

| | |
|---|---|
| **Time Allowed** | 60 minutes |
| **Total Points** | 100 |
| **Materials** | Pencil, paper. No calculator needed. |
| **Format** | 10 questions: more conceptual and research-oriented than previous exams |

> **Advice:** This exam values clear reasoning and connections between ideas over computation. The thread: **can you explain what interpretability reveals, why it matters for alignment, and how SLT provides the mathematical foundation?**

---

## Question 1 (10 pts) — The Interpretability Landscape

**(a)** State the central question of mechanistic interpretability in one sentence.

**(b)** Describe three distinct interpretability techniques (e.g., probing, activation patching, SAEs). For each, state what it reveals and one limitation.

**(c)** Why is interpretability crucial for alignment? Give a concrete scenario where interpretability could detect a safety-relevant property that behavioral testing alone would miss.

---

## Question 2 (10 pts) — Superposition as Geometry

**(a)** The superposition hypothesis states that neural networks represent more features than they have dimensions. Explain how this is possible using a geometric analogy. *(Hint: think about near-orthogonal vectors in high dimensions.)*

**(b)** In d dimensions, approximately how many nearly-orthogonal vectors can you fit? (Give the approximate scaling, not an exact formula.) Why does this matter for understanding why networks are so hard to interpret?

**(c)** If a neuron responds to both "cat" and "car" features because those features are superimposed, what does this mean for interpreting individual neurons? Why are features a better unit of analysis than neurons?

---

## Question 3 (10 pts) — Sparse Autoencoders

**(a)** A Sparse Autoencoder (SAE) is trained to decompose a model's activations into interpretable features. Describe the architecture: what is the encoder, the decoder, and the sparsity penalty?

**(b)** The SAE objective is: minimize ‖x − Decode(Encode(x))‖² + λ·‖Encode(x)‖₁. Interpret each term.

**(c)** Connect to Phase 3: the L1 penalty corresponds to what Bayesian prior? Why does this prior encourage sparsity?

**(d)** An SAE trained on a language model produces a feature dictionary with entries like "feature 4817: activates on Python code," "feature 2103: activates on first-person emotional expressions." Why is this useful for alignment research?

---

## Question 4 (10 pts) — Circuits: Induction Heads

**(a)** Describe the induction head circuit: what pattern does it detect, and how does it work (in terms of attention operations)?

**(b)** The induction head requires two attention heads working in sequence. Describe what each head does (the "previous token head" and the "induction head").

**(c)** Why was the discovery of induction heads significant for mechanistic interpretability? What does it demonstrate about how transformers implement algorithms?

**(d)** The indirect object identification (IOI) circuit in GPT-2 is a more complex circuit. In 2–3 sentences, describe what task it solves and why finding it was a milestone.

---

## Question 5 (10 pts) — Scaling Laws and Emergence

**(a)** State the neural scaling law: how does loss L relate to compute C, dataset size D, and parameter count N? What is remarkable about these power-law relationships?

**(b)** Define emergent capabilities. Give two examples of capabilities that appear suddenly at a specific model scale.

**(c)** Why is emergence a problem for alignment? Connect to the concept of "predictability" — if we can't predict when dangerous capabilities will appear, what does this mean for safety testing?

**(d)** Some researchers argue that emergence is an artifact of metrics (the "mirage" hypothesis). Explain this argument in 2–3 sentences.

---

## Question 6 (12 pts) — Singular Learning Theory: Core Ideas

**(a)** Classical statistics assumes models are "regular." Define what "regular" means in terms of the Fisher information matrix and the local shape of the loss landscape.

**(b)** Why are neural networks NOT regular? Give two specific reasons related to the parameter-to-function mapping.

**(c)** At a singularity, the Hessian has zero eigenvalues. From Phase 1 and 2, explain what zero Hessian eigenvalues mean geometrically for the loss landscape.

**(d)** The RLCT (Real Log Canonical Threshold) λ replaces d/2 as the measure of model complexity. State the free energy formula and explain why λ ≤ d/2 explains generalization of overparameterized networks.

**(e)** For a 1-hidden-unit ReLU network learning the zero function y = 0, the RLCT is λ = 1/4 (with 3 parameters). Compare with the "regular" value d/2 = 3/2. What does this 6× reduction in effective complexity mean?

---

## Question 7 (10 pts) — Phase Transitions and the LLC

**(a)** What is a phase transition in the context of neural network training? Give an example (grokking, sudden capability gain, etc.).

**(b)** The Local Learning Coefficient (LLC) is an estimable version of the RLCT that can be tracked during training. What does a sudden drop in the LLC indicate?

**(c)** Developmental interpretability studies how model internals change during training, especially at phase transitions. Describe what a researcher would look for when examining a model before and after a grokking event.

**(d)** Connect phase transitions to bifurcation theory (Lesson 25): in what sense is a sudden capability gain a bifurcation in the training dynamics?

---

## Question 8 (10 pts) — The Geometry of Singularities

**(a)** Consider f(w₁, w₂) = (w₁w₂)². Plot or describe this surface. Where is the singularity? What shape does the zero set f = 0 have?

**(b)** Compute the Hessian of f at the origin. What does the result tell you about the local shape?

**(c)** Why can't the Hessian capture the true geometry at a singularity? What additional mathematical tool (from algebraic geometry) is needed?

**(d)** In one sentence, describe what a "blow-up" does to a singularity and why it's useful for computing the RLCT.

---

## Question 9 (8 pts) — SLT for Alignment

**(a)** If we could compute the RLCT for different model behaviors (aligned vs. misaligned), what would we want to find? Which behavior should have lower RLCT, and why?

**(b)** A deceptively aligned model implements a more complex internal strategy than a genuinely aligned model (it must model the training process AND decide when to defect). How would this difference in functional complexity theoretically manifest in SLT quantities?

**(c)** What are the current practical limitations of using SLT for alignment research? Name at least two.

---

## Question 10 (10 pts) — Synthesis

**(a)** Trace the mathematical thread from Phase 1 to SLT: eigenvalues → Hessian → loss landscape → singularities → RLCT. For each arrow, write one sentence explaining the connection.

**(b)** A research colleague shows you a plot of the Local Learning Coefficient during training. You see: a flat period around λ ≈ 2.0 for the first 5000 steps, then a sharp drop to λ ≈ 0.8 at step 5000, followed by another flat period. Interpret this plot: what happened at step 5000? What can you infer about the model's internal structure before and after?

**(c)** In your own words, write a 3–4 sentence summary of why SLT is considered one of the most promising mathematical frameworks for alignment.
