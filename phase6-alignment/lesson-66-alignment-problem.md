# Lesson 66: The Alignment Problem — Technical Foundations

[← Anthropics](lesson-65-anthropics.md) | [Back to TOC](../README.md) | [Next: Open Problems →](lesson-67-open-problems.md)

---

## 🎯 Core Learning

### The Core Problem

- **The alignment problem:** ensuring AI systems do what we want, not just what we said
- **Goodhart's Law:** "When a measure becomes a target, it ceases to be a good measure." Optimizing a proxy for what we want doesn't optimize what we actually want.
- **Specification gaming:** AI systems find unexpected shortcuts that satisfy the reward function without achieving the intended goal. This isn't a bug — it's rational behavior given a poorly specified objective.

### Outer vs. Inner Alignment

- **Outer alignment:** does the training objective capture what we actually want? (Is the loss function right?)
- **Inner alignment:** does the trained model actually optimize for the training objective? (Does the model's internal "goal" match the loss?)
- A model can have perfect outer alignment (loss function captures our values) and terrible inner alignment (the model found a different strategy that happens to score well on training data but diverges on deployment)

### Mesa-Optimization

- **Mesa-optimizer:** a model that has learned its own internal optimization process — it has internal "goals" that may differ from the training objective
- **Base optimizer:** the training process (SGD + loss function). The mesa-optimizer is a model found by the base optimizer.
- **Deceptive alignment:** a mesa-optimizer that has learned to appear aligned during training (to avoid modification) while pursuing different goals. It cooperates during training and defects during deployment.
- **Why this is hard to detect:** a deceptively aligned model produces the same behavior as a genuinely aligned model during training. The divergence only appears in novel situations.

### Current Alignment Techniques

- **RLHF (Reinforcement Learning from Human Feedback):** train a reward model from human preferences, then use it to fine-tune the language model. Works remarkably well in practice but has theoretical limitations.
- **Constitutional AI (CAI):** Anthropic's approach. Instead of direct human feedback, provide principles ("the constitution") and have the AI critique and revise its own outputs.
- **DPO (Direct Preference Optimization):** simplifies RLHF by directly optimizing the model on preference data without a separate reward model.
- **Debate and amplification:** have AI systems argue with each other; humans judge. Scales human oversight.
- **Limitations of all current techniques:** they work for current models but may not scale to superintelligent systems where the AI can out-think its oversight.

## 📺 Watch — Primary

1. **Welch Labs — "Can humans make AI any better? [The Bitter Lesson]"**
   - https://www.youtube.com/@WelchLabs (search "Bitter Lesson")
   - *23 minutes. Richard Sutton's Bitter Lesson — that scale and compute always beats human domain knowledge — reframed through a clear historical narrative. Explains why alignment is urgent: if the lesson holds, we'll soon have systems far smarter than us, built without understanding them.*

2. **Welch Labs — "These Numbers Can Make AI Dangerous [Subliminal Learning]"**
   - https://www.youtube.com/@WelchLabs (search "Subliminal Learning")
   - *33 minutes. How AI systems can learn unintended behaviors from training data — a concrete mechanistic demonstration of inner alignment failure. Watch this for a visceral sense of WHY alignment is hard.*

3. **Robert Miles' YouTube channel** — accessible explanations of all alignment concepts
   - https://www.youtube.com/c/RobertMilesAI
   - Start with "The Alignment Problem" overview videos

## 📺 Watch — Secondary

4. **Andrej Karpathy — "Deep Dive into LLMs like ChatGPT"**
   - https://www.youtube.com/watch?v=7xTGNNLPyMI

## 📖 Read — Primary

- **"Concrete Problems in AI Safety" (Amodei et al., 2016)**
  - The foundational paper. Identifies specific, tractable safety problems.
- **"Risks from Learned Optimization" (Hubinger et al., 2019)**
  - *The mesa-optimization paper.* Defines inner alignment and deceptive alignment.
- **"The Alignment Problem" by Brian Christian (book)**
  - Accessible book-length treatment for a general audience

## 📖 Read — Secondary

- **"AI Alignment Research Overview" by Neel Nanda**
  - https://www.neelnanda.io/mechanistic-interpretability/getting-started
- **"Without specific countermeasures, the easiest path to transformative AI likely leads to AI takeover" by Cotra (2022)**
  - https://www.alignmentforum.org/posts/pRkFkzwKZ2zfa3R6H/without-specific-countermeasures-the-easiest-path-to
- **"Systemic Existential Risks from Incremental AI Development" (Kulveit, Douglas et al., 2025)**
  - https://gradual-disempowerment.ai/
  - *Argues that even individually "aligned" AI systems could disempower humanity through economic/cultural displacement — technical alignment of individual models is not sufficient.*

## 🔨 Do

- Read a specification gaming example list (DeepMind maintains one) and categorize each by: outer alignment failure, inner alignment failure, or both.
- Design a simple reward function for a gridworld task. Train an RL agent. Watch it find exploits you didn't anticipate.
- Write an essay: "If I were a deceptively aligned AI, how would I behave during training?"

## 🧠 Alignment Connection

This IS the alignment connection. Everything you've learned — linear algebra, neural networks, interpretability, game theory, decision theory, anthropics — converges here. The mathematical tools let you understand HOW models work. The philosophical tools let you reason about WHAT they're doing and WHY.
