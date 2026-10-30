# Local check log

Date: 2026-10-30 UTC

## Dependency-free checks

The same logic committed in `verify_m89_pivot_matching.py` was run in the available Python runtime.

```text
m=8: scalar_states=79, x=[8,23], y=[0,24], z=[0,12]
m=9: scalar_states=61, x=[13,25], y=[0,19], z=[0,9]
mu_4(t): [4, 6, 8, 8, 10, 10, 12, 12, 12, 13, 13, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16]
matching_composition_local_obstruction_cases: 2304
source_profiles: x in O -> 11 single-outside witnesses;
                x in H two-double -> 10; x in H triple -> 11
m=8 canonical color vector sum=1830
m=9 canonical color vector sum=1830
```

Result: all local checks passed.

Additional independent local check: the 2,304 local matching-composition obstruction cases were rebuilt explicitly as 12-vertex graphs; in each case the missing composed edge creates an independent 5-set. The μ4(t) table was re-enumerated over all 65,536 K4,4 edge sets.

A guarded-cut audit found and repaired an earlier overconstraint: composition edges and multi-projection capacities are now implications guarded by the same selected pivot blocks and both incident pairs remaining exactly four-edge pairs.

The source-core exact accounting and conditional 69/70 near-Turan partition constraints were added. The partition constraints now apply to all eleven non-target colors. The independent verifier reconstructs the 11K4+K3 partition from the color graph for every low-layer candidate, then checks source-witness alignment for exact colors. These additions were statically inspected; the full solver and full candidate verifier have not been run.

## Full solver

```text
Python import check: ModuleNotFoundError: No module named 'z3'
```

The full CSP was not run. No solver version, SAT/UNSAT output, proof log, or full candidate is available. No UNSAT certificate is claimed.


## All-color near-Turan orthogonality strengthening

The conditional 69/70 partition variables and independent reconstruction now apply to all eleven non-target colors. Whenever two colors are both in the 69/70 layer, their 12-partitions are pairwise orthogonal: no two H-vertices may share a part in both partitions. This is encoded explicitly in the solver and replayed by the independent verifier.

The partition-code consequence was checked analytically: k simultaneous low-layer partitions give 47 codewords over 12 symbols with pairwise agreement at most one, and the exact agreement count yields 69k<=1081 (k<=15). This does not exclude k<=11, so it is recorded as a structural constraint, not a closure.


## Staged-verifier overconstraint repair

The independent verifier's source-only pass is called with alpha/omega checks disabled so the solver can add lazy validity cuts to provisional models. A final audit found that the pivot matching, residual-neighbor, near-Turan, and Turan-floor checks depend on alpha hypotheses and therefore must not run in that first pass. All such checks are now guarded by check_alpha; the 130/131 degree floors and reserve caps remain guarded by both check_alpha and check_omega. Source-only checks continue to validate exact edge ownership, Type-I factors, canonical counts, target-core degrees, full support, witness linearity, and source-derived gap bounds.

No SAT/UNSAT computation has been run.


## Low-layer source localization and matching skeleton

Added the conditional special-gadget localization theorem. In x-in-H low-layer exact colors, the Nt factor must be the overfull factor (occupancy 2 in two-double, 3 in triple), y must be outside H, the Nt H-interior shares x's near-Turan part, and at most one H vertex of Ns\A0 remains. The core count becomes exactly 69 plus this residual Ns count. For x outside H, the unique double K3 is aligned and the core excess is exactly the y--A0 H-intersection count.

The solver implications were inserted inside the per-exact-color near-Turan loop. An indentation audit caught and repaired an initial placement inside the pairwise-orthogonality loop before this commit; the final code scopes all xvar/comp/a0 constraints to the exact-color loop.

The independent verifier adds the corresponding source-part checks under check_alpha, so the provisional source-only pass is not strengthened by alpha-dependent conclusions.

A separate Hall argument proves a 253-edge target matching skeleton for any low-layer partition. The 32-edge residual has 36 baseline degree-1 vertices and 11 baseline degree-2 vertices, with only six total excess units; at least 30 residual vertices are leaves. This skeleton is not yet encoded with explicit matching-choice variables.


## Static syntax check for source-localization patch

The newly inserted solver and verifier blocks were separately reconstructed from the committed source and parsed with Python's AST parser. Both snippets passed. This is only a syntax check of the inserted blocks; the complete files were not executed or fully imported. The runtime still lacks z3-solver, so no m=8/9 solver execution, SAT/UNSAT result, or proof log is available.


The 32-edge residual decomposition was sharpened. If q of the 36 baseline-degree-11 vertices receive positive excess and t is the number of isolated K2 components, then the residual has exactly 36-q leaves, a core of 11+q vertices, and exactly q+t-4 edges inside that core. In particular q+t>=4 and the core has at most17 vertices. The degree-sum derivation is recorded in MATH_PROOF.md §9.6; it is analytic only and is not yet a solver cut.


## Tight-part K7 theorem and 71-edge floor

Proved that any 11K4+K3 partition of H forces alpha(H)>=5 or omega(H)>=7. The Hall matching skeleton has 253 edges and leaves 32 residual edges. The part-degree ledger yields at least five tight 4-parts; one tight part has three F-leaves. Their unique F-neighbors can dirty at most three of the ten other 4-parts, leaving seven clean parts. Each clean part contributes a fourth vertex nonadjacent to the three leaves. Any two such fourth vertices must be adjacent under alpha(H)<=4, producing K7.

Consequently the registered 69/70 near-Turán layer is impossible for every non-target color, so \(e_C(H)\ge71\) for all eleven colors and the 37-unit ledger has only 15 units of slack above this floor.

The solver now asserts core_edges[c]>=71 and removes the dead conditional near-Turán partition variables. The verifier independently replays the Hall matching/tight-part witness and checks the 71-edge floor when both alpha and clique premises are enabled. This does not claim m=8/9 closure; 71+ remains open.


## Analytic Type-I partition obstruction closes m=8 and m=9

The source-verified exact-129 Type-I factorization forces one of three partitions of H:
- x outside O: 11 independent 4-sets plus one independent 3-set;
- x in H, two-double profile: 10 independent 4-sets, two independent 3-sets, and x;
- x in H, triple profile: 11 independent 4-sets, one independent 2-set, and x.

For each shape, choose Hall matchings between all 4-parts, saturating matchings from each 4-part to each smaller part, and one edge from each 4-part to a singleton if present. The matching skeleton has respectively 253, 250, or 253 edges. The residual F-degree ledger has total excess exactly six above the partwise lower bounds, so at least r-6 four-parts are tight. In a tight part the three lowest-F-degree vertices have total residual degree at most three, leaving at least six clean four-parts. Their fourth vertices form either an independent-5 witness with the selected triple or a clique of size at least six. Both contradict the H-core premises.

Therefore every exact-129 Type-I color is impossible. m=8 and m=9 both require such colors, so both full-support Q32 branches are analytically excluded. This supersedes the previous 71+ edge-distribution search. The full SMT model was not run and no solver UNSAT certificate is claimed.

The independent verifier now reconstructs each source-induced partition, replays the Hall/tight-part argument with augmenting paths, and checks the explicit witness. Synthetic self-tests cover all three partition shapes.


## 2026-10-30 critical premise audit — previous closure withdrawn

The actual EG617 counterexample is a balanced coloring: every 13-set contains all 12 colors. Thus each color C has alpha(C)<=12 and omega(C)<=12; K6 is not forbidden. The target 47-core lies in R(4,49), so omega(H)<=11, not five.

The previous Type-I partition replay was conditional on a source factorization not proved for every exact color under these hypotheses. The exact-129 source audit's non-12-partite and size-six exclusions used omega(C)<=5. A 12-partite local example C0=5K6 dot-union 3K5 dot-union 4K4 has n=61, e=129, alpha=12, omega=6, and complement 12-partite.

The tight-part helper remains a valid conditional implication but returns K6/K7 witnesses that are allowed in EG617. The previous verifier's default omega check, Type-I universal source assumption, and 71-edge floor are not valid for the original problem. The verifier was changed so omega checking is opt-in via --check-omega and its result is explicitly labelled Type-I-restricted. The solver is now labelled as an augmented Type-I/K6-free diagnostic and defaults to OPEN.

No full verifier execution or SMT run was performed. No m=8/9 closure or parent promotion is claimed.


## 2026-10-30 continued research — source-complete exact-129 repair

A stronger result was proved after the K6-free retraction:

1. **Universal H-partition:** every exact-129 color induces one of 11K4+K3, 10K4+2K3+K1, 11K4+K2+K1. The proof handles both a 12-partite complement and all three non-12-partite Kang–Pikhurko equality profiles; it does not assume Type I or omega(C)<=5.
2. **Core-edge bounds:** every exact color has 69<=e_C(H)<=75. The 12-partite branch has at most four cross-partition C-edges; the nonpartite branch is handled by the exact gadget formula for x/y placements.
3. **Witness interface:** every exact color supplies at least ten disjoint core K4 witnesses, pairwise linear across colors. This is a source-complete replacement for the ten-witness input used in Q32_U_COLOR_RESERVE.md.
4. **Boundary:** the Hall/tight-part lemma still only forces omega(H)>=6; this is allowed by omega(H)<=11. The new theorem does not close m=8/9. It does not provide a special point or a fixed-pivot K4 in the 12-partite complement branch, so the current pivot CSP remains restricted and incomplete.

The Kang–Pikhurko source card was checked against the published statement: Theorem 1 gives p_12(61)=1701; the equality construction has twelve parts plus special x; Theorem 4 gives all extremizers and Lemma 5 gives the three part-size profiles. The original Problem 617 statement confirms the balanced counterexample condition is every 13-set containing all 12 colors, not K6-freeness.

No full SMT run or full verifier execution was performed. No Q32 closure or root promotion is claimed.
