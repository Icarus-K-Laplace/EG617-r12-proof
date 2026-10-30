# Import receipt for the low-edge obstruction and four parent layers

Date: 2026-10-30.

**Local theorem receipt: ISSUED / PROVED.**

    47_POINT_LOW_EDGE_UNIVERSAL_OBSTRUCTION = PROVED

No simple47-vertex graph has e<=285, delta>=12, alpha<=4 and omega<=11. Two complete proof routes are supplied: audited exact285 theorem plus safe augmentation, and a direct total-excess<=6 proof. The common-neighbor bound, each augmentation step, K10 completion exceptions, support rotation and pointwise D accounting have been checked.

**Generic source-gate receipt: ISSUED / PROVED.**

    J in R(4,47), e(J)<=286 => delta(J)>=12.
    J in R(4,47) => e(J)>=286.

The first statement has a self-contained reconstruction of the lower-order chain, including the121/122-neighborhood classification. The second combines it with the new obstruction. Neither statement is Q33-specific.

**Four parent-layer receipts: ISSUED / PROVED_CONDITIONAL on P0.**

E407/q31, E407/q32, E408/q32 and E408/q33 are impossible under the genuine h13 T61 parent contract P0 in CROSS_ROOT_PARENT_CONTRACT_AUDIT.md. Each row supplies order, exact edges, independence, clique cap, inherited density caps and the generic minimum-degree gate. The statements also apply to the corresponding Q_max layers by choosing a charge-maximizing regular pivot.

The E407/Q32 completion contradiction bypasses V12 and MS-29. The E408/Q33 contradiction bypasses witness-support promotion. E408/Q32 is covered uniformly over all m and selected support sizes. No source profile or exceptional location is constrained by the terminal proof.

## Import instructions and boundary

Import the theorem statements together with their explicit hypotheses and the new generic source gate. Do not import only a CLOSED label. Do not delete other global obligations based on these terminal results.

Suggested replacement dependency paths, for root review only:

    E407/q31 or q32 -> P0 pivot map -> R(4,47) gate -> low-edge obstruction
    E408/q32 or q33 -> P0 pivot map -> R(4,47) gate -> low-edge obstruction

The residual charge bounds are q_p<=30 for E407 and q_p<=31 for E408. They do not prove parent nonexistence unless a separate lower-bound or branch-coverage theorem is supplied.

**Global EG617 root receipt: NOT ISSUED.** The original K145 front end, contextual R(4,49), lower-energy/h12 layers and remaining charge layers are outside this new proof. The global root and sibling files have not been edited. This receipt is confined to the independent workstream and awaits root-side mathematical review/integration.

## Verification evidence

INDEPENDENT_VERIFIER.py was executed with Python3.12.14 and exited0. VERIFICATION_RESULTS.json and VERIFICATION_LOG.txt retain actual output. The checks cover all augmentation budgets, support orbits, scalar inequalities,8,400 local D accounting cases,20 C5 type-set pairs,55 singleton extensions,10 missing-edge endpoint cases, and263 maximal independent sets in49 admissible neighborhood representatives. They support the analytic proof; they are not proof-assistant certification or exhaustive enumeration of47-vertex graphs.
