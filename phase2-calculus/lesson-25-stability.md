# Lesson 25: Stability, Lyapunov Functions, and Phase Transitions

[← Gradient Flow](lesson-24-gradient-flow.md) | [Back to TOC](../README.md) | [Next: Neural ODEs →](lesson-26-neural-odes.md)

---

> **Why this lesson exists:** Training doesn't always progress smoothly. Models sometimes hit plateaus, then suddenly learn new capabilities. These are **phase transitions** — qualitative changes in the dynamics of training. Understanding them requires stability theory (when is a solution robust to perturbation?), Lyapunov functions (how do you prove something stays safe?), and bifurcation theory (how do systems change character as parameters vary?). These tools are directly relevant to predicting sudden capability gains — one of the most dangerous phenomena from an alignment perspective.

## 🎯 Core Concepts

### Lyapunov Stability — Formal Guarantees Without Solving

- **The problem:** you have a dynamical system and a fixed point. You want to prove the fixed point is stable — that nearby trajectories stay nearby (or converge). But you can't solve the ODE. What do you do?
- **Lyapunov's insight:** find a function V(x) that (1) is positive away from the fixed point, (2) equals zero at the fixed point, and (3) **decreases along trajectories** (dV/dt ≤ 0). If such a V exists, the fixed point is stable. If dV/dt < 0 (strictly), it's asymptotically stable — trajectories converge.
- **You've already seen this:** the loss function L is a Lyapunov function for gradient flow, since dL/dt = -‖∇L‖² ≤ 0. This is the formal proof that gradient flow converges.
- **The power of Lyapunov functions:** you don't need to solve anything. You just need to find the right V. This is how control theorists prove stability of engineered systems — and potentially how we could prove safety properties of AI systems.

### Lyapunov Functions for AI Safety

- **The alignment dream:** find a function V(behavior) that (1) measures "distance from aligned behavior," (2) is zero when the system is aligned, and (3) provably decreases (or at least doesn't increase) as the system operates. If you could find such a V, you'd have a mathematical guarantee of alignment stability.
- **Why this is hard:** for gradient flow, L itself is a natural Lyapunov function — it decreases by construction. For an AI system operating in the world, there's no such natural candidate. You'd need to define "aligned behavior" formally, construct a V, and prove dV/dt ≤ 0 for all possible inputs. Each step is an open problem.
- **But partial guarantees are possible:** even without a complete Lyapunov function, showing that certain quantities remain bounded during training (e.g., weight norms, activation magnitudes, behavioral measures) gives partial safety guarantees. This is the spirit of current work on training safety.

### Bifurcations — When Systems Change Character

- **A bifurcation** occurs when the qualitative behavior of a system changes as a parameter varies. At a critical parameter value, fixed points can appear, disappear, change stability, or split.
- **Saddle-node bifurcation:** as a parameter crosses a threshold, two fixed points (one stable, one unstable) collide and annihilate — or appear from nothing. Before the threshold: two equilibria. After: none (or vice versa).
- **Pitchfork bifurcation:** a single fixed point becomes unstable and two new stable fixed points appear. This is symmetry breaking — the system "chooses" one of two equivalent states.
- **For ML:** when a hyperparameter (learning rate, regularization strength, model size) crosses a threshold, the loss landscape can change qualitatively — minima can appear or disappear. This is a structural change in what the model can learn.

### Phase Transitions in Training

- **Phase transitions in physics** occur when a system's macroscopic behavior changes discontinuously as a control parameter varies (temperature → ice/water, pressure → liquid/gas). The system reorganizes on a large scale.
- **Phase transitions in training** are analogous: as training progresses (time as the parameter), the model's behavior changes *qualitatively*. The loss drops suddenly. New capabilities emerge. The internal representations reorganize.
- **Grokking** is the most dramatic example: a model memorizes the training data quickly, then — after much more training — suddenly generalizes. The training loss was already low, but validation accuracy suddenly jumps. In dynamical systems terms: the training trajectory was near a saddle point (memorization regime) and eventually escaped along an unstable direction into a basin corresponding to generalization.
- **Emergent capabilities** in large language models — where a capability appears to be absent below a certain model size and suddenly present above it — may be related to phase transitions in the loss landscape as the model dimension parameter changes.

### SLT's Phase Transitions

- **Singular Learning Theory** (which you'll study in depth in Lesson 48) characterizes phase transitions as changes in the **effective dimensionality** of the model, measured by the RLCT (Real Log Canonical Threshold) λ.
- **During training:** the trajectory passes through different regions of weight space with different singularity structures. At boundary crossings, the RLCT jumps, and the model's effective complexity changes. These jumps correspond to phase transitions — the acquisition of new computational capabilities.
- **The LLC (Local Learning Coefficient)** tracks these transitions in real time during training. Monitoring it could predict when a model is about to acquire a new capability.

### Attractors Beyond Fixed Points

- **Not all long-term behavior is convergence to a fixed point.** Dynamical systems can exhibit:
  - **Limit cycles:** periodic oscillations (training loss oscillates at a fixed amplitude)
  - **Quasiperiodic orbits:** motion on a torus (multiple incommensurate frequencies)
  - **Strange attractors / chaos:** deterministic but unpredictable long-term behavior
- **For gradient flow specifically:** Strogatz proves that gradient systems (where the vector field is a gradient) cannot have limit cycles. They always converge to fixed points. But **SGD is not gradient flow** — the stochasticity breaks this guarantee. SGD can oscillate, and the noise structure matters.
- **For alignment:** if training dynamics can be chaotic (sensitive to initial conditions), then small changes to training setup could lead to qualitatively different outcomes. Understanding when training dynamics are "robust" versus "chaotic" is directly relevant to alignment reliability.

## 📺 Watch — Primary

1. **Steve Brunton — "Stability and Lyapunov Functions" and "Bifurcations" (Dynamical Systems playlist, videos 6–10)**
   - https://www.youtube.com/c/Eigensteve
   - *Brunton covers Lyapunov theory with engineering applications, then all the major bifurcation types with beautiful visualizations.*
2. **Veritasium — "The Logistic Map and the Route to Chaos"**
   - https://www.youtube.com/watch?v=ovJcsL7vyrk
   - *Not directly about ML, but the best visual explanation of how bifurcations lead to chaos. The period-doubling cascade is mesmerizing and builds deep intuition for what "qualitative change" means in dynamical systems.*

## 📺 Watch — Secondary

3. **MIT OCW — Strogatz "Nonlinear Dynamics and Chaos" (Lectures 7–10)**
   - Bifurcations, limit cycles, and the beginning of chaos. Strogatz is the master.
4. **Welch Labs — "Grokking and Double Descent"**
   - *Connects phase transition ideas to the specific ML phenomena you'll encounter.*
5. **Neel Nanda — Grokking paper walkthrough**
   - https://www.youtube.com/@neelnanda2469
   - *Neel's walkthrough of the grokking phenomenon with mechanistic interpretability analysis. Connects stability/phase transitions to what neural networks actually learn.*

## 📖 Read — Primary

- **"Nonlinear Dynamics and Chaos" by Steven Strogatz** — Chapter 3 (Bifurcations), Chapter 8.1–8.2 (Intro to Lyapunov functions)
  - *Chapter 3 covers all the major 1D bifurcation types with beautiful examples. Lyapunov theory in Chapter 8 ties it to stability proofs.*
- **"Grokking: Generalization Beyond Overfitting" by Power et al.**
  - https://arxiv.org/abs/2201.02177
  - *The paper that identified grokking as a phenomenon. Read with phase transition eyes.*

## 📖 Read — Secondary

- **"A Dynamical Systems Perspective on Optimization" (various survey papers)**
  - Search for recent surveys connecting bifurcation theory to training dynamics
- **"Deep Double Descent" by Nakkiran et al.**
  - https://arxiv.org/abs/1912.02292
  - *Double descent is another phase transition phenomenon in training — performance gets worse then better as model size increases.*

## 🔨 Do

- **Bifurcation diagram:** for dx/dt = r + x², vary r from -2 to 2. For each r, find the fixed points and their stability. Plot fixed point position vs r — this is a bifurcation diagram showing the saddle-node bifurcation at r = 0.
- **Pitchfork bifurcation:** for dx/dt = rx - x³, do the same. See the single fixed point split into three at r = 0.
- **Lyapunov function verification:** for the system dx/dt = -x³, dy/dt = -y, verify that V(x,y) = x⁴/4 + y²/2 is a Lyapunov function by computing dV/dt along trajectories and confirming it's ≤ 0.
- **Grokking dynamics visualization:** if you have access to a small model trained on modular arithmetic (or create one — see Power et al.), plot training loss and validation accuracy over time. Identify the phase transition. If you track weight norms or gradient norms during training, see if they signal the transition.
- **Key exercise:** design a toy 1D dynamical system dx/dt = f(x; r) that has a bifurcation at r = r*. Plot the bifurcation diagram. Then interpret: if x represents "model capability" and r represents "training time" (or "model size"), what does the bifurcation mean for capability emergence? This is the conceptual framework for understanding sudden capability gains.

## 🔗 ML & Alignment Connection

- **Grokking, double descent, and emergent capabilities** are all phase transitions. The dynamical systems framework gives you the mathematical language to describe them, predict them, and (potentially) control them.
- **Learning rate as bifurcation parameter:** as you increase the learning rate, stable minima can become unstable (the loss landscape's "effective topology" changes). This is a bifurcation with η as the parameter.
- **Model size as bifurcation parameter:** as model width or depth increases, new critical points appear in the loss landscape. Certain solutions become reachable that were unreachable before. This is the lens for understanding scaling laws.

- **Sudden capability gain is an alignment threat:** if a model acquires a dangerous capability through a phase transition, we may not have warning. Predicting phase transitions (via RLCT monitoring, Lyapunov analysis, or bifurcation detection) is directly safety-relevant.
- **Lyapunov safety certificates:** if we could construct a Lyapunov function for "aligned behavior stays aligned," we'd have a formal safety guarantee. This is the control theory approach to alignment.
- **Bifurcation sensitivity:** near a bifurcation point, the system is maximally sensitive to perturbation. If training passes near a bifurcation, small changes to data or hyperparameters could cause large behavioral shifts. Identifying and avoiding these sensitive regions is a practical safety measure.