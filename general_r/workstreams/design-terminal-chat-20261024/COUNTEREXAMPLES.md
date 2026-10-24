# Counterexample and construction search

## C1. Is `5r+1` itself disproved as a general pattern?

No. Its numerical origin is exact: `r^2-(r-1)-(r-6)r=5r+1`. Status: **PROVED_SYMBOLIC**.

What is open is whether general front extraction is forced to this stop.

For `r=4,5`, the literal block count `r-6` is nonpositive, so this terminal branch is intrinsically a `r>=6` architecture; small r must be handled separately.

## C2. r=12 equality features do not survive asymptotically

The hereditary cap forces outer charge at least

`(r^2-19r-10)/2`,

which is quadratic from `r>=20`. Hence the r=12 `<=11` charge and the consequent `z=0` proof are not asymptotic. Status: **DISPROVED_AS_GENERAL_PATTERN** for that forcing mechanism.

The budget also stops forcing `delta<=r+1` after r=15. Status: **DISPROVED_AS_GENERAL_PATTERN**.

## C3. Exact affine-plane-like nonextension

The standard affine-plane `r^2` construction is itself a real extremal-looking family, but it cannot be extended to `r^2+1`; this is favorable evidence for the global conjecture, not a counterexample.

## C4. Exact resolvable `TD(5,r)+one point` attempt

The most natural terminal-level infinite construction is rejected in `NONEXTENSION.md`: for `r>=6` it violates the target clique cap, and even without that cap it creates a target-independent 6-set. Status: **DISPROVED** as a legal terminal template.

## C5. Naked graph-level terminals

No claim is made that a single graph on `5r+1` vertices with `alpha<=5`, `omega<=r-1` is impossible. The real rigidity comes from simultaneous completion by the other `r-1` colors and the inherited density caps.

Status: **OPEN** for abstract one-color existence; not a useful terminal notion by itself.

## C6. Remaining plausible objects

Any surviving large-r terminal must be a defected design rather than the naive exact one:

- five near-`r` target groups;
- `r-1` non-target color partitions, almost all blocks being size-5 transversals;
- only `O(r)` repeated/uncovered pair incidences globally;
- mandatory internal target deletions and linear cross-target corrections;
- at least one defect in every non-target parallel class due the extra point.

The next counterexample search should therefore enumerate symbolic **defect incidence patterns**, not arbitrary graphs or literal r=12 shell profiles.
