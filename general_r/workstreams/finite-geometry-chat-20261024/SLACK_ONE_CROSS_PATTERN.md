# Simultaneous Slack-One Cross Pattern

Status: **PROVED for q>=3; a rigid local pattern, not a contradiction**.

## Setup

Let a hypothetical counterexample to P(q) be given. Fix x and W=V minus {x}, with |W|=q^2 and q>=3. Suppose two distinct colors i,j have

\[
s_i(x)=s_j(x)=1.
\]

By low-slack coordinatization, G_i[W] is a union of q color-i clique blocks (rows) plus one color-i defect edge; G_j[W] is a union of q color-j clique blocks (columns) plus one color-j defect edge. The row and column partitions are orthogonal.

For each row A_a, define B_a={v in A_a : xv is not color i}; for each column C_b, define D_b={v in C_b : xv is not color j}. Every B_a,D_b is nonempty.

## Theorem K.S1 — Exact two-row/two-column pattern

There are two rows A_1,A_2 and two columns C_1,C_2 with the following properties:

1. B_1={u_1} and B_2={u_2}; all other rows may have larger B_a.
2. The unique color-i defect edge is u_1u_2, and u_1,u_2 lie in distinct columns.
3. D_1={v_1} and D_2={v_2}; the unique color-j defect edge is v_1v_2, and v_1,v_2 lie in distinct rows.
4. The two exceptional rows and two exceptional columns are paired in a crossed pattern. After relabeling the four cells:
   - the two i-exception cells are (A_1,C_1) and (A_2,C_2), and both have x-edge color j;
   - the two j-exception cells are (A_1,C_2) and (A_2,C_1), and both have x-edge color i.
   - the unique i-defect edge joins the two i-exception cells; the unique j-defect edge joins the two j-exception cells.

Thus the four cells form a crossed 2-by-2 pattern: the i-defect and j-defect edges occupy opposite diagonals, while row edges are color i and column edges are color j.

### Proof

Every choice of one point from each B_a must contain a color-i edge; otherwise those q points together with x form a (q+1)-set missing color i. The only available cross-block color-i edge is the unique defect edge. To hit every transversal, its endpoints must lie in two distinct rows whose B-sets are singletons; otherwise a choice can avoid an endpoint. This proves (1) and (2). The same argument proves (3) for j.

Because the partitions are orthogonal, the i-defect endpoints cannot lie in the same j-column, and the j-defect endpoints cannot lie in the same i-row.

Now consider any intersection of one of the two exceptional rows and one of the two exceptional columns. If the cell is not the unique non-i point of its row, its x-edge must be color i. If it is not the unique non-j point of its column, its x-edge must be color j. These two requirements cannot hold simultaneously. Therefore, for every such row-column pair, either it is the row's i-exception cell or the column's j-exception cell. Since both exceptional row columns and exceptional column rows are distinct, the two matchings must cross. The row-exception cells are not column-exception cells, so their x-edges are color j; the column-exception cells have x-edges color i. The two unique defect edges join the respective exceptional points. QED.

## Corollary K.S2 — Excess lower bound

Write e_i=m_q+q+a_i, where m_q=q*C(q,2), and use

\[
s_i(x)=q+a_i-d_i(x).
\]

Each of the two exceptional i-rows has q-1 color-i edges to x. Hence d_i(x)>=2(q-1), and since s_i(x)=1,

\[
\boxed{a_i\ge q-1.}
\]

Likewise,

\[
\boxed{a_j\ge q-1.}
\]

Thus simultaneous local slack one forces both colors to have global excess at least q-1.

## Audit boundary

This is a necessary local pattern, not a contradiction. The other cross-grid edges can use colors outside {i,j}; the theorem does not assert that only two colors occur on W. It does not imply a third direction or an affine plane.

## Round 2 contract audit — empty premise under full counterexample

The crossed-pattern implication is valid as a conditional structural statement, but the new theorem `HIGH_SLACK_COMPATIBILITY.md` proves `s_i(x)>=q-1` for every color and vertex under the full counterexample contract. Consequently the premise `s_i(x)=s_j(x)=1` is impossible for q>=3. The crossed pattern is therefore vacuous in a full hypothetical counterexample and is not evidence that such a pattern can be realized. The new proof uses the q+1-set block-plus-x condition in addition to the blocker lemma.
