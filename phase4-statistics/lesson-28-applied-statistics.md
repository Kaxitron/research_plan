# Lesson 28: Applied Statistics — Genetics, Epidemiology, and Adjudicating Debates

[← Causal Inference](lesson-27-causal-inference.md) | [Back to TOC](../README.md) | [Next: Computability →](../phase5-math-enrichment/lesson-29-computability.md)

---

> **Why this lesson exists:** This is the payoff lesson. You now have hypothesis testing, experimental design, regression, and causal inference in your toolkit. This lesson applies ALL of it to the specific domains where statistical debates are fiercest — genetics, epidemiology, and social science. By the end, you'll have a concrete framework for evaluating statistical claims you encounter online. This also connects to alignment: population-level statistics about AI capabilities, benchmark evaluations, and risk estimates all use these methods.

## 🎯 Core Concepts

### Genetics — The Statistical Landscape

#### Heritability: The Most Misunderstood Statistic

- **What heritability IS:** the fraction of trait variation in a POPULATION that is associated with genetic variation. Formally: h² = Var(genetic) / Var(total).
- **What heritability IS NOT:**
  - ❌ How "genetic" a trait is for an individual. Heritability is a POPULATION statistic. Saying "height is 80% heritable" does NOT mean "80% of your height is determined by your genes."
  - ❌ Fixed across environments. Heritability changes with the environment. In a society where everyone gets identical nutrition, height heritability would be ~100% (all remaining variation is genetic). In a society with extreme nutrition inequality, heritability would be lower (environment accounts for more variance).
  - ❌ A measure of genetic determinism. High heritability doesn't mean the trait can't be changed by environment. Myopia is highly heritable AND strongly affected by reading/screen time.
- **The critical point for debates:** between-group differences in a trait tell you NOTHING about whether those differences are genetic, even if the trait is highly heritable WITHIN each group.
  - **Lewontin's analogy:** plant seeds from the same bag in two plots — one with rich soil, one with poor soil. Within each plot, height differences are 100% genetic (same environment). Between plots, the height difference is 100% environmental. Within-group heritability says nothing about between-group causes.
- **Twin studies:** compare identical twins (sharing ~100% of DNA) with fraternal twins (~50%). Higher similarity among identical twins → higher heritability. But twin studies have assumptions: shared environment is truly shared, no gene-environment correlation, no epigenetics. These are often violated.

#### GWAS — Genome-Wide Association Studies

- **What GWAS does:** tests ~millions of genetic variants (SNPs) for association with a trait. Each variant is tested independently. This is the massive multiple comparisons problem.
- **Significance threshold:** p < 5×10⁻⁸ (not p < 0.05). This is the Bonferroni correction for ~1 million independent tests. Extremely stringent.
- **Effect sizes are tiny.** A typical GWAS hit might have an odds ratio of 1.05-1.15 for a disease, or explain 0.01% of trait variance. Individual genetic variants have SMALL effects on complex traits.
- **Polygenic scores (PRS):** combine thousands of small GWAS effects into a single prediction score. Accuracy for most traits is moderate — PRS for height explains ~25% of variance, for schizophrenia risk ~7%.
- **Population stratification:** different populations have different allele frequencies AND different environments. Without careful correction, GWAS can find "genetic" associations that are actually confounders of ancestry and environment. Modern GWAS use principal components of genetic ancestry to control for this — connecting your PCA knowledge (Lessons 8-9) directly to genetics.
- **The "missing heritability" problem:** GWAS hits explain much less variance than twin studies predict. This gap is narrowing but remains. Explanations include: rare variants not captured by GWAS, gene-gene interactions, gene-environment interactions, and inflated twin-study estimates.

#### The Nature-Nurture Debates You'll See Online

- **The genetic essentialist claim:** "[Group difference in trait X] is genetic because heritability is high." This is a LOGICAL ERROR. High within-group heritability doesn't tell you about between-group causes.
- **The blank slatist claim:** "Genes don't matter for [trait X] because environment is important." Also wrong. The question isn't either/or — it's how much of the observed variation is associated with each.
- **What the data actually show (for most complex traits):** both genetic and environmental factors contribute. Gene-environment interactions mean the answer depends on context. Causal inference from observational genetics is very hard.
- **Your role as a statistical adjudicator:** you're not resolving nature vs. nurture. You're asking: "Does this specific statistical claim follow from this specific evidence?" Usually the answer is "not as cleanly as the claimant suggests."

### Epidemiology — Reading Health Claims

#### The Typical Epidemiology Study

- **Observational study:** researchers collect data on exposure (diet, behavior, environmental factors) and outcome (disease, death, recovery). Usually a cohort study or case-control study.
- **The analysis:** regression (logistic for binary outcomes, Cox for survival data) with "adjustment" for confounders.
- **Reported as:** "exposure X was associated with [relative risk / odds ratio / hazard ratio] for outcome Y, after adjusting for age, sex, BMI, smoking, alcohol, and socioeconomic status."

#### How to Evaluate Epidemiological Claims

The Bradford Hill criteria (1965, still useful):

1. **Strength of association:** OR = 1.1 is weak; OR = 10 is strong. Weak associations are more likely to be confounders.
2. **Consistency:** has it been found in multiple studies, populations, and methods?
3. **Specificity:** does the exposure specifically lead to this outcome?
4. **Temporality:** does the cause precede the effect? (essential)
5. **Biological gradient (dose-response):** more exposure → more effect?
6. **Plausibility:** is there a biological mechanism?
7. **Coherence:** does it fit with what else we know?
8. **Experiment:** is there experimental evidence (RCTs)?
9. **Analogy:** are there similar cause-effect relationships?

- **In practice:** no single criterion is sufficient. Strong associations with dose-response relationships, multiple replications, temporal ordering, and biological plausibility are convincing. Weak associations found once with no mechanism are suspicious.

#### Nutrition Science — A Cautionary Tale

- **Almost all nutrition epidemiology is observational.** You can't randomize people to eat specific diets for 20 years.
- **Confounders are everywhere.** People who eat more vegetables are also richer, better educated, exercise more, and smoke less.
- **Food frequency questionnaires** are notoriously inaccurate. People can't accurately recall what they ate.
- **Publication bias:** "Red wine prevents heart disease!" gets published and shared. "Red wine has no effect" doesn't.
- **The result:** nutrition claims flip constantly. Eggs are bad, then good, then bad again. The underlying effects (if any) are small, confounders are massive, and measurement is poor.

### Meta-Analysis — Combining Studies

- **What it does:** statistically combines results from multiple studies of the same question to get a more precise estimate.
- **Forest plots:** the standard visualization. Each study is a line (estimate ± CI), and the combined estimate is a diamond at the bottom. You should be able to read these.
- **Heterogeneity (I²):** measures how much studies disagree. I² > 75% = high heterogeneity, meaning the studies may not be measuring the same thing.
- **Publication bias detection:** funnel plots show whether small studies with null results are missing (they often are). Egger's test quantifies this.
- **Garbage in, garbage out:** combining 20 bad studies doesn't give you a good answer. If every study has the same confounder, meta-analysis preserves the bias.
- **Systematic reviews > meta-analyses:** the systematic review (structured search + quality assessment) is more important than the numerical combination. A meta-analysis without rigorous study selection is just a weighted average of garbage.

### The Adjudication Framework — Your Checklist

When you encounter a statistical claim online, run through this:

**Step 1: What's the claim?** Restate it precisely. Is it causal or correlational?

**Step 2: What's the evidence?** What kind of study? (RCT, cohort, cross-sectional, case report?) Where in the evidence hierarchy is it?

**Step 3: What's the effect size?** Not just "significant" — how BIG is the effect? Is it meaningful in practice?

**Step 4: What could go wrong?**
  - Confounders? Draw a quick mental DAG.
  - Multiple comparisons? How many tests were run?
  - Selection bias? Who's in the sample?
  - Reverse causation? Could the "effect" cause the "cause"?
  - Ecological fallacy? Are they inferring individual-level claims from group-level data?

**Step 5: Has it been replicated?** One study means almost nothing. Consistent evidence across multiple studies, methods, and populations is what matters.

**Step 6: Who's making the claim and why?** Not ad hominem — but incentives matter. Researchers need publications. Companies need positive results. Advocacy groups need supporting evidence. Adjust your prior accordingly.

## 📺 Watch — Primary

1. **StatQuest — "GWAS (Genome-Wide Association Studies), Clearly Explained"**
   - https://www.youtube.com/results?search_query=statquest+gwas+clearly+explained
2. **Numberphile — "Problems with Observational Studies"**

## 📺 Watch — Secondary

4. **Robert Sapolsky — Stanford Human Behavioral Biology Lectures** (select lectures on heritability)
   - https://www.youtube.com/results?search_query=robert+sapolsky+behavioral+genetics+lecture
   - *Sapolsky is masterful at explaining gene-environment interactions.*
5. **StatQuest — "Odds Ratios, Clearly Explained"**
6. **3Blue1Brown — "The medical test paradox"** (review from Lesson 23)

## 📖 Read — Primary

- **"Calling Bullshit" by Bergstrom & West** — Full book
  - https://www.callingbullshit.org/
  - *THE book for adjudicating statistical claims. Covers genetics, epidemiology, big data, and media reporting.*
- **"Blueprint: How DNA Makes Us Who We Are" by Robert Plomin** — Chapters 1–5
  - *The behavior genetics perspective. Read critically — Plomin is bullish on genetic determinism. Good for understanding what heritability studies actually find.*

## 📖 Read — Secondary

- **"She Has Her Mother's Laugh" by Carl Zimmer** — excellent popular science on heredity
- **"Behave" by Robert Sapolsky** — Chapters on genes, environment, and their interaction. Long but transformative.
- **Ben Goldacre — "Bad Science" and "Bad Pharma"** — how statistics get abused in medicine
- **"Race, Monogamy, and Other Lies They Told You" by Agustín Fuentes** — critical reading on biological claims in social debates

## 📖 Read — Going Deep

- **"Introduction to Genetic Epidemiology" (online courses)**
  - https://www.coursera.org/courses?query=genetic+epidemiology
- **"Statistical Methods in Genetic Epidemiology" by Thomas** — the technical reference
- **International Genetic Epidemiology Society (IGES)** resources

## 🔨 Do

- **Heritability calculator:** simulate a population where a trait is determined by 50 genetic variants + environment. Vary the environmental noise. Show how heritability changes while the genes stay the same.
- **GWAS simulation:** generate 10,000 individuals with 1000 SNPs. Make 10 SNPs truly causal. Run association tests on all 1000. Apply Bonferroni correction. How many true hits do you find? How many false positives?
- **Meta-analysis exercise:** find a Cochrane review on a health intervention. Read the forest plot. Identify: the overall effect estimate, the confidence interval, the heterogeneity (I²), and whether any individual studies disagree with the consensus.
- **Adjudication practice (do 5 of these):** find statistical claims on Twitter/Reddit about:
  1. A genetics/heritability claim
  2. A nutrition/health claim
  3. A psychology/social science claim
  4. An AI capabilities claim
  5. A policy/economics claim
  For each, apply the 6-step adjudication framework. Write up your analysis in a paragraph.
- **Key exercise:** Take the most contentious statistical claim you've seen online recently. Apply everything from Lessons 24–28: identify the study design, the effect size, potential confounders, the appropriate causal model, what the evidence actually supports vs. what's being claimed. Write 500 words. This is the skill the entire phase was building toward.

## 🔗 ML Connection

- **GWAS methodology parallels feature selection in ML.** Testing millions of features for association, correcting for multiple comparisons, and building polygenic/aggregate scores is conceptually similar to selecting features for a model.
- **Population stratification correction** uses PCA on genetic data — the exact eigendecomposition from Lessons 8-9, applied to genetic similarity matrices.
- **ML for genomics** is a growing field: deep learning models predict gene expression, protein structure, and disease risk from genetic sequence data.
- **Benchmark evaluation** in ML should use the same rigor as clinical trials: pre-registered evaluations, proper test sets, confidence intervals, and replication.

## 🧠 Alignment Connection

- **AI capabilities evaluation** is epidemiology for AI. "Does this model have [dangerous capability]?" requires the same statistical rigor as "Does this drug work?" Effect sizes, sample sizes, and confounders all apply.
- **The genetics of alignment:** understanding heritability and gene-environment interaction gives you a framework for thinking about nature vs. training in AI systems. How much of a model's behavior comes from the architecture (its "genes") vs. the training data (its "environment") vs. the interaction?
- **Reading the alignment literature critically:** alignment researchers make empirical claims ("RLHF reduces harmful outputs by X%"). You now have the tools to evaluate those claims rigorously.
- **AI risk estimation** uses the same kind of base rate reasoning, prior-updating, and evidence evaluation that this entire phase covers. When someone claims "there's a 10% chance of AI catastrophe," you can ask: what evidence is this based on? What's the model? How sensitive is it to assumptions?
