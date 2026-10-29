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

The same 13-set argument applies to T_i union {v}; no symmetric degree-one claim is made for vertices on the size-12 side of the T_0--T_i pair. This asymmetry matters and must not be silently strengthened to a matching.

## 3. Exact vertex cross-degree ledger

Every outer pivot vertex and every residual vertex has H-degree exactly 12 in the 3+7 zero-slack cell. A track T_h has 10 pivot vertices and n_h residual vertices, so its size is 10+n_h and every non-small vertex q in that track has cross-track degree
`12-((10+n_h)-1)=3-n_h`.
Thus:
- every outer/residual vertex in T_1,T_2,T_3 has cross-track degree exactly 1;
- every outer/residual vertex in T_0 has cross-track degree exactly 2.

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
