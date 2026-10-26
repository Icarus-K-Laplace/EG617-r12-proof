# Q33 exact-129 P_C=49 profile ledger

Updated: 2026-10-26  
Status: **two profiles excluded conditionally; two all-component-edge-present branches remain OPEN.**

## Contract

This ledger concerns only the E408 Q33 contract:
\[
|V(H)|=47,\quad e(H)=284,\quad \alpha(H)\le4,\quad \delta(H)\ge12,
\quad \sum_{x\in H}(d_H(x)-12)=4.
\]
For an exact-129 color \(C\), the seven-block equality is
\[
P_C+R_C+s_C=62,\qquad s_C=0.
\]
At \(P_C=49\), \(\sum_i r_i(C)=R_C=13\). The sorted positive integer profiles of this sum that remain relevant are listed below. This is not the Q32 285-edge contract.

## Reconciled profile status

| Profile | Status | What is actually established |
|---|---|---|
| \((6,2,1^5)\) | **PROVED_CONDITIONAL** | The Q33 sibling theorem R12_P49_R6_R2_DOUBLE_STAR_EXCLUSION.md enumerates 452 Case-A and 570,942 Case-B/C gadget/incidence configurations; independent replay here gives 571,394 checks, zero failures. The proof forces a \(C\)-colored \(K_{12}\) and a vertex with at least two external \(C\)-edges. |
| \((7,1^6)\) | **PROVED_CONDITIONAL** | New theorem Q33_P49_R7_DOUBLE_STAR_EXCLUSION.md. The no-component row split and exact gadget alignment force a \(C\)-colored \(K_{12}\) plus a double-star violation. Its new standalone verifier checks 27,380 high-pair cases and 48 low-pair/\(D\) cases, zero failures. |
| \((4,4,1^5)\) | **OPEN** | The missing-component-edge branch is excluded by the retained incidence-sensitive screen. The all-component-representative-edges-present branch is not excluded. |
| \((4,3,2,1^4)\) | **OPEN** | The missing-component-edge branch is excluded by the retained incidence-sensitive screen. The all-component-representative-edges-present branch is not excluded. |

The older Q33 canonical summary and R12_P49_INCIDENCE_SENSITIVE_SCREEN.md still list all four profiles as open. Those summaries predate the separate \((6,2,1^5)\) double-star theorem and this line's \((7,1^6)\) theorem; they must not be used as the current profile ledger.

## Why the two remaining branches are hard

If every component-label edge is present across every outer-block pair, the ten isolated \(K_5\) components each extend with one representative from each of the seven outer \(K_{12}\) blocks to a \(C\)-colored \(K_{12}\). This alone is **not** a contradiction.

The only registered star-capacity consequence is
\[
d_C(z,Q)\le1
\]
for an outside vertex \(z\) and a \(C\)-colored \(K_{12}\) \(Q\). A single external \(C\)-edge is allowed. Any argument asserting that one external edge already contradicts star capacity is invalid. In particular, the historical inference “ten disjoint \(K_{12}\)'s imply \(P_C\le42\)” is not promoted here: the current star-capacity theorem alone does not justify that bound.

The next proof target is to combine the all-component-edge-present incidence pattern with the exact 284-edge core and labelled witness packing, or else produce a valid stronger outer-edge bound. Merely constructing ten \(K_{12}\)'s or satisfying scalar budgets is insufficient.

## Finite verifier record

The verifier for the new \((7,1^6)\) alignment is:
- Path: verify_q33_p49_r7_double_star.py
- Commit containing verifier: 6e896507bee2d91701b173b52678788f3dfcc826
- Independently replayed output: 27,380 high-pair checks + 48 low-pair/\(D\) checks; zero failures.

The \((6,2,1^5)\) verifier was independently replayed in a separate runtime:
- 452 Case-A configurations;
- 570,942 Case-B/C configurations;
- total 571,394; zero failures.

These are exact finite checks of the stated gadget predicates, conditional on the upstream row classifications and exact-129 factor theorem. They are not an UNSAT certificate for the full graph problem.
