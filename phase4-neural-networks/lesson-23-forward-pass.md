# Lesson 23: The Forward Pass as Matrix Multiplications

[← Single Neuron](lesson-22-single-neuron.md) | [Back to TOC](../README.md) | [Next: Backpropagation →](lesson-24-backprop.md)

---

## 🎯 Core Learning

- A layer of neurons = single matrix multiplication + bias + activation
- The forward pass: input → layer 1 → layer 2 → ... → output
- This is just composition of functions! f₃(f₂(f₁(x)))
- Batch processing: multiple inputs simultaneously (wider matrices)
- Every matrix IS a linear transformation — Lessons 1-8 apply directly
- Softmax: turning raw scores into probabilities

## 📺 Watch

- **Karpathy — "Building makemore" (Lecture 2)**
  - https://www.youtube.com/watch?v=PaCmpygFfXo
- **Karpathy — "Building makemore Part 2: MLP" (Lecture 3)**
  - https://www.youtube.com/watch?v=TCH_1BHY58I

## 📖 Read

- **Nelson Elhage — "Transformers for Software Engineers"**
  - https://blog.nelhage.com/post/transformers-for-software-engineers/

## 🔨 Do

- Implement a 2-layer MLP from scratch in NumPy (no PyTorch)
- Train on MNIST digit classification
- Visualize weight matrices as images — what patterns do they learn?

## 🔗 ML Connection

When interpretability researchers say "the model moves information through the residual stream," they mean each matrix multiplication's output gets added back to a running total. Understanding the forward pass as composed matrix multiplications is THE prerequisite for reading Anthropic's papers.
