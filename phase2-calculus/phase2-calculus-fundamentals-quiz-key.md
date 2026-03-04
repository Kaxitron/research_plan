# 📝 Phase 2 Calculus Fundamentals — Entry Quiz: Answer Key

> Attempt all problems before reading this. Answers without shown work don't count.

---

## Q1 — Algebraic Limits

**(a)**

$$\lim_{x \to 3} \frac{x^3 - 27}{x^2 - 9}$$

Factor: $x^3 - 27 = (x-3)(x^2+3x+9)$, $x^2 - 9 = (x-3)(x+3)$

$$= \lim_{x \to 3} \frac{x^2 + 3x + 9}{x + 3} = \frac{9 + 9 + 9}{6} = \boxed{\frac{9}{2}}$$

**(b)**

$$\lim_{x \to 0} \frac{\sqrt{1+x} - \sqrt{1-x}}{x}$$

Multiply by conjugate $\dfrac{\sqrt{1+x}+\sqrt{1-x}}{\sqrt{1+x}+\sqrt{1-x}}$:

$$= \lim_{x \to 0} \frac{(1+x)-(1-x)}{x(\sqrt{1+x}+\sqrt{1-x})} = \lim_{x \to 0} \frac{2x}{x(\sqrt{1+x}+\sqrt{1-x})} = \frac{2}{1+1} = \boxed{1}$$

---

## Q2 — L'Hôpital's Rule

**(a)**

$$\lim_{x \to \infty} \frac{3x^2 + 5x}{e^x}$$

Apply L'Hôpital twice (both times $\infty/\infty$):

$$\to \lim \frac{6x + 5}{e^x} \to \lim \frac{6}{e^x} = \boxed{0}$$

*Polynomials always lose to exponentials.*

**(b)**

$$\lim_{x \to 0^+} x \ln x = \lim_{x \to 0^+} \frac{\ln x}{1/x} \quad \left(\frac{-\infty}{\infty}\right)$$

L'Hôpital: $\dfrac{1/x}{-1/x^2} = \dfrac{-x^2}{x} = -x \to \boxed{0}$

---

## Q3 — Continuity and IVT

**(a)** The three conditions for continuity at $x=2$:

1. $f(2) = 5$ ✓ (defined)
2. $\displaystyle\lim_{x\to 2} f(x) = \lim_{x\to 2} \frac{(x-2)(x+2)}{x-2} = \lim_{x\to 2}(x+2) = 4$ ✓ (limit exists)
3. $f(2) = 5 \neq 4 = \lim_{x\to 2} f(x)$ ✗

**Not continuous** at $x = 2$.

**(b)** Setting $f(2) = 4$ would make $f$ continuous. This is called a **removable discontinuity**.

**(c)** Let $g(x) = x^5 - 4x + 2$. Since $g$ is a polynomial, it is continuous everywhere.

- $g(0) = 2 > 0$
- $g(2) = 32 - 8 + 2 = 26 > 0$

These don't straddle zero! Try a smaller value: $g(1) = 1 - 4 + 2 = -1 < 0$.

So on $[0,1]$: $g(0) = 2 > 0$ and $g(1) = -1 < 0$. Since $g$ is continuous and changes sign, by the IVT there exists $c \in (0,1) \subset [0,2]$ with $g(c) = 0$. $\blacksquare$

---

## Q4 — Mean Value Theorem

**(a)** $f(x) = x^3 - x$ is a polynomial, so continuous on $[0,2]$ and differentiable on $(0,2)$ — hypotheses satisfied.

$$\frac{f(2)-f(0)}{2-0} = \frac{6-0}{2} = 3$$

Set $f'(c) = 3c^2 - 1 = 3$, so $c^2 = \frac{4}{3}$, giving $c = \frac{2}{\sqrt{3}} \approx 1.155 \in (0,2)$. ✓

**(b)** Let $h(x) = \sin x$. Then $h'(x) = \cos x$, and $|h'(x)| = |\cos x| \leq 1$ for all $x$.

By the MVT, for any $a \neq b$ there exists $c$ between them such that:

$$\frac{\sin a - \sin b}{a - b} = \cos c$$

Taking absolute values:

$$\frac{|\sin a - \sin b|}{|a - b|} = |\cos c| \leq 1$$

Therefore $|\sin a - \sin b| \leq |a - b|$. $\blacksquare$

---

## Q5 — Logarithmic Differentiation

**(a)** Let $y = x^{\sin x}$. Take $\ln$:

$$\ln y = \sin x \cdot \ln x$$

Differentiate both sides:

$$\frac{y'}{y} = \cos x \cdot \ln x + \sin x \cdot \frac{1}{x}$$

$$\boxed{f'(x) = x^{\sin x}\!\left(\cos x \ln x + \frac{\sin x}{x}\right)}$$

**(b)** Let $y = \dfrac{(x^2+1)^3 \sqrt{\cos x}}{e^x (x+4)^2}$. Take $\ln$:

$$\ln y = 3\ln(x^2+1) + \tfrac{1}{2}\ln(\cos x) - x - 2\ln(x+4)$$

Differentiate:

$$\frac{y'}{y} = \frac{6x}{x^2+1} - \frac{\tan x}{2} - 1 - \frac{2}{x+4}$$

$$\boxed{g'(x) = \frac{(x^2+1)^3\sqrt{\cos x}}{e^x(x+4)^2}\left(\frac{6x}{x^2+1} - \frac{\tan x}{2} - 1 - \frac{2}{x+4}\right)}$$

---

## Q6 — Implicit Differentiation: Folium of Descartes

$x^3 + y^3 = 6xy$

**(a)** Differentiate both sides:

$$3x^2 + 3y^2\frac{dy}{dx} = 6y + 6x\frac{dy}{dx}$$

$$\frac{dy}{dx}(3y^2 - 6x) = 6y - 3x^2$$

$$\boxed{\frac{dy}{dx} = \frac{2y - x^2}{y^2 - 2x}}$$

**(b)** At $(3,3)$: $\dfrac{dy}{dx} = \dfrac{6-9}{9-6} = \dfrac{-3}{3} = -1$

Tangent line: $y - 3 = -1(x-3)$, so $\boxed{y = -x + 6}$

**(c)** Horizontal tangent when $dy/dx = 0$, i.e., numerator $= 0$:

$$2y - x^2 = 0 \implies y = \frac{x^2}{2}$$

Substitute back into $x^3 + y^3 = 6xy$ and simplify to find the exact points.

---

## Q7 — Related Rates: Conical Tank

**(a)** The cone has full dimensions $H=12$, $R=4$, giving ratio $r/h = 4/12 = 1/3$, so $r = h/3$.

$$V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi \left(\frac{h}{3}\right)^2 h = \frac{\pi h^3}{27}$$

**(b)** Differentiate with respect to $t$:

$$\frac{dV}{dt} = \frac{\pi h^2}{9}\frac{dh}{dt}$$

Given $dV/dt = -2$ (draining) and $h = 3$:

$$-2 = \frac{\pi (9)}{9}\frac{dh}{dt} = \pi \frac{dh}{dt}$$

$$\boxed{\frac{dh}{dt} = -\frac{2}{\pi} \approx -0.637\ \text{m/min}}$$

---

## Q8 — Optimization and Newton's Method

**(a)** Let $x$ = side of square base, $h$ = height. Volume: $x^2 h = 32$, so $h = 32/x^2$.

- Base cost: $3x^2$
- Four sides, each area $xh$: $4 \cdot 1 \cdot xh = 4x \cdot \frac{32}{x^2} = \frac{128}{x}$

$$\boxed{C(x) = 3x^2 + \frac{128}{x}}$$

**(b)**

$$C'(x) = 6x - \frac{128}{x^2} = 0 \implies 6x^3 = 128 \implies x^3 = \frac{64}{3} \implies \boxed{x = \frac{4}{3^{1/3}} = 4 \cdot 3^{-1/3}\ \text{cm}}$$

**(c)** $g(x) = xe^x - 5$, $g'(x) = e^x + xe^x = (1+x)e^x$. Newton: $x_{n+1} = x_n - \dfrac{x_n e^{x_n} - 5}{(1+x_n)e^{x_n}}$

- $x_0 = 1$: $g(1) = e - 5 \approx -2.2817$, $g'(1) = 2e \approx 5.4366$

$$x_1 = 1 - \frac{-2.2817}{5.4366} \approx \boxed{1.4197}$$

- $x_1 = 1.4197$: $g(1.4197) = 1.4197 \cdot e^{1.4197} - 5 \approx 5.835 - 5 = 0.835$, $g'(1.4197) = 2.4197 \cdot e^{1.4197} \approx 9.955$

$$x_2 = 1.4197 - \frac{0.835}{9.955} \approx \boxed{1.3357}$$

*(True answer is $\approx 1.3267$; one more iteration would nail it.)*

**(d)** Newton's method converges **quadratically** near a simple root: the number of correct decimal digits roughly doubles each step, because the error satisfies $|e_{n+1}| \leq M|e_n|^2$ for some constant $M$.

---

## Q9 — Polar Coordinates

**(a)** $x^2 + y^2 = 4y$. Since $x^2 + y^2 = r^2$ and $y = r\sin\theta$:

$$r^2 = 4r\sin\theta \implies \boxed{r = 4\sin\theta}$$

This is a **circle of radius 2 centred at $(0,2)$**.

**(b)** $r = 3\cos\theta$. Multiply both sides by $r$:

$$r^2 = 3r\cos\theta \implies x^2 + y^2 = 3x \implies \left(x - \frac{3}{2}\right)^2 + y^2 = \frac{9}{4}$$

A **circle of radius $\frac{3}{2}$ centred at $\left(\frac{3}{2}, 0\right)$**.

**(c)** $r = \cos(2\theta)$. One petal exists where $r \geq 0$; starting from $\theta = -\pi/4$ to $\theta = \pi/4$:

$$A = \frac{1}{2}\int_{-\pi/4}^{\pi/4} \cos^2(2\theta)\,d\theta = \frac{1}{2}\int_{-\pi/4}^{\pi/4} \frac{1+\cos(4\theta)}{2}\,d\theta$$

$$= \frac{1}{4}\left[\theta + \frac{\sin(4\theta)}{4}\right]_{-\pi/4}^{\pi/4} = \frac{1}{4}\cdot\frac{\pi}{2} = \boxed{\frac{\pi}{8}}$$

---

## Q10 — Integration

$$\int \frac{\ln x}{x^2}\,dx$$

**Method: Integration by parts.** Let $u = \ln x$, $dv = x^{-2}dx$, so $du = \frac{1}{x}dx$, $v = -\frac{1}{x}$.

$$= -\frac{\ln x}{x} - \int\left(-\frac{1}{x}\right)\frac{1}{x}\,dx = -\frac{\ln x}{x} + \int x^{-2}\,dx = -\frac{\ln x}{x} - \frac{1}{x} + C$$

$$\boxed{= -\frac{\ln x + 1}{x} + C}$$

---

## Q11 — Integration

$$\int_0^1 x^2\sqrt{1-x^2}\,dx$$

**Method: Trig substitution.** Let $x = \sin\theta$, $dx = \cos\theta\,d\theta$, $\sqrt{1-x^2} = \cos\theta$.

Limits: $x=0 \to \theta=0$; $x=1 \to \theta=\pi/2$.

$$= \int_0^{\pi/2} \sin^2\theta \cdot \cos\theta \cdot \cos\theta\,d\theta = \int_0^{\pi/2}\sin^2\theta\cos^2\theta\,d\theta$$

Use double-angle identities: $\sin^2\theta\cos^2\theta = \frac{1}{4}\sin^2(2\theta) = \frac{1}{8}(1-\cos(4\theta))$

$$= \frac{1}{8}\left[\theta - \frac{\sin(4\theta)}{4}\right]_0^{\pi/2} = \frac{1}{8}\cdot\frac{\pi}{2} = \boxed{\frac{\pi}{16}}$$

---

## Q12 — Improper Integrals

**(a)**

$$\int_1^{\infty} \frac{1}{x^2+x}\,dx = \int_1^{\infty}\frac{1}{x(x+1)}\,dx$$

Partial fractions: $\dfrac{1}{x(x+1)} = \dfrac{1}{x} - \dfrac{1}{x+1}$

$$= \lim_{b\to\infty}\left[\ln x - \ln(x+1)\right]_1^b = \lim_{b\to\infty}\ln\frac{b}{b+1} - \ln\frac{1}{2} = \ln(1) + \ln 2 = \boxed{\ln 2}$$

**Converges.**

**(b)**

$$\int_0^1 \frac{1}{\sqrt{x}}\,dx = \lim_{\varepsilon\to 0^+}\int_\varepsilon^1 x^{-1/2}\,dx = \lim_{\varepsilon\to 0^+}\left[2\sqrt{x}\right]_\varepsilon^1 = 2 - 0 = \boxed{2}$$

**Converges.**

---

## Q13 — Series Convergence

**(a)**

$$\sum_{n=1}^{\infty}\frac{n^2}{n^3+1}$$

For large $n$, $\dfrac{n^2}{n^3+1} \sim \dfrac{1}{n}$. **Limit comparison** with $\sum \frac{1}{n}$:

$$\lim_{n\to\infty}\frac{n^2/(n^3+1)}{1/n} = \lim_{n\to\infty}\frac{n^3}{n^3+1} = 1 \in (0,\infty)$$

Since $\sum\frac{1}{n}$ diverges, this series **diverges**.

**(b)**

$$\sum_{n=0}^{\infty}\frac{(-1)^n 3^n}{n!}$$

**Ratio test:** $\left|\dfrac{a_{n+1}}{a_n}\right| = \dfrac{3}{n+1} \to 0 < 1$.

**Converges absolutely.** (In fact, the sum equals $e^{-3}$.)

**(c)**

$$\sum_{n=2}^{\infty}\frac{1}{n(\ln n)^2}$$

**Integral test.** Let $f(x) = \frac{1}{x(\ln x)^2}$, continuous, positive, decreasing for $x \geq 2$.

$$\int_2^\infty \frac{dx}{x(\ln x)^2}$$

Let $u = \ln x$, $du = dx/x$:

$$= \int_{\ln 2}^{\infty} u^{-2}\,du = \left[-\frac{1}{u}\right]_{\ln 2}^\infty = \frac{1}{\ln 2} < \infty$$

**Converges.**

---

## Q14 — The Tripartite

$$\int \frac{dx}{x^2\sqrt{x^2+9}}$$

**Step 1 — Trig substitution.** The $\sqrt{x^2+9}$ form calls for $x = 3\tan\theta$, $dx = 3\sec^2\theta\,d\theta$, $\sqrt{x^2+9} = 3\sec\theta$.

$$= \int\frac{3\sec^2\theta\,d\theta}{9\tan^2\theta \cdot 3\sec\theta} = \frac{1}{9}\int\frac{\sec\theta}{\tan^2\theta}\,d\theta = \frac{1}{9}\int\frac{\cos\theta}{\sin^2\theta}\,d\theta$$

**Step 2 — u-substitution.** Let $u = \sin\theta$, $du = \cos\theta\,d\theta$:

$$= \frac{1}{9}\int u^{-2}\,du = -\frac{1}{9u} + C = -\frac{1}{9\sin\theta} + C$$

**Step 3 — Convert back.** From $x = 3\tan\theta$: draw a reference triangle with opposite $= x$, adjacent $= 3$, hypotenuse $= \sqrt{x^2+9}$. So $\sin\theta = \dfrac{x}{\sqrt{x^2+9}}$.

$$\boxed{\int\frac{dx}{x^2\sqrt{x^2+9}} = -\frac{\sqrt{x^2+9}}{9x} + C}$$

*(Check: differentiate the answer to verify.)*

---

## Q15 — Chained Integration

$$\int x^3 e^{x^2}\,dx$$

**Step 1 — u-substitution.** Let $u = x^2$, $du = 2x\,dx$, so $x\,dx = du/2$. Also $x^3\,dx = x^2 \cdot x\,dx = u\cdot\frac{du}{2}$.

$$= \frac{1}{2}\int u e^u\,du$$

**Step 2 — Integration by parts.** Let $p = u$, $dq = e^u\,du$, so $dp = du$, $q = e^u$.

$$= \frac{1}{2}\left(ue^u - \int e^u\,du\right) = \frac{1}{2}(ue^u - e^u) + C = \frac{e^u}{2}(u-1) + C$$

**Step 3 — Back-substitute** $u = x^2$:

$$\boxed{\int x^3 e^{x^2}\,dx = \frac{e^{x^2}}{2}(x^2-1) + C}$$

---

*End of answer key.*
