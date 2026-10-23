# q36 f=2, 2K1 far, a_F=0 — allowance-two d3 capacity

Status: `PROVED` under `Q36_F2_2K1_A0_REDUCTION.md`, CORE211, row closure, and lexicographic q36 maximality.

The theorem proved here is:

> Any d3 common-missing class of allowance exactly2 has at most six owners.

This is a triple-row analogue of the repeated-pair capacity mechanisms used elsewhere in the backend.

## 1. Setup

Let x be the decorated vertex defining one d3 class. All owners in the class have missing set

  S=F union {x},

where F is the far 2K1. Their 3-point supports lie in the fixed 11-point remainder R with

  alpha(H[R])<=2.

Allowance two means

  A_x=2.

For every support D,

  delta(D):=kappa(D)+m(D)+e_F(x,D)<=2,

and

  q_D=34+delta(D).

Let r=|X|. Repivoting an owner removes the one decorated shell vertex x from S and retains the other r-1 old decorated shell vertices.

## 2. Repeated supports have defect at most one and multiplicity at most five

If a support D is repeated and delta(D)=2, then q_D=36. Every vertex of D has at least two shell owners and core degree at least12, so all three inserted support vertices are globally decorated. The new shell has at least

  (r-1)+3=r+2

decorated vertices, exceeding the old tau=r. This contradicts lexicographic maximality.

Hence every repeated support satisfies

  delta(D)<=1.                                              (1)

Therefore a repeated support cannot properly overlap a different support: proper overlap costs h(3-h)=2.

A repeated support repivots to q<=35. Every q<=35 shell has total decoration at most13. Since at least r-1 old decoration units are retained and each support vertex has decoration at least m-1 when the support multiplicity is m,

  (r-1)+3(m-1)<=13.

Because r>=1,

> m<=5.                                                     (2)

Distinct supports from a repeated class are disjoint, and a repeated support has common-S cross allowance at most1 to every different support.

## 3. Singleton intersection components are sunflowers of size at most two

Let distinct singleton supports D,E properly overlap. The overlap cost equals2, hence both supports have delta=2 and their repivots remain at q36.

An overlap of size2 would insert two decorated shared vertices while retaining r-1 old decorated vertices, giving tau at least r+1. Thus

  |D intersect E|=1.                                       (3)

Let v be the shared vertex. Lexicographic maximality forces the two nonshared vertices of D to be globally regular. Each such petal u has core degree12 and exactly one old shell neighbour (its owner), hence

  kappa_u=0,
  e_F(u,S)=0.

Row closure against E then gives e_H(u,E)=0. Therefore u is target-nonadjacent to the shared hub v and to the petals of E.

Since delta(D)<=2, D must contain at least one target edge; the only possible one is the edge joining its two petals. Hence every support in the same intersection component consists of

- one common hub;
- one target edge on its two petals;
- no target edge from the hub to a petal.

If one support met two others at different vertices it would contain two decorated shared vertices and violate q36 lexicographic maximality. Thus each connected intersection component is a common-hub sunflower.

Three supports in one sunflower are impossible: choose one petal from each. Petals from different supports are pairwise target-anticomplete by row closure, giving an independent triple in R.

Therefore

> every singleton-support sunflower has size at most2.     (4)

## 4. Seven or more owners are impossible

Assume for contradiction that the allowance-two class has n>=7 owners.

### No repeated support

Then all n supports are singleton supports partitioned into sunflower components of size at most2. Different components are vertex-disjoint. A component with s supports uses 1+2s vertices. Even with maximal packing into size-two components, seven supports require at least

  5+5+5+3=18

vertices, exceeding |R|=11.

Thus a repeated support exists.

### Exactly one repeated class

Let its multiplicity be m<=5 by (2). Every singleton support is disjoint from it.

If singleton supports occupy at least two intersection components, choose one support E,F from two different components. The repeated support D, E and F are three disjoint 3-sets with

  e(D,E)<=1,
  e(D,F)<=1,
  e(E,F)<=2.

A random one-from-each choice has expected target-edge count at most4/9<1, yielding an independent triple in R.

Hence all singleton supports lie in one sunflower component. By (4) there are at most two of them.

If there are zero or one singleton supports then m>=6, contradicting (2). If there are exactly two, they form one two-support sunflower. The total number of target cross-edges from the repeated support D to the two singleton supports is at most2, so among the three vertices of D one vertex d is incident to no such cross-edge. Choosing one petal from each sunflower support gives two target-nonadjacent petals, both nonadjacent to d. This is an independent triple.

Thus exactly one repeated class is impossible.

### At least three repeated classes

Any three repeated support classes are pairwise disjoint and each pair has at most one target cross-edge. A random one-from-each choice has expected target-edge count at most3/9<1, giving an independent triple.

Hence there are at most two repeated classes.

### Two repeated classes

If any singleton support also existed, the two repeated supports and that singleton would be three disjoint 3-sets with pairwise cross-edge counts at most1. Again the random-choice expectation is at most3/9<1, contradiction.

Therefore the only final architecture consists of exactly two repeated supports D,E and no singleton supports.

They are disjoint and satisfy

  e_H(D,E)<=1.

Put

  L=R\(D union E),

so |L|=5.

For v in L, its neighbourhood in D union E must cover all target-nonedges between D and E; otherwise v together with one uncovered d in D and e in E is an independent triple. Since the bipartite target-nonedge graph is K3,3 with at most one edge removed, its minimum vertex-cover size is3. Thus

  e_H(v,D)+e_H(v,E)>=3.                                    (5)

Define

  w_v=kappa_v+e_F(v,x).

Row closure for D and E gives each cut at most w_v, so (5) implies w_v>=2. Therefore

  sum_L w_v>=10.                                           (6)

But repeated supports have defect<=1, so

  e_F(x,D)<=1,
  e_F(x,E)<=1.

Also x has allowance2, hence its core row has size

  |N_H(x)|=A_x+9=11.

More directly, on R we have

  e_F(x,R)<=1+1+|L|=7.

CORE211 gives kappa(R)<=2, so

  sum_R w_v<=2+7=9,

contradicting (6).

Thus n>=7 is impossible.

## 5. Conclusion

> Every allowance-two d3 common-missing class in the `2K1,a_F=0` f=2 branch has multiplicity at most6.

Consequences for the all-d3 single-class high-c channel:

- c=7 cannot have allowance1 (by the low-allowance theorem) or allowance2 (by this theorem), so it is forced to allowance3;
- for every c>=7, allowance2 is excluded;
- the next genuine single-class barrier is therefore allowance3 and above.