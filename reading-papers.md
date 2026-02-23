# How to Read ML & Alignment Papers

[Back to TOC](../README.md)

---

> **Why this guide exists:** There's a specific skill to reading ML papers that nobody teaches explicitly. You'll go from textbook learning to "read Anthropic's Scaling Monosemanticity paper" with a massive gap in between — unless you learn the technique. This guide bridges that gap. Use it starting in Phase 4.

## The Three-Pass Method

### Pass 1: Scout (5–10 minutes)

The goal is to decide whether to read the paper at all, and to get the gist.

1. Read the **title, abstract, and introduction** (first 2 paragraphs only)
2. Read **all section headings** — this is the skeleton
3. Look at **every figure and table** with their captions. In ML papers, figures often tell the whole story.
4. Read the **conclusion** (first paragraph)
5. Ask yourself: *"What is the one-sentence claim of this paper?"*

After Pass 1, you should be able to say: "This paper shows that [method X] achieves [result Y] by [key insight Z]."

If you can't, the paper might be outside your current level — and that's fine. Come back later.

### Pass 2: Understand (30–60 minutes)

Now read the whole paper, but strategically:

- **Skip proofs and dense math on first read.** Mark them and come back if needed.
- **Pay close attention to:** figures, equations that are *used* (not just derived), experimental setup, and results tables.
- **For each section, write one sentence** summarizing the key point.
- **Circle things you don't understand.** Don't stop to look them up yet — you might find the paper explains them later.
- **Look up 2–3 key references** that the paper builds on. Often understanding the parent paper unlocks the current one.

### Pass 3: Internalize (1–3 hours, only for important papers)

This is for papers you want to truly master (like "A Mathematical Framework for Transformer Circuits" or "Risks from Learned Optimization"):

- **Re-derive key equations** from scratch on paper
- **Reproduce a key figure** with code if possible
- **Explain the paper to an imaginary audience** (or Claude) without looking at it
- **List the assumptions.** What would break if each assumption failed?
- **Write a 3-paragraph summary:** what they did, why it matters, what's missing

## ML Paper Anatomy — What to Expect

| Section | What's there | How to read it |
|---------|-------------|----------------|
| **Abstract** | The whole paper in 150 words | Read carefully — this IS the paper's claim |
| **Introduction** | Motivation, context, contribution list | Read first 2 paragraphs, skim the rest |
| **Related Work** | What came before | Skim unless you need context on a specific predecessor |
| **Method** | The actual contribution | Read carefully. This is the core. |
| **Experiments** | Does it work? | Look at tables and figures first, then read setup |
| **Discussion/Limitations** | Honest assessment | Read — this is where authors admit what doesn't work |
| **Conclusion** | Summary + future work | Read first paragraph |
| **Appendix** | Technical details, extra results | Reference as needed |

## Paper-Specific Strategies

### Interpretability Papers (Anthropic's Circuits Thread)

These papers are unusually visual. Strategy:

1. **Start with the figures.** The interactive visualizations ARE the result.
2. **Follow the "path" through the model.** These papers trace information flow — draw the path yourself.
3. **Connect to linear algebra:** every operation they describe is a matrix multiplication, projection, or decomposition you learned in Phase 1.
4. **Run the code.** Most Anthropic papers have companion notebooks. Use TransformerLens to reproduce findings.

### Theoretical Alignment Papers (MIRI, agent foundations)

These are more philosophical. Strategy:

1. **Read the thought experiments first** — they motivate the formalism.
2. **Don't get lost in notation.** If a definition has 5 subscripts, ask: "What is this trying to capture in plain English?"
3. **Check LessWrong/Alignment Forum** for community discussions — they often clarify confusing parts.

### ML Architecture Papers ("Attention Is All You Need")

Strategy:

1. **Architecture diagram = the whole paper.** Study Figure 1 intensely.
2. **Trace dimensions.** For every operation, track the shape of the tensors: input is [batch, seq_len, d_model], after Q projection it's [batch, seq_len, d_k], etc.
3. **Implement it.** You don't truly understand an architecture paper until you've coded it.

## Reading Queue — In Order

Start reading papers in Phase 4. Here's the progression from "accessible" to "dense":

### Level 1: Accessible (readable after Phase 4)
- "Attention Is All You Need" (Vaswani et al.) — the original transformer paper
- "The Illustrated Transformer" by Jay Alammar (blog post, not a paper — warm-up)

### Level 2: Core Interpretability (readable after Phase 5)
- "A Mathematical Framework for Transformer Circuits" (Elhage et al.)
- "In-context Learning and Induction Heads" (Olsson et al.)
- "Toy Models of Superposition" (Elhage et al.)

### Level 3: Alignment Foundations (readable after Phase 6)
- "Concrete Problems in AI Safety" (Amodei et al.)
- "Risks from Learned Optimization" (Hubinger et al.)
- "Functional Decision Theory" (Yudkowsky & Soares)

### Level 4: Frontier Research (post-curriculum)
- "Scaling Monosemanticity" (Anthropic)
- "Logical Induction" (Garrabrant et al.)
- "Embedded Agency" (Demski & Garrabrant)

## Common Paper-Reading Mistakes

1. **Reading linearly from start to finish** — don't. Use the three-pass method.
2. **Getting stuck on one equation** — mark it and move on. Context often clarifies.
3. **Not looking at the figures** — in ML, figures > text.
4. **Reading alone** — discuss papers with others. The Alignment Forum, EleutherAI Discord, and LessWrong have active paper discussions.
5. **Trying to read papers too early** — the curriculum exists so you have the vocabulary. Don't read "Scaling Monosemanticity" before you understand what SVD, attention, and superposition are.
6. **Skipping the code** — if a paper has companion code or a colab notebook, USE IT.
