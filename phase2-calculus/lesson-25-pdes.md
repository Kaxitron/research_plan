# Lesson 25: Partial Differential Equations — Diffusion, Heat, and Generative Models

[← Neural ODEs](lesson-24-neural-odes.md) | [Back to TOC](../README.md) | [Next: Matrix Calculus →](lesson-26-matrix-calculus.md)

---

> **Why this lesson exists:** Diffusion models — the engine behind DALL-E, Stable Diffusion, and modern image generation — are built on stochastic PDEs. The forward process adds noise according to a heat equation; the reverse process denoises using a learned score function. You also need PDEs for the Fokker-Planck equation (the probability distribution of SGD), the Black-Scholes equation (decision theory under uncertainty), and the deep connections between probability, physics, and optimization that run through alignment theory.

## 🎯 Core Concepts

### What's a PDE?

- **An ODE** has one independent variable (time). A **partial differential equation** has multiple: the heat equation u_t = ku_{xx} involves both time t and space x. The unknown u(x,t) is a function of multiple variables.
- **We only need a few key PDEs,** not the full PDE theory. The three essential ones for ML: the heat equation, the Fokker-Planck equation, and their stochastic versions.
- **The geometric picture:** where an ODE describes flow along curves, a PDE describes how entire fields (temperature distributions, probability densities, image features) evolve.

### The Heat Equation — Diffusion as Smoothing

- **u_t = k∇²u.** The temperature at each point changes at a rate proportional to how much it differs from its neighbors (the Laplacian ∇²u). Hot spots cool; cold spots warm. Everything smooths toward the average.
- **The solution is a convolution with a Gaussian:** given initial temperature u(x,0), the solution at time t is u(x,t) = u(x,0) * G_t(x) where G_t is a Gaussian with variance 2kt. Diffusion IS Gaussian blurring, where the blur width grows with √t.
- **This is the forward process of diffusion models.** Start with a data sample (the "initial temperature"). Add Gaussian noise progressively. After enough time, everything is just noise — the "equilibrium temperature" is uniform randomness.

### The Fokker-Planck Equation — How Probability Evolves

- **For the SDE** dX = f(X)dt + σ dB_t (deterministic drift f plus noise σ), the probability density p(x,t) evolves according to: ∂p/∂t = -∂(fp)/∂x + (σ²/2)∂²p/∂x². This IS a heat equation with an extra drift term.
- **For SGD:** the Fokker-Planck equation describes the probability distribution over weight space during stochastic training. The steady-state solution gives the Boltzmann distribution p(W) ∝ exp(-L(W)/T) mentioned in Lesson 24. This is the rigorous version of "SGD explores the loss landscape like a particle in a heat bath."
- **For alignment:** the Fokker-Planck equation tells you the probability that training reaches different solutions. If you could solve it (usually you can't), you'd know the probability of arriving at an aligned vs misaligned model.

### Score Functions and Denoising

- **The score function** ∇_x log p(x) is the gradient of log-probability. It points toward regions of high probability — "uphill" on the probability landscape.
- **Score matching:** you can learn the score function from data without knowing the normalization constant of p. This bypasses the intractable integral problem that plagues other generative models.
- **Diffusion model reversal:** the forward SDE adds noise: dX = f(X)dt + σ dB_t. The REVERSE SDE that undoes this requires the score: dX = [f(X) - σ²∇_x log p(X,t)]dt + σ dB̄_t. Train a neural network to approximate the score, and you can generate samples by running the reverse process from pure noise.
- **The connection to ODEs:** there's also a deterministic ODE (the "probability flow ODE") that generates the same distribution as the reverse SDE but without noise. Neural ODEs meet diffusion models.

### Separation of Variables and Fourier Series

- **The standard technique** for solving linear PDEs: assume the solution factors as u(x,t) = X(x)T(t). This converts one PDE into two ODEs, which you can solve separately.
- **Fourier series:** the general solution to the heat equation is a sum of sinusoidal modes, each decaying exponentially at a rate determined by its frequency. High-frequency modes (sharp features) decay fastest — this is why diffusion blurs fine details first and coarse structure last.
- **For ML:** this frequency-dependent decay explains why diffusion models generate images from coarse to fine — the reverse process reconstructs low frequencies (overall layout) before high frequencies (texture and detail).

### The Laplace Transform — A Brief Detour

- **The Laplace transform** converts a time-domain function f(t) into a complex-frequency function: F(s) = ∫₀^∞ f(t)e^{-st} dt, where s = σ + iω is a complex number. It's the "sibling" of the Fourier transform — where Fourier decomposes into pure oscillations (e^{iωt}), Laplace decomposes into exponentially growing/decaying oscillations (e^{st}).
- **Why it exists:** the Fourier transform only works cleanly on functions that don't blow up. The Laplace transform handles transient, decaying, and growing signals by building exponential decay (the e^{-σt} factor) into the decomposition. This makes it the workhorse of control theory and engineering.
- **The core trick:** differentiation becomes multiplication. If ℒ{f(t)} = F(s), then ℒ{f'(t)} = sF(s) - f(0). This converts differential equations into algebraic equations — solve for F(s), then invert to get f(t). It's enormously powerful for linear ODEs.
- **Connection to what you already know:**
  - The **matrix exponential** e^{At} from Lesson 21 can be derived via the inverse Laplace transform: e^{At} = ℒ⁻¹{(sI - A)⁻¹}. The eigenvalues of A become poles in the s-domain — stable systems have poles in the left half-plane (Re(s) < 0), matching the "negative eigenvalues → convergence" rule.
  - The **Fourier transform** is the special case where s = iω (purely imaginary — no growth or decay, just oscillation). Laplace is Fourier's generalization to the full complex plane.
  - **Transfer functions** in control theory — G(s) = output/input in the s-domain — are exactly how engineers analyze feedback systems. This connects to alignment: an RLHF training loop IS a feedback control system, and stability analysis of such loops uses these tools.
- **Why it's not central to this curriculum:** modern ML overwhelmingly uses Fourier methods (spectral analysis, diffusion models) and direct ODE/SDE simulation rather than Laplace techniques. You're unlikely to encounter Laplace transforms in alignment papers. But if you read control theory literature on AI safety (e.g., modeling training dynamics as a control system), you'll see transfer functions and s-domain analysis everywhere.
- **The one thing to remember:** Laplace transforms turn differential equations into algebra by moving to the frequency domain, just as Fourier does — but Laplace handles transient (non-periodic, decaying) behavior that Fourier can't.

## 📺 Watch — Primary

1. **3Blue1Brown — "But what is a partial differential equation?"**
   - https://www.youtube.com/watch?v=ly4S0oi3Yz8
   - *Covers the heat equation with beautiful visualizations of Fourier modes.*
2. **Welch Labs — "But How Do AI Images and Videos Actually Work?" (Ch. 9, w/ 3B1B)**
   - https://www.youtube.com/watch?v=iv-5mZ_9CPY
   - *📖 Book: Welch Labs, "The Illustrated Guide to AI," Ch. 9: Video & Image Generation*
   - *Diffusion models, CLIP, and the math of turning text into images. The perfect application of everything in this lesson — the reverse diffusion process IS a PDE solved backward in time.*
3. **Sander Dieleman — "Diffusion models explained"**
   - *The best accessible explanation connecting PDEs to diffusion generative models.*

## 📺 Watch — Secondary

3. **Steve Brunton — "Fourier Series and Heat Equation"**
   - https://www.youtube.com/c/Eigensteve
4. **3Blue1Brown — "Solving the heat equation" (Diff Eq Ch. 3)**
   - https://www.youtube.com/watch?v=ToIXSwZ1pJU
   - *How Fourier series actually solve the heat equation — watch right after the primary 3B1B PDE video.*
5. **3Blue1Brown — "But what is a Fourier series?" (Diff Eq Ch. 4)**
   - https://www.youtube.com/watch?v=r6sGWTCMz2k
   - *The visual intuition for Fourier decomposition. Essential for understanding how diffusion models work.*

## 📺 Watch — Optional

6. **3Blue1Brown — "e^(iπ) in 3.14 minutes" (Diff Eq Ch. 5)**
   - https://www.youtube.com/watch?v=v0YEaeIClKY
   - *A beautiful 3-minute aside on Euler's identity. Not directly needed but deepens appreciation for complex exponentials in Fourier analysis.*

## 📖 Read — Primary

- **Welch Labs — *The Illustrated Guide to AI*, Ch. 9: Video & Image Generation**
  - http://www.welchlabs.com/resources/ai-book
  - *How diffusion models turn text into images — the reverse diffusion process IS a PDE solved backward in time.*
- **"Understanding Diffusion Models: A Unified Perspective" by Calvin Luo**
  - https://arxiv.org/abs/2208.11970
  - *Comprehensive tutorial connecting all the pieces: SDEs, score matching, Fokker-Planck.*

## 🔨 Do

- Simulate the 1D heat equation numerically: start with a step function, watch it smooth into a Gaussian. Implement both explicit Euler and spectral (Fourier) methods.
- Implement a toy 2D diffusion model: forward process (add noise to MNIST digits), learn the score function with a small neural net, reverse process (denoise). See images emerge from noise.
- Solve the Fokker-Planck equation for the double-well potential L(x) = (x²-1)². Show that the steady-state distribution concentrates at the two minima with relative probability determined by the "temperature" σ².
- Visualize how Fourier modes decay: decompose an image into Fourier components, multiply each by exp(-k²t) for increasing t. Watch the image blur progressively — this is diffusion.

## 🔗 ML & Alignment Connection

- **Diffusion models** are the most successful generative models in 2024-2026. They're pure applied PDE theory.
- **The Fokker-Planck equation** is the theoretical foundation for understanding SGD's implicit bias and the distribution of trained models.
- **Score-based methods** bypass the normalization problem that plagues energy-based models and Boltzmann machines.

- **Controllable generation:** if diffusion models generate content by following a PDE, can we modify the PDE to guarantee the output satisfies safety constraints? Classifier-free guidance is a step in this direction.
- **The Fokker-Planck perspective on training** could, in principle, give probabilistic guarantees about where training ends up. This is a theoretical alignment tool.
---

## 📝 Time to Take the Exam

You've completed Phase 2. From single-variable derivatives to PDEs governing diffusion models, you now speak the language of change and dynamics.

👉 **[Exam 2B: Differential Equations — The Language of Dynamics](../assessments/exam-2b-differential-equations.md)**
