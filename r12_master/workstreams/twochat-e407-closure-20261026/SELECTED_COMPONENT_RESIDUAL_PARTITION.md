# E407 Q32 — selected-component residual partition in each exact-129 color

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL on the frozen exact-129 factor theorem and selected-support-component identity. Necessary structure only.**

## 1. Setup

Fix one exact-129 non-target color c. The factor theorem partitions all 61 vertices into

- ten pairwise-disjoint isolated color-c K5 components; and
- one 11-vertex exceptional gadget.

The minimum-support boundary selects seven of the ten K5 components. By `SUPPORT_BLOCK_ANCHOR_IDENTITY.md`, their vertex sets are

\[
Q_{c,j}\cup\{a_{c,j}\},\qquad j=1,\ldots,7,
\]

where

- \(Q_{c,j}\subset U\), \(|Q_{c,j}|=4\);
- the seven Q-blocks are pairwise disjoint and cover exactly 28 of the 29 U-points;
- the seven anchors \(a_{c,j}\in\{p\}\cup A\) are pairwise distinct.

Let \(u_c\) be the unique U-point omitted by the seven selected support blocks, and let

\[
A_c^{\rm sel}=\{a_{c,1},\ldots,a_{c,7}\}\subseteq\{p\}\cup A.
\]

## 2. Exact 26-vertex residual

The seven selected K5 components cover exactly

\[
28+7=35
\]

vertices. Hence their complement has 26 vertices. Since

\[
V(F)=U\dot\cup W\dot\cup A\dot\cup\{p\},
\]

that complement is exactly

\[
\boxed{
R_c=\{u_c\}\dot\cup W\dot\cup
\bigl((\{p\}\cup A)\setminus A_c^{\rm sel}\bigr).
} \tag{2.1}
\]

The outside-core term has size seven. Thus

\[
|R_c|=1+18+7=26.
\]

By the exact-129 factor theorem, \(R_c\) is also exactly the disjoint union of

\[
\boxed{3K_5\ \dot\cup\ G_{11}}, \tag{2.2}
\]

where \(G_{11}\) is the 11-vertex exceptional gadget.

This is an exact per-color identity: the omitted support point, all eighteen W-points, and the seven unused outside-core labels are precisely the vertices of the three unselected K5 components plus the gadget.

## 3. Residual B-labelled component floor

Let

\[
b_c=|A_c^{\rm sel}\cap B|.
\]

The anchor theorem gives \(b_c\ge3\).

The corrected exact-129 component-packing theorem gives at least six B-labelled, no-S K5 components among all ten K5 components of color c. Every selected component with B-anchor is one of these. Therefore among the three **unselected** K5 components there are at least

\[
\boxed{m_c:=\max(0,6-b_c)} \tag{3.1}
\]

B-labelled, no-S components.

Each such unselected component has the form

\[
\{b\}\cup X,\qquad b\in B,\quad X\subset H,\quad |X|=4,
\]

with X target-independent in H. Because the component is unselected, its H-four-set X is disjoint from the 28 selected U-points. Hence

\[
X\subseteq W\cup\{u_c\}. \tag{3.2}
\]

Across the \(m_c\) residual B-components, at most one H-vertex can be \(u_c\). Consequently these components contain at least

\[
\boxed{4m_c-1} \tag{3.3}
\]

W-points in total.

Explicitly:

| selected B anchors \(b_c\) | residual B-components \(m_c\) | W-points forced in them |
|---:|---:|---:|
| 3 | 3 | at least 11 |
| 4 | at least 2 | at least 7 |
| 5 | at least 1 | at least 3 |
| 6 or 7 | no positive floor | 0 |

The W-points lying in one residual B-component form a target-independent set, of size three or four whenever that component contains at least three W-points.

## 4. Sharp structure when \(b_c=3\)

If \(b_c=3\), then the seven selected anchors consist of exactly

\[
\{p\}\cup S\cup B_c,\qquad |B_c|=3,
\]

because all four non-B labels must be selected.

All three unselected K5 components are B-labelled no-S components. Their H-four-sets are pairwise disjoint and lie in \(W\cup\{u_c\}\). Hence the three W-intersections have sizes either

\[
(4,4,4)
\]

if the omitted point \(u_c\) lies in the exceptional gadget, or

\[
(4,4,3)
\]

up to permutation if \(u_c\) lies in one of the three residual K5 components.

Thus:

\[
\boxed{
 b_c=3\Longrightarrow
 H[W]\text{ contains three pairwise-disjoint target-independent sets of sizes }
 (4,4,4)\text{ or }(4,4,3).
} \tag{4.1}
\]

In the second case the three sets use 11 W-points; in the first they use 12.

## 5. Shell-row consequence when \(b_c=3\)

Let \(Q_s^c\) be the selected support block anchored at \(s\in S\). These three blocks are pairwise disjoint.

For any \(b\in B\) with \(k_b>0\), and for every \(s\in N_M(b)\cap S\), the row-transversal theorem gives

\[
Q_s^c\cap D_b\ne\varnothing.
\]

The \(k_b\) relevant S-anchored blocks are disjoint, while

\[
|D_b|=t_b=k_b.
\]

Therefore equality is forced:

\[
\boxed{
D_b\subset U,\qquad
|D_b\cap Q_s^c|=1
\text{ for each }s\in N_M(b)\cap S,
} \tag{5.1}
\]

and \(D_b\) contains no other point.

Hence a single exact color with \(b_c=3\) implies

\[
oxed{N_F(B)\cap W=\varnothing.} \tag{5.2}
\]

That is, no B-shell vertex has a target neighbour in W.

Moreover, if there are \(r\) exact colors with \(b_c=3\), then for any fixed missing edge sb with \(b\in B\), the \(r\) blocks \(Q_s^c\) are pairwise disjoint across those colors (otherwise the edge from s to a shared core point would have two non-target colors). Since each must meet \(D_b\),

\[
\boxed{r\le |D_b|=k_b.} \tag{5.3}
\]

Thus the number of exact colors with \(b_c=3\) is bounded by the minimum positive B-row size in the shell template.

Examples:
- if a template contains a \(k=1\) B-row, at most one exact color can have \(b_c=3\);
- if all positive B-rows have size at least two but some has size two, at most two such colors occur;
- in a pure \(k=3\) positive-row state, at most three occur.

## 6. Consequence for global selected-B anchor count

Let r be the number of exact-129 colors with \(b_c=3\). Every other exact color has \(b_c\ge4\), so across the seven exact colors

\[
\sum_c b_c\ge3r+4(7-r)=28-r. \tag{6.1}
\]

Together with (5.3), any template with a positive B-row of size k satisfies

\[
\boxed{\sum_c b_c\ge28-k.} \tag{6.2}
\]

Thus a k=1 row gives at least 27 selected B-anchor occurrences, and a k=2 row gives at least 26.

This is a global labelled-incidence restriction on the actual 49 support blocks, not on the larger family of all exact-129 component witnesses.

## 7. Scope

This theorem does not show that \(b_c=3\) occurs. It gives an exact residual-factor structure if it does, and quantitative lower bounds when \(b_c=4,5\).

The key new bridge is that selected-anchor data now constrain both sides simultaneously:

- the unselected exact-129 factor components inside \(W\cup\{u_c\}\);
- the shell B-row supports \(D_b\);
- and the 49-block support system itself.

No five-template contradiction or original K145 proof is claimed here.
