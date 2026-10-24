# Assumption Ledger — Front Recurrence Round 2

Date: 2026-10-24

| ID | Statement | Status | Exact scope / dependency |
|---|---|---|---|
| A-H1 | Symbolic recurrence has seven transition schemas and potential \(\Phi_r(a,n)=(r^2+2)a+n\) strictly decreases | PROVED | Conditional termination only; does not prove EG617 |
| A-H2 | Contextual state contract: \(\alpha(J)\le a\), \(\omega(J)\le r-1\), every induced subset obeys \(e(J[Y])\le D_r(|Y|)\) | INPUT CONTRACT | Must be checked for every state to which a cutoff is applied |
| A-H3 | \(M_r(2)\le2r-1\) | PROVED for \(r\ge6\) | Complement argument + Andrásfai–Erdős–Sós; false for abstract contract at r=4,5 |
| A-H4 | \(M_r(3)\le3r\) | PROVED for \(r\ge6\) | Depends on A-H3, minimum-degree pivot, and exact integer comparison |
| A-H5 | \(M_r(4)\le4r\) | CONTEXTUAL ONLY | Available under the reductio assuming no induced \((4r+1)\) extraction residual; not an unconditional theorem |
| A-H6 | Five seed edge-floor excesses at \((2,2r-1),(3,3r-1),(3,3r),(4,4r-1),(4,4r)\) | OPEN for general r | r=12 values do not define all-r formulas |
| A-H7 | All admissible nonterminal outer states satisfy \(B_r(a,n)>U_r(d,j)\) for all sufficiently large r | OPEN | Requires a uniform seed envelope and exact integer checks |
| A-H8 | (r_0) for all-large-r EG617 | NOT PROVED | Do not infer from recurrence termination or the two new cutoffs |
| A-H9 | I local slack-gap theorem supplies an H seed floor | NOT ESTABLISHED | I theorem requires a full coloring neighborhood of size (r^2); H states are arbitrary induced residuals of order (ar+O(1)) |

## External theorem

Andrásfai–Erdős–Sós: a triangle-free graph on n vertices with minimum degree (>2n/5) is bipartite. Citation: B. Andrásfai, P. Erdős, V. T. Sós, “On the connection between chromatic number, maximal clique and minimal degree of a graph,” *Discrete Mathematics* 8 (1974), 205–218. The application here is exactly at (n=2r), degree (r-1>4r/5), valid for integer (r\ge6).

## Small-parameter warning

The abstract state contract admits examples in \(\mathcal C_4(2,8)\) and \(\mathcal C_5(2,10)\), so the desired (M_r(2)\le2r-1) cutoff is not an all-r consequence of this contract. These examples are not full EG617 colorings.