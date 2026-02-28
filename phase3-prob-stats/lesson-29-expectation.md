# Lesson 29: Expectation, Variance, and Covariance

[← Probability](lesson-28-probability.md) | [Back to TOC](../README.md) | [Next: MLE →](lesson-30-mle.md)

---

## 🎯 Core Learning

- Expected value: the "center of mass" of a distribution
- Variance: how spread out the distribution is
- Covariance: how two variables move together
- Covariance matrices: connecting back to linear algebra (it's a matrix! with eigenvalues!)
- PCA as eigendecomposition of the covariance matrix

## 📺 Watch — Primary

1. **StatQuest — "Expected Values"**
   - https://www.youtube.com/results?search_query=statquest+expected+values
   - *Clear introduction to the "center of mass" interpretation.*
2. **StatQuest — "Covariance, Clearly Explained"**
   - https://www.youtube.com/results?search_query=statquest+covariance+clearly+explained
   - *How two variables move together, with visual examples.*
3. **StatQuest — "PCA, Step by Step"**
   - https://www.youtube.com/results?search_query=statquest+pca+step+by+step
   - *Connects covariance eigenvalues to principal components — ties together Lessons 8, 8, and this one.*

## 📺 Watch — Secondary

4. **3Blue1Brown — "But what is a convolution?"**
   - https://www.youtube.com/watch?v=KuXjwB4LzSA
   - *While about convolution, includes beautiful visualizations of expected value and probability distributions that build intuition.*
5. **Khan Academy — "Covariance and correlation"**
   - Good worked numerical examples if StatQuest moves too fast

## 📖 Read

- **MML Book, Chapter 6.4–6.5** — covariance and correlation

## 🔨 Do

- Generate correlated 2D data, compute covariance matrix, find eigenvectors
- Show that PCA directions = eigenvectors of the covariance matrix
- This connects SVD → covariance → PCA into one unified picture

## 🔗 ML Connection

Batch normalization controls mean and variance of activations. The covariance structure of internal representations is crucial for understanding what networks learn. PCA on activations is a basic interpretability tool.
