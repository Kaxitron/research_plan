# Lesson 58: Neural Scaling Laws and Emergence

[← AlexNet and ConvNets](lesson-57-alexnet-convnets.md) | [Back to TOC](../README.md) | [Next: Attention →](lesson-59-attention.md)

---

**Welch Ch. 6 | Hours: 10-12h | Prereqs: [44]**

## Core Learning

- Kaplan scaling laws: loss scales as a power law with model size, L(N) is proportional to N^{-alpha}
- Loss also scales as a power law with dataset size and compute budget
- Chinchilla compute-optimal training: for a fixed compute budget, there is an optimal ratio of model size to data
- The Chinchilla result: most large models before 2022 were significantly undertrained relative to their size
- Emergent capabilities: abilities that appear suddenly at certain scales (e.g., chain-of-thought reasoning, arithmetic)
- The measurement artifact debate: are emergent capabilities real discontinuities, or artifacts of how we measure performance?
- Phase transitions in learning: some capabilities may require a critical mass of parameters before they become possible

## Watch -- Primary

1. **Welch Labs -- Scaling Laws video (Ch. 6 video)**
   - *Covers how loss predictably decreases with scale, and the surprising emergence of capabilities at certain thresholds.*

## Watch -- Secondary

2. **Relevant research talks on emergence and scaling**
   - *Search for talks by Jason Wei (Google) on emergent abilities, or Ethan Dyer (Google DeepMind) on scaling laws. The debate is active and evolving.*

## Read

- **Welch Labs -- *The Illustrated Guide to AI*, Ch. 6: Scaling Laws**
  - http://www.welchlabs.com/resources/ai-book
  - *The book chapter on scaling laws and their implications.*
- **Kaplan et al. -- "Scaling Laws for Neural Language Models"**
  - https://arxiv.org/abs/2001.08361
  - *The original OpenAI paper establishing power-law relationships between loss and model size, dataset size, and compute.*
- **Hoffmann et al. -- "Training Compute-Optimal Large Language Models" (Chinchilla)**
  - https://arxiv.org/abs/2203.15556
  - *The DeepMind paper that showed most models were undertrained and established compute-optimal scaling ratios.*

## Do

**1. Plot scaling laws from published data**

Using data from the Kaplan et al. paper (Table 1 or digitized from figures), create three log-log plots:
- Test loss vs. parameter count (at fixed data and compute)
- Test loss vs. dataset size (at fixed model and compute)
- Test loss vs. compute budget (optimally allocated)

Each should show a straight line on log-log axes — that's the power law.

**2. Fit power laws**

For each plot, fit `L(x) = a * x^(-alpha) + L_irreducible` using `scipy.optimize.curve_fit`. Print the exponents and compare to Kaplan's published values (α_N ≈ 0.076, α_D ≈ 0.095, α_C ≈ 0.050).

**3. Reproduce the Chinchilla frontier**

Using the Chinchilla paper's formula for compute-optimal training (`N_opt ∝ C^0.5`, `D_opt ∝ C^0.5`), plot the optimal model size and dataset size as functions of compute budget. Mark where GPT-3 (175B params, 300B tokens) and Chinchilla (70B params, 1.4T tokens) sit relative to the frontier. GPT-3 should be clearly above the optimal line (too large for its data budget).

**4. Emergence discussion (written, ~200 words)**

Write up in comments or a markdown cell: are emergent capabilities real discontinuities or measurement artifacts? Cite the Schaeffer et al. (2023) paper arguing they're artifacts of metric choice, and the Wei et al. response. Take a position and explain why it matters for alignment forecasting.

## ML & Alignment Connection

Scaling laws suggest capabilities grow predictably with compute -- until emergence breaks that prediction. If capabilities can emerge suddenly at certain scales, predicting when a model becomes "too capable" is fundamentally difficult. This is a core alignment challenge: how do you align a system whose capabilities may jump discontinuously?

The Chinchilla result also has alignment implications. Compute-optimal training means frontier models are getting both larger AND better-trained, which accelerates capability growth. If we cannot predict when dangerous capabilities will emerge, we need alignment techniques that work robustly across a wide range of capability levels -- not techniques calibrated to today's models that might break when the next scale-up produces unexpected new abilities. The scaling laws are the empirical foundation for forecasting AI progress, and understanding them is essential for anyone working on alignment timelines.
