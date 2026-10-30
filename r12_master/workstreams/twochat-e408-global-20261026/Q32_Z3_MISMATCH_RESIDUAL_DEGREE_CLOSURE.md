# E408 Q32 m=10, 3+7, z=3 — residual-degree closure of F/G mismatch

Date: 2026-10-30  
Status: **PROVED_CONDITIONAL local reduction.** It eliminates every nontrivial F/G mismatch in the no-double-track z=3 branch and reduces that branch to aligned profile (2,2,2,1). It does not close the aligned terminal or the double-track branch.

## 1. Inputs

Use the exact dual-fiber partition-pair enumeration in Q32_Z3_DUAL_FIBER_SWITCH_COST_AUDIT.md. The only nontrivial zero-cost mismatch profiles are:
- R=2C3+K1: F=(3,3,1,0), G=(3,2,1,1), with a size-three F-fiber split 2+1;
- R=C3+P4: F=(3,2,2,0), G=(3,2,1,1), with a size-two F-fiber split 1+1;
- R=C3+P4: F=(3,2,2,0), G=(2,2,2,1), with a size-three F-fiber split 2+1.

The valid endpoint-load argument in the dual-fiber audit shows that any completion with F!=G has exactly five zero-cost synchronized-switch outer blocks and two aligned outer blocks. For the five switch blocks, y_D=eta_D=0. For the two aligned blocks, y_D=eta_D=1; they are the endpoints of the unique path component of the outer weighted-heavy graph.

## 2. Equality neighborhoods in the seven outer blocks

For every q in outer block D, the valid incidence inequality is
\[
d_R(q)\ge |G_{g(q)}|+|F_{s(q)}\setminus G_{g(q)}|.
\]
Summing over D gives 7+eta_D, while the exact block ledger gives 7+y_D. In each of the five switch blocks y_D=eta_D=0, so equality holds for every q. The duplicated common fiber F_s is empty, and the two switched tracks are the two G-pieces of the split F_j. Thus each q has exactly its own track G_g as its residual neighborhood; no extra residual incidence occurs in a switch block.

In either aligned endpoint y_D=eta_D=1, equality again holds for every q. The common label j is assigned to one G-piece G_u of F_j, while the empty label s is assigned to the other piece G_v. Therefore the q on track u has residual neighborhood F_j, and the q on track v has residual neighborhood G_v. The two intact fibers match their corresponding tracks exactly.

For r in F_j, the five switch blocks contribute only its one baseline track neighbor. In an aligned endpoint, r gets one extra neighbor precisely when its own G-piece is not the piece assigned common label j. Hence
\[
b_r=\#\{\text{two aligned endpoints that assign }F_j
\text{ to the other G-piece than the one containing }r\}.
\]
The residual degree identity is
\[
d_R(r)+b_r=2.
\]

## 3. Eliminate a 2+1 split

When F_j splits into G-pieces of sizes 2 and 1, eta_D=1 forces each aligned endpoint to assign common label j to the size-two piece; assigning it to the singleton would cost two. Therefore both endpoints choose the same size-two piece.

The residual vertex r in the singleton G-piece then receives one extra incidence in each aligned endpoint, so b_r=2 and d_R(r)=0. But F_j is a clique of size three, so r has at least two neighbors inside F_j. Contradiction.

This eliminates both 2+1 mismatch modes:
- R=2C3+K1, F=(3,3,1,0), G=(3,2,1,1);
- R=C3+P4, F=(3,2,2,0), G=(2,2,2,1).

## 4. Eliminate a 1+1 split

For the remaining mismatch mode, R=C3+P4 and F_j is a K2 split into two singleton G-pieces.

If both aligned endpoints choose the same piece for common label j, the vertex in the other piece gets b_r=2 and d_R(r)=0, contradicting its K2 neighbor.

If the two endpoints choose opposite pieces, each of the two residual vertices gets b_r=1 and hence d_R(r)=1. Since F_j is a K2, each vertex's only residual neighbor is the other one. Thus F_j is an isolated K2 connected component of R. But R=C3+P4 has components of orders 3 and 4, not 2. Contradiction.

Therefore every nontrivial F/G mismatch is impossible:
\[
\boxed{F=G\quad\text{in every no-double-track z=3 completion}.}
\]

## 5. Aligned F=G profiles

Once F=G, the existing aligned-case switch blocker from V47_Z01_TRACK_ALIGNMENT.md applies legitimately. In a synchronized switch, the q-vertex on track j is adjacent to all of F_j by track completeness (G_j=F_j), and to all of F_s by the singleton-track blocker. Since it receives at least two extra Q-Q incidences, its degree identity forces n_s+n_j<=1.

Among the four registered profiles, only (3,3,1,0) permits an empty/singleton switch. That transposition fixes a size-three fiber h. The three small-block vertices and seven outer-track vertices in h form a K10; the three residual vertices in F_h form a K3 adjacent to all ten, yielding a forbidden monochromatic K13.

Profiles (3,2,2,0) and (3,2,1,1) have no switch allowed by n_s+n_j<=1 and also contain a size-three fiber, so they yield K13. Profile (2,2,2,1) has no empty fiber and no size-three fiber; no switch is possible, so all seven outer blocks are aligned.

## 6. Result and open boundary

The no-double-track m=10, 3+7, z=3 branch reduces to
\[
\boxed{F=G,\quad \operatorname{profile}(F)=(2,2,2,1),\quad
\text{all seven outer blocks aligned}.}
\]

The separate double-track branch remains open. The aligned (2,2,2,1) terminal must still be combined with the exact residual graph, three cross-fiber edges, endpoint-load matrix, and outer weighted-heavy graph. Full-support Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.

No retracted degree-nine claim, exceptional-vertex injectivity, Q33 identity, or E407 identity is used.
