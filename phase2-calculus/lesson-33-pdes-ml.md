# Lesson 33: PDEs in ML -- Diffusion Models, Numerical Methods, and Score Matching

[<- Previous](lesson-32-helmholtz-laplace.md) | [Back to TOC](../README.md) | [Next: Matrix Calculus ->](lesson-34-matrix-calculus.md)

---

This lesson brings the PDE block full circle by showing how every equation from Lessons 74-77 converges in the mathematical framework behind diffusion generative models. The forward process of a diffusion model is literally the heat equation: data is progressively corrupted by Gaussian noise until it becomes indistinguishable from pure noise. The reverse process -- the one that generates images, audio, and video -- requires learning the score function, the gradient of the log-probability density, which tells you which direction points toward "more probable" data at each noise level. This is a PDE problem solved by a neural network.

The connection runs through stochastic differential equations and the Fokker-Planck equation. The forward SDE adds noise to data along a prescribed schedule; the Fokker-Planck equation describes how the probability density evolves under this process. To reverse it, you need the score function at every noise level -- and this is what the neural network (typically a U-Net or a transformer) learns via score matching. The resulting reverse SDE or probability flow ODE generates samples by starting from pure noise and iteratively denoising. Every major image generator (DALL-E 3, Stable Diffusion, Midjourney) and video generator (Sora) is built on this framework.

Numerical methods matter here too. The forward and reverse processes must be discretized in practice. The choice of discretization scheme (Euler-Maruyama, stochastic Runge-Kutta, exponential integrators) directly affects sample quality and generation speed. Understanding PDE numerics from the finite difference solvers you built in earlier lessons gives you the vocabulary to understand why some samplers (DDIM, DPM-Solver) are faster than others: they use better numerical schemes for the underlying ODE/SDE.

## Core Learning

- Forward diffusion process: dx = f(x,t)dt + g(t)dW (an SDE that progressively adds noise to data)
- Common schedules: variance-preserving (VP), variance-exploding (VE), sub-VP -- these determine f and g
- Fokker-Planck equation: dp/dt = -nabla . (f*p) + (1/2) nabla . (g^2 nabla p) describes how the probability density p(x,t) evolves under the forward SDE
- Score function: s(x,t) = nabla_x log p_t(x) -- the gradient of log-probability, pointing toward high-density regions
- Score matching: train a neural network s_theta(x,t) to approximate the true score by minimizing E[||s_theta - nabla_x log p_t||^2]; denoising score matching makes this tractable
- Reverse SDE: dx = [f - g^2 * s(x,t)]dt + g*dW_bar -- requires the learned score to run backward in time
- Probability flow ODE: dx/dt = f - (1/2)g^2 * nabla_x log p_t(x) -- a deterministic ODE that generates the same marginal distributions as the reverse SDE; enables exact likelihood computation
- Connection between score and denoising: the optimal denoiser at noise level sigma is related to the score by s(x,t) = (D(x,t) - x) / sigma^2, where D is the denoiser
- Numerical discretization: Euler-Maruyama for SDEs, predictor-corrector methods, exponential integrators; fewer steps = faster generation but lower quality

## Watch -- Primary

- **Jason Bramburger -- PDEs Course** (Numerical methods sections)
  - https://www.youtube.com/@jasonbramburger
  - *Finite difference methods, stability analysis, and discretization of PDEs -- the numerical foundations that samplers rely on.*

## Watch -- Secondary

- **Yang Song -- "Score-Based Generative Modeling" lectures/talks**
  - *The creator of score-based diffusion models explains the SDE framework, score matching, and the connection to PDEs. Essential for understanding the full mathematical picture.*

## Read

- **Yang Song et al., "Score-Based Generative Modeling through Stochastic Differential Equations" (2021)**
  - https://arxiv.org/abs/2011.13456
  - *The foundational paper unifying diffusion models through the SDE/PDE lens.*
- **Calvin Luo, "Understanding Diffusion Models: A Unified Perspective" (2022)**
  - https://arxiv.org/abs/2208.11970
  - *Comprehensive tutorial connecting DDPM, score matching, SDEs, and Fokker-Planck.*

## Key Equations

**Forward SDE:**
$$dx = f(x,t)\, dt + g(t)\, dW$$

**Score function:**
$$s(x,t) = \nabla_x \log p_t(x)$$

**Reverse SDE:**
$$dx = \big[f(x,t) - g(t)^2\, \nabla_x \log p_t(x)\big]\, dt + g(t)\, d\bar{W}$$

**Fokker-Planck equation:**
$$\frac{\partial p}{\partial t} = -\nabla \cdot (f\, p) + \frac{1}{2} \nabla \cdot \big(g^2 \nabla p\big)$$

**Probability flow ODE:**
$$\frac{dx}{dt} = f(x,t) - \frac{1}{2} g(t)^2\, \nabla_x \log p_t(x)$$

**Denoising score matching objective:**
$$\mathcal{L}(\theta) = \mathbb{E}_{t, x_0, \epsilon}\!\left[\big\| s_\theta(x_t, t) - \nabla_{x_t} \log p(x_t | x_0) \big\|^2\right]$$

**Score-denoiser relationship** (Gaussian noise with variance $\sigma^2$):
$$\nabla_x \log p(x_t | x_0) = -\frac{x_t - x_0}{\sigma^2} = \frac{\epsilon}{\sigma} \quad \text{(predicting noise } \epsilon \text{)}$$

## Block D Capstone Project — PDE Solver & Mini Diffusion Model (4h)

**C++ Component (~1h):**
1. Build finite difference solvers for the heat equation (u_t = α u_xx) and wave equation (u_tt = c² u_xx) in C++
2. Output time-step snapshots to CSV — visualize heat diffusion (information-losing) vs wave propagation (information-preserving) side by side

**Python Component (~3h):**
3. Implement forward diffusion as progressive Gaussian noise on 2D data (mixture of Gaussians). Visualize the data distribution at t = 0, T/4, T/2, 3T/4, T — confirm convergence to standard Gaussian
4. Train a small score network s_θ(x,t) ≈ ∇_x log p_t(x) using denoising score matching. Use a 3-layer MLP with time conditioning
5. Reverse the diffusion via Euler-Maruyama SDE solver to generate new samples. Compare generated vs original distribution. Connect every step to PDE theory from this block

## ML and Alignment Connection

This lesson IS the ML connection. Diffusion models -- DALL-E 3, Stable Diffusion, Midjourney, Sora -- are the most successful generative models as of 2024-2026. They work by running the heat equation forward (adding noise to data, destroying structure) and learning to reverse it (denoising, creating structure). The score function nabla_x log p(x) is what the neural network learns: it is a vector field pointing toward higher-probability regions of data space at every noise level.

The Fokker-Planck equation from Lesson 74 describes how the data distribution evolves into noise during the forward process. The reverse SDE uses the learned score to undo this evolution -- literally solving a PDE backward in time. The probability flow ODE provides an alternative that enables exact likelihood computation, connecting diffusion models to normalizing flows (Lesson 16's change of variables).

For alignment, this framework raises critical questions. Conditioning (text prompts, safety classifiers) modifies the score function: classifier-free guidance replaces s(x,t) with s(x,t) + w * [s(x,t|c) - s(x,t)], amplifying the influence of the condition c. Understanding this mathematically is essential for building reliable safety filters for generative models. The score function also reveals what the model considers "probable" -- analyzing learned score fields is a form of mechanistic interpretability for diffusion models. If we can understand and control the score function, we can control what the model generates.
