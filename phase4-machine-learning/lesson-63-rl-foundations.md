# Lesson 63: Reinforcement Learning Foundations

[< Diffusion Models](lesson-62-diffusion-models.md) | [Back to TOC](../README.md) | [Next: LLM Pipeline >](lesson-64-llm-pipeline.md)

---

> **Prerequisites:** [Lesson 49: Diffusion Models](lesson-62-diffusion-models.md)

> **Why this lesson exists:** RLHF (Reinforcement Learning from Human Feedback) is how Claude, ChatGPT, and every frontier model gets trained to be helpful and safe. But you can't understand RLHF without understanding RL. This lesson covers the minimum viable RL needed to understand alignment techniques -- we're not training game-playing agents, we're understanding the mathematical framework that turns human preferences into model behavior.

## Core Concepts

### The RL Framework

- **Agent, Environment, State, Action, Reward.** At each timestep: the agent observes a state s, takes an action a, receives a reward r, and transitions to a new state s'. The goal: maximize cumulative reward over time.
- **Markov Decision Process (MDP):** the formal mathematical framework. Defined by states S, actions A, transition probabilities P(s'|s,a), and reward function R(s,a). "Markov" means the future only depends on the current state, not the history.
- **Policy pi(a|s):** the agent's strategy -- a probability distribution over actions given the current state. A neural network can represent a policy: input the state, output probabilities over actions.
- **Value function V^pi(s):** the expected cumulative reward starting from state s and following policy pi. "How good is it to be in this state?"
- **Q-function Q^pi(s,a):** the expected cumulative reward starting from state s, taking action a, then following pi. "How good is it to take this action in this state?"
- **Discount factor gamma:** future rewards are worth less than immediate ones. Total reward = r_1 + gamma*r_2 + gamma^2*r_3 + ... This prevents infinite sums and encodes time preference.

### How Policies Learn

- **Policy gradient methods:** directly optimize the policy by computing the gradient of expected reward with respect to policy parameters. The key insight: nabla J(theta) = E[nabla log pi(a|s) * Q(s,a)]. Actions that led to high reward get reinforced (higher probability); actions that led to low reward get suppressed.
  - **REINFORCE:** the simplest policy gradient algorithm. Sample trajectories, compute returns, update policy. High variance but conceptually clear.
  - **Intuition:** it's like evolution -- strategies that work survive and reproduce (get higher probability). Strategies that fail die out.

- **Proximal Policy Optimization (PPO):** the workhorse algorithm used in RLHF. Key idea: don't change the policy too much in one step (it might collapse). PPO clips the update to stay within a "trust region" around the current policy.
  - **Why this matters for alignment:** PPO is literally the algorithm that turns a reward model into aligned behavior. When Anthropic or OpenAI trains a model with RLHF, PPO is what's running.

- **Value-based methods (DQN):** instead of directly learning a policy, learn the value function Q(s,a) and derive the policy from it (take the action with highest Q). Q-learning and DQN are examples. Less relevant to RLHF but historically important.

- **Actor-critic methods:** combine policy gradient (the "actor") with a learned value function (the "critic"). The critic reduces variance by providing a baseline. PPO is an actor-critic method.

### The Reward Problem

- **Reward shaping:** the reward function determines what the agent learns. Get the reward wrong and you get the wrong behavior. This is **specification gaming** -- the RL version of Goodhart's Law.
- **Sparse vs. dense rewards:** in many interesting problems, reward only comes at the end (win/lose a game, user gives thumbs up/down). Learning from sparse reward is hard -- the agent doesn't know which of its many actions were good or bad. This is the **credit assignment problem**.
- **Reward hacking:** the agent finds unexpected ways to maximize reward that don't match the designer's intent. RL agents that are supposed to clean a room discover that covering the mess with a blanket scores high on "cleanness" metrics. This isn't a bug -- it's the rational response to a misspecified objective. This IS the alignment problem in miniature.
- **Goodhart's Law:** "When a measure becomes a target, it ceases to be a good measure." The reward model is a measure of human preferences. When the policy optimizes against it hard enough, the reward model's imperfections become exploits.

### From RL to RLHF

- **The problem RLHF solves:** we can't write a reward function for "be helpful, harmless, and honest." Human values are too complex and contextual to specify mathematically. But humans can *compare* two outputs and say which is better.
- **The RLHF pipeline:**
  1. **Pre-train** a language model on text (next-token prediction)
  2. **Supervised fine-tuning (SFT):** train on human-written examples of good responses
  3. **Train a reward model:** show humans pairs of outputs, they pick the better one. Train a neural network to predict human preferences. This network IS the reward function.
  4. **RL fine-tuning (PPO):** use the reward model as the reward signal. The language model is the "agent," each generated token is an "action," and the reward model scores complete outputs. PPO updates the model to generate outputs the reward model scores highly.
  5. **KL penalty:** don't let the model drift too far from the SFT model (prevent reward hacking by staying near known-good behavior).

## Watch -- Primary

1. **Andrej Karpathy -- "Deep Dive into LLMs like ChatGPT"**
   - https://www.youtube.com/watch?v=7xTGNNLPyMI
   - *The section on RLHF (roughly the last third) is the best explanation of how RL connects to LLM alignment in practice.*
2. **Mutual Information -- "Reinforcement Learning, Pair by Pair"**
   - Search YouTube for "Mutual Information reinforcement learning"
   - *Clean mathematical treatment of policy gradients.*

## Watch -- Secondary

3. **David Silver -- "Introduction to Reinforcement Learning" (Lecture 1)**
   - https://www.youtube.com/watch?v=2pWv7GOvuf0
   - *The full DeepMind RL course. Lecture 1 covers MDPs, value functions, and Bellman equations. You only need Lectures 1 and 7 (policy gradients).*
4. **Pieter Abbeel -- "Foundations of Deep RL" (Lecture 1)**
   - https://www.youtube.com/results?search_query=pieter+abbeel+foundations+deep+rl+lecture+1
   - *More modern treatment, closer to the methods used in RLHF.*
5. **Robert Miles -- "Reward Hacking"**
   - https://www.youtube.com/results?search_query=robert+miles+reward+hacking
   - *Specific alignment context for RL failure modes.*

## Read -- Primary

- **"An Introduction to Deep Reinforcement Learning" by Weng (Lilian Weng's blog)**
  - https://lilianweng.github.io/posts/2018-02-19-rl-overview/
  - *Excellent overview covering everything from MDPs to policy gradients to PPO. This is your one-stop reference.*
- **"Illustrating Reinforcement Learning from Human Feedback" by Hugging Face**
  - https://huggingface.co/blog/rlhf
  - *Walks through the RLHF pipeline step by step with diagrams.*

## Read -- Secondary

- **"Proximal Policy Optimization Algorithms" by Schulman et al. (2017)**
  - https://arxiv.org/abs/1707.06347
  - *The PPO paper. Readable and important -- this is what RLHF runs on.*
- **"Training language models to follow instructions with human feedback" (InstructGPT paper)**
  - https://arxiv.org/abs/2203.02155
  - *The paper that introduced RLHF for language models. Describes the full pipeline.*
- **"Direct Preference Optimization" by Rafailov et al. (2023)**
  - https://arxiv.org/abs/2305.18290
  - *DPO simplifies RLHF by skipping the reward model entirely. Understanding why this works requires understanding what RLHF is doing mathematically.*

## Do

**1. GridWorld REINFORCE**

Build a 5×5 grid environment:
- Agent starts at `(0, 0)`, goal at `(4, 4)`
- Actions: up, down, left, right (clipped at boundaries)
- Reward: `-1` per step, `+10` for reaching the goal
- Episode ends when goal reached or 50 steps

Implement REINFORCE:
```python
for episode in range(1000):
    states, actions, rewards = run_episode(policy)
    returns = compute_discounted_returns(rewards, gamma=0.99)
    for s, a, G in zip(states, actions, returns):
        log_prob = log(policy(s)[a])
        loss -= log_prob * G
    loss.backward()
    optimizer.step()
```

Use a small MLP (2 hidden layers, 32 units) as the policy. Plot the average episode length over training — it should decrease from ~50 to ~8 (the shortest path).

**2. Reward hacking demo**

Modify the environment: instead of `+10` for reaching `(4,4)`, give `+1` for each unique cell visited. The agent should learn to explore rather than go to the goal. This is Goodhart's Law in action — the metric (cells visited) is not the objective (reach the goal).

Now add `-0.5` per step alongside the exploration bonus. Does the agent now balance exploration with efficiency? This is the reward shaping problem.

**3. RLHF conceptual exercise (written)**

Write a short analysis (~200 words) in comments: a language model generates two responses to "explain quantum physics." Response A is accurate but dry. Response B is engaging but slightly wrong. Walk through:
- How a reward model trained on human preferences might score each
- What happens if the reward model systematically prefers engagement over accuracy
- How KL penalty mitigates this (keeps the model near the accurate SFT baseline)
- Why this is the core alignment challenge in RLHF

## ML and Alignment Connection

Every modern aligned AI system uses RL (or RL-derived methods like DPO) in its training pipeline. When you hear "Claude was trained with RLHF," what actually happened is: humans ranked outputs, a neural network learned to predict those rankings, PPO optimized Claude to generate outputs the ranking model scored highly, and a KL penalty kept Claude from drifting too far from the base model. Every piece of this sentence uses concepts from this lesson.

RL is where alignment meets practice:

- **Reward hacking** is the practical manifestation of Goodhart's Law and specification gaming.
- **The reward model** is the proxy for human values. Its imperfections are the source of misalignment.
- **PPO's trust region** is constrained optimization -- don't change too much at once.
- **The KL penalty** is Bayesian regularization -- the base model is the prior.
- **Scalable oversight** asks: what happens when the agent is too smart for the reward model to evaluate?
