# Lesson 42: Backpropagation Through the Full Network

[← Forward Pass](lesson-41-forward-pass.md) | [Back to TOC](../README.md) | [Next: Attention →](lesson-43-attention.md)

---

## 🎯 Core Learning

- Applying the chain rule through every layer
- Gradient flow: how error propagates backward
- Vanishing and exploding gradients: why deep networks were historically hard
- Residual connections: the trick that solved vanishing gradients
- Batch normalization: keeping activations well-behaved
- Weight initialization: random but scaled correctly

## 📺 Watch — Primary

1. **Welch Labs — "The F=ma of Artificial Intelligence [Backpropagation, How Models Learn Part 2]"**
   - https://www.youtube.com/@WelchLabs (search "How Models Learn Part 2")
   - *30 minutes. Welch frames backprop as the fundamental law of deep learning — the way F=ma is the fundamental law of classical mechanics. The geometric treatment of gradients flowing backward through the folded-space picture from Part 1 is exceptional.*

2. **Karpathy — "Becoming a Backprop Ninja" (Lecture 5)**
   - https://www.youtube.com/watch?v=q8SA3rM6ckI
   - *You manually backpropagate through an entire MLP. Painful and transformative.*

3. **Karpathy — "Activations & Gradients, BatchNorm" (Lecture 4)**
   - https://www.youtube.com/watch?v=P6sfmUTpUmc

## 📺 Watch — Secondary

4. **3Blue1Brown — "Backpropagation, intuitively" | Deep Learning Ch. 3**
   - https://www.youtube.com/watch?v=Ilg3gGewQ5U
5. **3Blue1Brown — "Backpropagation calculus" | Deep Learning Ch. 4**
   - https://www.youtube.com/watch?v=tIeHLnjs5U8

## 📖 Read

- **Stanford CS231n — "Backpropagation" notes**
  - https://cs231n.github.io/optimization-2/

## 🔨 Do

- **The Backprop Ninja exercise:** manually compute gradients through cross-entropy, linear layers, tanh, batchnorm — no autograd

## 🔗 ML Connection

Residual connections create "information highways" central to how transformers work. The residual stream IS the backbone of transformer architecture. Understanding gradient flow explains *why* transformers have the structure they do.
