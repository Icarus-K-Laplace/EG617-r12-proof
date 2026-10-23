# Global d=3 q32 Nine-Owner Decorated-Escape Theorem

Status: `PROVED_ANALYTIC` under the retained r=12 contracts and the source-reported q32/CORE211 channel for the final non-full-decoration exclusion.

Dependencies:

- `GLOBAL_D3_Q32_MULTI_S_EXTRACTION_THEOREM.md`;
- exact d3 exchange identity;
- `GLOBAL_SUBCRITICAL_ALLOWANCE_DECOMPOSITION.md`;
- `GLOBAL_PLATEAU_CAPACITY_THEOREM.md`;
- `GLOBAL_COMMON_S_CHARGE_LOCALIZATION.md`;
- common-S row closure;
- inherited caps `D(14)=69`, `D(17)=81`;
- `alpha(H)<=3`.

Purpose: classify the next q32 d3 owner-count boundary after the ten-owner closure. Nine simultaneous owners are forced into one common missing triple, and in the CORE211 channel every non-fully-decorated state is impossible. Thus the only nine-owner escape is full decoration of the missing triple.

## 1. Nine simultaneous d3 owners form a clique

Let p be a maximal q32 pivot and let

`Y={y_1,...,y_9}`

be nine simultaneous regular d3 shell owners.

The q32 multi-S theorem shows that any two simultaneous d3 owners are target-adjacent. Hence

> `Y=K9`.                                                     (N1)

Put

`Q=A\Y`, so `|Q|=4`.

Every missing triple S_y avoids every other owner, therefore

> `S_y subset Q`, `|S_y|=3`.                                (N2)

For each y there is a unique point

`r_y in Q\S_y`.                                              (N3)

Call r_y the type label of y.

## 2. q32 forces all nine rows to have the same type

Fix y and write r=r_y.

The shell block remaining after deleting y and S_y is

`T_y=(Y\{y}) union {r}`.                                    (N4)

The exact d3 exchange formula is

`q_y=30+B_y+nonnegative support defect terms`,               (N5)

where

`B_y=e_M(T_y)+G_(T_y)`.                                     (N6)

Since p has maximum q=32,

`q_y<=32`,

so

> `B_y<=2`.                                                   (N7)

Let

`n_r=#{z in Y:r_z=r}`.

Among the eight other owners z, the edge zr is a shell missing edge exactly when

`r in S_z`,

i.e. exactly when

`r_z!=r`.

Therefore T_y contains at least

`8-(n_r-1)=9-n_r`

missing edges incident with r. Hence

> `B_y>=9-n_r`.                                              (N8)

Combining (N7)--(N8):

> every type which occurs satisfies `n_r>=7`.                (N9)

Two distinct types cannot both occur because their counts would sum to at least14>9.

Thus:

> **all nine owners have the same type r and hence the same missing triple**
>
> `S=Q\{r}`.                                                  (N10)

So the N=9 boundary is automatically common-S; no common-S assumption is needed.

## 3. Canonical K11 dense base

All owners are target-adjacent to r because r is excluded from their common missing triple S.

Hence

`B={p} union Y union {r}`

is a target K11.                                             (N11)

The common-S leftover block is the singleton

`T={r}`.

Its common row allowance is

`a=q-30-G_r=2-g_r<=2`.                                      (N12)

## 4. Assume the missing triple is not fully decorated

Assume

`s=|S intersect X|<3`.                                      (N13)

Then the subcritical decomposition applies.

Let P be the number of plateau owners and L=9-P the strict owners.

Plateau capacity gives

> `P<=3`, `L>=6`.                                            (N14)

Every strict support is disjoint from every distinct support class. Distinct strict supports have at most one target cross-edge.

By the d3/cross-one block-transversal theorem there are at most three distinct strict support classes.

Let their multiplicities be `m_1,...,m_k`, where

`1<=k<=3`,
`sum m_i=L`.                                                  (N15)

Every strict support has defect at most1, hence

> `e_H(D_i)>=2`.                                             (N16)

The canonical K11 base plus a repeated strict support gives from D14

`55+3m_i+e_H(D_i)<=69`,

so every repeated strict class satisfies

> `m_i<=4`.                                                   (N17)

## 5. One strict class is impossible

If k=1 then

`m_1=L>=6`,

contradicting (N17).

Thus

> `k>=2`.                                                     (N18)

## 6. Two strict classes are impossible

Assume k=2.

If one class were singleton, the other would have multiplicity at least5 because L>=6, contradicting (N17). Hence both classes repeat and each has multiplicity at most4.

Therefore

`L<=8`,

so

> `P>=1`.                                                     (N19)

Let z be a private clean zero-charge witness from any plateau row. By row closure and strict-support disjointness,

`e_H(z,D_1)=e_H(z,D_2)=0`.                                  (N20)

If either strict support has only two internal target edges, it contains an internal nonedge pair `{u,v}`. The other 3-support contains a vertex e target-nonadjacent to both u and v because there is at most one cross target edge between the two supports.

Together with z, the four vertices `{u,v,e,z}` are target-independent, contradiction.

Therefore both strict supports would have to be target K3s.

If P>=2, choose two plateau witnesses z_1,z_2. They are target-nonadjacent to each other and anticomplete to both strict supports. Since the two K3 supports have at most one cross edge, choose `u in D_1`, `v in D_2` with uv a target nonedge. Then

`{z_1,z_2,u,v}`

is independent4, contradiction.

Hence P=1 and L=8.

Both strict classes repeat, have multiplicity at most4, and sum to8, so

`(m_1,m_2)=(4,4)`.                                          (N21)

But a multiplicity-4 strict target K3 violates D14:

`55+12+3=70>69`.

Contradiction.

Therefore

> `k!=2`.                                                     (N22)

## 7. Three strict classes force zero plateau rows

Hence k=3.

If P>=1, take a plateau witness z. It is target-anticomplete to every strict support.

The three strict supports are pairwise-disjoint 3-blocks with at most one target cross-edge per pair.

Restrict to one uniformly chosen vertex from each support. The expected number of target edges is at most1/3, so an independent transversal of the three blocks exists.

Together with z this gives an independent4-set.

Therefore

> `P=0`, `L=9`.                                              (N23)

All nine owners are strict.

## 8. Multiplicity partitions

The three positive multiplicities sum to9.

Every repeated class has multiplicity at most4.

The possible unordered partitions are

- `(4,4,1)`;
- `(4,3,2)`;
- `(3,3,3)`.

### 8.1 Partition 4+4+1

Each multiplicity-4 support D satisfies

`55+12+e_H(D)<=69`,

so `e_H(D)=2`.

Its strict defect is at most1, hence `w(D)=0`. Two such supports are target-anticomplete by row closure. Choosing an internal nonedge pair from each gives an independent4-set.

Impossible.

### 8.2 Partition 4+3+2

The multiplicity-4 support D is again a zero-charge two-edge triple and is target-anticomplete to both other supports.

If either other support has only two internal edges, its internal nonedge pair together with one from D gives an independent4-set.

Hence the other two supports E,F must both be target K3s.

They have at most one target cross-edge. Choose `e in E`, `f in F` with ef a target nonedge, and choose an internal nonedge pair `{u,v}` in D. Since D is anticomplete to E and F,

`{u,v,e,f}`

is independent4.

Impossible.

### 8.3 Partition 3+3+3

If at least one support is a two-edge triple D, then `w(D)=0` and D is target-anticomplete to the other two supports.

- if another support is also two-edge, the two internal nonedge pairs give independent4;
- if the other two are K3s, choose a target-nonedge cross pair between them (there is at most one cross edge) and combine it with an internal nonedge pair of D to get independent4.

Thus the only remaining possibility is:

> all three multiplicity-3 supports are target K3s.           (N24)

For each such support, strict defect <=1 gives

`w(D_i)<=1`.                                                 (N25)

## 9. The all-K3 3+3+3 terminal is impossible in CORE211

Now use the source-reported CORE211 channel:

`K=2`, `q=32`.

The common-S charge-localization theorem gives

`W<=K+q+C(3,2)=37`.                                         (N26)

The three K3 supports occupy nine core vertices and carry total charge at most3 by (N25).

There are 26 core vertices outside their union. If every outside vertex had charge at least2, then

`W>=26*2=52`,

contradicting (N26).

Hence some outside core vertex z satisfies

> `w_z<=1`.                                                   (N27)

Row closure gives

`e_H(z,D_i)<=1`

for each of the three K3 supports.

Therefore each D_i contains at least two vertices target-nonadjacent to z.

Choose a two-point subset `A_i subset D_i` of z-nonneighbours for each i.

Between any two supports there is at most one target cross-edge. Among the `2*2*2=8` triples in

`A_1 x A_2 x A_3`,

a single cross edge between a support pair can forbid at most2 triples. There are at most three support-pair cross edges total, so at most6 of the eight triples are forbidden.

Thus there exists

`(u_1,u_2,u_3) in A_1 x A_2 x A_3`

which is target-independent.

Each u_i is also target-nonadjacent to z. Hence

`{z,u_1,u_2,u_3}`

is an independent4-set in H.

Contradiction.

Therefore the 3+3+3 terminal is impossible.

## 10. Non-full-decoration conclusion

All possible strict-class systems have been excluded.

Hence, under q32/CORE211:

> a nine-owner simultaneous d3 system cannot satisfy `|S intersect X|<3`.   (N28)

Combined with Section2:

> **Nine-Owner Decorated-Escape Theorem.**
>
> Every simultaneous nine-owner q32 d3 survivor in the CORE211 channel must have one common missing triple S and that triple must be fully decorated:
>
> `S subseteq X`.                                            (N29)

Thus the maximal remaining owner-count boundary is not a generic multi-view system; it is exactly the fully-decorated escape regime of the Global Support-Compatibility V2 theorem.

## 11. Consequences

Together with `GLOBAL_D3_Q32_TEN_OWNER_CLOSURE.md`:

- ten simultaneous q32 d3 owners are impossible;
- nine owners, if they exist, are one common-S fully-decorated equality state;
- any genuinely multi-S q32 d3 system has at most eight owners, or lies at lower owner count before the same bounded-transversal machinery is applied.

This substantially shrinks the d3 multi-view bridge.

## 12. Generalization template

The type-concentration step uses only:

- owner clique structure;
- small complement `A\Y`;
- the exact B_y term in the exchange formula.

The non-full-decoration closure uses the subcritical decomposition, hereditary owner-clique packing and a small core independence number. The same architecture is applicable at maximal or near-maximal owner counts in higher-r pivot systems.