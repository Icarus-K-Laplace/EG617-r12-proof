# Shortest Route to an Unconditional All-Large-r Theorem

**Status:** CONDITIONAL_ROUTE_CERTIFIED; UNCONDITIONAL P(r0) NOT CERTIFIED

Updated: 2026-10-24  
Branch: workstream/general-r-asymptotic-20261024

## 1. Main synthesis decision

The shortest currently evidenced route is **not** the old backend composition A_ext + C* + D. It bypasses the scalable d2 endpoint closure C* entirely and instead pushes the front-end 5r+1 terminal directly into a bounded-offset near-anchor problem.

The new conditional theorem is:

> **Theorem S67-low.** For every r ≥ 67, if A_ext*(r) and D_low(r) hold, then P(r) holds.

Here A_ext* must deliver one of the following, with the exact contextual assumptions below:
1. a legal induced 4r+1 residual F4, with alpha(F4) ≤ 4, omega(F4) ≤ r−1, and the inherited full-colour cap; or
2. the anchored 5r+1 terminal T, with alpha(T)=5, omega(T) ≤ r−1, delta(T) ≥ r, the inherited contextual full-colour cap, and the no-4r+1-extraction condition.

D_low is the remaining terminal nonextension theorem for the direct near-anchor outputs whose common target anti-neighbourhood W has the size windows in §3. This is a **weaker target than robustly classifying every design-like terminal**.

Neither A_ext* nor D_low is proved. Thus S67-low is a conditional synthesis theorem, not an unconditional solution.

## 2. Proof of S67-low from imported theorems

Assume r ≥ 67 and a hypothetical counterexample.

### Branch R: a 4r+1 residual

The residual-branch theorem gives delta(F4)=r+1 for every r ≥ 17. The contextual (k,s)=(4,1) cap is
\[
e(F_4) \le U_{4,1}(r)=2r^2+r+7.
\]
But
\[
e(F_4)\ge\frac{(4r+1)(r+1)}2,
\qquad
\frac{(4r+1)(r+1)}2-U_{4,1}(r)=\frac{3r-13}{2}>0
\]
for r ≥ 5. This branch is impossible.

### Branch T: an anchored 5r+1 terminal

The contextual cap is
\[
e(T)\le U_{5,1}(r)=\frac{5r^2+7r+18}{2}.
\]
Since delta(T) ≥ r, if delta(T) ≥ r+2 then
\[
e(T)\ge\frac{(5r+1)(r+2)}2,
\qquad
\frac{(5r+1)(r+2)}2-U_{5,1}(r)=2r-8>0
\]
for r ≥ 5. Hence delta(T) is either r or r+1.

The direct near-anchor extraction theorem gives, for r ≥ 67:

- if delta(T)=r, an independent triple with degree pattern (r, ≤r+1, ≤r+1);
- if delta(T)=r+1, an independent triple with degree pattern (r+1, ≤r+2, ≤r+2).

The common-antineighbourhood compression theorem gives the initial windows:
\[
2r-4\le |W|\le2r+1
\quad(\delta(T)=r),
\]
\[
2r-7\le |W|\le2r+1
\quad(\delta(T)=r+1).
\]
It eliminates |W|=2r and 2r+1 for r ≥ 11.

For the **high-minimum-degree branch** delta(T)=r+1, the imported Cell B and Cell A nonextension theorems eliminate |W|=2r−1 for r ≥ 25.

For the **low-minimum-degree branch** delta(T)=r, the new LOW_DEGREE_TOP_LAYER_CLOSURE.md theorem also eliminates |W|=2r−1 for r ≥ 25. It uses the W-local Cell A/B pointwise target-degree bound, proves alpha(F[V\W])≤3, and then derives an anchor-incidence contradiction: the unique-anchor neighbourhoods would be target cliques, but the duplicate-incidence budget is at most three.

Thus the remaining terminal interface is finite-width:
- delta(T)=r: 2r−4 ≤ |W| ≤ 2r−2;
- delta(T)=r+1: 2r−7 ≤ |W| ≤ 2r−2.

If D_low excludes these remaining configurations, Branch T is impossible. This proves S67-low.

## 3. Exact remaining downstream contract

The low-layer theorem must cover these cases, with all inherited colour and embedding constraints retained:

| Anchor minimum degree | Required near-anchor triple | Remaining |W| values |
|---|---|---|
| delta(T)=r | (r, ≤r+1, ≤r+1) | 2r−4, 2r−3, 2r−2 |
| delta(T)=r+1 | (r+1, ≤r+2, ≤r+2) | 2r−7, …, 2r−2 |

The Cell A/B edge-count exclusions use delta(T)=r+1, but the new LOW_DEGREE_TOP_LAYER_CLOSURE.md proof independently excludes the low-degree delta(T)=r, |W|=2r−1 case for r ≥ 25. The remaining D_low windows therefore have |W|≤2r−2 in both anchor-degree branches.

## 4. Imported source ledger

All imports retain their original contracts; no statement is promoted beyond its hypotheses.

- **Residual branch contract:** general_r/workstreams/residual-core-extraction-chat-20261024/RESIDUAL_BRANCH_CLOSURE.md; theorem recorded at commit 07cd8fb58ffd93d234b1e8b6104f939175d7fbda; current source branch head 7a4fb4c37cefec8d801fc7deb778568bfb24002e.
- **Contextual (k,s) cap:** general_r/GENERAL_R_KS_CONTEXTUAL_CAP_PLANE.md; current architecture branch head a922c4d7646eb8d0087bde8547562c8aace02ee2.
- **5r+1 direct near-anchor extraction:** general_r/GENERAL_R_5R1_ALL_LARGE_R_ANCHOR_EXTRACTION.md, relative to Liu–Ren–Wang 2025; r ≥ 67 (classical AES fallback r ≥ 71); architecture branch head a922c4d7646eb8d0087bde8547562c8aace02ee2.
- **Common anti-neighbourhood compression:** general_r/GENERAL_R_NEAR_ANCHOR_COMMON_ANTINEIGHBORHOOD.md; same architecture branch.
- **Cell B high-layer exclusion:** general_r/GENERAL_R_CELL_B_HIGH_LAYER_FULL_EXCLUSION_R16.md, r ≥ 16, relative to Brouwer second-Turán and the stated Cell-B normal form.
- **Cell A high-layer exclusion:** general_r/GENERAL_R_CELL_A_HIGH_LAYER_FULL_EXCLUSION_R25.md, r ≥ 25, relative to the sharp non-bipartite triangle-free extremal theorem and Brouwer second-Turán, under the stated Cell-A normal form.
- **Low-degree top-layer closure:** LOW_DEGREE_TOP_LAYER_CLOSURE.md, commit 301dcacab800fd95b7a750042ba92143cf0f2c5f; this closes delta(T)=r, |W|=2r−1 using the exact Cell A/B local certificates and the duplicate-anchor-incidence budget.
- **Current D terminal contract:** design-terminal branch head 5b4162c239d3dfad84d130c3015a0db5919228c4; the global defect-chain propagation remains OPEN.
- **Current C endpoint contract:** repivot branch head 35fec3eaaab70b31e10b41065634b35b02a28e6c; clean-pair nonextension remains OPEN.

## 5. What this route removes—and what it does not

This route **does not require**:
- the exact three-anchor floor K ≥ 8 as a separate asymptotic hypothesis;
- the global residual endpoint theorem C*, including scalable d2 closure;
- a robust classification of every 5r+1 terminal.

It **still requires**:
1. A_ext*: force the contextual 4r+1 / 5r+1 dichotomy;
2. D_low: exclude the finite-offset near-anchor terminal family above.

No unconditional r0 has been certified.


## Round 3 — forced hub

The low-offset family is now reduced to one structural condition: every surviving terminal has some h outside T union W with d_F(h,W)>=floor((r-j)/4)+1. This is proved by the exact duplicate-anchor incidence count. The next missing theorem is to exclude this hub under full colour ownership; D_low and A_ext* remain OPEN. No unconditional r0 is certified.
