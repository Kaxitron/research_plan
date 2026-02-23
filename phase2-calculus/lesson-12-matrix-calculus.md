# Lesson 12: Matrix Calculus — Bridging to Backpropagation

[← LA Capstone](../phase1-linear-algebra/lesson-11-capstone.md) | [Back to TOC](../README.md) | [Next: Gradients →](lesson-13-gradients.md)

---

## 🎯 Core Learning

- Derivatives of scalar functions (quick refresh)
- Partial derivatives: how a function changes when you wiggle *one* input
- The gradient vector: collecting all partial derivatives into one object that points "uphill"
- Jacobian matrices: when your function maps vectors to vectors, the derivative is a *matrix*
- Key matrix calculus results: derivatives of **Ax**, **xᵀAx**, and why these matter

## 📺 Watch

- **3Blue1Brown — Essence of Calculus, Chapter 1:** "The essence of calculus"
  - https://www.youtube.com/watch?v=WUvTyaaNkzM
- **3Blue1Brown — Essence of Calculus, Chapter 10:** "Taylor series"

## 📖 Read

- **"The Matrix Calculus You Need for Deep Learning" by Parr & Howard**
  - https://arxiv.org/abs/1802.01528
  - Designed specifically for ML practitioners. Essential reading.
- **MML Book, Chapter 5** — vector calculus

## 🔨 Do

- Compute the gradient of f(x,y) = x²y + sin(xy) by hand
- Compute the Jacobian of a simple 2→2 function
- Write Python code that numerically approximates gradients and compares to analytical results

## 🔗 ML Connection

Every parameter in a neural network gets updated by its gradient. The Jacobian tells you how a layer's output changes with its input — exactly what backpropagation multiplies through. The gradient of the loss is literally the "direction to adjust weights."
