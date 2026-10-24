# Complete symbolic ledger for the requested offsets

Date: 2026-10-24. Status: **PROVED** for all formulas and stated exclusions.

Use c=2r-|W|, epsilon=delta(F)-r, and eta=e_2+e_3 in the original
anchor degree pattern
(r+epsilon,r+epsilon+e_2,r+epsilon+e_3), e_2,e_3 in {0,1}.

## 1. Exact original-triple table

Let O=V\W, O'=V\(W union T). Then

    |O|=3r+c+1, |O'|=3r+c-2,
    sum_(t in T)d_F(t)=3r+3epsilon+eta,
    D_3=3epsilon+eta-c+2.

Every vertex of O' has at least one T-neighbor by the DEFINITION of W.
If n_2,n_3 vertices have two or three T-neighbors, then
n_2+2n_3=D_3. No extra premise is required for that covering fact.

|epsilon|c|allowed eta by D_3>=0|D_3|W-color excess upper bound|
|---:|---:|---|---|---|
|0|2|0,1,2|eta|r-1|
|0|3|1,2|eta-1|r-1|
|0|4|2|0|r|
|1|2|0,1,2|3+eta|r-1|
|1|3|0,1,2|2+eta|r-1|
|1|4|0,1,2|1+eta|r|
|1|5|0,1,2|eta|r+1|
|1|6|1,2|eta-1|r+3|
|1|7|2|0|r+5|

These are all nine requested degree/offset cells. They are necessary
symbolic possibilities, not graph existence certificates.

## 2. Exact W-local defect and matching table

For every non-target color let t_i=e(G_i[W])-(r-c).
Then t_i>=0 and sum t_i<=r+floor(c^2/4)-c.
Some color has t_i<=1 when r>=8.

For that color the complete sparse possibilities are:

|t_i|nontrivial components|number of isolates|matching size|
|---:|---|---:|---:|
|0|(r-c) copies of K2|c|r-c|
|1|(r-c+1) copies of K2|c-2|r-c+1|
|1|one P3 and (r-c-1) copies of K2|c-1|r-c|
|1|one P4 and (r-c-2) copies of K2|c|r-c|

Here P3/P4 denote paths on three/four vertices. Nonnegative component
counts hold throughout r>=67. The proof of exhaustion is the
e-tau<=1 component argument in THEOREM.md, not a solver run.

## 3. Whole-terminal defects and budgets

The inherited contextual cap gives total degree excess

    sum(d_F-r)<=6r+18       (epsilon=0),
    sum(d_F-(r+1))<=r+17    (epsilon=1).

The five-anchor extension produces a kernel of size m<=10+eta.
With b_i=r-1-d_i, sum d_i=m-6, write

    L=sum_i binom(b_i,2), h=e_F(H),
    A_C=sum_(i<j)e_F(C_i,C_j), B_C=e_F(H,V\H).

The exact target ledger is

    e(F)=L+A_C+B_C+h <=(5r^2+7r+18)/2,
    B_C>=m(r+epsilon)-2h,
    A_C>=0.

Thus

    A_C <= (5r^2+7r+18)/2 -L-m(r+epsilon)+h.

This is an actual-edge budget; A_C has not been set to zero.
For each non-target color, its internal kernel defect is
e_i=e(G_i[H]), its independent kernel demand is alpha(G_i[H]),
and every clique C_j requires

    |N_(G_i)(R_i) intersect C_j| >= |R_i|+b_j-r

for every color-i independent R_i subset H.
Summation gives the uniform unique-edge capacity theorem.

## 4. Thresholds, with no extrapolation from finite samples

|eta|kernel maximum|low branch excluded for all r>=|high branch excluded for all r>=|
|---:|---:|---:|---:|
|0|10|162|152|
|1|11|190|179|
|2|12|221|209|

These thresholds use the common r>=67 contract. In every table entry
the stated exclusion range is larger than 67, so the matching and
five-anchor inequalities have already been justified.

For all nine offset cells, status is PROVED for r>=221.
The entire high branch is additionally PROVED for 209<=r<=220.
For any smaller r, apply the eta- and m-specific bounds rather than
silently assigning a stronger result. The remaining cells at r>=67
are OPEN, not realized counterexamples.

