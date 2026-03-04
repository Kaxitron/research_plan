# Lesson 13: Calculus Fundamentals — Rebuilding Your Intuition

[← LA Capstone](../phase1-linear-algebra/lesson-12-capstone.md) | [Back to TOC](../README.md) | [Next: Gradients →](lesson-14-gradients.md)

---

> **Why this lesson exists:** You haven't touched calculus in 6 years. Lessons 26–27 assume fluency with derivatives, the chain rule, integration techniques, and series. This lesson rebuilds that fluency from geometric intuition — exactly the way we approached linear algebra — so that when you hit partial derivatives and gradients, they feel like natural extensions rather than cold formulas.

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

This is called the **logarithmic derivative**. It measures the *relative* rate of change — "what fraction of itself is f changing by?" This shows up constantly in maximum likelihood estimation (Lesson 17).

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

### Limits — Making "Approaches" Precise

Everything in calculus — derivatives, integrals, series — rests on the concept of a **limit.** You've already been using limits intuitively: "shrink h toward zero" in the derivative definition, "zoom in until the curve looks linear." Now let's make it precise.

**Informal definition:** lim_{x→a} f(x) = L means "as x gets arbitrarily close to a, f(x) gets arbitrarily close to L."

**Formal ε-δ definition:** For every ε > 0 (however small a tolerance you choose for the output), there exists a δ > 0 such that whenever 0 < |x - a| < δ (input is within δ of a), we have |f(x) - L| < ε (output is within ε of L).

**The intuition:** You pick how close the output needs to be (ε). I guarantee I can find a neighborhood around a (of width δ) where the function stays within your tolerance. If I can do this for *any* ε you throw at me, the limit exists.

You won't use ε-δ proofs in ML work. But the concept matters: it's the foundation for understanding when approximations (like Taylor series, or gradient descent steps) are valid.

**One-sided limits:** lim_{x→a⁺} f(x) approaches from the right; lim_{x→a⁻} from the left. The two-sided limit exists only if both one-sided limits exist and agree. This is why ReLU has no derivative at x = 0 — the slope from the left (0) and the slope from the right (1) disagree.

### Continuity — No Jumps, No Holes, No Blowups

A function f is **continuous at a** if and only if:

$$\lim_{x \to a} f(x) = f(a)$$

This says three things at once: (1) the limit exists, (2) f(a) is defined, and (3) they're equal. Geometrically: you can draw the graph without lifting your pen.

**Why continuity matters for ML:** The Fundamental Theorem of Calculus (below) requires the integrand to be continuous. More practically, gradient descent assumes the loss function is continuous (and differentiable) — if the loss had jumps, the gradient wouldn't be defined at those points. ReLU introduces a non-differentiable point at x = 0, but it's still *continuous* there, which is enough for practical optimization.

### The Squeeze Theorem — Bounding What You Can't Compute

If g(x) ≤ f(x) ≤ h(x) near a point a, and both g(x) and h(x) approach the same limit L as x → a, then f(x) → L too. You "squeeze" the unknown function between two known ones.

**Classic example:** lim_{x→0} x² sin(1/x). The sin(1/x) part oscillates wildly near 0, so you can't just plug in. But -1 ≤ sin(1/x) ≤ 1, so -x² ≤ x² sin(1/x) ≤ x². Both bounds → 0, so the limit is 0.

**ML connection:** The squeeze theorem is the conceptual tool behind **bounding arguments** in learning theory. When you can't compute an exact quantity (like generalization error), you bound it between two computable quantities and show they converge.

### Three Foundational Theorems About Continuous Functions

These are "existence theorems" — they tell you something *exists* without telling you how to find it. They're the theoretical bedrock under all of optimization.

**Intermediate Value Theorem (IVT):** If f is continuous on [a, b] and y is any value between f(a) and f(b), then there exists some c in (a, b) where f(c) = y.

*Intuition:* A continuous function can't jump over a value. If you start below a horizontal line and end above it, you must cross it somewhere. This guarantees that equations like f(x) = 0 have solutions — which is why root-finding algorithms (bisection method, Newton's method) work.

**Extreme Value Theorem (EVT):** If f is continuous on a closed interval [a, b], then f attains its maximum and minimum somewhere on [a, b].

*Intuition:* A continuous function on a closed, bounded domain can't "escape to infinity" or approach a value without reaching it. This is why optimization on compact domains is well-behaved — the optimal solution **exists**. In ML, weight decay (L2 regularization) effectively constrains the weights to a bounded region, and the EVT guarantees the regularized loss has a minimum.

**Mean Value Theorem (MVT):** If f is continuous on [a, b] and differentiable on (a, b), then there exists some c in (a, b) where:

$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

*Intuition:* Somewhere between a and b, the instantaneous rate of change equals the average rate of change. If you drive 100 miles in 2 hours, at some point you must have been going exactly 50 mph.

*Why the MVT matters for ML:* It's the theoretical reason gradient descent makes progress. If the gradient is nonzero at a point, the MVT guarantees the function actually changes value as you move — the function can't be "stuck" at a non-critical point. The MVT also underlies convergence proofs for optimization algorithms: it connects the local information (gradient at a point) to global behavior (actual function change over a step).

---

### What Integration IS (Geometrically)

If differentiation asks "what's the slope?", integration asks "what's the area?"

**The definite integral** ∫ₐᵇ f(x) dx = the (signed) area between f(x) and the x-axis from x = a to x = b.

"Signed" means area below the x-axis counts as negative.

### Riemann Sums — Building Area from Rectangles

But how do you actually *compute* the area under a curve? Curves aren't rectangles — you can't just do length × width. The brilliant idea: **approximate** the area with rectangles, then take a limit as the rectangles get thinner.

**The setup:** Take the interval [a, b] and chop it into n equal pieces of width Δx = (b − a)/n. In each piece, build a rectangle whose height is the function value at some point in that subinterval.

**Left Riemann sum:** use the left endpoint of each subinterval for the height:

$$L_n = \sum_{i=0}^{n-1} f(x_i) \cdot \Delta x$$

**Right Riemann sum:** use the right endpoint:

$$R_n = \sum_{i=1}^{n} f(x_i) \cdot \Delta x$$

**Midpoint rule:** use the midpoint of each subinterval:

$$M_n = \sum_{i=0}^{n-1} f\!\left(\frac{x_i + x_{i+1}}{2}\right) \cdot \Delta x$$

**Trapezoidal rule:** average the left and right sums (equivalent to connecting the dots with straight lines instead of flat rectangles):

$$T_n = \frac{L_n + R_n}{2} = \sum_{i=0}^{n-1} \frac{f(x_i) + f(x_{i+1})}{2} \cdot \Delta x$$

**The key idea:** As n → ∞ (rectangles get infinitely thin), ALL of these approaches converge to the same number — the definite integral:

$$\int_a^b f(x)\, dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \cdot \Delta x$$

where $x_i^*$ is any point in the i-th subinterval. This limit IS the definition of the integral, and the fact that the choice of sample point doesn't matter (for continuous functions) is a deep consequence of continuity.

**Accuracy:** Midpoint and trapezoidal rules are more accurate than left/right for the same n. For even better accuracy, **Simpson's rule** uses parabolic arcs instead of flat tops or straight lines:

$$S_n = \frac{\Delta x}{3}\left[f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \cdots + f(x_n)\right]$$

**🔗 ML Connection:** Riemann sums are the conceptual ancestor of **numerical integration** (quadrature), which is how computers actually compute integrals. When you can't find a closed-form antiderivative (which is most of the time in ML), you approximate the integral with a finite sum. Monte Carlo integration — used heavily in Bayesian inference and reinforcement learning — is essentially a randomized Riemann sum: instead of evenly-spaced sample points, you use random samples drawn from a distribution.

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

In one dimension, f''(x) tells you curvature. In many dimensions, the matrix of all second partial derivatives — the **Hessian** — tells you curvature in every direction. You'll meet this properly in Lesson 26, but the intuition is the same: the Hessian tells you if you're at a bowl (minimum), a hill (maximum), or a saddle point. In neural networks, saddle points are far more common than local minima — this is a key insight you'll explore in Lesson 30.

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

It also appears directly in **constrained optimization** (Lesson 29): when you optimize subject to a constraint g(x, y) = 0, implicit differentiation tells you how y must change when x changes to stay on the constraint surface.

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

### L'Hôpital's Rule — Resolving 0/0 and ∞/∞

When evaluating limits, you'll often hit an **indeterminate form** — expressions like 0/0 or ∞/∞ where you can't just plug in. L'Hôpital's rule says:

$$\text{If } \lim_{x \to a} \frac{f(x)}{g(x)} \text{ gives } \frac{0}{0} \text{ or } \frac{\pm\infty}{\pm\infty}, \text{ then } \lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

**Differentiate the top and bottom separately** (this is NOT the quotient rule — you take the derivative of numerator and denominator independently), then try the limit again.

**Example 1:** lim_{x→0} sin(x)/x. Direct substitution gives 0/0. Apply L'Hôpital: lim_{x→0} cos(x)/1 = **1**.

**Example 2:** lim_{x→∞} x/eˣ. Direct substitution gives ∞/∞. Apply L'Hôpital: lim_{x→∞} 1/eˣ = **0**. Exponentials grow faster than any polynomial.

**Example 3 (apply twice):** lim_{x→∞} x²/eˣ. Gives ∞/∞. L'Hôpital: lim_{x→∞} 2x/eˣ. Still ∞/∞. Apply again: lim_{x→∞} 2/eˣ = **0**. No matter the polynomial degree, eˣ wins eventually.

**Other indeterminate forms** like 0·∞, ∞ - ∞, 0⁰, 1^∞, and ∞⁰ can be rewritten as fractions to use L'Hôpital's. For example, for 0·∞: rewrite f·g as f/(1/g) to get 0/0.

**Why this matters here:** When checking whether improper integrals converge, you often need to evaluate limits involving competing growth rates. L'Hôpital's rule is the standard tool. It also shows up when analyzing the asymptotic behavior of loss functions — for instance, understanding how cross-entropy loss behaves as predictions approach 0 or 1.

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

### Sequences — The Prerequisite for Series

Before we can add infinitely many numbers, we need to understand infinitely long *lists* of numbers.

A **sequence** is an ordered list: a₁, a₂, a₃, ... (one number for each positive integer). For example: 1, 1/2, 1/4, 1/8, ... or 1, 1/4, 1/9, 1/16, ... (which is 1/n²).

A sequence **converges** if the terms approach a specific finite number: lim_{n→∞} aₙ = L. It **diverges** if they don't (they blow up, oscillate, or otherwise fail to settle down).

**Key properties:**

A sequence is **bounded** if there's some number M where |aₙ| ≤ M for all n. The terms stay within a finite box.

A sequence is **monotone** if it's always increasing (a₁ ≤ a₂ ≤ a₃ ≤ ...) or always decreasing (a₁ ≥ a₂ ≥ a₃ ≥ ...).

**The Monotone Convergence Theorem:** If a sequence is both **bounded** and **monotone**, it converges. This is deeply intuitive — if you're always going up but can't pass a ceiling, you must settle onto some value. This theorem appears in ML convergence proofs: to show that a training algorithm converges, you often show that the loss sequence is decreasing (monotone) and bounded below (by 0), so it must converge.

**Examples:**
- aₙ = 1/n → 0. Converges. Decreasing and bounded below by 0.
- aₙ = (-1)ⁿ → oscillates between -1 and 1. Diverges (bounded but not monotone, and no single limit).
- aₙ = n² → ∞. Diverges (monotone but not bounded).
- aₙ = (1 + 1/n)ⁿ → e ≈ 2.718. Converges. This sequence *defines* e, and the convergence is non-obvious — each term is bigger than the last, but bounded above.

The distinction between sequences and series: a **sequence** is a list of numbers; a **series** is what you get when you try to *add them all up*. A series Σ aₙ converges if the sequence of **partial sums** S₁ = a₁, S₂ = a₁ + a₂, S₃ = a₁ + a₂ + a₃, ... converges.

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

**Taylor series** are the mathematical foundation of gradient descent. The first-order Taylor approximation f(x + δ) ≈ f(x) + f'(x)δ is exactly the "locally linear" model that gradient descent trusts for one step. The second-order approximation involves the Hessian and is the basis for Newton's method. You'll explore this in depth in Lesson 17.

**Power series** concepts also appear in **neural tangent kernel** theory, where the training dynamics of infinitely wide networks can be expressed as series expansions, and in **Singular Learning Theory,** where the "real log canonical threshold" involves analyzing singularities of loss functions — a topic you'll encounter toward the end of this curriculum.

---

## Part 13: Partial Fraction Decomposition — Breaking Apart Rational Functions

### The Problem

How do you integrate a fraction like this?

$$\int \frac{3x + 5}{x^2 + 3x + 2}\, dx$$

There's no u-substitution that works (the numerator isn't the derivative of the denominator), and it's not an arctan or arcsin pattern. The technique: **split the fraction into simpler pieces** that you *can* integrate.

### The Core Idea

Factor the denominator:

$$x^2 + 3x + 2 = (x + 1)(x + 2)$$

Then **assume** the fraction can be written as:

$$\frac{3x + 5}{(x + 1)(x + 2)} = \frac{A}{x + 1} + \frac{B}{x + 2}$$

for some constants A and B. Each simple fraction integrates to a logarithm — easy.

### Finding A and B

Multiply both sides by (x + 1)(x + 2):

$$3x + 5 = A(x + 2) + B(x + 1)$$

This must hold for **all** x. The fastest method: plug in values that kill one term.

**Set x = -1:** 3(-1) + 5 = A(1) + B(0) → 2 = A, so **A = 2**

**Set x = -2:** 3(-2) + 5 = A(0) + B(-1) → -1 = -B, so **B = 1**

Therefore:

$$\int \frac{3x + 5}{(x+1)(x+2)}\, dx = \int \frac{2}{x+1}\, dx + \int \frac{1}{x+2}\, dx = 2\ln|x+1| + \ln|x+2| + C$$

### When the Denominator Has a Repeated Factor

If a factor appears twice, you need separate terms for each power:

$$\frac{f(x)}{(x - a)^2(x - b)} = \frac{A}{x - a} + \frac{A_2}{(x - a)^2} + \frac{B}{x - b}$$

**Example:**

$$\frac{5x + 1}{(x-1)^2(x+2)}$$

Set up:

$$5x + 1 = A(x-1)(x+2) + A_2(x+2) + B(x-1)^2$$

**Set x = 1:** 6 = 3A₂ → **A₂ = 2**

**Set x = -2:** -9 = 9B → **B = -1**

**Set x = 0 (or any convenient value):** 1 = A(-1)(2) + 2(2) + (-1)(1) = -2A + 3 → **A = 1**

The (x-1)² term integrates to -A₂/(x-1) via a simple power rule, not a logarithm.

### When the Denominator Has an Irreducible Quadratic

If the denominator contains a quadratic that doesn't factor (like x² + 1), the numerator for that piece needs to be **Ax + B**, not just A:

$$\frac{f(x)}{(x - a)(x^2 + bx + c)} = \frac{A}{x - a} + \frac{Bx + C}{x^2 + bx + c}$$

The quadratic piece often leads to a combination of ln (from the Bx part) and arctan (from the C part, after completing the square). This is exactly the scenario that came up in ∫ 1/(1 + u³) — factoring 1 + u³ = (1 + u)(1 - u + u²) gives one linear factor and one irreducible quadratic.

### 🔗 ML Connection

Partial fractions rarely appear directly in ML computations, but the underlying skill — decomposing a complex expression into simpler pieces that are individually tractable — is a recurring theme. In Bayesian inference, breaking a complicated posterior into simpler components (mixture models, factored distributions) follows the same logic. The technique also appears in solving differential equations via Laplace transforms (Lessons 20–27), where partial fractions convert a complicated transfer function into a sum of terms you can invert individually.

---

## Part 14: Newton's Method — From First-Order to Second-Order Thinking

### The Problem Gradient Descent Can't Solve Efficiently

Imagine you want to find the root of a function — the value of x where f(x) = 0. You could try gradient descent on f(x)², but that's slow and indirect. Newton's method takes a more elegant approach: **use the tangent line as a local approximation, then jump to where the tangent line crosses zero.**

### The Geometric Picture

Stand at a point (xₙ, f(xₙ)) on the curve. Draw the tangent line there. Follow it down to where it hits the x-axis. That x-intercept becomes your next guess xₙ₊₁. Repeat.

The tangent line at xₙ has the equation:

$$y - f(x_n) = f'(x_n)(x - x_n)$$

Setting y = 0 and solving for x:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

That's it. That's Newton's method.

### Step-by-Step Example

Find √2 by solving f(x) = x² - 2 = 0.

f'(x) = 2x, so the iteration is:

$$x_{n+1} = x_n - \frac{x_n^2 - 2}{2x_n} = \frac{x_n + 2/x_n}{2}$$

Starting from x₀ = 1:

| Step | xₙ | f(xₙ) = xₙ² - 2 | Error |
|------|-----|-------------------|-------|
| 0 | 1.000000 | -1.000000 | 0.414 |
| 1 | 1.500000 | 0.250000 | 0.086 |
| 2 | 1.416667 | 0.006944 | 0.0025 |
| 3 | 1.414216 | 0.000006 | 0.0000021 |

Notice how the error *squares* at each step — from 0.086 to 0.0025 to 0.0000021. This is **quadratic convergence**: each step roughly doubles the number of correct digits. Gradient descent converges *linearly* (each step reduces error by a constant factor). Newton's method is dramatically faster.

### Why the Derivative Matters

Look at the formula again: you divide by f'(xₙ). This means:

- **When the slope is steep** (|f'| is large): you take a small step. The tangent line is nearly vertical, so it crosses zero close to where you are. Good — the linear approximation is trustworthy here.
- **When the slope is gentle** (|f'| is small): you take a huge step. The tangent line is nearly horizontal, so it crosses zero far away. Risky — you might overshoot.
- **When f'(xₙ) = 0**: the formula explodes. You're at a critical point where the tangent line is horizontal and never crosses zero. Newton's method fails here.

This is the same tension as choosing a learning rate in gradient descent, but Newton's method handles it *automatically* by using curvature information.

### Newton's Method for Optimization

To **minimize** a function g(x), you want to find where g'(x) = 0. Apply Newton's method to the function f(x) = g'(x):

$$x_{n+1} = x_n - \frac{g'(x_n)}{g''(x_n)}$$

Now the second derivative g''(x) — the curvature — appears explicitly. This is why Newton's method is called a **second-order method**: it uses both the gradient (first derivative) and the curvature (second derivative).

Compare:
- **Gradient descent:** $x_{n+1} = x_n - \alpha \cdot g'(x_n)$ — you choose α (learning rate) yourself
- **Newton's method:** $x_{n+1} = x_n - \frac{g'(x_n)}{g''(x_n)}$ — the curvature automatically sets the "right" step size

### When Newton's Method Fails

Newton's method is not foolproof:

1. **Starting too far away:** The tangent line approximation is only good locally. If your initial guess is far from the root, Newton's method can oscillate, diverge, or converge to the wrong root.

2. **Near inflection points:** When f''(x) ≈ 0 near the root, Newton's method can overshoot wildly.

3. **Multiple roots:** The method converges to whichever root is "nearest" in a complicated sense that depends on the starting point. Different starting points can lead to different roots.

### 🔗 ML & Alignment Connection

**Why this is foundational for your path:**

In multiple dimensions, Newton's method for optimization becomes:

$$w_{n+1} = w_n - H^{-1} \nabla L$$

where H is the **Hessian matrix** (all second partial derivatives) and ∇L is the gradient. This is beautiful but impractical for neural networks: if you have 1 billion weights, H is a 10⁹ × 10⁹ matrix. You can't even store it, let alone invert it.

This impossibility drives the entire field of practical optimization:

- **Adam** (the standard optimizer for LLMs) approximates second-order information by tracking running averages of the gradient and its square — a cheap proxy for curvature
- **L-BFGS** approximates the Hessian inverse using gradient history — used for smaller models
- **Natural gradient** methods use the Fisher information matrix instead of the Hessian — connects to information geometry
- **Shampoo, K-FAC** and other methods approximate the Hessian with structured matrices (Kronecker products) — an active research area

Understanding *why* these approximations exist starts with understanding Newton's method in 1D. The 1D version teaches you the payoff (quadratic convergence) and the cost (needing second-order information), and every practical optimizer is a different answer to "how do we get some of Newton's benefit without paying the full price?"

For alignment specifically: the curvature of the loss landscape around a solution tells you about **robustness**. A sharp minimum (high curvature, large g'') means the model's behavior changes rapidly with small weight perturbations — potentially fragile alignment. A broad minimum (low curvature, small g'') suggests more stable behavior. This sharp-vs-broad distinction, which you'll explore in Lesson 30, starts with understanding what the second derivative tells you about the shape of a function.

---

## Part 15: Inverse Function Derivatives — How Inverses Inherit Slopes

### The Geometric Intuition

If you have a function f and its inverse f⁻¹, their graphs are mirror images across the line y = x. This means: **wherever f has slope m, f⁻¹ has slope 1/m at the corresponding point.**

Think about it visually. If f climbs steeply (slope = 3), then f⁻¹ climbs gently (slope = 1/3) at the mirror point. The slopes are reciprocals. This is just the geometric consequence of reflecting across y = x, which swaps rise and run.

### The Formula

If y = f(x), then x = f⁻¹(y), and:

$$\frac{d}{dy}[f^{-1}(y)] = \frac{1}{f'(f^{-1}(y))}$$

Or equivalently, using Leibniz notation:

$$\frac{dx}{dy} = \frac{1}{dy/dx}$$

This is intuitive: dx/dy is literally the reciprocal of dy/dx. The rates of change are reciprocals because the roles of input and output are swapped.

### Deriving the Arctangent Derivative (Example)

Let's use the inverse function rule to derive d/dx [arctan(x)] from scratch instead of memorizing it.

Let y = arctan(x). Then by definition, x = tan(y).

Differentiate both sides with respect to x (implicit differentiation):

$$1 = \sec^2(y) \cdot \frac{dy}{dx}$$

$$\frac{dy}{dx} = \frac{1}{\sec^2(y)} = \cos^2(y)$$

Now we need this in terms of x. Since x = tan(y), draw a right triangle: opposite = x, adjacent = 1, hypotenuse = √(1 + x²).

So cos(y) = 1/√(1 + x²), and therefore cos²(y) = 1/(1 + x²).

$$\boxed{\frac{d}{dx}\arctan(x) = \frac{1}{1 + x^2}}$$

This isn't a formula you need to memorize — it's a formula you can *re-derive* in 30 seconds from the relationship between tan and arctan.

### Deriving the Arcsine Derivative

Let y = arcsin(x), so x = sin(y).

$$1 = \cos(y) \cdot \frac{dy}{dx} \quad \Rightarrow \quad \frac{dy}{dx} = \frac{1}{\cos(y)}$$

Since sin(y) = x, and cos(y) = √(1 - sin²y) = √(1 - x²):

$$\boxed{\frac{d}{dx}\arcsin(x) = \frac{1}{\sqrt{1 - x^2}}}$$

### Deriving the Natural Log Derivative

Let y = ln(x), so x = eʸ.

$$1 = e^y \cdot \frac{dy}{dx} \quad \Rightarrow \quad \frac{dy}{dx} = \frac{1}{e^y} = \frac{1}{x}$$

$$\boxed{\frac{d}{dx}\ln(x) = \frac{1}{x}}$$

This is elegant: eˣ is its own derivative, and because the inverse function rule takes the reciprocal, ln(x) inherits a derivative of 1/x. The "special" property of eˣ propagates to its inverse.

### The General Pattern

Notice what's happening in all three examples:
1. Write y = f⁻¹(x), so x = f(y)
2. Differentiate implicitly: 1 = f'(y) · dy/dx
3. Solve: dy/dx = 1/f'(y)
4. Re-express in terms of x using the original relationship

This is really just implicit differentiation in disguise. The "inverse function derivative formula" is not a new rule — it's a consequence of the chain rule and implicit differentiation that you already know.

### 🔗 ML & Alignment Connection

**Change of variables in probability — the 1D Jacobian:**

This is where inverse function derivatives become essential for your path. Suppose X is a random variable with known density pₓ(x), and you transform it through an invertible function: Y = g(X). What's the density of Y?

The answer uses the inverse function derivative:

$$p_Y(y) = p_X(g^{-1}(y)) \cdot \left|\frac{d}{dy}g^{-1}(y)\right|$$

That absolute derivative term — |d/dy g⁻¹(y)| — is the **1D Jacobian**. It accounts for how the function g stretches or compresses the probability density. If g stretches a region (|g'| > 1), the density thins out. If g compresses a region (|g'| < 1), the density concentrates. The Jacobian ensures the total probability stays at 1.

**Example:** If X ~ Uniform(0, 1) and Y = X², then g(x) = x², g⁻¹(y) = √y, and d/dy[√y] = 1/(2√y). So:

$$p_Y(y) = 1 \cdot \frac{1}{2\sqrt{y}} = \frac{1}{2\sqrt{y}} \quad \text{for } 0 < y < 1$$

This is a valid density — it integrates to 1, and it tells you Y is concentrated near 0 (squaring uniform numbers pushes them toward zero).

In multiple dimensions, this 1D derivative becomes the **Jacobian determinant** — which you already know is connected to how matrices scale volumes. This is the mathematical foundation of **normalizing flows**, a generative model architecture where simple distributions (Gaussian noise) are pushed through layers of invertible transformations, each with a tractable Jacobian determinant, to produce complex distributions (realistic images, text, etc.). You'll encounter the multivariable version in Lesson 14 (Gradients and Jacobians), and it will feel like a direct extension of what you've just learned.

---

## Part 16: Polar Coordinates — A Different Way to Describe Position

### Why Another Coordinate System?

Cartesian coordinates (x, y) describe a point by its horizontal and vertical distances from the origin. But some shapes are awkward in Cartesian coordinates. A circle of radius 3 centered at the origin requires the equation x² + y² = 9 — a relationship between *two* variables. In polar coordinates, the same circle is simply r = 3 — just one variable.

**Polar coordinates** describe a point by:
- **r** = the distance from the origin (always ≥ 0)
- **θ** (theta) = the angle measured counterclockwise from the positive x-axis

### The Conversion Formulas

$$x = r\cos\theta \qquad y = r\sin\theta$$

$$r = \sqrt{x^2 + y^2} \qquad \theta = \arctan\left(\frac{y}{x}\right)$$

These follow directly from the right triangle formed by the point, the origin, and the point's projection onto the x-axis. You've seen these relationships before — they're just trigonometry.

**Key identity:** $x^2 + y^2 = r^2$ — this is the Pythagorean theorem, and it's why circles are simple in polar coordinates.

### Polar Curves — Thinking in (r, θ)

In polar coordinates, a curve is defined by r = f(θ). As θ sweeps from 0 to 2π, the radius r changes according to the function, tracing out a curve.

**Examples:**
- **r = a** → circle of radius a (constant distance from origin)
- **r = θ** → spiral (distance grows with angle, called the Archimedean spiral)
- **r = cos(2θ)** → four-petaled rose (the radius oscillates, creating lobes)
- **r = 1 + cos(θ)** → cardioid (heart-shaped curve)

### Area in Polar Coordinates

In Cartesian coordinates, we chop the region into thin vertical rectangles. In polar coordinates, we chop it into thin **pie slices** (sectors).

A thin sector at angle θ with radius r and angular width dθ has area:

$$dA = \frac{1}{2} r^2 \, d\theta$$

This is because a sector of a circle with radius r and angle dθ has area (1/2)r²dθ (a fraction dθ/(2π) of the full circle area πr²).

So the total area enclosed by r = f(θ) from θ = α to θ = β is:

$$A = \frac{1}{2} \int_\alpha^\beta [f(\theta)]^2 \, d\theta$$

### The Jacobian: Why dA = r dr dθ (Not Just dr dθ)

This is the critical part for your ML path. When you change from Cartesian to polar in a double integral:

$$\iint f(x, y) \, dx \, dy = \iint f(r\cos\theta, \, r\sin\theta) \cdot r \, dr \, d\theta$$

That extra factor of **r** is the **Jacobian determinant** of the coordinate transformation. Here's why it appears:

A tiny Cartesian box dx × dy has area dx · dy. But a tiny polar "box" (a thin wedge between r and r + dr, and between θ and θ + dθ) has area approximately r · dr · dθ, not dr · dθ. The wedge is wider when r is larger — further from the origin, the same angle dθ sweeps out a larger arc. The factor of r corrects for this stretching.

Formally, the Jacobian of the transformation (r, θ) → (x, y) is:

$$J = \det \begin{bmatrix} \partial x/\partial r & \partial x/\partial \theta \\ \partial y/\partial r & \partial y/\partial \theta \end{bmatrix} = \det \begin{bmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{bmatrix} = r\cos^2\theta + r\sin^2\theta = r$$

This is the determinant from your linear algebra knowledge — it measures how much the transformation stretches area at each point. The connection: **the determinant scales areas** (Lesson 6 in linear algebra) and **the Jacobian determinant scales area elements in coordinate changes** (what you're seeing here). Same concept, different setting.

### The Gaussian Integral — The Payoff

Now you can prove the most important result in all of probability. We want to show:

$$I = \int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}$$

**The trick:** Square the integral.

$$I^2 = \left(\int_{-\infty}^{\infty} e^{-x^2} \, dx\right)\left(\int_{-\infty}^{\infty} e^{-y^2} \, dy\right) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} e^{-(x^2 + y^2)} \, dx \, dy$$

Now convert to polar coordinates. Since x² + y² = r²:

$$I^2 = \int_0^{2\pi} \int_0^{\infty} e^{-r^2} \cdot r \, dr \, d\theta$$

The θ integral is trivial: ∫₀²π dθ = 2π.

The r integral is a u-substitution: let u = r², du = 2r dr:

$$\int_0^{\infty} r \, e^{-r^2} \, dr = \frac{1}{2}\int_0^{\infty} e^{-u} \, du = \frac{1}{2}[-e^{-u}]_0^{\infty} = \frac{1}{2}$$

So:

$$I^2 = 2\pi \cdot \frac{1}{2} = \pi$$

$$\boxed{I = \sqrt{\pi}}$$

The magic: the r factor from the Jacobian (r dr dθ) combines with the e^(-r²) integrand to create r·e^(-r²), which is a simple u-substitution. Without polar coordinates — without the Jacobian factor of r — this integral is impossible to evaluate with elementary techniques.

**The Gaussian normalization constant:** The standard normal distribution has density:

$$p(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$$

The 1/√(2π) factor is there precisely because ∫ e^(-x²/2) dx = √(2π) (substitute u = x/√2 in our result). Every time you see √(2π) in a Gaussian formula, you're looking at a shadow of the Gaussian integral.

### 🔗 ML & Alignment Connection

**Why polar coordinates matter for your path:**

The Gaussian integral proof isn't just beautiful mathematics — it's the foundation of the normal distribution, which is the most important distribution in all of statistics and ML. Every time a paper says "assume Gaussian noise," "Gaussian prior," "reparameterization trick," or "variational inference with diagonal Gaussian," the mathematical validity ultimately traces back to this integral and the normalizing constant it provides.

The Jacobian factor connects directly to your existing knowledge: in linear algebra, the determinant scales areas under linear transformations. The Jacobian generalizes this to nonlinear transformations. In Lesson 14 (Gradients and Jacobians), you'll see this generalize further to arbitrary coordinate changes in high-dimensional spaces. And in normalizing flows (a generative model architecture), the entire model is designed so that the Jacobian determinant is easy to compute — because computing it is necessary for evaluating the probability of generated outputs.

The broader principle: **choosing the right coordinate system can transform an impossible problem into a simple one.** Polar coordinates turn the Gaussian integral from intractable to trivial. In ML, choosing the right parameterization of a model, the right basis for representing features, or the right coordinate system for optimization can make the same dramatic difference. This is the same insight as change of basis in linear algebra — it doesn't change the underlying reality, only how easy it is to work with.

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

### Supplementary

- **Professor Leonard — Calculus 2 playlist**
  - https://www.youtube.com/playlist?list=PLDesaqWTN6ESPaHy2QUKVaXNZuQNxkYQ_
  - Lecture-style walkthroughs of integration by parts, trig substitution, and series if you want extra worked examples

---

## 📖 Read

- **MML Book, Chapter 5.1–5.3** — Differentiation of univariate functions, partial differentiation basics
  - https://mml-book.github.io/
  - Focus on: derivative rules, chain rule, and Taylor series (5.1–5.3 before moving to 5.4+ in Lesson 26)

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

### Drill Set 9: Newton's Method

1. Use Newton's method to find √5 by solving x² - 5 = 0. Start at x₀ = 2. Compute x₁, x₂, x₃. How many correct decimal places does x₃ have?
2. Use Newton's method to find the root of f(x) = x³ - 2x - 5 near x = 2. Compute two iterations.
3. Apply Newton's method for optimization: minimize g(x) = x⁴ - 4x² + 2 starting from x₀ = 3. Write the iteration formula (using g'/g'') and compute x₁ and x₂. Does it approach a local minimum?
4. **Failure mode:** Try Newton's method on f(x) = x³ - x starting from x₀ = 1/√3. What happens? Why? ← (Hint: what is f'(1/√3)?)

### Drill Set 10: Inverse Function Derivatives

1. Derive d/dx [arccos(x)] using the inverse function method. ← (Start from x = cos(y), differentiate implicitly)
2. Derive d/dx [arcsin(x)] from scratch using the inverse function method. Verify it matches the table.
3. If f(x) = x³ + x (which is strictly increasing, hence invertible), find (f⁻¹)'(2). ← (Hint: f(1) = 2, so f⁻¹(2) = 1. Use the formula.)
4. **Change of variables practice:** Let X ~ Uniform(0, 1) and Y = -ln(X). Find the density of Y using the change-of-variables formula with the inverse function derivative. What named distribution is this?

### Drill Set 11: Polar Coordinates

1. Convert the point (x, y) = (-1, √3) to polar coordinates (r, θ).
2. Convert r = 2cos(θ) to Cartesian form. What shape is this? ← (Hint: multiply both sides by r)
3. Find the area enclosed by one petal of r = cos(2θ). ← (One petal goes from θ = -π/4 to θ = π/4)
4. **The Gaussian integral:** Verify the key step by computing ∫₀^∞ r·e^(-r²) dr using u-substitution with u = r². Confirm you get 1/2.

---

## ✅ Self-Assessment: Am I Ready for Lesson 26?

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
- [ ] Apply Newton's method to find roots and explain why it converges quadratically
- [ ] Explain the difference between first-order (gradient descent) and second-order (Newton's) optimization
- [ ] Derive inverse trig derivatives (arcsin, arctan) using implicit differentiation
- [ ] Apply the 1D change-of-variables formula for probability densities
- [ ] Convert between Cartesian and polar coordinates
- [ ] Explain why the Jacobian factor r appears in polar double integrals
- [ ] Reproduce the Gaussian integral proof using polar coordinates

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

Every concept in Lessons 26–19 is a multivariable generalization of something in this lesson. If this lesson is solid, the rest of Phase 2 will feel like natural extensions rather than new territory.



