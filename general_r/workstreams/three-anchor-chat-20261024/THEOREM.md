# Theorem ledger

## Main target — Exact Three-Anchor Excess Theorem

Let `r>=12` and let `H` be a graph on `3r-1` vertices with `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`. If `H` contains three pairwise nonadjacent vertices of degree exactly `r`, prove

`K_r(H)=2e(H)-r(3r-1)>=8`.

Status: **OPEN in full generality**.

## Theorem A — sufficiently-large-r closure

**CLAIM.** The main target holds for every `r>=68`.

**STATUS.** `PROVED_ANALYTIC` (using the classical Andrasfai–Erdos–Sos theorem).

Let `J=bar H`. Then `J` is `K4`-free, `alpha(J)=omega(H)<=r-1`, and

`d_J(v)=2r-2-(d_H(v)-r)`.

If `K_r(H)<=7`, every H-excess is at most 7, hence `delta(J)>=2r-9`. For `n=3r-1`,

`2r-9 > 5n/8`

exactly when `r>=68`. AES forces a `K4`-free graph above this threshold to be 3-partite. One part then has size at least `ceil((3r-1)/3)=r`, contradicting `alpha(J)<=r-1`.

## Theorem B — balanced two-triple-connector pattern is impossible

**CLAIM.** Under the main contract and `K_r(H)<=7`, the symbolic pattern

`c=2`, `t=2`, `(|X1|,|X2|,|X3|)=(r-2,r-2,r-2)`

is impossible for every `r>=12`.

**STATUS.** `PROVED_SYMBOLIC`.

This is the entire `c=2` branch, not a fixed-r case check. The proof uses the tripartite degree-2 transversal-cover lemma recorded in `PROOF_ATTEMPTS.md`.

Consequently any remaining counterexample must have `c=3` or `c=4`, i.e. one of

- `(r-2,r-2,r-3)`;
- `(r-2,r-2,r-4)`;
- `(r-2,r-3,r-3)`.
