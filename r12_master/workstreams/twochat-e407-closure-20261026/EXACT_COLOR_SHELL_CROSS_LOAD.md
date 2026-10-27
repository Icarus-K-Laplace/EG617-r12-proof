# E407 Q32 — exact-color shell cross-load and the b=5 hub theorem

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL on the frozen exact-129 factor/selected-component contract. Necessary structure only; E407 remains OPEN.**

## 1. Setup

Use the current E407 Q32 shell notation

\[
A=S\dot\cup B,\qquad |S|=3,\quad |B|=10,
\]

with `B` a target `K10`, pivot `p` target-adjacent to every shell vertex, and

\[
M=\overline{F[A]}.
\]

There are seven exact-129 non-target colors. By `SHELL_COLOR_EDGE_LOAD.md`, each exact color has at least two color edges entirely inside the shell `A`.

Write

\[
\beta:=e(M[S]).
\]

For the five retained templates,

\[
\beta(A)=\beta(B)=0,\qquad
\beta(C)=\beta(D)=1,\qquad
\beta(E)=2.
\]

Because `B` is a target clique, `M[B]` is empty. Hence every non-target shell edge has type `S-B` or `S-S`.

## 2. Universal cross-load theorem

### Theorem 2.1

Across the seven exact-129 colors, at least

\[
\boxed{14-\beta}
\]

distinct `S-B` shell edges receive one of the exact colors. Consequently

\[
\boxed{e_M(S,B)=\sum_{b\in B}k_b\ge14-\beta.}\tag{2.1}
\]

### Proof

Each of the seven exact colors contributes at least two shell edges, hence there are at least fourteen exact-color shell-edge incidences. A physical shell edge has only one color, so these fourteen edges are distinct across the seven exact colors.

There are no non-target `B-B` shell edges because `B` is a target `K10`. Therefore every one of these exact-color shell edges is either `S-B` or `S-S`. Only the `\beta` physical edges of `M[S]` are available for the latter type. Hence at least `14-\beta` of the fourteen distinct exact-color edges are `S-B` edges. Every exact-colored non-target edge belongs to `M`, so (2.1) follows. QED.

### Corollary 2.2 — template floors

| Template | `beta` | forced distinct exact-colored `S-B` edges | resulting `e_M(S,B)` floor |
|---|---:|---:|---:|
| A | 0 | at least 14 | at least 14 |
| B | 0 | at least 14 | at least 14 |
| C | 1 | at least 13 | at least 13 |
| D | 1 | at least 13 | at least 13 |
| E | 2 | at least 12 | at least 12 |

The row-type screens for A-D can be stronger numerically. The new point is that the weakest template E also satisfies the exact-color-driven lower bound `e_M(S,B)>=12`; this does not come from the previous `h>=5` high-row floor alone.

## 3. Sharp residual-hub structure when `b_c=5`

Fix an exact color `c` and let `b_c` be the number of its seven selected support components whose outside-core anchor is in `B`.

By `SELECTED_B_ANCHOR_FLOOR.md`, if

\[
b_c=5,
\]

then the selected anchors are exactly

\[
\{p,s_c\}\cup B_c,
\qquad s_c\in S,\quad |B_c|=5.
\]

Thus the two hubs in

\[
S\setminus\{s_c\}
\]

are residual vertices. The three unselected isolated color-`c` `K5` components each contain a `B` vertex, and the exceptional 11-vertex gadget contains exactly two `B` vertices and has color-`c` independence number two.

### Theorem 3.1 — every residual hub sees residual B in color c

Let `s in S\{s_c}`. Then there exists an unselected `b in B` such that

\[
\boxed{sb\text{ has color }c.}\tag{3.1}
\]

### Proof

The residual vertex `s` lies either in one of the three unselected isolated `K5` components or in the exceptional gadget.

**Case 1: `s` lies in an unselected K5.**  Every one of the three unselected K5 components contains a B vertex. Let that vertex be `b`. Since the component is monochromatic color `c`, the edge `sb` has color `c`.

**Case 2: `s` lies in the exceptional gadget.**  The gadget contains exactly two B vertices, say `b_1,b_2`. Because B is a target clique, the edge `b_1b_2` does not have color `c`; hence `b_1,b_2` are nonadjacent in the color-`c` gadget graph. If `s` were color-`c` nonadjacent to both, then `s,b_1,b_2` would be an independent triple in the exceptional gadget, contradicting its color-`c` independence number two. Thus `s` has a color-`c` edge to at least one of `b_1,b_2`.

In both cases the B endpoint is residual/unselected, because every selected isolated component is disjoint from the residual factor. QED.

### Corollary 3.2

Every exact color with `b_c=5` contributes at least **two distinct exact-colored S-B shell edges**, one incident to each of its two unselected hubs.

These two physical edges are distinct because they have different S endpoints. Edges contributed by different exact colors are also distinct by edge-color uniqueness.

## 4. Global localization of b=5 colors

Let

\[
n_5:=|\{c:b_c=5\}|.
\]

For `s in S`, let

\[
\lambda_s:=|\{c:b_c=5\text{ and }s_c=s\}|.
\]

Every `b_c=5` color selects exactly one S anchor, so

\[
\boxed{\sum_{s\in S}\lambda_s=n_5.}\tag{4.1}
\]

For a fixed hub `s`, it is residual in exactly `n_5-\lambda_s` of the `b=5` colors. Theorem 3.1 supplies a distinct exact-colored `S-B` edge incident to `s` in every such color. Therefore

\[
\boxed{d_M(s,B)\ge n_5-\lambda_s.}\tag{4.2}
\]

Summing over all three hubs and using (4.1),

\[
\boxed{e_M(S,B)\ge2n_5.}\tag{4.3}
\]

This lower bound is independent of Theorem 2.1 and can dominate it if many exact colors have `b_c=5`.

## 5. Coupling to repeated-anchor capacity

`ANCHOR_REPETITION_TRANSVERSAL_PACKING.md` proves that for any missing shell pair `sb`, repeated selected S-anchor multiplicity satisfies

\[
m_s\le k_b.
\]

Since `lambda_s<=m_s`, any B row missing to `s` gives

\[
\boxed{\lambda_s\le m_s\le k_b.}\tag{5.1}
\]

Combining with (4.2), if `s` has a missing B-row of size `k`, then

\[
\boxed{d_M(s,B)\ge n_5-k.}\tag{5.2}
\]

In particular:

- a missing `k=1` row gives `d_M(s,B)>=n_5-1`;
- a missing `k=2` row gives `d_M(s,B)>=n_5-2`;
- in A/C, the full-row structure gives the universal `m_s<=3`, hence `d_M(s,B)>=n_5-3` for every hub.

These are exact-color / selected-anchor compatibility inequalities on the same shell. They are not yet contradictions because the present template summaries do not fix the per-hub `S-B` degree vector sharply enough in every survivor.

## 6. Dependency audit and scope

Theorem 2.1 uses:

1. seven exact-129 colors;
2. the proved conditional per-color shell-edge floor `|E_c(A)|>=2` from `SHELL_COLOR_EDGE_LOAD.md`;
3. B being a target `K10`;
4. ordinary edge-color uniqueness.

Theorem 3.1 additionally uses the exact-129 factor placement theorem at `b_c=5`:

- three residual isolated K5 components each carrying one B vertex;
- two B vertices in the exceptional gadget;
- color independence number two for that gadget.

No Didin-dependent delta=14 saturated result is used. No low-delta classification is used.

This note strengthens the five-template global shell interface, especially Template E, and localizes every `b_c=5` color onto two residual hub-to-B edges. It does **not** exclude any template by itself and does not close E407 Q32 or the original K145 bridge.
