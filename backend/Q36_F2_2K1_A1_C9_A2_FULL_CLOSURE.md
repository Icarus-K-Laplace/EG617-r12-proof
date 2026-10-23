# q36 f=2, 2K1 far, a_F=1 — full closure of c=9, allowance two

Status: `PROVED` under `Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md`, common-S row closure, CORE211, inherited D14, lexicographic q36 maximality, and `alpha(H[R])<=2`.

For c=9, Y has one vertex and `nu_Y=0`. If A=2, the inactive identity gives `G_Y=4`.

## 1. Repeated supports have defect at most one

A repeated support using full defect2 would repivot to q36. The repivot removes x0, retains the decorated vertex Y, and inserts three globally decorated support vertices, giving new tau at least4 versus old tau2. Contradiction.

Thus repeated supports have defect at most1. Proper overlap of 3-supports costs2, so every repeated support is disjoint from every distinct support and has at most one target cross-edge to it.

## 2. Singleton components have size at most two

For singleton supports, any proper overlap uses full allowance2. An overlap of size2 inserts two decorated shared vertices while retaining Y, raising tau from2 to at least3. Thus proper overlap has size1.

If a singleton support meets two others at different shared vertices, its repivot again inserts two decorated vertices and retains Y, increasing tau. Therefore each singleton intersection component is a common-hub sunflower.

Three supports in one sunflower yield an independent triple by choosing one petal from each, so components have size at most2. A component of s singleton supports uses `1+2s` vertices of R.

## 3. A repeated support must exist

Nine singleton supports, packed as four two-support components plus one singleton component, require

`4*5+3=23`

vertices, impossible in |R|=12.

Hence at least one repeated support exists.

The high-c multiplicity bounds with G_Y=4 give every repeated class multiplicity at most4.

## 4. Exactly one repeated class is impossible

Let its multiplicity be m=2,3,4. The remaining `9-m` singleton supports are disjoint from the repeated support and must fit into the nine vertices outside it.

The minimal singleton packing uses

- m=2: seven singletons -> `5+5+5+3=18` vertices;
- m=3: six singletons -> `5+5+5=15` vertices;
- m=4: five singletons -> `5+5+3=13` vertices.

All exceed nine. Contradiction.

## 5. Multiple repeated classes are impossible

If two repeated classes coexist with any singleton support, the three supports are pairwise disjoint and every repeated-to-other cross count is at most1. Choosing one vertex uniformly from each gives expected target-edge count at most `3/9<1`, hence an independent triple.

If no singleton occurs, two repeated classes cannot carry all nine owners because each has multiplicity at most4. Thus at least three repeated classes are needed.

Three distinct repeated supports are pairwise disjoint with at most one target edge between any pair. The same random one-from-each argument produces an independent triple.

Contradiction.

## 6. Conclusion

No c=9,A=2 state exists:

> `c=9, A=2` is EMPTY.