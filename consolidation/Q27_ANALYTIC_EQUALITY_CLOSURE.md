# q27 analytic equality closure

Status split:

- `PROVED_ANALYTIC`: decoration uniqueness for both q27 equality topologies.
- `PROVED_ANALYTIC`: Type-I / Type-II repivot contradictions.
- `OPEN_CERTIFICATE_DEPENDENCY`: replayable proof/certificate that the only q27 shell topologies are exactly the two listed below.

This file intentionally separates analytic mathematics from the finite-topology classification dependency.

## Setup

Let `M` be the 13-vertex missing-shell graph for a degree-13 pivot. For each shell vertex `v`, define

`g_v = d_F(v)-13 >= 0`,

`t_v = d_M(v)+g_v`,

and

`q = e(M)+sum_v g_v`.

Every missing-shell edge `uv` satisfies

`t_u+t_v >= 12`.

Assume `q=27` and that the finite equality classification has reduced `M` to one of:

1. Type I: `K3,8 + 2K1`;
2. Type II: `K3,9 + K1`.

Assume also that every degree-13 repivot used below remains in the same q27 equality regime.

## Lemma 1 — Type-I decoration is unique

For Type I, `e(M)=24`, hence `sum g=3`.
Write the nontrivial bipartition as `A union B`, with `|A|=3`, `|B|=8`, where vertices of A have missing degree 8 and vertices of B have missing degree 3.
For every `a in A`, `b in B`,

`8+g_a + 3+g_b >= 12`,

so

`g_a+g_b >= 1`.

If some `a in A` had `g_a=0`, every `b in B` would satisfy `g_b>=1`, giving `sum g>=8`, contradiction.
Thus all three vertices in A have positive decoration. Since total decoration is exactly 3,

`g_a=1` for every `a in A`,

and all remaining vertices have decoration 0.
Therefore heavy rows have `t=9`, light rows have `t=3`, isolates have `t=0`, and every Type-I missing edge is tight:

`9+3=12`.

## Lemma 2 — Type-II decoration is unique

For Type II, `e(M)=27`, and q=27 immediately yields `sum g=0`.
Therefore all decorations vanish. Heavy rows have `t=9`, light rows have `t=3`, the isolate has `t=0`, and every missing edge is tight.

## Lemma 3 — Type II is impossible under q27 repivot equality

Let the heavy vertices be `x1,x2,x3`, light set `Y` with `|Y|=9`, and isolate `z`.
Every `y in Y` has shell degree 3 and `g_y=0`, hence target degree 13 and is a legal repivot.

Repivot at such a light vertex. In the new shell, the old pivot and old isolate both have missing degree 9. Therefore the new equality shell cannot be Type I, whose high missing degree is 8. It must again be Type II.

The new missing degrees of the remaining heavy vertices are controlled by intersections of their attachment rows with the repivot row. Since Type II allows only missing degrees `9,3,0`, and since the repivoted shell has exactly one isolate, one of the remaining heavy vertices must become that isolate. This forces its attachment row to coincide with the repivot-determined heavy row. Repeating symmetrically forces all three heavy attachment rows to be equal.

Repivoting again with this equality of heavy rows creates two isolates, contradicting that Type II has exactly one isolate.
Hence Type II cannot occur.

## Lemma 4 — Type I is impossible under q27 repivot equality

Let heavy set `X` have size 3, light set `Y` have size 8, and isolate set `Z` have size 2.
Every `y in Y` has a 3-row `D_y` and is a degree-13 repivot.

After repivoting `y`, the ten old-shell vertices outside the three heavy centers form an independent 10-set in the new missing graph. Thus the new q27 equality shell must again be one of the two canonical topologies.

For `b in D_y`, define

`m_y(b)=|{y' in Y : b in D_{y'}}|`.

In the repivoted shell, the missing degree of `b` is

`11-m_y(b)`.

If the new shell is Type II, its relevant high missing degree is 9, hence `m_y(b)=2` for all `b in D_y`.
If the new shell is Type I, its relevant high missing degree is 8, hence `m_y(b)=3` for all `b in D_y`.

The isolate structure forces all light rows containing a given `b in D_y` to coincide with `D_y`. Therefore the family `{D_y : y in Y}` decomposes into duplicate-row equivalence classes, each of size 2 or 3.

Since `|Y|=8`, the only partitions into 2s and 3s are

`8=2+2+2+2`

or

`8=2+3+3`.

Thus at least one duplicate class has size 2. Repivot a row from such a class. By the multiplicity rule above, the new equality shell must be Type II, already ruled out by Lemma 3. Contradiction.
Hence Type I cannot occur.

## Conclusion

Conditional on the finite two-topology q27 classification and the universal q27 repivot licensing condition,

`q=27`

has no surviving equality shell.

The analytic part is now source-recovered and self-contained at the level above. The remaining consolidation task is to recover or rebuild a replayable certificate for the two-topology classification itself.

## Historical source provenance

- B-version pp.581-583: analytic decoration uniqueness and tightness of all q27 missing edges.
- A-version: Type-I/Type-II repivot elimination via duplicate-row geometry.
