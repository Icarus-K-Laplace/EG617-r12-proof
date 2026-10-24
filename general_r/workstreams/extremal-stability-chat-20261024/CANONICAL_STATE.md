# CHAT F — Canonical State

Branch: `workstream/general-r-extremal-stability-20261024`

Headline target: explain the `r^2` threshold through extremal/design rigidity and prove nonextension to `r^2+1` without using the residual-core / three-anchor / repivot backend.

## Round F-001 status

### F1 — known sharpness: PARTIALLY CLOSED

For every order `r` admitting an affine plane, there is a much larger sharp family on `r^2` points than the usual presentation “`r-1` parallel classes plus one color containing two classes”.

Take the `r+1` parallel classes `P_1,...,P_r,Q`. For each color `i`, color every edge lying on a line of `P_i` with color `i`. Every remaining edge lies on a line of `Q`; color those edges **arbitrarily** with any of the `r` colors.

Every color still contains the full partition `P_i` into `r` monochromatic `K_r` blocks. Hence every `(r+1)`-set contains a color-`i` edge, for every `i`. Therefore every such assignment is balanced on `K_{r^2}`.

If `m_0=r*C(r,2)=r^2(r-1)/2` is the number of edges in one parallel class, this gives `r^{m_0}` labeled leftover-edge assignments before quotienting by isomorphism.

Consequence: edge-edit stability to one “standard” affine coloring at scale `O(r)` or `o(r^2)` is false. The correct stability object is the **orthogonal partition skeleton**, not the exact leftover-edge coloring.

### F2 — local regularity: OPEN

No theorem yet forces all color-degree vectors near the affine vector. Exact affine examples already have large flexibility in edge allocation on the leftover class.

### F3 — stability: REFORMULATED

The useful target is now:

> Reconstruct `r` pairwise orthogonal spanning `r`-clique partitions (an `r`-net skeleton), possibly after deleting `O(r)` exceptional vertices/edges, rather than approximate a particular edge-coloring.

A particularly strong sufficient statement for Problem 617 would be:

> **Common-deletion perfection target.** In a hypothetical balanced coloring of `K_{r^2+1}`, there exists a vertex `x` such that for every color, the restriction to `V\{x}` contains a spanning partition into `r` monochromatic `K_r` blocks.

The present round does not prove this.

### F4 — canonical design nonextension: PROVED for the full affine-skeleton family

A new theorem proves that the entire arbitrary-leftover family above is nonextendable for every `r>=3`; the proof does **not** require two pure colors.

Core mechanism: for a hypothetical new vertex `x`, each incident color class `A_i=N_i(x)` must hit every permutation transversal of the orthogonal pair `(P_i,Q)`. Minimum matching-preclusion in `K_{r,r}` gives `|A_i|>=r`; summing forces equality for every color. Equality blockers are exactly one `P_i`-line or one `Q`-line. A `Q`-line blocker for color `i` further forces every edge on every other `Q`-line to have color `i`. Hence at most one color can use a `Q`-line blocker; at most one color can use a `P_i`-line blocker because two lines from different `P_i` classes intersect. For `r>=3` this cannot accommodate all `r` colors.

Full proof: `NONEXTENSION_THEOREMS.md`.

### F5/F6 — all-large/all-r: OPEN

The missing bridge is a stability/reconstruction theorem showing that an arbitrary hypothetical extremal restriction contains the affine/net skeleton. The nonextension side is no longer the main blocker.

## Prime-power versus arbitrary r

- Affine planes exist for every prime-power order, so the sharp family and the proved nonextension theorem apply there.
- Affine planes are known not to exist for some composite orders (notably 6 and 10); no finite affine/projective plane is known at any non-prime-power order in general.
- The abstract perfect-sector route uses only orthogonal partitions / nets plus the classical deficiency-one completion theorem; it does not require field coordinates.
- Existence of balanced `K_{r^2}` colorings outside the net/perfect sector for arbitrary non-prime-power `r` remains a separate question.

## Unique largest blocker

> **Skeleton reconstruction:** prove that every `r^2` restriction arising from a hypothetical `K_{r^2+1}` counterexample contains enough orthogonal `r`-clique partitions to enter the proved nonextension theorem.
