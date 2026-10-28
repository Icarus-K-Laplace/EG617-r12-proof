# E408 Q32 — v=44, m=9 shell-edge floor from the corrected Type-I gadget

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL** under the registered Q32 / Type-I / v=44,m=9 equality contract.

## 1. Starting point

By `Q32_CORRECTED_NONFULL_SUPPORT_MULTIPLICITY.md`, when |U|=44 and m=9:

- W=H\U has three vertices;
- every exact color has its Type-I special vertex x_C in W;
- each w in W is x_C for exactly three exact colors;
- every exact color is either double type (two double-shell K5s) or triple type (one triple-shell K5);
- the number t of triple-type exact colors satisfies t<=1.

A double-type exact color contributes two internal shell edges to M; a triple-type exact color contributes the three edges of one shell triangle. These base shell edges are color-distinct across exact colors.

Thus the base exact-color contribution to M is

\[
2(9-t)+3t=18+t.
\]

The two nonexact colors have edge counts 130 and131. Since every non-target color has independence number at most12, its restriction to O={p} union A, |O|=14, contains at least p_12(14)=2 edges. The thirteen p-A edges are target edges, so these two edges must lie in M[A]. Hence the two nonexact colors contribute at least four further shell edges, distinct from all exact-color shell edges.

## 2. Zero-shell-neighbor tradeoff for the Type-I special vertex

Fix an exact color C and write its source-verified Type-I gadget with special 5-parts N_s,N_t, distinguished y in N_t, nonempty proper subset P subset N_s, and special vertex x=x_C.

In the original color graph C:

- x is adjacent to N_s\P and N_t\{y};
- y is adjacent to every vertex of P;
- every one of the two 5-parts is a color K5;
- both 5-parts must meet O, because a color K5 wholly inside H would be an H-independent 5-set.

### Lemma 2.1

Assume x=w is in H and has no color-C neighbor in the shell A. Then at least one of the following holds:

1. pw is a color-C edge; or
2. C contains a shell-shell edge joining y to a vertex of P.

The edge in alternative 2 is an additional M-edge between the two special K5 parts, hence is different from every base shell edge internal to a multi-outside K5.

### Proof

Each special K5 must contain an outside-H vertex.

To avoid an A-neighbor of x, a shell vertex chosen outside H in N_s must lie in P, and a shell vertex chosen outside H in N_t must be y. If both are shell vertices, the source construction gives the color-C edge yP, proving alternative 2.

The only way to avoid that shell-shell edge is to use p as the outside vertex in one special part. Since p is target-adjacent to every shell vertex, p cannot occupy a role that is color-adjacent to the shell outside vertex in the other special part. The surviving placement puts p in an x-neighbor role, giving the color-C edge px=pw. Thus alternative 1 holds. QED.

For a fixed w, the edge pw has one unique color. Hence among any k exact colors for which x_C=w and w has zero shell neighbors in color C, at least k-1 of them contribute an additional shell-shell edge of type 2. These additional edges are distinct across colors by edge-color uniqueness.

## 3. The t=0 floor

Assume all nine exact colors are double type.

At each w in W, the six exact colors for which x_C!=w place w in a double-shell K5. Their six shell pairs are pairwise vertex-disjoint at w, so they use exactly twelve distinct shell vertices. Therefore at most one of the remaining seven color classes (the three special exact colors, two nonexact colors, and target/other accounting) can use a shell edge incident with w outside those twelve exact incidences.

In particular, among the three exact colors with x_C=w, at least two have zero shell neighbors. By Lemma 2.1, at most one of those zero-shell special colors can use pw; therefore at least one special color at w contributes an additional cross-special-parts shell edge.

The three W-points carry disjoint groups of special exact colors, so this yields at least three additional exact-color shell edges globally.

Thus

\[
e(M)\ge18+3+4=25.
\]

Using the Q32 identity

\[
e(M)+G_A=32,
\]

we obtain

\[
\boxed{t=0\Longrightarrow e(M)\ge25,\quad G_A\le7.}
\]

## 4. The t=1 floor

Let C_* be the unique triple-type exact color and let x_{C_*}=w_0.

For each of the other two W-points w, the six non-special exact colors consist of the triple-type color plus five double-type colors. Their shell-neighbor sets have sizes3,2,2,2,2,2 and are pairwise disjoint, so they use all thirteen shell vertices. Hence all three exact colors with x_C=w have zero shell neighbors at w. Lemma 2.1 then forces at least two additional cross-special-parts shell edges at each of these two W-points.

At w_0, the six non-special exact colors are all double type and use twelve shell vertices. Among the three special exact colors at w_0, at least two have zero shell neighbors, so at least one additional cross-special-parts shell edge is forced.

Therefore at least

\[
2+2+1=5
\]

additional exact-color shell edges occur beyond the base `18+t=19`.

Adding the four nonexact shell edges gives

\[
e(M)\ge19+5+4=28.
\]

Thus

\[
\boxed{t=1\Longrightarrow e(M)\ge28,\quad G_A\le4.}
\]

The earlier corrected multiplicity theorem also forces at least two of the six core-excess units onto the two W-points non-special for C_*.

## 5. Scope

This theorem does not close v=44,m=9. It strengthens its shell normal form to two alternatives:

1. t=0, `e(M)>=25`, `G_A<=7`;
2. t=1, `e(M)>=28`, `G_A<=4`, with at least two core-excess units on W.

No degree9 assertion, no 284-edge identity, and no Case-I assumption `M[B]=empty` is used. The result therefore applies to the remaining Case-II v=44,m=9 terminal as well.