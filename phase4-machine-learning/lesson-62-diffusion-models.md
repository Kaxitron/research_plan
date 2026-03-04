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

- **Implement a simple 2D diffusion model from scratch:**
  1. Define a 2D target distribution (e.g., a mixture of Gaussians or a spiral)
  2. Implement the forward noise schedule: progressively add noise over T steps
  3. Train a small neural network (MLP) to predict the noise at each timestep
  4. Implement the reverse sampling loop: start from pure noise, iteratively denoise
  5. Visualize: plot the generated samples and compare to the target distribution
- **Noise schedule experiment:** try different noise schedules (linear, cosine) and observe how they affect sample quality and training stability
- **Score visualization:** for the 2D case, plot the learned score field (gradient arrows) at different noise levels. Watch how the field points toward data modes at low noise and becomes uniform at high noise.

## ML and Alignment Connection

Diffusion models generate images and video that are increasingly realistic and hard to distinguish from real content. Understanding the math behind generation is crucial for several alignment-relevant reasons:

- **Detecting AI-generated content:** understanding the generation process informs detection methods. The artifacts of iterative denoising leave statistical signatures that differ from natural images.
- **Understanding what models "know":** a diffusion model that generates photorealistic faces must have learned a rich internal representation of facial structure, lighting, and geometry. What does this representation look like? Can we apply mechanistic interpretability techniques to understand it?
- **Multimodal alignment:** as AI systems integrate text, image, and video generation (e.g., GPT-4V, Sora), alignment must extend beyond text. The diffusion framework is the dominant approach for the visual modality.
- **Controllability and safety:** steering what diffusion models generate (and preventing harmful generation) requires understanding the generation process mathematically, not just empirically.
