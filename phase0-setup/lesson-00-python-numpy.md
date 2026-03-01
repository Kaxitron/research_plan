# Lesson 0: Python and NumPy for Machine Learning

[Back to TOC](../README.md) | [Next: Vectors →](../phase1-linear-algebra/lesson-02-vectors.md)

---

> **Why this lesson exists:** Every exercise in this curriculum uses Python. This lesson isn't about learning Python from scratch — you already have intermediate skills. It's about getting fluent with the specific tools you'll use constantly: NumPy for matrix operations, Matplotlib for visualization, and Jupyter notebooks for interactive exploration. If you can already write a for-loop and use NumPy, skim this and move on.

## 🎯 Core Skills

### NumPy — Thinking in Arrays

- **The mental shift:** stop writing for-loops over numbers. Start thinking in terms of whole arrays and matrices being transformed at once. `A @ v` multiplies a matrix by a vector. `np.linalg.eig(A)` gives eigenvalues. You'll use these hundreds of times.
- **Key operations you'll use every lesson:**
  ```python
  import numpy as np

  # Creating arrays
  v = np.array([1, 2, 3])           # vector
  A = np.array([[1, 2], [3, 4]])    # matrix
  I = np.eye(3)                      # 3×3 identity
  Z = np.zeros((3, 4))              # 3×4 zeros
  R = np.random.randn(3, 3)         # random 3×3

  # Linear algebra
  A @ v                              # matrix-vector multiply
  A @ B                              # matrix-matrix multiply
  np.linalg.inv(A)                   # inverse
  np.linalg.det(A)                   # determinant
  np.linalg.eig(A)                   # eigenvalues + eigenvectors
  np.linalg.svd(A)                   # SVD
  np.linalg.norm(v)                  # L2 norm
  A.T                                # transpose

  # Broadcasting (crucial!)
  v + 1                              # adds 1 to every element
  A * v                              # multiplies each row by v
  ```

- **Broadcasting** is NumPy's most powerful and most confusing feature. When shapes don't match, NumPy stretches the smaller array. Understanding this prevents hours of debugging.

### Matplotlib — Seeing the Math

- **2D plots:** `plt.plot(x, y)` for functions, `plt.scatter(x, y)` for point clouds
- **Arrows for vectors:** `plt.quiver(0, 0, v[0], v[1])` draws a vector arrow from origin
- **Contour plots:** `plt.contour(X, Y, Z)` for visualizing 2D functions (loss landscapes!)
- **Heatmaps:** `plt.imshow(A)` to visualize matrices (attention patterns, weight matrices)

### Jupyter Notebooks — Interactive Exploration

- Use Jupyter (or Google Colab, which requires no setup) for all exercises
- The workflow: write code in a cell → see the output → tweak → re-run. This interactive loop is how you build intuition.
- **Google Colab** requires zero installation: https://colab.research.google.com/

## 📺 Watch

1. **Karpathy — "The spelled-out intro to neural networks and backpropagation"**
   - This is the micrograd lecture. You'll revisit it in Lesson 16, but the first 30 minutes are a good Python warm-up.
2. **NumPy in 10 Minutes (various YouTube channels)**
   - Search "NumPy tutorial 10 minutes" — any top result will do
3. **Corey Schafer — "Matplotlib Tutorial"**
   - https://www.youtube.com/results?search_query=corey+schafer+matplotlib

## 📖 Read

- **NumPy Quickstart Tutorial** — https://numpy.org/doc/stable/user/quickstart.html
- **Python Data Science Handbook, Chapter 2** (NumPy) — https://jakevdp.github.io/PythonDataScienceHandbook/
- **Matplotlib Cheat Sheet** — https://matplotlib.org/cheatsheets/

## 🔨 Do

- **Setup:** install Python, NumPy, Matplotlib, Jupyter (or just open Google Colab)
- **NumPy speed test:** multiply two 1000×1000 matrices using (a) nested Python for-loops and (b) `A @ B`. Time both. See the 100x+ speedup. This is why NumPy exists — and why GPUs are matrix multiplication accelerators.
- **Visualization starter:** plot the unit circle, then apply a 2×2 matrix to it. See the circle become an ellipse. You'll do this in Lesson 4 for real.
- **Linear algebra warm-up:** create a random 3×3 matrix. Compute its determinant, eigenvalues, SVD, and inverse using NumPy. Print them. You don't need to understand these yet — just verify the tools work.

## 🔗 ML & Alignment Connection

Every ML researcher's daily workflow is: write NumPy/PyTorch code → visualize results → iterate. The faster you are with these tools, the more experiments you can run, and experiments are how alignment researchers make discoveries. TransformerLens (which you'll use in Phase 5) is built on PyTorch, which has nearly identical syntax to NumPy.
