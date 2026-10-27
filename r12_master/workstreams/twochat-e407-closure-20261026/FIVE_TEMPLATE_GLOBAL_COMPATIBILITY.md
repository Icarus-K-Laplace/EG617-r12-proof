# E407 Q32 — five-template global compatibility

Date: 2026-10-27  
Status: **OPEN / NOT_CERTIFIED. Current same-core compatibility snapshot.**

## 1. Shared object and template shell data

Every legal A–E completion must use a 47-vertex core H with e(H)=284, alpha(H)<=4, omega(H)<=11, total internal excess four, a 29-point support U and 18-point W, and the same 49-block exact support contract.

The five templates are alternative shell states, not simultaneous shell graphs. Write A=S dot-union B, |S|=3, |B|=10, B a target K10, M=bar(F[A]), D_a=N_F(a) cap H, and k_b=|N_M(b) cap S|=|D_b| for b in B.

| Template | S-row sizes | beta=e(M[S]) | full-row floor n3 |
|---|---|---:|---:|
| A | (12,10,10) | 0 | >=6 |
| B | (11,11,10) | 0 | >=2 |
| C | (12,11,10) | 1 | >=6 |
| D | (11,11,11) | 1 | >=1 |
| E | (12,11,11) | 2 | either >=1, or exactly ten ends-pair rows |

## 2. Actual selected exact-color support blocks

Every support block Q is the four-core-vertex part of a selected exact-color isolated K5, with a genuine anchor in {p} union S union B. For every exact color c:

\[
b_c=\#\{\text{selected B anchors}\}\in\{5,6,7\},
\]
with at most one selected S anchor. Across all seven exact colors at least35 selected blocks are B-anchored.

Deleting the seven selected K5s leaves exactly 3K5+G11 in that color.

## 3. Selected hub-complete forcing across all templates

### Fixed-full-row theorem

If f is a full B row, any selected B-anchored block Q which misses a hub must meet D_f. Because |D_f|=3 and same-color selected blocks are disjoint, at most three selected B-blocks per exact color fail to be hub-complete. Hence
\[
N_{hub,c}^{sel}\ge b_c-3\ge2.
\]
Thus every full-row branch has at least14 actual selected hub-complete B-blocks globally.

For E with no full row, the row equations force all ten B rows to be the P3 ends-pair type. Every selected B-block then hits both endpoint rows, yielding at least35 actual selected endpoint-complete blocks globally.

### Full-row linearity capacity

Let h be the number of full B rows and N_bad the global number of selected B-blocks that are not hub-complete. For u in U let d(u) count full rows whose target-core neighbourhood contains u. Pairwise support linearity and pointwise anchor injectivity give
\[
N_{bad}\le C(h):=\min\{21,\lfloor9+60/h\rfloor\}.
\]
Therefore
\[
N_{hub}^{sel}\ge B_{sel}-C(h),\qquad B_{sel}=\sum_c b_c\ge35.
\]
In particular:

| h | hub-complete selected floor |
|---:|---:|
| 1-5 | 14 |
| 6 | 16 |
| 7 | 18 |
| 8 | 19 |
| 9-10 | 20 |

Thus A and C now have the certified global floor
\[
\boxed{N_{hub}^{sel}\ge16}.
\]

## 4. Exact shell cross-load and selected S anchors

For exact color c let q_c=|E_c(S,B)|. Every exact color has q_c>=1. If it contains a selected S anchor, q_c>=2. If sigma is the total number of selected S-anchor occurrences, then
\[
\sum_c q_c\ge7+\sigma.
\]
Together with the earlier exact shell-edge theorem,
\[
\boxed{|E_{exact}(S,B)|\ge\max\{14-\beta,\,7+\sigma\}.}
\]
This is a per-color residual-factor result, not merely a scalar shell edge count.

## 5. Target-excess and color-premium join

The current same-state ledger additionally gives:

- every B vertex has target degree exactly13;
- if c=e_M(S,B), then core full-target excess is c+beta-11;
- at least 54-c-beta H vertices have d_H=12 and full target degree13, hence exactly one target shell neighbour;
- every B vertex has exactly seven units of non-target color degree premium above the `129^7,130^4` minimum baselines;
- selected B-anchor cells in their exact color are zero-premium cells;
- a two-B exceptional G11 costs at least one B-premium unit;
- selected B-anchor point incidences total at least140, so at least eight U points lie in at least five selected B-anchored blocks with distinct B labels.

These constraints have not yet been converted into a contradiction.

## 6. Template status after current forcing

| Template | Status | strongest current selected-support obligation |
|---|---|---|
| A | OPEN | h>=6; >=16 actual selected hub-complete B-blocks |
| B | OPEN | h>=2; >=14 actual selected hub-complete B-blocks; earlier >=21 selected k>=2 block occurrences |
| C | OPEN | h>=6; >=16 actual selected hub-complete B-blocks; beta=1 |
| D | OPEN | h>=1; >=14 actual selected hub-complete B-blocks; beta=1 |
| E, h>=1 | OPEN | >=14 selected hub-complete blocks; beta=2 |
| E, h=0 | OPEN | exactly ten ends-pair rows; >=35 selected blocks hit both P3 endpoints |

No template has been shown realizable.

## 7. Why shell-only methods remain insufficient

`SHELL_LIST_RELAXATION_AUDIT.md` gives a coarse shell-label relaxation for every missing graph with at least14 edges. The new theorems escape that audit because they use actual selected blocks on U, pairwise linearity, pointwise anchor injectivity, and the exact residual factor.

The remaining contradiction must use these common-core resources, especially support multiplicities / omission degrees, U/W degrees, target-excess concentration, or exact residual factor ownership.

## 8. Primary theorem target

> No A–E shell row system can coexist with seven exact-color selected-component classes on one legal 29-point support / 284-edge core satisfying the strengthened hub-complete, cross-load, anchor, U/W, residual-factor, and four-excess constraints.

Primary new files: `SELECTED_SUPPORT_HUB_COMPLETENESS.md`, `FULL_ROW_LINEARITY_CAPACITY.md`, `S_ANCHOR_CROSS_LOAD_REFINEMENT.md`, plus the previously registered selected-anchor / residual-factor / target-excess ledgers.