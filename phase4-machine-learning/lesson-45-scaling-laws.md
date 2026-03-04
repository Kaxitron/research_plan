# Lesson 45: Neural Scaling Laws and Emergence

[← AlexNet and ConvNets](lesson-44-alexnet-convnets.md) | [Back to TOC](../README.md) | [Next: Attention →](lesson-46-attention.md)

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

- Plot scaling law curves from published data: loss vs parameter count, loss vs dataset size, loss vs compute
- Fit power laws to the data and verify the exponents match published results
- Reproduce the compute-optimal frontier from Chinchilla: for a given compute budget, what is the optimal model size and data ratio?
- Discuss and write up: are emergent capabilities real or measurement artifacts? What evidence supports each view?

## ML & Alignment Connection

Scaling laws suggest capabilities grow predictably with compute -- until emergence breaks that prediction. If capabilities can emerge suddenly at certain scales, predicting when a model becomes "too capable" is fundamentally difficult. This is a core alignment challenge: how do you align a system whose capabilities may jump discontinuously?

The Chinchilla result also has alignment implications. Compute-optimal training means frontier models are getting both larger AND better-trained, which accelerates capability growth. If we cannot predict when dangerous capabilities will emerge, we need alignment techniques that work robustly across a wide range of capability levels -- not techniques calibrated to today's models that might break when the next scale-up produces unexpected new abilities. The scaling laws are the empirical foundation for forecasting AI progress, and understanding them is essential for anyone working on alignment timelines.
