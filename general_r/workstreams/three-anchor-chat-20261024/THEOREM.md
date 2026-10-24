# Theorem ledger

## Main target — Exact Three-Anchor Excess Theorem

Let `r>=12` and let `H` be a graph on `3r-1` vertices with `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`. If `H` contains three pairwise nonadjacent vertices of degree exactly `r`, prove

`K_r(H)=2e(H)-r(3r-1)>=8`.

Status: **OPEN in full generality**. The `c=2` branch is closed for all `r>=12`; the `c=3` branch is closed for all `r>=13`; only the two `c=4` symbolic geometries remain for the general-r theorem (plus the already-existing historical r=12 closure).

## Theorem 0 — parity collapse

**CLAIM.** `K_r(H)` is always even.

**STATUS.** `PROVED_SYMBOLIC`.

Indeed `2e(H)` is even. Also `r(3r-1)` is even: if `r` is even this is immediate, while if `r` is odd then `3r-1` is even. Hence `K_r=2e-r(3r-1)` is even.

Therefore a putative counterexample with `K_r<=7` automatically satisfies

`K_r<=6`.

This one-line observation is now used throughout the workstream.

## Theorem A — sufficiently-large-r closure

**CLAIM.** The main target holds for every `r>=60`.

**STATUS.** `PROVED_ANALYTIC` (using the classical Andrasfai–Erdos–Sos theorem).

Let `J=bar H`. Then `J` is `K4`-free, `alpha(J)=omega(H)<=r-1`, and

`d_J(v)=2r-2-(d_H(v)-r)`.

If `K_r(H)<=7`, parity gives `K_r<=6`, so every H-excess is at most 6 and `delta(J)>=2r-8`. For `n=3r-1`,

`2r-8 > 5n/8`

exactly when `r>=60`. AES forces a `K4`-free graph above this threshold to be 3-partite. One part then has size at least `ceil((3r-1)/3)=r`, contradicting `alpha(J)<=r-1`.

## Theorem B — balanced two-triple-connector pattern is impossible

**CLAIM.** Under the main contract and `K_r(H)<=7`, the symbolic pattern

`c=2`, `t=2`, `(|X1|,|X2|,|X3|)=(r-2,r-2,r-2)`

is impossible for every `r>=12`.

**STATUS.** `PROVED_SYMBOLIC`.

This is the entire `c=2` branch, not a fixed-r case check. The proof uses the tripartite degree-2 transversal-cover lemma recorded in `PROOF_ATTEMPTS.md`. With the parity lemma, its previous apparent `r=12,K=7` equality layer vanishes automatically.

## Theorem C — one-triple/two-pair pattern is impossible for r>=13

**CLAIM.** Under the main contract and `K_r(H)<=7`, the symbolic pattern

`c=3`, `t=1`, `(|X1|,|X2|,|X3|)=(r-2,r-2,r-3)`

is impossible for every `r>=13`.

**STATUS.** `PROVED_SYMBOLIC`.

The connector incidence identity forces exactly one triple connector `w` and two pair connectors `u,v`, where `u` misses `a1` and `v` misses `a2`. For a pair connector that is not complete to `X3`, the nonneighbour sets in its incident zero-deficit block and in `X3` form a complete bipartite rectangle. The rectangle charges excess. Two noncomplete pair connectors already require at least `2(r-8)>=10` units for `r>=13`; two complete pair connectors force a huge common-nonneighbour rectangle between `X1,X2`; hence exactly one is complete to `X3`. The remaining mixed case is closed by a sharpened rectangle charge, with the unique `r=13,K=6` arithmetic equality killed by the triple connector `w`. Full details are in `PROOF_ATTEMPTS.md`.

Consequently every general-r counterexample for `r>=13` must lie in `c=4`, i.e. one of exactly two geometries:

- `(r-2,r-2,r-4)` / deficits `(0,0,2)`;
- `(r-2,r-3,r-3)` / deficits `(0,1,1)`.
