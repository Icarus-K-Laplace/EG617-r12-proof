# Global d=3 Allowance-Two Overlap Rigidity Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_SUPPORT_COMPATIBILITY_THEOREM.md`;
- `GLOBAL_SUPPORT_REPETITION_CHARGING_THEOREM.md`;
- the exact common-S joint-row overlap inequality;
- exact tau transport and lexicographic maximality of `(q,tau)`.

Purpose: classify the equality geometry created by proper overlap in a triple-support family with allowance two. This is the next low-support bridge regime after `GLOBAL_D3_ALLOWANCE_ONE_COLLAPSE.md`.

## 1. Setup

Let H satisfy

`alpha(H)<=3`.

Let Y be a common-S family of regular owner rows with

`|S|=d=3`.

For a support D write

`w(D)=sum_(v in D)(kappa_v+e_F(v,S))`,

`mu(D)=3-e_H(D)`.

Assume common row allowance

> `w(D)+mu(D)<=a=2` for every owner support D.               (1)

Let

`s=|S intersect X|`,                                        (2)

where X is the globally decorated set.

## 2. Proper overlap forces full allowance saturation

Let D,E be two distinct support classes with proper overlap

`h=|D intersect E| in {1,2}`.

The exact joint-row inequality gives

`h(3-h)<=w(E\D)+mu(E)`.                                    (3)

But

`h(3-h)=2`                                                   (4)

for h=1 or2, while

`w(E\D)+mu(E)<=w(E)+mu(E)<=2`.                              (5)

Therefore equality holds throughout:

> `w(E\D)+mu(E)=2`,                                         (6)
>
> `w(E)+mu(E)=2`,                                           (7)
>
> `w(E intersect D)=0`.                                     (8)

By symmetry the same conclusions hold with D and E exchanged.

Hence every support participating in a proper overlap is a q-plateau support:

`q_E=q_D=q`.                                                 (9)

Also every shared vertex has zero common-S charge.

## 3. Overlap vertices are decorated

The exact two-row decoration identity from the joint-pivot theorem implies that every support-overlap vertex is globally decorated.

Thus every point in `D intersect E` lies in X.               (10)

Since D and E are plateau supports, tau-maximality gives

`|D intersect X|<=s`,
`|E intersect X|<=s`.                                       (11)

Combining (10)--(11):

> every proper overlap satisfies `h<=s`.                    (12)

This immediately separates the decoration regimes.

## 4. The case s=0: proper overlap is impossible

If `s=0`, equation (12) rules out h=1 and h=2.

Therefore

> for `s=0`, distinct support classes are pairwise disjoint. (13)

This converts the entire allowance-two family to the disjoint-block regime, where `GLOBAL_BLOCK_TRANSVERSAL_THEOREM.md` applies directly with cross allowance at most2.

In particular the number of distinct support classes is at most6.

## 5. The case s=1: every overlap component is a common-hub sunflower

Assume `s=1`.

Equation (12) forces

> every proper overlap has size exactly1.                    (14)

Consider one support D that properly overlaps another support. Let x be the shared point.

By (10), x is decorated. Since D is a plateau support and may contain at most one decorated vertex, every other point of D is globally clean.

Now suppose D properly overlaps two distinct classes E and T in points x and y respectively. Both x and y are support-overlap vertices and therefore decorated. Tau-maximality forces x=y.

Hence

> all proper overlaps incident with one support use the same support vertex.   (15)

Along any connected component of the support-intersection graph, (15) propagates from edge to edge. Therefore there is a single core point x_C common to every support in the component.

Thus:

> every nontrivial proper-overlap component is a common-hub sunflower.   (16)

Different components are vertex-disjoint at the support level.

## 6. Exact support geometry in an s=1 sunflower

Let D={x,u,v} be a support in a nontrivial sunflower component, where x is the common hub.

The hub x is decorated by overlap and has charge

`w_x=0`                                                     (17)

from the equality statement (8).

The private points u,v cannot be decorated, because D is a plateau support and already contains the unique allowed decorated vertex x.

By the repetition/charge decoration theorem, any support-union point with positive charge is decorated. Therefore

`w_u=w_v=0`.                                                (18)

Also a private point cannot lie in a second distinct support class, because that would create a second overlap point in D and violate (15). Hence its support-incidence degree is exactly1.

Thus

`w(D)=0`.                                                    (19)

Since the support saturates allowance two by (7),

`mu(D)=2`.                                                   (20)

Therefore

> every support in a nontrivial s=1 overlap component is an exact one-edge triple.   (21)

Its hub is zero-charge but globally decorated by overlap; its two petals are private, globally clean, zero-charge vertices.

This is a rigid equality geometry, not merely a sunflower incidence pattern.

## 7. Repeated support classes are isolated from proper-overlap components

Let D be a support class used by at least two owners.

Every point of D is globally decorated by repetition.

Since `s<3` for s=0 or1, a repeated support cannot be a q-plateau row: at equal q its repivot would insert all three decorated support points while deleting at most s decorated missing-set points, strictly increasing tau.

Hence every owner using D has strict q-loss and

`w(D)+mu(D)<=1`.                                            (22)

But every support participating in a proper overlap has full defect exactly2 by Section2.

Therefore

> a repeated support class cannot properly overlap any distinct support class.   (23)

So repeated classes are disjoint from all distinct classes in the s=0,1 allowance-two regimes.

Moreover (22) shows that every repeated class is necessarily one of:

- a target K3 with `w(D)<=1`; or
- a two-edge triple with `w(D)=0`.

A one-edge repeated triple is impossible because `mu(D)=2>1`.

## 8. Structural decomposition for s=1

Combining the preceding sections, every d=3,a=2,s=1 common-S family decomposes into disjoint structural pieces of only three kinds:

1. isolated repeated dense supports (K3 or two-edge, defect at most1);
2. nontrivial common-hub sunflower components made entirely of exact one-edge zero-charge triples;
3. singleton support classes disjoint from the above components.

No repeated support belongs to a sunflower component. No sunflower support has more than one overlap hub.

Thus the original multi-view system is reduced to a bounded collection of explicit support-incidence geometries.

## 9. Connection to block-transversal capacity

If the family contains seven pairwise-disjoint distinct supports, `GLOBAL_BLOCK_TRANSVERSAL_THEOREM.md` with d=3,c=2 gives an immediate contradiction.

Therefore, after removing the rigid sunflower components and isolated repeated supports, the disjoint-support matching number is at most6.

Together with `GLOBAL_LOW_SUPPORT_MATCHING_COVER_BRIDGE.md`, all remaining support classes are hit by an 18-point core transversal.

The genuinely new equality object at allowance two is therefore not an arbitrary hypergraph but the union of:

- exact one-edge common-hub sunflowers;
- isolated repeated dense triples;
- a bounded disjoint matching skeleton.

This is the correct input for the hereditary support-packing theorem.

## 10. Why this is a bridge theorem

The theorem identifies the exact reason proper-overlap survivors can exist at allowance two: the overlap inequality is forced to equality.

That equality simultaneously fixes

- q plateau status;
- zero charge on overlap vertices;
- decoration on overlap vertices;
- the number of decorated vertices permitted by tau;
- and, for s=1, the entire internal edge type of each overlapping support.

Thus the allowance-two branch should be closed by excluding one sunflower/repeated-block equality geometry, not by enumerating owner views.

## 11. Generalization

The saturation mechanism uses only

`h(d-h)=a`

at the overlap threshold and exact tau transport. For other support sizes d, any regime in which the minimum proper-overlap cost equals the full row allowance has the same qualitative consequence:

proper overlap => plateau => shared zero-charge decorated core => equality geometry.

Hence this theorem is a d=3 instance of a more general overlap-saturation principle potentially applicable for r>=13.