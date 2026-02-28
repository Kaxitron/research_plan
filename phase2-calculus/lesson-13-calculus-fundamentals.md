# Lesson 13: Calculus Fundamentals — Rebuilding Your Intuition

[← Linear Algebra Capstone](../phase1-linear-algebra/lesson-12-capstone.md) | [Back to TOC](../README.md) | [Next: Matrix Calculus →](lesson-14-matrix-calculus.md)

---

> **Why this lesson exists:** You haven't touched calculus in 6 years. Lessons 13–18 assume fluency with derivatives, the chain rule, and basic integration. This lesson rebuilds that fluency from geometric intuition — exactly the way we approached linear algebra — so that when you hit partial derivatives and gradients, they feel like natural extensions rather than cold formulas.

> **Estimated time:** 6–10 hours (take your time — this is the foundation everything else rests on)

---

## Part 1: The Big Idea — What IS a Derivative?

### The Geometric Picture (Start Here)

Forget the limit definition for a moment. Here's what a derivative *is*:

**A derivative measures how fast something is changing at a specific instant.**

Imagine driving a car. Your speedometer reads 60 mph. That's a derivative — it's telling you the *instantaneous rate of change* of your position with respect to time. You haven't actually traveled 60 miles, and you might speed up or slow down in the next second. But *right now*, at this exact instant, your position is changing at 60 miles per hour.

Geometrically, picture a curve. Pick a point on it. The derivative at that point is the **slope of the tangent line** — the line that just barely touches the curve at that point and matches its direction.

### From Secant Lines to Tangent Lines

Here's how to build the derivative step by step:

1. Pick two points on a curve: (x, f(x)) and (x+h, f(x+h))
2. Draw a line through them — that's a **secant line**
3. Its slope is: (f(x+h) - f(x)) / h — the "rise over run"
4. Now **shrink h toward zero**. The second point slides toward the first.
5. The secant line *rotates* and settles into the **tangent line**
6. The slope it settles on is the derivative: **f'(x)**

This is the limit definition:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

You don't need to compute limits from scratch in ML. But you need to *feel* what this means: the derivative is what you get when you zoom in on a curve until it looks like a straight line.

### The "Zooming In" Intuition

This is the single most important intuition for all of calculus:

**Every smooth curve, if you zoom in far enough, looks like a straight line.**

Try it: graph y = x² and zoom into the point (1, 1). Keep zooming. Eventually it looks perfectly straight, with slope 2. That slope *is* the derivative at x = 1.

This is also **why gradient descent works** in neural networks. The loss surface is a complicated curved landscape. But near any point, if you zoom in enough, it looks flat — like a tilted plane. The gradient tells you which direction that plane tilts, and you step "downhill." Then you zoom in again at the new point, get a new local tilt, step downhill again. You're following straight-line approximations of a curved surface, one small step at a time.

### 🔗 ML Connection: Local Linearity IS Gradient Descent

When a neural network computes a gradient and takes a step, it's doing exactly this:
1. Zoom into the loss surface at the current weights
2. Approximate the surface as a flat plane (first-order Taylor approximation)
3. Step in the direction the plane tilts downhill
4. The **learning rate** controls how far you step before re-zooming

Step too far → the straight-line approximation is no longer accurate → you overshoot.
Step too small → you waste compute on tiny improvements.
This is why learning rate matters — it controls how much you trust the local linear approximation.

---

## Part 2: The Differentiation Toolkit

You need to be able to differentiate common functions quickly and confidently. Here are the rules, each with geometric intuition.

### The Power Rule

$$\frac{d}{dx} x^n = nx^{n-1}$$

**Examples:**
- d/dx (x²) = 2x — the slope of a parabola at x is 2x (steeper as you move away from 0)
- d/dx (x³) = 3x² — cubic curves change faster, and the rate accelerates
- d/dx (x) = 1 — a straight line has constant slope
- d/dx (constant) = 0 — flat lines have zero slope
- d/dx (x⁻¹) = -x⁻² — i.e., d/dx (1/x) = -1/x²
- d/dx (√x) = d/dx (x^(1/2)) = (1/2)x^(-1/2) = 1/(2√x)

**Intuition:** The power rule says "bring the exponent down as a multiplier, then reduce the power by 1." Higher powers mean the function grows (or shrinks) faster, so the derivative is a higher-degree polynomial.

### Constant Multiple and Sum Rules

$$\frac{d}{dx}[cf(x)] = c \cdot f'(x) \qquad \frac{d}{dx}[f(x) + g(x)] = f'(x) + g'(x)$$

Derivatives are **linear operators**. If you've internalized linear algebra, this should feel familiar — differentiation distributes over addition and commutes with scalar multiplication. In fact, the derivative operator D is a *linear transformation* on the space of functions. This is not a coincidence; it connects directly to how we think about function spaces in ML.

### The Product Rule

$$\frac{d}{dx}[f(x) \cdot g(x)] = f'(x) \cdot g(x) + f(x) \cdot g'(x)$$

**Intuition:** Imagine a rectangle with sides f(x) and g(x). As x changes, *both* sides change. The area changes by: (change in f) × g + f × (change in g). The two terms capture each side's contribution while the other holds still.

**Example:** d/dx [x² · sin(x)] = 2x · sin(x) + x² · cos(x)

### The Quotient Rule

$$\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{[g(x)]^2}$$

**Tip:** You can usually avoid the quotient rule by rewriting f/g as f · g⁻¹ and using the product rule + chain rule instead. Many practitioners prefer this approach.

### ⭐ The Chain Rule — The Most Important Rule in All of ML

$$\frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x)$$

In words: **"Derivative of the outside, evaluated at the inside, times the derivative of the inside."**

**Why this is THE rule for ML:** Every neural network is a composition of functions. Layer 1 feeds into Layer 2 feeds into Layer 3 feeds into the loss. Backpropagation is literally the chain rule applied to this composition. When you hear "backprop," think "chain rule on a computation graph."

**Example — step by step:**

Find d/dx (x² + 1)⁵

1. Identify the "outside" function: ( · )⁵ and the "inside" function: x² + 1
2. Derivative of outside: 5( · )⁴
3. Evaluate at inside: 5(x² + 1)⁴
4. Multiply by derivative of inside: × 2x
5. **Result:** 10x(x² + 1)⁴

**Chaining multiple layers:**

If you have f(g(h(x))), the chain rule gives:

$$\frac{d}{dx} f(g(h(x))) = f'(g(h(x))) \cdot g'(h(x)) \cdot h'(x)$$

Each "link" in the chain multiplies. In a 100-layer neural network, backprop multiplies through 100 chain rule factors. This is why **vanishing gradients** happen — if each factor is less than 1, the product shrinks exponentially.

**Example — nested:**

Find d/dx sin(e^(x²))

1. Outermost: sin(·) → derivative: cos(·) → cos(e^(x²))
2. Middle: e^(·) → derivative: e^(·) → e^(x²)
3. Innermost: x² → derivative: 2x
4. **Multiply all three:** 2x · e^(x²) · cos(e^(x²))

---

## Part 3: The Cast of Characters — Functions You'll See Everywhere in ML

### e^x — The Function That Is Its Own Derivative

$$\frac{d}{dx} e^x = e^x$$

This is remarkable and unique. No other function has this property. It means e^x grows at a rate proportional to its current value — pure exponential growth.

**Why ML loves it:**
- The **softmax** function uses e^x to convert raw scores into probabilities
- The **natural logarithm** (inverse of e^x) appears in every loss function involving log-likelihood
- **Exponential decay** (e^(-x)) models forgetting, cooling, and learning rate schedules

**With chain rule:** d/dx e^(g(x)) = e^(g(x)) · g'(x)

**Example:** d/dx e^(3x) = 3e^(3x) — the 3 comes "out" via the chain rule

### ln(x) — The Natural Logarithm

$$\frac{d}{dx} \ln(x) = \frac{1}{x}$$

**Why ML loves it:**
- **Cross-entropy loss** = -Σ yᵢ ln(ŷᵢ) — the log turns products into sums
- **Log-likelihood** — taking the log of a likelihood function makes optimization easier because it converts products into sums (and products of small numbers become sums, which don't underflow)
- **Information theory** — entropy and KL divergence are defined with logarithms (you'll see this in Phase 3)

**With chain rule:** d/dx ln(g(x)) = g'(x)/g(x)

**Key identity that appears everywhere:**
$$\frac{d}{dx} \ln(f(x)) = \frac{f'(x)}{f(x)}$$

This is called the **logarithmic derivative**. It measures the *relative* rate of change — "what fraction of itself is f changing by?" This shows up constantly in maximum likelihood estimation (Lesson 21).

### sin(x) and cos(x) — The Oscillators

$$\frac{d}{dx} \sin(x) = \cos(x) \qquad \frac{d}{dx} \cos(x) = -\sin(x)$$

**Intuition:** sin and cos are 90° out of phase. When sin is at its peak (slope = 0), cos = 0. When sin is climbing fastest (at x = 0), cos = 1. The derivative of sin tracks cos exactly.

**Where they appear in ML:**
- **Positional encodings** in transformers use sin and cos to encode token positions
- **Fourier features** for encoding high-frequency patterns
- Less central than e^x and ln(x), but they show up in specific architectures

### ⭐ The Sigmoid Function — The Original Activation Function

$$\sigma(x) = \frac{1}{1 + e^{-x}}$$

**What it does:** Squashes any real number into the range (0, 1). Large positive inputs → close to 1. Large negative inputs → close to 0. At x = 0, σ(0) = 0.5.

**Its beautiful derivative:**

$$\sigma'(x) = \sigma(x) \cdot (1 - \sigma(x))$$

The derivative of the sigmoid is expressed *in terms of itself*. This made it very convenient for early neural networks. The maximum derivative is 0.25 (at x = 0), which means gradients always shrink when passing through a sigmoid — this is one cause of the **vanishing gradient problem**.

**Derivation (good chain rule practice):**

σ(x) = (1 + e^(-x))⁻¹

Using chain rule:
- σ'(x) = -1 · (1 + e^(-x))⁻² · (-e^(-x))
- σ'(x) = e^(-x) / (1 + e^(-x))²
- σ'(x) = [1/(1 + e^(-x))] · [e^(-x)/(1 + e^(-x))]
- σ'(x) = σ(x) · [(1 + e^(-x) - 1)/(1 + e^(-x))]
- σ'(x) = σ(x) · [1 - 1/(1 + e^(-x))]
- **σ'(x) = σ(x) · (1 - σ(x))**

### tanh — The Centered Sigmoid

$$\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} = 2\sigma(2x) - 1$$

**Output range:** (-1, 1) — centered at zero, which is often better for optimization.

**Derivative:** tanh'(x) = 1 - tanh²(x) — again expressible in terms of itself.

### ReLU — The Modern Default

$$\text{ReLU}(x) = \max(0, x) = \begin{cases} x & \text{if } x > 0 \\ 0 & \text{if } x \leq 0 \end{cases}$$

**Derivative:**

$$\text{ReLU}'(x) = \begin{cases} 1 & \text{if } x > 0 \\ 0 & \text{if } x < 0 \\ \text{undefined} & \text{if } x = 0 \end{cases}$$

**Why ReLU won:** Its gradient is either 0 or 1 — never a fraction. This means gradients don't shrink when passing through ReLU layers, largely solving the vanishing gradient problem. In practice, we just define ReLU'(0) = 0 and it works fine.

**The tradeoff:** "Dead neurons" — if a neuron's input is always negative, its gradient is always 0, and it never learns. Variants like Leaky ReLU (small positive slope for x < 0) address this.

---

## Part 4: Integration — The Reverse Journey

### What Integration IS (Geometrically)

If differentiation asks "what's the slope?", integration asks "what's the area?"

**The definite integral** ∫ₐᵇ f(x) dx = the (signed) area between f(x) and the x-axis from x = a to x = b.

"Signed" means area below the x-axis counts as negative.

### The Fundamental Theorem of Calculus

**Differentiation and integration are inverses of each other.**

Part 1: If F(x) = ∫ₐˣ f(t) dt, then F'(x) = f(x).

(The derivative of the "area so far" function is the original function.)

Part 2: ∫ₐᵇ f(x) dx = F(b) - F(a), where F is any antiderivative of f.

(To compute a definite integral, find an antiderivative and evaluate at the endpoints.)

### Basic Antiderivatives (Reverse the Derivative Table)

| Function | Antiderivative |
|----------|---------------|
| xⁿ | x^(n+1)/(n+1) + C (for n ≠ -1) |
| 1/x | ln\|x\| + C |
| eˣ | eˣ + C |
| sin(x) | -cos(x) + C |
| cos(x) | sin(x) + C |

The "+ C" is the **constant of integration** — a reminder that many functions have the same derivative (vertical shifts don't change slope).

### 🔗 ML Connection: Why Integration Matters

You won't integrate much by hand in ML, but you need to understand it conceptually because:

1. **Probability:** P(a ≤ X ≤ b) = ∫ₐᵇ p(x) dx — probability IS area under a density curve. Every time you say "the probability of X being between 1 and 3," you're computing an integral. This is the entire foundation of Phase 3.

2. **Expectation:** E[X] = ∫ x · p(x) dx — the expected value IS a weighted integral. Loss functions in ML are often expectations.

3. **Normalization:** Probability densities must integrate to 1: ∫ p(x) dx = 1. This constraint is why softmax exists — it ensures neural network outputs form a valid probability distribution.

4. **Evidence in Bayesian inference:** P(data) = ∫ P(data|θ) P(θ) dθ — the denominator in Bayes' theorem is an integral over all possible parameter values. This integral is often intractable, which is why approximate methods (MCMC, variational inference) are so important.

---

## Part 5: Finding Maxima and Minima — This IS What Training Does

### Critical Points

A **critical point** is where f'(x) = 0 or f'(x) is undefined. These are candidates for maxima, minima, or saddle points.

**To find the minimum of a function:**
1. Take the derivative
2. Set it equal to zero: f'(x) = 0
3. Solve for x
4. Check whether it's a minimum (second derivative test)

**This is exactly what training a neural network does, in spirit.** Setting ∂L/∂w = 0 for every weight w would give you the optimal weights. But in high dimensions with millions of parameters, you can't solve this system analytically, so gradient descent *iteratively approximates* the solution by taking steps toward where the gradient is zero.

### The Second Derivative Test

The **second derivative** f''(x) measures how the *slope itself* is changing — it's the curvature.

At a critical point where f'(x) = 0:
- f''(x) > 0 → **local minimum** (concave up — bowl shape — the slope is increasing)
- f''(x) < 0 → **local maximum** (concave down — hill shape — the slope is decreasing)
- f''(x) = 0 → **inconclusive** (could be an inflection point)

**Example:**

f(x) = x³ - 3x

f'(x) = 3x² - 3 = 0 → x² = 1 → x = ±1

f''(x) = 6x

At x = 1: f''(1) = 6 > 0 → **local minimum** at (1, -2)
At x = -1: f''(-1) = -6 < 0 → **local maximum** at (-1, 2)

### 🔗 ML Connection: The Second Derivative Becomes the Hessian

In one dimension, f''(x) tells you curvature. In many dimensions, the matrix of all second partial derivatives — the **Hessian** — tells you curvature in every direction. You'll meet this properly in Lesson 13, but the intuition is the same: the Hessian tells you if you're at a bowl (minimum), a hill (maximum), or a saddle point. In neural networks, saddle points are far more common than local minima — this is a key insight you'll explore in Lesson 18.

---

## 📺 Watch

### Primary (watch these in order)

- **3Blue1Brown — Essence of Calculus, full playlist (12 videos)**
  - https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr
  - **This is your main resource.** Grant builds calculus from geometric intuition exactly the way we built linear algebra. Watch the whole playlist before moving to Lesson 13.
  - Key chapters for ML:
    - Ch. 1: "The essence of calculus" — area under curves, the fundamental theorem
    - Ch. 2: "The paradox of the derivative" — limits and instantaneous change
    - Ch. 3: "Derivative formulas through geometry" — visual power rule, product rule
    - Ch. 6: "Implicit differentiation" — useful for understanding constrained optimization later
    - Ch. 7: "Limits" — the formal machinery (watch for completeness, don't obsess)
    - Ch. 10: "Taylor series" — critical for understanding why gradient descent works
    - Ch. 11: "Taylor series (geometric view)" — connects to the "zooming in" intuition

- **Khan Academy — Calculus 1 (selected videos for extra practice)**
  - https://www.khanacademy.org/math/calculus-1
  - Use as supplementary practice if any rule feels shaky after 3B1B
  - Particularly recommended: Chain rule section, Optimization problems section

### Supplementary

- **Professor Leonard — Calculus 1 full lectures** (if you want a slower, classroom-style walkthrough)
  - https://www.youtube.com/playlist?list=PLF797E961509B4EB5
  - Very thorough but long — only use if 3B1B isn't enough

---

## 📖 Read

- **MML Book, Chapter 5.1–5.3** — Differentiation of univariate functions, partial differentiation basics
  - https://mml-book.github.io/
  - Focus on: derivative rules, chain rule, and Taylor series (5.1–5.3 before moving to 5.4+ in Lesson 13)

- **Paul's Online Math Notes — Calculus I Review**
  - https://tutorial.math.lamar.edu/Classes/CalcI/CalcI.aspx
  - Excellent for quick lookup and practice problems if a specific rule feels rusty

---

## 🔨 Do

### Drill Set 1: Core Differentiation (Warm Up)

Differentiate each by hand. No calculator. Check by plugging into a derivative calculator afterward.

1. f(x) = 3x⁴ - 2x² + 7x - 5
2. f(x) = (x² + 1)(x³ - x)  ← product rule
3. f(x) = (2x + 1)⁷  ← chain rule
4. f(x) = sin(x²)  ← chain rule
5. f(x) = e^(3x² - x)  ← chain rule
6. f(x) = ln(x² + 1)  ← chain rule
7. f(x) = x · e^x  ← product rule
8. f(x) = sin(x)/x  ← quotient rule or product rule with x⁻¹

### Drill Set 2: The Chain Rule (Critical for ML)

These are deliberately nested to build your chain-rule muscle:

1. f(x) = (sin(x))³
2. f(x) = e^(sin(x))
3. f(x) = ln(cos(x))
4. f(x) = σ(3x) where σ is the sigmoid — express your answer using σ(3x)
5. f(x) = (e^x + e^(-x))² ← this relates to cosh²(x)

### Drill Set 3: Finding Critical Points

For each function, find all critical points and classify them (min/max/inflection):

1. f(x) = x³ - 6x² + 9x + 1
2. f(x) = xe^(-x)  ← where does this peak?
3. f(x) = x - ln(x) for x > 0  ← this shape appears in KL divergence

### Drill Set 4: ML-Connected Exercises

1. **Sigmoid derivative:** Verify that σ'(x) = σ(x)(1 - σ(x)) by computing the derivative of 1/(1 + e^(-x)) from scratch using chain rule. Then plot σ(x) and σ'(x) in Python. Note where the derivative is largest and smallest.

2. **Cross-entropy gradient:** For L = -ln(σ(x)) (binary cross-entropy for the positive class), compute dL/dx. Simplify. What happens as σ(x) → 1 (confident correct)? As σ(x) → 0 (confident wrong)?

3. **Learning rate visualization:** Plot f(x) = x⁴ - 2x² + 1 (a double-well potential). Implement gradient descent manually:
   - Start at x = -0.5
   - Try learning rates: 0.01, 0.1, 0.5, 1.0
   - Plot the trajectory for each. Which converges? Which oscillates? Which diverges?

4. **Taylor approximation:** Plot f(x) = e^x alongside its 1st, 2nd, and 3rd order Taylor approximations around x = 0. See how each term adds precision. This is the math behind "locally linear" — gradient descent uses the 1st order approximation.

---

## ✅ Self-Assessment: Am I Ready for Lesson 13?

Before moving on, you should be able to:

- [ ] Differentiate any polynomial, exponential, logarithmic, or trigonometric function
- [ ] Apply the chain rule confidently to nested functions (2–3 layers deep)
- [ ] Apply the product rule without hesitation
- [ ] Derive σ'(x) = σ(x)(1 - σ(x)) from scratch
- [ ] Find critical points and classify them using the second derivative test
- [ ] Explain geometrically what a derivative, tangent line, and "locally linear" mean
- [ ] Explain why integration gives area under a curve
- [ ] Articulate why the chain rule is the mathematical foundation of backpropagation
- [ ] Explain why "zooming in" makes gradient descent work

---

## 🔗 Looking Ahead

This lesson gives you the single-variable foundations. Here's how each subsequent lesson builds on them:

| Lesson | How It Extends This Material |
|--------|------------------------------|
| **13: Matrix Calculus** | Derivatives of functions with *vector/matrix* inputs → gradients, Jacobians |
| **14: Gradients** | The gradient generalizes "slope" to multiple dimensions — points uphill |
| **15: Chain Rule** | The single-variable chain rule extends to computation graphs — this IS backprop |
| **16: Optimization** | Gradient descent is "follow the negative derivative" scaled up to millions of parameters |
| **17: Constrained Opt.** | What if you need the minimum *subject to a constraint*? Lagrange multipliers |
| **18: Loss Landscapes** | The geometry of high-dimensional critical points — why saddle points dominate |

Every concept in Lessons 13–18 is a multivariable generalization of something in this lesson. If this lesson is solid, the rest of Phase 2 will feel like natural extensions rather than new territory.
