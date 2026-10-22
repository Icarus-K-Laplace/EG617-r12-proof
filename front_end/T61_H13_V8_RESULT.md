# T61 H13 V8 result ledger

Status: `SOURCE_REPORTED / PACKAGE_PRESENT / INDEPENDENT_REPLAY_PENDING`.

Package supplied by the external Line-A agent: `T61_H13_V8.zip`.

Under the retained T61 hereditary-cap contract, the package reports the following analytic theorem. Let `p` be a maximum-charge degree-13 pivot with

`Q=30+k`, `1<=k<=3`.

For every regular shell neighbour of missing degree3, the correction parameter `rho` satisfies

`rho <= k-1`.

The boundary family `rho=k` is reported analytically excluded using the common `K11`, row-triangle structure, and repeated legal repivots. The package also reports full excess-migration and reverse-repivot identities.

The package explicitly does **not** close `E407` or `E408`.

Remaining Line-A obligations reported by V8:

1. exclude the low maximum-charge branches
   - `E407: Q_max=27`,
   - `E408: Q_max in {27,28}`;
2. rule out compatibility/cycles of nonzero correction terms across different pivots. A single-row equality is not enough to establish global row consistency.

The package reports exact arithmetic checks/certificate tables passing, but scalar certificate rows are necessary conditions only and are not treated as realized graphs.

Until the package proof body and verifier are independently replayed inside this repository, the evidence status remains source-reported. No `E407/E408` closure is registered here.