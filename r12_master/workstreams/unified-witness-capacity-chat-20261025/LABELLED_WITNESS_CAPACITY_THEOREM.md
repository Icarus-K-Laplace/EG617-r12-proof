# Unified labelled witness-capacity theorem (E407 Q32 / E408 Q33)

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained T61 shell contract and exact-129 factor theorem. This is a cross-terminal structural theorem, not a terminal contradiction.

## 1. Common contract

Let \(H\) be the 47-vertex target-color core with
\[
\alpha(H)\le4,\qquad \delta(H)\ge12,\qquad e(H)=284,
\qquad d_H(x)=12+\epsilon_x,\quad
\epsilon_x\ge0,\quad\sum_{x\in H}\epsilon_x=4.
\]
Let the T61 shell be \(A=S\dot\cup B\), where \(|S|=3\), \(|B|=10\), and \(B\) is a clique in the target-color graph. The theorem applies to the retained E407 Q32 shell templates and the E408 Q33/d3 interface; it does not silently extend to arbitrary E408 Q32 states.

For each exact-129 non-target color \(i\), the registered factor theorem supplies at least seven pairwise vertex-disjoint isolated \(K_5\) components avoiding \(S\). Their four-point core parts are independent sets
\[
Q_{i1},\ldots,Q_{i7}\subseteq V(H),\qquad |Q_{ij}|=4.
\]
At least six components per color have the form \(\{b\}\cup Q_{ij}\) with \(b\in B\); call these **B-labelled witnesses**. A seventh witness, if not B-labelled, has label \(p\), the shell pivot. Every witness has exactly one label in \(B\cup\{p\}\). Within one color, the seven \(Q_{ij}\) are disjoint. Across distinct colors, any two selected \(Q\)-sets intersect in at most one vertex, since a shared pair would assign one edge two colors.

Let \(c=7\) for E407 Q32 and \(c=8\) for E408 Q33. Select seven witnesses from each of the \(c\) exact-129 colors and let
\[
U=\bigcup_{i=1}^{c}\bigcup_{j=1}^{7}Q_{ij},\qquad |U|=v.
\]
The minimum-support boundaries are \((c,v)=(7,29)\) and \((8,31)\). Write \(W=V(H)\setminus U\), \(r_x=|\{(i,j):x\in Q_{ij}\}|\), and \(o_x=c-r_x\). At the boundary define \(\epsilon_U=\sum_{x\in U}\epsilon_x\) and \(\delta=e(\overline{H[U]})-42c\), the number of complement edges not covered by the selected witness blocks.

## 2. The labelled-packing theorem

**Theorem 2.1 (label capacity and omission ledger).** Under the common contract:

1. \(r_x\le c\), \(\sum_{x\in U}r_x=28c\), and \(\sum_{x\in U}o_x=c(v-28)\).
2. For every fixed label \(\lambda\in B\cup\{p\}\), the witnesses carrying \(\lambda\) are pairwise vertex-disjoint. Thus the number \(n_\lambda\) of occurrences of any one label satisfies
   \[
   n_\lambda\le\left\lfloor\frac v4\right\rfloor.
   \]
3. Let \(P\) be the number of pivot-labelled witnesses. Then
   \[
   P\le\left\lfloor\frac v4\right\rfloor,\qquad
   L:=\#\{\text{B-labelled witnesses}\}=7c-P.
   \]
   Consequently:
   - E407 Q32: \(P\le7\). Either all seven colors have a pivot-labelled witness (then those seven \(Q\)'s are disjoint and cover 28 of the 29 support points), or at least one color has seven B-labelled witnesses.
   - E408 Q33: \(P\le7<8\). Hence at least one of the eight colors has **seven B-labelled witnesses**, and \(L\ge49\) (not merely \(48\)).
4. Since \(|X|\le4\) for \(X=\{x:\epsilon_x>0\}\), every color has at least three zero-excess witnesses among its seven selected \(Q\)'s. Every color with a pivot-labelled witness has at least two zero-excess B-labelled witnesses; every color without one has at least three. Therefore the total number \(Z_B\) of zero-excess B-labelled witnesses satisfies
   \[
   Z_B\ge 2P+3(c-P)=3c-P.
   \]
   In particular, E407 has \(Z_B\ge14\), and E408 Q33 has \(Z_B\ge17\).

### Proof

Within a color the seven \(Q\)'s are disjoint, so each vertex occurs at most once per color; this gives \(r_x\le c\). Every color contributes 28 vertex incidences, hence \(\sum r_x=28c\). Since \(o_x=c-r_x\),
\[
\sum_{x\in U}o_x=cv-28c=c(v-28).
\]
Every point of \(U\) occurs in at least one witness, so \(o_x\le c-1\).

If two witnesses with the same label \(\lambda\) shared a core vertex \(x\), the edge \(\lambda x\) would belong to two distinct non-target colors. Thus equal-label witnesses are disjoint. Their four-point parts occupy disjoint vertices of \(U\), proving \(n_\lambda\le\lfloor v/4\rfloor\). Apply this to \(\lambda=p\) to obtain \(P\le\lfloor v/4\rfloor\). For E408, \(v=31\) gives \(P\le7\), so at least one of the eight colors has no pivot-labelled witness and all seven of its selected witnesses are B-labelled.

Finally, \(e(H)=284\) gives total excess four, so at most four vertices have positive excess. The seven \(Q\)'s in any one color are disjoint; at most four can meet \(X\), leaving at least three zero-excess \(Q\)'s. If the color has a pivot-labelled witness, only six of its seven selected witnesses are guaranteed B-labelled, so at least \(6-4=2\) of those are zero-excess. Otherwise all seven are B-labelled, yielding at least \(7-4=3\). Summing over colors proves the bound on \(Z_B\). \(\square\)

## 3. Exact omission and overlap theorem at minimum support

For each color \(i\), put \(U_i=\bigcup_{j=1}^7Q_{ij}\), so \(|U_i|=28\), and let \(O_i=U\setminus U_i\). At the minimum-support boundary, \(|O_i|=\sigma:=v-28\), and \(o_x\) counts how many omission sets contain \(x\). Define
\[
\Omega=\sum_{x\in U}\binom{o_x}{2}
       =\sum_{i<j}|O_i\cap O_j|.
\]
Let \(P_{\rm int}\) be the number of unordered pairs of witness sets with nonempty intersection. Since the family is linear, \(P_{\rm int}=\sum_x\binom{r_x}{2}\). Each pair of color classes has exactly \(|U_i\cap U_j|=v-|O_i\cup O_j|=28-\sigma+|O_i\cap O_j|\) intersecting witness pairs. Hence
\[
\boxed{P_{\rm int}=\binom c2(28-\sigma)+\Omega.}
\]

The exact finite omission ledger is:

| Terminal | \(c,v,\sigma\) | \(\sum o_x\) | \(\Omega\) before shell-capacity refinement |
|---|---:|---:|---:|
| E407 Q32 | \(7,29,1\) | 7 | \(0\le\Omega\le15\), so \(567\le P_{\rm int}\le582\) |
| E408 Q33 | \(8,31,3\) | 24 | \(0\le\Omega\le66\), so \(700\le P_{\rm int}\le766\) |

For E407, \(\sum o_x=7\), \(o_x\le6\), and convexity shows the maximum \(\Omega=15\) occurs at omission multiplicities \(6,1\). For E408, the raw maximum \(66\) occurs at \(7,7,7,3\). The next section strengthens the E408 bound by using the core degree/cross-edge budget.

## 4. Labelled omission-capacity refinement

For every \(x\in U\), the \(r_x\) witness sets containing \(x\) have pairwise-disjoint three-point remainders: if two remainders shared a vertex, the two \(Q\)'s would intersect in at least two points. Since each \(Q\) is independent in \(H\), \(x\) has at least \(3r_x\) distinct non-neighbours in \(U\). Therefore
\[
d_{H[U]}(x)\le v-1-3r_x
\quad\Longrightarrow\quad
d_H(x,W)\ge 13-v+3r_x+\epsilon_x.
\]
As a nonnegative degree, this gives the common inequality
\[
\boxed{
e_H(U,W)\ge
\sum_{x\in U}\max\{0,\,13-v+3(c-o_x)\}.
} \tag{1}
\]

The exact 284-edge ledger and the \(K_5\)-free-complement/Turán lower bound on \(H[W]\) give:

- E407 Q32:
  \[
  e_H(U,W)=124+S,\quad S:=\epsilon_U+2\delta,\quad
  \epsilon_U+\delta\le16,\quad 9\le S\le32.
  \]
  From (1), with \(n_j=|\{x:o_x=j\}|\),
  \[
  \boxed{5n_0+2n_1\le124+S.} \tag{2}
  \]
  Exhausting the integer omission profiles \(o_x\in\{0,\ldots,6\}\), \(\sum o_x=7\), gives:

  | \(S\) | Maximum \(\Omega\) allowed by (2) |
  |---:|---:|
  | 9 | 7 |
  | 10 | 10 |
  | 11–12 | 11 |
  | 13–32 | 15 |

- E408 Q33:
  \[
  e_H(U,W)=114+S_0,\quad S_0:=\epsilon_U+2\delta,\quad
  \epsilon_U+\delta\le17,\quad 12\le S_0\le34.
  \]
  From (1),
  \[
  \boxed{6n_0+3n_1\le114+S_0.} \tag{3}
  \]
  Exhausting the integer profiles \(o_x\in\{0,\ldots,7\}\), \(\sum o_x=24\), gives:

  | \(S_0\) | Maximum \(\Omega\) allowed by (3) |
  |---:|---:|
  | 12–14 | 24 |
  | 15–17 | 29 |
  | 18–20 | 31 |
  | 21–23 | 33 |
  | 24–26 | 37 |
  | 27–29 | 41 |
  | 30–32 | 47 |
  | 33–34 | 48 |

The integer-profile tables are checked by verify_unified_witness_capacity.py. They are exact finite arithmetic statements, not graph-realization certificates.

## 5. Edge ownership and the remaining non-contradiction

Each witness contributes six nonedges of \(H[U]\). Pairwise intersection at most one means no such edge is contributed by two witnesses, so
\[
6(7c)\le e(\overline{H[U]}).
\]
The exact core capacity is
\[
e(\overline{H[U]})
\le \binom v2-p_4(47-v)-12v+284-\epsilon_U,
\]
where \(p_4(w)=\binom w2-t_4(w)\), the minimum edge count of a \(w\)-vertex graph with independence number at most four. Thus \(p_4(18)=32\) and \(p_4(16)=24\), yielding
\[
\begin{array}{ll}
\text{E407:}&294+\delta\le310-\epsilon_U,\quad \epsilon_U+\delta\le16,\\
\text{E408 Q33:}&336+\delta\le353-\epsilon_U,\quad \epsilon_U+\delta\le17.
\end{array}
\]
These inequalities are consistent with the omission-capacity refinements. The theorem closes no terminal by itself. The precise unresolved bridge is to turn the labelled row-hit constraints of the selected \(Q\)'s into an additional upper bound on the right side of (1), or into a stronger lower bound on \(e_H(U,W)\). An arbitrary independent four-set supplied by the zero-excess theorem cannot be inserted into the labelled family without a separate color-component lemma.


## 6. Labelled row capacity in the four-partite branches

This section is conditional on the corresponding terminal being genuinely four-partite and every selected witness being a transversal of its four parts. It does not assume the non-four-partite branch away.

### Lemma 6.1 (per-part label-row capacity)

Let \(L=\overline{H[U]}\) be four-partite with parts \(V_1,\ldots,V_4\), and let every selected witness \(Q\) be a transversal \(Q\cap V_j\) of size one. For a shell label \(b\in B\), let \(n_b\) be the number of selected witnesses labelled \(b\), and let \(D_b=N_F(b)\cap H\) be its target-colour core neighborhood. Then
\[
\boxed{|D_b\cap V_j|\le |V_j|-n_b\quad(j=1,\ldots,4),}
\qquad
\boxed{|D_b\cap U|\le |U|-4n_b.}
\]
In particular, in E407's part sizes \((8,7,7,7)\), \(n_b=7\) forces \(D_b\cap U\) to lie in at most one point of the size-eight part. In E408 Q33's part sizes \((8,8,8,7)\), \(n_b=7\) forces \(D_b\cap U\) to lie in at most one point in each of the three size-eight parts and no point in the size-seven part. If \(t_b=|D_b|\), these give
\[
|D_b\cap W|\ge \max\{0,t_b-(|U|-4n_b)\}.
\]

**Proof.** The \(n_b\) witness blocks carrying label \(b\) are pairwise vertex-disjoint: otherwise the edge from \(b\) to a shared core vertex would be assigned two non-target colors. Since each block is a transversal, these blocks occupy \(n_b\) distinct vertices in every part \(V_j\). Each labelled block is anticomplete to \(b\) in the target graph, so \(D_b\) avoids every one of these occupied vertices. At most \(|V_j|-n_b\) vertices in part \(V_j\) remain available to \(D_b\). Summing the four part bounds proves the second inequality. The W-bound follows by subtracting the maximum possible number of neighbors in U from \(t_b\). \(\square\)

### Theorem 6.2 (exact Q33 four-partite incidence profile)

Assume the E408 Q33 minimum-support contract and that \(L\) is four-partite with parts \(A_1,A_2,A_3,D\) of sizes \(8,8,8,7\). The 56 selected witness K4s are edge-disjoint transversals, seven from each of eight exact-129 colors. Then
\[
r_d=8\quad(d\in D),\qquad r_x=7\quad(x\in A_1\cup A_2\cup A_3).
\]
Consequently the omission multiplicities satisfy
\[
o_d=0\quad(d\in D),\qquad o_x=1\quad(x\in A_1\cup A_2\cup A_3),
\qquad \boxed{\Omega=\sum_{x\in U}\binom{o_x}{2}=0.}
\]
Equivalently, the eight color omission triples partition the 24 vertices of \(A_1\cup A_2\cup A_3\); no two colors omit the same support vertex.

**Proof.** Each color has seven pairwise-disjoint transversals and therefore uses every vertex of D exactly once, so every \(d\in D\) lies in eight blocks. For \(x\in A_1\), edge-disjointness implies that no pair \((x,d)\) can be used twice. There are only seven choices of \(d\), so \(r_x\le7\). There are \(56\) total incidences with \(A_1\), spread over eight vertices, hence every vertex of \(A_1\) has multiplicity exactly seven. The same argument applies to \(A_2,A_3\). Thus every large-part vertex is omitted by exactly one of the eight color classes, while no D vertex is omitted. \(\square\)

### Corollary 6.3 (Q33 label budget on the seven-point part)

Under Theorem 6.2, the eight blocks through any fixed \(d\in D\) have eight distinct labels: a repeated label would produce two same-label witnesses sharing \(d\). At most one label is the pivot \(p\). Hence each \(d\) has at least seven distinct B labels and is target-adjacent to at most three B rows; if no pivot-labelled witness contains \(d\), it has eight B labels and is target-adjacent to at most two B rows.

If \(P\) is the number of pivot-labelled selected witnesses, the pivot witnesses occupy \(P\) distinct points of D, so
\[
\boxed{e_F(B,D)\le 3P+2(7-P)=14+P\le21.}
\]
Under the retained Q33/d3 row budget \(K_B:=\sum_{b\in B}k_b\ge22-\beta\) and \(G_B:=\sum_b g_b\), where \(t_b=k_b+g_b\), it follows that
\[
\boxed{e_F(B,H\setminus D)\ge
\max\{0,\ 8-\beta+G_B-P\}.}
\]
This is a genuine labelled row-capacity constraint. It does not by itself contradict the current budget; it records the minimum target incidence that must leave the seven-point part.

## 7. Cross-terminal interpretation

The generic omission-capacity inequality remains valid in both terminal types. The partite theorem sharpens it in the Q33 four-partite branch to the exact profile \(\Omega=0\), whereas the non-four-partite branch retains the broader omission profiles. Therefore any future use of the scalar profile \(\Omega>0\) to exclude Q33 must explicitly be a non-four-partite argument; it cannot be used against the four-partite branch. Conversely, the Q33 four-partite label-row cap \(|D_b\cap D|\le7-n_b\) is not available in the non-four-partite branch.


## 8. Cross-terminal interface to the exact-129 outer-block system

The core-witness omission ledger and the exact-129 outer-block ledger are distinct but now have an explicit interface. For each exact-129 color C, the seven-block equality system supplies \(P_C+R_C=62\) and the low-budget block set \(\mathcal I_C=\{i:r_i(C)\le5\}\). The outer-row theorem proves that every pair in \(\mathcal I_C\) has at least nine of ten same-component representative edges, and every missing diagonal costs at least one unit of \(d_{ij}(C)\). Thus
\[
\sum_{\{i,j\}\subseteq\mathcal I_C}m_{ij}(C)\le P_C.
\]

This bound is reusable in both the E407 Q32 and E408 Q33 minimum-support contracts because it depends on the shared exact-129 factor theorem and seven-block equality system, not on the 29-point versus 31-point support profile. It does not itself improve the target-core inequality (1) or assign labels to arbitrary graph-theoretic common witnesses; the label-transfer barrier in Section 5 remains.
