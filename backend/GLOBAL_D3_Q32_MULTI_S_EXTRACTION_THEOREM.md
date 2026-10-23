# Global d=3 q32 Multi-S Extraction Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- `HIGH_LAYER_V3_JOINT_CANONICAL.md`;
- `GLOBAL_BLOCK_TRANSVERSAL_THEOREM.md`;
- maximality of q;
- the all-pivot 35-core minimum-degree contract.

Purpose: bridge a genuine multi-view d3 system to the common-S support machinery without assuming in advance that the missing triples are equal.

## 1. Setup

Let p be a maximum-q pivot in the r=12 backend with

`q<=32`.

Let Y be any family of regular shell vertices satisfying

`|S_y|=|D_y|=3`

for every `y in Y`, where

`S_y=N_M(y)`,

`D_y=N_H(y)`.

No common-S hypothesis is imposed.

## 2. Any two d3 owners are target-adjacent

Take distinct `y,z in Y`.

Suppose yz were a target nonedge, equivalently an edge of the shell missing graph M.

The regular nonadjacent zero-gap theorem gives

`S_y union S_z=A`.

But both missing sets have size3, hence

`|S_y union S_z|<=6`,

whereas `|A|=13`.

Contradiction.

Therefore

> **every two d3 owners in Y are target-adjacent.**           (Q1)

Hence Y itself is a target clique. Together with the pivot p,

`{p} union Y`

is a target clique, so under `omega(F)<=11`,

> `|Y|<=10`.                                                  (Q2)

## 3. Pair-intersection compatibility

Take distinct y,z in Y. Put

`o=|S_y intersect S_z|`,

`h=|D_y intersect D_z|`.

Because yz is a target edge, the exact third-view formula gives the missing degree of z in the y-view:

`delta_y(z)=6-o-h`.                                          (Q3)

For adjacent regular pivots, the metric/exchange bound gives

`delta_y(z)(13-delta_y(z))<=q_z<=q<=32`.                     (Q4)

Now `0<=delta_y(z)<=6`.

The values 4,5,6 give respectively

`36,40,42>32`.

Therefore

`delta_y(z)<=3`.

Using (Q3):

> **`|S_y intersect S_z|+|D_y intersect D_z|>=3`.**           (Q5)

This is the basic multi-S compatibility inequality.

## 4. Disjoint supports force a common missing triple

If

`D_y intersect D_z=empty`,

then h=0, so (Q5) gives

`|S_y intersect S_z|>=3`.

Since both sets have size3,

> `S_y=S_z`.                                                  (Q6)

Thus any two disjoint d3 core supports automatically belong to the same common-S family.

By transitivity:

> **every pairwise-disjoint collection of d3 supports is a common-S owner subfamily.**   (Q7)

This is the missing extraction bridge between multi-S and common-S arguments.

## 5. Matching number at q32

Let

`D_1,...,D_k`

be pairwise-disjoint supports from Y.

By (Q7), their owners share one missing triple S.

For a q32 d3 row, the exact exchange formula has base term30. Hence the common-S row allowance is at most2:

`w(D_i)+mu(D_i)<=2`.                                        (Q8)

For two distinct disjoint common-S supports, joint row closure gives

`e_H(D_i,D_j)<=min(w(D_i),w(D_j))<=2`.                       (Q9)

Therefore the disjoint supports form 3-point blocks with pairwise target cross-edge count at most2.

`GLOBAL_BLOCK_TRANSVERSAL_THEOREM.md` proves that seven such blocks are impossible in a core with `alpha(H)<=3`.

Hence

> **the support-hypergraph matching number satisfies `nu<=6`.**   (Q10)

## 6. Bounded core transversal

Take a maximal matching of distinct support classes. By (Q10) it has at most6 blocks.

The union C of these blocks has size at most18 and meets every distinct support class; otherwise a support disjoint from C would extend the matching.

Thus

> **every q32 multi-S d3 support system has a core transversal of size at most18.**   (Q11)

This conclusion is now genuinely multi-S; no missing-set equality was assumed.

## 7. Strong owner-count consequences

Because Y is a clique, every missing set S_y avoids every vertex of Y. Hence

`S_y subseteq A\Y`.                                         (Q12)

Therefore:

### |Y|=10

`|A\Y|=3`.

Every S_y is a 3-subset of this same three-point complement, so

> **all ten rows automatically have one common missing triple.**   (Q13)

Thus the N=10 regime is not genuinely multi-S at all.

### |Y|=9

`|A\Y|=4`.

Every S_y is one of the four 3-subsets of a fixed four-point set. Any two distinct missing-set types intersect in exactly2 points. By (Q5), rows of different missing-set types have supports intersecting in at least one core vertex.

Hence the N=9 multi-S regime already has a four-type bounded-hub structure.

### |Y|=8

`|A\Y|=5`.

Any two missing triples intersect in at least one point. If their intersection has size1, (Q5) forces support overlap at least2; if it has size2, support overlap at least1. Disjoint supports can occur only inside one common-S type by (Q6).

These are structural reductions, not case closures.

## 8. Repeated-support versus distinct-support dichotomy

Combine (Q10)--(Q11) with `GLOBAL_MULTI_S_REPIVOT_COMPATIBILITY.md`.

Any q32 d3 multi-view system satisfies one of two regimes:

1. **high repetition:** some core support has significant owner multiplicity, triggering the multi-S strict-loss / near-K3 dichotomy and the repeated-support dense-block theorem;
2. **mostly distinct supports:** all distinct supports are hit by an at-most18-point core transversal, and pairwise support/missing-set intersections obey (Q5).

Thus the unresolved multi-view problem is no longer arbitrary. It is a bounded-transversal incidence problem with an exact pair-intersection law.

## 9. Relation to the source-reported E334 eleven-view system

This theorem does not assert that the source-reported eleven views are eleven simultaneous d3 owners at one pivot; indeed (Q2) shows that such a configuration would be impossible.

What it proves is the correct reusable statement:

> whenever a subset of those views is represented by simultaneous q32 d3 regular rows at one maximal pivot, its support/missing-set data satisfy (Q1)--(Q13).

Therefore any full eleven-view bridge must specify how the views are distributed among pivots or row systems, then apply this theorem inside each simultaneous system.

This is the exact scope boundary needed to avoid conflating `view` with `common-S owner`.

## 10. Parameterized interpretation

The key inequality (Q5) comes from

`delta=d+d-o-h`

combined with the forbidden metric gap forced by the q ceiling.

Thus for other r or other q ceilings, the same method yields a symbolic lower bound on

`|S_y intersect S_z|+|D_y intersect D_z|`.

The multi-S extraction mechanism is therefore not intrinsically tied to r=12.