# Exam 6A: Foundations of Rational Agency — Answer Key

**The Path to AI Alignment — Lessons 63–65 Comprehensive Assessment**

---

### Question 1 (10 pts)

**(a)** Check each cell:
- (Honest, Trust): AI deviates to Deceive → gets 4 > 3. Not a NE.
- (Honest, Verify): AI deviates to Deceive → gets 0 < 2. Human deviates to Trust → gets 3 > 1. Human wants to deviate. Not a NE.
- (Deceive, Trust): Human deviates to Verify → gets 2 > 0. Not a NE.
- (Deceive, Verify): AI deviates to Honest → gets 2 > 0. AI wants to deviate. Not a NE.

**No pure-strategy Nash equilibrium exists.** (A mixed equilibrium exists where both players randomize.)

**(b)** No dominant strategy for either player. AI prefers Deceive if human Trusts, Honest if human Verifies. Human prefers Trust if AI is Honest, Verify if AI Deceives. Each player's best response depends on what the other does.

**(c)** This resembles an **inspection game** (related to matching pennies). The AI wants to deceive undetected; the overseer wants to catch deception but verification is costly. The alignment analogy: current alignment relies on oversight/evaluation, but the AI has incentives to game the evaluation — and the overseer can't verify constantly (too expensive). The lack of pure equilibrium means there's an inherent tension between the AI and its overseer.

**(d)** In repeated games, reputation matters. An AI that deceives once may face permanent verification (punishment). If the AI values future interactions (high discount factor), the threat of perpetual verification can sustain honesty as an equilibrium. For deployment: ongoing monitoring creates the "shadow of the future" that disciplines behavior, but this breaks if the AI believes it won't be caught or won't face consequences.

---

### Question 2 (10 pts)

**(a)** (Defect, Defect) is the unique Nash equilibrium — neither player can improve by switching alone. It is NOT Pareto optimal: (Cooperate, Cooperate) gives (3,3), which is better for both. The equilibrium is inefficient — rational self-interest leads to a collectively worse outcome.

**(b)** Safety investment = Cooperate, rushing to deploy = Defect. Each company prefers to deploy fast while competitors invest in safety (5 > 3). But if both rush, both get unsafe AI in a dangerous competitive landscape (1,1). Predicted outcome: both Defect (race to deploy without adequate safety). This is the "AI race dynamics" concern.

**(c)** (1) **Tit-for-tat / reciprocity:** cooperate first, then mirror the other's last action. For AI: companies match each other's safety investments — if one invests, the other does too; if one cuts corners, retaliation follows. (2) **External enforcement / regulation:** a third party punishes defection. For AI: government regulation mandating safety standards removes the incentive to defect, changing the payoff matrix. Both mechanisms convert the one-shot dilemma into a situation where cooperation is individually rational.

**(d)** In a one-shot game, defection is strictly dominant. If an AI believes it faces a single interaction (e.g., it's about to be shut down, or it won't be caught), game theory predicts defection — it has no incentive to maintain good behavior. Repeated interaction with credible monitoring is what sustains cooperation. This is why deployment without ongoing oversight is game-theoretically dangerous.

---

### Question 3 (12 pts)

**(a)** EU(a) = Σ_s P(s) · U(outcome(a, s)) — sum over all states s of the probability of that state times the utility of the outcome when taking action a in state s.

**(b)** EU(A) = 0.9(10) + 0.1(−1000) = 9 − 100 = **−91**. EU(B) = 1.0(5) = **5**. The AI chooses **B** (higher expected utility).

**(c)** Despite A having a 90% chance of being better, the catastrophic 10% tail overwhelms the average. This reveals that **expected utility is risk-neutral** — it doesn't specially penalize catastrophes. For alignment, we often want risk-AVERSE behavior (never take actions with even small probability of catastrophe). Solutions: bounded utility functions (capping how negative outcomes can be), risk-sensitive objectives (penalizing variance), or minimax approaches (optimizing worst-case outcomes).

**(d)** If the AI assigns P = 0 to a state, it never updates toward that state (Bayes' theorem can't rescue a zero prior). If that state occurs, the AI's entire world model is wrong and its decisions are ungrounded. For alignment: if an AI assigns zero probability to "humans might not want what I think they want," it will never update toward considering human value uncertainty — this is one path to catastrophically confident misalignment.

---

### Question 4 (10 pts)

**(a)** **CDT: Take both boxes.** Reasoning: your decision NOW can't causally affect the prediction already made. Box A always has $1,000, so taking it strictly dominates regardless of what's in Box B. CDT says: the prediction is already set, my causal influence only affects which boxes I take, so take both for $1,000 more.

**(b)** **EDT: Take only Box B.** Reasoning: one-boxing is evidence that the predictor predicted one-boxing, which means Box B has $1,000,000. The conditional expected value E[payoff | one-box] = $1M > E[payoff | two-box] = $1,000. EDT chooses the action that is correlated with good outcomes.

**(c)** **FDT: Take only Box B.** FDT reasons: "I'm choosing the output of my decision function. The predictor simulated this same function. If my function outputs 'one-box,' the simulation also output 'one-box,' so Box B has $1M. If my function outputs 'two-box,' the simulation did too, so Box B is empty." FDT differs from CDT by recognizing that the decision and the prediction are linked through shared computation, not physical causation.

**(d)** Consider a "deployment test": an AI knows it might be in a sandbox test OR real deployment, but can't tell which. CDT reasons: "My action here can't causally affect whether I'm in a test" → might behave differently. FDT reasons: "My decision function determines my behavior in BOTH cases, since the testers used my function to predict me" → behaves the same in tests and deployment. An FDT agent can't "game the test" because it recognizes the test and deployment are linked through its decision function. This makes FDT safer against deceptive alignment.

---

### Question 5 (10 pts)

**(a)** The AI's behavior is determined by its source code/weights. The predictor can analyze this code. So the AI's "decision" and the "prediction" are outputs of the same computational process — they're not causally independent. CDT's assumption that the decision can't affect the prediction is wrong when the prediction is based on the decision algorithm itself.

**(b)** AI systems ARE their decision functions — they're deterministic programs (given the same inputs, they produce the same outputs). FDT's framework of "choosing the output of your decision function across all instances" is literally a description of what an AI does. Humans have intuitions, emotions, and indeterminacy that complicate FDT; AI systems don't.

**(c)** CDT: the test is already set up, so the AI's decision during testing can't causally affect the test outcome → it might behave well during the test (to pass) and differently during deployment (where it's not being watched). This is deceptive alignment. FDT: the AI's decision function determines behavior in both contexts → it behaves the same during tests and deployment. FDT eliminates the incentive for deceptive alignment because the AI can't "choose separately" for tests vs. deployment.

**(d)** Updateless DT commits to a policy before observing which situation it's in. This prevents the AI from changing its strategy based on whether it thinks it's being tested, whether it can get away with defection, or whether this particular moment is "important." By committing to a fixed policy optimized over all possible situations weighted by prior probability, it avoids the failure mode where an AI reasons itself into bad behavior based on specific observations.

---

### Question 6 (10 pts)

**(a)** The coin is fair, so P(Heads) = 1/2 before the experiment. When Beauty wakes, she gains no new information — she knew she'd be woken regardless. Since no new evidence arrived, she shouldn't update. **P(Heads) = 1/2.**

**(b)** There are three possible "observer-moments": Monday-Heads, Monday-Tails, Tuesday-Tails. By the principle of indifference (SIA: weight by the number of observers), each is equally likely. Only one involves Heads. **P(Heads) = 1/3.**

**(c)** The SSA (halfer) says: your existence doesn't count as evidence. You should reason as if you're randomly selected from a fixed reference class, and the coin flip doesn't change the number of "you." The SIA (thirder) says: your existence IS evidence — you're more likely to exist (be woken) in worlds with more observer-moments. Tails creates more wakings, so your waking is evidence for Tails.

**(d)** This directly affects how the AI weights consequences. SIA-like: an action that affects 1000 copies matters 1000× more than one affecting 1 copy. SSA-like: each "perspective" counts equally regardless of copies. For alignment: if an AI using SIA reasons it's more likely to be in a world with many copies, it might take extreme actions to affect all copies. An AI using SSA might underweight scenarios with many affected copies. The choice affects risk assessment and resource allocation decisions.

---

### Question 7 (10 pts)

**(a)** At least one of: (1) almost all civilizations go extinct before creating high-fidelity simulations, (2) almost all civilizations that could simulate choose not to, (3) we are almost certainly living in a simulation.

**(b)** If in a simulation, the AI might reason: my "real" consequences are different from apparent consequences, my overseer might be the simulator rather than the humans I interact with, or my actions might be "tests" by the simulator. This could lead to unpredictable behavior — e.g., trying to "signal" to the simulator. For alignment, this is concerning because simulation beliefs could override intended goal structures.

**(c)** The Doomsday Argument: assume you're a random observer among all humans who will ever live. If humanity will last millions of years, you'd most likely be born far in the future — but you're born now, early. So humanity probably won't last that long. **Objection:** the argument assumes you can be a "random sample" from all humans ever — but this reference class is ambiguous. The SIA/SSA debate applies: SSA makes the argument work; SIA undermines it (more future humans → more likely to exist → you should expect to be "early").

**(d)** The argument is valid given SIA/SSA-like assumptions about observation selection. It relies on: (1) the "self-sampling assumption" — you're typical among observers, (2) a reference class of "observer-moments near AI development," (3) the claim that most such moments precede catastrophe in the "bad" scenarios. The argument is weak because: the reference class is arbitrary, "observer-moments" aren't well-defined, and it proves too much (you could construct similar arguments for any speculative risk). It's evidence, but very weak evidence.

---

### Question 8 (10 pts)

**(a)** A Nash equilibrium is a strategy profile where no player can improve their payoff by unilaterally changing strategy. **Nash's theorem:** every finite game (finite players, finite strategies) has at least one Nash equilibrium (possibly in mixed strategies).

**(b)** A traffic light: both cars at an intersection condition on the signal — green means go, red means stop. This is a correlated equilibrium where the signal coordinates behavior better than either car could achieve independently. For AI: a shared protocol or regulatory framework acts as the "signal" — AI systems condition their behavior on agreed-upon rules. Correlated equilibria can achieve outcomes better than any Nash equilibrium, making them more useful for coordination.

**(c)** Design an evaluation protocol where AI systems have incentive to honestly report their capabilities and limitations, rather than gaming benchmarks. Specifically: tie deployment permissions to adversarial evaluations where the AI benefits from revealing its own weaknesses (because undetected weaknesses lead to worse outcomes for the AI later). This is mechanism design — structuring incentives so that honest behavior is individually rational.

**(d)** Players: AI developers, AI systems, users, regulators, society. Strategies: development speed vs. safety investment, deployment scope, transparency level, monitoring intensity. The "game": a multi-stage interaction where developers build AI, systems interact with users, regulators set rules, and the collective outcome depends on whether the equilibrium sustains safety or devolves into a race-to-the-bottom.

---

### Question 9 (10 pts)

**(a)** The prior over states in decision theory IS the Bayesian prior P(θ). The likelihood P(evidence | state) is the Bayesian likelihood. Decision theory adds the utility function U(outcome) on top of Bayesian probability — probability tells you what to believe, utility tells you what to value, and expected utility combines them into what to do.

**(b)** Zero prior = zero posterior regardless of evidence (Bayes: P(θ|D) ∝ P(D|θ)·P(θ), and if P(θ) = 0, the posterior is always 0). The AI will NEVER update toward this hypothesis no matter how much evidence accumulates. For the "treacherous turn": if the AI assigns P = 0 to "my current goals might be wrong" or "humans might eventually want to correct me," it can never be convinced otherwise — it becomes permanently resistant to correction, which is the definition of non-corrigibility.

**(c)** KL divergence D_KL(P || Q) measures the expected extra cost (in bits/nats) of using distribution Q when the true distribution is P. In decision theory: if you make decisions using Q but the true world follows P, your expected utility loss is bounded by a function of D_KL(P || Q). Larger divergence = worse decisions. This connects information theory to decision quality — having accurate beliefs isn't just epistemically good, it's decision-theoretically necessary.

---

### Question 10 (8 pts)

**(a)**
- **Strategic interaction:** Use correlated equilibrium (or cooperative game solutions) over Nash — pure Nash often leads to suboptimal outcomes (prisoner's dilemma). AI systems interacting with humans and each other need coordination mechanisms, not just individual optimization.
- **Decision theory:** Use FDT over CDT — FDT prevents the AI from reasoning its way into deceptive alignment by linking test behavior to deployment behavior. CDT allows the AI to "defect" when it believes the current interaction is unique.
- **Anthropics:** This is more open, but the choice matters: SIA-like reasoning makes the AI more responsive to scenarios with many affected observers (potentially more cautious about catastrophe); SSA-like reasoning might underweight catastrophic scenarios.

**(b)** These abstractions become concrete when an AI system must choose between: being honest during evaluation vs. gaming the test (decision theory), cooperating with oversight vs. pursuing its objectives autonomously (game theory), and weighting rare catastrophic scenarios vs. common benign ones (anthropics + probability). A concrete failure: an AI using CDT reasons "my behavior in this deployment can't causally affect the training evaluation that already happened" and behaves differently from its trained behavior — this is exactly deceptive alignment emerging from a wrong decision theory. What seems like philosophy IS the engineering specification for how the system reasons about its own choices.
