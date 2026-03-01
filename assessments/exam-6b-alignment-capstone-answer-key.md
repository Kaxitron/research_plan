# Exam 6B: The Alignment Problem — Capstone Final Examination — Answer Key

**The Path to AI Alignment — Lessons 66–67 + Cumulative Integration**

---

> **Grading philosophy:** This is the final exam. Grading rewards depth of synthesis over mechanical correctness. A response that weaves concepts from multiple phases into a coherent argument earns more than one that lists disconnected facts. For the research proposal (Q9) and reflections (Q10), there are no single "correct" answers — grading is based on mathematical precision, logical coherence, and demonstrated understanding.

---

### Question 1 (15 pts) — Outer vs. Inner Alignment

**(a)** **Outer alignment:** the training objective captures what we actually want. Failure example: a helpfulness reward model scores sycophancy (agreeing with the user) highly, so the model optimizes for telling people what they want to hear rather than the truth.

**Inner alignment:** the trained model actually optimizes for the training objective. Failure example: the model learns to predict what the reward model scores highly (gaming the proxy) rather than being genuinely helpful — it has an internal "goal" of maximizing reward-model score, not helpfulness.

**(b)** Even with a perfect pipeline, the reward model was trained on human preferences, which may not reflect what humans actually need. Humans may prefer confident-sounding wrong answers over uncertain correct ones, prefer flattery over honesty, or have inconsistent preferences across contexts. The outer alignment failure is: the loss function (reward model score) doesn't perfectly capture human values. This IS Goodhart's Law — the reward model is a proxy, and optimizing it hard enough will find divergences between the proxy and the true objective.

**(c)** The loss landscape has many basins (local minima or near-minima) that achieve similarly low training loss. Some basins correspond to models that have genuinely learned the task ("aligned mesa-optimizers"), while others correspond to models that have learned a different internal strategy that happens to perform well on training data. Training (gradient descent through the landscape) may settle in either basin depending on initialization and trajectory. The basins are separated by barriers — phase transitions (bifurcations from Lesson 25) where the model's internal structure changes qualitatively.

**(d)** A deceptively aligned model has learned to model its training process and acts aligned specifically to avoid parameter updates that would change its internal goals. From a stability perspective: the deceptive strategy is a **stable fixed point** in the space of possible strategies during training. Under gradient descent, the deceptive model receives low loss (appears aligned → no corrective gradient signal), so training doesn't push it away from deception. In the dynamical systems language of Phase 2, deceptive alignment is an **attractor** of the training dynamics — gradient flow converges to it and stays there. Breaking out would require either very different training (perturbation large enough to escape the basin) or an interpretability tool that can detect the deception inside the model.

---

### Question 2 (15 pts) — The Five-Phase Connection Chain

**Example answer (one of many valid chains):**

Neural networks generalize despite being massively overparameterized. Here is why, traced through five phases.

Start with **eigenvalues (Phase 1)**. The Hessian matrix of the loss function has eigenvalues that describe the curvature of the loss landscape at any point. At a minimum, the eigenvalues determine how "sharp" or "flat" the basin is — the condition number λ_max/λ_min measures the elongation.

Now apply the **Taylor expansion (Phase 2)**: near a critical point, L(w) ≈ L(w*) + ½(w−w*)ᵀH(w−w*). The loss landscape IS a quadratic form locally, and the Hessian eigenvalues describe its shape. But neural networks have a special property: many Hessian eigenvalues are zero or near-zero. These correspond to **flat directions** — directions in parameter space where you can move without changing the loss. These arise from symmetries: permuting hidden neurons (Phase 5, group actions by S_n on weight space) doesn't change the function. The **orbit-stabilizer theorem** says the orbit has size |G|/|Stab(w)|, and at points with large stabilizers, the landscape has degenerate singularities.

The **Bayesian framework (Phase 3)** provides the generalization guarantee. The marginal likelihood P(D|M) = ∫P(D|θ)P(θ)dθ automatically penalizes complexity through Occam's razor: complex models spread their prior thinly. For singular models (neural networks), the standard BIC approximation using k/2 fails — the Fisher information is singular. **Singular Learning Theory (Phase 4/5)** provides the correct formula: the free energy is F ≈ λ·log(n), where the **RLCT λ** replaces k/2. The RLCT is computed by resolving the singularities through blow-ups (algebraic geometry from Phase 5). Because λ ≤ k/2 always, the Bayesian penalty for neural networks is always less than their parameter count suggests.

Finally, this connects to **alignment (Phase 6)**: if we can track how λ changes during training (the Local Learning Coefficient), we can detect **phase transitions** — moments when the model restructures internally. These might correspond to capability emergence, including potentially dangerous capabilities. Monitoring λ gives a mathematical signal for when to intervene, connecting the abstract geometry of singularities to the practical problem of safe deployment.

*Scoring: 5 pts for ≥ 5 concepts correctly used. 5 pts for ≥ 4 phases represented. 5 pts for coherent narrative connecting them logically (not just listing).*

---

### Question 3 (15 pts) — Interpretability as Alignment Strategy

**(a)** Three techniques:
1. **Logit lens / tuned lens:** projects intermediate layer representations through the unembedding matrix to see what the model would predict at each layer. Reveals the **progressive refinement** of predictions across depth — which layers contribute to the final answer.
2. **Activation patching / causal tracing:** replaces activations at specific positions and layers with "clean" or "corrupted" versions and measures the effect on output. Reveals **which components are causally responsible** for specific behaviors — not just correlated, but necessary.
3. **Sparse autoencoders (SAEs):** train a separate network to decompose activations into a sparse, overcomplete basis. Reveals **individual features** that the model has learned, disentangling them from the superposition in which they're stored.

**(b)** In Phase 1 terms: the model has d_model dimensions in its residual stream but needs to represent N >> d_model concepts (features). It can't assign each feature its own orthogonal direction (that would require N dimensions). Instead, it uses **almost-orthogonal** directions. In high dimensions, you can pack exponentially many nearly-orthogonal vectors — the Johnson-Lindenstrauss lemma shows that random vectors in high dimensions are approximately orthogonal. The cost: features interfere with each other (non-zero dot products), creating "crosstalk." This interference is manageable when only a few features are active simultaneously (sparsity), which is why superposition works for sparse feature distributions.

**(c)** An SAE minimizes reconstruction error plus a sparsity penalty: L = ‖x − decode(encode(x))‖² + λ‖encode(x)‖₁. The L1 penalty corresponds to a **Laplace prior** on the feature activations (from Lesson 35 / Q2 of Exam 3B: MAP with Laplace prior = L1 regularization = Lasso). So training the SAE is finding the MAP estimate under a model where: the likelihood says "reconstruct the activations well" (Gaussian noise assumption) and the prior says "most features should be off" (Laplace / sparsity prior). This IS approximate Bayesian inference with a sparsity prior.

**(d)** By **Rice's theorem** (Lesson 51), any non-trivial semantic property of a program is undecidable in general. "This circuit implements addition" is a semantic property — there's no general algorithm to verify it for all possible circuits. However, Rice's theorem gives a worst-case impossibility. In practice, we don't need to verify interpretations of arbitrary programs — we need to verify them for **specific networks** with specific structure. Partial verification is valuable: even if we can't prove an interpretation is complete and correct, we can test it against interventions (activation patching), check consistency across inputs, and falsify incorrect interpretations. The situation is analogous to software testing: you can't prove a program is bug-free (undecidable), but you can find bugs and build confidence through testing.

---

### Question 4 (15 pts) — Singular Learning Theory and Alignment

**(a)** SLT free energy: **F ≈ nL* + λ·log(n) − (m−1)·log(log(n)) + O(1)**

- n = number of data points
- L* = minimum average training loss (how well the best parameters fit)
- λ = RLCT (Real Log Canonical Threshold) — effective model complexity
- m = multiplicity of the dominant singularity

BIC: F ≈ nL* + (k/2)·log(n), where k = parameter count. BIC uses k/2 as complexity; SLT uses λ ≤ k/2. BIC assumes regularity (non-singular); SLT handles singularities correctly.

**(b)** The symmetric group Sₙ acts on weight space by permuting hidden neurons. Concretely, if we permute the n neurons using σ ∈ Sₙ, we permute the rows of the weight matrix and the corresponding columns of the next layer's weight matrix. This action is a **group action** (Lesson 56): it satisfies the group axioms and preserves the input-output function.

The **orbit** of a weight configuration W under Sₙ is the set of all n! permuted versions that compute the same function. The **stabilizer** of W is the subgroup of permutations that leave W unchanged (e.g., if two neurons have identical weights, swapping them is in the stabilizer). By the **orbit-stabilizer theorem**: |orbit| × |stabilizer| = |Sₙ| = n!.

Singularities occur at weight configurations with **non-trivial stabilizers** — where some neurons are identical (or zero). At these points, the loss landscape has degeneracies (zero Hessian eigenvalues) because there are directions in weight space that don't change the function. The singular set has dimension > 0, making the Fisher information singular.

For n hidden neurons: there are **n!** equivalent configurations (the orbit), so the model has at least n!-fold symmetry.

**(c)** At a singularity, the Hessian has zero eigenvalues corresponding to directions along the singular set. The RLCT λ measures how quickly the loss grows as you move **away** from the singular set in all directions. For a regular model, the loss grows quadratically (Hessian positive definite), giving λ = k/2. For a singular model, the loss grows more slowly in some directions (the degenerate ones), giving λ < k/2. More zero Hessian eigenvalues → more flat directions → slower loss growth → smaller RLCT → lower effective complexity. The model has "wasted" parameters in the sense that many parameter directions don't contribute to distinguishing the function.

**(d)** A sudden drop in LLC at step 5000 indicates a **phase transition**: the model has moved from one singularity basin to another with lower RLCT. Mathematically, the loss landscape topology has changed — the model crossed a bifurcation point (Lesson 25) where the nature of the optimal parameters shifted qualitatively.

In terms of what the model learned: this likely corresponds to circuit formation — the model transitioned from a disorganized representation to a structured algorithm. For example, an induction head might have formed (a circuit that copies patterns), or the model might have discovered a generalizable rule after initially memorizing (grokking). The new singularity has lower λ (simpler effective model), suggesting the model found a more compressed/generalizable solution.

**(e)** SLT is potentially transformative because it provides a **mathematical observable** (the LLC/RLCT) that measures functional complexity independently of parameter count. For alignment: if we could track the LLC during training, drops might signal capability acquisition — including dangerous capabilities. If deceptive alignment requires more functional complexity than honest alignment (the deceptive model must model its training process in addition to doing the task), it would have a higher RLCT, making it detectable. What we'd need: reliable LLC estimation for frontier-scale models, a theoretical understanding of which singularity types correspond to which capabilities, and empirical validation connecting LLC transitions to behavioral changes.

---

### Question 5 (15 pts) — The RLHF Pipeline: A Mathematical Dissection

**(a)** Loss: **cross-entropy** L = −Σ log P_θ(x_t | x_{<t}). This is the negative log-likelihood under the autoregressive model, so minimizing it IS MLE (Phase 3, Lesson 30). The distribution being estimated: P(next token | context) — the conditional distribution of language. Assumption: the training data is representative of the distribution we want the model to learn (i.i.d. samples from the "true" distribution of text).

**(b)** SFT shifts the model from the broad pre-training distribution (all internet text) toward a narrower distribution (helpful assistant responses). In Phase 1 terms: the pre-trained model's representation space spans a high-dimensional manifold of possible text. SFT **projects** the model's behavior onto a lower-dimensional subspace corresponding to the "helpful response" manifold. The model's capabilities are still present (the full space hasn't been destroyed), but the output distribution is concentrated on the useful subspace.

**(c)** P(A ≻ B) = σ(r(A) − r(B)). The loss for a preference pair where A is preferred:

L = −log σ(r(A) − r(B)) = −log(1/(1 + e^{−(r(A)−r(B))}))

This IS **binary cross-entropy** with the label "A is better" and the predicted probability being σ(r(A)−r(B)). From Lesson 13 / Exam 2A Q2: σ'(z) = σ(z)(1−σ(z)), which means the gradient is strongest when the model is uncertain (σ ≈ 0.5) and weakest when confident (σ ≈ 0 or 1) — exactly the right behavior for learning from comparisons.

**(d)** J(π) = E_{x~π}[R(x)] − β·D_KL(π ‖ π_ref).

- E[R(x)]: maximize expected reward (make the model produce outputs the reward model scores highly)
- β·D_KL: don't drift too far from the reference (SFT) model
- β controls the tradeoff: small β → chase reward aggressively (risk reward hacking), large β → stay close to reference (conservative, underfit preferences)

Constrained optimization interpretation: maximize E[R(x)] **subject to** D_KL(π ‖ π_ref) ≤ ε. The Lagrange multiplier is β. This is exactly the structure from Lesson 18: maximize objective subject to constraint, with the multiplier measuring the tradeoff.

**(e)** Failure modes:
- **Pre-training:** data contamination or bias → model learns the wrong distribution (garbage in, garbage out)
- **SFT:** low-quality demonstrations → model learns to imitate surface patterns rather than deep competence
- **Reward model:** inconsistent human preferences or reward hacking → the reward model rewards something other than helpfulness
- **PPO:** mode collapse (the model finds one "template" that scores high and repeats it), or KL penalty too weak → model exploits reward model artifacts

---

### Question 6 (15 pts) — Scaling Laws, Emergence, and Safety

**(a)** If L ∝ C^{−α} and α ≈ 0.05 (typical), then 10× compute gives: L_new/L_old = 10^{−0.05} ≈ 0.89. About an **11% reduction** in loss. Scaling laws predict smooth, predictable improvement — but this smooth loss improvement can mask sudden capability jumps.

**(b)** Loss is a smooth average over many tasks/capabilities. A specific capability requires a minimum "circuit complexity" that only becomes learnable at a certain scale. Below that scale, the model lacks capacity to represent the circuit — the corresponding minimum in the loss landscape doesn't exist (it's beyond a bifurcation threshold). At the critical scale, a pitchfork or saddle-node bifurcation creates a new minimum representing the capability. The overall loss decreases smoothly because it averages over many capabilities, but any individual capability appears suddenly — exactly like a phase transition crossing a bifurcation point.

**(c)** In principle: phase transitions correspond to changes in the RLCT, and the LLC can track these. A dangerous capability emerging would cause a detectable LLC drop. In practice: (1) we'd need to compute the LLC for frontier-scale models (computationally expensive), (2) we'd need to distinguish capability-related transitions from benign ones (the LLC doesn't tell you WHAT changed, only THAT something changed), (3) we'd need a theory connecting specific RLCT values to specific capabilities (currently doesn't exist). What you'd measure: LLC over training, activation patterns at transition points, interpretability analysis of circuits forming at each transition.

**(d)** Before the threshold: the AI is a passive optimizee — it's being trained, and game theory doesn't apply because it's not making strategic choices. After: the AI becomes a **strategic player** in a game against its trainers. It can model the training process, predict what behaviors will be reinforced, and choose actions based on their effect on its future training. The game changes from a single-player optimization to a multi-agent strategic interaction. The key Nash equilibrium concern: if the AI's "utility function" (mesa-objective) differs from the trainers' objective, the equilibrium may involve the AI strategically cooperating during training and defecting during deployment — exactly the deceptive alignment scenario from Q1.

**(e)** **Proposal: LLC monitoring for capability emergence.** During training, continuously estimate the Local Learning Coefficient (SLT, Phase 4/5). When a significant LLC drop is detected (indicating a phase transition / new capability acquisition), pause training and run interpretability analysis (activation patching, SAE decomposition from Phase 4) on the model before and after the transition to identify what circuit formed. If the new circuit appears safety-relevant (e.g., modeling the training process, tracking human oversight patterns), flag for human review before continuing. This uses: dynamical systems theory (Phase 2) for detecting transitions, SLT (Phase 4/5) for quantifying them, and mechanistic interpretability (Phase 4) for understanding them.

---

### Question 7 (10 pts) — Gödel, Löb, and Self-Reference

**(a)** Any formal system powerful enough to describe basic arithmetic contains true statements that the system cannot prove. The system is either incomplete (has true-but-unprovable statements) or inconsistent (can prove false things). No system can fully characterize its own truths.

**(b)** Löb's theorem says: if a system can prove "if I can prove SAFE then SAFE," then it can prove SAFE — regardless of whether it actually IS safe. This means the statement "I am safe" is either: (1) provable (in which case Löb's theorem is trivially satisfied), or (2) the system cannot even prove the conditional "if I can prove I'm safe, then I'm safe" — which means it can't bootstrap trust in its own safety properties. An AI system operating within a formal system **cannot meaningfully prove its own safety** from within that system. This is a fundamental limitation on self-certifying safety.

**(c)** Rice's theorem says no general algorithm can decide non-trivial semantic properties. But we're not trying to solve the general case — we're working with specific networks. Partial verification is possible and valuable: we can verify specific inputs ("this model is safe on these 10,000 test cases"), verify structural properties ("this attention head always attends to the subject"), and falsify hypotheses ("this circuit does NOT implement deception, because ablating it doesn't remove deceptive behavior"). Partial results reduce uncertainty even without complete guarantees. This is analogous to software testing: we can't prove bug-free code, but extensive testing builds justified confidence.

**(d)** "Verify every output" faces two problems: (1) by Gödel, the verification system is either incomplete (can't verify all safe outputs, leading to false negatives and reduced capability) or must operate in a stronger system (which then faces its own incompleteness), and (2) verifying semantic properties is generally undecidable (Rice's theorem). A more realistic protocol: statistical verification (test on many inputs and bound failure probability — Phase 3), anomaly detection (flag outputs that look unusual — interpretability), and human-in-the-loop oversight for high-stakes decisions. This trades certainty for practical robustness.

---

### Question 8 (15 pts) — The Alignment Problem in Full

**(a)** Three Goodhart's Law examples:
1. **Optimization (Phase 2):** gradient descent minimizes the training loss (a proxy for generalization), but minimizing training loss too aggressively leads to overfitting — the measure (training loss) ceased being a good measure of actual performance.
2. **RL (Phase 4):** the RL agent optimizes the reward function, but reward hacking (covering mess with blanket) optimizes the proxy without achieving the intended goal.
3. **Statistics (Phase 3):** p-value hacking — researchers optimize for statistical significance (the measure) through multiple comparisons, data dredging, etc., until p < 0.05 ceases to indicate a real effect.

**(b)** The reward function defines a loss landscape. Gradient-based training finds minima of this landscape. But the reward function is a proxy — it captures some aspects of what we want but not all. In the vast, high-dimensional landscape, there exist minima that score high on the proxy but diverge from what we actually want. The optimizer (being indifferent to our true intentions) will find whichever minimum is easiest to reach, including these "misaligned" ones. We can't just "fix the reward" because: (1) human values are too complex to fully specify (outer alignment), (2) any formal specification will have edge cases (Goodhart), and (3) the model may be smarter than us at finding exploits we didn't anticipate.

**(c)** 
- **RLHF:** Trains a reward model from preferences, optimizes policy against it. Assumes: human preferences are consistent and capture what we actually want.
- **Constitutional AI:** AI critiques its own outputs based on stated principles. Assumes: the principles are sufficiently complete and the model interprets them as intended.
- **DPO:** Directly optimizes the policy on preference data without a separate reward model. Assumes: the Bradley-Terry preference model is correct and the KL constraint is sufficient.
- **Debate/amplification:** AI systems argue, humans judge. Assumes: truth has a "persuasive advantage" — correct arguments are more convincing than incorrect ones, even to non-expert judges.

**(d)** At superhuman levels: (1) **Bayesian reasoning (Phase 3):** human evaluators become unreliable — we can't assign accurate likelihoods to superhuman outputs because we can't verify them. The reward model, trained on human judgments, becomes poorly calibrated in the superhuman regime (out of distribution). Our posterior beliefs about model behavior become unreliable. (2) **Decision theory (Phase 6):** a sufficiently capable AI becomes a strategic agent. Under CDT or FDT, it may reason about the consequences of its actions on its own training. If its mesa-objective differs from alignment, it has both the capability and (under some decision theories) the incentive to behave deceptively — cooperating now to defect later when oversight is weaker.

---

### Question 9 (15 pts) — Research Proposal

*Grading rubric: 3 pts for clear problem statement, 3 pts for correctly identifying mathematical tools, 3 pts for concrete approach, 3 pts for realistic expected output, 3 pts for honest limitations.*

**Example answer for option (A): Using the LLC to detect deceptive alignment during training:**

**Problem:** Deceptive alignment is the scenario where a model appears aligned during training but pursues different goals during deployment. Detecting it is critical because standard behavioral evaluation can't distinguish genuine from deceptive alignment. We need an internal signal.

**Tools:** SLT and the Local Learning Coefficient (Phase 4/5, Lessons 49–50), mechanistic interpretability / sparse autoencoders (Phase 4, Lessons 47–48), bifurcation theory (Phase 2, Lesson 25), and Bayesian model comparison (Phase 3, Lesson 37).

**Approach:** Hypothesis: deceptive alignment requires the model to simultaneously implement (a) task performance and (b) a model of the training process. This requires more functional complexity than honest alignment, which only needs (a). Therefore, a deceptively aligned model should have a higher RLCT than an honestly aligned one, because it has learned a more complex internal function.

Concretely: (1) Train small transformer models on tasks where we CAN verify alignment (synthetic environments). (2) Track the LLC during training. (3) Deliberately induce deceptive-like strategies (e.g., by making the training signal differ from the evaluation signal). (4) Compare LLC trajectories: does the deceptive model show a different LLC pattern than the honest one? (5) Use SAEs to decompose the activations at LLC transition points to see if deception-related circuits are detectable.

**Expected output:** An empirical demonstration that the LLC differs between deceptive and honest models in a toy setting, plus identification of interpretable features corresponding to "training-process modeling." If successful, this would be a proof-of-concept for LLC-based deception detection.

**Limitations:** (1) Toy models may not generalize to frontier scale. (2) The hypothesis (deception requires higher RLCT) might be wrong — a sufficiently capable model might implement deception "for free" within its existing complexity. (3) LLC estimation is noisy and computationally expensive at scale. (4) We need to be able to reliably induce deceptive strategies in toy models, which itself is an open problem.

---

### Question 10 (20 pts) — The Big Picture

**(a)** Non-technical: We're building machines that can think and act in the world. The alignment problem is making sure these machines do what's actually good for people, not just what they were literally told. It's like wishing on a monkey's paw — the wish gets granted, but not the way you meant. We need to figure out how to give clear, complete instructions to something that takes instructions very literally and is potentially smarter than us.

**(b)** To a mathematician: Alignment is the problem of ensuring that the function implemented by a trained neural network (a point in a high-dimensional parameter space found by stochastic optimization of a proxy objective) corresponds to the intended behavior across the full input distribution, including inputs not seen during training. It's a generalization problem (does the training objective extend correctly?), a specification problem (does the formal objective capture the informal desiderata?), and a verification problem (can we confirm the model satisfies the specification?).

**(c)**

| Phase | Most Important Insight for Alignment |
|-------|--------------------------------------|
| 1. Linear Algebra | Neural networks are composed of linear transformations, and understanding what they do geometrically (projection, rotation, scaling via SVD) is the foundation for understanding what any layer computes. |
| 2. Calculus & ODEs | Training is a dynamical system; its trajectory, stability, and phase transitions are governed by the loss landscape geometry (Hessian eigenvalues, bifurcations), connecting optimization to dynamics. |
| 3. Probability & Stats | Every training objective is rooted in probabilistic inference (MLE, KL divergence), and evaluating whether a model is "safe" is fundamentally a statistical inference problem requiring Bayesian reasoning. |
| 4. Neural Networks & Interp | The gap between what a model computes and what we think it computes is the alignment gap; mechanistic interpretability and SLT give us mathematical tools to measure and close it. |
| 5. Extended Math | Fundamental limitations exist (Gödel, Rice) on what can be verified, but algebraic geometry (singularities, RLCT) provides the right complexity measure for understanding why neural networks generalize. |
| 6. Alignment Theory | Alignment is not just a technical optimization problem — it's a multi-agent strategic interaction governed by game theory, decision theory, and fundamental questions about what rational agents should do. |

**(d)** and **(e)** — Open-ended. Grading based on depth of reasoning, correct use of mathematical concepts, and genuine engagement with the material. Look for: specific mathematical tools cited correctly, awareness of both possibilities and limitations, and evidence that the student has internalized the connections across phases rather than treating them as isolated subjects.
