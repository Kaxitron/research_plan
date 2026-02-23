# Lesson 22: How a Single Neuron Works

[← Bayesian Inference](../phase3-probability/lesson-21-bayesian-inference.md) | [Back to TOC](../README.md) | [Next: Forward Pass →](lesson-23-forward-pass.md)

---

## 🎯 Core Learning

- A neuron: linear transform (weights · inputs + bias) → nonlinear activation
- This is just a dot product followed by a squish! You already know both pieces.
- Activation functions: sigmoid, tanh, ReLU and why ReLU won
- A single neuron as a linear classifier (it draws a hyperplane)
- Universal approximation theorem: enough neurons can approximate any function (but can they *learn* to?)

## 📺 Watch

- **3Blue1Brown — "But what is a neural network?" | Deep Learning Ch. 1**
  - https://www.youtube.com/watch?v=aircAruvnKk
- **Karpathy — Building micrograd** (review relevant sections)

## 📖 Read

- **Michael Nielsen — "Neural Networks and Deep Learning," Chapter 1**
  - http://neuralnetworksanddeeplearning.com/chap1.html
- **colah — "Neural Networks, Manifolds, and Topology"**
  - http://colah.github.io/posts/2014-03-NN-Manifolds-Topology/

## 🔨 Do

- Implement a single neuron in Python (no libraries), train it on AND, OR, XOR
- Discover that XOR *requires* a hidden layer — this is why deep networks exist

## 🔗 ML Connection

Every neuron in every AI system — GPT, Claude, image classifiers — does exactly this: dot product + nonlinearity. The entire edifice of modern AI is this atomic operation repeated billions of times.
