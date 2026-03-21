# Lesson 79: Godel's Incompleteness Theorems

[<- Proof Systems](lesson-78-proof-systems.md) | [Back to TOC](../README.md) | [Next: Groups ->](lesson-80-groups.md)

---

> **Why this lesson exists:** Godel's incompleteness theorems are among the most profound results in all of mathematics, and they bear directly on the foundations of AI alignment. They tell us that any sufficiently powerful formal system has inherent blind spots -- true statements it cannot prove, and an inability to certify its own consistency. For AI alignment, this means that a sufficiently powerful AI system cannot, within its own formal framework, fully verify its own alignment. Lob's theorem sharpens this further and connects directly to decision theory and logical uncertainty, which are active research topics in alignment. If you want to understand the fundamental limits of formal verification for AI systems -- what can and cannot be guaranteed by proof -- this lesson is essential.

> **Estimated time:** 12--18 hours

---

## Part 1: The Setup -- Formal Arithmetic

### Why Arithmetic?

Godel's theorems apply to formal systems that are "strong enough to encode basic arithmetic." This means the system can express statements about natural numbers: addition, multiplication, and their properties.

The standard system is **Peano Arithmetic (PA)**, which has:

- A constant 0
- A successor function S (so S(0) = 1, S(S(0)) = 2, etc.)
- Addition and multiplication, defined by recursive axioms
- Induction: for any property P, if P(0) holds and P(n) implies P(S(n)) for all n, then P(n) holds for all n

PA is strong enough to formalize essentially all of number theory and, by encoding, much of computer science. This is the system Godel targets.

### Consistency and Expressiveness

A system is **consistent** if it does not prove both a statement and its negation. If a system proves P and ~P, it is inconsistent, and by the principle of explosion (ex falso quodlibet), it proves everything -- which makes it useless.

The key tension Godel reveals is between consistency and completeness. We want both:

- **Consistency:** The system never proves a falsehood.
- **Completeness:** The system proves every truth (about arithmetic).

Godel shows we cannot have both (for sufficiently strong systems). Something must give.

---

## Part 2: Godel Numbering

### Encoding Formulas as Numbers

Godel's key insight was that a formal system can talk about itself. The trick is to encode every symbol, formula, and proof as a natural number -- a **Godel number**.

Here is the basic idea:

1. Assign a unique number to each symbol in the language: 0 gets code 1, S gets code 2, + gets code 3, etc.
2. Encode a sequence of symbols (a formula) as a single number using a pairing or sequence-coding function. A common approach uses prime factorization: the formula with symbols having codes c1, c2, ..., cn is encoded as 2^c1 * 3^c2 * 5^c3 * ... * p_n^cn, where p_n is the nth prime.
3. Encode a sequence of formulas (a proof) as a number using the same technique, one level up.

Because of unique prime factorization, every number decodes to at most one formula, and every formula encodes to exactly one number.

### Why This Matters

With Godel numbering, statements ABOUT formulas and proofs become statements ABOUT numbers. The statement "formula F is provable" becomes "there exists a number n that encodes a valid proof of the formula with Godel number g(F)."

Crucially, the property "n encodes a valid proof of g(F)" is a property of natural numbers that can be expressed within PA itself. The system can talk about its own proofs.

### The Provability Predicate

Define Prov(x) to be the formula (in the language of PA) that says "there exists a proof of the formula with Godel number x." More precisely:

Prov(x) means: there exists y such that y encodes a valid proof of x.

This predicate is expressible in PA because "y encodes a valid proof of x" can be broken down into checkable arithmetic conditions (each line of the proof is an axiom or follows from previous lines by an inference rule, and these are all arithmetically definable).

---

## Part 3: The Fixed-Point Lemma

### Self-Reference

The fixed-point lemma (also called the diagonal lemma) is the technical heart of Godel's proof. It shows that self-reference is unavoidable in sufficiently strong systems.

**Fixed-Point Lemma:** For any formula F(x) with one free variable, there exists a sentence G such that the system proves:

G <-> F(g(G))

where g(G) is the Godel number of G.

In words: G says "F holds of my own Godel number." The sentence G refers to itself -- not directly, but through its numerical encoding.

### Intuition: The Liar Paradox Made Precise

The liar paradox says: "This sentence is false." It is a sentence that refers to itself and asserts its own falsehood. It is paradoxical because if it is true, it is false, and if it is false, it is true.

Godel's construction is a careful, non-paradoxical version: instead of "this sentence is false," we get "this sentence is not provable." This is NOT paradoxical -- it is simply true if the system is consistent (as we will see).

### How the Construction Works (Sketch)

1. Consider a formula F(x) -- say, ~Prov(x), which says "x is not provable."
2. There is a formula D(x) that says "take the formula with Godel number x, substitute x for the free variable, and compute the Godel number of the result."
3. Let d be the Godel number of the formula ~Prov(D(x)).
4. Define G to be the formula obtained by substituting d into ~Prov(D(x)), i.e., G is ~Prov(D(d)).
5. By the definition of D, D(d) computes the Godel number of G itself.
6. So G says: ~Prov(g(G)) -- "my own Godel number is not provable" -- "I am not provable."

This is the Godel sentence.

---

## Part 4: The First Incompleteness Theorem

### Statement

**Godel's First Incompleteness Theorem:** For any consistent formal system F that is strong enough to encode basic arithmetic (specifically, that is "sufficiently strong" and has a recursively enumerable set of axioms), there exists a sentence G such that:

1. G is true (in the standard model of arithmetic), but
2. G is not provable in F, and
3. ~G is not provable in F.

Such a sentence is called **undecidable** (or independent) relative to F. The system can neither prove it nor refute it.

### Proof Sketch

Let G be the Godel sentence: G says "I am not provable in F."

**Case 1: Suppose G is provable in F.**
Then there exists a proof of G. But G says "I am not provable." So G is false. But if F is sound (proves only true things), this is a contradiction. Even with the weaker assumption of consistency (plus a technical condition called omega-consistency, or the weaker assumption of 1-consistency), we get a contradiction. So G is not provable.

**Case 2: Since G is not provable, and G says "I am not provable," G is true.**
G correctly asserts its own unprovability.

**Case 3: Suppose ~G is provable in F.**
~G says "I am provable." If ~G is provable, then by soundness, G is provable. But we just showed G is not provable. Contradiction. So ~G is not provable either.

Therefore: G is true but unprovable, and ~G is also unprovable. The system cannot decide G.

### What Does "True but Unprovable" Mean?

"True" here means true in the **standard model** -- the natural numbers 0, 1, 2, 3, ... with the usual addition and multiplication. The Godel sentence is true because it says "there is no proof of me," and indeed there is none.

But PA cannot prove this, because PA cannot "see" that the standard model is the right one. There are nonstandard models of PA -- models with extra elements beyond the standard natural numbers -- in which G is false (because a "proof" exists, encoded by a nonstandard number that does not correspond to any real proof).

### The Rosser Improvement

Rosser (1936) strengthened Godel's theorem by weakening the assumption from omega-consistency to plain consistency. Rosser's sentence says: "If I am provable, then there is a shorter proof of my negation." This more careful construction eliminates the need for the stronger consistency assumption.

---

## Part 5: The Second Incompleteness Theorem

### Statement

**Godel's Second Incompleteness Theorem:** For any consistent formal system F that is strong enough to encode basic arithmetic, F cannot prove its own consistency.

More precisely: let Con(F) be the sentence ~Prov(g(0 = 1)), which says "F does not prove 0 = 1" (a natural formalization of "F is consistent"). Then:

If F is consistent, then F does not prove Con(F).

### Proof Idea

The proof builds on the first theorem. The key insight is:

1. Within F, one can formalize the argument: "If F is consistent, then the Godel sentence G is not provable" -- i.e., F proves Con(F) -> ~Prov(g(G)).
2. But ~Prov(g(G)) is essentially what G says (G says "I am not provable").
3. So F proves Con(F) -> G.
4. If F also proved Con(F), then by modus ponens, F would prove G.
5. But the first theorem says F does not prove G.
6. Therefore, F does not prove Con(F).

### Implications

This result has a devastating elegance:

- **You cannot use mathematics to prove mathematics is consistent** (from within the same system). PA cannot prove PA is consistent. ZFC (the standard foundation for all of mathematics) cannot prove ZFC is consistent.
- **You can prove consistency in a stronger system.** Gentzen proved PA is consistent using transfinite induction up to epsilon-0, but this requires methods beyond PA. The consistency of ZFC would require even stronger methods.
- **For AI systems:** An AI system reasoning within a formal framework cannot, within that framework, prove that its own reasoning is consistent. This is not merely a technical limitation -- it is a fundamental barrier to self-verification.

---

## Part 6: Lob's Theorem

### Statement

**Lob's Theorem (1955):** For any sentence P, if the system proves "if I can prove P, then P" (formally: if F proves Prov(g(P)) -> P), then F already proves P.

In contrapositive: if F does not prove P, then F does not prove Prov(g(P)) -> P.

### Why This Is Surprising

The sentence "if I can prove P, then P" seems obviously true -- of course provable things are true! This is just soundness. But Lob's theorem says the system can prove this sentence (for a specific P) only if it already proves P.

Think about it: the system cannot prove "if I prove 0 = 1, then 0 = 1" without actually proving 0 = 1 (which it cannot, if consistent). The conditional "if I prove 0 = 1, then 0 = 1" seems harmless -- its consequent is trivially false and its antecedent (we hope) is also false. But the system cannot prove it, because proving it would (by the internal logic of provability) collapse into actually proving 0 = 1.

### Connection to the Second Incompleteness Theorem

Set P = falsum (a contradiction). Then Prov(g(falsum)) -> falsum is equivalent to ~Prov(g(falsum)), which is Con(F). Lob's theorem says: F proves Con(F) only if F proves falsum -- i.e., only if F is inconsistent. This directly yields the second incompleteness theorem as a special case.

### The Hilbert-Bernays-Lob Derivability Conditions

Lob's theorem relies on three properties of the provability predicate Prov:

1. **D1:** If F proves A, then F proves Prov(g(A)).
2. **D2:** F proves Prov(g(A -> B)) -> (Prov(g(A)) -> Prov(g(B))).
3. **D3:** F proves Prov(g(A)) -> Prov(g(Prov(g(A)))).

Any predicate satisfying D1-D3 gives rise to Lob's theorem. This abstract formulation connects to **provability logic** (GL), a modal logic where the box operator satisfies exactly these conditions.

---

## Part 7: Tarski's Undefinability Theorem

### Statement

**Tarski's Undefinability Theorem (1936):** No sufficiently strong formal system can define its own truth predicate.

More precisely: there is no formula True(x) in the language of PA such that for every sentence S, PA proves True(g(S)) <-> S.

### Proof

By contradiction. If True(x) existed, apply the fixed-point lemma with ~True(x) to get a sentence L such that PA proves L <-> ~True(g(L)). This is the liar paradox formalized. If L is true, then True(g(L)) holds, so ~True(g(L)) is false, so L is false. Contradiction. Similarly in the other direction. So True(x) cannot exist.

### Comparison with Godel's Theorem

| | Godel | Tarski |
|---|---|---|
| What fails? | Completeness of provability | Definability of truth |
| The sentence says: | "I am not provable" | "I am not true" |
| Paradox status: | Not paradoxical (it is true) | Genuinely paradoxical (so the predicate cannot exist) |

Godel's sentence is merely unprovable; the system remains consistent. Tarski's hypothetical sentence would be outright contradictory, which is why the truth predicate cannot exist in the first place.

### Implications for AI

An AI system cannot have a fully general internal representation of "what is true in my own reasoning system." Truth about the system must be assessed from outside. This connects to the AI alignment problem of **transparency**: we want to understand what an AI system "believes," but the system cannot provide a complete, self-consistent account of its own beliefs (if its reasoning is sufficiently powerful).

---

## Part 8: Implications for AI Alignment

### Limits of Self-Verification

The second incompleteness theorem says: a consistent formal system cannot prove its own consistency. Applied to AI:

An AI system that reasons within a formal framework F cannot prove, within F, that F is consistent. If the system's safety depends on the consistency of F, the system cannot self-certify its own safety.

This does not mean verification is impossible -- it means SELF-verification within a single framework is impossible. Verification by an external, stronger system is still possible (just as Gentzen proved PA consistent using methods outside PA).

### Lob's Theorem and Decision Theory

Lob's theorem has direct implications for AI decision theory, particularly for problems involving self-reference:

**The Loebian obstacle:** Consider two AI agents that want to cooperate but need to verify that the other will cooperate. Agent A reasons: "If I can prove Agent B will cooperate, I will cooperate." Agent B reasons symmetrically. By Lob's theorem, if both agents' reasoning is formalized in a system satisfying the derivability conditions, they CAN achieve cooperation -- Lob's theorem guarantees that the self-referential reasoning "bottoms out." This is the basis of the "Loebian cooperation" result in the AI alignment literature (Barasz et al., 2014).

But Lob's theorem also creates obstacles. An agent trying to reason about its own trustworthiness faces Loebian difficulties: it cannot prove "I am trustworthy" without already being in a position where the proof is trivially available.

### Logical Uncertainty

Standard probability theory handles uncertainty about empirical facts. But AI systems also face uncertainty about logical and mathematical facts (e.g., "will this program halt?"). This is **logical uncertainty**.

Godel's theorems show that logical uncertainty is not just practical (we have not found the proof yet) but fundamental (some truths have no proof in the system). Logical induction (Garrabrant et al., 2016) is a framework for handling logical uncertainty that takes Godel's theorems seriously, assigning probabilities to logical sentences that converge to correct values as the system processes more and more deductions.

### The Self-Reference Problem in Alignment

The alignment problem is partly a self-reference problem: we want an AI system to reason about its own goals, its own modifications, and its own reasoning processes. Godel's theorems show that self-referential reasoning is inherently limited:

1. **An AI cannot fully verify its own alignment** within its own formal framework (second incompleteness theorem).
2. **An AI cannot define its own truth predicate** (Tarski), so it cannot have a fully general model of "what I believe is true."
3. **An AI's reasoning about its own provability has a peculiar structure** (Lob), creating both obstacles and opportunities for cooperation.

These are not merely theoretical curiosities. They constrain the design space for aligned AI. Any alignment proposal that relies on an AI system fully verifying its own safety from within a single formal framework must contend with these impossibility results.

### What We CAN Do

The incompleteness theorems do not say that verification is hopeless. They say:

- Use external verification (a human, a separate system, a stronger formal framework) rather than relying solely on self-verification.
- Accept that some safety properties will be verified with high confidence rather than absolute certainty.
- Design AI systems with modular reasoning, where different components verify each other rather than a single monolithic self-check.
- Use probabilistic and Bayesian approaches to complement formal proof, particularly for properties that are undecidable in the system.

---

## Watch -- Primary

- **Trefor Bazzett -- Logic playlist** (YouTube): Videos on formal systems and metatheory.
- **Veritasium -- "Math's Fundamental Flaw"** (YouTube): An excellent accessible introduction to Godel's incompleteness theorems with clear visualizations.
- **Numberphile -- Godel's Incompleteness Theorem** (YouTube): A concise walkthrough of the key ideas.

## Read -- Primary

- Nagel and Newman, "Godel's Proof" -- a classic, accessible book-length treatment of the first incompleteness theorem. Highly recommended as a primary text for this lesson.
- Hofstadter, "Godel, Escher, Bach" -- a deeper, more expansive exploration of self-reference, formal systems, and their implications for minds and machines. Read selectively; Chapters 1-9 and 13-14 are most relevant.
- Smith, "An Introduction to Godel's Theorems" -- a more rigorous mathematical treatment, suitable if you want to see the full proofs.

---

## Exercises

1. **Godel numbering:** Using the prime-power encoding scheme (2^c1 * 3^c2 * 5^c3 * ...), compute the Godel number of the formula "0 = 0" assuming the encoding: 0 -> 1, = -> 2. Verify that your number uniquely decodes back to the original formula.

2. **Self-reference intuition:** Explain, in your own words and without using any formal notation, why the sentence "I am not provable" is not paradoxical (unlike "I am not true"). What is the key difference? What happens in each case if the sentence is true? What happens if it is false?

3. **First incompleteness theorem consequences:** Consider a hypothetical AI system that uses Peano Arithmetic as its reasoning framework. Give a concrete example of a statement about natural numbers that the system cannot prove or disprove. Explain why this limitation exists and whether it matters practically for the AI's operation.

4. **Second incompleteness theorem application:** An AI safety proposal says: "The AI will run a self-check that proves its formal reasoning system is consistent before taking any action." Explain, using the second incompleteness theorem, why this proposal is fundamentally flawed. What would you suggest instead?

5. **Lob's theorem exercise:** Explain why a formal system F (satisfying the derivability conditions) cannot prove the sentence "If F proves that 0 = 1, then 0 = 1" (assuming F is consistent). This sentence seems trivially true -- its consequent is just a false statement, and we hope the antecedent is also false. Why can the system not prove it?

6. **Tarski vs. Godel:** Compare Tarski's undefinability theorem with Godel's first incompleteness theorem. Both use self-reference via the fixed-point lemma, but they reach different conclusions. Explain: (a) what each theorem shows is impossible, (b) why one produces a true-but-unprovable sentence while the other produces an outright contradiction, and (c) what each implies about AI systems.

7. **Loebian cooperation:** Two AI agents, A and B, each reason in PA. Agent A's source code says: "Search for a proof that B cooperates. If found, cooperate. Otherwise, defect." Agent B's source code is symmetric. Using Lob's theorem, explain why both agents will cooperate. (Hint: Agent A proves "if I can prove B cooperates, then B cooperates" -- why? -- and then Lob's theorem applies.)

8. **Reflection on limits:** Write a one-paragraph response to the following challenge: "Godel's theorems only apply to formal systems. Real AI systems are not formal systems -- they are neural networks. So the theorems are irrelevant to AI alignment." Do you agree or disagree? What assumptions does this challenge make, and are they valid?
