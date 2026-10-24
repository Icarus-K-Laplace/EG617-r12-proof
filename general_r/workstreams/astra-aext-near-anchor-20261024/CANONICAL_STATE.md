# ASTRA A_ext* extraction attack
Status: PARTIAL. A_EXT_STAR remains OPEN.
Date: 2026-10-24.

## Frozen input
- architecture: a922c4d7646eb8d0087bde8547562c8aace02ee2
- CHAT E asymptotic: aa7fbbda16ff0170c9bf7c440ca961a7a8aab3c0
- CHAT H front recurrence: 95c9df0e06de61c84c4cfed0ec00bbd48f0ebf64
- CHAT A extraction: 614a956a7e964f42c0818eca05e3ca9e26a6458a

See SOURCE_MANIFEST.json for exact inspected paths and blob SHAs. No sibling workstream is modified.

## Results
PROVED: original colouring constraints, normalized greedy extraction with exact cross-edge accounting, simultaneous second-Turan excess ledger.
PROVED: an explicit non-target-colour graph attains the contextual lower bound while satisfying alpha=r, omega=a; for r>=2a(a-1)+2 it satisfies every inherited single-colour density cap. In particular this obstruction exists for a=6 and every r>=62.
PROVED: the scalar edge ledger leaves 8r+12 units at a=6 even after a second-Turan floor for the target.
OPEN: eliminate or bypass all first K_r-free stops 6<=a<=r-1 using simultaneous colour compatibility.
OPEN: A_ext*(r), at r>=67 or any larger uniform threshold.
CONDITIONAL: the desired dichotomy follows if the precise high-stop extraction lemma in THEOREM.md is supplied, together with the pinned lower-terminal results.

No actual counterexample colouring, no realized target high stop, and no design-terminal exclusion is claimed.
