# Lesson 71: Recurrences and Generating Functions — Sequences, Structure, and Closed Forms

[← Graph Theory](lesson-70-graph-theory.md) | [Back to TOC](../README.md) | [Next: Finite Automata →](lesson-72-finite-automata.md)

---

> **Why this lesson exists:** Recurrence relations describe processes that build on their own past — and that is exactly what happens in recurrent neural networks, dynamic programming algorithms, and iterative training procedures. Generating functions transform recurrences into algebra, letting you extract closed-form solutions and asymptotic behavior. For alignment research, understanding recurrences is essential for analyzing how errors accumulate over time in sequential decision-making, how recursive self-improvement dynamics behave, and how the computational cost of safety checks scales with model complexity.

> **Estimated time:** 15–20 hours

---

## Part 1: Recurrence Relations

### What Is a Recurrence?

A **recurrence relation** defines a sequence where each term is expressed in terms of previous terms. You also need **initial conditions** to pin down a specific sequence.

**Example — Fibonacci numbers:**
- F(0) = 0, F(1) = 1
- F(n) = F(n-1) + F(n-2) for n >= 2

This produces: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

A recurrence is a "recipe" for building the sequence one step at a time. But computing the n-th term by following the recipe takes time proportional to n (or worse, exponential time for the naive recursive Fibonacci). A **closed-form solution** gives you the n-th term directly, without computing all previous terms.

### Linear Homogeneous Recurrences with Constant Coefficients

These have the form:

a(n) = c1 * a(n-1) + c2 * a(n-2) + ... + ck * a(n-k)

where c1, ..., ck are constants and ck != 0. The "homogeneous" means there is no additional term that depends on n (no extra "+f(n)" on the right side).

**The Characteristic Equation Method:**

The key insight is to guess that a(n) = r^n for some constant r. Substituting into the recurrence:

r^n = c1 * r^(n-1) + c2 * r^(n-2) + ... + ck * r^(n-k)

Dividing both sides by r^(n-k):

r^k = c1 * r^(k-1) + c2 * r^(k-2) + ... + ck

This is the **characteristic equation**, a polynomial equation in r.

**Case 1: k distinct roots r1, r2, ..., rk.**
The general solution is:

a(n) = A1 * r1^n + A2 * r2^n + ... + Ak * rk^n

where A1, ..., Ak are constants determined by the initial conditions.

**Case 2: A repeated root r with multiplicity m.**
For a root r of multiplicity m, the contribution to the general solution is:

(B1 + B2*n + B3*n^2 + ... + Bm*n^(m-1)) * r^n

The powers of n "break the degeneracy" from the repeated root.

### Solving the Fibonacci Recurrence

The Fibonacci recurrence F(n) = F(n-1) + F(n-2) has characteristic equation:

r^2 = r + 1, i.e., r^2 - r - 1 = 0

The roots are: r = (1 + sqrt(5))/2 (the golden ratio, phi) and r = (1 - sqrt(5))/2 (call it psi).

General solution: F(n) = A * phi^n + B * psi^n.

Using initial conditions F(0) = 0 and F(1) = 1:
- F(0) = 0: A + B = 0, so B = -A
- F(1) = 1: A*phi + B*psi = 1, so A*(phi - psi) = 1, so A = 1/sqrt(5)

The closed form (Binet's formula):

F(n) = (phi^n - psi^n) / sqrt(5)

This is remarkable: the Fibonacci numbers, which are integers defined by adding integers, have a closed form involving irrational numbers (sqrt(5)) and irrational bases (phi). Yet the irrational parts cancel perfectly to always give an integer.

Since |psi| < 1, the term psi^n shrinks to zero, so F(n) is approximately phi^n / sqrt(5) for large n. The Fibonacci numbers grow exponentially at rate phi (about 1.618).

### Non-Homogeneous Recurrences

These have the form:

a(n) = c1 * a(n-1) + ... + ck * a(n-k) + f(n)

where f(n) is some function of n (not involving a).

**Solution strategy:** The general solution is:

a(n) = (general solution to the homogeneous part) + (a particular solution)

Finding the particular solution depends on the form of f(n):
- If f(n) is a polynomial of degree d, try a polynomial of degree d.
- If f(n) = C * s^n, try a(n) = D * s^n (unless s is a root of the characteristic equation; then multiply by n^m where m is the multiplicity).
- If f(n) is a sum of such terms, use superposition (try the sum of the corresponding particular solutions).

**Example:** a(n) = 2*a(n-1) + 3^n with a(0) = 1.

Homogeneous solution: a_h(n) = A * 2^n.
Particular solution: try a_p(n) = D * 3^n. Substituting: D * 3^n = 2D * 3^(n-1) + 3^n. So D * 3 = 2D + 3 (dividing by 3^(n-1)). So 3D - 2D = 3, giving D = 3. Thus a_p(n) = 3 * 3^n = 3^(n+1).

General solution: a(n) = A * 2^n + 3^(n+1). Using a(0) = 1: A + 3 = 1, so A = -2.

Final answer: a(n) = -2 * 2^n + 3^(n+1) = 3^(n+1) - 2^(n+1).

### Connection to AI: Analyzing Recursive Algorithms and RNN Dynamics

Every recursive algorithm has a running time described by a recurrence. Merge sort: T(n) = 2T(n/2) + O(n). Binary search: T(n) = T(n/2) + O(1). Solving these recurrences tells you the algorithm's complexity.

In recurrent neural networks, the hidden state evolves by a recurrence: h(t) = f(W_h * h(t-1) + W_x * x(t)). While nonlinear (so the characteristic equation method does not directly apply), the *linearized* dynamics around a fixed point are governed by a linear recurrence whose characteristic roots determine stability. If any root has magnitude greater than 1, gradients explode; if all roots have magnitude less than 1, gradients vanish. This is the mathematical heart of the vanishing/exploding gradient problem in RNNs.

---

## Part 2: Generating Functions

### The Big Idea

A **generating function** encodes an entire sequence into a single algebraic object. Instead of working with the sequence a(0), a(1), a(2), ... term by term, you work with:

A(x) = a(0) + a(1)*x + a(2)*x^2 + a(3)*x^3 + ...

This is a **formal power series** — you treat it as an algebraic object and do not worry about convergence (though convergence is a bonus when it happens).

Why is this useful? Because operations on generating functions correspond to operations on sequences:

| Sequence operation | Generating function operation |
|---|---|
| Shift: b(n) = a(n+1) | (A(x) - a(0)) / x |
| Multiply by n: b(n) = n*a(n) | x * A'(x) |
| Prefix sum: b(n) = a(0) + a(1) + ... + a(n) | A(x) / (1 - x) |
| Convolution: c(n) = sum a(k)*b(n-k) | C(x) = A(x) * B(x) |

The last row is the most powerful: **multiplication of generating functions corresponds to convolution of sequences**. This transforms recurrences into algebraic equations that you can solve with standard algebra.

### Ordinary Generating Functions (OGF)

The **ordinary generating function** of a sequence {a(n)} is:

A(x) = sum from n=0 to infinity of a(n) * x^n

**Fundamental example:** The sequence 1, 1, 1, 1, ... has OGF:

1 + x + x^2 + x^3 + ... = 1 / (1 - x)

This is the geometric series. It converges for |x| < 1, but as a formal power series, we use it algebraically regardless.

**More examples:**
- Sequence 1, r, r^2, r^3, ... has OGF 1/(1 - rx)
- Sequence 1, 0, 1, 0, 1, 0, ... has OGF 1/(1 - x^2)
- Sequence 0, 1, 2, 3, 4, ... has OGF x/(1 - x)^2 (differentiate 1/(1-x) and multiply by x)

### Solving Recurrences with Generating Functions

**Example: Fibonacci via generating functions.**

Start with F(n) = F(n-1) + F(n-2), F(0) = 0, F(1) = 1.

Let G(x) = sum F(n) * x^n. Multiply both sides of the recurrence by x^n and sum from n = 2 to infinity:

sum F(n)*x^n = sum F(n-1)*x^n + sum F(n-2)*x^n

The left side is G(x) - F(0) - F(1)*x = G(x) - x.

The first term on the right: x * sum F(n-1)*x^(n-1) = x*(G(x) - F(0)) = x*G(x).

The second term: x^2 * sum F(n-2)*x^(n-2) = x^2 * G(x).

So: G(x) - x = x*G(x) + x^2*G(x).

Solving: G(x) * (1 - x - x^2) = x, so G(x) = x / (1 - x - x^2).

To extract coefficients, use partial fractions. Factor the denominator: 1 - x - x^2 = -(x^2 + x - 1) = -(x - (-1+sqrt(5))/2)(x - (-1-sqrt(5))/2).

After partial fraction decomposition and expanding each fraction as a geometric series, you recover Binet's formula: F(n) = (phi^n - psi^n) / sqrt(5).

The generating function approach is more systematic than guessing the form of the solution. You mechanically convert the recurrence to an algebraic equation, solve for G(x), then extract coefficients.

### Operations on Generating Functions

**Addition:** If A(x) generates {a(n)} and B(x) generates {b(n)}, then A(x) + B(x) generates {a(n) + b(n)}.

**Scalar multiplication:** c * A(x) generates {c * a(n)}.

**Multiplication (Cauchy product):** A(x) * B(x) generates {c(n)} where c(n) = sum from k=0 to n of a(k) * b(n-k).

This is convolution. When you multiply two generating functions, you get the generating function of their convolution. This is the same convolution that appears in signal processing, probability (convolution of distributions gives the distribution of a sum), and convolutional neural networks (in a discrete, finite-dimensional sense).

**Differentiation:** A'(x) generates {(n+1) * a(n+1)}.

**Integration:** The integral of A(x) generates {a(n-1)/n} for n >= 1 (with constant term 0).

### Coefficient Extraction

The notation [x^n] A(x) means "the coefficient of x^n in A(x)" — i.e., a(n).

**Useful closed forms for extraction:**

- [x^n] 1/(1-x) = 1 for all n >= 0
- [x^n] 1/(1-x)^k = C(n+k-1, k-1) (the stars-and-bars formula from combinatorics!)
- [x^n] x/(1-x-x^2) = F(n) (Fibonacci)

The connection to stars and bars is beautiful: the generating function 1/(1-x)^k = (1 + x + x^2 + ...)^k. The coefficient of x^n counts the number of ways to write n as an ordered sum of k non-negative integers — exactly the stars-and-bars count.

---

## Part 3: Exponential Generating Functions

### Definition

The **exponential generating function (EGF)** of a sequence {a(n)} is:

E(x) = sum from n=0 to infinity of a(n) * x^n / n!

EGFs are natural for counting **labeled** structures (where the objects have distinct identities), just as OGFs are natural for **unlabeled** structures.

**Key example:** The sequence a(n) = 1 for all n has EGF:

sum x^n / n! = e^x

The EGF of the constant sequence 1 is the exponential function. This is why it is called the "exponential" generating function.

### Multiplication of EGFs

If A(x) is the EGF for {a(n)} and B(x) is the EGF for {b(n)}, then A(x) * B(x) is the EGF for:

c(n) = sum from k=0 to n of C(n, k) * a(k) * b(n-k)

The binomial coefficient C(n, k) appears because EGF multiplication corresponds to "choosing which labels go to which part" — a labeled partition operation.

### Application: Counting Permutations and Derangements

The EGF for the number of permutations of n objects is:

sum n! * x^n / n! = sum x^n = 1/(1-x)

The EGF for derangements D(n) is:

e^(-x) / (1-x)

This follows from inclusion-exclusion and the EGF framework, and it encodes the formula D(n) = n! * sum from k=0 to n of (-1)^k / k! that we derived combinatorially in the previous lesson.

---

## Part 4: The Catalan Numbers

### Definition and Recurrence

The **Catalan numbers** C_0, C_1, C_2, ... are defined by:

C_0 = 1, C(n+1) = sum from k=0 to n of C(k) * C(n-k)

The first few values: 1, 1, 2, 5, 14, 42, 132, 429, ...

### What Do They Count?

The Catalan numbers count a remarkable variety of structures:

- The number of ways to properly parenthesize n+1 factors: ((ab)(cd)) vs (a((bc)d)) vs ...
- The number of paths from (0,0) to (n,n) on a grid that stay below or on the diagonal (Dyck paths)
- The number of full binary trees with n+1 leaves
- The number of triangulations of a convex polygon with n+2 sides
- The number of non-crossing partitions of {1, 2, ..., n}

### Generating Function Solution

Let G(x) = sum C(n) * x^n. The recurrence C(n+1) = sum C(k)*C(n-k) is a convolution, so:

(G(x) - 1)/x = G(x)^2

(We shift by dividing out C_0 and x.) This gives:

G(x) = x*G(x)^2 + 1, i.e., x*G(x)^2 - G(x) + 1 = 0.

By the quadratic formula:

G(x) = (1 - sqrt(1 - 4x)) / (2x)

(We choose the minus sign to get G(0) = C_0 = 1.)

Using the generalized binomial theorem to expand sqrt(1 - 4x), we extract:

C(n) = C(2n, n) / (n+1)

This is the closed form for the Catalan numbers. For large n, Stirling's approximation gives C(n) ~ 4^n / (n^(3/2) * sqrt(pi)).

### ML Connection

The Catalan numbers count the number of binary tree structures with n leaves. In the context of recursive neural networks or parsing, the number of possible tree structures grows as a Catalan number — exponential in n but with a polynomial correction. This combinatorial growth constrains how tree-structured models process sequential data.

---

## Part 5: Asymptotic Analysis of Recurrences

### The Master Theorem (Brief Overview)

For divide-and-conquer recurrences of the form T(n) = a*T(n/b) + O(n^d):

- If d > log_b(a): T(n) = O(n^d)
- If d = log_b(a): T(n) = O(n^d * log n)
- If d < log_b(a): T(n) = O(n^(log_b(a)))

**Examples:**
- Merge sort: T(n) = 2T(n/2) + O(n). Here a=2, b=2, d=1, log_2(2)=1, so d = log_b(a): T(n) = O(n log n).
- Binary search: T(n) = T(n/2) + O(1). Here a=1, b=2, d=0, log_2(1)=0, so d = log_b(a): T(n) = O(log n).
- Strassen's matrix multiplication: T(n) = 7T(n/2) + O(n^2). Here a=7, b=2, d=2, log_2(7) ~ 2.81, so d < log_b(a): T(n) = O(n^2.81).

### Asymptotic Extraction from Generating Functions

For generating functions with a closed form, asymptotic behavior of coefficients is determined by the **singularity closest to the origin**.

If G(x) = P(x)/Q(x) is a rational function, the roots of Q(x) closest to zero determine the exponential growth rate. If the smallest root (in absolute value) is at x = 1/r, then [x^n] G(x) grows like C * r^n for some constant C.

For the Fibonacci generating function G(x) = x/(1-x-x^2), the roots of 1-x-x^2 = 0 are at x = 1/phi and x = 1/psi. Since 1/phi < 1/|psi|, the dominant singularity gives F(n) ~ phi^n / sqrt(5).

This technique — reading off asymptotics from singularities — is a cornerstone of **analytic combinatorics**, developed extensively by Flajolet and Sedgewick.

---

## Watch — Primary

1. **Trefor Bazzett — "Discrete Math" playlist (recurrence and generating function sections)**
   - *Covers solving recurrences with the characteristic equation, introduction to generating functions, and worked examples*

## Watch — Supplementary

1. **TrevTutor — "Discrete Math 2" playlist (generating functions deep dive)**
   - *More advanced treatment of generating function operations, coefficient extraction, and applications to counting problems*

## Read — Primary

- **"Discrete Mathematics and Its Applications" by Kenneth Rosen** — Chapter 8
  - *Covers recurrence relations, the characteristic equation method, and generating functions at an introductory level.*

- **"Generatingfunctionology" by Herbert Wilf** — Chapters 1–2
  - *Freely available online. The classic treatment of generating functions, written with clarity and humor. Chapter 1 alone is worth the investment.*

## Read — Supplementary

- **"Analytic Combinatorics" by Philippe Flajolet and Robert Sedgewick** — Chapter 1
  - *The definitive reference on extracting asymptotics from generating functions. Freely available online. Advanced but extraordinarily rewarding.*

## Exercises

1. Solve the recurrence a(n) = 5a(n-1) - 6a(n-2) with a(0) = 1, a(1) = 4. (Find the characteristic roots, write the general solution, apply initial conditions.)

2. Solve the recurrence a(n) = 4a(n-1) - 4a(n-2) with a(0) = 1, a(1) = 3. (Note the repeated root.)

3. Solve the non-homogeneous recurrence a(n) = 2a(n-1) + 3 with a(0) = 1.

4. Find the ordinary generating function for the sequence 1, 3, 5, 7, 9, ... (odd positive integers) in closed form.

5. Use generating functions to solve the recurrence a(n) = 3a(n-1) - 2a(n-2) with a(0) = 0, a(1) = 1. Verify by computing the first 5 terms both from the recurrence and from your closed form.

6. Verify that [x^n] 1/(1-x)^3 = C(n+2, 2) = (n+1)(n+2)/2 for n = 0, 1, 2, 3.

7. Use the generating function for Catalan numbers to compute C_5. Verify by listing the 14 Dyck paths from (0,0) to (4,4) (or equivalently, all properly parenthesized products of 5 factors).

8. Apply the Master Theorem to determine the asymptotic complexity of:
   - T(n) = 4T(n/2) + n
   - T(n) = 4T(n/2) + n^2
   - T(n) = 4T(n/2) + n^3

9. Consider an RNN with linear dynamics h(t) = A*h(t-1) where A is a 2x2 matrix. Write the characteristic equation for the recurrence governing each component of h(t). Under what conditions on A do solutions grow, shrink, or oscillate?

10. (Challenge) The number of binary strings of length n with no two consecutive 1s satisfies a(n) = a(n-1) + a(n-2) with a(1) = 2, a(2) = 3. Solve this recurrence using generating functions. Show that a(n) = F(n+2) where F is the Fibonacci sequence. Discuss why this is equivalent to counting independent sets in a path graph of length n.
