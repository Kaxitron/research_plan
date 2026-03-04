# 📝 Phase 2 Calculus Fundamentals — Entry Quiz

> **Instructions:** Work all problems by hand. No calculator. Show all reasoning — a correct answer without justification receives no credit. Give yourself **~90 minutes**.
>
> For integration problems, no method is specified — part of the task is recognising which technique applies.

---

## Question 1 — Algebraic Limits

Evaluate the following limits **without L'Hôpital's rule**.

**(a)**

$$\lim_{x \to 3} \frac{x^3 - 27}{x^2 - 9}$$

**(b)**

$$\lim_{x \to 0} \frac{\sqrt{1+x} - \sqrt{1-x}}{x}$$

---

## Question 2 — L'Hôpital's Rule

Evaluate:

**(a)**

$$\lim_{x \to \infty} \frac{3x^2 + 5x}{e^x}$$

**(b)**

$$\lim_{x \to 0^+} x \ln x$$

*(Hint for (b): rewrite as a fraction first.)*

---

## Question 3 — Continuity and the Intermediate Value Theorem

Let

$$f(x) = \begin{cases} \dfrac{x^2 - 4}{x - 2} & x \neq 2 \\ 5 & x = 2 \end{cases}$$

**(a)** Is $f$ continuous at $x = 2$? Justify with the three-part definition of continuity.

**(b)** What value would you need to assign $f(2)$ to make $f$ continuous? What is this called?

**(c)** Using the IVT, prove that the equation $x^5 - 4x + 2 = 0$ has at least one root in the interval $[0, 2]$. State explicitly what conditions you are checking.

---

## Question 4 — Mean Value Theorem

**(a)** Verify that $f(x) = x^3 - x$ satisfies the hypotheses of the MVT on $[0, 2]$, then find all values $c \in (0,2)$ guaranteed by the theorem.

**(b)** Use the MVT to prove the following inequality:

$$|\sin a - \sin b| \leq |a - b| \quad \text{for all } a, b \in \mathbb{R}$$

---

## Question 5 — Logarithmic Differentiation

Differentiate the following. Simplify your answer.

**(a)** $f(x) = x^{\sin x}$

**(b)** $g(x) = \dfrac{(x^2+1)^3 \sqrt{\cos x}}{e^x (x+4)^2}$

---

## Question 6 — Implicit Differentiation and Tangent Lines

Consider the curve defined by

$$x^3 + y^3 = 6xy$$

*(This is the Folium of Descartes.)*

**(a)** Find $\dfrac{dy}{dx}$ implicitly.

**(b)** The point $(3, 3)$ lies on this curve. Find the equation of the tangent line there.

**(c)** At what points does this curve have a **horizontal** tangent? Set up the condition (you do not need to fully solve).

---

## Question 7 — Related Rates

A conical tank (vertex down) has height $12$ m and radius $4$ m at the top. Water drains out at $2\ \text{m}^3/\text{min}$.

**(a)** Express the volume of water in terms of the water height $h$ alone.

**(b)** At the moment when $h = 3$ m, how fast is the water level dropping?

---

## Question 8 — Optimization and Newton's Method

A metal box with a **square base and no lid** must have a volume of $32\ \text{cm}^3$. The material for the base costs $\$3/\text{cm}^2$ and the sides cost $\$1/\text{cm}^2$.

**(a)** Write the total cost $C$ as a function of the base side-length $x$ alone.

**(b)** Set $C'(x) = 0$ and show this reduces to

$$6x^3 = 128$$

Solve exactly for $x$.

**(c)** Now suppose the cost structure changes so that $C'(x) = 0$ produces the transcendental equation

$$x e^x = 5$$

Starting from $x_0 = 1$, perform **two iterations** of Newton's method applied to $g(x) = xe^x - 5$. Give each iterate to four decimal places.

**(d)** Briefly: why does Newton's method converge so fast near a simple root? (One sentence using the word "quadratic.")

---

## Question 9 — Polar Coordinates

**(a)** Convert the Cartesian equation $x^2 + y^2 = 4y$ to polar form. Identify and sketch the curve.

**(b)** Convert $r = 3\cos\theta$ to Cartesian form and identify the curve.

**(c)** Find the area enclosed by one petal of the rose curve $r = \cos(2\theta)$.

*(Hint: sketch first to identify the $\theta$-interval for one petal.)*

---

## Question 10 — Integration

Evaluate:

$$\int \frac{\ln x}{x^2}\, dx$$

---

## Question 11 — Integration

Evaluate:

$$\int_0^1 x^2 \sqrt{1 - x^2}\, dx$$

---

## Question 12 — Improper Integrals

**(a)** Determine whether the following converges or diverges. If it converges, find its value.

$$\int_1^{\infty} \frac{1}{x^2 + x}\, dx$$

**(b)** Determine whether the following converges or diverges. If it converges, find its value.

$$\int_0^1 \frac{1}{\sqrt{x}}\, dx$$

---

## Question 13 — Series Convergence

For each series, determine convergence or divergence. State the test used and show it applies.

**(a)**

$$\sum_{n=1}^{\infty} \frac{n^2}{n^3 + 1}$$

**(b)**

$$\sum_{n=0}^{\infty} \frac{(-1)^n \, 3^n}{n!}$$

**(c)**

$$\sum_{n=2}^{\infty} \frac{1}{n(\ln n)^2}$$

---

## Question 14 — The Tripartite

Evaluate:

$$\int \frac{1}{x^2\sqrt{x^2 + 9}}\, dx$$

*(No hints. Part of the problem is identifying and executing the full chain of techniques.)*

---

## Question 15 — Chained Integration

Evaluate:

$$\int x^3 e^{x^2}\, dx$$

*(No hints.)*

---

*End of quiz. Check all answers before looking at the key.*
