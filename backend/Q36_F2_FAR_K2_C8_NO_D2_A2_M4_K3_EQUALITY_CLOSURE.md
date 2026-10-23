# q36 f=2 far-target-K2 — c=8 no-d2 A=2, multiplicity-four K3 equality closure

Status: `PROVED` under `Q36_F2_FAR_K2_C8_NO_D2_CLASS_REDUCTION_V2.md`, `Q36_F2_FAR_K2_D14_CONTRACT_CORRECTION.md`, common-S row closure, q36 lexicographic maximality, CORE211, `alpha(H)<=3`, and `omega<=11`.

This closes the corrected-D14 equality channel omitted by the retracted A=2 aggregate.

## 1. Equality setup

Let D be a repeated target K3 support of owner multiplicity4 in the unique A=2 common missing-set class.

A repeated support cannot use full defect2, so

`w(D)=sum_(d in D)(kappa_d+e_F(d,S))<=1`,

where `S=F union {x}`.

Corrected D14 gives

`12+O_D+e_F(Y,D)+3<=14+rho`.

Multiplicity4 is possible only for `rho=1`, and then equality forces

> `O_D=0`, `e_F(Y,D)=0`.                                    (1)

Therefore every one of the four remaining owner supports is disjoint from D.

Because `w(D)<=1`, D contains at least two zero-weight points. Fix one such point d0. Row closure makes d0 target-anticomplete to every external support.

Hence the union U_ext of all external support classes satisfies

> `alpha(H[U_ext])<=2`;                                      (2)

otherwise d0 together with an independent triple in U_ext gives an independent4 in H.

## 2. External repeated classes are K3s

Any repeated external support has defect at most1.

A repeated one-edge support is impossible because its internal missing count is2.

Suppose a repeated external support E has exactly two target edges. Then its internal missing count is1, so repeated defect<=1 forces zero common-S weight. Hence E has zero cross allowance to every distinct support class.

If another external class T exists, let uv be the unique internal target nonedge of E. Since E--T target cross edges are zero, any t in T gives an independent triple `{u,v,t}` in U_ext, contradicting (2).

Therefore every repeated external support class is a target K3.   (3)

## 3. Partition 3+1 is impossible

Suppose the four external owners split as multiplicities3+1, with repeated K3 E and singleton support T.

The repeated supports D and E have non-missing allowance at most1, so

`e_H(D,E)<=1`, `e_H(D,T)<=1`, `e_H(E,T)<=1`.                (4)

If T were nonclique with internal target nonedge uv, choose a zero-weight point e0 in E. The total E--T cross edge count is at most1, so some e in E can be chosen target-nonadjacent to both u,v; also d0 is anticomplete to T and E except possibly the unique D--E edge. Choosing e to avoid d0 as well is possible because the two bad edge incidences occupy at most two of the three E vertices. Then `{d0,e,u,v}` is an independent4, contradiction.

Thus T is also a target K3.

Now D,E,T are three K3 blocks with at most one target cross-edge between every pair.

Let v be any of the 26 other core vertices and suppose `w_v<=1`. Row closure against each block gives at most one target neighbour in each K3, leaving at least two nonneighbours per block. Choose uniformly one of two nonneighbours from each block. The expected number of target edges among the three choices is at most

`3*(1/4)=3/4<1`.

Hence an independent transversal exists; together with v this gives an independent4. Thus every outside vertex has `w_v>=2`, so

`sum_H w_v>=52`.                                             (5)

For A=2 the common-S global weight satisfies

`sum_H w_v =2+e_F(S,H)<=36`,                                (6)

because the two far core rows contribute `22-a_F` and the active x row contributes `12+a_F-t_x`, totaling at most34, plus CORE211 excess2.

Contradiction.

Therefore 3+1 is impossible.                                 (7)

## 4. Partition 2+2 is impossible

Both external repeated classes are target K3s by (3). Thus D plus the two external classes again form three K3 blocks with pairwise target cross-edge count at most1.

The identical outside-weight argument from Section3 yields `sum_H w>=52>36`.

Therefore 2+2 is impossible.                                 (8)

## 5. Partition 2+1+1 is impossible

Let E be the repeated external class; E is a target K3.

We show each singleton class T is also a K3. Suppose T contains an internal target nonedge uv.

Choose a zero-weight point e0 in E. Since E is repeated, `e_H(E,T)<=1`; since D is repeated, `e_H(D,E)<=1`. Among the three E vertices there is a point e target-nonadjacent to u,v and to d0: at most one E vertex is incident with the unique possible E--T edge and at most one with the unique possible D--E edge from d0.

Then `{d0,e,u,v}` is an independent4, contradiction.

Thus both singleton classes T,U are target K3s.

For the four K3 blocks D,E,T,U, pairwise cross-edge bounds are

- at most1 for every pair involving D or E;
- at most2 for the singleton pair T--U.

Hence the sum of all six cross-edge counts is at most7.

Choose one vertex uniformly from each K3. The expected number of target edges among the four choices is at most

`7/9<1`.

Therefore some choice is an independent4, contradiction.

Thus 2+1+1 is impossible.                                    (9)

## 6. Partition 1+1+1+1 is impossible

All four external support classes are singleton triples. By (2), their union has independence number at most2.

### 6.1 Disjoint nonclique supports are impossible

If singleton E is nonclique and disjoint from another support T, an internal target nonedge of E must be covered from every point of T to avoid an independent triple in U_ext, requiring at least3 E--T target edges.

But A=2 gives E non-missing allowance at most1 when E is nonclique. Joint row closure gives fewer than3 cross edges. Contradiction.

Thus any disjoint pair of singleton supports consists of K3s.

### 6.2 Intersection components

If two singleton supports properly overlap, overlap cost2 exhausts the A=2 defect budget, so both repivot to q36. The two inactive decorated shell vertices are retained; lexicographic maximality therefore allows at most one globally decorated/shared support point.

Consequently:

- proper overlap size is exactly1;
- a singleton support cannot intersect two different classes at two different support vertices;
- every nontrivial intersection component is a common-hub sunflower;
- each support in such a component has two clean private weight-zero petals.

A sunflower component cannot contain three supports: choosing one clean petal from each gives an independent triple in U_ext. Thus every component has size at most2.

There cannot be three intersection components. Choose a weight-zero private point from one support in each component; row closure makes the three points pairwise target-nonadjacent, violating `alpha(H[U_ext])<=2`.

With four supports, component size at most2 and at most two components forces exactly two two-support sunflower components.

Choose clean private petals from two supports in the first component and one support in the second. They are pairwise target-nonadjacent by row closure, again contradicting `alpha(H[U_ext])<=2`.

Therefore 1+1+1+1 is impossible.                           (10)

## 7. Conclusion

All multiplicity partitions of the four external owners are impossible. Hence

> the corrected-D14 `rho=1`, A=2, multiplicity-four repeated-K3 equality channel is EMPTY.

This repairs the specific multiplicity-four K3 gap in the retracted A=2 aggregate. Other A=2 channels, especially repeated two-edge support capacity, still require corrected-contract re-audit before the whole A=2 layer can be re-certified.