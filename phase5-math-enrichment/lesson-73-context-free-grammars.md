# Lesson 73: Context-Free Grammars and Pushdown Automata

[<- Finite Automata](lesson-72-finite-automata.md) | [Back to TOC](../README.md) | [Next: Turing Machines ->](lesson-74-turing-machines.md)

---

> **Why this lesson exists:** Context-free grammars occupy the next rung on the Chomsky hierarchy, capturing the ability to handle nested and recursive structure -- precisely the kind of structure that appears in programming languages, natural language syntax, and, increasingly, in how we think about transformer attention patterns. For AI alignment, understanding CFGs helps clarify what kinds of structural properties of AI-generated code or text can be verified by relatively efficient algorithms, and where we start to hit the boundaries of tractable analysis.

> **Estimated time:** 12--18 hours

---

## Part 1: Context-Free Grammars

### Formal Definition

A context-free grammar (CFG) is a 4-tuple G = (V, Sigma, R, S) where:

- **V** is a finite set of variables (also called nonterminals)
- **Sigma** is a finite set of terminals, disjoint from V (the alphabet of the language)
- **R** is a finite set of production rules, each of the form A -> w, where A is a variable and w is a string over (V union Sigma)*
- **S in V** is the start variable

The term "context-free" comes from the fact that a variable A can be replaced by its right-hand side regardless of what surrounds A -- the replacement does not depend on A's context. This contrasts with context-sensitive grammars where the replacement rule for A can depend on neighboring symbols.

### Derivations

A derivation is a sequence of rule applications that transforms the start variable into a string of terminals. Starting from S, at each step we choose a variable in the current string and replace it according to some production rule.

There are two standard derivation orders:

- **Leftmost derivation:** Always expand the leftmost variable first.
- **Rightmost derivation:** Always expand the rightmost variable first.

For example, consider the grammar with rules S -> aSb | epsilon. This generates the language {a^n b^n : n >= 0}, which we proved is not regular using the pumping lemma. A derivation of "aabb":

S => aSb => aaSbb => aaepsilonbb => aabb

Each step replaces S using one of the two rules. This demonstrates the core power of CFGs over regular languages: the recursive nesting of S between a and b naturally ensures that the counts match.

### Parse Trees

A parse tree (or derivation tree) provides a graphical representation of a derivation that abstracts away the order in which rules were applied:

- The root is labeled with the start variable S
- Each internal node is labeled with a variable
- The children of an internal node labeled A correspond to the right-hand side of a production A -> w
- Leaves are labeled with terminals or epsilon
- Reading the leaves left-to-right yields the derived string

Parse trees are the central data structure for understanding the structure of a string with respect to a grammar. In programming languages, the parse tree of a program determines its meaning. In natural language processing, the parse tree of a sentence reveals its syntactic structure.

### Ambiguity

A grammar is **ambiguous** if there exists a string that has two or more distinct parse trees (equivalently, two or more distinct leftmost derivations).

**Classic example of ambiguity:** The expression grammar:

E -> E + E | E * E | (E) | id

The string "id + id * id" has two parse trees: one where + is at the root (treating * as binding tighter) and one where * is at the root (treating + as binding tighter). These correspond to different mathematical interpretations, which is why ambiguity in programming language grammars must be resolved.

Ambiguity is resolved in practice by:

- **Rewriting the grammar** to enforce precedence and associativity (e.g., introducing separate nonterminals for terms and factors)
- **Disambiguation rules** in the parser (e.g., specifying that * has higher precedence than +)

A language is **inherently ambiguous** if every grammar generating it is ambiguous. The language {a^i b^j c^k : i = j or j = k} is a classic example of an inherently ambiguous context-free language.

### Designing CFGs

Designing a CFG for a given language requires creativity. Here are some strategies:

1. **Recursive structure:** Identify the recursive pattern. For matched parentheses: S -> (S) | SS | epsilon.

2. **Union:** If L = L1 union L2, and you have grammars G1 (start S1) and G2 (start S2), create S -> S1 | S2.

3. **Concatenation:** If L = L1 L2, create S -> S1 S2.

4. **Relating to a regular language:** Every regular language is context-free, and you can convert a DFA to a grammar mechanically: create a variable for each state, and for each transition delta(q_i, a) = q_j, add the rule Q_i -> a Q_j. For accept states q_f, add Q_f -> epsilon.

**Example:** CFG for {w in {0,1}* : w has equal numbers of 0s and 1s}:

S -> 0S1S | 1S0S | epsilon

The intuition: read the string left to right. If the first symbol is 0, eventually a 1 must balance it, and the portions before and after that 1 must themselves be balanced.

---

## Part 2: Chomsky Normal Form

### Definition

A CFG is in Chomsky Normal Form (CNF) if every production rule has one of these forms:

- A -> BC (two variables on the right)
- A -> a (a single terminal on the right)
- S -> epsilon (only allowed for the start variable, and only if epsilon is in the language)

### Why CNF Matters

CNF is important for several reasons:

1. **Parsing algorithm:** The CYK (Cocke-Younger-Kasami) algorithm requires CNF and runs in O(n^3 |G|) time, where n is the length of the input string. This is the standard proof that membership in any context-free language is decidable in polynomial time.

2. **Proof technique:** Many proofs about CFGs are simpler when the grammar is in CNF because the structure of derivations is more constrained.

3. **Binary tree structure:** In CNF, every parse tree is a binary tree. A string of length n has a parse tree with exactly n leaves and n-1 internal nodes (plus the root), giving us tight control over derivation lengths.

### Conversion to CNF

Any CFG can be converted to CNF through a sequence of transformations:

1. **Add a new start variable** S_0 -> S to ensure the start variable does not appear on the right side of any rule.

2. **Eliminate epsilon-productions:** If A -> epsilon, find all rules with A on the right side and add versions with A removed. Remove the original epsilon-production (unless A = S_0).

3. **Eliminate unit productions:** If A -> B (a single variable), replace with A -> (everything B can produce, transitively).

4. **Convert remaining rules:** For A -> u_1 u_2 ... u_k where k >= 3, introduce new variables to create a chain of binary productions. Replace terminals in multi-symbol rules with fresh variables (e.g., if the rule has terminal 'a' mixed with variables, introduce U_a -> a and substitute).

Each step preserves the generated language, so the final CNF grammar is equivalent to the original.

---

## Part 3: Pushdown Automata

### Intuition: Finite Automata with a Stack

A pushdown automaton (PDA) is a finite automaton augmented with a stack -- an unbounded memory that can only be accessed in a last-in-first-out manner. The stack gives PDAs the ability to count and match that finite automata lack.

Think of a PDA as having three components that it examines at each step: the current state, the current input symbol (or epsilon for a free move), and the top of the stack. Based on these three things, it transitions to a new state, pops the top of the stack, and pushes a new string onto the stack.

### Formal Definition

A pushdown automaton is a 6-tuple P = (Q, Sigma, Gamma, delta, q_0, F) where:

- **Q** is a finite set of states
- **Sigma** is the input alphabet
- **Gamma** is the stack alphabet
- **delta: Q x (Sigma union {epsilon}) x (Gamma union {epsilon}) -> P(Q x (Gamma union {epsilon}))** is the transition function
- **q_0** is the start state
- **F** is the set of accept states

The transition function says: in state q, reading input a (or epsilon), with stack top b (or epsilon), the machine can move to state q', pop b from the stack, and push c onto the stack. The notation delta(q, a, b) contains (q', c) encodes this.

Note that PDAs are nondeterministic by default. Unlike finite automata, nondeterministic PDAs are strictly more powerful than deterministic PDAs -- a fundamental asymmetry in computation theory.

### Example: Recognizing {a^n b^n}

The PDA for {a^n b^n : n >= 0} works as follows:

1. Start in state q_1. Push a special bottom-of-stack marker $.
2. In state q_1, reading 'a': push 'a' onto the stack. Stay in q_1.
3. In state q_1, reading 'b': pop 'a' from the stack. Move to state q_2.
4. In state q_2, reading 'b': pop 'a' from the stack. Stay in q_2.
5. In state q_2, reading epsilon with $ on stack: move to accept state q_3.

The stack keeps count of the a's we have seen. Each b pops one a. If the counts match, the stack returns to $ and we accept. If they do not match (too many b's or a's), the machine gets stuck and rejects.

### Example: Recognizing Palindromes

The language L = {ww^R : w in {0,1}*} (even-length palindromes) is context-free. The PDA uses nondeterminism: it guesses where the middle of the string is. In the first half, it pushes symbols onto the stack. At its guessed midpoint, it switches to popping and matching. If the guess is correct and the string is a palindrome, one computation path accepts.

This example illustrates why nondeterminism matters for PDAs: without it, the machine cannot determine the midpoint of the palindrome (there is no marker telling it where the middle is).

### Equivalence of PDAs and CFGs

One of the central theorems of formal language theory states:

**A language is context-free if and only if some pushdown automaton recognizes it.**

The proof has two directions:

1. **CFG -> PDA:** Given a grammar G, build a PDA that simulates leftmost derivations. The PDA guesses which production to apply (nondeterminism) and uses the stack to keep track of what the grammar is "expecting" to see in the remaining input.

2. **PDA -> CFG:** Given a PDA P, build a grammar whose variables encode "the computation of P that starts in state q with stack symbol s and ends in state r with that symbol popped." The construction is more involved but establishes the full equivalence.

---

## Part 4: The Pumping Lemma for Context-Free Languages

### Statement

If L is a context-free language, there exists a pumping length p such that every string s in L with |s| >= p can be split into five parts s = uvxyz satisfying:

1. |vy| > 0 (at least one of v and y is non-empty)
2. |vxy| <= p
3. For all i >= 0, uv^i xy^i z is in L

### Key Difference from the Regular Pumping Lemma

The CFL pumping lemma pumps two substrings (v and y) simultaneously. This reflects the tree structure of context-free derivations: in a sufficiently long derivation, some variable must repeat along a path from root to leaf, and the portions generated by the two occurrences of that variable give the v and y portions.

### Classic Application

**L = {a^n b^n c^n : n >= 0} is not context-free.**

Proof: Assume L is context-free with pumping length p. Choose s = a^p b^p c^p. For any split s = uvxyz with |vxy| <= p and |vy| > 0:

Since |vxy| <= p, the substring vxy can span at most two of the three symbol blocks (a's, b's, c's). Therefore pumping v and y can only increase the count of at most two of the three symbols. Pumping up (i = 2) gives a string where the three counts are no longer equal. This is not in L, contradiction.

This result places {a^n b^n c^n} strictly above context-free languages in the Chomsky hierarchy.

---

## Part 5: The Chomsky Hierarchy

### The Four Levels

The Chomsky hierarchy classifies formal languages into four nested classes based on the type of grammar that generates them:

| Type | Grammar Class        | Automaton            | Example Language       |
|------|---------------------|----------------------|------------------------|
| 3    | Regular             | Finite automaton     | a*b*                   |
| 2    | Context-free        | Pushdown automaton   | {a^n b^n}              |
| 1    | Context-sensitive   | Linear bounded automaton | {a^n b^n c^n}      |
| 0    | Recursively enumerable | Turing machine    | {<M,w> : M accepts w} |

Each level strictly contains the one below it:

Regular languages (subset of) Context-free languages (subset of) Context-sensitive languages (subset of) Recursively enumerable languages

### Significance for Computer Science and AI

The Chomsky hierarchy provides a roadmap for understanding the computational power needed to process different kinds of structure:

- **Type 3 (Regular):** Flat patterns, no nesting. Sufficient for tokenization, simple pattern matching.
- **Type 2 (Context-free):** Nested structure, recursion. Sufficient for programming language syntax, basic sentence structure.
- **Type 1 (Context-sensitive):** Cross-serial dependencies, agreement. Relevant for natural language phenomena like Swiss German cross-serial dependencies.
- **Type 0 (Recursively enumerable):** Full computational power. Any computable language.

### Connection to AI: Transformers and the Hierarchy

A fascinating question in modern AI theory is: where do transformers sit in the Chomsky hierarchy?

- Finite-depth, finite-precision transformers can be shown to recognize only languages in a class related to (but not identical to) regular languages -- specifically, those recognizable by constant-depth threshold circuits (TC^0).

- However, transformers with unbounded precision or with chain-of-thought (autoregressive generation allowing intermediate computation) can simulate more powerful computation.

- This connects to alignment: if a transformer's "native" computational class is limited, then certain safety properties might be efficiently verifiable. But chain-of-thought and tool use expand the effective computational class, making verification harder.

---

## Part 6: Parsing Algorithms

### Top-Down Parsing

Top-down parsers start from the start symbol and try to derive the input string by expanding nonterminals. Recursive descent parsers implement this directly: each nonterminal becomes a function, and the parser tries production rules in order.

LL(k) parsers look ahead k tokens to decide which production to use. LL(1) grammars are particularly important because they can be parsed efficiently with no backtracking, using a parsing table.

### Bottom-Up Parsing

Bottom-up parsers start from the input tokens and work backward to the start symbol by "reducing" sequences of symbols that match the right-hand side of a production. LR parsers (LR(0), SLR, LALR, LR(1)) use a state machine and a stack to do this efficiently.

LALR(1) parsers are the basis of tools like yacc/bison, which generate parsers from grammar specifications. Most practical programming language parsers are LALR(1).

### CYK Algorithm

The Cocke-Younger-Kasami algorithm works on any CFG in Chomsky Normal Form. It uses dynamic programming: for a string of length n, it fills an n x n table where entry (i, j) contains all variables that can derive the substring from position i to position j.

The time complexity is O(n^3 |G|), making it polynomial but too slow for practical use on large inputs. Its importance is theoretical: it proves that CFL membership is decidable in polynomial time.

### Earley Parser

The Earley parser works on any CFG (not just CNF) and runs in O(n^3) time in general, O(n^2) for unambiguous grammars, and O(n) for most LR grammars. It is more practical than CYK and is used in some NLP systems.

---

## Watch -- Primary

1. **Neso Academy -- "Theory of Computation" (CFG and PDA sections)**
   - *Covers context-free grammar definitions, derivations, parse trees, ambiguity, pushdown automata, and the pumping lemma for CFLs. Work through the relevant 10-15 videos.*

2. **Computerphile -- "Chomsky Hierarchy"**
   - *Clear overview of the four levels of the hierarchy with examples and motivation.*

---

## Read -- Primary

- **"Introduction to the Theory of Computation" by Michael Sipser** -- Chapter 2 (Context-Free Languages)
  - Sections 2.1 (Context-Free Grammars), 2.2 (Pushdown Automata), 2.3 (Non-Context-Free Languages). Sipser's treatment is rigorous and builds excellent intuition.

---

## Exercises

1. **CFG Design:** Write a CFG for each of the following languages:
   - {a^i b^j : i >= j >= 0}
   - {w in {0,1}* : w is a palindrome}
   - {a^i b^j c^k : i + k = j}
   - The set of all balanced parentheses strings using both () and []

2. **Ambiguity Analysis:** Consider the grammar S -> aS | Sa | a. Show that this grammar is ambiguous by finding a string with two distinct parse trees. Then design an unambiguous grammar for the same language.

3. **CNF Conversion:** Convert the following grammar to Chomsky Normal Form:
   S -> ASA | aB
   A -> B | S
   B -> b | epsilon

4. **PDA Construction:** Build a PDA (give the state diagram with stack operations) that recognizes {a^i b^j c^k : i = j or j = k}. Explain why nondeterminism is essential for this language.

5. **CFL Pumping Lemma:** Prove that each of the following languages is not context-free:
   - {a^n b^n c^n d^n : n >= 0}
   - {a^(n^2) : n >= 0}
   - {ww : w in {a,b}*}

6. **Chomsky Hierarchy Classification:** For each language, determine the lowest level of the Chomsky hierarchy it belongs to and justify your answer:
   - {0^n : n is prime}
   - {a^n b^n : n >= 0}
   - (a|b)*a(a|b)
   - {<M> : M is a Turing machine that halts on empty input}

7. **CYK Algorithm:** Apply the CYK algorithm to parse the string "aabb" using the CNF grammar you obtained in Exercise 3. Show the complete table.

8. **Programming Language Parsing:** Explain why most programming languages have context-free syntax but context-sensitive (or even undecidable) semantics. Give specific examples of language features that cannot be captured by a CFG (e.g., variable declaration before use, type checking).

9. **Transformers and Formal Languages:** Read the paper "Transformers as Recognizers of Formal Languages" (Bhatt et al., or similar surveys). Summarize the key results about which formal language classes fixed-depth transformers can recognize. What are the implications for what transformers can and cannot learn?

10. **Reflection:** If an AI system generates code, and we want to verify that the code has some structural property (e.g., all opened files are closed, all allocated memory is freed), at what level of the Chomsky hierarchy does this verification problem sit? What does this tell us about the feasibility of automated verification?
