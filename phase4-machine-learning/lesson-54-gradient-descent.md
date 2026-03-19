# Lesson 54: Gradient Descent -- Learning from Errors

[← Perceptron](lesson-53-perceptron.md) | [Back to TOC](../README.md) | [Next: Backpropagation →](lesson-55-backpropagation.md)

---

**Welch Ch. 2 | Karpathy ZtH #1 (first half) | Hours: 9-11h | Prereqs: [40]**

## Core Learning

- Loss functions: measuring how wrong the model is (MSE, cross-entropy)
- The gradient: the direction of steepest ascent -- negate it to descend
- Learning rate: too large and you overshoot, too small and you stall
- Convergence: when the gradient is near zero, you are at a (possibly local) minimum
- Batch gradient descent vs stochastic gradient descent vs mini-batch
- The loss landscape: saddle points, local minima, and why SGD noise helps escape them

## Watch -- Primary

1. **Welch Labs -- "The Misconception that Almost Stopped AI" (Ch. 2 video)**
   - https://www.youtube.com/watch?v=PFDMhdDR_1M
   - *The historical misconception about gradient-based learning and how it was overcome. The Belgium/Netherlands map example builds geometric intuition for how gradient descent navigates loss surfaces.*

2. **Karpathy -- "Building micrograd" (Lecture 1, first half: Value class, gradient)**
   - https://www.youtube.com/watch?v=VMj-3S1tku0
   - *The first half covers building the Value class and manual gradient computation. This is where you build the engine that makes learning possible.*

## Watch -- Secondary

3. **3Blue1Brown -- "Gradient descent, how neural networks learn" | Deep Learning Ch. 2**
   - https://www.youtube.com/watch?v=IHZwWFHWa-w
   - *Visual intuition for gradient descent in high-dimensional parameter spaces.*

## Read

- **Welch Labs -- *The Illustrated Guide to AI*, Ch. 2: Gradient Descent**
  - http://www.welchlabs.com/resources/ai-book
  - *Covers the historical misconception and gradient descent with code and exercises.*

## Do

**1. Gradient descent on a bowl (pure Python, no libraries)**

Define `f(x, y) = x^2 + 4*y^2` (an elliptical bowl). Implement gradient descent:
```
for step in range(200):
    grad_x = 2*x
    grad_y = 8*y
    x -= lr * grad_x
    y -= lr * grad_y
```

Start from `(4, 3)`. Print `(x, y, f(x,y))` every 20 steps. Watch it converge to `(0, 0)`.

**2. Learning rate experiments**

Run the same optimization with `lr = 0.01` (slow), `lr = 0.1` (good), `lr = 0.3` (oscillating), `lr = 0.6` (diverging). Plot all four trajectories on a contour plot of `f`. This directly connects to the ODE capstone — gradient descent IS Euler's method on `dx/dt = -∇f`.

**3. Build the `Value` class — follow Karpathy ZtH #1 (0:00–1:00)**

Follow the first hour of Karpathy's micrograd video. Type every line yourself. You're building:
- `Value(data)` that stores a float and a gradient
- Overloaded `+`, `*`, `**` that build a computation graph
- A `_backward()` closure on each node storing the local chain rule

At this point you should have a working `Value` that can compute `a*b + c` and propagate gradients backward through it.

**4. Visualize your computation graph**

For a small expression like `L = (a*b + c) * d`, draw the computation graph (on paper or with graphviz). Label each edge with the local gradient. Trace the backward pass manually and verify it matches `Value.grad`.

## ML & Alignment Connection

Gradient descent IS how AI learns. Every modern AI system -- from GPT to AlphaFold -- learns by following gradients downhill on a loss surface. The learning rate determines whether the model converges, oscillates, or diverges.

For alignment, the critical question is whether the gradient from our objective actually points toward aligned behavior. If we train on "predict the next token," gradient descent will make the model better at prediction -- but does that gradient also push toward honesty, helpfulness, and harmlessness? The gap between "what gradient descent optimizes" and "what we actually want" is the core alignment problem. RLHF and related techniques attempt to reshape the loss landscape so that the gradient points toward alignment.
