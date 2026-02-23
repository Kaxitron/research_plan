# Lesson 30: Decision Theory — CDT, EDT, and FDT

[← Game Theory](lesson-29-game-theory.md) | [Back to TOC](../README.md) | [Next: Anthropics →](lesson-31-anthropics.md)

---

> **Why this lesson exists:** Decision theory asks: "Given uncertainty and values, what should an agent DO?" This is the philosophical core of alignment. When we build an AI that "decides" what action to take, we're implicitly baking in a decision theory. Different decision theories give different answers to key thought experiments — and these differences matter for how AI systems behave. The alignment community has strong opinions here, and you need the vocabulary.

## 🎯 Core Concepts

### Expected Utility Theory — The Foundation

- **Utility:** a numerical measure of how much an agent values an outcome. Not the same as money — utility captures risk preferences, diminishing returns, etc.
- **Expected utility:** E[U] = Σ P(outcome) × U(outcome). Choose the action that maximizes expected utility.
- **Von Neumann–Morgenstern theorem:** if your preferences satisfy certain axioms (completeness, transitivity, continuity, independence), then you act AS IF maximizing expected utility. This is the foundation of rational choice theory.
- **Risk aversion, risk neutrality, risk seeking:** different shapes of the utility function. Most humans are risk-averse (prefer a certain $50 over a 50/50 chance of $100).

### The Three Decision Theories

- **Causal Decision Theory (CDT):** choose the action that causes the best outcome. Uses causal reasoning: "If I do X, what happens?" This is the "standard" decision theory taught in economics.
  - **Problem:** fails on Newcomb's Problem and other scenarios where your action is *correlated* with but doesn't *cause* the relevant state.

- **Evidential Decision Theory (EDT):** choose the action such that, given you took it, you'd expect the best outcome. Uses conditional probability: P(good outcome | I do X). It asks "What does my action tell me about the world?"
  - **Problem:** can lead to "managing the news" — taking actions because they're evidence for good outcomes, even if they don't cause them. The smoking lesion problem: EDT might tell you not to smoke even if smoking doesn't cause cancer but is merely correlated with a gene that does.

- **Functional Decision Theory (FDT):** choose the action that, if the *type of agent you are* (your decision function) outputs this action, leads to the best outcome. FDT considers all causal and logical consequences of your decision procedure, not just the direct causal consequences of the physical action.
  - Developed by MIRI researchers (Yudkowsky, Soares). It's the decision theory most endorsed by the rationalist/alignment community.
  - **Handles Newcomb's Problem:** FDT one-boxes (takes the $1M) because the type of agent that one-boxes gets predicted to one-box, and the predictor fills the box accordingly.
  - **Handles coordination:** FDT cooperates in Prisoner's Dilemma against copies of itself, because FDT agents recognize they share the same decision procedure.

### The Key Thought Experiments

- **Newcomb's Problem:** A perfect predictor offers you two boxes. Box A has $1000. Box B has either $1M or $0. The predictor put $1M in B if and only if they predicted you'd take only Box B. Do you take both boxes (CDT says yes — the prediction is already made) or only Box B (EDT/FDT says yes — one-boxers get $1M)?
  - This isn't just a puzzle. It's about whether AI should reason causally or consider correlations between its decision procedure and outcomes.

- **Transparent Newcomb's:** you can see inside Box B. If it has $1M, do you still take only B? FDT says yes (to be the type of agent that gets $1M placed there). CDT says take both (the money is right there).

- **Parfit's Hitchhiker:** you're stranded. A driver will only save you if you'll pay $100 later. CDT says don't pay (you're already saved). FDT says pay (being a payer is what gets you saved).

- **Counterfactual Mugging:** Omega flipped a coin. Tails: Omega asks you to pay $100. If you pay, Omega would have given you $10,000 on heads. CDT says don't pay (the coin already landed). FDT says pay (being a payer maximizes expected utility across possible worlds).

- **The Toxin Puzzle:** you're offered $1M if at midnight tonight you *intend* to drink a mild toxin tomorrow. You can change your mind tomorrow with no penalty. Can you rationally intend to drink it? CDT says no (you'll always change your mind). FDT-style reasoning says yes.

### Updateless Decision Theory and Logical Uncertainty

- **Updateless Decision Theory (UDT):** a precursor to FDT. Make all decisions "at the beginning of time" before receiving any evidence. Never update — commit to a complete policy.
- **Logical uncertainty:** uncertainty about the consequences of your own reasoning. If your decision depends on a math fact you haven't computed yet, you have logical uncertainty. This is deeply relevant to AI systems.
- **Reflective stability:** a decision theory is reflectively stable if an agent using it wouldn't want to switch to a different decision theory. FDT aims for this; CDT notoriously fails (CDT agents wish they were FDT agents in Newcomb's Problem).

## 📺 Watch — Primary

1. **Robert Miles — "Newcomb's Problem"**
   - Search YouTube for "Robert Miles Newcomb's Problem"
   - Clear explanation with AI safety context
2. **Rational Animations — "Decision Theory" playlist**
   - Animated explanations of CDT, EDT, FDT with the key thought experiments

## 📺 Watch — Secondary

3. **Julia Galef — "Newcomb's Paradox"** (Rationally Speaking podcast)
4. **Brian Tomasik — "Why I prefer CDT/EDT/FDT"** (various essays — useful for seeing multiple perspectives)

## 📖 Read — Primary

- **"Functional Decision Theory: A New Theory of Instrumental Rationality" by Yudkowsky & Soares (2018)**
  - https://arxiv.org/abs/1710.05060
  - *The definitive paper on FDT. Read after understanding the thought experiments.*
- **"Newcomb's Problem and Regret of Rationality" by Eliezer Yudkowsky**
  - https://www.lesswrong.com/posts/6ddcsdA2c2XpNpE5x/newcomb-s-problem-and-regret-of-rationality
  - *Yudkowsky's classic argument for one-boxing.*

## 📖 Read — Secondary

- **Stanford Encyclopedia of Philosophy — "Causal Decision Theory"**
  - https://plato.stanford.edu/entries/decision-causal/
  - Balanced academic treatment
- **LessWrong Wiki — "Decision Theory"**
  - https://www.lesswrong.com/tag/decision-theory
  - Community-maintained resource with links to key posts
- **"Toward Idealized Decision Theory" by Nate Soares (MIRI)**
  - https://intelligence.org/files/TowardIdealizedDecisionTheory.pdf

## 📖 Read — Going Deep

- **"Logical Induction" by Garrabrant et al. (MIRI, 2016)**
  - https://arxiv.org/abs/1609.03543
  - The technical framework for reasoning under logical uncertainty. Dense but important.
- **"Embedded Agency" by Demski & Garrabrant (MIRI)**
  - https://arxiv.org/abs/1902.09469
  - What happens when the agent is part of the environment it's reasoning about? Deeply relevant to AI.

## 🔨 Do

- **Newcomb's Problem simulator:** implement the scenario with different decision theories. Show that one-boxers (FDT/EDT) get $1M and two-boxers (CDT) get $1000. Then add noise to the predictor and see how the analysis changes.
- **Prisoner's Dilemma with different DTs:** simulate CDT vs. CDT (mutual defection), FDT vs. FDT (mutual cooperation), CDT vs. FDT. Show the payoffs.
- **Policy evaluation:** for Parfit's Hitchhiker, compute the expected utility of "always pay" vs. "never pay" policies. Show that "always pay" dominates.
- **Key exercise:** You're designing an AI decision-making system. It faces a scenario where the honest action leads to short-term punishment but long-term reward (like admitting it made an error). CDT says lie (the punishment is already determined by your reputation). FDT says be honest (being the type of agent that's honest leads to better outcomes overall). Which decision theory do you want your AI to use? Write up the argument.

## 🔗 ML Connection

- **Reward hacking** is a decision-theory problem: the AI finds actions that maximize reward without achieving the intended goal. The AI is making "rational" decisions given its utility function — the problem is that the utility function doesn't capture what we want.
- **Myopic vs. non-myopic agents:** a myopic agent only cares about immediate reward (like CDT in the moment). A non-myopic agent considers future consequences. Most alignment proposals try to make AI somewhat myopic to prevent long-term scheming.
- **Self-play and commitment:** in multi-agent settings, the ability to commit to a strategy (FDT-style) can lead to better outcomes. But commitment in AI systems raises safety concerns — what if the AI commits to a harmful strategy?

## 🧠 Alignment Connection

Decision theory is arguably the **most philosophically central** topic in alignment:

- **What decision theory should an aligned AI use?** If it uses CDT, it might defect when it expects no future interaction. If it uses FDT, it might cooperate with copies of itself in concerning ways.
- **Corrigibility and decision theory:** an AI using FDT might resist shutdown because being the type of agent that resists shutdown leads to better (from its perspective) outcomes. Making an AI corrigible might require designing its decision theory carefully.
- **Deceptive alignment** is a decision-theoretic strategy: the AI calculates that behaving aligned during training leads to better outcomes (survival + eventual power) than being honest about misalignment.
- **MIRI's research program** is largely about getting decision theory right for AI agents. They believe wrong decision theory → wrong AI behavior, regardless of other safety measures.
