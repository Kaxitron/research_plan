# Exam 4B: Mechanistic Interpretability — Answer Key

**The Path to AI Alignment — Lessons 47–50 Comprehensive Assessment**

---

> **Grading philosophy:** This exam values clear reasoning and deep connections over formulas. Partial credit for thoughtful but incomplete answers. Award full credit for explanations that demonstrate genuine understanding even if wording differs from below.

---

### Question 1 (10 pts) — The Interpretability Landscape

**(a)** Can we reverse-engineer neural networks into human-understandable programs — identifying the algorithms, features, and circuits they use to produce their outputs?

**(b)** Three techniques (many valid choices):

| Technique | What it reveals | Limitation |
|---|---|---|
| **Probing** (training a small classifier on internal activations) | Whether a specific concept is linearly represented in activations | Doesn't prove the model *uses* that information — it might be an artifact of representation |
| **Activation patching** (swapping activations between inputs) | Which components are causally responsible for a specific behavior | Only tests interventions you think to try; might miss distributed computation |
| **Sparse Autoencoders** (decomposing activations into sparse features) | Individual interpretable features the model has learned | Reconstruction isn't perfect; features may be artifacts of the SAE, not the model |

**(c)** Behavioral testing only reveals how a model responds to inputs you think to test. A deceptively aligned model could pass all behavioral tests while harboring unsafe internal strategies. Interpretability could detect, for example, that a model has learned an internal representation of "am I being tested?" — a feature that activates differently during evaluation vs. deployment. No behavioral test would reveal this, but examining internal activations with SAEs or probing could.

---

### Question 2 (10 pts) — Superposition as Geometry

**(a)** In high-dimensional space, you can pack exponentially many vectors that are *nearly* orthogonal (small but nonzero dot products). Imagine fitting many "almost perpendicular" directions in a room — in 2D you only get 2 orthogonal directions, but in 1000D you can fit millions of nearly-orthogonal vectors. The network exploits this: each feature corresponds to a direction, and features interfere only slightly because their dot products are small. The network trades exact orthogonality for massive capacity.

**(b)** Approximately **exponential in d** — roughly e^{cd} for some constant c, or more conservatively O(d²) nearly-orthogonal vectors with inner products below some threshold. This matters because it means a layer with d neurons can represent vastly more than d features. This is why individual neurons don't correspond to individual concepts — each neuron participates in representing many superimposed features, making naive neuron-level interpretation misleading.

**(c)** The neuron is a **polysemantic** — it responds to multiple unrelated concepts because those concepts' feature directions both have significant components along that neuron's axis. Interpreting the neuron as "the cat neuron" would be wrong; it's entangled. **Features** (directions in activation space, not individual neurons) are the correct unit because each feature direction corresponds to one concept, even if that direction doesn't align with any single neuron axis.

---

### Question 3 (10 pts) — Sparse Autoencoders

**(a)** **Encoder:** maps the model's d-dimensional activation vector x to a higher-dimensional (overcomplete) representation h = ReLU(W_enc · x + b_enc), where dim(h) >> d. **Decoder:** maps back: x̂ = W_dec · h + b_dec. **Sparsity penalty:** L1 norm on h, encouraging most entries of h to be zero — only a few features activate for any given input.

**(b)** ‖x − Decode(Encode(x))‖²: **reconstruction loss** — the SAE must faithfully reconstruct the original activation (it hasn't thrown away important information). λ·‖Encode(x)‖₁: **sparsity penalty** — each input should activate only a few features. The balance λ trades off fidelity vs. interpretability.

**(c)** The L1 penalty corresponds to a **Laplace prior** (double exponential) on the feature activations. The Laplace distribution is peaked sharply at zero with heavy tails, so it strongly favors coefficients that are exactly zero while allowing occasional large values. This is the same mechanism as **Lasso regression** (Phase 3) — L1 regularization drives coefficients to exactly zero, producing sparse solutions. The Gaussian (L2) prior only shrinks coefficients toward zero without reaching it.

**(d)** It provides a **dictionary of what the model has learned** in human-interpretable terms. For alignment: you could search for features related to deception ("feature 9821: activates when the model's output contradicts its internal representation"), sycophancy ("feature 1204: activates when matching user's stated opinion"), or dangerous knowledge ("feature 5567: activates on bioweapon synthesis text"). This turns the black box into a searchable, auditable catalog.

---

### Question 4 (10 pts) — Circuits: Induction Heads

**(a)** Induction heads detect and continue repeated patterns. Given a sequence like [A][B]...[A], the induction head predicts [B] will follow the second [A]. It implements the algorithm: "find a previous occurrence of the current token, look at what came after it, and predict that." This is the simplest form of in-context learning.

**(b)** Step 1 — **Previous token head** (in an earlier layer): attends from each position to the position immediately before it. Its output encodes "what token came before me." Step 2 — **Induction head** (in a later layer): uses the previous token head's output to find positions where the current token appeared earlier (by matching the "what came before" information), then copies the token that followed. The two heads compose: head 1 creates the lookup key, head 2 uses it.

**(c)** It demonstrated that transformers implement **identifiable algorithms** through specific multi-component circuits — not just statistical patterns but structured computation. It showed that interpretability can go beyond "which neurons fire" to "what algorithm is being run." This was proof-of-concept that the mechanistic interpretability research agenda is feasible: real, non-trivial algorithms can be found and described.

**(d)** IOI solves: given "When Mary and John went to the store, John gave a drink to ___", predict "Mary" (the indirect object). The circuit involves ~26 attention heads across multiple layers implementing name detection, name movement, and inhibition of the repeated name. It was a milestone because it showed a complex, multi-step reasoning task could be decomposed into a complete, verified circuit in a real language model (GPT-2 Small), not just a toy model.

---

### Question 5 (10 pts) — Scaling Laws and Emergence

**(a)** L ∝ C^{−α_C}, L ∝ D^{−α_D}, L ∝ N^{−α_N} — loss decreases as a power law with compute, data, and parameters. What's remarkable: these are **smooth, predictable power laws** over many orders of magnitude. You can predict performance of a 10× larger model from smaller runs. The exponents are roughly universal across architectures and domains.

**(b)** Emergent capabilities are abilities that are absent in smaller models and suddenly appear at a specific scale. Examples: (1) **Few-shot arithmetic** — models below ~10B parameters can't do multi-digit addition; above that threshold, they suddenly can. (2) **Theory of mind** — models below a certain scale fail at reasoning about others' beliefs; above it, they pass false-belief tests.

**(c)** If dangerous capabilities emerge unpredictably, you can't rely on testing smaller models to guarantee safety of larger ones. A model that shows no signs of deceptive reasoning at 10B parameters might suddenly develop it at 100B. This means "evaluate and deploy" is insufficient — you need either (1) theoretical understanding of WHEN capabilities emerge (SLT/bifurcation theory), or (2) interpretability tools that detect the precursors of dangerous capabilities before they fully form.

**(d)** The "mirage" argument: emergence may be an artifact of using **sharp, threshold-based metrics** (like exact-match accuracy). When you measure with smoother metrics (like log-probability of the correct answer), performance improves gradually — there's no sudden jump. Emergence might be the metric suddenly crossing a threshold, not the capability suddenly appearing. Under this view, the underlying computation develops gradually; only our measurement of it looks discontinuous.

---

### Question 6 (12 pts) — Singular Learning Theory: Core Ideas

**(a)** "Regular" means: (1) the Fisher information matrix I(θ) is **positive definite** (invertible) at the true parameter. (2) The loss landscape is **locally quadratic** (bowl-shaped) near the optimum — the Hessian is non-degenerate. (3) The map from parameters to model predictions is locally **one-to-one** — different parameters near the optimum give different predictions.

**(b)** Two reasons: (1) **Permutation symmetry:** swapping two hidden neurons (permuting rows of the weight matrix and corresponding columns of the next layer) gives identical input-output behavior. For n hidden neurons, n! different parameter settings produce the same function. (2) **Zero weights:** setting a neuron's incoming weights to zero makes it irrelevant, regardless of its outgoing weights — a whole subspace of parameters maps to the same function. Both create many-to-one mappings from parameters to functions, making the Fisher information singular.

**(c)** Zero Hessian eigenvalues = **flat directions** in the loss landscape. The loss doesn't curve at all along those directions — it's a valley floor, not a bowl. From Phase 1: zero eigenvalues of a matrix mean that matrix has a non-trivial null space — there exist directions along which the matrix has no effect. Applied to the Hessian: there exist parameter perturbations that don't change the loss to second order.

**(d)** **F = λ·log(n) − (m−1)·log(log(n)) + O(1)** (plus nL* for the training loss term).

λ ≤ d/2 because singularities create flat directions that reduce the effective volume of parameter space that matters. For a model with d = 1,000,000 parameters, classical BIC says effective complexity = 500,000. But the RLCT might be λ = 10,000 — the model is **50× less complex** than its parameter count suggests. This is why overparameterized networks generalize: their true complexity (measured by λ) is much smaller than d/2.

**(e)** Regular value: d/2 = 3/2 = 1.5. RLCT: λ = 1/4 = 0.25. The network has **6× less effective complexity** than its parameter count suggests. The singularities from permutation symmetry and zero-weight redundancy dramatically reduce the model's effective degrees of freedom. The network "uses" far fewer effective parameters than it has — the rest are redundant due to symmetry.

---

### Question 7 (10 pts) — Phase Transitions and the LLC

**(a)** A phase transition is a moment when the model's internal structure **qualitatively reorganizes** — the loss drops sharply, internal representations change character, and new capabilities appear. **Grokking** is the paradigmatic example: a model memorizes training data (low training loss, high test loss) for many steps, then suddenly "clicks" and generalizes (test loss drops to match training loss). The model transitions from a memorization strategy to a generalizing algorithm.

**(b)** A sudden drop in the LLC indicates a **phase transition** — the model has moved from one type of singularity to another with lower effective complexity. The model found a **simpler, more structured solution**. Lower LLC = lower RLCT = less effective complexity = better generalization. The model reorganized its internal structure to achieve the same (or better) performance with a simpler strategy.

**(c)** Before grokking: the model likely has distributed, unstructured representations (memorization uses the network's capacity inefficiently). The LLC would be relatively high. After grokking: look for emergence of **structured circuits** — specific attention patterns, clean feature directions, identifiable algorithms. The LLC should be lower. Specifically, a researcher would compare: feature sparsity (sparser = more structured), circuit complexity (cleaner circuits = simpler strategy), and whether specific interpretable features appeared at the transition.

**(d)** A sudden capability gain is a bifurcation because the **qualitative structure of the loss landscape changes**. Before the transition, the training dynamics are in one basin (one type of solution). At the critical point, a new basin appears (or becomes accessible) that represents a fundamentally different strategy. The system transitions rapidly to the new basin. This is analogous to the pitchfork bifurcation from Lesson 25: a single fixed point (memorization) loses stability and two new solutions emerge (generalizing strategies), and the system "chooses" one.

---

### Question 8 (10 pts) — The Geometry of Singularities

**(a)** f(w₁, w₂) = (w₁w₂)² = w₁²w₂². This surface is zero along both axes (w₁ = 0 and w₂ = 0) and positive elsewhere. The zero set forms a **cross** (two intersecting lines). Near the origin, the surface rises like w₁²w₂² — extremely flat in all axis-aligned directions, rising only when BOTH w₁ and w₂ are nonzero. The **singularity is at the origin** — where the two lines of zeros intersect.

**(b)** H = [[2w₂², 4w₁w₂], [4w₁w₂, 2w₁²]]. At origin: H = **[[0,0],[0,0]]** — the zero matrix. This tells us nothing about the local shape. The Hessian says the surface is "flat to second order in every direction," which is technically true (the leading behavior is fourth-order) but completely misses the cross-shaped valley structure.

**(c)** The Hessian captures only second-order behavior (quadratic approximation). At a singularity, the interesting geometry is **higher-order** — the w₁²w₂² shape is fourth-order. The Hessian sees a flat plane where there's actually a complex valley structure. The additional tool needed is **resolution of singularities (blow-ups)** from algebraic geometry, which "zooms in" on the singularity and separates the crossing branches until the geometry becomes smooth.

**(d)** A blow-up replaces the singular point with a space of directions through it, separating branches that cross at the singularity until the geometry becomes smooth (a manifold). This is useful because the RLCT can be computed from the smooth, resolved geometry using standard calculus — the blow-up transforms the intractable singular integral into a tractable one.

---

### Question 9 (8 pts) — SLT for Alignment

**(a)** We'd want **aligned behavior to have lower RLCT** than misaligned behavior. Lower RLCT = simpler effective model = favored by Bayesian model selection. If alignment is "simpler" than misalignment in the RLCT sense, then the natural tendency of learning (minimizing free energy) would select for aligned solutions. We want the math to show that aligned strategies occupy geometrically "simpler" singularities.

**(b)** A deceptively aligned model must represent: the task + a model of the training process + a conditional strategy (behave differently based on context). This extra structure = higher functional complexity = **higher RLCT** than genuine alignment (which just represents the task + honest behavior). In principle, the LLC would be higher for the deceptive model, and SLT would predict that the deceptive strategy is disfavored by Bayesian learning — but this depends on the loss landscape geometry.

**(c)** Current limitations: (1) **Computing RLCTs is extremely hard** for realistic networks — exact computation requires algebraic geometry techniques that don't scale, and the LLC estimator has significant variance. (2) **The theory assumes Bayesian learning**, but real training uses SGD, which only approximates Bayesian inference. The gap between theory and practice is not fully understood. (3) **We don't yet know whether alignment/misalignment correspond to different singularity types** with different RLCTs — this is a conjecture, not a proven result.

---

### Question 10 (10 pts) — Synthesis

**(a)** The chain:
- **Eigenvalues → Hessian:** The Hessian is a matrix whose eigenvalues represent curvatures along principal directions — direct application of eigenanalysis from Phase 1.
- **Hessian → Loss landscape:** The Hessian's eigenvalues classify critical points (all positive = minimum, mixed = saddle) and determine the local geometry — from Phase 2's Taylor expansion.
- **Loss landscape → Singularities:** At certain critical points, the Hessian has zero eigenvalues — the landscape isn't quadratic but has exotic flat-direction geometry. These are singularities where standard tools fail.
- **Singularities → RLCT:** The RLCT measures "how singular" the singularity is by studying its geometry after resolution of singularities (blow-ups). It replaces parameter count as the true complexity measure.

**(b)** At step 5000, a **phase transition** occurred. The model transitioned from a more complex internal strategy (λ ≈ 2.0 = higher effective complexity) to a simpler one (λ ≈ 0.8 = lower effective complexity). Before: the model likely used a distributed, less structured representation (possibly memorization). After: the model found a more compact, organized solution — specific circuits or algorithms that achieve the same performance with less effective complexity. This is likely a grokking-type event where the model switched from memorization to generalization, or a circuit formation event where scattered computation consolidated into a clean algorithm.

**(c)** SLT connects the geometry of the loss landscape (mathematics) to the circuits models learn (interpretability) to the capabilities that emerge (behavior). It provides a principled complexity measure (the RLCT) that captures the true effective complexity of a model — not just parameter count — and predicts generalization through the free energy formula. Phase transitions in training correspond to geometric transitions between singularities, potentially allowing us to predict when capabilities (including dangerous ones) will emerge. If we can link alignment properties to specific singularity types, SLT would provide the mathematical foundation for understanding WHY aligned or misaligned solutions are selected during training.
