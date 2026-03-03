# Phase 4 Overview: Machine Learning & Interpretability — Every Concept and Method

> **Purpose:** Exhaustive reference of every concept, technique, and method covered in Phase 4 (Lessons 43–53). Spans from the single neuron through transformers to mechanistic interpretability and Singular Learning Theory.

---

## Machine Learning Foundations (Lessons 43–49)

### Lesson 43: How a Single Neuron Works

- **Perceptron model:** output = activation(Σ wᵢxᵢ + b) = activation(wᵀx + b)
- Weighted sum + bias + nonlinear activation
- **Linear decision boundary:** the hyperplane wᵀx + b = 0 separates classes
- **Activations:** step function (original perceptron), sigmoid (smooth gate), ReLU (modern default)
- **Perceptron learning rule:** w ← w + η(y − ŷ)x (update when wrong)
- **XOR problem:** single neuron can only separate linearly separable data; XOR is not linearly separable → need multiple layers
- **Single neuron with sigmoid = logistic regression** (from Phase 3)
- **Geometric view:** the neuron carves space with a hyperplane

---

### Lesson 44: The Forward Pass as Matrix Multiplications

- **Multi-layer networks:** stacking layers of affine transformations + nonlinearities
- **Forward pass for one layer:** h = σ(Wx + b) where σ is element-wise activation
- **Full network:** y = f_L ∘ f_{L-1} ∘ ... ∘ f_1(x) — composition of layers
- **Matrix multiplication IS the core computation:** batch of inputs × weight matrix = batch of outputs
- **ReLU folds space:** each ReLU neuron creates a fold; deep networks create complex piecewise-linear decision boundaries
- **Universal approximation theorem:** a single hidden layer with enough neurons can approximate any continuous function (but may need exponentially many neurons — depth helps)
- **Width vs depth tradeoffs:** wider = more features per layer; deeper = more compositional/hierarchical features
- **Parameter counting:** layer with m inputs and n outputs has m×n + n parameters

---

### Lesson 45: Backpropagation Through the Full Network

- **Goal:** compute ∂L/∂w for every weight w in the network
- **Backprop = reverse-mode automatic differentiation** applied to the computation graph
- **Forward pass:** compute and cache all intermediate activations
- **Backward pass:** propagate gradients from loss back through each layer using chain rule
- **Local gradients × upstream gradients** = gradients for current layer
- **Gradient flow through layers:** gradients must pass through every layer; long chains → problems
- **Vanishing gradients:** sigmoid/tanh squash gradients (max derivative < 1); deep networks → exponentially small gradients in early layers
- **Exploding gradients:** large weight magnitudes amplify gradients exponentially
- **Solutions to vanishing/exploding:**
  - **Residual connections (skip connections):** x + f(x) provides gradient highway
  - **Batch normalization / Layer normalization:** stabilize activation distributions
  - **Careful initialization:** Xavier/Glorot (sigmoid/tanh), He/Kaiming (ReLU)
  - **Gradient clipping:** cap gradient norms to prevent explosions
- **Gradient checking:** numerical differentiation (finite differences) to verify analytical gradients

---

### Lesson 46: Attention — Dot Products in Action

- **Query, Key, Value:** Q = XW_Q, K = XW_K, V = XW_V (learned linear projections)
- **Attention scores:** S = QKᵀ/√d_k (scaled dot-product similarity)
- **Softmax → attention weights:** A = softmax(S) — probability distribution over positions
- **Output:** O = AV — weighted sum of value vectors
- **Scaling by √d_k:** prevents dot products from growing with dimension (keeps softmax from saturating)
- **Multi-head attention:** split into h parallel attention heads, each with d_k = d_model/h
  - Concatenate outputs, project back: MultiHead = Concat(head₁, ..., head_h)W_O
  - Different heads can attend to different patterns simultaneously
- **Causal/autoregressive masking:** set future positions to −∞ before softmax (prevents attending to future tokens during generation)
- **Cross-attention:** Q from one sequence, K and V from another (used in encoder-decoder)
- **Multi-head Latent Attention (MLA):** DeepSeek variant using compressed latent representations
- **Attention as soft dictionary lookup:** Q = query, K = keys, V = values; attention weights = soft matches

---

### Lesson 47: Building a Transformer from Scratch

- **Full transformer block:** LayerNorm → Multi-Head Attention → Residual → LayerNorm → MLP → Residual
- Pre-norm (modern) vs post-norm (original paper) architectures
- **Residual stream:** the central "highway" that attention heads and MLPs read from and write to
- **MLP layers:** typically two linear layers with GELU/ReLU: MLP(x) = W₂ · GELU(W₁x + b₁) + b₂
  - Often 4× expansion (d_model → 4·d_model → d_model)
- **Positional encoding:** sinusoidal (fixed) or learned embeddings; RoPE (Rotary Position Embeddings)
- **Token embeddings:** vocabulary → d_model vectors via lookup table
- **Unembedding:** d_model → vocabulary logits (often tied with embedding weights)
- **QK circuit** (W_Qᵀ W_K): determines what each head attends to (attention pattern)
- **OV circuit** (W_O W_V): determines what information moves when attending (value copying)
- **"A Mathematical Framework for Transformer Circuits"** (Elhage, Nanda et al.): the key paper connecting linear algebra to transformer internals
- **Building GPT from scratch** (Karpathy): implement every component

---

### Lesson 48: Reinforcement Learning Foundations

- **Framework:** Agent interacts with Environment: state → action → reward → next state
- **Markov Decision Process (MDP):** (S, A, P, R, γ) — states, actions, transition probabilities, rewards, discount factor
- **Policy π(a|s):** strategy mapping states to action probabilities
- **Value function V^π(s):** expected cumulative discounted reward from state s under policy π
- **Q-function Q^π(s,a):** expected return from taking action a in state s, then following π
- **Bellman equations:** recursive definitions relating V and Q to future values
- **Discount factor γ ∈ [0,1):** how much to weight future vs immediate rewards
- **Policy gradient:** ∇J(θ) = E[∇log π_θ(a|s) · Q(s,a)] — increase probability of good actions
- **REINFORCE algorithm:** Monte Carlo policy gradient
- **PPO (Proximal Policy Optimization):** clipped updates prevent large policy changes; trust region
- **Value-based methods:** Q-learning, DQN (learn Q, act greedily)
- **Actor-critic:** combine policy gradient (actor) with learned value function (critic)
- **Reward shaping, specification gaming, Goodhart's Law**
- **Sparse vs dense rewards, credit assignment problem**
- **Reward hacking:** the alignment problem in miniature

---

### Lesson 49: The LLM Training Pipeline

- **Stage 1: Pre-training** — next-token prediction (autoregressive LM) on internet-scale text
  - Loss: cross-entropy on next token = MLE
  - **Scaling laws:** loss ∝ N^{-α} (power law in model size, data, compute)
  - **Chinchilla scaling:** optimal data/params ratio ≈ 20:1
- **Stage 2: Supervised Fine-Tuning (SFT)** — train on (instruction, response) demonstrations
  - Teaches format and style, not judgment
- **Stage 3: Preference Optimization**
  - **RLHF:** train reward model from human comparisons → PPO to optimize policy + KL penalty from base
  - **DPO (Direct Preference Optimization):** skip reward model, directly optimize on preference pairs
  - **Constitutional AI:** principle-based self-critique (Anthropic's approach)
  - **RLAIF:** AI-generated feedback instead of human
- **Stage 4: Deployment** — monitoring, safety filters, serving infrastructure
- **The bitter lesson** (Rich Sutton): compute + data + simple algorithms > clever hand-engineering

---

## Mechanistic Interpretability (Lessons 50–53)

### Lesson 50: Interpretability — What Researchers Actually Do

- **Mechanistic interpretability:** understanding model internals at the circuit/algorithm level
- **Activation patching (causal tracing):** swap activations between clean and corrupted runs to measure causal importance of each component
- **Direct logit attribution:** which components contribute to the final token prediction via the unembedding
- **Probing:** train simple linear classifiers on intermediate representations to test what information is encoded
- **Steering vectors:** add learned direction vectors to the residual stream to modify model behavior at inference time
- **Logit lens / tuned lens:** project intermediate layers through the unembedding to see "what the model is thinking" at each layer
- **TransformerLens:** Neel Nanda's library for mechanistic interpretability experiments
- **Hooks in PyTorch:** `register_forward_hook()` — the atomic operation of interpretability

---

### Lesson 51: Interpretability — Circuits and Features in Practice

- **Induction heads:** attention heads that implement in-context learning by copying patterns seen earlier in context
  - Two-head composition: previous-token head + induction head
- **Feature circuits:** networks of components (attention heads + MLP neurons) that together implement a specific computation
- **Sparse autoencoders (SAEs):** decompose MLP activations into interpretable, monosemantic features
  - x ≈ D · ReLU(E · x + b) where E encodes and D decodes, with sparsity penalty
- **Superposition:** models represent more features than they have dimensions using non-orthogonal directions
  - Trade-off: interference vs capacity
  - **Toy models of superposition** (Anthropic paper)
- **Monosemantic vs polysemantic neurons:** monosemantic = responds to one concept; polysemantic = responds to multiple unrelated concepts
- **Scaling monosemanticity** (Anthropic): SAEs at scale finding millions of interpretable features
- **Attention pattern analysis:** visualizing what each head attends to; identifying copying, induction, inhibition patterns
- **Residual stream as shared communication bus:** all components read from and write to it

---

### Lesson 52: Interpretability — Scaling Laws and Emergence

- **Kaplan scaling laws:** L(N) ∝ N^{-α} — loss as power law in model size/data/compute
- **Chinchilla scaling:** compute-optimal training (balance model size and data)
- **Emergent capabilities:** abilities that appear abruptly at certain model scales
  - In-context learning, chain-of-thought reasoning, theory of mind (claimed)
- **Measurement artifact debate** (Schaeffer et al.): many "emergent" capabilities appear smooth on log scale; sharp only on accuracy metrics
- **Practical danger threshold** may still be sharp regardless of metric smoothness
- **Grokking as phase transition** in training time (not model scale)
- **Developmental interpretability:** tracking internal representational changes at capability transitions
- **Phase transitions in training:** loss plateaus followed by sudden drops; internal restructuring

---

### Lesson 53: Interpretability — Singular Learning Theory

- **Standard statistics fails for neural networks:** parameter-to-function map is many-to-one
- **Symmetries create singularities:** neuron permutation, weight rescaling, zero neurons → multiple parameters give same function
- **Fisher information matrix is singular** at these symmetries
- **Free energy:** F = −log ∫ P(D|θ)P(θ)dθ
  - Regular models: F ≈ (d/2) log n (= BIC)
  - **Singular models: F ≈ λ · log n − (m−1) · log log n**
- **RLCT (Real Log Canonical Threshold) λ:** true effective dimension, λ ≤ d/2
  - Computed via resolution of singularities (algebraic geometry)
- **Why overparameterized networks generalize:** real complexity (RLCT) << parameter count
- **Phase transitions:** model moves between regions of parameter space with different RLCTs during training
- **Local Learning Coefficient (LLC):** estimable version of RLCT; tracks phase transitions empirically
- Connection to eigenvalues (flat Hessian directions), rank (degenerate Fisher information), algebraic geometry (blow-ups)

---

## Assessments

- **Exam 4A: Neural Network Foundations** (Lessons 43–49) — 60 min
- **Exam 4B: Mechanistic Interpretability** (Lessons 50–53) — 60 min
