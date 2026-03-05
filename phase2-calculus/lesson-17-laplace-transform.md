# Lesson 17: The Laplace Transform

[<- Previous](lesson-16-higher-order-odes.md) | [Back to TOC](../README.md) | [Next: Systems of ODEs ->](lesson-18-systems-odes.md)

---

## Core Learning

- Understand the Laplace transform as a tool that converts differential equations into algebraic equations
- Compute Laplace transforms of standard functions: constants, exponentials, polynomials, sine, cosine
- Use the derivative property to transform ODEs into algebraic equations in the s-domain, then solve
- Apply the convolution theorem: convolution in the time domain equals multiplication in the s-domain
- Understand the Dirac delta function as an idealized impulse and compute impulse responses
- Perform inverse Laplace transforms using partial fractions and transform tables

## Watch --- Primary

- **Trefor Bazett --- ODE Course (Laplace Transforms)**
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxde-SlgmWlCmNHroIWtujBw
  - *The Laplace transform section of the playlist. Bazett builds from the definition through applications to solving ODEs, with clear worked examples. Pay special attention to the convolution theorem videos.*

## Watch --- Secondary

- **3Blue1Brown --- "But what does the Laplace transform really do?"**
  - https://www.youtube.com/watch?v=n2y7n6jw5d0
  - *If available, this gives the geometric/visual intuition for what the transform "means" rather than just how to compute it.*
- **Zach Star or Dr. Peyam --- Laplace Transform intuition videos**
  - *Search for supplementary intuition-building if the mechanical computation feels unmotivated.*

## Read

- **Paul's Online Math Notes --- Laplace Transforms**
  - https://tutorial.math.lamar.edu/Classes/DE/LaplaceIntro.aspx
  - *Complete walkthrough with examples: definition, transform tables, solving IVPs, convolution, step and delta functions.*
- **Strogatz, "Nonlinear Dynamics and Chaos"** --- does not cover Laplace transforms directly, but the frequency-domain thinking connects to Chapter 8 (bifurcations in 2D).

## Key Equations

**Definition of the Laplace transform:**

$$\mathcal{L}\{f(t)\} = F(s) = \int_0^{\infty} e^{-st} f(t)\, dt$$

**Key transform pairs:**

| $f(t)$           | $F(s)$                  |
|-------------------|-------------------------|
| $1$               | $1/s$                   |
| $t^n$             | $n!/s^{n+1}$           |
| $e^{at}$          | $1/(s-a)$              |
| $\sin(\omega t)$  | $\omega/(s^2+\omega^2)$ |
| $\cos(\omega t)$  | $s/(s^2+\omega^2)$      |
| $\delta(t)$       | $1$                     |

**Transform of derivatives:**

$$\mathcal{L}\{f'(t)\} = sF(s) - f(0)$$

$$\mathcal{L}\{f''(t)\} = s^2 F(s) - sf(0) - f'(0)$$

**Solving an ODE:** Apply $\mathcal{L}$ to both sides, substitute initial conditions, solve for $Y(s)$, then invert: $y(t) = \mathcal{L}^{-1}\{Y(s)\}$.

**Convolution theorem:**

$$\mathcal{L}\{(f * g)(t)\} = F(s) \cdot G(s)$$

where $(f * g)(t) = \int_0^t f(\tau)\, g(t - \tau)\, d\tau$.

**Impulse response:** The response to $\delta(t)$ is the system's fundamental building block. Any input can be decomposed as a sum of impulses, and the output is the convolution of the input with the impulse response.

## ML and Alignment Connection

The convolution theorem --- that convolution in the time/spatial domain equals pointwise multiplication in the frequency/transform domain --- is the mathematical foundation underlying convolutional neural networks. When a CNN applies a learned filter to an image, it is performing a convolution. The Fourier and Laplace transforms reveal that this same operation could be done as multiplication in the frequency domain, which is why FFT-based convolution is used to accelerate large-kernel operations. Understanding this duality between domains is essential for grasping why certain architectures work and how to make them efficient.

The impulse response concept connects to understanding how neural networks respond to perturbations. If you feed a small, localized change into a network (an "impulse" in the input), the impulse response tells you how that perturbation propagates through layers. This is directly relevant to adversarial robustness: adversarial examples are small input perturbations that cause large output changes, meaning the network's impulse response is poorly behaved. The Laplace/transfer-function framework gives tools for analyzing such input-output relationships systematically, and it connects to the broader question of how sensitive an AI system's behavior is to small changes in its inputs --- a core concern in alignment.
