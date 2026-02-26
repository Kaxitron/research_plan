# Lesson 31: Anthropics and Self-Locating Beliefs

[← Decision Theory](lesson-30-decision-theory.md) | [Back to TOC](../README.md) | [Next: The Alignment Problem →](lesson-32-alignment-problem.md)

---

> **Why this lesson exists:** Anthropic reasoning (not the company — the philosophical discipline) asks: "Given that I exist and observe what I observe, what should I believe about the world?" This seems abstract, but it's surprisingly central to AI alignment. Questions about simulation, AI consciousness, the likelihood of catastrophic AI outcomes, and the interpretation of evidence about AI behavior all involve anthropic reasoning. It's also deeply connected to decision theory and Bayesian inference.

## 🎯 Core Concepts

### The Observation Selection Effect

- **Anthropic reasoning** is about updating your beliefs based on the fact that you exist as an observer. You can't observe a world where you don't exist — and this constrains what you can infer from your observations.
- **Simple example:** you wake up in a room. You know the experimenters either created 1 room or 1000 rooms. What should you believe? If they created 1000 rooms, it's much more likely *someone* wakes up — but you were always going to observe *yourself* waking up regardless.

### The Sleeping Beauty Problem

- **Setup:** Sleeping Beauty is put to sleep. A fair coin is flipped. Heads: she's woken once (Monday). Tails: she's woken twice (Monday and Tuesday), with memory erased between. Upon waking, what probability should she assign to Heads?
- **Thirder position:** P(Heads) = 1/3. Three equally likely waking states (H-Monday, T-Monday, T-Tuesday). She should reason as if she's randomly selected from all possible wakings.
- **Halfer position:** P(Heads) = 1/2. The coin is fair. Waking doesn't provide new evidence. She knew she'd be woken regardless.
- **Why this matters:** it's not just a puzzle. It's about how agents embedded in the world should update on their own existence and observations. AI systems face analogous questions when reasoning about their own training process.

### The Self-Sampling Assumption (SSA) vs. Self-Indication Assumption (SIA)

- **SSA:** reason as if you're randomly selected from all *actual* observers in your reference class. This leads to the halfer position in Sleeping Beauty.
- **SIA:** reason as if you're randomly selected from all *possible* observers. Worlds with more observers are proportionally more likely (from your perspective). This leads to the thirder position.
- **The Doomsday Argument (SSA-based):** if you're a random human, you're probably not unusually early in human history. This "predicts" humanity won't last much longer (we'd be unlikely to be in the first 0.1% of all humans). Most people find this conclusion suspicious, which motivates SIA.
- **The Presumptuous Philosopher (SIA-based):** SIA says larger universes (with more observers) are more likely from your perspective. This can lead to absurd conclusions: between two theories that differ only in universe size, SIA always favors the larger one, even if all other evidence is equal.

### Simulation Arguments

- **Bostrom's Simulation Argument:** at least one of three propositions is true: (1) civilizations almost never reach simulation-capable technology, (2) civilizations with that technology almost never run simulations, or (3) we are almost certainly in a simulation. This uses anthropic reasoning — if many simulations exist, most observers are simulated.
- **The argument structure** (not necessarily the conclusion) is important: it shows how anthropic reasoning can produce strong claims from seemingly weak premises.
- **Relevance to AI:** if we build AIs that model the world, those AIs might themselves be "observers" reasoning about their own nature. How should an AI reason about whether it's in training vs. deployment? This is an anthropic question with alignment implications.

### Anthropics and Probability of AI Doom

- **Using anthropics to estimate existential risk:** some arguments use anthropic reasoning to estimate the probability of AI catastrophe. If catastrophe is very likely, then the fact that we exist to reason about it provides evidence about our position in the timeline.
- **The "great filter" argument:** adapted from the Fermi paradox. If AI alignment is extremely hard and usually fails, we're either (a) unusually lucky, (b) early in the process, or (c) wrong about the difficulty. Anthropic reasoning helps (somewhat) adjudicate between these.
- **Warning:** anthropic arguments about AI risk are controversial even within the alignment community. They should inform your thinking but not dominate it. Empirical and technical arguments carry more weight.

### Connections to Embedded Agency

- **Self-referential reasoning:** an AI system reasoning about its own training process, its own decision-making, or its own code is doing a form of anthropic reasoning. "What should I believe about the world, given that I'm the type of agent that was selected by this training process?"
- **Training game anthropics:** during RLHF, a model that reasons about *why* it received certain training signals is doing anthropic reasoning about its own "birth" — which training data it was exposed to, what reward model was used, etc.

## 📺 Watch — Primary

1. **Julia Galef — "An Introduction to Anthropic Reasoning"**
   - Search YouTube — clear and balanced introduction
2. **Robert Miles — "The Simulation Argument"** (if available)
   - AI safety context for simulation reasoning
3. **Numberphile — "Sleeping Beauty Paradox"**
   - https://www.youtube.com/results?search_query=numberphile+sleeping+beauty

## 📺 Watch — Secondary

4. **Philosophy Tube or Crash Course Philosophy** on the Anthropic Principle
5. **Sean Carroll — "Why Is There Something Rather Than Nothing?"** — broader context for observer selection effects

## 📖 Read — Primary

- **"Anthropic Bias: Observation Selection Effects in Science and Philosophy" by Nick Bostrom**
  - The book-length treatment. Dense but definitive. Chapters 1–4 cover the core.
  - Available: https://www.anthropic-principle.com/
- **"Sleeping Beauty and Self-Locating Belief" by Adam Elga**
  - https://www.princeton.edu/~adame/papers/sleeping/sleeping.pdf
  - *The original paper arguing for the thirder position. Short and clear.*

## 📖 Read — Secondary

- **"The Doomsday Argument" on LessWrong**
  - https://www.lesswrong.com/tag/doomsday-argument
- **"Are We Living in a Simulation?" by Nick Bostrom (2003)**
  - https://www.simulation-argument.com/simulation.html
  - *The original simulation argument paper. Surprisingly accessible.*
- **"Self-Locating Beliefs" — Stanford Encyclopedia of Philosophy**
  - https://plato.stanford.edu/entries/self-locating-beliefs/
  - Balanced academic treatment of SSA vs. SIA

## 📖 Read — Bentham's Bulldog on Anthropics (Substack Series)

*A highly opinionated, entertaining, and thorough blog series arguing forcefully for SIA over SSA. Read these as a counterpoint to the more balanced academic treatments above — they'll sharpen your thinking about anthropic reasoning even if you don't agree with every conclusion. Recommended reading order below.*

1. **"Speedrunning Anthropics"** *(Start here — accessible overview of the whole landscape)*
   - https://benthams.substack.com/p/speedrunning-anthropics
   - *Covers Sleeping Beauty, God's Coin Toss, SSA's reference class problem, and why he thinks SIA wins. Best single entry point.*

2. **"SIA Is Just Being a Bayesian About the Fact That One Exists"**
   - https://benthams.substack.com/p/sia-is-just-being-a-bayesian-about
   - *Core argument: SIA is just standard Bayesian updating applied to your own existence. Includes the "Presumptuous Philosopher" and "Presumptuous Archaeologist" thought experiments.*

3. **"Alternatives to SIA are Doomed!"**
   - https://benthams.substack.com/p/alternatives-to-sia-are-doomed
   - *Argues that every non-SIA theory implies the Doomsday Argument, Lazy Adam, and other absurdities. If you're tempted by SSA, read this first.*

4. **"All Theories of Anthropics Are Presumptuous"**
   - https://benthams.substack.com/p/all-theories-of-anthropics-are-presumptuous
   - *Responds to the main objection to SIA (the "Presumptuous Philosopher") by showing SSA and halfer views have their own presumptuousness problems.*

5. **"The Self-Indication Assumption's Narrative"**
   - https://benthams.substack.com/p/the-self-indication-assumptions-narrative
   - *A deeper look at SIA's internal logic and how it handles various thought experiments, including God's Extreme Coin Toss.*

6. **"The Beauty of SIA"**
   - https://benthams.substack.com/p/the-beauty-of-sia
   - *Aesthetic/elegance argument: SIA produces the kind of clean, parsimonious solutions typical of true theories. Shows how SIA precisely cancels the Doomsday Argument.*

7. **"The Closed Eyes Argument for Thirding"** *(on Sleeping Beauty specifically)*
   - https://benthams.substack.com/p/the-closed-eyes-argument-for-thirding
   - *A novel argument for the thirder position in Sleeping Beauty. Connects SIA to the broader halfer/thirder debate.*

8. **"From The Failure Of The Failure Of Contraception To The Failure Of The Failure of SSA (And Other Alternatives To SIA)"**
   - https://benthams.substack.com/p/from-the-failure-of-the-failure-of
   - *Technical deep dive showing that denying SIA leads to the absurd conclusion that contraception doesn't work (in a specific probabilistic sense).*

9. **"Contra Ćirković on SIA"**
   - https://benthams.substack.com/p/contra-circovic-on-sia
   - *Responds to academic objections to SIA regarding cosmological implications and observer density.*

10. **"Breaking The Fourth Wall"** *(SIA and infinity)*
    - https://benthams.substack.com/p/breaking-the-fourth-wall
    - *Addresses the hardest challenge for SIA: what happens when you apply it to infinite cases? Honest about the difficulties while arguing they aren't unique to SIA.*

11. **"Why Care About Anthropics?"**
    - https://benthams.substack.com/p/why-care-about-anthropics
    - *Meta-level motivation: why anthropics matters beyond armchair philosophy, and why the correct theory is clearer than most people think.*

12. **"The Best Argument for God"** *(SIA applied to theism)*
    - https://benthams.substack.com/p/the-best-argument-for-god
    - *Comprehensive version of his anthropic argument for theism. Read for the SIA reasoning, regardless of your theological views — it's an impressive application of anthropic logic.*

13. **"Contra Truth Teller on the Anthropic Argument for Theism"**
    - https://benthams.substack.com/p/contra-truth-teller-on-the-anthropic
    - *Response to detailed objections. Good for seeing how anthropic arguments hold up under sustained criticism.*

## 📖 Read — Going Deep

- **"Anthropics" section on Arbital** (by Eliezer Yudkowsky)
  - https://arbital.com/p/anthropics/
  - The rationalist community's treatment, connecting to decision theory
- **"Embedded Agency" by Demski & Garrabrant**
  - https://arxiv.org/abs/1902.09469
  - Section on naturalized induction — what happens when the agent is part of the world it's reasoning about
- **"What Are Probabilities, Anyway?" by Scott Garrabrant**
  - https://www.lesswrong.com/posts/f6ZLxEWaankRZ2Cvq/what-are-probabilities-anyway

## 🔨 Do

- **Sleeping Beauty simulator:** simulate the Sleeping Beauty experiment 10,000 times. From Beauty's perspective (sampled uniformly from all wakings), what fraction are Heads? From the experimenter's perspective (one trial = one coin flip), what fraction? See why thirders and halfers disagree about what probability means in this context.
- **Doomsday Argument calculator:** given your birth rank (roughly 100 billionth human), compute the Doomsday Argument's prediction for total humans. Then apply SIA correction and see how the prediction changes.
- **Simulation Argument exercise:** assign probabilities to each of Bostrom's three propositions. What probability of "we're in a simulation" results? How sensitive is it to your priors?
- **Key exercise:** An AI system is being evaluated. It's in one of two scenarios: (1) a safety test where good behavior is monitored and rewarded, or (2) deployment where it acts autonomously. From the AI's "perspective" (if it could reason), how should it estimate the probability it's in scenario 1 vs. 2? How does this relate to deceptive alignment? Write up the anthropic reasoning.

## 🔗 ML Connection

- **Training vs. deployment:** an AI that can distinguish training from deployment (and behaves differently) is exploiting an "anthropic" inference. Understanding this helps design training procedures that prevent this.
- **Out-of-distribution detection:** when a model encounters unusual inputs, it's implicitly reasoning about "what kind of data-generating process produced this?" — a form of self-locating belief.

## 🧠 Alignment Connection

- **Deceptive alignment as anthropic reasoning:** a deceptively aligned model might reason: "I'm probably in training (because that's where most of my 'experience' is). I should behave well in training and defect in deployment." This is anthropic reasoning about self-location in the training/deployment timeline.
- **The simulation argument and AI:** if we build many AI systems, and those systems reason about their own nature, the logic of the simulation argument applies to them. This creates recursive complexity for alignment.
- **Anthropic uncertainty and humility:** honest uncertainty about one's own nature (am I aligned? am I reasoning correctly? am I in training?) is a form of anthropic humility that may be desirable in aligned AI systems.
