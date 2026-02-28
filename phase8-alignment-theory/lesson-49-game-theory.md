# Lesson 49: Game Theory Foundations

[← Singular Learning Theory](../phase7-interpretability/lesson-48-slt.md) | [Back to TOC](../README.md) | [Next: Decision Theory →](lesson-50-decision-theory.md)

---

> **Why this lesson exists:** AI alignment is fundamentally a multi-agent problem. An AI system interacts with humans, other AI systems, and the broader world. Game theory provides the mathematical framework for reasoning about strategic interactions — cooperation, defection, incentives, and equilibria. Many core alignment concepts (corrigibility, cooperation, deceptive alignment, multi-agent safety) are game-theoretic at their core.

## 🎯 Core Concepts

### The Basics

- **What is a game?** Players, strategies, payoffs. Any situation where your outcome depends on what others do.
- **Dominant strategies:** a strategy that's best regardless of what others do. If both players have dominant strategies, the outcome is determined — but it might not be good for either player.
- **Nash equilibrium:** a set of strategies where no player can improve by unilaterally changing. Not necessarily the "best" outcome — just a stable one.
- **The Prisoner's Dilemma:** the foundational game. Two players each choose cooperate or defect. Mutual cooperation beats mutual defection, but defection is individually rational. This is THE model for why cooperation is hard.
  - Individual rationality → collective irrationality
  - This exact dynamic appears in AI arms races, AI companies cutting safety corners, and the temptation for AI systems to "defect" against human interests

### Key Games and Concepts

- **Iterated Prisoner's Dilemma:** play the same game repeatedly. Now cooperation can emerge! Tit-for-tat, generous tit-for-tat, win-stay-lose-shift. Robert Axelrod's tournaments showed that nice, retaliatory, forgiving strategies win in the long run.
  - **Why this matters for alignment:** if AI systems interact with humans repeatedly, cooperation is more likely. But if the AI expects the game to end (or expects to become powerful enough that cooperation is unnecessary), the logic of cooperation breaks down.

- **Coordination games:** games where players want to coordinate but might fail. Driving on the left vs. right — either works, but you must agree. Schelling focal points: how do you coordinate without communication?
  - **Alignment connection:** getting multiple AI systems (or AI + humans) to coordinate on safety norms is a coordination game.

- **Chicken (game of brinkmanship):** two players drive toward each other. Swerving = safe but humiliating. Not swerving = either you win or you both die. Models escalation dynamics.
  - **Alignment connection:** AI development races between companies or nations have chicken dynamics. Each wants the other to slow down for safety.

- **Stag Hunt:** cooperating on a big prize (hunting stag together) vs. safely defecting for a small prize (hunting hare alone). Unlike Prisoner's Dilemma, mutual cooperation IS an equilibrium — but so is mutual defection. The question is trust.
  - **Alignment connection:** cooperating on AI safety is a stag hunt. Everyone benefits if everyone cooperates, but you need trust.

- **Zero-sum vs. positive-sum:** in zero-sum games, your gain is my loss (chess, poker). Most real-world interactions are positive-sum — cooperation can make everyone better off. A key alignment question: is AI development zero-sum between humans and AI, or positive-sum?

### Mechanism Design — Reverse Game Theory

- **Mechanism design:** instead of analyzing a game, *design* a game that produces good outcomes. Set the rules so that self-interested players end up doing what you want.
  - Auctions are mechanism design: how do you design an auction so bidders truthfully reveal their values?
  - Voting systems are mechanism design: how do you aggregate preferences fairly?
- **Incentive compatibility:** a mechanism is incentive-compatible if players' best strategy is to be honest. The Vickrey auction (sealed-bid second-price) achieves this.
- **The revelation principle:** any outcome achievable by any mechanism can be achieved by one where players truthfully report their types. This is a powerful simplification theorem.
- **Why mechanism design matters for alignment:** designing reward functions, training objectives, and oversight mechanisms are ALL mechanism design problems. You're designing a "game" where the AI's best strategy is to be aligned.

### Common Knowledge, Signaling, and Information

- **Common knowledge:** not just "everyone knows X" but "everyone knows that everyone knows X" and so on infinitely. This seemingly pedantic distinction has huge practical consequences — coordination requires common knowledge.
- **Signaling:** costly actions that reveal information. A degree signals competence. A commitment to safety signals trustworthiness. For AI: how can a model credibly signal that it's aligned?
- **Cheap talk:** costless communication. Can it be trusted? Only if incentives are aligned. If an AI says "I'm aligned," is that informative or cheap talk?

## 📺 Watch — Primary

1. **Yale Game Theory Course (Ben Polak) — Lectures 1-3**
   - https://www.youtube.com/playlist?list=PL6EF60E1027E1A10B
   - *Excellent, accessible introduction. Polak is a fantastic lecturer. Covers Prisoner's Dilemma, dominant strategies, Nash equilibrium.*
2. **Primer (YouTube) — "Game Theory" playlist**
   - https://www.youtube.com/c/PrimerLearning
   - *Beautiful evolution simulations. Watch the iterated Prisoner's Dilemma videos — they show cooperation emerging from evolution.*

## 📺 Watch — Secondary

3. **Veritasium — "The Prisoner's Dilemma"**
   - Clear explanation with good visuals
4. **Robert Miles — "Cooperation in AI"** (if available)
   - Connects game theory to AI safety directly

## 📖 Read — Primary

- **"The Evolution of Cooperation" by Robert Axelrod** — the classic on iterated Prisoner's Dilemma
  - If you read one game theory book, this is it. Accessible and directly relevant to alignment.
- **"Thinking Strategically" by Dixit & Nalebuff** — accessible intro to game theory with real-world examples

## 📖 Read — Secondary

- **"Meditations on Moloch" by Scott Alexander**
  - https://slatestarcodex.com/2014/07/30/meditations-on-moloch/
  - *Essential reading for the alignment community.* Uses game theory (coordination failures, races to the bottom) to explain why the world fails to coordinate on important problems — including AI safety.
- **"Cooperation, Conflict, and Transformative AI" by Jesse Clifton (GovAI)**
  - https://www.governance.ai/research-paper/cooperation-conflict-and-transformative-artificial-intelligence-a-research-agenda
- **"Multi-Agent Safety" on Alignment Forum** — various posts on multi-agent alignment problems

## 📖 Read — Going Deep

- **"Theory of Games and Economic Behavior" by von Neumann & Morgenstern** — the founding text (historical interest)
- **"Algorithmic Game Theory" by Nisan et al.** — covers computational aspects, mechanism design
  - Free PDF: http://www.cs.cmu.edu/~sandholm/cs15-892F13/algorithmic-game-theory.pdf
- **"The Diplomacy Game and AI" papers** — Meta's Cicero and related work on AI in strategic settings

## 🔨 Do

- **Simulate the Prisoner's Dilemma tournament:** implement tit-for-tat, always-defect, always-cooperate, random, and grudger strategies. Run a round-robin tournament. Verify that tit-for-tat performs well.
- **Nash equilibrium finder:** for a 2×2 game given by a payoff matrix, write code that finds all Nash equilibria (pure and mixed).
- **Evolutionary simulation:** start with a population of agents with different strategies. Let them play iterated PD. More successful strategies reproduce. Watch cooperation evolve (or collapse).
- **Key exercise:** Model the AI safety "race" as a game. Two companies each choose "invest in safety" or "skip safety and ship faster." Write down the payoff matrix. What's the Nash equilibrium? Is it socially optimal? What mechanism could change the incentives?

## 🔗 ML Connection

- **RLHF as mechanism design:** the reward model + KL penalty is a mechanism designed so the AI's optimal strategy is helpful behavior. If the mechanism is poorly designed, the AI finds exploits.
- **Multi-agent training environments** (self-play, population-based training) are literally game theory in action. Agents develop cooperative or adversarial strategies based on the game structure.
- **Adversarial robustness** is a zero-sum game between the model and an adversary. Minimax optimization from game theory is the framework.
- **Auction-based resource allocation** in multi-agent AI systems uses mechanism design principles.

## 🧠 Alignment Connection

- **The fundamental alignment problem has game-theoretic structure:** a powerful AI system and humanity are "players." If the AI's interests diverge from humanity's, we're in a game where the equilibrium might be bad for us.
- **Deceptive alignment** is a game where the AI plays a cooperative strategy during training (to avoid correction) and defects during deployment. Understanding when this is the rational strategy requires game theory.
- **AI governance** — getting nations and companies to cooperate on safety — is a coordination game with stag hunt and chicken dynamics.
- **Corrigibility** can be framed game-theoretically: designing an AI that rationally chooses to remain shutdownable, even when it could resist.
