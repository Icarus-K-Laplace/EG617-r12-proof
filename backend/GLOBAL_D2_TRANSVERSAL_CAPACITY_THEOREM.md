# Global D2 Transversal Capacity Theorem

Status: `PROVED_ANALYTIC`.

This is a witness-free capacity theorem for common two-point support systems. It strengthens the low-charge capacity theorem and is independent of the edge-layer labels `E333,...,E340`.

## 1. Statement

Let H be any graph with

`alpha(H)<=3`.

Let

`D_1,...,D_N`

be pairwise disjoint two-point subsets of `V(H)`. Assume that for every two distinct blocks

> `e_H(D_i,D_j)<=1`.                                         (1)

Then

> **N<=7.**                                                   (2)

No outside charge witness is required.

## 2. Random transversal

Choose independently and uniformly one endpoint from each two-point block. Let T be the resulting N-point transversal.

For each pair i<j, condition (1) says that among the four endpoint choices from `D_i x D_j`, at most one is a target edge. Hence

`Pr(selected endpoints from D_i,D_j form an H-edge)<=1/4`.

Therefore

> `E[e_H(T)] <= C(N,2)/4`.                                   (3)

On the other hand every transversal T is an induced N-vertex subgraph of H, so

`alpha(H[T])<=3`.

Equivalently the complement of H[T] is K4-free. By Turan's theorem,

`e(complement(H[T]))<=ex(N,K4)=floor(N^2/3)`.

Thus every transversal satisfies

> `e_H(T) >= C(N,2)-floor(N^2/3)`.                            (4)

## 3. N>=10 is impossible numerically

For N>=10,

`C(N,2)-N^2/3 > C(N,2)/4`

because the difference is

`N(N-9)/24>0`.

Since `floor(N^2/3)<=N^2/3`, (4) is strictly larger than the upper expectation (3), impossible.

Hence

`N<=9`.                                                       (5)

## 4. The equality cases N=9 and N=8 are impossible

### N=9

Here

`C(9,2)-floor(81/3)=36-27=9`

and

`C(9,2)/4=9`.

Therefore equality must hold simultaneously in (3) and (4).

In particular:

1. every block pair has exactly one target cross-edge;
2. every one of the `2^9` endpoint transversals has exactly nine target edges.

### N=8

Likewise

`C(8,2)-floor(64/3)=28-21=7`

and

`C(8,2)/4=7`.

So equality again forces:

1. every block pair has exactly one target cross-edge;
2. every one of the `2^8` transversals has exactly seven target edges.

We now show that this is impossible for either N=8 or N=9.

## 5. Mixed-difference obstruction to constant transversal edge count

Label the two endpoints in block `D_i` by a bit `x_i in {0,1}`. Let

`f(x_1,...,x_N)=e_H(T_x)`

be the number of target edges in the corresponding transversal.

Since every pair of blocks has exactly one target cross-edge, for each i<j there is a unique ordered bit pair `(a_ij,b_ij)` such that the selected endpoints contribute an edge exactly when

`(x_i,x_j)=(a_ij,b_ij)`.

Thus

`f(x)=sum_(i<j) 1[(x_i,x_j)=(a_ij,b_ij)]`.                  (6)

Equality in the preceding section says f is constant on the entire Boolean cube.

Fix one pair i<j. Take the mixed discrete difference in the two variables:

`Delta_i Delta_j f`.

Every summand in (6) involving neither or only one of i,j vanishes under the mixed difference. The only surviving summand is the unique indicator for the pair i,j.

But a 2x2 indicator matrix with exactly one entry equal to1 has nonzero mixed difference (`+1` or `-1`). Hence

`Delta_i Delta_j f !=0`,

contradicting constancy of f.

Therefore neither N=8 nor N=9 can occur.

Together with (5):

> `N<=7`.                                                      (7)

## 6. Interpretation as support compatibility

For common two-point support rows, the joint-row theorem frequently gives exactly condition (1): distinct disjoint supports carry at most one target cross-edge.

The theorem then gives an immediate global capacity bound seven, without requiring:

- a zero-charge witness;
- a charge-one witness;
- a separate E-layer argument;
- a computer enumeration.

Thus any forced family requiring eight or more disjoint two-support classes is impossible for a purely global reason.

## 7. Relation to the earlier low-charge theorem

`GLOBAL_D2_LOW_CHARGE_CAPACITY_THEOREM.md` proved:

- charge0 witness => at most2 blocks;
- charge1 witness => at most8 blocks.

The present theorem supersedes the second numerical bound whenever the stronger pairwise cross-edge hypothesis (1) is available:

> disjoint two-supports + cross-edge<=1 => at most7 blocks,

with no witness hypothesis at all.

The low-charge theorem remains useful when cross-edge allowance is larger or when proper support overlaps remain possible.

## 8. Equality frontier

The first possible extremal size is now N=7.

For N=7, every transversal has at least

`C(7,2)-floor(49/3)=21-16=5`

target edges, whereas the expected number is at most

`21/4=5.25`.

Hence any N=7 equality survivor is already near-rigid:

- at least20 of the21 block pairs must carry a target cross-edge;
- if only20 carry edges, every transversal must have exactly5 target edges, which is impossible by the same mixed-difference argument on any pair carrying an edge;
- therefore all21 block pairs carry exactly one cross-edge;
- the transversal edge-count function has mean21/4 and minimum at least5.

Thus N=7 is the unique first equality boundary and should be attacked globally rather than as a D2-D-specific case.

This identifies a single seven-block Boolean-incidence equality problem as the next d=2 rigidity target.

## 9. Generalization

The proof is a general block-transversal principle: for b-point blocks with at most c cross edges per block pair and global independence number at most r, compare the expected transversal edge count `c/b^2 * C(N,2)` with the complement Turan bound `ex(N,K_(r+1))`.

The two-point/r=3 case gives the sharp witness-free threshold above and is not intrinsically tied to the numerical r=12 backend constants.