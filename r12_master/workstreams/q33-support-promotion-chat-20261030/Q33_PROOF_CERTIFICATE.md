# Q33 variable-core profile proof certificate

Status: **COMPUTATION_CERTIFIED** for the finite necessary-profile screen only.

Run:
\`\`\`bash
python3 Q33_INDEPENDENT_VERIFIER.py
\`\`\`

The verifier independently generates every per-color option twice:
1. Cartesian product over ten-component residual profiles (three or four unselected components);
2. recursive dynamic programming over the component core-size/U-incidence states.

For every v=31,...,47, the two group-option sets agree. The global DP checks every m in {8,9,10}, every h=0,...,m, and every support size from its registered lower bound through47.

Results:
- m=8: v=31,32,33,34 excluded; first profile-feasible v=35,h=6,7,8.
- m=9: v=32,33,34 excluded; first profile-feasible v=35,h=9.
- m=10: v=34,35,36,37 excluded; first profile-feasible v=38,h=10.

The variable-core model allows each isolated K5 component to have any core size0,...,4. It does not assume one shell vertex per component.

This is not a full graph CSP, not a graph realization, and not a Q33 UNSAT certificate.


## 2026-10-30 component-only screen

The canonical support family uses seven isolated-K5 component witnesses per exact-129 color, so h=0. Run the component-only verifier:
    python3 Q33_INDEPENDENT_VERIFIER.py

The verifier compares two independent per-color generators (Cartesian product and recursive state DP) for every v=31..47, then combines m identical color-option sets under the exact U/W budgets for all 47 registered (m,v) cells.

Results:
- m=8: v=31..38 excluded; first aggregate survivor v=39.
- m=9: v=32..39 excluded; first aggregate survivor v=40.
- m=10: v=34..40 excluded; first aggregate survivor v=41.

The final DP-state counts are aggregate pair-cost states, not labelled graph configurations. A survivor does not certify graph existence. This certificate is only for the necessary aggregate profile screen; Q33 remains OPEN.
