# E407 Q32 — target-excess transfer and B color-premium ledger

Date: 2026-10-27  
Status: **PROVED under the frozen V12 E407-Q32 shell/core contract, with the color-premium part additionally relative to the registered Brouwer/Kang–Pikhurko degree floors. Necessary structure only; E407 remains OPEN.**

## 1. Setup

Work in the retained E407 Q32 T61 state:

- `e(F)=407`, `|F|=61`, `delta(F)=13`;
- pivot `p` has target degree 13 and shell `A=N_F(p)`, `|A|=13`;
- `A=S dot-union B`, `|S|=3`, `|B|=10`;
- `B` is a target `K10`;
- core `H` has 47 vertices and `e(H)=284`;
- for `a in A`, `D_a=N_F(a) cap H`, `t_a=|D_a|`;
- for `b in B`, `k_b=|N_M(b) cap S|` and the frozen V12 equality is
  \[
  t_b=k_b\le3.
  \]

Put

\[
c:=e_M(S,B)=\sum_{b\in B}k_b,
\qquad
\beta:=e(M[S]).
\]

For A/B/C/D/E, respectively, `beta=0,0,1,1,2`.

The retained V12 Q32 color profile is

\[
129^7,130^4
\]

on the eleven non-target colors.

## 2. Every B vertex is a global target minimum-degree vertex

### Theorem 2.1

For every `b in B`,

\[
\boxed{d_F(b)=13.}\tag{2.1}
\]

### Proof

The target neighbors of `b` are:

- pivot `p`: one;
- the other nine B vertices: nine;
- S: exactly `3-k_b`;
- H: exactly `t_b=k_b`.

Therefore

\[
d_F(b)=1+9+(3-k_b)+k_b=13.
\]

QED.

Thus all ten B vertices, together with the pivot, sit exactly at the global minimum target degree.

## 3. Exact shell/core target-edge transfer

Because B is a target clique and `M[S]` has `beta` edges,

\[
e(F[A])=45+(30-c)+(3-\beta)=78-c-\beta.\tag{3.1}
\]

Using `e(F)=407`, `e(H)=284`, and the thirteen pivot-shell edges,

\[
\boxed{e_F(A,H)=32+c+\beta.}\tag{3.2}
\]

Since the B rows contribute exactly `sum_B t_b=c`,

\[
\boxed{\sum_{s\in S}t_s=32+\beta.}\tag{3.3}
\]

This recovers the five template S-row sums:

- A/B: 32;
- C/D: 33;
- E: 34.

For `s in S`, let

\[
q_s:=d_M(s,A)=d_M(s,B)+d_{M[S]}(s).
\]

Then

\[
d_F(s)=13+t_s-q_s.
\]

Summing over S, and noting `sum_S q_s=c+2beta`, gives the exact S-shell excess

\[
\boxed{\sum_{s\in S}(d_F(s)-13)=32-c-\beta.}\tag{3.4]
\]

(The closing bracket in (3.4) is typographical; the formula is the displayed equality.)

The total target excess in E407 is

\[
2\cdot407-13\cdot61=21.
\]

The pivot and all ten B vertices have zero excess by Theorem 2.1. Therefore the full-target excess carried by H is

\[
\boxed{\sum_{h\in H}(d_F(h)-13)=c+\beta-11.}\tag{3.5}
\]

Equivalently, writing `epsilon_h=d_H(h)-12` and `a_h=d_F(h,A)`,

\[
d_F(h)-13=\epsilon_h+a_h-1,
\]

and summing reproduces (3.5).

### Corollary 3.2 — exact-color shell load forces core excess

`EXACT_COLOR_SHELL_CROSS_LOAD.md` proves

\[
c\ge14-\beta.
\]

Hence

\[
\boxed{\sum_{h\in H}(d_F(h)-13)\ge3.}\tag{3.6}
\]

Using the stronger template high-row floors gives the safe template-specific lower bounds

| Template | safe `c` floor | `beta` | core full-target excess floor `c+beta-11` |
|---|---:|---:|---:|
| A | 18 | 0 | 7 |
| B | 16 | 0 | 5 |
| C | 18 | 1 | 8 |
| D | 14 | 1 | 4 |
| E | 12 | 2 | 3 |

For A/C these use only the already-audited `n_3>=6` floor; no stronger row optimization is needed here.

## 4. Large degree-13 sector in the core

Since every H vertex has full target degree at least13, each vertex of degree at least14 consumes at least one unit of (3.5). Therefore at least

\[
\boxed{58-c-\beta}\tag{4.1}
\]

vertices of H have full target degree exactly13.

The core-internal excess satisfies

\[
\sum_{h\in H}\epsilon_h=4,
\]

so at most four H vertices have positive `epsilon_h`. Consequently at least

\[
\boxed{54-c-\beta}\tag{4.2}
\]

H vertices satisfy simultaneously

\[
d_H(h)=12,\qquad d_F(h)=13.
\]

For every such vertex,

\[
\boxed{d_F(h,A)=1.}\tag{4.3}
\]

Indeed `12+d_F(h,A)=13` because h is not target-adjacent to p.

Since W has only 18 vertices, at least

\[
\boxed{36-c-\beta}\tag{4.4}
\]

points of U are core-regular and have exactly one target shell neighbor. This lower bound is always nonnegative in the five-template state because `c<=30` and `beta<=2`.

This provides a direct bridge from the 3-by-10 shell missing graph to pointwise structure inside the 29-point support design.

## 5. Exact per-B non-target color premium budget

Now invoke the registered non-target color degree floors:

- every 129-edge exact color has minimum degree at least4;
- every 130-edge color has minimum degree at least3.

Fix `b in B`. By Theorem 2.1 its target degree is13, so its total degree over the eleven non-target colors is

\[
60-13=47.
\]

For the V12 profile `129^7,130^4`, the minimum baseline is

\[
7\cdot4+4\cdot3=40.
\]

Hence every B vertex has the exact seven-unit premium ledger

\[
\boxed{
\sum_{c\in\mathcal C_{129}}(d_c(b)-4)
+
\sum_{j\in\mathcal C_{130}}(d_j(b)-3)
=7.
}\tag{5.1}
\]

Summing over all ten B vertices gives total B color premium exactly70.

If b is in one of the ten isolated K5 components of an exact-129 color, then `d_c(b)=4`, so that color spends zero premium at b. In particular every selected B anchor occurrence contributes zero exact-color premium at its anchor.

Thus the repeated selected-anchor multiplicities `m_b` from `ANCHOR_REPETITION_TRANSVERSAL_PACKING.md` identify exact colors in which the corresponding B point is forced onto the zero-premium cell of (5.1).

## 6. Two-B exceptional gadget costs positive B premium

Fix an exact-129 color c. Its factorization is ten isolated K5 components plus an 11-vertex exceptional gadget `G_c` with

\[
\alpha(C_c[G_c])=2.
\]

Suppose the gadget contains two B vertices `b_1,b_2`. Since B is a target clique, the edge `b_1b_2` is not color c. In the complement of the color-c gadget, `b_1b_2` is therefore an edge. The complement is triangle-free because the gadget has color independence number two.

For adjacent vertices in a triangle-free graph, their neighborhoods are disjoint. Hence in the 11-vertex complement gadget,

\[
d_{\overline C}(b_1)+d_{\overline C}(b_2)\le11.
\]

Their color-c gadget degrees therefore satisfy

\[
\boxed{d_c(b_1)+d_c(b_2)\ge9.}\tag{6.1}
\]

Relative to the exact-color baseline 4+4, every two-B gadget consumes at least one unit of the B-premium budget:

\[
\boxed{(d_c(b_1)-4)+(d_c(b_2)-4)\ge1.}\tag{6.2}
\]

This is a genuine factor/shell-color coupling. It is not by itself terminal because the total B premium budget is70.

## 7. Support-point consequence of the selected-B mass

Across the seven exact colors there are at least35 selected B-anchor blocks. Each such support block contains four U points, so the number of selected B-anchor point incidences is at least

\[
140.
\]

By pointwise anchor injectivity, a fixed `u in U` can lie in blocks with at most seven distinct B anchors. Let `q_B(u)` be the number of selected support blocks containing u whose anchor is in B. Then

\[
\sum_{u\in U}q_B(u)\ge140,\qquad q_B(u)\le7.
\]

If at most seven U points had `q_B(u)>=5`, the total would be at most

\[
7\cdot7+22\cdot4=137,
\]

contradiction. Therefore

\[
\boxed{|\{u\in U:q_B(u)\ge5\}|\ge8.}\tag{7.1}
\]

Thus at least eight support points simultaneously carry selected exact-color incidences to at least five distinct B anchors.

## 8. Dependency firewall and scope

Sections 2–4 use only the frozen V12 E407 target-shell/core equalities, including `t_b=k_b`, the target minimum-degree 13 contract, and the already-proved exact-color shell cross-load.

Section 5 additionally uses the registered Brouwer/Kang–Pikhurko non-target degree floors. Section 6 uses the exact-129 factor theorem and the exceptional gadget independence-two property. Section 7 uses the selected support-component identity and anchor injectivity.

No Didin-dependent delta=14 saturated argument is used.

The new information is a same-state upper/lower join:

- shell missing mass `c` determines exactly how the 21 units of target excess split between S and H;
- every B point has exactly seven units of non-target color degree premium;
- repeated selected B anchors occupy zero-premium exact-color cells;
- two-B gadgets force positive premium;
- at least eight U points see five or more distinct selected B anchors.

These constraints do not yet exclude any of templates A–E. The remaining task is to combine them with the 49-block omission system / W-side slack or to prove a sharper exact-factor premium bound.