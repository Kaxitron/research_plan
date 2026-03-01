# Exam 4A: Neural Network Foundations

**The Path to AI Alignment — Lessons 40–46 Comprehensive Assessment**

---

| | |
|---|---|
| **Time Allowed** | 60 minutes |
| **Total Points** | 100 |
| **Materials** | Pencil, paper, calculator (no CAS). No code. |
| **Format** | 10 questions: trace forward/backward passes, attention, transformers, RL, LLM pipeline |

> **Advice:** This exam is heavily computational. Show matrix dimensions at every step. The integrative thread: **can you trace the complete path from raw input through a transformer to aligned output, identifying the math from previous phases at each stage?**

---

## Question 1 (10 pts) — The Single Neuron

**(a)** A single neuron computes y = σ(wᵀx + b) where σ is the sigmoid. With w = [2, −1], b = 0.5, and x = [1, 3], compute the output y.

**(b)** A single neuron with sigmoid activation draws a decision boundary in input space. For the weights above, write the equation of this boundary. What shape is it?

**(c)** Why did ReLU replace sigmoid as the default activation? Answer in terms of the vanishing gradient problem, referencing the maximum value of σ'(x).

**(d)** A ReLU neuron with the same weights computes y = max(0, wᵀx + b). Compute the output for x = [1, 3]. Compare with the sigmoid output.

---

## Question 2 (12 pts) — Forward Pass as Matrix Multiplication

A 2-layer network has:
- Input x = [1, 0, −1]ᵀ (3×1)
- Layer 1: W₁ = [[1, 0, 1], [0, 1, −1]] (2×3), b₁ = [0, 0]ᵀ
- Activation: ReLU
- Layer 2: W₂ = [[1, −1]] (1×2), b₂ = [0.5]

**(a)** Compute z₁ = W₁x + b₁. State the dimensions at each step.

**(b)** Compute a₁ = ReLU(z₁).

**(c)** Compute z₂ = W₂a₁ + b₂ (the output).

**(d)** If we process a batch of 4 inputs simultaneously, what are the dimensions of the input matrix X, each weight matrix multiplication, and the output? Why is batch processing efficient?

---

## Question 3 (12 pts) — Backpropagation by Hand

Using the network from Question 2 with the output z₂ you computed, suppose the target is y = 1 and the loss is L = (z₂ − y)².

**(a)** Compute L.

**(b)** Compute ∂L/∂z₂.

**(c)** Compute ∂L/∂a₁ = W₂ᵀ · (∂L/∂z₂). State dimensions.

**(d)** Compute ∂L/∂z₁ by applying the ReLU derivative element-wise to ∂L/∂a₁.

**(e)** Compute ∂L/∂W₁ = (∂L/∂z₁) · xᵀ. Verify the dimensions match W₁.

**(f)** In one sentence: why do vanishing gradients occur in deep networks with sigmoid activations? How do residual connections fix this?

---

## Question 4 (10 pts) — Attention Mechanism

Consider 3 tokens with embedding dimension d = 2. The input matrix is X = [[1,0], [0,1], [1,1]] (3×2).

Projection matrices: W_Q = W_K = W_V = I (identity, for simplicity).

**(a)** Compute Q = XW_Q, K = XW_K, V = XW_V.

**(b)** Compute the attention score matrix S = QKᵀ (3×3). What does entry S_{ij} represent?

**(c)** Apply scaled attention: S/√d_k where d_k = 2. Then apply softmax to each ROW of the result. *(You may leave softmax values as approximate decimals.)*

**(d)** Compute the attention output: A = softmax(S/√d_k) · V. What has the attention mechanism done to each token's representation?

---

## Question 5 (10 pts) — Transformer Architecture

**(a)** List the components inside a single transformer block in order. For each, state its purpose in one sentence.

**(b)** A transformer processes tokens of dimension d_model = 512 with 8 attention heads. What is the dimension of each head's Q, K, V? Why do we use multiple heads instead of one big attention?

**(c)** Positional encodings add position information to token embeddings. Why can't a transformer know word order without them? *(Hint: what is attention's relationship to the order of inputs?)*

**(d)** The residual stream hypothesis says the residual connections create a shared "communication bus" that all components read from and write to. Explain how this view simplifies understanding what transformers compute.

---

## Question 6 (10 pts) — Reinforcement Learning Foundations

**(a)** Define: state, action, reward, policy π(a|s), value function V^π(s), and discount factor γ. Each in one sentence.

**(b)** The policy gradient theorem states: ∇J(θ) = E[∇log π(a|s; θ) · Q(s,a)]. Interpret this: what happens to the probability of an action that leads to high reward? Low reward?

**(c)** PPO (Proximal Policy Optimization) clips the policy update to stay within a "trust region." Why is this necessary? What goes wrong with unconstrained policy gradient updates?

**(d)** Give an example of reward hacking (specification gaming). Why is this the RL version of Goodhart's Law?

---

## Question 7 (10 pts) — The LLM Training Pipeline

Trace the complete pipeline, identifying the mathematical concept from earlier phases at each stage:

**(a)** Pre-training: next-token prediction on internet text. What loss function is used? What earlier concept is this equivalent to? (Phase 3)

**(b)** Supervised Fine-Tuning (SFT): training on human-written examples. How does the loss function differ from pre-training?

**(c)** Reward Model Training: humans compare pairs of outputs. What is the reward model learning to approximate?

**(d)** RLHF with PPO: optimizing the language model against the reward model with a KL penalty. Write the RLHF objective function. Identify the role of each term.

**(e)** Name the Phase 2 concept (constrained optimization) that the KL penalty implements.

---

## Question 8 (8 pts) — Matrix Dimensions Through a Transformer

A GPT-style model processes a sequence of 128 tokens with vocabulary size 50,000, d_model = 768, 12 attention heads, and MLP hidden size 3072.

State the dimensions of:

**(a)** The token embedding matrix.

**(b)** Q, K, V matrices for a single attention head.

**(c)** The output projection matrix that recombines heads.

**(d)** The MLP weight matrices (up-projection and down-projection).

---

## Question 9 (8 pts) — Credit Assignment and the Reward Problem

**(a)** In RLHF, reward is given for an entire generated response, not per token. Why does this create a credit assignment problem?

**(b)** DPO (Direct Preference Optimization) skips the reward model entirely. The key insight is that the optimal RLHF policy can be expressed in closed form as a function of the preference data and the reference model. What advantage does this give over the standard RLHF pipeline?

**(c)** Both RLHF and DPO optimize for human preferences. Why might these preferences not capture "what we actually want"? Name two failure modes.

---

## Question 10 (10 pts) — Synthesis: Math Across Phases

For each component of the LLM pipeline, identify the specific mathematical concept from the specified phase:

| Pipeline Stage | Phase 1 (Linear Algebra) | Phase 2 (Calculus) | Phase 3 (Probability) |
|---|---|---|---|
| Token embedding | ___ | ___ | ___ |
| Attention computation | ___ | ___ | ___ |
| Backpropagation | ___ | ___ | ___ |
| RLHF | ___ | ___ | ___ |

Fill in each cell with a specific concept (e.g., "dot products," "chain rule," "KL divergence"). Then pick any one cell and explain the connection in 2–3 sentences.
