# Lesson 16: Loss Landscapes and Local Minima

[← Optimization](lesson-15-optimization.md) | [Back to TOC](../README.md) | [Next: Probability →](../phase3-probability/lesson-17-probability.md)

---

## 🎯 Core Learning

- Loss as a function of all parameters: a surface in absurdly high-dimensional space
- Local minima, saddle points, and plateaus
- Why high-dimensional landscapes are actually *easier* (saddle points dominate, not local minima)
- Loss landscape visualization techniques
- Generalization: why memorizing training data fails on new data
- The double descent phenomenon

## 📺 Watch

- **3Blue1Brown — "But what is a neural network?" | Deep Learning Ch. 1**
  - https://www.youtube.com/watch?v=aircAruvnKk

## 📖 Read

- **"Visualizing the Loss Landscape of Neural Nets" (Li et al., 2018)** — skim for the stunning visualizations
- **colah's blog — "Neural Networks, Manifolds, and Topology"**
  - http://colah.github.io/posts/2014-03-NN-Manifolds-Topology/

## 🔨 Do

- Visualize the loss landscape of a tiny 2-parameter network
- Implement early stopping and see its effect on generalization

## 🔗 ML Connection

The shape of the loss landscape is intimately connected to alignment. When we train a model to be "helpful and harmless," the loss landscape determines *which* behaviors emerge. Singularities in the loss landscape (from singular learning theory) are an active area of alignment research.
