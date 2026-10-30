# E408 Q32 m=10, 3+7, z=3 — switch-partner pointwise degree blocker

Date: 2026-10-30  
Status: **PROVED_CONDITIONAL local theorem.** It eliminates all nontrivial F/G mismatches in the no-double-track z=3 branch and reduces that branch to aligned profile (2,2,2,1). It does not close the aligned terminal or the double-track branch.

## 1. Exact normalized switch

Use the registered 4,5,5 theorem. For the synchronized switch in the 3+7 small triangle A,B,C and outer block D, relabel so that:
- A-D and B-D base matchings are identity;
- C-D base matching is sigma=(s j);
- the extra edges are A_sD_j, B_sD_j, C_sD_s.

Then the two moved outer vertices have the following small-block neighbor-label sets:

| Outer vertex | S_A | S_B | S_C | k(q) |
|---|---|---|---|---:|
| q=D_j | {s,j} | {s,j} | {s} | 2 |
| q=D_s | {s} | {s} | {s,j} | 1 |

The other two outer vertices have one common label each and k=0. In particular, q=D_j has singleton common label s, but it also has label j in both A and B. This partner label was not charged by the earlier common-fiber-only switch budget.

## 2. Pointwise degree inequality

Let F_s,F_j be the common small-map residual fibers, with sizes n_s,n_j. Every r in F_s is adjacent to q by its common label s. Every r in F_j is adjacent to A_j and B_j by the common small-map definition, and q=D_j is adjacent to both A_j and B_j. Hence
\[
N_R(q)\supseteq F_s\cup F_j,\qquad d_R(q)\ge n_s+n_j.
\]
The switch vertex q=D_j receives two extra small-component edges, so k(q)=2 and e_Q(q)>=2. The exact degree identity is
\[
e_Q(q)+d_R(q)=3.
\]
Therefore d_R(q)<=1, and
\[
\boxed{n_s+n_j\le1.}
\]
This bound is pointwise and does not use the aggregate y=2 budget.

## 3. Eliminate the nontrivial partition mismatches

The exact 91,584-pair dual-fiber enumeration has only three nontrivial zero-cost F/G mismatch modes:
- F=(3,3,1,0), G=(3,2,1,1), with empty duplicated fiber and a size-three split partner;
- F=(3,2,2,0), G=(3,2,1,1), with empty duplicated fiber and a size-two split partner;
- F=(3,2,2,0), G=(2,2,2,1), with empty duplicated fiber and a size-three split partner.

Each mode requires a synchronized switch with n_s=0 and n_j in {2,3}, violating n_s+n_j<=1. The seven-block incidence-slack budget forces at least one zero-cost switch whenever F and G differ (in fact at least five by the earlier endpoint-load argument). Thus
\[
\boxed{F=G}
\]
in every no-double-track z=3 completion.

## 4. Reduce aligned F=G profiles

If F=G, any synchronized switch must have n_s+n_j<=1. Among the four registered profiles:
- (3,3,1,0) permits only the empty/singleton transposition;
- (3,2,2,0), (3,2,1,1), and (2,2,2,1) permit no transposition.

For profile (3,3,1,0), the empty/singleton transposition fixes both size-three labels. A fixed size-three fiber h has its three small-block vertices and seven outer-track vertices forming a K10; the three residual vertices in F_h form a K3 adjacent to all ten. This gives a forbidden monochromatic K13.

For profiles (3,2,2,0) and (3,2,1,1), no switch is possible, so every outer block is aligned; their size-three fiber again gives K13.

The only profile without a size-three fiber is (2,2,2,1). It has no empty fiber, so no switch is possible; every outer block is aligned.

## 5. Result and open boundary

The no-double-track m=10, 3+7, z=3 branch reduces to
\[
\boxed{F=G,\quad \operatorname{profile}(F)=(2,2,2,1),\quad\text{all seven outer blocks aligned}.}
\]

The separate double-track branch remains open. The aligned (2,2,2,1) configuration remains open and must still be combined with the exact residual graph, three cross-fiber edges, endpoint-load matrix, and outer weighted-heavy graph. No full-support Q32 or EG617(r=12) closure is claimed.

No retracted degree-nine claim, exceptional-vertex injectivity, Q33 identity, or E407 identity is used.
