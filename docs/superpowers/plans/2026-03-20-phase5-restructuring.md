# Phase 5 Restructuring Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restructure Phase 5 from 13 lessons into 28 lessons across 6 video-course-based blocks, renumber Phase 6 downstream, and update all dependent files.

**Architecture:** Four sequential phases: (1) backup + rename Phase 6 files, (2) delete old Phase 5 + create new content, (3) update all infrastructure files, (4) verify. Content creation tasks within Phase 2 are independent and parallelizable.

**Spec:** `docs/superpowers/specs/2026-03-20-phase5-restructuring-design.md`

---

## Phase 1: Preparation

### Task 1: Create backup branch and rename Phase 6 files

**Files:**
- Rename: `phase6-alignment/lesson-80-game-theory.md` → `lesson-95-game-theory.md`
- Rename: `phase6-alignment/lesson-81-decision-theory.md` → `lesson-96-decision-theory.md`
- Rename: `phase6-alignment/lesson-82-anthropics.md` → `lesson-97-anthropics.md`
- Rename: `phase6-alignment/lesson-83-alignment-problem.md` → `lesson-98-alignment-problem.md`
- Rename: `phase6-alignment/lesson-84-open-problems.md` → `lesson-99-open-problems.md`
- Rename: `phase6-alignment/lesson-84a-alignment-capstone-project.qmd` → `lesson-99a-alignment-capstone-project.qmd`
- Delete: `phase6-alignment/lesson-84a-alignment-capstone-project.pdf`

- [ ] **Step 1: Create backup branch**

```bash
cd /mnt/c/Users/Veste/Documents/Local_Code/research_plan
git checkout -b phase5-restructuring
git push -u origin phase5-restructuring
```

- [ ] **Step 2: Rename Phase 6 lesson files**

```bash
cd /mnt/c/Users/Veste/Documents/Local_Code/research_plan/phase6-alignment
git mv lesson-80-game-theory.md lesson-95-game-theory.md
git mv lesson-81-decision-theory.md lesson-96-decision-theory.md
git mv lesson-82-anthropics.md lesson-97-anthropics.md
git mv lesson-83-alignment-problem.md lesson-98-alignment-problem.md
git mv lesson-84-open-problems.md lesson-99-open-problems.md
git mv lesson-84a-alignment-capstone-project.qmd lesson-99a-alignment-capstone-project.qmd
rm lesson-84a-alignment-capstone-project.pdf
```

- [ ] **Step 3: Update navigation links inside each renamed Phase 6 file**

Each lesson has a navigation header like:
```
[← Prev](../phase5-math-enrichment/lesson-78-godel-lob.md) | [Back to TOC](../README.md) | [Next →](lesson-81-decision-theory.md)
```

**NOTE:** The Prev link for lesson-95 will point to `../phase5-math-enrichment/lesson-94-lower-bounds-amortized.md` which does not exist yet (created in Phase 2, Task 8). This is expected — set the link now and it will resolve after content creation.

Update ALL internal cross-references:
- `lesson-95-game-theory.md`: Prev link → `../phase5-math-enrichment/lesson-94-lower-bounds-amortized.md`, Next → `lesson-96-decision-theory.md`
- `lesson-96-decision-theory.md`: Prev → `lesson-95-game-theory.md`, Next → `lesson-97-anthropics.md`
- `lesson-97-anthropics.md`: Prev → `lesson-96-decision-theory.md`, Next → `lesson-98-alignment-problem.md`
- `lesson-98-alignment-problem.md`: Prev → `lesson-97-anthropics.md`, Next → `lesson-99-open-problems.md`
- `lesson-99-open-problems.md`: Prev → `lesson-98-alignment-problem.md`
- Also update any "Lesson 80/81/82/83/84" references in body text to 95/96/97/98/99

- [ ] **Step 4: Update PHASE-6-OVERVIEW.md**

Change all lesson number references:
- "Lessons 80–84" → "Lessons 95–99"
- "Lesson 80:" → "Lesson 95:" (etc. for each lesson header)

- [ ] **Step 5: Update lesson-99a-alignment-capstone-project.qmd**

Update any internal lesson number references from old numbering to new.

- [ ] **Step 6: Fix Phase 7 stale link**

In `phase7-research/research-guide.md` line 2:
Change: `[← Open Problems](../phase6-alignment/lesson-70-open-problems.md)`
To: `[← Open Problems](../phase6-alignment/lesson-99-open-problems.md)`

- [ ] **Step 7: Commit**

```bash
git add -A
git commit -m "refactor: renumber Phase 6 lessons 80-84 → 95-99 for Phase 5 expansion"
```

---

### Task 2: Delete old Phase 5 content

**Files:**
- Delete: All 22 files in `phase5-math-enrichment/`

- [ ] **Step 1: Delete all old Phase 5 files**

```bash
cd /mnt/c/Users/Veste/Documents/Local_Code/research_plan
rm phase5-math-enrichment/PHASE-5-OVERVIEW.md
rm phase5-math-enrichment/lesson-67-turing-machines.md
rm phase5-math-enrichment/lesson-68-computational-complexity.md
rm phase5-math-enrichment/lesson-69-kolmogorov-complexity.md
rm phase5-math-enrichment/lesson-69a-computability-coding-project.qmd
rm phase5-math-enrichment/lesson-69a-computability-coding-project.pdf
rm phase5-math-enrichment/lesson-70-groups.md
rm phase5-math-enrichment/lesson-71-rings-fields.md
rm phase5-math-enrichment/lesson-72-group-actions.md
rm phase5-math-enrichment/lesson-72a-abstract-algebra-coding-project.qmd
rm phase5-math-enrichment/lesson-72a-abstract-algebra-coding-project.pdf
rm phase5-math-enrichment/lesson-73-point-set-topology.md
rm phase5-math-enrichment/lesson-74-homotopy.md
rm phase5-math-enrichment/lesson-75-manifolds.md
rm phase5-math-enrichment/lesson-76-algebraic-geometry.md
rm phase5-math-enrichment/lesson-76a-topology-geometry-coding-project.qmd
rm phase5-math-enrichment/lesson-76a-topology-geometry-coding-project.pdf
rm phase5-math-enrichment/lesson-77-propositional-logic.md
rm phase5-math-enrichment/lesson-78-godel-lob.md
rm phase5-math-enrichment/lesson-78a-formal-logic-coding-project.qmd
rm phase5-math-enrichment/lesson-78a-formal-logic-coding-project.pdf
rm phase5-math-enrichment/lesson-79-differential-forms.md
```

- [ ] **Step 2: Delete old Phase 5 assessment files (8 files)**

```bash
cd /mnt/c/Users/Veste/Documents/Local_Code/research_plan/assessments
rm exam-5a-computability-algebra.qmd exam-5a-computability-algebra.pdf
rm exam-5a-computability-algebra-answer-key.qmd exam-5a-computability-algebra-answer-key.pdf
rm exam-5b-topology-logic.qmd exam-5b-topology-logic.pdf
rm exam-5b-topology-logic-answer-key.qmd exam-5b-topology-logic-answer-key.pdf
```

- [ ] **Step 3: Remove discrete math from cs_foundations**

```bash
rm phase0-cs-foundations/lesson-cs09-discrete-math.md
```

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "chore: remove old Phase 5 content (22 files), old exams (8 files), and discrete math from cs_foundations"
```

---

## Phase 2: New Content Creation

**IMPORTANT:** Tasks 3–8 are independent and can be executed in parallel by separate subagents. Each creates lesson files following the existing lesson format (see `phase2-calculus/lesson-13-calculus-fundamentals.md` as template). Each lesson must include:
- Title line: `# Lesson N: Title`
- Navigation: `[← Prev](prev-file.md) | [Back to TOC](../README.md) | [Next: Title →](next-file.md)`
- `> **Why this lesson exists:**` paragraph
- `> **Estimated time:**` line
- Content sections with `## Part N:` headers
- `## Watch — Primary` section with video links from the block's primary resource
- `## Read — Primary` section with textbook/article references
- `## Exercises` section

### Task 3: Create Block A lessons — Discrete Mathematics (67–71)

**Files:**
- Create: `phase5-math-enrichment/lesson-67-logic-propositions.md`
- Create: `phase5-math-enrichment/lesson-68-sets-functions-relations.md`
- Create: `phase5-math-enrichment/lesson-69-combinatorics.md`
- Create: `phase5-math-enrichment/lesson-70-graph-theory.md`
- Create: `phase5-math-enrichment/lesson-71-recurrences-generating-functions.md`
- Create: `phase5-math-enrichment/lesson-71a-discrete-math-coding-project.qmd`

- [ ] **Step 1: Create lesson-67-logic-propositions.md**

Content scope: Propositional logic, truth tables, logical equivalences, quantifiers, proof techniques (direct, contrapositive, contradiction, induction). Based on Trefor Bazzett Discrete Math playlist.
- Prev link: `../phase4-machine-learning/lesson-66-interp-slt.md`
- Next link: `lesson-68-sets-functions-relations.md`
- Video: Trefor Bazzett — Discrete Math (logical statements, truth tables, proof techniques sections)
- Supplement: TrevTutor DM1 — Logic and proof technique videos

- [ ] **Step 2: Create lesson-68-sets-functions-relations.md**

Content scope: Set operations, power sets, Cartesian products, functions (injective, surjective, bijective), relations, equivalence relations, partial orders. Based on Trefor Bazzett Discrete Math playlist.
- Prev: `lesson-67-logic-propositions.md`
- Next: `lesson-69-combinatorics.md`

- [ ] **Step 3: Create lesson-69-combinatorics.md**

Content scope: Counting principles, permutations, combinations, binomial theorem, pigeonhole principle, inclusion-exclusion. Based on Trefor Bazzett Discrete Math playlist.
- Prev: `lesson-68-sets-functions-relations.md`
- Next: `lesson-70-graph-theory.md`

- [ ] **Step 4: Create lesson-70-graph-theory.md**

Content scope: Graph definitions, paths, cycles, trees, Euler/Hamilton paths, planarity, graph coloring, chromatic number, spanning trees. Based on Trefor Bazzett Discrete Math playlist.
- Prev: `lesson-69-combinatorics.md`
- Next: `lesson-71-recurrences-generating-functions.md`

- [ ] **Step 5: Create lesson-71-recurrences-generating-functions.md**

Content scope: Recurrence relations (homogeneous, non-homogeneous), solving with characteristic equations, generating functions (ordinary, exponential), coefficient extraction. Based on Trefor Bazzett Discrete Math playlist.
- Prev: `lesson-70-graph-theory.md`
- Next: `lesson-72-finite-automata.md`
- Supplement: TrevTutor DM2 for generating functions deep dive

- [ ] **Step 6: Create lesson-71a-discrete-math-coding-project.qmd**

Coding project: Graph theory implementation (adjacency representations, BFS/DFS, coloring algorithms) + generating function computation (symbolic manipulation, sequence generation).

- [ ] **Step 7: Commit**

```bash
git add phase5-math-enrichment/lesson-{67,68,69,70,71}*.md phase5-math-enrichment/lesson-71a*.qmd
git commit -m "feat: add Phase 5 Block A — Discrete Mathematics (lessons 67-71 + coding project)"
```

---

### Task 4: Create Block B lessons — Computability & Complexity (72–76)

**Files:**
- Create: `phase5-math-enrichment/lesson-72-finite-automata.md`
- Create: `phase5-math-enrichment/lesson-73-context-free-grammars.md`
- Create: `phase5-math-enrichment/lesson-74-turing-machines.md`
- Create: `phase5-math-enrichment/lesson-75-kolmogorov-complexity.md`
- Create: `phase5-math-enrichment/lesson-76-computational-complexity.md`
- Create: `phase5-math-enrichment/lesson-76a-computability-coding-project.qmd`

**Migration notes:** Refactor content from old lessons 67 (→74), 68 (→76), 69 (→75). Read old content from git history: `git show HEAD~2:phase5-math-enrichment/lesson-67-turing-machines.md` (adjust commit ref as needed).

- [ ] **Step 1: Create lesson-72-finite-automata.md**

Content scope: DFAs, NFAs, NFA-to-DFA conversion, regular expressions, pumping lemma, closure properties. Based on Neso Academy Theory of Computation playlist.
- Prev: `lesson-71-recurrences-generating-functions.md`
- Next: `lesson-73-context-free-grammars.md`
- Video: Neso Academy — DFA/NFA sections
- Textbook: Sipser Ch. 1

- [ ] **Step 2: Create lesson-73-context-free-grammars.md**

Content scope: CFGs, parse trees, ambiguity, Chomsky normal form, pushdown automata, CFL pumping lemma. Based on Neso Academy.
- Video: Neso Academy — CFG/PDA sections
- Textbook: Sipser Ch. 2

- [ ] **Step 3: Create lesson-74-turing-machines.md**

Content scope: Turing machine definition, Church-Turing thesis, universal TM, halting problem, Rice's theorem, decidability landscape, reductions. Refactor from old lesson 67.
- Video: Neso Academy — Turing machine/decidability sections
- Textbook: Sipser Ch. 3–5

- [ ] **Step 4: Create lesson-75-kolmogorov-complexity.md**

Content scope: Kolmogorov complexity, algorithmic information, MDL, Solomonoff induction, AIXI, Occam's razor connection. Refactor from old lesson 69.
- Video: Neso Academy (limited coverage) + individual curated videos
- Textbook: Sipser + Li & Vitanyi

- [ ] **Step 5: Create lesson-76-computational-complexity.md**

Content scope: P, NP, NP-completeness, Cook-Levin, polynomial reductions, NP-hard problems in ML, space complexity, BPP, approximation. Refactor from old lesson 68, expand scope.
- Video: Neso Academy (limited) + Hackerdashery "Complexity Zoo" + Abdul Bari NP-hard videos
- Textbook: Sipser Ch. 7–9

- [ ] **Step 6: Create lesson-76a-computability-coding-project.qmd**

Coding project: Turing machine simulator (tape, head, transitions) + decidability demonstrations (halting problem via diagonalization, Rice's theorem examples).

- [ ] **Step 7: Commit**

```bash
git add phase5-math-enrichment/lesson-{72,73,74,75,76}*.md phase5-math-enrichment/lesson-76a*.qmd
git commit -m "feat: add Phase 5 Block B — Computability & Complexity (lessons 72-76 + coding project)"
```

---

### Task 5: Create Block C lessons — Formal Logic (77–79)

**Files:**
- Create: `phase5-math-enrichment/lesson-77-propositional-predicate-logic.md`
- Create: `phase5-math-enrichment/lesson-78-proof-systems.md`
- Create: `phase5-math-enrichment/lesson-79-godel-incompleteness.md`

**Migration notes:** Refactor from old lessons 77 (→77) and 78 (→79). Lesson 78 (Proof Systems) is new content.

- [ ] **Step 1: Create lesson-77-propositional-predicate-logic.md**

Content scope: Propositional logic (syntax, semantics, normal forms), predicate logic (quantifiers, scope, prenex form), validity, satisfiability, model theory basics. Refactor from old lesson 77.
- Prev: `lesson-76-computational-complexity.md`
- Next: `lesson-78-proof-systems.md`
- Video: Trefor Bazzett — Logic playlist
- Note: Some overlap with lesson 67 (logic in discrete math context) — this lesson goes deeper into formal systems

- [ ] **Step 2: Create lesson-78-proof-systems.md**

Content scope: Natural deduction, sequent calculus, soundness and completeness theorems, proof strategies, automated theorem proving basics. NEW content — no old equivalent.
- Video: Trefor Bazzett — Logic playlist (proof-related videos)

- [ ] **Step 3: Create lesson-79-godel-incompleteness.md**

Content scope: Godel's first and second incompleteness theorems, Godel numbering, self-reference, Lob's theorem, implications for AI verification, logical limits of formal systems. Refactor from old lesson 78.
- Video: Trefor Bazzett — Logic playlist + individual curated videos on Godel

- [ ] **Step 4: Commit**

```bash
git add phase5-math-enrichment/lesson-{77,78,79}*.md
git commit -m "feat: add Phase 5 Block C — Formal Logic (lessons 77-79)"
```

---

### Task 6: Create Block D lessons — Abstract Algebra (80–84)

**Files:**
- Create: `phase5-math-enrichment/lesson-80-groups.md`
- Create: `phase5-math-enrichment/lesson-81-cosets-lagrange.md`
- Create: `phase5-math-enrichment/lesson-82-homomorphisms.md`
- Create: `phase5-math-enrichment/lesson-83-rings-fields.md`
- Create: `phase5-math-enrichment/lesson-84-group-actions.md`
- Create: `phase5-math-enrichment/lesson-84a-algebra-coding-project.qmd`

**Migration notes:** Refactor from old lessons 70 (→80), 71 (→83), 72 (→84). Lessons 81–82 expand from old 2 lessons to 3.

- [ ] **Step 1: Create lesson-80-groups.md**

Content scope: Group definition, examples (Z_n, S_n, D_n, GL_n), Cayley tables and diagrams, subgroups, cyclic groups, order. Based on Macauley Visual Group Theory.
- Prev: `lesson-79-godel-incompleteness.md`
- Next: `lesson-81-cosets-lagrange.md`
- Video: Macauley Visual Group Theory (lectures 1–~10)
- Supplement: Socratica — Groups introduction
- Textbook: Aluffi Ch. I–II

- [ ] **Step 2: Create lesson-81-cosets-lagrange.md**

Content scope: Cosets, Lagrange's theorem, index, normal subgroups, simple groups. Based on Macauley.
- Video: Macauley Visual Group Theory (lectures ~11–20)

- [ ] **Step 3: Create lesson-82-homomorphisms.md**

Content scope: Group homomorphisms, isomorphisms, kernel/image, first isomorphism theorem, quotient groups, classification. Based on Macauley.
- Video: Macauley Visual Group Theory (lectures ~21–30)
- Textbook: Aluffi Ch. III

- [ ] **Step 4: Create lesson-83-rings-fields.md**

Content scope: Ring definition, ideals, quotient rings, polynomial rings, field extensions, finite fields. Refactor from old lesson 71.
- Video: Macauley Visual Group Theory (ring section) + Michael Penn rings/fields videos
- Textbook: Aluffi Ch. IV–V

- [ ] **Step 5: Create lesson-84-group-actions.md**

Content scope: Group actions, orbits, stabilizers, Burnside's lemma, representations, neural network weight symmetry, connections to SLT. Refactor from old lesson 72.
- Video: Macauley Visual Group Theory (actions section)
- Textbook: Aluffi Ch. II (actions)

- [ ] **Step 6: Create lesson-84a-algebra-coding-project.qmd**

Coding project: Group symmetry explorer (Cayley diagram generation, subgroup lattice visualization) + neural network weight permutation symmetry analysis.

- [ ] **Step 7: Commit**

```bash
git add phase5-math-enrichment/lesson-{80,81,82,83,84}*.md phase5-math-enrichment/lesson-84a*.qmd
git commit -m "feat: add Phase 5 Block D — Abstract Algebra (lessons 80-84 + coding project)"
```

---

### Task 7: Create Block E lessons — Geometry for Alignment (85–89)

**Files:**
- Create: `phase5-math-enrichment/lesson-85-curves-surfaces.md`
- Create: `phase5-math-enrichment/lesson-86-tangent-spaces.md`
- Create: `phase5-math-enrichment/lesson-87-manifolds.md`
- Create: `phase5-math-enrichment/lesson-88-differential-forms.md`
- Create: `phase5-math-enrichment/lesson-89-algebraic-geometry.md`
- Create: `phase5-math-enrichment/lesson-89a-geometry-coding-project.qmd`

**Migration notes:** Refactor from old lessons 73 (→~85), 75 (→87), 76 (→89), 79 (→88). Lesson 86 is new. Old lesson 74 (Homotopy) is deliberately dropped.

- [ ] **Step 1: Create lesson-85-curves-surfaces.md**

Content scope: Parametric curves, regular surfaces, first/second fundamental forms, Gauss map, principal curvatures. Based on What is Math differential geometry playlist.
- Prev: `lesson-84-group-actions.md`
- Next: `lesson-86-tangent-spaces.md`
- Video: What is Math — Differential Geometry playlist (early videos)
- Supplement: eigenchris Tensors for Beginners
- Note: Expedited — focus on concepts needed for alignment/SLT, skip pure topology

- [ ] **Step 2: Create lesson-86-tangent-spaces.md**

Content scope: Tangent vectors, tangent spaces, cotangent spaces, metric tensors, Riemannian metrics, curvature tensors. NEW content.
- Video: What is Math + eigenchris Tensor Calculus series

- [ ] **Step 3: Create lesson-87-manifolds.md**

Content scope: Topological manifolds, smooth manifolds, charts and atlases, geodesics, exponential map, Lie groups connection. Refactor from old lesson 75.
- Video: What is Math — manifolds section
- Supplement: eigenchris for geodesics/connections

- [ ] **Step 4: Create lesson-88-differential-forms.md**

Content scope: k-forms, wedge product, exterior derivative, Stokes' theorem, de Rham cohomology basics. Refactor from old lesson 79.
- Video: Michael Penn — Differential Forms playlist
- Supplement: What is Math for geometric intuition

- [ ] **Step 5: Create lesson-89-algebraic-geometry.md**

Content scope: Affine varieties, polynomial ideals, singularities, resolution of singularities, blowups, RLCT definition, connection to SLT and model selection. Refactor from old lesson 76.
- Video: Limited video resources — use Aleph 0 "What is Algebraic Geometry?" + individual videos
- Note: Include "go deeper" pointers to NPTEL algebraic geometry course and Harpreet Bedi lectures

- [ ] **Step 6: Create lesson-89a-geometry-coding-project.qmd**

Coding project: Manifold visualization (surface plotting, geodesic computation, curvature heatmaps) + singularity resolution for SLT (blowup computation, RLCT estimation).

- [ ] **Step 7: Commit**

```bash
git add phase5-math-enrichment/lesson-{85,86,87,88,89}*.md phase5-math-enrichment/lesson-89a*.qmd
git commit -m "feat: add Phase 5 Block E — Geometry for Alignment (lessons 85-89 + coding project)"
```

---

### Task 8: Create Block F lessons — Advanced Algorithms (90–94)

**Files:**
- Create: `phase5-math-enrichment/lesson-90-analysis-of-algorithms.md`
- Create: `phase5-math-enrichment/lesson-91-randomized-algorithms.md`
- Create: `phase5-math-enrichment/lesson-92-combinatorial-algorithms.md`
- Create: `phase5-math-enrichment/lesson-93-advanced-graph-algorithms.md`
- Create: `phase5-math-enrichment/lesson-94-lower-bounds-amortized.md`
- Create: `phase5-math-enrichment/lesson-94a-algorithms-coding-project.qmd`

- [ ] **Step 1: Create lesson-90-analysis-of-algorithms.md**

Content scope: Asymptotic analysis beyond big-O (little-o, Theta, Omega), recurrence solving (master theorem, Akra-Bazzi), generating functions for algorithm analysis (Flajolet/Sedgewick style), amortized cost preview. Knuth/TAOCP style.
- Prev: `lesson-89-algebraic-geometry.md`
- Next: `lesson-91-randomized-algorithms.md`
- Video: Curated individual videos (Reducible for intuition, specific topic videos)

- [ ] **Step 2: Create lesson-91-randomized-algorithms.md**

Content scope: Probabilistic analysis, randomized quicksort analysis, hashing theory (universal hashing, perfect hashing, cuckoo hashing), random graphs, Chernoff bounds, Monte Carlo vs Las Vegas algorithms.
- Video: Curated individual videos

- [ ] **Step 3: Create lesson-92-combinatorial-algorithms.md**

Content scope: Systematic enumeration (permutations, combinations, partitions — Knuth Vol 4A), backtracking with pruning, combinatorial generation algorithms, Gray codes, de Bruijn sequences.
- Video: Curated individual videos + Reducible

- [ ] **Step 4: Create lesson-93-advanced-graph-algorithms.md**

Content scope: Maximum matching (bipartite and general), planarity testing, network flow (Ford-Fulkerson, Edmonds-Karp, Dinic's), min-cut applications, algebraic graph theory basics.
- Video: WilliamFiset for network flow; curated for matching/planarity

- [ ] **Step 5: Create lesson-94-lower-bounds-amortized.md**

Content scope: Information-theoretic lower bounds (comparison sorting Omega(n log n), decision tree model), adversary arguments, amortized analysis (aggregate, accounting, potential methods), connections to computational complexity (circuit lower bounds).
- Prev: `lesson-93-advanced-graph-algorithms.md`
- Next: `../phase6-alignment/lesson-95-game-theory.md`
- Video: Curated individual videos + Roughgarden for NP-hardness connections

- [ ] **Step 6: Create lesson-94a-algorithms-coding-project.qmd**

Coding project: Probabilistic algorithm analysis (empirical vs theoretical runtime distributions) + combinatorial generation (implement Knuth's Algorithm L for permutations, partition generation).

- [ ] **Step 7: Commit**

```bash
git add phase5-math-enrichment/lesson-{90,91,92,93,94}*.md phase5-math-enrichment/lesson-94a*.qmd
git commit -m "feat: add Phase 5 Block F — Advanced Algorithms (lessons 90-94 + coding project)"
```

---

### Task 9: Create PHASE-5-OVERVIEW.md

**Files:**
- Create: `phase5-math-enrichment/PHASE-5-OVERVIEW.md`

- [ ] **Step 1: Write PHASE-5-OVERVIEW.md**

Follow the format of the existing Phase 6 overview (`phase6-alignment/PHASE-6-OVERVIEW.md`). Structure:
- Title: `# Phase 5 Overview: Mathematical Enrichment — Every Concept and Method`
- Purpose paragraph referencing Lessons 67–94
- 6 sections matching the 6 blocks (A–F)
- Under each block: lesson-by-lesson concept summaries (bullet points of key definitions, theorems, methods)
- Pull concept summaries from the lesson files just created

- [ ] **Step 2: Commit**

```bash
git add phase5-math-enrichment/PHASE-5-OVERVIEW.md
git commit -m "feat: add Phase 5 overview document covering lessons 67-94"
```

---

### Task 10: Create Phase 5 assessments (6 exams + 6 answer keys)

**Files:**
- Create: `assessments/exam-5a-discrete-math.qmd`
- Create: `assessments/exam-5a-discrete-math-answer-key.qmd`
- Create: `assessments/exam-5b-computability-complexity.qmd`
- Create: `assessments/exam-5b-computability-complexity-answer-key.qmd`
- Create: `assessments/exam-5c-formal-logic.qmd`
- Create: `assessments/exam-5c-formal-logic-answer-key.qmd`
- Create: `assessments/exam-5d-abstract-algebra.qmd`
- Create: `assessments/exam-5d-abstract-algebra-answer-key.qmd`
- Create: `assessments/exam-5e-geometry-alignment.qmd`
- Create: `assessments/exam-5e-geometry-alignment-answer-key.qmd`
- Create: `assessments/exam-5f-advanced-algorithms.qmd`
- Create: `assessments/exam-5f-advanced-algorithms-answer-key.qmd`

Follow the format of existing exams (e.g., `assessments/exam-6a-rational-agency.qmd`): Quarto .qmd with YAML frontmatter (title, subtitle, format: pdf), mix of multiple-choice, short-answer, and essay/proof questions.

- [ ] **Step 1: Create exam-5a-discrete-math.qmd + answer key**

Covers lessons 67–71. Questions on: logic proofs, set theory, counting problems, graph theory, recurrences/generating functions.

- [ ] **Step 2: Create exam-5b-computability-complexity.qmd + answer key**

Covers lessons 72–76. Questions on: DFA/NFA construction, CFG derivations, Turing machine design, undecidability proofs, NP-completeness reductions.

- [ ] **Step 3: Create exam-5c-formal-logic.qmd + answer key**

Covers lessons 77–79. Questions on: formal proofs, soundness/completeness, Godel's theorems implications, Lob's theorem.

- [ ] **Step 4: Create exam-5d-abstract-algebra.qmd + answer key**

Covers lessons 80–84. Questions on: group properties, Lagrange's theorem, homomorphism proofs, ring/field constructions, group action applications.

- [ ] **Step 5: Create exam-5e-geometry-alignment.qmd + answer key**

Covers lessons 85–89. Questions on: curvature computation, manifold properties, differential forms, singularity analysis, RLCT connection.

- [ ] **Step 6: Create exam-5f-advanced-algorithms.qmd + answer key**

Covers lessons 90–94. Questions on: recurrence analysis, probabilistic algorithm analysis, combinatorial generation, flow problems, lower bound proofs.

- [ ] **Step 7: Commit**

```bash
git add assessments/exam-5*.qmd
git commit -m "feat: add 6 Phase 5 block exams with answer keys"
```

---

## Phase 3: Infrastructure Updates

### Task 11: Update README.md

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Update CS Foundations section**

Remove the cs09 discrete math row (line 25):
```
| cs09 | [Discrete Math Essentials...](phase0-cs-foundations/lesson-cs09-discrete-math.md) | ⬜ Not Started |
```

- [ ] **Step 2: Rewrite Phase 5 section**

Replace lines 188–222 (old Phase 5) with new 6-block structure matching Phase 2 format:

```markdown
## Phase 5: Mathematical Enrichment (XXX–XXXh)

### Block A: Discrete Mathematics (67–71) — Trefor Bazzett

| # | Lesson | Status |
|---|--------|--------|
| 67 | [Logic, Propositions, and Proof Techniques](phase5-math-enrichment/lesson-67-logic-propositions.md) | ⬜ Not Started |
| 68 | [Sets, Functions, and Relations](phase5-math-enrichment/lesson-68-sets-functions-relations.md) | ⬜ Not Started |
...
```

(Continue for all 6 blocks with all 28 lessons + 5 coding projects)

- [ ] **Step 3: Update Phase 6 section**

Change lesson numbers 80–84 → 95–99 and update all file path links:
```markdown
## Phase 6: Alignment Theory (52–62h)

| # | Lesson | Status |
|---|--------|--------|
| 95 | [Game Theory Foundations](phase6-alignment/lesson-95-game-theory.md) | ⬜ Not Started |
...
```

- [ ] **Step 4: Update Assessments table**

Remove old Exam 5A/5B rows. Add 6 new rows (5A–5F). Update Exam 6A lesson range to "Lessons 95–98" and 6B to "Lessons 95–99".

- [ ] **Step 5: Update header**

Change "85 lessons across 8 phases" to reflect new lesson count (85 - 13 + 28 - 1 = 99 lessons, minus cs09 = 98 numbered + cs lessons).

- [ ] **Step 6: Commit**

```bash
git add README.md
git commit -m "docs: update README with new Phase 5 structure (6 blocks, 28 lessons) and renumbered Phase 6"
```

---

### Task 12: Update curriculum-dashboard.html

**Files:**
- Modify: `curriculum-dashboard.html`

This is the largest single file update (~191KB). Focus on the JavaScript data structures.

- [ ] **Step 1: Find and replace Phase 5 lesson data**

Locate the Phase 5 lesson array (approximately lines 2136–2366). Replace the 13 old lesson objects with 28 new ones. Each lesson object follows this pattern:
```javascript
{ id: 67, title: 'Logic, Propositions, and Proof Techniques', phase: 'p5', block: 'A',
  duration: { min: 15, max: 20 }, prereqs: [66],
  file: 'phase5-math-enrichment/lesson-67-logic-propositions.md' },
```

Ensure strict sequential ordering 67–94 (no ordering anomaly like the old 79-between-75-and-76).

- [ ] **Step 2: Update Phase 5 checkpoints**

Replace old checkpoint `cp5` with 6 block checkpoints or one end-of-phase checkpoint:
```javascript
{ id: 'cp5', afterLesson: 94, title: 'Phase 5 Review: Mathematical Enrichment' }
```

- [ ] **Step 3: Shift Phase 6 lesson IDs**

Find Phase 6 lesson objects (id: 80–84) and change to 95–99. Update all prerequisite arrays that reference these IDs.

- [ ] **Step 4: Update prerequisite chains**

- Lesson 67 prereqs: [66] (bridges from Phase 4)
- Lesson 72 prereqs: [71] (Block B follows Block A)
- Lesson 77 prereqs: [76] (Block C follows Block B)
- Lesson 80 prereqs: [79] (Block D follows Block C)
- Lesson 85 prereqs: [84] (Block E follows Block D)
- Lesson 90 prereqs: [89] (Block F follows Block E)
- Lesson 95 prereqs: [94] (Phase 6 follows Phase 5)

- [ ] **Step 5: Update phase color mappings if they exist**

Check for any color/styling data that maps 'p5' to visual properties. Ensure new blocks are accounted for.

- [ ] **Step 6: Commit**

```bash
git add curriculum-dashboard.html
git commit -m "feat: update dashboard with 28 Phase 5 lessons across 6 blocks + renumbered Phase 6"
```

---

### Task 13: Update sr-data.js

**Files:**
- Modify: `sr-data.js`

- [ ] **Step 1: Find Phase 5 entries in sr-data.js**

Search for lesson references in the 67–79 range and any Phase 5 section markers.

- [ ] **Step 2: Replace Phase 5 spaced repetition entries**

Replace old entries with new ones covering all 28 lessons. Each entry should follow the existing format (inspect the file for the exact structure — likely topic/question/answer objects keyed by lesson number).

- [ ] **Step 3: Update any Phase 6 lesson references (80–84 → 95–99)**

- [ ] **Step 4: Commit**

```bash
git add sr-data.js
git commit -m "feat: update spaced repetition data for new Phase 5 structure"
```

---

### Task 13b: Check JSON data files for stale Phase 6 references

**Files:**
- Check: `daily-plan.json`, `calendar-data.json`, `pace-data.json`, `hours-log.json`, `sr-progress.json`, `ms-progress.json`

- [ ] **Step 1: Grep JSON files for old Phase 6 lesson numbers**

```bash
cd /mnt/c/Users/Veste/Documents/Local_Code/research_plan
grep -n "80\|81\|82\|83\|84" daily-plan.json calendar-data.json pace-data.json hours-log.json sr-progress.json ms-progress.json
```

If any results reference lesson numbers 80–84 (not arbitrary numbers), update them to 95–99. Phase 5 entries (67–79) in these files can be left as-is — they'll be orphaned but harmless since all Phase 5 lessons were "Not Started".

- [ ] **Step 2: Commit if changes were made**

```bash
git add *.json
git commit -m "fix: update Phase 6 lesson references in JSON data files (80-84 → 95-99)"
```

---

### Task 14: Update full-concept-overview.md

**Files:**
- Modify: `full-overview/full-concept-overview.md`

- [ ] **Step 1: Rewrite Phase 5 section (lines ~726–824)**

Replace with 6-block structure. Pull concept summaries from PHASE-5-OVERVIEW.md (Task 9) to keep DRY — but this file is more condensed (1–3 bullet points per lesson vs. exhaustive in the overview).

- [ ] **Step 2: Update Phase 6 lesson references**

Change any "Lesson 80" → "Lesson 95" etc. in the Phase 6 section.

- [ ] **Step 3: Commit**

```bash
git add full-overview/full-concept-overview.md
git commit -m "docs: update full concept overview for new Phase 5 and renumbered Phase 6"
```

---

### Task 15: Update resources files

**Files:**
- Modify: `resources/video-index.md`
- Modify: `resources/cheat-sheet.md`
- Modify: `resources/intuition-notebook.md`

- [ ] **Step 1: Rewrite video-index.md Phase 5 section**

Replace the existing Phase 5 video mappings (Aleph 0 lesson refs, Socratica lesson refs, eigenchris refs — lines ~282–314+) with new mappings:

Add new sections for:
- Trefor Bazzett — Discrete Math (lessons 67–71)
- Neso Academy — Theory of Computation (lessons 72–76)
- Trefor Bazzett — Logic (lessons 77–79)
- Macauley — Visual Group Theory (lessons 80–84)
- What is Math — Differential Geometry (lessons 85–89)
- Curated Advanced Algorithms videos (lessons 90–94)

Keep existing supplement channels (Socratica, eigenchris, Michael Penn, Aleph 0) but update their lesson number references.

- [ ] **Step 2: Update cheat-sheet.md**

Change the Phase 5 section header (line ~98):
From: `### Phase 5 — Extended Mathematical Foundations`
To: `### Phase 5 — Mathematical Enrichment (Lessons 67–94)`

Update the placeholder text:
From: `*Section not yet started — items will be added during lessons 67–79.*`
To: `*Section not yet started — items will be added during lessons 67–94.*`

- [ ] **Step 3: Update intuition-notebook.md**

Change Phase 5 placeholder (line ~428):
From: `*(To be filled as you progress through Phase 5)*`
To: `*(To be filled as you progress through Phase 5, Lessons 67–94)*`

- [ ] **Step 4: Commit**

```bash
git add resources/video-index.md resources/cheat-sheet.md resources/intuition-notebook.md
git commit -m "docs: update video index, cheat sheet, and intuition notebook for new Phase 5"
```

---

### Task 16: Update capstone assessments and Phase 6 exams

**Files:**
- Modify: `assessments/exam-6a-rational-agency.qmd`
- Modify: `assessments/exam-6a-rational-agency-answer-key.qmd`
- Modify: `assessments/exam-6b-alignment-capstone.qmd`
- Modify: `assessments/exam-6b-alignment-capstone-answer-key.qmd`
- Modify: `assessments/final-project-alignment-observatory.qmd`
- Modify: `assessments/capstone-comprehensive-project.qmd`
- Modify: `assessments/refresher-quizzes-phases-0-6.qmd`

Use the old-to-new lesson number mapping from the spec (Section 3) for all replacements.

- [ ] **Step 1: Update exam-6a-rational-agency.qmd + answer key**

Change subtitle: "Lessons 80--83" → "Lessons 95--98"
Update any body text referencing old lesson numbers.

- [ ] **Step 2: Update exam-6b-alignment-capstone.qmd + answer key**

Change subtitle: "Lessons 80--84" → "Lessons 95--99"
Update ALL Phase 5 cross-references using mapping:
- "Phase 5" topic references: update lesson numbers (67→74 for Turing, 68→76 for complexity, 70→80 for groups, etc.)
- "algorithmic complexity (Phase 5)" → keep, but update any specific lesson numbers
- "singularity type from Phase 5" → keep, update lesson refs
- "group actions, Phase 5" → keep, update lesson refs

- [ ] **Step 3: Update final-project-alignment-observatory.qmd**

Update Phase 5 lesson ranges: "67–72" → new ranges per block, "73–79" → new ranges.
Update topic references to match new lesson numbers.

- [ ] **Step 4: Update capstone-comprehensive-project.qmd**

Update "Phase 5: Computability, Algebra, Topology, Logic" description to reflect new 6-block scope.

- [ ] **Step 5: Rewrite refresher-quizzes-phases-0-6.qmd Phase 5 section**

Find the "# Phase 5 Quiz" section (line ~557) and rewrite entirely to cover new lesson topics across all 6 blocks.

- [ ] **Step 6: Commit**

```bash
git add assessments/exam-6a-rational-agency*.qmd assessments/exam-6b-alignment-capstone*.qmd
git add assessments/final-project-alignment-observatory.qmd assessments/capstone-comprehensive-project.qmd
git add assessments/refresher-quizzes-phases-0-6.qmd
git commit -m "docs: update all capstone/Phase 6 assessments with new Phase 5 lesson numbers"
```

---

### Task 17: Update Phase 4 → Phase 5 navigation link

**Files:**
- Modify: `phase4-machine-learning/lesson-66-interp-slt.md`

- [ ] **Step 1: Update navigation link**

Change the "Next" link (line 3):
From: `[Next: Phase 5 -- Turing Machines >](../phase5-math-enrichment/lesson-67-turing-machines.md)`
To: `[Next: Phase 5 -- Discrete Math >](../phase5-math-enrichment/lesson-67-logic-propositions.md)`

- [ ] **Step 2: Commit**

```bash
git add phase4-machine-learning/lesson-66-interp-slt.md
git commit -m "fix: update Phase 4→5 navigation link to new lesson 67"
```

---

## Phase 4: Verification

### Task 18: Verify all links and references

- [ ] **Step 1: Check for broken internal links**

```bash
cd /mnt/c/Users/Veste/Documents/Local_Code/research_plan
# Find all markdown links and verify targets exist
grep -roh '\[.*\](\.\.\/[^)]*\.md)' phase5-math-enrichment/ phase6-alignment/ phase7-research/ | sed 's/.*(\(.*\))/\1/' | sort -u | while read link; do
  if [ ! -f "phase5-math-enrichment/$link" ] && [ ! -f "$link" ]; then
    echo "BROKEN: $link"
  fi
done
```

- [ ] **Step 2: Check for stale lesson number references**

```bash
# Search for old lesson numbers that should have been updated
grep -rn "lesson-80\|lesson-81\|lesson-82\|lesson-83\|lesson-84" --include="*.md" --include="*.qmd" --include="*.html" --include="*.js" | grep -v phase5-math-enrichment/lesson-8
grep -rn "Lesson 80\|Lesson 81\|Lesson 82\|Lesson 83\|Lesson 84" --include="*.md" --include="*.qmd" | grep -v "phase5-math-enrichment"
```

Any hits outside `phase5-math-enrichment/` are stale references that need fixing.

- [ ] **Step 3: Verify lesson count in README header**

Confirm the total lesson count in the README.md header line matches reality.

- [ ] **Step 4: Verify dashboard lesson count**

Open `curriculum-dashboard.html` in browser and confirm:
- Phase 5 shows 28 lessons in 6 blocks
- Phase 6 shows lessons 95–99
- No gaps or duplicates in the dependency graph

- [ ] **Step 5: Spot-check navigation chain**

Read the nav links in sequence: lesson 66 → 67 → 68 → ... → 94 → 95. Verify each "Next" and "Prev" link points to the correct file.

- [ ] **Step 6: Final commit**

```bash
git add -A
git commit -m "fix: resolve any broken links or stale references from Phase 5 restructuring"
```

- [ ] **Step 7: Merge to main (if on branch)**

```bash
git checkout main
git merge phase5-restructuring
git push
```
