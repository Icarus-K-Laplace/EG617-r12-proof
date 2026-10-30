# Model validation and overconstraint audit

## Source audit

| Item | Result | Status |
|---|---|---|
| 61-point edge variables and unique edge ownership | Present | PROVED_CONDITIONAL |
| Exact color counts 408 / 129 / 130 / 131 | Correct vector in both m cases | PROVED_CONDITIONAL |
| Twelve Type-I K5 factors per exact color | Present | PROVED_CONDITIONAL |
| All legal outside profiles | Sum and caps imply exactly the three permitted profiles | PROVED_CONDITIONAL |
| Special-factor single-outside witnesses | Allowed; no factor-index restriction | PROVED_CONDITIONAL |
| At least ten witnesses per exact color | Follows from profiles; now explicitly checked by verifier | PROVED_CONDITIONAL |
| Cross-color pairwise linearity | Follows from unique edge ownership; now explicitly checked | PROVED_CONDITIONAL |
| Full support U=H | Explicit coverage constraints and verifier | PROVED_CONDITIONAL |
| alpha(H)<=4, alpha(G_C)<=12, omega(G_C)<=5 | Lazy exact separation and independent verifier | PROVED_CONDITIONAL |
| Reserve caps | Uses unconditional (4,5,5); stronger caps only conditional | PROVED_CONDITIONAL |

## New m=8/9 strengthening

1. Pairwise perfect-matching existence is forced by exact alpha(H) separation and independently recomputed by the candidate verifier; no redundant matching-choice variables are added.
2. Pointwise neighbor constraints for each pivot vertex against every other pivot block.
3. Exact per-block degree ledger `X_i+Y_i=5+epsilon_i`.
4. Lazy light-pair matching-composition cuts.
5. Multi-projection edge lower bounds using the independently enumerated `mu_4(t)` table.
6. Independent candidate verifier now recomputes perfect matchings, uniqueness of light pairs, all forced compositions, per-block ledgers, residual-to-pivot neighbor counts, witness counts, and cross-color linearity.

These additions are consequences of the frozen source contract and alpha(H)<=4; they do not force any special-factor placement.

## Common-P applicability audit

The inspected `V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM.md`, `V47_T0_POINTWISE_COLOR_SATURATION.md`, and `V47_Z01_SHARED_P_FACTOR_PACKING.md` are part of the aligned m=10 3+7 track cell. They do not establish an m=8/9 track partition. Their six common-P factors and residual-signature rules are therefore not used here.

## Execution status

The dependency-free local verifier for scalar arithmetic, source profiles, the matching-composition cases, and the K4,4 lookup table passed. The full Z3 solver was **not run**: the available Python runtime has no `z3-solver` module. No solver version, SMT run, SAT candidate, UNSAT proof, or proof replay is claimed.

## Invalid shortcuts explicitly rejected

- **WITHDRAWN:** `delta(H[R])>=12-m` without controlling extra Q-R edges.
- **WITHDRAWN:** `d_H(q,R)>=13-m` without controlling extra Q-Q edges.
- **WITHDRAWN for m=8/9:** importing the aligned m=10 common-P and residual-signature constraints.


## Additional 2026-10-30 audits

### Guarded matching-composition cuts

A code audit found that the first lazy matching-composition implementation added unconditional consequences inferred from one candidate model. That was an overconstraint: a future legal model could make one incident pivot pair heavy or change the selected pivot blocks. **WITHDRAWN:** those unconditional cuts.

The solver now adds only implications guarded by:
- both incident pivot-pair edge counts remaining exactly four;
- the same four vertices remaining selected in each of the three pivot blocks;
- the same four matching edges remaining target-colored.

The multi-projection \(\mu_4(t)\) cut is guarded by the conjunction of the distinct matching-composition conditions. This preserves validity under changes of source placement and pivot blocks.

### Exact source-core and near-Turan strengthening

The solver now encodes the exact identity \(e_C(H)=B_C+G_C^H\), the source-parameter bounds for x in O / two-double / triple profiles, and the conditional 69/70 partition normal form. The independent verifier reconstructs a \(11K_4+K_3\) partition from the source witnesses whenever \(e_C(H)\le70\), and checks its cross-edge count.

### Nonexact m=9 floor reconciliation

The model uses the source-correct pointwise floors 4 for a 130-edge color and 3 for a 131-edge color, hence \(L_9=7\). The root global canonical/dependency summaries still contain an older \(L_9=6\) line; the read-only Case-II canonical/dependency audit explicitly marks 6 as stale and records \(4+3=7\). No root-side file was modified.


## 69/70 theorem scope expansion

The conditional near-Turan partition is now encoded for **all eleven non-target colors**, not only exact colors. This is valid because every non-target color C has alpha(C[H])<=12 and omega(C[H])<=4. The independent verifier reconstructs the 11K4+K3 partition from C[H] itself: take connected components in the 69-layer, or delete the unique cross-part edge and take components in the 70-layer. For exact colors it additionally checks that each source single-outside witness K4 is one of the size-four parts.

This expansion adds necessary conditions only; no color is forced into the 69/70 layer.


## Pairwise orthogonality of low-layer partitions

When two non-target colors both have 69 or 70 H-edges inside H, their reconstructed 11K4+K3 partitions have intersections of size at most one in every pair of parts. The solver now states this explicitly for every pair of H-vertices and low-layer color pair; the independent verifier replays the same no-common-2-set condition. This is implied by unique edge ownership but is exposed as a direct global cut.


## Staged verifier audit

The candidate verifier has two phases in the solver loop: a source/model-integrity pass with alpha/omega checks disabled, followed by a full mathematical replay after lazy cuts stop. A further audit identified that several consequences of alpha(H)<=4 had initially been checked during the source-only phase. This could misclassify a provisional alpha-invalid model as a model-encoding failure.

Repaired: the verifier now guards all alpha-dependent checks behind check_alpha, including:
- Turan's e_C(H)>=69 floor;
- the pivot-pair perfect-matching and matching-composition replay;
- the residual-to-pivot neighbor lower bound and nonnegative reserve slack;
- the 69/70 near-Turan partition reconstruction and pairwise orthogonality.

The two-double source lower bound is checked as 72-a in the source-only pass and strengthened to max(69,72-a) only after alpha(C)<=12 is verified. The source-derived upper bounds remain checked unconditionally. Nonexact degree floors and safe/conditional reserve caps remain guarded by both alpha and omega checks.

This prevents an invalid provisional candidate from being mistaken for a defect in the source encoding.


## Source-triangle and special-gadget alignment audit

The full verifier now checks the exact low-layer source geometry after alpha premises are enabled:
- each double-outside factor's H-triangle is contained in one near-Turan part;
- x-in-H two-double/triple cases force the Nt occupancy to 2/3 respectively, y outside H, and the Nt H-interior into x's part;
- the Ns residual x-neighbor count is at most one and equals the core excess above 69;
- x-outside cases check the unique double K3 and the exact y--A0 core contribution.

The solver has matching implications. These constraints are necessary consequences of the one-cross-edge near-Turan structure and the source edge ownership, not imported m=10 alignment assumptions.


## Tight-part low-layer exclusion validation

The verifier includes an independent augmenting-path implementation of every Hall matching between the reconstructed 11K4+K3 parts. It forms M (253 edges), F (32 edges), finds a tight part with F-degree profile 1,1,1,2, identifies at least seven clean 4-parts, and returns either an explicit independent 5-set or a K7. The full alpha and clique checks independently validate the corresponding contradiction.

When both alpha and omega validation are enabled, every non-target color is also checked against the derived floor \(e_C(H)\ge71\). The solver uses this floor and no longer allocates dead 69/70 partition variables.


## Type-I source partition obstruction replay

The verifier reconstructs, for every exact color, the H-interiors of all twelve source K5 factors and appends the singleton {x_C} when x_C lies in H. The resulting sizes must be one of 11K4+K3, 10K4+2K3+K1, or 11K4+K2+K1.

The type_i_partition_obstruction_witness helper independently:
1. checks that the parts are independent and partition H;
2. finds each 4-by-4 perfect matching and each 4-by-(2 or 3) matching saturating the smaller part using augmenting paths, or returns a Hall-deficiency independent 5-set;
3. selects one edge from each 4-part to a singleton when present, or returns the resulting independent 5-set;
4. checks the exact matching-edge count (253/250), residual degree sum, and existence of at least r-6 tight 4-parts;
5. selects the three lowest-F-degree vertices in a tight part, finds at least six clean 4-parts, and returns either an independent 5-set or a clique of size at least six.

The self-test runs this replay on all three partition shapes using a synthetic 285-edge graph with minimum degree 12. The full candidate verifier invokes the replay for every exact color when the H-core edge and minimum-degree contract is met. This is a proof-replay check, not an SMT result.


## 2026-10-30 critical premise audit — previous closure withdrawn

The actual EG617 counterexample is a balanced coloring: every 13-set contains all 12 colors. Thus each color C has alpha(C)<=12 and omega(C)<=12; K6 is not forbidden. The target 47-core lies in R(4,49), so omega(H)<=11, not five.

The previous Type-I partition replay was conditional on a source factorization not proved for every exact color under these hypotheses. The exact-129 source audit's non-12-partite and size-six exclusions used omega(C)<=5. A 12-partite local example C0=5K6 dot-union 3K5 dot-union 4K4 has n=61, e=129, alpha=12, omega=6, and complement 12-partite.

The tight-part helper remains a valid conditional implication but returns K6/K7 witnesses that are allowed in EG617. The previous verifier's default omega check, Type-I universal source assumption, and 71-edge floor are not valid for the original problem. The verifier was changed so omega checking is opt-in via --check-omega and its result is explicitly labelled Type-I-restricted. The solver is now labelled as an augmented Type-I/K6-free diagnostic and defaults to OPEN.

No full verifier execution or SMT run was performed. No m=8/9 closure or parent promotion is claimed.


## Source-complete exact-color theorem validation

The new source theorem handles two branches: 12-partite complement directly, and non-12-partite complement by Kang–Pikhurko Theorem 1, Theorem 4, and Lemma 5. The three extremal part-size sequences were checked arithmetically:
- (5^12): internal part edges 120; gadget cross edges 9;
- (4,5^10,6): internal part edges 121; gadget cross edges 8;
- (4,4,5^8,6,6): internal part edges 122; gadget cross edges 7.

Each gives total C-edge count129. The outside-incidence deficit argument yields the three H-partition shapes. The separate core-edge theorem computes gadget edges in H by x/y placement and establishes 69<=e_C(H)<=75. These are analytic calculations; no full candidate/verifier or SMT run is claimed.
