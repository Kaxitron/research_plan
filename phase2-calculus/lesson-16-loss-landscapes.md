# Lesson 16: Loss Landscapes and Local Minima

[← Optimization](lesson-15-optimization.md) | [Back to TOC](../README.md) | [Next: Probability →](../phase3-probability/lesson-17-probability.md)

---

## 🎯 Core Learning

- Loss as a function of all parameters: a surface in absurdly high-dimensional space
- Local minima, saddle points, and plateaus
- Why high-dimensional landscapes are actually *easier* (saddle points dominate, not local minima)
- Loss landscape visualization techniques
- Generalization: why memorizing training data fails on new data
- The double descent phenomenon
- **Grokking:** the mysterious phenomenon where networks suddenly "get it" after appearing to overfit

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

- **"Visualizing the Loss Landscape of Neural Nets" (Li et al., 2018)** — skim for the stunning visualizations
- **colah's blog — "Neural Networks, Manifolds, and Topology"**
  - http://colah.github.io/posts/2014-03-NN-Manifolds-Topology/

## 🔨 Do

- Visualize the loss landscape of a tiny 2-parameter network
- Implement early stopping and see its effect on generalization
- **Grokking demo:** Train a small network on modular addition. Watch the train loss drop, validation stay high, then suddenly both collapse to near zero.

## 🔗 ML Connection

The shape of the loss landscape is intimately connected to alignment. When we train a model to be "helpful and harmless," the loss landscape determines *which* behaviors emerge. Grokking shows that phase transitions — sudden qualitative changes in model behavior — are real and can appear long after training seems complete. Singularities in the loss landscape (from singular learning theory) are an active area of alignment research.
