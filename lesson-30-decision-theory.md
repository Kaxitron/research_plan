# Lesson 30: Decision Theory — CDT, EDT, and FDT

[← Back to Table of Contents](../README.md) | [← Lesson 29](lesson-29-game-theory.md)

---

## 🎯 Core Learning

### What Is Decision Theory?
- Game theory studies multi-agent strategic interaction. **Decision theory** studies how a *single agent* should make choices under uncertainty.
- The fundamental question: given your beliefs and values, what should you do?
- **Expected utility theory:** choose the action that maximizes expected utility (probability-weighted average of outcomes). The baseline framework.
- **Utility functions:** numerical representations of preferences. If you prefer A to B to C, assign u(A) > u(B) > u(C). The von Neumann-Morgenstern theorem shows that "rational" preferences can always be represented this way.
- **Decision matrices:** states of the world × actions → outcomes. Choose the action with highest expected utility given your probability distribution over states.

### Three Decision Theories

- **Causal Decision Theory (CDT):** choose the action that *causes* the best outcome. Standard in economics and most philosophy. Uses causal counterfactuals: "if I were to do X, what would happen?"
  - **Problem:** fails on Newcomb's Problem. CDT two-boxes because it reasons "my choice can't cause the predictor to have already changed the box contents." But two-boxers get $1,000 while one-boxers get $1,000,000.

- **Evidential Decision Theory (EDT):** choose the action that, conditional on you performing it, makes the best outcome most probable. "Given that I'm the kind of agent that does X, what's the expected outcome?"
  - **Problem:** falls for "smoking lesion"-type problems. EDT might avoid smoking not because it causes cancer, but because smokers tend to have the gene — confuses correlation with causation.

- **Functional Decision Theory (FDT):** choose the output of your decision procedure that leads to the best outcome across all instances where that same decision procedure runs. "What decision function, if implemented, produces the best outcomes?"
  - FDT one-boxes in Newcomb's (because the predictor simulated your decision procedure, so your output determines box contents)
  - FDT smokes in the smoking lesion (because the decision to smoke doesn't cause the gene)
  - FDT cooperates in the symmetric Prisoner's Dilemma (because if you and your copy run the same algorithm, your output determines both actions)

### Key Thought Experiments

- **Newcomb's Problem:** A predictor (who's almost always right) has either put $1M in an opaque box or not, based on whether it predicts you'll take only the opaque box or both boxes. A transparent box contains $1,000. CDT two-boxes; FDT one-boxes.
- **Parfit's Hitchhiker:** You're stranded. A driver will rescue you only if they predict you'll pay $100 upon reaching town. CDT won't pay (the rescue already happened); FDT pays (because the driver's prediction was based on your decision procedure).
- **Transparent Newcomb's:** You can see what's in both boxes. CDT always two-boxes; FDT still one-boxes when the opaque box is full, because its decision procedure being the "one-box type" is what caused the box to be full.
- **The Smoking Lesion:** A gene causes both cancer and desire to smoke. Smoking itself doesn't cause cancer. EDT avoids smoking (confuses evidence for causation); CDT and FDT smoke.
- **Psychological Twin Prisoner's Dilemma:** You and your opponent are psychological twins — you'll make the same choice. CDT defects (can't cause twin's choice); FDT cooperates (same algorithm → same output → mutual cooperation beats mutual defection).
- **Death in Damascus:** You flee to Damascus to avoid Death, but Death went to Damascus because they predicted you'd flee there. No decision theory handles this perfectly — it's about the limits of prediction.

### Utility Theory Deep Cuts
- **Risk aversion:** concave utility functions (diminishing marginal utility). Explains why people buy insurance.
- **Von Neumann-Morgenstern axioms:** completeness, transitivity, continuity, independence. If your preferences satisfy these, they can be represented as expected utility maximization.
- **St. Petersburg paradox:** a game with infinite expected value that nobody would pay much to play. Reveals that we don't maximize expected money — we maximize expected utility.
- **Ellsberg paradox:** people prefer known risks over unknown risks. Violates expected utility theory. Related to the distinction between risk and uncertainty (Knightian uncertainty).
- **Bounded rationality:** real agents have limited computation. Herbert Simon's insight that "satisficing" (finding good enough) often beats "optimizing" (finding the best). Relevant to how AI systems actually make decisions.

## 📺 Watch — Primary

1. **Robert Miles — "Newcomb's Problem and the Tragedy of Rationality"**
   - https://www.youtube.com/watch?v=M6LkGpDYl-A (or search his channel)
   - *Clear explanation of why decision theory matters for AI alignment.*

## 📺 Watch — Secondary

2. **Rational Animations — "Functional Decision Theory"**
   - Animated explanation of FDT and why it matters for AI
3. **Actualized.org — "Newcomb's Paradox"** or any other visual Newcomb's explainer
4. **Yale ECON 159 — Ben Polak, Lectures on Expected Utility** (same series as game theory)

## 📖 Read — Primary

- **"Functional Decision Theory" by Yudkowsky & Soares (2017)**
  - https://arxiv.org/abs/1710.05060
  - *The paper that defines FDT. Technical but readable. The core argument for why CDT fails for advanced AI.*
- **Stanford Encyclopedia of Philosophy — "Causal Decision Theory"**
  - https://plato.stanford.edu/entries/decision-causal/
  - Comprehensive philosophical treatment with full landscape of positions
- **LessWrong — "Newcomb's Problem and Regret of Rationality" by Eliezer Yudkowsky**
  - https://www.lesswrong.com/posts/6ddcsdA2c2XpNpE5x/newcomb-s-problem-and-regret-of-rationality
  - *The classic argument for why one-boxing is rational*

## 📖 Read — Secondary

- **"The Foundations of Causal Decision Theory" by James Joyce** — the definitive academic treatment of CDT
- **"Rationally Speaking" podcast episodes on Newcomb's Problem** — Julia Galef's accessible discussions
- **LessWrong Decision Theory FAQ** — community-maintained overview of the landscape
- **"Toward Idealized Decision Theory" by Nate Soares (MIRI)**
  - https://intelligence.org/files/TowardIdealizedDecisionTheory.pdf
  - How decision theory connects to building aligned AI agents

## 🔨 Do

- **Implement the Newcomb's simulation:** Create a predictor with 95% accuracy. Run 10,000 simulations for CDT agents (two-box) vs. FDT agents (one-box). Compare average payoffs. The FDT agents win decisively.
- **Expected utility calculator:** Build a tool that takes a decision matrix + probability distribution over states and computes the optimal action under each decision theory.
- **Parfit's Hitchhiker simulation:** Simulate the scenario with agents that can/can't make binding commitments. Show that agents capable of commitment (FDT-like) get rescued more often.

## 🔗 ML Connection

- **AI agents as decision-makers:** When an RL agent learns a policy, it's implicitly implementing a decision theory. Understanding which decision theory the agent converges to matters enormously for safety.
- **Precommitment and self-modification:** Can an AI commit to future actions? CDT agents are "dynamically inconsistent" — they make commitments they'll later break. FDT agents follow through. This matters for corrigibility.
- **Prediction and self-fulfilling prophecies:** In decision theory, the predictor models the agent. In ML, the training objective shapes the agent. The feedback loop between "what the agent does" and "what the environment expects" is structurally identical.

## 🧠 Alignment Connection

Decision theory is arguably the MOST important philosophical foundation for alignment:

1. **What decision theory should an aligned AI use?** If we build a CDT agent, it might defect in Prisoner's Dilemma-like situations with humans. An FDT agent cooperates when cooperation is mutual — which is closer to what we want.
2. **Corrigibility as a decision-theoretic property.** A corrigible AI allows itself to be shut down. Under CDT, a sufficiently intelligent AI has no causal reason to allow shutdown (it's already built). Under FDT, it might reason "the kind of AI that allows shutdown is the kind that gets built" — cooperating with its designers.
3. **The agent foundations agenda** at MIRI is essentially the project of building correct decision theory for AI systems. What should an AI agent do when it faces logical uncertainty, embedded agency, and self-reference?
4. **Utility function specification** is a core alignment challenge. Even with the "right" decision theory, the agent optimizes for its utility function — and specifying human values as a utility function is extraordinarily hard (Goodhart's Law, specification gaming, etc.).

---
[Next: Lesson 31 — Anthropics and Self-Locating Beliefs →](lesson-31-anthropics.md)
