# Lesson 74: Turing Machines and Undecidability

[<- Context-Free Grammars](lesson-73-context-free-grammars.md) | [Back to TOC](../README.md) | [Next: Kolmogorov Complexity ->](lesson-75-kolmogorov-complexity.md)

---

> **Why this lesson exists:** Turing machines define the boundary between what is and is not computable, and undecidability results establish absolute limits on what any algorithm -- including any AI system -- can ever do. For AI alignment, these results are not merely theoretical curiosities: Rice's theorem directly implies that there is no general algorithm to determine whether an AI system satisfies any non-trivial behavioral specification. Understanding these limits is essential for developing realistic expectations about what alignment verification can achieve and for designing approaches that work within these constraints.

> **Estimated time:** 18--24 hours

---

## Part 1: Turing Machine Formal Definition

### The Model

A Turing machine (TM) is a 7-tuple M = (Q, Sigma, Gamma, delta, q_0, q_accept, q_reject) where:

- **Q** is a finite set of states
- **Sigma** is the input alphabet (not containing the blank symbol)
- **Gamma** is the tape alphabet, where Sigma is a subset of Gamma and the blank symbol (denoted by underscore or B) is in Gamma
- **delta: Q x Gamma -> Q x Gamma x {L, R}** is the transition function
- **q_0 in Q** is the start state
- **q_accept in Q** is the accept state
- **q_reject in Q** is the reject state (q_accept != q_reject)

### Tape, Head, and Operation

The Turing machine operates on an infinite tape divided into cells, each containing a symbol from Gamma. Initially, the tape contains the input string followed by blanks extending infinitely to the right. The machine has a read/write head positioned on the leftmost cell.

At each step, the machine:
1. Reads the symbol under the head
2. Based on the current state and the symbol read, the transition function specifies:
   - A new state to enter
   - A symbol to write (replacing the current symbol)
   - A direction to move the head (Left or Right)
3. If the machine enters q_accept, it halts and accepts. If it enters q_reject, it halts and rejects. Otherwise, it continues.

A critical feature is that the machine might never halt -- it could loop forever. This possibility is fundamental and gives rise to the concept of semi-decidability.

### Why This Model Matters

The Turing machine is remarkable for its simplicity and power. Despite having only a finite number of states and a single tape that can only be accessed one cell at a time, it can compute anything that any known computational model can compute. This robustness is the empirical content of the Church-Turing thesis.

The components of a TM correspond to components of modern computers: the finite control (states and transitions) is like the CPU, the tape is like memory, and the head is like the memory bus. The key abstraction is that memory is unbounded -- the tape extends infinitely.

### Example: Binary Addition

Consider a TM that adds 1 to a binary number. The input is a binary string representing a number, and the machine should halt with the tape containing the binary representation of the number plus one.

The strategy: move the head to the rightmost bit, and carry out addition with carry, moving left. If the current bit is 0, change it to 1 and halt. If the current bit is 1, change it to 0 (carry) and move left. If you run out of digits (reach a blank), write 1 and halt.

This requires about 4 states and demonstrates how simple state machines operating on tape can perform arithmetic.

### Variants of Turing Machines

Several variations on the basic TM model exist, and all are equivalent in computational power:

- **Multi-tape TMs:** Have multiple tapes with independent heads. Can be simulated by a single-tape TM with at most a quadratic slowdown.
- **Nondeterministic TMs:** At each step, the machine can choose from multiple transitions. Accepts if any computation path reaches q_accept. Can be simulated by a deterministic TM (but with potentially exponential slowdown).
- **Two-way infinite tape:** Tape extends infinitely in both directions. Easily simulated by the standard model.
- **Multi-dimensional tapes, multiple heads, etc.:** All equivalent.

The robustness of the TM model under these variations is strong evidence for the Church-Turing thesis.

---

## Part 2: The Church-Turing Thesis

### Statement

The Church-Turing thesis asserts:

*The class of functions that are computable by an effective procedure (an algorithm) is exactly the class of functions computable by a Turing machine.*

This is a thesis, not a theorem, because "effective procedure" is an informal notion. However, every proposed formalization of computation -- lambda calculus (Church), recursive functions (Godel), Turing machines (Turing), Post systems, register machines, and many others -- has been shown to define exactly the same class of computable functions.

### Significance

The Church-Turing thesis tells us that when we prove something is not computable by a Turing machine, it is not computable by *any* algorithmic method. This is what gives undecidability results their force: they are not artifacts of a particular model but fundamental limitations on all computation.

For AI alignment, the thesis means that the impossibility results we derive (like Rice's theorem) apply to any AI system, regardless of its architecture. A transformer, a diffusion model, a symbolic AI system, a quantum computer -- none can overcome Turing-undecidability.

### The Physical Church-Turing Thesis

A stronger version claims that any physically realizable computation can be simulated by a Turing machine. This is more controversial -- it touches on questions about hypercomputation, the computational power of physical systems, and whether the universe itself is computable. For our purposes, the standard thesis suffices.

---

## Part 3: The Universal Turing Machine

### Encoding Turing Machines

A key insight is that Turing machines can be described as finite strings. We can encode a TM M as a binary string <M> by systematically encoding its states, alphabet, and transition function. This encoding allows us to treat TMs as both programs and data.

### The Universal Machine

A universal Turing machine U takes as input a pair (<M>, w) -- an encoding of a TM M and an input string w -- and simulates M on w. Specifically:

- If M accepts w, then U accepts (<M>, w)
- If M rejects w, then U rejects (<M>, w)
- If M loops on w, then U loops on (<M>, w)

The existence of U is profound: it means there is a single, fixed machine that can simulate any other Turing machine. This is exactly the concept of a general-purpose computer -- a stored-program machine that can run any program.

### Construction Sketch

U works as follows:
1. Parse <M> to extract M's transition function, states, and alphabets.
2. Maintain a simulation of M's tape on its own tape (e.g., using a multi-track encoding).
3. Track M's current state and head position.
4. At each step, look up M's transition in the encoded transition function and apply it to the simulated tape.

The details are tedious but straightforward. What matters is the conceptual point: computation is universal.

### Connection to Modern Computing

The universal Turing machine is the theoretical foundation for all general-purpose computing. Your laptop, a cloud server, and an AI training cluster are all physical realizations of the universal TM concept. The program (neural network weights, for instance) is the <M> part, and the input data is the w part.

---

## Part 4: The Halting Problem

### Statement

The halting problem asks: given a Turing machine M and an input w, does M halt (either accept or reject) when run on w?

Define the language:

HALT = {(<M>, w) : M is a TM and M halts on input w}

**Theorem (Turing, 1936):** HALT is undecidable. That is, there is no Turing machine that decides HALT.

### Proof by Diagonalization

This is one of the most important proofs in all of mathematics and computer science. It uses a self-referential argument inspired by Cantor's diagonal argument.

Assume for contradiction that there exists a TM H that decides HALT. That is, H(<M>, w) = accept if M halts on w, and H(<M>, w) = reject if M loops on w.

Construct a new TM D that takes input <M> (a TM description) and does the following:
1. Run H(<M>, <M>) -- ask whether M halts when given its own description as input.
2. If H says "halt" (accepts), then D enters an infinite loop.
3. If H says "loop" (rejects), then D halts and accepts.

Now consider: what happens when we run D on input <D>?

- If D(<D>) halts: then H(<D>, <D>) = accept (H correctly says D halts on <D>), so by D's construction, D loops on <D>. Contradiction.
- If D(<D>) loops: then H(<D>, <D>) = reject (H correctly says D loops on <D>), so by D's construction, D halts on <D>. Contradiction.

Both cases lead to contradiction, so our assumption that H exists must be false. The halting problem is undecidable.

### Understanding the Proof

The key insight is self-reference: D is designed to do the opposite of what H predicts. This is the same logical structure as the liar paradox ("this statement is false") and Cantor's proof that the reals are uncountable.

The proof works because Turing machines can be given their own descriptions as input -- this is possible because TMs are encoded as strings, and TMs operate on strings. The ability of programs to reflect on themselves is what creates the impossibility.

### Semi-Decidability

Although HALT is undecidable, it is semi-decidable (also called recursively enumerable). There exists a TM that:
- Accepts if M halts on w (by simply simulating M on w and waiting)
- Loops if M does not halt on w

The complement of HALT (the set of pairs where M does not halt on w) is not even semi-decidable. This asymmetry between HALT and its complement is a fundamental feature of the decidability landscape.

---

## Part 5: Rice's Theorem

### Statement

Rice's theorem is a sweeping generalization of the undecidability of the halting problem:

**Rice's Theorem:** Every non-trivial semantic property of Turing machines is undecidable.

More precisely: let P be any property of the languages recognized by Turing machines (a "semantic" property). If P is non-trivial -- meaning some TMs have the property and some do not -- then the language {<M> : L(M) has property P} is undecidable.

### Examples

Rice's theorem immediately gives us that all of the following are undecidable:

- Does a TM accept the empty string?
- Does a TM accept all strings?
- Is the language of a TM finite?
- Is the language of a TM regular?
- Is the language of a TM equal to some specific language?
- Does a TM halt on all inputs? (This is a semantic property because it concerns the TM's behavior on all inputs, which depends on its language.)

### What Rice's Theorem Does Not Cover

Rice's theorem only applies to semantic properties -- properties of the language L(M) recognized by M. It does not apply to syntactic properties of the machine description, such as:

- Does the TM have fewer than 100 states? (Decidable -- just count.)
- Does the TM's description contain the substring "abc"? (Decidable -- string matching.)
- Does the TM move its head left within the first 5 steps on empty input? (Decidable -- simulate for 5 steps.)

### Proof Sketch

The proof reduces from the halting problem. Given a TM M and input w, we construct a new TM M' that:
1. First simulates M on w (ignoring the actual input to M')
2. If M halts on w, then M' proceeds to behave like some fixed TM T that has property P
3. If M does not halt on w, M' loops forever (recognizing the empty language)

If property P is non-trivial, we can choose T to have property P. Then:
- If M halts on w, L(M') = L(T) which has property P
- If M does not halt on w, L(M') = empty set which does not have property P (or we handle this case by choosing T appropriately)

So deciding whether M' has property P decides whether M halts on w, which is impossible.

### Devastating Implications for AI Safety

Rice's theorem has direct and sobering implications for AI alignment:

**You cannot build a general "is this AI safe?" checker.** If "safety" is defined as any non-trivial property of the AI system's input-output behavior (which it must be -- a trivially safe system that always outputs nothing is useless), then Rice's theorem says no algorithm can determine whether an arbitrary AI system satisfies this property.

This does not mean safety verification is hopeless -- it means we must be more creative:

- **Restrict the class of systems** being checked (don't try to verify arbitrary TMs)
- **Use approximate methods** (testing, formal verification of restricted properties)
- **Design systems that are verifiable by construction** (build safety in rather than checking it after the fact)
- **Accept probabilistic or partial guarantees**

These are exactly the strategies pursued in modern AI alignment research.

---

## Part 6: The Decidability Landscape

### Decidable Languages

A language is **decidable** (or recursive) if some TM always halts on every input and correctly accepts strings in the language and rejects strings not in it.

Examples of decidable problems:
- Is a string in the language of a given DFA?
- Is a given CFG empty (generates no strings)?
- Is a given string in the language of a given CFG?
- Are two DFAs equivalent?
- Is a given number prime?

### Semi-Decidable Languages

A language is **semi-decidable** (or recursively enumerable, or r.e.) if some TM accepts every string in the language but may loop forever on strings not in the language.

The key: a semi-decider can confirm membership but cannot confirm non-membership in bounded time.

Examples:
- HALT = {(<M>, w) : M halts on w}
- {<M> : L(M) is non-empty} (there exists some input M accepts)

### Co-Semi-Decidable Languages

A language is co-semi-decidable (or co-r.e.) if its complement is semi-decidable. Equivalently, there is a TM that rejects every string not in the language but may loop on strings in the language.

**Key theorem:** A language is decidable if and only if it is both semi-decidable and co-semi-decidable. This is because if you have a semi-decider for L and a semi-decider for the complement of L, you can run them in parallel (interleaving steps); one of them must eventually halt, telling you whether the input is in L.

### Beyond Semi-Decidable: The Arithmetic Hierarchy

The classification continues above semi-decidable. The arithmetic hierarchy stratifies undecidable problems by how many alternations of quantifiers are needed:

- Sigma_1 = semi-decidable (there exists a halting computation)
- Pi_1 = co-semi-decidable (for all computations, they halt)
- Sigma_2 = there exists... for all... (e.g., "L(M) is infinite")
- And so on

This hierarchy is strict -- each level contains problems not in the level below.

---

## Part 7: Reductions

### What is a Reduction?

A reduction from problem A to problem B is a computable function f such that x is in A if and only if f(x) is in B. We write A <=_m B (A is many-one reducible to B, or A mapping-reduces to B).

The intuition: if you can solve B, you can solve A (by applying f first, then the solver for B). Contrapositive: if A is undecidable, then B is undecidable too.

### Proving Undecidability via Reduction

To show that a problem B is undecidable, reduce a known undecidable problem (typically HALT or its variants) to B. The strategy:

1. Assume B is decidable by some TM R_B.
2. Show how to use R_B to decide A (a known undecidable problem).
3. This contradicts the undecidability of A.

### Example: Emptiness Is Undecidable

Let E_TM = {<M> : L(M) = empty set}. We show E_TM is undecidable by reduction from HALT.

Given (<M>, w), construct M' that:
1. On input x, M' first simulates M on w.
2. If M halts on w, M' then simulates some machine that accepts everything.
3. If M does not halt on w, M' loops.

Then L(M') is empty if and only if M does not halt on w. So if we could decide E_TM, we could decide HALT. Contradiction.

### Example: Equivalence Is Undecidable

Let EQ_TM = {(<M1>, <M2>) : L(M1) = L(M2)}. This is also undecidable (reducible from E_TM by comparing M with a fixed machine that rejects everything).

---

## Part 8: The Busy Beaver Function

### Definition

The Busy Beaver function BB(n) is defined as the maximum number of 1s that an n-state Turing machine can write on a blank tape before halting. (The machine must eventually halt -- machines that loop forever do not count.)

### Growth Rate

BB(n) grows faster than any computable function. This is not just "fast" -- it outgrows every function you could ever write a program to compute. For any computable function f, there exists N such that BB(n) > f(n) for all n > N.

Known values:
- BB(1) = 1
- BB(2) = 4
- BB(3) = 6
- BB(4) = 13
- BB(5) >= 47,176,870 (recently established bounds suggest vastly larger values)
- BB(6) is known to be enormous (related to Rado's Sigma function values)

### Why BB Is Uncomputable

If BB were computable, we could decide the halting problem: to check if an n-state TM M halts on empty input, simulate M for BB(n) steps. If it hasn't halted by then, it never will (since BB(n) is the maximum steps any halting n-state machine takes). But the halting problem is undecidable, so BB is uncomputable.

### Connection to AI

The Busy Beaver function illustrates that there are well-defined mathematical functions that no AI system can compute. The uncomputability of BB is not due to a lack of computing power or data -- it is a fundamental logical impossibility. This underscores that some questions about AI systems (like "what is the maximum harm this system could cause across all possible inputs?") may be similarly uncomputable.

---

## Watch -- Primary

1. **Neso Academy -- "Theory of Computation" (Turing machine and decidability sections)**
   - *Covers TM formal definitions, multi-tape TMs, the universal TM, the halting problem proof, Rice's theorem, and reductions. Work through approximately 15-20 videos in the relevant sections.*

2. **Computerphile -- "Halting Problem" and "Turing Machines Explained"**
   - *Excellent supplementary explanations of the halting problem diagonalization proof and TM fundamentals, presented accessibly.*

3. **PBS Infinite Series -- "The Busy Beaver Problem"**
   - *Engaging introduction to the Busy Beaver function and its connection to uncomputability.*

---

## Read -- Primary

- **"Introduction to the Theory of Computation" by Michael Sipser** -- Chapters 3, 4, and 5
  - Chapter 3: The Church-Turing Thesis (TM definition, variants, Church-Turing thesis)
  - Chapter 4: Decidability (decidable problems about regular and context-free languages, the halting problem, undecidable problems)
  - Chapter 5: Reducibility (undecidability proofs via reduction, Rice's theorem, mapping reducibility)

---

## Exercises

1. **TM Design:** Design a Turing machine that accepts the language {0^n 1^n : n >= 0}. Provide the full state diagram with transitions. Trace its execution on inputs "0011" (accept) and "011" (reject).

2. **TM Design:** Design a Turing machine that computes the function f(x) = x + 1, where x is represented in unary (a string of 1s). The machine should halt with the output on the tape.

3. **Halting Problem Deep Dive:** Write out the diagonalization proof of the undecidability of the halting problem in complete detail. Then explain, in your own words, why the self-referential step works -- what goes wrong if we try to apply the same argument to simpler computational models (like DFAs)?

4. **Rice's Theorem Application:** For each of the following properties, determine whether it is decidable. If it is undecidable, explain which part of Rice's theorem applies. If it is decidable, explain why Rice's theorem does not apply.
   - "TM M has at most 50 states"
   - "TM M accepts at least one string of length less than 100"
   - "TM M accepts a regular language"
   - "TM M, when given input epsilon, moves its head left at least once"

5. **Reduction Practice:** Prove that the following problem is undecidable by reducing from the halting problem: "Given a TM M, does M accept all strings of length at most 5?"

6. **Semi-Decidability:** Show that {<M> : L(M) is infinite} is semi-decidable but not decidable. For semi-decidability, describe a TM that accepts exactly this language (it may loop on TMs whose languages are finite). For undecidability, give a reduction from the halting problem.

7. **Universal TM Simulation:** Describe in detail how a universal TM U simulates a given TM M on input w. What encoding scheme do you use for <M>? How does U handle the simulation of M's tape, state, and head? What is the time overhead of the simulation?

8. **Busy Beaver Analysis:** Look up the current best known bounds for BB(5) and BB(6). Explain why pinning down the exact value of BB(n) for relatively small n is so difficult. What is the connection between BB and open problems in mathematics (like the Goldbach conjecture)?

9. **Alignment Implications Essay:** Write a 1-2 page essay addressing the following: Given Rice's theorem, what realistic approaches to AI safety verification remain? Discuss the tradeoff between the generality of the systems you want to verify and the strength of the guarantees you can provide. Consider approaches like: restricting to specific system architectures, runtime monitoring, probabilistic guarantees, formal verification of finite-state abstractions.

10. **Reflection:** The halting problem shows that self-reference creates fundamental limits on computation. In what ways does AI alignment involve self-reference? (Hint: consider an AI system reasoning about its own behavior, or a system designed to improve its own code.)
