# Phase 5 Restructuring — Design Spec

**Date:** 2026-03-20
**Scope:** Complete restructuring of Phase 5 (Math Enrichment) from 13 lessons to 28 lessons across 6 blocks, with full downstream renumbering of Phases 6–7 and all dependent files.

---

## 1. New Phase 5 Structure

**Phase title:** Phase 5: Mathematical Enrichment
**Lessons:** 67–94 (28 lessons)
**Blocks:** 6 (modeled after Phase 2's block structure)

### Block A: Discrete Mathematics (67–71) — Trefor Bazzett

Primary video: Trefor Bazzett — Discrete Math (~85 videos, ~9hrs)
Supplement: TrevTutor DM1+DM2 for deeper combinatorics/generating functions

| # | Lesson Title |
|---|---|
| 67 | Logic, Propositions, and Proof Techniques |
| 68 | Sets, Functions, and Relations |
| 69 | Combinatorics — Counting, Permutations, and the Binomial Theorem |
| 70 | Graph Theory — Paths, Trees, and Coloring |
| 71 | Recurrence Relations and Generating Functions |

Coding project: 71a — Graph theory implementation + generating function computation

### Block B: Computability & Complexity (72–76) — Neso Academy

Primary video: Neso Academy — Theory of Computation (114 videos)
Supplement: Easy Theory for worked proofs; individual curated videos for P vs NP / complexity classes (Hackerdashery, Abdul Bari NP-hard videos)
Textbook: Sipser — Introduction to the Theory of Computation

| # | Lesson Title |
|---|---|
| 72 | Finite Automata, Regular Languages, and Regular Expressions |
| 73 | Context-Free Grammars and Pushdown Automata |
| 74 | Turing Machines, Decidability, and the Halting Problem |
| 75 | Kolmogorov Complexity, Algorithmic Information, and Solomonoff Induction |
| 76 | Computational Complexity — P, NP, NP-Completeness, and Reductions |

Coding project: 76a — Turing machine simulator + decidability demonstrations

### Block C: Formal Logic (77–79) — Trefor Bazzett

Primary video: Trefor Bazzett — Logic playlist
Shorter block (3 lessons) — less depth than other blocks

| # | Lesson Title |
|---|---|
| 77 | Propositional and Predicate Logic |
| 78 | Proof Systems, Natural Deduction, and Soundness/Completeness |
| 79 | Godel's Incompleteness, Lob's Theorem, and Self-Reference |

No coding project for this block.

### Block D: Abstract Algebra (80–84) — Macauley (Visual Group Theory)

Primary video: Matthew Macauley — Visual Group Theory (46 videos)
Supplement: Socratica for quick intros; Michael Penn for rings/fields
Textbook (deep reference): Aluffi — Algebra: Chapter 0

| # | Lesson Title |
|---|---|
| 80 | Groups — Symmetry, Cayley Diagrams, and Subgroups |
| 81 | Cosets, Lagrange's Theorem, and Normal Subgroups |
| 82 | Homomorphisms, Isomorphisms, and Quotient Groups |
| 83 | Rings, Fields, and Algebraic Structures |
| 84 | Group Actions, Representations, and Neural Network Symmetry |

Coding project: 84a — Group symmetry explorer + neural network weight symmetry analysis

### Block E: Geometry for Alignment (85–89) — What is Math

Primary video: What is Math — Differential Geometry playlist (https://www.youtube.com/watch?v=sAVdmhLiys8&list=PLXo8Tdaw0czOWyRD-esa6mNajlPZnjHQs)
Supplement: eigenchris for tensors/Riemannian geometry; Michael Penn for differential forms
Expedited block — scoped to alignment relevance, with pointers to deeper resources

| # | Lesson Title |
|---|---|
| 85 | Curves, Surfaces, and the Language of Differential Geometry |
| 86 | Tangent Spaces, Metrics, and Curvature |
| 87 | Manifolds and Geodesics |
| 88 | Differential Forms and Stokes' Theorem |
| 89 | Algebraic Geometry — Singularities, Resolution, and SLT |

Coding project: 89a — Manifold visualization + singularity resolution for SLT

### Block F: Advanced Algorithms (90–94) — Curated Videos

Primary video: Individual curated videos per topic (no single series)
Supplement: WilliamFiset for network flow; Reducible for FFT/select topics; Roughgarden for approximation/LP
Style: Knuth/TAOCP-influenced — mathematical analysis of algorithms, not standard DSA

| # | Lesson Title |
|---|---|
| 90 | Analysis of Algorithms — Asymptotic Methods, Recurrences, and Generating Functions |
| 91 | Randomized Algorithms — Probabilistic Analysis, Random Structures, and Hashing Theory |
| 92 | Combinatorial Algorithms — Enumeration, Backtracking, and Combinatorial Generation |
| 93 | Advanced Graph Algorithms — Matching, Planarity, and Network Optimization |
| 94 | Information-Theoretic Lower Bounds, Amortized Analysis, and Computational Complexity Connections |

Coding project: 94a — Probabilistic algorithm analysis + combinatorial generation

---

## 2. Assessments

**6 exams** (one per block), replacing the current 2 Phase 5 exams:

| Exam | Block | Covers | Replaces |
|------|-------|--------|----------|
| Exam 5A: Discrete Mathematics | A | Lessons 67–71 | — |
| Exam 5B: Computability & Complexity | B | Lessons 72–76 | old exam-5a-computability-algebra (partial) |
| Exam 5C: Formal Logic | C | Lessons 77–79 | old exam-5b-topology-logic (partial) |
| Exam 5D: Abstract Algebra | D | Lessons 80–84 | old exam-5a-computability-algebra (partial) |
| Exam 5E: Geometry for Alignment | E | Lessons 85–89 | old exam-5b-topology-logic (partial) |
| Exam 5F: Advanced Algorithms | F | Lessons 90–94 | — |

**Files to create (12 files):**
- exam-5a-discrete-math.qmd + exam-5a-discrete-math-answer-key.qmd
- exam-5b-computability-complexity.qmd + exam-5b-computability-complexity-answer-key.qmd
- exam-5c-formal-logic.qmd + exam-5c-formal-logic-answer-key.qmd
- exam-5d-abstract-algebra.qmd + exam-5d-abstract-algebra-answer-key.qmd
- exam-5e-geometry-alignment.qmd + exam-5e-geometry-alignment-answer-key.qmd
- exam-5f-advanced-algorithms.qmd + exam-5f-advanced-algorithms-answer-key.qmd

(PDFs are build artifacts generated from .qmd — not tracked as created files.)

**Files to delete (8 files):**
- exam-5a-computability-algebra.qmd + .pdf (2)
- exam-5a-computability-algebra-answer-key.qmd + .pdf (2)
- exam-5b-topology-logic.qmd + .pdf (2)
- exam-5b-topology-logic-answer-key.qmd + .pdf (2)

---

## 3. Downstream Renumbering

### Phase 6: Alignment Theory (lessons 80–84 → 95–99)

| Old | New | File Rename |
|-----|-----|-------------|
| lesson-80-game-theory.md | lesson-95-game-theory.md | yes |
| lesson-81-decision-theory.md | lesson-96-decision-theory.md | yes |
| lesson-82-anthropics.md | lesson-97-anthropics.md | yes |
| lesson-83-alignment-problem.md | lesson-98-alignment-problem.md | yes |
| lesson-84-open-problems.md | lesson-99-open-problems.md | yes |
| lesson-84a-alignment-capstone-project.qmd | lesson-99a-alignment-capstone-project.qmd | yes |
| lesson-84a-alignment-capstone-project.pdf | DELETE (regenerate from renamed .qmd) | yes |
| PHASE-6-OVERVIEW.md | PHASE-6-OVERVIEW.md | content update only |

Phase 6 assessments (filenames stay, content references update):
- exam-6a-rational-agency.qmd: currently covers "Lessons 80–83" → update to "Lessons 95–98"
- exam-6a-rational-agency-answer-key.qmd: same update
- exam-6b-alignment-capstone.qmd: currently covers "Lessons 80–84" → update to "Lessons 95–99" (full phase capstone, all Phase 5 cross-references also updated)
- exam-6b-alignment-capstone-answer-key.qmd: same update

### Phase 7: Independent Research

- research-guide.md: fix stale navigation link `lesson-70-open-problems.md` → `lesson-99-open-problems.md` (pre-existing bug — currently points to nonexistent file)
- No file renames needed (no numbered lessons)

### Old-to-New Lesson Number Quick Reference

For use when updating assessment cross-references:

| Old # | Old Topic | New # |
|-------|-----------|-------|
| 67 | Turing Machines | 74 |
| 68 | Computational Complexity | 76 |
| 69 | Kolmogorov Complexity | 75 |
| 70 | Groups | 80 |
| 71 | Rings/Fields | 83 |
| 72 | Group Actions | 84 |
| 73 | Point-Set Topology | ~85 (partial) |
| 74 | Homotopy | DELETED (out of scope) |
| 75 | Manifolds | 87 |
| 76 | Algebraic Geometry | 89 |
| 77 | Propositional Logic | 77 |
| 78 | Godel/Lob | 79 |
| 79 | Differential Forms | 88 |
| 80 | Game Theory | 95 |
| 81 | Decision Theory | 96 |
| 82 | Anthropics | 97 |
| 83 | Alignment Problem | 98 |
| 84 | Open Problems | 99 |

---

## 4. CS Foundations Changes

**Remove from phase0-cs-foundations:**
- lesson-cs09-discrete-math.md (content absorbed into Block A, lessons 67–71)

**Keep in phase0-cs-foundations:**
- advanced-theoretical-cs.md (reference document, still useful as a map)
- algorithm-classification.md (LeetCode-style patterns, separate concern from Knuth-style Block F)

**Update:**
- README.md cs_foundations section: remove discrete math lesson reference

---

## 5. Infrastructure File Updates

### README.md
- Rewrite Phase 5 section with 6 blocks (matching Phase 2 format: `### Block X: Topic (##–##) — Source`)
- Renumber Phase 6 lesson table (95–99)
- Update Phase 7 if any numbered references
- Update Assessments table (remove old 5A/5B, add 5A–5F, update 6A/6B lesson ranges)
- Remove discrete math from cs_foundations section

### curriculum-dashboard.html
- Rewrite Phase 5 lesson data (28 lessons across 6 blocks with phase 'p5')
- Ensure strict sequential ordering (67–94) — current dashboard has lesson 79 out of order between 75 and 76; do not replicate this anomaly
- Add checkpoint per block or one at end
- Shift Phase 6 lesson IDs (80–84 → 95–99)
- Update prerequisite chains

### sr-data.js
- Rewrite Phase 5 spaced repetition entries for new 28-lesson structure

### JSON data files
The following files may contain lesson number references or Phase 5-related progress data:
- daily-plan.json
- calendar-data.json
- pace-data.json
- hours-log.json
- sr-progress.json
- ms-progress.json

**Policy:** These are runtime/progress tracking files. Since all Phase 5 lessons are currently "Not Started", any Phase 5 entries in these files can be safely cleared or left as-is (they'll be orphaned but harmless). Phase 6 entries should be checked — if any reference lesson numbers 80–84, update to 95–99.

### full-overview/full-concept-overview.md
- Rewrite Phase 5 section (6 blocks, 28 lessons)
- Update any Phase 6 lesson number references

### resources/video-index.md
- Rewrite Phase 5 video mappings with new resources:
  - Trefor Bazzett Discrete Math
  - Neso Academy Theory of Computation
  - Trefor Bazzett Logic
  - Macauley Visual Group Theory
  - What is Math Differential Geometry
  - Curated individual videos for Advanced Algorithms
- Update supplement references (eigenchris, Michael Penn, etc.)

### resources/cheat-sheet.md
- Update Phase 5 section header and lesson range (67–94)

### resources/intuition-notebook.md
- Update Phase 5 placeholder text and lesson range

### Spaced repetition app files
- spaced-repetition-app.html and SpacedRepetitionWeb.py: these are consumers of sr-data.js. No changes needed beyond the sr-data.js update.
- math-symbols-flashcards.html and MathSymbols.py: unrelated to Phase 5 content, no changes needed.

### Navigation links (cross-phase)
- phase4-machine-learning/lesson-66-interp-slt.md: "Next" link → lesson-67 (same number, new content — title changes)
- phase6-alignment/lesson-95-game-theory.md: "Prev" link → lesson-94 (was pointing to lesson-78)

### Capstone assessments (content updates)
- exam-6b-alignment-capstone.qmd + answer key: update all Phase 5 concept references and lesson numbers per quick reference table in Section 3
- final-project-alignment-observatory.qmd: update Phase 5 lesson ranges and topic references
- capstone-comprehensive-project.qmd: update Phase 5 references
- refresher-quizzes-phases-0-6.qmd: rewrite Phase 5 quiz section entirely (new topics)

---

## 6. Files in Phase 5 Directory

### Files to delete (old structure)
All 22 existing files in phase5-math-enrichment/:
- PHASE-5-OVERVIEW.md (1)
- lesson-67 through lesson-79 (.md files) (13)
- lesson-69a, 72a, 76a, 78a coding projects (.qmd + .pdf each) (8)

### Files to create (new structure)
- PHASE-5-OVERVIEW.md (rewritten) (1)
- 28 lesson files: lesson-67 through lesson-94 (.md) (28)
- 5 coding project files: lesson-71a, lesson-76a, lesson-84a, lesson-89a, lesson-94a (.qmd) (5)
- 12 assessment files in assessments/ (6 exams + 6 answer keys) (12)

Total new files: 46

---

## 7. Content Migration Notes

Some existing Phase 5 lesson content maps to new lessons and should be refactored rather than written from scratch:

| Old Lesson | New Lesson | Action |
|------------|------------|--------|
| 67 (Turing Machines) | 74 (Turing Machines) | Refactor — similar scope |
| 68 (Complexity) | 76 (Complexity) | Refactor — expand scope |
| 69 (Kolmogorov) | 75 (Kolmogorov) | Refactor — similar scope |
| 70 (Groups) | 80 (Groups) | Refactor — restructure around Macauley |
| 71 (Rings/Fields) | 83 (Rings/Fields) | Refactor |
| 72 (Group Actions) | 84 (Group Actions) | Refactor |
| 73 (Point-Set Topology) | 85 (Curves/Surfaces) | Partial overlap — rewrite |
| 74 (Homotopy) | — | DELETE — homotopy/fundamental groups deemed out of scope for alignment-focused curriculum. Covering spaces and Morse theory not needed. |
| 75 (Manifolds) | 87 (Manifolds) | Refactor |
| 76 (Algebraic Geometry) | 89 (Algebraic Geometry) | Refactor |
| 77 (Propositional Logic) | 77 (Propositional Logic) | Refactor — same number |
| 78 (Godel/Lob) | 79 (Godel/Lob) | Refactor |
| 79 (Differential Forms) | 88 (Differential Forms) | Refactor |

**New content (no existing equivalent):**
- Lessons 67–71 (Discrete Math — entirely new block)
- Lessons 72–73 (Automata/CFGs — new)
- Lesson 78 (Proof Systems — new)
- Lessons 80–82 (Algebra detail — expanded from old 2 lessons to 3 new lessons covering Cayley diagrams, cosets/Lagrange, homomorphisms/quotients)
- Lesson 86 (Tangent Spaces/Curvature — new standalone)
- Lessons 90–94 (Advanced Algorithms — entirely new block)
