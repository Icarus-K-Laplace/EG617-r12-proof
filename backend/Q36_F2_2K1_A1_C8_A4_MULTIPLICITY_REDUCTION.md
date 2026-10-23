# q36 f=2, 2K1 far, a_F=1 — c=8, allowance four multiplicity reduction

Status: `PROVED REDUCTION` under `Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md`, common-S row closure, inherited D14, lexicographic q36 maximality, and `alpha(H[R])<=2`.

For c=8,A=4 the high-c identity forces

- `nu_Y=0`;
- Y is a target K2;
- `G_Y=2`, so both inactive decorations are exactly1.

This note proves multiplicity4 impossible and shows that any multiplicity-three support must be a target K3 with weighted overlap plus Y-incidence at most2.

## 1. Repeated supports have defect at most three

A repeated support with full defect4 would repivot to q36. The repivot removes x0, retains both decorated vertices Y, and inserts three globally decorated support vertices. The new tau would be at least5, exceeding the old tau3. Therefore every repeated support has defect at most3 and repivots to q<=35.

## 2. Multiplicity four is impossible

Let D have multiplicity4. The K11/D14 support cap is

`12 + O_D + e_F(Y,D)+e_H(D)<=14`,

hence

`O_D+e_F(Y,D)+e_H(D)<=2`.                                 (1)

Since `alpha(H[R])<=2`, `e_H(D)>=1`.

If another support E were disjoint from D:

- when `e_H(D)=1`, the repeated-support defect bound gives common-S cross allowance at most1, but each vertex of E must meet the target-nonedge graph of D; this requires at least3 D--E target edges;
- when `e_H(D)=2`, the cross allowance is at most2, while the unique target nonedge again requires at least3 cross edges;
- `e_H(D)=3` is already impossible in (1).

Thus no support is disjoint from D. Four owner incidences remain outside the multiplicity-four class, so `O_D>=4`, contradicting (1).

Therefore multiplicity4 is impossible.

## 3. Multiplicity-three nonclique supports are impossible

Let D have multiplicity3. D14 gives

`O_D+e_F(Y,D)+e_H(D)<=5`.                                 (2)

### One-edge D

Here `m(D)=2`, so defect<=3 gives common-S cross allowance at most1. A disjoint support would require at least3 D--E target edges to cover the two internal nonedges of D, impossible. Hence all five remaining owner incidences intersect D and `O_D>=5`.

Equation (2) would then force `O_D=5`, `e_F(Y,D)=0`, `e_H(D)=1`.

But the global decoration of D is at least

`lambda(D)-3 = (3*3+5)-3 =11`,

with any core/x0/Y contribution only increasing it. Repivoting a D-owner retains `G_Y=2`, so the new shell has `G'>=13`.

The support defect is at least2, hence q' is either34 or35. Every shell has at least22 missing edges, so `G'<=q'-22<=13`. Equality would require q'=35 and no additional decoration beyond the 11 owner units. But q'=35 means defect3, requiring one additional unit of `kappa(D)+e_F(x0,D)` beyond the internal missing count2, which would increase `G'` to at least14. Contradiction.

Thus the one-edge multiplicity-three state is impossible.

### Two-edge D

Here `m(D)=1`, so the cross allowance is at most2. A disjoint support again requires at least3 cross edges to cover the unique internal nonedge, impossible. Hence `O_D>=5`, while (2) gives `O_D<=3`. Contradiction.

Therefore no nonclique multiplicity-three support exists.

## 4. Only a repeated target K3 can remain

If D is a target K3, (2) reduces to

> `O_D+e_F(Y,D)<=2`.                                       (3)

Thus at least three of the five remaining owner incidences are carried by supports disjoint from D.

No closure of this repeated-K3 equality sector is claimed here. It is the only multiplicity-three geometry surviving the current c=8,A=4 analysis.

## 5. Interface

The c=8,A=4 branch now satisfies:

- support multiplicity at most3;
- every multiplicity-three support is a target K3;
- for such a support, `O_D+e_F(Y,D)<=2`, so most remaining owner incidences lie in disjoint supports.

The next task is to rule out this repeated-K3/disjoint-support geometry or reduce it to a finite secondary shell.