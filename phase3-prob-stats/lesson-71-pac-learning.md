# Lesson 71: PAC Learning and Generalization Bounds

[← Concentration Inequalities (L68)](lesson-68-concentration-inequalities.md) | [Back to TOC](../README.md) | [Next: Hypothesis Testing (L32) →](lesson-32-hypothesis-testing.md)

---

> **Why this lesson exists:** The deepest question in machine learning is: *why does a model that performs well on training data also perform well on new data?* Generalization bounds provide mathematical answers. PAC (Probably Approximately Correct) learning theory gives you guarantees of the form "with probability at least 1−δ, the model's true error is within ε of its training error, provided you have n ≥ f(ε, δ, complexity) samples." For alignment, this is directly relevant: if you evaluate a model on a safety benchmark, generalization bounds tell you whether that evaluation transfers to deployment. Without these tools, all safety evaluations are acts of faith.

## 🎯 Core Concepts

### The Generalization Problem

- **Empirical risk:** the average loss on the training set. L̂(h) = (1/n)Σ ℓ(h(xᵢ), yᵢ).
- **True risk:** the expected loss over the entire data distribution. L(h) = E[ℓ(h(x), y)].
- **The generalization gap:** |L(h) − L̂(h)|. This is what we need to bound. If the gap is small, training performance predicts deployment performance.
- **The fundamental challenge:** h was chosen to minimize L̂(h) on the training set. The model "saw" the training data. By Hoeffding's inequality (Lesson 68), any FIXED hypothesis h has |L(h) − L̂(h)| ≤ O(1/√n). But the learner CHOSE h based on the data — this breaks the independence assumption.

### The PAC Framework

- **Probably Approximately Correct:** a hypothesis class H is PAC learnable if there exists an algorithm A such that for any distribution D and any ε, δ > 0:

$$P\left(L(h_A) \leq \min_{h \in H} L(h) + \varepsilon\right) \geq 1 - \delta$$

provided n ≥ n₀(ε, δ, H).

- **The sample complexity** n₀ tells you how much data you need. The goal of learning theory is to characterize n₀ in terms of the "complexity" of H.
- **For finite hypothesis classes:** if |H| = M, then by a union bound (Lesson 68) over all h ∈ H plus Hoeffding:

$$n \geq \frac{1}{2\varepsilon^2}\log\frac{2M}{\delta}$$

- **The log(M) dependence is remarkable:** you only need logarithmically many samples in the number of hypotheses. A class with a million hypotheses needs only ~20/ε² more samples than a class with one hypothesis.

### VC Dimension — Measuring Hypothesis Complexity

- **The problem:** real hypothesis classes (like neural networks) are infinite — you can't just count them.
- **VC (Vapnik-Chervonenkis) dimension:** the largest number of points that H can **shatter** — assign any possible labeling to.
  - A line in 2D can shatter 3 points (any labeling of 3 points in general position can be achieved by some line) but cannot shatter 4 points. So VC(linear classifiers in ℝ²) = 3.
  - In general: VC(linear classifiers in ℝᵈ) = d + 1.
- **The VC bound:** for hypothesis class H with VC dimension d:

$$P\left(\sup_{h \in H}|L(h) - \hat{L}(h)| > \varepsilon\right) \leq 4 \left(\frac{2en}{d}\right)^d e^{-n\varepsilon^2/8}$$

- This gives sample complexity n = O(d/ε² · log(d/ε)). The "effective size" of an infinite class is controlled by its VC dimension.
- **For neural networks:** VC dimension scales roughly with the number of parameters — but this gives VERY loose bounds (vacuous for modern networks with millions of parameters).

### Rademacher Complexity — A Sharper Measure

- **Idea:** How well can H fit random noise? If H can fit random labels, it's complex. If it can't, it's simple.
- **Rademacher complexity:**

$$\hat{R}_n(H) = E_\sigma\left[\sup_{h \in H} \frac{1}{n}\sum_{i=1}^n \sigma_i h(x_i)\right]$$

  where σᵢ are independent random ±1 (Rademacher variables).

- **Generalization bound:**

$$L(h) \leq \hat{L}(h) + 2R_n(H) + \sqrt{\frac{\log(1/\delta)}{2n}}$$

- **Advantages over VC:** Rademacher complexity is data-dependent — it captures how complex H is relative to the specific data distribution, not the worst case.

### PAC-Bayes — The Tightest Practical Bounds

- **The breakthrough:** PAC-Bayes bounds combine the PAC framework with Bayesian reasoning. Instead of bounding the error of a single hypothesis, they bound the expected error of a distribution over hypotheses.
- **The PAC-Bayes bound:** for any prior P (chosen before seeing data) and any posterior Q (chosen after):

$$E_{h \sim Q}[L(h)] \leq E_{h \sim Q}[\hat{L}(h)] + \sqrt{\frac{D_{KL}(Q \| P) + \log(n/\delta)}{2n}}$$

- **Why this is revolutionary:** The KL divergence D_KL(Q ‖ P) measures how far the learned distribution Q is from the prior P. If you start with a "good" prior (one that assigns reasonable probability to good hypotheses), the bound is tight — even for neural networks.
- **Connection to Lesson 31:** KL divergence from information theory appears as the "complexity penalty." More complex posteriors (further from the prior) need more data to justify.
- **Connection to regularization:** L2 regularization pulls weights toward zero (a Gaussian prior centered at zero). The PAC-Bayes bound explains WHY this helps generalization — it keeps D_KL(Q ‖ P) small.

### Why Classical Bounds Fail for Deep Learning

- **The puzzle:** a neural network with millions of parameters should, by VC theory, need billions of training samples. But they generalize well with far fewer. This is the "generalization mystery."
- **Partial answers:**
  1. **Implicit regularization** (Lesson 24): SGD biases toward simpler solutions, effectively reducing the "used" complexity.
  2. **PAC-Bayes with SGD priors:** if the prior P is centered at the initialization and Q is the training distribution of SGD, the KL term is manageable.
  3. **Compression-based bounds:** if a network can be compressed (pruned, quantized) without losing accuracy, the effective complexity is the compressed size, not the parameter count.
  4. **SLT perspective (Lesson 50):** singular models have lower effective dimension (RLCT) than their parameter count suggests.

## 📺 Watch

1. **Mathematicalmonk — "Machine Learning" playlist (PAC learning lectures)**
   - Search YouTube: mathematicalmonk ML PAC learning
   - *Clear, careful presentation of the theory*
2. **Sébastien Bubeck — "Convex Optimization: Algorithms and Complexity"** (select lectures)
   - Bubeck's lectures often cover generalization bounds alongside optimization
3. **Arora — "Generalization Theory for Deep Learning" talks**
   - Sanjeev Arora has given several accessible talks on why generalization bounds for deep learning are hard and what alternatives exist

## 📖 Read — Primary

- **Shalev-Shwartz & Ben-David "Understanding Machine Learning: From Theory to Algorithms" — Chapters 2–6**
  - https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/
  - *Free online. THE textbook for PAC learning. Chapters 2 (PAC), 3 (uniform convergence), 4 (bias-complexity tradeoff), 6 (VC dimension). Beautifully written and self-contained.*

## 📖 Read — Secondary

- **"PAC-Bayes with Backprop" by Dziugaite & Roy (2017)**
  - https://arxiv.org/abs/1703.11008
  - *Shows PAC-Bayes bounds can be non-vacuous for neural networks — a landmark result.*
- **"Computing Nonvacuous Generalization Bounds for Deep (Stochastic) Neural Networks" by Dziugaite & Roy**
  - Extends the above with practical algorithms for computing tight bounds

## 🔨 Do

- **Shattering experiment:** implement a linear classifier in 2D. Generate 3 random points. Show that for ALL 8 possible labelings, there exists a separating line. Then generate 4 points and find a labeling that NO line can achieve. This demonstrates VC dimension = 3.
- **Rademacher complexity estimation:** for a dataset of n points, estimate the Rademacher complexity of (a) linear classifiers and (b) a small neural network by: generate random ±1 labels, fit the model, record the correlation. Repeat 1000 times. Average. Compare — the neural network has higher Rademacher complexity.
- **PAC-Bayes bound computation:** train a small neural network. Set the prior P = N(0, σ²I) (Gaussian at zero). Set the posterior Q = N(w_trained, s²I) where s is estimated from SGD noise. Compute D_KL(Q ‖ P) and the PAC-Bayes bound. Is it vacuous (> 1) or non-vacuous (< 1)?
- **Key exercise:** you're evaluating an AI system for safety. You test it on 10,000 examples and find 0 failures. Using the PAC bound for finite hypothesis classes, give a 95% confidence upper bound on the true failure rate. Is 10,000 enough? What about 1,000,000?

## 🔗 ML & Alignment Connection

- **Safety evaluation guarantees:** when you test an AI system on n safety-critical scenarios and observe k failures, generalization bounds tell you the true failure rate. Without these bounds, "zero failures on the test set" is meaningless — you might just not have tested enough.
- **The alignment tax:** adding safety constraints (like RLHF) changes the hypothesis class. Generalization bounds help quantify whether safety constraints help or hurt generalization — the "alignment tax" question.
- **Distributional shift:** classical bounds assume test data comes from the same distribution as training data. In deployment, this is often false. Robust generalization bounds that handle distribution shift are an active research frontier directly relevant to alignment.
- **PAC-Bayes and Bayesian alignment:** if you have a prior belief about "what aligned behavior looks like" and update it with data, PAC-Bayes bounds tell you how reliable the posterior is. This connects formal learning theory to Bayesian approaches to alignment (Lesson 35).
- **Kolmogorov complexity connection (Lesson 53):** the simplest hypothesis consistent with the data is, in some sense, the "most aligned" — it's not encoding deceptive complexity. MDL (minimum description length) and PAC-Bayes bounds formalize this Occam's razor argument.
