# Lesson 69: Markov Chains and Mixing

[← Probability (L28)](lesson-28-probability.md) | [Back to TOC](../README.md) | [Next: Fisher Information (L70) →](lesson-70-fisher-information.md)

---

> **Why this lesson exists:** A Markov chain is a random process where the future depends only on the present, not the past. This is the mathematical model for reinforcement learning (an agent's next state depends only on current state + action), for MCMC sampling (Lesson 36), and for understanding how language models generate sequences. The stationary distribution of a Markov chain is the eigenvector with eigenvalue 1 — connecting your Phase 1 eigenvalue knowledge to a powerful probabilistic tool. Mixing time — how quickly a chain forgets its starting point — determines whether your MCMC sampler, RL agent, or language model actually converges.

## 🎯 Core Concepts

### What Is a Markov Chain?

- **Definition:** A sequence of random variables X₀, X₁, X₂, ... where:

$$P(X_{n+1} = j \mid X_n = i, X_{n-1}, ..., X_0) = P(X_{n+1} = j \mid X_n = i)$$

- The future depends only on the present state — the chain has "no memory."
- **The transition matrix** P: entry Pᵢⱼ = P(X_{n+1} = j | Xₙ = i). This is a matrix where each row sums to 1 (it's a **stochastic matrix**).
- **n-step transitions:** The probability of going from state i to state j in n steps is the (i,j) entry of Pⁿ — the matrix power. This is why linear algebra (matrix multiplication from Lesson 5) is the computational engine of Markov chains.

### The Stationary Distribution — Eigenvalues Revisited

- A distribution π is **stationary** if πP = π. In words: if you start distributed according to π, after one step you're still distributed according to π. The chain is "in equilibrium."
- **This is an eigenvalue equation:** π is a left eigenvector of P with eigenvalue 1. From Lesson 8, you know how to find eigenvectors — and here's a real-world application.
- **Every stochastic matrix has eigenvalue 1.** The columns of P sum to 1, which guarantees that the all-ones vector is a right eigenvector with eigenvalue 1. The corresponding left eigenvector is the stationary distribution.
- **Multiple stationary distributions?** This can happen if the chain is "reducible" (some states can't reach others). For irreducible chains, the stationary distribution is unique.

### Ergodicity and Convergence

- An irreducible, aperiodic Markov chain converges to its unique stationary distribution from ANY starting point:

$$\lim_{n \to \infty} P^n = \mathbf{1}\pi$$

- **Irreducible:** every state can reach every other state (the graph is connected).
- **Aperiodic:** the chain doesn't cycle with a fixed period. (A chain that alternates between two states is periodic with period 2.)
- **Why this matters:** convergence guarantees that MCMC will eventually sample from the correct posterior (Lesson 36). Without ergodicity, your sampler might get stuck in a subset of the space forever.

### Mixing Time — How Fast Does It Converge?

- **Mixing time** τ_mix: the number of steps until the chain is "close" to stationarity (typically measured by total variation distance ≤ 1/4).
- **The eigenvalue gap determines mixing:** if the eigenvalues of P are 1 = λ₁ ≥ λ₂ ≥ ... ≥ λₙ, then:

$$\tau_{\text{mix}} \approx \frac{1}{1 - \lambda_2}$$

- Large gap (λ₂ far from 1) → fast mixing. Small gap (λ₂ close to 1) → slow mixing.
- **ML connection:** when your MCMC sampler is "slow to converge," this is slow mixing — λ₂ is too close to 1. HMC (Lesson 36) works because it creates a chain with a larger spectral gap.

### Detailed Balance — Designing the Right Chain

- A chain satisfies **detailed balance** if:

$$\pi(i) P(i \to j) = \pi(j) P(j \to i) \quad \text{for all } i, j$$

- **Why this matters:** if you WANT a chain with a specific stationary distribution π (e.g., a posterior distribution), you can design transition probabilities that satisfy detailed balance with respect to π. This is exactly how Metropolis-Hastings works (Lesson 36).
- **Geometric interpretation:** detailed balance means "the flow from i to j equals the flow from j to i" — the chain is "reversible."

### PageRank — The World's Most Famous Markov Chain

- Google's PageRank models a "random web surfer" as a Markov chain. The stationary distribution ranks pages by importance.
- The transition matrix: with probability (1−α), follow a random link from the current page. With probability α, jump to a uniformly random page. The damping factor α ensures ergodicity.
- **Connection to eigenvalues:** PageRank = dominant eigenvector of the modified web graph matrix. Power iteration (computing Pⁿv) is how it's computed at scale — exactly the tool from Lesson 8.

## 📺 Watch

1. **Steve Brunton — "Markov Chains" (Data-Driven Science playlist)**
   - https://www.youtube.com/c/Eigensteve
   - *Clear visual treatment connecting Markov chains to linear algebra and dynamical systems.*
2. **3Blue1Brown — "Markov chains" (if available) or "Eigenvectors" (review)**
   - Review the eigenvalue episode with Markov chains in mind — the stationary distribution IS the eigenvector.
3. **StatQuest — "Markov Chain Monte Carlo"**
   - Connects Markov chains to MCMC sampling, bridging to Lesson 36.

## 📖 Read — Primary

- **Levin, Peres & Wilmer "Markov Chains and Mixing Times" — Chapters 1–4**
  - https://pages.uoregon.edu/dlevin/MARKOV/markovmixing.pdf
  - *Free online. The definitive introduction. Chapter 1 covers basics, Chapter 4 covers mixing times. Beautifully written.*
- **Grinstead & Snell "Introduction to Probability" — Chapter 11 (Markov Chains)**
  - https://math.dartmouth.edu/~prob/prob/prob.pdf
  - *Free. More elementary treatment with good examples.*

## 📖 Read — Secondary

- **Bishop "Pattern Recognition and Machine Learning" — Section 11.2 (Markov Chain Monte Carlo)**
  - Places Markov chains in the ML context

## 🔨 Do

- **Transition matrix from data:** take a corpus of English text. Build a character-level transition matrix (26×26 for letters). Compute P², P⁴, P⁸. Watch the rows converge to the same stationary distribution — the character frequency distribution of English. Generate random text by sampling from the chain.
- **Eigenvalue analysis:** for a 3-state chain, compute eigenvalues and find the stationary distribution as the eigenvector with λ=1. Verify πP = π. Then compute the mixing time estimate 1/(1−λ₂) and verify by computing Pⁿ for increasing n.
- **PageRank implementation:** build a small web graph (5–10 nodes). Construct the transition matrix with damping α=0.15. Find the stationary distribution using (a) eigendecomposition and (b) power iteration. Verify they match.
- **Key exercise:** implement Metropolis-Hastings (from Lesson 36) as a Markov chain with a known target distribution (e.g., a mixture of Gaussians). Plot the trajectory, histogram of samples, and track convergence to the target. Compute the empirical autocorrelation to diagnose mixing speed.

### 💻 Coding Mini-Project: Language Model as Markov Chain (~50 lines)

```python
class CharacterMarkovModel:
    def __init__(self, order=1):
        """Build an n-gram character model (order=1 is classic Markov chain)."""
        ...
    
    def fit(self, text):
        """Count transitions and build probability matrix."""
        ...
    
    def generate(self, length=200, seed=None):
        """Generate text by sampling from the chain."""
        ...
    
    def stationary_distribution(self):
        """Compute via eigendecomposition. Return character frequencies."""
        ...
```

**Your tasks:**
1. Fit on a Shakespeare text. Generate 500 characters. Is it recognizably English?
2. Compare order=1, 2, 3. How does increasing memory improve generation?
3. Compute the transition matrix entropy for each character: H(next | current = 'e') vs H(next | current = 'q'). Which characters are most/least predictable?
4. This IS a simple language model. Modern LLMs are the same idea but with neural network transition probabilities and much longer context.

## 🔗 ML & Alignment Connection

- **RL as a Markov Decision Process (MDP):** an MDP is a Markov chain where the transitions depend on the agent's actions. The Markov property (future depends only on present state) is a core assumption of RL. When this assumption fails (partially observable environments), alignment becomes harder because the agent might need to remember past observations to behave correctly.
- **MCMC for Bayesian inference:** Metropolis-Hastings and HMC (Lesson 36) construct Markov chains whose stationary distributions are posterior distributions. Mixing time determines how long you need to run the sampler. Poorly-mixing chains give misleading posterior estimates — dangerous for safety-critical Bayesian decisions.
- **Language model generation** is sampling from a (very complex, non-Markov) generative process. The "temperature" parameter (Lesson 31) controls how peaked vs. flat the transition probabilities are.
- **Convergence of SGD:** the weight updates of SGD can be modeled as a Markov chain on parameter space. The stationary distribution (if it exists) determines what solutions SGD converges to on average.
