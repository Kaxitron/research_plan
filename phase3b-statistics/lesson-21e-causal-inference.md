# Lesson 21e: Causal Inference — From Correlation to Causation

[← Regression](lesson-21d-regression.md) | [Back to TOC](../README.md) | [Next: Applied Statistics →](lesson-21f-applied-statistics.md)

---

> **Why this lesson exists:** This is arguably the most important lesson in the entire statistics phase. Causal inference is what separates "we observed a correlation" from "X actually causes Y." The techniques here — DAGs, counterfactuals, instrumental variables — give you a rigorous framework for evaluating causal claims. This is directly relevant to alignment (counterfactual reasoning is central to decision theory, Lesson 30) and to the genetics/epidemiology debates you want to adjudicate.

## 🎯 Core Concepts

### The Fundamental Problem of Causal Inference

- **You want to know:** what would have happened if we had done something different? If patient A took the drug, what would have happened if they HADN'T taken it?
- **The problem:** you can only observe one outcome. You can't see both worlds simultaneously. The unobserved scenario is called the **counterfactual.**
- **The potential outcomes framework (Rubin):** for each unit i, there are two potential outcomes: Y₁ᵢ (outcome with treatment) and Y₀ᵢ (outcome without). The causal effect for i is Y₁ᵢ - Y₀ᵢ. But you only observe one of these.
- **The Average Treatment Effect (ATE):** E[Y₁ - Y₀] — the average causal effect across the population. This is what RCTs estimate.
- **Why randomization works:** if treatment is randomly assigned, the treatment and control groups are on average identical in every way except treatment. So the difference in average outcomes IS the ATE.

### Directed Acyclic Graphs (DAGs) — The Language of Causation

- **A DAG is a causal diagram.** Nodes are variables. Arrows show causal relationships. No cycles (causes can't loop back on themselves in a single moment).
- **Example:** Smoking → Lung Cancer. Simple. The arrow means smoking causes lung cancer.
- **DAGs aren't just pictures.** They encode precise mathematical assumptions about which variables are independent, which are conditionally independent, and which are confounded.

### The Three Fundamental Patterns

Understanding these three patterns is the key to ALL of causal inference:

**1. The Fork (Confounding):**
```
     Z
    / \
   ↓   ↓
   X   Y
```
Z causes both X and Y. X and Y are correlated (because of Z), but X doesn't cause Y. If you control for Z, the correlation between X and Y disappears.

**Example:** Income (Z) causes both good nutrition (X) and good health (Y). Nutrition and health are correlated, but forcing someone to eat well without changing their income won't fully explain the health difference.

**Rule: CONTROL for confounders to remove bias.**

**2. The Chain (Mediator):**
```
   X → M → Y
```
X causes M, which causes Y. X does cause Y, but the effect goes through M. If you control for M, you block the effect of X on Y.

**Example:** Education (X) → Higher income (M) → Better health (Y). If you control for income, the effect of education on health shrinks — because you've blocked the pathway through income.

**Rule: DON'T control for mediators if you want the total effect of X on Y. DO control for them if you want the direct effect only.**

**3. The Collider:**
```
   X   Y
    \ /
     ↓
     C
```
Both X and Y cause C. X and Y are NOT inherently correlated. But if you control for C (condition on it), you CREATE a spurious correlation between X and Y.

**Example:** Talent (X) and Luck (Y) both cause Success (C). In the general population, talent and luck are independent. But among successful people (conditioning on C), talent and luck appear NEGATIVELY correlated — successful people with less talent must have had more luck.

**Rule: NEVER control for a collider. It creates bias where none existed.**

### Why "Controlling For" Can Go Wrong

This is the critical insight that most people miss:

- **Controlling for a confounder:** GOOD — removes bias
- **Controlling for a mediator:** sometimes bad — blocks the effect you're trying to measure
- **Controlling for a collider:** ALWAYS BAD — creates bias

**This means the common practice of "controlling for everything" is WRONG.** You need a causal model (DAG) to decide what to control for. Blindly throwing variables into a regression can make your estimates WORSE.

**Example that causes endless Twitter debates:**
- Question: "Does [race/gender/other variable] affect [outcome], after controlling for [education/income/etc.]?"
- Problem: if the variable in question CAUSES the controls (e.g., discrimination affects income), then controlling for income removes part of the effect you're trying to measure. You're conditioning on a mediator.
- The correct analysis depends on the causal structure, not just the statistical association.

### Methods for Causal Inference Without Experiments

When you can't run an RCT (most situations), these methods try to approximate the logic of randomization:

**Instrumental Variables (IV):**
- Find a variable Z that: (1) affects X, (2) has no direct effect on Y, (3) isn't associated with confounders
- Then Z acts as a "natural experiment" — variation in X caused by Z is as good as random
- **Classic example:** distance to college as an instrument for education. Living closer to a college doesn't directly affect income — but it increases education, which affects income. The part of education variation driven by distance is "clean."
- **Weak instruments:** if Z only weakly affects X, IV estimates are noisy and biased. This is a common problem.

**Difference-in-Differences (DiD):**
- Compare changes over time in a treatment group vs. a control group
- Even if the groups differ at baseline, you can estimate the treatment effect if you assume they would have followed parallel trends without treatment
- **Example:** a policy change in one state but not another. Compare the change in outcomes in the policy state to the change in the comparison state.

**Regression Discontinuity (RD):**
- People just above and just below a threshold (test score cutoff for a program, age cutoff for eligibility) are essentially randomly assigned to treatment vs. control
- Compare outcomes for people just above vs. just below the cutoff
- **Example:** scholarship cutoff at GPA 3.5. Students at 3.49 and 3.51 are essentially identical, but one gets the scholarship. Comparing their outcomes estimates the scholarship's causal effect.

**Propensity Score Matching:**
- For observational data: estimate the probability of receiving treatment given covariates (the "propensity score")
- Match treated individuals to untreated individuals with similar propensity scores
- Compare outcomes within matched pairs
- **Limitation:** only accounts for OBSERVED confounders. Hidden confounders still bias results.

### Mendelian Randomization — Causal Inference Using Genetics

- **The brilliant idea:** genetic variants are assigned at conception, essentially randomly (within a population). If a genetic variant affects X (say, a variant that affects alcohol metabolism), you can use it as an instrument for X's effect on Y (say, heart disease).
- **Why this matters for genetics debates:** Mendelian randomization lets you make causal claims from observational data. "People who drink moderately have better heart health" is an observational correlation. Mendelian randomization using alcohol-metabolism genes can test whether it's causal.
- **Limitations:** pleiotropy (the gene affects multiple things), population stratification, and weak instruments all threaten validity.

## 📺 Watch — Primary

1. **Brady Neal — "Introduction to Causal Inference" (YouTube course)**
   - https://www.youtube.com/results?search_query=brady+neal+causal+inference+introduction
   - *A full course, but the first 3-4 lectures cover all the core concepts. The best free resource on the topic.*
2. **Judea Pearl — "The New Science of Cause and Effect" (talks)**
   - https://www.youtube.com/results?search_query=judea+pearl+causality+lecture
   - *Pearl invented DAGs for causal inference. Hearing him explain the framework is worth it.*

## 📺 Watch — Secondary

3. **Crash Course Statistics — "Causal Inference"**
4. **NBER Causal Inference Boot Camp** (YouTube) — for the econometrics perspective
5. **StatQuest — "Logistic Regression" (review)** — needed for propensity scores

## 📖 Read — Primary

- **"The Book of Why" by Judea Pearl** — Chapters 1–4
  - The accessible version of Pearl's framework. Written for general readers. Excellent.
- **"Causal Inference: The Mixtape" by Scott Cunningham** — free online
  - https://mixtape.scunning.com/
  - *Written for social scientists. Covers IV, DiD, RD, matching with code examples. The best free causal inference textbook.*

## 📖 Read — Secondary

- **"Mostly Harmless Econometrics" by Angrist & Pischke** — the classic
- **"Causal Inference: What If" by Hernán & Robins** — free PDF
  - https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/
  - *The biostatistics/epidemiology perspective. More technical than Pearl, equally rigorous.*
- **"An Introduction to Causal Inference" by Judea Pearl (primer)**
  - https://ftp.cs.ucla.edu/pub/stat_ser/r354-corrected-reprint.pdf

## 📖 Read — Going Deep

- **"Causality" by Judea Pearl** — the full technical treatment
- **"Elements of Causal Inference" by Peters, Janzing, Schölkopf** — the ML perspective on causality
  - https://mitpress.mit.edu/9780262037310/ — free PDF available
  - *Connects causal inference to machine learning directly.*

## 🔨 Do

- **DAG practice:** for each of these scenarios, draw the DAG and determine what to control for:
  1. Does exercise reduce heart disease? (confounder: overall health consciousness)
  2. Does college education increase income? (mediator: type of job; confounder: family background)
  3. Does hospital quality affect patient outcomes? (collider: being in the hospital)
- **Collider bias simulator:** generate data where X and Y are independent, both cause Z. Show that among observations where Z > threshold, X and Y appear correlated. This is Berkson's paradox from a causal perspective.
- **Instrumental variables:** simulate data with a confounder. Show that naive regression gives a biased estimate. Introduce an instrument and show that IV estimation recovers the true effect.
- **Difference-in-differences:** find a real policy change (minimum wage increase, legalization of something) and replicate a simple DiD analysis using public data.
- **Key exercise:** A major genetics debate: "Are observed [group differences in trait X] genetic or environmental?" Draw the DAG. Identify confounders. Explain why observational correlations between ancestry and trait don't establish genetic causation. What would you need to establish it? (This is exactly the kind of debate you want to adjudicate.)

## 🔗 ML Connection

- **Counterfactual reasoning** is central to interpretability. "If this neuron had fired differently, would the output change?" Activation patching (Lesson 27) IS causal inference — you're intervening on variables and measuring effects.
- **Pearl's do-calculus** formalizes the difference between observing and intervening. This is exactly the distinction that matters in alignment: observing that a model says "I'm safe" is different from intervening to test whether it actually IS safe.
- **Causal representation learning** is an active ML research area: can models learn causal structure from data? This connects to the "world model" question in alignment.
- **Spurious correlations in training data** are confounders. A model that learns "text mentioning hospitals predicts negative sentiment" may have learned a spurious correlation, not a causal relationship.

## 🧠 Alignment Connection

This is one of the most alignment-relevant lessons in the entire statistics phase:

- **Decision theory (Lesson 30) IS causal reasoning.** CDT uses causal interventions ("if I do X, what happens?"). EDT uses correlations. FDT uses logical/functional connections. The CDT vs. EDT debate is literally about whether agents should reason causally or evidentially.
- **Counterfactual reasoning in alignment:** "Would this model have behaved differently if it knew it was being tested?" This is a counterfactual question that requires causal, not just statistical, analysis.
- **Interpretability as causal inference:** when Anthropic's researchers do activation patching, they're performing interventions on the model's internal states and measuring causal effects. Understanding causal inference means understanding the methodology of interpretability.
- **Goodhart's Law is a causal phenomenon:** optimizing a proxy (the measure) instead of the target (what we care about) is a causal error — you're intervening on the wrong node in the causal graph.
