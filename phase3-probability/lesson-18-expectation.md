# Lesson 18: Expectation, Variance, and Covariance

[← Probability](lesson-17-probability.md) | [Back to TOC](../README.md) | [Next: MLE →](lesson-19-mle.md)

---

## 🎯 Core Learning

- Expected value: the "center of mass" of a distribution
- Variance: how spread out the distribution is
- Covariance: how two variables move together
- Covariance matrices: connecting back to linear algebra (it's a matrix! with eigenvalues!)
- PCA as eigendecomposition of the covariance matrix

## 📺 Watch

- **StatQuest — "Covariance, Clearly Explained" and "PCA, Step by Step"**
  - https://www.youtube.com/c/joshstarmer

## 📖 Read

- **MML Book, Chapter 6.4–6.5** — covariance and correlation

## 🔨 Do

- Generate correlated 2D data, compute covariance matrix, find eigenvectors
- Show that PCA directions = eigenvectors of the covariance matrix
- This connects SVD → covariance → PCA into one unified picture

## 🔗 ML Connection

Batch normalization controls mean and variance of activations. The covariance structure of internal representations is crucial for understanding what networks learn. PCA on activations is a basic interpretability tool.
