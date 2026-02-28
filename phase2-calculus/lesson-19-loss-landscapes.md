# Lesson 19: Loss Landscapes and Local Minima

[← Constrained Optimization](lesson-18-constrained-optimization.md) | [Back to TOC](../README.md) | [Next: Multiple Integration →](lesson-20-multiple-integration.md)

---

## 🎯 Core Learning

- Loss as a function of all parameters: a surface in absurdly high-dimensional space
- Local minima, saddle points, and plateaus
- Why high-dimensional landscapes are actually *easier* (saddle points dominate, not local minima)
- Loss landscape visualization techniques
- Generalization: why memorizing training data fails on new data
- The double descent phenomenon
- **Grokking:** the mysterious phenomenon where networks suddenly "get it" after appearing to overfit

### The Bias-Variance Tradeoff — THE Framework for Generalization

- **Empirical risk minimization:** we can't compute the *true* error (on all possible data), so we minimize the *empirical* error (on training data) and hope it generalizes. This gap between training error and true error is the central tension of ML.
- **Decomposition of error:** for any model, the expected prediction error decomposes as:
  - **Error = Bias² + Variance + Irreducible Noise**
  - **Bias:** how far off is the model *on average* from the truth? A too-simple model (e.g., fitting a line to quadratic data) has high bias — it systematically misses the pattern.
  - **Variance:** how much does the model change if you train on different data? A too-complex model (e.g., fitting a degree-100 polynomial to 10 points) has high variance — it memorizes noise and changes wildly.
  - **Noise:** inherent randomness in the data. Nothing can reduce this.
- **The classic picture:** as model complexity increases, bias decreases (more flexible = less systematic error) but variance increases (more flexible = more sensitive to noise). The sweet spot minimizes their sum.
- **The dartboard analogy:** bias = how far the average dart lands from the bullseye. Variance = how spread out the darts are. You want low bias (centered on target) AND low variance (tight cluster).
- **Double descent breaks the classic picture:** for very overparameterized models (like modern neural networks), the error curve doesn't just go up after the sweet spot — it comes back DOWN. This is the double descent phenomenon (see Welch Labs video below). Classical statistics says "more parameters = overfitting." Deep learning says "way more parameters = generalization again."
- **Cross-validation:** the practical tool for estimating generalization. Split data into train/validation/test. Train on train, evaluate on validation, report on test. K-fold cross-validation averages over multiple splits.
- **Model selection criteria:** AIC and BIC approximate the bias-variance tradeoff mathematically, penalizing complex models. BIC penalizes more heavily → prefers simpler models. In deep learning, these are less used (early stopping and regularization do the work), but the theory connects.

**MML Book, Chapter 8** covers empirical risk minimization, cross-validation, and model selection in detail. Chapter 8.1–8.2 are the most important sections.

### Hessian Analysis of Loss Landscapes

- The **Hessian matrix** (Lesson 13) at a critical point tells you everything about the local landscape:
  - **All eigenvalues positive** → local minimum (you're at the bottom of a bowl)
  - **All eigenvalues negative** → local maximum (top of a hill)
  - **Mixed signs** → saddle point (valley in some directions, ridge in others)
  - **Some eigenvalues near zero** → flat direction (plateau or ridge — the landscape barely curves)
- **The key insight for high dimensions:** in a 100-000-dimensional space (typical neural network), for a random critical point to be a local minimum, ALL 100,000 eigenvalues must be positive. The probability of this is vanishingly small. Almost all critical points are saddle points. This is why local minima are NOT the main problem in deep learning — saddle points and flat regions are.
- **Condition number** = λ_max / λ_min. High condition number → elongated landscape → gradient descent zig-zags. This is why adaptive optimizers (Adam) and preconditioning help.

## 📺 Watch — Primary

1. **Welch Labs — "What the Books Get Wrong about AI [Double Descent]"**
   - https://www.youtube.com/@WelchLabs (search "Double Descent")
   - *34 minutes. The classic bias-variance tradeoff from ML textbooks is WRONG for modern deep learning. Welch explains double descent — the counterintuitive finding that more parameters eventually *helps* generalization. Essential for understanding why massive models work.*

2. **Welch Labs — "The most complex model we actually understand [Grokking]"**
   - https://www.youtube.com/@WelchLabs (search "Grokking")
   - *35 minutes. A network trains on modular arithmetic, appears to massively overfit... and then suddenly "grokks" — generalizing perfectly after thousands of additional steps. This connects directly to phase transitions in singular learning theory and is one of the most striking demonstrations in modern ML.*

3. **3Blue1Brown — "But what is a neural network?" | Deep Learning Ch. 1**
   - https://www.youtube.com/watch?v=aircAruvnKk

## 📺 Watch — Secondary

4. **Welch Labs — "Why Deep Learning Works Unreasonably Well [How Models Learn Part 3]"**
   - https://www.youtube.com/@WelchLabs (search "How Models Learn Part 3")
   - *34 minutes. Ties together the geometry-of-depth framing with why overparameterized networks generalize. Completes the How Models Learn trilogy.*

## 📖 Read

- **MML Book, Chapter 8.1–8.2** (empirical risk minimization, bias-variance tradeoff) — essential theoretical framework
- **MML Book, Chapter 8.6** (model selection — cross-validation, AIC, BIC)
- **"Visualizing the Loss Landscape of Neural Nets" (Li et al., 2018)** — skim for the stunning visualizations
- **colah's blog — "Neural Networks, Manifolds, and Topology"**
  - http://colah.github.io/posts/2014-03-NN-Manifolds-Topology/

## 🔨 Do

- Visualize the loss landscape of a tiny 2-parameter network
- Implement early stopping and see its effect on generalization
- **Grokking demo:** Train a small network on modular addition. Watch the train loss drop, validation stay high, then suddenly both collapse to near zero.
- **Bias-variance visualization:** Generate noisy data from y = sin(x) + noise. Fit polynomials of degree 1, 3, 5, 10, 20. For each, train on 20 different random datasets and plot ALL fits. See that degree-2 has high bias (always wrong in the same way) and low variance (fits look similar). Degree-22 has low bias (passes through data) but high variance (fits look wildly different).
- **Cross-validation implementation:** Implement 5-fold cross-validation for polynomial regression. Plot train error and validation error vs. polynomial degree. Find the "elbow" where validation error is minimized.
- **Hessian eigenvalue analysis:** For a 2-parameter network, compute the Hessian at several critical points. Classify each as minimum, maximum, or saddle by checking eigenvalue signs. Visualize the loss surface with critical points marked.

## 🔗 ML Connection

The shape of the loss landscape is intimately connected to alignment. When we train a model to be "helpful and harmless," the loss landscape determines *which* behaviors emerge. Grokking shows that phase transitions — sudden qualitative changes in model behavior — are real and can appear long after training seems complete. Singularities in the loss landscape (from singular learning theory) are an active area of alignment research.
