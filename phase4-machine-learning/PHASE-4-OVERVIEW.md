# Phase 4 Overview: Machine Learning & Interpretability — Every Concept and Method

> **Purpose:** Exhaustive reference of every concept, technique, and method covered in Phase 4 (Lessons 53-66). Spans from the single neuron through transformers to mechanistic interpretability and Singular Learning Theory. Structured around Welch Labs *The Illustrated Guide to AI* (9 chapters) + Karpathy *Neural Networks: Zero to Hero*.
>
> **Estimated time:** ~148-176 hours

---

## Block A: Welch Labs Chapters 1-9 + Karpathy (Lessons 53-62)

### Lesson 53: The Perceptron — How a Single Neuron Works
**Source: Welch Labs Ch. 1**

**The Perceptron Model**
- **Neuron computation:** output = activation(sum(w_i * x_i) + b) = activation(w^T x + b)
- Weighted sum + bias + nonlinear activation — the atomic unit of neural networks
- **Linear decision boundary:** the hyperplane w^T x + b = 0 separates classes in input space
- **Geometric view:** the neuron carves space with a hyperplane; everything on one side fires, other side does not

**Activations**
- **Step function:** original perceptron — binary output, non-differentiable
- **Sigmoid:** sigma(z) = 1/(1 + e^{-z}) — smooth gate squashing to (0,1); gradient max = 0.25
- **ReLU:** max(0, z) — modern default; sparse activation, avoids vanishing gradient for positive inputs
- **Single neuron with sigmoid = logistic regression** (connection to Phase 3 statistics)

**The Perceptron Learning Rule**
- **Update rule:** w <- w + eta(y - y_hat)x (update only when prediction is wrong)
- **Convergence theorem:** if data is linearly separable, the perceptron will converge in finite steps
- **XOR problem:** a single neuron can only separate linearly separable data; XOR is not linearly separable, so we need multiple layers
- XOR as the historical motivation for multi-layer networks

**ML/alignment connection:** The perceptron shows that even the simplest learning unit has implicit assumptions (linearity). Understanding what a single neuron can and cannot represent is the foundation for understanding what larger networks can and cannot learn.

---

### Lesson 54: Gradient Descent — Learning from Errors
**Source: Welch Labs Ch. 2, Karpathy ZtH #1**

**Loss Functions and Optimization**
- **Loss function L(theta):** measures how wrong the model is; training = minimizing L
- **Mean Squared Error (MSE):** L = (1/n) sum((y_i - y_hat_i)^2) — regression default
- **Cross-entropy loss:** L = -sum(y_i log(y_hat_i)) — classification default; connects to MLE
- **Loss landscape:** the surface L(theta) over parameter space; goal is to find low points

**Gradient Descent**
- **Update rule:** theta <- theta - eta * grad_theta L — move opposite the gradient
- **Learning rate eta:** step size; too large = divergence/oscillation, too small = slow convergence
- **Batch gradient descent:** compute gradient over entire dataset per step
- **Stochastic gradient descent (SGD):** compute gradient on single example — noisy but fast
- **Mini-batch SGD:** gradient over random subset (batch size B) — the practical default
- Stochastic noise helps escape shallow local minima

**Momentum and Adaptive Methods**
- **Momentum:** accumulate velocity v = beta * v - eta * grad; theta <- theta + v — smooths oscillations
- **Adam optimizer:** adaptive learning rates per parameter using first and second moment estimates
- **Learning rate schedules:** warmup, cosine decay, step decay
- **Weight decay (L2 regularization):** theta <- (1 - lambda * eta) * theta - eta * grad — penalizes large weights

**Micrograd (Karpathy ZtH #1)**
- Building a tiny autograd engine from scratch: Value objects with _backward() methods
- Computation graph: every operation records its inputs and local gradient
- **Topological sort** of the graph, then call _backward() in reverse order
- Forward pass builds the graph; backward pass computes all gradients via chain rule

**ML/alignment connection:** The choice of loss function defines what the model optimizes for — it is the mathematical specification of the objective. Misspecified objectives (wrong loss) are the optimization-level analog of misalignment.

---

### Lesson 55: Backpropagation — The F=ma of AI
**Source: Welch Labs Ch. 3, Karpathy ZtH #1, #5**

**The Chain Rule in Neural Networks**
- **Goal:** compute dL/dw for every weight w in the network — these gradients drive learning
- **Backprop = reverse-mode automatic differentiation** applied to the computation graph
- **Forward pass:** compute and cache all intermediate activations (values at every node)
- **Backward pass:** propagate gradients from loss back through each layer using the chain rule
- **Local gradients x upstream gradients** = gradients for current layer

**Computation Graphs**
- Every neural network computation is a directed acyclic graph (DAG)
- Nodes = operations (add, multiply, ReLU, etc.); edges = data flow
- Each node knows its local derivative: d(output)/d(input)
- Backprop traverses this graph in reverse topological order
- **Gradient checking:** numerical differentiation (finite differences) to verify analytical gradients

**Gradient Flow Problems**
- **Vanishing gradients:** sigmoid/tanh squash gradients (max derivative < 1); deep networks produce exponentially small gradients in early layers
- **Exploding gradients:** large weight magnitudes amplify gradients exponentially
- **Solutions:**
  - **Residual connections (skip connections):** x + f(x) provides a gradient highway
  - **Batch normalization / Layer normalization:** stabilize activation distributions across layers
  - **Careful initialization:** Xavier/Glorot (sigmoid/tanh), He/Kaiming (ReLU) — match variance to layer width
  - **Gradient clipping:** cap gradient norms to prevent explosions

**Karpathy makemore (ZtH #5): Building a Character-Level Language Model Backprop**
- Manually computing gradients through an MLP for character-level prediction
- Backpropagating through cross-entropy, softmax, batch norm, tanh, linear layers by hand
- Understanding every gradient in the network — "becoming one with backprop"

**ML/alignment connection:** Backpropagation is the F=ma of AI — the single equation that makes learning possible. Understanding gradient flow is essential for interpretability (which gradients are large tells you what the network cares about).

---

### Lesson 56: Deep Learning — Why Depth Works
**Source: Welch Labs Ch. 4, Karpathy ZtH #2-3, #4**

**Multi-Layer Networks**
- **Stacking layers:** h = sigma(Wx + b) — affine transformation + nonlinearity, repeated
- **Full network:** y = f_L compose f_{L-1} compose ... compose f_1(x) — composition of layers
- **Matrix multiplication IS the core computation:** batch of inputs x weight matrix = batch of outputs
- **ReLU folds space:** each ReLU neuron creates a fold; deep networks create complex piecewise-linear decision boundaries

**Why Depth Matters**
- **Universal approximation theorem:** a single hidden layer with enough neurons can approximate any continuous function — but may need exponentially many neurons
- **Depth = compositionality:** deep networks learn hierarchical features (edges -> textures -> parts -> objects)
- **Width vs depth tradeoffs:** wider = more features per layer; deeper = more compositional/hierarchical features
- **Parameter counting:** layer with m inputs and n outputs has m*n + n parameters
- **Overparameterization:** modern networks have far more parameters than training examples, yet generalize — a puzzle explained partly by implicit regularization and SLT (Lesson 66)

**Karpathy makemore Series (ZtH #2-3): Bigram to MLP**
- Bigram language model: counting pairs, converting to probabilities
- Negative log-likelihood as loss; equivalence of count-based and gradient-based approaches
- MLP language model (Bengio et al. 2003): embedding lookup + hidden layers + softmax
- Training/validation/test splits; overfitting vs underfitting diagnostics
- **Embedding space:** each character/word becomes a learned vector; similar items cluster

**Karpathy makemore (ZtH #4): Becoming a Backprop Ninja**
- Building and training an MLP with batch normalization
- Diagnosing activation statistics: dead neurons, saturated neurons
- Initialization strategies and their effect on training dynamics
- The importance of understanding internals, not just treating networks as black boxes

**Regularization Techniques**
- **Dropout:** randomly zero out neurons during training — ensemble effect, prevents co-adaptation
- **Weight decay / L2 regularization:** penalize large weights
- **Early stopping:** stop training when validation loss starts increasing
- **Data augmentation:** artificially expand training data with transformations

**ML/alignment connection:** The fact that deep networks develop hierarchical internal representations is what makes interpretability possible — and necessary. The gap between "universal approximation" (what networks can represent) and "what they actually learn" (inductive biases from depth, architecture, optimization) is central to alignment.

---

### Lesson 57: AlexNet and Convolutional Neural Networks
**Source: Welch Labs Ch. 5**

**Convolution as Feature Detection**
- **Convolutional layer:** slide a small filter (kernel) across the input, computing dot products
- **Kernel/filter:** small weight matrix (e.g., 3x3, 5x5) that detects a local pattern
- **Feature map:** the output of applying one filter across the entire input
- **Stride:** how many pixels the filter moves per step
- **Padding:** adding zeros around the border to control output spatial dimensions
- **Parameter sharing:** same filter weights used at every spatial position — translation equivariance

**Pooling and Architecture**
- **Max pooling:** take the maximum value in each local region — spatial downsampling + local invariance
- **Average pooling:** take the mean instead — smoother downsampling
- **Receptive field:** the region of input that influences a given output neuron; grows with depth
- **CNN architecture pattern:** [Conv -> ReLU -> Pool] x N -> Flatten -> FC layers -> Softmax

**AlexNet (2012) — The Deep Learning Revolution**
- Krizhevsky, Sutskever, Hinton: won ImageNet 2012 by a massive margin
- Key innovations combined: ReLU activation, dropout regularization, GPU training, data augmentation
- 8 layers (5 conv + 3 FC), ~60M parameters
- Demonstrated that deep learning + data + compute beats hand-engineered features
- **Historical significance:** triggered the modern deep learning era

**The Hierarchy of Learned Features**
- Layer 1: edges and color gradients
- Layer 2: textures and simple patterns
- Layer 3: parts of objects (wheels, eyes)
- Layer 4+: whole objects and complex patterns
- **Feature visualization:** optimizing inputs to maximally activate specific neurons reveals what each neuron detects

**Beyond AlexNet**
- **VGGNet:** deeper (16-19 layers), uniform 3x3 filters
- **ResNet:** residual connections enabling 100+ layer networks; skip connections solve vanishing gradients at depth
- **Modern architectures:** EfficientNet, Vision Transformers (ViT) applying attention to image patches

**ML/alignment connection:** CNNs demonstrate that architecture imposes inductive biases (locality, translation equivariance). The hierarchy of learned features (edges -> objects) is an early example of interpretable internal representations — a precursor to mechanistic interpretability.

---

### Lesson 58: Neural Scaling Laws and Emergence
**Source: Welch Labs Ch. 6**

**Kaplan Scaling Laws**
- **Power law relationship:** L(N) proportional to N^{-alpha} — loss decreases as a power law in model size, data, and compute
- Loss scales smoothly and predictably with resources on log-log plots
- **Three axes of scaling:** model parameters N, dataset size D, compute budget C
- Each axis has its own scaling exponent
- Scaling laws enable predicting performance of larger models from smaller experiments

**Chinchilla Scaling (Hoffmann et al. 2022)**
- **Compute-optimal training:** for a given compute budget, balance model size and data
- **Optimal ratio:** approximately 20 tokens per parameter
- Previous models (GPT-3) were undertrained relative to their size
- Chinchilla (70B params, 1.4T tokens) matched the 280B Gopher with 4x less compute
- Shifted the field toward more data, not just more parameters

**Emergent Capabilities**
- **Emergence:** abilities that appear abruptly at certain model scales — absent in small models, present in large ones
- Examples: in-context learning, chain-of-thought reasoning, few-shot task performance
- **Phase transitions in capability:** smooth loss curves but sharp jumps in task accuracy

**The Emergence Debate**
- **Measurement artifact hypothesis** (Schaeffer et al. 2023): many "emergent" capabilities appear smooth on log scale; sharp only on nonlinear metrics like accuracy
- Choosing different evaluation metrics can create or eliminate apparent emergence
- **Practical danger threshold may still be sharp:** even if underlying capabilities grow smoothly, dangerous capability thresholds (e.g., ability to deceive, to assist with bioweapons) may be effectively discontinuous
- **Grokking:** a different kind of phase transition — in training time, not model scale; sudden generalization long after memorization

**Developmental Interpretability**
- **Tracking internal representational changes** at capability transitions
- Phase transitions in training: loss plateaus followed by sudden drops; internal restructuring
- Circuit formation and reorganization during training
- Connection to Singular Learning Theory phase transitions (Lesson 66)

**ML/alignment connection:** Scaling laws and emergence are central to AI safety forecasting. If dangerous capabilities emerge unpredictably at scale, we cannot rely on testing smaller models. The emergence debate determines whether we can predict when models will acquire specific capabilities.

---

### Lesson 59: Attention — How Transformers Think
**Source: Welch Labs Ch. 8*, Karpathy ZtH #7**

*Note: Welch Labs chapters 7 and 8 are taught in swapped order — build the transformer first, then interpret it.

**Query, Key, Value**
- **Three projections:** Q = XW_Q, K = XW_K, V = XW_V (learned linear projections from the residual stream)
- **Attention scores:** S = QK^T / sqrt(d_k) — scaled dot-product similarity between queries and keys
- **Softmax produces attention weights:** A = softmax(S) — probability distribution over positions (which tokens to attend to)
- **Output:** O = AV — weighted sum of value vectors (what information to move)
- **Scaling by sqrt(d_k):** prevents dot products from growing with dimension, keeping softmax from saturating

**Multi-Head Attention**
- **Parallel heads:** split into h parallel attention heads, each with d_k = d_model/h
- Concatenate outputs, project back: MultiHead = Concat(head_1, ..., head_h) W_O
- Different heads can attend to different patterns simultaneously (syntactic, semantic, positional)
- **Attention as soft dictionary lookup:** Q = query, K = keys, V = values; attention weights = soft matches

**Masking and Cross-Attention**
- **Causal/autoregressive masking:** set future positions to -inf before softmax — prevents attending to future tokens during generation
- **Cross-attention:** Q from one sequence, K and V from another (used in encoder-decoder models, multimodal)
- **Bidirectional attention:** no mask — used in BERT-style models for understanding tasks

**Positional Information**
- Attention is permutation-equivariant without positional encoding — order information must be injected
- **Sinusoidal embeddings:** fixed, based on position and dimension (original Transformer)
- **Learned positional embeddings:** trainable vectors per position
- **RoPE (Rotary Position Embeddings):** encode relative position in the rotation of Q and K vectors — modern default
- **ALiBi:** add linear bias to attention scores based on distance

**ML/alignment connection:** Attention patterns are one of the most interpretable aspects of transformers. Understanding what tokens attend to what gives direct insight into model reasoning. Attention is also where many safety-relevant behaviors are implemented (e.g., refusal circuits, truthfulness).

---

### Lesson 60: Building a Transformer from Scratch
**Source: Karpathy ZtH #7, #9**

**The Transformer Block**
- **Full block:** LayerNorm -> Multi-Head Attention -> Residual Add -> LayerNorm -> MLP -> Residual Add
- **Pre-norm (modern)** vs **post-norm (original paper)** architectures — pre-norm is more stable to train
- **Residual stream:** the central "highway" that attention heads and MLPs read from and write to
- Every component reads from the residual stream and adds its output back to it

**MLP Layers**
- **Two linear layers with nonlinearity:** MLP(x) = W_2 * GELU(W_1 * x + b_1) + b_2
- Typically 4x expansion: d_model -> 4*d_model -> d_model
- **Gated variants:** SwiGLU, GeGLU — multiply by a learned gate, better performance
- MLPs store factual knowledge (key-value memories); attention routes information

**Embeddings and Unembeddings**
- **Token embeddings:** vocabulary -> d_model vectors via lookup table (embedding matrix W_E)
- **Unembedding:** d_model -> vocabulary logits via W_U (often tied with W_E^T — weight tying)
- **Softmax + sampling:** convert logits to probabilities; temperature, top-k, top-p (nucleus) sampling

**Circuit-Level View**
- **QK circuit** (W_Q^T W_K): determines what each head attends to — the "where to look" circuit
- **OV circuit** (W_O W_V): determines what information moves when attending — the "what to copy" circuit
- **"A Mathematical Framework for Transformer Circuits"** (Elhage, Nanda et al.): the key paper connecting linear algebra to transformer internals
- The residual stream as a shared communication bus between all components

**Karpathy nanoGPT (ZtH #7)**
- Implement every component of GPT-2 from scratch in PyTorch
- Training on Shakespeare text: tokenization, batching, training loop
- **KV cache:** during autoregressive generation, cache key and value tensors to avoid recomputation
- Reproducing GPT-2 (124M) results with careful engineering

**Karpathy tokenization (ZtH #9)**
- **Byte Pair Encoding (BPE):** iteratively merge most frequent byte pairs to build a vocabulary
- Tokenization as a separate learned compression layer before the transformer
- Edge cases: numbers, Unicode, multilingual text, code
- Token boundaries affect model behavior in subtle ways

**ML/alignment connection:** Building a transformer from scratch demystifies the architecture. The circuit-level view (QK and OV circuits) is the foundation of mechanistic interpretability — understanding alignment-relevant behaviors requires understanding these circuits.

---

### Lesson 61: Mechanistic Interpretability — The Dark Matter of AI
**Source: Welch Labs Ch. 7***

*Note: Taught after the transformer build (Lesson 60) so that interpretability techniques can be applied to a model you understand from the inside.

**What Mechanistic Interpretability Is**
- **Mechanistic interpretability:** understanding model internals at the circuit/algorithm level — not just what models do, but how they do it
- Goal: reverse-engineer the algorithms learned by neural networks
- Contrast with behavioral testing (black-box) — mechanistic interp opens the box
- The "dark matter" metaphor: we know these models work, but not why or how

**Core Techniques**
- **Activation patching (causal tracing):** swap activations between clean and corrupted runs to measure causal importance of each component
- **Direct logit attribution:** which components contribute to the final token prediction via the unembedding — trace logit contributions back through the residual stream
- **Probing:** train simple linear classifiers on intermediate representations to test what information is encoded at each layer
- **Logit lens / tuned lens:** project intermediate layers through the unembedding to see "what the model is thinking" at each layer
- **Steering vectors:** add learned direction vectors to the residual stream to modify model behavior at inference time — activation engineering

**Tools and Infrastructure**
- **TransformerLens:** Neel Nanda's library for mechanistic interpretability experiments
- **Hooks in PyTorch:** register_forward_hook() — the atomic operation of interpretability; insert probes at any layer
- **Ablation studies:** zero-ablation, mean-ablation, resample ablation — test component necessity
- **Attention pattern visualization:** heatmaps of what each head attends to

**Known Circuits**
- **Induction heads:** attention heads that implement in-context learning by copying patterns seen earlier in context
  - Two-head composition: previous-token head + induction head
  - Perhaps the most important circuit discovered in transformers
- **Indirect Object Identification (IOI):** circuit for "John gave the book to Mary" -> predicting "Mary"
  - Multiple attention heads with specific roles: name mover heads, backup name mover heads, inhibition heads
- **Greater-than circuit:** heads that compare numbers using learned ordinal representations

**ML/alignment connection:** Mechanistic interpretability is the primary technical approach to understanding whether AI systems are safe. If we can identify the circuits responsible for deception, sycophancy, or goal-directed behavior, we can potentially detect and correct misalignment. This is why Anthropic, DeepMind, and OpenAI all invest heavily in this research.

---

### Lesson 62: Video & Image Generation — Diffusion Models
**Source: Welch Labs Ch. 9**

**The Core Idea: Denoising**
- **Forward process:** gradually add Gaussian noise to data over T timesteps until it becomes pure noise
- **Reverse process:** learn to denoise — a neural network predicts the noise to remove at each step
- **Training objective:** predict the noise epsilon added at each step; minimize ||epsilon - epsilon_theta(x_t, t)||^2
- **Sampling:** start from pure noise, iteratively denoise to generate a new sample

**Mathematical Framework**
- **Forward diffusion:** q(x_t | x_{t-1}) = N(x_t; sqrt(1-beta_t) x_{t-1}, beta_t I) — add a bit of noise at each step
- **Noise schedule beta_t:** controls how fast noise is added; linear, cosine, or learned schedules
- **Reparameterization trick:** x_t = sqrt(alpha_bar_t) x_0 + sqrt(1 - alpha_bar_t) epsilon — jump to any timestep directly
- **Reverse process:** p_theta(x_{t-1} | x_t) — learned denoising; parameterized by a neural network (usually a U-Net or Transformer)
- **Connection to score matching:** the model learns the score function grad_x log p(x)

**Conditioning and Guidance**
- **Text conditioning:** cross-attention between denoising network and text encoder (CLIP, T5)
- **Classifier-free guidance:** train with and without conditioning; interpolate at inference for stronger adherence to prompt
- **Guidance scale:** higher = more faithful to prompt but less diverse
- **ControlNet:** add spatial conditioning (edges, depth maps, poses) to control generation

**Key Models and Architectures**
- **DDPM (Denoising Diffusion Probabilistic Models):** foundational paper establishing the modern diffusion framework
- **Latent diffusion (Stable Diffusion):** run diffusion in the latent space of a VAE — much more computationally efficient
- **U-Net architecture:** encoder-decoder with skip connections at each scale; processes at multiple resolutions
- **DiT (Diffusion Transformers):** replace U-Net with a transformer — scales better

**Video Generation**
- Extend image diffusion to temporal dimension: generate sequences of frames
- **Temporal attention:** attend across frames to maintain consistency
- **Challenges:** temporal coherence, motion realism, computational cost (3D tensor instead of 2D)
- **Sora, Runway, Kling:** state-of-the-art video generation systems

**ML/alignment connection:** Generative models raise alignment questions around deepfakes, misinformation, and content authenticity. The diffusion framework also connects to the theoretical understanding of how models represent and reconstruct the data distribution — relevant to understanding what models "know" about the world.

---

## Block B: Additional ML Topics (Lessons 63–64)

### Lesson 63: Reinforcement Learning Foundations

**The RL Framework**
- **Agent-Environment loop:** state -> action -> reward -> next state -> ...
- **Markov Decision Process (MDP):** (S, A, P, R, gamma) — states, actions, transition probabilities, rewards, discount factor
- **Policy pi(a|s):** strategy mapping states to action probabilities
- **Deterministic vs stochastic policies**

**Value Functions**
- **State value function V^pi(s):** expected cumulative discounted reward from state s under policy pi
- **Action-value function Q^pi(s,a):** expected return from taking action a in state s, then following pi
- **Bellman equations:** recursive definitions relating V and Q to future values — the fundamental equations of RL
- **Discount factor gamma in [0,1):** how much to weight future vs immediate rewards; gamma=0 is myopic, gamma->1 is far-sighted
- **Optimal value functions V* and Q*:** the best possible values under any policy

**Policy Optimization**
- **Policy gradient theorem:** grad J(theta) = E[grad log pi_theta(a|s) * Q(s,a)] — increase probability of good actions
- **REINFORCE algorithm:** Monte Carlo policy gradient — high variance but unbiased
- **Baseline subtraction:** subtract V(s) to reduce variance: advantage A(s,a) = Q(s,a) - V(s)
- **PPO (Proximal Policy Optimization):** clipped surrogate objective prevents large policy changes; trust region method
- **Value-based methods:** Q-learning, DQN — learn Q, act greedily; no explicit policy

**Actor-Critic Methods**
- **Actor:** the policy network pi_theta(a|s) — decides what to do
- **Critic:** the value network V_phi(s) or Q_phi(s,a) — evaluates how good the action was
- **Advantage Actor-Critic (A2C):** actor uses advantage estimates from the critic
- **Combining policy and value learning** reduces variance of policy gradient

**Reward and Alignment**
- **Reward shaping:** modifying the reward function to guide learning without changing the optimal policy
- **Specification gaming:** the agent finds unintended ways to maximize reward that violate the designer's intent
- **Goodhart's Law:** "When a measure becomes a target, it ceases to be a good measure"
- **Sparse vs dense rewards:** sparse rewards make credit assignment harder
- **Reward hacking:** the alignment problem in miniature — the agent optimizes the reward signal, not the intended objective
- **Credit assignment problem:** determining which actions led to delayed rewards

**ML/alignment connection:** RL is where alignment problems are most concrete. RLHF uses RL to align language models, but reward hacking, specification gaming, and Goodhart's Law are fundamental obstacles. Understanding RL deeply is prerequisite to understanding why alignment is hard.

---

### Lesson 64: The LLM Training Pipeline
**Source: Karpathy ZtH #8, Deep Dive into LLMs**

**Stage 1: Pre-training**
- **Objective:** next-token prediction (autoregressive language modeling) on internet-scale text
- **Loss:** cross-entropy on next token = maximum likelihood estimation (MLE)
- **Training data:** web crawls (Common Crawl, RefinedWeb), books, code, filtered and deduplicated
- **Data quality matters:** filtering, deduplication, and domain mixing ratios significantly affect model quality
- **Scaling laws apply:** loss = f(N, D, C) as power laws — predictable performance from compute budget
- **Chinchilla-optimal training:** balance model size N and data D for given compute C
- **Curriculum effects:** ordering of training data can matter

**Stage 2: Supervised Fine-Tuning (SFT)**
- **Data:** (instruction, response) pairs — demonstrations of desired behavior
- Train on the same next-token prediction objective, but on curated conversation data
- **Teaches format and style, not judgment** — the model learns how to respond, not what is true
- **Quality over quantity:** a few thousand high-quality examples can be very effective
- **LoRA (Low-Rank Adaptation):** fine-tune only low-rank updates to weight matrices — parameter-efficient

**Stage 3: Preference Optimization**
- **RLHF (Reinforcement Learning from Human Feedback):**
  - Collect human comparisons: "response A is better than response B"
  - Train a reward model on these preferences
  - Use PPO to optimize the language model policy against the reward model
  - **KL penalty:** prevent the policy from drifting too far from the SFT model
- **DPO (Direct Preference Optimization):** skip the reward model, directly optimize on preference pairs using a closed-form objective derived from the RL formulation
- **Constitutional AI (Anthropic's approach):** principle-based self-critique and revision; model critiques its own outputs against a set of principles
- **RLAIF:** AI-generated feedback instead of human feedback — scalable but introduces the AI's biases
- **Reward model overoptimization:** optimizing too hard against the reward model leads to Goodhart's Law — exploiting the reward model rather than being genuinely helpful

**Stage 4: Deployment and Inference**
- **Serving infrastructure:** batching, KV cache, speculative decoding, quantization (INT8, INT4)
- **Safety systems:** input/output filters, monitoring, rate limiting
- **Evaluation:** benchmarks (MMLU, HumanEval, etc.), red-teaming, human evaluation
- **Post-training enhancements:** tool use, retrieval-augmented generation (RAG), chain-of-thought prompting

**The Bitter Lesson (Rich Sutton)**
- Compute + data + simple algorithms consistently outperform clever hand-engineering
- Methods that scale with compute will win in the long run
- Historically, researchers who bet on scaling were right

**ML/alignment connection:** The training pipeline is where alignment happens in practice. Each stage (pretraining, SFT, RLHF/DPO) shapes the model's values and behaviors. Understanding this pipeline is essential for understanding how current AI systems are aligned — and where that alignment can break down.

---

## Block C: Deep Interpretability (Lessons 65-66)

### Lesson 65: Interpretability — Circuits, Features, and Superposition

**Feature Representation in Neural Networks**
- **Monosemantic vs polysemantic neurons:** monosemantic = responds to one concept; polysemantic = responds to multiple unrelated concepts
- Most neurons in large models are polysemantic — making interpretation hard
- **Features vs neurons:** the fundamental units of representation may not align with individual neurons

**Superposition**
- **Superposition hypothesis:** models represent more features than they have dimensions using non-orthogonal directions
- **Trade-off:** interference vs capacity — slight interference allows storing many more features
- **Toy models of superposition** (Anthropic paper): systematic study of when and how superposition occurs
- Superposition is more likely for sparse, less important features
- **Geometry of superposition:** features arrange in structured geometric configurations (simplices, polytopes)
- **Implication:** you cannot understand a network by looking at individual neurons; features are distributed

**Sparse Autoencoders (SAEs)**
- **Goal:** decompose activations into interpretable, monosemantic features
- **Architecture:** x_approx = D * ReLU(E * x + b) where E encodes and D decodes, with sparsity penalty
- **Training:** minimize reconstruction error + L1 sparsity penalty on the hidden activations
- **Overcomplete dictionary:** the number of SAE features >> d_model — one feature per concept
- **Scaling monosemanticity** (Anthropic): SAEs at scale finding millions of interpretable features in Claude
- Features found include: Golden Gate Bridge, code errors, deception, sycophancy, many languages and concepts
- **SAE quality metrics:** reconstruction fidelity, sparsity, feature interpretability, downstream task performance

**Circuits**
- **Feature circuits:** networks of components (attention heads + MLP neurons) that together implement a specific computation
- **Circuit discovery:** use activation patching and ablation to identify which components matter for a given behavior
- **Composition:** attention heads compose through the residual stream (Q-composition, K-composition, V-composition)
- **Attention pattern analysis:** visualizing what each head attends to; identifying copying, induction, inhibition patterns
- **Residual stream as shared communication bus:** all components read from and write to it — the "backbone" of the transformer

**Key Results**
- **Induction heads in detail:** the mechanism for in-context learning; develop during a phase transition in training
- **Indirect Object Identification:** the most complete circuit analysis of a real-world behavior
- **Successor heads:** heads that compute the "next" item in a sequence (next letter, next number, next month)

**ML/alignment connection:** Superposition is why interpretability is hard — features are not neatly separated. SAEs are the current best approach to cracking superposition. Finding interpretable features like "deception" or "sycophancy" in real models is directly relevant to detecting and preventing misaligned behavior.

---

### Lesson 66: Interpretability — Singular Learning Theory

**Why Standard Statistics Fails for Neural Networks**
- **Parameter-to-function map is many-to-one:** different parameter settings can produce identical input-output behavior
- **Symmetries create singularities:** neuron permutation symmetry, weight rescaling, zero neurons — multiple parameter vectors map to the same function
- **Fisher information matrix is singular** at these symmetric points — standard asymptotic theory (based on regularity) breaks down
- Neural networks are "singular models" in the sense of algebraic geometry — they violate the regularity conditions assumed by BIC, AIC, etc.

**The Free Energy and RLCT**
- **Free energy:** F = -log integral P(D|theta) P(theta) d(theta) — the Bayesian model evidence (marginal likelihood)
- **Regular models:** F approx (d/2) log n — effective complexity = half the parameter count (this gives BIC)
- **Singular models:** F approx lambda * log n - (m-1) * log log n — the key formula of SLT
- **RLCT (Real Log Canonical Threshold) lambda:** the true effective dimension of the model
  - lambda <= d/2 always (singular models are "simpler" than their parameter count suggests)
  - Computed via resolution of singularities — a technique from algebraic geometry
  - lambda depends on the geometry of the loss landscape near the optimal parameter region

**Why Overparameterized Networks Generalize**
- **The puzzle:** networks with millions of parameters can generalize from thousands of examples — classical statistics says this should overfit catastrophically
- **SLT answer:** the real complexity (RLCT lambda) is much smaller than the parameter count d
- The loss landscape has flat directions (symmetries, redundant parameters) that do not contribute to effective complexity
- **Connection to the Hessian:** flat directions correspond to near-zero eigenvalues of the Hessian; the RLCT captures this geometry precisely

**Phase Transitions in Training**
- **Model moves between regions** of parameter space with different RLCTs during training
- **Phase transitions:** sudden drops in loss correspond to the model finding parameter regions with lower RLCT (simpler effective models that fit the data)
- **Grokking explained:** delayed generalization corresponds to a phase transition from a high-RLCT (memorization) region to a low-RLCT (generalization) region

**The Local Learning Coefficient (LLC)**
- **Estimable version of RLCT:** can be computed empirically during training without algebraic geometry
- **LLC tracks phase transitions:** jumps in LLC correspond to qualitative changes in what the model has learned
- **Developmental interpretability:** using LLC to monitor when models acquire new capabilities during training
- **Connection to loss of plasticity, catastrophic forgetting, and curriculum learning**

**Mathematical Foundations**
- **Resolution of singularities (Hironaka's theorem):** any singular variety can be transformed into a smooth one by a sequence of blow-ups
- **Blow-ups in algebraic geometry:** replace singular points with projective spaces to "spread out" the singularity
- **Watanabe's theorem:** the asymptotic expansion of the free energy in terms of lambda and m (the multiplicity)
- **Zeta functions and poles:** the RLCT equals the largest real pole of a certain zeta function associated with the loss landscape

**ML/alignment connection:** SLT provides the deepest theoretical framework for understanding neural network behavior. It explains why networks generalize, when they undergo phase transitions, and how to measure their true complexity. For alignment, SLT offers tools to detect when models acquire new capabilities (phase transitions) and to understand the geometry of what models learn — potentially providing early warning of emergent dangerous capabilities.

---

## Assessments

- **Exam 4A: Neural Networks & ML** (Lessons 53–64) — 10 short questions (30 min) + 5-hour Karpathy-style build project
- **Exam 4B: Mechanistic Interpretability** (Lessons 61, 65–66) — 10 short questions (30 min) + 3-4 hour interpretability project
