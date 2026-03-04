# Lesson 16: Higher-Order Linear ODEs and Mechanical Vibrations

[<- Previous](lesson-15-first-order-odes.md) | [Back to TOC](../README.md) | [Next: Laplace Transform ->](lesson-17-laplace-transform.md)

---

## Core Learning

- Solve constant-coefficient second-order linear ODEs using the characteristic equation
- Handle all three cases of the characteristic equation: distinct real roots, repeated roots, and complex conjugate roots
- Use the method of undetermined coefficients to find particular solutions for nonhomogeneous equations
- Understand variation of parameters as a general-purpose method for particular solutions
- Interpret second-order ODEs as damped oscillators: overdamped, critically damped, underdamped, and forced oscillations
- Recognize resonance as what happens when the forcing frequency matches the natural frequency

## Watch --- Primary

- **Trefor Bazett --- ODE Course (Second-Order Linear ODEs, Characteristic Equation, Undetermined Coefficients, Variation of Parameters)**
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxde-SlgmWlCmNHroIWtujBw
  - *Continue through the playlist sections on higher-order equations. Bazett connects the characteristic equation to the exponential ansatz clearly, and his treatment of mechanical vibrations provides excellent physical intuition.*

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
- **Strogatz, "Nonlinear Dynamics and Chaos"** --- Chapter 5.1-5.3 (Linear Systems)
  - *Covers the eigenvalue classification of 2D systems, which is the matrix formulation of second-order equations.*

## Key Equations

**Constant-coefficient second-order homogeneous ODE:**

$$ay'' + by' + cy = 0$$

**Characteristic equation:**

$$ar^2 + br + c = 0$$

**Three cases for the homogeneous solution:**

1. **Distinct real roots** $r_1 \neq r_2$: $\quad y_h = c_1 e^{r_1 x} + c_2 e^{r_2 x}$

2. **Repeated root** $r_1 = r_2 = r$: $\quad y_h = c_1 e^{rx} + c_2\, x\, e^{rx}$

3. **Complex conjugate roots** $r = \alpha \pm \beta i$: $\quad y_h = e^{\alpha x}\left(c_1 \cos\beta x + c_2 \sin\beta x\right)$

**Nonhomogeneous equation:**

$$ay'' + by' + cy = g(x) \quad \Longrightarrow \quad y = y_h + y_p$$

where $y_p$ is a particular solution found by undetermined coefficients or variation of parameters.

**Damped harmonic oscillator (spring-mass system):**

$$m\ddot{x} + b\dot{x} + kx = F(t)$$

- Underdamped ($b^2 < 4mk$): oscillates while decaying
- Critically damped ($b^2 = 4mk$): fastest non-oscillatory decay
- Overdamped ($b^2 > 4mk$): slow exponential decay, no oscillation

**Resonance:** when forcing frequency matches natural frequency $\omega_0 = \sqrt{k/m}$, amplitude grows without bound (in the undamped case).

**SGD with momentum as a second-order ODE:**

$$\frac{d^2 W}{dt^2} + \gamma \frac{dW}{dt} = -\nabla L(W)$$

This is exactly a damped oscillator with the loss gradient as the driving force.

## Do

**Damped Oscillator and SGD Momentum Dynamics**

Simulate a damped harmonic oscillator, then show that SGD with momentum traces similar dynamics on a quadratic loss surface.

```python
import numpy as np
import matplotlib.pyplot as plt

# --- Part 1: Damped Harmonic Oscillator ---

def simulate_oscillator(m, b, k, x0, v0, t_end, dt=0.01):
    """
    Simulate m*x'' + b*x' + k*x = 0.
    Convert to system: x' = v, v' = -(b/m)*v - (k/m)*x
    Use RK4 or scipy.integrate.solve_ivp.

    Returns: t_array, x_array, v_array
    """
    # TODO: implement
    pass

# Simulate three regimes with k=1, m=1:
# 1. Underdamped:  b = 0.5
# 2. Critically damped: b = 2.0
# 3. Overdamped: b = 4.0
# Plot x(t) for all three on the same axes. Label each regime.

# --- Part 2: SGD with Momentum on Quadratic Loss ---

def sgd_momentum(grad_fn, w0, lr, beta, n_steps):
    """
    SGD with momentum: v = beta*v + grad; w = w - lr*v
    grad_fn: callable, takes w and returns gradient
    w0: initial parameters (numpy array)
    Returns: array of w values at each step
    """
    # TODO: implement
    pass

# Quadratic loss: L(w1, w2) = 0.5*(10*w1^2 + w2^2)
# Gradient: dL/dw1 = 10*w1, dL/dw2 = w2
# This is an elongated bowl --- eigenvalues are 10 and 1.
grad_fn = lambda w: np.array([10*w[0], w[1]])
w0 = np.array([1.0, 1.0])

# Tasks:
# 1. Run SGD without momentum (beta=0) with lr=0.05 for 200 steps
# 2. Run SGD with momentum (beta=0.9) with lr=0.05 for 200 steps
# 3. Plot both trajectories on contour plot of the loss
# 4. Observe: without momentum, the trajectory zigzags along the
#    narrow valley. With momentum, the oscillations are damped.
# 5. Vary beta: try 0.5, 0.9, 0.99. Which behaves like underdamped
#    vs critically damped vs overdamped?
# 6. Try lr=0.19 (near stability limit 2/lambda_max = 0.2).
#    Show that without momentum it diverges, but with momentum
#    the damping can stabilize it.
```

**Tasks:**
1. Produce the three-regime oscillator plot (underdamped, critical, overdamped)
2. Produce contour plots comparing SGD with and without momentum
3. Identify which momentum values correspond to which damping regimes
4. Demonstrate the stabilizing effect of momentum near the learning rate limit

## ML and Alignment Connection

Momentum in SGD is a second-order ODE, and the entire vocabulary of mechanical vibrations applies directly. The update rule with momentum --- $\Delta w = -\eta \nabla L + \beta \Delta w_{\text{prev}}$ --- is discretized from $\ddot{W} + \gamma \dot{W} = -\nabla L$, which is a damped oscillator driven by the loss gradient. The momentum coefficient beta controls damping: too little damping (beta close to 1) and the optimizer oscillates wildly around the minimum like an underdamped spring. Too much damping and convergence is sluggish. The critical damping point gives the fastest convergence without oscillation.

Resonance has a direct training analogue: when the learning rate and momentum are tuned so that the optimizer's natural frequency matches some structure in the loss landscape, you can get catastrophic oscillation --- the training loss explodes. This is learning rate instability, and it is the same phenomenon as a bridge resonating with wind. Understanding the characteristic equation of the optimizer's ODE lets you predict exactly which learning rate and momentum combinations will be stable, which is essential for training large models reliably. The eigenvalues of the Hessian set the natural frequencies; the optimizer parameters must be chosen so that no mode is driven into resonance.
