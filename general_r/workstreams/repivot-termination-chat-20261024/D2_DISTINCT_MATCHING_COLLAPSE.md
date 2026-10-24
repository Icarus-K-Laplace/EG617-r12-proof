# d2 Distinct-Support Matching Collapse — RETRACTED

Status: **`DISPROVED_AS_STATED`**.

## Dependency audit

The attempted theorem used the implication

> an owner y together with an independent triple in `H\D_y` would form a forbidden independent 4-set in F.

That implication requires

`alpha(F)<=3`.

However the actual general backend setup in `GENERAL_R_SYMBOLIC_BACKEND_IDENTITY.md` is

> **`alpha(F)<=4`, `omega(F)<=r-1`.**

Therefore an independent 4-set is allowed. The support-transversal step

`alpha(H\D_y)<=2`

is not justified, and every downstream conclusion from that step is withdrawn, including:

- the claimed allowance-independent matching bound `nu(Q)<=3`;
- the claimed six-hub core vertex cover;
- the 63-signature collapse derived from that cover.

The Mantel comparison used later in the attempted proof is arithmetically correct *conditional on* `alpha(H)<=2`, but the proof does not establish `alpha(H)<=2` from four disjoint supports under the real backend hypotheses.

## What remains valid elsewhere

This retraction does **not** affect the independently proved results in `D2_DISTINCT_SUPPORT_REDUCTION.md`, which use only the valid core condition `alpha(H)<=3`, row closure, the exact q-flat support equation, and hereditary/residual caps. In particular the following remain valid:

- exact support-transition identity `d_z^(y)=2-|D_y intersect D_z|`;
- absolute `a=0` bound `|E(Q)|<=3`;
- absolute `a=1` bound `|E(Q)|<=12`;
- weighted matching inequality `nu(Q)(a-1)<=W`;
- the partial `a=2` structural reduction;
- the distinct-support hereditary capacity inequality in its stated range.

## Research consequence

The distinct-support fully-decorated d2 branch is therefore **still open**. Any future matching/hub collapse must be derived from `alpha(H)<=3`, row closure, transported excess, hereditary capacity, or a genuinely valid consequence of `alpha(F)<=4`; it may not forbid independent 4-sets in F.

This file is retained as an explicit negative audit certificate so the invalid argument is not accidentally reused.