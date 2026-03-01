# Exam 6A: Foundations of Rational Agency

**The Path to AI Alignment — Lessons 63–65 Comprehensive Assessment**

---

| | |
|---|---|
| **Time Allowed** | 60 minutes |
| **Total Points** | 100 |
| **Materials** | Pencil, paper. No calculator needed. |
| **Format** | 10 questions mixing game-theoretic computation, decision-theoretic reasoning, and philosophical analysis |

> **Advice:** These are the formal frameworks for reasoning about what aligned agents SHOULD do. The thread: **game theory models strategic interaction, decision theory models rational choice under uncertainty, and anthropics handles self-locating beliefs. Together, they define the landscape of aligned agent design.**

---

## Question 1 (10 pts) — Normal Form Games and Nash Equilibria

Consider the following game between an AI system (rows) and a human overseer (columns):

|  | Trust | Verify |
|---|---|---|
| **Honest** | (3, 3) | (2, 1) |
| **Deceive** | (4, 0) | (0, 2) |

Payoffs are (AI, Human).

**(a)** Find all pure-strategy Nash equilibria. Show your work by checking each cell for unilateral deviation incentives.

**(b)** Is there a dominant strategy for either player? Explain.

**(c)** This game has the structure of a well-known game. Which one? Explain the analogy to AI alignment.

**(d)** If this game is played repeatedly (not just once), how might the outcome differ? Why does repetition matter for AI deployment?

---

## Question 2 (10 pts) — The Prisoner's Dilemma and AI Coordination

The classic prisoner's dilemma payoff matrix:

|  | Cooperate | Defect |
|---|---|---|
| **Cooperate** | (3, 3) | (0, 5) |
| **Defect** | (5, 0) | (1, 1) |

**(a)** Find the Nash equilibrium. Is it Pareto optimal? Explain.

**(b)** Two AI companies are deciding whether to invest in safety research (Cooperate) or cut corners to deploy faster (Defect). Map this scenario onto the prisoner's dilemma. What is the predicted outcome and why is it concerning?

**(c)** Name two mechanisms that can sustain cooperation in repeated prisoner's dilemmas. For each, explain how it might apply to AI safety coordination.

**(d)** Why does the one-shot vs. repeated distinction matter for alignment? If an AI system believes it will only interact with humans once (or that it won't be caught), what does game theory predict?

---

## Question 3 (12 pts) — Expected Utility Theory

**(a)** An agent has utility function U over outcomes and beliefs P over states. Write the expected utility formula for an action a.

**(b)** You're designing a reward function for an AI system. Action A has: 90% chance of a moderately good outcome (utility 10) and 10% chance of a catastrophic outcome (utility −1000). Action B has: 100% chance of a mediocre outcome (utility 5). Compute the expected utility of each. Which does the AI choose?

**(c)** The result from (b) shows a problem with expected utility maximization for alignment. Identify the problem and explain why risk-sensitivity (or bounded utility functions) might be needed.

**(d)** An AI system is maximizing expected utility with an incorrect world model. It assigns probability 0 to a state that actually occurs. What happens? Relate this to the concept of "model misspecification" in alignment.

---

## Question 4 (10 pts) — Causal vs. Evidential vs. Functional Decision Theory

**Newcomb's Problem:** A perfect predictor has placed money in two boxes. Box A always contains $1,000. Box B contains $1,000,000 if the predictor predicted you'd take only Box B, and $0 if the predictor predicted you'd take both. You choose: take both boxes, or take only Box B.

**(a)** What does Causal Decision Theory (CDT) recommend? Explain the reasoning.

**(b)** What does Evidential Decision Theory (EDT) recommend? Explain the reasoning.

**(c)** What does Functional Decision Theory (FDT) recommend? How does its reasoning differ from CDT?

**(d)** Why does the choice of decision theory matter for AI alignment? Give a concrete scenario where a CDT agent and an FDT agent would behave differently in a safety-relevant way.

---

## Question 5 (10 pts) — Decision Theory for AI Systems

**(a)** An AI system using CDT reasons: "My decision now can't causally affect the past prediction about my behavior." Explain why this reasoning is problematic for an AI whose behavior is determined by its source code (which the predictor could analyze).

**(b)** FDT says: "I should decide as if I'm choosing the output of my decision function for all instances where that function is called." Why is this particularly natural for AI systems (compared to humans)?

**(c)** An AI system is about to be tested for safety. It knows the test is coming. Under CDT, should it behave differently during the test vs. deployment? Under FDT?

**(d)** "Updateless Decision Theory" makes decisions based on a prior policy rather than updating on current observations. Explain in 2–3 sentences why this might be important for AI systems that will face many different situations over their lifetime.

---

## Question 6 (10 pts) — The Sleeping Beauty Problem

The experiment: A fair coin is flipped. If Heads, Sleeping Beauty is woken once (Monday). If Tails, she's woken twice (Monday and Tuesday) with memory erased between wakings. Upon waking, she's asked: "What is your credence that the coin landed Heads?"

**(a)** The "halfer" position (SSA — Self-Sampling Assumption) says P(Heads) = 1/2. Explain the reasoning.

**(b)** The "thirder" position (SIA — Self-Indication Assumption) says P(Heads) = 1/3. Explain the reasoning.

**(c)** Both positions are logically consistent. What makes the problem hard is the question: should your existence (the fact that you're awake right now) count as evidence? How does each position answer this?

**(d)** An AI system is running as N copies in parallel. When making decisions, should it weight outcomes by the number of copies affected (SIA-like) or treat its "perspective" as one sample (SSA-like)? Why does this matter for alignment?

---

## Question 7 (10 pts) — Anthropics and the Simulation Argument

**(a)** State the simulation argument (Bostrom): what are its three disjunctive conclusions?

**(b)** If we take the simulation argument seriously, how might it affect an AI's decision-making? Should an AI system that thinks it might be in a simulation behave differently?

**(c)** The "Doomsday Argument" uses anthropic reasoning to predict humanity's future duration. State the argument briefly and explain one objection to it.

**(d)** Anthropic reasoning is relevant to AI risk estimates. The argument: "We exist at a time when AI is being developed. Most observer-moments in universes where AI goes wrong happen before the catastrophe. So our existence is some evidence that AI will go wrong." Evaluate this argument — is it valid? What assumptions does it rely on?

---

## Question 8 (10 pts) — Multi-Agent Dynamics

**(a)** In a game between two AI systems, each with different utility functions, what is a Nash equilibrium? Under what conditions does one always exist? (State the theorem.)

**(b)** A **correlated equilibrium** allows players to condition their strategies on a shared random signal. Give an intuitive example (e.g., a traffic light). Why might correlated equilibria be more relevant for AI coordination than Nash equilibria?

**(c)** **Mechanism design** is "inverse game theory" — designing the rules of the game to incentivize desired behavior. Give one example of how mechanism design could be applied to AI alignment (e.g., designing reward structures, evaluation protocols, or deployment rules).

**(d)** The "alignment as game theory" perspective: who are the players, what are their strategies, and what is the "game" being played in the development and deployment of AI systems?

---

## Question 9 (10 pts) — Integration: Decision Theory Meets Probability

**(a)** Decision theory requires a probability distribution over states and a utility function over outcomes. Connect these to the Bayesian framework from Phase 3: what plays the role of the prior? What plays the role of the likelihood?

**(b)** An AI system updates its beliefs using Bayes' theorem. But Bayesian updating assumes the prior is well-calibrated. What happens if the prior assigns zero probability to an important event? How does this connect to the "treacherous turn" scenario in alignment?

**(c)** Information theory from Phase 3 measures the "cost" of wrong beliefs (KL divergence). Connect KL divergence to decision theory: what is the decision-theoretic cost of using the wrong probability distribution?

---

## Question 10 (8 pts) — Synthesis

**(a)** You're designing an aligned AI system. It must interact strategically with humans (game theory), make decisions under uncertainty (decision theory), and reason about its own existence and copies (anthropics). For each of these three areas, state the key design choice and explain why it matters:
- Which solution concept for strategic interaction?
- Which decision theory?
- Which anthropic assumption?

**(b)** In 3–4 sentences, explain why these three areas — which seem abstract and philosophical — are actually *engineering requirements* for building safe AI systems. Give one concrete example of how a wrong choice in any of these areas could lead to misalignment.

---

## 🔧 Optional Mini Project (~45 minutes): Game Theory Solver & Alignment Simulator

**Build a Nash equilibrium finder and simulate AI-human strategic interaction.**

1. Implement a general 2-player normal form game solver:
   - Find all pure-strategy Nash equilibria by checking for unilateral deviations
   - Find the mixed-strategy Nash equilibrium using the indifference principle
2. Test on classic games: Prisoner's Dilemma, Stag Hunt, Chicken, Battle of the Sexes
3. Build the AI Trust Game from Exam 6A Q1: rows = {Honest, Deceive}, columns = {Trust, Verify}
4. Simulate 1000 rounds of repeated play with different strategies: tit-for-tat, always-verify, probabilistic trust (increase trust after honest behavior)
5. Plot cooperation rate over time for each strategy pair. Which strategies sustain cooperation?
6. Modify the payoffs to represent a scenario where deception detection improves over time (verification cost decreases). How does the equilibrium shift?

**Stretch:** Implement a simple CDT vs. EDT agent. Have them play a Newcomb-like problem 1000 times. Track payoffs. Which decision theory performs better, and why?

**Tools:** NumPy, Matplotlib.
