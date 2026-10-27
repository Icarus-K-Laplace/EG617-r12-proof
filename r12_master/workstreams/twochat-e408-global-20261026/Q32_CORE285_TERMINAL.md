# E408 Q32 — independent 285-edge terminal

Updated: 2026-10-27  
Status: **PROVED_CONDITIONAL impossible under the registered E408/Q32 residual contract.**

## 1. Frozen Q32 contract

\[
|V(H)|=47,\quad e(H)=285,\quad \alpha(H)\le4,\quad\delta(H)\ge12,
\quad\sum_{x\in H}(d_H(x)-12)=6.
\]
The shell parameter is \(q=32\), equivalently \(e(M)+G_A=32\). The outer equality system gives eleven non-target colors with
\[
e_C(R)=129+s_C,\qquad s_C\ge0,\qquad\sum_Cs_C=3,
\]
so the number m of exact-129 colors is in \(\{8,9,10\}\).

No Q33 284-edge identity is imported.

## 2. Earlier support reductions remain valid but are no longer load-bearing

The read-only Q32 sibling workstream proves \(|U|\ge44\) for the union U of exact-color single-outside K5 core witnesses. This branch then proved:

- global exceptional-vertex injectivity;
- v=44 impossible;
- the uniform nonfull-support theorem \(U=H\), excluding v=44,45,46 at once.

These results remain valid audits. However, the stronger theorem `Q32_EXACT_COLOR_COUNT_COLLAPSE.md` now contradicts the E408 Q32 residual before any support-size case split is needed.

## 3. Load-bearing exact-color-count contradiction

`Q32_EXACT_COLOR_COUNT_COLLAPSE.md` proves all three possible values of m impossible.

### 3.1 Low-degree structure

Using the full-color pointwise degree floors and the Brouwer--Kang--Pikhurko second-Turan theorem:

1. A 131-edge non-target color has minimum degree at least three.
2. In a 130-edge non-target color, every degree-three vertex lies in an isolated K4 component.
3. A 130-edge non-target color has at most one such isolated K4, hence at most four degree-three vertices. Two isolated K4s would leave a 53-vertex, 118-edge graph with alpha<=10 and omega<=5, while the Brouwer lower bound is 119.
4. In a 132-edge non-target color, every degree-two vertex lies in an isolated K3 component. Four such triangles would leave a 49-vertex, 120-edge graph with alpha<=8, below the elementary Turan floor p_8(49)=126. Thus there are at most nine degree-two vertices.

### 3.2 m=10

There is one nonexact color, with 132 edges. At each of the ten distinct exact exceptional vertices, target degree >=13, own exact degree 9, and the other nine exact degrees >=4 force the nonexact degree to be exactly two. This gives at least ten degree-two vertices, but the 132-edge lemma permits at most nine. Contradiction.

### 3.3 m=9

The two nonexact colors have 130 and 131 edges. At each of the nine distinct exact exceptional vertices their degree sum is at most six. Both have minimum degree at least three, so both equal three. The 130-edge color would therefore have at least nine degree-three vertices, but it can have at most four. Contradiction.

### 3.4 m=8

The three nonexact colors all have 130 edges. At each of the eight distinct exact exceptional vertices their three degrees sum to at most ten. Since each is at least three, at least two colors have degree exactly three there. Hence the eight exceptional vertices demand at least 16 degree-three incidences across the three 130-edge colors. Each color has at most four, so the total capacity is at most 12. Contradiction.

Therefore
\[
\boxed{m\notin\{8,9,10\}},
\]
contradicting the outer equality system. Hence
\[
\boxed{\text{E408 Q32 is impossible under the registered contract}.}
\]

## 4. Verification

Proof: `Q32_EXACT_COLOR_COUNT_COLLAPSE.md`.  
Arithmetic regression: `verify_q32_exact_color_count_collapse.py`.

The verifier checks all Turan numbers and local degree-budget arithmetic used in the proof. It is not a substitute for the analytic Brouwer theorem.

## 5. Dependency firewall

Load-bearing inputs:

- E408 residual excess ledger \(\sum s_C=3\);
- exact-129 Type-I degree structure;
- `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md`;
- the independent full-color pointwise degree floors;
- alpha(C)<=12 and omega(C)<=5 for non-target residual colors;
- Brouwer / Kang--Pikhurko non-r-partite Turan theorem;
- target minimum degree 13 and the 12-color degree partition at every residual vertex.

Not used:

- Q33's 284-edge core;
- the support-41 theorem;
- a specific M[B]=empty shell split;
- speculative SAT/ILP output;
- the older v=47 edge-surplus heuristic.

## 6. Global scope

This file closes the **registered E408 Q32 terminal**, not the original K145 theorem. The Q33 terminal is separately conditionally excluded by `Q33_NONEXACT_U_RESERVE_CLOSURE.md`. Upstream reduction and other E407/backend obligations retain their sibling statuses. EG617(r=12) remains **OPEN / NOT_CERTIFIED**.