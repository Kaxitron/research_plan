# Lesson 37: Formal Logic — Self-Reference, Incompleteness, and the Limits of Reason

[← Topology](lesson-36-topology.md) | [Back to TOC](../README.md) | [Next: How a Single Neuron Works →](../phase6-neural-networks/lesson-38-single-neuron.md)

---

> **Why this lesson exists:** MIRI's agent foundations research — the most theoretical wing of alignment — is deeply rooted in formal logic. Löb's theorem explains why a sufficiently reflective AI might not be able to trust its own reasoning about its own trustworthiness. Gödel's incompleteness theorems set fundamental limits on self-knowledge. Logical uncertainty (from Lesson 46) only makes sense against the backdrop of formal logic. If you want to engage with the "can an AI prove it's aligned?" question rigorously, you need this vocabulary.

## 🎯 Core Concepts

### Propositional and Predicate Logic — The Basics

- **Propositional logic** deals with statements that are true or false, connected by AND (∧), OR (∨), NOT (¬), IMPLIES (→), and IFF (↔). "If it rains, the ground is wet" is p → q. You can build truth tables to evaluate any compound statement mechanically.
- **Predicate logic** (first-order logic) adds quantifiers: "for all x" (∀x) and "there exists x" (∃x), plus predicates that take arguments. "Every even number greater than 2 is the sum of two primes" is ∀n(Even(n) ∧ n > 2 → ∃p∃q(Prime(p) ∧ Prime(q) ∧ n = p + q)). This is Goldbach's conjecture — formally expressible, unproven.
- **A formal system** consists of: a language (symbols, grammar), axioms (starting truths), and inference rules (ways to derive new truths from existing ones). Mathematics is done in formal systems. Proofs are finite sequences of statements where each follows from axioms and previous statements by inference rules.
- **Soundness vs. completeness:** a formal system is *sound* if every provable statement is true (you never prove a falsehood). It's *complete* if every true statement is provable (you can always prove truths). We want both, but Gödel showed we can't always have completeness.

### Gödel's Incompleteness Theorems — The Walls of Knowledge

- **First Incompleteness Theorem:** any consistent formal system strong enough to express basic arithmetic contains statements that are true but unprovable within the system. There will always be true mathematical statements that the system cannot prove.
  - **The construction:** Gödel built a sentence G that essentially says "I am not provable in this system." If G is provable → the system proves something false → inconsistent. If G is not provable → G is true (it correctly states its own unprovability) → true but unprovable. Either way, the system is incomplete or inconsistent.
  - **The connection to the halting problem:** Gödel's theorem and the halting problem are deeply related. Both use self-reference to establish fundamental limits. Both say: no sufficiently powerful system can fully characterize itself.

- **Second Incompleteness Theorem:** a consistent system cannot prove its own consistency. If a system CAN prove "I am consistent," then it's actually inconsistent (or too weak to express arithmetic).
  - **For AI:** an AI system cannot prove its own alignment using only its own reasoning, if that reasoning is sufficiently powerful. Any self-proof of alignment would either be vacuous (the system is too weak to express what "aligned" means) or unreliable (the proof doesn't guarantee truth). This is a deep reason why external oversight matters.

### Löb's Theorem — The Self-Trust Problem

- **Löb's theorem:** if a formal system proves "if I can prove P, then P is true," then the system actually proves P. In symbols: if ⊢ (□P → P), then ⊢ P, where □P means "P is provable."
- **Why this is surprising:** it seems reasonable for a system to believe "if I can prove something, it's true" — that's just trusting your own reasoning (soundness). But Löb's theorem says you can't assert this inside the system unless the statement is already provable.
- **The intuition:** if the system assumes its own soundness, it bootstraps — the assumption creates a proof, which validates the assumption, which... This self-referential loop either proves everything (inconsistency) or only works for statements already provable.
- **For AI alignment:** imagine an AI that reasons: "If I can verify that action X is safe, then X is safe, so I should do X." Löb's theorem says this self-trusting reasoning is dangerous — the AI might "prove" safety and act on that proof, even though the proof is only valid if the conclusion was already true. An AI that trusts its own safety proofs can convince itself of anything.
- **Connection to corrigibility:** a key alignment desideratum is that an AI should defer to human judgment rather than trust its own reasoning about what's good. Löb's theorem provides a formal reason why self-trust is problematic — even for perfectly rational agents.

### Self-Reference and Fixed Points

- **Gödel numbering:** every statement in a formal system can be encoded as a number. This lets the system talk about its own statements — a sentence can refer to its own Gödel number, creating self-reference.
- **The diagonal lemma (fixed-point theorem for logic):** for any property φ, there exists a sentence S such that S is equivalent to φ(⌜S⌝), where ⌜S⌝ is the Gödel number of S. In plain English: for any property, there's a sentence that says "I have this property."
  - φ = "is not provable" → Gödel sentence G: "I am not provable"
  - φ = "is false" → Liar paradox: "This sentence is false" (not a well-formed statement in consistent systems, but the construction shows how self-reference works)
  - φ = "if provable then true" → Löb's theorem
- **Why self-reference matters for AI:** an AI system that models itself — reasons about its own code, its own decisions, its own training — is doing a form of self-reference. The paradoxes and limitations of self-reference in formal logic translate to limitations on AI self-modeling.

### Modal Logic and Provability

- **Modal logic** extends standard logic with operators for "necessarily" (□) and "possibly" (◇). In provability logic, □P means "P is provable."
- **GL (Gödel-Löb logic):** the modal logic of provability. Its key axiom is the Löb axiom: □(□P → P) → □P. This single axiom captures the essential behavior of self-referential provability.
- **Why logicians care about this:** GL precisely characterizes what a system can prove about its own provability. It's a complete logic for self-referential reasoning.
- **For AI:** modal logic frameworks are used in agent foundations to reason about AI belief, knowledge, and trustworthiness. "The AI believes it's aligned" has a formal treatment in modal logic that reveals the subtleties self-reference creates.

### Logical Uncertainty — Logic Meets Probability

- **The problem:** in Bayesian reasoning (Lesson 23), you update beliefs with evidence. But what about beliefs about mathematical truths? You might be uncertain whether Goldbach's conjecture is true — but it's either necessarily true or necessarily false. Standard probability theory doesn't handle this well.
- **Logical uncertainty:** uncertainty about the consequences of your own axioms and definitions. A perfect reasoner would know all mathematical truths instantly, but real reasoners (including AI systems) have bounded computation and can't compute all consequences.
- **Logical induction (MIRI):** Garrabrant et al. (2016) developed a framework for assigning probabilities to logical statements that converges to truth in the limit, satisfies desirable rationality properties, and handles self-reference. This is the most sophisticated treatment of logical uncertainty available.
- **For AI:** a neural network making a prediction is implicitly handling logical uncertainty — it has "beliefs" about things it hasn't fully computed. Understanding logical uncertainty helps reason about what it means for an AI to be "calibrated" on novel reasoning tasks, not just empirical predictions.

## 📺 Watch — Primary

1. **Veritasium — "Math's Fundamental Flaw" (Gödel's Incompleteness)**
   - https://www.youtube.com/watch?v=HeQX2HjkcNo
   - *Excellent visual explanation of Gödel numbering and the incompleteness proof. High production value, accessible.*
2. **Numberphile — "Gödel's Incompleteness Theorem"**
   - Shorter, more focused treatment

## 📺 Watch — Secondary

3. **PBS Infinite Series — "Löb's Theorem and the Prisoner's Dilemma"**
   - If available — connects Löb's theorem to game theory and cooperation
4. **Robert Miles — videos on logical uncertainty and agent foundations** (if available)
   - Connects formal logic to AI safety directly

## 📖 Read — Primary

- **"Gödel, Escher, Bach" by Douglas Hofstadter** — Chapters 1–10 (the "formal systems" core)
  - *The classic. Builds intuition for formal systems, self-reference, and incompleteness through playful dialogues and deep insights. Not a quick read, but transformative for understanding self-reference.*
- **"Computability and Logic" by Boolos, Burgess, & Jeffrey** — Chapters on incompleteness and Löb's theorem
  - More rigorous but very clear treatment
- **"An Introduction to Gödel's Theorems" by Peter Smith** — Chapters 1–10
  - *The most accessible rigorous treatment. Smith explains the proofs with excellent clarity.*

## 📖 Read — Secondary

- **Eliezer Yudkowsky — "Gödel's Completeness and Incompleteness Theorems" (LessWrong)**
  - https://www.lesswrong.com/posts/pv7Qpu8WSge8NRbpB/godel-s-completeness-and-incompleteness-theorems
- **"Löb's Theorem: A community blog post" (LessWrong)**
  - https://www.lesswrong.com/tag/lob-s-theorem
  - Community explanations connecting to decision theory and agent foundations

## 📖 Read — Going Deep

- **"Logical Induction" by Garrabrant et al. (MIRI, 2016)**
  - https://arxiv.org/abs/1609.03543
  - *The definitive treatment of logical uncertainty. Dense but foundational for agent foundations.*
- **"Embedded Agency" by Demski & Garrabrant (MIRI)**
  - https://arxiv.org/abs/1902.09469
  - The section on "reasoning about reasoning" directly uses formal logic concepts
- **"Provability Logic" — Stanford Encyclopedia of Philosophy**
  - https://plato.stanford.edu/entries/logic-provability/
  - Rigorous overview of GL and provability logic

## 🔨 Do

- **Gödel numbering exercise:** define a simple formal language (say, propositional logic with variables p, q, r and connectives ∧, ∨, ¬, →). Assign Gödel numbers to each symbol. Encode a few sentences as numbers. Then construct a function that takes a Gödel number and checks if it encodes a well-formed formula. See how meta-mathematics (reasoning about formulas) reduces to arithmetic (reasoning about numbers).
- **Self-reference construction:** using the diagonal lemma idea, construct (informally, in English) a sentence that says: "This sentence has exactly eleven words." Verify it. Then try: "This sentence is unprovable." Think about why the second is meaningful in a formal system but paradoxical in natural language.
- **Löb's theorem scenario:** write a short story or scenario where an AI system reasons: "If I can prove this action is safe, then it IS safe, so let me try to prove it..." Show how this self-trusting loop can lead to unjustified confidence. Then explain what external oversight (like human review) breaks in this loop.
- **Logical uncertainty exercise:** assign probabilities to: (a) "The 10^10^10th digit of π is 7" — you have no idea, so maybe 0.1? (b) "Goldbach's conjecture is true" — most mathematicians think so, maybe 0.95? (c) "P ≠ NP" — strong consensus, maybe 0.98? These are all mathematical facts with definite truth values, but you have genuine uncertainty. How should these probabilities update as you learn more mathematics? This is logical uncertainty in action.
- **Key exercise:** explain in your own words why Gödel's second incompleteness theorem implies that an AI system cannot prove its own alignment using only its own reasoning. Then explain why this doesn't make alignment hopeless — what role does external verification, interpretability, and empirical testing play?

## 🔗 ML Connection

- **Self-referential models:** when a language model is asked about its own capabilities, training process, or alignment, it's doing a form of self-reference. The logical limits on self-reference (Gödel, Löb) apply, at least in principle.
- **Proof assistants and formal verification:** tools like Lean, Coq, and Isabelle formalize mathematical reasoning. Some alignment researchers explore using these to verify properties of AI systems — but Gödel's theorems set limits on what can be verified.
- **Calibration under logical uncertainty:** a well-calibrated model should have appropriate uncertainty about mathematical truths it hasn't verified. Current models are often poorly calibrated on mathematical reasoning — they state false mathematical claims with high confidence. Understanding logical uncertainty clarifies what good calibration looks like in this domain.

## 🧠 Alignment Connection

- **Can an AI prove it's aligned?** Gödel's second incompleteness theorem suggests fundamental limits. An AI system using sufficiently powerful reasoning cannot prove its own consistency/alignment within its own reasoning framework. This motivates external oversight rather than self-certification.
- **Löb's theorem and self-trust:** an AI that trusts its own safety proofs is in a Löbian loop. The formal resolution is to NOT trust your own reasoning unconditionally — to defer to external checks. This is one formal motivation for corrigibility (the AI defers to human judgment rather than its own assessment).
- **Decision theory and self-reference (Lesson 46):** FDT agents that reason about their own decision procedure are doing formal self-reference. The limitations revealed by Löb's theorem constrain what such agents can know about themselves. The connection between Löb's theorem and cooperation in the Prisoner's Dilemma is a key result in agent foundations.
- **MIRI's research program** uses formal logic pervasively: logical induction, decision theory under logical uncertainty, and reasoning about self-modifying agents all require this vocabulary. If you want to engage with the most theoretical alignment work, formal logic is essential.
