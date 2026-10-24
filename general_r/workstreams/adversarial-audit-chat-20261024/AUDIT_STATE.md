# CHAT G — Adversarial Audit State

Branch: `workstream/general-r-adversarial-audit-20261024`

Mission: attempt to falsify every promoted general-r claim before it enters a master proof. This branch is read-only with respect to sibling workstreams.

## Round G-001 summary

### Chat A — residual-core extraction

**CLAIM AUDITED:** under the hereditary-cap core contract, `delta(H)>=r-1` for `r>=6`, with the only failure of the desired `delta(H)>=r` being a degree-`r-1` boundary blocker whose complement is within one edge of the non-bipartite Mantel extremum.

**VERDICT:** `PASS_WITH_EXTERNAL_INPUT`.

The internal algebra and the reduction are correct. In particular, the current sibling source does **not** claim `delta(H)>=r`; it explicitly leaves that final boundary elimination open. Any master theorem silently replacing `r-1` by `r` would be invalid.

### Chat B — exact three-anchor excess

**CLAIM AUDITED:** if the main three-anchor contract holds and `K_r(H)<=7`, then for `r>=68` the complement has minimum degree above the `K4`-free Andrasfai--Erdos--Sos threshold and becomes 3-partite, contradicting `alpha(bar H)<=r-1`.

**VERDICT:** `PASS` for the stated `r>=68` theorem, conditional only on the classical AES theorem.

Exact threshold check:

`2r-9 > 5(3r-1)/8  <=>  r>67`.

Thus the integer threshold is exactly `r>=68`.

This audit does **not** certify the still-open range `12<=r<=67` and does not certify the full conjecture.

### Chat C — repivot termination

**CLAIM AUDITED:** `(q,tau)` plateau-cycle rigidity, affine relation between `K` and `q`, and the proposed `Q2` refinement.

**VERDICT:** `PASS_WITH_LIMITATIONS`.

The telescoping identity rules out any closed cycle containing a strict decrease if all steps are assumed non-improving, but it does not prove that every plateau move improves `Q2`. The sibling source explicitly marks universal `Q2` monotonicity and the full termination theorem as OPEN. No false promotion was detected in the audited files.

### Chat F — extremal stability

**CLAIM AUDITED:** extremal `K_{r^2}` colorings should be `O(r)` or `o(r^2)` edge edits from the usual affine construction with one heavy color.

**VERDICT:** `COUNTEREXAMPLE`.

On every affine plane of order `r`, reserve one full parallel class `P_i` for each color `i` and color every edge of the remaining parallel class `Q` arbitrarily. Balance survives because each color retains a spanning partition into `r` monochromatic `K_r` blocks. If the `Q`-edges are spread among colors, these examples are `Theta(r^3)` edits away from any single-heavy-color standard assignment.

This kills edge-edit stability to one canonical coloring, but it does **not** kill stability to the underlying orthogonal-partition skeleton.

### Chats D/E

**VERDICT:** `NOT_TESTABLE_YET` in this first pass.

The branches were visible, but their expected workstream paths were not available through the first content lookup. No claim from D/E is promoted here merely from branch names or user summaries.

## Dependency status

No circular dependency was found in the audited A/B/C files. In particular, Chat C labels its endpoint theorems as conditional on A+B and does not use its own conclusion to prove B.

## Highest-value next attacks

1. Search for actual counterexamples to the three-anchor conjecture in `12<=r<=67`, first on structural quotients / degree sequences, then SAT/ILP if needed.
2. Attack Chat C's remaining d2 plateau: construct an equal-`(q,tau)` legal cycle or show the proposed `Q2` coordinate can decrease/oscillate.
3. Attack the corrected F skeleton-stability conjecture by seeking balanced `K_{r^2}` colorings with no full `r`-net skeleton.

## Current strongest negative result

`F-NAIVE-STABILITY-FAIL`: exact edge-label stability to one standard affine coloring is false for an exponentially large family of sharp examples.
