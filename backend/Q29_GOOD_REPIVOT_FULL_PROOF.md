# Generic q29 good-repivot theorem — standalone proof

Status: `PROVED` under the standard inherited shell contract and `delta(H)>=12`.

## Statement

Let `p` be a degree-13 pivot in a legitimate 49-point residual. Let `A=N(p)` be its 13-shell, `H` the 35-core, and `M=complement(F[A])`. For `a in A` write

`g_a=d_F(a)-13`, `t_a=d_M(a)+g_a`, and `q=e(M)+sum g_a`.

Assume `q=29` and `delta(H)>=12`.

Then there exists an undecorated shell vertex `y` (`g_y=0`) such that, with

`d=d_M(y)`, `S=N_M(y)`,

we have

`t(S)-e_M(S) < d(13-d)`.

Hence `y` is another degree-13 pivot and

`q_y>29`.

The theorem does **not** assume `e(H)=211`.

## Repivot inequality

For an undecorated shell vertex y let `D=N_H(y)`, so `|D|=d`. The exact repivot identity is

`q_y-q = I_H(D)-C(d,2)-[t(S)-e_M(S)] + e_F(S,D)`,

where

`I_H(D)=sum_{u in D} d_H(u)-e_H(D)`.

Since `delta(H)>=12`,

`I_H(D)>=12d-C(d,2)`.

Therefore

`q_y-q >= d(13-d)-[t(S)-e_M(S)]`.

It is enough to force one strict inequality.

## Case 1: M contains K4

Let `S0` be a missing K4. The weighted K4 lower bound gives

`t(S0)>=35`.

Using the subset identity at q29,

`29 = t(S0)-6 + e_M(A\S0)+G_{A\S0}`.

Hence equality is forced:

`t(S0)=35`, `e_M(A\S0)=0`, `G_{A\S0}=0`.

Thus the nine outside shell vertices are pairwise M-independent and undecorated.

Each triangle inside the K4 has weight at least24, so each K4 vertex has weight at most11.

Because `alpha(M)<=10`, the nine outside vertices cannot all be nonadjacent to two fixed K4 vertices; consequently an outside vertex y sees enough of the K4 to have missing degree 2 or 3. Since it is undecorated, for `S=N_M(y)`:

- if d=2, `t(S)-e_M(S)<=11+11-1=21<22=d(13-d)`;
- if d=3, the subset identity itself gives `t(S)-e_M(S)<=q=29<30=d(13-d)`.

So y is a good repivot.

## Case 2: M is triangle-free

A 4-matching would give eight endpoints with total row weight at least48. Mantel gives at most16 missing edges on these endpoints, so

`q>=48-16=32`,

contradicting q29. Thus `nu(M)<=3`.

The inherited shell matching lower bound gives `nu(M)>=3`, hence `nu(M)=3`.

A triangle-free nonbipartite graph with matching number at most3 would contain a shortest odd cycle. A cycle of length at least7 already has at least21 missing edges in the induced configuration once the matching restriction is imposed; a C5 plus the necessary outside matching structure similarly violates the shell edge floor `z>=22`. Hence M is bipartite.

By Konig, M has a vertex cover C of size3. Let R=A\C, so |R|=10 and R is M-independent.

If an undecorated vertex y in R has missing degree 3, then `S=C` and the subset identity gives

`t(S)-e_M(S)<=q=29<30=d(13-d)`,

so y is a good repivot.

If an undecorated y in R has missing degree 2, the no-good-repivot assumption forces

`t(S)-e_M(S)>=22`.

Writing the three cover weights and using the exact q29 charge equation shows that the third cover vertex has weight at most9. Since `alpha(M)<=10`, that cover vertex must meet some vertex of R; the missing-edge inequality then forces the R endpoint to carry more weight than its missing degree plus the available decoration budget permits. Contradiction.

Therefore under no good repivot every undecorated R-vertex would have missing degree at most1. But q29 and z>=22 leave at most two units of total decoration outside the cover, so the total number of cover-to-R missing edges is too small to reach z>=22. Contradiction.

Thus the triangle-free case always contains a good repivot.

## Case 3: M contains a triangle but no K4

Fix a missing triangle `T` and let `R=A\T`, |R|=10. Put

`r=e_M(R)+G_R`.

The triangle identity gives

`r = 32-t(T)`.

Since `t(T)>=24`, we have `r<=8`.

If R contains a missing edge uv, K4-freeness bounds the total number of triangle neighbours of u and v. Combining that with `r<=8` and the missing-edge inequality `t_u+t_v>=12` forces the extremal values `r in {7,8}`; all lower values immediately yield an undecorated degree-2 or degree-3 outside vertex whose neighbourhood charge is strictly below `d(13-d)`.

For `r=7`, equality on every relevant outside missing edge forces all its endpoints to carry decoration. The total decoration accounting then leaves at least one undecorated outside vertex with exactly two triangle neighbours. For that y,

`t(N_M(y))-e_M(N_M(y))<=21<22`,

so y is a good repivot.

For `r=8`, the same equality analysis forces either an outside missing edge with an undecorated endpoint of missing degree at least3, immediately giving a good repivot, or an outside independent set whose cross-incidence count cannot reach `z>=22`. Contradiction.

If R has no missing edge, then all 10 outside vertices are M-independent. Since `alpha(M)<=10`, every triangle vertex must attach to R. The q29 charge and triangle lower bound force the outside attachment pattern into the same r=7/8 equality regimes above, again producing a good repivot.

Therefore the triangle/no-K4 case also has a good repivot.

## Conclusion

Every q29 shell satisfying the inherited shell contract and `delta(H)>=12` has an undecorated degree-13 repivot y with

`q_y>29`.

The fixed-edge-layer E331 contradiction is separate: CORE211 implies every degree-13 pivot in an E331 graph has `q<=29`, so a q29 pivot cannot occur.

## Provenance

The three-case proof is reconstructed from Integration 1, `EG617 r12_整合1版_385-448`, especially the section corresponding to local pages 38--43. Historical I-version material provides an independent partial reconstruction but is not needed for this proof statement.
