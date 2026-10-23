# q36 f=2, 2K1 far, a_F=1 — full closure of the c=6 allowance-two terminal

Status: `PROVED` under `Q36_F2_2K1_A1_REDUCTION.md`, the common-S row-closure theorem, CORE211 total excess 2, and lexicographic q36 maximality.

This eliminates the exact terminal with

- far shell F={a,b}=2K1;
- exactly one far--decoration target incidence, through x0;
- |C|=c=6;
- all six low rows share the same missing triple S=F union {x0};
- common-S allowance A0=2;
- the 12-point remainder R has alpha(H[R])<=2;
- x0 has an 11-point core row;
- all X-missing edges are incident to x0;
- g_x0=4-nu and all other decorated shell vertices have g=1.

For a low owner y write D_y for its 3-point core support and

  delta(D_y)=kappa(D_y)+m(D_y)+e_F(x0,D_y).

The exact charge formula is

  q_y=34+delta(D_y),

so delta(D_y)<=2.

## 1. Repeated supports have defect at most one

Suppose one support D is used by at least two low owners. If delta(D)=2 then q_y=36 for every owner.

Every vertex of D has at least two shell neighbours (the two owners), while its core degree is at least12, so every vertex of D is globally decorated. Repivoting one owner removes S, hence removes only the decorated vertex x0 and retains the other four old decorated shell vertices. The new q36 shell would therefore contain at least

  4+3=7

decorated vertices, strictly exceeding the old tau=5. This contradicts lexicographic maximality.

Hence every repeated support satisfies

  delta(D)<=1.                                               (1)

By the common-S overlap theorem, a repeated support cannot properly overlap any different support: proper overlap h=1 or2 costs h(3-h)=2, contradicting (1). Therefore every repeated support is disjoint from every different support.

For distinct disjoint supports D,E, the common-S joint-row theorem gives

  e_H(D,E)<=min(u_D,u_E),

where u_D=kappa(D)+e_F(x0,D)<=delta(D). Thus if D is repeated,

  e_H(D,E)<=1.                                               (2)

## 2. Multiplicity four is impossible

Let a repeated support D have multiplicity m=4.

Repivoting one owner removes x0, so exactly four units of old shell decoration are retained. Each vertex of D has at least four shell owners, hence global decoration at least3. Therefore the new shell has decoration total at least

  4+3*3=13.

Since q_y=34+delta(D)<=35, the 13-shell missing-edge floor e(M')>=22 gives

  G'<=q_y-22<=13.

Equality is forced. Thus delta(D)=1, every vertex of D has decoration exactly3, kappa(D)=0, and D has no shell neighbour outside its four owners. In particular e_F(x0,D)=0, so m(D)=1.

Hence H[D] is a 3-vertex graph with exactly two target edges and one target nonedge. Moreover u_D=0, so by (2) D is target-anticomplete to every different support E.

Because six rows exist, some different support E exists. Taking the target-nonadjacent pair in D together with any vertex of E gives an independent triple in H[R], contradicting alpha(H[R])<=2.

Therefore

  repeated multiplicity <=3.                               (3)

## 3. Properly intersecting singleton supports form small sunflowers

Let D,E be distinct supports with proper overlap.

The overlap cost is h(3-h)=2, so equality in the common-S overlap bound forces

  delta(D)=delta(E)=2.

Thus both owner repivots stay at q36. Lexicographic maximality allows at most one decorated inserted support vertex, because four old decorated shell vertices are retained.

If h=2, the two shared support vertices each have at least two shell owners and are both decorated, contradiction. Hence

  |D intersect E|=1.                                       (4)

Let v be the unique shared vertex. The two nonshared vertices of D must be globally regular; otherwise the D-repivot would insert at least two decorated vertices.

A globally regular core vertex u in D\E has core degree12 and exactly one old shell neighbour, namely its owner. Therefore kappa_u=0 and e_F(u,S)=0. Row closure for the E-repivot gives

  e_H(u,E)=0.

In particular u is target-nonadjacent to the shared vertex v. Applying this to both petals shows that inside D the only possible target edge is the edge joining its two petals. Since delta(D)<=2, D must contain at least one target edge, hence exactly that one. Therefore

- m(D)=2;
- kappa(D)=0;
- e_F(x0,D)=0;
- v is target-nonadjacent to both petals.

The same holds for every support in the same intersection component. If one support met two others at different vertices, it would contain two decorated shared vertices, contradicting q36 lexicographic maximality. Hence every connected intersection component is a sunflower with one common hub.

Petals belonging to different supports of the same sunflower are pairwise target-anticomplete by row closure. Consequently a sunflower with at least three supports contains an independent triple obtained by choosing one petal from each of three supports. This contradicts alpha(H[R])<=2.

Therefore every singleton-support sunflower has size at most2.  (5)

## 4. There must be a repeated support

Assume all six rows had distinct supports.

By (4)--(5), the supports decompose into disjoint sunflower components, each of size at most2. A sunflower component with s supports uses exactly 1+2s vertices of R (with s=1 giving3 vertices).

If there are k components, six supports use

  12+k

vertices, because the support components are vertex-disjoint. Since |R|=12 and k>=1, this is impossible.

Thus at least one support is repeated.                              (6)

## 5. One repeated class is impossible

Let D be the only repeated support class, with multiplicity m in {2,3} by (3).

Every other support is disjoint from D. If the singleton supports split into at least two intersection components, choose one support E from one component and F from another. Then D,E,F are three disjoint 3-sets with

  e(D,E)<=1,
  e(D,F)<=1,
  e(E,F)<=2.

Choose one vertex uniformly from each block. The expected number of target edges among the three chosen vertices is at most

  (1+1+2)/9 < 1.

Hence some choice has zero target edges, an independent triple in H[R], contradiction.

Therefore all singleton supports lie in one sunflower component. Its size is 6-m, equal to4 when m=2 and3 when m=3. Both violate (5).

So one repeated class is impossible.                               (7)

## 6. Two repeated classes force the 3+3 pattern

If there are at least three distinct repeated support classes, choose three of them. They are pairwise disjoint, and each pair has at most one target cross-edge by (2). A random one-from-each choice has expected target-edge count at most3/9<1, yielding an independent triple. Thus there are at most two repeated classes.

By (6)--(7), there are exactly two repeated classes D,E and no singleton class. Their multiplicities sum to6. By (3), both multiplicities are at most3, hence necessarily

  3+3.                                                       (8)

The supports D,E are disjoint and satisfy e_H(D,E)<=1.

## 7. The 3+3 terminal contradicts the global w-mass

Put

  L=R\(D union E),

so |L|=6. Define

  w_v=kappa_v+e_F(v,x0).

For any v in L, if its target neighbours in D union E failed to cover all target-nonedges between D and E, there would exist d in D and e in E such that

- de is a target nonedge;
- vd and ve are target nonedges.

Then {v,d,e} would be an independent triple in H[R], impossible.

Since e_H(D,E)<=1, the bipartite target-nonedge graph between D and E is K3,3 with at most one edge removed. Its minimum vertex-cover size is3. Hence

  e_H(v,D)+e_H(v,E)>=3.                                     (9)

Row closure applied to D and E gives

  e_H(v,D)<=w_v,
  e_H(v,E)<=w_v.

Thus 2w_v>=3, so w_v>=2 for every v in L. Therefore

  sum_(v in L) w_v >=12.                                    (10)

But CORE211 gives kappa(R)<=2. Also (1) implies

  e_F(x0,D)<=1,
  e_F(x0,E)<=1,

and trivially e_F(x0,L)<=6. Therefore

  sum_(v in R)w_v
  =kappa(R)+e_F(x0,R)
  <=2+1+1+6
  =10,

contradicting (10).

## 8. Conclusion

Every possible six-row support architecture leads to contradiction. Therefore the c=6 allowance-two terminal is empty:

> no q36 f=2 candidate with far topology 2K1, a_F=1 and c=6 exists.

Combined with `Q36_F2_2K1_A1_REDUCTION.md`, this branch now satisfies

  c>=7.

The cases c>=7 remain open and are to be treated next.