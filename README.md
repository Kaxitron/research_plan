# The Path to AI Alignment

## A Complete Self-Study Curriculum: Mathematics → Neural Networks → Alignment

---

**Goal:** Develop deep intuitive understanding of the mathematics underlying neural networks, the architecture and philosophy of modern AI systems, and the tools of mechanistic interpretability — all in service of solving AI alignment.


**Estimated total time:** ~160–215 hours over 4–6 months at a steady pace.

> 📊 **NEW: [Interactive Curriculum Dashboard](https://kaxitron.github.io/research_plan/curriculum-dashboard.html)** — Visual dependency map, time estimates, concept checks, failure mode warnings, and project tracker in one navigable interface. Open this alongside your studies.

---

## Quick Navigation

| I want to... | Go to |
|---|---|
| See the visual dependency map | [Curriculum Dashboard](curriculum-dashboard.html) → Dependency Map |
| Check estimated time for a lesson | [Curriculum Dashboard](curriculum-dashboard.html) → Timeline view |
| See what I should build and when | [Curriculum Dashboard](curriculum-dashboard.html) → Project Tracker |
| Learn how to read ML papers | [Reading Papers Guide](resources/reading-papers.md) |
| Find a specific video | [Video Series Index](resources/video-index.md) |
| Find a book or textbook | [Books & Textbooks](resources/books.md) |

---

## Table of Contents

### [PHASE 1: Linear Algebra Foundations](phase1-linear-algebra/) · ~32–47h
*The language that transformers speak*

| # | Lesson | Est. Time | Status |
|---|--------|-----------|--------|
| 1 | [Vectors — What They Actually Are](phase1-linear-algebra/lesson-01-vectors.md) | 2–3h | ✅ Complete |
| 2 | [Linear Combinations, Span, and Basis](phase1-linear-algebra/lesson-02-span-basis.md) | 3–4h | ✅ Complete |
| 3 | [Linear Transformations and Matrices](phase1-linear-algebra/lesson-03-transformations.md) | 3–5h | ✅ Complete |
| 4 | [Matrix Operations Deep Dive](phase1-linear-algebra/lesson-04-matrix-operations.md) | 3–4h | ✅ Complete |
| 5 | [Rank, Null Space, and Column Space](phase1-linear-algebra/lesson-05-rank-nullspace.md) | 4–5h | ✅ Complete |
| 6 | [The Determinant](phase1-linear-algebra/lesson-06-determinant.md) | 2–3h | ✅ Complete |
| 7 | [Eigenvalues and Eigenvectors](phase1-linear-algebra/lesson-07-eigenvalues.md) | 4–6h | ✅ Complete |
| 8 | [Singular Value Decomposition (SVD)](phase1-linear-algebra/lesson-08-svd.md) | 5–7h | 🔄 In Progress |
| 9 | [Dot Products, Orthogonality, and Projections](phase1-linear-algebra/lesson-09-dot-products.md) | 4–6h | ⬜ Not Started |
| 10 | [Change of Basis, Norms, and Special Matrices](phase1-linear-algebra/lesson-10-change-of-basis.md) | 4–5h | ⬜ Not Started |
| 11 | [Linear Algebra Capstone](phase1-linear-algebra/lesson-11-capstone.md) | 4–6h | ⬜ Not Started |
| — | *✎ Phase 1 Review: LA → ML Bridge* | 2–3h | ⬜ |

### [PHASE 2: Calculus for ML](phase2-calculus/) · ~19–27h
*The mathematical engine of neural network learning*

| # | Lesson | Est. Time | Status |
|---|--------|-----------|--------|
| 12 | [Matrix Calculus — Bridging to Backpropagation](phase2-calculus/lesson-12-matrix-calculus.md) | 3–5h | ⬜ Not Started |
| 13 | [Partial Derivatives and Gradients — Going Deeper](phase2-calculus/lesson-13-gradients.md) | 3–4h | ⬜ Not Started |
| 14 | [The Chain Rule — This IS Backpropagation](phase2-calculus/lesson-14-chain-rule.md) | 4–6h | ⬜ Not Started |
| 15 | [Optimization and Gradient Descent](phase2-calculus/lesson-15-optimization.md) | 6–8h | ⬜ Not Started |
| 16 | [Loss Landscapes and Local Minima](phase2-calculus/lesson-16-loss-landscapes.md) | 3–4h | ⬜ Not Started |
| — | *✎ Phase 2 Review: Calculus → Training Bridge* | 2–3h | ⬜ |

### [PHASE 3: Probability, Information Theory, and Bayesian Thinking](phase3-probability/) · ~19–27h
*The language of uncertainty and learning*

| # | Lesson | Est. Time | Status |
|---|--------|-----------|--------|
| 17 | [Probability Distributions and Bayes' Theorem](phase3-probability/lesson-17-probability.md) | 4–5h | ⬜ Not Started |
| 18 | [Expectation, Variance, and Covariance](phase3-probability/lesson-18-expectation.md) | 3–5h | ⬜ Not Started |
| 19 | [Maximum Likelihood Estimation](phase3-probability/lesson-19-mle.md) | 3–4h | ⬜ Not Started |
| 20 | [Information Theory — Entropy, KL Divergence, Cross-Entropy](phase3-probability/lesson-20-information-theory.md) | 4–6h | ⬜ Not Started |
| 21 | [Bayesian Reasoning and Inference](phase3-probability/lesson-21-bayesian-inference.md) | 5–7h | ⬜ Not Started |
| — | *✎ Phase 3 Review: Probability → LLM Training Bridge* | 2–3h | ⬜ |

### [PHASE 4: Neural Networks — From Neurons to Transformers](phase4-neural-networks/) · ~30–42h
*Building the machine, piece by piece*

| # | Lesson | Est. Time | Status |
|---|--------|-----------|--------|
| 22 | [How a Single Neuron Works](phase4-neural-networks/lesson-22-single-neuron.md) | 3–4h | ⬜ Not Started |
| 23 | [The Forward Pass as Matrix Multiplications](phase4-neural-networks/lesson-23-forward-pass.md) | 6–8h | ⬜ Not Started |
| 24 | [Backpropagation Through the Full Network](phase4-neural-networks/lesson-24-backprop.md) | 6–8h | ⬜ Not Started |
| 25 | [Attention — Dot Products in Action](phase4-neural-networks/lesson-25-attention.md) | 5–7h | ⬜ Not Started |
| 26 | [Building a Transformer from Scratch](phase4-neural-networks/lesson-26-transformer.md) | 10–15h | ⬜ Not Started |
| — | *✎ Phase 4 Review: Everything → Transformer Bridge* | 3–4h | ⬜ |

> 📖 **Start reading papers here.** See the [Reading Papers Guide](resources/reading-papers.md).

### [PHASE 5: Mechanistic Interpretability](phase5-interpretability/) · ~14–20h
*Using everything you've learned to open the black box*

| # | Lesson | Est. Time | Status |
|---|--------|-----------|--------|
| 27 | [What Interpretability Researchers Actually Do](phase5-interpretability/lesson-27-intro-interp.md) | 6–8h | ⬜ Not Started |
| 28 | [Circuits and Features in Practice](phase5-interpretability/lesson-28-circuits.md) | 8–12h | ⬜ Not Started |
| — | *✎ Phase 5 Review: Interp → Alignment Bridge* | 2–3h | ⬜ |

### [PHASE 6: Alignment Theory and Foundations](phase6-alignment-theory/) · ~25–35h
*The philosophical and strategic landscape*

| # | Lesson | Est. Time | Status |
|---|--------|-----------|--------|
| 29 | [Game Theory Foundations](phase6-alignment-theory/lesson-29-game-theory.md) | 6–8h | ⬜ Not Started |
| 30 | [Decision Theory — CDT, EDT, and FDT](phase6-alignment-theory/lesson-30-decision-theory.md) | 5–7h | ⬜ Not Started |
| 31 | [Anthropics and Self-Locating Beliefs](phase6-alignment-theory/lesson-31-anthropics.md) | 4–6h | ⬜ Not Started |
| 32 | [The Alignment Problem — Technical Foundations](phase6-alignment-theory/lesson-32-alignment-problem.md) | 6–8h | ⬜ Not Started |
| 33 | [Open Problems and Research Frontiers](phase6-alignment-theory/lesson-33-open-problems.md) | 4–6h | ⬜ Not Started |
| — | *✎ Phase 6 Review: Full Integration* | 3–4h | ⬜ |

### [PHASE 7: Independent Research](phase7-research/)

| # | Lesson | Status |
|---|--------|--------|
| — | [Your First Research Project](phase7-research/research-guide.md) | ⬜ Not Started |

### [Resource Index](resources/)

| Resource | Link |
|----------|------|
| [📊 Interactive Curriculum Dashboard](curriculum-dashboard.html) | **Dependency map, time estimates, concept checks, failure warnings** |
| [📖 How to Read ML Papers](resources/reading-papers.md) | **Three-pass method, paper anatomy, reading queue** |
| [Linear Algebra Textbook Rankings](resources/textbook-rankings.md) | Comparison of all LA resources |
| [Video Series Index](resources/video-index.md) | 3B1B, Karpathy, Strang, Brunton |
| [Books & Textbooks](resources/books.md) | All free online resources |
| [Essential Blogs](resources/blogs.md) | colah, Neel Nanda, Jay Alammar, etc. |
| [Key Papers](resources/papers.md) | Reading list in order |
| [Courses & Programs](resources/courses.md) | MIT OCW, ARENA, Stanford, etc. |
| [Practice Problem Sources](resources/practice-problems.md) | MIT OCW, Khan Academy, Axler, Paul's Notes |

---

## How to Use This Plan

Each lesson block contains:

- **🎯 Core learning** — what we'll work through together in our sessions
- **📺 Watch** — videos organized as Primary → Secondary
- **📖 Read** — supplementary reading, similarly layered
- **🔨 Do** — hands-on exercises and coding projects
- **🔗 ML Connection** — why this matters for alignment work
- **🧠 Alignment Connection** — direct ties to alignment research

### The Minimum Viable Lesson

Every lesson has a **Minimum Viable Lesson (MVL)** — the absolute smallest set of resources that covers the core concept — visible in the [Dashboard](curriculum-dashboard.html). When time is tight, do the MVL. When you have time, go deeper with secondary resources.

**When to go deeper:** If the concept check questions in the Dashboard feel shaky, add secondary resources. If they feel solid, move on.

### Phase Review Checkpoints

After each phase, complete the **Review Checkpoint** exercises (visible in the sidebar of the Dashboard). These integration exercises force you to connect concepts across multiple lessons and phases — this is where the real learning happens.

### Recommended Learning Stack Per Concept

```
3Blue1Brown video (geometric intuition)
    ↓
MIT OCW / Strang lecture (deeper understanding, formal framework)
    ↓
MML Book chapter (ML-focused notation)
    ↓
Interactive Linear Algebra / Immersive Math (play with it)
    ↓
Exercises & Python code (make it stick)
    ↓
ML connection discussion (why it matters)
```

You don't need ALL resources for every concept. Use 3B1B as your primary and add others where you want more depth.

### Self-Assessment

For each lesson, the Dashboard includes:

- **Concept Check Questions** — Can you answer these without looking anything up? If yes, you've learned it. If not, revisit.
- **Common Failure Modes** — Known pitfalls that trip up learners. Read these BEFORE starting the lesson so you know what to watch for.

---

*This plan is a living document. As you progress, we'll adjust pacing, add resources, and dive deeper into areas that resonate. The goal isn't to memorize procedures — it's to build the geometric intuition that lets you "see" what a matrix does the way you "see" what addition does.*
