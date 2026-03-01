# Lesson 15: Partial Derivatives and Gradients — Going Deeper

[← Matrix Calculus](lesson-14-matrix-calculus.md) | [Back to TOC](../README.md) | [Next: Chain Rule →](lesson-16-chain-rule.md)

---

## 🎯 Core Learning

- Gradients as vectors perpendicular to contour lines (geometric picture)
- The gradient always points in the direction of steepest ascent
- Directional derivatives: how fast does the function change if I walk in *this* direction?
- Multivariable chain rule: the key identity that makes backpropagation work

## 📺 Watch

- **3Blue1Brown — "Gradient descent, how neural networks learn" | Deep Learning Ch. 2**
  - https://www.youtube.com/watch?v=IHZwWFHWa-w
- **Dr. Trefor Bazett — Multivariable Calculus (gradient and directional derivative sections)**
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxc_CvEy7xBKRQr6I214QJcd
  - *Clear visual lectures on partial derivatives and gradients. Use for extra practice if 3B1B moves too fast.*
- **Dr. Trefor Bazett — Vector Calculus (gradient fields)**
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxfW0GMqeUE1bLKaYor6kbHa
  - *Connects gradient concepts to vector fields — directly relevant to understanding gradient flow in training.*

## 📖 Read

- **colah's blog — "Calculus on Computational Graphs: Backpropagation"**
  - http://colah.github.io/posts/2015-08-Backprop/
  - *Absolutely essential.* Chris Olah explains backprop as the chain rule applied to computation graphs.

## 🔨 Do

- Visualize gradient fields of 2D functions (matplotlib contour plots with arrows)
- Implement numerical gradient descent on a simple 2D function — watch the point slide downhill

### 💻 Coding Mini-Project: Reusable Gradient Descent Toolkit (~40 lines)

Write a general-purpose gradient descent function and test it on multiple surfaces:

```python
def gradient_descent(f, grad_f, x0, lr=0.01, n_steps=500):
    """
    Args: f (callable), grad_f (callable), x0 (np.array), lr, n_steps
    Returns: trajectory as list of np.arrays
    """
    ...
```

**Your tasks:**
1. Implement the function. Store the full trajectory (every point visited)
2. Write a `plot_descent(f, trajectory, xlim, ylim)` helper that overlays the trajectory on a contour plot
3. Test on three surfaces:
   - Bowl: `f(x,y) = x² + y²` (should go straight to origin)
   - Elongated bowl: `f(x,y) = x² + 25y²` (should zigzag — why?)
   - Saddle: `f(x,y) = x² - y²` (what happens? it should escape along y)
4. For the elongated bowl, try `lr = 0.01, 0.03, 0.06, 0.08`. Plot all four trajectories side by side. Find the largest stable learning rate.

**Programming skills practiced:** function design, numpy arrays, matplotlib subplots, code reuse

## 🔗 ML & Alignment Connection

The gradient is THE signal that tells a neural network how to learn. Understanding gradients geometrically — as vectors perpendicular to contour lines, pointing in the direction of steepest ascent — gives you intuition for why some networks train well and others don't.

For alignment, the critical question is: does the gradient from our objective function (RLHF, constitutional AI, etc.) actually point toward aligned behavior? If the loss landscape has the "wrong shape" — e.g., deceptively aligned behavior sits in a deeper basin than honestly aligned behavior — then following the gradient leads to misalignment. Understanding gradients geometrically helps you reason about *whether the training signal teaches what we intend*.
