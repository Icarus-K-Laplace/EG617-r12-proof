# Global Block-Transversal Theorem

Status: `PROVED_ANALYTIC`.

This is a parameterized support-capacity theorem for arbitrary support size. It contains the main counting mechanism behind the sharp d=2 theorem and gives immediate d=3 capacities relevant to the E334 eleven-view system.

## 1. Theorem

Let H be a graph with

`alpha(H)<=3`.

Let

`D_1,...,D_N`

be pairwise disjoint vertex blocks, each of size d. Assume that for all i!=j,

`e_H(D_i,D_j)<=c`.                                          (1)

Then necessarily

> `C(N,2)-floor(N^2/3) <= (c/d^2) C(N,2)`.                 (2)

If (2) fails, the support system is impossible.

## 2. Proof

Choose one vertex independently and uniformly from each block, producing an N-point transversal T.

For a fixed block pair i,j, at most c of the `d^2` endpoint pairs are target edges. Hence

`Pr(T chooses an H-edge between D_i,D_j)<=c/d^2`.

Summing,

`E[e_H(T)] <= (c/d^2) C(N,2)`.                             (3)

But every transversal is an induced subgraph of H and therefore has independence number at most3. Its complement is K4-free, so Turan's theorem gives

`e_H(T)>=C(N,2)-ex(N,K4)`
`       =C(N,2)-floor(N^2/3)`.                              (4)

Averaging (4) and comparing with (3) proves (2).

## 3. Equality mechanism

If equality holds in (2), then equality must hold in both parts of the argument:

1. every block pair carries exactly c target cross-edges;
2. every transversal has exactly
   `C(N,2)-floor(N^2/3)` target edges;
3. every transversal complement is a Turan-extremal K4-free graph.

Thus an average bound becomes a rigid global product-space equality problem.

Write the transversal edge-count function as

`f(x_1,...,x_N)=sum_(i<j) A_ij(x_i,x_j)`,                  (5)

where each A_ij is the d-by-d 0/1 cross-adjacency matrix between D_i and D_j.

If f is constant, every mixed discrete difference in coordinates i,j vanishes. Therefore every A_ij has zero 2x2 mixed minors:

`A_ij(a,b)+A_ij(a',b')=A_ij(a,b')+A_ij(a',b)`              (6)

for all endpoint choices.

A 0/1 matrix satisfying (6) is additive (row potential plus column potential). Unless it is constant, all of its 1s are a union of complete rows or a union of complete columns. In particular its number of 1s is a multiple of d.

Hence an equality state with

`0<c<d`

is impossible. This recovers the mixed-difference obstruction used in the d=2 equality cases.

## 4. d=3, cross allowance one

Take d=3,c=1.

For N=4,

`C(4,2)-floor(16/3)=6-5=1`,

while

`(1/9)C(4,2)=2/3`.

Thus N=4 is impossible, and the gap only grows for larger N.

Therefore

> **d=3, c<=1 => N<=3.**                                    (7)

This is a strong generic capacity theorem for disjoint triple supports with unit cross allowance.

## 5. d=3, cross allowance two

Take d=3,c=2.

For N=7,

`C(7,2)-floor(49/3)=21-16=5`,

whereas

`(2/9)C(7,2)=14/3<5`.

For N>7 the asymptotic gap is strictly larger; algebraically, replacing the floor by `N^2/3`, the lower-minus-upper difference is

`N(N-7)/18`,

strictly positive for N>7.

Hence

> **d=3, c<=2 => N<=6.**                                    (8)

## 6. d=2 specialization

For d=2,c=1, (2) gives the basic threshold and equality cases N=8,9 analyzed in `GLOBAL_D2_TRANSVERSAL_CAPACITY_THEOREM.md`.

The sharper Boolean-cube argument in `GLOBAL_D2_TRANSVERSAL_SHARP_CAPACITY_THEOREM.md` eliminates N=7 as well and yields

`N<=6`.

Thus the d=2 and d=3 low-cross regimes now share one conceptual proof architecture.

## 7. Bridge to the E334 d3 eleven-view system

Suppose the unresolved E334 d3 eleven-view system can be shown to contain seven pairwise disjoint three-point support classes whose pairwise target cross-edge counts are at most2.

Then (8) immediately contradicts `alpha(H)<=3`.

Therefore the entire eleven-view problem reduces to one extraction/equality question:

> either extract seven disjoint low-cross triple supports,
> or prove that failure of such an extraction forces a common-pair / four-set / sunflower / high-codegree equality geometry.

This is substantially smaller than eleven independent view cases and is the natural d=3 component of the Global Support-Compatibility Bridge.

## 8. General form

For a residual core with independence number at most r, the same proof replaces K4 by K_(r+1):

`C(N,2)-ex(N,K_(r+1)) <= (c/d^2)C(N,2)`.

Hence the theorem is not specific to r=12. Any higher-r pivot reduction that yields bounded cross-density between disjoint support blocks inherits the same transversal obstruction.