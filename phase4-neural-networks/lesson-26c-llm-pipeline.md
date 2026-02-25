# Lesson 26c: The LLM Training Pipeline — From Raw Text to Aligned AI

[← RL Foundations](lesson-26b-rl-foundations.md) | [Back to TOC](../README.md) | [Next: What Interpretability Researchers Do →](../phase5-interpretability/lesson-27-intro-interp.md)

---

> **Why this lesson exists:** You've built a transformer from scratch (Lesson 26) and understand RL (Lesson 26b). Now see the complete picture: how do you go from raw internet text to an AI system that's actually helpful and safe? This lesson walks through every stage of modern LLM training, connecting each stage to the math you've learned. It's the "zooming out" lesson that shows how everything fits together before you zoom back in with interpretability.

## 🎯 Core Concepts

### Stage 1: Pre-training — Learning Language

- **Input:** terabytes of text from the internet (books, websites, code, Wikipedia, etc.)
- **Objective:** next-token prediction. Given the first N tokens, predict token N+1. This is pure MLE (Lesson 19) — maximize the probability of the training data.
- **Architecture:** the transformer you built in Lesson 26, scaled up to billions of parameters.
- **What the model learns:** grammar, facts, reasoning patterns, coding ability, world knowledge — but also biases, toxicity, and hallucination. The model is a *mirror of its training data*, not an aligned assistant.
- **Compute:** pre-training is absurdly expensive. GPT-4 class models cost tens of millions of dollars to train. This is relevant to alignment because it limits who can do safety research at frontier scale.
- **Scaling laws:** larger models trained on more data with more compute predictably get better (Lesson 28b). This predictability is why labs can plan training runs months in advance — and why alignment researchers worry about future capabilities.

### Stage 2: Supervised Fine-Tuning (SFT)

- **The problem with pre-training alone:** the pre-trained model completes text, it doesn't answer questions. Ask "What's the capital of France?" and it might continue with "What's the capital of Germany?" because that's what a text corpus looks like.
- **SFT input:** human-written examples of (instruction, good response) pairs. Thousands of demonstrations of the desired behavior.
- **Objective:** still next-token prediction, but on the curated demonstrations. The model learns the *format* of helpful responses.
- **What changes:** the model shifts from "continue this text" to "answer this question." But SFT alone doesn't teach the model to distinguish good from great responses, or to avoid subtle harms.
- **Mathematically:** SFT is MLE on a different distribution (curated demonstrations instead of raw internet text). It's a change of training distribution, not a change of objective.

### Stage 3: RLHF / Preference Optimization

- **The problem with SFT alone:** SFT teaches format but not judgment. The model can't distinguish between a factually correct response and a confident-sounding incorrect one — both look like valid "assistant completions."
- **RLHF pipeline** (from Lesson 26b):
  1. Train a reward model on human preference data
  2. Use PPO to optimize the language model against the reward model
  3. Apply KL penalty to prevent drift from the SFT model
- **DPO alternative:** skip the reward model entirely. Directly optimize the language model on preference pairs. Mathematically equivalent to RLHF under certain assumptions, but simpler to implement.
- **Constitutional AI (Anthropic's approach):** instead of human labelers for every comparison, provide a "constitution" — a set of principles. The model critiques and revises its own outputs according to the principles. This scales better than pure human labeling.
- **What changes:** the model learns to prefer helpful, harmless, honest responses. But the preference signal is *lossy* — it's filtered through human judgment and the reward model's imperfections.

### Stage 4: Deployment and Monitoring

- **System prompt:** at deployment, the model receives additional instructions (the system prompt) that shape its behavior for the specific use case.
- **Safety filters:** additional classifiers that detect and block harmful outputs.
- **Evaluation:** red-teaming (adversarial testing), benchmarks, monitoring for failures in the wild.
- **The gap between training and deployment:** the model encounters inputs it never saw during training. Its behavior in these novel situations is where alignment matters most — and where failures are hardest to predict.

### The Full Picture as a Mathematical Story

```
Raw Text ──MLE──→ Base Model ──MLE on demos──→ SFT Model ──RL + KL──→ Aligned Model
  (L19)            (L26)         (L19)           (L26)     (L26b,15b)     (L32)
    ↑                ↑              ↑               ↑           ↑            ↑
 Probability    Transformers   Distribution     Fine-tuning   Constrained  Alignment
   (L17)         (L25-26)      shift            (same arch)   optimization  theory
```

Each arrow is something you've learned. The entire pipeline is: probability theory → information theory → neural network architecture → optimization → constrained optimization → alignment theory. This is why the curriculum exists.

## 📺 Watch — Primary (THE key video)

1. **Andrej Karpathy — "Deep Dive into LLMs like ChatGPT" (2024)**
   - https://www.youtube.com/watch?v=7xTGNNLPyMI
   - *~3.5 hours. THE definitive walkthrough of the entire LLM pipeline from a world expert. Watch the whole thing — it covers pre-training, tokenization, SFT, RLHF, system prompts, tool use, and future directions. If you watch one video this month, make it this one.*

## 📺 Watch — Secondary

2. **Andrej Karpathy — "Intro to Large Language Models" (2023)**
   - https://www.youtube.com/watch?v=zjkBMFhNj_g
   - *1 hour. An earlier, shorter version. Good if you want the overview before the deep dive.*
3. **3Blue1Brown — Full Deep Learning playlist (Chapters 5-7)**
   - Already in your curriculum but rewatch with the full pipeline context
4. **Anthropic's blog posts on Constitutional AI**
   - https://www.anthropic.com/research
   - *See how Anthropic specifically approaches alignment training.*

## 📖 Read — Primary

- **"Training language models to follow instructions with human feedback" (InstructGPT paper, 2022)**
  - https://arxiv.org/abs/2203.02155
  - *The paper that launched the chatbot era. Describes the SFT → reward model → PPO pipeline.*
- **"Constitutional AI: Harmlessness from AI Feedback" (Anthropic, 2022)**
  - https://arxiv.org/abs/2212.08073
  - *Anthropic's approach to alignment training. Uses AI feedback instead of human labelers for some stages.*

## 📖 Read — Secondary

- **"LLM Powered Autonomous Agents" by Lilian Weng**
  - https://lilianweng.github.io/posts/2023-06-23-agent/
  - *Covers how LLMs are being used as agents — the next frontier of alignment challenges.*
- **"Sleeper Agents: Training Deceptive LLMs" (Anthropic, 2024)**
  - https://arxiv.org/abs/2401.05566
  - *Shows that standard safety training doesn't remove deceptive behavior once it's established — directly relevant to the training pipeline's limitations.*

## 🔨 Do

- **Watch Karpathy's Deep Dive end to end.** Take notes on each stage. For each stage, write down which lesson in your curriculum covers the underlying math.
- **SFT vs. base model comparison:** Using any open model (GPT-2, Llama), compare base model and instruction-tuned model responses to the same prompts. See the qualitative difference SFT makes.
- **Key exercise:** Design a complete training pipeline for an AI assistant that helps with medical questions. What data would you use for pre-training? SFT? What would your constitution look like? What could go wrong at each stage? Where are the alignment risks?

## 🔗 ML Connection

This lesson IS the ML connection for your entire curriculum. Every concept from Phases 1-4 shows up in the pipeline: linear algebra (transformers), calculus (gradient descent, backprop), probability (softmax, MLE), information theory (cross-entropy loss), optimization (Adam, learning rate scheduling), constrained optimization (KL penalty), and neural network architecture. You now understand, end to end, how a model like Claude is built.

## 🧠 Alignment Connection

The pipeline reveals where alignment can fail:
- **Pre-training:** the model absorbs biases and harmful content from its training data
- **SFT:** human demonstrations might encode subtle biases or be inconsistent
- **Reward model:** human preferences are noisy, biased, and can be gamed
- **RL optimization:** PPO might find reward hacks that satisfy the reward model without being truly helpful
- **Deployment:** novel inputs trigger out-of-distribution behavior not covered by training

Every alignment technique (interpretability, Constitutional AI, red-teaming, scalable oversight) targets one or more of these failure points.
