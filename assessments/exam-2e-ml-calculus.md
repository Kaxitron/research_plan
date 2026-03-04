# Exam 2E: ML-Applied Calculus

**The Path to AI Alignment -- Lessons 34-36 Assessment**

---

| | |
|---|---|
| **Time Allowed** | 60 minutes |
| **Total Points** | 80 |
| **Materials** | Pencil, paper, calculator (no CAS). No code. |
| **Format** | 8 questions, 10 pts each. Matrix calculus, optimization algorithms, loss landscape theory. |

> **Advice:** This is a shorter, focused exam covering the ML-specific calculus that bridges Phases 1-2 into deep learning. Show all work. When a question says "explain," 2-3 precise sentences are expected -- not a paragraph.

> *"The loss landscape is not a bowl. It is a vast, high-dimensional saddle -- and the miracle of SGD is that it navigates this terrain anyway."*

---

## Question 1 (10 pts) -- Matrix Calculus Identities

**(a)** Let f(x) = Ax where A is an m x n matrix and x is an n x 1 vector. Compute the Jacobian df/dx. State its dimensions and explain why this is the natural generalization of "the derivative of a linear function is the slope."

**(b)** Let g(x) = x^T A x where A is an n x n matrix and x is n x 1. Derive dg/dx = (A + A^T)x from first principles by expanding g(x + epsilon*e_i) and collecting terms. Under what condition on A does this simplify to dg/dx = 2Ax?

**(c)** In numerator layout, the Jacobian of f: R^n -> R^m has shape m x n (each row is the gradient of one output). In denominator layout, it has shape n x m. PyTorch uses neither consistently -- it computes vector-Jacobian products (VJPs) directly. In one sentence, explain why VJPs are what backpropagation actually needs, regardless of layout convention.

---

## Question 2 (10 pts) -- Computation Graphs and Autodiff

Consider the computation:

```
x = 3, W = 2, b = -1
z = Wx + b
a = max(0, z)        (ReLU)
L = (1/2)(a - 4)^2
```

**(a)** Draw the computation graph with nodes for each intermediate value (z, a, L). Compute the forward pass: find z, a, and L.

**(b)** Compute the backward pass using reverse-mode autodiff. Find dL/da, da/dz, dz/dW, dz/db. Then assemble dL/dW and dL/dB using the chain rule.

**(c)** Now consider forward-mode autodiff. To compute dL/dW via forward mode, you propagate dz/dW forward through each node. Trace this computation. How many forward passes would you need to compute gradients with respect to ALL parameters? How many backward passes does reverse mode need?

**(d)** A neural network has 100 million parameters and 1 scalar loss. Explain in 2 sentences why reverse mode is ~10^8 times more efficient than forward mode for this network.

---

## Question 3 (10 pts) -- The Optimization Zoo

For each optimizer below, write the update rule and answer the follow-up.

**(a)** **Vanilla SGD:** w_{t+1} = ___. A loss landscape has a narrow ravine (eigenvalues of the Hessian: lambda_1 = 100, lambda_2 = 1). Describe qualitatively what happens to the SGD trajectory and why.

**(b)** **SGD with Momentum:** Write the two-line update (velocity v_t and weight w_t). Using the physical analogy of a ball rolling downhill, explain why momentum helps traverse the ravine from part (a).

**(c)** **Adam:** Write the full update rule including the bias-corrected first and second moment estimates (m-hat_t and v-hat_t). Adam adapts the learning rate per-parameter. Which parameters get larger effective learning rates -- those with consistently large gradients or those with sparse/noisy gradients? Why?

**(d)** **AdamW vs. Adam with L2 regularization:** These are NOT the same. Explain the difference in 2-3 sentences. Which does the original BERT paper use, and why does the distinction matter for large models?

---

## Question 4 (10 pts) -- Learning Rate Schedules and Convexity

**(a)** Define convexity for a function f. State the key property that makes convex optimization "easy" (in terms of local vs. global minima). Is the loss function of a neural network convex? Why or why not?

**(b)** A learning rate warmup schedule starts with a very small learning rate and linearly increases it over the first T_warmup steps. Why is this helpful at the beginning of training? *(Hint: think about the quality of gradient estimates when the model is randomly initialized.)*

**(c)** Cosine annealing sets eta_t = eta_min + (1/2)(eta_max - eta_min)(1 + cos(pi * t / T)). Sketch this schedule. Why does the gradual decay near the end of training help compared to a sharp step-down?

**(d)** Some practitioners use cyclical learning rates that repeatedly increase and decrease. Give one argument for why temporarily INCREASING the learning rate mid-training could improve generalization. *(Hint: what kind of minima does a large learning rate escape?)*

---

## Question 5 (10 pts) -- Saddle Points and High-Dimensional Landscapes

**(a)** At a critical point (where nabla L = 0), the Hessian has n eigenvalues. In a random high-dimensional landscape, each eigenvalue is positive or negative with roughly equal probability. What fraction of critical points are true local minima (all eigenvalues positive) when n = 100? Express as a power of 2.

**(b)** The Hessian at a critical point has eigenvalues {5, 3, 1, -0.5, -2}. Classify this critical point. In how many directions is it a minimum? In how many is it a maximum? What is the index of this saddle point?

**(c)** Gradient descent can get "stuck" near saddle points even though they are not minima. Explain why by considering the gradient magnitude near a saddle point. How does SGD noise help escape saddle points?

**(d)** Despite the prevalence of saddle points, modern networks train successfully. State the empirical observation about the relationship between the loss value at a critical point and its index (number of negative Hessian eigenvalues). Why is this good news for optimization?

---

## Question 6 (10 pts) -- Gradient Flow and Stability

The continuous-time limit of gradient descent is the gradient flow ODE:

dW/dt = -nabla L(W)

**(a)** Consider the 1D case L(w) = (1/2)(w - w*)^2. Write the gradient flow ODE. Solve it explicitly (this is a first-order linear ODE). Show that w(t) -> w* as t -> infinity.

**(b)** A Lyapunov function V(W) satisfies V >= 0 and dV/dt <= 0 along trajectories. Show that L(W) itself is a Lyapunov function for gradient flow by computing dL/dt along the flow and showing dL/dt = -||nabla L||^2 <= 0. What does this guarantee?

**(c)** For discrete gradient descent w_{t+1} = w_t - eta * nabla L(w_t) on L(w) = (1/2) * lambda * w^2, derive the condition on eta that ensures |w_{t+1}| < |w_t| (convergence). Show that this gives eta < 2/lambda.

**(d)** A loss function has Hessian eigenvalues ranging from lambda_min = 0.1 to lambda_max = 100. What is the maximum stable learning rate? What is the condition number? Explain in one sentence why a large condition number makes optimization difficult even with a stable learning rate.

---

## Question 7 (10 pts) -- Momentum as Second-Order Dynamics and Neural ODEs

**(a)** Momentum turns gradient descent into a second-order ODE. Write the continuous-time heavy ball equation: m * d^2W/dt^2 + gamma * dW/dt = -nabla L(W). Identify the mass term, the friction/damping term, and the force term. Why does underdamped motion (low gamma) cause oscillation?

**(b)** A ResNet computes h_{t+1} = h_t + f(h_t, theta_t). Explain why this is an Euler discretization of the ODE dh/dt = f(h, t). What is the "step size" of this discretization?

**(c)** Neural ODEs replace the discrete layers with a continuous ODE: dh/dt = f(h, t, theta), solved by a numerical ODE solver. Name one advantage of Neural ODEs over standard ResNets in terms of memory during backpropagation. *(Hint: look up the adjoint method.)*

**(d)** SGD with learning rate eta and batch size B on a loss landscape with Hessian H can be modeled as the stochastic differential equation dW = -nabla L dt + sqrt(eta / B) * Sigma^{1/2} dB_t, where Sigma is the gradient noise covariance. What happens to the noise term as batch size B increases? As learning rate eta decreases? Why does this suggest SGD acts as "implicit regularization"?

---

## Question 8 (10 pts) -- Edge of Stability and Grokking

**(a)** The "edge of stability" phenomenon (Cohen et al., 2021): when training with a fixed learning rate eta, the largest eigenvalue of the Hessian (the sharpness) initially increases, then stabilizes near 2/eta. This contradicts classical convergence theory. In 2-3 sentences, explain what classical theory predicts should happen when sharpness exceeds 2/eta, and what actually happens instead.

**(b)** Grokking (Power et al., 2022): a model trains on a small dataset, achieves perfect training accuracy quickly, but test accuracy only improves MUCH later (sometimes 10x-100x more training steps). Sketch a qualitative plot of training loss, training accuracy, and test accuracy vs. training step for a grokking experiment. Label the key phases.

**(c)** One hypothesis for grokking is that the model first memorizes the training data (finding a "sharp" minimum) and then slowly transitions to a generalizing solution (a "flat" minimum). Connect this to the SDE model of SGD from Question 7(d): why might SGD noise eventually push the model out of the memorizing solution?

**(d)** Both edge of stability and grokking suggest that neural network training is NOT well-described by simple gradient descent on a fixed loss landscape. In 3-4 sentences, articulate why: what changes during training that makes the "ball rolling downhill" metaphor inadequate? Reference at least two specific phenomena from this exam.

---

## Optional Mini-Project (~45 minutes): The Optimizer Showdown

**Compare optimization algorithms on a carefully designed loss landscape.**

1. Implement the following loss function in NumPy: L(w1, w2) = 0.5*(w1^2) + 50*(w2^2) + 10*sin(w1)*sin(w2). This has a global minimum near the origin, a high condition number, and local structure from the sinusoidal terms.

2. Implement from scratch (no ML libraries): vanilla SGD, SGD with momentum (beta=0.9), RMSProp, and Adam. Each should take a gradient function, initial point, and learning rate.

3. For each optimizer, run 500 steps from the initial point (5, 5) with learning rate 0.01. Plot all four trajectories on the same contour plot of L. Also plot L vs. step number for all four.

4. Find the maximum stable learning rate for each optimizer experimentally (binary search). Which optimizer tolerates the largest learning rate? Relate this to the theory from Question 6(c).

5. Add Gaussian noise to the gradients (simulating mini-batch SGD with different batch sizes). How does noise magnitude affect which optimizer "wins"?

**Stretch:** Implement learning rate warmup + cosine annealing for Adam. Show that this combination converges faster than any fixed learning rate on this landscape. Measure the sharpness (largest Hessian eigenvalue) during training -- do you observe edge-of-stability behavior?

**Tools:** NumPy, Matplotlib. No PyTorch/TensorFlow.
