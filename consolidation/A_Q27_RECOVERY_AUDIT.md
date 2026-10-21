# q27 recovery audit from A/B versions

Status: `RECOVERY_AUDIT`.

Purpose: determine whether the supplied historical A/B versions contain a recoverable standalone proof body for the q=27 equality closure.

## Verdict

The analytic closure is now substantially recovered.

- The **two-topology equality classification**
  `q=27 => M is K3,8 + 2K1 or K3,9 + K1`
  remains finite-classification dependent in the recovered source material.
- The **decoration assignment inside both topologies is analytic**: B-version pp.581-582 proves it directly from the edge inequalities and q=27 budget.
- The **repivot contradiction for both equality families is analytic** in the A-version once every degree-13 repivot is known to remain in the q=27 equality regime.

Thus the old belief that decoration uniqueness itself needed a solver is too pessimistic. The only irreducibly non-analytic dependency still visible in the recovered q27 chain is the topology classification unless its verifier/certificate is separately recovered.

## Analytic decoration uniqueness recovered from B581-B582

Use corrected shell notation

`q = z + sum g_v`, `t_v = d_M(v) + g_v`, and for every missing-shell edge `uv`, `t_u+t_v >= 12`.

### Type I topology

`M = K3,8 + 2K1`, so `z=24` and `sum g = 3`.
Let the bipartition be A (size 3, degree 8) and B (size 8, degree 3).
For every `a in A`, `b in B`, the missing edge inequality gives

`8 + g_a + 3 + g_b >= 12`, hence `g_a+g_b >= 1`.

If some heavy vertex `a` had `g_a=0`, then every `b in B` would have `g_b>=1`, so `sum g >= 8`, contradicting `sum g=3`.
Therefore all three heavy vertices have `g_a>=1`; since the total excess is exactly 3,

`g=(1,1,1,0,...,0)`.

Consequently every heavy row has `t=9`, every light row has `t=3`, and every missing edge is tight: `9+3=12`.

### Type II topology

`M = K3,9 + K1`, so `z=27` and `q=27` forces `sum g=0`.
Hence `g=0` identically. Heavy rows have `t=9`, light rows have `t=3`, the isolate has `t=0`, and every missing edge is tight.

So for both q27 equality topologies, every missing-shell edge is exactly tight.

## Recovered analytic repivot closure

Assume the proof architecture licenses that every relevant degree-13 repivot satisfies the same upper and lower charge bounds, hence again has `q=27`; therefore its new missing-shell graph must be one of the two equality topologies above.

### Type II: `M=K3,9+K1`

Let the three heavy shell vertices be `x1,x2,x3`, the nine light vertices `Y`, and `z` the isolate. Every light vertex is degree 13 and can be repivoted.

Repivot a light row. In the new shell, the old pivot and old isolate both appear as degree-9 vertices, so the new equality topology cannot be Type I (whose heavy degree is 8); it must again be Type II.
For the other heavy vertices, their new missing degrees are controlled by row intersections. Since the only allowed missing degrees in Type II are `9,3,0`, the unique new isolate must come from one of the remaining heavy vertices. This forces two heavy rows to be identical; symmetry forces all three heavy rows identical.
Repivoting again then creates two isolates, contradicting the fact that Type II has exactly one isolate.
Therefore Type II is impossible.

### Type I: `M=K3,8+2K1`

Let `Y` be the eight light vertices and `Z` the two isolates. Every light vertex is degree 13 with a 3-row `D_y`.
Repivot a light vertex `y`. The ten old-shell vertices outside the three heavy centers form an independent 10-set in the new missing graph, so the new q27 equality shell is forced into one of the two canonical topologies.

For `b in D_y`, define

`m_y(b)=|{y' in Y : b in D_{y'}}|`.

In the repivoted shell, the missing degree of `b` is `11-m_y(b)`.
If the new topology is Type II, its allowed high degree 9 forces `m_y(b)=2` for all `b in D_y`.
If the new topology is Type I, its allowed high degree 8 forces `m_y(b)=3` for all `b in D_y`.
The isolate structure in either case forces every other row containing `b` to equal `D_y`; hence the light rows partition into exact duplicate-row equivalence classes, each of size 2 or 3.

Since `|Y|=8`, the only partitions into 2s and 3s are `2+2+2+2` and `2+3+3`. Thus a size-2 duplicate class must exist. Repivoting a row from that class forces a Type-II equality shell, already impossible. Hence Type I is impossible.

Therefore, conditional only on the two-topology equality classification and universal q27 repivot licensing, no q27 equality shell survives.

## Remaining proof-completeness dependency

The current recovered sources do not yet provide a repository-replayable certificate for the statement that the only q27 shell topologies are

- `K3,8 + 2K1`, and
- `K3,9 + K1`.

A-version records a finite classification; B-version confirms and analytically resolves the decoration assignments. Until the finite classifier/verifier is recovered or the topology classification is re-proved analytically, the full q27 theorem should be represented as:

- `COMPUTATION_CERTIFIED` for the two-topology classification, once a replayable certificate is stored;
- `PROVED` for decoration uniqueness and Type-I/Type-II repivot elimination.

## Provenance

- A-version: q27 equality classification and analytic repivot/duplicate-row contradiction.
- B-version pp.581-583: analytic decoration uniqueness, tightness of every q27 missing edge, and corrected two-topology statement.
