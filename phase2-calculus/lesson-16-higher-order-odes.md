# Lesson 16: Higher-Order Linear ODEs, Mechanical Vibrations, and Power Series Solutions

[<- Previous](lesson-15-first-order-odes.md) | [Back to TOC](../README.md) | [Next: Laplace Transform ->](lesson-17-laplace-transform.md)

---

## Core Learning

- Analyze autonomous equations qualitatively using phase line diagrams: identify equilibrium points and classify them as stable, unstable, or semi-stable
- Understand the logistic growth model as the canonical autonomous ODE example
- Solve constant-coefficient second-order linear ODEs using the characteristic equation
- Handle all three cases of the characteristic equation: distinct real roots, repeated roots, and complex conjugate roots
- Extend constant-coefficient methods to higher-order ODEs (3rd order and above) via higher-degree characteristic polynomials
- Test linear independence of solutions using the Wronskian: W(y_1, y_2) = y_1 y_2' - y_1' y_2; nonzero Wronskian guarantees a fundamental solution set
- Interpret second-order ODEs as damped oscillators: overdamped, critically damped, underdamped, and forced oscillations
- Recognize resonance as what happens when the forcing frequency matches the natural frequency
- Use the method of undetermined coefficients to find particular solutions for nonhomogeneous equations
- Understand variation of parameters as a general-purpose method for particular solutions
- Solve ODEs using power series: assume y = sum a_n x^n, substitute, and find recurrence relations for the coefficients
- Classify points as ordinary or singular, and understand when power series solutions are valid

## Watch --- Primary

- **Trefor Bazett --- ODE Course (Second-Order Theory through Power Series Solutions)**
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxde-SlgmWlCmNHroIWtujBw
  - *Continue through the playlist from video 13 onward. The sequence is: 2nd-order theory and existence/uniqueness, constant-coefficient homogeneous (all three cases), higher-order constant-coefficient, linear independence and the Wronskian, theory of higher-order DEs, mechanical vibrations (undamped then damped), undetermined coefficients, variation of parameters, then power series solutions (ordinary vs singular points and Airy's equation). Follow this order through the playlist.*

## Watch --- Secondary

- **3Blue1Brown --- "But what is a differential equation?"**
  - https://www.youtube.com/watch?v=p_di4Zn4wz4
  - *The pendulum example in this video is a second-order ODE. Revisit for the geometric intuition of phase space (position, velocity) for second-order systems.*
- **Steve Brunton --- Second-Order Systems and Oscillations**
  - https://www.youtube.com/c/Eigensteve
  - *Applied perspective on damping, resonance, and how second-order dynamics appear in engineering systems.*

## Read

- **Paul's Online Math Notes --- Second Order Differential Equations**
  - https://tutorial.math.lamar.edu/Classes/DE/SecondOrder.aspx
  - *Complete coverage of all solution methods with worked examples.*
- **Paul's Online Math Notes --- Series Solutions to Differential Equations**
  - https://tutorial.math.lamar.edu/Classes/DE/SeriesSolutions.aspx
  - *Covers power series method, ordinary and singular points, with worked examples.*
- **Strogatz, "Nonlinear Dynamics and Chaos"** --- Chapter 5.1-5.3 (Linear Systems)
  - *Covers the eigenvalue classification of 2D systems, which is the matrix formulation of second-order equations.*

## Key Equations

**Autonomous equations --- phase line analysis:**

An autonomous ODE $dy/dt = f(y)$ can be analyzed qualitatively without solving:

1. Find equilibria: set $f(y^*) = 0$
2. Draw the phase line: mark equilibria on a vertical $y$-axis, draw arrows up where $f(y) > 0$ and down where $f(y) < 0$
3. Classify each equilibrium:
   - **Stable** (attractor): arrows point toward it from both sides ($f'(y^*) < 0$)
   - **Unstable** (repeller): arrows point away from both sides ($f'(y^*) > 0$)
   - **Semi-stable**: arrows point toward from one side, away from the other

**The logistic growth model:**

$$\frac{dP}{dt} = rP\left(1 - \frac{P}{K}\right)$$

- $r$ = growth rate, $K$ = carrying capacity
- Equilibria: $P^* = 0$ (unstable) and $P^* = K$ (stable)
- Solutions starting between 0 and $K$ grow sigmoidally toward $K$

**Constant-coefficient second-order homogeneous ODE:**

$$ay'' + by' + cy = 0$$

**Characteristic equation:**

$$ar^2 + br + c = 0$$

**Three cases for the homogeneous solution:**

1. **Distinct real roots** $r_1 \neq r_2$: $\quad y_h = c_1 e^{r_1 x} + c_2 e^{r_2 x}$

2. **Repeated root** $r_1 = r_2 = r$: $\quad y_h = c_1 e^{rx} + c_2\, x\, e^{rx}$

3. **Complex conjugate roots** $r = \alpha \pm \beta i$: $\quad y_h = e^{\alpha x}\left(c_1 \cos\beta x + c_2 \sin\beta x\right)$

**Wronskian (linear independence test):**

$$W(y_1, y_2) = \begin{vmatrix} y_1 & y_2 \\ y_1' & y_2' \end{vmatrix} = y_1 y_2' - y_1' y_2$$

If $W \neq 0$ on an interval, then $y_1, y_2$ are linearly independent and form a fundamental solution set.

**Damped harmonic oscillator (spring-mass system):**

$$m\ddot{x} + b\dot{x} + kx = F(t)$$

- Underdamped ($b^2 < 4mk$): oscillates while decaying
- Critically damped ($b^2 = 4mk$): fastest non-oscillatory decay
- Overdamped ($b^2 > 4mk$): slow exponential decay, no oscillation

**Resonance:** when forcing frequency matches natural frequency $\omega_0 = \sqrt{k/m}$, amplitude grows without bound (in the undamped case).

**Nonhomogeneous equation:**

$$ay'' + by' + cy = g(x) \quad \Longrightarrow \quad y = y_h + y_p$$

where $y_p$ is a particular solution found by undetermined coefficients or variation of parameters.

**Power series solution method:**

Assume $y = \sum_{n=0}^{\infty} a_n x^n$, substitute into the ODE, match coefficients of each power of $x$, and derive a recurrence relation for the $a_n$. Valid at ordinary points (where the coefficient functions are analytic). A point $x_0$ is **singular** if the leading coefficient vanishes there.

**Airy's equation** (canonical example):

$$y'' - xy = 0$$

Has no closed-form solution in elementary functions but is solved exactly by the power series method, yielding two linearly independent series solutions.

**SGD with momentum as a second-order ODE:**

$$\frac{d^2 W}{dt^2} + \gamma \frac{dW}{dt} = -\nabla L(W)$$

This is exactly a damped oscillator with the loss gradient as the driving force.

## ML and Alignment Connection

Phase line analysis of autonomous equations is the simplest version of training dynamics analysis. When you ask "does this training process converge?", you are asking whether the loss minimum is a stable equilibrium of the gradient flow ODE $dW/dt = -\nabla L(W)$. A loss minimum is a stable equilibrium (arrows point toward it); a saddle point is unstable (arrows point away in at least one direction). The logistic growth model's sigmoid solution also appears directly as the sigmoid activation function --- same ODE, different context.

Momentum in SGD is a second-order ODE, and the entire vocabulary of mechanical vibrations applies directly. The update rule with momentum --- $\Delta w = -\eta \nabla L + \beta \Delta w_{\text{prev}}$ --- is discretized from $\ddot{W} + \gamma \dot{W} = -\nabla L$, which is a damped oscillator driven by the loss gradient. The momentum coefficient beta controls damping: too little damping (beta close to 1) and the optimizer oscillates wildly around the minimum like an underdamped spring. Too much damping and convergence is sluggish. The critical damping point gives the fastest convergence without oscillation.

Resonance has a direct training analogue: when the learning rate and momentum are tuned so that the optimizer's natural frequency matches some structure in the loss landscape, you can get catastrophic oscillation --- the training loss explodes. This is learning rate instability, and it is the same phenomenon as a bridge resonating with wind. Understanding the characteristic equation of the optimizer's ODE lets you predict exactly which learning rate and momentum combinations will be stable, which is essential for training large models reliably. The eigenvalues of the Hessian set the natural frequencies; the optimizer parameters must be chosen so that no mode is driven into resonance.

Power series solutions connect to ML through the broader principle that not every function has a neat closed form --- but you can still represent and compute with it via series. Neural networks themselves are universal function approximators, and understanding when exact symbolic solutions exist versus when you need numerical/series approximations builds the right intuition for why we need learned approximations in the first place.
