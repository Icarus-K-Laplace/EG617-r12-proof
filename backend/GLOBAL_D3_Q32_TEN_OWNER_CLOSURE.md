# Global d=3 q32 Ten-Owner Closure Theorem

Status: `PROVED_ANALYTIC` under the retained r=12 residual/core/hereditary contracts.

Dependencies:

- `GLOBAL_D3_Q32_MULTI_S_EXTRACTION_THEOREM.md`;
- `GLOBAL_COMMON_S_OWNER_CLIQUE_THEOREM.md`;
- `GLOBAL_SUBCRITICAL_ALLOWANCE_DECOMPOSITION.md`;
- `GLOBAL_PLATEAU_CAPACITY_THEOREM.md`;
- common-S row closure;
- inherited caps `D(14)=69`, `D(17)=81`, `D(20)=102`;
- `alpha(H)<=3`, `omega(F)<=11`.

Purpose: show that the abstract q32 d3 owner-clique upper bound10 is never attained. This is a complete global closure obtained from the unified compatibility machinery, not from a ten-view enumeration.

## 1. Assume ten simultaneous q32 d3 owners

Let p be a maximal pivot with

`q=32`,

and suppose there are ten simultaneous regular shell vertices

`Y={y_1,...,y_10}`

with missing/support size3.

`GLOBAL_D3_Q32_MULTI_S_EXTRACTION_THEOREM.md` shows any simultaneous d3 owner family is a target clique.

Hence Y is a target K10.

The 13-shell has only three vertices outside Y. Every missing set S_y has size3 and avoids all owners because owners are mutually target-adjacent. Therefore every row has the same missing triple

> `S=A\Y`.                                                    (T1)

Thus the ten-owner state is automatically common-S.

Together with p,

`B={p} union Y`

is a target K11.

## 2. Exact shell budget

Every owner misses all three vertices of S, contributing

`3*10=30`

shell missing edges.

There is no leftover shell block T. Hence

`e(M)=30+e_M(S)`.                                            (T2)

Since

`q=e(M)+G_A=32`,

> `e_M(S)+G_A=2`.                                            (T3)

In particular

`G_A<=2`,

so the three-point missing set cannot be fully decorated:

> `s=|S intersect X|<=2<3`.                                  (T4)

The common-S row allowance is exactly

> `a=q-3(13-3)=32-30=2`.                                    (T5)

Therefore the system lies in the subcritical regime `a=d-1`.

## 3. Global decomposition

By `GLOBAL_SUBCRITICAL_ALLOWANCE_DECOMPOSITION.md`:

1. plateau owners are singleton support classes;
2. there are at most3 plateau owners;
3. every strict-loss support is disjoint from every distinct support class;
4. two distinct strict supports have at most one target cross-edge;
5. the distinct strict support classes number at most3.

Let

`P=# plateau owners`,
`L=10-P`.

Then

> `P<=3`, `L>=7`.                                            (T6)

Let the distinct strict support classes be

`D_1,...,D_k`,

with multiplicities

`m_1,...,m_k`,

so

`1<=k<=3`,
`sum m_i=L`.                                                  (T7)

Every strict row has q-loss at least1, so with allowance2 its support defect satisfies

`w(D_i)+mu(D_i)<=1`.                                         (T8)

Hence every strict support has

> `e_H(D_i)>=2`.                                             (T9)

A repeated strict support has all three support points decorated and is subject to the canonical K11+D hereditary cap:

`55+3m_i+e_H(D_i)<=69`.

Using (T9):

> every repeated strict class has `m_i<=4`.                  (T10)

## 4. One strict class is impossible

If k=1, then the single strict support has multiplicity

`m_1=L>=7`,

contradicting (T10).

Therefore

> `k>=2`.                                                     (T11)

## 5. Two strict classes force the 4+3 terminal

Assume k=2.

Both classes must repeat because `L>=7` and each repeated class has multiplicity at most4. Hence

`L=7`,
`P=3`,

and after relabelling

> `(m_1,m_2)=(4,3)`.                                         (T12)

The two strict supports D,E are disjoint.

Apply the hereditary D17 cap to

`B union D union E`.

The induced set contains exactly/certifiably:

- 55 edges in B=K11;
- `3*(4+3)=21` owner-support edges;
- at least2 internal edges in each support;
- nonnegative D--E cross edges.

Thus

`55+21+e_H(D)+e_H(E)+e_H(D,E)<=81`,

or

> `e_H(D)+e_H(E)+e_H(D,E)<=5`.                              (T13)

Each internal count is at least2.

If both had only2 internal edges, then both supports contain an internal target-nonedge pair. Their cross-edge count is zero because two-edge strict supports have `mu=1`, so (T8) forces `w=0`, and row closure gives zero cross edges. Choosing one nonedge pair from each support gives an independent4-set, impossible.

Therefore exactly one support is a target K3 and the other is a two-edge triple; the cross-edge count is zero. More explicitly, after relabelling:

> `e_H(D)=2`, `w(D)=0`,                                     (T14)
>
> `e_H(E)=3`, `e_H(D,E)=0`.                                 (T15)

The multiplicity-4 support cannot be E=K3, because D14 would give

`55+12+3=70>69`.

Hence the multiplicities align as

> D: multiplicity4, two-edge, zero charge;
>
> E: multiplicity3, target K3.                               (T16)

Now use any plateau row. By P=3, such a row exists.

The plateau-capacity theorem supplies a private clean zero-charge witness z in its support.

Since z lies outside the distinct strict supports D,E, row closure gives

`e_H(z,D)=e_H(z,E)=0`.                                       (T17)

Choose an internal target-nonedge pair `{u,v}` in the two-edge support D and any point `e in E`.

By (T15)--(T17), every pair among

`{u,v,z,e}`

is a target nonedge.

This is an independent4-set in H, contradiction.

Therefore

> `k!=2`.                                                     (T18)

## 6. Three strict classes cannot coexist with a plateau row

Hence k=3.

Suppose P>=1 and let z be a private clean zero-charge plateau witness.

Because every strict support D_i is distinct from the plateau support, subcritical isolation gives disjointness, and row closure gives

`e_H(z,D_i)=0`

for all i.

The three strict supports are pairwise-disjoint 3-blocks with at most one target cross-edge between each pair.

Choose one vertex uniformly from each D_i. The expected number of target edges among the chosen triple is at most

`3*(1/9)=1/3<1`.

Hence some transversal `{u_1,u_2,u_3}` is target-independent.

Together with z, which is target-anticomplete to all three supports, this gives an independent4-set.

Contradiction.

Therefore

> `P=0`, `L=10`.                                             (T19)

All ten owners are strict.

## 7. Multiplicity partitions with three strict classes

We have

`m_1+m_2+m_3=10`.

No class can be singleton. Indeed if one multiplicity were1, the other two would sum9, but each repeated class has multiplicity at most4 by (T10), giving total at most8.

Thus every class repeats and

`2<=m_i<=4`.

The only unordered partitions of10 are

> `(4,4,2)` or `(4,3,3)`.                                    (T20)

For any multiplicity-4 support D, D14 and (T9) force

`55+12+e_H(D)<=69`,

hence

> `e_H(D)=2`.                                                (T21)

By (T8), such a support has

`mu(D)=1`, `w(D)=0`.                                        (T22)

Therefore a multiplicity-4 class is a zero-charge two-edge triple and is target-anticomplete to every distinct strict support by row closure.

## 8. Partition 4+4+2 is impossible

Take the two multiplicity-4 supports D,E.

Both are zero-charge two-edge triples by (T21)--(T22), so

`e_H(D,E)=0`.

Choose one internal target-nonedge pair from D and one from E.

All four selected vertices are pairwise target-nonadjacent, giving an independent4-set.

Contradiction.

Therefore

> `(4,4,2)` is impossible.                                   (T23)

## 9. Partition 4+3+3 is impossible

Let D be the multiplicity-4 support. It is a zero-charge two-edge triple and is target-anticomplete to both other supports E,F.

If E or F were also a two-edge support, then its defect bound would force zero charge, and the same two-nonedge-pair argument with D would give an independent4-set.

Hence both E and F must be target K3s.

Their cross-edge count satisfies

`e_H(E,F)<=min(w(E),w(F))<=1`.                               (T24)

Among the nine pairs in `E x F`, at most one is a target edge. Therefore choose

`e in E`, `f in F`

with ef a target nonedge.

Choose an internal target-nonedge pair `{u,v}` in D.

Because D is target-anticomplete to E and F, the four vertices

`{u,v,e,f}`

are pairwise target-nonadjacent.

Again this is an independent4-set, contradiction.

Thus

> `(4,3,3)` is impossible.                                   (T25)

## 10. Conclusion

All possible strict-class counts have been excluded.

Therefore:

> **Global q32 d3 ten-owner closure.**
>
> A maximal q32 pivot in the retained r=12 backend cannot have ten simultaneous regular d3 owner rows.   (T26)

Combining with the owner-clique upper bound gives the sharpened simultaneous-owner capacity

> **`N_d3(q32)<=9`.**                                        (T27)

No computer enumeration is used.

## 11. Structural meaning

The proof is a direct application of the unified architecture:

1. maximal owner count automatically creates one common missing triple;
2. q-budget forces subcritical allowance and non-full decoration;
3. plateau capacity bounds exceptional rows;
4. strict supports become isolated low-cross blocks;
5. hereditary packing restricts repeated multiplicity;
6. the only equality partitions create forbidden independent4-sets.

Thus a former multi-view boundary is closed by one global support theorem rather than ten local row cases.

## 12. Higher-r template

The same proof pattern extends whenever a higher-r pivot system has:

- owner clique saturation at maximal owner count;
- q-budget forcing subcritical allowance;
- a plateau-capacity theorem;
- hereditary bounds for the canonical owner-clique base plus support blocks;
- a small core independence number.

The numerical partitions and cap values are r=12-specific, but the architecture is reusable.