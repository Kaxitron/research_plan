# Lesson 20: Information Theory — Entropy, KL Divergence, Cross-Entropy, and Mutual Information

[← MLE](lesson-19-mle.md) | [Back to TOC](../README.md) | [Next: Bayesian Inference →](lesson-21-bayesian-inference.md)

---

> **Why this lesson exists:** Information theory is the mathematical language of "how much does this tell me about that?" Every loss function in language modeling is an information-theoretic quantity. KL divergence keeps RLHF models from drifting. Cross-entropy trains every LLM. Mutual information measures how much a hidden layer "knows" about the input or output — the core question of interpretability. Temperature controls the explore/exploit tradeoff in generation. This isn't abstract theory — it's the daily vocabulary of ML research.

## 🎯 Core Concepts

### Information Content — Surprise as a Number

- **Information content** of an event: I(x) = −log₂ P(x). The rarer an event, the more "information" it carries when it happens.
  - P = 1 (certain) → I = 0 bits (no surprise, you already knew)
  - P = 0.5 (coin flip) → I = 1 bit
  - P = 0.01 (rare) → I ≈ 6.6 bits (very surprising)
- **Why logarithm?** So information from independent events adds: I(x AND y) = I(x) + I(y) when x, y are independent. This matches our intuition that "two coin flips give 2 bits of information."
- **Bits vs. nats:** log₂ gives bits, ln gives nats. ML typically uses nats (natural log), which just differs by a constant factor.

### Entropy — Average Surprise

- **Entropy** of a distribution: H(X) = −Σ P(x) log P(x) = E[I(X)]. The average information content — how "surprising" samples from this distribution are, on average.
  - Uniform distribution over n outcomes: H = log₂(n) — maximum entropy. You have no idea what's coming next.
  - Peaked distribution (one outcome has P ≈ 1): H ≈ 0 — almost no surprise.
  - Fair coin: H = 1 bit. Loaded coin (90/10): H ≈ 0.47 bits. The loaded coin is less surprising.
- **Entropy as uncertainty:** H measures how uncertain you are about the outcome. Higher entropy = more uncertainty = harder to predict.
- **Maximum entropy principle:** given constraints (known mean, known variance), the distribution with maximum entropy is the "most uncertain" distribution consistent with those constraints. For fixed mean and variance → Gaussian. For bounded interval → uniform. This connects to Bayesian reasoning (Lesson 21): maximum entropy priors encode minimal assumptions.

### Cross-Entropy — Using the Wrong Code

- **Cross-entropy:** H(P, Q) = −Σ P(x) log Q(x). If the true distribution is P but you use distribution Q to encode/predict, cross-entropy measures the average number of bits needed.
- **Cross-entropy ≥ entropy:** H(P, Q) ≥ H(P), with equality iff P = Q. Using the "wrong" distribution always costs more bits. The extra cost is the KL divergence.
- **Cross-entropy as loss function:** when training a language model, P is the true distribution (one-hot: the correct next token) and Q is the model's predicted distribution (softmax output). Minimizing cross-entropy = making Q match P = making the model's predictions match reality.
- **The connection:** minimizing cross-entropy loss = maximizing likelihood (Lesson 19). They're the same thing viewed from different angles. Cross-entropy is the information theory lens; likelihood is the probability lens.

### KL Divergence — Distance Between Distributions

- **KL divergence:** D_KL(P || Q) = Σ P(x) log(P(x)/Q(x)) = H(P, Q) − H(P). The "extra surprise" from using Q when truth is P.
- **Properties:**
  - Always ≥ 0 (Gibbs' inequality)
  - = 0 iff P = Q
  - NOT symmetric: D_KL(P || Q) ≠ D_KL(Q || P) in general. It's not a true distance metric.
  - NOT satisfying triangle inequality
- **Forward vs. reverse KL:**
  - D_KL(P || Q) ("forward"): penalizes Q for putting low probability where P has high probability. Q is forced to cover all of P's mass. Result: Q tends to be broad, covering P.
  - D_KL(Q || P) ("reverse"): penalizes Q for putting high probability where P has low probability. Q avoids placing mass where P doesn't. Result: Q tends to be narrow, mode-seeking.
  - This asymmetry has practical consequences: variational inference minimizes reverse KL (mode-seeking), while MLE minimizes forward KL (mass-covering).
- **KL in RLHF:** during fine-tuning with human feedback, the loss includes a KL penalty: reward − β · D_KL(π_new || π_base). This prevents the model from drifting too far from the base model. Too high β = model barely changes. Too low β = model collapses to reward-hacking behavior. Finding the right β is a key alignment challenge.

### Mutual Information — The Core Measure of "How Much Does X Tell Me About Y?"

- **Mutual information:** I(X; Y) = H(X) − H(X|Y) = H(Y) − H(Y|X) = H(X) + H(Y) − H(X, Y). The amount by which knowing Y reduces your uncertainty about X (and vice versa — it's symmetric!).
- **The geometric picture (Venn diagram):** think of H(X) as a circle and H(Y) as another circle. Their overlap is I(X; Y) — the shared information. H(X|Y) is the part of X's entropy not explained by Y. H(X, Y) is the total area of both circles together.

  ```
  ┌──────────────────────────────────────┐
  │  H(X,Y) = total joint entropy       │
  │  ┌─────────────┐ ┌─────────────┐    │
  │  │   H(X|Y)    │▓│   H(Y|X)    │    │
  │  │  (X's info  │▓│  (Y's info  │    │
  │  │  NOT in Y)  │▓│  NOT in X)  │    │
  │  └─────────────┘ └─────────────┘    │
  │                 ▓▓▓                  │
  │               I(X;Y)                │
  │         (shared information)         │
  └──────────────────────────────────────┘
  ```

- **Properties:**
  - I(X; Y) ≥ 0 always (knowing Y can never increase uncertainty about X)
  - I(X; Y) = 0 iff X and Y are independent (knowing Y tells you nothing about X)
  - I(X; Y) = H(X) iff X is a deterministic function of Y (Y tells you everything about X)
  - Unlike KL divergence, mutual information IS symmetric: I(X; Y) = I(Y; X)
- **Conditional mutual information:** I(X; Y | Z) = H(X|Z) − H(X|Y,Z). How much does Y tell you about X, given that you already know Z. This appears in information-theoretic analyses of neural network layers.

### The Information Bottleneck — What Networks Learn

- **The information bottleneck principle (Tishby et al., 2000):** a good representation T of input X for predicting output Y should maximize I(T; Y) while minimizing I(T; X). In English: keep the information relevant to the task, throw away everything else.
- **For neural networks:** at each layer l with representation T_l, you can measure I(T_l; X) (how much the layer remembers about the input) and I(T_l; Y) (how much the layer knows about the output). The claim: during training, layers first memorize (increase I(T; X)) then compress (decrease I(T; X) while keeping I(T; Y) high).
- **The information plane:** plot I(T_l; X) vs I(T_l; Y) for each layer l. As training progresses, layers trace paths through this plane. Deep networks show a "fitting phase" (moving right — more input information) followed by a "compression phase" (moving left — discarding irrelevant input information).
- **Controversy:** the information bottleneck theory for deep learning is actively debated. Some results depend on activation functions (it may not apply to ReLU networks in the same way), and estimation of mutual information in high dimensions is notoriously difficult. But the framework is influential and gives useful intuition.
- **Why this matters for alignment:** the information bottleneck perspective asks: what does the model *remember* vs. *forget* about its input? A model that "remembers" private user data when it shouldn't → privacy violation. A model that "forgets" important context → capability failure. Understanding information flow through layers is central to both alignment and interpretability.

### Mutual Information in Practice

- **Probing as MI estimation:** when interpretability researchers train a linear probe to predict property P from layer l's activations, they're estimating a lower bound on I(T_l; P). If the probe achieves high accuracy, the layer contains substantial information about P.
- **Feature importance:** mutual information I(feature; output) measures how important a feature is for prediction. This is more principled than correlation because MI captures nonlinear relationships.
- **Privacy and differential privacy:** information-theoretic bounds on how much a model's outputs reveal about its training data use mutual information. I(output; training_example) bounds the privacy leakage.
- **Representational similarity analysis:** comparing representations across models or layers often uses mutual information. Two layers with high I(T_l; T_l') represent similar information even if their activation patterns look different.

### Temperature in Softmax

- **Softmax temperature τ:** softmax(z/τ) where z is the logit vector.
  - τ → 0: distribution becomes one-hot (greedy, zero entropy) — the model always picks its top prediction
  - τ = 1: standard softmax (the model's actual learned distribution)
  - τ → ∞: distribution approaches uniform (maximum entropy) — completely random
- **Temperature as information control:** higher temperature = more entropy = more diversity/randomness in outputs. Lower temperature = less entropy = more focused/deterministic.
- **Distillation:** training a smaller "student" model to match a larger "teacher" model's outputs uses a high temperature to soften the teacher's predictions, revealing more information about the teacher's knowledge (its second-best guess, etc.) than the hard predictions would.

## 📺 Watch — Primary

1. **Aurélien Géron — "A Short Introduction to Entropy, Cross-Entropy and KL-Divergence"** (YouTube)
   - Clear 15-minute overview with good visualizations
2. **Luis Serrano — "A Friendly Introduction to Cross-Entropy Loss"** (YouTube)
   - Builds from information theory to the loss function step by step
3. **StatQuest — "Mutual Information, Clearly Explained"** (YouTube)
   - https://www.youtube.com/c/joshstarmer
   - Good intuition for MI with visual examples

## 📺 Watch — Secondary

4. **3Blue1Brown — "Information Theory" (if available)**
   - Visual treatment of entropy and information
5. **Naftali Tishby — "Information Theory of Deep Learning"** (YouTube talks)
   - Search for Tishby's talks at various conferences — the originator of the information bottleneck theory for deep learning. Controversial but stimulating.
6. **Chris Olah — presentations on information flow in networks** (if available)

## 📖 Read — Primary

- **colah's blog — "Visual Information Theory"**
  - http://colah.github.io/posts/2015-09-Visual-Information/
  - *Gorgeous visual explanations of entropy, cross-entropy, KL divergence. The best intuitive treatment available.*
- **"Deep Learning" by Goodfellow et al., Chapter 3.13** — information theory section
  - https://www.deeplearningbook.org/
  - Concise, formal treatment with ML context
- **"Elements of Information Theory" by Cover & Thomas** — Chapters 1–2 (entropy, mutual information basics)
  - *The gold standard textbook for information theory. Chapters 1-2 give you the core. Chapter 2's treatment of mutual information is definitive.*

## 📖 Read — Secondary

- **"Deep Learning and the Information Bottleneck Principle" by Tishby & Zaslavsky (2015)**
  - https://arxiv.org/abs/1503.02406
  - *The paper that launched the information bottleneck interpretation of deep learning.*
- **"On the Information Bottleneck Theory of Deep Learning" by Saxe et al. (2018)**
  - https://openreview.net/forum?id=ry_WPG-A-
  - *The critique — argues the compression phase depends on activation functions and may not be universal. Read both sides.*
- **"Opening the Black Box of Deep Neural Networks via Information" by Shwartz-Ziv & Tishby (2017)**
  - https://arxiv.org/abs/1703.00810
  - The information plane visualizations that started the debate

## 📖 Read — Going Deep

- **"Estimating Mutual Information" by Belghazi et al. (MINE, 2018)**
  - https://arxiv.org/abs/1801.04062
  - How to estimate MI in high dimensions using neural networks — connects information theory to deep learning practice
- **"The Information Lattice" (various treatments)**
  - Lattice-theoretic view of how information decomposes across variables. Advanced but clarifying.

## 🔨 Do

- **Entropy of distributions:** compute entropy of: uniform over {1,...,n} for n = 2, 4, 8, 16; Bernoulli(p) for p = 0.01, 0.1, 0.5, 0.9, 0.99; a custom bimodal distribution. Plot H vs. p for Bernoulli. Verify maximum at p = 0.5.
- **KL divergence exploration:** for two Gaussians with different means and variances, compute D_KL(P || Q) and D_KL(Q || P). Visualize both distributions and see how the asymmetry relates to where the distributions differ.
- **Cross-entropy loss implementation:** implement cross-entropy loss from scratch. Train a simple classifier. Show that as model predictions approach the true distribution, cross-entropy decreases toward entropy.
- **Mutual information estimation:** generate 2D data where X and Y have known mutual information (e.g., jointly Gaussian with correlation ρ, where I(X;Y) = -0.5 log(1-ρ²)). Estimate MI using: (a) the analytic formula, (b) binning/histogram method, (c) k-nearest-neighbors estimator. See how estimation difficulty increases with dimension.
- **Information plane (advanced):** train a small MLP on a classification task. After each epoch, estimate I(T_l; X) and I(T_l; Y) for each hidden layer l using a probe or binning method. Plot layers' trajectories in the information plane. Do you see compression?
- **Temperature experiment:** take a pre-trained language model (even a simple one). Generate text at temperatures τ = 0.1, 0.5, 1.0, 1.5, 2.0. Compute the entropy of the output distributions at each temperature. See the diversity-coherence tradeoff.
- **Key exercise:** explain why minimizing cross-entropy H(P, Q) is the same as minimizing D_KL(P || Q) when P is fixed (the true data distribution). Then explain: in RLHF, the KL penalty D_KL(π_new || π_base) prevents the model from "collapsing" to always saying what gets rewarded. What would happen without the KL penalty? Why is this an information-theoretic alignment mechanism?

## 🔗 ML Connection

- **Cross-entropy is THE loss function** for language modeling, classification, and most discrete prediction tasks. Understanding it information-theoretically (not just as "a formula to minimize") gives you intuition for why models behave as they do.
- **KL divergence in RLHF** keeps the fine-tuned model from drifting too far from the base model. This is an information-theoretic constraint on alignment.
- **KL divergence in VAEs:** the ELBO (Evidence Lower Bound) includes a KL term that regularizes the latent space toward a prior distribution.
- **Mutual information in probing:** interpretability researchers use probing accuracy (a proxy for MI) to measure what information is encoded in each layer.
- **Temperature** controls creative vs. focused outputs and is used in distillation, calibration, and generation.
- **Information bottleneck** provides a theoretical framework for understanding what neural networks learn to encode at each layer — central to both capabilities and interpretability research.

## 🧠 Alignment Connection

Information theory provides the quantitative language for key alignment questions:

- **"How much does the model know about X?"** is a mutual information question: I(model_state; X). For X = "user's private data," this is a privacy question. For X = "the correct answer," this is a capability question. For X = "its own training process," this is a deceptive alignment question.
- **KL penalties in RLHF** are an alignment mechanism. Too little KL constraint → reward hacking (model says whatever gets high reward). Too much → model barely changes from pre-training. The information-theoretic view clarifies this tradeoff.
- **Information flow through layers** determines what the model "remembers" and "forgets." A model that retains information about "how to appear aligned" across many layers is more concerning than one where that information is quickly compressed away.
- **Eliciting Latent Knowledge (ELK):** the question "does the model know something it's not telling us?" is I(model_internals; truth) vs. I(model_output; truth). If the internal MI is much higher than the output MI, the model is withholding information — exactly the ELK problem.
