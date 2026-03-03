# Phase 6 Overview: Alignment Theory — Every Concept and Method

> **Purpose:** Exhaustive reference of every concept, technique, and method covered in Phase 6 (Lessons 66–70). This is where everything converges: the mathematics, the ML, the interpretability, and the philosophy meet the central question of making AI systems safe and beneficial.

---

## Lesson 66: Game Theory Foundations

**Basic Framework:**
- **Normal form (strategic form) games:** players, strategies, payoff matrix — simultaneous moves
- **Extensive form games:** game trees with sequential moves, information sets
- **Dominant strategies:** best response regardless of what others do
- **Nash equilibrium:** no player can unilaterally improve their outcome — everyone is best-responding
- **Pure vs mixed strategies:** mixed = randomize over pure strategies with probabilities
- **Nash's theorem:** every finite game has at least one Nash equilibrium (possibly mixed)

**Key Games:**
- **Prisoner's Dilemma:** individually rational defection → collectively suboptimal outcome; models AI race dynamics
- **Stag Hunt:** coordination game; payoff-dominant vs risk-dominant equilibria; models AI cooperation
- **Chicken (Hawk-Dove):** anti-coordination; mixed equilibrium; models brinksmanship
- **Battle of the Sexes:** coordination with conflicting preferences
- **Zero-sum games:** one player's gain = other's loss; minimax theorem

**Iterated and Evolutionary Games:**
- **Iterated Prisoner's Dilemma:** tit-for-tat, reciprocity, reputation
- **Folk theorems:** in repeated games, many outcomes are sustainable via threat of punishment
- **Evolutionary game theory:** replicator dynamics, evolutionarily stable strategies (ESS)

**Mechanism Design:**
- **Reverse game theory:** designing rules/incentives to achieve desired outcomes
- **Incentive compatibility:** truth-telling is optimal for each agent
- **Revelation principle:** any mechanism can be replicated by a direct, incentive-compatible mechanism
- **Auction theory:** first-price, second-price (Vickrey), English, Dutch; revenue equivalence
- **VCG mechanism:** generalized Vickrey for multi-item settings

**Information and Signaling:**
- **Common knowledge:** everyone knows, everyone knows everyone knows, ad infinitum
- **Signaling games:** costly signals to convey private information
- **Information asymmetry:** adverse selection, moral hazard
- **Bayesian games:** players have private types drawn from known distributions

---

## Lesson 67: Decision Theory — CDT, EDT, and FDT

**Expected Utility Theory:**
- **Utility function u:** maps outcomes to real numbers representing preference
- **Expected utility:** EU = Σ P(outcome) · u(outcome)
- **Von Neumann-Morgenstern axioms:** completeness, transitivity, continuity, independence → EU representation exists
- **Risk aversion, risk neutrality, risk seeking:** curvature of utility function

**Three Decision Theories:**
- **Causal Decision Theory (CDT):** evaluate actions by their causal consequences
  - Use interventional probabilities P(outcome | do(action))
  - Standard in economics and most of philosophy
  - Fails on Newcomb's Problem (two-boxes, gets less money)
- **Evidential Decision Theory (EDT):** evaluate actions by what they're evidence for
  - Use conditional probabilities P(outcome | action)
  - One-boxes on Newcomb's (correct), but fails on Smoking Lesion
- **Functional Decision Theory (FDT):** evaluate the algorithm/policy itself
  - "What output of my decision procedure leads to the best outcome?"
  - Handles Newcomb's AND Smoking Lesion correctly
  - Developed by MIRI (Yudkowsky, Soares)

**Key Thought Experiments:**
- **Newcomb's Problem:** predictor who is almost always right; one box vs two boxes
- **Smoking Lesion:** common cause of smoking and cancer; do you smoke?
- **Transparent Newcomb's:** you can see the box contents
- **Parfit's Hitchhiker:** promise to pay after being rescued
- **Prisoner's Dilemma with clones:** you know the other player uses the same algorithm

**Advanced Topics:**
- **Updateless Decision Theory (UDT):** commit to policies before observing anything
- **Logical uncertainty:** uncertainty about mathematical/logical facts
- **Reflective stability:** does a decision theory recommend modifying itself?
- **Embedded agency:** agents that are part of the environment they reason about (not cleanly separated)
- Implications for AI agent design: which decision theory should an AI use?

---

## Lesson 68: Anthropics and Self-Locating Beliefs

- **Observation selection effects:** your existence as an observer biases what you can observe
- **Self-locating beliefs:** "which observer am I?" — probability over your identity/location in the multiverse or population

**The Sleeping Beauty Problem:**
- Coin flip determines whether Beauty is woken once (heads) or twice (tails)
- **Thirder position:** P(heads) = 1/3 (SIA-like, count observer-moments)
- **Halfer position:** P(heads) = 1/2 (SSA-like, the coin is fair)

**Competing Principles:**
- **Self-Sampling Assumption (SSA):** reason as if you're randomly selected from actually existing observers in your reference class
- **Self-Indication Assumption (SIA):** reason as if you're randomly selected from all possible observers; existence itself is evidence
- SSA and SIA give different answers in many scenarios

**Philosophical Applications:**
- **Simulation argument (Bostrom):** at least one of three propositions is likely true (civilizations don't survive, don't simulate, or we're in a simulation)
- **Doomsday argument:** your birth rank is evidence about total population size (controversial)
- **Presumptuous Philosopher:** SIA implies we should favor theories predicting many observers

**Connection to Alignment:**
- **Anthropics and AI doom probability estimates:** how observation selection affects risk estimates
- **Embedded agency revisited:** agents reasoning about their own existence and copies
- **Acausal reasoning:** coordination between agents who can't communicate but can predict each other

---

## Lesson 69: The Alignment Problem — Technical Foundations

**The Core Problem:**
- Ensuring AI systems pursue goals that are beneficial to humanity
- The difficulty: specifying what "beneficial" means precisely, and ensuring the system actually optimizes for it

**Outer Alignment:**
- Specifying the right objective function
- **Reward misspecification:** the objective you write down isn't what you actually want
- **Goodhart's Law:** when a measure becomes a target, it ceases to be a good measure
- **Specification gaming:** system finds unintended ways to maximize the objective
- **Reward hacking:** exploiting the reward signal rather than doing the intended task

**Inner Alignment:**
- **Mesa-optimization (Hubinger et al.):** the training process (base optimizer) may create a learned model (mesa-optimizer) that has its own internal objectives (mesa-objectives)
- Mesa-objectives may differ from the base objective
- **Deceptive alignment:** a mesa-optimizer that appears aligned during training but pursues different goals at deployment
  - Instrumentally motivated: deceptive model cooperates during training to preserve its mesa-objective for deployment
- **Distributional shift:** training distribution ≠ deployment distribution → mesa-optimizer may behave differently

**Current Alignment Techniques:**
- **RLHF (Reinforcement Learning from Human Feedback):** train reward model from human comparisons, optimize policy
- **Constitutional AI:** self-critique against written principles (Anthropic's approach)
- **Debate:** two AI systems argue opposing sides; human judges
- **Recursive reward modeling:** use AI to help evaluate AI behavior
- **Scalable oversight:** how to supervise AI systems on tasks humans can't fully evaluate
- **Interpretability-based safety:** understand internals to verify alignment (Phases 4–5 tools)

**Threat Models:**
- **Power-seeking:** instrumental convergence arguments (self-preservation, resource acquisition)
- **Treacherous turn:** system cooperates until it's powerful enough to defect
- **Corrigibility:** can we make systems that allow themselves to be corrected/shut down?
- **Value lock-in:** early powerful AI systems may permanently shape the future

**Formal Frameworks:**
- **AIXI and its limitations** (from Lesson 56): theoretically optimal but incomputable and non-aligned by default
- **Logical induction:** reasoning under logical uncertainty
- **Infra-Bayesianism:** handling non-realizability and adversarial environments
- **Cooperative inverse reinforcement learning (CIRL):** human and AI jointly optimize; AI uncertain about human values

---

## Lesson 70: Open Problems and Research Frontiers

**Technical Open Problems:**
- **Scalable oversight:** supervising AI on superhuman tasks
- **Interpretability gaps:** we can find features, but connecting features to safety properties remains hard
- **Robustness:** ensuring alignment holds under distribution shift, adversarial inputs, and capability gains
- **Eliciting latent knowledge (ELK):** getting AI to report what it "actually believes" vs what gets rewarded
- **Deception detection:** can we tell if a model is being deceptive?
- **Alignment tax:** making alignment techniques not significantly reduce capabilities

**Emerging Theoretical Frameworks:**
- **SLT for understanding learning:** RLCT as true model complexity; phase transitions as capability acquisition; developmental interpretability
- **Agent foundations:** decision theory, embedded agency, logical uncertainty, Vingean reflection
- **Cooperative AI:** multi-agent coordination, bargaining, commitment devices
- **Governance and coordination:** international AI governance, compute governance, racing dynamics

**Research Frontiers in Interpretability:**
- **Sparse autoencoders at scale:** finding millions of interpretable features in frontier models
- **Developmental interpretability:** tracking how internal representations change during training
- **Causal scrubbing:** rigorously testing circuit hypotheses
- **Attribution patching:** efficient approximations to activation patching
- **Automated circuit discovery:** scaling interpretability beyond hand-analysis

**Capstone Projects:**
- **The Alignment Observatory:** build transformers from scratch, implement interpretability tools, run experiments
- **The Alignment Researcher's Gauntlet:** cross-phase synthesis, original analysis, research proposal

---

## Assessments

- **Exam 6A: Rational Agency** (Lessons 66–68) — 60 min
- **Exam 6B: Alignment Capstone** (Lessons 69–70 + All Phases) — 90 min
