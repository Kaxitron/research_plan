# Lesson 84: Open Problems and Research Frontiers

[← Alignment Problem](lesson-83-alignment-problem.md) | [Back to TOC](../README.md) | [Next: Independent Research →](../phase7-research/research-guide.md)

---

## 🎯 Core Learning

### Technical Open Problems

- **Scalable oversight:** how do you supervise an AI that's smarter than you? Current RLHF requires human judgment, but humans can't evaluate superhuman outputs.
- **Eliciting Latent Knowledge (ELK):** does the model's internal world model match reality? If a model "knows" something is dangerous but reports it as safe, how do you detect this?
- **Interpretability at scale:** we can analyze small models. Can we interpret models with billions of parameters? What new techniques are needed?
- **Formal verification for neural networks:** can we mathematically prove that a model satisfies safety properties? Currently extremely limited.
- **Alignment tax:** making AI safe likely makes it somewhat less capable or more expensive. How do we minimize this tax so safety doesn't lose to competition?

### Emerging Theoretical Frameworks

- **Singular Learning Theory (SLT):** uses algebraic geometry to understand neural network generalization. Phase transitions in learning correspond to changes in the geometry of the loss landscape. May explain when and why capabilities emerge suddenly.
- **Developmental interpretability:** studying how model capabilities develop during training, not just what the final model knows. Connects to SLT's phase transitions.
- **Agent foundations (MIRI):** decision theory, logical uncertainty, embedded agency. Trying to build a rigorous theory of what it means for an agent to reason correctly about itself and the world.
- **Cooperative AI (CHAI, GovAI):** multi-agent alignment, AI governance, international coordination on AI safety.

### Research Frontiers in Interpretability

- **Feature circuits:** mapping how specific features interact to produce model behaviors
- **Developmental interpretability:** tracking feature formation during training
- **Superposition and disentanglement:** how to cleanly separate features that are entangled in the model's representations
- **Causal scrubbing / causal abstraction:** formalizing what it means for an interpretation to be "correct"

## 📖 Read

- **"Open Problems in AI X-Risk" (Carlsmith, 2022)**
- **Neel Nanda — "200 Concrete Open Problems in Mechanistic Interpretability"**
  - https://www.youtube.com/@neelnanda2469
  - https://www.neelnanda.io/mechanistic-interpretability/favourite-problems
- **The Alignment Forum** — https://www.alignmentforum.org/
- **"An Overview of Catastrophic AI Risks" by Hendrycks et al.**

## 📺 Watch

1. **Robert Miles** — ongoing coverage of new alignment research
   - https://www.youtube.com/c/RobertMilesAI
   - *Start with his videos on mesa-optimization and scalable oversight*
2. **The Inside View — "Neel Nanda on mechanistic interpretability, superposition and grokking"**
   - https://www.youtube.com/watch?v=cVBGjhN4-1g
   - *Deep dive into mech interp research directions. Also browse other Inside View episodes with Chris Olah and Paul Christiano.*
3. **AXRP (AI X-Risk Research Podcast)** by Daniel Filan
   - https://axrp.net/
   - *Deep technical episodes. Ep. 19 (Neel Nanda on mech interp) and Ep. 12 (Chris Olah on circuits) are standouts*
4. **80,000 Hours Podcast — "Neel Nanda on the race to read AI minds"**
   - https://80000hours.org/podcast/episodes/neel-nanda-mechanistic-interpretability/
   - *Neel's updated and candid assessment of mech interp's promise and limitations. Important reality check.*
5. **Neel Nanda — "200 Open Problems in Mechanistic Interpretability"**
   - https://www.youtube.com/@neelnanda2469
   - https://www.neelnanda.io/mechanistic-interpretability/getting-started
   - *A research project catalog. Browse this for thesis/project ideas — many are approachable with the skills from this curriculum.*

## What's Next

You now have the mathematical foundations, the technical understanding of neural networks, the interpretability toolkit, and the philosophical framework to engage with alignment research. The next phase is doing the research yourself.

---

## 📝 Time to Take the Exam

This is it — the final exam of the entire curriculum. It covers Lessons 69–67 but draws on every phase. Everything you've learned converges here.

👉 **[Exam 6B: The Alignment Problem — Capstone Final Examination](../assessments/exam-6b-alignment-capstone.md)**

---

## 🏗️ The Final Projects

After the capstone exam, two 5-hour intensive projects await. Each requires you to use nearly everything you've learned across all 67 lessons. Choose one (or do both, if you're feeling ambitious):

👉 **[The Alignment Observatory](../assessments/final-project-alignment-observatory.md)** — Build a small transformer from scratch, train it, analyze its training dynamics, interpret its internals, and attempt to align it. *Focus: constructing everything yourself from the ground up.*

👉 **[The Alignment Researcher's Gauntlet](../assessments/capstone-comprehensive-project.md)** — Investigate sycophantic behavior in GPT-2 small using TransformerLens. Locate the circuit, analyze features, connect to SLT, and propose a fix. *Focus: investigating a real model the way alignment researchers actually work.*
