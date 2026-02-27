# Lesson 2: Vectors — What They Actually Are

[← Back to Table of Contents](../README.md) | [Next: Linear Combinations, Span, and Basis →](lesson-03-span-basis.md)

---

## 🎯 Core Concepts

- A vector is an arrow in space (geometric view) AND a list of numbers (computational view) — both are true simultaneously
- Addition: tip-to-tail composition. Scaling: stretching/shrinking
- Coordinates are just instructions: "walk 3 along x, then 2 along y"
- **The key insight:** coordinates only mean something *relative to a basis*. Change the basis, change the numbers — but the arrow stays the same

## 📺 Watch — Primary

1. **3Blue1Brown — "Vectors, what even are they?" (Ch. 1)**
   - https://www.youtube.com/watch?v=fNk_zzaMoSs
   - *Watch this first. Grant's dual view (physicist arrow vs. CS list vs. mathematician abstract) is the perfect foundation. Pay special attention to the idea that coordinates are basis-dependent.*

## 📺 Watch — Secondary

2. **Khan Academy — "Introduction to Vectors"** (as review/practice)
   - Good for extra worked examples if 3B1B moves too fast on any point
3. **Maththebeautiful (Pavel Grinfeld) — "What is a Vector?"**
   - https://www.youtube.com/watch?v=iVZGsGlmEPk
   - A more formal treatment that emphasizes the abstract definition

## 📖 Read

- **MML Book (Deisenroth et al.), Chapter 2.1–2.4** — https://mml-book.github.io/
  - Formal definitions with consistent notation you'll see in ML papers
  - *Read after watching 3B1B so the notation has geometric meaning*
- **Interactive Linear Algebra (Margalit & Rabinoff)** — https://textbooks.math.gatech.edu/ila/
  - Free Georgia Tech textbook with embedded interactive visualizations

## 🔨 Do

- Plot 2D vectors in Python with matplotlib — draw addition and scalar multiplication geometrically
- **Key exercise:** Given v = [3, 1], draw v, 2v, -v, and v + [1, 2] as arrows. Verify the geometry matches the arithmetic.

## 🔗 ML Connection

In a transformer, every token gets converted to an **embedding vector** — a point in ~768-dimensional space. The word "king" is literally a vector. The word "queen" is another vector. The famous relationship king − man + woman ≈ queen is *vector arithmetic* in embedding space. You're learning the operations that make this possible.

## 🧠 Alignment Connection

When mechanistic interpretability researchers talk about "directions in activation space that correspond to concepts," they mean specific vectors. A "truthfulness direction" or a "toxicity direction" is a vector. Understanding what vectors are — geometrically, not just as lists of numbers — is what lets you reason about whether a model's internal representations are aligned with human concepts.
