# Lesson 21: Multiple Integration and Change of Variables

[<- Previous](lesson-20-multivariable-chain-rule.md) | [Back to TOC](../README.md) | [Next: Taylor Expansions ->](lesson-22-taylor-expansions.md)

**Prerequisite note:** This lesson also depends on Lesson 7 (determinants). The Jacobian determinant from change-of-variables is the same determinant you studied in the linear algebra phase -- it measures how a transformation stretches or compresses volume.

---

## Core Learning

- Double and triple integrals extend single-variable integration to higher dimensions. A double integral computes the "volume" under a surface over a 2D region; a triple integral computes the "hypervolume" over a 3D region. Fubini's theorem says you can evaluate these as iterated integrals -- integrate one variable at a time -- and you can swap the order of integration when the integrand is continuous. Setting up the correct bounds is often the hardest part.
- Change of variables is the multivariable analogue of u-substitution. When you transform coordinates (e.g., Cartesian to polar), the area/volume element picks up a factor of |det(J)|, where J is the Jacobian matrix of the transformation. This is why dA = r dr d(theta) in polar coordinates -- the factor r IS the Jacobian determinant. Cylindrical and spherical coordinates are the standard 3D extensions, and the general formula works for any invertible smooth coordinate change.
- The Gaussian integral (integral of e^{-x^2} from -infinity to infinity = sqrt(pi)) is proved using a polar coordinate change of variables and is one of the most important single results in all of applied mathematics. It is the reason the normal distribution normalizes. Monte Carlo integration -- approximating integrals by random sampling -- provides a practical alternative when analytical integration is intractable, which is nearly always the case in high-dimensional ML problems.

## Watch -- Primary

- **Trefor Bazett -- Multivariable Calculus** (double integrals, triple integrals, change of variables sections)
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxc_CvEy7xBKRQr6I214QJcd
  - Focus on the videos covering iterated integrals, Fubini's theorem, polar/cylindrical/spherical coordinates, and the Jacobian determinant.

## Watch -- Secondary

- **3Blue1Brown -- "But what is a convolution?"**
  - https://www.youtube.com/watch?v=KuXjwB4LzSA
  - Convolution involves integrating the product of two functions -- relevant background for understanding how Gaussian kernels interact with integration.
- **Trefor Bazett -- Multivariable Calculus** (Gaussian integral derivation)
  - Same playlist. Look for the video proving the Gaussian integral via polar coordinates.

## Read

- **Stewart's Calculus** -- Chapters on multiple integrals (typically Chapter 15-16). Covers iterated integrals, change of variables, and all three coordinate systems with worked examples.
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

## Do

1. **Monte Carlo integration.** Implement Monte Carlo integration to estimate the integral of f(x) = e^{-x^2} from -5 to 5 (which should be close to sqrt(pi)). Plot the estimate as a function of N (number of samples) on a log scale. Show that the error decreases as 1/sqrt(N) regardless of dimension.

2. **High-dimensional comparison.** Extend your Monte Carlo integrator to compute the volume of the unit ball in d = 2, 5, 10, 20 dimensions (fraction of random points in the unit cube that land inside the unit ball). Compare with the analytical formula. Observe how grid-based quadrature becomes hopeless but Monte Carlo still works (the "curse of dimensionality" for grids).

3. **Gaussian integral numerically.** Compute the Gaussian integral numerically by: (a) direct numerical quadrature (scipy.integrate.quad), (b) Monte Carlo sampling, and (c) the polar coordinates trick implemented numerically (integrate in polar, transform back). Verify all three give sqrt(pi).

```python
import numpy as np

def monte_carlo_integrate(f, a, b, N=100000):
    """Monte Carlo estimate of integral of f from a to b."""
    x = np.random.uniform(a, b, N)
    return (b - a) * np.mean(f(x))

# Estimate the Gaussian integral
f = lambda x: np.exp(-x**2)
estimates = []
Ns = [100, 1000, 10000, 100000, 1000000]
for N in Ns:
    est = monte_carlo_integrate(f, -5, 5, N)
    estimates.append(est)
    print(f"N={N:>8d}: estimate = {est:.6f}, true = {np.sqrt(np.pi):.6f}, "
          f"error = {abs(est - np.sqrt(np.pi)):.6f}")
```

## ML and Alignment Connection

The Gaussian integral is WHY the normal distribution normalizes to 1 -- without it, Gaussian distributions (which appear everywhere in ML: weight initialization, noise models, variational inference, diffusion models) would not be valid probability distributions. The proof via polar coordinates is a beautiful application of the change-of-variables formula.

Monte Carlo integration is how we approximate intractable expectations in Bayesian ML and reinforcement learning. Whenever you see E_{x ~ p}[f(x)] in a paper, it is almost certainly estimated by sampling x_i from p and averaging f(x_i). Importance sampling, MCMC, and the reparameterization trick in VAEs are all refinements of this basic idea.

The Jacobian determinant from the change-of-variables formula reappears in normalizing flows -- a class of generative models that construct complex distributions by composing simple invertible transformations. Each transformation contributes a |det(J)| factor to the density, and training requires computing or efficiently approximating these determinants. This directly connects Lesson 7 (determinants) to modern generative modeling.
