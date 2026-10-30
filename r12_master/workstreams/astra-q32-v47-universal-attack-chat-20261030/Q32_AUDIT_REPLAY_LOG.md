# Independent U6 audit replay log

Date: 2026-10-30  
Mode: independent JavaScript replay using the committed edge lists and a fresh S4 support-orbit enumerator.

## Results

- Support orbits: h=3 -> 2; h=4 -> 3; h=5 -> 5.
- Surviving intermediate support templates: exactly P and D.
- P mixed-pair bound: 90 legal (a,b) cases, minimum 4 at (2,3).
- D mixed-pair bound: 90 legal (a,b) cases, minimum 5 at (2,2).
- P diagnostic graph: 47 vertices, 285 edges, minimum degree12, excess6, 3,256 independent 5-sets, zero K12.
- D diagnostic graph: 47 vertices, 285 edges, minimum degree12, excess6, 1,901 independent 5-sets, two K12s.

Both diagnostic graphs fail the full core contract. This confirms the committed failed-search reports; it does not prove nonexistence. The nonexistence conclusion is analytic in UNIVERSAL_Q32_THEOREM.md.

The existing Python verifier receipt remains available in verification_log.txt and verification_results.json. The JavaScript replay independently covers the support-orbit and terminal integer checks and directly recounts both stored graph edge lists.
