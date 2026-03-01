# Lesson 15: Partial Derivatives and Gradients — Going Deeper

[← Matrix Calculus](lesson-14-matrix-calculus.md) | [Back to TOC](../README.md) | [Next: Chain Rule →](lesson-16-chain-rule.md)

---

## 🎯 Core Learning

- Gradients as vectors perpendicular to contour lines (geometric picture)
- The gradient always points in the direction of steepest ascent
- Directional derivatives: how fast does the function change if I walk in *this* direction?
- Multivariable chain rule: the key identity that makes backpropagation work

## 📺 Watch

- **3Blue1Brown — "Gradient descent, how neural networks learn" | Deep Learning Ch. 2**
  - https://www.youtube.com/watch?v=IHZwWFHWa-w

## 📖 Read

- **colah's blog — "Calculus on Computational Graphs: Backpropagation"**
  - http://colah.github.io/posts/2015-08-Backprop/
  - *Absolutely essential.* Chris Olah explains backprop as the chain rule applied to computation graphs.

## 🔨 Do

- Visualize gradient fields of 2D functions (matplotlib contour plots with arrows)
- Implement numerical gradient descent on a simple 2D function — watch the point slide downhill

## 🔗 ML & Alignment Connection

The gradient is THE signal that tells a neural network how to learn. Understanding gradients geometrically — as vectors perpendicular to contour lines, pointing in the direction of steepest ascent — gives you intuition for why some networks train well and others don't.

For alignment, the critical question is: does the gradient from our objective function (RLHF, constitutional AI, etc.) actually point toward aligned behavior? If the loss landscape has the "wrong shape" — e.g., deceptively aligned behavior sits in a deeper basin than honestly aligned behavior — then following the gradient leads to misalignment. Understanding gradients geometrically helps you reason about *whether the training signal teaches what we intend*.
