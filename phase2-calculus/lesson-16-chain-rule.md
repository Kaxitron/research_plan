# Lesson 16: The Chain Rule — This IS Backpropagation

[← Gradients](lesson-15-gradients.md) | [Back to TOC](../README.md) | [Next: Optimization →](lesson-17-optimization.md)

---

## 🎯 Core Learning

- Single-variable chain rule refresh: d/dx f(g(x)) = f'(g(x)) · g'(x)
- Multivariable chain rule: how gradients flow backward through composed functions
- Computation graphs: every neural network is a graph of simple operations
- Forward pass vs. backward pass: compute values forward, then gradients backward
- Why "backward" (reverse-mode autodiff) is so much cheaper than "forward" for neural networks

## 📺 Watch (CRITICAL videos)

- **3Blue1Brown — Essence of Calculus, Chapter 4:** "Visualizing the chain rule and product rule"
  - https://www.youtube.com/watch?v=YG15m2VwSjA
  - *The visual foundation for the chain rule before seeing it applied in backpropagation.*
- **3Blue1Brown — "Backpropagation, intuitively" | Deep Learning Ch. 3**
  - https://www.youtube.com/watch?v=Ilg3gGewQ5U
- **3Blue1Brown — "Backpropagation calculus" | Deep Learning Ch. 4**
  - https://www.youtube.com/watch?v=tIeHLnjs5U8

## 📖 Read

- **Michael Nielsen — "Neural Networks and Deep Learning," Chapter 2**
  - http://neuralnetworksanddeeplearning.com/chap2.html
- Re-read colah's backpropagation blog post with fresh eyes

## 🔨 Do

- Draw a computation graph for L = (wx + b - y)² and manually trace gradients backward

### 💻 Coding Mini-Project: Tiny Backprop Engine (~50 lines)

Build a `Scalar` class that tracks computation and can backpropagate gradients. Much smaller than a full autograd engine — just the core idea:

```python
class Scalar:
    def __init__(self, value, _children=(), _op=''):
        self.value = value
        self.grad = 0.0
        self._backward = lambda: None
        self._children = set(_children)
        self._op = _op

    def __add__(self, other): ...   # return new Scalar, define _backward
    def __mul__(self, other): ...   # return new Scalar, define _backward
    def backward(self): ...         # topological sort, then call _backward in reverse
```

**Your tasks:**
1. Implement `__add__`, `__mul__`, and `backward()` (hint: topological sort using DFS)
2. Test on: `a=2, b=3, c=4` → compute `f = (a + b) * c` → call `f.backward()` → verify `a.grad=4, b.grad=4, c.grad=5`
3. Test on: `w=0.5, x=2.0, b=0.1, y=1.0` → compute `L = ((w*x + b) - y)**2` (you'll need `__sub__` and `__pow__`)
4. Compare your gradients to hand-computed values from the drill above

**Programming skills practiced:** operator overloading, recursive algorithms, graph traversal (topological sort), testing

## 🔗 ML & Alignment Connection

Backpropagation is the *single most important algorithm* in deep learning. For alignment: understanding backprop lets you reason about *what the training signal actually looks like* for different objectives — central to understanding why models behave the way they do.
