# Lesson 56: Deep Learning -- Why Depth Works

[← Backpropagation](lesson-55-backpropagation.md) | [Back to TOC](../README.md) | [Next: AlexNet and ConvNets →](lesson-57-alexnet-convnets.md)

---

**Welch Ch. 4 | Karpathy ZtH #2-3 (makemore), ZtH #4 (activations/BatchNorm) | Hours: 10-12h | Prereqs: [42]**

## Core Learning

- Universal approximation theorem: a single hidden layer can approximate any function -- but depth makes it exponentially more efficient
- Depth vs width: adding a layer adds another "fold" of space; adding width makes each fold more complex
- ReLU folding: each ReLU neuron folds the input space along a hyperplane, composing these folds creates rich piecewise-linear decision boundaries
- Batch normalization: keeping activations well-behaved across layers by normalizing their statistics
- Representation learning: each layer learns increasingly abstract features -- edges, textures, objects, concepts
- The training pipeline: initialization, forward pass, loss, backward pass, parameter update, repeat

## Watch -- Primary

1. **Welch Labs -- "Why Deep Learning Works Unreasonably Well" (Ch. 4 video)**
   - https://www.youtube.com/watch?v=qx7hirqgfuU
   - *Shows why depth matters more than width with the Belgium/Netherlands example extended to multi-layer networks. The geometric view of ReLU folding is exceptional.*

2. **Karpathy -- "Building makemore" (Lecture 2)**
   - https://www.youtube.com/watch?v=PaCmpygFfXo
3. **Karpathy -- "Building makemore Part 2: MLP" (Lecture 3)**
   - https://www.youtube.com/watch?v=TCH_1BHY58I
   - *Build a character-level language model with an MLP. This is where theory becomes code.*

4. **Karpathy -- "Becoming a Backprop Ninja" (Lecture 4: activations, BatchNorm)**
   - https://www.youtube.com/watch?v=P6sfmUTpUmc
   - *Deep dive into activation statistics, gradient flow, and BatchNorm. You will understand WHY training deep networks was historically hard.*

## Watch -- Secondary

5. **3Blue1Brown -- Neural Networks series (remaining chapters)**
   - *Complete the 3B1B deep learning series for visual reinforcement of depth, gradient flow, and learned representations.*

## Read

- **Welch Labs -- *The Illustrated Guide to AI*, Ch. 4: Deep Learning**
  - http://www.welchlabs.com/resources/ai-book
  - *The book chapter on why depth works, with code and exercises.*

## Do

**1. Build makemore (bigram model) — follow Karpathy ZtH #2**

Follow Karpathy's makemore Lecture 2 from scratch:
- Load a dataset of names
- Build a character-level bigram model using a 27×27 count matrix
- Convert counts to probabilities, sample new names
- Reframe as a neural network: one-hot input → embedding → logits → softmax → cross-entropy loss
- Train with gradient descent

This is your first real language model. It's terrible — but it generates pronounceable gibberish.

**2. MLP language model — follow Karpathy ZtH #3**

Follow makemore Part 2 to build an MLP character-level model:
- Embedding layer: characters → learned vectors
- Hidden layer(s) with tanh activation
- Output layer → softmax → cross-entropy

Train on the names dataset. Generate samples — they should be noticeably better than the bigram model.

**3. Activation diagnostics — follow Karpathy ZtH #4**

This is where you see WHY deep networks are hard to train. Following Karpathy's Lecture 4:
- Plot histograms of activations at each layer during training. Are they saturated (all near ±1 for tanh)? Are they dead (all zero for ReLU)?
- Plot histograms of gradients at each layer. Are they vanishing? Exploding?
- Implement Kaiming initialization (`std = sqrt(2/fan_in)` for ReLU) and show it fixes the activation distributions

**4. Implement BatchNorm from scratch**

Following Karpathy ZtH #4:
- Compute running mean and variance during training
- Normalize activations: `x_hat = (x - mean) / sqrt(var + eps)`
- Learn scale and shift: `y = gamma * x_hat + beta`
- Compare training curves with and without BatchNorm — BatchNorm should converge faster and be less sensitive to learning rate

## ML & Alignment Connection

Depth enables compositional representations -- each layer builds on the previous. This is why deep networks learn abstract features: early layers detect edges, middle layers compose them into textures and parts, later layers recognize objects and concepts.

For alignment, representation learning determines WHAT the model learns to represent internally. Understanding this is crucial for interpretability -- aligned models need representations that humans can inspect. If a model's internal representations are entangled and opaque, verifying alignment becomes impossible. The goal of mechanistic interpretability is precisely to understand what each layer has learned to represent, and whether those representations encode the concepts we need for safe behavior.
