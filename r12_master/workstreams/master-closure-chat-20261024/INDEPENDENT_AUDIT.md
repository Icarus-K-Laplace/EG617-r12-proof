# Independent audit

Audit date: 2026-10-24  
Branch: workstream/r12-master-closure-20261024.

This audit checks the new algebra and theorem scope. It does not certify the complete EG617 proof.

## 1. Repository boundary

- The base branch was queried at the start and resolved to b98bea36e36a033100b8bf09a599897cb5afd7de.
- Work was isolated on workstream/r12-master-closure-20261024.
- All created files are under r12_master/workstreams/master-closure-chat-20261024/.
- Root canonical files and sibling workstreams were not edited.

## 2. Independent arithmetic checks

### Seven-block duplicate ledger

For each non-target color C,

e(C) = (252+P_C) + (427+R_C) + (129+s_C)
     = 808 + P_C + R_C + s_C.

Every color has 870 edges, so P_C+R_C+s_C=62.

Summing over the eleven non-target colors gives:

- sum P_C = 252;
- sum R_C = 427;
- sum s_C = 3.

These values independently reconcile with the actual pair counts:

- between distinct target blocks: 21*144 = 3024 edges; baseline 11*252 = 2772; duplicate total 252;
- between the 84 block vertices and R: 84*61 = 5124 edges; baseline 11*427 = 4697; duplicate total 427;
- inside R: 1830-408 = 1422 non-target edges; baseline 11*129 = 1419; residual excess total 3.

Thus the non-target edge total is 3024+5124+1422 = 9570 = 10440-870. The full graph has C(145,2)=10440 edges. The per-color identity and the global pair count agree.

### Exact-129 aggregate bound

If m colors have s_C=0, then P_C+R_C=62 for each exact-129 color. Since the sum of their P_C values is at most252,

sum over exact-129 colors R_C >= 62m-252.

For m=8,9,10 this gives 244,306,368. Since sum s_C=3 and each s_C is a nonnegative integer, the number of exact-129 colors is indeed one of 8,9,10.

### Q33 d3 exact budget

The row equations imply

c_a+g_a=10+X_a.

Summing over the three S vertices gives c_S+G_S=30+X. With q=e(M)+G_A=33, e(M)=c_S+beta, and G_A=G_S+G_B, the exact identity is

beta+X+G_B=3.

The ten feasible aggregate triples are:
(0,0,3), (0,1,2), (0,2,1), (0,3,0),
(1,0,2), (1,1,1), (1,2,0),
(2,0,1), (2,1,0), (3,0,0).

The D(14) cap gives e(M)>=22, hence c_S>=22-beta. Since k_b<=3, c_S<=10+2*n_2, so n_2>=ceil((12-beta)/2). At most G_B B-vertices are decorated, yielding guaranteed regular counts 3,4,4,5 for beta=0,1,2,3.

### d3 multi-S allowance bound

The proof in R12_D3_MULTIS_EXTRACTION_BOUND.md uses only:
- the exact nonadjacent zero-gap identity;
- the clique cap omega(F)<=11;
- S_y subset A minus Y;
- one distinct M-edge x_z z for each owner of a different missing-triple class;
- the exact exchange formula and maximality q_y<=q.

A separate arithmetic check enumerated all 70 pairs q in {32,...,38}, N in {1,...,10} and verified the class-size implication n>=N+30-q whenever the allowance bound permits a nonempty class. The N=9 consequences in that file follow directly from this inequality.

## 3. Mathematical audit status

| Claim | Independent check | Status |
|---|---|---|
| R12 status labels | Compared canonical/live/frontier and local proof files; scope differences recorded. | Evidence-qualified status only; not theorem closure. |
| d3 multi-S allowance theorem | Re-derived the proof and checked the finite q/N arithmetic. | PROVED_ANALYTIC under legal backend + all-pivot core-minimum-degree contracts. |
| E408 exact budget | Re-derived the algebra and ten aggregate integer cases. | PROVED_CONDITIONAL on the retained V11 Q33 interface. |
| E407 Cell-B exclusion | Checked scope against E407 Q32 common-K11 templates. | Cell-B only; full E407 remains OPEN. |
| E408 Q32/Q33 | Checked the local/global necessary conditions for scope. | OPEN; no global contradiction established. |
| R(4,49) forcing-to-master | Exact missing contract stated in FORCING_TO_MASTER_CONTRACT.md. | OPEN. |
| EG617(r=12) | Front-end and backend are not both fully closed; no final contradiction. | OPEN / NOT_CERTIFIED. |

## 4. Audit limitation

This audit independently checked algebraic consequences and source scope, not the entire 1752-node recurrence, every retained lower-order seed, every V11/V12 package, or every historical finite certificate. Those assets remain dependencies and require their own replay before the final theorem can be promoted.
