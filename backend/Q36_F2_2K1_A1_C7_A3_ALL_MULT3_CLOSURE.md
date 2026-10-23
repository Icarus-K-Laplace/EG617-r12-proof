# q36 f=2, 2K1 far, a_F=1 — closure of all remaining c=7,A=3 multiplicity-three partitions

Status: `PROVED` under `Q36_F2_2K1_A1_C7_A3_MULTIPLICITY_RIGIDITY.md`, `Q36_F2_2K1_A1_C7_A3_322_FULL_CLOSURE.md`, row closure, CORE211, K11/D14, and `alpha(H[R])<=2`.

The earlier files already exclude multiplicity4, partition 3+3+1, and partition 3+2+2. This note eliminates 3+2+1+1 and 3+1+1+1+1. Consequently every surviving support class has multiplicity at most2.

Write `w_v=kappa_v+e_F(v,x0)`. Then `sum_R w_v<=14`.

## 1. Closure of 3+2+1+1

Let D have multiplicity3, E multiplicity2, and F,G be singleton supports.

### 1.1 D cannot be the exact one-edge support

Assume D is the one-edge equality type from the multiplicity-rigidity theorem. Then

- `e_H(D)=1`;
- every vertex of D has `w=0`;
- `e_F(Y,D)=0`;
- every one of the other four owner incidences must come from a support meeting D in exactly one point.

Thus E,F,G each meet D in one point.

Because E is repeated and overlaps D, the overlap cost is2 and E has exact defect2. Let z=E intersect D. The two E-petals lie outside D. Each must cover the two target-nonedges of D, so row closure forces at least one unit of w on each petal. Since the total E-defect is2 and z has w=0, this forces

- `m(E)=0`;
- H[E]=K3;
- each E-petal has w=1.

The intersection point z must be the isolated vertex of the one-edge triple D. If z were one endpoint of the unique D-edge, the other endpoint together with the isolated D-vertex would be a target-nonedge pair of zero-weight vertices outside E. Row closure would make both target-anticomplete to E, producing an independent triple with any E-vertex.

The same argument applies to each singleton support F,G: its unique D-intersection must also be the isolated vertex z. Therefore all E,F,G contain z.

Let a,b be the endpoints of the unique target edge of D. They have w=0 and lie outside E,F,G, hence row closure makes them target-anticomplete to every one of these supports.

Since a is target-nonadjacent to z as well, alpha(H[R])<=2 forces the union `E union F union G` to induce a target clique: any target-nonedge inside that union together with a would be an independent triple.

In particular F and G are target K3s and all petals are mutually target-adjacent across supports.

Consider any support, say F={z,u,v}. Because F overlaps D, its defect is at least2. Since H[F]=K3, its defect is `w_u+w_v` and is at most3.

For a petal u not contained in another support, say G, clique-union forces `e_H(u,G)=3`; row closure gives `e_H(u,G)<=w_u`, hence `w_u>=3`. Thus in every support edge on the petal set, at least one endpoint must belong to all four owner supports E,F,G? More directly, model the four non-D owner supports by their two-petal sets. If a petal is absent from one of the other supports, then its w-value is at least3. But every support has petal w-sum at most3, so each petal pair must contain one vertex of w=0 that is present in all remaining supports.

Hence all four owner supports share a common petal q in addition to z. Their other petals are distinct because the support classes are distinct. The support-incidence count is then

`lambda_z=7`, `lambda_q=4`.

For any one of these K3 supports `{z,q,r}`, K11/D14 gives

`lambda_z+lambda_q+lambda_r+e_H(z,q,r)<=14`.

The left side is at least `7+4+1+3=15`, contradiction.

Thus the one-edge multiplicity-three case is impossible.

### 1.2 D cannot be a target K3

Assume H[D]=K3. Its weighted overlap budget is at most2.

The repeated support E cannot be disjoint from D. If E were nonclique, an internal target-nonedge of E would require at least three target cross-edges from the three vertices of clique D, but repeated-support defect<=2 gives cross allowance at most1 or0. If E were a clique, two disjoint K3 blocks with at most two target cross-edges force, on their six-point complement L, `w_v>=2` for every v, hence `sum_L w_v>=12`; this is incompatible with the global w-mass once the support weights are included.

Therefore E meets D. Since E has multiplicity2, this one-point overlap already consumes the entire weighted overlap budget2 of D. Hence F and G are disjoint from D.

If F and G were disjoint from one another, the three disjoint blocks D,F,G have pairwise target cross-edge bounds at most2,2,3. A random one-from-each choice has expected target-edge count at most7/9<1, yielding an independent triple. Thus F and G properly overlap.

Any internal target-nonedge in F would require three cross-edges from the clique D, contradicting the D--F bound at most2. Therefore F is a target K3, and similarly G is a target K3.

Apply the two-disjoint-K3 nonedge-cover argument to D and F. Every vertex outside D union F has w>=2, so `sum_(R\(D union F))w>=12`. Hence

`w(D)+w(F)<=2`.                                             (1)

Because F and G properly overlap, the common-S overlap cost is2. Since F is a target K3, its defect equals w(F), so `w(F)>=2`. Equation (1) forces

`w(F)=2`, `w(D)=0`.

The same argument with D and G gives w(G)=2. Moreover the total w-mass is now at least14, hence equals14. Equality in the global bound `sum_R w<=kappa(R)+e_F(x0,R)<=2+12=14` forces x0 to be target-adjacent to every vertex of R.

But then every vertex of D contributes at least1 to w, contradicting `w(D)=0`.

Therefore the K3 multiplicity-three case is impossible.

Thus partition 3+2+1+1 is empty.

## 2. Closure of 3+1+1+1+1

Let D have multiplicity3 and let F1,...,F4 be singleton supports.

### 2.1 D cannot be the exact one-edge support

In the one-edge equality type every remaining owner support must meet D exactly once. As above, a support intersecting D at an endpoint of the unique D-edge leaves a zero-weight target-nonedge pair outside that support and is impossible. Hence all four singleton supports meet D at the isolated D-vertex z.

Let a be either endpoint of the unique D-edge. The vertex a has w=0 and is target-anticomplete by row closure to every Fi. Since a is also target-nonadjacent to z, alpha(H[R])<=2 forces the union of all Fi to be a target clique.

Write each Fi as `{z,u_i,v_i}`. Every Fi is therefore a target K3. For a petal q, if q is absent from some Fj, clique-union gives `e_H(q,Fj)=3`; row closure forces `w_q>=3`.

But each Fi overlaps D and is a K3 of defect at most3, so

`w_(u_i)+w_(v_i)<=3`.

Thus each petal pair must contain a vertex of w=0. Such a zero-weight petal cannot be absent from another support (otherwise it would need w>=3), so it belongs to all four singleton supports. Therefore all Fi share one common petal q.

Then `lambda_z=7`, `lambda_q=4`, and for any Fi the D14 left side is at least

`7+4+1+3=15`,

contradicting the cap14.

Hence the one-edge case is impossible.

### 2.2 D cannot be a target K3

If H[D]=K3, its weighted overlap budget is at most2. Thus at least two of the four singleton supports, say F and G, are disjoint from D.

As above, any support disjoint from clique D must itself be a target K3; otherwise its internal target-nonedge requires at least three D-cross edges, exceeding the D cross allowance at most2.

The supports F and G cannot be disjoint from each other, since otherwise D,F,G are three disjoint blocks with total cross-edge allowance at most7 and a random one-from-each choice gives an independent triple. Therefore F and G properly overlap.

Apply the same two-disjoint-K3 w-mass argument to D and F. It gives `w(D)+w(F)<=2`. Proper overlap F--G costs2 and F is a K3, so w(F)>=2. Hence w(F)=2 and w(D)=0. The same with G gives w(G)=2.

The global w-mass is forced to equality14, which implies x0 is target-adjacent to all12 points of R. This contradicts w(D)=0.

Thus the K3 case is impossible too.

Therefore partition 3+1+1+1+1 is empty.

## 3. Conclusion

All owner partitions containing a multiplicity-three support are now eliminated. Combined with the previous files, every surviving c=7,A=3 support system satisfies

> maximum support multiplicity <=2.

The remaining owner partitions are therefore

- `2+2+2+1`;
- `2+2+1+1+1`;
- `2+1+1+1+1+1`;
- seven singleton supports.