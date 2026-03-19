# Lesson 53: The Perceptron -- How a Single Neuron Works

[← Applied Statistics](../phase3-prob-stats/lesson-48-applied-statistics.md) | [Back to TOC](../README.md) | [Next: Gradient Descent →](lesson-54-gradient-descent.md)

---

**Welch Ch. 1 | Hours: 8-10h | Prereqs: [39]**

## Core Learning

- The perceptron model: weighted sum of inputs + bias, passed through an activation function
- This is just a dot product followed by a nonlinearity -- you already know both pieces
- Activation functions: step function (original perceptron), sigmoid, ReLU -- and why ReLU won
- A single perceptron as a linear classifier: it draws a decision boundary (a hyperplane in input space)
- The XOR problem: a single perceptron cannot solve it -- this is why hidden layers exist
- Decision boundary as hyperplane: the weight vector is the normal to the boundary, bias shifts it

## Watch -- Primary

1. **Welch Labs -- "ChatGPT is made from 100 million of these [The Perceptron]"** (Ch. 1 video)
   - https://www.youtube.com/watch?v=l-CjXFmcVzY
   - *Traces the perceptron from its 1950s origins through to modern neural networks. Historical narrative, hardware demonstrations, and geometric intuition.*

2. **3Blue1Brown -- "But what is a neural network?" | Deep Learning Ch. 1**
   - https://www.youtube.com/watch?v=aircAruvnKk
   - *The canonical visual explanation. After Welch's historical context, Grant gives you the mathematical structure.*

## Watch -- Secondary

3. **StatQuest -- Neural Networks / Deep Learning playlist**
   - https://www.youtube.com/playlist?list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1
   - *Josh Starmer walks through neural network fundamentals with clear visuals. Good supplement for the perceptron and early network lessons.*

## Read

- **Welch Labs -- *The Illustrated Guide to AI*, Ch. 1: The Perceptron**
  - http://www.welchlabs.com/resources/ai-book
  - *The book's first chapter pairs with the video. Historical narrative, hardware demos, and exercises.*
- **Michael Nielsen -- "Neural Networks and Deep Learning," Chapter 1**
  - http://neuralnetworksanddeeplearning.com/chap1.html
- **colah -- "Neural Networks, Manifolds, and Topology"**
  - http://colah.github.io/posts/2014-03-NN-Manifolds-Topology/

## Do

**1. Implement a single neuron from scratch (Python, no libraries)**

Write a `Neuron` class with:
- `weights`: list of floats, randomly initialized
- `bias`: float
- `forward(inputs)`: compute `sum(w*x for w,x in zip(weights, inputs)) + bias`, then apply a step function (return 1 if positive, 0 otherwise)

**2. Train on AND and OR gates**

Implement the perceptron learning rule:
```
for each (input, target):
    prediction = neuron.forward(input)
    error = target - prediction
    weights += learning_rate * error * input
    bias += learning_rate * error
```

Train until convergence on AND and OR truth tables. Print the learned weights and bias.

**3. Attempt XOR — and fail**

Try training on XOR: `(0,0)→0, (0,1)→1, (1,0)→1, (1,1)→0`. The perceptron will NOT converge. Run for 1000 epochs and print the accuracy — it should stay at ~50-75%.

**4. Visualize why XOR fails**

Plot all four input points color-coded by class (0 = red, 1 = blue). Draw the decision boundary `w1*x1 + w2*x2 + b = 0` as a line. For AND and OR, the line separates the classes cleanly. For XOR, no single line can — this is the motivation for hidden layers.

**5. Solve XOR with a 2-layer network**

Manually construct a 2-layer network (2 hidden neurons + 1 output neuron) that solves XOR. Hint: one hidden neuron computes AND, the other computes OR, and the output computes the difference. Verify it produces correct outputs for all 4 inputs.

## ML & Alignment Connection

Every neuron in every AI system -- GPT, Claude, image classifiers -- does exactly this: dot product + nonlinearity. The entire edifice of modern AI is this atomic operation repeated billions of times.

The choice of activation function has alignment implications. Sigmoid's vanishing gradients mean safety-relevant signals can be lost in deep networks. Understanding the atomic unit is prerequisite to understanding alignment-relevant circuits. Modern alignment research explores whether specific activation patterns correspond to safety-relevant behaviors -- for instance, whether "refusal" behavior in a language model is mediated by specific neurons.
