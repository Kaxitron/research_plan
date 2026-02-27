# Lesson 14: Partial Derivatives and Gradients — Going Deeper

[← Matrix Calculus](lesson-13-matrix-calculus.md) | [Back to TOC](../README.md) | [Next: The Chain Rule →](lesson-15-chain-rule.md)

---

## 🎯 Core Learning

- Gradients as vectors perpendicular to contour lines (geometric picture)
- The gradient always points in the direction of steepest ascent
- Directional derivatives: how fast does the function change if I walk in *this* direction?
- Multivariable chain rule: the key identity that makes backpropagation work

## 📺 Watch

- **3Blue1Brown — "Gradient descent, how neural networks learn" | Deep Learning Ch. 2**
  - https://www.youtube.com/watch?v=IHZwWFHWa-w
- **Khan Academy — Gradient and directional derivatives** (extra practice)

## 📖 Read

- **colah's blog — "Calculus on Computational Graphs: Backpropagation"**
  - http://colah.github.io/posts/2015-08-Backprop/
  - *Absolutely essential.* Chris Olah explains backprop as the chain rule applied to computation graphs.

## 🔨 Do

- Visualize gradient fields of 2D functions (matplotlib contour plots with arrows)
- Implement numerical gradient descent on a simple 2D function — watch the point slide downhill

## 🔗 ML Connection

The gradient is THE signal that tells a neural network how to learn. Understanding gradients geometrically gives you intuition for why some networks train well and others don't — it's about the *shape* of the loss landscape.
