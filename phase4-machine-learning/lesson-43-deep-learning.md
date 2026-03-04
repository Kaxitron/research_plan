# Lesson 43: Deep Learning -- Why Depth Works

[← Backpropagation](lesson-42-backpropagation.md) | [Back to TOC](../README.md) | [Next: AlexNet and ConvNets →](lesson-44-alexnet-convnets.md)

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

- Build a 3+ layer MLP for character-level language modeling (following makemore)
- Monitor activation statistics across layers -- plot histograms of activations at each layer during training
- Implement BatchNorm from scratch and compare training with/without it
- Visualize what happens to the activation distribution as you go deeper, before and after BatchNorm

## ML & Alignment Connection

Depth enables compositional representations -- each layer builds on the previous. This is why deep networks learn abstract features: early layers detect edges, middle layers compose them into textures and parts, later layers recognize objects and concepts.

For alignment, representation learning determines WHAT the model learns to represent internally. Understanding this is crucial for interpretability -- aligned models need representations that humans can inspect. If a model's internal representations are entangled and opaque, verifying alignment becomes impossible. The goal of mechanistic interpretability is precisely to understand what each layer has learned to represent, and whether those representations encode the concepts we need for safe behavior.
