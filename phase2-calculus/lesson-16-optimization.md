# Lesson 16: Optimization and Gradient Descent

[← Chain Rule](lesson-15-chain-rule.md) | [Back to TOC](../README.md) | [Next: Constrained Optimization →](lesson-17-constrained-optimization.md)

---

## 🎯 Core Learning

- Gradient descent: step opposite the gradient, scaled by learning rate
- Stochastic gradient descent (SGD): random mini-batches instead of all data
- Learning rate: too big = overshoot, too small = too slow
- Momentum: "rolling downhill with inertia"
- Adam optimizer: the adaptive method used for almost all modern training
- Convexity vs. non-convexity: why neural network optimization is hard in theory but works in practice

## 📺 Watch

- **Andrej Karpathy — "Building micrograd"** (Lecture 1, ~2.5 hours)
  - https://www.youtube.com/watch?v=VMj-3S1tku0
  - *Build a complete autograd engine and neural network from scratch.*

## 📖 Read

- **Stanford CS231n notes on Optimization**
  - https://cs231n.github.io/optimization-1/ and /optimization-2/

## 🔨 Do

- Complete Karpathy's micrograd: implement `Value` class with automatic differentiation
- Train a small neural network on simple 2D data
- Experiment: learning rate 0.001 vs 0.1 vs 10 — what happens?

## 🔗 ML Connection

The optimizer shapes what solutions the network finds. For alignment, the "attractor basins" in the loss landscape determine what behaviors emerge. Understanding optimization helps you reason about: "Why does the network learn *this* strategy instead of *that* one?"
