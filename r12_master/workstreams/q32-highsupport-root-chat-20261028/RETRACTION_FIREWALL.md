# E408-Q32 retraction firewall

Date: 2026-10-28
Status: **ACTIVE / FAIL-CLOSED**

This workstream may not use any theorem whose load-bearing proof depends on the withdrawn universal KP degree-nine exceptional vertex or the derived exceptional-point injectivity.

## 1. Primary source correction

The source-correct exact-129 Type-I graph is

`10 isolated K5 dot-union G11`.

For source parameter `a in {1,2,3,4}`, the two variable gadget degrees are

`4+a` and `9-a`,

i.e. `(5,8),(6,7),(7,6),(8,5)`.

Therefore there is **no universal degree-nine exceptional vertex**.

The valid consequences retained in this workstream are the factorization, twelve K5 partition after deleting x, the exact nine gadget edges, and arguments re-derived directly from those statements.

## 2. Forbidden historical claims

The following may be read only as historical artifacts and may not be cited as active closure lemmas:

- `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md`;
- `Q32_EXACT_COLOR_COUNT_COLLAPSE.md`;
- the injectivity-dependent closure portion of `Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md`;
- `E408_WHOLE_LAYER_EXACT_COUNT_CLOSURE.md` as a Q32 whole-layer theorem;
- any root promotion that cites those results as closing E408-Q32;
- old `Q32_V45_TWOPOINT_REDUCTION.md` conclusions such as “at most three 11-witness colors” or “at most one exceptional outside H” when their proof uses exceptional injectivity.

A verifier script attached to a retracted statement does not revive the statement.

## 3. Explicitly invalid root-promotion artifact

`R12_ROOT_CLOSURE_PROMOTION_AUDIT.md` predates the fail-close and contains the withdrawn Q32 closure route. It must not be used for current status.

The newer `ROOT_PROMOTION_RECEIPT.md` is the controlling branch-local root receipt. It explicitly withdraws the old promotion and sets

`EG617(r=12) = OPEN / NOT_CERTIFIED`.

## 4. Safe replacements already used here

The following deductions were re-derived from source-correct Type-I structure and current minimum-degree theorems:

1. corrected non-full-support multiplicity
   `n_w>=m-6`;
2. latest nonexact degree floors
   `L8=12`, `L9=7`, `L10=3`;
3. m=8 exact parameters satisfy `a in {2,3}` from the exact three-unit pointwise surplus ledger;
4. in m=8 all variable points `{x_C,y_C}` are pairwise distinct;
5. Case-II v=45,m=8 and v=46,m=8 are closed by weighted special-incidence capacity, not by historical injectivity;
6. v=47 exact-color H-edge normal forms and the 69/70 near-Turan analysis use only the true Type-I factorization.

## 5. E407 firewall

The E407 U-reserve contradiction is allowed because its load-bearing inputs are:

- V12 survivor exhaustiveness under retained screen assumptions;
- the common `|U|=29`, 49-block support contract;
- selected-component color identity;
- edge uniqueness;
- `alpha(D)<=12`;
- Turan.

It does **not** use universal degree9 or exceptional injectivity.

The fact that the frozen five-template compatibility file was still OPEN is not a defect in this later closure: the U-reserve theorem bypasses template-by-template incompatibility once the common support contract is available.

## 6. Q33 firewall

The Q33 global nonexact-U-reserve route is allowed. It depends on the 284-edge / 31-point / 56-witness contract and component/gadget distinction, not on the false degree-nine statement and not on the Q32 excess-six identities.

## 7. Fail-closed policy for new work

For every proposed Q32 lemma:

- identify whether x, y, or a generic G11 vertex is being used;
- if a degree is used, derive it from `(4+a,9-a)` or the fixed degree-five gadget vertices;
- never infer uniqueness merely from the label “exceptional”;
- distinguish residual degree from H-degree and shell degree;
- distinguish a chosen ten-witness family from all possible single-outside K5 witnesses;
- do not transfer an E407 excess-four identity to the E408 285-edge excess-six core;
- if a source statement cannot be matched exactly, mark the dependent result OPEN rather than interpolating it.

Root promotion stays disabled until this firewall is satisfied by every Q32 closure row.

## 8. Support-exhaustiveness audit gate (added 2026-10-28)

Local U-reserve arithmetic must be kept separate from the theorem that all parent completions enter the U-contract.

- **E407 Q32:** `E407_FOUR_COLOR_U_RESERVE_CLOSURE.md` validly excludes the frozen V12 `|U|=29`, 49-block contract by `294 + p_12(29)=316 > 310`. Its parent-level use remains conditional on V12 survivor exhaustiveness and the selected-component identity. The dedicated E407 branch still has a stale OPEN canonical/proof-audit snapshot; reconcile that branch state before treating the root gate as unconditional.
- **E408 Q33:** `Q33_NONEXACT_U_RESERVE_CLOSURE.md` validly excludes the frozen `|U|=31`, 56-witness contract by `26(11-m) <= delta+6h <= 41`, while m=8,9 require 78 or52. The inspected witness-packing source gives a support lower bound, not equality by itself. The root receipt asserts an upstream exhaustive reduction, but its exact source path was not identified in this pass. Until that source is linked and checked, Q33 parent-level exhaustion remains conditional.
- **E408 Q32:** the new pivot-neighborhood packing theorem is valid as a structural reduction. Its scalar slack system has feasible states and is not an UNSAT certificate.

Accordingly, the root DAG must preserve the exact conditional premises above and must not turn a support-boundary contradiction into a whole-parent closure without an exhaustive bridge.

## 9. New v47 high-support local lemmas — firewall check (2026-10-28)

The 2+8 two-block transversal blocker and the 3+7 double-track fiber cap use only:
- the source-correct 4,5,5 matching-switch classification;
- the already-proved zero-slack map alignment;
- `alpha(H)<=4`, `Delta(H[R])<=2`;
- the pointwise degree ledger `e_Q(q)+d_R(q)=3);
- the endpoint-load identity for small blocks.

They do not invoke the retracted universal KP degree-nine statement, exceptional-point injectivity, the E407 excess-four identity, or the Q33 284-edge identity. The singleton/triangle exception in the 2+8 double-track case is explicitly preserved. Root status remains OPEN / NOT_CERTIFIED.


## 10. z=0,1 track-alignment proof firewall (2026-10-28)

The new `V47_Z01_TRACK_ALIGNMENT.md` uses only:
- the registered `alpha(H[R])=4) residual-type fact for z=0,1;
- the zero-slack small-triangle map fibers;
- globally aligned outer K7 tracks and their clique fibers;
- the exact residual incidence ledger `sum_{q in D} d_R(q)=7+y_D);
- the source-correct 4,5,5 switch normal form and pointwise degree identity.

The mismatch inequality is local and source-correct. The switch contradiction is applied only after proving all four fibers on both partitions are nonempty and equal as unlabelled partitions. No retracted KP degree-nine claim, exceptional-point injectivity, E407 excess-four identity, or Q33 284-edge identity is used. Root status remains OPEN / NOT_CERTIFIED.


## 11. Aligned low-z Type-I placement firewall (2026-10-29)

The new `V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM.md` uses only:
- the proved aligned partition into three target K12 cliques and one K11 clique;
- the balanced-coloring condition that every 13-set contains all twelve colors;
- the registered `10K5 dot-union G11` Type-I component decomposition;
- the source-correct placement and gap caps.

It does not use the retracted universal degree-nine assertion, exceptional-point injectivity, E407/Q33 identities, or any claim that the aggregate track-count relaxation is infeasible. It eliminates the triple-outside Type-I placement only within the aligned z=0,1 cell. EG617(r=12) remains OPEN / NOT_CERTIFIED.


## 12. Type-I special-K5 correction (2026-10-29)

The earlier section 11 claim that triple placement was eliminated is withdrawn. It incorrectly conflated the twelve K5 factors with the ten isolated K5 components. The source-correct Type-I structure has two special K5 cliques inside G11. The balanced-coloring argument only excludes an isolated triple-outside K5; a triple special K5 may have additional incident gadget edges and remains open subject to `b_s+b_t=4`. All canonical status documents must preserve this distinction. No root promotion follows.


## 13. Triple-special refinement firewall (2026-10-29)

The new triple-placement refinement is conditional on the aligned low-z clique partition and source Type-I gadget. It uses the 13-set balanced-coloring degree floor, the fact that the two special K5s lie inside G11, and the exact nine-gadget-edge incidence pattern. It proves a necessary geometry and `g_C=3), not a contradiction. No statement that triple placement is eliminated is authorized.


## 14. Exact-gap cap scope (2026-10-29)

The `g_C<=3) theorem applies only after the aligned low-z 3+7 normal form and source-correct Type-I component placement are established. The nonexact-color interval `7<=g_D<=21` also uses the registered 37-unit total gap, the 132-edge nonexact color, and the 13-set balanced-coloring condition for each O vertex and each K12 part. It does not imply graph nonexistence; do not promote the aligned cell or root theorem.


## 15. Nonexact-color shell floor (2026-10-29)

The refined range `7<=g_D<=19` depends on the 132-edge nonexact color D, the balanced-coloring bound `alpha(D)<=12), and p being D-nonadjacent to the shell A. It is not a generic consequence of the 37-gap identity alone. The resulting `e_D(H) in [76,88]` remains a necessary range, not a contradiction.


## 16. Type-I factor-occupancy ledger (2026-10-29)

The occupancy vectors use the source statement that the twelve K5 factors partition the 60 vertices other than x_C. Single-outside K5 H vertices form a transversal of the four target cliques; other K5-factor H vertices are independent and occupy distinct parts. The vector equations are count consequences, not an UNSAT certificate, and the two special K5s must remain distinguished from the ten isolated components.


## 12. T0 pointwise saturation firewall (2026-10-29)

The new T0 degree ledger uses only:
- the aligned target clique partition \(K_{12},K_{12},K_{12},K_{11}\);
- the balanced-coloring condition that every 13-set contains every non-target color;
- the exact H degree/cross-track degree ledger;
- the corrected Type-I factorization into ten isolated K5 components plus G11.

It distinguishes special K5s in G11 from isolated components and does not assume exceptional-point injectivity, a universal degree-nine point, or any Q33/E407 identity. The result is a pointwise capacity theorem only, not an UNSAT certificate. EG617(r=12) remains OPEN / NOT_CERTIFIED.


## 12. T0 pointwise saturation firewall (2026-10-29)

The new T0 degree ledger uses only:
- the aligned target clique partition \(K_{12},K_{12},K_{12},K_{11}\);
- the balanced-coloring condition that every 13-set contains every non-target color;
- the exact H degree/cross-track degree ledger;
- the corrected Type-I factorization into ten isolated K5 components plus G11.

It distinguishes special K5s in G11 from isolated components and does not assume exceptional-point injectivity, a universal degree-nine point, or any Q33/E407 identity. The result is a pointwise capacity theorem only, not an UNSAT certificate. EG617(r=12) remains OPEN / NOT_CERTIFIED.


## 13. Isolated-double residual firewall (2026-10-29)

Do not apply the seven-vertex residual catalog or its 64-baseline holonomy classes to an exact color until its placement has been checked to have all ten isolated K5 components single-outside. The outside-count profiles (2,1^11), (2,2,1^10), and (3,1^11) do not by themselves guarantee that condition.

The registered source-correct isolated-double placement yields nine isolated H-K4s plus one isolated H-K3, and an eight-vertex G11 H-residual with profile (2,2,2,2), e=12+g_C. The two-K4 local relaxation is not a full gadget completion. The exceptional x_C in H, y in H isolated-double subcase has g_C=3 and t_C=1. The global exact-color cap t_C<=1 means at most one T0-incident extra edge may be chosen across the two T0 vertices. The correct globally capped relaxation counts are 8, 96, 408, 880 for gaps 0,1,2,3; the weaker per-T0-vertex-cap counts 8, 96, 480, 1312 and earlier uncapped counts 8, 96, 528, 1760 are superseded.

The global low-gap orientation may be cited only through the independent 69/70 near-Turan classification or the explicit case split in V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md. The placement-sensitive T0 count is now t_C<=1 for every exact color, including the isolated-double x_C in H, y in H two-double branch (g_C=3): its two T0 vertices lie in the special K3 and K4 and have degrees 3 and 4, respectively. Therefore the cap of one extra edge across all three T0--Ti pairs is global for exact colors. No Q32 or EG617 root closure is certified.
