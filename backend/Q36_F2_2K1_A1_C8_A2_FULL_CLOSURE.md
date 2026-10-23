# q36 f=2, 2K1 far, a_F=1 — full closure of c=8, allowance two

Status: `PROVED` under `Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md`, common-S row closure, CORE211, inherited D14, lexicographic q36 maximality, and `alpha(H[R])<=2`.

This closes the A=2 layer of c=8.

## 1. Setup

Here c=8, |Y|=2, and the common-S allowance is A=2. The eight low owners have 3-point supports in the fixed 12-point remainder R with `alpha(H[R])<=2`.

From the high-c normal form, every repeated support has multiplicity at most4.

## 2. Repeated supports have defect at most one

If a repeated support D used full defect2, its repivot would remain at q36. The repivot removes x0 but retains the two decorated vertices Y, while all three support vertices are globally decorated because D repeats. Thus the new shell has at least five decorated vertices, exceeding the old three (`x0 union Y`) and contradicting lexicographic maximality.

Hence every repeated support has defect at most1 and repivots to q<=35. A proper overlap of two 3-supports costs `h(3-h)=2`, so a repeated support cannot properly overlap any different support. Therefore it is disjoint from every other distinct support, and common-S row closure gives at most one target cross-edge to any such support.

## 3. Singleton intersection components have size at most two

For two singleton supports, any proper overlap uses the full allowance2. An overlap of size2 would insert two decorated shared vertices while retaining both decorated vertices Y, increasing tau from3 to at least4. Thus proper overlap has size1.

If one singleton support met two others at different shared vertices, its repivot would again insert two decorated vertices and retain Y, increasing tau. Hence each connected intersection component of singleton supports is a common-hub sunflower.

Within one such sunflower, row closure at equality forces petals of different supports to be target-anticomplete. Three supports in one component would therefore yield an independent triple by choosing one petal from each. Thus every singleton component has size at most2.

A size-s singleton component uses `1+2s` vertices of R.

## 4. At least one repeated support exists

If all eight supports were singleton, the most economical packing would use four size-two sunflower components, requiring `4*5=20` vertices, impossible in |R|=12.

Hence a repeated support exists.

## 5. Exactly one repeated class is impossible

Let D be the only repeated class, of multiplicity m. Since m<=4, consider m=2,3,4.

The remaining `8-m` singleton supports lie outside D because a repeated support cannot properly overlap another support.

- m=2: six singleton supports require at least three size-two components, hence at least15 vertices outside D;
- m=3: five singleton supports require at least two size-two components plus one singleton component, hence at least13 vertices outside D;
- m=4: four singleton supports require at least two size-two components, hence at least10 vertices outside D.

But only nine vertices lie outside the 3-set D. Contradiction in every case.

Therefore exactly one repeated class is impossible.

## 6. Repeated classes cannot coexist with a singleton

If D,E are two repeated classes and F is any singleton support, then D,E,F are pairwise disjoint. The common-S cross-edge bound from a repeated support gives at most one target edge between each pair.

Choosing one vertex uniformly from each support gives expected target-edge count at most `3/9<1`, so some choice is an independent triple in H[R], contradiction.

Three distinct repeated classes are similarly impossible by the same random-choice argument.

Hence if repeated classes exist, there are exactly two of them and no singleton support.

## 7. The only 4+4 terminal is impossible

The two repeated multiplicities sum to8 and each is at most4, so both are4.

Let D,E be the two repeated 3-supports. They are disjoint and have `e_H(D,E)<=1`.

Put `L=R\(D union E)`, so |L|=6. To avoid an independent triple formed by one vertex of D, one vertex of E and v in L, the neighbourhood of v in D union E must cover the target-nonedge graph `K3,3` with at most one edge removed. Its minimum vertex-cover size is3. Hence

`e_H(v,D)+e_H(v,E)>=3`.

Write `w_v=kappa_v+e_F(v,x0)`. Row closure against D and E bounds each cut by w_v, so w_v>=2 for every v in L. Thus

`sum_L w_v>=12`.

But CORE211 gives `kappa(L)<=2`, and `e_F(x0,L)<=6`, so

`sum_L w_v<=8`,

contradiction.

## 8. Conclusion

No c=8,A=2 state exists:

> `c=8, A=2` is EMPTY.