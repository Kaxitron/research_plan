# Lesson 28b: Scaling Laws, Emergent Capabilities, and Phase Transitions

[← Circuits](lesson-28-circuits.md) | [Back to TOC](../README.md) | [Next: Singular Learning Theory →](lesson-28c-slt.md)

---

> **Why this lesson exists:** The most important empirical fact in modern AI: when you make models bigger, they don't just get incrementally better — they *suddenly acquire new capabilities.* A model that can't do arithmetic at 1B parameters can do it at 10B. A model that can't reason about others' beliefs at 10B can do it at 100B. Understanding scaling laws and emergence is essential for alignment because it tells you when to expect dangerous capabilities and why "just test it" isn't sufficient for safety.

## 🎯 Core Concepts

### Scaling Laws — The Predictable Part

- **The core finding (Kaplan et al., 2020):** model performance (loss) follows a power law in three variables: model size N, dataset size D, and compute budget C. Specifically: L(N) ∝ N^(-α) for some exponent α. Double the parameters → predictable loss reduction.
- **Chinchilla scaling (Hoffmann et al., 2022):** the optimal ratio of model size to training data is roughly 1:20. A 70B model should be trained on ~1.4T tokens. Earlier models (like GPT-3) were *undertrained* — too big for their data. Chinchilla showed you get better results with a smaller model trained on more data.
- **Why power laws matter:** they let you *predict* how good a model will be before you train it. You can train small models cheaply, fit the scaling curve, and extrapolate. This is how labs plan multi-million-dollar training runs.
- **The bitter lesson (Rich Sutton):** historically, methods that leverage more compute beat methods based on clever engineering. Hand-crafted features lose to learned features. Expert systems lose to neural networks. The lesson: scale wins. This has profound implications for alignment — clever safety techniques might be outpaced by raw capability scaling.

### Emergent Capabilities — The Unpredictable Part

- **Emergence:** some capabilities appear *abruptly* at a certain scale. The model can't do the task at all below the threshold, then suddenly can. This is not predicted by smooth scaling laws — it's a qualitative phase transition.
- **Examples of emergent capabilities:**
  - Multi-step arithmetic (appears around 10B parameters)
  - Chain-of-thought reasoning (appears in 100B+ range)
  - Theory of mind / understanding others' beliefs
  - In-context learning with many examples
  - Code generation from natural language descriptions
- **Why this terrifies alignment researchers:** if dangerous capabilities (deception, power-seeking, situational awareness) emerge suddenly at some scale, we might not get advance warning. You can't test for a capability that doesn't exist in smaller models.
- **The phase transition metaphor:** like water freezing at 0°C. At 1°C, water is liquid. At -1°C, it's solid. The transition is sharp, not gradual. Models might be "safe" at one scale and "dangerous" at a slightly larger scale, with no smooth interpolation.

### Are Emergent Capabilities Real?

- **The counterargument (Schaeffer et al., 2023):** "emergence" might be a measurement artifact. If you measure accuracy on a binary task (right/wrong), you'll see a sharp jump. But if you measure log-probability (continuous), improvement is smooth. The capability was gradually improving all along — the metric made it look sudden.
- **Resolution:** both sides have a point. The underlying capability improves smoothly, but the *practical usefulness* often has a threshold. A model that gets 40% of math problems right is useless for math. At 90%, it's useful. The transition from "useless" to "useful" is sharp even if the underlying skill curve is smooth.
- **Why this matters for alignment:** even if capabilities improve smoothly in log-space, the *danger* threshold might be sharp. A model that's 40% good at deception is not dangerous. A model that's 90% good at deception is extremely dangerous. The practical transition is what matters.

### Grokking as a Phase Transition

- **Connection to Lesson 16:** grokking (sudden generalization after apparent overfitting) is a phase transition during training, not during scaling. It shows that the same sudden-emergence phenomenon happens in the time dimension too.
- **Developmental interpretability** studies these transitions: how do internal representations change at the moment a capability emerges? This connects scaling/emergence to the circuits work in Lesson 28 and to Singular Learning Theory (Lesson 28c).

## 📺 Watch — Primary

1. **Welch Labs — "Why Deep Learning Works Unreasonably Well"**
   - https://www.youtube.com/@WelchLabs
   - *Explains why overparameterized models generalize, connecting to double descent (Lesson 16) and scaling.*
2. **Andrej Karpathy — "Deep Dive into LLMs" (scaling laws section)**
   - https://www.youtube.com/watch?v=7xTGNNLPyMI
   - *Karpathy explains scaling laws with concrete numbers and graphs. If you watched this for Lesson 26c, re-watch the scaling section.*

## 📺 Watch — Secondary

3. **Yannic Kilcher — "Scaling Laws for Neural Language Models" (paper review)**
   - Search YouTube for "Yannic Kilcher scaling laws neural language models"
4. **Robert Miles — "AI Scaling and the Future"** (if available)
   - Search YouTube for "Robert Miles AI scaling"
5. **The Bitter Lesson by Rich Sutton (various presentations)**
   - http://www.incompleteideas.net/IncIdeas/BitterLesson.html (original essay)

## 📖 Read — Primary

- **"Scaling Laws for Neural Language Models" by Kaplan et al. (2020)**
  - https://arxiv.org/abs/2001.08361
  - *The foundational scaling laws paper. Readable and well-written.*
- **"Training Compute-Optimal Large Language Models" (Chinchilla paper)**
  - https://arxiv.org/abs/2203.15556
  - *Changed how labs think about the compute/data tradeoff.*
- **"The Bitter Lesson" by Rich Sutton**
  - http://www.incompleteideas.net/IncIdeas/BitterLesson.html
  - *One page. Essential reading for understanding the AI landscape.*

## 📖 Read — Secondary

- **"Are Emergent Abilities of Large Language Models a Mirage?" by Schaeffer et al. (2023)**
  - https://arxiv.org/abs/2304.15004
  - *The counterargument to sharp emergence. Read both sides.*
- **"Predictability and Surprise in Large Generative Models" (Ganguli et al., 2022)**
  - https://arxiv.org/abs/2202.07785
  - *Anthropic's take on what's predictable and what's not.*

## 🔨 Do

- **Plot scaling laws:** find published benchmark results for models of different sizes (GPT-2 124M → 774M → 1.5B, Llama 7B → 13B → 70B). Plot loss vs. parameters on a log-log scale. Verify the power law. Extrapolate: what loss would a 1T parameter model achieve?
- **Emergence simulation:** Create a simple task with a threshold (e.g., multi-digit addition). Train models of increasing size. Plot accuracy vs. size. See the sharp transition. Then plot log-probability and see it's smoother.
- **Key exercise:** You're advising a government on AI safety policy. Models below 100B parameters show no signs of deceptive behavior. Should you conclude models above 100B are also safe? Write up the argument using the concepts from this lesson.

## 🔗 ML Connection

Scaling laws inform every major decision in AI development: how much compute to buy, how much data to collect, when to expect new capabilities, and whether safety techniques that work at current scale will work at future scale. The answer to "will alignment keep up with capabilities?" depends critically on whether alignment insights scale as well as raw performance.

## 🧠 Alignment Connection

This is where alignment meets reality:
- **Predictable capabilities** (from scaling laws) can be prepared for
- **Unpredictable capabilities** (emergent/phase transitions) cannot — this is the core safety argument for caution
- **The alignment tax** interacts with scaling: if safety techniques slow training by 10%, and competitors skip them, competitive pressure pushes toward less safety
- **Developmental interpretability** (tracking how capabilities emerge during training) is a direct bridge between scaling/emergence and the circuits work from Lesson 28
