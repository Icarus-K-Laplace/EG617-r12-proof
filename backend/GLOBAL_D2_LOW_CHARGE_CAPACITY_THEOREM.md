# Global D2 Low-Charge Capacity Theorem

Status: `PROVED_ANALYTIC`.

This is a first concrete bridge theorem derived from the global support-compatibility framework. It unifies the zero-charge and charge-one witness mechanisms for common two-point support systems.

## 1. Setup

Let H be a core with

`alpha(H)<=3`.

Let

`D_1,...,D_N`

be pairwise disjoint two-point support classes belonging to one common missing-set family.

Assume the common-S row closure / allowance gives

> `e_H(D_i,D_j)<=1` for every `i!=j`.                       (1)

Let U be their union.

Let v be a core vertex outside U and suppose row closure gives

`e_H(v,D_i)<=t`

for every i.

The two useful cases are `t=0` and `t=1`.

## 2. Zero-charge witness: at most two disjoint supports

Assume `t=0`.

Then v is target-anticomplete to U. Therefore

`alpha(H[U])<=2`,                                             (2)

because an independent triple in U together with v would be an independent4 in H.

Suppose three disjoint support blocks exist. Select one endpoint independently and uniformly from each of the three two-point blocks.

For each pair of support blocks, (1) says there is at most one target cross-edge among the four possible endpoint pairs. Hence the probability that the selected pair is a target edge is at most `1/4`.

The expected number of target edges among the three selected vertices is therefore at most

`3/4<1`.

Hence some selection spans no target edge, producing an independent triple in U, contradicting (2).

Therefore

> if an outside zero-charge witness exists, `N<=2`.          (3)

This is the disjoint-support core of the V5 zero-charge concentration mechanism.

## 3. Charge-one witness: at most eight disjoint supports

Assume `t<=1`.

For each support block

`D_i={x_i,y_i}`,

choose `x_i` target-nonadjacent to v; this is possible because v has at most one target neighbour in D_i.

Put

`X={x_1,...,x_N}`.

Since v is target-nonadjacent to every x_i,

> `alpha(H[X])<=2`.                                          (4)

Let

`Y={y_1,...,y_N}`

be the complementary endpoints.

For any pair i,j, if both `x_i x_j` and `y_i y_j` were target edges, there would be at least two target cross-edges between D_i and D_j, contradicting (1). Therefore

`E(H[Y]) subseteq E(complement(H[X]))`.                      (5)

By (4), `complement(H[X])` is triangle-free. Hence

> H[Y] is triangle-free.                                     (6)

Also Y is a subset of H, so

`alpha(H[Y])<=3`.                                            (7)

A triangle-free graph on nine vertices always has an independent4. For completeness:

- if some vertex has degree at least4, its neighbourhood is an independent4;
- otherwise maximum degree is at most3;
- on nine vertices not every degree can equal3 because the degree sum would be odd, so some vertex has degree at most2;
- that vertex has at least six nonneighbours;
- among six vertices, triangle-freeness and the classical `R(3,3)=6` fact give an independent3;
- together with the original vertex this is an independent4.

Thus a triangle-free graph with independence number at most3 has at most eight vertices.

Combining (6)--(7),

> if an outside charge-at-most-one witness exists, `N<=8`.  (8)

## 4. Equality regime at N=8

If N=8 in the charge-one case, H[Y] is an eight-vertex `(3,4)` Ramsey-critical graph:

- triangle-free;
- independence number exactly3.

Simultaneously H[X] has independence number at most2 and every H[Y] edge lies in the complement of H[X].

Therefore every N=8 disjoint-support survivor is forced into a Ramsey-critical equality geometry rather than an arbitrary support system.

This is the correct equality object to combine with core excess, hereditary 13/14-point caps and support multiplicity constraints.

## 5. Consequences for the r=12 backend

### R9-type lower bound

Any common two-point family which forces nine pairwise disjoint supports, has cross allowance at most1, and admits an outside charge-one witness is impossible immediately by (8).

Thus the old `R9` repetition-nine phenomenon is explained by a general low-charge capacity theorem, not a family-specific contradiction.

### Eight-support families

D2 families requiring eight supports naturally fall onto the N=8 equality boundary. They should therefore be treated together by one equality-rigidity argument, rather than as separate D2-A/D2-B cases.

The V5/V6 two-clique-plus-perfect-matching and intersecting-K11 arguments can be interpreted as stronger equality closures once additional support/hub information is imposed.

## 6. Why this matters for E334+

The V5 method required an outside zero-charge witness. The theorem above shows the first stable extension:

- charge0 witness => at most2 disjoint supports;
- charge1 witness => at most8 disjoint supports, with N=8 Ramsey-critical;
- charge2 is therefore the next genuinely new structural threshold.

This identifies the high-layer problem more sharply: E334--E337 do not need new layer-by-layer shell enumerations; they need a charge-2 equality theorem for the support incidence graph.

That is now the natural next bridge target.
