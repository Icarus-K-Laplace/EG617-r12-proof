# q36 f=2, 2K1 far, a_F=1 — full elimination of all repeated supports in c=7,A=3

Status: `PROVED` under `Q36_F2_2K1_A1_C7_A3_REPEATED_SUPPORT_RIGIDITY.md`, row closure, CORE211, and `alpha(F)<=4`.

This closes the last possible repeated-support branch. Hence every surviving support in c=7,A=3 would have to be a distinct singleton support.

## 1. Exact repeated-support state

By the repeated-support rigidity theorem, if a repeated support D exists then

- D is a target K3;
- it is the unique repeated support class;
- `e_F(Y,D)=0`;
- the other five owner incidences each meet D exactly once.

Let

`L=R\D`, so `|L|=9`.

The far regular vertices a,b form a target nonedge. Since R is the 12-point remainder outside their core supports, both a and b are target-anticomplete to R. In the `a_F=1` branch, x0 is the unique decorated shell vertex with a far target neighbour, so the inactive set Y is target-anticomplete to both a and b.

Moreover `e_F(Y,D)=0`, so D and Y are target-anticomplete K3 blocks.

## 2. Every v in L must cover the D--Y K3,3 nonedge graph

Fix `v in L`.

Suppose there existed `d in D` and `y in Y` such that v were target-nonadjacent to both d and y.

Then

`{a,b,v,d,y}`

would be an independent5-set:

- ab is a target nonedge;
- a,b are target-anticomplete to v,d because all three lie in R;
- a,b are target-anticomplete to y because y is inactive;
- dy is a target nonedge because `e_F(Y,D)=0`;
- vd and vy are target nonedges by assumption.

This contradicts `alpha(F)<=4`.

Therefore `N_F(v) intersect (D union Y)` is a vertex cover of the complete bipartite nonedge graph K3,3 between D and Y. Its minimum vertex-cover size is3, so

> `e_F(v,D)+e_F(v,Y)>=3` for every v in L.                (1)

Summing over the nine vertices of L,

> `e_F(L,D)+e_F(L,Y)>=27`.                                 (2)

## 3. Row closure and the small Y core rows give an upper bound23

For v in L, row closure against the repeated support D gives

`e_H(v,D)<=kappa_v+e_F(v,x0)`,

because every vertex of R is target-nonadjacent to the far pair.

Hence

`e_H(L,D)<=kappa(L)+e_F(x0,L)<=2+9=11`,                   (3)

using CORE211 and |L|=9.

Now consider the three inactive shell vertices Y. Each has global decoration1. In the c=7,A=3 normal form, a vertex y in Y has shell missing degree

`2 + 1_{yx0 in M}`,

so its core row has size

`3 + 1_{yx0 in M}`.

Summing over Y gives total core degree

`sum_(y in Y)|N_H(y)| = 9+nu_0 <=12`.                     (4)

Since Y is target-anticomplete to D, all Y--R edges available to D union L actually lie in L. Therefore

`e_F(Y,L)<=12`.                                             (5)

Combining (3) and (5),

`e_F(L,D)+e_F(L,Y)<=11+12=23`,

contradicting the lower bound27 in (2).

## 4. Conclusion

No repeated support can exist in the c=7,A=3 terminal.

Therefore the only remaining owner partition is

> `1+1+1+1+1+1+1`:
> all seven 3-supports are distinct singleton supports.

The next task is the final simple 7-triple compatibility problem on the 12-point alpha-two remainder.