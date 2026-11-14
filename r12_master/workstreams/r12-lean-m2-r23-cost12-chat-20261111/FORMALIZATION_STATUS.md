# Verified partial M2 checkpoint — GATE47 still open in Lean

Latest verified code: 89183d0c770227daf4d4a45bc699480586cb4210, CI 43570397008
(2026-11-14). Focused C5 module checks followed by full lake build, statement
inspection, complete axiom allowlist audit and source SHA256 emission all PASS.
C5Types.lean and C5MissingEdge.lean now prove the exact graph-to-type bridge,
complete bipartite singleton-side quotient, incompatible missing-endpoint singleton
type sets, exhaustive five rotations/two orientations, and singleton extension.
All use only propext, Classical.choice and Quot.sound. Full R23 classification is
NOT proved: graph-level neighbor saturation and blow-up identification remain.
The previous checkpoint details below are historical, not the latest totals.

Verified source commit: 875bd3de7478129b507b4f8e9df14f0c8e8bd4f5.
Successful standalone Linux CI: 43361985046. The whole lake build, all 122
declaration axiom reports, statement inspection, nine dependency pins and source
SHA256 checks passed. The project contains 99 kernel-checked theorems.

The substantive new results are the full odd-cycle graph bound and the reduction
of the dense 23-point problem to a shortest C5 with one of three exact bipartite
exterior forms. The type/blow-up classification and Cost-6 are still missing;
the sharp R335/R336 results and GATE47 are not proved. Counts do not certify those
targets. MainTheorem is absent and original baseline mathematics is byte-unchanged.

The numeric maxima use the feasible-cycle bounds 2<=k and 2*k+1<=n. No E286 work
was attempted. The new root workflow is the only user-approved directory exception.
Earlier disk-space approval failures were resolved before retrying; no bypass was used.
