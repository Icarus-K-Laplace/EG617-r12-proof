# Claim Ledger

## G-A-001 — core minimum degree one-step bound

Claim: hereditary-cap core implies `delta(H)>=r-1` for `r>=6`.

Verdict: **PASS**.

Attack: complement translation, exact cap recomputation, AES threshold, induced-nonneighbor reduction.

Impact: safe to use as stated. It does not supply `delta(H)>=r`.

## G-A-002 — exact `delta(H)>=r`

Claim: the present A assets already imply `delta(H)>=r`.

Verdict: **FAIL AS A PROMOTION / OPEN IN SOURCE**.

Witness: source itself retains the degree-`r-1` boundary class. No graph counterexample to the final desired theorem has been produced; the failure is a proof-status issue, not a mathematical disproof.

Repair: eliminate the boundary blocker using the residual/shell interface, exactly as the sibling branch proposes.

## G-B-001 — sufficiently-large three-anchor closure

Claim: main three-anchor target holds for every `r>=68` by AES.

Verdict: **PASS**.

Attack: recompute complement degrees and solve the strict threshold exactly.

Numerics: `2r-9 > 5(3r-1)/8` iff `r>67`.

Impact: any counterexample to the three-anchor theorem must lie in `12<=r<=67` once the stated contract holds.

## G-C-001 — K as a third potential coordinate

Claim: `K` adds a genuinely new monotone coordinate after `q`.

Verdict: **FAIL**.

Reason: inside a fixed residual, `Delta K=-2 Delta q`; K is affine-redundant with q. The sibling branch already recognizes this, so this is a killed idea rather than a bug in its current state.

## G-C-002 — closed non-improving cycle rigidity

Claim: a closed cycle all of whose steps are lexicographically non-improving in `(q,tau)` must be q-flat and tau-flat.

Verdict: **PASS**.

Attack: direct telescoping of q around the cycle, followed by telescoping/monotonicity of tau on the q-flat plateau.

Limitation: does not eliminate flat cycles.

## G-C-003 — universal Q2 refinement

Claim: every non-rigid equal-`(q,tau)` move strictly improves `Q2`.

Verdict: **NOT_PROVED / NOT PROMOTABLE**.

The sibling branch gives an exact update formula but explicitly leaves monotonicity open.

## G-F-001 — edge-edit stability to standard affine coloring

Claim: every sharp/near-sharp coloring is `O(r)` or `o(r^2)` edge recolorings from the usual construction with one heavy color.

Verdict: **COUNTEREXAMPLE**.

Witness family: affine-plane skeleton with arbitrary coloring of every edge in the unused parallel class.

Impact: stability must be formulated modulo leftover-edge freedom, at the level of orthogonal partitions / nets.

## G-F-002 — arbitrary-leftover affine-skeleton nonextension

Claim: the full arbitrary-leftover affine-skeleton family cannot be extended by one new vertex for `r>=3`.

Verdict: **PASS (analytic audit of the new proof)**.

Attack: verify transversal-independence, Hall/matching-preclusion equality cases, row-case incompatibility, and column-case forcing.

No field algebra is used after the affine-plane incidence axioms are supplied.
