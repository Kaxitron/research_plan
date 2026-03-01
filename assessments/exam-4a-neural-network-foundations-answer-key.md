# Exam 4A: Neural Network Foundations — Answer Key

**The Path to AI Alignment — Lessons 40–46 Comprehensive Assessment**

---

### Question 1 (10 pts)
**(a)** wᵀx + b = 2(1) + (−1)(3) + 0.5 = 2 − 3 + 0.5 = −0.5. y = σ(−0.5) = 1/(1+e^0.5) ≈ **0.378**.

**(b)** Decision boundary: wᵀx + b = 0 → 2x₁ − x₂ + 0.5 = 0 → **x₂ = 2x₁ + 0.5**. A straight **line** (hyperplane in 2D). The neuron classifies points above vs. below this line.

**(c)** σ'(x) = σ(x)(1−σ(x)) has maximum **0.25** at x = 0. Each sigmoid layer multiplies gradients by at most 0.25. Through L layers: gradient ≤ 0.25^L → vanishes exponentially. ReLU'(x) = 1 for x > 0, so gradients pass through unchanged — no shrinking.

**(d)** ReLU(−0.5) = max(0, −0.5) = **0**. The ReLU output is 0 (neuron is "off"), while sigmoid gave 0.378. ReLU is piecewise linear and sparse (many outputs are exactly 0), while sigmoid is always nonzero.

### Question 2 (12 pts)
**(a)** z₁ = W₁x + b₁ = [[1,0,1],[0,1,−1]][1,0,−1]ᵀ + [0,0]ᵀ = [1(1)+0(0)+1(−1), 0(1)+1(0)+(−1)(−1)]ᵀ = **[0, 1]ᵀ** (2×1).

**(b)** a₁ = ReLU([0, 1]ᵀ) = **[0, 1]ᵀ**.

**(c)** z₂ = [1,−1][0,1]ᵀ + 0.5 = 0 − 1 + 0.5 = **−0.5**.

**(d)** X is 3×4 (3 features, 4 samples). W₁X: (2×3)(3×4) = 2×4. After ReLU: 2×4. W₂·ReLU: (1×2)(2×4) = 1×4. Batch processing is efficient because matrix multiplications are highly parallelizable on GPUs — computing 4 examples takes barely longer than 1.

### Question 3 (12 pts)
**(a)** L = (−0.5 − 1)² = (−1.5)² = **2.25**.

**(b)** ∂L/∂z₂ = 2(z₂ − y) = 2(−0.5 − 1) = **−3** (scalar).

**(c)** ∂L/∂a₁ = W₂ᵀ · (−3) = [[1],[−1]] · (−3) = **[−3, 3]ᵀ** (2×1).

**(d)** ReLU derivative: z₁ = [0, 1]. ReLU'(0) = 0, ReLU'(1) = 1. So ∂L/∂z₁ = [−3, 3]ᵀ ⊙ [0, 1]ᵀ = **[0, 3]ᵀ**.

**(e)** ∂L/∂W₁ = (∂L/∂z₁)·xᵀ = [0,3]ᵀ · [1,0,−1] = **[[0,0,0],[3,0,−3]]** (2×3 ✓ matches W₁).

**(f)** Sigmoid squeezes gradients by at most 0.25 per layer; after many layers, the gradient signal is exponentially small and early layers learn nothing. Residual connections add a skip path: the gradient flows directly through the addition, bypassing the potentially-small layer gradients. This ensures gradients reach early layers intact.

### Question 4 (10 pts)
**(a)** Since W_Q = W_K = W_V = I: **Q = K = V = X** = [[1,0],[0,1],[1,1]].

**(b)** S = QKᵀ = XXᵀ = [[1,0,1],[0,1,1],[1,1,2]]. S_{ij} is the **dot product similarity** between token i's query and token j's key — how much token i should attend to token j.

**(c)** S/√2 = [[0.71,0,0.71],[0,0.71,0.71],[0.71,0.71,1.41]]. Softmax per row:
- Row 1: softmax([0.71, 0, 0.71]) ≈ [0.39, 0.19, 0.42] (approximately)
- Row 2: softmax([0, 0.71, 0.71]) ≈ [0.19, 0.39, 0.42]
- Row 3: softmax([0.71, 0.71, 1.41]) ≈ [0.24, 0.24, 0.52]

**(d)** A = softmax(S/√d)·V. Each output row is a weighted average of the V vectors, where weights come from the attention scores. Token 3 ([1,1]) gets the most self-attention because it has the highest dot product with itself. The attention mechanism has allowed each token to "look at" all other tokens and create a new representation that blends information from the most relevant positions.

### Question 5 (10 pts)
**(a)** 1. **Multi-head self-attention:** lets each token gather information from all positions. 2. **Add & LayerNorm (post-attention):** residual connection preserves information; normalization stabilizes training. 3. **MLP (feed-forward):** applies a nonlinear transformation to each token independently. 4. **Add & LayerNorm (post-MLP):** another residual + normalization.

**(b)** d_head = d_model/num_heads = 512/8 = **64**. Each head operates in a 64-dimensional subspace. Multiple heads let the model attend to different types of relationships simultaneously (syntax, semantics, position, etc.) in different subspaces.

**(c)** Attention computes dot products between all pairs — S = QKᵀ. This is **permutation equivariant**: shuffling input order shuffles the output the same way but doesn't change which tokens attend to which. Without positional encodings, "The cat sat on the mat" and "mat the on sat cat The" produce identical representations.

**(d)** The residual stream view: every component (attention head, MLP) reads from and writes to a shared d_model-dimensional vector per position. This means you can analyze each component independently — what does it read? what does it write? — rather than tracing information through a tangled chain. It makes interpretability more tractable.

### Question 6 (10 pts)
**(a)** State: current situation. Action: what the agent does. Reward: scalar feedback signal. Policy π(a|s): probability of choosing action a in state s. V^π(s): expected total discounted reward from state s following π. Discount factor γ ∈ [0,1): weights future rewards less than immediate (γ = 0.99 means rewards 100 steps ahead are worth ~37% of immediate rewards).

**(b)** ∇log π(a|s)·Q(s,a) scales the gradient by the return. **High Q** → gradient pushes π(a|s) higher (reinforce the action). **Low Q** → gradient pushes π(a|s) lower (suppress the action). Actions that lead to good outcomes become more probable.

**(c)** Unconstrained policy gradients can make large updates that collapse the policy — moving too far in parameter space can destroy previously learned behavior. PPO clips the ratio π_new/π_old to [1−ε, 1+ε], preventing catastrophically large updates. This is a practical implementation of the "trust region" idea.

**(d)** Example: A cleaning robot trained with reward "number of messes detected reduces to zero" learns to cover messes with a blanket (or close its camera) instead of cleaning. This IS Goodhart's Law: the reward function was a proxy for "room is clean," and the agent found an unintended shortcut that maximizes the proxy without achieving the intended goal.

### Question 7 (10 pts)
**(a)** Cross-entropy loss: L = −Σ log p(x_t | x_{<t}). This is **MLE** — maximizing the log-likelihood of the training data under the model.

**(b)** Same loss function (cross-entropy), but on curated examples of desired behavior. The data distribution shifts from "internet text" to "helpful, high-quality responses."

**(c)** The reward model learns to approximate **human preference orderings** — given two outputs, it predicts which one a human would prefer. It's learning a proxy for human values.

**(d)** Objective: **max_π E[R(x,y)] − β·DKL(π ‖ π_ref)**. R(x,y): reward model score (maximize quality). DKL: divergence penalty (don't drift far from reference). β: tradeoff coefficient (the Lagrange multiplier controlling the alignment-capability balance).

**(e)** **Lagrange multipliers / constrained optimization** (Lesson 18). The KL penalty implements a soft constraint: "maximize reward subject to staying near the reference model." β is the Lagrange multiplier.

### Question 8 (8 pts)
**(a)** Embedding: **50,000 × 768** (vocab_size × d_model).
**(b)** Each head: Q, K, V are **128 × 64** (seq_len × d_head, where d_head = 768/12 = 64).
**(c)** Output projection: **768 × 768** (concatenated heads back to d_model).
**(d)** Up-projection: **768 × 3072**. Down-projection: **3072 × 768**.

### Question 9 (8 pts)
**(a)** A 100-token response gets one reward score. Which of the 100 tokens were responsible? Maybe token 50 was misleading but tokens 1–49 were great. The reward gives no per-token signal — the model must figure out which tokens contributed to the overall quality.

**(b)** DPO avoids training a separate reward model (saving compute and potential reward model errors), provides a more stable optimization (no RL inner loop), and has a simpler implementation. It shows that the optimal policy under RLHF has an analytical form that depends only on the preference data and reference model.

**(c)** (1) **Sycophancy:** humans prefer responses that agree with them, so the model learns to tell people what they want to hear rather than the truth. (2) **Reward hacking of the reward model:** the policy finds outputs that score high on the reward model but seem unnatural or game specific patterns the reward model learned, not actual quality.

### Question 10 (10 pts)

| Pipeline Stage | Phase 1 | Phase 2 | Phase 3 |
|---|---|---|---|
| Token embedding | Matrix lookup / column selection | — | Learned representation (no direct connection) |
| Attention | Dot products, projections | Softmax (exp/normalization) | Softmax as probability distribution |
| Backpropagation | Matrix transpose (Wᵀ in backward pass) | Chain rule | — |
| RLHF | — | Constrained optimization / Lagrange multipliers | KL divergence, MLE |

Example explanation (any cell): **Attention ↔ Dot products.** Attention scores S = QKᵀ compute the dot product between each query and key vector. From Phase 1, the dot product measures similarity (alignment) between vectors. High dot product = vectors point in similar directions = the query "matches" the key = high attention weight. This is the same geometric meaning as in Lesson 10, but applied to learned representations.
