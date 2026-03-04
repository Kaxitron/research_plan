# Lesson 44: AlexNet and Convolutional Neural Networks

[← Deep Learning](lesson-43-deep-learning.md) | [Back to TOC](../README.md) | [Next: Scaling Laws →](lesson-45-scaling-laws.md)

---

**Welch Ch. 5 | Hours: 10-12h | Prereqs: [43]**

## Core Learning

- The convolution operation: a small filter slides across the input, computing dot products at each position
- Pooling: downsampling to reduce spatial dimensions and gain translation invariance
- Stride and padding: controlling output dimensions
- Feature hierarchies: early layers learn edges, middle layers learn textures, deep layers learn object parts
- AlexNet architecture: conv-pool-conv-pool-fc-fc-softmax, ReLU activation, dropout regularization
- The ImageNet moment (2012): AlexNet crushed the competition by 10+ percentage points, proving deep learning at scale
- The GPU revolution: training on two GTX 580s made AlexNet possible -- compute as the bottleneck

## Watch -- Primary

1. **Welch Labs -- AlexNet/CNN video (Ch. 5 video)**
   - *The chapter on how convolutional networks exploit spatial structure, culminating in the AlexNet breakthrough.*

## Watch -- Secondary

2. **3Blue1Brown -- "But what is a convolution?"**
   - https://www.youtube.com/watch?v=KuXjwB4LzSA
   - *Visual intuition for the convolution operation itself, independent of neural networks.*

3. **Stanford CS231n -- CNN lectures**
   - *The Stanford course covers convolutional networks in depth: architecture design, training tricks, and visualization techniques.*

## Read

- **Welch Labs -- *The Illustrated Guide to AI*, Ch. 5: AlexNet and CNNs**
  - http://www.welchlabs.com/resources/ai-book
  - *The book chapter on convolutional networks and the ImageNet moment.*
- **Krizhevsky et al. -- "ImageNet Classification with Deep Convolutional Neural Networks" (the AlexNet paper)**
  - https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
  - *The paper that launched the modern deep learning era. Read for historical significance and architectural details.*

## Do

- Implement a simple CNN from scratch (conv layer + pooling + fully connected)
- Train on MNIST or CIFAR-10
- Visualize learned filters at each layer -- what patterns does the network discover?
- Compare parameter count to an equivalent fully-connected network -- appreciate why weight sharing matters

## ML & Alignment Connection

CNNs exploit spatial structure through weight sharing -- the same pattern detector works everywhere in the image. This inductive bias dramatically reduces parameters and improves generalization. AlexNet proved that scale + GPUs + data could solve previously intractable problems, launching the modern AI era.

This historical lesson matters for alignment: capability jumps happen suddenly when compute thresholds are crossed. In 2011, the best image classifiers were hand-engineered feature pipelines. By 2013, deep learning dominated. Nobody predicted the speed of this transition. The same dynamic -- gradual progress followed by a sudden capability jump -- is what alignment researchers worry about with future AI systems. Understanding the AlexNet moment helps calibrate expectations for how quickly the landscape can shift.
