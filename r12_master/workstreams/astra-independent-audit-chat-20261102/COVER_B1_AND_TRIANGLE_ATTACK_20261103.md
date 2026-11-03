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
