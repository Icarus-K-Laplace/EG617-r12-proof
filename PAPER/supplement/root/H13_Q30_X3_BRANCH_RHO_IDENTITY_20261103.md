# H13 Q30: explicit |X|=3 rho identity and branch-closure attack

Date: 2026-11-03  
Frozen source: `frozen/cover/COVER_THEOREM.md`, Section10, snapshot `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.

## Why this branch matters

The cross-missing-edge near-witness recorded in `H13_Q30_FAMILY_I_II_ADVERSARIAL_RECHECK_20261103.md` falls into `|X|=3`. The source eliminates this branch by saying that every regular outside point has `q_y>=31`. This note expands that exact rho calculation; it is the load-bearing reason the apparent alternative cannot escape the `|X|=2` normal form.

## Derivation

Let X={a,b,c} be the three weight-11 points. Equality in the subset identity forces X to be a triangle, the other ten points R to be independent and regular, and all ten to have missing degree exactly2:
- K4-freeness bounds each R-degree by2;
- degree1 violates EDGE13 because every X-point has weight11;
- z>=22 and e_M(X)=3 require at least19 cross incidences, while ten R-points contribute at most20.

Every y in R therefore has one of the three pair types ab, ac, bc. Write their multiplicities n_ab,n_ac,n_bc. The three X-vertices have M-degrees
$$
d_M(a)=2+n_{ab}+n_{ac},\
d_M(b)=2+n_{ab}+n_{bc},\
d_M(c)=2+n_{ac}+n_{bc}.
$$
Since t_a=t_b=t_c=11 and decorations are nonnegative, each degree is at most11. This forces all three pair types to occur (otherwise one hub has degree12).

Fix y of type ab. Its missing neighborhood S={a,b}; the complement A\\S consists of y, c, and the other nine R-points. Let
$$
r_c=n_{ac}+n_{bc}=10-n_{ab}
$$
be the number of those other points adjacent to c. There are no edges among R, and y is not adjacent to c. Thus
$$
e_M(A\\S)=r_c.
$$
Also
$$
g_c=11-d_M(c)=11-(2+r_c)=9-r_c,
$$
and every other vertex in A\\S is regular. Hence
$$
\rho=e_M(A\\S)+G_{A\\S}=r_c+(9-r_c)=9.
$$
The same argument applies symmetrically to every outside point, whatever its pair type. Formula (3) at beta12 and d=2 now gives
$$
q_y=2(13-2)+\rho+h_{12}+\kappa+b
\ge22+9=31,
$$
contradicting Q=30.

## Independent finite replay

`RECHECK_H13_Q30_X3_BRANCH.py` enumerates all positive integer triples (n_ab,n_ac,n_bc) summing to10: 36 distributions. For each it checks the three hub-degree bounds, the exact decoration identity, and q_y>=31. No distribution evades the charge.

## Disposition

The |X|=3 branch correctly blocks the cross-missing-edge near-witness. No gap found in this branch's rho calculation. The script is a finite arithmetic replay, not a substitute for the graph-theoretic equality reduction or whole-proof certification.
