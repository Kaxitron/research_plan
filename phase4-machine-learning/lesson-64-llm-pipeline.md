# Lesson 64: The LLM Training Pipeline

[< RL Foundations](lesson-63-rl-foundations.md) | [Back to TOC](../README.md) | [Next: Interpretability -- Circuits >](lesson-65-interp-circuits.md)

---

> **Karpathy framing:** Karpathy's "Deep Dive into LLMs" is THE definitive walkthrough of the entire pipeline -- pre-training, tokenization, SFT, RLHF, system prompts, tool use, and future directions. His tokenization lecture (Zero to Hero #8) goes deep on BPE, the preprocessing step that determines what a model can even see.

> **Why this lesson exists:** You've built a transformer from scratch and understand RL. Now see the complete picture: how do you go from raw internet text to an AI system that's actually helpful and safe? This lesson walks through every stage of modern LLM training, connecting each stage to the math you've learned.

## Core Concepts

### Tokenization (BPE)

- **Byte Pair Encoding (BPE):** the dominant tokenization algorithm. Start with individual bytes, iteratively merge the most frequent adjacent pair into a new token. Repeat until you reach the desired vocabulary size.
- **Why tokenization matters:** the tokenizer determines the model's "alphabet." Different tokenizers produce different token sequences for the same text. Tokenization artifacts (e.g., splitting numbers inconsistently) explain many LLM failure modes.
- **The tokenizer is trained separately** from the model, on a large text corpus. It's a fixed preprocessing step -- the model never changes it.

### Stage 1: Pre-training -- Learning Language

- **Input:** terabytes of text from the internet (books, websites, code, Wikipedia, etc.)
- **Objective:** next-token prediction. Given the first N tokens, predict token N+1. This is pure MLE -- maximize the probability of the training data.
- **Architecture:** the transformer, scaled up to billions of parameters.
- **What the model learns:** grammar, facts, reasoning patterns, coding ability, world knowledge -- but also biases, toxicity, and hallucination. The model is a *mirror of its training data*, not an aligned assistant.
- **Compute:** pre-training is absurdly expensive. GPT-5 class models cost tens of millions of dollars to train.
- **Chinchilla scaling:** the optimal ratio of model size to training data is roughly 1:20. A 70B model should be trained on ~1.4T tokens.
- **The bitter lesson (Rich Sutton):** historically, methods that leverage more compute beat methods based on clever engineering. Scale wins. This has profound implications for alignment.

### Stage 2: Supervised Fine-Tuning (SFT)

- **The problem with pre-training alone:** the pre-trained model completes text, it doesn't answer questions. Ask "What's the capital of France?" and it might continue with "What's the capital of Germany?" because that's what a text corpus looks like.
- **SFT input:** human-written examples of (instruction, good response) pairs. Thousands of demonstrations of the desired behavior.
- **Objective:** still next-token prediction, but on the curated demonstrations. The model learns the *format* of helpful responses.
- **Mathematically:** SFT is MLE on a different distribution (curated demonstrations instead of raw internet text). It's a change of training distribution, not a change of objective.

### Stage 3: RLHF / Preference Optimization

- **The problem with SFT alone:** SFT teaches format but not judgment. The model can't distinguish between a factually correct response and a confident-sounding incorrect one.
- **RLHF pipeline** (from Lesson 50):
  1. Train a reward model on human preference data
  2. Use PPO to optimize the language model against the reward model
  3. Apply KL penalty to prevent drift from the SFT model
- **DPO alternative:** skip the reward model entirely. Directly optimize the language model on preference pairs. Mathematically equivalent to RLHF under certain assumptions, but simpler to implement.
- **Constitutional AI (Anthropic's approach):** instead of human labelers for every comparison, provide a "constitution" -- a set of principles. The model critiques and revises its own outputs according to the principles. This scales better than pure human labeling.

### Stage 4: Deployment and Monitoring

- **System prompt:** at deployment, the model receives additional instructions that shape its behavior for the specific use case.
- **Safety filters:** additional classifiers that detect and block harmful outputs.
- **Evaluation:** red-teaming (adversarial testing), benchmarks, monitoring for failures in the wild.
- **The gap between training and deployment:** the model encounters inputs it never saw during training. Its behavior in these novel situations is where alignment matters most.

### The Full Picture as a Mathematical Story

```
Raw Text --MLE--> Base Model --MLE on demos--> SFT Model --RL + KL--> Aligned Model
```

Each arrow is something you've learned. The entire pipeline is: probability theory, information theory, neural network architecture, optimization, constrained optimization, alignment theory. This is why the curriculum exists.

## Watch -- Primary (THE key videos)

1. **Andrej Karpathy -- "Deep Dive into LLMs like ChatGPT" (2024)**
   - https://www.youtube.com/watch?v=7xTGNNLPyMI
   - *~3.5 hours. THE definitive walkthrough of the entire LLM pipeline from a world expert. Watch the whole thing -- it covers pre-training, tokenization, SFT, RLHF, system prompts, tool use, and future directions. If you watch one video this month, make it this one.*

2. **Andrej Karpathy -- "Let's build the GPT Tokenizer" (Zero to Hero #8)**
   - https://www.youtube.com/watch?v=zduSFxRajkE
   - *Deep dive into BPE tokenization -- the preprocessing step that determines what a model can even see. You implement a tokenizer from scratch.*

## Watch -- Secondary

3. **Andrej Karpathy -- "Intro to Large Language Models" (2023)**
   - https://www.youtube.com/watch?v=zjkBMFhNj_g
   - *1 hour. An earlier, shorter version. Good if you want the overview before the deep dive.*
4. **3Blue1Brown -- Full Deep Learning playlist (Chapters 5-7)**
   - Already in your curriculum but rewatch with the full pipeline context
5. **Anthropic's blog posts on Constitutional AI**
   - https://www.anthropic.com/research
   - *See how Anthropic specifically approaches alignment training.*

## Read -- Primary

- **"Training language models to follow instructions with human feedback" (InstructGPT paper, 2022)**
  - https://arxiv.org/abs/2203.02155
  - *The paper that launched the chatbot era. Describes the SFT, reward model, PPO pipeline.*
- **"Constitutional AI: Harmlessness from AI Feedback" (Anthropic, 2022)**
  - https://arxiv.org/abs/2212.08073
  - *Anthropic's approach to alignment training. Uses AI feedback instead of human labelers for some stages.*

## Read -- Secondary

- **"LLM Powered Autonomous Agents" by Lilian Weng**
  - https://lilianweng.github.io/posts/2023-06-23-agent/
  - *Covers how LLMs are being used as agents -- the next frontier of alignment challenges.*
- **"Sleeper Agents: Training Deceptive LLMs" (Anthropic, 2024)**
  - https://arxiv.org/abs/2401.05566
  - *Shows that standard safety training doesn't remove deceptive behavior once it's established -- directly relevant to the training pipeline's limitations.*

## Do

- **Watch Karpathy's Deep Dive end to end.** Take notes on each stage. For each stage, write down which lesson in your curriculum covers the underlying math.
- **Implement BPE tokenization from scratch** following Karpathy's Zero to Hero #8. Train it on a small corpus and examine the learned vocabulary.
- **SFT vs. base model comparison:** Using any open model (GPT-2, Llama), compare base model and instruction-tuned model responses to the same prompts. See the qualitative difference SFT makes.
- **Key exercise:** Design a complete training pipeline for an AI assistant that helps with medical questions. What data would you use for pre-training? SFT? What would your constitution look like? What could go wrong at each stage? Where are the alignment risks?

## ML and Alignment Connection

This lesson IS the ML connection for your entire curriculum. Every concept from earlier phases shows up in the pipeline: linear algebra (transformers), calculus (gradient descent, backprop), probability (softmax, MLE), information theory (cross-entropy loss), optimization (Adam, learning rate scheduling), constrained optimization (KL penalty), and neural network architecture. You now understand, end to end, how a model like Claude is built.

The pipeline reveals where alignment can fail:
- **Pre-training:** the model absorbs biases and harmful content from its training data
- **SFT:** human demonstrations might encode subtle biases or be inconsistent
- **Reward model:** human preferences are noisy, biased, and can be gamed
- **RL optimization:** PPO might find reward hacks that satisfy the reward model without being truly helpful
- **Deployment:** novel inputs trigger out-of-distribution behavior not covered by training

Every alignment technique (interpretability, Constitutional AI, red-teaming, scalable oversight) targets one or more of these failure points.

---

## Time to Take the Exam

You can now trace the complete path from a single neuron through transformers to the full LLM training pipeline. Time to demonstrate that understanding.

**[Exam 4A: Neural Networks & ML](../assessments/exam-4a-neural-networks.md)**
