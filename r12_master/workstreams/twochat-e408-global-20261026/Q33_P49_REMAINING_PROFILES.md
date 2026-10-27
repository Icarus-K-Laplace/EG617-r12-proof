# Q33 exact-129 P_C=49 profile ledger

Updated: 2026-10-27  
Status: **local classification incomplete, but globally bypassed by the Q33 nonexact-U reserve contradiction.**

## Contract

This ledger concerns only the E408 Q33 284-edge contract. For an exact-129 color \(C\), \(P_C=49\) means \(R_C=13\) and the seven positive block budgets sum to 13.

## Local profile status

| Profile | Local status |
|---|---|
| \((6,2,1^5)\) | **PROVED_CONDITIONAL excluded** by the audited double-star theorem. |
| \((7,1^6)\) | **PROVED_CONDITIONAL excluded** by `Q33_P49_R7_DOUBLE_STAR_EXCLUSION.md`. |
| \((4,4,1^5)\) | **OPEN locally** only in the all-component-representative-edges-present branch. |
| \((4,3,2,1^4)\) | **OPEN locally** only in the all-component-representative-edges-present branch. |

The two local OPEN branches force ten component-label K12 structures but are not contradicted by the valid star-capacity theorem alone.

## Global status changed on 2026-10-27

The new theorem `Q33_NONEXACT_U_RESERVE_CLOSURE.md` makes these local branches unnecessary for Q33 closure.

At the 31-point/56-witness terminal, every nonexact non-target color needs at least
\[
p_{12}(31)=26
\]
U-edges. The \(56-h\) selected exact-color component witnesses already occupy \(336-6h\) of the \(336+\delta\) edges in \(L=\overline{H[U]}\), so all nonexact colors combined have at most \(\delta+6h\) slots. Hence
\[
26(11-m)\le\delta+6h.
\]
The exact-color count theorem excludes \(m=10\), while \(m\in\{8,9\}\), \(\delta\le17\), and the preliminary bound \(h\le4\) give a maximum right side of 41. The left side is 78 for \(m=8\) and 52 for \(m=9\). Contradiction.

Therefore the simultaneous Q33 full-color system is impossible even if one of the two local P49 profiles were colorwise realizable.

## Audit note

The historical statement that one external same-color edge into a monochromatic \(K_{12}\) is impossible remains false and is not revived here. The global closure uses only U-edge ownership and Turan capacity.

Future work should treat the two remaining P49 profiles as optional local classification problems, not as blockers for E408 Q33.