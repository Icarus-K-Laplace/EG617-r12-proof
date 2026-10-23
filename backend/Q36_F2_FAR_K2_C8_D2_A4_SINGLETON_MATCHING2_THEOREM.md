# q36 f=2 far-target-K2 — c=8, one d2 row, A=4 all-singleton matching theorem

Status: `PROVED REDUCTION` under the current far-K2 A=4 all-singleton contract, common-S row closure, q36 lexicographic maximality, and `alpha(H[U])<=2`.

This proves that the seven distinct singleton d3 supports have matching number at most two.

## 1. Setup

All seven d3 support classes are singleton triples with common missing set

`S=F union {x}`

and allowance4. Let

`w_v=kappa_v+e_F(v,S)`.

For a support E,

`Delta(E)=m(E)+w(E)<=4`,

where `m(E)` is the number of internal target nonedges.

The pure d2 support D0 is target-anticomplete to the d3-support union U, so

`alpha(H[U])<=2`.                                           (1)

For disjoint d3 supports E,E', joint row closure gives

`e_H(E,E')<=min(w(E),w(E'))`.                              (2)

## 2. A full-defect support cannot belong to a disjoint triple of supports

Suppose E has full defect4. Its repivot stays at q36 and retains the two inactive decorated shell vertices.

Therefore lexicographic maximality allows at most one globally decorated support vertex of E; otherwise the q36 repivot would insert at least two decorated core vertices and strictly increase tau.

Every positive-weight vertex is globally decorated. Hence E has at least two vertices of weight0. Choose one such vertex `u in E`.

By row closure, `u` is target-anticomplete to every disjoint support.

Now suppose E,E',E'' are pairwise disjoint. Equation (2) gives

`e_H(E',E'')<=4<9`,

so there is a target-nonedge `v v'` with `v in E'`, `v' in E''`.

Then `{u,v,v'}` is an independent triple in U, contradicting (1).

Thus in any hypothetical three pairwise-disjoint supports, none has full defect4.    (3)

## 3. The low-defect random-choice bound

Assume E1,E2,E3 are pairwise disjoint. By (3),

`Delta(E_i)<=3`.

Hence `w(E_i)<=3` for each i. By (2), every pair has at most3 target cross-edges.

Choose independently and uniformly one vertex from each E_i. The expected number of target edges among the three selected vertices is at most

`(3+3+3)/9=1`.                                              (4)

Because alpha(H[U])<=2, every choice must contain at least one target edge. Therefore equality must hold everywhere in (4):

- each `w(E_i)=3`;
- each E_i is a target K3 (otherwise Delta would exceed3);
- every pair E_i,E_j has exactly3 target cross-edges;
- every one of the 27 triples obtained by choosing one point from each support contains exactly one target edge.    (5)

## 4. Equality would partition the 3x3x3 cube by nine axis-parallel lines

Label the supports A,B,C, each of size3.

Each target edge between A and B contributes a full line of three choices in `A x B x C`, parallel to the C-axis. Similarly AC edges give B-parallel lines and BC edges give A-parallel lines.

Condition (5) says the three AB edges, three AC edges and three BC edges form nine pairwise-disjoint axis-parallel lines whose union is all 27 cells of the 3x3x3 cube.

We show this is impossible.

For the three AB edges, let

- `p_A` be the number of A-coordinates used;
- `p_B` be the number of B-coordinates used.

Since there are three distinct AB edges,

`p_A p_B>=3`.                                               (6)

Define analogously the two projection sizes for AC and BC.

Pairwise disjointness of an AB-line and an AC-line requires different A-coordinates. Therefore

`p_A(AB)+p_A(AC)<=3`.                                      (7)

Likewise

`p_B(AB)+p_B(BC)<=3`,
`p_C(AC)+p_C(BC)<=3`.                                      (8)

Every projection size is at least1. Hence no projection size can equal3: if, for example, `p_A(AB)=3`, then (7) leaves no A-coordinate for the nonempty AC family.

Thus every projection size is at most2. Combining with the product lower bound (6), every edge-family must use projection sizes exactly `(2,2)`.

But then (7) reads

`2+2<=3`,

a contradiction.

Therefore the equality case in (4) is impossible.

## 5. Conclusion

No three d3 support classes are pairwise disjoint. Hence the seven-support all-singleton hypergraph satisfies

> matching number at most two.

The next step is to choose a maximal disjoint pair and classify the remaining five supports by their intersections with that six-point carrier.