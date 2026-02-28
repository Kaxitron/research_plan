# Lesson 16: The Chain Rule — This IS Backpropagation

[← Gradients](lesson-15-gradients.md) | [Back to TOC](../README.md) | [Next: Optimization →](lesson-17-optimization.md)

---

## 🎯 Core Learning

- Single-variable chain rule refresh: d/dx f(g(x)) = f'(g(x)) · g'(x)
- Multivariable chain rule: how gradients flow backward through composed functions
- Computation graphs: every neural network is a graph of simple operations
- Forward pass vs. backward pass: compute values forward, then gradients backward
- Why "backward" (reverse-mode autodiff) is so much cheaper than "forward" for neural networks

## 📺 Watch (CRITICAL videos)

- **3Blue1Brown — "Backpropagation, intuitively" | Deep Learning Ch. 3**
  - https://www.youtube.com/watch?v=Ilg3gGewQ5U
- **3Blue1Brown — "Backpropagation calculus" | Deep Learning Ch. 4**
  - https://www.youtube.com/watch?v=tIeHLnjs5U8

## 📖 Read

- **Michael Nielsen — "Neural Networks and Deep Learning," Chapter 2**
  - http://neuralnetworksanddeeplearning.com/chap2.html
- Re-read colah's backpropagation blog post with fresh eyes

## 🔨 Do

- Draw a computation graph for L = (wx + b - y)² and manually trace gradients backward
- **Build micrograd (Part 1):** Start Karpathy's Lecture 1 and implement a tiny autograd engine

## 🔗 ML Connection

Backpropagation is the *single most important algorithm* in deep learning. For alignment: understanding backprop lets you reason about *what the training signal actually looks like* for different objectives — central to understanding why models behave the way they do.
