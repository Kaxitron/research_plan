# Lesson 33: Experimental Design and Common Statistical Fallacies

[← Hypothesis Testing](lesson-32-hypothesis-testing.md) | [Back to TOC](../README.md) | [Next: Regression →](lesson-34-regression.md)

---

> **Why this lesson exists:** Knowing what a p-value means is necessary but not sufficient. Most flawed statistical claims don't fail because someone ran the wrong test — they fail because the study was designed badly, the data was collected with hidden biases, or the conclusion commits a well-known fallacy. This lesson gives you the vocabulary to immediately spot 80% of the bad statistics you'll encounter on Twitter, Reddit, and in papers. It also matters for alignment: designing evaluations for AI systems is experimental design, and all these failure modes apply.

## 🎯 Core Concepts

### What Makes a Study Reliable?

- **Randomization:** subjects assigned to treatment/control randomly. This is THE gold standard because it balances all confounders — known and unknown. Without randomization, you can't tell if the treatment caused the outcome or if some hidden variable did.
- **Control groups:** you need a comparison. "Patients who took the drug got better" means nothing without knowing how patients NOT taking the drug did.
- **Blinding:** single-blind (subjects don't know their group), double-blind (researchers don't know either). Without blinding, expectations contaminate results (placebo effect, observer bias).
- **Pre-registration:** publishing your analysis plan before collecting data. Prevents p-hacking and outcome-switching. If a study wasn't pre-registered, be more skeptical.
- **Sample size:** bigger is better, but you can calculate exactly how big using power analysis. Many studies are too small to detect the effects they're looking for.

### The Hierarchy of Evidence

From weakest to strongest:

1. **Anecdotes / case reports** — "My uncle took X and got better." Utterly useless for causal claims.
2. **Cross-sectional studies** — snapshot at one time. Can show correlations, not causes.
3. **Case-control studies** — compare people with an outcome to those without. Retrospective, prone to recall bias.
4. **Cohort studies** — follow people forward in time. Better than case-control but still observational.
5. **Randomized Controlled Trials (RCTs)** — the gold standard for causal inference.
6. **Systematic reviews / meta-analyses** — combine multiple RCTs systematically.

- **The key principle:** you go up this hierarchy when you need stronger causal evidence. You go down when RCTs are impractical or unethical (you can't randomly assign people to smoke for 30 years).
- **Observational vs. experimental:** if you can't randomize, you're stuck with observational data and must deal with confounders explicitly.

### The Common Fallacies You'll See Everywhere

#### Correlation ≠ Causation (and its subtleties)

- **Everyone knows this slogan, but most people can't apply it.** When someone posts "countries with more chocolate consumption win more Nobel Prizes" and another person replies "correlation isn't causation" — that's the easy case.
- **The hard cases:** when there IS a causal story that sounds plausible. "Students who eat breakfast get better grades." Plausible that breakfast helps. But also plausible that families who provide breakfast are higher-income, more structured, etc. The correlation is real; the cause is ambiguous.
- **Confounders:** a third variable that causes both the observed "cause" and "effect." Poverty confounds almost everything in social science.

#### Simpson's Paradox

- **A trend that appears in several groups REVERSES when the groups are combined.** This is not rare — it's common.
- **Classic example:** a treatment appears better in men AND better in women, but worse overall. How? If more severe cases are men, and men get the new treatment more, the overall numbers get skewed.
- **Why it matters:** if you see someone presenting aggregate statistics without subgroup analysis (or vice versa), ask which level is appropriate. The answer depends on whether the grouping variable is a confounder.
- **The lesson:** always ask "what happens when we break this down by [obvious grouping variable]?"

#### Survivorship Bias

- **Looking only at the survivors/successes and drawing conclusions.** "College dropouts like Bill Gates and Zuckerberg became billionaires, so dropping out must be fine." You don't see the millions who dropped out and failed.
- **In ML:** "Our model succeeded on the deployment examples we tested" — but you only tested examples that made it to deployment. What about the ones that were filtered out?

#### Base Rate Neglect (The Prosecutor's Fallacy)

- **Ignoring how common the condition is in the population.** You already know this from Bayes' theorem (Lesson 23), but it's worth seeing the classical version.
- **Example:** A test for a rare disease has 99% sensitivity and 99% specificity. The disease affects 1 in 10,000. You test positive. The probability you have the disease is about 1% — not 99%. Almost all positives are false positives.
- **In genetic debates:** "This SNP is associated with [trait] at p < 0.001" — but if you tested 1 million SNPs, you expect 1000 false positives.

#### Ecological Fallacy

- **Inferring individual-level relationships from group-level data.** "Countries with higher average income have lower crime rates" does NOT mean "rich individuals commit less crime." The relationship at the group level can be completely different from the individual level.
- **In genetics discussions:** this is CRUCIAL. Population-level differences in some trait (e.g., average height between countries) tell you essentially nothing about the cause of individual differences within a population.

#### Regression to the Mean

- **Extreme observations tend to be followed by less extreme ones, purely due to randomness.** If a student scores very high on one test, they'll likely score lower on the next — not because they got worse, but because their first score included positive luck that's unlikely to repeat.
- **This fools people constantly:** "We intervened with the worst-performing students, and they improved!" They probably would have improved anyway. "Sports Illustrated jinx" = athletes on the cover perform worse afterward. They were already at an extreme.
- **To detect a real effect, you need a CONTROL GROUP.** Without one, regression to the mean masquerades as a treatment effect.

#### Berkson's Paradox

- **When you condition on a variable that's affected by both your variables of interest, you create a spurious correlation.** Among hospitalized patients, diseases A and B appear correlated — because people with neither don't end up in your sample.
- **In ML:** training data selection creates Berkson's paradox. If you only study models that passed a performance threshold, you'll see spurious relationships between model properties.

### Sampling and Selection

- **Random sampling:** every member of the population has equal chance of being selected. In practice, almost never achieved.
- **Convenience sampling:** using whoever's available (college students, online volunteers). Very common, very biased.
- **Selection bias:** the sample systematically differs from the population you care about. All ML benchmarks suffer from this.
- **Attrition / dropout:** if participants leave a study non-randomly (sicker patients drop out), results are biased.
- **Response bias:** people answer questions differently depending on how they're asked, who's asking, and what they think you want to hear.
- **Volunteer bias:** people who choose to participate in studies are systematically different from those who don't.

## 📺 Watch — Primary

1. **Veritasium — "Is Most Published Research Wrong?"**
   - https://www.youtube.com/results?search_query=veritasium+is+most+published+research+wrong
   - *The replication crisis, base rates, and why we should expect most findings to be false.*
2. **MinutePhysics — "Simpson's Paradox"**
   - https://www.youtube.com/results?search_query=minutephysics+simpsons+paradox
   - *Quick, visual, correct.*
3. **StatQuest — "Experimental Design, Clearly Explained"**
   - https://www.youtube.com/results?search_query=statquest+experimental+design

## 📺 Watch — Secondary

4. **Primer (YouTube) — "Survivorship Bias"**
5. **Numberphile — "Simpson's Paradox"**
6. **Cassie Kozyrkov — "What's Wrong with A/B Testing?"**
   - Connects experimental design to tech/ML applications

## 📖 Read — Primary

- **"Statistics Done Wrong" by Alex Reinhart** — Chapters on base rate fallacy, pseudoreplication, and researcher degrees of freedom
  - https://www.statisticsdonewrong.com/
- **"Calling Bullshit" by Bergstrom & West** — Chapter on causality and selection bias
  - https://www.callingbullshit.org/
  - *Textbook literally designed for adjudicating statistical claims in the wild. Based on a UW course.*

## 📖 Read — Secondary

- **Judea Pearl — "The Book of Why," Chapters 1–3** — accessible introduction to thinking causally
- **Andrew Gelman & Eric Loken — "The garden of forking paths" (2013)**
  - https://www.stat.columbia.edu/~gelman/research/unpublished/p_hacking.pdf
  - *Why p-hacking doesn't require intentional fraud.*
- **"Why Most Published Research Findings Are False" by John Ioannidis (2005)**
  - https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124
  - *The most-cited paper in PLoS Medicine. Uses math (base rates + power) to show the surprising result.*

## 📖 Read — Going Deep

- **Cochrane Handbook for Systematic Reviews** — the gold standard methodology for evidence synthesis
  - https://training.cochrane.org/handbook
- **"Thinking, Fast and Slow" by Daniel Kahneman** — cognitive biases that produce bad statistical reasoning

## 🔨 Do

- **Simpson's Paradox generator:** create a dataset where treatment A beats B in every subgroup but B beats A overall. Visualize it. Understand why it happens (different group sizes + different baseline rates).
- **Survivorship bias simulator:** simulate 1000 startup founders. Give each a random "talent" and random "luck." Filter to only the successes (top 5% of outcome). Show that among successes, talent and luck appear negatively correlated (Berkson's paradox). Now ask: "Do the most talented founders have the least luck?" No — you just can't see the talented failures.
- **Confounding demo:** generate data where X causes Y, but Z causes both X and Y. Show that the naive correlation between X and Y is biased. Then "control for" Z and see the true effect.
- **Key exercise:** Find a headline from a real news article making a causal claim from observational data. Identify: (1) what confounders might exist, (2) whether it's an ecological fallacy, (3) what study design would be needed to establish causation, (4) what the effect size is (if reported). Write a paragraph-long critique. Do this 3 times with different articles.

## 🔗 ML Connection

- **Benchmark gaming** is survivorship bias: we only see the models and methods that score highest. Hundreds of approaches that didn't work never get published.
- **A/B testing at scale** (how tech companies evaluate model changes) is experimental design. Understanding randomization, power, and multiple testing directly applies.
- **Distribution shift** between training and deployment is a selection bias problem: the training data isn't representative of deployment conditions.
- **Simpson's paradox appears in model evaluation:** a model can be better on every subgroup but worse overall if the subgroups are differently distributed.

## 🧠 Alignment Connection

- **Evaluating AI safety claims** requires experimental design literacy. If someone says "we tested the model on 100 adversarial prompts and it passed," you need to ask about the selection of prompts, the power of the test, and whether the evaluation was pre-registered.
- **Confounders in alignment research:** "models trained with RLHF are safer" — is that because of RLHF specifically, or because RLHF models also tend to be larger, more recent, and from better-resourced labs?
- **The AI safety evaluation hierarchy:** just like medical evidence has RCTs > observational studies, AI safety evidence should be ranked by rigor. Anecdotes ("I jailbroke it once") < red-teaming < systematic evaluation < formal verification.
