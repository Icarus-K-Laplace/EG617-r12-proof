# E407 Q32: the augmentable-edge reduction for non-four-partite \(\delta=14\)

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL strict reduction** under the retained 49-witness/core contract, Brouwer's second-Turán theorem, and the Kang–Pikhurko equality classification.

## 1. Contract

Let \(H\) be the 47-vertex core and let \(U\subset V(H)\), \(|U|=29\), \(W=V(H)\setminus U\), \(|W|=18\). Assume
\[
e(H)=284,\quad \alpha(H)\le4,\quad \omega(H)\le11,\quad
\delta(H)\ge12,\quad \sum_{v\in H}(d_H(v)-12)=4.
\]
The 49 witness blocks are independent 4-sets in \(H[U]\), pairwise edge-disjoint as \(K_4\)'s in
\(L=\overline{H[U]}\), with seven blocks from each of seven exact-129 colors. Set
\[
\delta=e(L)-294,\qquad
\epsilon_U=\sum_{u\in U}(d_H(u)-12).
\]
Assume \(\delta=14\) and \(L\) is non-four-partite. Then
\[
e(L)=308,\quad e(H[U])=98,\quad
0\le\epsilon_U\le2.
\]

Call a nonedge \(uv\notin E(L)\) **augmentable** if \(L+uv\) remains \(K_5\)-free.

## 2. An augmentable edge forces the balanced Kang–Pikhurko base

Suppose an augmentable edge \(uv\) exists, and put \(L'=L+uv\). Since \(L\) is non-four-partite, \(L'\) is also non-four-partite: every subgraph of a four-partite graph is four-partite. Moreover \(e(L')=309\), the Brouwer maximum for a non-four-partite \(K_5\)-free graph on 29 vertices. The Kang–Pikhurko equality classification therefore applies.

The 49 witness \(K_4\)'s remain pairwise edge-disjoint in \(L'\). The witness-packing calculation in DELTA15_SECOND_TURAN_PACKING.md, Sections 1–3, excludes the two unbalanced base profiles:
- \((6,7,7,8)\), since \(t\ge7+a\) and \(3t\le16+a\) imply \(21+3a\le16+a\);
- \((6,6,8,8)\), since \(t\ge13+a\) and \(3t\le17+a\) imply \(39+3a\le17+a\).

Thus the only possible base profile is \((7,7,7,7)\). Write its parts \(P_1,P_2,P_3,P_4\), let \(A\subsetneq P_1\) have size \(a\in\{1,\ldots,6\}\), let \(y\in P_2\), and let \(x\) be the exceptional vertex. The exact degree identities in \(L'\) give
\[
d_{\overline{L'}[U]}(x)=13-a,\qquad
d_{\overline{L'}[U]}(y)=6+a.
\]
Since \(L'=L+uv\), the original \(H[U]=\overline L\) is obtained from \(\overline{L'}\) by adding the edge \(uv\). Define \(I_x=1\) iff \(x\in\{u,v\}\), and \(I_y=1\) iff \(y\in\{u,v\}\). Writing \(\epsilon_z=d_H(z)-12\), we obtain the exact \(W\)-degree equations
\[
d_H(x,W)=a-1+\epsilon_x-I_x,\qquad
d_H(y,W)=6-a+\epsilon_y-I_y. \tag{1}
\]
In particular,
\[
d_H(x,W)+d_H(y,W)
=5+\epsilon_x+\epsilon_y-I_x-I_y
\le 5+\epsilon_U. \tag{2}
\]

## 3. The \(W\)-side profile list is exhaustive

Because \(e(H[W])=48-\epsilon_U-\delta=34-\epsilon_U\), the complement \(\overline{H[W]}\) is \(K_5\)-free and has
\[
e(\overline{H[W]})=153-(34-\epsilon_U)=119+\epsilon_U\ge119.
\]
For 18 vertices, \(t_4(18)=121\), while Brouwer's non-four-partite bound is
\(121-\lfloor18/4\rfloor+1=118\). Hence \(\overline{H[W]}\) is four-partite. Exact partition and edge-count arithmetic gives the following exhaustive list; the displayed clique parts are the components of \(H[W]\), with the indicated number of cross edges between them.

| \(\epsilon_U\) | \(H[W]\) clique-part sizes | Cross edges |
|---:|---|---:|
| 0 | \((4,4,5,5)\) | 2 |
| 0 | \((3,5,5,5)\) | 1 |
| 0 | \((4,4,4,6)\) | 1 |
| 0 | \((3,4,5,6)\) | 0 |
| 1 | \((3,5,5,5)\) | 0 |
| 1 | \((4,4,4,6)\) | 0 |
| 1 | \((4,4,5,5)\) | 1 |
| 2 | \((4,4,5,5)\) | 0 |

## 4. Independent-transversal obstruction for an unsaturated vertex

Call \(z\in U\) component-saturated if it is complete to at least one of the four clique components of \(H[W]\). If \(H[W]\) has no cross edges, every \(z\in U\) is component-saturated: otherwise choosing one non-neighbour from each component yields an independent 5-set with \(z\), contrary to \(\alpha(H)\le4\).

If there is one cross edge between components of sizes \(s_i,s_j\), a vertex not component-saturated must have at least \(s_i+s_j-2\) neighbours in \(W\): its non-neighbour set in each component is nonempty, and every transversal of the four non-neighbour sets must contain the unique cross edge, forcing those two sets to be the singleton endpoints.

If there are two cross edges and all four components have size at least four, a vertex not component-saturated has at least five neighbours in \(W\). Indeed, to hit every transversal with two edges, the most economical possible pattern is two edges sharing an endpoint between the same pair of components: the non-neighbour sets in those two components must then have sizes at most \(1\) and \(2\), costing at least \((4-1)+(4-2)=5\) neighbours. If the two edges are disjoint, or lie between different pairs of components, the required number is at least six (in fact at least nine in the shared-endpoint/different-pair case).

Thus:
- for the \((4,4,5,5)\)+two-edge profile, an unsaturated vertex needs \(d_H(z,W)\ge5\);
- for any listed one-cross-edge profile, an unsaturated vertex needs \(d_H(z,W)\ge6\);
- for a no-cross-edge profile, no unsaturated vertex is possible.

## 5. Eliminate all but one augmentable-edge terminal

Use (1)–(2) and the exhaustive \(W\)-profile list.

### Case \(\epsilon_U=0\)

Equation (2) gives \(d_H(x,W)+d_H(y,W)\le5\).

- For \((4,4,5,5)\) with two cross edges, two saturated vertices would need at least \(4+4=8\) neighbours in \(W\); one unsaturated and one saturated would need at least \(5+4=9\). Impossible.
- For \((3,5,5,5)\) or \((4,4,4,6)\) with one cross edge, two saturated vertices need at least \(3+3=6\) or \(4+4=8\), respectively. Any unsaturated vertex alone needs at least six neighbours, and the other vertex must still have at least three or four. Impossible.
- For \((3,4,5,6)\) with no cross edges, both vertices must be saturated and need at least \(3+3=6\) neighbours. Impossible.

So \(\epsilon_U\ne0\).

### Case \(\epsilon_U=1\)

Now the sum in (2) is at most six.

- For \((4,4,4,6)\) with no cross edge, both vertices need at least four neighbours: impossible.
- For \((4,4,5,5)\) with one cross edge, two saturated vertices need at least eight neighbours in total; if either is unsaturated it needs at least six and the other at least four. Impossible.
- For \((3,5,5,5)\) with no cross edge, both vertices must be saturated and each needs at least three neighbours. Equality in (2) is forced, so
  \[
  d_H(x,W)=d_H(y,W)=3,\quad
  \epsilon_x+\epsilon_y=1,\quad I_x=I_y=0.
  \]
  Both are therefore complete to the unique \(K_3\) component of \(H[W]\). Solving (1) gives exactly
  \[
  (a,\epsilon_x,\epsilon_y)=(3,1,0)
  \quad\text{or}\quad
  (4,0,1).
  \]

### Case \(\epsilon_U=2\)

The only profile is \((4,4,5,5)\) with no cross edge. Both \(x,y\) need at least four \(W\)-neighbours, while (2) bounds their sum by seven. Impossible.

We have proved the following strict reduction.

> **Augmentable-edge theorem.** If a non-four-partite \(L\) exists at \(\delta=14\) and it has at least one augmentable nonedge, then necessarily:
> - \(\epsilon_U=1\);
> - \(H[W]=K_3\dot\cup K_5\dot\cup K_5\dot\cup K_5\), with no cross edges;
> - the balanced Kang–Pikhurko profile \((7,7,7,7)\) occurs in \(L+uv\);
> - the exceptional vertices \(x,y\) are both complete to the \(K_3\) component;
> - \(uv\) is incident to neither \(x\) nor \(y\), and \((a,\epsilon_x,\epsilon_y)\) is either \((3,1,0)\) or \((4,0,1)\).

The leave table in DELTA15_SECOND_TURAN_PACKING.md has no \(P_3P_4\) leave edge, so \(uv\) is one of the listed cross-part leave types \(P_1P_2,P_1P_3,P_1P_4,P_2P_3,P_2P_4\). Since it is not incident to \(x,y\), at least one endpoint lies in \(P_1\) or \(P_2\setminus\{y\}\). That endpoint has \(d_H(z,W)=4\), hence is also complete to the \(K_3\) component. This adds a third vertex to the common neighbourhood of that \(K_3\).

## 6. What remains open

The follow-up theorem DELTA14_NONPARTITE_AUGMENTABLE_TERMINAL_CLOSURE.md eliminates the final \(\epsilon_U=1\), \(K_3\cup K_5^3\) augmentable-edge terminal by a four-component common-neighbour capacity argument. Thus, under the retained contracts, the only remaining \(\delta=14\), non-four-partite possibility is that \(L\) is \(K_5\)-saturated (no augmentable nonedge). The \(\delta\le13\) cases and all five E407 shell templates remain open. E407 Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
