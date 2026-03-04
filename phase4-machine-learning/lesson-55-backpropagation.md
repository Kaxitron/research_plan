# Lesson 55: Backpropagation -- The F=ma of AI

[< Gradient Descent](lesson-54-gradient-descent.md) | [Back to TOC](../README.md) | [Next: Deep Learning >](lesson-56-deep-learning.md)

---

> **Welch Labs framing:** Welch calls backpropagation "the F=ma of artificial intelligence" -- just as Newton's second law is the one equation that powers all of classical mechanics, backprop is the one algorithm that powers all of deep learning. The geometric treatment of gradients flowing backward through the folded-space picture from Part 1 is exceptional.

> **Karpathy framing:** In Lecture 1 (micrograd), Karpathy builds a tiny autograd engine from scratch so you see every gradient computed by hand. In Lecture 5 (backprop ninja), you manually backpropagate through an entire MLP -- painful and transformative. Together they give you the computational and the mathematical side.

## Core Learning

- Chain rule applied on computation graphs: every forward operation has a local gradient; backprop chains them
- Forward pass: compute values node by node from input to loss
- Backward pass: compute gradients node by node from loss to parameters
- Vanishing gradients: why deep sigmoid/tanh networks were historically hard to train (gradients shrink exponentially)
- Exploding gradients: the opposite failure mode (gradients grow exponentially), mitigated by gradient clipping
- Skip / residual connections: the architectural trick that solved vanishing gradients and enabled depth
- Weight initialization: random but scaled correctly (Xavier, He initialization) -- without it, activations and gradients blow up or collapse
- Gradient checking: finite-difference verification that your analytical gradients are correct
- Batch normalization: keeping activations well-behaved across layers

## Watch -- Primary

1. **Welch Labs -- "The F=ma of Artificial Intelligence [Backpropagation, How Models Learn Part 2]"**
   - https://www.youtube.com/watch?v=GKZoOHXGcLo
   - *Book: Welch Labs, "The Illustrated Guide to AI," Ch. 3: Backpropagation*
   - *30 minutes. Welch frames backprop as the fundamental law of deep learning -- the way F=ma is the fundamental law of classical mechanics. The geometric treatment of gradients flowing backward through the folded-space picture from Part 1 is exceptional.*

2. **Karpathy -- "The spelled-out intro to neural networks and backpropagation: building micrograd" (Zero to Hero #1)**
   - https://www.youtube.com/watch?v=VMj-3S1tku0
   - *~2.5 hours. You build a tiny autograd engine from scratch. Every gradient is computed by hand before being automated. This is where backprop stops being abstract.*

3. **Karpathy -- "Becoming a Backprop Ninja" (Zero to Hero #5)**
   - https://www.youtube.com/watch?v=q8SA3rM6ckI
   - *You manually backpropagate through an entire MLP -- cross-entropy, linear layers, tanh, batchnorm. No autograd. Painful and transformative.*

4. **Karpathy -- "Activations & Gradients, BatchNorm" (Zero to Hero #4)**
   - https://www.youtube.com/watch?v=P6sfmUTpUmc

## Watch -- Secondary

5. **3Blue1Brown -- "Backpropagation, intuitively" | Deep Learning Ch. 3**
   - https://www.youtube.com/watch?v=Ilg3gGewQ5U
6. **3Blue1Brown -- "Backpropagation calculus" | Deep Learning Ch. 4**
   - https://www.youtube.com/watch?v=tIeHLnjs5U8

## Read

- **Welch Labs -- *The Illustrated Guide to AI*, Ch. 3: Backpropagation**
  - http://www.welchlabs.com/resources/ai-book
  - *"The F=ma of artificial intelligence." The book walks through backprop with code and exercises.*
- **Stanford CS231n -- "Backpropagation" notes**
  - https://cs231n.github.io/optimization-2/

## Do

- **The Backprop Ninja exercise:** manually compute gradients through cross-entropy, linear layers, tanh, batchnorm -- no autograd
- **Gradient checking:** implement numerical gradient checking (finite differences) and verify your analytical gradients match
- **micrograd extension:** after completing Karpathy's micrograd, add support for a new operation (e.g., division, exp) and verify with gradient checking

## ML and Alignment Connection

Residual connections create "information highways" central to how transformers work. The residual stream IS the backbone of transformer architecture. Understanding gradient flow explains *why* transformers have the structure they do.

**Gradient flow through residual connections** is also why transformers are interpretable at all. Without residual connections, the gradient (and information) must pass sequentially through every layer, making the computation opaque and gradient-starved. With them, each layer can directly contribute to the output, making it possible to attribute specific behaviors to specific components. This architectural choice is what makes mechanistic interpretability of transformers feasible.
