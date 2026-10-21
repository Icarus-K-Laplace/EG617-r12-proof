# B version partial (pages 1-300) recovery audit

Status: SOURCE_AUDIT / NOT_CANONICAL_PROOF

This file records what can and cannot currently be recovered from the user-supplied partial B version (global B pages 1-300). It is a provenance map for proof consolidation, not a replacement for the canonical theorem registry.

## Scope boundary

The currently supplied B material ends at B:300. It therefore does **not** include the later B:581-B:582 pages cited elsewhere for the q=27 equality decoration uniqueness arguments. Those later pages must not be inferred from this partial batch.

## What this partial B actually contains

The dominant subject of B:1-300 is a later weighted-shell / multi-pivot program around q=38,39,40, K_{5,8}-type shell states, repeated-low-row capacity, simultaneous-tight-edge geometry, and r=11/r=12 external-bootstrap comparisons. Much of this is not a direct source for the modern q=27/q=29 backend.

## Useful boundary/core material

B:241-B:255 contains a 35-vertex boundary analysis proving a generic minimum-degree floor delta(H)>=11 under an inherited cap-three framework. It explicitly states that the easy delta(H)>=12 branch was already removed in that local program and that the remaining object is a degree-11 boundary case. This is **not** the modern CORE211 proof and must not be cited as such.

The same section derives tight-row occupancy inequalities for a degree-13 shell. If ab is a genuine tight missing-shell edge and S=D_a union D_b, then in the r=12 instance the residual calculation gives a lower-core occupancy threshold k=|S cap Z| depending on the edge layer; for the q=38,39,40 states the thresholds are 5,6,7 respectively. This belongs to the historical high-q weighted-shell program.

## Potentially powerful r=12 candidate lemma

B:226-B:240 contains a general residual obstruction specialized to r=12. In the notation used there, for a degree-13 shell with 35-vertex core H, assuming delta(H)>=12 and a **genuine tight missing-shell edge** ab satisfying

- t_a+t_b=12,
- D_a cap D_b = empty,
- |D_a union D_b|=12,

an external/general residual theorem is instantiated to force

    e(H) >= 218.

The pages then compare this with the old q=38,39,40 edge ledgers, where E=e(H) is at most 213,212,211, and derive contradictions.

### Current audit status of this lemma

**CONDITIONAL / NEEDS CLEAN-ROOM AUDIT.**

Reason: the B pages do include the r=12 instantiation and the tight-row implication t_a+t_b=12 => disjoint rows of total size 12, but they explicitly describe the underlying general residual obstruction as coming from a public/pre-review r=10/11-style package or an externally parameterized derivation. The theorem body and provenance are not yet reconstructed in this repository as a self-contained proof. Therefore the implication

    delta(H)>=12 + genuine tight row pair => e(H)>=218

must not yet be promoted to canonical PROVED status.

## Relevance to the current E332 frontier

If the candidate lemma is independently re-proved under the current E332 hypotheses, it would be very strong: E332 has e(H)=211, so **no genuine tight missing-shell edge could exist**. Several q=30 equality mechanisms create exactly such tight row pairs. This could potentially subsume portions of the existing d=3/d=10 equality analysis and may simplify the remaining extreme-shell cases.

For now this is a research lead, not a dependency.

## What this partial B does NOT supply

- no complete modern CORE211 proof;
- no standalone generic q=29 good-repivot theorem;
- no later B:581-B:582 q=27 decoration pages;
- no direct modern E329-E331 closure manuscript.

These remain separate consolidation targets.
