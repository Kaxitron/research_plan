# Lesson 26: Regression — From Linear to Logistic and Beyond

[← Experimental Design](lesson-25-experimental-design.md) | [Back to TOC](../README.md) | [Next: Causal Inference →](lesson-27-causal-inference.md)

---

> **Why this lesson exists:** You already understand linear regression geometrically — it's projection onto a subspace (Lesson 10). Now you need regression as a *statistical* tool: what do coefficients mean, when can you trust them, what happens with multiple predictors, and how do you handle binary outcomes (logistic regression). Most real-world statistical claims — in genetics, epidemiology, economics, and ML — come from regression models. Reading these results fluently is a prerequisite for adjudicating debates.

## 🎯 Core Concepts

### Linear Regression as Statistics (Not Just Geometry)

You know the mechanics: x̂ = (AᵀA)⁻¹Aᵀb minimizes ||Ax - b||². Now let's add the statistical layer.

- **The statistical model:** yᵢ = β₀ + β₁x₁ᵢ + β₂x₂ᵢ + ... + εᵢ, where ε ~ N(0, σ²). The randomness comes from ε — the part of y we can't explain.
- **Coefficients are estimates, not truths.** β̂₁ is your BEST GUESS of the true β₁ given your data. Different samples → different β̂₁. This variation is the standard error.
- **T-tests on coefficients:** "is β₁ significantly different from zero?" This uses the same hypothesis testing framework from Lesson 24. The test statistic is t = β̂₁ / SE(β̂₁).
- **Confidence intervals for coefficients:** β̂₁ ± t* × SE. If the CI includes zero, you can't conclude the predictor has an effect.
- **R² (coefficient of determination):** fraction of variance in y explained by the model. R² = 0.3 means 30% explained, 70% unexplained. In social science, R² = 0.1 is typical. In physics, R² = 0.99 is expected.

### Multiple Regression — The Power and Peril of "Controlling For"

- **Why it matters:** most real questions involve multiple variables. "Does education affect income, CONTROLLING FOR age, gender, and location?"
- **Each coefficient means:** "the change in y per unit change in x_j, HOLDING ALL OTHER VARIABLES CONSTANT." This is the "partial" effect — it's what you get after accounting for the other predictors.
- **Multicollinearity:** when predictors are correlated with each other, their individual coefficients become unreliable (huge standard errors). The model as a whole can still predict well, but you can't interpret individual coefficients.
  - **In linear algebra terms:** the columns of A are nearly linearly dependent → AᵀA is nearly singular → (AᵀA)⁻¹ has huge entries. This is exactly the situation that motivated ridge regression (Lesson on ridge/lasso).
- **Confounders and "controlling for":** adding a confounder to the regression removes its effect. If Z causes both X and Y, then including Z as a predictor gives you the TRUE effect of X on Y (approximately). But — and this is critical — you can also BREAK your analysis by "controlling for" the wrong things (see collider bias below and Lesson 27 on causal inference).
- **Adjusted R²:** penalizes for adding predictors. Regular R² always goes up when you add variables, even useless ones. Adjusted R² can go down.

### Interpreting Regression Tables (The Skill You Actually Need)

When you see a regression table in a paper or a Twitter debate, here's what to look for:

| Term | What it tells you |
|------|------------------|
| **Coefficient (β̂)** | Effect size and direction. "One unit increase in X → β̂ change in Y" |
| **Standard Error (SE)** | How uncertain the coefficient is. Large SE = don't trust it |
| **t-statistic** | β̂ / SE. Bigger = more significant |
| **p-value** | Significance of this coefficient (see Lesson 24 for caveats) |
| **95% CI** | Range of plausible values for the true coefficient |
| **R²** | Overall model fit. Not always meaningful for individual predictors |
| **N** | Sample size. Small N = everything uncertain |

### Logistic Regression — When the Outcome is Binary

- **The problem:** you can't use linear regression for yes/no outcomes. Predicting "probability of disease" with linear regression can give values > 1 or < 0.
- **The logistic function:** σ(z) = 1/(1 + e⁻ᶻ) — maps any number to (0, 1). You already know this as the sigmoid from neural networks (Lesson 34).
- **The model:** P(y = 1 | x) = σ(β₀ + β₁x₁ + ... + βₖxₖ). The linear combination goes through the logistic function to produce a probability.
- **Coefficients are in log-odds:** β₁ = 0.5 means "one unit increase in x₁ increases the log-odds of the outcome by 0.5." To get the odds ratio: OR = eᵝ¹ ≈ 1.65. This means "65% higher odds."
- **Why OR matters in practice:** almost all genetics results (GWAS) and many epidemiology results are reported as odds ratios. OR = 1.1 means 10% higher odds — typical for genetic variants. OR = 2.0 means double the odds — that's a strong effect in genetics.
- **Connection to neural networks:** a single neuron with sigmoid activation IS logistic regression. The first neural network layer is literally doing (possibly multiple) logistic regressions on the input features.

### Generalized Linear Models (GLMs) — The Unified Framework

- **The pattern:** y = f(β₀ + β₁x₁ + ...) where f is a "link function" that maps the linear prediction to the appropriate range.
  - Linear regression: f = identity (no transformation)
  - Logistic regression: f = logistic (maps to 0–2)
  - Poisson regression: f = exp (for count data — always positive)
- **Why you should know this exists:** when you see "we used a Poisson regression" or "negative binomial regression," it's the same framework with a different link function. Don't be intimidated.

### The Assumptions and When They Fail

- **Linearity:** the relationship between predictors and outcome is linear (or log-linear for GLMs). If it's actually curved, your coefficients are wrong. Fix: add polynomial terms, or use non-parametric methods.
- **Independence:** observations don't influence each other. Violated by: time series data, clustered data (students within schools), spatial data. Fix: mixed-effects models, clustered standard errors.
- **Homoscedasticity:** constant variance of residuals. When variance depends on X, standard errors are wrong. Fix: robust standard errors (Huber-White).
- **No perfect multicollinearity:** already discussed.
- **The key point:** when someone presents regression results, these assumptions may or may not hold. Violated assumptions don't necessarily invalidate the results, but they change what you can conclude.

## 📺 Watch — Primary

1. **StatQuest — "Linear Regression, Clearly Explained"**
   - https://www.youtube.com/results?search_query=statquest+linear+regression+clearly+explained
2. **StatQuest — "Logistic Regression"**
   - https://www.youtube.com/results?search_query=statquest+logistic+regression+clearly+explained
   - *Josh covers the odds ratio interpretation well.*
3. **StatQuest — "Multiple Regression"**
   - https://www.youtube.com/results?search_query=statquest+multiple+regression

## 📺 Watch — Secondary

4. **StatQuest — "R-squared, Clearly Explained"**
5. **StatQuest — "Ridge vs. Lasso Regression"** (connects to your recent ridge/lasso work)
6. **Crash Course Statistics — "Regression" (Episode 32)**

## 📖 Read — Primary

- **"An Introduction to Statistical Learning" (ISLR)** — Chapters 3 (linear) and 4 (logistic)
  - https://www.statlearning.com/ — free PDF
  - *THE standard reference. Clear, practical, accessible.*
- **"Statistical Rethinking" by McElreath** — Chapters 4–6 for the Bayesian take on regression

## 📖 Read — Secondary

- **"Mostly Harmless Econometrics" by Angrist & Pischke** — Chapters 1–3
  - Economists' perspective on what regression can and can't tell you about causation. Excellent and surprisingly readable.
- **UCLA Statistical Consulting — Regression tutorials**
  - https://stats.oarc.ucla.edu/other/dae/
  - Worked examples in R and Python for every type of regression

## 🔨 Do

- **Multiple regression in Python:** use scikit-learn or statsmodels to fit a multiple regression on a real dataset (try the Boston housing dataset or similar). Interpret each coefficient. Find which predictors are significant. Compute R².
- **Logistic regression on real data:** predict a binary outcome (e.g., titanic survival, diabetes diagnosis). Interpret odds ratios. Plot the predicted probabilities.
- **Multicollinearity demo:** create two highly correlated predictors. Show that individual coefficients are unstable (huge SEs) even though the model predicts well. Add ridge regression and see coefficients stabilize.
- **Regression table reading exercise:** find 3 papers in different fields (genetics, economics, psychology) that report regression tables. For each: identify the key coefficient, its effect size, confidence interval, and sample size. Assess whether the conclusion is well-supported.
- **Key exercise:** Someone on Twitter posts: "Controlling for education and income, [variable X] still predicts [outcome Y] at p < 0.01." Write a response considering: (1) is "controlling for" appropriate here? (2) could there be omitted variable bias? (3) what's the effect size? (4) is the causal claim justified? Practice this exact pattern — it's the most common statistical argument you'll encounter online.

## 🔗 ML Connection

- **Neural networks generalize regression.** A single layer with no activation = linear regression. A single layer with sigmoid = logistic regression. Deep networks = very flexible nonlinear regression with learned features. Understanding the statistical perspective helps you reason about what the network is "fitting."
- **Interpretable ML** methods like LIME and SHAP essentially fit local regression models to explain individual predictions.
- **The bias-variance tradeoff** in regression (underfitting vs. overfitting) is the same tradeoff in ML, just with more parameters.

## 🧠 Alignment Connection

- **Probing classifiers** in interpretability (Lesson 41) are logistic regressions trained on model activations. When researchers say "we found a direction in activation space that predicts truthfulness," they mean "a logistic regression on activations achieves high accuracy." Understanding regression means understanding probing results.
- **"Controlling for" in alignment evaluations:** if a model appears safer after RLHF, is that the RLHF or the additional compute/data? Regression-style reasoning helps disentangle these.
