# E407 Q32 — four-partite support transversal gap lemma

Date: 2026-10-28  
Status: **PROVED_ANALYTIC** under the frozen `(7,7,7,8)` support design. This is a reusable pure-incidence theorem; no E407 closure is claimed here.

## 1. Frozen support design

Assume
\[
U=T_1\dot\cup T_2\dot\cup T_3\dot\cup R,
\qquad |T_i|=7,\quad |R|=8,
\]
and the 49 support blocks form the exact transversal system supplied by `DELTA12_FOURPARTITE_SUPPORT_KERNEL.md`:

- every support block contains exactly one point from each T_i and one point from R;
- every point t in T_i lies in exactly seven support blocks;
- support blocks are pairwise linear;
- every w in W meets every support block.

## 2. Seven-outside-neighbours lemma

Fix w in W and one T_i. Put
\[
k=|N_U(w)\cap T_i|.
\]
If k<7, then
\[
\boxed{|N_U(w)\setminus T_i|\ge7.}
\tag{2.1}
\]
Consequently
\[
\boxed{d_U(w)\ge k+7.}
\tag{2.2}
\]

### Proof

There are 7-k points t of T_i not adjacent to w. Each such t lies in seven support blocks, so there are exactly
\[
7(7-k)
\]
support blocks whose T_i point is outside N_U(w).

Every one of those blocks must still meet N_U(w), because w hits every support block. Its witnessing neighbour must lie outside T_i.

Fix u in U\T_i. By pairwise linearity, for each fixed t in T_i the pair {t,u} occurs in at most one support block. Therefore u belongs to at most 7-k of the `7(7-k)` blocks under consideration: at most one for each missing T_i point.

Thus at least
\[
\frac{7(7-k)}{7-k}=7
\]
distinct outside-T_i neighbours are necessary. QED.

## 3. Gap consequences at epsilon_U=2

In the delta=12 four-partite epsilon_U=2 branch, the total W-excess is
\[
\epsilon_W=2.
\]
Every listed W profile has minimum W-internal degree at least two. Hence, for every w in W,
\[
d_U(w)=12+\epsilon_w-d_W(w,W)\le12.
\tag{3.1}
\]
Combining with (2.2):

1. **Six-neighbour gap.** If `|N_U(w) cap T_i|>=6`, then w is actually complete to T_i. Indeed k=6 would give d_U(w)>=13.
2. **Five-neighbour exception.** If `|N_U(w) cap T_i|=5`, then d_U(w)=12 is forced. Therefore
   \[
   \epsilon_w=2,\qquad d_W(w,W)=2.
   \tag{3.2}
   \]
   In particular there is at most one such exceptional w, because it carries both W-excess units. It must be a W-internal degree-two vertex.
3. If d_U(w)<=11, then w cannot have exactly five or six neighbours in a T_i: any `>=5` forces all seven.

These statements use only the support design and the two-unit W-excess ledger, not the shell templates or any external extremal theorem.

## 4. Application to low-omission R points

For r in R, let q=r_r be its omission weight. In each T_i, exactly q support-pair leaves are incident with r. Let h_i(r) be the number of those q leave pairs that are target edges. Put
\[
h_r=h_1(r)+h_2(r)+h_3(r).
\]
Then
\[
A_i(r):=T_i\setminus N_H(r)
\]
has size
\[
|A_i(r)|=7-h_i(r).
\tag{4.1}
\]

If w is H-nonadjacent to r, then w must be complete to at least one A_i(r). Otherwise choose t_i in A_i(r) nonadjacent to w; since the T_i are pairwise H-anticomplete, the five vertices `r,w,t1,t2,t3` would be independent.

If q<=2, then h_i<=2. Hence:
- h_i=0: w is complete to T_i;
- h_i=1: w sees six points of T_i and the gap lemma upgrades this to all seven;
- h_i=2: w sees five points of T_i; this also upgrades to all seven except possibly for the unique degree-two W vertex carrying both W-excess units.

This is the exact interface used by `DELTA12_FOURPARTITE_EPS2_CLOSURE.md`.