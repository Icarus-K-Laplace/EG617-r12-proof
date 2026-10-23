# q36 f=2, 2K1 far, a_F=1 — full closure of the final c=7,A=3 all-singleton support system

Status: `PROVED` under `Q36_F2_2K1_A1_C7_A3_REPEATED_FULL_CLOSURE.md`, common-S row closure, CORE211, inherited D14, lexicographic q36 maximality, `alpha(F)<=4`, and `alpha(H[R])<=2`.

Together with the A=2 closure and the repeated-support closures, this proves the entire c=7 layer empty.

## 1. Setup

All seven owner supports are distinct singleton 3-subsets of the 12-point remainder R. The inactive shell set Y is a target K3 with decorations `(1,1,1)`, and `{p} union C union Y` is a target K11.

For a support D define its defect

`delta(D)=kappa(D)+m(D)+e_F(x0,D)<=3`,

where `m(D)=3-e_H(D)`.

Its intrinsic charge is

`q_D=33+delta(D)`.

Put

`w_v=kappa_v+e_F(v,x0)`

for v in R. CORE211 gives

`sum_R kappa_v<=2`, hence `sum_R w_v<=14`.

## 2. At most one support can have q=36

Suppose D has q_D=36, so delta(D)=3.

Repivoting at its owner removes the decorated vertex x0 and the two regular far vertices, while retaining the three decorated vertices Y. The original q36 maximum shell has exactly four decorated shell vertices `x0 union Y`. Therefore lexicographic maximality forces the inserted support D to contain at most one globally decorated vertex; at least two vertices of D are globally regular.

A globally regular support vertex u in R must satisfy

- `kappa_u=0`;
- `e_F(u,x0)=0`;
- `e_F(u,Y)=0`;
- u occurs in no other low support.

Thus it is a clean private vertex.

If two q36 supports D,E existed, choose clean private vertices u in D and v in E. Both are target-nonadjacent to every y in Y. If uv were a target nonedge, `{a,b,y,u,v}` would be an independent5-set. Hence uv is a target edge.

But v is core-regular, lies outside D, and is target-nonadjacent to the common missing set `F union {x0}`. Row closure against D gives

`e_H(v,D)<=0`,

contradicting uv being an edge with u in D.

Therefore at most one support has q=36.                    (1)

## 3. All seven supports are pairwise intersecting

At least six supports have q<=35, hence defect at most2.

Let D be any such low-charge support. We claim D cannot be disjoint from any other support E.

- If `e_H(D)=1`, then m(D)=2, so the defect bound forces `kappa(D)=e_F(x0,D)=0`. The disjoint cross allowance is zero; any target-nonedge pair in D together with a vertex of E gives an independent triple.
- If `e_H(D)=2`, its cross allowance is at most1, while the unique target nonedge in D forces all three vertices of E to cover it, requiring at least3 cross edges.
- If `e_H(D)=3`, the cross allowance is at most2. A nonclique E again requires at least3 cross edges. If E is a K3, then the bipartite D--E nonedge graph is K3,3 with at most two edges removed. For the six vertices `L=R\(D union E)`, alpha-two forces each neighbourhood in D union E to cover that bipartite nonedge graph, hence each `v in L` has `w_v>=2`. This gives `sum_L w_v>=12`, while CORE211 and |L|=6 give at most8, contradiction.

Thus every low-charge support intersects every other support. Since there are at least six low supports, all seven supports are pairwise intersecting.      (2)

## 4. In fact no q36 support exists

Assume D is the unique q36 support.

Every one of the six low supports intersects D. Every intersection vertex belongs to at least two supports and is therefore globally decorated. But D contains at most one globally decorated vertex by Section2. Hence all six intersections use the same vertex z in D.

For a low support E meeting D at z, the proper-overlap inequality has cost2 and E has defect at most2. Equality is forced, so the overlap vertex contributes no w-mass:

`w_z=0`.

The other two vertices of D are clean private regular vertices from Section2, hence also have w=0.

Therefore the q36 defect of D is just its internal missing count:

`delta(D)=m(D)`.

But `alpha(H[R])<=2` implies every 3-set spans at least one target edge, so `m(D)<=2`, contradicting `delta(D)=3`.

Hence

> every support has q<=35 and defect exactly2.              (3)

## 5. Every shared support vertex has w=0

Take two supports D,E. They intersect by (2), and both have defect2 by (3).

For a proper intersection of size h=1 or2, the common-S overlap inequality costs

`h(3-h)=2`.

Since the total defect of E is exactly2, equality forces all defect mass to lie outside the intersection plus the internal missing count. Thus every vertex in `D intersect E` has

`w_v=0`.

Therefore

> every vertex of R occurring in at least two supports has w=0.  (4)

Call such vertices shared; all other support vertices are private.

## 6. A nonclique support is impossible

Suppose some support D is nonclique and contains a target-nonedge pair.

Let s be any shared vertex outside D. By (4), w_s=0. Row closure against D gives

`e_H(s,D)=0`.

Then s together with a target-nonedge pair in D is an independent triple in H[R], contradiction.

Hence every shared vertex of the entire seven-support family lies inside D. Let S be the global set of shared vertices. Then `1<=|S|<=3`, every support intersection occurs inside S, and every vertex outside S is private.

### |S|=1

All seven supports contain the unique shared point. The remaining14 support incidences are private and therefore require14 distinct vertices in addition to the shared point, exceeding |R|=12.

### |S|=2

Write S={a,b}. The nonempty subsets `D_i intersect S` are pairwise intersecting. Hence all supports contain one common element, say a. Let k be the multiplicity of b; because b is shared, k>=2.

The number of private incidences is `21-(7+k)=14-k`, so the 12-point bound gives

`2+(14-k)<=12`, hence `k>=4`.

The nonclique support D contains both a,b and one private vertex. Thus

`lambda(D)=7+k+1=8+k`.

For a nonclique triple, each y in Y must meet every internal target-nonedge; in particular `e_F(Y,D)>=3`. D14 gives

`lambda(D)+e_F(Y,D)+e_H(D)<=14`.

Since `e_H(D)>=1`, this yields `8+k+3+1<=14`, hence k<=2, contradiction.

### |S|=3

Then the nonclique support D must equal S. The number of private incidences is `21-lambda(D)`, and the 12-point bound gives

`3+21-lambda(D)<=12`, so `lambda(D)>=12`.

But again `e_F(Y,D)>=3` and `e_H(D)>=1`, so D14 gives

`lambda(D)<=10`, contradiction.

Therefore no support is nonclique.                         (5)

## 7. All supports cannot be K3s either

By (5), all seven supports are target K3s. Since every support has defect2 and every shared vertex has w=0, each support must contain at least one private vertex carrying positive w-mass.

For each support D let `S_D` be its set of shared vertices. Then `|S_D|<=2`, and because private vertices occur in only one support, the family `{S_D}` is pairwise intersecting.

### No common shared point

If the sets S_D have no common point, no S_D can be a singleton. A pairwise-intersecting family of 2-subsets with no common point consists of the three edges of a triangle, with repetitions allowed.

Thus every support has exactly two shared vertices and one private vertex.

For a K3 support the internal missing count is zero, so defect2 forces its unique private vertex p to satisfy

`w_p=2`.

But `w_p=kappa_p+e_F(p,x0)` and the second term is at most1. Hence `kappa_p>=1` for each of the seven distinct private vertices. This forces

`sum_R kappa_v>=7`,

contradicting CORE211 (`sum kappa<=2`).

### A common shared point exists

Suppose every S_D contains a common point z. Let k be the number of supports having a second shared vertex in addition to z.

A support with two shared vertices has exactly one private vertex. Again, because it is a K3 of defect2, that private vertex has w=2 and hence kappa>=1. Therefore `k<=2` by CORE211.

The total number of private vertices is

`2(7-k)+k =14-k >=12`.

Together with the common shared point z, this requires at least13 vertices of R, impossible.

Thus the all-K3 alternative is also impossible.

## 8. Conclusion

No seven-distinct-singleton support system exists in the c=7,A=3 terminal.

Therefore

> `q36 f=2, 2K1, a_F=1, c=7, A=3` is EMPTY.

Combined with `Q36_F2_2K1_A1_C7_A2_FULL_CLOSURE.md`, the entire c=7 layer of the `2K1,a_F=1` branch is EMPTY.