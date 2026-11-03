# Focused COVER attack: q27/q28 B1 and triangle-channel stress test

Date: 2026-11-03  
Frozen COVER source: `frozen/cover/COVER_THEOREM.md` at integration commit `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.

## Verdict

**NO GAP FOUND** in the q27/q28 bipartite classification or the B1 row-class contradiction after expanding the compressed cross-class nonadjacency step. A near-counterexample to the triangle single-edge case was constructed, but it violates the independent triangle row-union bound and is therefore not a legal witness.

## 1. Adversarial near-counterexample to the triangle single-edge case

I tried to defeat Section5's single-edge B case by constructing a 13-vertex M with:
- T={w,x,y} a triangle;
- one B-edge ab;
- a adjacent to {w,x}, b adjacent to {w,y};
- seven other B-vertices adjacent to {w,y}, and one isolated B-vertex.

Set weights:
`(t_w,t_x,t_y)=(11,3,10)`, `(t_a,t_b)=(9,3)`, seven row weights2, one row weight0.

This candidate has:
- `z=e(M)=22`;
- `q=z+G=28`;
- `alpha(M)=10`;
- `omega(M)=3`;
- every M-edge satisfies `t_u+t_v>=12`.

It looks dangerous if one checks only EDGE12 and the q budget. But it fails the separate triangle-row lower bound:
`t_a+t_w+t_x=9+11+3=23<24`.

The source's two extra triangle constraints close this loophole. Since N_T(a) and N_T(b) are distinct 2-subsets (otherwise {a,b} plus the common T-edge is a K4), write them as {w,x} and {w,y}. The triangles {a,w,x} and {b,w,y} each have row sum at least24:
`t_a+t_w+t_x>=24`,
`t_b+t_w+t_y>=24`.
Together with `t_a+t_b=12` and `t_w+t_x+t_y=24`, this gives `t_w>=12`. EDGE12 on xy gives `t_x+t_y>=12`, hence `t_w<=12`. Therefore
`t_w=12,quad t_x=t_b,quad t_y=t_a`.
Since `t_a,t_b<=9`, the eight other B-vertices can meet only w by EDGE12, contributing at most8 edges. Then
`z<=3+1+4+8=16`,
contradicting z>=22. The constructed candidate is therefore excluded by a genuinely load-bearing condition, not by a bookkeeping artifact.

## 2. B1 nonadjacency step: explicit derivation

The q28 B1 states have hub weights (9,9,10), and q27 states have (9,9,9); all low rows are full or empty, with full-row count k in {8,9}. For every K-point v, its shell q_v is27 or28 because the energy-independent q>=27 result applies and Q=28. Since all other K-points are regular, no decorated low is allowed; hence only q27 or B1 states occur. Thus every T_v is a triangle, and the row class multiplicity is
`c=11-k in {2,3}`.

Fix a row class i and a base point x in T_i whose shell weight is9. In the shell at a representative p_i of that class, its M-degree is `11-c`, so
`9=t_x=d_M(x)+g_x=11-c+(d_F(x)-13)`,
hence
`d_F(x)=c+11`.

Now take a pivot p_j in a different row class j. Because T_i and T_j are disjoint and p_j's outside neighborhood is exactly T_j, x is nonadjacent to p_j and lies in the 47-core C_{p_j}. Its only neighbors in K are the c vertices of class i, and the only other deleted vertices are T_j. Therefore
`d_{C_{p_j}}(x)=d_F(x)-c-e_F(x,T_j)=11-e_F(x,T_j)`.
Every actual47-core has minimum degree at least11, so `e_F(x,T_j)=0`. In particular x is anticomplete to every vertex of T_j.

This works for every ordered pair of distinct row classes. Hence distinct row triangles are pairwise anticomplete. Now fix p in one class i0. Choose base points x,y from two other distinct classes i,j. Both are in C_p and the same formula gives
`d_{C_p}(x)=d_{C_p}(y)=11`.
They are nonadjacent because the previous argument, applied with a pivot in class j, shows x is anticomplete to T_j, which contains y. But degree-11 vertices in any actual47-core must form a clique. Contradiction.

Thus the phrase “nonadjacent by the same formula” in COVER Section7.2 is compressed but valid: the nonadjacency is obtained by applying the core-degree formula with a pivot from the other base point's row class. No missing premise remains.

## 3. Independent q27/q28 enumeration

A separately written enumerator, `RECHECK_COVER_Q27_Q28_INDEPENDENT.py`, was run against the necessary shell conditions:
- all 19,448 row multiplicity vectors;
- z>=22 and Hall's seven inequalities;
- all integer decoration distributions over the three hubs and ten low rows;
- EDGE12 on every M-edge;
- INS11 for every regular pivot;
- direct verification of all 8,192 subset identities for each retained state.

It reproduces exactly:
- q=27: 2 canonical states;
- q=28: 8 canonical states.

The state lists match the five-row table in COVER Section6. This independently supports the completeness of the finite classification; it does not replace the analytic reduction to the bipartite 3+10 channel.

## 4. Disposition

- Triangle single-edge near-witness: **REJECTED** by the triangle row-union bound.
- B1 cross-row anticompleteness: **PROVED** from the 47-core minimum-degree11 lemma.
- q27/q28 canonical state enumeration: **REPRODUCED** independently, 2 and8 states.
- No fatal or repairable gap found in these attacked subclaims.

The frozen COVER source is unchanged. This remains a focused attack, not whole-proof certification.


## 5. Q30 K4 terminal: expand the equality case

The K4 branch in Section10 is valid, but its compressed equality chain is worth making explicit.

Let S be a K4 in M and B=A\\S (nine vertices). Since M is the complement of F[A], S is independent in F. The common antineighborhood of S in the 47-core C is a clique: two nonadjacent vertices there, together with S, would be an independent6-set in F. As omega(F)<=11, this common antineighborhood has size at most11. Hence the union of the four C-neighborhood rows has size at least36, so t(S)>=36. Equation(1), q=30 and e_M(S)=6 give
`30=t(S)-6+e_M(B)+G_B`,
forcing t(S)=36, e_M(B)=0 and G_B=0. Thus B is independent and all nine B-vertices are regular.

There can be no K5 in M: a K5 is an independent5-set in F, so its common antineighborhood in C is empty (else alpha(F)>=6). Its row union has size47, and equation(1) would give q>=47-10=37. Therefore every b in B has at most3 neighbors in S. In the no-regular-middle-degree branch, each b is regular, so d_M(b)<=2. But z>=22 and e_M(S)=6 imply e(S,B)=z-6>=16. The nine B-degrees sum to at least16, so some regular y in B has d_M(y)=2.

Its two neighbors s1,s2 lie in the clique S, so e_M(N_M(y))=1. Each s in S has t_s<=12 because S\\{s} is an M-triangle with row sum at least24, while t(S)=36. Equation(1) gives
`30=t_{s1}+t_{s2}-1+rho`,
so rho=31-(t_{s1}+t_{s2}) and rho>=7. Formula(3) at beta12 yields
`q_y=22+rho+h_12+kappa+b >= 53-(t_{s1}+t_{s2}) >=29`.
Since q_y<=Q=30, its new core has E-91-q_y in {287,288} edges and therefore minimum degree12 by Section8. Each inserted s_i has new-core degree
`d_{C_y}(s_i)=t_{s_i}-e_F(s_i,D_y)`,
because s1,s2 are nonadjacent in F (they are adjacent in M). Thus t_{s_i}>=12; combined with t_{s_i}<=12, both equal12. The other two vertices of S then have total weight 36-24=12, contradicting EDGE13 on their M-edge. This closes the K4 branch.

The attempted near-witness above is therefore not merely blocked by an unexplained status label: the row-union bound, K5 exclusion, degree-2 regular point, and beta12 repivot form an explicit chain.

## 6. Cross-row anticompleteness in Q30 Families I and II

The Family I and II exclusions use the same general mechanism, and the pivot must be chosen from the *other* row class.

- **Family I:** for x in a multiplicity-c row triangle T_i, the shell hub weight10 gives d_F(x)=c+12. For a pivot p_j in a different row class j, x lies in C_{p_j}, and
  `d_{C_{p_j}}(x)=d_F(x)-c-e_F(x,T_j)=12-e_F(x,T_j)>=12`.
  Hence e_F(x,T_j)=0. Distinct row triangles are pairwise anticomplete. This licenses both the independent-set argument for r=5 and the common avoiding-point argument for r=4.
- **Family II:** for x in T_i, d_F(x)=13 and it is adjacent to v_i alone in K. For p_j in another class, x lies in C_{p_j} and
  `d_{C_{p_j}}(x)=13-1-e_F(x,T_j)>=12`,
  so T_i and T_j are anticomplete. The ten disjoint pairs then give an independent10-set.

The use of the core minimum-degree12 is licensed because the repivoted cores have 287 or288 edges in the E408 setting. No edge bound is silently transported to an arbitrary 47-core.
