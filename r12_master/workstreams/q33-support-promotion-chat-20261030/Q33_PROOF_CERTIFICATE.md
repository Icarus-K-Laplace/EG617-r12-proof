# Q33 support-screen proof certificate

Status: **COMPUTATION_CERTIFIED** for exact integer/profile screening only.

Run:
\`\`\`bash
python3 Q33_INDEPENDENT_VERIFIER.py
\`\`\`

The verifier checks all allowed support sizes and all h values. It exhausts each color's 3- or 4-component U-incidence profile in {0,1,2,3,4}, applies the U and W reserve budgets, and independently checks that the component-pair charge condition gives exactly the same feasible h states as a grouped-profile dynamic program.

The analytic charge is:
\[
\binom{4-k}{2}+2\binom{k}{2}\ge3\quad(k=0,\ldots,4).
\]
Summing over 3m+h unselected component K4s yields
\[
3(3m+h)\le B_W+2B_U.
\]

Verified result:
- m=8: v=31,32,33 excluded; first survivor v=34,h=4,5,6,7.
- m=9: v=32,33,34 excluded; first survivor v=35,h=3,...,9.
- m=10: v=34,35 excluded; first survivor v=36,h=3,...,10.

The grouped-profile DP and the three scalar inequalities agree on all47 (m,v) cells.

Scope: no graph realization is asserted; no complete Q33 UNSAT certificate is claimed.
