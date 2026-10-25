# Complete terminal closure: \(\delta=13,\epsilon_U=1\), \(2K_4\cup2K_5\) plus two W-cross-edges

Date: 2026-10-26  
Status: **PROVED_CONDITIONAL** under the retained 47-core / 49-witness contract, the four-partite-\(L\) hypothesis, and the registered component-capacity and reverse-saturation lemmas.

## 1. Frozen contract and common capacity floor

Assume
\[
|H|=47,\quad e(H)=284,\quad \alpha(H)\le4,\quad \omega(H)\le11,\quad
\delta(H)\ge12,\quad \sum_{v\in H}\epsilon_v=4,
\]
where \(\epsilon_v=d_H(v)-12\ge0\). Let \(|U|=29, |W|=18\), with \(\delta=13\), \(\epsilon_U=1\), and \(L=\overline{H[U]}\) four-partite with parts \(A,B,C,D\) of sizes \(7,7,7,8\). Then
\[
e(H[U])=99,\quad e(H[W])=34,\quad e_H(U,W)=151,\quad
\sum_{w\in W}\epsilon_w=3.
\]
For \(d\in D\), let \(t_d=|N_H(d)\cap(A\cup B\cup C)|\). The eight \(H[U]\) cross-edges give
\[
\sum_{d\in D}t_d=8.
\]
For a small-part vertex \(u\in A\cup B\cup C\),
\(d_H(u,W)=6+\epsilon_u-t_u\le7\); for \(d\in D\),
\(d_H(d,W)=5+\epsilon_d-t_d\le6\).

Write \(C_1,C_2\cong K_4\) and \(C_3,C_4\cong K_5\) for the four clique parts of \(H[W]\). For \(S_i=\{u\in U:u\text{ is complete to }C_i\}\), the registered load bounds are
\[
|S_i|\le 8+\mathbf1_{\{E_i\ge e_i\}}\quad(i=1,2),\qquad
|S_i|\le2+E_i\quad(i=3,4),
\]
where \(e_i\) counts cross-edge incidences at \(C_i\) and \(E_i=\sum_{w\in C_i}\epsilon_w\). Since \(\sum_iE_i=3\), if at least one cross-edge meets a \(K_4\), then
\[
\sum_i|S_i|\le24.
\]
Indeed, if one \(K_4\) has capacity upper bound at most \(8\), the total is at most \(8+9+4+3=24\). If both \(K_4\) capacity upper bounds are \(9\), then \(E_1+E_2\ge e_1+e_2\ge1\), so \(E_3+E_4\le2\) and the total is at most \(18+4+2=24\). The sets \(S_i\) are disjoint because every \(u\in U\) has at most seven W-neighbours, while two W-components require at least eight. Thus every placement with a cross-edge incident to a \(K_4\) has at least
\[
k:=|\{u\in U:u\text{ is W-unsaturated}\}|\ge29-24=5. \tag{1}
\]

## 2. Exact blocker shapes and D-part degree arithmetic

For a W-unsaturated \(u\), let \(X_i=C_i\setminus N_H(u)\), all nonempty. Every tuple in \(X_1\times X_2\times X_3\times X_4\) must contain one of the two W-cross-edges, or it would be an independent 5-set with \(u\).

- If the two edges are disjoint, only a **Type I** blocker is possible: one edge has both endpoint non-neighbour sets singleton.
- If they form a star, either Type I is possible or there is a **Type II** blocker: the non-neighbour sets in the two endpoint parts are the two distinct leaves in one part and the singleton shared endpoint in the other.

The minimum W-degrees are therefore:
- \(K_4\)-\(K_4\) Type I: \(3+3=6\);
- \(K_4\)-\(K_4\) Type II: \(2+3=5\);
- \(K_4\)-\(K_5\) Type I: \(3+4=7\);
- \(K_4\)-\(K_5\) Type II: \(2+4=6\).

For every \(d\in D\), \(t_d\le1+\epsilon_d\): if \(d\) is saturated, it has at least four W-neighbours; if it is unsaturated, the blocker lower bound gives the stronger \(t_d\le\epsilon_d\). Since \(\sum t_d=8\) and at most one D-vertex can have positive excess, at least six D-vertices satisfy
\[
t_d=1,\qquad \epsilon_d=0,\qquad d_H(d,W)=4. \tag{2}
\]
Each such vertex is saturated (all blocker minima above are at least five), so its W-neighbourhood is exactly one of the two \(K_4\) components.

Also, any W-vertex in a \(K_4\) component that is not complete to a U-part must have \(\epsilon_w=3\), by the retained reverse-saturation lemma and \(d_H(w,U)=9+\epsilon_w\). Since the total W-excess is three, at most one W-vertex in the two \(K_4\) components can be unlabelled by a U-part.

## 3. The same-pair \(K_4\)-\(K_4\) placements are impossible

Assume both W-cross-edges join \(C_1\) and \(C_2\), either as a matching or as a star. By (1), \(k\ge5\). At most one W-unsaturated vertex lies in \(D\): any such D-vertex has \(t_d\le\epsilon_d\), so it must be the unique possible positive-excess D-vertex or the unique \(t_d=0\) vertex in the \((2,1,\ldots,1,0)\) degree pattern. At most one exception has positive excess because \(\epsilon_U=1\). Hence there is a small-part W-unsaturated vertex \(u\) with \(\epsilon_u=0\).

In the matching case every exception is Type I, so \(t_u=0\) and \(u\) has a non-neighbour in each \(K_4\) and in each \(K_5\). In the star case, \(u\) is Type I or II; it has a non-neighbour in each \(K_4\), and at most one additional W-neighbour outside the two \(K_4\)'s. Thus in either case choose non-neighbours \(y\in C_3,z\in C_4\) of \(u\).

Choose one of the at least six vertices \(d\in D\) in (2) that is not adjacent to \(u\); at most one of those vertices can be adjacent to \(u\), because \(u\) has at most one H-edge to D. The vertex \(d\) is complete to one \(K_4\) and anticomplete to the other \(K_4\) and both \(K_5\)'s. Choose \(x\) from the \(K_4\) opposite \(N_W(d)\), with \(ux\notin E(H)\). The three W-vertices \(x,y,z\) are pairwise nonadjacent, since all W-cross-edges are between the two \(K_4\)'s. Also \(d\) is nonadjacent to all three and \(u\not\sim d\). Therefore
\[
\{u,d,x,y,z\}
\]
is an independent 5-set, contradicting \(\alpha(H)\le4\). This excludes both the K4-K4 matching and star.

## 4. The same-pair \(K_4\)-\(K_5\) stars are impossible

Let \(P\cong K_4\) be the K4 component incident to both cross-edges, let \(Q\cong K_4\) be the other K4, and let \(R,S\cong K_5\). The two edges form a star between \(P\) and one of \(R\); the other K5 is \(S\).

### 4.1 A D-vertex has W-neighbourhood exactly \(P\)

We prove that some \(d\in D\) has \(N_W(d)=P\). Suppose no D-vertex has W-neighbourhood exactly \(P\). By (2), at least six D-vertices have W-neighbourhood equal to a K4; under the supposition they all have W-neighbourhood \(Q\). Thus every \(w\in Q\) has at least six D-neighbours.

If such a \(w\) is not complete to \(D\), it cannot be complete to any small U-part: those seven vertices plus its six D-neighbours would give degree at least thirteen, but \(d_H(w,U)=9+\epsilon_w\le12\). Hence it is unlabelled by U-parts. At most one vertex of \(Q\) can be unlabelled, so at least three vertices of \(Q\) are complete to all of \(D\).

Every \(d\in D\) is adjacent to these three vertices of \(Q\). Also \(d_H(d,W)\le5\): the only possible way to have degree six would be \(\epsilon_d=1,t_d=0\), which is impossible because the other seven \(t\)-values are at most one and sum to only seven. A D-vertex is W-saturated, since an unsaturated vertex in a K4-K5 star needs at least six W-neighbours. If \(d\) is not complete to \(Q\), its W-neighbourhood of size at most five is either a K5, or a K4 plus at most one extra vertex; it then has at most one neighbour in \(Q\), contradicting its adjacency to the three Q-vertices complete to D. Therefore all D-vertices are complete to \(Q\), making \(D\cup Q\) a \(K_{12}\), contrary to \(\omega(H)\le11\). The supposition fails, proving the claim.

### 4.2 The independent-5-set contradiction

By (1), there are at least five W-unsaturated U-vertices. A Type I K4-K5 blocker needs at least seven W-neighbours, so it must be the unique positive-excess small-part vertex. No D-vertex can be an exception here, because an unsaturated D-vertex would need at least six W-neighbours, while \(\epsilon_d=1,t_d=0\) is impossible by \(\sum t_d=8\). Thus at least three exceptions are zero-excess small-part Type II blockers. Such a vertex \(u\) has \(t_u=0\) and exactly six W-neighbours, so it is anticomplete to the two W-components not incident to the two cross-edges.

Choose such a \(u\); since \(t_u=0\), every D-vertex is nonadjacent to \(u\). The D-vertex \(d\) from Section 4.1 has W-neighbourhood exactly \(P\).

If the star is centred in the K5 \(R\), the Type II non-neighbour set in \(R\) is its shared endpoint \(y\). If the star is centred in the K4 \(P\), choose either leaf endpoint \(y\in R\), which is a non-neighbour of \(u\). In both cases choose \(q\in Q\) and \(s\in S\). The three vertices \(y,q,s\) are pairwise nonadjacent, and each is nonadjacent to both \(u\) and \(d\). Also \(u\not\sim d\). Thus \(\{u,d,y,q,s\}\) is an independent 5-set, contradiction.

Therefore both same-pair K4-K5 star placements are excluded.

## 5. Complete placement conclusion

The remaining placements are now all excluded under the same contract:
- different-pair placements: already excluded by the component-capacity bound with all U-vertices saturated;
- both edges between the K5 parts: already excluded by the Type-I/Type-II degree lower bounds and the capacity bound;
- same-pair disjoint K4-K5: excluded in DELTA13_EPS1_TWO_CROSS_EDGE_K4K5_DISJOINT_CLOSED.md;
- same-pair K4-K4 matching or star: Section 3 above;
- same-pair K4-K5 star centred in either endpoint part: Section 4 above.

Hence the entire four-partite-\(L\), \(\delta=13,\epsilon_U=1\), \(H[W]=2K_4\cup2K_5\) plus two-cross-edge profile is **EXCLUDED** under the retained core/witness contract. This does not close the \(\epsilon_U=2\) one-cross-edge profile, the \(\epsilon_U=0\) row, non-four-partite \(L\), \(\delta\le12\), the five shell templates globally, or the original \(K_{145}\)-to-T61 bridge.
