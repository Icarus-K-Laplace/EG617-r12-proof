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
4. A shortest-odd-cycle argument forces a `C5`; the remaining `2r-6` vertices are exactly a near-complete bipartite graph with total defect at most one.
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

Alpha equality is now automatic from the canonical budget. Branch-A irreducibility is exactly equivalent to the independent-5 hypergraph resisting every r-vertex transversal. Minimum degree follows because a degree at most `r-1` vertex leaves at least `4r+1` nonneighbors with alpha at most 4.

### Dependency

Residual branch closure + alpha-saturation theorem.

### Independent of r?

Symbolic; terminal use currently paired with `r>=17` residual closure.

### External theorem?

None beyond dependencies.

### Minimal failure point

Whether the terminal exists remains open.

### GitHub commits

- initial terminal: `4d2feba3cf8c52f9099fe14b7953eb637148df46`
- alpha-equality strengthening: `fc774dd80d94c1abc508c285f435d5a5eedfbea2`

---

## 2026-10-24 — Round 5: scalar recurrence replacement

### NEW THEOREM / LEMMA

**Exact multicolour slack potential + critical-core potential.**

### Hypotheses

Canonical state `R_a` on `ar+1` vertices inside the full balanced r-colouring.

### Exact conclusions

1. If `x_0` is the target-colour excess above `p_a` and `x_i` the other colours' excess above `p_r`, then

   `x_0 + sum x_i = S_a(r)=[a(a-1)r+2a-2r]/2`.

2. `S_a-S_{a-1}=(a-1)r+1`.
3. Every canonical state has exact `alpha(R_a)=a`.
4. Every canonical state contains an induced `(r+1)`-critical core.
5. At a `K_r`-free stop, its critical-core order is at least `3r-1` for `r>=4`.
6. Writing the critical-core order as `lr+t`, `0<=t<r`, compatibility with the hereditary cap and Kostochka--Yancey is exactly one quadratic inequality `P_{l,t}(r)<=0`.

### Proof sketch

The slack identity is exact edge partitioning across all r colours after subtracting their individual Turan minima. Alpha saturation follows because `p_{a-1}(ar+1)` already exceeds the canonical edge budget. Critical-core order is obtained by colliding Dirac/Kostochka--Yancey lower bounds with the hereditary least-color upper cap.

### Dependency

- internal: canonical ray + full balanced-colouring alpha constraints;
- external: Dirac critical-graph bound and Kostochka--Yancey 2014.

### Independent of r?

The identities are fully symbolic; the sharpened `|Q|>=3r-1` holds for `r>=4`.

### Minimal remaining counterconfiguration

A first `K_r`-free stop with `a>=6` satisfying simultaneously exact alpha saturation, the `S_a` ledger, the hereditary cap, and a critical-core residue passing `P_{l,t}(r)<=0`.

### GitHub commit

`76f65dca0f1bf755a93b2a25331a238bd73383b2`

---

## 2026-10-24 — Round 6: high-stop concentration + exact predecessor interface

### NEW THEOREM / LEMMA A — Simultaneous excess concentration

### Hypotheses

First `K_r`-free canonical stop `R_a`, `a>=6`, `r>=a+1`, with exact ledger `sum_i x_i=S_a(r)`.

### Exact conclusion

At least `floor(r/2)` non-target colors satisfy

`x_i<=C_{a,r}:=ceil(2S_a(r)/(r-1))<=a^2-1`.

For each such color, its complement is `K_{r+1}`-free and exactly `x_i` edges below the Turán maximum. For `a=6,r>=41`, at least `floor(r/2)` colors have `x_i<=29`.

### Proof sketch

Markov counting: if more than half of the `r-1` non-target excesses exceeded `C_{a,r}`, their sum would exceed `S_a(r)`. The bound `C_{a,r}<=a^2-1` follows from `r>=a+1`.

### Dependency / range

Purely symbolic, uniform for all canonical `a<=r-1`; no external theorem.

### Status

`PROVED_SYMBOLIC`. This is edge-count near-extremality only; it does not yet give an edit-distance partition theorem.

### NEW THEOREM / LEMMA B — Critical-core residue windows

### Hypotheses

Critical core order `q=lr+t`, `0<=t<r`, with `P_{l,t}(r)<=0` and `l>=2`.

### Exact conclusion

For `r>=R_l=l(l-1)^2(l-2)+2l+2`, feasibility forces

`t<=l^2-3l+1` or `r-t<=l^2-l-1`.

For `a=6,r>=614`, the only possible core-order windows are

`[3r-1,3r+1]`, `[4r-5,4r+5]`, `[5r-11,5r+11]`, `[6r-19,6r+1]`.

### Proof sketch

Rewrite `P/r` as a concave quadratic in `t`, and also in `u=r-t`. At the first integer outside each proposed boundary window and at the midpoint, the corresponding quadratic is positive for `r>=R_l`; concavity excludes the entire middle interval.

### Dependency / range

Symbolic algebra plus the already-approved Kostochka--Yancey compatibility inequality. Uniform for each fixed `l` once `r>=R_l`; not uniform for unbounded `a` without further work.

### Status

`PROVED_ANALYTIC` as a necessary-condition reduction. It kills all middle residues, but does not eliminate the surviving windows or close `a=6`.

### NEW THEOREM / LEMMA C — First-stop predecessor interface

### Hypotheses

`R_a` is the first `K_r`-free state, and `B=K_r` is the target clique removed from predecessor `R_{a+1}`.

### Exact conclusion

For each outside vertex `v`, the `r` edges `vB` either contain one target edge and every non-target color exactly once, or contain no target edge and exactly one duplicated non-target color. If `q_0` is the target cross-edge count and `z_i` counts duplicated color `i`, then

`sum_i z_i=ar+1-q_0`,

`x_0(R_{a+1})=x_0(R_a)+q_0`,

`x_i(R_{a+1})=x_i(R_a)+z_i`.

### Proof sketch

Every `r+1`-vertex set `B union {v}` must contain every color; `B` already supplies the target color. Counting the remaining `r` cross-edges yields the two alternatives and the excess increment identities.

### Dependency / range

Exact balanced-coloring property only; all r.

### Status

`PROVED_SYMBOLIC`. The lemma is a new input for the clique-transversal route, but no induced `R_{a-1}` theorem follows yet.

### Minimal remaining counterconfiguration

A first high stop satisfying the excess ledger, simultaneous near-Turán edge counts, one of the surviving critical-core windows, and the predecessor near-permutation interface.

### GitHub commit

`365f6b4e98fc49cd5586eef97afde2d52c0e8e35`

---

## Current single blocker

Status: **`OPEN`**.

**NO-HIGH-STOP LEMMA:** a canonical greedy process cannot first become `K_r`-free at `a>=6` for all sufficiently large `r`.

Round 6 did not close this theorem. Specifically, `a=6` is still open; no high-a induction trim is proved; uniform Turán edit stability and a design-trimming implication are open.

If this is closed, the requested front-end dichotomy is proved for all `r>=17` (or whatever final threshold the lemma requires).

Latest state / proposal commits:

- `CANONICAL_STATE.md`: `ea5f2a8d104239cf4d65a1b52d27960170db2bea`
- `OPEN_GAPS.md`: `defa92989e533889406398ac7b67442a89ff75a1`
- `NO_HIGH_STOP_ROUND2_LEMMAS.md`: `365f6b4e98fc49cd5586eef97afde2d52c0e8e35`.