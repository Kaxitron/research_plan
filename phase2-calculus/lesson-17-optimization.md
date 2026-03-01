# Lesson 17: Optimization and Gradient Descent

[← Chain Rule](lesson-16-chain-rule.md) | [Back to TOC](../README.md) | [Next: Constrained Optimization →](lesson-18-constrained-optimization.md)

---

## 🎯 Core Learning

- Gradient descent: step opposite the gradient, scaled by learning rate
- Stochastic gradient descent (SGD): random mini-batches instead of all data
- Learning rate: too big = overshoot, too small = too slow
- Momentum: "rolling downhill with inertia"
- Adam optimizer: the adaptive method used for almost all modern training
- Convexity vs. non-convexity: why neural network optimization is hard in theory but works in practice

## 📺 Watch

- **Andrej Karpathy — "Building micrograd"** (Lecture 1, ~2.5 hours)
  - https://www.youtube.com/watch?v=VMj-3S1tku0
  - *Build a complete autograd engine and neural network from scratch.*

## 📖 Read

- **Stanford CS231n notes on Optimization**
  - https://cs231n.github.io/optimization-1/ and /optimization-2/

## 🔨 Do

### 💻 Coding Mini-Project: Optimizer Showdown (~60 lines)

Implement three optimizers from scratch as pure functions — no frameworks:

```python
def sgd_step(params, grads, lr):
    """Vanilla gradient descent."""
    ...

def momentum_step(params, grads, velocity, lr, beta=0.9):
    """SGD with momentum. Returns updated params AND velocity."""
    ...

def rmsprop_step(params, grads, cache, lr, decay=0.99, eps=1e-8):
    """RMSProp. Returns updated params AND cache."""
    ...
```

**Your tasks:**
1. Implement all three optimizers (just numpy, no PyTorch)
2. Test on the Rosenbrock function: `f(x,y) = (1-x)² + 100(y-x²)²` (a classic hard optimization surface)
3. Race all three from starting point `(-1, -1)` for 5000 steps. Plot trajectories overlaid on contour plot
4. Print final positions and iteration count to reach within 0.01 of the minimum at `(1, 1)`
5. Experiment: what learning rate works best for each? Why does momentum help on Rosenbrock?

- Train a small neural network on simple 2D data
- Experiment: learning rate 0.001 vs 0.1 vs 10 — what happens?

**Programming skills practiced:** numerical computing with numpy, function design, matplotlib visualization, parameter tuning

## 🔗 ML & Alignment Connection

The optimizer shapes what solutions the network finds. For alignment, the "attractor basins" in the loss landscape determine what behaviors emerge. Understanding optimization helps you reason about: "Why does the network learn *this* strategy instead of *that* one?"
