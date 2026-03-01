# Exam 5B: Topology and Formal Logic — Answer Key

**The Path to AI Alignment — Lessons 57–62 Comprehensive Assessment**

---

### Question 1 (10 pts)

**(a)** (0,1): **open** (every point has a neighborhood inside it). [0,1]: **closed** (contains all its limit points, complement is open). [0,1): **neither** (0 has no open neighborhood inside it → not open; 1 is a limit point not in the set → not closed).

**(b)** A set K is **compact** if every open cover has a finite subcover (equivalently, every sequence has a convergent subsequence with limit in K). **Heine-Borel:** a subset of ℝⁿ is compact if and only if it is **closed and bounded**.

**(c)** **Extreme value theorem:** if f is continuous on a compact set K, then f attains its maximum and minimum on K — there exist points where f achieves its greatest and least values. Optimization is guaranteed to have a solution.

**(d)** ℝᵈ is unbounded, so not compact. Parameters could drift to infinity without the loss achieving a minimum. **Weight decay** adds λ‖W‖² to the loss, which grows to infinity as ‖W‖ → ∞. This effectively restricts optimization to a bounded region (the sublevel sets become bounded), recovering a compact domain where the extreme value theorem applies.

---

### Question 2 (10 pts)

**(a)** A space is **connected** if it cannot be written as the union of two non-empty, disjoint open sets. Intuitively: it's "one piece" — you can walk between any two points without leaving the space.

**(b)** {x : x² < 4} = (−2, 2): **connected** (it's a single interval). {x : x² > 4} = (−∞, −2) ∪ (2, ∞): **disconnected** (two disjoint open intervals, separated by [−2, 2]).

**(c)** Connected: gradient descent can potentially move between any two minima through continuous weight changes staying in the minimum set. Disconnected: different minima are "isolated" — training from different initializations may converge to qualitatively different solutions in separate components, and there's no continuous path between them through the minimum set.

**(d)** Not necessarily. Even in a connected minimum set, gradient descent follows the negative gradient, which may not point along the path connecting the minima. The trajectory depends on the full loss landscape, not just the topology of the minimum set. Saddle points and ridges can block gradient-based paths even when a topological path exists.

---

### Question 3 (10 pts)

**(a)** A homotopy between maps f, g: X → Y is a continuous map H: X × [0,1] → Y with H(x,0) = f(x) and H(x,1) = g(x). It continuously deforms f into g. Two paths are homotopic if one can be continuously deformed into the other while keeping the endpoints fixed.

**(b)** (i) π₁(ℝ²) = **{e}** (trivial) — every loop in ℝ² can be shrunk to a point. (ii) π₁(S¹) = **ℤ** — loops classified by winding number (how many times they wrap around). (iii) π₁(T²) = **ℤ × ℤ** — two independent winding numbers (one for each "hole" of the torus).

**(c)** A hole in S_ε means there exist loops in weight space (at loss ≤ ε) that cannot be contracted. For optimization, this means the sublevel set "wraps around" an obstacle — there could be regions of high loss completely surrounded by low-loss regions, creating "pockets" that trap or redirect gradient flow.

**(d)** The topology of S_ε changes exactly at critical values ε = L(W*) where W* is a critical point. As ε increases past a local minimum, a new connected component appears (handle attachment). As ε passes a saddle point, components merge. This Morse-theoretic picture connects the critical point structure of L (Hessian eigenvalues) to the topology of its sublevel sets.

---

### Question 4 (10 pts)

**(a)** A smooth manifold is a space that **looks locally like ℝⁿ** — every point has a neighborhood with a smooth coordinate system, but globally the space may be curved. Examples: the surface of a sphere (locally flat maps, globally curved), the surface of a donut (torus).

**(b)** T_pM is the vector space of all "velocity vectors" of curves passing through p on M. It's the best linear approximation to M at p. Useful for optimization because the gradient must live in the tangent space — on a curved space, "steepest descent" means "steepest descent within the tangent plane," which requires knowing T_pM.

**(c)** Singularities occur where the **stabilizer is non-trivial** — at weight configurations with extra symmetry (e.g., two or more neurons with identical weights, or a neuron with zero weights). At these points, the orbit is smaller than generic orbits, so the quotient space "pinches" — it's not locally Euclidean and fails to be a manifold.

**(d)** Project the Euclidean gradient onto the tangent space T_pM, then follow this projected gradient along the manifold (via the exponential map or retraction). The curvature of the space is encoded in the Riemannian metric, which defines inner products on each tangent space.

---

### Question 5 (12 pts)

**(a)** An algebraic variety is the set of common zeros of a collection of polynomial equations: V = {x : f₁(x) = ... = fₖ(x) = 0}. Smooth example: the unit circle V = {x² + y² − 1 = 0}. Singular example: the cusp V = {y² − x³ = 0} (singular at origin).

**(b)** **Jacobian criterion:** compute the Jacobian matrix J of the defining polynomials. A point is **smooth** if J has full rank there; **singular** if J drops rank.

**(c)** (i) y² − x² = (y−x)(y+x) = 0: two crossing lines. Jacobian (−2x, 2y) = (0,0) at origin. This is a **node** — two branches crossing transversally. (ii) y² − x³ = 0: Jacobian (−3x², 2y) = (0,0) at origin. This is a **cusp** — one branch with a sharp point.

**(d)** For the node y² − x² = 0, substitute y = tx (blow-up in one chart). Then t²x² − x² = x²(t² − 1) = 0. The strict transform (removing the factor x² from the exceptional divisor) is t² − 1 = 0, giving t = ±1 — **two separate points** on the exceptional divisor. The crossing lines have been separated into two parallel lines on the blown-up surface. Yes, the singularity is **resolved** — the blown-up variety is smooth.

**(e)** f(w) = w⁶. The integral ∫₀¹ w^{−6t} dw = [w^{1−6t}/(1−6t)]₀¹ converges iff 1 − 6t > 0, i.e., t < 1/6. The pole is at t = 1/6, so **RLCT λ = 1/6**. Compare with regular value d/2 = 1/2. The singularity (a very flat minimum) reduces effective complexity by 3×.

---

### Question 6 (10 pts)

**(a)** Permutation symmetry → **singularities in weight space** (many-to-one parameter map) → **blow-up resolution** (resolve singularities to smooth varieties) → **normal crossing form** (the loss in resolved coordinates factors as a product of powers) → **RLCT** (computed from the exponents in the normal crossing form).

**(b)** λ = 1/2 vs. d/2 = 1 means the model has **half the effective complexity** predicted by parameter counting. The singularity (two crossing zero-directions in the loss landscape) reduces the effective degrees of freedom. In the free energy formula F ≈ λ log n, using λ = 1/2 instead of d/2 = 1 predicts better generalization — the model effectively has 1 "real" parameter's worth of complexity despite having 2 actual parameters.

**(c)** SLT's core technique requires integrating over the loss landscape near singularities. On a singular variety, standard integration tools fail. Hironaka's theorem guarantees you can ALWAYS resolve the singularities to a smooth variety via blow-ups, where standard calculus works. Without this guarantee, SLT would only apply to specific singularity types — with it, the theory is universal.

---

### Question 7 (10 pts)

**(a)** Let D = "model is deceptive," B = "passes behavioral tests," I = "interpretability is necessary."
**(D ∧ B) → I**

**(b)** Truth table for (P → Q) ∧ (¬Q):

| P | Q | P→Q | ¬Q | (P→Q) ∧ (¬Q) |
|---|---|---|---|---|
| T | T | T | F | **F** |
| T | F | F | T | **F** |
| F | T | T | F | **F** |
| F | F | T | T | **T** |

This simplifies to **¬P ∧ ¬Q** (both P and Q are false). It's the logical basis of *modus tollens*: if P implies Q and Q is false, then P must be false.

**(c)** ∀x [Harmful(Model(x)) → Catches(SafetyFilter, x)]

**(d)** ¬∃x [Harmful(Model(x)) ∧ ¬Catches(SafetyFilter, x)]
Or equivalently: ∀x [Harmful(Model(x)) → Catches(SafetyFilter, x)]
(These are logically equivalent by De Morgan's laws for quantifiers.)

---

### Question 8 (10 pts)

**(a)** Any consistent formal system powerful enough to express basic arithmetic contains true statements that cannot be proven within the system. No such system is both complete (proves all truths) and consistent (proves no falsehoods).

**(b)** G says "I am not provable." If G were false, then G IS provable, and since the system only proves truths (consistency), G would be true — contradiction. So G must be **true**. But if G is true, it's not provable (that's what it says). So G is **true but unprovable**.

**(c)** No consistent formal system powerful enough to express arithmetic can prove its own consistency. A system cannot prove "I will never derive a contradiction."

**(d)** If an AI uses formal logic: (1) There will be true safety-relevant statements it cannot prove (first theorem). (2) It cannot prove "my reasoning system is consistent" — it can't guarantee its own logical foundations are sound (second theorem). This means an AI cannot provide complete self-certification of safety using its own reasoning framework. External verification or different logical frameworks are necessary.

---

### Question 9 (10 pts)

**(a)** If a system can prove "□P → P" (if I can prove P then P is true), then the system can already prove P. Symbolically: if ⊢ (□P → P), then ⊢ P.

**(b)** The Löbian obstacle: an AI system might try: "If I can prove I'm safe (□Safe), then I am safe (Safe)." Löb's theorem says: if the system can prove this conditional (□Safe → Safe), then the system can prove Safe outright. But the system CAN'T prove Safe outright (the whole point is that safety is hard to establish). So the system also can't prove the conditional □Safe → Safe. The bootstrap fails — you can't go from "my proofs are trustworthy" to "I'm safe" without already knowing you're safe.

**(c)** System A needs to verify: "If B can prove B is safe, then B IS safe" (□_B Safe_B → Safe_B). But by Löb's theorem applied to B's proof system, this would require that B can already prove its own safety. The same applies in reverse for B verifying A. Neither system can establish trust in the other's safety proofs without already having the very guarantee they're trying to establish. It's a circularity that Löb's theorem makes precise.

**(d)** If multiple AI systems need to coordinate safely (e.g., during deployment), they need to establish mutual trust in each other's safety properties. Löb's theorem is the precise barrier to naive approaches. Workarounds — using different logical frameworks, probabilistic trust, or shared commitment mechanisms — are essential for multi-agent alignment scenarios.

---

### Question 10 (8 pts)

**(a)**
- **Permutation symmetry → singularity:** S_n acting on weight space creates orbits; where stabilizers are non-trivial (neurons identical/zero), the parameter-to-function map is many-to-one, creating singularities.
- **Singularity → blow-up resolution:** Hironaka's theorem guarantees we can replace each singularity with smooth geometry by introducing new "directional" coordinates that separate crossing branches.
- **Resolution → RLCT computation:** in blow-up coordinates, the loss takes normal crossing form (products of powers), and the RLCT is computed as the minimum ratio of (Jacobian exponent + 1) / (2 × loss exponent) over all exceptional divisors.
- **RLCT → free energy:** the RLCT λ plugs into F ≈ λ log n − (m−1) log log n, replacing the classical d/2 and giving the correct complexity penalty for singular (neural network) models.

**(b)** The algebraic geometry thread (singularities, RLCT) tells us **what models learn and why they generalize** — it provides the complexity measure that explains how overparameterized networks work and potentially predicts capability emergence. The logic thread (Gödel, Löb) tells us **what we can and cannot prove about AI systems** — the fundamental limits on self-verification and formal safety guarantees. Both are necessary because alignment requires both UNDERSTANDING models (what they've learned, whether it's safe) AND VERIFYING models (proving safety properties hold). The first requires geometry; the second runs into logical barriers that define the boundaries of what formal methods can achieve.
