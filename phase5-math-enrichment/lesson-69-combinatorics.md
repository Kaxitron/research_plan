# Lesson 69: Combinatorics — Counting with Purpose

[← Sets & Functions](lesson-68-sets-functions-relations.md) | [Back to TOC](../README.md) | [Next: Graph Theory →](lesson-70-graph-theory.md)

---

> **Why this lesson exists:** Counting is not just arithmetic — it is the foundation of probability, information theory, and computational complexity, all of which are central to AI alignment. When we ask "how many possible reward functions are there?", "how large is the hypothesis space?", or "can we enumerate all dangerous inputs?", we are doing combinatorics. PAC learning bounds depend on counting the effective size of hypothesis classes. The combinatorial explosion of possible plans, states, or strategies is what makes alignment hard in practice. This lesson equips you with the tools to count precisely and to recognize when counting reveals fundamental limits.

> **Estimated time:** 12–18 hours

---

## Part 1: Fundamental Counting Principles

### The Sum Rule (Rule of Addition)

If a task can be done in one of n1 ways OR in one of n2 ways, and these ways are mutually exclusive (no overlap), then the task can be done in n1 + n2 ways.

**Example:** A model can be a transformer (5 architecture variants) or an RNN (3 architecture variants). There are 5 + 3 = 8 choices total.

The sum rule generalizes: if there are k mutually exclusive categories with n1, n2, ..., nk options respectively, the total is n1 + n2 + ... + nk. When the categories are NOT mutually exclusive, you need the inclusion-exclusion principle (covered below).

### The Product Rule (Rule of Multiplication)

If a task consists of a sequence of steps — step 1 can be done in n1 ways, step 2 in n2 ways (regardless of step 1's choice), and so on — then the entire sequence can be done in n1 * n2 * ... * nk ways.

**Example:** Designing a neural network requires choosing an activation function (3 options), a number of layers (5 options), and an optimizer (4 options). Total configurations: 3 * 5 * 4 = 60.

**The combinatorial explosion:** This multiplication is why AI systems face such enormous search spaces. A model with 10 hyperparameters, each with 5 possible values, has 5^10 = 9,765,625 configurations. A model with 100 binary decisions has 2^100 configurations, roughly 10^30 — more than the number of grains of sand on Earth. This exponential growth from the product rule is the fundamental reason that brute-force search is intractable for most AI problems, and why we need smart search strategies (gradient descent, tree search, etc.).

### Subtraction Principle (Complementary Counting)

Sometimes it is easier to count what you do NOT want and subtract from the total.

|desired outcomes| = |total outcomes| - |undesired outcomes|

**Example:** How many 4-digit PINs (0000–9999) have at least one repeated digit? Total PINs: 10^4 = 10,000. PINs with NO repeats: 10 * 9 * 8 * 7 = 5,040. PINs with at least one repeat: 10,000 - 5,040 = 4,960.

---

## Part 2: Permutations and Combinations

### Permutations

A **permutation** is an arrangement of objects where **order matters**.

**Permutations of n distinct objects:** n! = n * (n-1) * (n-2) * ... * 2 * 1

**Permutations of r objects chosen from n:** P(n, r) = n! / (n-r)!

*Intuition:* You have n choices for the first position, n-1 for the second (one object is used), n-2 for the third, and so on, until you have filled r positions.

**Example:** In how many ways can you arrange 3 books from a shelf of 10? P(10, 3) = 10 * 9 * 8 = 720.

### Combinations

A **combination** is a selection of objects where **order does not matter**.

**Combinations of r objects from n:** C(n, r) = n! / (r! * (n-r)!)

Also written as "n choose r." The factor of r! in the denominator removes the overcounting from permutations: the r! arrangements of the same r objects are all considered the same selection.

**Example:** Choosing a committee of 3 from 10 people: C(10, 3) = 10! / (3! * 7!) = 120.

**Key identity:** C(n, r) = C(n, n-r). Choosing r objects to include is the same as choosing n-r objects to exclude. This symmetry is not just a computational convenience — it reveals a deep duality in counting.

### When to Use Which

The critical question is always: **does order matter?**

- Assigning people to specific ranked positions (1st place, 2nd place, ...): **permutation**
- Choosing a subset with no ranking: **combination**
- Arranging letters in a word: **permutation**
- Choosing ingredients for a recipe: **combination**

In ML: choosing which 5 features to include in a model (out of 20) is a combination problem: C(20, 5) = 15,504. Ranking those 5 features by importance would be a permutation problem: P(20, 5) = 1,860,480.

---

## Part 3: The Binomial Theorem and Beyond

### The Binomial Theorem

For any non-negative integer n:

(x + y)^n = sum from k=0 to n of C(n, k) * x^(n-k) * y^k

The binomial coefficients C(n, k) tell you how many ways to choose which k factors contribute a y (and the remaining n-k contribute an x).

**Example:** (x + y)^3 = x^3 + 3x^2y + 3xy^2 + y^3

The coefficients 1, 3, 3, 1 are the third row of **Pascal's Triangle**, which encodes the identity C(n, k) = C(n-1, k-1) + C(n-1, k). Each entry is the sum of the two entries above it. This recurrence is the combinatorial fact that choosing k items from n either includes the n-th item (C(n-1, k-1) ways) or excludes it (C(n-1, k) ways).

### Multinomial Coefficients

The generalization: (x1 + x2 + ... + xm)^n expands with coefficients n! / (k1! * k2! * ... * km!) where k1 + k2 + ... + km = n.

**Practical use:** The number of ways to arrange a word with repeated letters. "MISSISSIPPI" has 11 letters: 1 M, 4 I's, 4 S's, 2 P's. The number of distinct arrangements is 11! / (1! * 4! * 4! * 2!) = 34,650.

### Connection to AI: Hypothesis Space Size

In PAC (Probably Approximately Correct) learning theory, a central quantity is the size of the hypothesis class H. For a binary classifier on n binary features, the hypothesis class of ALL possible classifiers has |H| = 2^(2^n) (each of the 2^n inputs can be mapped to 0 or 1). This double-exponential growth means that without structural assumptions (inductive bias), learning is hopeless — you cannot generalize from a feasible number of examples. The binomial coefficient appears when you restrict hypotheses: the number of classifiers that classify exactly k of the 2^n inputs as positive is C(2^n, k).

---

## Part 4: The Pigeonhole Principle

### Statement

If you place more than n objects into n containers, at least one container must hold more than one object.

More generally: if you place kn + 1 objects into n containers, at least one container holds at least k + 1 objects.

### Why It Matters

The pigeonhole principle is deceptively simple but produces powerful non-constructive existence proofs — it tells you something must exist without telling you how to find it.

**Example:** In any group of 367 people, at least two share a birthday (since there are at most 366 days in a year).

**Example:** If you compress n-bit strings into (n-1)-bit strings, at least two original strings must map to the same compressed string. This means lossless compression cannot shorten *every* input — a fundamental limit in information theory.

**ML connection:** The pigeonhole principle explains why hash collisions are inevitable, why dimensionality reduction must lose some information, and why neural networks with fewer parameters than data points cannot memorize every training example perfectly (in general).

---

## Part 5: Inclusion-Exclusion Principle

### Two Sets

|A union B| = |A| + |B| - |A intersect B|

We subtract the intersection because it was counted twice — once in |A| and once in |B|.

### Three Sets

|A union B union C| = |A| + |B| + |C| - |A intersect B| - |A intersect C| - |B intersect C| + |A intersect B intersect C|

### General Form

For n sets A1, A2, ..., An:

|A1 union ... union An| = (sum of individual sizes) - (sum of pairwise intersections) + (sum of triple intersections) - ... + (-1)^(n+1) |A1 intersect ... intersect An|

The signs alternate: add, subtract, add, subtract...

### Application: Derangements

A **derangement** is a permutation where no element stays in its original position. How many derangements of {1, 2, ..., n} exist?

Let Ai = {permutations where element i stays in place}. We want |A1 union ... union An|^c — the number of permutations NOT in any Ai.

By inclusion-exclusion and complementary counting:

D(n) = n! * sum from k=0 to n of (-1)^k / k!

This approaches n!/e as n grows (where e is Euler's number). Remarkably, the probability that a random permutation is a derangement approaches 1/e for large n.

---

## Part 6: Stars and Bars

### The Problem

How many ways can you distribute n identical objects into k distinct containers?

Equivalently: how many solutions are there to x1 + x2 + ... + xk = n where each xi is a non-negative integer?

### The Answer

C(n + k - 1, k - 1)

**Intuition:** Imagine n stars (objects) in a row, and you place k-1 bars among them to divide them into k groups. The number of ways to place the bars among the n + k - 1 total positions is C(n + k - 1, k - 1).

**Example:** Distributing 5 identical tokens among 3 people: C(5 + 3 - 1, 3 - 1) = C(7, 2) = 21.

**With lower bounds:** If each container must have at least 1 object, substitute yi = xi - 1 (so yi >= 0) and solve y1 + ... + yk = n - k. Answer: C(n - 1, k - 1).

---

## Part 7: Combinatorial Proofs

### What Is a Combinatorial Proof?

A **combinatorial proof** establishes an identity by showing that both sides count the same thing in different ways. This is also called a **double counting** argument.

**Example:** Prove that C(n, k) = C(n, n-k).

*Combinatorial proof:* The left side counts the number of ways to choose k items from n. The right side counts the number of ways to choose n-k items from n. But choosing k items to include is exactly the same as choosing n-k items to exclude. Both sides count the same thing.

**Example:** Prove that the sum from k=0 to n of C(n, k) = 2^n.

*Combinatorial proof:* The right side counts the number of subsets of an n-element set (each element is in or out: 2^n choices). The left side counts the same thing by categorizing subsets by size: C(n, 0) subsets of size 0, plus C(n, 1) subsets of size 1, etc.

Combinatorial proofs are often more elegant and illuminating than algebraic proofs. They reveal *why* an identity is true, not just *that* it is true.

---

## Watch — Primary

1. **Trefor Bazzett — "Discrete Math" playlist (counting sections)**
   - *Covers the sum and product rules, permutations, combinations, the binomial theorem, pigeonhole principle, and inclusion-exclusion with worked examples*

## Watch — Supplementary

1. **TrevTutor — "Discrete Math 1" playlist (combinatorics videos)**
   - *Additional worked problems and explanations, particularly strong on stars and bars and combinatorial proofs*

## Read — Primary

- **"Discrete Mathematics and Its Applications" by Kenneth Rosen** — Chapters 6 and 8
  - *Chapter 6 covers counting fundamentals; Chapter 8 covers advanced counting (inclusion-exclusion, generating functions preview). Excellent exercises.*

## Read — Supplementary

- **"A Walk Through Combinatorics" by Miklos Bona** — Chapters 1–5
  - *A gentler and more story-driven introduction to combinatorics, with many beautiful examples.*

## Exercises

1. A password consists of 3 uppercase letters followed by 4 digits. How many possible passwords are there? How many if no character can repeat?

2. A committee of 5 is to be formed from 8 men and 6 women. How many committees are possible with (a) no restrictions, (b) exactly 2 women, (c) at least 1 woman?

3. Expand (2x - 3y)^4 using the binomial theorem.

4. How many distinct arrangements of the letters in "ALIGNMENT" are there?

5. Prove that C(n, 0) + C(n, 1) + ... + C(n, n) = 2^n using (a) the binomial theorem and (b) a combinatorial proof.

6. A class has 45 students. Prove that at least 4 of them were born in the same month.

7. Use inclusion-exclusion to count the number of integers from 1 to 1000 that are divisible by 3, 5, or 7.

8. How many ways can you distribute 10 identical cookies among 4 children if (a) there are no restrictions, (b) each child gets at least 1 cookie, (c) no child gets more than 4 cookies?

9. Give a combinatorial proof that C(2n, 2) = 2 * C(n, 2) + n^2. (Hint: split a set of 2n elements into two groups of n.)

10. (Challenge) Suppose a neural network's input is a binary vector of length 20. The model outputs a binary classification. How many possible input-output functions exist? If you could only evaluate the model on 100 randomly chosen inputs, use a counting argument to explain why you cannot distinguish all possible functions. Relate this to the need for inductive bias in machine learning.
