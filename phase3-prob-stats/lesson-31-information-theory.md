# Lesson 31: Information Theory — Entropy, KL Divergence, Cross-Entropy, and Mutual Information

[← MLE](lesson-30-mle.md) | [Back to TOC](../README.md) | [Next: Hypothesis Testing →](lesson-32-hypothesis-testing.md)

---

> **Why this lesson exists:** Information theory is the mathematical language of uncertainty, compression, and communication — and it turns out to be the mathematical language of neural network training. The loss function for language models IS cross-entropy. The penalty that keeps RLHF from going off the rails IS KL divergence. Temperature in sampling IS an information-theoretic parameter. And mutual information — how much knowing one thing tells you about another — is the key to formalizing what a neural network layer "knows" about its input. Every concept in this lesson has a direct, operational role in modern ML.

## 🎯 Core Concepts

### Information Content and Entropy

- **Information content** of an event: I(x) = -log₂ P(x). Rare events carry more information. Guaranteed events carry zero information. If something happens with probability 1/8, learning it happened gives you 3 bits of information.
  - **Intuition:** information is "surprise." Learning that a coin landed heads (P = 0.5) gives 1 bit. Learning that a specific card was drawn from a deck (P = 1/52) gives ~5.7 bits. Learning that the sun rose (P ≈ 1) gives ~0 bits.

- **Entropy:** H(X) = -Σ P(x) log P(x) = E[I(X)]. The *average* surprise of a distribution. It measures how uncertain you are before observing the outcome.
  - **Uniform distribution** has maximum entropy: every outcome is equally surprising. A fair coin has H = 1 bit. A fair 6-sided die has H ≈ 2.58 bits.
  - **Peaked distribution** has low entropy: you can predict the outcome. A biased coin with P(heads) = 0.99 has H ≈ 0.08 bits.
  - **Entropy as compression:** H(X) is the minimum average number of bits needed to encode samples from X. You literally cannot compress below the entropy — Shannon's source coding theorem proves this.

### Cross-Entropy and KL Divergence

- **Cross-entropy:** H(P, Q) = -Σ P(x) log Q(x). The average number of bits needed to encode events from the *true* distribution P using an encoding optimized for distribution Q.
  - If Q = P, cross-entropy equals entropy (optimal encoding).
  - If Q ≠ P, cross-entropy is always *larger* than entropy — you're wasting bits because your encoding doesn't match reality.
  - **THIS is the language model loss function.** P is the true next-token distribution, Q is the model's predicted distribution. Minimizing cross-entropy = making Q match P = making the model's predictions match reality.

- **KL divergence:** D_KL(P || Q) = H(P, Q) - H(P) = Σ P(x) log [P(x)/Q(x)]. The "extra bits" wasted by using Q instead of P. Always ≥ 0 (Gibbs' inequality). Zero if and only if P = Q.
  - **Not a true distance:** D_KL(P || Q) ≠ D_KL(Q || P) in general. It's asymmetric.
  - **Forward KL** D_KL(P || Q): penalizes Q for assigning low probability where P is high. Forces Q to "cover" P. Tends to produce overdispersed approximations.
  - **Reverse KL** D_KL(Q || P): penalizes Q for assigning high probability where P is low. Forces Q to "fit inside" P. Tends to produce mode-seeking approximations.
  - **Cross-entropy = entropy + KL divergence:** H(P, Q) = H(P) + D_KL(P || Q). Since H(P) is a constant (the true distribution doesn't change), minimizing cross-entropy is equivalent to minimizing KL divergence. They're the same optimization.

### Temperature — Sharpening and Flattening

- **Temperature in softmax:** instead of softmax(z), use softmax(z/T) where T is the temperature parameter.
  - T < 1: sharper distribution (more confident, less diverse). As T → 0, becomes argmax (greedy).
  - T > 1: flatter distribution (less confident, more diverse). As T → ∞, becomes uniform.
  - T = 1: the "native" distribution learned by the model.
- **Information-theoretic interpretation:** temperature controls the entropy of the output distribution. Low temperature = low entropy = predictable. High temperature = high entropy = creative/random.
- **In RLHF:** temperature scaling is used in the KL penalty to control how far the fine-tuned model can drift from the base model.

### Mutual Information — What Does X Tell You About Y?

- **Mutual information:** I(X; Y) = H(X) - H(X|Y) = H(Y) - H(Y|X) = H(X) + H(Y) - H(X, Y).
  - **In words:** how much does knowing Y reduce your uncertainty about X? (Or equivalently, how much does knowing X reduce your uncertainty about Y? — it's symmetric.)
  - **I(X; Y) = 0** means X and Y are independent — knowing one tells you nothing about the other.
  - **I(X; Y) = H(X)** means Y completely determines X — no uncertainty remains.

- **The Venn diagram picture:** think of H(X) and H(Y) as two overlapping circles. The overlap is I(X; Y). The non-overlapping parts are H(X|Y) and H(Y|X) (the uncertainty that remains after observing the other variable). H(X, Y) is the total area of both circles.

- **Conditional mutual information:** I(X; Y | Z) = H(X|Z) - H(X|Y,Z). How much Y tells you about X *beyond what Z already tells you.* Essential for understanding what each layer of a network contributes.

- **Data Processing Inequality:** if X → Y → Z forms a Markov chain (Z depends on X only through Y), then I(X; Z) ≤ I(X; Y). Processing data can only lose information, never create it.
  - **For neural networks:** as data passes through layers, each layer can lose information about the input but never gain it. The residual stream's skip connections are crucial because they allow information to bypass lossy transformations.

### The Information Bottleneck

- **The information bottleneck principle** (Tishby et al.): a good internal representation T of input X should:
  1. **Compress:** minimize I(X; T) — the representation should be compact, discarding irrelevant details.
  2. **Preserve:** maximize I(T; Y) — the representation should retain everything relevant to the output Y.
  - The optimal tradeoff between compression and preservation defines the "information curve."

- **The information bottleneck in deep learning:** one hypothesis (Shwartz-Ziv & Tishby, 2017) is that neural networks learn in two phases:
  1. **Fitting phase:** I(T; Y) increases rapidly (the network learns to predict correctly).
  2. **Compression phase:** I(X; T) decreases (the network learns to discard irrelevant input features).
  - This is controversial — it may depend on activation functions and architecture. But the framework is influential.

- **Why this matters for interpretability:** when you ask "what does this layer know about the input?" you're asking about I(X; T_layer). When you ask "what does this layer know about the output?" you're asking about I(T_layer; Y). Mutual information formalizes the questions that interpretability researchers ask informally.

### Pointwise Mutual Information (PMI)

- **PMI(x, y) = log [P(x, y) / (P(x) P(y))]** — how much more likely x and y are to co-occur than if they were independent.
  - PMI > 0: x and y co-occur more than expected (positive association).
  - PMI = 0: independent.
  - PMI < 0: they co-occur less than expected (negative association).
- **Mutual information is the expected PMI:** I(X; Y) = E[PMI(X, Y)].
- **In NLP:** PMI between words is a classical measure of word association. Word2Vec's skip-gram with negative sampling implicitly factorizes a PMI matrix. The connection between information theory and word embeddings runs deep.

## 📺 Watch — Primary

1. **Aurélien Géron — "A Short Introduction to Entropy, Cross-Entropy and KL-Divergence"** (YouTube)
   - Clear, visual explanation of the core trio
2. **Luis Serrano — "A Friendly Introduction to Cross-Entropy Loss"** (YouTube)
   - Builds intuition for why cross-entropy is the right loss function
3. **3Blue1Brown — "Wordle and Information Theory"**
   - https://www.youtube.com/watch?v=v68zYyaEmEA
   - *Applies information theory to a concrete game. Excellent for building entropy intuition.*

## 📺 Watch — Secondary

4. **StatQuest — "Entropy (for Data Science)"**
   - https://www.youtube.com/watch?v=YtebGVx-Fxw
5. **Mutual Information (YouTube) — "Mutual Information" channel**
   - Multiple videos on MI, KL divergence, and applications
6. **Tishby — "Information Theory of Deep Learning"** (talk recordings)
   - Search YouTube — Naftali Tishby presents the information bottleneck theory for deep learning

## 📖 Read — Primary

- **colah's blog — "Visual Information Theory"**
  - http://colah.github.io/posts/2015-09-Visual-Information/
  - *Gorgeous visual explanations. THE best introduction to entropy, cross-entropy, and KL divergence.*
- **"Deep Learning" by Goodfellow et al., Chapter 3** — information theory section
  - https://www.deeplearningbook.org/
  - Formal treatment with ML focus

## 📖 Read — Secondary

- **"Elements of Information Theory" by Cover & Thomas** — Chapters 1-2
  - The standard textbook. Chapters 1-3 cover entropy, mutual information, and the data processing inequality rigorously.
- **"Opening the Black Box of Deep Neural Networks via Information" (Shwartz-Ziv & Tishby, 2017)**
  - https://arxiv.org/abs/1703.00810
  - The information bottleneck paper for deep learning. Controversial but influential.
- **"Information Flow in Deep Neural Networks" (various papers)**
  - Search for recent work on tracking mutual information through network layers

## 📖 Read — Going Deep

- **"The Information Bottleneck Method" by Tishby, Pereira, and Bialek (1999)**
  - https://arxiv.org/abs/physics/0004057
  - The original information bottleneck paper
- **"On the Information Plane of Autoencoders" and related work**
  - More recent empirical investigation of information flow in networks

## 🔨 Do

- **Entropy calculator:** compute entropy of various distributions (uniform over 2/4/8/100 outcomes, biased coin with P = 0.1/0.5/0.9, natural language character frequencies). Plot entropy vs. bias for a coin — see the inverted U shape (maximum at P = 0.5).
- **Cross-entropy loss from scratch:** implement cross-entropy loss for a softmax classifier. Train on a simple dataset. Show that as predictions improve, cross-entropy decreases toward the entropy of the true distribution.
- **KL divergence visualization:** take two Gaussians with different means/variances. Compute D_KL(P||Q) and D_KL(Q||P). See the asymmetry. Plot the "information landscape" — at each point, show how much KL divergence there is between the true distribution and a Gaussian centered at that point.
- **Mutual information estimation:** generate correlated 2D data (bivariate Gaussian with correlation rho). Estimate I(X; Y) by discretizing into bins. Plot I(X; Y) vs. rho — zero for independent (rho = 0), increasing with correlation.
- **Information bottleneck experiment:** train a simple network. At each layer, estimate I(X; T_layer) and I(T_layer; Y) (using binning or other estimation methods). Plot the information plane. Do you see the fitting and compression phases?
- **Temperature experiment:** take a trained language model (or a simple softmax classifier). Vary temperature from 0.1 to 5.0. For each temperature, compute the entropy of the output distribution and sample outputs. See diversity increase with temperature.
- **Key exercise:** you're training a language model. The cross-entropy loss plateaus at 3.2 nats. What does this number mean? (It means the model's predictions have an average surprise of 3.2 nats — equivalently, the model assigns, on average, e^(-3.2) ≈ 4% probability to the correct next token.) If the entropy of English text is estimated at ~1.0 nat per character, how much room for improvement remains?

## 🔗 ML & Alignment Connection

- **Cross-entropy** is THE loss function for language modeling. Minimizing cross-entropy = maximizing likelihood (Lesson 21) = minimizing KL divergence from the true distribution. These are all the same optimization.
- **KL divergence in RLHF:** the KL penalty keeps the fine-tuned model from straying too far from the base model. D_KL(π_finetuned || π_base) is added to the reward. This is information-theoretic regularization — "don't change your predictions too much."
- **Mutual information in interpretability:** when researchers ask "does this layer represent part-of-speech?" they're asking whether I(layer_activations; part_of_speech) > 0. Linear probes estimate this mutual information.
- **The data processing inequality** explains why information bottlenecks in neural architectures (like the low-rank attention projection) force the model to discard irrelevant information and keep what matters.
- **Temperature** controls the entropy of generated text. Low temperature = predictable, repetitive. High temperature = creative, potentially incoherent. Finding the right temperature is finding the right point on the entropy spectrum.
- **VAEs** (variational autoencoders) minimize a loss that includes a KL divergence term, keeping the latent space close to a prior distribution.

- **The KL penalty in RLHF** is one of the most important alignment-relevant applications of information theory. Without it, RLHF training can "overoptimize" — the model finds reward hacks that score well but don't represent genuine improvement. The KL penalty is an information-theoretic leash.
- **Mutual information and ELK (Eliciting Latent Knowledge):** the question "does the model internally represent the truth?" can be formalized as: is the mutual information between the model's internal state and the ground truth positive? If I(internal_state; truth) > 0 but I(output; truth) = 0, the model "knows" but is hiding it.
- **Calibration** (Lesson 23) is an information-theoretic property: a well-calibrated model's predicted probabilities are informative about outcome frequencies. This connects to proper scoring rules and cross-entropy loss.
- **Information-theoretic alignment metrics:** some researchers propose measuring alignment as mutual information between the model's objectives and human values. This is speculative but shows how information theory provides a language for alignment concepts.