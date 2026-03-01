# Lesson 22: Introduction to ODEs — Rates of Change as Vector Fields

[← Taylor Expansions](lesson-21-taylor-expansions.md) | [Back to TOC](../README.md) | [Next: Linear Systems →](lesson-23-linear-systems.md)

---

> **Why this lesson exists:** A differential equation is nothing more than a rule that says "given where you are, here's how fast and which direction you're moving." That's *exactly* what gradient descent does — given the current weights, the gradient tells you how to change them. Before you can understand training dynamics, neural ODEs, or stability analysis of AI systems, you need the geometric vocabulary of ODEs: vector fields, solution curves, and the idea that equations describe *flow* through a space.

## 🎯 Core Concepts

### What Is an ODE?

- **An ordinary differential equation** describes how something changes: dx/dt = f(x, t). The function f gives you the "velocity" — which direction x moves and how fast, given current position x and time t.
- **The geometric picture is everything:** think of f as a **vector field** — at every point in space, there's an arrow telling you which way to flow and how fast. A solution to the ODE is a curve that follows the arrows. You don't need to find a formula — you need to *see* the flow.
- **Why "ordinary"?** Because there's only one independent variable (time). Partial differential equations (PDEs) have multiple independent variables — we won't need those.
- **Order:** dx/dt = f(x) is *first-order* (only first derivatives). d²x/dt² = f(x, dx/dt) is *second-order*. Most of what we need is first-order, with one key exception (momentum in gradient descent is second-order).

### From Discrete Updates to Continuous Flow

- **You already know ODEs in disguise.** Gradient descent: W_{t+1} = W_t - η∇L(W_t). This is a discrete update rule. If you make the step size η infinitesimally small, this becomes the ODE: dW/dt = -∇L(W). The discrete update is an *approximation* to continuous flow.
- **Euler's method** is the bridge: to approximate the solution of dx/dt = f(x), take x_{n+1} = x_n + h·f(x_n) where h is the step size. This IS gradient descent with h = η and f = -∇L. Every time you run gradient descent, you're running Euler's method on an ODE.
- **The step size matters:** too large and Euler's method overshoots and oscillates (learning rate too high → training diverges). Too small and it converges painfully slowly. This is the same tradeoff you'll encounter in optimizer tuning.

### Solution Curves and Existence

- **A solution curve** (or trajectory) is a path through space that follows the vector field. Given a starting point x(0) = x₀, there's (usually) exactly one trajectory through that point.
- **Existence and uniqueness theorem:** if f(x) is "nice enough" (Lipschitz continuous), then for any initial condition there exists a unique solution. This matters for ML: it means that given an initialization, there's one deterministic training trajectory (in the continuous limit).
- **You never need to solve analytically.** For almost all real ODEs (including gradient flow on neural networks), there's no closed-form solution. What matters is understanding the *qualitative behavior* — where does the flow go? Where does it converge? What structures does it create?

### Vector Fields in 1D and 2D

- **1D: dx/dt = f(x).** The vector field is just arrows on a number line. Where f(x) > 0, x moves right. Where f(x) < 0, x moves left. Where f(x) = 0, x doesn't move — these are **fixed points** (equilibria).
- **Stability in 1D is visual:** if arrows point *toward* a fixed point from both sides, it's stable (a ball rolling into a valley). If arrows point away, it's unstable (a ball balanced on a hilltop). If f'(x*) < 0 at a fixed point x*, it's stable. If f'(x*) > 0, it's unstable.
- **2D: dx/dt = f(x,y), dy/dt = g(x,y).** Now the vector field lives in the plane — at every (x,y) there's a 2D arrow. Solution curves are paths through the plane. This is where things get rich: spirals, saddles, cycles.
- **For ML:** the 2D case is directly analogous to gradient descent on a loss function L(w₁, w₂) with two parameters. The vector field is -∇L, and the solution curves are training trajectories.

### Fixed Points and Their Character

- **Fixed point:** a point where f(x*) = 0 — the velocity is zero, so the system stays put. For gradient flow, fixed points are where ∇L = 0: the critical points of the loss.
- **In 1D:** fixed points are either stable (attracting) or unstable (repelling). That's it.
- **In 2D and higher:** fixed points come in a richer variety — stable nodes, unstable nodes, saddle points, spirals, centers. The type is determined by the eigenvalues of the Jacobian matrix at the fixed point. (You already know eigenvalues — this is where they enter the story of dynamics.)
- **Saddle points matter enormously for ML:** in high-dimensional loss landscapes, almost all critical points are saddle points, not local minima. The dynamics near saddles determine how training escapes to find good solutions.

## 📺 Watch — Primary

1. **3Blue1Brown — "Differential equations, studying the unsolvable"**
   - https://www.youtube.com/watch?v=p_di4Zn4wz4
   - *The "tourist's guide" overview. Emphasizes that most ODEs can't be solved analytically — the geometric/qualitative approach is what matters. Watch this first for the big picture.*
2. **3Blue1Brown — "But what is a partial differential equation?"** (first 10 minutes only)
   - https://www.youtube.com/watch?v=ly4S0oi3Yz8
   - *The opening section recaps ODEs beautifully before moving to PDEs. Stop when PDEs start — we don't need them.*

## 📺 Watch — Secondary

3. **Steve Brunton — "Overview of Dynamical Systems" (Dynamical Systems playlist, videos 1–2)**
   - https://www.youtube.com/c/Eigensteve
   - *Brunton is an applied mathematician who connects dynamical systems to data science. Excellent for seeing why this matters beyond pure math.*
   - Useful if you want a slower, example-heavy walkthrough of the basic mechanics
4. **Dr. Trefor Bazett — Multivariable Calculus playlist (ODE-relevant sections)**
   - https://www.youtube.com/playlist?list=PLHXZ9OQGMqxc_CvEy7xBKRQr6I214QJcd
   - *Clear, visual university lectures. Use for extra practice on differential equations fundamentals.*

## 📖 Read — Primary

- **"Nonlinear Dynamics and Chaos" by Steven Strogatz** — Chapter 1 (Overview) and Chapter 2 (Flows on the Line)
  - *Strogatz is the gold standard for geometric intuition about dynamical systems. Chapter 2 covers 1D flows — simple but foundational. His writing is beautiful and emphasizes pictures over formulas.*

## 📖 Read — Secondary

- **Paul's Online Math Notes — "Basic Concepts" section of Differential Equations**
  - https://tutorial.math.lamar.edu/Classes/DE/Intro.aspx
  - *Good for drill problems if you want more practice with the mechanics*

## 🔨 Do

- **Vector field plotter:** write a Python script using matplotlib's `quiver` to plot the vector field for dx/dt = sin(x) on the number line. Mark the fixed points. Verify that stable ones have f'(x*) < 0.
- **2D vector field:** plot the vector field for dx/dt = -x, dy/dt = -2y. This is gradient flow on L = x²/2 + y². Overlay several solution curves from different starting points. See how they all converge to the origin but faster in the y-direction (because the eigenvalue is more negative).
- **Euler's method by hand:** for dx/dt = -x with x(0) = 1, compute x(0.5) using step sizes h = 0.5, 0.25, 0.1. Compare with the exact solution x(t) = e^{-t}. See the accuracy improve as h shrinks. Relate to learning rate.
- **Key exercise:** for the 1D ODE dx/dt = x(1-x)(x-2), find all fixed points. Classify each as stable or unstable by checking the sign of f'(x*). Sketch the flow on the number line. This is a "bifurcation" preview — the dynamics partition the line into basins of attraction.

## 🔗 ML & Alignment Connection

- **Gradient descent IS Euler's method** on the gradient flow ODE. The learning rate IS the step size. This isn't an analogy — it's literally the same algorithm. Everything you learn about Euler's method stability directly predicts when training will diverge.
- **Vector fields on loss landscapes:** when you see a contour plot of a 2-parameter loss with gradient arrows, you're looking at the vector field of gradient flow. The solution curves are training trajectories.
- **Fixed points = trained models:** every local minimum of the loss is a stable fixed point of gradient flow. Training dynamics select which fixed point you reach.

- **Initial conditions determine outcomes:** just as different starting points lead to different fixed points, different random initializations of a neural network lead to different trained models. Some may be "aligned," others not. Understanding basin structure is understanding the probability that training produces aligned behavior.
- **The qualitative approach:** we usually can't solve training dynamics analytically. But we can classify the types of fixed points, understand basin structure, and predict qualitative behavior — exactly the approach Strogatz teaches. This is the methodology for analyzing training at scale.