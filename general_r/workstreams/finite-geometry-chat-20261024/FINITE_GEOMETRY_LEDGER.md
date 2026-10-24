# Finite-Geometry Ledger

## 1. What affine geometry already gives

The architecture branch already proves:

> the standard affine-plane coloring on `q^2` points cannot be extended by one vertex while preserving the property that every `(q+1)`-set sees all `q` colors.

Only two orthogonal clique partitions are needed for that proof.

Therefore K-line work should not re-prove affine nonextension. The missing step is extraction/stability: force two sufficiently rigid near-partitions from an arbitrary hypothetical counterexample.

## 2. Prime-power hypothesis: precise role

The statement `q` is a prime power guarantees the existence of the Desarguesian affine plane `AG(2,q)` and the field `F_q`, but an arbitrary coloring has no canonical coordinates.

Thus the following implication is **invalid without an extraction theorem**:

`q prime power => arbitrary color classes are algebraic direction classes`.

Polynomial method, character sums, Bose-Mesner algebra, and finite-field incidence bounds become legitimate only after a coordinate-bearing incidence object has been extracted.

## 3. Kakeya/Besicovitch bridge

In an affine plane, if a deletion set must completely contain one line from many distinct directions, its union is a partial Kakeya configuration.

For all `q+1` directions, the elementary pair-intersection argument gives the universal lower bound

`|K| >= C(q+1,2) = q(q+1)/2`.

For odd prime powers, the sharp planar finite-field Kakeya theorem is stronger:

`|K| >= q(q+1)/2 + (q-1)/2`.

The key strategic point is scale: Kakeya obstruction size is `Theta(q^2)`, whereas the induction shell `2q-1` is only `Theta(q)`.

Hence once a failed compression can be shown to contain full lines in `Omega(q)` genuinely distinct directions, a contradiction with a linear shell becomes plausible even without needing the sharp constant.

## 4. Partial-direction elementary bound

If a set contains one full affine line from each of `t` distinct directions, then

`|K| >= tq - C(t,2)`.

Proof: each line has `q` points and each pair of distinct-direction lines intersects in at most one point; use the first two terms of inclusion-exclusion.

Consequently, if `|K| <= 2q-1`, then necessarily

`tq - C(t,2) <= 2q-1`.

For `t>=3` and large `q`, this already becomes restrictive; for `t` linear in `q`, the lower bound is quadratic.

## 5. Structural target suggested by the literature

Do not try to apply Dvir/Nullstellensatz directly to the original coloring. Instead prove a bridge of the form:

> many low-slack colors => many almost-clique blocks => after cleaning, one line-like block per many directions must be simultaneously respected by the exceptional vertex or by any compression shell.

At that point finite-plane Kakeya/nonextension results can finish the argument.

## Literature anchors

- A. Blokhuis and F. Mazzocca, *The Finite Field Kakeya Problem*, Bolyai Society Mathematical Studies 19 (2008); arXiv:0911.4370.
- S. Ball, *On sets of points in a finite affine plane containing a line in every direction* (planar Kakeya lower bounds).

These are supporting tools only; they do not by themselves prove Problem 617.