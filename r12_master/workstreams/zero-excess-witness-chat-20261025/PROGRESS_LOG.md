# Progress log — R12 zero-excess witness workstream

## 2026-10-25 — Round 1: robust zero-excess witnesses

### Repository intake

Read-only intake from \`workstream/r12-emergency-sprint-20261024\` and \`workstream/r12-ultimate-closure-20261024\` confirmed the headline theorem remains OPEN / NOT_CERTIFIED. The live T61 front-end bottlenecks are E407 Q32 and E408 Q32/Q33; the shared interface identifies the 47-point, 284-edge core as the common case for E407 Q32 and E408 Q33, while E408 Q32 has 285 core edges. Existing witness-capacity files explicitly leave labelled witness packing open.

This workstream was isolated on branch \`workstream/r12-zero-excess-witness-20261025\`, based on the read-only sprint HEAD \`5258c5fe17af3bf17eb7a2bfb08315c9be9116cd\`. No sibling path was modified.

### New analytic result

Added \`R12_ZERO_EXCESS_WITNESS_THEOREM.md\`.

For \(H\) on 47 vertices with \(\alpha(H)\le4\), \(\delta(H)\ge12\), and \(e(H)\in\{284,285\}\), delete all vertices of positive degree excess to obtain \(H_0\). A Turán comparison proves:
- \(e(H)=284\): \(\alpha(H_0-T)=4\) for every \(|T|\le6\);
- \(e(H)=285\): \(\alpha(H_0-T)=4\) for every \(|T|\le4\).

The proof gives the exact upper bound
\[
e(H_0-T)\le282-\frac E2-12k+\binom{k}{2}-t(12-k)+\binom t2,
\]
where \(E=2e(H)-564\), \(k\) is the number of positive-excess vertices, \(t=|T|\), and \(n=47-k-t\). If \(\alpha(H_0-T)\le3\), Turán's theorem forces \(e(H_0-T)\ge p_3(n)\). The minimum endpoint gaps are 5 for the 284-edge case and 6 for the 285-edge case, so all allowed cases contradict.

The arithmetic table was exhaustively checked over all \(k,t\) in the stated finite ranges. The proof itself is analytic and does not rely on the table as a substitute for the Turán argument.

### Derived applications

1. Any shell row with \(t_b\le3\) has a target-independent four-set \(Q_b\subseteq H_0\) anticomplete to it.
2. In the 284-edge core, any two such regular rows have a common independent-four witness because the union of their core neighborhoods has size at most six.
3. Under the retained exact-129 factor theorem, the ten isolated K5 components in an exact-129 color include at least five components \(\{b\}\cup Q\) with \(b\in B\), \(Q\subseteq H\), and no \(S\)-vertex. Since the 284-edge core has at most four positive-excess vertices and the five components are disjoint within a color, at least one such \(Q\) has all four vertices of degree 12 in \(H\).
4. E407 has non-target residual excess four, hence at least seven exact-129 colors; E408 Q33 has excess three, hence at least eight. Conditional on the retained factor theorem, this gives at least seven/eight zero-excess colored witnesses, respectively.

### Audit boundaries

- **PROVED_ANALYTIC:** robust zero-excess independent-four theorem for 284/285 cores.
- **PROVED_ANALYTIC:** common zero-excess witness for any pair of \(t_b,t_c\le3\) rows in a 284-edge core.
- **PROVED_CONDITIONAL:** at least one zero-excess no-S K5 component per exact-129 color for the 284-edge E407 Q32 and E408 Q33 cases.
- **OPEN:** no E407 Q32 or E408 Q32/Q33 terminal is eliminated.
- **OPEN:** labelled overlap/capacity theorem; actual color-component witnesses cannot be replaced by arbitrary graph-theoretic witnesses without proof.
- **OPEN:** full EG617(r=12).

### Commit log

- \`R12_ZERO_EXCESS_WITNESS_THEOREM.md\`: \`e02fc41103d43e06edd040b93d39bb7dba783510\`.
- \`CANONICAL_STATE.md\`: \`2a3c4a604d7f66daf5fbe31af1fb9500ef56519b\`.


## 2026-10-25 — Round 2: witness-overlap edge-load audit

Added \`R12_WITNESS_OVERLAP_CAPACITY.md\`.

For any family \(\mathcal Q\) of independent 4-sets in \(H\) with pairwise intersections at most one, every pair \(Q,Q'\) has at least three H-edges between \(Q\setminus Q'\) and \(Q'\setminus Q\). If \(r_x\) is the number of selected witness sets containing \(x\), exact double-counting gives
\[
\sum_{\{Q,Q'\}\subseteq\mathcal Q}e_H(Q\setminus Q',Q'\setminus Q)
=\sum_{xy\in E(H)}r_xr_y
\ge3\binom{|\mathcal Q|}{2}.
\]

For five no-S K5 witnesses from each of \(c\) exact-129 colors, \(|\mathcal Q|=5c\), \(r_x\le c\), \(\sum_xr_x=20c\), and \(\sum_x\epsilon(x)=4\). The exact scalar upper bound is
\[
\sum_{xy\in E(H)}r_xr_y
\le\frac12\sum_x(12+\epsilon(x))r_x^2
\le122c^2.
\]
At \(c=7\), this is \(5978\) versus lower bound \(1785\); at \(c=8\), it is \(7808\) versus lower bound \(2340\). Thus the pairwise-crossing inequality does not close the terminals. The arithmetic was corrected and checked; no contradiction is claimed.

This records a valid reusable incidence identity and a clear failed scalar route. The remaining blocker is a labelled overlap bound that uses each witness's shell-row hit pattern and the actual 284-edge core, rather than only the total number of memberships and degree excess.

Commits:
- \`R12_WITNESS_OVERLAP_CAPACITY.md\` (initial): \`c49e9b83a4888ae8573e3657af90687f5e7c7459\`.
- \`R12_WITNESS_OVERLAP_CAPACITY.md\` (corrected arithmetic): \`21a11a95de35cba62f45c07409e58b3f88cbb482\`.

