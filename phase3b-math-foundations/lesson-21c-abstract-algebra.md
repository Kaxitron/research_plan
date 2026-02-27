# Lesson 21c: Abstract Algebra — Groups, Symmetry, and Neural Networks

[← Computability](lesson-21b-computability.md) | [Back to TOC](../README.md) | [Next: Topology →](lesson-21d-topology.md)

---

> **Why this lesson exists:** Singular Learning Theory (Lesson 33) — one of the most promising mathematical frameworks for understanding neural network generalization — is built on the symmetries of neural networks. When you permute the neurons in a hidden layer, the network computes the exact same function. These symmetries form mathematical *groups*, and they create *singularities* in the loss landscape that SLT analyzes. Without understanding what a group is, SLT stays a black box. Groups also appear in equivariant neural networks, weight space geometry, and the structure of attention heads. This lesson gives you the minimum abstract algebra to unlock those connections.

## 🎯 Core Concepts

### What Is a Group?

- **A group is a set with an operation that satisfies four axioms.** Think of it as the mathematical formalization of "symmetry." A group captures all the ways you can transform something and end up with the same object.

- **The four axioms (using multiplication notation):**
  1. **Closure:** if a and b are in the group, then ab is in the group. (Combining two symmetries gives another symmetry.)
  2. **Associativity:** (ab)c = a(bc). (The order of *applying* doesn't matter, though the order of *which* operations you do matters.)
  3. **Identity:** there exists an element e such that ae = ea = a. (Doing nothing is a symmetry.)
  4. **Inverse:** for every a, there exists a^(-1) such that aa^(-1) = e. (Every symmetry can be undone.)

- **Concrete examples that build intuition:**
  - **Integers under addition:** 0 is the identity, -n is the inverse of n. Infinite group.
  - **Rotations of a square:** four rotations (0, 90, 180, 270 degrees). The identity is 0 degrees. The inverse of 90 is 270. This is the cyclic group Z/4Z.
  - **Permutations of {1, 2, 3}:** all ways to rearrange three objects. There are 3! = 6 elements. This is the symmetric group S₃. Composing two permutations gives another permutation.
  - **Invertible n x n matrices under multiplication:** the identity is I, the inverse is A^(-1). This is the general linear group GL(n). The matrices from Lessons 3-8 live here.

### Permutation Groups — The Key to Neural Network Symmetry

- **The symmetric group S_n** is the group of all permutations of n elements. It has n! elements. For large n, this is astronomically large (100! > 10^157).

- **Why permutations matter for neural networks:** consider a hidden layer with n neurons. Each neuron has incoming weights (a row of W₁) and outgoing weights (a column of W₂). If you simultaneously permute the rows of W₂ and the columns of W₁ (and the biases), the network computes *exactly the same function.* The neurons just got relabeled — nothing about the computation changed.

- **This means:** for a network with one hidden layer of n neurons, the symmetric group S_n acts on the weight space. Every weight configuration has n! equivalent copies. The loss landscape has a built-in n!-fold symmetry.

- **Geometric picture:** imagine the loss landscape. Every minimum has n! copies, related by neuron permutation. These copies aren't isolated — they're connected by paths through the loss landscape (the permutations are continuous in weight space for networks with smooth activations). This creates a complex topology of equivalent solutions.

### Group Actions — How Groups Transform Objects

- **A group action** is a formal way of saying "group G transforms set X." Each group element g defines a function from X to X, and the group operation corresponds to composition of functions.

- **The action of S_n on weight space:** each permutation sigma in S_n rearranges the neurons. This maps one weight vector to another weight vector with the same loss. Formally, sigma acts on the parameter space Theta by permuting rows/columns of weight matrices.

- **Orbits and stabilizers:**
  - The **orbit** of a point x is the set of all points reachable from x by applying group elements: {g(x) : g in G}. For a weight vector w, its orbit under S_n is the set of all equivalent weight vectors.
  - The **stabilizer** of x is the set of group elements that fix x: {g in G : g(x) = x}. For weight vectors, the stabilizer is the set of neuron permutations that don't actually change anything — this happens when some neurons are *identical* (same weights).

- **The orbit-stabilizer theorem:** |orbit| x |stabilizer| = |group|. If the stabilizer is trivial (only identity), the orbit has |G| elements — full symmetry, no coincidences. If some neurons are identical, the stabilizer is non-trivial and the orbit is smaller. This matters for SLT because **singularities occur where stabilizers are large** — where neurons coincide and the symmetry "collapses."

### Singularities from Symmetry — The SLT Connection

- **Why this matters for SLT:** consider what happens when two neurons in a hidden layer have exactly the same weights. The permutation swapping them is in the stabilizer — it does nothing. At this point in weight space, the loss landscape has a *singularity:* the Fisher information matrix degenerates, the Hessian has extra zero eigenvalues, and standard statistical theory breaks down.

- **The simplest example:** a network with 2 hidden neurons computing f(x) = a₁ * sigma(w₁x) + a₂ * sigma(w₂x). When w₁ = w₂ and a₁ = a₂, this is the same as a single neuron with double the output weight. The two-neuron description is "redundant" — there's a whole curve of equivalent parameters, not just a point. This curve is a singularity.

- **Phase transitions occur at these singularities.** When a model is training and neurons begin to "split" from identical to specialized, the model passes through a singularity. SLT's RLCT (real log canonical threshold) measures how severe these singularities are, which determines the model's effective complexity.

- **Without group theory, you can't explain *why* these singularities exist.** They exist because the neural network function is invariant under the group action — the symmetry forces degeneracies in the parameter space.

### Quotient Spaces — Removing Redundancy

- **The quotient space Theta / G** is the parameter space with the group symmetry "factored out." Each point in the quotient represents an equivalence class of parameter vectors that compute the same function.

- **Intuition:** imagine the surface of a cylinder. If you identify (glue together) all points with the same height, you get a line — the quotient. The cylinder has a rotational symmetry; the quotient removes it.

- **For neural networks:** the "true" parameter space (up to symmetry) is Theta / S_n, which is much smaller than Theta. The loss function on Theta / S_n has no permutation-symmetry-induced redundancy. But this quotient space is not smooth — it has singularities where orbits change dimension (where neurons coincide). These are exactly the singularities SLT studies.

### Other Groups in ML

- **Orthogonal group O(n):** rotations and reflections of n-dimensional space. Matrices Q where QQ^T = I. Preserves lengths and angles. SVD's U and V are in O(n). The orthogonal group appears in understanding how representations rotate during training.

- **Special orthogonal group SO(n):** rotations only (det = +1, no reflections). The "clean" symmetry group of rotations.

- **Equivariant neural networks:** networks designed to respect a known group symmetry. Convolutional networks are equivariant under translation (shifting the input shifts the output the same way). Graph neural networks are equivariant under node permutation. The key principle: if you know the symmetry, bake it in — don't make the network learn it from scratch.

## 📺 Watch — Primary

1. **3Blue1Brown — "Groups, the Monsters, and the quest to understand symmetry"**
   - Search YouTube — 3B1B's treatment of group theory with beautiful visuals
2. **Visual Group Theory (Nathan Carter) — lecture videos**
   - Search YouTube — excellent visual approach to groups with Cayley diagrams and multiplication tables
3. **Socratica — "Abstract Algebra: What is a Group?"**
   - Short, clear introduction with concrete examples

## 📺 Watch — Secondary

4. **Mathemaniac — "Group Theory and Physics"**
   - Shows how symmetry groups appear in the physical world
5. **Michael Penn — "Abstract Algebra" playlist**
   - More rigorous treatment if you want to go deeper

## 📖 Read — Primary

- **"Visual Group Theory" by Nathan Carter** — Chapters 1-4
  - The most visual, intuition-first group theory book available. Uses Cayley diagrams and color-coded multiplication tables. Perfect for this curriculum's approach.
- **"Algebra: Chapter 0" by Aluffi** — Chapter 1 (if you want the formal treatment)
  - More abstract but beautifully motivated. Chapter 1 covers groups with the "right" level of generality.

## 📖 Read — Secondary

- **"Neural Network Symmetries and the Loss Landscape"** — survey material
  - Search for recent papers on weight space symmetries
- **LessWrong / Alignment Forum posts on SLT**
  - https://www.lesswrong.com/tag/singular-learning-theory
  - The community's treatment connecting groups to SLT
- **"An Introduction to Singular Learning Theory" — various blog posts**
  - Several accessible introductions exist that explain the role of symmetry groups

## 📖 Read — Going Deep

- **"Algebraic Geometry and Statistical Learning Theory" by Sumio Watanabe** — Chapter 2
  - The original SLT text. Chapter 2 covers the algebraic geometry foundation, including how group actions create singularities.
- **"Equivariant Neural Networks" survey papers**
  - Formal treatment of how group theory constrains network architecture

## 🔨 Do

- **Permutation group exercise:** write out the multiplication table for S₃ (all 6 permutations of {1,2,3}). Verify closure, find the identity, find each element's inverse. Notice: the group is NOT commutative (ab != ba for some elements).
- **Neural network symmetry demonstration:** create a simple 2-input, 3-hidden-neuron, 1-output network in PyTorch. Find a specific permutation of the hidden neurons. Show that the permuted weights compute the exact same output on all test inputs.
- **Orbit counting:** for a network with 4 hidden neurons where all neurons are distinct, how many equivalent weight vectors exist? (Answer: 4! = 24.) What if 2 neurons are identical? (Answer: 24/2 = 12.) What if all 4 are identical? (Answer: 24/24 = 1.)
- **Singularity visualization:** take a 2-hidden-neuron network f(x) = a₁ * relu(w₁x) + a₂ * relu(w₂x). Plot the function for various (w₁, w₂, a₁, a₂) values. Then set w₁ = w₂ and observe that (a₁, a₂) and (a₂, a₁) give the same function — the singularity.
- **Key exercise:** explain in your own words why a network with n hidden neurons has at least n! equivalent parameterizations. Then explain why this creates problems for gradient descent (the loss landscape has many "copies" of each solution) and for statistical analysis (the Fisher information matrix is singular at coincident neurons).

## 🔗 ML Connection

- **Weight space symmetries** mean that the loss landscape of neural networks is fundamentally different from the smooth, well-behaved landscapes assumed by classical optimization theory. Every minimum has n! copies for each hidden layer of n neurons. This is why loss landscape analysis must account for symmetry.
- **Equivariant architectures** (CNNs, GNNs, transformers) are designed around group symmetry. Convolutions are equivariant under translation. Attention is equivariant under permutation of the input sequence (without positional encoding). Understanding the symmetry group tells you what the architecture can and cannot represent.
- **Mode connectivity:** the observation that different trained networks (different minima) are often connected by low-loss paths relates to the group structure. Permutation of neurons provides one class of such paths.
- **Lottery ticket hypothesis:** the idea that sparse subnetworks within large networks can match full network performance. The group structure of weight space is relevant to understanding why these subnetworks exist.

## 🧠 Alignment Connection

- **SLT's RLCT** is the central quantity for understanding neural network generalization in a principled way. The RLCT depends on the singularity structure, which comes from group symmetry. To go from "I know what RLCT means" to "I can compute or reason about RLCT," you need the group theory in this lesson.
- **Phase transitions** during training — when a model suddenly acquires a new capability — occur as the training trajectory passes through singularities created by symmetry. Understanding these transitions is critical for predicting when dangerous capabilities might emerge.
- **Developmental interpretability** studies how model internals change during training. The group-theoretic structure of weight space determines which developmental paths are possible and which transitions are abrupt vs. gradual.
