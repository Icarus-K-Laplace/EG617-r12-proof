# Q33 component-pair charge lemma

Status: **PROVED_CONDITIONAL** under the registered seven-witness exact-129 factor contract.

Let \(Q\) be one of the unselected isolated component four-sets of a selected exact-129 color, and put \(k=|Q\cap U|\). Its U-part contributes \(\binom{k}{2}\) distinct complement edges to \(L_U\), and its W-part contributes \(\binom{4-k}{2}\) distinct complement edges to \(L_W\).

For every \(k\in\{0,1,2,3,4\}\),
\[
\boxed{\binom{4-k}{2}+2\binom{k}{2}\ge3.}
\]
The five values of the left-hand side are respectively \(6,3,3,6,12\).

If h of the m selected exact colors use a selected gadget witness, then:
- each of the m-h other colors leaves three isolated component four-sets unselected;
- each of the h gadget-witness colors leaves four isolated component four-sets unselected.

Thus the number of unselected component four-sets is
\[
N=3(m-h)+4h=3m+h.
\]
Write
\[
X_U=\sum_Q\binom{|Q\cap U|}{2},\qquad
X_W=\sum_Q\binom{|Q\cap W|}{2}.
\]
Summing the pointwise inequality gives
\[
\boxed{X_W+2X_U\ge3(3m+h).}\tag{C}
\]

The U- and W-reserve arguments independently give
\[
X_U\le B_U:=L_{\max}(v)-42m-(11-m)p_{12}(v)+\rho_mh,
\]
\[
X_W\le B_W:=t_4(w)-(11-m)p_{12}(w).
\]
Therefore every source-correct parent must satisfy the additional scalar charge inequality
\[
\boxed{3(3m+h)\le B_W+2B_U.}\tag{C'}
\]

This inequality couples the U- and W-internal pair costs of every unselected component K4. It is stronger than checking the two reserves independently.

For the first cells surviving the separate U/W inequalities:
- m=8,v=33: C' requires h in {7,8}, while the W reserve allows h<=5;
- m=9,v=34: C' requires h in {7,8,9}, while the W reserve allows h<=6;
- m=10,v=35: C' requires h=10, while the W reserve allows h<=8.

Hence all three first scalar survivors are excluded. This does not close larger support sizes.
