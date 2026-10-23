# q36 f=2 far-target-K2 — c=8 no-d2, allowance two full closure V2

Status: `PROVED` under `Q36_F2_FAR_K2_C8_NO_D2_CLASS_REDUCTION_V2.md`, `Q36_F2_FAR_K2_D14_CONTRACT_CORRECTION.md`, `Q36_F2_FAR_K2_C8_NO_D2_A2_M4_K3_EQUALITY_CLOSURE.md`, common-S row closure, q36 lexicographic maximality, CORE211, `alpha(H)<=3`, and `omega<=11`.

This rebuilds the A=2 closure after the D14/clique-contract audit. No false far-K2 K11 base and no global target-K4 prohibition is used.

All eight owners share one common missing set `S=F union {x}` with allowance2. Put

`w_v=kappa_v+e_F(v,S)`.

For every support E,

`Delta(E)=m(E)+w(E)<=2`.

A repeated support cannot use full defect2, so every repeated support satisfies

`Delta(E)<=1`.                                               (1)

## 1. Repeated one-edge supports are impossible

A one-edge triple has internal missing count2, already exceeding the repeated-support defect bound (1).

Hence no repeated one-edge support exists.                  (2)

## 2. Repeated two-edge supports are impossible

Let D be a repeated two-edge support. Its internal missing count is1, so (1) forces

`w(D)=0`.                                                     (3)

Proper overlap costs2 and is impossible for D. Thus every distinct support class is disjoint from D, and joint row closure gives zero target D-cross edges.

Let ab be the unique internal target nonedge of D, and let Q be the union of all external support classes.

If Q contained a target-nonedge uv, then because D is target-anticomplete to Q,

`{a,b,u,v}`

would be an independent4-set in H. Therefore

> Q is a target clique.                                      (4)

In particular every external support is a target K3.

### 2.1 A repeated external class would have to be the only external class

Let E be a repeated external class. By (1), `w(E)<=1`.

E cannot properly overlap another class. If another class T were disjoint from E, the clique property (4) gives all nine target cross-edges E--T, while joint row closure gives at most `w(E)<=1`. Contradiction.

Thus E would be the unique external class.

The repeated D has multiplicity at most4 by corrected D14. If `m_D=2` or3, the unique external class would need multiplicity6 or5, impossible under corrected D14 (`m<=4`).

If `m_D=4`, the unique external class must have multiplicity4. Since it is a target K3, this is exactly the corrected `rho=1` multiplicity-four K3 equality channel closed by `Q36_F2_FAR_K2_C8_NO_D2_A2_M4_K3_EQUALITY_CLOSURE.md`.

Hence no repeated external class can occur.                 (5)

### 2.2 All-singleton external classes are also impossible

Now every external support class is singleton.

Two distinct external supports cannot be disjoint: Q is a target clique, so a disjoint pair has nine target cross-edges, while a singleton K3 support has common-S weight at most2 and joint row closure allows at most2.

Thus all external supports pairwise intersect.

Every proper overlap costs2, so each external singleton support has exact defect2 and repivots to q36. The two inactive decorated shell vertices are retained. Lexicographic maximality therefore permits only one shared/global-decorated support vertex.

Hence intersections have size1 and all pairwise intersections of one support occur through the same shared point. The family is a common-hub sunflower, and every petal is clean with weight0.

But Q is a target clique. Take a clean petal u of one support and another support T in the sunflower. The petal lies outside T and has weight0, so row closure gives

`e_H(u,T)=0`,

whereas the clique property Q says u is target-adjacent to all three points of T. Contradiction.

Thus the repeated two-edge support D cannot exist.          (6)

## 3. Repeated K3 supports are impossible

Let D be a repeated target K3. The multiplicity-four equality case is already closed by the dedicated corrected-D14 file, so

`m_D in {2,3}`.                                              (7)

By (1), `w(D)<=1`; choose a zero-weight point z in D. Proper overlap is impossible, so every distinct support class is disjoint from D. Row closure makes z target-anticomplete to all external support vertices.

### 3.1 Every external support is a K3

Suppose an external support E is nonclique, with internal target-nonedge uv. Its non-missing allowance is at most1.

There must be another distinct external class E': D has multiplicity at most3 and one external class has multiplicity at most4, so one class cannot carry all remaining five or six owners.

If every point of E' met u or v, then `e_H(E,E')>=3`, exceeding the row-closure allowance of E. Therefore some e' in E' is target-nonadjacent to both u,v.

Then

`{z,u,v,e'}`

is an independent4-set. Contradiction.

Thus every external support is a target K3.                 (8)

### 3.2 At most two external support classes

Suppose three distinct external K3 classes E1,E2,E3 exist.

If two overlap, they must be singleton classes because repeated supports cannot properly overlap. Their overlap costs2 and both repivot to q36. Lexicographic maximality gives clean private weight-zero petals. Choose one clean petal from each of the two overlapping supports. They are target-nonadjacent to each other and, by row closure, target-anticomplete to the third class. Any point of the third class together with these two petals and z yields an independent4-set.

If E1,E2,E3 are pairwise disjoint, each pair has at most2 target cross-edges. Choosing one point uniformly from each gives expected target-edge count at most

`3*(2/9)=2/3<1`.

So an independent triple exists, again completed by z to an independent4.

Therefore

> at most two distinct external support classes exist.       (9)

### 3.3 Owner counting forces three repeated K3 blocks

There are five or six owners outside D. With at most two external classes and every repeated K3 multiplicity at most3, both external classes must be repeated K3s. The three owner multiplicities are `3,3,2` up to permutation.

Repeated-support allowance gives total weight at most1 on every block. Proper overlap is impossible, so the three K3 blocks B1,B2,B3 are pairwise disjoint, and joint row closure gives at most one target cross-edge between each pair.

Let v be any of the other 26 core vertices. If `w_v<=1`, then row closure leaves at least two target-nonneighbours of v in each block. Choose uniformly one of two such nonneighbours from each block. The expected target-edge count among the three choices is at most

`3*(1/4)=3/4<1`.

Hence an independent transversal exists, and together with v gives an independent4. Therefore every outside vertex has

`w_v>=2`.

Thus

`sum_H w_v>=52`.                                             (10)

For A=2, the common-S global budget is

`sum_H w_v = sum_H kappa_v + e_F(S,H) <= 2+34=36`,          (11)

because the two far rows contribute `22-a_F` and the active x row contributes `12+a_F-t_x`.

Contradiction. Hence no repeated K3 support exists.          (12)

Together with Sections1-2, there are no repeated support classes at all.

## 4. The all-singleton system is impossible

All eight supports are now distinct singleton triples.

If two supports properly overlap, overlap cost2 forces both to have exact defect2 and q36 repivots. The two inactive decorated shell vertices are retained, so lexicographic maximality permits only one shared/global-decorated support point. Hence:

- every proper overlap has size1;
- a support cannot intersect two different classes at two different vertices;
- every nontrivial intersection component is a common-hub sunflower;
- petals in a nontrivial component are clean weight-zero private vertices.   (13)

A sunflower component cannot contain four supports: choose one clean petal from each of four supports; row closure makes them pairwise target-anticomplete, giving an independent4.

Thus every component has size at most3.                     (14)

There cannot be four components. Choose a weight-zero private point from one support in each component. Such a point exists in every isolated support because a 3-set of defect at most2 has at least one zero-weight point; in a nontrivial component it is a clean petal from (13). Points from different components are pairwise target-nonadjacent by row closure. Four components would yield an independent4.

Hence there are at most three components.                  (15)

Eight supports with component size at most3 and at most three components force the unique partition

`3+3+2`.                                                     (16)

Every component is nontrivial. Let E={z,u,v} be a support in such a component. Its petals u,v have weight0 and lie outside another support sharing hub z. Row closure makes u and v target-nonadjacent to that support, in particular to z. Thus E has at least two internal target nonedges. Since its exact defect is2, equality forces

- uv is the sole target edge;
- `w_z=w_u=w_v=0`.

Therefore distinct components are completely target-anticomplete by row closure.

Choose in one component its hub z and one petal u; zu is a target nonedge. Choose the hubs z',z'' of the other two components. All cross-component pairs are target nonedges and z'z'' is also a target nonedge. Hence

`{z,u,z',z''}`

is an independent4-set, contradiction.

Thus the all-singleton system is impossible.               (17)

## 5. Conclusion

Every possible support architecture has been excluded under the corrected far-K2 contract. Therefore

> `q36 f=2`, far-target-K2, `c=8`, no-d2, `A=2` is EMPTY.

This V2 file supersedes the retracted pre-audit A=2 aggregate.