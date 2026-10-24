# R12 -> general-r dependency map

Workstream: `general-r-residual-core-extraction-20261024`

Status: `PROVED_SYMBOLIC` for algebraic provenance statements; `SOURCE_REPORTED` where the entry records an audited r=12 theorem/certificate rather than a new all-r proof.

## Purpose

This map separates the r=12 front end into genuinely symbolic ingredients and fixed-r inputs. It is deliberately upstream of the backend d2/d3/support machinery.

## Constant provenance

| r=12 quantity | general-r expression | class | provenance / verdict |
|---|---:|---|---|
| 145 | `r^2+1` | A | Problem order; genuinely symbolic. |
| 870 | `r(r^2+1)/2` | A | Least-color averaging budget; genuinely symbolic. |
| 12 | `r` | A/F | Size of a monochromatic clique block `K_r`; cross edges between two target-color `K_r` blocks are matchings because a vertex cannot hit two vertices of another block. |
| 49 | `4r+1` | A/F | Not an arithmetic accident. If a degree-`(r-1)` anchor is followed by `r-5` extracted `K_r` blocks, residual order is `r^2-(r-1)-(r-5)r=4r+1`; the independence cap drops to 4. In r=12 this is also the eight-`K_12` residual. |
| 61 | `5r+1` | A/D | On the same critical anchor ray, one block earlier (`r-6` blocks) gives `5r+1` and independence cap 5. In r=12 this is the unique surviving outer recurrence stop `(d,j,a,n)=(11,6,5,61)`. Its *formula* is symbolic; its *uniqueness as the only stop* is fixed-r recurrence data. |
| 13 | `r+1` | A/B/F | Desired residual pivot degree. The order identity is symbolic, but forcing such a pivot/minimum degree is not yet general. For r=12, `delta(F)>=13` uses lower-order Ramsey exclusions. |
| 35 | `3r-1` | A | If `|F|=4r+1` and `d_F(p)=r+1`, then `|F-N[p]|=3r-1`. Pure algebra. |
| 284/308/310 | no established all-r exact analog | B/C | r=12 edge floors on 47/48 vertices use exact lower-order seeds, recurrence, and/or local repivot machinery. Do not parameterize merely because the numbers fit a polynomial. |
| 397--408 on 61 vertices | candidate symbolic budget at top: `3r^2-2r` | D/F | The r=12 top budget 408 equals `3r^2-2r`; the lower floor 397 is recurrence-specific. |
| CORE211 | `[r(3r-1)+2]/2` for `r>=12`, conditional on residual-core contract | E/F | Already proved in the general-r line by AES once `delta(H)>=r`, `alpha(H)<=3`, `omega(H)<=r-1` are supplied. |

## Classification A--F

### A. Purely symbolic in r

1. Least-color graph `G` on `r^2+1`:
   - `alpha(G)<=r`, `omega(G)<=r`;
   - `e(G)<=r(r^2+1)/2`.
2. Hereditary cap:
   `D_r(n)=C(n,2)-(r-1)p_r(n)`.
3. Anchor/block residual:
   for an anchor of degree `d` and `j` extracted `K_r` blocks,
   `n=r^2-d-jr`, `alpha<=r-1-j`.
4. If `d=r-1`, then `j=r-5` gives `(n,alpha-cap)=(4r+1,4)` and `j=r-6` gives `(5r+1,5)`.
5. A degree-`(r+1)` pivot in a `4r+1` residual leaves a `3r-1` core.

### B. Exact Ramsey / lower-order seeds

The r=12 recurrence and residual minimum-degree proof use:

- emptiness thresholds corresponding to `R(2,24)`, `R(3,37)`, contextual `R(4,49)`;
- edge seeds `(2,23)->131`, `(3,35)->210`, `(3,36)->234`, `(4,47)->284`, `(4,48)->308`;
- later refinements such as the 48-vertex floor 310.

These are not presently all-r theorems. In particular, the r=12 proof of `delta(F)>=13` is seed-dependent.

### C. Small-r arithmetic coincidence

The individual q-values, shell charges, and exact 47/48-edge layers in E401--E406 are fixed-r data unless independently rederived symbolically. The current workstream does not promote them.

### D. Recurrence cutoff

The 1752-node / 144-outer-comparison certificate proves only the fixed-r arithmetic recurrence. Its unique surviving outer stop is `(11,6,5,61)`.

The important general lesson is not the node count but the outer invariant proved in `OUTER_RAY_INVARIANT.md`: extraction moves preserve `n-r a=r-d`.

### E. Extremal stability

The post-extraction core floor via Andrasfai--Erdos--Sos is genuinely uniform once the residual-core contract is available. The present workstream also uses triangle-free stability/exact extremal input only after stating hypotheses explicitly.

### F. Genuinely structural inequalities

The following survive parameterization cleanly:

- cross-matching between target-color `K_r` blocks;
- minimum-degree pivot identity
  `e(J)=C(h+1,2)+q+e(C)`, `q>=0`;
- hereditary cap `D_r`;
- complement-neighborhood clique-number drops (`alpha<=k` gives `alpha` one smaller in the non-neighborhood of a vertex);
- the new `2r` exclusion and near-Mantel boundary compression in `CORE_MINDEG_BOUNDARY_THEOREM.md`.

## Dependency conclusion

`4r+1`, `5r+1`, and `3r-1` are genuinely structural orders. What does **not** automatically generalize is the r=12 forcing chain that reaches them with the needed minimum degrees. The precise current load-bearing gap is now narrower than before:

> under the inherited core cap, `alpha(H)<=3`, `omega(H)<=r-1` already force `delta(H)>=r-1` for `r>=6`; only the exact boundary `d_H(v)=r-1` remains to be eliminated or classified.

See `CORE_MINDEG_BOUNDARY_THEOREM.md`.