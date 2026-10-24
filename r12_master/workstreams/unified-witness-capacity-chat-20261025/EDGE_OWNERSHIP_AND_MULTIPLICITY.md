# Edge ownership and witness multiplicity: exact identities

Date: 2026-10-25  
Status: **PROVED_ANALYTIC** under the common 284-edge labelled-witness contract. Scalar consequences alone are insufficient; see COUNTEREXAMPLE_OR_GAP_AUDIT.md.

## 1. Three different edge ledgers — do not conflate them

For a witness \((i,b,Q)\), \(Q\) is an independent four-set in the target-color graph \(H\), while \(\{b\}\cup Q\) is a \(K_5\) in a non-target color \(i\).

1. **Internal witness pairs:** the six pairs in \(Q\) are nonedges of \(H\) and are all assigned color \(i\). Distinct witnesses never share an internal pair: if two \(Q\)'s shared two vertices, they would share an edge and assign it two colors. Thus \(6N\) is a genuine count of distinct edges in \(\overline{H[U]}\).
2. **Label-to-core pairs:** the four edges \(bx\), \(x\in Q\), belong to the non-target color \(i\), not to \(E(H)\). They must not be charged against \(e(H)\) or \(e_H(U,W)\). If two witnesses use the same label \(b\), their four-point parts are disjoint; otherwise a shared \(x\) would assign \(bx\) two colors.
3. **Target-core crossing edges:** an edge \(xy\in E(H[U])\) can certify the incompatibility of many pairs of witnesses. Its exact multiplicity is \(r_xr_y\), not one. Summing pairwise crossing costs without this multiplicity correction is invalid.

## 2. Pairwise crossing lemma

For distinct witnesses \(Q_i,Q_j\), let \(s_{ij}=|Q_i\cap Q_j|\in\{0,1\}\). Then
\[
e_H(Q_i\setminus Q_j,Q_j\setminus Q_i)\ge4-s_{ij}.
\]
Indeed, the two difference sets have size \(4-s_{ij}\). Every vertex in one difference set must have a neighbour in the other; otherwise it and the other independent four-set form an independent five-set in \(H\).

The exact edge-load identity is
\[
\boxed{
\sum_{i<j}e_H(Q_i\setminus Q_j,Q_j\setminus Q_i)
=\sum_{xy\in E(H[U])}r_xr_y.
} \tag{1}
\]
For an \(H\)-edge \(xy\), no witness contains both endpoints. Each of the \(r_xr_y\) choices of a witness containing \(x\) and a witness containing \(y\) is therefore a distinct witness pair that charges \(xy\) once. Hence
\[
\boxed{
\sum_{xy\in E(H[U])}r_xr_y
\ge4\binom{N}{2}-\sum_{x\in U}\binom{r_x}{2}.
} \tag{2}
\]
The final term is exactly the number of intersecting witness pairs, because the family is linear.

An upper bound that respects edge multiplicity is
\[
\sum_{xy\in E(H[U])}r_xr_y
\le\frac12\sum_{x\in U}d_{H[U]}(x)r_x^2
\le6\sum_{x\in U}r_x^2+\frac12\sum_{x\in U}\epsilon_xr_x^2. \tag{3}
\]
The first inequality follows from \(r_xr_y\le(r_x^2+r_y^2)/2\); the second uses \(d_{H[U]}(x)\le12+\epsilon_x\). Equations (2) and (3) are valid but do not contradict the current edge budgets.

## 3. Exact support-boundary values

At the support boundary define \(\epsilon_U=\sum_{x\in U}\epsilon_x\) and \(\delta=e(\overline{H[U]})-6N\), the number of complement edges not covered by the witness blocks. At the E407 boundary \(N=49,c=7,v=29\):
\[
\sum r_x=196,\quad \sum o_x=7,\quad
\sum_x\binom{r_x}{2}=567+\Omega,\quad 0\le\Omega\le15.
\]
Thus the pairwise crossing lower bound is
\[
4\binom{49}{2}-(567+\Omega)=4137-\Omega\ge4122.
\]
The internal witness edges give \(e(\overline{H[U]})\ge294\), with exact ledger
\[
e(H[U])=112-\delta,\quad e_H(U,W)=124+\epsilon_U+2\delta,\quad
e(H[W])=48-\epsilon_U-\delta.
\]
The inherited E407 theorem gives \(\epsilon_U+2\delta\ge9\), \(\delta\ge3\), and the core capacity gives \(\epsilon_U+\delta\le16\).

At the E408 Q33 boundary \(N=56,c=8,v=31\):
\[
\sum r_x=224,\quad \sum o_x=24,\quad
\sum_x\binom{r_x}{2}=700+\Omega.
\]
The new labelled omission-capacity theorem gives \(\Omega\le48\) globally, and \(\Omega\le24\) if \(S_0=\epsilon_U+2\delta\in\{12,13,14\}\). Therefore
\[
4\binom{56}{2}-(700+\Omega)=5460-\Omega\ge5412.
\]
The internal witness edges give \(e(\overline{H[U]})\ge336\), with exact ledger
\[
e(H[U])=129-\delta,\quad e_H(U,W)=114+\epsilon_U+2\delta,\quad
e(H[W])=41-\epsilon_U-\delta.
\]
The inherited universal boundary theorem gives \(S_0\ge12\), and the core capacity gives \(\epsilon_U+\delta\le17\).

## 4. The labelled row-zero constraint

For each core vertex \(x\), let \(L_x\subseteq B\) be the set of distinct B labels on witnesses containing \(x\). The same-label disjointness lemma makes these labels distinct. At most one witness containing \(x\) can have label \(p\), so
\[
|L_x|\ge r_x-1.
\]
Every label in \(L_x\) is a shell row anticomplete to \(x\) in the target-color graph. Hence
\[
d_F(x,B)\le11-r_x.
\]
This is a genuine labelled constraint, but it is only an upper bound on the B-row degree of \(x\). The present hypotheses do not force a matching lower bound on B-row incidence, because zero-excess vertices may obtain their required shell support through the three hub rows. This is the exact capacity gap; do not convert it into a contradiction without another hub/row theorem.


## 5. Four-partite branch: the crossing inequality is exactly saturated by within-part edges

Suppose \(L=\overline{H[U]}\) is four-partite and every selected witness \(Q_i\) is a transversal of its four parts. For any pair \(Q_i,Q_j\), let \(s_{ij}=|Q_i\cap Q_j|\in\{0,1\}\). In every part where the two transversals choose different vertices, that pair is an edge of \(H[U]\), because a four-partite graph \(L\) has no within-part edges. There are exactly \(4-s_{ij}\) such parts. Hence the within-part edges already contribute exactly the lower-bound amount \(4-s_{ij}\) for every witness pair.

Summing over all pairs gives the exact identity
\[
\boxed{
\sum_{\substack{xy\in E(H[U])\\x,y\text{ in the same part of }L}}r_xr_y
=4\binom N2-\sum_{x\in U}\binom{r_x}{2}.
} \tag{4}
\]
Thus the generic crossing inequality (2) is sharp in every four-partite witness branch. Any additional target edges of \(H[U]\) between different parts only add positive load to the left side; the lower bound alone cannot exclude such a branch. This identifies a precise limitation of the unlabelled edge-charge method rather than incorrectly treating it as a contradiction.

### Exact Q33 value

For the E408 Q33 four-partite profile \((8,8,8,7)\), Theorem 6.2 of LABELLED_WITNESS_CAPACITY_THEOREM.md gives \(r=8\) on the seven-point part \(D\) and \(r=7\) on the other 24 points. The within-part target edges contribute
\[
64\binom72+49\cdot3\binom82
=1344+4116
=\boxed{5460}.
\]
Also \(\sum_x\binom{r_x}{2}=700\), so the generic lower bound is
\[
4\binom{56}{2}-700=6160-700=\boxed{5460}.
\]
The 24 unused cross-part pair slots are the only possible extra edges of \(H[U]\) between different parts. Since \(\delta\) of these slots are present as leftover edges of \(L\), the other \(24-\delta\) are edges of \(H[U]\), each with weight \(7\cdot7=49\). Consequently
\[
\boxed{
\sum_{xy\in E(H[U])}r_xr_y
=5460+49(24-\delta)=6636-49\delta.
}
\]
The crossing inequality reduces to \(5460\le5460+49(24-\delta)\), i.e. only \(\delta\le24\). The current core budget \(\delta\le17\) and four-partite theorem \(\delta\ge9\) are compatible with it. A further contradiction must force an additional labelled restriction on the unused slots or on the shell rows; generic edge ownership cannot do the job alone.

The same saturation identity (4) applies to a four-partite E407 branch, even though its part sizes and multiplicity profile differ.
