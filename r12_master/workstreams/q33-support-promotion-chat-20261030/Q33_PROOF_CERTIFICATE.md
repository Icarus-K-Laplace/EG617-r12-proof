# Q33 support-screen proof certificate

Status: **COMPUTATION_CERTIFIED** for exact integer/profile screening only.

Run:
\`\`\`bash
python3 Q33_INDEPENDENT_VERIFIER.py
\`\`\`

The verifier exhausts all support sizes, h values, and per-color 3/4-component k-profiles. It checks the U reserve with the sharp gadget-overlap coefficient4, the W reserve, and the component-pair charge. A grouped-profile dynamic program independently confirms the scalar feasible h sets for all47 (m,v) cells.

Verified:
- m=8: v=31,32,33 excluded; first survivor v=34,h=7.
- m=9: v=32,33,34 excluded; first survivor v=35,h=5,...,9.
- m=10: v=34,35 excluded; first survivor v=36,h=3,...,10.

The sharp coefficient4 follows because alpha(C[Q])<=2 forces at least two of the six Q-pairs to be owned by C itself; all other colors together can occupy at most four.

No graph realization or complete Q33 UNSAT certificate is claimed.
