# E408 Q32: v=45 two-point-complement reduction

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL reduction**, not a v=45 contradiction.

## 1. Contract

Assume the independent Q32 285-edge contract and \(|U|=45\). Put
\[
W=H\setminus U=\{w_1,w_2\}.
\]
For an exact-129 color C, let \(t_C\in\{10,11\}\) be its number of four-point witnesses.

The shell-support classification gives:

- If \(t_C=10\), then \(x_C\in H\), and the complement of the ten witness K4s in H is
  \[
  T_{C,1}\dot\cup T_{C,2}\dot\cup\{x_C\},
  \]
  where \(T_{C,1},T_{C,2}\) are the core triples of the two double-shell K5s.
- If \(t_C=11\) and \(x_C\notin H\), the complement of the eleven witness K4s is one core triple T_C.
- If \(t_C=11\) and \(x_C\in H\), the complement is a core pair T_C together with x_C, coming from the triple-shell K5.

Because the global support U contains all witness K4s, the relevant complement for each color is W together with the points of U omitted by that color.

## 2. Every 11-witness color consumes one of three global resources

For an 11-witness color, its witness union has size 44, so \(O_C=U\setminus Q_C\) has one point and
\[
W\dot\cup O_C
\]
has three points.

### Case A: x_C is outside H

Then these three points are exactly the core triple T_C. Hence \(w_1w_2\) is a C-colored edge. Since an edge has a unique color, at most one exact color can be of this type.

### Case B: x_C is in H

Then
\[
W\dot\cup O_C=T_C\dot\cup\{x_C\}.
\]
If \(x_C\in O_C\), then \(T_C=W\), so again \(w_1w_2\) is a C-colored edge. Across all exact colors, this can happen for at most one color total together with Case A.

If \(x_C\in W\), the global exceptional-vertex injectivity theorem allows at most one exact color per W vertex. Hence at most two exact colors can be of this subtype.

Therefore
\[
\boxed{\#\{C:t_C=11\}\le3.}\tag{1}
\]
Moreover every exact color with \(x_C\notin H\) is in Case A, so
\[
\boxed{\#\{C:x_C\notin H\}\le1.}\tag{2}
\]

## 3. Structure of all remaining exact colors

Every other exact color has t_C=10, x_C∈H, and cannot have x_C∈W unless it uses one of the two injectivity slots. Excluding the at most one color that owns the W-pair and the at most two colors with x_C∈W, at least
\[
\boxed{m-3}
\]
exact colors satisfy all of:

1. t_C=10;
2. x_C∈O_C=U\setminus Q_C;
3. w_1 and w_2 lie in different double-shell core triples.

Thus for each such color
\[
T_{C,1}=\{w_1,a_C,b_C\},\qquad
T_{C,2}=\{w_2,c_C,d_C\},
\]
with a_C,b_C,c_C,d_C∈O_C⊂U and all four distinct.

Across different colors, the pairs \(\{w_1,a_C\},\{w_1,b_C\}\) are globally distinct, and likewise on w_2, by unique edge ownership. This is the canonical v=45 split-triple terminal.

## 4. Consequences for sibling interfaces

- At most three exact colors may have 11 witnesses.
- At most one exact color has its Type-I exceptional vertex outside H. Therefore the seven-block good-component aggregate can improve by at most +1 from the x_C∉H term.
- At least m−3 exact colors are ten-witness colors with split W triples and exceptional point in their five-point O_C.

These conditions are necessary but do not yet contradict the U-edge capacity, M-edge budget, or seven-block blocker ledger. They are intended as the structural input for the next v=45 closure attempt.

## 5. Firewall

No Q33 284-edge identity is used. The only global new input is `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md`, itself proved from the Q32 residual degree ledger.