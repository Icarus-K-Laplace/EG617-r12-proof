# q36 f=2, 2K1 far, a_F=1 — c=9, allowance four multiplicity reduction

Status: `PROVED REDUCTION` under `Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md`, common-S row closure, inherited D14, lexicographic q36 maximality, and `alpha(H[R])<=2`.

For c=9, Y consists of one inactive decorated vertex y. At A=4 the inactive identity gives `g_y=2`.

This note eliminates multiplicity4 and every nonclique multiplicity-three support. Any remaining multiplicity-three support must be a target K3 with very small weighted overlap.

## 1. Repeated supports have defect at most three

A repeated support with full defect4 would repivot to q36, retain the decorated vertex y, and insert three globally decorated support vertices. The new tau would be at least4, exceeding the old tau2. Therefore every repeated support has defect at most3 and repivots to q<=35.

## 2. Multiplicity four is impossible

Let D have multiplicity4. The K11/D14 cap is

`12+O_D+e_F(y,D)+e_H(D)<=14`,

so

`O_D+e_F(y,D)+e_H(D)<=2`.                                 (1)

If D is nonclique, its common-S cross allowance is at most1 (one-edge D) or2 (two-edge D). Any disjoint support requires at least3 D--E target edges to cover an internal nonedge, impossible. Hence all five remaining owner incidences intersect D, giving `O_D>=5`, contradicting (1).

If D is a K3, `e_H(D)=3` already contradicts (1).

Thus multiplicity4 is impossible.

## 3. Multiplicity-three nonclique supports are impossible

Let D have multiplicity3. D14 gives

`O_D+e_F(y,D)+e_H(D)<=5`.                                 (2)

### One-edge D

Here m(D)=2, and defect<=3 gives common-S cross allowance at most1. A disjoint support would require at least3 cross edges to cover the two internal nonedges of D. Hence no disjoint support exists.

Six owner incidences remain outside the multiplicity-three class, so `O_D>=6`, contradicting (2).

### Two-edge D

Here m(D)=1 and the cross allowance is at most2. Again a disjoint support would require at least3 cross edges to cover the unique internal nonedge. Thus `O_D>=6`, while (2) gives `O_D<=3`. Contradiction.

Therefore every multiplicity-three support must be a target K3.           (3)

## 4. Exact interface for a repeated K3

For a target K3 D, (2) reduces to

> `O_D+e_F(y,D)<=2`.                                       (4)

There are six owner incidences outside the D-class. Since each intersecting incidence contributes at least one to O_D, at most two of them can come from supports intersecting D.

Hence at least four owner incidences lie in supports disjoint from D.       (5)

The repeated-support defect bound gives

`kappa(D)+e_F(x0,D)<=3`,

so a disjoint nonclique support can in principle saturate the three-edge cross-cover threshold. This is the first allowance level at which the previous low-allowance disjoint-support contradiction no longer closes automatically.

## 5. Frontier

The c=9,A=4 layer now satisfies:

- support multiplicity at most3;
- every multiplicity-three support is a target K3;
- such a K3 obeys `O_D+e_F(y,D)<=2` and therefore has at least four external owner incidences in supports disjoint from it.

The next task is the compatibility of this repeated K3 with the forced disjoint-support family.