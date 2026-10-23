# High backend V6 canonical audit — E334–E337

Status: `PROVED_RELATIVE_TO_RETAINED_BACKEND_CONTRACT` for the capacity theorems below. Full `E334..E337` remain `OPEN`.

This file records an independent replay of the uploaded `HIGH_LAYER_BACKEND_V6.zip` on 2026-10-23.

## 1. Reproducibility audit

The package verifier was rerun with

`python verify_v6.py`

and reported:

- PASS: all 18 actual E334–E337 core channels;
- PASS: near-cover thresholds and all 15 matching-obstruction parameter pairs;
- PASS: parent codegree constants;
- PASS: the old scalar three-edge interval is preserved.

The SHA-256 values in `MANIFEST.json` were independently recomputed for all ten listed files. Every digest matched exactly, including the retained V5 dependency archive.

The verifier certifies arithmetic and finite parameter tables only; the structural lemmas are written analytic proofs. No necessary integer state is treated as a realized graph.

## 2. Core212/core213 matching residual theorem

Let `H` be a 35-point backend core satisfying the retained contract:

- `alpha(H)<=3`, `omega(H)<=11`;
- `delta(H)>=12`;
- every 13-set has at most67 target edges;
- total excess `K=sum(d_H-12)<=6`.

Suppose `U=P union Q` induces two `K_m` blocks joined by exactly a perfect matching, with `7<=m<=11`.

Then this configuration is impossible.

The proof has two load-bearing ingredients.

### Nonadjacent-pair codegree bound

For nonadjacent `u,v`, their common non-neighbours form a clique; otherwise `alpha(H)>=4`. The clique cap gives

`|N(u) intersect N(v)| <= 2+kappa_u+kappa_v`.

### Intersecting K11 rigidity

Two distinct 11-cliques cannot overlap in at least six vertices under `K<=6` and the inherited 13-set cap. If each clique has at least two exclusive vertices, one clique plus two vertices of the other gives at least68 edges on13 vertices. The remaining overlap-10 case forces the two exclusive vertices to be nonadjacent with codegree at least10, while the preceding bound allows at most `2+K<=8`.

Hence the residual 11-cliques forced by the matching system must coincide. Two missing-edge witnesses then require

`K >= 2m-6`.

For `m>=7`, this exceeds the available excess in the relevant matching cases after the exact witness bookkeeping. This closes the former core212 three-edge scalar gap and extends the obstruction through core213 (`K=6`).

## 3. Uniform repeated-pair capacity through core213

For a repeated two-point missing set with

- `r=1`;
- row allowance at most2;
- `K in {2,4,6}`;

one has

> `m<=6`.

If `m>=7`, the V6 near-cover theorem gives an outside zero-charge vertex and forces `alpha(H[U])<=2`. Matching rigidity then forces the two-clique-plus-perfect-matching structure, which is excluded by the theorem above.

This simultaneously covers cores with211,212 and213 edges whenever such a repeated family is actually forced.

Sharper retained bounds include:

- `r=1`, allowance<=1, `K in {2,4,6}` => `m<=4`;
- `r=2`, allowance<=1, `alpha(H[U])<=2` => `m<=5`;
- under the old zero-hub condition with `K<=2`, the last bound sharpens to4;
- one-contributing-hub, allowance<=2, `K<=4`, `W<=31` => `m<=5`.

These are capacity upper bounds, not existence claims at equality.

## 4. E334 forcing progress and exact boundary

The short-row / no-far branch at `q<=32` has exactly two active hubs. The one-hub branch and three-hub branch are analytically impossible.

The new capacity theorem removes the large `r=1`, allowance<=2 obstruction uniformly across the actual E334 core channels 211/212/213.

What remains is explicitly outside this theorem:

1. far-neighbour configurations;
2. missing-degree-three rows;
3. double-hub branches with `r>=2`;
4. the `r=1`, allowance-three boundary.

The allowance-three boundary has only three necessary hub-weight geometries, but they are not asserted to be realizations.

Therefore `E334` is still OPEN, and nothing in V6 automatically closes `E335..E337`.

## 5. Higher-layer boundary

For E335–E337 the exact channels with core excess `K<=6` inherit the `m<=6` repeated-pair capacity. Channels with `K>=8` do not: the near-cover concentration theorem no longer guarantees an outside zero, and overlap-10 K11 exchange can consume the entire excess budget at `K=8`.

The next Astra-B tasks therefore remain a genuine maximal-pivot forcing theorem and the `K>=8` concentration / overlapping-K11 equality mechanism.

## Certification boundary

This audit retains all upstream backend contracts, including the all-pivot core minimum-degree theorem and hereditary density caps. It does not recertify those upstream inputs and does not mark `E334..E337` closed.