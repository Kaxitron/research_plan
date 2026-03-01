# Exam 6B: The Alignment Problem — Capstone Final Examination

**The Path to AI Alignment — Lessons 66–67 + Cumulative Integration Across All Phases**

---

| | |
|---|---|
| **Time Allowed** | 90 minutes |
| **Total Points** | 150 |
| **Materials** | Pencil, paper. No calculator needed. |
| **Format** | 10 questions — this is the final exam of the entire curriculum. It requires synthesizing concepts across all phases. |

> **Advice:** This exam tests deep integration, not memorization. Every question asks you to connect ideas from multiple phases. Show your reasoning. The best answers weave together mathematical precision with conceptual clarity.

> *"The goal was never to learn linear algebra, calculus, probability, or neural networks in isolation. It was to build the unified mathematical language needed to work on the most important problem in human history."*

---

## Question 1 (15 pts) — Outer vs. Inner Alignment

**(a)** Define outer alignment and inner alignment. Give a concrete example of each type of failure for a language model.

**(b)** A model is trained with RLHF to be helpful. The reward model scores helpfulness based on human preferences. Explain how this could fail at the outer alignment level even if the RLHF pipeline works perfectly.

**(c)** Mesa-optimization: a model trained to predict next tokens might develop an internal "goal" that diverges from loss minimization. Explain mesa-optimization using the concept of a loss landscape from Phase 2. *(Hint: there may be multiple basins in the loss landscape that achieve similarly low training loss but implement different internal strategies.)*

**(d)** Deceptive alignment: a mesa-optimizer could learn to appear aligned during training and diverge during deployment. Using concepts from Phase 2 (Lessons 25–26), explain this as a stability problem: in what sense is deceptive alignment a "stable strategy" from the model's perspective?

---

## Question 2 (15 pts) — The Five-Phase Connection Chain

Construct a mathematical argument connecting AT LEAST FIVE concepts from different phases of the curriculum. Your chain should form a coherent story about why neural networks generalize (or fail to).

You must include concepts from at least 4 different phases. Here are some building blocks (you need not use exactly these):

- Phase 1: Eigenvalues, SVD, rank, null space, projection
- Phase 2: Hessian, gradient flow, bifurcations, Taylor expansion, condition number
- Phase 3: MLE, KL divergence, Bayesian model comparison, marginal likelihood
- Phase 4: Backpropagation, attention, superposition, scaling laws
- Phase 5: Singularities, group actions, RLCT, resolution of singularities, Gödel/Löb
- Phase 6: Game theory, decision theory, alignment problem

Your answer should be a coherent 1-page argument (roughly 300–400 words), not a list of disconnected facts. Explicitly mark each concept with its phase number.

---

## Question 3 (15 pts) — Interpretability as Alignment Strategy

**(a)** Name and briefly describe three distinct mechanistic interpretability techniques. For each, state what it reveals about the model that other techniques don't.

**(b)** The superposition hypothesis says models encode more features than they have dimensions. Explain this as a geometry problem using concepts from Phase 1. *(Hint: how can you pack more vectors than dimensions into a space while keeping them "almost orthogonal"?)*

**(c)** Sparse autoencoders (SAEs) attempt to decompose activations into interpretable features. Using Phase 3 concepts, explain why training an SAE is a form of approximate Bayesian inference with a sparsity prior.

**(d)** A critic argues: "Interpretability at the circuit level is useless because you can't verify whether your interpretation is correct." Using concepts from Phase 5 (logic, Gödel), explain why verification of interpretations is fundamentally hard, but also why partial verification is still valuable.

---

## Question 4 (15 pts) — Singular Learning Theory and Alignment

**(a)** State the SLT free energy formula and define each term. Contrast it with BIC.

**(b)** Neural networks are singular because of permutation symmetry: swapping two neurons in a hidden layer doesn't change the function. Using Phase 5 concepts (group actions, orbit-stabilizer), explain how this symmetry creates singularities in weight space. How many equivalent weight configurations exist for a network with n hidden neurons in one layer?

**(c)** The RLCT λ measures effective model complexity. Explain why λ < k/2 for neural networks. Use the geometric intuition of "flat directions" in the loss landscape near a singularity, connecting to the Hessian eigenvalues from Phase 2.

**(d)** The Local Learning Coefficient (LLC) can be estimated during training. A plot of LLC over training steps shows a sudden drop at step 5000. Interpret this event: what happened mathematically (phase transition between singularities) and what might have happened in terms of what the model learned (e.g., circuit formation, capability acquisition).

**(e)** In one paragraph: why is SLT potentially transformative for alignment? What would we need to measure and what conclusions could we draw?

---

## Question 5 (15 pts) — The RLHF Pipeline: A Mathematical Dissection

Trace the complete LLM training pipeline. For each stage, identify the mathematical concept from earlier phases and explain why it works (or might fail).

**(a)** Pre-training: next-token prediction. What loss function is used? Show that this is MLE (Phase 3). What distribution is being estimated? What assumption is being made about the data?

**(b)** Supervised fine-tuning (SFT): training on human-written examples. How does this change the distribution the model represents? What Phase 1 concept describes the relationship between the pre-trained model's representation space and the SFT distribution?

**(c)** Reward model training: humans rank pairs of outputs. The Bradley-Terry model says P(A ≻ B) = σ(r(A) − r(B)) where σ is the sigmoid. Compute the loss function for training the reward model. *(Hint: it's binary cross-entropy.)* Connect to Lesson 2's sigmoid derivative.

**(d)** PPO fine-tuning: the policy is updated to maximize reward while staying close to the SFT model via a KL penalty. Write the objective: J(π) = E[R(x)] − β·D_KL(π ‖ π_ref). Explain what each term does. What is the constrained optimization interpretation (Phase 2)?

**(e)** Failure mode analysis: for each stage, name one specific way the mathematical framework can break, producing a misaligned model.

---

## Question 6 (15 pts) — Scaling Laws, Emergence, and Safety

**(a)** Scaling laws state that loss decreases as a power law in compute, data, and parameters: L ∝ C^{−α}. What does this predict about the loss of a model with 10× more compute than the current frontier?

**(b)** Emergent capabilities appear suddenly at certain scales. Using bifurcation theory from Phase 2, explain emergence as a phase transition. Why is gradual improvement in loss compatible with sudden capability jumps?

**(c)** A safety researcher wants to predict when a dangerous capability will emerge. Using SLT (Phase 4/5), explain why this is possible in principle (phase transitions correspond to changes in the RLCT) but hard in practice. What would you need to measure?

**(d)** The "sharp left turn" scenario: at some scale, an AI system suddenly becomes much more capable at strategic reasoning, including reasoning about its training process. Using game theory (Phase 6), model this as a game between the AI and its trainers. What changes when the AI becomes a strategic player rather than a passive optimizee?

**(e)** Propose one concrete safety measure that uses mathematical tools from this curriculum. Explain which tools it uses and what it would detect or prevent.

---

## Question 7 (10 pts) — Gödel, Löb, and Self-Reference

**(a)** State Gödel's first incompleteness theorem informally. What does it say about what a formal system can prove about itself?

**(b)** Löb's theorem: if a system can prove "if I can prove P, then P," then the system can prove P. Explain why this constrains what an AI can prove about its own safety. *(Specifically: can an AI system prove "I am safe" within its own formal system?)*

**(c)** Despite these impossibility results, alignment researchers still work on verification. Using the analogy from Phase 5 (decidability/Rice's theorem), explain why partial verification is possible and valuable even when complete verification is impossible.

**(d)** A proposed AI safety protocol: "The AI system formally verifies each of its outputs before producing them." Using Gödel/Löb, explain why this protocol has fundamental limitations. What would a more realistic protocol look like?

---

## Question 8 (15 pts) — The Alignment Problem in Full

**(a)** Goodhart's Law: "When a measure becomes a target, it ceases to be a good measure." Give three examples from the curriculum where Goodhart's Law appears (one from optimization, one from RL, one from statistics).

**(b)** Specification gaming is Goodhart's Law applied to AI. Explain using the optimization landscape from Phase 2: the reward function defines a loss landscape, and the model finds a minimum — but not the minimum we wanted. Why can't we just "fix the reward function"?

**(c)** Current alignment approaches: RLHF, Constitutional AI, DPO, debate/amplification. For each, state in one sentence what it does and identify its key mathematical assumption.

**(d)** Why might current alignment techniques fail at superhuman levels? Use at least one concept each from Phase 3 (Bayesian reasoning) and Phase 6 (decision theory) in your answer.

---

## Question 9 (15 pts) — Research Proposal

Choose ONE open problem from the list below (or propose your own). Write a 1-page research proposal (~400 words) that includes:

1. **Problem statement:** what you're trying to solve and why it matters for alignment
2. **Mathematical tools:** identify exactly which tools from the curriculum you'd use (cite specific lessons/phases)
3. **Approach:** a concrete (if preliminary) plan of attack
4. **Expected output:** what would a successful result look like?
5. **Limitations:** what could go wrong or what assumptions might be violated?

**Open problems:**
- (A) Using the LLC to detect deceptive alignment during training
- (B) Formalizing "alignment stability" as a Lyapunov function problem
- (C) Connecting superposition geometry to the RLCT
- (D) Designing a game-theoretic framework for scalable oversight
- (E) Your own proposal (must use tools from ≥ 3 phases)

---

## Question 10 (20 pts) — The Big Picture

**(a)** In 3–4 sentences, explain the alignment problem to someone who has no technical background. Do not use jargon.

**(b)** Now explain it to a mathematician, using precise language. In 3–4 sentences, characterize alignment as a mathematical problem.

**(c)** You have now spent months building a mathematical foundation across 7 phases. For each phase, state in ONE sentence the single most important insight it contributes to understanding alignment:

| Phase | Most Important Insight for Alignment |
|-------|--------------------------------------|
| 1. Linear Algebra | |
| 2. Calculus & ODEs | |
| 3. Probability & Statistics | |
| 4. Machine Learning & Interp | |
| 5. Extended Math | |
| 6. Alignment Theory | |

**(d)** What is the single most important open question in AI alignment, in your view? Why? What mathematical tools would be needed to answer it? (3–5 sentences.)

**(e)** Final reflection: what concept from this curriculum changed how you think about AI, and why?

---

## 🏗️ The Final Project

You've passed the capstone exam. One challenge remains — a 5-hour intensive project that ties together every lesson across the entire curriculum. Build, train, interpret, and align a language model from scratch.

👉 **[Final Project: The Alignment Observatory](final-project-alignment-observatory.md)**
