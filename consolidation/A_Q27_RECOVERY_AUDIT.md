# A-version q27 recovery audit

Status: `RECOVERY_AUDIT`.

Purpose: determine whether the user-supplied A-version contains a standalone recoverable proof body for the q=27 equality closure.

## Verdict

Yes, with an important split:

- the **equality classification** `q=27 => K3,8+2K1 or K3,9+K1` is finite-computation dependent in the A-version;
- the **repivot contradiction for both equality families** is analytic and substantially self-contained once the universal q=27 repivot condition is licensed.

Therefore the A-version contains enough material to reconstruct a clean analytic `Q27_TYPE_I_II` closure proof, but the lower-floor/equality-classification certificate must remain a separate dependency.

## Recovered analytic skeleton

For any degree-13 pivot in the equality regime, the A-version uses the universal condition `q_p=27` and the two shell possibilities.

### Type II: `M=K_{3,9}+K1`

Let the three heavy shell vertices be `x1,x2,x3`, the nine light vertices `Y`, and `z` the isolate. Every light vertex is degree 13 and can be used as a repivot.

After repivoting a light row `D_y`, the new equality shell must again belong to the two classified topologies. The newly introduced vertices force the repivoted topology to remain Type II. For `j=2,3`, the new missing degree of `x_j` is determined by `9-|D_{x1} intersect D_{xj}|`, and the allowed equality degrees are only `9,3,0`. The unique isolate in the new shell must come from another heavy vertex; this forces complete equality of the heavy rows. Repivoting then produces two isolates although Type II has only one, contradiction.

### Type I: `M=K_{3,8}+2K1`

Let `Y` be the eight light vertices and `Z` the two isolates. Repivot a light vertex `y`, with `|D_y|=3`. The ten old-shell vertices outside the three centers form an independent 10-set in the new missing graph, so any new equality topology is forced into one of the two canonical q=27 types.

For `b in D_y`, define the multiplicity

`m_y(b)=|{y' in Y : b in D_{y'}}|`.

The new missing degree of `b` is `11-m_y(b)`. Equality topology therefore forces multiplicity 2 in a Type-II repivot and multiplicity 3 in a Type-I repivot. Hence the light rows decompose into exact duplicate-row equivalence classes, each of size 2 or 3.

Because `|Y|=8`, the only partitions into parts of size 2 or 3 are

- `2+2+2+2`, or
- `2+3+3`.

So at least one size-2 duplicate class exists. Repivoting a member of that class forces Type II, already impossible. Contradiction.

Thus both equality families are analytically excluded.

## Dependencies that must be explicit in the clean rewrite

1. Correct shell semantics: `q=z+sum g_a`, `t_a=d_M(a)+g_a`.
2. Every shell missing edge satisfies `t_a+t_b>=12`.
3. Every relevant repivot vertex is genuinely degree 13.
4. Every degree-13 repivot in the regime satisfies the same upper and lower charge bounds, hence exactly `q=27`.
5. The q=27 equality classification is exactly the two shell types.

Only item 5 is computation-dependent in the A-version. Items 3--4 must be licensed by the proof architecture in which this lemma is used.

## Status recommendation

After a line-by-line clean rewrite and dependency check, the Type I/II repivot contradiction can be promoted to `PROVED` as an analytic theorem. The equality classification should remain separately labelled `COMPUTATION_CERTIFIED` until an independently replayable certificate is stored.
