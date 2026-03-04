# Lesson 80: Optimization Algorithms -- SGD through Adam

[← Matrix Calculus](lesson-79-matrix-calculus.md) | [Back to TOC](../README.md) | [Next: Loss Landscapes →](lesson-81-loss-landscapes.md)

---

Gradient descent in its vanilla form is almost never used in practice. The history of deep learning optimization is a sequence of fixes for vanilla GD's pathologies: SGD adds stochastic noise that helps escape saddle points, momentum accumulates velocity to power through narrow valleys, and adaptive methods like Adam give each parameter its own learning rate. Understanding this progression is not just engineering trivia -- each modification changes what solutions training finds, and therefore what behaviors the trained model exhibits.

The learning rate schedule adds another layer of control. Warmup prevents the early gradients (computed on a randomly initialized network) from sending parameters to bad regions. Cosine annealing slowly reduces the learning rate, encouraging convergence to flatter minima that tend to generalize better. These are not arbitrary heuristics -- each has a mathematical justification rooted in the optimization theory and dynamical systems ideas from earlier lessons.

Convexity is the dividing line between easy and hard optimization. For convex losses, every local minimum is the global minimum, and gradient descent provably converges. Neural networks are emphatically non-convex, which means none of the convergence guarantees apply directly. Yet somehow SGD with Adam works extraordinarily well in practice. The gap between theory and practice here is one of the most important open questions in deep learning.

## Core Learning

- Vanilla gradient descent: follow the negative gradient with fixed step size
- Stochastic gradient descent (SGD): use mini-batch gradient estimates instead of full-batch
- Mini-batch tradeoffs: smaller batches = more noise = better exploration but noisier gradients
- Momentum: accumulate a velocity vector; damp oscillations across narrow valleys (damped ball analogy)
- Nesterov momentum: compute gradient at the look-ahead position for better correction
- AdaGrad: per-parameter learning rates that shrink for frequently-updated parameters
- RMSProp: fix AdaGrad's ever-shrinking rates with exponential moving average of squared gradients
- Adam: combines momentum (first moment) with RMSProp (second moment) plus bias correction
- AdamW: decouples weight decay from the adaptive learning rate (the correct way to regularize with Adam)
- Learning rate schedules: warmup, step decay, cosine annealing, and their effects on training dynamics
- Convexity: what it guarantees and why neural networks violate it

## Watch -- Primary

1. **Stanford CS231n -- Optimization lecture**
   - *Covers SGD, momentum, Adam with clear visualizations of optimizer trajectories on 2D surfaces.*
2. **Deeplearning.AI -- Optimization algorithms (Course 2, Week 2)**
   - *Andrew Ng's walkthrough of momentum, RMSProp, and Adam with intuitive explanations.*

## Watch -- Secondary

3. **Kilcher/Yannic -- "Decoupled Weight Decay Regularization" (AdamW paper)**
   - *Why vanilla Adam's weight decay is broken and how AdamW fixes it. Short and important.*
4. **The AI Epiphany -- "Adam optimizer explained"**
   - *Step-by-step derivation with bias correction.*

## Read

- **Ruder -- "An overview of gradient descent optimization algorithms"**
  - https://ruder.io/optimizing-gradient-descent/
  - *The definitive survey. Covers every major optimizer with equations and comparisons.*
- **Kingma & Ba -- "Adam: A Method for Stochastic Optimization" (2015)**
  - *The original Adam paper. Short and readable. Focus on Sections 1-3.*

## Key Equations

**Vanilla SGD:**

theta <- theta - eta * grad_L

**Momentum:**

v <- beta * v + grad_L
theta <- theta - eta * v

**Adam (full update):**

m <- beta_1 * m + (1 - beta_1) * grad_L          (first moment estimate)
v <- beta_2 * v + (1 - beta_2) * (grad_L)^2       (second moment estimate)
m_hat = m / (1 - beta_1^t)                         (bias correction)
v_hat = v / (1 - beta_2^t)                         (bias correction)
theta <- theta - eta * m_hat / (sqrt(v_hat) + eps)

**Cosine annealing:**

eta_t = eta_min + 0.5 * (eta_max - eta_min) * (1 + cos(pi * t / T))

**Convexity condition:**

f(lambda*x + (1-lambda)*y) <= lambda*f(x) + (1-lambda)*f(y) for all lambda in [0,1]

## Do

1. **Implement SGD, momentum, and Adam from scratch** in pure NumPy. Each optimizer should be a class with an `update(params, grads)` method. No frameworks allowed.
2. **Visualize optimizer trajectories on a 2D surface:** Use the Rosenbrock function f(x,y) = (1-x)^2 + 100(y-x^2)^2. Plot the path each optimizer takes from the same starting point. Observe how momentum overshoots and Adam adapts.
3. **Implement cosine annealing** and compare convergence curves (loss vs step) against constant learning rate for a small network trained on MNIST. Plot both on the same axes.
4. **Learning rate sensitivity experiment:** Train the same network with learning rates spanning 1e-5 to 1.0 (log-spaced). Plot final loss vs learning rate for SGD and Adam. Show that Adam is more robust to learning rate choice.
5. **AdamW vs Adam+L2:** Train a small network with both. Show that Adam+L2 regularization does not actually produce the same result as AdamW, confirming the decoupling insight.

## ML & Alignment Connection

The choice of optimizer has direct alignment implications. Adam's adaptive learning rates mean different parameters learn at different speeds -- safety-relevant features might be learned faster or slower than capabilities, depending on gradient magnitudes. Learning rate schedules affect training dynamics: warmup prevents early memorization of spurious patterns, while cosine annealing helps find flatter (more generalizable) minima that may also be more robust to distribution shift. The batch size controls the noise level of SGD, which determines whether training escapes sharp minima (potentially memorized or overfit solutions) in favor of flat ones (potentially more general and aligned). For RLHF specifically, the optimizer choice affects how quickly the model moves away from the pretrained distribution -- too aggressive optimization can cause reward hacking, where the model exploits the reward model rather than learning genuinely helpful behavior. Understanding optimizers at this level is essential for designing stable, controllable training procedures.
