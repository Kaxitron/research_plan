# Lesson 24: Backpropagation Through the Full Network

[← Forward Pass](lesson-23-forward-pass.md) | [Back to TOC](../README.md) | [Next: Attention →](lesson-25-attention.md)

---

## 🎯 Core Learning

- Applying the chain rule through every layer
- Gradient flow: how error propagates backward
- Vanishing and exploding gradients: why deep networks were historically hard
- Residual connections: the trick that solved vanishing gradients
- Batch normalization: keeping activations well-behaved
- Weight initialization: random but scaled correctly

## 📺 Watch

- **Karpathy — "Becoming a Backprop Ninja" (Lecture 5)**
  - https://www.youtube.com/watch?v=q8SA3rM6ckI
  - *You manually backpropagate through an entire MLP. Painful and transformative.*
- **Karpathy — "Activations & Gradients, BatchNorm" (Lecture 4)**
  - https://www.youtube.com/watch?v=P6sfmUTpUmc

## 📖 Read

- **Stanford CS231n — "Backpropagation" notes**
  - https://cs231n.github.io/optimization-2/

## 🔨 Do

- **The Backprop Ninja exercise:** manually compute gradients through cross-entropy, linear layers, tanh, batchnorm — no autograd

## 🔗 ML Connection

Residual connections create "information highways" central to how transformers work. The residual stream IS the backbone of transformer architecture. Understanding gradient flow explains *why* transformers have the structure they do.
