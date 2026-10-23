# q36 f=2, 2K1 far, a_F=1 — full closure of c=7 allowance-two branch

Status: `PROVED` under `Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md`, row closure, CORE211, inherited D14, lexicographic q36 maximality, and `alpha(H[R])<=2`.

This leaves only the c=7 allowance-three/K11 branch.

## 1. Exact c=7,A=2 setup

The inactive decorated set Y has three vertices. From the high-c normal form,

`A+G_Y=6-nu_Y`.

With A=2, `G_Y=4-nu_Y` and `nu_Y in {0,1}`.

The old decorated-vertex count is four: x0 plus Y.

Every support is a 3-subset of the fixed 12-point remainder R with `alpha(H[R])<=2`.

## 2. Repeated supports have defect at most one and are disjoint from all other supports

If a repeated support D had full defect2, its repivot would remain at q36. All three support vertices have at least two shell owners and are globally decorated. The repivot removes x0 but retains the three decorated vertices Y, so the new shell would have at least six decorated vertices versus the old four, contradicting lexicographic maximality.

Hence every repeated support has defect at most1 and repivots to q<=35.

A proper overlap of two 3-supports costs `h(3-h)=2`. Therefore a repeated support cannot properly overlap any different support. Distinct supports from a repeated class are disjoint from it, and the common-S joint-row theorem gives at most one target cross-edge.

## 3. Singleton intersection components are size-at-most-two sunflowers

Let D,E be distinct singleton supports with proper overlap.

Because the overlap cost is2, both rows use the full allowance. An overlap of size2 would insert two decorated shared vertices into a q36 repivot while retaining the three decorated inactive shell vertices Y, giving new tau at least5>4. Hence any proper overlap has size1.

If one support met two others at different shared vertices, its repivot would again insert two decorated vertices and raise tau. Thus every connected intersection component of singleton supports is a common-hub sunflower.

For a support in such a component, the two petals are forced by row closure to be target-anticomplete to petals of the other supports in the same sunflower. Three supports in one sunflower therefore yield an independent triple by choosing one petal from each.

Hence every singleton-support component has size at most2.

A component with s singleton supports uses `1+2s` vertices of R.

## 4. A repeated support must exist

Seven distinct singleton supports, packed into components of size at most2, need at least

`5+5+5+3=18`

vertices, exceeding `|R|=12`.

Thus a repeated support exists.

Every repeated class has multiplicity at most4 by the high-c D14/decoration bounds.

## 5. Exactly one repeated class is impossible

Let D be the only repeated class, of multiplicity m.

The remaining `7-m` singleton supports lie outside D.

If m=2, five singleton supports need at least13 vertices outside D.
If m=3, four singleton supports need at least10 vertices outside D.
Both exceed the available nine vertices.

Thus m=4 is the only packing possibility. Then three singleton supports remain. Since a singleton component has size at most2, they consist of one two-support sunflower component and one disjoint singleton component.

Choose one support E from the sunflower pair and the disjoint singleton support F. The three supports D,E,F are pairwise disjoint. Cross-edge bounds are

- `e(D,E)<=1`;
- `e(D,F)<=1`;
- `e(E,F)<=2`.

Choosing one vertex uniformly from each block gives expected target-edge count at most

`(1+1+2)/9<1`.

Hence some choice is an independent triple in H[R], contradiction.

So exactly one repeated class is impossible.

## 6. Exactly two repeated classes and no singleton are forced

Three distinct repeated classes are pairwise disjoint with at most one target edge between any pair. A random one-from-each choice has expected target-edge count at most `3/9<1`, giving an independent triple. Thus there are at most two repeated classes.

If two repeated classes D,E coexisted with any singleton support F, then D,E,F would be three pairwise disjoint supports with each repeated-to-other cross count at most1. Again the expected target-edge count is at most `3/9<1`, contradiction.

Therefore all seven owners are split between exactly two repeated supports D,E.

Each multiplicity is at most4, so the only partition is

> `4+3`.                                                     (1)

The supports are disjoint and satisfy `e_H(D,E)<=1`.

## 7. The 4+3 terminal violates the w-mass bound

Put

`L=R\(D union E)`,

so `|L|=6`.

For v in L, to avoid an independent triple with one vertex from D and one from E, the neighbourhood of v in `D union E` must cover all target-nonedges between D and E. Since `e_H(D,E)<=1`, that nonedge graph is K3,3 with at most one edge removed and has minimum vertex-cover size3. Therefore

`e_H(v,D)+e_H(v,E)>=3`.                                    (2)

Define

`w_v=kappa_v+e_F(v,x0)`.

Row closure for D and E gives each cut at most w_v. Thus (2) implies `w_v>=2` for every v in L, so

`sum_L w_v>=12`.                                           (3)

But CORE211 gives `kappa(L)<=2`, and trivially `e_F(x0,L)<=|L|=6`. Hence

`sum_L w_v = kappa(L)+e_F(x0,L) <= 8`,

contradicting (3).

## 8. Conclusion

The c=7 allowance-two branch is empty:

> `c=7, A=2` is EMPTY.

By the high-c normal form, the only remaining c=7 state has

- `A=3`;
- `nu_Y=0`;
- Y is a target K3;
- all three inactive decorations equal1;
- `{p} union C union Y` is a target K11.