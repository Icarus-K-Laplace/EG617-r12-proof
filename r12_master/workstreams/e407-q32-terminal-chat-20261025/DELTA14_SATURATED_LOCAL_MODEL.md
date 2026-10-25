# E407 Q32: explicit local model for the \(\delta=14\) saturated boundary

Date: 2026-10-25  
Status: **LOCAL MODEL VERIFIED; not a global counterexample to EG617.** This construction shows that the 29-point saturated graph plus the 49-witness packing constraints alone do not force a contradiction.

## 1. The 15-vertex triangle-free saturated graph

Work in \(\mathbb Z_7\). Let \(J\) be the blow-up of a 5-cycle with consecutive parts
\[
X,\ Y,\ C,\ D,\ E
\]
of sizes \(5,5,2,1,2\), respectively. The edges are complete bipartite between consecutive parts only:
\[
XY,\ YC,\ CD,\ DE,\ EX.
\]
Then
\[
|V(J)|=15,\qquad e(J)=25+10+2+2+10=49.
\]
The graph is triangle-free and non-bipartite. It is triangle-saturated: every nonedge joins either two vertices in one blow-up part or vertices in parts at distance two on the 5-cycle, so it has a common neighbor.

Set
\[
H_U=K_7^A\ \dot\cup\ K_7^B\ \dot\cup\ \overline J,
\qquad L=\overline{H_U}.
\]
Then
\[
e(H_U)=21+21+\left(\binom{15}{2}-49\right)=98,
\quad \alpha(H_U)=1+1+\omega(J)=4,
\quad e(L)=406-98=308.
\]
The graph \(L\) is the complete join of two independent 7-sets \(A,B\) and \(J\). Because \(J\) is triangle-free, \(L\) is \(K_5\)-free. It is \(K_5\)-saturated:
- adding an edge inside \(A\) or \(B\), together with one vertex from the other 7-set and any edge of \(J\), creates a \(K_5\);
- adding any nonedge of \(J\) creates a triangle in \(J\), which together with one vertex from each of \(A,B\) creates a \(K_5\).

Moreover \(\chi(J)=3\), so \(\chi(L)=1+1+3=5\); thus \(L\) is non-four-partite. This realizes the exact 29-point, 98-edge complement boundary in the saturated non-four-partite branch.

## 2. Explicit 49-witness labeling

Label the two 7-sets by \(A=\{a_x:x\in\mathbb Z_7\}\) and \(B=\{b_y:y\in\mathbb Z_7\}\). Each of the 49 cells \((x,y)\in\mathbb Z_7^2\) will label one edge of \(J\).

Put
\[
i=y-x\pmod 7,\qquad j=y-2x\pmod 7,
\]
with
\[
S_A=\{0,1,2,3,4\},\qquad S_B=\{0,1,2,4,5\}.
\]
The cell-to-edge rule is:
- if \(i\in S_A\) and \(j\in S_B\), use the edge \(X_iY_j\);
- if \(i\in S_A\), \(j\notin S_B\), use the \(X_i\)-to-\(E\) edge in Table 1;
- if \(i\notin S_A\), \(j\in S_B\), use the \(Y_j\)-to-\(C\) edge in Table 2;
- otherwise use the \(D\)-to-\(C/E\) edge in Table 3.

Table 1. The two exceptional cells for each \(X_i\); first cell goes to \(E_1\), second to \(E_2\).

| Vertex | Cell for \(E_1\) | Cell for \(E_2\) |
|---|---|---|
| \(X_0\) | \((1,1)\) | \((4,4)\) |
| \(X_1\) | \((2,3)\) | \((5,6)\) |
| \(X_2\) | \((3,5)\) | \((6,1)\) |
| \(X_3\) | \((4,0)\) | \((0,3)\) |
| \(X_4\) | \((5,2)\) | \((1,5)\) |

Table 2. The two exceptional cells for each \(Y_j\); first cell goes to \(C_1\), second to \(C_2\).

| Vertex | Cell for \(C_1\) | Cell for \(C_2\) |
|---|---|---|
| \(Y_0\) | \((5,3)\) | \((6,5)\) |
| \(Y_1\) | \((4,2)\) | \((5,4)\) |
| \(Y_2\) | \((3,1)\) | \((4,3)\) |
| \(Y_4\) | \((1,6)\) | \((2,1)\) |
| \(Y_5\) | \((0,5)\) | \((1,0)\) |

Table 3. The four remaining cells.

| Cell | Edge |
|---|---|
| \((2,0)\) | \(DC_1\) |
| \((0,6)\) | \(DC_2\) |
| \((6,4)\) | \(DE_1\) |
| \((3,2)\) | \(DE_2\) |

The verifier checks that this is a bijection from the 49 cells to \(E(J)\). For every vertex \(v\in V(J)\), its incident cells have pairwise distinct first coordinates, second coordinates, and values of
\[
\kappa=x+y\pmod 7.
\]

For a cell \((x,y)\) whose assigned edge is \(uv\in E(J)\), define
\[
Q_{x,y}=\{a_x,b_y,u,v\}.
\]
Every \(Q_{x,y}\) is an independent 4-set in \(H_U\), equivalently a \(K_4\) in \(L\). The 49 sets:
- cover all 29 vertices;
- pairwise intersect in at most one vertex, so their \(K_4\)'s are edge-disjoint;
- split by \(\kappa=x+y\pmod 7\) into seven classes of seven pairwise vertex-disjoint witnesses.

Indeed, for fixed \(\kappa\), the cells \(x+y=\kappa\) form a perfect matching of the \(A\)-\(B\) pairs, and the corresponding edges of \(J\) form a matching. This is exactly the local witness-packing shape that a proposed core-only contradiction would need to exclude.

## 3. What this construction does and does not prove

It **does** prove that the following local constraints are mutually compatible:
\[
|U|=29,\quad e(H_U)=98,\quad \alpha(H_U)=4,\quad
e(L)=308,\quad L\text{ is }K_5\text{-saturated and non-four-partite},
\]
together with 49 pairwise-linear independent 4-sets partitioned into seven classes of seven disjoint sets.

It **does not** construct the remaining 18 vertices \(W\), the full 47-vertex core \(H\), the 13-vertex shell, or the required shell-row labels. It is therefore not a counterexample to the original coloring problem and does not refute the five-template reduction.

For the zero-excess-on-\(U\) version of the full-core contract, this model fixes the required \(U\)-to-\(W\) degrees to
\[
6^{14},\quad 5^{10},\quad 4^4,\quad 2^1,
\]
because the degrees of \(J\) are \(7^{10},6^4,4^1\). Their sum is \(152\), matching the \(\delta=14,\epsilon_U=0\) cross-edge budget. Whether these degree demands can be completed while satisfying all core independence, clique, and shell-row constraints remains open.

## 4. Research consequence

The proposed next lemma “no triangle-free saturated 15-vertex graph with 49 edges admits the required orthogonal matching structure” is **false**: this explicit blow-up of \(C_5\) and cell labeling realize it, including the third coloring \(\kappa=x+y\pmod7\).

The next attack must use the full \(W\)-incidence and shell-row constraints, not only the 29-point saturated graph and its 49 witnesses. Status of E407 Q32 and EG617(\(r=12\)) remains **OPEN / NOT_CERTIFIED**.
