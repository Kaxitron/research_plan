# Lesson 76: The Wave Equation -- Vibrations and d'Alembert

[<- Previous](lesson-75-separation-fourier.md) | [Back to TOC](../README.md) | [Next: Helmholtz, Laplace, and Transport Equations ->](lesson-77-helmholtz-laplace.md)

---

The wave equation is the prototypical hyperbolic PDE, governing vibrating strings, sound waves, electromagnetic radiation, and seismic activity. Where the heat equation diffuses and smooths, the wave equation propagates and preserves. An initial disturbance on a string splits into two pulses traveling in opposite directions at speed c -- information moves but is not destroyed. This fundamental contrast between diffusion (information loss) and wave propagation (information preservation) runs through all of physics and, as we will see, through neural network architecture design.

The wave equation can be solved by separation of variables (yielding standing waves as superpositions of spatial modes oscillating in time) or by d'Alembert's formula, which expresses the solution as a sum of left- and right-traveling waves. The d'Alembert approach reveals the characteristic lines x +/- ct along which information travels -- these are the "light cones" of the PDE. Points outside the characteristic cone of an initial disturbance are completely unaffected by it, a stark contrast to the heat equation where any initial disturbance is instantly felt everywhere (though exponentially weakly).

Standing waves emerge when traveling waves reflect off boundaries and interfere constructively. The allowed frequencies form a discrete spectrum determined by the boundary conditions -- this is the physics behind musical harmonics and is mathematically identical to the eigenvalue problems of Lesson 75. The wave equation thus provides a second major application of Fourier series and eigenfunction expansions, reinforcing those techniques in a context where modes oscillate rather than decay.

## Core Learning

- Wave equation derivation: Newton's second law applied to a small element of a vibrating string yields utt = c^2 * uxx, where c = sqrt(tension/density) is the wave speed
- The wave equation is hyperbolic (B^2 - AC > 0 in the classification scheme)
- d'Alembert's solution: u(x,t) = f(x - ct) + g(x + ct) -- superposition of right- and left-traveling waves determined by initial displacement and velocity
- Characteristic lines: x - ct = const and x + ct = const; information propagates along these lines at finite speed c
- Separation of variables yields standing waves: u(x,t) = sin(n*pi*x/L) * cos(n*pi*c*t/L) -- spatial modes oscillating in time (contrast: spatial modes decaying in heat equation)
- Superposition principle: linear combinations of solutions are solutions (linearity of the wave equation)
- Energy conservation: the wave equation conserves total energy (kinetic + potential), unlike the heat equation which dissipates energy
- Fundamental contrast: waves propagate information at finite speed; heat diffuses information instantly but weakly. Waves preserve; heat destroys.

## Watch -- Primary

- **Jason Bramburger -- PDEs Course** (Wave equation sections)
  - https://www.youtube.com/@jasonbramburger
  - *Derivation, d'Alembert's solution, and the connection to standing waves.*

## Watch -- Secondary

- **3Blue1Brown -- Differential Equations series** (wave equation segments)
  - *Visual comparison of wave propagation versus heat diffusion -- seeing the difference is more illuminating than reading about it.*

## Read

- **Haberman, *Applied Partial Differential Equations***, Ch. 4: Wave equation, d'Alembert, characteristics
- **Strauss, *Partial Differential Equations: An Introduction***, Ch. 2: Waves and d'Alembert

## Key Equations

**Wave equation (1D):**
$$\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}$$

**d'Alembert's solution:**
$$u(x,t) = f(x - ct) + g(x + ct)$$

**d'Alembert with initial conditions** $u(x,0) = \phi(x)$, $u_t(x,0) = \psi(x)$:
$$u(x,t) = \frac{1}{2}\big[\phi(x-ct) + \phi(x+ct)\big] + \frac{1}{2c}\int_{x-ct}^{x+ct} \psi(s)\, ds$$

**Standing waves** (Dirichlet BCs on $[0, L]$):
$$u_n(x,t) = \sin\!\left(\frac{n\pi x}{L}\right) \cos\!\left(\frac{n\pi c t}{L}\right)$$

**General solution via Fourier:**
$$u(x,t) = \sum_{n=1}^{\infty} \left[ A_n \cos\!\left(\frac{n\pi c t}{L}\right) + B_n \sin\!\left(\frac{n\pi c t}{L}\right) \right] \sin\!\left(\frac{n\pi x}{L}\right)$$

**Energy conservation:**
$$E(t) = \frac{1}{2}\int_0^L \left[ u_t^2 + c^2 u_x^2 \right] dx = \text{const}$$

## Do

1. **Wave equation finite difference solver.** Implement the 1D wave equation on [0, L] using central differences in both space and time: u(i, n+1) = 2*u(i,n) - u(i,n-1) + (c*dt/dx)^2 * [u(i+1,n) - 2*u(i,n) + u(i-1,n)]. Use the CFL condition c*dt/dx <= 1 for stability. Start with a Gaussian pulse initial condition and zero initial velocity. Animate the solution and observe the pulse splitting into two traveling waves.

2. **Wave vs heat comparison.** From the same initial condition (a Gaussian bump), solve both the wave equation and the heat equation. Create a side-by-side animation. Observe: the wave splits and propagates while preserving its shape; the heat diffuses, spreads, and loses amplitude. The wave solution has the same total energy at all times; the heat solution's "energy" (integral of u^2) decreases monotonically.

3. **Standing waves and harmonics.** Set up a vibrating string (Dirichlet BCs at both ends). Initialize with the first 3 Fourier modes individually and visualize each standing wave. Then initialize with a plucked string (triangular initial condition) and decompose into Fourier modes. Animate the full solution and verify it is a superposition of standing waves.

## ML and Alignment Connection

Waves propagate information without losing it; heat diffuses and destroys information. This distinction is directly relevant to neural network architecture design. Residual connections (y = x + f(x)) preserve the input signal like a wave -- information passes through even if f contributes nothing. Without residual connections, deep networks behave more like the heat equation: signals attenuate and gradients vanish as they propagate through layers.

This is why ResNets, transformers (which are residual by construction), and other skip-connection architectures can be trained to extreme depth while plain deep networks cannot. The mathematical reason is the same as why the wave equation preserves energy while the heat equation dissipates it. For alignment-critical applications where you need reliable signal propagation -- where a safety-relevant input feature must influence the output even through 100+ layers -- wave-like (residual) architectures are essential.

The characteristic lines of the wave equation also connect to the concept of receptive fields in neural networks: information from an input at position x can only reach outputs within a certain cone, determined by the architecture. Understanding how information propagation speed depends on architecture is important for ensuring that safety-relevant context is actually "visible" to the output layer.
