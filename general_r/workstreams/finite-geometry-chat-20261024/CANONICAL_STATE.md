# CHAT K — Finite Geometry / Prime-Power Route

Branch: `workstream/general-r-finite-geometry-20261024`

Scope: prime-power / finite-geometry route only. Do not treat existence of an affine plane as a proof of Problem 617.

## Target

For `q` a prime power, prove `P(q)` or at least `P(q)` for all sufficiently large prime powers.

## First-round status

**K1 not yet achieved**, but two structural facts are now isolated and one strategic obstruction is explicit.

### K.1 — Two exact `q^2` Turan partitions force orthogonality

On any `q^2`-vertex restriction, if two color graphs both attain the minimum edge count compatible with independence number at most `q`, then each is a disjoint union of `q` copies of `K_q`. Because the two colors are edge-disjoint, every block of one partition meets every block of the other in at most one point. There are exactly `q^2` block pairs and `q^2` points, so every intersection has size exactly one.

Thus the two clique partitions are abstractly orthogonal, with no field assumption.

Combined with the already-proved two-partition nonextension theorem in `GENERAL_R_AFFINE_PLANE_NONEXTENSION.md`, a hypothetical counterexample on `q^2+1` vertices has the property:

> for every removed vertex `x`, among the `q` color graphs on `V\{x}`, at most one color can be exactly Turan-minimal.

### K.2 — Prime-power assumption is currently inert before coordinatization

An arbitrary coloring of `K_(q^2+1)` does not come with a canonical identification of `q^2` vertices with `F_q^2`. Therefore polynomial, character-sum, or association-scheme methods cannot be applied directly merely because `q` is a prime power.

A field-specific proof must first extract one of:

- two or more near/exact orthogonal clique partitions;
- an affine-net / resolvable-design incidence structure;
- a coordinate-bearing difference structure.

Hence the immediate K-line target is **structural extraction/coordinatization**, not a raw polynomial identity on arbitrary vertex labels.

### K.3 — Kakeya connection

If a deletion/compression obstruction in an affine model requires the deleted set to contain a whole line in many directions, the deleted set is a partial Kakeya/Besicovitch set. Known planar finite-field Kakeya bounds are quadratic in `q`, whereas the induction shell has only linear size `2q-1`.

This strongly supports a dichotomy strategy:

> small shell succeeds, or failure forces enough affine directions that finite-geometry nonextension/Kakeya bounds become available.

## Next theorem target

Prove a quantitative **multicolor near-Turan coordinatization lemma** on a `q^2` restriction:

> if several color graphs have sufficiently small Turan slack, then two of them admit clique partitions (possibly after `o(q^2)` edits) whose block-intersection matrix is close to the all-ones matrix.

Then use the extra vertex to upgrade robust orthogonality to an exact contradiction.