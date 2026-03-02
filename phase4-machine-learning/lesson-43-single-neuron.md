# Lesson 43: How a Single Neuron Works

[← Applied Statistics](../phase3-prob-stats/lesson-42-applied-statistics.md) | [Back to TOC](../README.md) | [Next: Forward Pass →](lesson-44-forward-pass.md)

---

## 🎯 Core Learning

- A neuron: linear transform (weights · inputs + bias) → nonlinear activation
- This is just a dot product followed by a squish! You already know both pieces.
- Activation functions: sigmoid, tanh, ReLU and why ReLU won
- A single neuron as a linear classifier (it draws a hyperplane)
- Universal approximation theorem: enough neurons can approximate any function (but can they *learn* to?)

## 📺 Watch — Primary

1. **Welch Labs — "ChatGPT is made from 100 million of these [The Perceptron]"**
   - https://www.youtube.com/watch?v=l-CjXFmcVzY
   - *📖 Book: Welch Labs, "The Illustrated Guide to AI," Ch. 1: The Perceptron*
   - *24 minutes. Welch Labs traces the perceptron from its 1950s origins through to modern neural networks — hardware demonstrations, historical narrative, and geometric intuition. Pairs perfectly with 3B1B's approach. Watch this FIRST for motivation.*

2. **3Blue1Brown — "But what is a neural network?" | Deep Learning Ch. 1**
   - https://www.youtube.com/watch?v=aircAruvnKk
   - *The canonical visual explanation. After Welch's historical context, Grant gives you the mathematical structure.*

## 📺 Watch — Secondary

3. **Karpathy — Building micrograd** (review relevant sections on neurons)

4. **StatQuest — Neural Networks / Deep Learning playlist**
   - https://www.youtube.com/playlist?list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1
   - *Josh Starmer walks through neural network fundamentals with clear visuals. Good supplement for lessons 40–42.*

## 📖 Read

- **Welch Labs — *The Illustrated Guide to AI*, Ch. 1: The Perceptron**
  - http://www.welchlabs.com/resources/ai-book
  - *The book's first chapter pairs with the video. Historical narrative, hardware demos, and exercises.*
- **Michael Nielsen — "Neural Networks and Deep Learning," Chapter 1**
  - http://neuralnetworksanddeeplearning.com/chap1.html
- **colah — "Neural Networks, Manifolds, and Topology"**
  - http://colah.github.io/posts/2014-03-NN-Manifolds-Topology/

## 🔨 Do

- Implement a single neuron in Python (no libraries), train it on AND, OR, XOR
- Discover that XOR *requires* a hidden layer — this is why deep networks exist

## 🔗 ML & Alignment Connection

Every neuron in every AI system — GPT, Claude, image classifiers — does exactly this: dot product + nonlinearity. The entire edifice of modern AI is this atomic operation repeated billions of times.

The choice of activation function has alignment implications. Sigmoid's vanishing gradients mean safety-relevant signals can be lost in deep networks. ReLU's "dead neurons" mean some capacity is permanently wasted. Modern alignment research explores whether specific activation patterns correspond to safety-relevant behaviors — for instance, whether "refusal" behavior in a language model is mediated by specific neurons. Understanding the atomic unit is prerequisite to understanding how alignment-relevant circuits are built from these units.
