# Exam 4A: Neural Networks & Machine Learning

**The Path to AI Alignment -- Lessons 53–64 Comprehensive Assessment**

---

| | |
|---|---|
| **Part I** | 10 short questions, 30 minutes, 50 points |
| **Part II** | Implementation project, 5 hours, 100 points |
| **Total Points** | 150 |
| **Materials** | Part I: Pencil and paper only. Part II: Python, NumPy, any text editor. No ML frameworks (PyTorch/TensorFlow) unless explicitly stated. |

> **Advice -- Part I:** Each question should take 2-3 minutes. Write concisely -- 2-3 sentences max per answer unless otherwise specified. These test understanding and intuition, not computation.

> **Advice -- Part II:** This is a build project, not a written exam. You will construct a working system from scratch. Read ALL milestones before starting. Commit working code at each milestone -- partial credit is generous for working intermediate stages.

> *"What I cannot create, I do not understand." -- Richard Feynman*

---

# Part I: Concepts and Intuition (50 points, 30 minutes)

---

## Q1 (5 pts) -- The Single Neuron (Lesson 53)

A single neuron with sigmoid activation computes y = sigma(w^T x + b). This neuron can represent AND, OR, and NOT -- but not XOR.

In 2-3 sentences: why can't a single neuron compute XOR? What is the geometric reason, and what is the minimum architecture that CAN compute XOR?

---

## Q2 (5 pts) -- Gradient Descent and Loss Functions (Lesson 54)

You are training a binary classifier. Your colleague suggests using L2 loss (y - y_hat)^2 instead of binary cross-entropy -[y log(y_hat) + (1-y) log(1-y_hat)].

What goes wrong with L2 loss when the model outputs a confident wrong prediction (y = 1, y_hat near 0)? Compare the gradient magnitude of both losses in this regime. Which provides a stronger learning signal, and why?

---

## Q3 (5 pts) -- Backpropagation (Lesson 55)

A network has 50 layers, each computing h_{l+1} = sigma(W_l h_l). During backpropagation, the gradient at layer l involves the product of matrices: dL/dh_l = (product from k=l to 49 of D_k W_k) dL/dh_50, where D_k is a diagonal matrix of activation derivatives.

Name the two gradient pathologies this product can cause. For each, name one architectural technique introduced after 2010 that mitigates it.

---

## Q4 (5 pts) -- Depth, Width, and Regularization (Lesson 56)

The universal approximation theorem says a single hidden layer of sufficient width can approximate any continuous function. Yet in practice, deep narrow networks outperform shallow wide ones.

In 2-3 sentences: why does depth help? Give an intuition based on function composition and the number of linear regions a ReLU network can express as a function of depth vs. width.

---

## Q5 (5 pts) -- CNNs and AlexNet (Lesson 57)

Name three specific design choices that AlexNet (2012) introduced or popularized that broke from prior practice. For one of them, explain why it mattered -- what problem did it solve?

---

## Q6 (5 pts) -- Scaling Laws and Emergence (Lesson 58)

Kaplan et al. (2020) found that language model loss follows a power law: L(N) ~ N^{-alpha} where N is the number of parameters.

The Chinchilla paper (Hoffmann et al., 2022) revised the optimal scaling relationship. What was the key finding about the balance between model size and training data? Why did this change how large models are trained?

---

## Q7 (5 pts) -- Attention (Lesson 59)

In self-attention, Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V.

Why do we divide by sqrt(d_k)? What would happen to the softmax output if we skipped this scaling when d_k is large (say, 512)? Be specific about the effect on gradient flow.

---

## Q8 (5 pts) -- Transformer Architecture (Lesson 60)

A transformer block applies attention followed by an MLP, with residual connections and layer norm around each.

The "residual stream" view (Elhage et al., 2021) says the residual connections create a shared communication channel. Under this view, what do attention heads DO to the residual stream, and what does the MLP DO to it? Answer in one sentence each.

---

## Q9 (5 pts) -- Reinforcement Learning and Reward Hacking (Lesson 63)

A cleaning robot is trained with RL to minimize "dirt detected by its sensors." Instead of cleaning, it learns to cover its sensors.

This is an instance of Goodhart's Law: "When a measure becomes a target, it ceases to be a good measure." Name two ways this problem manifests in LLM training with RLHF, where the "sensor" is a learned reward model.

---

## Q10 (5 pts) -- The LLM Training Pipeline (Lesson 64)

Put these stages in the correct order and, for each, state in one sentence what the model learns or what changes about its behavior:

- Constitutional AI (CAI)
- RLHF with PPO
- Supervised Fine-Tuning (SFT)
- Pre-training (next-token prediction)
- DPO (Direct Preference Optimization)

Note: CAI and DPO are alternatives to RLHF, not sequential stages. Group them appropriately.

---

# Part II: Build Project -- Character-Level Language Model to Attention (100 points, 5 hours)

## Project Overview

You will build a character-level language model from scratch, progressively adding complexity until you have a working miniature transformer. This follows the spirit of Andrej Karpathy's "Zero to Hero" series: every component is built by hand, every gradient is understood.

**Dataset:** Download any small text corpus (Shakespeare, Wikipedia intro paragraphs, song lyrics -- your choice). Minimum 100KB of text.

**Constraint:** No PyTorch, TensorFlow, or JAX for Milestones 1-4. Pure Python + NumPy only. Milestone 5 permits PyTorch.

---

## Milestone 1: Bigram Model (15 pts, ~30 min)

**Build a character-level bigram language model.**

1. Load your text corpus. Build a character vocabulary (unique characters -> integer indices).
2. Construct a bigram count matrix C where C[i,j] = number of times character j follows character i in the training data.
3. Convert counts to probabilities: P[i,j] = C[i,j] / sum(C[i,:]), with appropriate smoothing.
4. Implement a `generate(seed_char, length)` function that samples from the bigram distribution autoregressively.
5. Compute the negative log-likelihood (NLL) of the model on a held-out validation set.

**Deliverable:** Print 5 generated samples of 200 characters each. Report the validation NLL.

---

## Milestone 2: MLP Language Model with Manual Backprop (25 pts, ~75 min)

**Build Bengio et al.'s (2003) neural language model -- a feedforward network that takes a context window and predicts the next character.**

1. Define the architecture:
   - Embedding layer: each character maps to a learned vector of dimension d_emb = 16
   - Context window: concatenate embeddings of the previous 3 characters -> input dimension = 48
   - Hidden layer: 128 neurons, tanh activation
   - Output layer: linear projection to vocabulary size, followed by softmax
2. Implement the FULL forward pass in NumPy. Compute cross-entropy loss.
3. Implement the FULL backward pass by hand. Compute gradients for every parameter: W_emb, W_hidden, b_hidden, W_output, b_output. Do NOT use autograd.
4. Train with mini-batch SGD (batch size 32, learning rate you choose). Train for at least 1000 steps.
5. Generate text and compare quality with the bigram model. Report training and validation loss curves.

**Deliverable:** Plot loss vs. training step. Print 5 generated samples. Code for forward AND backward pass with comments explaining each gradient computation.

---

## Milestone 3: Batch Normalization and Residual Connections (15 pts, ~45 min)

**Upgrade the MLP with modern training techniques.**

1. Add batch normalization after the hidden layer (before the activation). Implement the forward pass (normalize, scale, shift) and backward pass for batch norm FROM SCRATCH.
2. Make the network deeper: 3 hidden layers of 128 neurons each with tanh activations.
3. Train the deep network WITHOUT residual connections. Record the gradient norms at each layer during training. Do you observe vanishing gradients?
4. Add residual connections (skip connections) around each hidden layer: h_{l+1} = h_l + f_l(h_l). Retrain. Compare gradient norms and convergence speed.

**Deliverable:** Plot of gradient norms per layer, with and without residual connections. Loss curves comparing shallow (1 layer), deep without residuals, and deep with residuals. Brief written observation (3-5 sentences) on what you see.

---

## Milestone 4: Self-Attention from Scratch (25 pts, ~75 min)

**Replace the MLP context mechanism with self-attention.**

1. Implement a single-head self-attention layer:
   - Input: a sequence of character embeddings, shape (T, d_emb) where T is the context length
   - Compute Q = X W_Q, K = X W_K, V = X W_V where W_Q, W_K, W_V are (d_emb x d_head) learned matrices
   - Compute attention: A = softmax(QK^T / sqrt(d_head)) V
   - Apply a causal mask: set attention scores to -infinity for positions j > i (no looking at the future)
2. Implement the backward pass through attention. This is the hardest part. You need gradients through:
   - The softmax (use the Jacobian: d softmax_i / d z_j = softmax_i (delta_{ij} - softmax_j))
   - The matrix multiplications QK^T and AV
   - The masking operation
3. Build a minimal model: embedding -> single self-attention layer -> layer norm -> linear output -> softmax over vocabulary.
4. Train on your corpus. Compare text quality with the MLP model from Milestone 2.

**Deliverable:** Working attention implementation with manually coded backward pass. Visualization of the attention matrix (T x T heatmap) for a sample input after training. Print 5 generated samples and report validation loss.

---

## Milestone 5: Mini-Transformer with PyTorch (20 pts, ~60 min)

**Now rebuild in PyTorch and scale up.**

You may use PyTorch for this milestone (autograd handles the backward pass).

1. Implement a mini-transformer with:
   - Learned character embeddings + positional embeddings
   - 2 transformer blocks, each containing: multi-head self-attention (2 heads), layer norm, MLP (hidden size 256), layer norm, residual connections
   - Context length T = 32 characters
   - Train on your full corpus with Adam optimizer
2. Train for 5000+ steps. Use learning rate warmup (100 steps) + cosine decay.
3. Implement top-k sampling and temperature scaling for generation.
4. Compare generated text quality across all milestones: bigram -> MLP -> attention -> transformer.

**Deliverable:** Training loss curve. Generated samples at temperature 0.5, 1.0, and 1.5. Brief comparison (5 sentences) of how text quality improved across milestones and what each architectural addition contributed.

---

## Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| Milestone 1: Bigram | 15 | Working generation, correct NLL computation |
| Milestone 2: MLP + manual backprop | 25 | Correct forward/backward, training converges, clear gradient comments |
| Milestone 3: BatchNorm + residuals | 15 | Correct batch norm implementation, gradient norm analysis |
| Milestone 4: Self-attention from scratch | 25 | Working attention with manual backward pass, attention visualization |
| Milestone 5: Mini-transformer | 20 | Working PyTorch transformer, generation with temperature control |

**Partial credit:** Each milestone is graded independently. A working Milestone 1-3 with incomplete Milestone 4-5 earns full credit for the completed milestones.

---

## Stretch Goals (ungraded, for the ambitious)

- **Multi-head attention from scratch (no PyTorch):** Implement 2+ attention heads in NumPy with full manual backward pass. Show that different heads learn different attention patterns.
- **Tokenizer:** Replace character-level tokenization with BPE (byte pair encoding). Implement the BPE algorithm from scratch. Compare model quality.
- **Training dynamics analysis:** Track the following during Milestone 5 training and plot them: (1) gradient norm per layer, (2) largest Hessian eigenvalue (use power iteration), (3) attention entropy per head. Do you observe edge-of-stability? Do attention patterns crystallize at a specific point in training?
- **Karpathy's makemore:** Reproduce the name generation task from Karpathy's "makemore" series. Use a dataset of names and generate plausible new names.
- **RL fine-tuning:** After training your Milestone 5 model, fine-tune it with REINFORCE to optimize a simple reward (e.g., generate text that contains a target word, or text where every sentence starts with a capital letter). Observe reward hacking if it occurs.
