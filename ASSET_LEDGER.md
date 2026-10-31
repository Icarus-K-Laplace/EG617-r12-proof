# Asset ledger — fixed-r12 publication view

| Asset | Status | Exact scope / source |
|---|---|---|
| Original $K_{145}$ 12-color obstruction | **PROVED** | Integrated proof commit `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`, `FINAL_GLOBAL_PROOF.md` |
| Independent audit | **PASS** | Commit `09a88cc4fe1e2cf1f3a87475d6484f681910b23e`; AI-assisted informal certification |
| Original coloring caps and extraction | PROVED | Original full-color context; exact frontend proof |
| Contextual $R(4,49)$ exclusion | PROVED | Only in the original full-color coloring context; not a generic uncolored theorem |
| 47-point low-edge obstruction | PROVED | Exact hypotheses: 47 vertices, minimum degree at least 12, alpha at most 4, clique number at most 11; no more than 285 edges excluded |
| 286-edge equality classification | PROVED | Same exact 47-point graph contract; see equality classification and audit |
| 47-point universal floor | PROVED | Every graph in the stated $R(4,47)$ contract has at least 287 edges |
| 48-point floor | PROVED | Every graph in the stated $R(4,48)$ contract has at least 310 edges |
| h12 terminal | PROVED EMPTY | Dedicated 48-point floor and q20 inserted-hub contradiction |
| COVER (Q\ge29) | PROVED | 61-point hereditary contract with minimum degree 13; energy-independent |
| COVER E407/E408 promotion | PROVED | Exact 61-point parent contract; E407 implies (Q\ge30), E408 implies (Q\ge31) |
| h13 low energies | PROVED EMPTY | (E\le406), using (Q\ge29) and the 287-edge core floor |
| h13 E407/E408 | PROVED EMPTY | Pointwise core bounds contradict COVER maximum-charge bounds |
| T61 other minimum degrees | PROVED EMPTY | Degree at most 11 and at least 14 excluded under the contextual contract |
| Frontend recurrence | COMPUTATIONALLY VERIFIED | 1,752 nodes and 144 terminal comparisons; analytic rule/completeness proofs are separately documented |
| Q27/Q28 finite states | COMPUTATIONALLY VERIFIED | 19,448 row vectors per case; 2 and 8 canonical states; 81,920 subset identities replayed |
| Q30 terminal classification | PROVED | Exact E408 maximum-charge parent contract; see independent report at commit `a0f922ad09af99575bae581864b673aa4d41f00d` |
| Q32 285-edge theorem | PROVED | Separate exact contract; not the Q33 theorem |
| Q33 284-edge theorem | PROVED | Separate exact contract; not the Q32 theorem |
| Lean 4 formalization | OPEN / NOT STARTED TO COMPLETION | No completed proof-assistant kernel certificate is claimed |
| External human peer review | OPEN | Not yet performed |
| General-r conjecture | OPEN | Outside the fixed-r12 result |
| Abstract uncolored high-energy $R(4,49)$ | OPEN / OUTSIDE DEPENDENCY PATH | Not claimed solved; contextual exclusion suffices for the original coloring proof |

All status labels above refer to the pinned fixed-r12 proof and its exact hypotheses. See `PUBLICATION/PROOF_STATUS.md` for the complete scope and limitations.
