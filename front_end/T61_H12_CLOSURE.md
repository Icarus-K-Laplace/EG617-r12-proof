# T61 minimum-degree-12 branch closure

Status: `PROVED`.

## Theorem

No embedded T61 residual can have minimum degree 12.

Hence every T61 survivor satisfies

`delta(R)=13`.

## Proof

Assume `R` is a T61 residual with `delta(R)=12`. Take a degree-12 pivot `p`, 12-shell `A`, and 48-core `C`. Then

`E = 78 + q + e(C)`.

The shell floor gives `q>=20`. The new generic theorem `R(4,48) => e>=310` gives `e(C)>=310`. Since T61 has `E<=408`, equality is forced everywhere:

`E=408`, `q=20`, `e(C)=310`.

The q20 equality argument in the 12-shell uses only the contextual order cutoffs `R(3,37)=empty` and `R(2,24)=empty`, so it gives the same normal form:

`M = complement(R[A]) = K_{2,r} disjoint_union (10-r)K1`, `6<=r<=10`.

Its two centres have 10-vertex rows in `C`, every leaf has a 2-vertex row, every isolate has empty row, and every leaf/isolate has degree exactly 12 in `R`.

Fix a leaf `y` and write its row as `P_y={u,w}`. Repivot at `y`. The new 48-core `C_y` is again in `R(4,48)`, hence has at least 310 edges. Since

`408 = 78 + q_y + e(C_y)`

and `q_y>=20`, equality again forces

`q_y=20`, `e(C_y)=310`.

Therefore the new shell missing graph is again a q20 normal form `K_{2,r_y}` plus isolates.

Exactly as in the 309-floor rotation proof, the new shell contains the old pivot `p` and the two row vertices `u,w`. The edges `pu,pw` are missing target edges. Triangle-freeness of the q20 normal form forces `uw` to be a target edge; `p` has missing degree exactly 2, so it is a leaf and `u,w` are the two new centres.

Consequently, every other old leaf row is either equal to `P_y` or disjoint from it. Let `c` be the size of the row-class of `P_y`. Then

`r_y=11-c`.

The q20 centre-decoration formula in the new pivot gives

`d_R(u)=12+(10-r_y)=11+c`.

In the original pivot decomposition, `u` is adjacent to exactly the `c` old shell leaves in this row-class, is nonadjacent to the old pivot, and is not contained in either old centre row or any other leaf/isolate row. Hence

`d_R(u)=d_C(u)+c`.

Thus

`d_C(u)=11`,

contradicting the audited fact `delta(C)>=12` for every `C in R(4,48)`.

Therefore the T61 minimum-degree-12 branch is empty.

## Consequences

The unique front-end obstruction now has the sharper contract

- order 61;
- `alpha<=5`, `omega<=11`, inherited density caps;
- `delta=13`;
- `397<=E<=408`;
- exact outer ledger `E+sigma+g+x6+y6=408` after the proved `z=0` lemma.

The h12 cells `E407` and `E408` are completely eliminated.
