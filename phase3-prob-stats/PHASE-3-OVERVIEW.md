# Phase 3 Overview: Probability & Statistics — Every Concept and Method

> **Purpose:** Exhaustive reference of every concept, technique, and method covered in Phase 3 (Lessons 37–52). Use for review, exam prep, or topic lookup.

---

## Core Probability (Lessons 37–40)

### Lesson 37: Probability Distributions and Bayes' Theorem

**Foundations:**
- Probability axioms: P(Ω) = 1, P(A) ≥ 0, P(A∪B) = P(A) + P(B) for disjoint events
- Conditional probability: P(A|B) = P(A∩B)/P(B)
- Independence: P(A∩B) = P(A)P(B)
- **Law of total probability:** P(B) = Σ P(B|Aᵢ)P(Aᵢ) over partition {Aᵢ}
- **Bayes' theorem:** P(A|B) = P(B|A)P(A)/P(B) — inverting conditional probabilities

**Discrete Distributions:**
- Bernoulli(p): single binary trial, P(X=1) = p
- Binomial(n, p): number of successes in n trials
- Poisson(λ): count of rare events, P(X=k) = λᵏe⁻ᵘ/k!
- Geometric(p): trials until first success
- Categorical/Multinomial: generalization to multiple categories (softmax output)

**Continuous Distributions:**
- Uniform(a,b): constant density on [a,b]
- Normal/Gaussian N(μ, σ²): bell curve, defined by mean and variance
- Exponential(λ): time between Poisson events, memoryless property
- Multivariate Gaussian N(μ, Σ): described by mean vector + covariance matrix
- Log-normal, Beta, Gamma, Dirichlet (used in Bayesian priors)

**Key Theorems:**
- **Central Limit Theorem (CLT):** averages of iid random variables → Gaussian regardless of original distribution
- **Law of Large Numbers (LLN):** sample mean → population mean as n → ∞
- **Change of variables for probability:** p(y) = p(f⁻¹(y))·|det(J_{f⁻¹})| (Jacobian factor)
- Joint, marginal, conditional distributions

---

### Lesson 38: Expectation, Variance, and Covariance

**Expectation:**
- E[X] = Σ xP(x) (discrete) or ∫ xp(x)dx (continuous) — weighted average
- **Linearity of expectation:** E[aX + bY] = aE[X] + bE[Y] (always, even if dependent!)
- E[g(X)] ≠ g(E[X]) in general (Jensen's inequality for convex g: E[g(X)] ≥ g(E[X]))

**Variance and Standard Deviation:**
- Var(X) = E[(X−μ)²] = E[X²] − (E[X])² (computational formula)
- σ = √Var (standard deviation, same units as X)
- Var(aX + b) = a²Var(X)
- Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y)

**Covariance and Correlation:**
- Cov(X,Y) = E[(X−μ_X)(Y−μ_Y)] = E[XY] − E[X]E[Y]
- Positive → tend to move together; negative → tend to move opposite; zero → uncorrelated
- **Correlation:** ρ = Cov(X,Y)/(σ_X σ_Y), normalized to [−1, 1]
- r measures directional alignment; r² measures proportion of variance explained by projection
- **Uncorrelated ≠ independent** (for non-Gaussian distributions)

**Covariance Matrix:**
- Σᵢⱼ = Cov(Xᵢ, Xⱼ) — symmetric, positive semi-definite
- Diagonal entries = variances; off-diagonal = covariances
- Eigendecomposition of Σ = PCA directions and magnitudes

**Other:**
- Moment generating functions: M(t) = E[eᵗˣ]
- Moments: E[Xⁿ] — mean (1st), variance (2nd central), skewness (3rd), kurtosis (4th)

---

### Lesson 39: Maximum Likelihood Estimation

**Likelihood and MLE:**
- **Likelihood:** L(θ) = P(data | θ) — probability of observed data given parameters
- **Log-likelihood:** ℓ(θ) = log L(θ) = Σ log P(xᵢ | θ) — turns products into sums
- **MLE:** θ̂ = argmax L(θ) = argmax ℓ(θ) = argmin(−ℓ(θ))
- **Cross-entropy loss = negative log-likelihood** for classification
- **MSE loss corresponds to MLE** under Gaussian noise assumption

**Properties of MLE:**
- Consistent: θ̂ → θ_true as n → ∞
- Asymptotically normal: √n(θ̂ − θ) → N(0, I(θ)⁻¹) where I is Fisher information
- Asymptotically efficient: achieves Cramér-Rao lower bound

**EM Algorithm (Expectation-Maximization):**
- For models with latent/hidden variables
- E-step: compute expected assignments given current parameters
- M-step: update parameters given expected assignments
- Alternates until convergence; guaranteed to increase likelihood each step
- **Gaussian Mixture Models (GMMs):** EM for fitting multiple Gaussians
- **K-means as hard EM:** hard assignments instead of soft probabilities

---

### Lesson 40: Information Theory — Entropy, KL Divergence, and Cross-Entropy

**Information Content:**
- I(x) = −log₂ P(x) (measured in bits) — rare events carry more information
- Certain events carry zero information

**Entropy:**
- H(X) = −Σ P(x) log P(x) = E[I(X)] — average surprise/uncertainty
- Maximum entropy = uniform distribution (maximum uncertainty)
- Minimum entropy = deterministic (zero uncertainty)
- Joint entropy H(X,Y), conditional entropy H(X|Y)
- Chain rule: H(X,Y) = H(X) + H(Y|X)

**Cross-Entropy:**
- H(P,Q) = −Σ P(x) log Q(x) — cost of encoding data from P using code optimized for Q
- H(P,Q) ≥ H(P) always (encoding with wrong distribution costs more)
- **Cross-entropy loss in ML:** compare true distribution P with model's predicted distribution Q

**KL Divergence:**
- D_KL(P‖Q) = H(P,Q) − H(P) = Σ P(x) log[P(x)/Q(x)] ≥ 0
- Measures "extra bits wasted" by using Q instead of P
- NOT symmetric: D_KL(P‖Q) ≠ D_KL(Q‖P)
- D_KL = 0 iff P = Q

**Temperature:**
- Softmax with temperature T: P(i) ∝ exp(logit_i / T)
- T → 0: argmax (greedy); T → ∞: uniform; T = 1: standard softmax
- Temperature controls entropy of the output distribution

**Mutual Information:**
- I(X;Y) = H(X) − H(X|Y) = H(Y) − H(Y|X) = D_KL(P(X,Y) || P(X)P(Y))
- Measures how much knowing Y reduces uncertainty about X (and vice versa)
- I(X;Y) = 0 iff X and Y are independent
- **Data Processing Inequality:** X→Y→Z implies I(X;Z) ≤ I(X;Y) — processing can't create information
- **Information Bottleneck:** compress input while preserving information about output

**Pointwise Mutual Information (PMI):**
- PMI(x,y) = log[P(x,y)/(P(x)P(y))] — connection to Word2Vec
- Positive PMI = co-occurrence more than chance

---

## Frequentist Methods (Lessons 41–43)

### Lesson 41: Hypothesis Testing and P-Values

- **Null hypothesis H₀** (default/no-effect) vs **alternative H₁**
- **P-value:** P(data ≥ this extreme | H₀ true) — NOT P(H₀ | data)
- **Base rate fallacy:** confusing P(data|H₀) with P(H₀|data)
- **Significance threshold:** p < 0.05 convention and its problems
- **Type I error (false positive, α):** rejecting H₀ when it's true
- **Type II error (false negative, β):** failing to reject H₀ when H₁ is true
- **Statistical power** = 1 − β (probability of detecting a real effect)
- **Effect sizes:** Cohen's d, Pearson's r, odds ratio — what p-values don't capture
- **Confidence intervals:** frequentist interpretation (repeated-experiment coverage)
- **Multiple comparisons:** Bonferroni correction, FDR, Benjamini-Hochberg
- **P-hacking, garden of forking paths, file drawer effect**

---

### Lesson 42: Experimental Design and Statistical Fallacies

- **Randomization:** eliminates systematic confounders
- **Control groups:** comparison baseline
- **Blinding:** single-blind, double-blind, triple-blind
- **Pre-registration:** commit to analysis plan before collecting data
- **Hierarchy of evidence:** case reports → observational → RCTs → systematic reviews → meta-analyses
- **Simpson's paradox:** aggregate trend reverses when data is split by a confounding variable
- **Ecological fallacy:** group-level statistics ≠ individual-level truths
- **Survivor bias, selection bias, response bias**
- **Regression to the mean**
- **Goodhart's Law:** when a measure becomes a target, it ceases to be a good measure
- **Publication bias and replication crisis**

---

### Lesson 43: Regression — From Linear to Logistic

- **Simple linear regression:** y = β₀ + β₁x + ε; OLS minimizes Σ(yᵢ − ŷᵢ)²
- **OLS solution:** β̂ = (XᵀX)⁻¹Xᵀy (least squares IS projection)
- **R² (coefficient of determination):** fraction of variance explained
- **Multiple regression:** y = β₀ + β₁x₁ + ... + βₚxₚ; "controlling for" variables
- **Multicollinearity:** correlated predictors → unstable coefficients
- **Regularization:** Ridge (L2: shrink all), Lasso (L1: sparse selection), Elastic Net (both)
- "Everything matters a little" → Ridge; "most things don't matter" → Lasso
- **Logistic regression:** P(y=1|x) = σ(β₀ + β₁x₁ + ...) — sigmoid output
- Coefficients in log-odds; odds ratios OR = e^β
- **Single neuron with sigmoid = logistic regression**
- **Generalized Linear Models (GLMs):** unified framework with link functions (identity, logit, log)
- **Assumptions:** linearity, independence, homoscedasticity, normality of residuals
- Robust standard errors (Huber-White) when assumptions violated

---

## Bayesian Deep Dive (Lessons 44–46)

### Lesson 44: Bayesian Reasoning & Foundations

- **Bayesian vs frequentist:** probability as degree of belief vs long-run frequency
- **Posterior ∝ likelihood × prior:** P(θ|D) ∝ P(D|θ)P(θ)
- **Prior types:** informative, weakly informative, "uninformative" (Jeffreys, maximum entropy)
- **Priors as regularization:** L2 penalty = Gaussian prior, L1 = Laplace prior, dropout ≈ approximate prior
- **Conjugate priors:** posterior has same form as prior (convenient closed-form updates)
  - Beta-Binomial, Normal-Normal, Gamma-Poisson, Dirichlet-Multinomial
- **MAP estimation:** argmax [log likelihood + log prior] = MLE + regularization
- MAP gives a point estimate — loses uncertainty information
- **Sequential updating:** today's posterior = tomorrow's prior
- Bayesian agent as normative model of rational belief updating

---

### Lesson 45: Bayesian Computation — Making the Intractable Tractable

- **The computational problem:** P(D) = ∫P(D|θ)P(θ)dθ is usually intractable
- **MCMC (Markov Chain Monte Carlo):** construct chain whose stationary distribution = posterior
  - **Metropolis-Hastings:** propose → accept/reject (normalizing constants cancel)
  - **Gibbs sampling:** update one parameter at a time from conditional
  - Diagnostics: burn-in, thinning, R-hat, effective sample size, trace plots
- **Hamiltonian Monte Carlo (HMC):** gradient-based sampling using physics analogy
  - Leapfrog integration, NUTS (No-U-Turn Sampler)
  - Much more efficient than random-walk MCMC in high dimensions
- **Variational Inference (VI):** approximate posterior with simple distribution q_φ
  - Minimize KL(q_φ ‖ P(θ|D)) by maximizing **ELBO**
  - **ELBO** = E_q[log P(D|θ)] − KL(q ‖ prior) = log P(D) − KL(q ‖ posterior)
  - **Mean-field approximation:** q factors as product of independent distributions
- **VAE connection:** encoder = variational params, decoder = likelihood, VAE loss = negative ELBO
- **Laplace approximation:** Gaussian at MAP with covariance = inverse Hessian (quick and dirty)

---

### Lesson 46: Bayesian Model Comparison and the Free Energy Principle

- **Marginal likelihood (evidence):** P(D|M) = ∫P(D|θ,M)P(θ|M)dθ
- **Automatic Occam's razor:** complex models spread prior thinly → lower evidence for specific data
- **Bayes factors:** BF₁₂ = P(D|M₁)/P(D|M₂) — can support null hypothesis
- **BIC approximation:** −2 log P(D|θ̂) + k log n ≈ −2 log marginal likelihood for regular models
- **BIC fails for neural networks** (singular models: Fisher information degenerates)
- **WAIC:** Bayesian generalization of AIC, works for singular models
- **LOO-CV (PSIS-LOO):** gold standard for predictive model comparison
- **Free energy:** F = −log P(D|M) — minimizing = maximizing evidence
- **SLT correction:** F ≈ nL(θ̂) + λ log n − (m−1) log log n
  - **RLCT (λ)** replaces k/2 as the true effective dimension
  - For neural networks: λ ≤ d/2 (simpler than parameter count suggests)

---

## Applied Statistics (Lessons 47–48)

### Lesson 47: Causal Inference — From Correlation to Causation

- **Counterfactuals:** what would have happened differently?
- **Potential outcomes (Rubin):** Y₁ᵢ, Y₀ᵢ, causal effect = Y₁ − Y₀
- **Average Treatment Effect (ATE)**
- **Directed Acyclic Graphs (DAGs):** causal diagrams
- **Three fundamental patterns:** chains (mediation), forks (confounding), colliders
- **d-separation rules** for conditional independence
- Controlling for confounders (good) vs mediators (sometimes bad) vs colliders (always bad)
- **Causal inference methods:** instrumental variables, difference-in-differences, regression discontinuity, propensity score matching
- **Mendelian randomization:** genetic variants as natural instruments

---

### Lesson 48: Applied Statistics — Adjudicating Real Debates

- **Heritability (h²):** fraction of trait variation from genetic variation (population-level)
- Between-group heritability ≠ between-group genetic causation
- **Twin studies:** identical vs fraternal twins, equal environments assumption
- **GWAS:** genome-wide association, p < 5×10⁻⁸, tiny effect sizes
- **Polygenic scores (PRS)** and their limitations
- **Population stratification** as confounder; PCA correction
- **Missing heritability problem**
- **Epidemiology:** Bradford Hill criteria, confounders, healthy user bias
- **Nutrition science pitfalls**
- Statistical adjudication of real-world empirical claims

---

## ML Theory Foundations (Lessons 49–52)

### Lesson 49: Concentration Inequalities — Markov to Chernoff

- **Markov's inequality:** P(X ≥ a) ≤ E[X]/a (weakest, most general)
- **Chebyshev's inequality:** P(|X−μ| ≥ kσ) ≤ 1/k²
- **Chernoff bounds:** exponential concentration via moment generating functions
- **Hoeffding's inequality:** tight bounds for bounded random variables
- **Sub-Gaussian and sub-exponential random variables**
- Applications: bounding sample means, uniform convergence, generalization bounds

### Lesson 50: Markov Chains and Mixing

- **Markov property:** future depends only on present, not past
- **Transition matrices:** Pᵢⱼ = P(X_{t+1}=j | X_t=i)
- **Stationary distribution π:** πP = π
- **Irreducibility, aperiodicity, ergodicity**
- **Convergence theorem:** ergodic chains converge to unique stationary distribution
- **Mixing time:** how quickly chain approaches stationary distribution
- Connection to MCMC: design chains whose stationary distribution = target posterior
- **Detailed balance** (reversibility): π_i P_{ij} = π_j P_{ji}

### Lesson 51: Fisher Information and Exponential Families

- **Fisher information:** I(θ) = E[(∂/∂θ log P(x|θ))²] = −E[∂²/∂θ² log P(x|θ)]
- Measures curvature of log-likelihood → how informative data is about θ
- **Cramér-Rao bound:** Var(θ̂) ≥ 1/I(θ) — fundamental limit on estimation precision
- **Fisher information matrix** (multivariate): Iᵢⱼ = −E[∂²ℓ/∂θᵢ∂θⱼ]
- **Singular Fisher information** at neural network symmetries (key for SLT)
- **Exponential families:** P(x|θ) = h(x) exp(η(θ)·T(x) − A(θ))
- Sufficient statistics, natural parameters
- Gaussian, Bernoulli, Poisson, Gamma, Beta all belong to exponential families
- **Natural gradient descent:** updates in Fisher information metric (accounts for parameter space geometry)

### Lesson 52: PAC Learning and Generalization Bounds

- **PAC framework:** Probably Approximately Correct
- **Sample complexity:** how many examples needed to learn within ε error with probability 1−δ
- **VC dimension:** largest set that can be shattered by hypothesis class
- VC dimension of linear classifiers = d+1 in d dimensions
- **Fundamental theorem of statistical learning:** finite VC dim ↔ PAC learnable
- **Rademacher complexity:** data-dependent capacity measure
- **Generalization bounds:** test error ≤ train error + complexity/√n
- Why these bounds are loose for neural networks (VC dim ∝ parameters, but networks generalize anyway)
- Connection to SLT: RLCT provides tighter effective complexity measure

---

## Assessments

- **Exam 3A: Probability & Frequentist** (Lessons 37–43) — 60 min
- **Exam 3B: Bayesian & Applied Stats** (Lessons 44–52) — 60 min
