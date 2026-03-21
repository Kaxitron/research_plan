# Lesson 72: Finite Automata and Regular Languages

[<- Recurrences & Generating Functions](lesson-71-recurrences-generating-functions.md) | [Back to TOC](../README.md) | [Next: Context-Free Grammars ->](lesson-73-context-free-grammars.md)

---

> **Why this lesson exists:** Finite automata are the simplest model of computation, and understanding them is foundational for reasoning about what can and cannot be computed -- a question that lies at the heart of AI alignment. When we ask whether an AI system's behavior can be verified, monitored, or constrained, we are implicitly asking questions about the computational complexity of those tasks. Regular languages and finite automata give us the first precise framework for characterizing a class of problems that *can* be efficiently decided, and they appear directly in practical AI systems through pattern matching, tokenization, and finite-state transducers used in natural language processing pipelines.

> **Estimated time:** 15--20 hours

---

## Part 1: Deterministic Finite Automata (DFA)

### Formal Definition

A deterministic finite automaton is a 5-tuple M = (Q, Sigma, delta, q_0, F) where:

- **Q** is a finite set of states
- **Sigma** is a finite alphabet (the set of input symbols)
- **delta: Q x Sigma -> Q** is the transition function
- **q_0 in Q** is the start state
- **F subset of Q** is the set of accept (final) states

The machine begins in state q_0, reads one symbol at a time from an input string, and transitions between states according to delta. After reading the entire input, the machine accepts if and only if it is in a state belonging to F.

The key constraint that makes this model "deterministic" and "finite" is twofold: (1) there are finitely many states, meaning the machine has bounded memory, and (2) for every state and every input symbol, there is exactly one transition -- the machine never has a choice about where to go next.

### State Diagrams

The most intuitive representation of a DFA is a directed graph called a state diagram:

- Each state is drawn as a circle (node)
- Accept states have a double circle
- The start state has an arrow pointing to it from nowhere
- Transitions are directed edges labeled with the input symbol that triggers them

For example, consider a DFA that accepts all binary strings containing an even number of 1s. This machine has two states: q_even (start and accept) and q_odd. Reading a 0 in either state loops back to the same state. Reading a 1 toggles between q_even and q_odd. The machine accepts precisely when it ends in q_even, which happens exactly when the number of 1s seen is even.

### Transition Tables

An equivalent but more systematic representation is the transition table. For the even-number-of-1s example:

| State    | Input 0  | Input 1  |
|----------|----------|----------|
| ->*q_even | q_even  | q_odd   |
| q_odd    | q_odd    | q_even  |

The arrow (->) marks the start state, and the asterisk (*) marks accept states. Transition tables are particularly useful when implementing DFAs in code, as the table maps directly to a lookup array.

### Extended Transition Function

We extend delta to handle strings rather than single symbols. Define delta-hat (the extended transition function) recursively:

- delta-hat(q, epsilon) = q (reading the empty string leaves you in the same state)
- delta-hat(q, wa) = delta(delta-hat(q, w), a) (process the string w first, then take one more step on symbol a)

The language of a DFA M, written L(M), is the set of all strings w such that delta-hat(q_0, w) is in F.

### Examples and Practice

**Example 1:** Design a DFA over Sigma = {a, b} that accepts all strings starting with "ab".

The idea: you need to track whether you have seen "a" as the first character and "b" as the second. This requires at least four states: a start state (waiting for 'a'), a state after seeing 'a' (waiting for 'b'), an accept state (seen "ab", now accept everything), and a "dead" or "trap" state (wrong prefix, reject forever). Once in the accept state, any further input keeps you there. Once in the dead state, any further input keeps you there.

**Example 2:** Design a DFA over Sigma = {0, 1} that accepts strings representing binary numbers divisible by 3.

This is a classic example that illustrates the power of thinking about what information the states need to track. Since we care about divisibility by 3, the states represent the remainder when dividing by 3: q_0 (remainder 0, start and accept), q_1 (remainder 1), q_2 (remainder 2). When you read a new bit b, the number so far doubles and adds b, so the new remainder is (2 * old_remainder + b) mod 3. This gives a clean 3-state DFA.

---

## Part 2: Nondeterministic Finite Automata (NFA)

### Nondeterminism

A nondeterministic finite automaton relaxes the constraint that each state must have exactly one transition per input symbol. Instead, from any state on any input symbol, the machine may have zero, one, or multiple possible transitions. The machine is said to accept a string if *there exists* at least one sequence of choices leading to an accept state.

Formally, an NFA is a 5-tuple N = (Q, Sigma, delta, q_0, F) where the transition function is now:

- **delta: Q x (Sigma union {epsilon}) -> P(Q)**

Here P(Q) denotes the power set of Q -- the set of all subsets of Q. This means delta returns a *set* of possible next states rather than a single state.

The conceptual model is that the machine "guesses" which transition to take, and it accepts if any guess leads to acceptance. You can also think of it as exploring all possible computation paths simultaneously.

### Epsilon-Transitions

NFAs may include epsilon-transitions (epsilon-moves): transitions that occur without reading any input symbol. These allow the machine to change state "for free." The epsilon-closure of a state q, written ECLOSE(q), is the set of all states reachable from q by following zero or more epsilon-transitions.

Epsilon-transitions are a notational convenience -- they never add computational power beyond what a standard NFA can do -- but they make certain constructions much cleaner, particularly when combining automata.

### NFA Execution Model

To determine whether an NFA accepts a string, you can think of tracking a *set* of current states. Start with ECLOSE(q_0). For each input symbol a, compute the set of all states reachable by: taking epsilon-transitions, then reading a, then taking epsilon-transitions again. The NFA accepts if the final set of states intersects F.

**Example:** An NFA that accepts strings ending in "01" over {0, 1}. The NFA has three states: q_0 (start, loops on 0 and 1), q_1 (seen a 0 that might be the start of "01"), q_2 (accept, seen "01"). From q_0, reading 0 goes to both q_0 and q_1 (nondeterminism). From q_1, reading 1 goes to q_2. This NFA is much simpler than the equivalent DFA, which would need to track whether the last character was 0.

---

## Part 3: NFA-to-DFA Conversion (Subset Construction)

### The Subset Construction Algorithm

Every NFA can be converted to an equivalent DFA using the subset construction (also called the powerset construction). This is one of the most important results in automata theory: nondeterminism does not add power to finite automata.

Given NFA N = (Q_N, Sigma, delta_N, q_0, F_N), construct DFA D = (Q_D, Sigma, delta_D, q_D0, F_D):

1. **States of D:** Each state of D is a *subset* of Q_N. So Q_D is a subset of P(Q_N). In the worst case, |Q_D| = 2^|Q_N|, though in practice many of these states are unreachable.

2. **Start state:** q_D0 = ECLOSE(q_0)

3. **Transition function:** For a DFA state S (which is a set of NFA states) and input symbol a:
   delta_D(S, a) = ECLOSE( union of delta_N(q, a) for all q in S )

4. **Accept states:** F_D = { S in Q_D : S intersects F_N }

### Worst-Case Exponential Blowup

The subset construction can produce exponentially many states. There exist NFAs with n states for which the minimal equivalent DFA requires 2^n states. A classic example is the NFA that accepts strings over {0, 1} whose n-th-to-last symbol is 1. This NFA needs only n+1 states, but any equivalent DFA requires at least 2^n states because it must remember the last n symbols.

This exponential blowup is relevant in practice: when you compile a regular expression for text search, the engine must decide between simulating the NFA directly (slower per step but compact) or converting to a DFA (faster per step but potentially huge). Real regex engines use hybrid strategies.

### Connection to AI Systems

In modern NLP pipelines, tokenizers often use finite-state methods. The SentencePiece and related tokenizers can be viewed as applying finite transducers to input text. Understanding the NFA-to-DFA tradeoff helps explain why certain tokenization schemes are chosen and what their computational costs are.

---

## Part 4: Regular Expressions

### Syntax and Semantics

Regular expressions are a concise algebraic notation for describing regular languages. The basic building blocks are:

- **a** (for any symbol a in Sigma): matches the single-character string "a"
- **epsilon**: matches the empty string
- **emptyset**: matches nothing (the empty language)

These are combined using three operations:

- **Union (R1 | R2):** matches any string matched by R1 or R2
- **Concatenation (R1 R2):** matches any string formed by concatenating a string from R1 with a string from R2
- **Kleene star (R*):** matches zero or more repetitions of strings from R

Parentheses control grouping, and by convention, Kleene star has the highest precedence, then concatenation, then union.

### Examples

- **(0|1)***: all binary strings (including the empty string)
- **(0|1)*1**: all binary strings ending in 1
- **0*10*10***: binary strings containing exactly two 1s
- **(a|b)*aba(a|b)***: all strings over {a,b} containing "aba" as a substring

### Kleene's Theorem

Kleene's theorem establishes that regular expressions and finite automata describe exactly the same class of languages. Specifically:

1. **Regex -> NFA:** Every regular expression can be converted to an equivalent NFA (Thompson's construction). The construction is recursive, building NFAs for subexpressions and combining them with epsilon-transitions for union, concatenation, and star.

2. **DFA -> Regex:** Every DFA can be converted to an equivalent regular expression (state elimination method). You systematically remove states from the automaton, replacing them with regular expression labels on the remaining edges.

This equivalence is fundamental: it means we have multiple equivalent ways to describe regular languages, each useful in different contexts. Regular expressions are convenient for humans to write; DFAs are convenient for machines to execute.

---

## Part 5: The Pumping Lemma for Regular Languages

### Statement

The pumping lemma is a tool for proving that certain languages are *not* regular. It states:

If L is a regular language, then there exists a pumping length p >= 1 such that every string s in L with |s| >= p can be split into three parts s = xyz satisfying:

1. |y| > 0 (the "pumped" portion is non-empty)
2. |xy| <= p (the pump occurs within the first p characters)
3. For all i >= 0, xy^i z is in L (repeating y any number of times keeps the string in L)

### How to Use It

The pumping lemma is used in proof by contradiction. To show L is not regular:

1. Assume L is regular.
2. Then the pumping lemma gives us some pumping length p.
3. Choose a specific string s in L with |s| >= p (the art is choosing s cleverly).
4. Show that for *every* possible split s = xyz satisfying conditions 1 and 2, there exists some i such that xy^i z is not in L.
5. This contradicts the pumping lemma, so L is not regular.

### Classic Example

**L = {0^n 1^n : n >= 0}** is not regular.

Proof: Assume L is regular with pumping length p. Choose s = 0^p 1^p (which is in L and has length 2p >= p). For any split s = xyz with |xy| <= p and |y| > 0, the portion y consists entirely of 0s (since xy fits within the first p characters, which are all 0s). Say y = 0^k where k >= 1. Then xy^0 z = 0^{p-k} 1^p. Since k >= 1, this string has fewer 0s than 1s, so it is not in L. Contradiction.

This result is deeply significant: it tells us that finite automata cannot count. Any language requiring matching or balancing requires more computational power.

---

## Part 6: Closure Properties of Regular Languages

### Operations That Preserve Regularity

Regular languages are closed under many operations, meaning that combining regular languages with these operations always yields another regular language:

- **Union:** If L1 and L2 are regular, so is L1 union L2. (Proof: product construction or NFA with epsilon-transitions to both machines.)
- **Intersection:** If L1 and L2 are regular, so is L1 intersect L2. (Proof: product construction where both component states must accept.)
- **Complement:** If L is regular, so is the complement of L. (Proof: swap accept and non-accept states in the DFA.)
- **Concatenation:** If L1 and L2 are regular, so is L1 L2. (Proof: NFA construction with epsilon-transitions from accept states of L1's NFA to start state of L2's NFA.)
- **Kleene star:** If L is regular, so is L*. (Proof: NFA with epsilon-transitions from accept states back to start state.)
- **Reversal:** If L is regular, so is L^R. (Proof: reverse all edges in the NFA, swap start and accept.)
- **Homomorphism and inverse homomorphism.**

### Why Closure Properties Matter

Closure properties are powerful proof tools. They let you prove a language is regular by constructing it from known regular languages using closed operations. They also let you prove non-regularity: if you can show that applying a closed operation to L and a known regular language would produce a known non-regular language, then L itself must not be regular.

### Connection to AI: Pattern Matching and Tokenization

Finite-state methods pervade practical AI systems:

- **Tokenization:** Before text reaches a neural network, it must be tokenized. Many tokenizers (including those used in earlier NLP systems and preprocessing for modern LLMs) use finite-state transducers -- a generalization of finite automata that produce output.

- **Named Entity Recognition:** Gazetteers and pattern-based NER systems use regular expressions and finite automata to identify entities like dates, phone numbers, and email addresses.

- **Finite-State Transducers in Speech:** Weighted finite-state transducers (WFSTs) were the backbone of speech recognition systems before end-to-end neural approaches, and they remain important in hybrid systems.

- **Alignment Relevance:** When we think about monitoring AI systems, one approach is to scan their outputs for dangerous patterns. If the patterns we care about are regular (describable by regex), then monitoring is efficient. But many safety-relevant properties are *not* regular -- they require understanding context, counting, or matching -- which foreshadows the need for more powerful computational models.

---

## Watch -- Primary

1. **Neso Academy -- "Theory of Computation" (DFA and NFA sections)**
   - *Comprehensive lecture series covering DFA formal definitions, state diagrams, NFA construction, and the subset construction algorithm. Work through the first 15-20 videos covering finite automata.*

2. **Computerphile -- "Regular Expressions"**
   - *Accessible introduction connecting regular expressions to automata theory, with practical examples.*

---

## Read -- Primary

- **"Introduction to the Theory of Computation" by Michael Sipser** -- Chapter 1 (Regular Languages)
  - Sections 1.1 (Finite Automata), 1.2 (Nondeterminism), 1.3 (Regular Expressions), and 1.4 (Nonregular Languages). Sipser's exposition is exceptionally clear and includes numerous examples and exercises at varying difficulty levels.

---

## Exercises

1. **DFA Design:** Construct a DFA over Sigma = {a, b} that accepts exactly those strings where every 'a' is immediately followed by a 'b'. Provide the state diagram and transition table. Test your DFA on the strings: epsilon, "ab", "b", "aab", "abab", "ba", "abb".

2. **NFA Design:** Construct an NFA over {0, 1} that accepts all strings containing either "101" or "010" as a substring. Your NFA should have at most 6 states. Then convert it to a DFA using the subset construction.

3. **Subset Construction Practice:** Given the NFA with states {q0, q1, q2}, alphabet {a, b}, start state q0, accept state q2, and transitions: delta(q0, a) = {q0, q1}, delta(q0, b) = {q0}, delta(q1, b) = {q2}, delta(q2, a) = {q2}, delta(q2, b) = {q2}. Perform the full subset construction. How many reachable DFA states are there?

4. **Regular Expression to NFA:** Convert the regular expression (ab|ba)* to an NFA using Thompson's construction. Trace the NFA's execution on the input "abba".

5. **Pumping Lemma Proofs:** Prove that each of the following languages is not regular:
   - L1 = {a^n b^n c^n : n >= 0}
   - L2 = {ww : w in {0,1}*} (the set of all strings that are some string repeated twice)
   - L3 = {0^(n^2) : n >= 0} (strings of 0s whose length is a perfect square)

6. **Closure Properties:** Let L be the language of all binary strings with an equal number of 01 and 10 substrings (overlapping occurrences counted). Is L regular? Prove your answer. (Hint: think about what determines the count of 01 and 10 substrings.)

7. **Minimal DFA:** The Myhill-Nerode theorem states that the number of states in the minimal DFA for a language L equals the number of equivalence classes of the indistinguishability relation. Two strings x and y are indistinguishable with respect to L if for every string z, xz is in L if and only if yz is in L. Use this to find the minimal DFA for the language of binary strings where the number of 1s is divisible by 3.

8. **Implementation:** Write a program (in Python or your preferred language) that takes a regular expression (supporting |, *, concatenation, and parentheses), converts it to an NFA using Thompson's construction, and then simulates the NFA on input strings. Test it on several examples.

9. **AI Connection:** Research how the SentencePiece tokenizer works. Identify which parts of its operation can be modeled as finite-state transduction and which parts require more powerful computation. Write a one-page analysis.

10. **Reflection:** The pumping lemma tells us that finite automata cannot count. In what sense does this limitation mirror the limitations of simple pattern-matching approaches to AI safety? Give a concrete example of a safety property that cannot be checked by a finite automaton monitoring an AI system's output stream.
