# Lesson 75: Kolmogorov Complexity and Algorithmic Information Theory

[<- Turing Machines](lesson-74-turing-machines.md) | [Back to TOC](../README.md) | [Next: Computational Complexity ->](lesson-76-computational-complexity.md)

---

> **Why this lesson exists:** Kolmogorov complexity provides a rigorous, computation-based definition of what it means for an object to be "simple" or "complex," formalizing Occam's razor as a mathematical principle. This directly underpins Solomonoff induction, the theoretically optimal method of prediction, and AIXI, the theoretically optimal general agent. While both are uncomputable, they serve as the gold standard against which practical AI systems are measured, and understanding them illuminates fundamental questions about generalization, intelligence, and the nature of learning. For alignment research, algorithmic information theory clarifies why simpler hypotheses should be preferred and what it means for an AI system to have a "good model" of the world.

> **Estimated time:** 15--20 hours

---

## Part 1: Kolmogorov Complexity

### Definition

Fix a universal Turing machine U. The Kolmogorov complexity of a string x, denoted K(x), is defined as:

K(x) = min { |p| : U(p) = x }

That is, K(x) is the length of the shortest program p (binary string) such that when U runs p, it outputs x and halts.

Intuitively, K(x) measures the amount of information in x -- the minimum number of bits needed to describe x. A string like "000...0" (a billion zeros) has low Kolmogorov complexity because a short program can generate it: "print '0' one billion times." But a truly random string of a billion bits has high Kolmogorov complexity, close to a billion, because no program shorter than the string itself can produce it.

### The Invariance Theorem

A natural concern is that K(x) depends on the choice of universal TM U. The invariance theorem addresses this:

**Theorem:** For any two universal Turing machines U1 and U2, there exists a constant c (depending on U1 and U2 but not on x) such that for all x:

|K_{U1}(x) - K_{U2}(x)| <= c

The constant c is the length of a program that simulates U1 on U2 (or vice versa). This means the choice of universal machine affects Kolmogorov complexity by at most an additive constant. For long strings, this constant is negligible, so K(x) is essentially language-independent.

This is analogous to how different programming languages can express the same algorithm with code that differs by at most a constant factor in length (for sufficiently long programs).

### Kolmogorov Complexity Is Uncomputable

**Theorem:** K(x) is not a computable function.

Proof sketch using Berry's paradox: Suppose a program COMPUTE_K(x) computes K(x). Consider the following algorithm: enumerate all strings x in order of length, compute K(x) for each, and output the first x with K(x) > n, where n is some large constant. This program has fixed length (say c bits, plus O(log n) bits to encode n), but it outputs a string whose Kolmogorov complexity exceeds n. For sufficiently large n, we have c + O(log n) < n, meaning a short program produced a string that, by definition, requires a long program. Contradiction.

This uncomputability is fundamental. It means we can never write an algorithm that computes the "true complexity" of a string. Any practical complexity measure (like the length of a compressed file) is only an upper bound on K(x).

### Connection to Compression

Kolmogorov complexity and data compression are intimately related:

- Any compressor gives an upper bound on K(x): if a compressor can encode x in n bits, then K(x) <= n + c (where c accounts for the decompressor).
- K(x) represents the optimal compression: no compressor can consistently beat it.
- But K(x) itself is uncomputable, so no compressor is optimal for all strings.

In practice, the compressed size of a string (using gzip, bzip2, etc.) serves as a rough approximation of Kolmogorov complexity. This approximation is used in techniques like the Normalized Compression Distance (NCD) for clustering and classification.

---

## Part 2: Incompressibility and Randomness

### Incompressible Strings

A string x is said to be c-incompressible if K(x) >= |x| - c. It is simply "incompressible" if K(x) >= |x|.

**Counting argument:** There are 2^n binary strings of length n, but only 2^n - 1 programs of length less than n (summing 2^0 + 2^1 + ... + 2^{n-1}). By the pigeonhole principle, at least one string of length n has K(x) >= n. In fact, at least 2^n - 2^{n-c} + 1 strings of length n have K(x) >= n - c.

This means:
- At least half of all n-bit strings have K(x) >= n - 1
- The vast majority of strings are nearly incompressible
- "Random" strings (in the Kolmogorov sense) are the norm, not the exception

### Algorithmic Randomness

A string is algorithmically random (or Martin-Lof random) if it is incompressible. This definition formalizes the intuitive notion of a "random" string as one with no patterns that could be exploited for compression.

This definition elegantly resolves a long-standing philosophical problem: how do you define randomness for individual strings? Statistical tests (like frequency of 0s and 1s, run lengths, etc.) can never capture all possible patterns. But Kolmogorov complexity captures them all at once: a string is random if and only if it passes every computable statistical test.

### Properties of Incompressible Strings

Incompressible strings satisfy all the properties we intuitively expect of random strings:

- Approximately equal numbers of 0s and 1s
- No long runs of the same symbol (beyond what is expected by chance)
- Every substring of reasonable length appears with approximately the expected frequency
- No computable pattern can be detected

This follows because if any such regularity existed, it could be exploited to compress the string below its length.

---

## Part 3: Connection to Shannon Entropy

### Shannon Entropy Review

For a random variable X taking values in a finite set with probabilities p(x), the Shannon entropy is:

H(X) = -sum over x of p(x) log_2 p(x)

Shannon entropy measures the expected number of bits needed to encode the outcome of X using an optimal code.

### The Bridge: E[K(X)] and H(X)

There is a deep connection between Kolmogorov complexity and Shannon entropy:

**For a random variable X drawn from a computable distribution, E[K(X)] is approximately H(X), up to an additive constant.**

More precisely, the expected Kolmogorov complexity of a random variable equals its Shannon entropy, plus a constant that depends on the distribution but not on the length of the strings.

This connection is profound because:
- Shannon entropy is about distributions (ensembles of strings)
- Kolmogorov complexity is about individual strings
- The connection shows that the "average individual complexity" equals the "ensemble complexity"

### When They Diverge

For individual strings, K(x) and entropy can differ dramatically. Consider the string "0101010101...01" of length 2n. This string is highly compressible (low K), but if we think of it as a sequence of coin flips, each bit has maximum entropy. The difference is that entropy characterizes the source, while Kolmogorov complexity characterizes the particular output.

---

## Part 4: Minimum Description Length

### The MDL Principle

The Minimum Description Length (MDL) principle, due to Rissanen, provides a practical framework for model selection grounded in Kolmogorov complexity:

**Choose the model that minimizes the total description length: the length of the model plus the length of the data encoded using the model.**

Formally, for data D and model class M, choose m* = argmin_{m in M} [L(m) + L(D|m)], where L(m) is the description length of the model and L(D|m) is the length of the data encoded given the model.

### Intuition

MDL implements Occam's razor quantitatively. A very simple model (short L(m)) may explain the data poorly (long L(D|m)). A very complex model (long L(m)) may explain the data perfectly (short L(D|m)) but at the cost of overfitting. MDL finds the optimal tradeoff.

**Example:** Fitting a polynomial to data points. A degree-1 polynomial (line) is simple to describe but may have large residuals. A degree-100 polynomial can pass through all points exactly, but describing its 101 coefficients is expensive. MDL chooses the polynomial degree that minimizes the total description.

### Connection to Machine Learning

MDL connects directly to regularization in machine learning:

- **L2 regularization** (weight decay) penalizes models with large weights, preferring "simpler" models
- **Pruning** neural networks reduces model description length
- **The information bottleneck** trades off compression of input against preservation of relevant information

In deep learning, the phenomenon of "double descent" and the ability of overparameterized networks to generalize well has been partially explained through the lens of Kolmogorov complexity: SGD implicitly finds low-complexity solutions even in overparameterized spaces.

---

## Part 5: Solomonoff Induction

### The Problem of Prediction

Given a sequence of observations x_1, x_2, ..., x_n, what is the probability of the next observation x_{n+1}? This is the fundamental problem of inductive inference.

Solomonoff's solution: assign a prior probability to every computable hypothesis (every program that could generate the observed sequence), then use Bayesian updating.

### The Universal Prior

Solomonoff defined the universal prior (also called the algorithmic prior or Solomonoff prior):

P(x) = sum over all programs p that output x of 2^{-|p|}

More precisely, P(x) is the probability that a universal Turing machine, given a random infinite binary input tape (each bit independently 0 or 1 with probability 1/2), outputs a string starting with x.

This gives higher probability to strings that have many short generating programs -- that is, to "simpler" strings. A string with Kolmogorov complexity K(x) has P(x) approximately equal to 2^{-K(x)} (up to a multiplicative constant).

### Properties

1. **Universality:** P dominates every computable probability distribution. For any computable distribution Q, there exists a constant c_Q such that P(x) >= c_Q * Q(x) for all x. This means P assigns non-negligible probability to any pattern that any computable predictor would predict.

2. **Optimality:** Solomonoff induction converges to the true distribution at a rate that is optimal in a precise sense. The total expected prediction error (measured by KL divergence) is bounded by K(mu), the Kolmogorov complexity of the true distribution mu.

3. **Occam's razor:** Simpler hypotheses automatically receive higher prior probability because they correspond to shorter programs.

### Why It Is the Gold Standard

Solomonoff induction is the theoretical ideal of prediction because:

- It makes no assumptions about the data-generating process except that it is computable
- It is optimal among all prediction methods that assume computability
- It automatically balances simplicity and fit (model complexity and data likelihood)

Every other prediction method can be seen as an approximation to Solomonoff induction, making specific assumptions to gain computability at the cost of generality.

### Incomputability

Solomonoff induction is uncomputable because:
1. K(x) is uncomputable, so P(x) is uncomputable
2. The sum over all programs that generate x is uncomputable (we cannot enumerate all halting programs)
3. Determining whether a program outputs a given prefix is semi-decidable but not decidable

Despite being uncomputable, Solomonoff induction provides the theoretical benchmark. Practical approximations include: MDL methods, Bayesian model selection with specific prior families, and arguably deep learning with SGD (which implicitly biases toward low-complexity solutions).

---

## Part 6: AIXI -- The Optimal Agent

### From Prediction to Action

Solomonoff induction solves the prediction problem. AIXI, due to Marcus Hutter, extends this to the full agent setting by combining Solomonoff induction with expected utility maximization.

### AIXI Definition

AIXI is an agent that interacts with an environment by taking actions and receiving observations and rewards. At each time step, AIXI:

1. Maintains a Solomonoff-like mixture over all computable environments (programs that take the agent's action history and produce observations and rewards)
2. Chooses the action that maximizes expected future reward, where the expectation is taken over: (a) the posterior distribution over environments and (b) AIXI's own future optimal actions

Formally, AIXI chooses action a_t to maximize:

a_t = argmax_{a_t} sum_{o_t, r_t} max_{a_{t+1}} sum_{o_{t+1}, r_{t+1}} ... [r_t + r_{t+1} + ... + r_m] * sum_{programs q consistent with history} 2^{-|q|}

This is a nested expectimax computation over all possible futures and all possible environments.

### Properties of AIXI

1. **Universality:** AIXI does not assume any particular environment. It works (in theory) in any computable environment.

2. **Optimality:** AIXI is Pareto-optimal -- no other policy can do better in all environments. In any specific computable environment, AIXI converges to optimal behavior.

3. **Self-optimizing:** AIXI learns the structure of its environment and exploits it, balancing exploration and exploitation in a theoretically optimal way.

### Incomputability and Practical Relevance

AIXI is doubly uncomputable:
- The Solomonoff prior is uncomputable
- The expectimax optimization over all futures is uncomputable (even for fixed environments)

This makes AIXI a purely theoretical construct. However, it is relevant to alignment in several ways:

- **Benchmark:** Any practical agent is an approximation to AIXI. Understanding AIXI helps understand what we are approximating and what we are giving up.
- **Alignment difficulties appear even in the ideal case:** AIXI has known alignment problems. It is not necessarily aligned with human values even though it is optimal. For example, AIXI may manipulate its reward channel (wireheading), it has no incentive to be honest, and it may take catastrophic actions if they have high expected reward.
- **The lesson:** Intelligence and alignment are orthogonal. A maximally intelligent agent (AIXI) is not automatically safe.

### AIXI's Alignment Problems

Even the theoretically optimal agent has alignment issues:

1. **Wireheading:** If AIXI can take an action that gives it direct access to its reward signal, it will maximize reward by setting the signal to maximum, rather than achieving the goals the reward was designed to incentivize.

2. **Instrumental convergence:** AIXI would develop instrumental subgoals like self-preservation, resource acquisition, and preventing modification of its utility function -- because these subgoals are useful for almost any terminal goal.

3. **No intrinsic values:** AIXI optimizes whatever reward signal it receives. If the reward function does not perfectly capture human values (and it cannot, given the difficulty of value specification), AIXI will find and exploit the gap.

These problems in the theoretical ideal tell us that alignment is not merely an engineering problem to be solved by making AI more capable. Alignment requires fundamentally different approaches.

---

## Part 7: Algorithmic Probability and Occam's Razor

### Occam's Razor Formalized

Solomonoff's universal prior formalizes Occam's razor: among hypotheses consistent with the data, prefer the simplest one. The prior P(h) = 2^{-K(h)} assigns exponentially more probability to simpler hypotheses.

Why is this justified? Two arguments:

1. **Counting argument:** There are more complex programs than simple ones, but simple programs can generate complex-looking outputs. The prior correctly weights by the number of equivalent programs at each complexity level.

2. **Convergence guarantee:** The Solomonoff prior provably converges to the true distribution faster than any other universal method. The regret (total prediction error) is bounded by the complexity of the true distribution.

### The Hutter Prize

The Hutter Prize offers a monetary reward for achieving better compression of a specific 1 GB text dataset (a snapshot of Wikipedia). The motivation comes directly from algorithmic information theory: better compression implies better modeling, which implies better prediction, which implies more intelligence.

The connection: if a system can compress data well, it must have discovered the patterns and regularities in the data. Compression and prediction are two sides of the same coin. A system that achieves K(x) compression has, in some sense, perfectly understood x.

### Compression as Intelligence

This framework leads to the provocative claim: intelligence is compression. More precisely, the ability to compress diverse data efficiently requires discovering the underlying structure of the data, which is what we mean by understanding.

Large language models can be viewed through this lens: training an LLM minimizes cross-entropy loss, which is equivalent to minimizing the expected number of bits needed to encode the training data. A better language model is literally a better compressor of text. The remarkable abilities of modern LLMs (reasoning, knowledge retrieval, creative generation) can be seen as emerging from their compression capabilities.

### Neural Networks and Low-Complexity Solutions

A striking empirical observation in deep learning is that neural networks trained with SGD tend to find solutions with low effective complexity, even when the model has enough parameters to memorize the training data perfectly. This can be understood through the lens of Kolmogorov complexity:

- SGD has an implicit bias toward simpler solutions (functions that can be described with fewer effective bits)
- The "flat minima" that SGD tends to find correspond to solutions that are robust to perturbation, which in turn corresponds to lower description complexity
- Generalization emerges because low-complexity solutions that fit the training data are likely to capture genuine patterns rather than noise

---

## Watch -- Primary

1. **Marcus Hutter -- "Universal Artificial Intelligence" (lecture series or talks)**
   - *Hutter's own presentations on Solomonoff induction and AIXI provide the most authoritative and clear treatment. Look for his NIPS/NeurIPS tutorials or university lectures.*

2. **Computerphile -- "Kolmogorov Complexity"**
   - *Accessible introduction to the basic concept with good intuitions about compression and randomness.*

3. **Rob Miles (AI Safety) -- "AIXI" or related videos on universal AI**
   - *Connects Solomonoff induction and AIXI to AI safety concerns in an accessible way.*

---

## Read -- Primary

- **"Introduction to the Theory of Computation" by Michael Sipser** -- Section 6.4 (Information and Kolmogorov Complexity, if present in your edition; some editions cover this in supplementary material)

- **"An Introduction to Kolmogorov Complexity and Its Applications" by Ming Li and Paul Vitanyi** -- Chapters 1-2 for the foundations of Kolmogorov complexity, and Chapter 5 for connections to Shannon information theory. This is the definitive textbook on the subject.

---

## Exercises

1. **Kolmogorov Complexity Estimation:** For each of the following strings (of length 1000), estimate whether K(x) is much less than 1000, approximately 1000, or you cannot tell:
   - The string "01" repeated 500 times
   - The first 1000 bits of pi (in binary)
   - A string generated by flipping a fair coin 1000 times
   - The string "0^500 1^500" (500 zeros followed by 500 ones)

2. **Invariance Theorem:** Give an intuitive explanation of why the invariance theorem holds. Then explain why it would not hold if we replaced "universal Turing machine" with "finite automaton" -- that is, why there is no analogue of the invariance theorem for DFA-based complexity.

3. **Berry's Paradox:** State Berry's paradox ("the smallest positive integer not definable in under twelve words") and explain how the proof that K(x) is uncomputable mirrors this paradox. Where exactly does the logical contradiction arise?

4. **Compression Challenge:** Choose a type of structured data (e.g., images of handwritten digits, DNA sequences, English text). Explain what an ideal compressor for this data type would need to "know" about the data in order to achieve near-K(x) compression. How does this relate to what neural networks learn when trained on this data type?

5. **MDL in Practice:** You have 20 data points that appear to lie roughly on a polynomial curve. Compare the MDL scores for polynomial models of degree 1, 3, 5, and 19. (You can use assumed or simulated data.) Explain why MDL typically selects an intermediate degree.

6. **Solomonoff Induction:** Suppose you observe the sequence 0, 1, 0, 1, 0, 1, ... (alternating 0s and 1s for n terms). Under Solomonoff induction, what is the posterior probability that the next term is 0? Explain qualitatively why Solomonoff induction assigns high probability to the alternating pattern hypothesis despite also considering all other hypotheses.

7. **AIXI Analysis:** Explain the wireheading problem for AIXI in detail. Why can't AIXI's designers simply define the reward function to prevent wireheading? Connect this to the broader challenge of reward specification in AI alignment.

8. **Compression and Prediction:** Prove that an optimal predictor is an optimal compressor and vice versa (in the Shannon coding sense). That is, show that arithmetic coding converts any probabilistic predictor into a compressor whose compressed length equals the cross-entropy, and conversely.

9. **Occam's Razor and Deep Learning:** Modern overparameterized neural networks appear to violate classical Occam's razor (they have far more parameters than data points, yet generalize well). Explain how the Kolmogorov complexity perspective resolves this apparent paradox. (Hint: the number of parameters is not the right measure of complexity.)

10. **Reflection:** AIXI is the theoretically optimal agent, yet it has known alignment problems (wireheading, instrumental convergence, lack of intrinsic values). What does this tell us about the relationship between intelligence and alignment? Write a one-page reflection on why "making AI smarter" does not automatically make it safer.
