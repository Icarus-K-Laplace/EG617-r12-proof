# M10 4+6 K4-e, Z=4 — global residual and cross-grid closure

Date: 2026-10-30  
Status: **PROVED_CONDITIONAL** under the registered 47-core contract and the inherited parent bound omega(H)<=11. The finite residual-map catalog and cut geometry are independently replayed.

## 1. Theorem and exact scope

Assume the disconnected ten-block light graph has a 4+6 split. Let S be its four-block component and T its six-block component. Assume the light graph on S is K4-e and the residual slack is Z=4.

Then the entire 4+6, K4-e, Z=4 cell is impossible, for every residual fiber profile and every six-column matching/extra-edge pattern.

The hypotheses used are:
- |H|=47, e(H)=285, alpha(H)<=4, delta(H)>=12;
- ten disjoint independent pivot blocks, each of order four, and a residual set R of order seven;
- the registered 4+6 slack ledger and the exact 4,5,5 and corrected 5,5,5 local theorems;
- omega(H)<=11 inherited from the 61-point parent residual: H is an induced 47-vertex subset of that residual, whose parent contract has clique number at most 11. This is not inferred from the 285-edge core alone.

This does not close:
- the K4 small-component branch;
- the K4-e branches Z=1,2,3;
- the other disconnected component sizes;
- connected L;
- full-support m=10 Q32 or the EG617 root.

## 2. Z=4 saturation and residual graph

Write the four small blocks as A,B,C,D, with AB the unique heavy pair inside S. Write the outer blocks as E_1,...,E_6, and let M be their internal heavy-pair graph.

The registered 4+6 ledger gives, in the K4-e case,
\[
2X_S+\delta_{ST}+Y_S\le2.
\]
Since X_S=1, this forces delta_ST=Y_S=0. Thus:
- all 24 small-to-outer pairs have exactly five edges;
- the six-block internal heavy graph is a matching, with X_T=Z-1;
- Y=8-2Z.

At Z=4, M is a perfect matching on the six outer labels and Y=0. Every residual vertex has at least one neighbor in every pivot block, since otherwise it together with that independent four-block would be an independent five-set. The total residual-to-block edge count is therefore exactly 70, so every residual vertex has exactly one neighbor in each of the ten blocks.

Also e(H[R])=3+Z=7. Each residual vertex has ten pivot-block neighbors and total degree at least 12, hence degree at least two in H[R]. Since the residual degree sum is 14, every residual vertex has degree exactly two. Therefore
\[
H[R]\cong C_7\quad\text{or}\quad C_3\dot\cup C_4.
\tag{2.1}
\]

## 3. Aligning the ten internal matching systems and the residual maps

Every pair of pivot blocks has either four or five edges and therefore a unique perfect matching. The light graph on S is K4-e; the outer light graph is K6-M, the complete tripartite graph with three parts of size two. In both graphs every pair of block labels has a common light neighbor.

The two-light matching-composition theorem says that if X-Z and Y-Z are light matching pairs, then the composed matching is present in X-Y. On every light triangle, all three pairs have exactly four edges, so the composed matching must equal the unique matching on the third side. The triangle boundaries generate the cycle space of each light graph: K4-e is the union of triangles ACD and BCD, while K6-M is the octahedral graph whose eight face triangles span its cycle space. Thus path products are independent of the chosen path, and all matching systems align within S and, independently, within T. Relabel the four vertices of every small block and every outer block so that all internal base matchings are identity.

For each block Q_i, the zero-slack condition gives a unique-neighbor map f_i:R->[4]. Its fibers are cliques in H[R]: if two nonadjacent residual vertices shared a block neighbor, the other three vertices of that independent block together with the residual pair would be an independent five-set.

We use the following zero-slack map-alignment lemma. If X,Y are independent four-sets joined by a perfect matching and every r in R has exactly one neighbor in each, then after matching alignment f_X=f_Y. Indeed, for every independent pair r,s, the unordered pair of their labels in X must equal the unordered pair in Y; otherwise the two X-labels outside the first pair, together with r,s and the unmatched Y-label, form an independent five-set. Fix r. Among its at least four nonneighbors in R choose two, s,t, that are nonadjacent to each other; such a pair exists because Delta(H[R])<=2. The labels f_X(s),f_X(t) are distinct and both differ from f_X(r). Applying the unordered-pair identity to (r,s) and (r,t) forces f_Y(r)=f_X(r).

The light graphs on S and T are connected, so the maps agree within each side. Denote the common small-side map by F:R->[4] and the common outer-side map by G:R->[4]. Every fiber of F or G is a clique in H[R].

The possible sorted nonempty fiber profiles are:
- for C7: (2,2,2,1);
- for C3 dot-union C4: (3,2,2), (3,2,1,1), or (2,2,2,1).

The profile (3,2,2) means (3,2,2,0), with one empty label.

## 4. Exact pointwise degree equations

Every outer block vertex has degree exactly 12. Its degree sum over the four vertices of E_j is 36 from the nine base matching incidences, plus seven residual incidences, plus five extra incidences (four small-to-outer cross edges and its one internal-heavy edge), totaling 48. Since every vertex has degree at least 12, equality holds pointwise.

For an outer block E_j, let m_t=|G^{-1}(t)|, let alpha_j be the endpoint label of its internal-heavy edge, and let c_j(t) count the four small-to-outer extra edges ending at label t. Then
\[
c_j(t)=3-m_t-\mathbf 1_{\{t=\alpha_j\}}\le3.
\tag{4.1}
\]

For a small block Q_i, let n_t=|F^{-1}(t)| and let c_i(t) count its six cross-extra edges starting at label t. In C,D, which have no internal-heavy edge,
\[
d_H((Q_i)_t)=9+n_t+c_i(t).
\tag{4.2}
\]
In A, if a is the endpoint in A of the unique extra edge on AB,
\[
d_H(A_t)=9+n_t+c_A(t)+\mathbf 1_{\{t=a\}}.
\tag{4.3}
\]

In particular, whenever the small profile is (3,2,2,0), write r for the size-3 label, u,v for the size-2 labels, and z for the empty label. Equations (4.2)-(4.3) give
\[
c_C(z),c_D(z)\ge3,\qquad
c_C(u),c_C(v),c_D(u),c_D(v)\ge1,
\tag{4.4}
\]
and
\[
c_A(t)+\mathbf 1_{\{t=a\}}\ge3-n_t.
\tag{4.5}
\]

## 5. Necessary two-block residual-incidence catalog

Fix one small block Q and one outer block E. Their pair graph has exactly five edges: a unique perfect matching p:Q->E and one off-matching extra edge. Normalize E by p^{-1}, so the base matching is identity. Let f,g:R->[4] be the common small- and outer-side residual maps and put h=p^{-1} composed with g.

For every independent pair {r,s} in R, define
\[
U=[4]\setminus\{f(r),f(s)\},\qquad
V=[4]\setminus\{h(r),h(s)\}.
\]
Both sets have size two. To avoid an independent five-set, the bipartite graph induced between U and V must contain a matching of size two: otherwise König's theorem gives an independent three-set across the two blocks, which together with r,s is an independent five-set. Since the block-pair graph is the identity matching plus one extra edge, this is possible only if:
- U=V; or
- U,V differ by one label each, and the extra edge is the unique edge from U\setminus V to V\setminus U.

If U and V are disjoint, the cell is impossible.

For every independent triple S in R, the three labels used by F and by G are distinct, because each fiber is a clique. Thus one label remains available in each block; these two remaining vertices must be adjacent, or together with S they form an independent five-set.

The companion verifier exhausts every map R->[4], every p in S_4, and all independent pairs and triples of R. This is deliberately a necessary-condition catalog: it may retain a cell edge that a larger independent-set test would later remove, but it contains every actual cell.

| Residual graph | Clique-fiber maps | Compatible ordered (F,G) pairs | Pair/triple-compatible cell states |
|---|---:|---:|---:|
| C7 | 168 | 12,096 | 56,448 |
| C3 dot-union C4 | 288 | 29,952 | 120,960 |

The map-pair classification is:

| Residual maps | Ordered map pairs | Necessary cell-state form |
|---|---:|---|
| C7, both full and aligned | 4,032 | one matching p0; 12 off-matching extra-edge choices survive the pair/triple test |
| C7, both full and nonaligned | 8,064 | one matching and one forced extra edge |
| C3 dot-union C4, both full and aligned | 5,760 | one matching p0; 12 choices survive the pair/triple test |
| C3 dot-union C4, both full and nonaligned | 11,520 | one matching and one forced extra edge |
| small map empty, outer map full | 5,760 | two matchings; every forced extra edge starts at the small empty label |
| small map full, outer map empty | 5,760 | two matchings; every forced extra edge ends at the outer empty label |
| both maps empty | 1,152 | only the same residual partition; one aligned matching plus three forced switches |

When both maps have an empty fiber, their partitions must coincide. After aligning them, write the common profile as (3,2,2,0), with empty label z and occupied labels r,u,v. The pair/triple catalog allows exactly:
1. p=p0, with any of the 12 off-matching extra edges surviving these tests;
2. p=p0 tau_k for k in {r,u,v}, with the extra edge joining the two empty-label vertices z and z' in the original block labels.

Here tau_k is the transposition (z k). The aligned-cell statement is only that the pair/triple tests leave the 12 choices; no claim is made that all 12 pass every larger independent-set test.

## 6. All residual-map cases except the common empty partition are impossible

### 6.1 Both maps full

If F,G are full and nonaligned, the local catalog gives the same unique matching and the same forced extra edge in every one of the 24 cross cells. In any outer column, all four cross-extra edges therefore end at the same outer vertex. This gives c_j(t)=4, contradicting (4.1).

If F,G are full and aligned, every cross matching is p0. Together with the internal matching alignment, all ten pivot blocks contain four global K10 tracks. Since seven residual vertices are mapped into four nonempty fibers, some F-fiber has size at least two. That fiber is a clique and every one of its vertices is adjacent to all ten vertices of the corresponding track. This gives a K12, contradicting omega(H)<=11.

### 6.2 Small map empty, outer map full

The local catalog forces every cross-extra edge to start at the same empty small-side label z. In either C or D, the two size-2 fiber vertices then have no cross-extra incidence. Each has degree 9+2=11 by (4.2), contradicting delta(H)>=12.

### 6.3 Small map full, outer map empty

The local catalog forces every cross-extra edge to end at the empty outer label z'. Thus each outer column has c_j(z')=4, contradicting (4.1).

Consequently, the only remaining map case is that F and G have the same empty-fiber partition (3,2,2,0).

## 7. The common-empty-fiber six-column grid is impossible

Align the common residual partition and the internal base matchings. Let z,z' be the empty small/outer labels, u,v the two size-2 labels, and r the size-3 label. Let P be the aligned small-to-outer matching, so P(z)=z' and P(k)=k' for each occupied label k.

By Section 5, every cross-cell matching is either:
- aligned, p0=P; or
- switched, p0 composed with tau_k for one occupied label k in {r,u,v}, with its extra edge equal to (z,z').

For a fixed small row, any two outer columns form either a 4,5,5 triangle (if their outer pair is light) or a corrected 5,5,5 triangle (if their outer pair is heavy). Both local theorems imply that the relative matching is identity or a transposition. Therefore all switches in a fixed row use one common k: two distinct transpositions (z k) and (z l) have a 3-cycle as their product, which is forbidden.

Let S be the switched columns in a row and s=|S|. The outer light graph is K6-M. Its cut between S and its complement has this exact form:
- for s=2,3,4, the cut graph is connected;
- for s=1, one aligned column (the heavy-matched partner) is isolated and the other five columns form a connected component;
- for s=5, one switched column (the heavy-matched partner) is isolated and the other five columns form a connected component.

On every light edge crossing this cut, the 4,5,5 switch theorem forces the extra-edge target labels at the two columns to agree. More explicitly, if p_j=P tau_k and p_l=P, applying the theorem to the light pair E_j,E_l with common block Q_i gives e_{Q_iE_j}=(z,z') and e_{Q_iE_l}=(k,z'). Thus on the connected component the row sources are z in switched cells and k in aligned cells. For s=5, the isolated switched cell also has source z by the cell classification. For s=1, only the isolated aligned cell is unconstrained by the cut.

### 7.1 The rows C,D cannot switch

For either C or D, the degree requirements are (4.4). If s=1, the connected component contributes only one z-source and the isolated aligned cell can contribute at most one more, so c_i(z)<=2<3. If s=2, the cut is connected and c_i(z)=2<3. If s=3,4,5, all sources lie in {z,k}, leaving at least one of u,v with zero incidence. If s=6, all six sources are z, again leaving u,v uncovered. Hence both C,D rows are aligned in all six columns.

### 7.2 Neither A nor B can switch

Consider row A, and let a be the endpoint in A of the unique extra edge AB. Its degree requirements are (4.5).

If s=1, the connected component contributes one z-source and four k-sources; the isolated aligned cell contributes at most one additional source. If a is not z, the empty label requires c_A(z)>=3, impossible. If a=z, the one free edge cannot both raise c_A(z) to two and supply both size-2 labels u,v. Thus s=1 is impossible.

If s=2, the connected cut gives exactly two z-sources and four k-sources. If a=z, both u,v still require positive incidence but only one source label is k; if a is not z, the empty label requires at least three incidences but has only two. Thus s=2 is impossible.

If s=3,4,5, all row sources lie in {z,k}. To meet both size-2 degree requirements, k must be one of u,v and a must be the other. In particular, a is outside the support {z,k} of tau_k. If s=6, all six sources are z, leaving at least one of u,v uncovered. Therefore any nonempty switch set in row A would have s in {3,4,5}, with k and a the two size-2 labels.

Now fix a switched column j of row A. Then p_Aj=P tau_k and e_Aj=(z,z'). Since C and D are aligned, the 4,5,5 theorem on the light pairs AC and AD gives
\[
e_{Cj}=e_{Dj}=(z,P(k))=(z,k').
\tag{7.1}
\]
In particular, both C and D contribute to c_j(k').

The corrected 5,5,5 theorem on the heavy triangle A,B,E_j says that p_Bj can only be P or P tau_k: any P tau_l with l!=k would give the forbidden 3-cycle tau_k tau_l.

- If p_Bj=P tau_k, its cell is switched, so e_Bj=(z,z'). Equation (7.1) then gives c_j(k')>=2.
- If p_Bj=P, normalize E_j by p_Aj^{-1}. The relative matching is tau_k and e_Aj becomes (z,k) in normalized labels. Since a is outside {z,k}, the AB extra edge is in the “other ten” class of the corrected 5,5,5 classifier. That classifier forces the normalized B-E_j extra edge to be (z,z). Undoing the normalization gives e_Bj=(z,P(k))=(z,k'), so c_j(k')>=3.

But k' has outer residual-fiber size m_{k'}=2. The exact outer degree equation (4.1) gives c_j(k')<=1. Both alternatives are impossible. Hence row A has no switches.

The same argument with A and B interchanged, using the B-endpoint of the AB extra edge, shows that row B has no switches either.

All four small rows are therefore aligned in all six columns. Every one of the ten pivot blocks now shares the same four matching tracks. Choose either size-2 residual fiber. Its two vertices are adjacent to each other and to all ten vertices of the corresponding track, producing a K12 and contradicting omega(H)<=11.

## 8. Conclusion and firewall

The entire 4+6, K4-e, Z=4 cell is **CLOSED**. The proof covers:
- R=C7 and R=C3 dot-union C4;
- every possible pair of small/outer residual clique-fiber maps;
- every 24-cell cross matching/extra-edge grid satisfying the registered local theorems and degree constraints.

The independent verifier checks the complete pair/triple necessary residual-map catalog and all six-column cut-graph shapes, together with the specific corrected 5,5,5 endpoint branch used in Section 7.2. The global grid contradiction is analytic; no full 4-by-6 SAT solver or 47-vertex Q32 SAT/UNSAT run is claimed.

The K4 small-component branch and the K4-e, Z=1,2,3 branches remain OPEN. Full-support m=10 Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
