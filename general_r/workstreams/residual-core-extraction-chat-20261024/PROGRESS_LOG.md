# Progress log

## 2026-10-24 — Round 1: r=12 reverse engineering -> Level A core theorem

### NEW THEOREM / LEMMA

**General residual-core minimum-degree theorem.**

### Hypotheses

For `r>=17`, `H` has `3r-1` vertices, `alpha(H)<=3`, `omega(H)<=r-1`, and inherits the least-color hereditary cap on every induced subgraph.

### Exact conclusion

`delta(H)>=r`.

### Proof sketch

1. A `2r` induced obstruction with alpha at most 2 is impossible by exact cap + triangle-free complement + AES.
2. Hence `delta(H)>=r-1`.
3. If `d(v)=r-1`, the complement on the `2r-1` nonneighbors is non-bipartite triangle-free with exactly `(r-1)^2` or `(r-1)^2+1` edges.
4. A shortest odd-cycle argument forces a `C5`; the remaining `2r-6` vertices are exactly a near-complete bipartite graph with total defect at most one.
5. Full hereditary cap on `C5 + one bipartition side + b` forces every row defect from the neighbor set `B=N_H(v)` into the nonneighbor set to be at most 8.
6. Any complement edge inside `B` needs two row defects summing to at least `r`; `omega(H)<=r-1` forces such a complement edge.
7. Contradiction for `r>=17`.

### Dependency

External: Andrasfai--Erdos--Sos; Erdos non-bipartite triangle-free edge bound.

Internal: hereditary least-color cap only. No backend.

### Independent of r?

Symbolic proof; threshold `r>=17` is explicit.

### Minimal remaining counterconfiguration if threshold not met

For `6<=r<=16`, only the exact degree-`r-1` near-Mantel/C5 boundary remains; no claim of existence.

### GitHub commits

- dependency map: `548ba50884d7d67ba1731b5e3d792aea0ad109fb`
- first boundary compression: `b92a7ee777b18dd78e24c340f87236d61998d136`
- upgraded full `delta(H)>=r` theorem: `9728aa35d3c7de6404cf86758435ba023d8b27c1`

---

## 2026-10-24 — Round 2: close the entire 4r+1 residual branch

### NEW THEOREM / LEMMA

**Residual branch closure theorem.**

### Hypotheses

For `r>=17`, `F` has `4r+1` vertices, `alpha(F)<=4`, `omega(F)<=r-1`, and inherits the hereditary cap.

### Exact conclusion

- `delta(F)=r+1`;
- there is a degree-`(r+1)` pivot `p`;
- `H=F-N[p]` has

  `|H|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`.

### Proof sketch

The core theorem implies a `3r` exclusion. A vertex of degree at most `r` in `F` would leave a `3r` induced nonneighbor subset with alpha at most 3, contradiction. Thus `delta(F)>=r+1`. The exact cap `D_r(4r+1)=2r^2+4r+4` rules out `delta(F)>=r+2`, so equality and a legal pivot follow.

### Dependency

`CORE_MINDEG_BOUNDARY_THEOREM.md` + AES for the derived `3r` exclusion.

### Independent of r?

Uniform symbolic/analytic proof for all `r>=17`.

### External theorem?

AES, via the core theorem and `3r` exclusion.

### Minimal failure point

No failure inside Branch A for `r>=17`; the only missing source is extraction of `F` itself.

### GitHub commit

`9740d0c798ea1374a5825c798bc808954f429ffc`

---

## 2026-10-24 — Round 3: eliminate anchor-defect rays

### NEW THEOREM / LEMMA

**Affine outer-ray invariant + induced trimming normalization.**

### Hypotheses

Minimum-degree anchor `d=r-s`, canonical block extraction, inherited edge budget.

### Exact conclusion

After `j` blocks, with `a=r-1-j`, the raw state has

`n=ar+s`.

For every `s>=1`, an induced `ar+1` subgraph exists with edge budget no larger than the critical `s=1` budget.

Thus all anchor defects normalize to one critical ray.

### Proof sketch

- exact algebra gives `n-ra=s`;
- averaging over induced `(ar+1)`-subsets and a factored polynomial inequality gives budget preservation.

### Dependency

Only the minimum-degree pivot identity and block edge count.

### Independent of r?

Yes.

### External theorem?

Brooks is used separately to guarantee an anchor with `d<=r-1`.

### Minimal failure point

None for normalization. The remaining issue is where greedy `K_r` extraction first stops.

### GitHub commits

- ray invariant: `7d36261a29192bd60b92d728a127ae6125d8d224`
- canonical normalization/extraction: `07cd8fb58ffd93d234b1e8b6104f939175d7fbda`

---

## 2026-10-24 — Round 4: exact 5r+1 terminal

### NEW THEOREM / LEMMA

**Irreducible 5r+1 terminal contract.**

### Hypotheses

The canonical greedy process first becomes `K_r`-free at `a=5`, and no `4r+1` Branch-A induced subgraph is already present.

### Exact conclusion

`T_r` satisfies

- order `5r+1`;
- `alpha=5`, `omega<=r-1`;
- hereditary cap;
- `e<=3r^2-2r`;
- no `K_r`;
- `delta>=r`;
- the hypergraph of independent 5-sets has transversal number at least `r+1`;
- every degree-r row has an explicit independent-4 witness property.

### Proof sketch

Branch-A irreducibility is exactly equivalent to the independent-5 hypergraph resisting every r-vertex transversal. Minimum degree follows because a degree at most `r-1` vertex leaves at least `4r+1` nonneighbors with alpha at most 4.

### Dependency

Residual branch closure.

### Independent of r?

Symbolic; terminal use currently paired with `r>=17` residual closure.

### External theorem?

None beyond dependencies.

### Minimal failure point

Whether the terminal exists remains open.

### GitHub commit

`4d2feba3cf8c52f9099fe14b7953eb637148df46`

---

## Current single blocker

Status: `OPEN`.

**NO-HIGH-STOP LEMMA:** a canonical greedy process cannot first become `K_r`-free at `a>=6` for all sufficiently large `r`.

If this is closed, the requested front-end dichotomy is proved for all `r>=17` (or whatever final threshold the lemma requires).

State commits:

- `CANONICAL_STATE.md`: `052d23b35f50515947ce9d7152073788a9f3f61a`
- `OPEN_GAPS.md`: `43bdac3389de02bb8b4d0c83fdacd279e7718364`.