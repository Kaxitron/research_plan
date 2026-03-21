# Lesson 66: Interpretability -- Singular Learning Theory

[< Circuits and Features](lesson-65-interp-circuits.md) | [Back to TOC](../README.md) | [Next: Phase 5 -- Discrete Math >](../phase5-math-enrichment/lesson-67-logic-propositions.md)

---

> **Prerequisites:** [Lesson 83: Circuits, Features, and Superposition](lesson-65-interp-circuits.md), [Lesson 37: Bayesian Model Comparison](../phase3-prob-stats/lesson-46-bayesian-model-comparison.md)

> **Why this lesson exists:** Singular Learning Theory (SLT) is an emerging mathematical framework that may explain *why* neural networks generalize, *when* they undergo phase transitions, and *what structure* they learn. It connects algebraic geometry (the study of solutions to polynomial equations) to deep learning, and has become a focal point for mathematical alignment research. SLT is where the cutting edge of alignment theory meets the deepest mathematics.

## Core Concepts

### Why Standard Statistics Fails for Neural Networks

- **The problem:** classical statistics assumes the model is *regular* -- meaning the mapping from parameters to predictions is smooth and one-to-one near the optimal solution. The Fisher information matrix is invertible. The loss landscape is locally quadratic (bowl-shaped).
- **Neural networks violate this.** Many different parameter settings produce the *same* input-output behavior. Swapping two neurons in a hidden layer doesn't change the function. Setting a weight to zero makes the connected neuron irrelevant. These **symmetries** mean the parameter-to-function map is many-to-one -- it has *singularities*.
- **At singularities:** the Fisher information matrix is singular (non-invertible). The Hessian has zero eigenvalues (flat directions). The loss landscape is NOT locally quadratic -- it's more like a valley, a ridge, or a more exotic shape.
- **Why this matters:** classical tools (AIC, BIC, standard Bayesian model comparison from Lesson 37) assume regularity. They give wrong answers for neural networks. SLT provides the right framework.

### The Core Idea: Free Energy and the RLCT

- **RLCT as effective dimension:** the Real Log Canonical Threshold (lambda) replaces d/2 (half the parameter count) as the measure of model complexity. Crucially, lambda <= d/2 -- the effective complexity of a neural network is LESS than its parameter count. This is why overparameterized networks can generalize.
- **Free energy F approximately equals lambda * log n:** for singular models (neural networks), the free energy scales as F ~ lambda * log(n) - (m-1) * log(log(n)) + constant, where n is the number of data points, lambda is the RLCT, and m is the multiplicity. Compare to BIC where F ~ (d/2) * log(n).
- **Fisher information is singular:** at the optimal parameters of a neural network, the Fisher information matrix has zero eigenvalues. This is not a numerical accident -- it's a consequence of the symmetries (neuron permutations, weight rescaling, dead neurons) inherent in the architecture.
- **Symmetries create singularities:** every symmetry in the model (permuting hidden neurons, rescaling weights between layers, zeroing out neurons) creates a flat direction in parameter space where the loss doesn't change. These flat directions are the singularities that SLT studies.

### Geometric Intuition

- **Think of the loss landscape near a minimum.** In a regular model, the minimum is a simple bowl. At a singularity, the minimum is more exotic -- a valley that gets wider in some directions, with flat directions corresponding to symmetries.
- **The RLCT measures "how singular" the singularity is** -- how many flat directions there are and how they interact. More flat directions means a smaller RLCT, lower effective complexity, and better generalization.
- **Connection to your earlier learning:**
  - **Eigenvalues of the Hessian:** near-zero eigenvalues indicate flat directions. SLT goes further -- it characterizes the geometry when eigenvalues are *exactly* zero.
  - **Rank:** if the Hessian has rank r < d, there are d-r flat directions. SLT studies the *shape* of the set of parameters where the loss is minimal.

### Phase Transitions and Developmental Interpretability

- **Phase transitions in training** are moments when the model suddenly learns a new structure -- the loss drops sharply, and the internal representations reorganize. Grokking is an example.
- **SLT explains these:** a phase transition occurs when the model moves from one "basin" (region near one singularity) to another with a different RLCT. The new singularity has lower effective complexity -- the model has found a simpler, more generalizable solution.
- **The Local Learning Coefficient (LLC):** an estimable version of the RLCT that can be computed during training. Researchers plot the LLC over training steps and look for discontinuities -- these mark phase transitions where the model is restructuring its learned representations.
- **LLC for phase transition detection:** track the LLC during training. Sharp drops indicate the model has found a qualitatively different (and simpler) solution. This connects the geometry of the loss landscape to the circuits the model learns.

## Watch -- Primary

1. **Liam Carroll -- "Singular Learning Theory" talks and presentations**
   - Search YouTube for "Liam Carroll singular learning theory"
   - *One of the clearest expositors of SLT for ML researchers.*
2. **Daniel Murfet -- "Singular Learning Theory and AI Safety"**
   - Search YouTube for "Daniel Murfet singular learning theory"
   - *Murfet is a key researcher connecting SLT to alignment. His talks lay out the research program.*

## Watch -- Secondary

3. **Timaeus Research -- YouTube channel**
   - https://www.youtube.com/@timaborovikov (or search "Timaeus singular learning theory")
   - *Research group dedicated to SLT for AI safety. Various technical talks.*
4. **Eigenrobot -- "What is Singular Learning Theory?"**
   - Search YouTube or LessWrong for introductory explainers

## Read -- Primary

- **"Neural Networks are Singular" by Jesse Hoogland (LessWrong)**
  - https://www.lesswrong.com/posts/ByExc3GdvdWEiPHpb/neural-networks-are-singular
  - *Accessible introduction to SLT aimed at ML researchers. Start here.*
- **"Introduction to Singular Learning Theory" (Timaeus/LessWrong sequence)**
  - https://www.lesswrong.com/s/czrXjvCLsqGepybHC
  - *Multi-post sequence building up SLT from foundations. The most accessible extended treatment.*

## Read -- Secondary

- **"Algebraic Geometry and Statistical Learning Theory" by Sumio Watanabe**
  - The definitive textbook. Dense mathematical treatment requiring algebraic geometry background. Read Chapter 1 for the overview and skim Chapter 7 for neural network applications.
- **"Quantifying Degeneracy in Singular Models via the Learning Coefficient" by Lau et al.**
  - https://arxiv.org/abs/2308.12108
  - *Technical paper on estimating the LLC. The practical measurement tool.*
- **"Birth of a Transformer: A Memory Viewpoint" by Edelman et al.**
  - https://arxiv.org/abs/2306.00802
  - *Developmental interpretability in action -- tracking how transformer mechanisms form during training.*

## Read -- Going Deep

- **Timaeus Research -- https://timaeus.co/**
  - The research group most actively connecting SLT to alignment
- **DevInterp (Developmental Interpretability)** community
  - https://devinterp.com/ (or search Alignment Forum for "developmental interpretability")

## Do

**1. Visualize a singularity**

Plot the surface `f(w1, w2) = (w1 * w2)^2` using `matplotlib` 3D surface plot.

Observe:
- The function is zero along both axes (w1 = 0 and w2 = 0), forming a cross-shaped valley
- This is NOT a simple bowl — the Hessian at the origin is the zero matrix
- Compute the Hessian numerically at (0, 0) and at (1, 1). At the origin it should be all zeros; away from the origin it should be positive definite

This cross-shaped valley is what "singular" means — the usual quadratic approximation breaks down completely.

**2. Parameter symmetry demo**

Train a small 2-layer network (e.g., 2-input, 4-hidden, 1-output with ReLU) on a simple regression task (e.g., `y = sin(x)`).

After training:
- Save the loss value
- Swap hidden neurons 0 and 1: permute rows 0,1 of `W1` and the corresponding columns of `W2`
- Recompute the loss — it should be identical (to machine precision)
- Count total symmetries: for `n = 4` hidden neurons, there are `4! = 24` equivalent parameterizations

Print: `"Loss before swap: {:.6f}, Loss after swap: {:.6f}, Total symmetries: 24"`

**3. LLC tracking during grokking**

Reproduce a grokking experiment: train a small transformer on modular addition (`(a + b) mod 97`). Use a tiny model (1-2 layers, ~10k parameters) with a large weight decay.

The model should:
- Memorize the training set quickly (training loss → 0 within ~100 epochs)
- Generalize suddenly much later (~1000-5000 epochs — the "grokking" moment)

Plot training loss AND test loss vs epoch on the same axes. The sudden drop in test loss is the phase transition.

If LLC estimation tools are available (e.g., from the `devinterp` package), track the LLC during training and look for a discontinuity at the grokking point — the LLC should decrease sharply, indicating the model has found a simpler (lower effective complexity) solution.

**4. Reflection (written, ~200 words)**

At the moment of grokking, the model transitions from a memorization strategy (high RLCT, many parameters needed) to an algorithmic strategy (low RLCT, the modular addition circuit is simple). Write up:
- What does this tell us about the relationship between loss landscape geometry and learned circuits?
- Why might SLT be useful for alignment? (Hint: if deceptive behavior is functionally complex, it would have a higher RLCT than honest behavior)

## ML and Alignment Connection

SLT explains the central mystery of deep learning: why do overparameterized models generalize? The answer isn't "regularization" (though that helps) -- it's that the effective complexity (RLCT) is much smaller than the parameter count. The singularities in the loss landscape enforce a form of implicit simplicity bias. Understanding this is understanding *why* deep learning works at all.

SLT is one of the most promising mathematical frameworks for alignment because it connects three things that alignment needs connected:

1. **What the model has learned** (functional complexity, measured by RLCT)
2. **How it learned it** (phase transitions during training, tracked by LLC)
3. **What it will do** (generalization behavior, predicted by the free energy)

If we can measure a model's functional complexity precisely enough, we might detect deceptive strategies (which are functionally complex), predict capability emergence, and understand *why* certain training regimes produce aligned or misaligned models. SLT isn't there yet -- but it's the most mathematically principled approach to these questions that currently exists.

---

## Phase 4 Capstone Project — From Neurons to Alignment (~10-14h)

The culminating project for Phase 4: build a transformer from scratch, train it on modular addition (observing grokking), reverse-engineer the learned algorithm using mechanistic interpretability, and investigate alignment-relevant questions.

See the full project spec: [lesson-66-capstone-project.pdf](lesson-66-capstone-project.pdf)

---

## Time to Take the Exam

Phase 4 is complete -- from neurons to transformers to interpretability to the mathematical foundations of why deep learning works. This is the exam that ties it all together.

**[Exam 4B: Mechanistic Interpretability](../assessments/exam-4b-mechanistic-interpretability.md)**
