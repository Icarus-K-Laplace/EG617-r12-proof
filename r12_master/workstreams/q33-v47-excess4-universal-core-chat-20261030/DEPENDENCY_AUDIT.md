# Independent Q33 284-edge theorem — dependency audit

Date: 2026-10-30  
Branch: workstream/r12-q33-v47-excess4-universal-core-attack-20261030

| Item | Required input | Status in this workstream | Notes |
|---|---|---|---|
| D1 | 47 vertices, 284 edges, minimum degree at least 12, alpha<=4, omega<=11 | **PROVED_CONDITIONAL** as Q33 parent contract | Four facts are directly inherited; minimum degree is retained V11 interface |
| D2 | Total excess equals four | **PROVED** | Handshake identity 568-564=4 |
| D3 | Independent four-set among degree-12 vertices | **PROVED** | Four Turan lower bounds 346,342,338,333 |
| D4 | Private clique construction and Z range 3..5 | **PROVED** | Uses alpha<=4 and omega<=11 |
| D5 | 25-point non-bipartite triangle-free extremal bound | **PROVED_CONDITIONAL** | Kang-Pikhurko Theorem 1, n=25,r=2; primary PDF checked |
| D6 | Common-neighbor capacity and K10 completion capacity | **PROVED** | Derived from D1 and D5 |
| D7 | K11-K11 pair spends at least six excess units | **PROVED** | Exact integer inequality; minimum six at (2,2) |
| D8 | All h=3,4,5 support templates excluded | **PROVED** | Analytic case split, no sibling lemma imported |
| D9 | Support multiset and local integer minima replay | **COMPUTATION_CERTIFIED** | Independent verifier; finite arithmetic only |
| D10 | V11 minimum-degree source package independently replayed | **OPEN** | Root audit still says INDEPENDENT_REPLAY_PENDING |
| D11 | Full EG617(r=12) theorem | **OPEN / NOT_CERTIFIED** | Outside this workstream |

## External source

Kang and Pikhurko, 2005, Theorem 1:
https://opikhurko.warwick.ac.uk/E/KangPikhurko05ms.pdf

At n=25,r=2, t_2(25)=156 and p_2(25)=145.

## Explicit non-dependencies

- Astra's Q32 285-edge theorem;
- any 285-edge / excess-six assumption;
- C's Q33 support-promotion casework;
- selected 31-point / 56-witness reserve;
- P49 component profiles;
- any fixed four-core assumption for exact-129 color components;
- any SAT/UNSAT solver result;
- random search failure;
- unproved zero-missing-set exclusions.

The support proof handles a_i=0 explicitly in the K10 branches.
