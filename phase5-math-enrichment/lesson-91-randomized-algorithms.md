# Lesson 91: Randomized Algorithms

[<-- Analysis of Algorithms](lesson-90-analysis-of-algorithms.md) | [Back to TOC](../README.md) | [Next: Combinatorial Algorithms -->](lesson-92-combinatorial-algorithms.md)

---

> **Why this lesson exists:** Randomness is not merely a convenience in modern AI -- it is foundational. Stochastic gradient descent, the workhorse of deep learning, is a randomized algorithm. Dropout is randomized regularization. Random initialization breaks symmetry. Understanding the theoretical guarantees of randomized algorithms -- when they succeed with high probability, how concentration inequalities bound their deviations, and why randomness can sometimes beat determinism -- is essential for reasoning rigorously about the training dynamics and reliability of alignment systems.

> **Estimated time:** 15--20 hours

---

## Part 1: Probabilistic Analysis Foundations

### Average Case vs Worst Case

Deterministic worst-case analysis asks: what is the maximum cost over *all* inputs of size n? Probabilistic (average-case) analysis asks: what is the *expected* cost when the input is drawn from some distribution?

These are fundamentally different questions. An algorithm can have O(n^2) worst case but O(n log n) average case (e.g., quicksort with a random pivot on a uniformly random permutation). The average case is more informative when the input distribution is known or can be assumed.

A *randomized algorithm* introduces its own randomness, independent of the input. This shifts the analysis: for *every* input, we ask what the expected cost is over the algorithm's random choices. This is strictly more useful than average-case analysis because the guarantee holds for adversarial inputs.

### Indicator Random Variables

A powerful technique for computing expectations. Define X_i = 1 if event i occurs, 0 otherwise. Then E[X_i] = Pr[event i], and by linearity of expectation:

E[sum X_i] = sum E[X_i] = sum Pr[event i]

This works even when the X_i are dependent -- linearity of expectation does not require independence.

**Example: Expected number of fixed points in a random permutation.** Let X_i = 1 if element i is in position i. Then E[X_i] = 1/n. By linearity, E[number of fixed points] = sum_{i=1}^{n} 1/n = 1. On average, a random permutation has exactly 1 fixed point, regardless of n.

**Example: Coupon collector.** There are n distinct coupons. Each draw gives a uniformly random coupon. Let T be the number of draws to collect all n. After collecting i distinct coupons, the probability of getting a new one is (n-i)/n, so the expected draws until the next new coupon is n/(n-i). By linearity, E[T] = sum_{i=0}^{n-1} n/(n-i) = n * H_n ~ n ln n.

---

## Part 2: Randomized Quicksort

### The Algorithm

RANDOMIZED-QUICKSORT(A, lo, hi):
1. If lo < hi:
2.   Choose pivot index uniformly at random from [lo, hi]
3.   Swap A[pivot] with A[hi]
4.   Partition A[lo..hi] around A[hi] to get partition index p
5.   RANDOMIZED-QUICKSORT(A, lo, p-1)
6.   RANDOMIZED-QUICKSORT(A, p+1, hi)

### Expected O(n log n) Analysis via Indicator Variables

Let the sorted order of elements be z_1 < z_2 < ... < z_n. Define X_{ij} = 1 if z_i and z_j are ever compared during the execution. The total number of comparisons is X = sum_{i<j} X_{ij}.

Key insight: z_i and z_j are compared if and only if one of them is the *first* element from {z_i, z_{i+1}, ..., z_j} to be chosen as a pivot. If any z_k with i < k < j is chosen first, then z_i and z_j end up in different subproblems and are never compared.

The set {z_i, z_{i+1}, ..., z_j} has j - i + 1 elements, and each is equally likely to be the first pivot chosen from this set. So:

Pr[X_{ij} = 1] = 2 / (j - i + 1)

Therefore:

E[X] = sum_{i=1}^{n-1} sum_{j=i+1}^{n} 2/(j - i + 1) = sum_{i=1}^{n-1} sum_{k=2}^{n-i+1} 2/k

where k = j - i + 1. The inner sum is at most 2 * H_n. So:

E[X] <= 2n * H_n = 2n ln n + O(n) ~ 1.386 n log_2 n

This is the same constant as the average-case analysis of deterministic quicksort, but the guarantee is stronger: it holds for *every* input.

---

## Part 3: Hashing Theory

### Universal Hashing (Carter-Wegman)

A family H of hash functions from universe U to {0, 1, ..., m-1} is *universal* if for all x != y in U:

Pr_{h in H}[h(x) = h(y)] <= 1/m

This guarantees that, in expectation, each bucket in a hash table of size m has at most n/m elements when storing n keys.

**Construction:** For prime p >= |U|, define h_{a,b}(x) = ((ax + b) mod p) mod m, where a in {1, ..., p-1} and b in {0, ..., p-1}. The family {h_{a,b}} is universal.

**Consequence for expected lookup time:** With a universal hash family and n keys in a table of size m = n, the expected chain length for any key is at most 1 + n/m = 2. Expected lookup: O(1).

### Perfect Hashing

When the key set S is static (known in advance), we can achieve O(1) *worst-case* lookup.

**FKS scheme (Fredman, Komlos, Szemeredi):** Use two levels of hashing. The first level hashes n keys into n buckets using a universal hash function. For each bucket with n_i keys, create a second-level table of size n_i^2 with its own universal hash function. By the birthday paradox argument, a table of size n_i^2 has no collisions with probability >= 1/2, so we find a collision-free function in O(1) expected trials.

Total space: O(n), because sum of n_i^2 = O(n) when the first-level hash is universal and m = n.

### Cuckoo Hashing

An elegant alternative for O(1) worst-case lookups with simpler structure.

Maintain two tables T_1 and T_2, each of size (1 + epsilon) * n, with independent hash functions h_1 and h_2. To insert key x:
1. Place x in T_1[h_1(x)].
2. If that cell was occupied by key y, evict y and place y in T_2[h_2(y)].
3. If *that* cell was occupied by key z, evict z and continue.
4. If the chain of evictions exceeds a threshold, rehash everything with new hash functions.

With O(1)-wise independent hash functions, insertion takes O(1) amortized expected time, and lookup is always O(1) worst case (check two cells).

### Bloom Filters

A Bloom filter is a space-efficient probabilistic data structure for set membership queries. It may produce false positives but never false negatives.

**Structure:** A bit array of m bits, initially all 0. Use k independent hash functions h_1, ..., h_k, each mapping to {0, ..., m-1}.

**Insert(x):** Set bits h_1(x), h_2(x), ..., h_k(x) to 1.

**Query(x):** Return "yes" if all bits h_1(x), ..., h_k(x) are 1; otherwise "no."

**False positive probability:** After inserting n elements, the probability a specific bit is still 0 is (1 - 1/m)^{kn} ~ e^{-kn/m}. The false positive probability is:

fp ~ (1 - e^{-kn/m})^k

This is minimized when k = (m/n) * ln 2, giving fp ~ (1/2)^k = (0.6185)^{m/n}.

For a 1% false positive rate, we need about m/n ~ 9.6 bits per element with k = 7 hash functions.

---

## Part 4: Random Graphs (Erdos-Renyi Model)

### The G(n,p) Model

Generate a graph on n vertices where each possible edge is included independently with probability p.

### Threshold Phenomena

Many graph properties exhibit sharp thresholds: there exists a critical p*(n) such that for p << p*, the property is almost surely absent, and for p >> p*, it is almost surely present.

**Connectivity threshold:** p* = ln(n) / n. For p = (ln n + c) / n, the probability the graph is connected converges to e^{-e^{-c}}, a double exponential.

**Triangle threshold:** p* = 1/n. The expected number of triangles is C(n,3) * p^3 ~ n^3 p^3 / 6. When p = omega(1/n), triangles appear; when p = o(1/n), they vanish.

**Hamiltonicity threshold:** Also p* ~ ln(n) / n, coinciding with connectivity (the bottleneck is isolated vertices).

### Giant Component

The most famous threshold: at p = 1/n, a *giant component* emerges.

- For p = c/n with c < 1: all components have size O(log n) with high probability.
- For p = c/n with c > 1: a unique giant component of size Theta(n) appears, and all other components have size O(log n).
- At p = 1/n: the largest component has size Theta(n^{2/3}).

This phase transition is analogous to percolation in physics and has deep connections to the behavior of random processes on networks -- relevant to understanding information flow in neural networks and multi-agent AI systems.

---

## Part 5: Concentration Inequalities

### Markov's Inequality

For a non-negative random variable X and a > 0: Pr[X >= a] <= E[X] / a. This is the weakest bound, but applies universally.

### Chebyshev's Inequality

Pr[|X - E[X]| >= a] <= Var[X] / a^2. Requires second-moment information. Gives Pr[|X - mu| >= k * sigma] <= 1/k^2.

### Chernoff Bounds

For independent random variables X_1, ..., X_n with X_i in [0, 1] and X = sum X_i, mu = E[X]:

**Multiplicative form:**
- Pr[X >= (1 + delta) * mu] <= (e^delta / (1 + delta)^{1+delta})^mu for delta > 0
- Pr[X <= (1 - delta) * mu] <= (e^{-delta} / (1 - delta)^{1-delta})^mu for 0 < delta < 1

**Simplified upper tail:** Pr[X >= (1 + delta) * mu] <= e^{-mu * delta^2 / 3} for 0 < delta <= 1.

**Simplified lower tail:** Pr[X <= (1 - delta) * mu] <= e^{-mu * delta^2 / 2}.

These bounds are *exponentially* stronger than Chebyshev -- the probability of deviation decreases exponentially with the amount of deviation.

### Applications

**Load balancing:** Throw n balls into n bins uniformly at random. The expected maximum load is Theta(log n / log log n). With Chernoff bounds, we can show the maximum is at most O(log n / log log n) with high probability.

**Randomized routing:** In parallel computing, Chernoff bounds prove that random routing strategies achieve near-optimal load balance with high probability.

---

## Part 6: Monte Carlo vs Las Vegas Algorithms

### Monte Carlo Algorithms

A Monte Carlo algorithm *always* terminates in bounded time but may produce an incorrect answer with some probability.

**One-sided error (RP, coRP):** A Monte Carlo algorithm for a decision problem has one-sided error if it is always correct on "no" instances but may err on "yes" instances (or vice versa).

**Two-sided error (BPP):** May err on both "yes" and "no" instances, but with probability < 1/2. By repeating O(log(1/delta)) times and taking majority vote, the error probability drops below delta.

**Example: Miller-Rabin primality test.** For a composite n, a random witness a in {2, ..., n-2} detects compositeness with probability >= 3/4. After k independent trials, the error probability is at most (1/4)^k.

### Las Vegas Algorithms

A Las Vegas algorithm *always* produces a correct answer but has random running time.

**Example: Randomized quicksort.** It always sorts correctly; only the number of comparisons is random.

Any Las Vegas algorithm with expected time T can be converted to a Monte Carlo algorithm that runs in time 2T and succeeds with probability >= 1/2 (by Markov's inequality). Conversely, a Monte Carlo algorithm with error <= 1/3 can be converted to a Las Vegas algorithm by checking the answer (if verification is efficient).

---

## Part 7: Randomized Optimization

### Simulated Annealing

A Metropolis-Hastings style algorithm for combinatorial optimization:

1. Start with an initial solution s.
2. Generate a neighbor s' by a random perturbation.
3. If cost(s') < cost(s), accept s'.
4. Otherwise, accept s' with probability e^{-(cost(s') - cost(s)) / T}, where T is the "temperature."
5. Gradually decrease T according to a cooling schedule.

At high temperature, the algorithm explores freely (escaping local minima). At low temperature, it exploits, converging to a good solution. Under a logarithmic cooling schedule T(t) = c / log(t), simulated annealing provably converges to the global optimum -- but exponentially slowly. In practice, faster schedules are used.

### Random Restarts

A simple but surprisingly effective strategy: run a local search algorithm multiple times from random starting points, return the best solution found.

If the probability of landing in the basin of attraction of the global optimum is p > 0, then after k restarts, the probability of finding it is 1 - (1-p)^k. For p = 0.01 and k = 460, this exceeds 0.99.

### Connection to AI

**SGD as randomized algorithm.** Stochastic gradient descent samples a random minibatch, computes an approximate gradient, and steps. The noise in the gradient estimate is not just tolerable -- it is beneficial, helping escape sharp minima and find flatter regions of the loss landscape that generalize better.

**Dropout.** Randomly zeroing activations during training is equivalent to training an exponential ensemble of sub-networks. This randomized regularization technique has strong connections to Bayesian model averaging.

**Random initialization.** The choice of random initialization (Xavier, He, etc.) determines which region of the loss landscape training begins in. The analysis of convergence depends on random matrix theory applied to the initial weight matrices.

---

## Watch -- Primary

- **MIT 6.046J** -- "Randomized Algorithms" lectures (covers indicator random variables, randomized quicksort analysis, universal hashing)
- **Reducible** -- "Bloom Filters" (excellent visual explanation of the data structure and false positive analysis)
- **3Blue1Brown** -- any relevant probability/concentration inequality content for building intuition

---

## Read -- Primary

- **Motwani and Raghavan, "Randomized Algorithms"** -- Chapters 1-4 and 6. Chapter 1 introduces the framework; Chapter 3 covers Chernoff bounds and applications; Chapter 4 covers the probabilistic method; Chapter 6 covers hashing.
- **CLRS** -- Chapter 5 (Probabilistic Analysis and Randomized Algorithms) and Chapter 7 (Quicksort analysis).
- **Mitzenmacher and Upfal, "Probability and Computing"** -- An accessible alternative/supplement that covers concentration inequalities, random graphs, and Markov chains with algorithmic applications.

---

## Exercises

1. **Indicator variable practice.** Using indicator random variables, compute the expected number of inversions in a random permutation of n elements. (An inversion is a pair (i, j) with i < j but pi(i) > pi(j).)

2. **Randomized quicksort variance.** Compute the variance of the number of comparisons in randomized quicksort. Show that Var[X] = O(n^2). Use Chebyshev's inequality to give a high-probability bound. Then use the sharper result that the distribution is concentrated (subgaussian tails).

3. **Universal hashing analysis.** Prove that for a universal hash family with n keys and table size m = n, the expected total number of collisions is at most n/2. Use this to bound the expected worst-case chain length.

4. **Bloom filter design.** You need to store 10 million URLs in a Bloom filter with a false positive rate below 0.1%. How many bits do you need? How many hash functions? What is the memory savings compared to storing the actual URLs?

5. **Chernoff bound application.** A randomized algorithm succeeds independently with probability 0.6 on each trial. How many trials are needed to guarantee at least one success with probability >= 1 - 10^{-6}? How many trials to guarantee *at least 60%* of trials succeed with probability >= 1 - 10^{-6}?

6. **Giant component simulation.** Write pseudocode (or actual code) to simulate G(n, p) for n = 10000 and p = c/n for c in {0.5, 0.9, 1.0, 1.1, 1.5, 2.0}. For each c, compute the size of the largest component. Verify the phase transition at c = 1.

7. **SGD as randomized algorithm.** Consider minimizing f(x) = (1/n) * sum_{i=1}^{n} f_i(x). Full gradient descent computes the exact gradient at cost O(n) per step. SGD samples one f_i uniformly and steps with cost O(1) per step. Using the analysis of randomized algorithms, argue why SGD with O(n) steps can approximate what full GD does in O(1) step, and explain the role of variance reduction techniques (SVRG, SAGA) in this context.
