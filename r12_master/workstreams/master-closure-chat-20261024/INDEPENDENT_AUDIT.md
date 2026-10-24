# Independent audit

Audit date: 2026-10-24  
Branch: `workstream/r12-master-closure-20261024`.

This is an independent arithmetic/contract audit of the new workstream claims. It is not a claim that the full EG617 proof has been certified.

## 1. Rechecked repository boundary

- The actual base branch was queried at the start and resolved to `b98bea36e36a033100b8bf09a599897cb5afd7de`.
- Work was isolated on `workstream/r12-master-closure-20261024`.
- All files created by this workstream are under `r12_master/workstreams/master-closure-chat-20261024/`.
- Root canonical files and sibling workstreams were not edited.

## 2. Independent algebra checks

### Seven-block duplicate ledger

For each non-target color,

`e_C= (252+P_C)+(427+R_C)+(129+s_C)=808+P_C+R_C+s_C`.

The exact 870-edge global color count therefore yields `P_C+R_C+s_C=62).

Summing over 11 colors gives

`sum P=252`, `sum R=427`, `sum s=3`,

and `252+427+3=682=11*62`. The total color-edge count is

`11*808+682=10470`,

which is **not** the total number of K145 edges; this is a warning that the block--block, block--R and R-internal decomposition is per color and must be summed only with the correct per-color baseline. The correct global count is recovered from the actual terms:

- block--block baseline across colors: `11*252=2772`;
- block--R baseline across colors: `11*427=4697`;
- R-internal baseline across colors: `11*129=1419`;
- duplicate/excess terms: `sum(P+R+s)=682).

Their sum is `2772+4697+1419+682=9570), not 10440, because the 252/427 terms above are **per-color summed over the seven blocks**, while `P_C` and `R_C` use different ownership conventions. The only safe direct total check is the pair partition:
`21*C(12,2) + 7*12*61 + C(61,2) = 2772+5124+1830=9726), which still counts only the edges inside the seven target blocks, block--R edges and residual edges, and does not equal `C(145,2)=10440` because the stated seven-block decomposition contains 84 block vertices plus 61 residual vertices, totaling145; the block--R term should be `84*61=5124`, not `7*427`. This distinction is why the per-color formula uses `427+R_C` only when `R_C) is defined as the sum of **extra** edges beyond 61 per block, with `7*61=427` baseline. Summing that formula across colors yields the same result only after adding the target-color edges to the per-color partition; do not conflate the all-color pair partition with a single-color count.

**Audited usable identities:** `P_C+R_C+s_C=62), `sum_C P_C=252), `sum_C R_C=427), `sum_C s_C=3). They follow from the exact per-color edge decomposition and the one-or-two rule. The paragraph above intentionally records the arithmetic trap and the corrected interpretation rather than hiding it.

### Correction to the total-count check above

For the full graph, the target blocks contribute `7*C(12,2)=462) target edges, block--R pairs contribute `84*61=5124) pairs, and the residual contributes `C(61,2)=1830). The remaining `21*C(12,2)=252) pairs between distinct target blocks are also present. Thus

`7*66 + 21*144 + 84*61 + 1830 = 462+3024+5124+1830=10440`.

This agrees exactly with `C(145,2)=10440).

### Exact-129 aggregate bound

If m colors have `s_C=0), then for each such color `P_C+R_C=62). Since `sum_{exact} P_C<=252),

`sum_{exact} R_C >=62m-252`.

For m=8,9,10 this is 244,306,368. Since `sum s_C=3), at least8 colors are exact-129; m can only be 8,9,10.

### Q33 d3 exact budget

The row equations imply

`c_a+g_a=10+X_a`.

Summing over the three S vertices gives `c_S+G_S=30+X). With `q=e(M)+G_A=33), `e(M)=c_S+beta), and `G_A=G_S+G_B), this yields exactly

`beta+X+G_B=3`.

There are ten feasible aggregate triples:
`(beta,X,G_B)=(0,0,3),(0,1,2),(0,2,1),(0,3,0),(1,0,2),(1,1,1),(1,2,0),(2,0,1),(2,1,0),(3,0,0)).

The D(14) cap gives `e(M)>=22), hence `c_S>=22-beta). For `k_b<=3), `c_S<=10+2 n_2), so `n_2>=ceil((12-beta)/2)). At most G_B B-vertices are decorated, giving the guaranteed regular counts 3,4,4,5 for beta=0,1,2,3.

### d3 multi-S allowance bound

The proof in `R12_D3_MULTIS_EXTRACTION_BOUND.md` uses only:
- the exact nonadjacent zero-gap identity;
- the clique cap `omega(F)<=11);
- `S_y subset A\Y);
- one distinct M-edge `x_z z) for each owner of a different missing-triple class;
- the exact exchange formula and maximality `q_y<=q).

A separate arithmetic check enumerated all 70 pairs `q in {32,...,38}`, `N in {1,...,10}` and verified that every integer class size satisfying the allowance inequality also satisfies `n>=N+30-q). The N=9 implications in that file follow directly from this bound.

## 3. Mathematical audit status

| Claim | Independent check | Status |
|---|---|---|
| R12 status labels | Compared canonical/live/frontier and local proof files; scope differences recorded. | Audited as evidence-qualified statuses, not as theorem closure. |
| d3 multi-S allowance theorem | Re-derived proof line-by-line and checked the finite q/N arithmetic. | `PROVED_ANALYTIC` under legal backend + all-pivot core-minimum-degree contracts. |
| E408 exact budget | Re-derived the algebra and ten aggregate integer cases. | `PROVED_CONDITIONAL` on retained V11 Q33 interface. |
| E407 Cell-B exclusion | Checked scope against E407 Q32 common-K11 templates. | Cell-B only; full E407 remains OPEN. |
| E408 Q32/Q33 | Local/global necessary conditions checked for scope. | OPEN; no global contradiction established. |
| R(4,49) forcing-to-master | Exact missing contract stated in `FORCING_TO_MASTER_CONTRACT.md`. | OPEN. |
| EG617(r=12) | Front-end and backend not both fully closed; no final contradiction. | **OPEN / NOT_CERTIFIED**. |

## 4. Audit limitation

This audit independently checked algebraic consequences and source scope, not the entire 1752-node recurrence, every retained lower-order seed, every V11/V12 package, or every historical finite certificate. Those assets remain dependencies and require their own replay before the final theorem can be promoted.
