# E408 Q32 — Case-I v=46 full-degree rigidity

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL** under the registered Q32, Type-I, full-color minimum-degree, and Case-I shell contracts.

## 1. Contract

Assume Case I of the Q32 shell split and |U|=46. Then W=H\U={w}. By `Q32_CASEI_LOW_SUPPORT_MATCHING_EXCLUSION.md`, if n=n_w is the number of exact colors whose Type-I special vertex is w, then

\[
\boxed{n\ge m-3},\qquad m\in\{8,9,10\}.
\]

For an exact color:

- if w is its Type-I special vertex, the source-verified degree is 9-a with a in {1,2,3,4}, hence at least 5;
- otherwise w belongs to a color K5, hence has color-degree at least 4.

The target residual degree is at least 13.

The nonexact-color edge-count distributions and registered minimum degrees are:

- m=8: three 130-edge colors, minimum degrees 3,3,3;
- m=9: one 130-edge and one 131-edge color, minimum degrees 3,2;
- m=10: one 132-edge color, minimum degree 2.

These follow from 1422 total non-target residual edges and the full-color degree theorem.

## 2. Degree inequality at the unique uncovered point

At w the exact colors contribute at least

\[
5n+4(m-n)=4m+n.
\]

Let L_m be the sum of the nonexact minimum-degree floors:

\[
L_8=9,\quad L_9=5,\quad L_{10}=2.
\]

Since all twelve color-degrees at w sum to 60,

\[
\boxed{13+(4m+n)+L_m\le60.}\tag{2.1}
\]

## 3. Exclude m=10

For m=10, Case I gives n>=7. Equation (2.1) yields

\[
13+40+7+2=62>60,
\]

contradiction.

Hence

\[
\boxed{\text{Case I},\ v=46\Longrightarrow m\ne10.}
\]

## 4. Rigidity for m=9

For m=9, Case I gives n>=6. Equation (2.1) gives

\[
13+36+n+5\le60,
\]

so n<=6. Therefore

\[
\boxed{n=6.}
\]

Moreover equality holds in every lower bound used in (2.1). Thus at w:

- target degree is exactly 13;
- the six exact colors with x_C=w give degree exactly 5;
- the other three exact colors give degree exactly 4;
- the 130-edge nonexact color gives degree exactly 3;
- the 131-edge nonexact color gives degree exactly 2.

For each of the six special exact colors, deg_C(x_C)=5 forces the Kang–Pikhurko parameter a=4.

### Shell matching refinement

The three non-special exact colors produce three pairwise vertex-disjoint M-edges at w. Since M[B]=empty and S=A\B has size three, a matching of size three must use all three vertices of S, one per edge.

No one of the three K5s containing w can be triple-shell. A shell triangle in Case I contains at least two vertices of S; the other two non-special colors would each require at least one further S-vertex, contradicting the disjointness of their shell neighbor sets at w.

Therefore all three are double-shell K5s. Their shell pairs are

\[
\boxed{\{s_1,b_1\},\{s_2,b_2\},\{s_3,b_3\}},
\]

where S={s_1,s_2,s_3} and b_1,b_2,b_3 are distinct vertices of B. In particular the three non-special exact colors use exactly six shell neighbors at w.

This is a rigid surviving terminal, not yet a contradiction.

## 5. The m=8 residue

For m=8, (2.1) gives n<=6 while Case I gives n>=5. Hence

\[
\boxed{n\in\{5,6\}.}
\]

- If n=6, equality holds in all degree floors: target degree13, all six special exact degrees5, the two non-special exact degrees4, and all three 130-edge colors degree3.
- If n=5, the total degree budget has exactly one unit of slack above those minima.
- In the n=5 subcase there are three non-special exact colors, so the same matching-size-three argument forces their K5s at w to be double-shell with shell pairs forming a perfect S-to-three-distinct-B matching.

## 6. Current Case-I frontier

Combining the Case-I matching theorem and this degree theorem:

- v=44: impossible;
- v=45: impossible;
- v=46,m=10: impossible;
- v=46,m=9: rigid equality terminal described above;
- v=46,m=8: n=5 or6 with the stated equality/slack structure;
- v=47: still open.

No 284-edge statement and no retracted degree-9 premise is used.