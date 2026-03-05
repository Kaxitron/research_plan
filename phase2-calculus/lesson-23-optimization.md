# Lesson 23: Multiple Integration and Change of Variables

[<- Previous](lesson-22-taylor-expansions.md) | [Back to TOC](../README.md) | [Next: Line Integrals ->](lesson-24-line-integrals.md)

**Prerequisite note:** This lesson also depends on Lesson 7 (determinants). The Jacobian determinant from change-of-variables is the same determinant you studied in the linear algebra phase -- it measures how a transformation stretches or compresses volume.

---

## Core Learning

- Double and triple integrals extend single-variable integration to higher dimensions. A double integral computes the "volume" under a surface over a 2D region; a triple integral computes the "hypervolume" over a 3D region. Fubini's theorem says you can evaluate these as iterated integrals -- integrate one variable at a time -- and you can swap the order of integration when the integrand is continuous. Setting up the correct bounds is often the hardest part.
- Change of variables is the multivariable analogue of u-substitution. When you transform coordinates (e.g., Cartesian to polar), the area/volume element picks up a factor of |det(J)|, where J is the Jacobian matrix of the transformation. This is why dA = r dr d(theta) in polar coordinates -- the factor r IS the Jacobian determinant. Cylindrical and spherical coordinates are the standard 3D extensions, and the general formula works for any invertible smooth coordinate change.
- The Gaussian integral (integral of e^{-x^2} from -infinity to infinity = sqrt(pi)) is proved using a polar coordinate change of variables and is one of the most important single results in all of applied mathematics. It is the reason the normal distribution normalizes. Monte Carlo integration -- approximating integrals by random sampling -- provides a practical alternative when analytical integration is intractable, which is nearly always the case in high-dimensional ML problems.

## Watch -- Primary

- **Trefor Bazett -- Multivariable Calculus** (double integrals, triple integrals, change of variables sections)
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxc_CvEy7xBKRQr6I214QJcd
  - Focus on the videos covering iterated integrals, Fubini's theorem, polar/cylindrical/spherical coordinates, the Jacobian determinant, and the Gaussian integral (roughly videos 25-30 in the playlist).

## Watch -- Secondary

- **3Blue1Brown -- "But what is a convolution?"**
  - https://www.youtube.com/watch?v=KuXjwB4LzSA
  - Convolution involves integrating the product of two functions -- relevant background for understanding how Gaussian kernels interact with integration.
- **Trefor Bazett -- Multivariable Calculus** (Gaussian integral derivation)
  - Same playlist. Look for the video proving the Gaussian integral via polar coordinates.

## Read

- **Stewart's Calculus** -- Chapters on multiple integrals (typically Chapters 15-16). Covers iterated integrals, change of variables, and all three coordinate systems with worked examples.
- **MML Book (Deisenroth, Faisal, Ong)** -- Section 6.3 on change of variables for probability densities. Directly connects the Jacobian determinant to how probability distributions transform.

## Key Equations

Double integral as iterated integral:

$$\iint_R f \, dA = \int_a^b \int_{c(x)}^{d(x)} f(x, y) \, dy \, dx$$

Change of variables formula:

$$\iint f(x, y) \, dA = \iint f(g(u, v)) \, |\det(J_g)| \, du \, dv$$

Polar coordinates area element:

$$dA = r \, dr \, d\theta$$

Spherical coordinates volume element:

$$dV = \rho^2 \sin\phi \, d\rho \, d\theta \, d\phi$$

The Gaussian integral:

$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$

Monte Carlo approximation:

$$\int f(x) p(x) \, dx \approx \frac{1}{N} \sum_{i=1}^{N} f(x_i), \quad x_i \sim p$$

## Block B Capstone Project — Multivariable Calculus Lab (3h)

**C++ Component (~1h):**
1. Implement gradient descent and Newton's method for arbitrary differentiable functions in C++
2. Compute Jacobians and Hessians numerically using finite differences — output optimization trajectories to CSV

**Python Component (~2h):**
3. Visualize gradient descent on 2D loss surfaces with 3D matplotlib surface plots and contour plots — show how Newton's method takes fewer steps but each step is more expensive
4. Build a Lagrange multiplier solver for constrained optimization using scipy. Demonstrate numerically that L2 regularization <-> constrained optimization (show equivalent solutions for matching lambda and C)
5. Implement Monte Carlo integration for a 10-dimensional integral and compare with the analytical result — show convergence rate of 1/sqrt(N)

## ML and Alignment Connection

The Gaussian integral is WHY the normal distribution normalizes to 1 -- without it, Gaussian distributions (which appear everywhere in ML: weight initialization, noise models, variational inference, diffusion models) would not be valid probability distributions. The proof via polar coordinates is a beautiful application of the change-of-variables formula.

Monte Carlo integration is how we approximate intractable expectations in Bayesian ML and reinforcement learning. Whenever you see E_{x ~ p}[f(x)] in a paper, it is almost certainly estimated by sampling x_i from p and averaging f(x_i). Importance sampling, MCMC, and the reparameterization trick in VAEs are all refinements of this basic idea.

The Jacobian determinant from the change-of-variables formula reappears in normalizing flows -- a class of generative models that construct complex distributions by composing simple invertible transformations. Each transformation contributes a |det(J)| factor to the density, and training requires computing or efficiently approximating these determinants. This directly connects Lesson 7 (determinants) to modern generative modeling.
