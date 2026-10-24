# Audit of the latest witness-transversal boundary theorem

Date: 2026-10-25  
Status: **Transversal floor and integer edge budgets PROVED_CONDITIONAL; non-four-partite conclusions NOT ESTABLISHED.**

Sibling source audited: ultimate-closure head 78c30e86b0f432464ca5375695da97a27b230878, file R12_WITNESS_TRANSVERSAL_BOUNDARY_THEOREM.md.

## 1. Independently checked theorem: transversal number at least seven

Let \(\mathcal Q\) be a linear family of m independent four-sets in U, where |U|=v. Linearity means two distinct sets intersect in at most one point. The two boundary values are (v,m)=(29,49) for E407 and (31,56) for E408 Q33.

Suppose T subset U, |T|=t, meets every Q. Let n_1 be the number of Q with |Q intersect T|=1 and n_2=m-n_1 the number with at least two points in T.

For each x in T, the triples Q\{x} from sets meeting T only at x are pairwise disjoint subsets of U\T. Hence

\[
n_1\le t\left\lfloor\frac{v-t}{3}\right\rfloor.
\]

Each Q counted by n_2 contains a pair from T, and no pair occurs in two Qs, so \(n_2\le\binom t2\). These inequalities rule out t<=4 for (29,49) and t<=5 for (31,56).

For the remaining cases, each point lies in at most floor((v-1)/3) members of Q, because the triples outside that point are disjoint. Thus the total incidence I(T) satisfies

\[
I(T)\le t\left\lfloor\frac{v-1}{3}\right\rfloor.
\]

Every Q is hit, and every Q with at least two points in T contributes an extra incidence, so

\[
I(T)\ge m+n_2\ge2m-t\left\lfloor\frac{v-t}{3}\right\rfloor.
\]

For E407:
- t=5 gives I(T)>=58 but I(T)<=45.
- t=6 gives I(T)>=56 but I(T)<=54.

For E408 Q33, t=6 gives I(T)>=64 but I(T)<=60.

Therefore \(\tau(\mathcal Q)\ge7\) in both boundary cases. This proof is purely combinatorial and does not use the disputed partiteness step.

## 2. Valid boundary budgets

Let L=overline(H[U]), W=H\U, and \(\epsilon_U=\sum_{u\in U}(d_H(u)-12)\). The core has e(H)=284 and total excess four.

### E407: v=29, m=49

Put \(\delta=e(L)-294\ge0\). Since \(\binom{29}{2}=406\),

\[
e(H[U])=112-\delta,
\]
\[
e_H(U,W)=124+2\delta+\epsilon_U,
\]
\[
e(H[W])=48-\delta-\epsilon_U.
\]

Because |W|=18 and alpha(H[W])<=4, \(e(H[W])\ge p_4(18)=32\). Thus

\[
\delta+\epsilon_U\le16.
\]

The transversal floor gives \(e_H(U,W)\ge7|W|=126\), hence

\[
\epsilon_U+2\delta\ge2.
\]

The valid unconditional window is therefore

\[
0\le\delta\le16,\quad 0\le\epsilon_U\le4,\quad
\delta+\epsilon_U\le16,\quad\epsilon_U+2\delta\ge2.
\]

If L is known independently to be non-four-partite, Brouwer's second-Turán bound gives e(L)<=309, hence delta<=15. That extra conclusion is conditional on non-four-partiteness.

### E408 Q33: v=31, m=56

Put \(\delta=e(L)-336\ge0\). Since \(\binom{31}{2}=465\),

\[
e(H[U])=129-\delta,
\]
\[
e_H(U,W)=114+2\delta+\epsilon_U,
\]
\[
e(H[W])=41-\delta-\epsilon_U.
\]

Since |W|=16 and alpha(H[W])<=4, \(e(H[W])\ge p_4(16)=24\), so

\[
\delta+\epsilon_U\le17.
\]

The transversal floor requires at least 112 cross edges; the exact identity already gives at least 114. Thus it does not further tighten this window.

## 3. Partiteness audit: a gap in the sibling proof

The sibling theorem claims that L must be non-four-partite because, if L were complete four-partite, the pair-product constraint from the witness K4s forces the balanced part sizes and too many edges.

That argument only excludes **complete** four-partite graphs. Brouwer's second-Turán theorem can be applied only after non-four-partiteness is proved. A four-partite graph may omit cross-part edges.

The correct conditional dichotomy is:

### E407

If L is four-partite, the 49 edge-disjoint K4 witnesses force part sizes (8,7,7,7): each pair of parts must have product at least 49. The complete four-partite graph has 315 edges, but the valid budget permits e(L)=294+delta up to 310. At delta=16, L would simply be a complete (8,7,7,7)-partite graph with five cross-part edges deleted. The 49 witness K4s use 294 distinct edges; the 21 unused cross-part pairs can contain those five deleted edges. This is arithmetically compatible and not ruled out by the current argument.

If L is non-four-partite, then e(L)<=309 and delta<=15.

### E408 Q33

If L is four-partite, the 56 edge-disjoint K4 witnesses force part sizes (8,8,8,7): every pair of parts must have product at least 56. The complete four-partite graph has 360 edges, while the valid budget gives e(L)<=353. A four-partite graph with seven cross-part edges deleted has 353 edges; the 56 witnesses use 336 edges and leave 24 cross-part pairs unused, so this deletion count is arithmetically compatible.

The second-Turán upper bound for a non-four-partite graph on 31 vertices is 354, which is weaker than the existing budget e(L)<=353 and does not eliminate the nonpartite branch either.

These are local arithmetic compatibility checks, not constructions of a full 47-vertex core. They establish that the cited proof does not currently eliminate the four-partite branch.

## 4. Consequence for this workstream

The seven-neighbour transversal theorem is imported as a proved necessary-structure result. The E407 window must retain delta<=16 unless a separate proof rules out the four-partite branch. The E408 window remains delta+epsilon_U<=17. Neither boundary is closed.

Next target: use the seven-neighbour condition together with the labelled shell-row support sets and the exact core degree sequence to eliminate or classify the four-partite design-like branch. Do not treat a non-complete four-partite graph as non-four-partite.
