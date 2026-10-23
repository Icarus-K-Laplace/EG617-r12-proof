# q36 f=2 far-target-K2 — c=8, one d2 row, allowance-three multiplicity reduction

Status: `PROVED REDUCTION` under `Q36_F2_FAR_K2_C8_D2_REDUCTION.md`, `Q36_F2_FAR_K2_C8_D2_A2_FULL_CLOSURE.md`, common-S row closure, inherited D14, q36 lexicographic maximality, and the induced `alpha(H[U])<=2` property from the pure d2 block.

Scope: c=8, n2=1, one d3 missing-set class of allowance A=3. This file does not close the layer; it reduces multiplicity >=3 to two exact geometries.

## 1. Setup and alpha-two support union

Let D0 be the unique pure globally-regular d2 support. All seven d3 owners share one missing set

`S=F union {x}`

with allowance3.

As proved in the A=2 closure, D0 is target-anticomplete to every d3 support. Hence the union U of all d3 supports satisfies

`alpha(H[U])<=2`: an independent triple in U together with either vertex of D0 would form an independent4-set in H.

## 2. Repeated supports have defect at most two

A repeated d3 support using full defect3 would repivot to q36. The repivot removes x, retains the two other decorated vertices of X, and inserts three globally decorated support vertices, increasing tau above3.

Therefore every repeated support has defect at most2 and repivots to q<=35.          (1)

## 3. Multiplicity four is impossible

Let D have multiplicity4. The K11 base `{p} union C union F` and D14 give

`12 + O_D + e_F(F,D) + e_H(D) <=14`.                       (2)

Because repeated defect<=2, D has at least one target edge.

### D has one target edge

Then m(D)=2 and defect<=2 forces

`kappa(D)=0`, `e_F(S,D)=0`.

Thus the non-missing cross allowance of D is zero. Any distinct support E cannot properly overlap D and, if disjoint, row closure gives zero target D--E edges.

But D contains internal target-nonedges. Since alpha(H[U])<=2, every vertex of E must meet the endpoints of those nonedges; at least three D--E target edges are required. Contradiction.

### D has two target edges

Then m(D)=1 and the non-missing allowance is at most1. Again a disjoint support requires at least three D--E target edges to cover the unique internal target nonedge, while proper overlap costs2 and is impossible for a repeated support of remaining allowance at most1. Thus no distinct support can exist, contradicting the three owner incidences outside the multiplicity-four class.

### D is a target K3

Then e_H(D)=3, and (2) already gives `12+3>14`.

Therefore

> multiplicity4 is impossible.                              (3)

## 4. Multiplicity-three nonclique supports

Let D have multiplicity3. D14 gives

`9 + O_D + e_F(F,D) + e_H(D) <=14`,

or

`O_D + e_F(F,D) + e_H(D) <=5`.                            (4)

### Two-edge D is impossible

If e_H(D)=2, then m(D)=1 and repeated defect<=2 gives non-missing cross allowance at most1.

A disjoint support requires at least3 D--E target edges to cover the unique internal nonedge, impossible. Proper overlap with D costs2; if it occurred it would use the full defect budget, but then the D14 inequality still forces at most3 intersecting owner incidences, whereas four owner incidences remain outside the multiplicity-three class. More directly, if no disjoint support exists then all four remaining owner incidences meet D, so `O_D>=4`, while (4) with e_H(D)=2 gives `O_D<=3`. Contradiction.

Hence no two-edge multiplicity-three support exists.                       (5)

### One-edge D is an exact equality state

If e_H(D)=1, then m(D)=2. Repeated defect<=2 forces

`kappa(D)=0`, `e_F(S,D)=0`,

so D has zero non-missing cross allowance.

Thus no distinct support may be disjoint from D: row closure would give zero D--E target edges, whereas an internal target-nonedge of D and alpha(H[U])<=2 require at least3 cross edges.

All four remaining owner incidences therefore meet D, so `O_D>=4`. Equation (4) gives `O_D<=4`. Hence equality is forced:

> `O_D=4`, `e_F(F,D)=0`, `e_H(D)=1`, `kappa(D)=0`, `e_F(x,D)=0`.  (6)

The D-repivot has defect2 and therefore q=35. All four remaining owner supports meet D. This is an exact secondary-shell equality terminal.

## 5. Multiplicity-three target K3 geometry

Assume D is a target K3. Equation (4) becomes

`O_D + e_F(F,D) <=2`.                                      (7)

Thus at most two of the four remaining owner incidences can come from supports intersecting D. Therefore at least two owner incidences lie in supports disjoint from D.                 (8)

For a disjoint support E, if E were nonclique then any internal target nonedge of E must be covered from every vertex of the K3 D because alpha(H[U])<=2. This requires at least3 D--E target edges.

But the repeated K3 D has non-missing cross allowance at most2, so common-S row closure gives `e_H(D,E)<=2`. Contradiction.

Therefore:

> every support disjoint from a multiplicity-three K3 D is itself a target K3.    (9)

Hence the only multiplicity-three K3 residual is:

- D is a target K3 of multiplicity3;
- `O_D+e_F(F,D)<=2`;
- at least two external owner incidences belong to disjoint target-K3 supports.

## 6. Interface

The c=8, n2=1, A=3 layer now has support multiplicity at most3. Every multiplicity-three support lies in exactly one of two geometries:

1. **one-edge q35 equality terminal**:
   `O_D=4`, `e_H(D)=1`, zero core/far/x excess, all four remaining owners intersect D;
2. **repeated K3/disjoint-K3 terminal**:
   `O_D+e_F(F,D)<=2`, with at least two external owner incidences carried by supports disjoint from D, and every such disjoint support is a K3.

The next task is to apply q35 secondary-shell dynamics and support-incidence capacity to these two exact terminals.