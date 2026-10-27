# E408 Q32 — independent 285-edge terminal

Updated: 2026-10-27  
Status: **OPEN overall; v=44 is PROVED_CONDITIONAL impossible. Surviving support sizes: v=45,46,47.**

## 1. Frozen Q32 contract

\[
|V(H)|=47,\quad e(H)=285,\quad \alpha(H)\le4,\quad\delta(H)\ge12,
\quad\sum_{x\in H}(d_H(x)-12)=6.
\]
The shell parameter is \(q=32\), equivalently \(e(M)+G_A=32\). Under the registered seven-block equality and exact-129 Type-I factorization, \(m\in\{8,9,10\}\) non-target colors are exact-129.

No Q33 284-edge identity is imported.

## 2. Retained support floor

The read-only Q32 sibling workstream proves
\[
|U|\ge44
\]
for the union U of all exact-color four-point witnesses, uniformly over both shell-support branches. The exact capacity ledger is
\[
6N\le\binom v2-p_4(47-v)-12v+285-E_U.
\]

## 3. New global exceptional-vertex injectivity

`Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md` proves that no residual vertex can be the KP Type-I exceptional vertex for two distinct exact-129 colors.

For any residual vertex v, exact colors contribute degree at least \(4m+5n_v\), where \(n_v\) is its exceptional multiplicity. A deletion-Turan argument forces the combined nonexact degree floor
\[
B_8=6,\qquad B_9=3,\qquad B_{10}=1.
\]
Together with target degree at least 13 and total degree 60, this gives \(n_v\le1\) for all m=8,9,10.

## 4. v=44 is closed

At v=44, W=H\U has three vertices. The sibling triple-pair theorem proves that at least m-3 exact colors have their exceptional vertex in W. Hence
\[
\sum_{w\in W}n_w\ge m-3\ge5.
\]
But injectivity gives \(n_w\le1\) for each of the three vertices, so the left side is at most three. Contradiction.

Therefore
\[
\boxed{v\ne44.}
\]
Proof: `Q32_V44_EXCEPTIONAL_DEGREE_CLOSURE.md`.  
Verifier: `verify_q32_v44_exceptional_degree.py`.

Combining with the sibling support floor:
\[
\boxed{v\in\{45,46,47\}.}
\]

## 5. Current high-support ledger

The simple U-edge capacities do not yet exclude v=45,46,47.

For any non-target color D on a v-point U, \(\alpha(D[U])\le12\), so
\[
p_{12}(45)=63,\qquad p_{12}(46)=66,\qquad p_{12}(47)=69.
\]
For an exact color:
- at v=45, a ten-witness color contributes at least 64 U-edges if its exceptional vertex is in W and at least 65 if it is in U; an eleven-witness color contributes at least 66;
- at v=46, every exact color contributes at least 66 U-edges;
- at v=47, the whole core is U and the global complement has exactly 796 edges.

These scalar floors leave positive capacity and are not promoted to closure.

## 6. Next structural target

For v=45,46,47 the v=44 triple-pair theorem no longer forces enough exceptional vertices into W. The next proof must use at least one genuinely structural input beyond scalar support capacity. The strongest currently available candidates are:

1. global exceptional-vertex injectivity together with shell location of the Type-I exceptional vertices;
2. the exact shell patterns: ten-witness colors use two double-shell K5s, while eleven-witness colors use either one double-shell K5 with x outside H or one triple-shell K5 with x in H;
3. the seven-block blocker lower bound and good-component labels;
4. near-Turan structure of the nonexact colors on H or U when their edge counts approach the p_12 floor.

## 7. Scope firewall

Source Q32 branch: `workstream/r12-e408-q32-excess6-20261025` at `a0ba6db26c7e8b00a4217dcbcbf298895dff93ce`.

The Q33 31-point/56-witness closure is not used. EG617(r=12) remains **OPEN / NOT_CERTIFIED** until v=45,46,47 and the other upstream/backend branches are closed.