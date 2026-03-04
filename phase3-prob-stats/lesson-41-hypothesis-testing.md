# Lesson 41: Hypothesis Testing, P-Values, and What They Actually Mean

[← Information Theory](lesson-40-information-theory.md) | [Back to TOC](../README.md) | [Next: Experimental Design →](lesson-42-experimental-design.md)

---

> **Why this lesson exists:** P-values are the single most misunderstood concept in all of science. Researchers get them wrong. Journalists get them wrong. Twitter gets them *spectacularly* wrong. If you want to adjudicate statistical debates — about genetics, medicine, psychology, or AI capabilities — you need to understand what hypothesis tests actually tell you (and what they don't). This also connects to alignment: when someone claims "this model is safe because it passed our statistical test," you need to evaluate that claim.

## 🎯 Core Concepts

### The Logic of Hypothesis Testing

- **The fundamental question:** "Could this data have occurred by chance, or is something real going on?"
- **The null hypothesis (H₀):** the boring explanation. "There's no effect. The drug doesn't work. The two groups are the same. The model performs no better than random." You assume this is true and see if the data contradicts it.
- **The alternative hypothesis (H₁):** "There IS an effect." This is what you're hoping to show.
- **The procedure:**
  1. Assume H₀ is true
  2. Ask: "How surprising is my data, given H₀?"
  3. If the data is very surprising under H₀, reject H₀ and conclude H₁

### P-Values — The Most Misunderstood Number in Science

- **What a p-value IS:** the probability of seeing data at least as extreme as what you observed, IF the null hypothesis were true. P(data ≥ this extreme | H₀ true).
- **What a p-value is NOT:**
  - ❌ The probability that the null hypothesis is true
  - ❌ The probability you're wrong
  - ❌ The probability the result will replicate
  - ❌ The size of the effect
- **The critical distinction:** P(data | H₀) ≠ P(H₀ | data). Confusing these is called the **base rate fallacy** — and you already know from Lesson 21 (Bayes' theorem) that flipping a conditional probability requires the prior. A p-value gives you the likelihood, not the posterior.
- **Concrete example:** A drug trial gives p = 0.03. This means: "If the drug had zero effect, there's a 3% chance we'd see results this extreme." It does NOT mean "there's a 97% chance the drug works." If the prior probability of ANY random drug working is 10%, then even p = 0.03 only gives you about 77% posterior probability via Bayes.

### The p < 0.05 Threshold and Its Problems

- **Why 0.05?** Ronald Fisher suggested it as a rough guideline in the 1920s. It stuck, became dogma, and has caused enormous damage to science.
- **The multiple comparisons problem:** if you test 20 hypotheses, you expect one to hit p < 0.05 by pure chance. Run enough tests → guaranteed "significant" results.
- **P-hacking:** trying different analyses until you find p < 0.05. This includes: testing multiple outcomes, adding/removing covariates, looking at subgroups, deciding when to stop collecting data based on interim results. All of these inflate false positive rates.
- **The garden of forking paths:** even without conscious p-hacking, researcher degrees of freedom (choices about how to clean data, which observations to exclude, which variables to control for) create many possible analyses. The one that happens to give p < 0.05 gets published.
- **Bonferroni correction:** divide your significance threshold by the number of tests. Testing 20 things? Need p < 0.05/20 = 0.0025. Conservative but simple.
- **False Discovery Rate (FDR):** Benjamini-Hochberg procedure. Instead of controlling false positives per test, control the fraction of your discoveries that are false. More powerful than Bonferroni, widely used in genomics.

### Types of Errors

- **Type I error (false positive):** rejecting H₀ when it's actually true. "Finding" an effect that doesn't exist. Controlled by α (typically 0.05).
- **Type II error (false negative):** failing to reject H₀ when H₁ is actually true. Missing a real effect. Rate is β.
- **Power = 1 − β:** the probability of detecting a real effect. Depends on: effect size (bigger effects are easier to find), sample size (more data = more power), and α level.
- **Why power matters:** a study with 80% power still misses 20% of real effects. Many published studies are severely underpowered (especially in psychology and neuroscience), meaning they can only detect enormous effects. Small but real effects slip through.

### Effect Sizes — What P-Values Don't Tell You

- **The fundamental problem with p-values:** with enough data, *any* tiny effect becomes "statistically significant." A drug that improves blood pressure by 0.01 mmHg can give p < 0.001 with a million patients. That's real but meaningless.
- **Effect size measures how BIG the effect is:**
  - **Cohen's d:** difference in means divided by standard deviation. d = 0.2 (small), 0.5 (medium), 0.8 (large).
  - **Relative risk (RR):** how much more likely an outcome is in the treatment group. RR = 2 means twice as likely.
  - **Odds ratio (OR):** ratio of odds in two groups. Common in genetics and medicine.
  - **R²:** fraction of variance explained. R² = 0.3 means 30% of the variation is accounted for.
- **ALWAYS report effect sizes alongside p-values.** A study showing p = 0.001, d = 0.02 found a real but trivial effect. A study showing p = 0.08, d = 0.7 found a large effect that just missed significance due to small sample.

### Confidence Intervals — What They Actually Mean

- **A 95% confidence interval:** if you repeated the experiment many times, 95% of the CIs would contain the true value. It is NOT "95% probability the true value is in this range" (that's a Bayesian credible interval, which requires a prior).
- **Why CIs are better than p-values:** they show both the estimated effect size AND the uncertainty. A CI of [0.1, 0.3] for a drug effect tells you much more than "p = 0.01."
- **Wide CI = uncertain.** Narrow CI = precise estimate. A CI that includes zero means "we can't rule out no effect."

### The Common Tests (Know What They're For)

| Test | What it tests | When to use |
|------|--------------|-------------|
| **t-test** | Difference in means between 2 groups | Comparing treatment vs. control |
| **Chi-squared (χ²)** | Association between categorical variables | "Is eye color associated with nationality?" |
| **ANOVA** | Differences in means among 3+ groups | Comparing multiple treatments |
| **Correlation test** | Linear relationship between two variables | "Does height predict weight?" |
| **Mann-Whitney U** | Non-parametric version of t-test | When data isn't normally distributed |
| **Fisher's exact test** | Like χ² but for small samples | Small contingency tables |

- **Parametric vs. non-parametric:** parametric tests assume distributions (usually Gaussian). Non-parametric tests don't. If your data isn't normal, use non-parametric.
- **You don't need to memorize formulas.** You need to know: which test is appropriate, what the output means, and what can go wrong.

## 📺 Watch — Primary

1. **StatQuest — "P-values, Clearly Explained"**
   - https://www.youtube.com/watch?v=0oc49DyA3hU
   - *Josh Starmer's signature style. Best single video on the topic.*
2. **StatQuest — "Hypothesis Testing and the Null Hypothesis"**
   - https://www.youtube.com/results?search_query=statquest+hypothesis+testing+null+hypothesis
3. **Cassie Kozyrkov — "Statistics is the grammar of science"**
   - https://www.youtube.com/results?search_query=cassie+kozyrkov+statistics+hypothesis+testing
   - *Google's former Chief Decision Scientist. Extremely clear, entertaining.*

## 📺 Watch — Secondary

4. **3Blue1Brown — "But what is the Central Limit Theorem?"**
   - https://www.youtube.com/watch?v=zeJD6dqJ5lo
   - *Why normal distributions underpin all hypothesis testing. The CLT is the reason p-values work.*
5. **3Blue1Brown — "Why p-values are weird" (if available)**
6. **Veritasium — "Is Most Published Research Wrong?"**
   - https://www.youtube.com/results?search_query=veritasium+is+most+published+research+wrong
   - *Covers the replication crisis, p-hacking, publication bias. Gripping.*
6. **StatQuest — "Effect Size, Clearly Explained"**
7. **StatQuest — "Confidence Intervals"**

## 📖 Read — Primary

- **"Statistics Done Wrong" by Alex Reinhart** — https://www.statisticsdonewrong.com/
  - Free online. Covers every major statistical mistake with real examples. Readable and eye-opening.
- **"The ASA Statement on P-Values" (2016)**
  - https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf
  - The American Statistical Association's official response to p-value misuse. Short and important.

## 📖 Read — Secondary

- **"Statistical Rethinking" by Richard McElreath** — Chapters 1–4
  - https://xcelab.net/rm/statistical-rethinking/
  - The best modern statistics textbook. Bayesian approach, but Chapter 1's critique of null hypothesis testing is essential regardless.
- **Andrew Gelman's blog** — https://statmodeling.stat.columbia.edu/
  - Columbia statistician who regularly dissects flawed studies and statistical reasoning.

## 📖 Read — Going Deep

- **"The Cult of Statistical Significance" by Ziliak & McCloskey** — the case against blind p-value worship
- **"Moving to a World Beyond p < 0.05" (Nature, 2019)** — 800+ scientists calling for reform
  - https://www.nature.com/articles/d41586-019-00857-9

## 🔨 Do

- **P-value simulator:** generate data from two distributions with known (small) difference. Run t-tests 1000 times. Plot the distribution of p-values. See that even with a real effect, p-values are UNIFORMLY distributed under the null. Feel why one study proves nothing.
- **Multiple comparisons demo:** generate 20 datasets with NO real effect. Test all 20. Count how many give p < 0.05. Verify it's about 1 in 20. Apply Bonferroni correction and see it vanish.
- **Power analysis:** for a given effect size and sample size, compute the power of a t-test. Show that small samples + small effects = terrible power. Plot power curves.
- **Effect size exercise:** find a real genetics paper reporting "statistically significant" GWAS results. Look up the effect sizes. Calculate how much variance is explained. Realize how small genetic effects typically are.
- **Key exercise:** A Twitter debate about a psychology study: "p = 0.04, therefore the effect is real." Write a response addressing: (1) what p = 0.04 actually means, (2) what's missing (effect size, power, prior probability), (3) multiple comparisons risk, (4) what a Bayesian analysis would require. This is practice for exactly the kind of adjudication you want to do.
- **ANOVA by hand (supplementary — from Bayesian Computation book gap analysis):** generate three groups of data in NumPy (e.g., model accuracy scores from three training methods, with slightly different means). Compute the between-group variance (how much group means differ from the grand mean), the within-group variance (how much individual scores differ from their group mean), and the F-statistic (ratio of between/within). Look up the p-value using `scipy.stats.f.sf()`. Then verify your answer with `scipy.stats.f_oneway()`. The goal isn't memorizing the formula — it's feeling that ANOVA is just "is the spread BETWEEN groups bigger than the spread WITHIN groups?" Once you've done this once, every ANOVA table in every paper you read will make sense.
- **Chi-squared test by hand (supplementary):** create a 2×2 contingency table (e.g., "did the model produce harmful output?" vs. "was RLHF applied?"). Compute expected counts under independence, compute χ² = Σ(observed − expected)² / expected, and find the p-value. Verify with `scipy.stats.chi2_contingency()`. This takes 10 minutes and demystifies every chi-squared result you'll encounter in alignment papers that report categorical outcomes.


## 🔗 ML & Alignment Connection

- **Model evaluation** uses statistical tests constantly. "Is model A better than model B on this benchmark?" requires significance testing. Many ML papers fail to do this — they report accuracy differences without confidence intervals.
- **A/B testing** in production ML is hypothesis testing. When Anthropic or OpenAI runs experiments on model behavior, they use these tools.
- **The replication crisis** parallels problems in ML: benchmark gaming, overfitting to test sets, and reporting only the best runs are all forms of p-hacking.
- **Calibration** (Lesson 21) connects: a well-calibrated model's confidence should match reality, just like a well-done study's p-values should reflect actual false positive rates.

- **Safety claims require statistical rigor.** When someone says "this model passed our safety evaluation," you need to ask: what was the power of the test? What effect size could it detect? How many evaluations were run?
- **The base rate fallacy in alignment:** even a good test for deceptive alignment (say, 95% sensitivity) has high false negative rates if deceptive alignment is rare. This is Bayes' theorem applied to AI safety testing.
- **Publication bias in safety research:** negative results (models that weren't dangerous) don't get published. This creates a skewed picture of the risk landscape.