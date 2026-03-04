# Lesson 15: First-Order ODEs --- Separable, Linear, and Exact

[<- Previous](lesson-14-intro-odes.md) | [Back to TOC](../README.md) | [Next: Higher-Order ODEs ->](lesson-16-higher-order-odes.md)

---

## Core Learning

- Solve separable equations by isolating variables: g(y)dy = f(x)dx
- Solve first-order linear equations using the integrating factor method
- Recognize and solve exact equations where M dx + N dy = 0 with dM/dy = dN/dx
- Understand substitution methods (Bernoulli, homogeneous) as tools for reducing to known forms
- Implement Euler's method and recognize it as the discrete analogue of continuous ODE solutions --- and as gradient descent
- Apply first-order ODEs to population models, mixing problems, and circuit analysis

## Watch --- Primary

- **Trefor Bazett --- ODE Course (Separable, Linear, Exact, Euler's Method)**
  - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxde-SlgmWlCmNHroIWtujBw
  - *Continue through the playlist covering separable equations, integrating factors for linear ODEs, exact equations, and Euler's method. Bazett works through examples methodically and the visual approach helps build solution intuition.*

## Watch --- Secondary

- **3Blue1Brown --- "Differential equations, studying the unsolvable"**
  - https://www.youtube.com/watch?v=p_di4Zn4wz4
  - *Revisit the section on Euler's method and numerical approximation if you want the geometric picture of stepping along the vector field.*

## Read

- **Paul's Online Math Notes --- First Order Differential Equations**
  - https://tutorial.math.lamar.edu/Classes/DE/FirstOrder.aspx
  - *Covers separable, linear, exact, and substitution methods with worked examples and practice problems.*
- **Strogatz, "Nonlinear Dynamics and Chaos"** --- Chapter 2 (Flows on the Line)
  - *Continues the qualitative approach: understanding 1D ODEs through their phase portraits rather than closed-form solutions.*

## Key Equations

**Separable equation:**

$$g(y)\,dy = f(x)\,dx \quad \Longrightarrow \quad \int g(y)\,dy = \int f(x)\,dx + C$$

**First-order linear equation:**

$$y' + P(x)\,y = Q(x)$$

**Integrating factor:**

$$\mu(x) = e^{\int P(x)\,dx}$$

**Solution via integrating factor:**

$$y = \frac{1}{\mu(x)}\left[\int \mu(x)\,Q(x)\,dx + C\right]$$

**Exact equation:**

$$M(x,y)\,dx + N(x,y)\,dy = 0 \quad \text{where} \quad \frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$$

Solution: find $F(x,y)$ such that $\partial F/\partial x = M$ and $\partial F/\partial y = N$; then $F(x,y) = C$.

**Euler's method:**

$$y_{n+1} = y_n + h \cdot f(x_n, y_n)$$

This is gradient descent: $W_{n+1} = W_n - \eta \cdot \nabla L(W_n)$ with $h = \eta$ and $f = -\nabla L$.

## Do

**Integrating Factor Solver and Euler Convergence Study**

Part 1: Implement an integrating factor solver for first-order linear ODEs. Part 2: Implement Euler's method and show that it converges to the exact solution as step size shrinks.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# --- Part 1: Integrating Factor Solver ---

def solve_linear_ode(P, Q, x_span, y0, n_points=200):
    """
    Solve y' + P(x)*y = Q(x) with y(x_span[0]) = y0
    using the integrating factor method (numerically).

    P, Q: callables of x
    Returns: x_array, y_array
    """
    # TODO: Compute mu(x) = exp(integral of P(x) dx) numerically
    # TODO: Compute y(x) = (1/mu(x)) * integral(mu(x)*Q(x) dx)
    #       adjusted for initial condition
    # Hint: use scipy.integrate.cumulative_trapezoid or solve as
    #       a system with scipy.integrate.solve_ivp for comparison
    pass

# Test: y' + 2y = 4x, y(0) = 1
# Exact solution: y = 2x - 1 + 2*e^(-2x)
P = lambda x: 2.0
Q = lambda x: 4.0 * x

# --- Part 2: Euler's Method Convergence ---

def euler_method(f, x0, y0, x_end, h):
    """Euler's method for dy/dx = f(x, y)."""
    # TODO: Implement the stepping loop
    pass

# Rewrite y' + 2y = 4x as y' = 4x - 2y
f_ode = lambda x, y: 4*x - 2*y
exact = lambda x: 2*x - 1 + 2*np.exp(-2*x)

# Tasks:
# 1. Solve with Euler's method using h = 0.5, 0.1, 0.05, 0.01
# 2. Plot all Euler solutions and the exact solution on [0, 3]
# 3. Compute error at x = 3 for each step size
# 4. Plot error vs step size on a log-log plot
# 5. Verify the slope is ~1 (Euler is first-order: error = O(h))
# 6. Print: "Euler's method IS gradient descent. Both step along
#    a local linear approximation. Shrinking h (or eta) improves
#    accuracy at the cost of more steps."

step_sizes = [0.5, 0.1, 0.05, 0.01]
# ... your convergence analysis here
```

**Tasks:**
1. Implement the integrating factor solver and verify on the test problem
2. Implement Euler's method and compare against the exact solution
3. Produce a log-log convergence plot demonstrating first-order accuracy
4. Bonus: implement the improved Euler method (Heun's method) and show it is second-order

## ML and Alignment Connection

The central insight of this lesson is that Euler's method IS gradient descent. This is not a metaphor. Euler's method approximates the solution of dy/dx = f(x,y) by stepping in the direction f tells you, with step size h. Gradient descent approximates the solution of dW/dt = -nabla L(W) by stepping in the direction the negative gradient tells you, with step size eta. They are the same algorithm applied to different ODEs. Everything you learn about Euler's method --- its first-order accuracy, its stability constraints, how smaller steps improve accuracy but cost more computation --- transfers directly to understanding gradient descent behavior.

The integrating factor method also has a conceptual parallel. When you multiply a messy equation by the right factor to make it tractable, you are performing a change of coordinates that simplifies the problem. This is what preconditioning does in optimization: Adam, natural gradient, and other adaptive methods multiply the gradient by a matrix that makes the effective loss landscape more uniform, just as the integrating factor transforms a non-exact equation into an exact one.
