# Lesson 21e: Differential Equations and Dynamical Systems — Training as Flow

[← Topology](lesson-21d-topology.md) | [Back to TOC](../README.md) | [Next: Formal Logic →](lesson-21f-formal-logic.md)

---

> **Why this lesson exists:** Gradient descent is a *dynamical system* — the weights evolve over time according to a rule (the gradient). In the continuous-time limit (very small learning rate), gradient descent becomes a differential equation: dW/dt = -∇L(W). This isn't just a cute analogy — it's the mathematical framework used to analyze training dynamics, convergence, stability, and phase transitions. Neural ODEs treat the network itself as a differential equation. SLT's phase transitions are dynamical phenomena. Understanding ODEs gives you the language for "how does training actually work?"

## 🎯 Core Concepts

### Ordinary Differential Equations (ODEs) — The Basics

- **An ODE** describes how something changes over time: dx/dt = f(x, t). The function f tells you the "velocity" — which direction x moves and how fast, given its current position x and time t.
- **The geometric picture:** think of f as a *vector field* — at every point in space, an arrow tells you which direction to flow. The solution to the ODE is a curve that follows the arrows. This is exactly how you should visualize gradient descent: the loss landscape defines a vector field (the negative gradient), and training follows the flow.
- **Linear ODEs:** dx/dt = Ax where A is a matrix. The solution is x(t) = e^{At}x(0), the *matrix exponential*. This connects directly to eigenvalues: if A has eigenvalue λ, the solution along that eigenvector direction is e^{λt}. If λ < 0 → decay (stable). If λ > 0 → growth (unstable). If λ is complex → oscillation. **Eigenvalue analysis of A tells you everything about the system's behavior.**
- **Phase portrait:** a visualization of the vector field and representative solution curves in 2D. You've seen these implicitly — gradient descent paths on contour plots ARE phase portraits of the ODE dW/dt = -∇L(W).

### Gradient Flow — Training in Continuous Time

- **Gradient descent** with learning rate η updates weights: W_{t+1} = W_t - η∇L(W_t). As η → 0, this becomes the ODE: dW/dt = -∇L(W). This is called **gradient flow**.
- **Why continuous time helps:** ODEs have a rich mathematical theory. You can prove convergence, analyze stability, classify critical points, and understand long-time behavior using tools that don't exist for discrete updates.
- **Critical points** of gradient flow are where ∇L = 0: the gradient is zero, so the flow stops. These are the minima, maxima, and saddle points of the loss landscape.
- **Stability of critical points:** the eigenvalues of the Hessian H = ∇²L at a critical point determine stability:
  - All eigenvalues negative → stable (local maximum of -L, local minimum of L) → gradient flow converges here
  - All eigenvalues positive → unstable (gradient flow repelled) — this is a minimum of -L but a maximum of L. Wait, we're doing gradient DESCENT, so negative eigenvalues of -∇L → positive eigenvalues of the Hessian → stable minimum. (Be careful with signs!)
  - Mixed signs → saddle point — flow approaches along some directions, repelled along others
- **This IS the Hessian analysis from Lesson 10 and 16:** the eigenvalues of the Hessian (positive definiteness, condition number) determine loss landscape curvature. Now you see this through the lens of dynamical stability.

### Fixed Points, Attractors, and Basins

- **Fixed point:** a point where f(x*) = 0 — the system stays put. For gradient flow, fixed points = critical points of the loss.
- **Basin of attraction:** the set of all initial conditions that eventually flow to a given fixed point. Different random initializations land in different basins → different trained models.
- **Attractor landscapes:** the loss landscape partitions weight space into basins of attraction. The question "which solution does training find?" is really "which basin did initialization land in?"
- **Alignment implication:** if there are basins corresponding to "aligned" behavior and basins corresponding to "misaligned" behavior, the initialization strategy determines which you reach. Understanding basin structure is understanding the probability of alignment.

### The Conditioning Problem — Why Training Is Hard

- **Condition number** κ = λ_max / λ_min of the Hessian (from Lesson 10). For gradient flow: the condition number determines how "elongated" the basins are.
- **In a badly conditioned loss landscape** (κ >> 1): the gradient points mostly in the "steep" direction, barely moving in the "shallow" direction. The flow zigzags — fast in one direction, painfully slow in another. This is why vanilla gradient descent on badly conditioned problems is slow.
- **Momentum, Adam, and preconditioning** are all ways to fix the conditioning problem. Adam effectively rescales the gradient by an approximation of the inverse Hessian, making all directions equally "easy." In dynamical systems terms: Adam transforms the vector field to improve the condition number.

### Phase Transitions in Training

- **Phase transitions** occur when the qualitative behavior of a dynamical system changes abruptly. Water freezing at 0°C is a phase transition — the dynamics (liquid flow vs. solid vibration) change discontinuously.
- **In neural network training:** as training progresses, the loss sometimes drops suddenly (not gradually). The network abruptly "learns" a new capability. These are phase transitions — the training dynamics cross a critical boundary where the effective model changes qualitatively.
- **Grokking** (sudden generalization long after memorization) is a dramatic phase transition. The network memorizes first (one dynamical regime), then suddenly finds the generalizing solution (different regime). The transition is sharp.
- **SLT's contribution:** Singular Learning Theory characterizes these transitions as changes in the *effective dimensionality* of the model — the RLCT λ jumps when the training trajectory crosses from one type of singularity to another. The dynamics near different singularities are qualitatively different.

### Neural ODEs — The Network IS a Differential Equation

- **Key idea (Chen et al., 2018):** a residual network x_{l+1} = x_l + f(x_l) looks like an Euler step of the ODE dx/dt = f(x). In the limit of infinitely many layers with infinitesimal changes, a ResNet IS an ODE.
- **Neural ODE:** parameterize f with a neural network and use an ODE solver (instead of a fixed number of layers) to transform the input. This is adaptive: the "depth" adjusts to the complexity of the input.
- **Continuous normalizing flows:** use neural ODEs to model complex probability distributions. The change-of-variables formula for ODEs involves the trace of the Jacobian (which connects to the determinant from Lesson 6 via Liouville's theorem).
- **Why this matters:** neural ODEs make the continuous-time perspective literal, not just an approximation. They connect deep learning directly to the rich theory of dynamical systems.

### Stability Theory and Lyapunov Functions

- **Lyapunov function:** a function V(x) that decreases along system trajectories. If you can find one, you can prove stability without solving the ODE explicitly. For gradient descent, the loss function L IS a Lyapunov function (it decreases along gradient flow by construction).
- **Lyapunov stability:** a fixed point is Lyapunov stable if nearby trajectories stay nearby forever. It's *asymptotically* stable if they actually converge to the fixed point.
- **For alignment:** can we design a Lyapunov function for an AI system's behavior? A quantity that's guaranteed to decrease (or stay bounded) as the system operates? This connects to formal safety guarantees and control theory approaches to alignment.

## 📺 Watch — Primary

1. **3Blue1Brown — "Differential Equations" (if available from Essence of Calculus / standalone series)**
   - Visual, geometric treatment of ODEs as vector fields
2. **Steve Brunton — "Dynamical Systems" playlist (first 5-6 videos)**
   - https://www.youtube.com/c/Eigensteve
   - *Brunton covers phase portraits, stability, eigenvalue analysis for dynamical systems with data science applications. Excellent.*
3. **Veritasium — "The Surprising Math Behind Neural Networks"** (neural ODEs segment, if available)

## 📺 Watch — Secondary

4. **MIT OCW — Strogatz, "Nonlinear Dynamics and Chaos" (Lectures 1–5)**
   - Strogatz is the gold standard for dynamical systems intuition
5. **Yannic Kilcher — "Neural ODE" paper review**
   - Search YouTube — connects the math to the ML implementation

## 📖 Read — Primary

- **"Nonlinear Dynamics and Chaos" by Steven Strogatz** — Chapters 1–3 (1D flows, phase portraits, bifurcations)
  - *The best dynamical systems textbook for building intuition. Strogatz writes beautifully and emphasizes geometric thinking. Chapters 1-3 are the core vocabulary you need.*
- **"Neural Ordinary Differential Equations" by Chen et al. (2018)**
  - https://arxiv.org/abs/1806.07366
  - *The paper that connected deep learning to ODEs. Read after understanding basic ODE concepts.*

## 📖 Read — Secondary

- **Steve Brunton & Nathan Kutz — "Data-Driven Science and Engineering"** — Chapter 7 (dynamical systems)
  - https://www.databookuw.com/
  - Applied treatment with data science focus
- **"A Dynamical Systems Perspective on Optimization" (various survey papers)**
  - The gradient flow perspective on training — connects everything above to neural network training directly

## 📖 Read — Going Deep

- **"Singular Learning Theory" by Watanabe** — dynamics near singularities
  - How the RLCT changes along training trajectories
- **"Implicit Regularization in Deep Learning" literature**
  - Gradient descent doesn't just find any minimum — the training dynamics implicitly prefer certain solutions. This implicit bias IS a dynamical systems phenomenon.

## 🔨 Do

- **Phase portrait generator:** implement the Euler method for 2D ODEs. Plot the vector field (arrows) and several solution curves from different starting points for: (a) a stable spiral dx/dt = -x + y, dy/dt = -x - y, (b) a saddle dx/dt = x, dy/dt = -y, (c) a center dx/dt = y, dy/dt = -x. See how eigenvalues of the coefficient matrix determine the behavior.
- **Gradient flow visualization:** take a 2D loss function L(w₁, w₂) = w₁² + 10w₂² (badly conditioned, κ = 10). Plot gradient descent trajectories from various starting points. Then plot gradient flow (continuous) using an ODE solver. Compare. Then try L(w₁, w₂) = w₁² + w₂² (well-conditioned, κ = 1). See the zigzag disappear.
- **Eigenvalue stability analysis:** for a linear ODE dx/dt = Ax with A = [[-1, 2], [-2, -1]], compute eigenvalues. Predict the behavior (stable spiral? unstable? saddle?). Then simulate and verify.
- **Grokking dynamics:** if you've already trained a small model that grokks (from Lesson 33 exercises), plot the training loss AND validation loss curves on the same graph. Identify the phase transition. If you also track weight norms or effective complexity measures during training, see if they show the transition.
- **Key exercise:** explain why gradient descent with momentum can be written as a second-order ODE: d²W/dt² + γ dW/dt = -∇L(W), where γ is the friction coefficient. What does this look like as a physical system? (A ball rolling in a loss landscape with friction.) Why does momentum help with bad conditioning?

## 🔗 ML Connection

- **Gradient descent analysis:** everything about learning rates, convergence, and optimizer behavior is cleaner in the continuous-time ODE framework. The theory of "which solutions SGD converges to" uses stochastic differential equations (SDEs), the noisy version of ODEs.
- **Neural ODEs** are a current research direction where the network's depth is continuous and adaptive. This connects deep learning to control theory and differential equations directly.
- **Implicit regularization:** gradient descent doesn't just find any minimum — it finds specific ones determined by the training dynamics. For linear models, gradient descent from small initialization converges to the minimum-norm solution. For deep networks, the implicit bias is more complex but equally important.
- **Learning rate warmup, schedules, and cyclical learning rates** are all interventions on the dynamical system of training. Understanding WHY they work requires dynamical systems thinking.

## 🧠 Alignment Connection

- **Training dynamics determine alignment:** whether a model learns "aligned" or "misaligned" behavior depends on the dynamical trajectory through weight space. The trajectory is determined by: initialization, learning rate, batch size, data ordering, and the landscape itself. Understanding training dynamics helps predict and control what behavior emerges.
- **Phase transitions and capabilities:** sudden capability gain (a dangerous scenario for alignment) corresponds to dynamical phase transitions. If we can predict when these transitions will occur (from the dynamical systems analysis), we can prepare for them.
- **Control theory for AI safety:** Lyapunov functions and stability theory from dynamical systems are directly applicable to designing AI systems with guaranteed safety properties — ensuring certain quantities stay bounded, or certain behaviors remain stable.
- **SLT dynamics:** the RLCT changes as training crosses singularity boundaries. These changes are the mechanistic explanation for why models suddenly acquire new capabilities — the most concerning phenomenon from an alignment perspective.
