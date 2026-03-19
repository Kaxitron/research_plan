# Lesson 62: Video and Image Generation -- Diffusion Models

[< Mechanistic Interpretability](lesson-61-mech-interp.md) | [Back to TOC](../README.md) | [Next: RL Foundations >](lesson-63-rl-foundations.md)

---

> **Welch Labs framing (Ch. 9):** Diffusion models are the mathematical engine behind DALL-E, Stable Diffusion, Midjourney, and Sora. The core idea is beautiful: destroy structure by adding noise, then learn to reverse the destruction. The connection to the heat equation from physics makes this one of the most elegant applications of the math you have learned.

## Core Learning

- **Forward diffusion process:** systematically add Gaussian noise to data over T timesteps until it becomes pure noise. Each step: x_t = sqrt(alpha_t) * x_{t-1} + sqrt(1 - alpha_t) * epsilon. The noise schedule (beta_1, ..., beta_T) controls how fast structure is destroyed.
- **Reverse diffusion process:** learn to undo each noise step. A neural network predicts the noise that was added at each step, then subtracts it. Start from pure noise, iteratively denoise, and recover a sample from the data distribution.
- **Denoising Diffusion Probabilistic Models (DDPM):** the foundational framework (Ho et al., 2020). The training objective simplifies to: predict the noise epsilon given the noised data x_t and timestep t. Loss = ||epsilon - epsilon_theta(x_t, t)||^2.
- **Score matching:** an alternative perspective. The "score" is the gradient of the log-density: nabla_x log p(x). If you know the score everywhere, you can generate samples by following the score field (Langevin dynamics). Diffusion models learn the score at each noise level.
- **Denoising score matching:** you do not need to know p(x) to learn its score. Adding noise to data and training a denoiser implicitly learns the score function. This connects denoising to density estimation.
- **Connection to the heat equation:** forward diffusion IS the heat equation from physics -- information (structure) dissipates over time exactly as heat spreads. Reverse diffusion is "running the heat equation backward," which is classically impossible without learned information about the data distribution.
- **Probability flow ODE:** the stochastic diffusion process has a deterministic counterpart -- an ordinary differential equation that traces the same marginal distributions. This connects diffusion models to neural ODEs and enables exact likelihood computation.

## Watch

1. **Welch Labs -- Ch. 9 video on Diffusion Models**
   - *Book: Welch Labs, "The Illustrated Guide to AI," Ch. 9*
   - *The visual treatment of forward/reverse diffusion and the connection to the heat equation.*

## Read

- **"Denoising Diffusion Probabilistic Models" by Ho, Jain, and Abbeel (2020)**
  - https://arxiv.org/abs/2006.11239
  - *The foundational DDPM paper. Establishes the framework, derives the simplified training objective, and demonstrates high-quality image generation.*
- **"Understanding Diffusion Models: A Unified Perspective" by Luo (2022)**
  - https://arxiv.org/abs/2208.11970
  - *An excellent tutorial that unifies the DDPM, score-matching, and SDE perspectives into one coherent picture.*
- **Lilian Weng -- "What are Diffusion Models?"**
  - https://lilianweng.github.io/posts/2021-07-11-diffusion-models/
  - *Clear, well-illustrated blog post covering the math and intuition.*

## Do

**1. Create a 2D target distribution**

Generate 1000 points from a mixture of 4 Gaussians centered at `(±2, ±2)` with `σ = 0.3`. Plot them — you should see four clear clusters.

**2. Implement forward diffusion**

Define a linear noise schedule: `β_t` linearly from 0.0001 to 0.02 over `T = 200` steps. Compute `α_bar_t = cumulative product of (1 - β_t)`.

The forward process: `x_t = sqrt(α_bar_t) * x_0 + sqrt(1 - α_bar_t) * ε` where `ε ~ N(0, I)`.

Plot the data at `t = 0, 50, 100, 150, 200`. The clusters should progressively blur into a uniform Gaussian cloud.

**3. Train a noise predictor**

Build a small MLP (3 hidden layers, 128 units, ReLU) that takes `(x_t, t)` as input and predicts the noise `ε` that was added.

Training loop:
```python
for step in range(5000):
    t = random timestep
    x_0 = random batch from data
    eps = random noise
    x_t = sqrt(alpha_bar[t]) * x_0 + sqrt(1 - alpha_bar[t]) * eps
    eps_pred = model(x_t, t)
    loss = MSE(eps_pred, eps)
```

Use Adam with `lr = 1e-3`. The loss should decrease steadily.

**4. Reverse diffusion (sampling)**

Starting from `x_T ~ N(0, I)`, iteratively denoise:
```python
for t in reversed(range(T)):
    eps_pred = model(x_t, t)
    x_{t-1} = (1/sqrt(α_t)) * (x_t - β_t/sqrt(1-α_bar_t) * eps_pred) + sqrt(β_t) * z
```

Generate 1000 new samples. Plot alongside the original data — if training worked, you should see four clusters in roughly the same locations.

**5. Score field visualization**

For a grid of points, plot the predicted noise `ε_θ(x, t)` as arrows at several noise levels (`t = 10, 50, 100, 190`). At low noise, arrows should point toward the nearest cluster center. At high noise, the field should be nearly uniform.

## ML and Alignment Connection

Diffusion models generate images and video that are increasingly realistic and hard to distinguish from real content. Understanding the math behind generation is crucial for several alignment-relevant reasons:

- **Detecting AI-generated content:** understanding the generation process informs detection methods. The artifacts of iterative denoising leave statistical signatures that differ from natural images.
- **Understanding what models "know":** a diffusion model that generates photorealistic faces must have learned a rich internal representation of facial structure, lighting, and geometry. What does this representation look like? Can we apply mechanistic interpretability techniques to understand it?
- **Multimodal alignment:** as AI systems integrate text, image, and video generation (e.g., GPT-4V, Sora), alignment must extend beyond text. The diffusion framework is the dominant approach for the visual modality.
- **Controllability and safety:** steering what diffusion models generate (and preventing harmful generation) requires understanding the generation process mathematically, not just empirically.
