# Lesson 13: Calculus Fundamentals — Rebuilding Your Intuition

[← Linear Algebra Capstone](../phase1-linear-algebra/lesson-12-capstone.md) | [Back to TOC](../README.md) | [Next: Matrix Calculus →](lesson-14-matrix-calculus.md)

---

> **Why this lesson exists:** You haven't touched calculus in 6 years. Lessons 14–27 assume fluency with derivatives, the chain rule, integration techniques, and series. This lesson rebuilds that fluency from geometric intuition — exactly the way we approached linear algebra — so that when you hit partial derivatives and gradients, they feel like natural extensions rather than cold formulas.

> **Estimated time:** 12–20 hours (take your time — this is the foundation everything else rests on)

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

### 🔗 ML & Alignment: Local Linearity IS Gradient Descent

When a neural network computes a gradient and takes a step, it's doing exactly this:
1. Zoom into the loss surface at the current weights
2. Approximate the surface as a flat plane (first-order Taylor approximation)
3. Step in the direction the plane tilts downhill
4. The **learning rate** controls how far you step before re-zooming

Step too far → the straight-line approximation is no longer accurate → you overshoot.
Step too small → you waste compute on tiny improvements.
This is why learning rate matters — it controls how much you trust the local linear approximation.

This matters for alignment: when we train a model with RLHF, gradient descent is the mechanism that teaches the model to be helpful, harmless, and honest. Understanding *how* the gradient signal propagates — where it's strong, where it vanishes, where it might be gamed — is essential for understanding whether alignment training actually works.

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

### 🔗 ML & Alignment: Why Integration Matters

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

### 🔗 ML & Alignment: The Second Derivative Becomes the Hessian

In one dimension, f''(x) tells you curvature. In many dimensions, the matrix of all second partial derivatives — the **Hessian** — tells you curvature in every direction. You'll meet this properly in Lesson 14, but the intuition is the same: the Hessian tells you if you're at a bowl (minimum), a hill (maximum), or a saddle point. In neural networks, saddle points are far more common than local minima — this is a key insight you'll explore in Lesson 19.

---

## Part 6: Implicit Differentiation — Derivatives Without y = f(x)

### The Idea

So far, every function has been written as y = f(x) — y is *explicitly* defined in terms of x. But sometimes you have a relationship between x and y that isn't solved for y, like:

$$x^2 + y^2 = 25$$

This is a circle. It's not a function (it fails the vertical line test), but it still defines a *relationship* between x and y. At most points on the circle, if you zoom in, you see a smooth curve with a well-defined slope. How do you find that slope?

### The Technique

The trick: **differentiate both sides with respect to x**, treating y as a function of x (even though you can't write it explicitly). Whenever you differentiate a term containing y, tack on a dy/dx via the chain rule.

**Example:** x² + y² = 25

Differentiate both sides with respect to x:
- d/dx(x²) = 2x
- d/dx(y²) = 2y · (dy/dx)  ← chain rule! y is a function of x
- d/dx(25) = 0

So: 2x + 2y(dy/dx) = 0

Solve for dy/dx: **dy/dx = -x/y**

This makes geometric sense! At the point (3, 4) on the circle, the slope is -3/4. The tangent line tilts down to the right, which matches the circle curving away from the top.

**A more complex example:** x³ + y³ = 6xy

This is the *folium of Descartes* — a beautiful curve that loops through the origin.

Differentiate: 3x² + 3y²(dy/dx) = 6y + 6x(dy/dx)

Collect dy/dx terms: 3y²(dy/dx) - 6x(dy/dx) = 6y - 3x²

Factor: (3y² - 6x)(dy/dx) = 6y - 3x²

**dy/dx = (6y - 3x²) / (3y² - 6x) = (2y - x²) / (y² - 2x)**

### 🔗 ML Connection

Implicit differentiation is the conceptual ancestor of **automatic differentiation.** In a computation graph, you don't have an explicit formula for the loss as a simple function of one weight — it's defined *implicitly* through layers of computation. The chain rule applied through the graph (backprop) is doing the same essential thing: finding derivatives of quantities that are defined through relationships rather than explicit formulas.

It also appears directly in **constrained optimization** (Lesson 18): when you optimize subject to a constraint g(x, y) = 0, implicit differentiation tells you how y must change when x changes to stay on the constraint surface.

---

## Part 7: Integration by Substitution (u-Substitution) — The Chain Rule in Reverse

### The Idea

The chain rule says: d/dx f(g(x)) = f'(g(x)) · g'(x)

Reading this *backward* as an integration rule: if you see an integrand that looks like f'(g(x)) · g'(x), its antiderivative is f(g(x)).

The technique: let **u = g(x)**, so **du = g'(x) dx**. Replace everything in the integral with u's and du's, integrate in the simpler u-world, then substitute back.

### Step-by-Step Example

$$\int 2x \cos(x^2) \, dx$$

1. **Spot the inner function:** x² looks like a good candidate for u
2. **Let u = x²**, so **du = 2x dx**
3. The integral becomes: ∫ cos(u) du
4. Integrate: sin(u) + C
5. Substitute back: **sin(x²) + C**

Check by differentiating: d/dx sin(x²) = cos(x²) · 2x ✓

### When the du Doesn't Match Perfectly

$$\int x \cdot e^{x^2} \, dx$$

Let u = x². Then du = 2x dx, so x dx = du/2.

∫ x · e^(x²) dx = ∫ e^u · (du/2) = (1/2)e^u + C = **(1/2)e^(x²) + C**

You often need to multiply/divide by constants to make the substitution work. You can always adjust constants, but you **cannot** adjust functions of x — if the "leftover" after substitution still contains x, you need a different approach.

### Definite Integrals: Change the Bounds

$$\int_0^1 2x(x^2 + 1)^3 \, dx$$

Let u = x² + 1, du = 2x dx. When x = 0, u = 1. When x = 1, u = 2.

= ∫₁² u³ du = [u⁴/4]₁² = 16/4 - 1/4 = **15/4**

### 🔗 ML Connection

Change of variables in integrals is essential for **probability.** When you transform a random variable — say, passing Gaussian noise through a neural network — you need u-substitution (or its multivariable cousin, the change-of-variables formula with a Jacobian determinant) to find the resulting distribution. This is the mathematical foundation of **normalizing flows,** a generative model architecture that transforms simple distributions into complex ones through invertible neural networks.

---

## Part 8: Integration by Parts — The Product Rule in Reverse

### The Formula

The product rule says: d/dx [u · v] = u'v + uv'

Rearranging: uv' = d/dx[uv] - u'v

Integrating both sides:

$$\int u \, dv = uv - \int v \, du$$

In words: pick one part of the integrand to differentiate (u) and the other to integrate (dv). The hope is that ∫ v du is simpler than what you started with.

### The LIATE Rule for Choosing u

When deciding what to call u, prioritize in this order (the thing you **differentiate**):

**L**ogarithmic → **I**nverse trig → **A**lgebraic → **T**rigonometric → **E**xponential

The idea: logs and polynomials get *simpler* when differentiated, while exponentials and trig functions are easy to integrate. You want u to simplify under differentiation.

### Example 1: ∫ x · eˣ dx

- Let u = x (algebraic — simplifies when differentiated), dv = eˣ dx
- Then du = dx, v = eˣ
- ∫ x eˣ dx = x eˣ - ∫ eˣ dx = **x eˣ - eˣ + C = eˣ(x - 1) + C**

### Example 2: ∫ x² sin(x) dx

This requires **two rounds** of integration by parts:

Round 1: u = x², dv = sin(x) dx → du = 2x dx, v = -cos(x)
= -x² cos(x) + ∫ 2x cos(x) dx

Round 2: u = 2x, dv = cos(x) dx → du = 2 dx, v = sin(x)
= -x² cos(x) + 2x sin(x) - ∫ 2 sin(x) dx
= **-x² cos(x) + 2x sin(x) + 2 cos(x) + C**

### Example 3: ∫ ln(x) dx — A Trick

This one surprises people. Let u = ln(x), dv = dx:
- du = (1/x) dx, v = x
- ∫ ln(x) dx = x ln(x) - ∫ x · (1/x) dx = x ln(x) - x + C = **x(ln(x) - 1) + C**

### Example 4: The "Circular" Trick — ∫ eˣ sin(x) dx

Sometimes integration by parts loops back to the original integral. When that happens, solve algebraically:

Let I = ∫ eˣ sin(x) dx

Round 1: u = sin(x), dv = eˣ dx → I = eˣ sin(x) - ∫ eˣ cos(x) dx

Round 2: u = cos(x), dv = eˣ dx → I = eˣ sin(x) - [eˣ cos(x) + ∫ eˣ sin(x) dx]

I = eˣ sin(x) - eˣ cos(x) - I

2I = eˣ(sin(x) - cos(x))

**I = eˣ(sin(x) - cos(x)) / 2 + C**

### 🔗 ML Connection

Integration by parts appears when computing **expectations** of products (e.g., E[X · g(X)] for certain distributions), in deriving properties of the **Gaussian distribution,** and in the **ELBO (Evidence Lower Bound)** derivations used in variational autoencoders. It's also the foundation of **Stein's method** in probability, which has connections to score-based generative models.

---

## Part 9: Trigonometric Substitution — Handling Square Roots

### When to Use It

Trig substitution handles integrals involving these patterns:

| Expression | Substitution | Why it works |
|-----------|-------------|-------------|
| √(a² - x²) | x = a sin(θ) | Because 1 - sin²θ = cos²θ eliminates the root |
| √(a² + x²) | x = a tan(θ) | Because 1 + tan²θ = sec²θ eliminates the root |
| √(x² - a²) | x = a sec(θ) | Because sec²θ - 1 = tan²θ eliminates the root |

### The Geometric Picture

For √(a² - x²): draw a right triangle with hypotenuse a and one leg x. Then the other leg is √(a² - x²). Setting x = a sin(θ) means θ is the angle opposite the leg x. All the square root expressions become simple trig functions of θ.

### Example: ∫ √(4 - x²) dx

This is the area under a semicircle of radius 2 — we should get something involving π if we do a definite integral.

Let x = 2 sin(θ), so dx = 2 cos(θ) dθ

√(4 - x²) = √(4 - 4sin²θ) = 2√(1 - sin²θ) = 2 cos(θ)

∫ 2cos(θ) · 2cos(θ) dθ = 4 ∫ cos²(θ) dθ

Use the identity cos²(θ) = (1 + cos(2θ))/2:

= 4 · (θ/2 + sin(2θ)/4) + C = 2θ + sin(2θ) + C

Since sin(2θ) = 2 sin(θ) cos(θ) = 2 · (x/2) · (√(4-x²)/2) = x√(4-x²)/2:

= **2 arcsin(x/2) + x√(4-x²)/2 + C**

### Example: ∫ dx / (x² + 9)

Let x = 3 tan(θ), dx = 3 sec²(θ) dθ

x² + 9 = 9 tan²(θ) + 9 = 9 sec²(θ)

∫ 3 sec²(θ) / (9 sec²(θ)) dθ = (1/3) ∫ dθ = θ/3 + C = **(1/3) arctan(x/3) + C**

### 🔗 ML Connection

Trig substitution is less common in day-to-day ML than the other integration techniques, but it appears in deriving the **normalizing constants** of certain probability distributions (especially the Student-t distribution, which involves (1 + x²/ν)^(-...) integrands) and in **kernel methods** where radial basis functions involve √(||x - y||² + σ²) expressions.

---

## Part 10: Improper Integrals — Integrating to Infinity

### The Core Idea

What happens when the bounds of an integral go to ±∞, or when the integrand blows up? These are **improper integrals,** and the key question is: **does the total area converge to a finite number, or does it diverge to infinity?**

### Type 1: Infinite Bounds

$$\int_1^{\infty} \frac{1}{x^2} \, dx = \lim_{b \to \infty} \int_1^b \frac{1}{x^2} \, dx = \lim_{b \to \infty} \left[-\frac{1}{x}\right]_1^b = \lim_{b \to \infty} \left(-\frac{1}{b} + 1\right) = 1$$

The area under 1/x² from 1 to ∞ is exactly 1. It **converges.**

Compare with: ∫₁^∞ 1/x dx = lim_{b→∞} [ln(x)]₁ᵇ = lim_{b→∞} ln(b) = ∞. This **diverges.**

### The p-Test: When Does 1/xᵖ Converge?

$$\int_1^{\infty} \frac{1}{x^p} \, dx \text{ converges if and only if } p > 1$$

This is worth memorizing. 1/x (p = 1) is the critical boundary case — it diverges (just barely). 1/x² (p = 2) converges. 1/x^(1.001) converges. 1/x^(0.999) diverges. The boundary is sharp.

### Type 2: Integrand Blows Up

$$\int_0^1 \frac{1}{\sqrt{x}} \, dx = \lim_{\epsilon \to 0^+} \int_\epsilon^1 x^{-1/2} \, dx = \lim_{\epsilon \to 0^+} [2\sqrt{x}]_\epsilon^1 = 2 - 0 = 2$$

Even though 1/√x → ∞ as x → 0, the area is finite. It **converges.**

### The Gaussian Integral — The Most Important Improper Integral in All of Statistics

$$\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}$$

This result is remarkable — the area under the bell curve involves π, even though there are no circles in sight. The proof uses a clever trick: square the integral, convert to polar coordinates, and the r integral becomes a simple u-substitution. You'll use this result constantly in Phase 3 when working with Gaussian (normal) distributions.

The full Gaussian PDF includes a normalizing constant: p(x) = (1/√(2π)) e^(-x²/2). That 1/√(2π) is there precisely to make the integral equal 1, as a probability distribution requires.

### Comparison Test (Intuition)

If you can't evaluate an improper integral directly, compare it:
- If 0 ≤ f(x) ≤ g(x) and ∫ g(x) converges → ∫ f(x) converges (it's smaller than something finite)
- If f(x) ≥ g(x) ≥ 0 and ∫ g(x) diverges → ∫ f(x) diverges (it's bigger than something infinite)

### 🔗 ML & Alignment Connection

**Every probability distribution you'll ever use** requires improper integrals to verify it integrates to 1. The Gaussian, exponential, Cauchy, and Student-t distributions all integrate over infinite domains. Understanding convergence vs. divergence tells you which distributions have finite means, finite variances, or neither — the Cauchy distribution, for example, has no mean at all because the integral ∫ x/(π(1+x²)) dx diverges. This matters for understanding **heavy-tailed phenomena** in ML, including the sometimes-surprising behavior of gradient norms during training.

---

## Part 11: Applied Optimization — Setting Up and Solving Word Problems

### The Framework

Applied optimization follows a consistent pattern:

1. **Draw a picture** and label everything
2. **Write the objective function** — what are you maximizing or minimizing?
3. **Write the constraint** — what relationship limits the variables?
4. **Use the constraint to eliminate a variable** — reduce to one variable
5. **Take the derivative, set it to zero, solve**
6. **Verify it's a max/min** (second derivative test or endpoint check)

### Example 1: The Classic Fence Problem

A farmer has 200 feet of fencing and wants to enclose the maximum rectangular area against a barn wall (one side doesn't need fencing).

1. Let x = length perpendicular to barn, y = length parallel to barn
2. **Objective:** Maximize A = xy
3. **Constraint:** 2x + y = 200 (two sides of length x, one of length y)
4. **Eliminate:** y = 200 - 2x, so A(x) = x(200 - 2x) = 200x - 2x²
5. **Differentiate:** A'(x) = 200 - 4x = 0 → x = 50, so y = 100
6. **Verify:** A''(x) = -4 < 0 → maximum ✓

**Maximum area = 5000 ft²** with dimensions 50 × 100.

### Example 2: Minimizing Distance

Find the point on the curve y = √x closest to the point (3, 0).

1. **Objective:** Minimize D² = (x - 3)² + (√x)² = (x - 3)² + x (minimizing D² avoids the square root, and the minimum occurs at the same point)
2. Let f(x) = x² - 6x + 9 + x = x² - 5x + 9
3. f'(x) = 2x - 5 = 0 → x = 5/2
4. y = √(5/2)
5. f''(x) = 2 > 0 → minimum ✓

### Example 3: Optimization with Trig

A window has the shape of a rectangle topped by a semicircle. If the perimeter is 12 feet, find the dimensions that maximize the area.

1. Let w = width (= diameter of semicircle), h = height of rectangular part
2. **Objective:** A = wh + π(w/2)²/2 = wh + πw²/8
3. **Constraint:** Perimeter = w + 2h + π(w/2) = w + 2h + πw/2 = 12
4. **Eliminate:** h = (12 - w - πw/2) / 2 = 6 - w/2 - πw/4
5. Substitute into A, differentiate, set to zero, solve

The algebra gets messy, but the *pattern* is the same every time: objective, constraint, eliminate, differentiate, solve.

### 🔗 ML Connection

This "set up an objective function, then optimize" pattern is *literally* what ML does. In ML, the objective is the loss function, the constraints might be regularization or architecture choices, and the optimization is gradient descent. The skill of translating a real-world problem into "what am I minimizing and what are the constraints?" is the same skill you use when designing a loss function for a new task.

---

## Part 12: Series and Infinite Sums — When Adding Forever Gives a Finite Answer

### The Core Question

Can you add up infinitely many numbers and get a finite result? Sometimes yes, sometimes no. The study of **when** and **why** is the theory of series.

### Geometric Series — The Most Important Series in Practice

$$\sum_{n=0}^{\infty} r^n = \frac{1}{1 - r} \quad \text{when } |r| < 1$$

**Example:** 1 + 1/2 + 1/4 + 1/8 + ... = 1/(1 - 1/2) = 2

**Intuition:** Each term adds half of the remaining distance to 2. You never overshoot, but you get arbitrarily close.

**When |r| ≥ 1,** the series diverges — the terms don't shrink, so the sum grows without bound.

### The Harmonic Series — A Surprise

$$\sum_{n=1}^{\infty} \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots = \infty$$

The terms go to zero, but the sum is infinite! The terms don't shrink *fast enough.* This is the series analog of ∫₁^∞ 1/x dx diverging.

**Key lesson:** Terms going to zero is **necessary** but **not sufficient** for convergence.

### p-Series

$$\sum_{n=1}^{\infty} \frac{1}{n^p} \text{ converges if and only if } p > 1$$

Same threshold as the improper integral, and for the same reason (the integral test connects them directly).

### Convergence Tests — A Quick Reference

| Test | When to use | How it works |
|------|------------|--------------|
| **Divergence test** | Always check first | If lim aₙ ≠ 0, the series diverges. (If = 0, inconclusive.) |
| **Geometric series** | aₙ = arⁿ | Converges iff \|r\| < 1, sum = a/(1-r) |
| **p-series** | aₙ = 1/nᵖ | Converges iff p > 1 |
| **Comparison** | Can bound aₙ by a known series | 0 ≤ aₙ ≤ bₙ and Σbₙ converges → Σaₙ converges |
| **Ratio test** | Terms with factorials or exponentials | lim \|aₙ₊₁/aₙ\| < 1 → converges; > 1 → diverges |
| **Integral test** | aₙ = f(n) with f positive, decreasing | Σaₙ and ∫f(x)dx converge/diverge together |
| **Alternating series** | Signs alternate: (-1)ⁿ aₙ | If aₙ decreasing → 0, the series converges |

### Power Series — Functions as Infinite Polynomials

A **power series** is an infinite polynomial: Σ aₙxⁿ. It converges for some values of x and diverges for others. The **radius of convergence R** defines the interval (-R, R) where the series converges.

Every Taylor series is a power series. The Taylor series of f(x) around x = 0 (also called the **Maclaurin series**) is:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n$$

**Key examples:**

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots \quad (R = \infty)$$

$$\sin(x) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots \quad (R = \infty)$$

$$\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n = 1 + x + x^2 + x^3 + \cdots \quad (R = 1)$$

$$\ln(1 + x) = \sum_{n=1}^{\infty} \frac{(-1)^{n+1} x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots \quad (R = 1)$$

### 🔗 ML & Alignment Connection

**Geometric series** show up directly in **reinforcement learning:** the discounted return G = r₁ + γr₂ + γ²r₃ + ... is a geometric-series-weighted sum of rewards. The discount factor γ < 1 ensures this converges, just like |r| < 1 ensures the geometric series converges.

**Taylor series** are the mathematical foundation of gradient descent. The first-order Taylor approximation f(x + δ) ≈ f(x) + f'(x)δ is exactly the "locally linear" model that gradient descent trusts for one step. The second-order approximation involves the Hessian and is the basis for Newton's method. You'll explore this in depth in Lesson 21.

**Power series** concepts also appear in **neural tangent kernel** theory, where the training dynamics of infinitely wide networks can be expressed as series expansions, and in **Singular Learning Theory,** where the "real log canonical threshold" involves analyzing singularities of loss functions — a topic you'll encounter toward the end of this curriculum.

---

## 📺 Watch

### Primary (watch these in order)

- **3Blue1Brown — Essence of Calculus, full playlist (12 videos)**
  - https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr
  - **This is your main resource.** Grant builds calculus from geometric intuition exactly the way we built linear algebra. Watch the whole playlist before moving on.
  - Key chapters for ML:
    - Ch. 1: "The essence of calculus" — area under curves, the fundamental theorem
    - Ch. 2: "The paradox of the derivative" — limits and instantaneous change
    - Ch. 3: "Derivative formulas through geometry" — visual power rule, product rule
    - Ch. 6: "Implicit differentiation" — useful for understanding constrained optimization later
    - Ch. 7: "Limits" — the formal machinery (watch for completeness, don't obsess)
    - Ch. 10: "Taylor series" — critical for understanding why gradient descent works
    - Ch. 11: "Taylor series (geometric view)" — connects to the "zooming in" intuition

### Integration Techniques

- **Khan Academy — Integration techniques**
  - https://www.khanacademy.org/math/calculus-2
  - Use the u-substitution, integration by parts, and trig substitution sections
  - Also: improper integrals section, series and convergence tests sections

- **3Blue1Brown — "But what is a convolution?"**
  - https://www.youtube.com/watch?v=KuXjwB4LzSA
  - Not strictly integration technique, but connects integration to signal processing and neural networks

### Supplementary

- **Khan Academy — Calculus 1**
  - https://www.khanacademy.org/math/calculus-1
  - Use as supplementary practice if any rule feels shaky after 3B1B
  - Particularly recommended: Chain rule section, Optimization problems section

- **Professor Leonard — Calculus 2 playlist**
  - https://www.youtube.com/playlist?list=PLDesaqWTN6ESPaHy2QUKVaXNZuQNxkYQ_
  - Very thorough, lecture-style. Good for integration by parts, trig substitution, and series if you want someone to walk through many examples slowly

---

## 📖 Read

- **MML Book, Chapter 5.1–5.3** — Differentiation of univariate functions, partial differentiation basics
  - https://mml-book.github.io/
  - Focus on: derivative rules, chain rule, and Taylor series (5.1–5.3 before moving to 5.4+ in Lesson 14)

- **Paul's Online Math Notes — Calculus I & II Review**
  - https://tutorial.math.lamar.edu/Classes/CalcI/CalcI.aspx
  - https://tutorial.math.lamar.edu/Classes/CalcII/CalcII.aspx
  - Excellent for quick lookup and practice problems. Especially useful sections:
    - Calculus I: Implicit differentiation, optimization
    - Calculus II: Integration by parts, trig substitution, improper integrals, series & convergence tests

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

### Drill Set 5: Implicit Differentiation

1. Find dy/dx for: x² + xy + y² = 7
2. Find the slope of the tangent line to x³ + y³ = 9xy at the point (2, 4)
3. Find dy/dx for: sin(xy) = x + y

### Drill Set 6: Integration Techniques

**U-substitution:**
1. ∫ x · cos(x²) dx
2. ∫ e^(2x) / (1 + e^(2x)) dx
3. ∫₀¹ x²(x³ + 1)⁴ dx

**Integration by parts:**
4. ∫ x · ln(x) dx
5. ∫ x² · eˣ dx
6. ∫ arctan(x) dx  ← (hint: let u = arctan(x), dv = dx)

**Trig substitution:**
7. ∫ dx / √(9 - x²)
8. ∫ √(1 + x²) dx  ← this is hard, don't worry if it takes a while

### Drill Set 7: Improper Integrals and Series

**Improper integrals:**
1. ∫₁^∞ 1/x³ dx — evaluate and verify convergence
2. ∫₀^∞ xe^(-x) dx — evaluate using integration by parts
3. Does ∫₁^∞ 1/(x ln(x)) dx converge or diverge? (hint: u-substitution)

**Series:**
4. Determine convergence/divergence: Σ (1/3)ⁿ for n = 0 to ∞. If convergent, find the sum.
5. Determine convergence/divergence: Σ n/(n+1) for n = 1 to ∞
6. Use the ratio test on: Σ n!/nⁿ for n = 1 to ∞
7. Write the first 4 nonzero terms of the Taylor series for f(x) = cos(x) around x = 0

### Drill Set 8: Applied Optimization

1. Find two positive numbers whose sum is 100 and whose product is maximized.
2. A box with a square base and open top must have a volume of 32,000 cm³. Find the dimensions that minimize the amount of material used.
3. A 10-foot ladder leans against a wall. The base slides away at 1 ft/sec. How fast is the top sliding down when the base is 6 ft from the wall? ← (related rates — uses implicit differentiation)

---

## ✅ Self-Assessment: Am I Ready for Lesson 14?

Before moving on, you should be able to:

- [ ] Differentiate any polynomial, exponential, logarithmic, or trigonometric function
- [ ] Apply the chain rule confidently to nested functions (2–3 layers deep)
- [ ] Apply the product rule without hesitation
- [ ] Use implicit differentiation to find dy/dx
- [ ] Derive σ'(x) = σ(x)(1 - σ(x)) from scratch
- [ ] Find critical points and classify them using the second derivative test
- [ ] Set up and solve applied optimization problems (objective + constraint → eliminate → differentiate)
- [ ] Evaluate integrals using u-substitution
- [ ] Evaluate integrals using integration by parts (including choosing u via LIATE)
- [ ] Set up a trig substitution for integrals involving √(a² - x²), √(a² + x²), or √(x² - a²)
- [ ] Evaluate improper integrals and determine convergence vs. divergence
- [ ] Determine whether a series converges using the appropriate test
- [ ] Write the Taylor/Maclaurin series for eˣ, sin(x), cos(x), and 1/(1-x)
- [ ] Explain geometrically what a derivative, tangent line, and "locally linear" mean
- [ ] Explain why integration gives area under a curve
- [ ] Articulate why the chain rule is the mathematical foundation of backpropagation
- [ ] Explain why "zooming in" makes gradient descent work

---

## 📝 Comprehensive Quiz: First-Semester Calculus / BC Calculus Refresher

> **Instructions:** Work these problems by hand, showing your reasoning. No calculator. This quiz covers the full scope of Lesson 13. Give yourself about 90 minutes.

---

### Question 1: Derivative Fundamentals + Chain Rule

Differentiate:

$$f(x) = \ln\!\Big(\frac{e^{3x}}{\sqrt{x^2 + 1}}\Big)$$

*Hint:* Simplify with log rules first, then differentiate. This tests whether you can combine logarithm properties with the chain rule — exactly the manipulation you'll need when working with log-likelihoods in ML.

---

### Question 2: Implicit Differentiation

The curve x²y + xy² = 6 passes through the point (1, 2).

**(a)** Find dy/dx using implicit differentiation.

**(b)** Find the equation of the tangent line at (1, 2).

---

### Question 3: The Sigmoid — An ML Rite of Passage

The sigmoid function is σ(x) = 1/(1 + e^(-x)).

**(a)** Derive σ'(x) from scratch using the chain rule. Show every step.

**(b)** The maximum value of σ'(x) is 1/4, occurring at x = 0. Explain in one sentence why this is a problem for deep neural networks. (This is the **vanishing gradient problem.**)

---

### Question 4: Applied Optimization

A rectangular poster must contain 150 in² of printed area. The top and bottom margins are 3 inches each, and the side margins are 2 inches each. Find the overall dimensions of the poster that minimize the total amount of paper used.

---

### Question 5: Integration by Substitution

Evaluate:

$$\int_0^{\pi/2} \sin^3(x) \cos(x) \, dx$$

---

### Question 6: Integration by Parts

Evaluate:

$$\int x^2 \ln(x) \, dx$$

---

### Question 7: Trig Substitution

Evaluate:

$$\int \frac{dx}{x^2 \sqrt{x^2 + 4}}$$

*Hint:* Let x = 2 tan(θ).

---

### Question 8: Improper Integrals

Determine whether each integral converges or diverges. If it converges, find its value.

**(a)** $$\int_1^{\infty} \frac{x}{(x^2 + 1)^2} \, dx$$

**(b)** $$\int_0^{\infty} e^{-3x} \, dx$$

---

### Question 9: Series and Convergence

**(a)** Does the series converge or diverge? Find the sum if it converges.

$$\sum_{n=1}^{\infty} \frac{4}{3^n}$$

**(b)** Use the ratio test to determine convergence or divergence:

$$\sum_{n=0}^{\infty} \frac{n^2}{2^n}$$

**(c)** Write the Taylor series for e^(-x²) around x = 0, up to the x⁶ term. *(Hint: start from the known series for eˣ and substitute.)*

---

### Question 10: Connecting Calculus to ML — Conceptual

Answer each in 2–3 sentences:

**(a)** Gradient descent takes a step in the direction -αf'(x). Using the idea of Taylor series / local linearity, explain why a large learning rate α can cause the loss to *increase* instead of decrease.

**(b)** The ReLU activation function has derivative 1 for x > 0 and 0 for x < 0. The sigmoid's maximum derivative is 0.25. Explain why this difference matters when you apply the chain rule across 50 layers (i.e., multiply 50 derivative factors together).

**(c)** In reinforcement learning, the total discounted reward is G = r₁ + γr₂ + γ²r₃ + ... where 0 < γ < 1. Why does this sum converge? What would happen if γ = 1?

---

### Quiz Answer Key

<details>
<summary>Click to reveal answers (try all problems first!)</summary>

**Q1:**
First simplify: ln(e^(3x) / √(x²+1)) = 3x - (1/2)ln(x²+1)

f'(x) = 3 - (1/2) · 2x/(x²+1) = 3 - x/(x²+1) = **(3x² + 3 - x) / (x² + 1)**

**Q2:**
(a) Differentiate: 2xy + x²(dy/dx) + y² + 2xy(dy/dx) = 0

dy/dx(x² + 2xy) = -(2xy + y²)

**dy/dx = -(2xy + y²) / (x² + 2xy)**

At (1,2): dy/dx = -(4 + 4)/(1 + 4) = **-8/5**

(b) y - 2 = (-8/5)(x - 1) → **y = (-8/5)x + 18/5**

**Q3:**
(a) σ(x) = (1 + e^(-x))^(-1)

σ'(x) = -1 · (1 + e^(-x))^(-2) · (-e^(-x)) = e^(-x) / (1 + e^(-x))²

= [1/(1+e^(-x))] · [e^(-x)/(1+e^(-x))]

= σ(x) · [(1 + e^(-x) - 1)/(1 + e^(-x))]

= **σ(x)(1 - σ(x))**

(b) When you chain 50 sigmoid layers via the chain rule, you multiply ~50 factors of σ'(x) ≤ 0.25. So the gradient shrinks by at least (0.25)^50 ≈ 10^(-30) — effectively zero. The gradient signal vanishes and early layers can't learn.

**Q4:**
Let x = width of printed area, y = height of printed area. Then xy = 150, so y = 150/x.

Total paper: A = (x + 4)(y + 6) = (x + 4)(150/x + 6)

A = 150 + 6x + 600/x + 24 = 6x + 600/x + 174

A'(x) = 6 - 600/x² = 0 → x² = 100 → x = 10, y = 15

Total dimensions: **(10 + 4) × (15 + 6) = 14 × 21 inches**

A''(x) = 1200/x³ > 0 → minimum ✓

**Q5:**
Let u = sin(x), du = cos(x) dx. When x = 0, u = 0; when x = π/2, u = 1.

∫₀¹ u³ du = [u⁴/4]₀¹ = **1/4**

**Q6:**
Let u = ln(x), dv = x² dx → du = (1/x) dx, v = x³/3

∫ x² ln(x) dx = (x³/3)ln(x) - ∫ (x³/3)(1/x) dx = (x³/3)ln(x) - (1/3)∫ x² dx

= **(x³/3)ln(x) - x³/9 + C = (x³/9)(3ln(x) - 1) + C**

**Q7:**
Let x = 2tan(θ), dx = 2sec²(θ)dθ, √(x²+4) = 2sec(θ)

∫ 2sec²(θ) / (4tan²(θ) · 2sec(θ)) dθ = (1/4) ∫ sec(θ)/tan²(θ) dθ = (1/4) ∫ cos(θ)/sin²(θ) dθ

Let u = sin(θ): = (1/4) · (-1/sin(θ)) + C = -1/(4sin(θ)) + C

Since x = 2tan(θ), we have sin(θ) = x/√(x²+4):

= **-√(x²+4) / (4x) + C**

**Q8:**
(a) u = x² + 1: ∫₂^∞ (1/2)u⁻² du = [-1/(2u)]₂^∞ = 0 + 1/4 = **1/4, converges**

(b) ∫₀^∞ e^(-3x) dx = [-e^(-3x)/3]₀^∞ = 0 + 1/3 = **1/3, converges**

**Q9:**
(a) Geometric with a = 4/3, r = 1/3: Sum = (4/3)/(1 - 1/3) = (4/3)/(2/3) = **2, converges**

(b) aₙ = n²/2ⁿ. Ratio: (n+1)²·2ⁿ / (n²·2^(n+1)) = ((n+1)/n)² · (1/2) → **1/2 < 1, converges**

(c) e^u = 1 + u + u²/2! + u³/3! + ... Substitute u = -x²:

**e^(-x²) = 1 - x² + x⁴/2 - x⁶/6 + ...**

**Q10:**
(a) Gradient descent trusts the first-order Taylor approximation: L(w - αL') ≈ L(w) - α(L')². This approximation is only accurate near w. If α is too large, you step beyond where the linear approximation is valid — the actual curved surface may go uphill even though the tangent plane pointed downhill.

(b) With ReLU, the chain rule product across 50 layers is 1^50 = 1 (for active neurons) — the gradient passes through unchanged. With sigmoid, the product is at most (0.25)^50 ≈ 10^(-30) — effectively zero. Sigmoid's fractional derivatives multiply to nothing; ReLU's derivative of 1 preserves the signal.

(c) It's a geometric series with ratio γ, so it converges to at most r_max/(1-γ). If γ = 1, the series becomes r₁ + r₂ + r₃ + ..., which diverges if rewards are consistently positive — the agent would value the infinite future equally with the present, making optimization impossible.

</details>

---

## 🔗 Looking Ahead

This lesson gives you the single-variable foundations. Here's how each subsequent lesson builds on them:

| Lesson | How It Extends This Material |
|--------|------------------------------|
| **14: Matrix Calculus** | Derivatives of functions with *vector/matrix* inputs → gradients, Jacobians |
| **15: Gradients** | The gradient generalizes "slope" to multiple dimensions — points uphill |
| **16: Chain Rule** | The single-variable chain rule extends to computation graphs — this IS backprop |
| **17: Optimization** | Gradient descent is "follow the negative derivative" scaled up to millions of parameters |
| **18: Constrained Opt.** | What if you need the minimum *subject to a constraint*? Lagrange multipliers |
| **19: Loss Landscapes** | The geometry of high-dimensional critical points — why saddle points dominate |

Every concept in Lessons 14–19 is a multivariable generalization of something in this lesson. If this lesson is solid, the rest of Phase 2 will feel like natural extensions rather than new territory.


