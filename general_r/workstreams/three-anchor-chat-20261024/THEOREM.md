# Theorem ledger

## Main target — Exact Three-Anchor Excess Theorem

Let `r>=12` and let `H` be a graph on `3r-1` vertices with `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`. If `H` contains three pairwise nonadjacent vertices of degree exactly `r`, prove

`K_r(H)=2e(H)-r(3r-1)>=8`.

Status: **PROVED_SYMBOLIC for every `r>=17`; OPEN only for `r=13,14,15,16` in the two `c=4` geometries, with `r=12` already closed by the historical fixed-r proof.**

## Theorem 0 — parity collapse

**CLAIM.** `K_r(H)` is always even.

**STATUS.** `PROVED_SYMBOLIC`.

`2e(H)` is even, and `r(3r-1)` is even (if `r` is odd then `3r-1` is even). Hence a putative counterexample with `K_r<=7` automatically has

`K_r<=6`.

## Theorem A — complement/AES closure

**CLAIM.** The main target holds for every `r>=60`.

**STATUS.** `PROVED_ANALYTIC` (classical Andrasfai–Erdos–Sos theorem).

For `J=bar H`, `J` is `K4`-free, `alpha(J)<=r-1`, and `d_J(v)=2r-2-(d_H(v)-r)`. Under `K<=6`, `delta(J)>=2r-8`. Since `2r-8>5(3r-1)/8` for `r>=60`, AES makes `J` 3-partite, forcing an independent part of size at least `r`, contradiction.

This route is now superseded quantitatively by Theorem D but remains a useful independent check.

## Theorem B — c=2 closure

**CLAIM.** The `c=2`, `t=2`, `(r-2,r-2,r-2)` geometry is impossible for every `r>=12`.

**STATUS.** `PROVED_SYMBOLIC`.

The proof uses a parameter-free degree-2 tripartite transversal-cover lemma. See `PROOF_ATTEMPTS.md`.

## Theorem C — c=3 closure

**CLAIM.** The `c=3`, `t=1`, `(r-2,r-2,r-3)` geometry is impossible for every `r>=13`.

**STATUS.** `PROVED_SYMBOLIC`.

The proof uses pair-connector nonneighbour rectangles, focus on `X3`, parity, and a single `r=13,K=6` equality elimination by the triple connector. See `PROOF_ATTEMPTS.md`.

## Theorem D — complete all-pattern closure for r>=17

**CLAIM.** The Exact Three-Anchor Excess Theorem holds for every `r>=17`.

**STATUS.** `PROVED_SYMBOLIC`.

Only `c=4` remains after Theorems B/C. There are two deficit geometries.

### D1. Deficits `(0,0,2)`
All four connectors are pair connectors, two missing `a1` and two missing `a2`; every connector is incident to `a3`. Let a connector be **focused** if it is complete to `X3` (`|X3|=r-4`).

If a connector is not focused, its nonneighbour rectangle lies between an incident zero-deficit block (external baseline 2) and `X3` (baseline 4). With connector excess `k` and connector-degree `gamma`, the rectangle charge gives

`k + charge >= r-10+gamma`.

For `r>=17` this is at least seven, impossible under `K<=6`. Hence all four connectors are focused.

For two focused connectors `p,q`, if `pq` were a nonedge, their common nonneighbour set would be a clique (otherwise two common nonneighbours together with `p,q` form an independent 4-set). They share at least `X3 union {a3}`, of size `r-3`, as common neighbours, so

`|M(p,q)| >= 2r-6-k_p-k_q >= 2r-12 > r-1`,

contradicting `omega(H)<=r-1`. Thus every pair of focused connectors is adjacent. In particular three of them form a triangle, and together with `X3 union {a3}` they form an `r`-clique, contradiction.

### D2. Deficits `(0,1,1)`
Here `|X1|=r-2`, `|X2|=|X3|=r-3`. The connector types are: two missing `a1`, one missing `a2`, one missing `a3`.

A connector missing `a2` or `a3` cannot be complete to the zero-deficit incident block `X1`; if it is complete to neither incident block, its `(2,3)` rectangle costs at least `r-8+gamma>=9` for `r>=17`. Hence these two connectors are forced to focus on `X3` and `X2`, respectively.

Each connector missing `a1` has incident baselines `(3,3)`. If it is complete to neither `X2` nor `X3`, its rectangle costs at least `r-10+gamma>=7`, impossible. Hence all four connectors focus on `X2` or `X3`.

But no two connectors can focus on the same deficit-1 block. If two such connectors are adjacent, that block together with its anchor and the two connectors is an `r`-clique. If they are nonadjacent, their common nonneighbour set is a clique; because they share the focused block plus its anchor (size `r-2`) as common neighbours,

`|M| >= 2r-5-k_p-k_q >= 2r-11 > r-1`,

again impossible. Thus at most one connector can focus on each of `X2,X3`, contradicting four connectors and only two focus blocks.

Therefore both `c=4` geometries are impossible for `r>=17`, completing the theorem in that range.

## Remaining exact gap

For the general-r theorem itself, the only unresolved symbolic parameter values are

`r in {13,14,15,16}`

inside the two `c=4` geometries `(0,0,2)` and `(0,1,1)`. The historical repository already contains the independent `r=12` closure.
