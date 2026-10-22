# K4,9 G=2 split residual — decorated-row overlap theorem

Status: `PROVED`.

Continue the unique residual from `K49_G2_SPLIT_CORE_REDUCTION.md`.

Let L be the 17-point remainder. Let P,Q be the two decorated four-side core rows; both have size10. For each of the nine regular vertices y on the nine-side, let `R_y` be its 4-point core row, contained in L.

## 1. Exact q-max inequality for a nine-side row

For y on the nine-side, the missing degree is4 and its missing-neighbour set is the full four-side X. Since the shell is K4,9 with total decoration2,

`t(X)=38=q`, `e_M(X)=0`.

The exact repivot identity gives

`q_y-q = I_H(R_y)-6-38+e_F(X,R_y)`.

Write

`epsilon(R_y)=sum_{u in R_y}(d_H(u)-12)`,
`e_y=e_H(R_y)`.

Because `I_H(R_y)=48+epsilon(R_y)-e_y`, and the two regular four-side rows D1,D2 are disjoint from L, the only X-to-R_y target edges come from the two decorated rows P,Q. Therefore

`e_F(X,R_y)=|R_y intersect P|+|R_y intersect Q|`.

Since p is q-maximal with q=38,

`q_y-q<=0`,

so

`e_y >= 4 + epsilon(R_y) + |R_y intersect P| + |R_y intersect Q|`.   (ROW)

## 2. Each Y-row has at most two decorated-row incidences

A 4-point induced graph has at most6 edges. Hence (ROW) implies

`epsilon(R_y)+|R_y intersect P|+|R_y intersect Q| <=2`.

In particular

`|R_y intersect P|+|R_y intersect Q| <=2`.

Membership in `P intersect Q` is counted twice in this inequality.

Thus each 4-row has at least two vertices outside `P union Q`.

## 3. The two decorated 10-rows overlap in at least five vertices

Put

`r=|P intersect Q|`.

Since |P|=|Q|=10 inside |L|=17,

`|L\(P union Q)| = 17-(20-r)=r-3`.

Each of the nine rows R_y contributes at least two incidences to this complement, for at least18 incidences total. A single L-vertex can belong to at most all nine Y-rows. Therefore the complement must contain at least two vertices:

`r-3>=2`.

Hence

`|P intersect Q|>=5`.

The final residual therefore satisfies

`5<=|P intersect Q|<=10`,

and every Y-row has decorated-row membership count at most2.

This is a strict refinement of the 17-point residual interface. It does not yet close the final G=2 split K4,9 family.
