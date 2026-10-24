# R12 E407 / E408 global compatibility audit

## 1. Exact shell/core arithmetic — corrected

For a T61 residual F with a degree-13 pivot, shell A of size13, core H of size47, and q=e(M)+G_A,

    e(F)=91+q+e(H).

| Energy / layer | q | e(H) | core excess 2e(H)-47*12 |
|---|---:|---:|---:|
| E407 Q32 | 32 | 284 | 4 |
| E408 Q32 | 32 | 285 | 6 |
| E408 Q33 | 33 | 284 | 4 |

The E408 Q32 core has 285 edges, not 284. The common 284-edge core applies to E407 Q32 and E408 Q33.

## 2. E407 Q32: five regular-K11 templates

The V12 package's finite certificate has now been independently replayed in this workstream. Its verifier confirms 8,677 kernel weight vectors, 17,957 count states, 1,984 labelled necessary shells, and 554 OPEN entries after the three recorded screen rules. All 554 have a regular d3/rho=0 candidate, and the remaining shell views are the five templates A–E in Q32_KERNEL_COVERAGE.md.

The replay certifies finite coverage of the necessary shell-state model. It does not certify that a 47-core completion exists or that all five templates are impossible. The retained lower-order seeds and analytic exclusion rules retain their stated contracts.

Repository-proved relative to extremal inputs:
- At a sharp |W|=23 Cell-B near-anchor, the subdivision vertex w has target degree20 and no target neighbours outside W.
- The 11 non-target colors have edge-count multiset 129^7,130^4.
- Four 130-edge colors create disjoint isolated K4 components through w.
- Independent 4-sets in the outside set force four disjoint target 3-neighbourhoods to partition B union {x} or A union {y}.
- Each saturated 3-neighbourhood must meet both A and B, contradiction.

This eliminates that sharp Cell-B completion only; it does not show every Q32 template is Cell-B.

## 3. E408 seven-block system

Repository-proved relative to the outer embedding ledger:
- Seven target K12 blocks are pairwise target-anticomplete and anticomplete to residual R, |R|=61, e(R)=408.
- Every color has exactly 870 edges globally.
- For each non-target color C, P_C+R_C+s_C=62 and sum_C s_C=3.
- At least eight colors have e_C(R)=129.
- For every exact-129 color, the blocker theorem gives e_C(B_i,R)>=62 in each outer block, hence R_C>=7 and P_C<=55.
- The Q33/d3 branch has beta+X+G_B=3, conditional on the retained V11 core interface.

These are simultaneous necessary constraints, not a contradiction.

The V12 package independently replayed here does not certify E408 Q32 coverage or Q33 closure. Its own E408 sections explicitly leave Q32/Q33 OPEN.

## 4. New cross-cutting witness-capacity theorem

R12_WITNESS_CAPACITY_CROSSCUT.md proves the following under the exact T61 contract:

1. Every independent 4-set Q in H hits at least three shell rows. Otherwise p together with the shell anti-neighbourhood of Q would violate omega(F)<=11.
2. For each witness Q_b anticomplete to b, its hit hubs contain T_b and cover every edge of M[S].
3. Every independent triple in H_b extends to an independent 4-set in H_b when t_b<=3. For t_b<=6, failure of triple extension forces t_b>=8-epsilon(X), so it can occur only when t_b>=4 and X contains enough of the four core-excess units.
4. In E408 Q33, each exact-129 color has at least five K5 components of the form {b} union Q with Q subset H. Their Q sets are disjoint within one color and intersect in at most one vertex across distinct colors. The five selected labels have sum k_b>=7-beta.

The scalar capacity bounds are not enough to close either layer: the 40 four-sets from at least eight exact-129 colors require 160 core incidences, while the coarse upper bound from four-edge memberships is 47*11=517. The next theorem must exploit the actual H adjacency structure and row-hit labels.

## 5. Still OPEN

- E407: simultaneous labelled completion of any of the five templates with the same 284-edge core.
- E408 Q32: exhaustive coverage at the q=32 threshold (its core has 285 edges and excess6); the E407 finite screen cannot be transferred without a new threshold-29 certificate.
- E408 Q33: global seven-block/color-factor/blocker compatibility under the exact budget beta+X+G_B=3.
- No aggregate sum identity is treated as forcing each local defect to zero.

EG617(r=12) remains OPEN / NOT_CERTIFIED.


## 5. New E407 Q32 A/C crosscut

The fresh color-factor theorem in R12_E407_Q32_COLOR_FACTOR_CROSSCUT.md proves:
- at least seven/eight independent core 4-sets per exact-129 color from K5 components disjoint from the hub triple S;
- at least four/five of these are hub-complete in templates A/C;
- at least 28/35 hub-complete witness sets across the at least seven exact-129 colors;
- any two witness sets have at most one common vertex, and their exclusive parts admit a Hall perfect matching in the 284-edge core.

This strengthens the local witness-capacity constraint but does not rule out A/C. It does not cover templates B/D/E, and no cross-color edge-reuse bound sufficient for contradiction has been established.


## 6. F-007 — witness-count coverage now spans A–E

The exact-129 color-factor argument now gives a necessary witness family for every E407 Q32 template:
- A/B: 28 hub-complete independent 4-sets;
- C/D: 35 hub-complete independent 4-sets;
- E with at least one full row: 35 hub-complete independent 4-sets;
- E with no full rows: 42 independent 4-sets hitting both endpoints of M[S].

Every family is pairwise linear across colors and obeys the Hall matching lemma. This does not yet exclude any template: the common-core completion obstruction still needs a bound on how often the same 284-core edge can serve as a matching edge for multiple witness-block pairs.
