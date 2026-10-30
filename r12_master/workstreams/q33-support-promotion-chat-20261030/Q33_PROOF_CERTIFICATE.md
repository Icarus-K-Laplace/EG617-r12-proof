# Q33 support-screen proof certificate

Status: **COMPUTATION_CERTIFIED** for the arithmetic screen only.

Run with Python 3 standard library:
\`\`\`bash
python3 Q33_INDEPENDENT_VERIFIER.py
\`\`\`

The verifier exhausts all k_i in {0,1,2,3,4} for the three- and four-component minima f0/f1, every h=0,...,m, and every support size from its lower bound through47.

First implementation:
- m=8: v=31,32 excluded; first survivor v=33,h=5.
- m=9: v=32,33 excluded; first survivor v=34,h=4,5,6.
- m=10: v=34 excluded; first survivor v=35,h=2,...,8.

A separate dynamic-programming implementation of f0/f1, independent of the Cartesian-product enumeration, reproduced all47 (m,v) cells and the same survivor sets. Result: **PASS**.

This certificate checks arithmetic only. It does not verify the parent graph hypotheses, produce a graph realization, or certify full Q33 UNSAT.
