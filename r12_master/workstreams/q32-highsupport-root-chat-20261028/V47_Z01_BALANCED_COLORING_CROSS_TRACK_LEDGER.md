# E408 Q32 — balanced-coloring constraints on the aligned z=0,1 cross-track graph

Date: 2026-10-29  
Status: **PROVED_CONDITIONAL structural theorem with exact arithmetic regression.** No Q32 closure claimed.

## 1. Contract

Use the already established `V47_Z01_TRACK_ALIGNMENT.md` normal form. In the remaining aligned z=0,1 cells, H is partitioned into four target-color cliques
`T_1,T_2,T_3,T_0`
of sizes
`12,12,12,11`,
where each track consists of its ten pivot vertices plus its residual fiber of size 2,2,2,1. Their within-track edge total is
`3*C(12,2)+C(11,2)=253`.
Since `e(H)=285`, the number of H-edges between tracks is exactly 32.

The balanced-coloring contract says every 13-set contains every color. Equivalently, each of the eleven non-target color graphs C has `alpha(C)<=12).

## 2. Pairwise cross-track H-edge restriction

**Lemma 2.1.** For any two size-12 tracks T_i,T_j, the bipartite graph H[T_i,T_j] is a matching.

**Proof.** Fix v in T_j. The 13-set T_i union {v} already contains the target color on all pairs inside T_i. Each of the eleven non-target colors must therefore occur among the twelve edges from v to T_i. At most one of these twelve edges can be an H-edge. By symmetry, every vertex on either side has H-degree at most one into the other track. QED.

**Lemma 2.2.** For each size-12 track T_i, every vertex v in T_0 has at most one H-neighbor in T_i.

The same 13-set argument does not give a symmetric degree-one claim for vertices on the size-12 side of the T_0--T_i pair. In the aligned zero-slack contract, each non-small vertex of T_i has total cross-track H-degree one, so its T_0-H degree is at most one. The three small-block vertices A_i,B_i,C_i may have epsilon excess; their T_0-H endpoint multiplicities are controlled by that excess budget. Therefore H[T_0,T_i] is not necessarily a matching on the T_i side.

## 3. Exact vertex cross-degree ledger

Every outer (non-small) pivot vertex and every residual vertex has H-degree exactly 12 in the 3+7 zero-slack cell. A track T_h has 10 pivot vertices and n_h residual vertices, so its size is 10+n_h and every non-small vertex q in that track has cross-track degree
`12-((10+n_h)-1)=3-n_h`.
Thus every non-small vertex in T_1,T_2,T_3 has cross-track degree exactly 1, and every non-small vertex in T_0 has cross-track degree exactly 2.

The three small-block vertices A_i,B_i,C_i in track T_i have degrees 12+epsilon_A(i), 12+epsilon_B(i), 12+epsilon_C(i), hence cross-track degrees 1+epsilon_A(i), 1+epsilon_B(i), 1+epsilon_C(i). Their total excess is E_i=epsilon_A(i)+epsilon_B(i)+epsilon_C(i), so the sum of cross-track degrees over T_i is 12+E_i. Likewise the three small-block vertices in T_0 contribute total cross-degree 6+E_0, while its seven outer vertices and one residual vertex contribute 16, giving 22+E_0.

For h_i(v)=d_H(v,T_0), the endpoint multiplicities satisfy
\[
h_i(v)\le1\quad\text{for every non-small }v\in T_i,\qquad
\sum_{v\in T_i}\max(h_i(v)-1,0)\le E_i.
\]
Thus a repeated T_0-H endpoint can occur only at a small-block vertex, and its total multiplicity excess is bounded by E_i. This is the correct T_i-side restriction; H[T_0,T_i] need not be a matching on all of T_i.

There is an exact decomposition of this same excess budget. Put
\[
\ell_i(v)=d_H(v,T_j)+d_H(v,T_k),\quad
u_i=\sum_v\max(h_i(v)-1,0),\quad
k_i=\sum_v\max(\ell_i(v)-1,0),
\]
and let \(\omega_i=|\{v:h_i(v)>0,\ \ell_i(v)>0\}|\). Since \(h_i(v)+\ell_i(v)=1+\epsilon_i(v)\ge1\), the pointwise identity
\[
h_i(v)+\ell_i(v)-1
=\max(h_i(v)-1,0)+\max(\ell_i(v)-1,0)
+\mathbf 1_{\{h_i(v)>0,\ell_i(v)>0\}}
\]
sums to the exact constraint
\[
\boxed{E_i=u_i+k_i+\omega_i.}
\]
Here \(k_i\) is exactly the number of vertices shared by the endpoint sets of the two large-pair H matchings incident to \(T_i\), and \(\omega_i\) counts vertices simultaneously incident to a T0-H edge and a large-pair H edge. Both kinds of overlap, as well as repeated T0 endpoints, can occur only at small-block vertices and consume the same \(E_i\) budget.

For \(E_i=2\), the only possible budget splits are
\[
(u_i,k_i,\omega_i)\in\{(2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1)\}.
\]
This is an exact local constraint to enforce jointly with the common P matchings, not merely three separate upper bounds.


For a small-block vertex A_h in small block A, let e_A(h) be the number of extra A-to-outer edges incident to it. The degree equation is
`d_H(A_h)=9+e_A(h)+n_h=12+epsilon_A(h)`,
so
`e_A(h)=3-n_h+epsilon_A(h)`,
where `epsilon_A(h)>=0` and `sum_h epsilon_A(h)=2` for each of the three small blocks. Summed across the three small blocks, let E_h be the total epsilon at label h. Then
`sum_h E_h=6`.
The balanced-coloring pair restriction further gives `e_A(0)<=3`, hence each `epsilon_A(0)<=1` and
`E_0 in {0,1,2,3}`.

## 4. Cross-track edge counts forced by the degree ledger

Let
- `y_i=e_H(T_0,T_i)` for i=1,2,3;
- `x=e_H(T_1,T_2)+e_H(T_1,T_3)+e_H(T_2,T_3)).

Every vertex in T_0 has cross-track degree 2, except the E_0 small-block excess units, which increase its degree to 3. Therefore
`y_1+y_2+y_3=22+E_0`.
The total cross-track edge count is 32, so
`x=32-(22+E_0)=10-E_0`.
Consequently
`x in {7,8,9,10}` and `y_1+y_2+y_3 in {22,23,24,25}`.

For each i in {1,2,3}, let E_i be the total small-block excess at label i. Since the sum of cross degrees over T_i is `12+E_i`,
`e_H(T_i,T_j)+e_H(T_i,T_k)=12+E_i-y_i`
for {i,j,k}={1,2,3}. These equations, together with the pairwise matching property, form a compact finite normal form for the remaining aligned cells.

The global deficit identity is recovered without approximation:
`sum_{i<j<=3}(12-e_H(T_i,T_j)) + sum_{i=1}^3(11-y_i)=69-32=37`.
Each term is nonnegative by Lemmas 2.1–2.2. This is the same 37-unit global reserve budget, now localized into six track-pair deficits.

## 5. Exact arithmetic regression

The companion verifier enumerates every allowed small-block excess vector:
- `epsilon_A(0)<=1`;
- `epsilon_A(1),epsilon_A(2),epsilon_A(3)>=0`;
- `sum_h epsilon_A(h)=2`.

There are nine vectors per small block and 729 ordered triples for A,B,C. It verifies for every triple that `E_0<=3`, `x=10-E_0`, `y=22+E_0`, and `x+y=32). This is an arithmetic consistency check, not a search over all graph completions.

No external theorem is used beyond the frozen balanced-coloring premise that every 13-set contains every color. The result does not eliminate the aligned z=0 or z=1 completions; full-support Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.


## 6. Color-repeat conservation on each track pair

The same 13-set argument gives a color-by-color refinement.

### Two K12 tracks

Fix distinct i,j in {1,2,3}, and let `e_{ij}=e_H(T_i,T_j)). Since H[T_i,T_j] is a matching, exactly `r_{ij}=12-e_{ij}` vertices on each side are unmatched by an H edge into the opposite track.

For every unmatched vertex v, its twelve edges into the opposite K12 track are all non-target-colored. Since all eleven non-target colors must appear, exactly one color appears twice and the other ten appear once. For a vertex matched by an H edge, the remaining eleven edges must contain each non-target color exactly once.

For each non-target color C, define
`s_{C,ij}=e_C(T_i,T_j)-12`.
Then
`s_{C,ij}>=0`, `sum_C s_{C,ij}=r_{ij}), and **s_{C,ij} is exactly the number of unmatched vertices on either side whose repeated color is C**. In particular, the repeat-color counts on the two sides must agree color by color.

### One K11 and one K12 track

Fix i in {1,2,3}, and let `y_i=e_H(T_0,T_i)`. There are `11-y_i` unmatched vertices in T_0, since each T_0 vertex has at most one H edge into T_i. Each unmatched T_0 vertex repeats exactly one non-target color among its twelve edges into T_i. Thus, for each C,
`s_{C,0i}=e_C(T_0,T_i)-11>=0`,
and `s_{C,0i}` counts the unmatched T_0 vertices whose repeated color is C. Therefore
`sum_C s_{C,0i}=11-y_i`.
No symmetric repeat-count statement is claimed for the T_i side, because T_0 union {v} has only 12 vertices for v in T_i.

These pairwise repeat labels are the color-level constraints to add to any exact completion search. They are stronger than the aggregate 37-unit identity: the same color surplus must be realized by matching repeat labels on both sides of each K12--K12 pair.


### Corollary 6.1 — each large-track pair has at most nine H-edges

Write `e_{ij}=e_H(T_i,T_j)). For the remaining large label k, the degree identity gives
`e_{ij}=y_k-2-E_0-E_k`.
Since `y_k<=11`,
`\boxed{e_{ij}<=9-E_0-E_k<=9.}`
Thus each K12--K12 pair has at least three unmatched vertices on each side. More precisely, its deficit satisfies
`12-e_{ij}>=3+E_0+E_k`,
so the color-repeat conservation in Section 6 forces at least that many repeated-color vertices on each side of the pair.

This does not close the aggregate system, but it rules out any large-track pair with 10, 11, or 12 H-edges in the aligned z=0,1 cells.


## 7. Common residual factor across all three large-track pairs

For each pair \(T_i,T_j\), choose the Hall matchings \(M_{C,ij}\) simultaneously for the eleven non-target colors, and let \(P_{ij}\) be their complementary perfect matching. The choice of \(P_{ij}\) is not canonical, but **once the choices are fixed, the same \(P_{ij}\) is shared by all colors**. Every H-edge lies in \(P_{ij}\). Define the repeated-color set
\[
S_{ij}=P_{ij}\setminus E_H(T_i,T_j).
\]
Then
\[
|S_{ij}|=12-e_H(T_i,T_j)=r_{ij},
\qquad
\sum_{1\le i<j\le3}|S_{ij}|=26+E_0.
\]

Each \(P_{ij}\) is a perfect matching. Consequently the union \(S=S_{12}\cup S_{13}\cup S_{23}\) on the 36 vertices of \(T_1\cup T_2\cup T_3\) satisfies the exact vertexwise identity
\[
\boxed{d_S(v)=2-d_{H[T_1\cup T_2\cup T_3]}(v)\le2.}
\]
In particular, the repeated-color edges on the three large-pair tracks form one common graph of maximum degree two, not three independent capacity lists.

Every edge of \(S_{ij}\) is assigned to exactly one repeated non-target color. For an exact Type-I color \(C\), any edge assigned to \(C\) must have both endpoints in its residual gadget set, because the ten isolated K5 components have no C-edges to the gadget. In single-outside mode this is the (2,2,2,1) residual; in isolated-double mode it is the separate (2,2,2,2) residual. The ten-color aggregate witness in verify_v47_z01_aggregate_budget_witness.py satisfies the scalar counts but does not enforce these actual endpoint labels; it therefore is not a global completion.

This common max-degree-two edge-packing is the next constraint for the exact vertex-labelled CSP in V47_Z01_SHARED_P_FACTOR_PACKING.md. It is a stronger structural formulation, not a contradiction by itself.


## 8. Exact saturation of the 132-edge nonexact color in the aligned low-z cell

The new source-correct theorem V47_Z01_NONEXACT_GAP_SATURATION.md strengthens the aligned m=10,z=0,1 ledger. The outside-H lower bound 42+14=56, combined with the 132-edge total and e_D(H)=69+g_D, forces g_D=7. The 37-unit identity and the source-correct cap g_C<=3 then force g_C=3 for every exact color. The equality pattern on D[A] and O-T0 has only two cases: 2K2 with two zero-T0-neighbor vertices, or K3 with three. No Q32 closure is claimed.
