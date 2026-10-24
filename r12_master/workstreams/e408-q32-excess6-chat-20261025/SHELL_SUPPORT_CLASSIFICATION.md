# Shell-support classification — E408 Q32

Status: **PROVED parameterized classification and uniform capacity reduction; no unsupported M[B]=∅ assumption.** The full graph-isomorphism classification of all 13-vertex missing graphs M is not claimed.

## 1. Frozen shell equations

Let F be the 61-point E408 residual, with e(F)=408, δ(F)=13, a degree-13 pivot p, shell A=N_F(p), |A|=13, and core H of size47 with e(H)=285. Let

\[
M=\overline{F[A]},\quad e(M)=m_M,\quad
t_a=|N_F(a)\cap H|,\quad
g_a=d_F(a)-13.
\]

For each a∈A,

\[
d_F(a)=1+(12-d_M(a))+t_a=13-d_M(a)+t_a,
\]

so t_a=d_M(a)+g_a and g_a≥0. The E408 Q32 identity q=e(M)+Σg_a=32 gives

\[
\boxed{22\le e(M)\le32,\qquad
\sum_{a\in A}g_a=32-e(M)\in[0,10].}
\]

The lower bound e(M)≥22 is independently derived from the 14-set {p}∪A. It has 91 pairs. Each of the eleven non-target colors has independence number at most12, so it must use at least two edges on any 14-set; otherwise that color would have an independent 13-set. Thus the target color has at most 91-22=69 edges on {p}∪A. But its edge count there is 13+e(F[A])=13+78-e(M)=91-e(M), giving e(M)≥22.

The upper bound e(M)≤32 follows from Σg_a=32-e(M)≥0. These are Q32 facts; no 284-edge/excess-four identity is used.

## 2. Zero shell-support vertices are allowed and budgeted

For x∈H let r_A(x)=|N_F(x)∩A| and ε_x=d_H(x)-12. The legal residual minimum-degree contract gives d_F(x)=d_H(x)+r_A(x)≥13. Thus r_A(x)=0 implies ε_x≥1. Since Σ_H ε_x=6, at most six core vertices have zero shell support.

Let z=|{x∈H:r_A(x)=0}|. The exact shell-incidence identity is

\[
\sum_{x:r_A(x)>0}(r_A(x)-1)
=e(A,H)-(47-z)=e(M)-15+z.
\]

The z term cannot be dropped: positive-excess core vertices may have no shell neighbor. This audit deliberately does not assume every core vertex is shell-supported.

## 3. Exhaustive split by whether a 10-point target clique exists in the shell

Since ω(F)≤11 and p is adjacent to every vertex of A, the shell target graph F[A] has clique number at most10. Equivalently α(M)≤10. Therefore exactly one of the following holds.

### Case I — M has an independent 10-set B

Choose B⊂A with |B|=10 and M[B]=∅; put S=A\\B, |S|=3. Let

\[
\beta=e(M[S])\in\{0,1,2,3\},\qquad
c=e_M(S,B).
\]

Then

\[
e(M)=\beta+c,\quad
c=e(M)-\beta\ge19,\quad c=\sum_{b\in B}k_b,\quad
k_b=d_M(b)\le3.
\]

Since each of ten B rows contributes at most one if k_b≤1 and at most three if k_b≥2, the number h of B rows with k_b≥2 obeys

\[
c\le10+2h,\qquad h\ge\left\lceil\frac{c-10}{2}\right\rceil\ge5.
\]

Also c≤30, so e(M)=32 forces β≥2 and e(M)=31 forces β≥1. The total row decoration remains Σg_a=32-e(M).

The exact-129 witness theorem does not need this case assumption. If it holds, each one-outside K5 witness labelled by a shell vertex a must hit every row D_b=N_F(b)∩H for which ab∈E(M). Because M[B]=∅, any K5 component with two shell vertices cannot use two vertices of B; if it has three shell vertices, at least two lie in S.

### Case II — M has no independent 10-set

Then α(M)≤9, equivalently every 10-subset B⊂A has M[B]≠∅. For any chosen B and S=A\\B, write

\[
\beta_B=e(M[B])\ge1,\quad
\beta_S=e(M[S])\le3,\quad
c=e_M(S,B)\ge0.
\]

The complete count identity is

\[
e(M)=\beta_B+\beta_S+c\in[22,32],\qquad
\beta_B+c=e(M)-\beta_S\ge19,\qquad
\sum g_a=32-e(M)\in[0,10].
\]

No row degree bound k_b≤3 is available here: a B vertex may have missing neighbors inside B. Accordingly, no conclusion that requires M[B]=∅ is transferred to this branch.

## 4. Component-level support classification valid in both cases

For each exact-129 color, the Type-I equality structure has twelve pairwise-disjoint 5-cliques in C[R]: ten isolated K5 components and two K5 cliques in the 11-point gadget. Every such clique must meet {p}∪A, because α(H)≤4. Let x be the gadget's exceptional vertex.

- If x∉H, the twelve K5 cliques have at most thirteen outside-H vertices available, so there is exactly one extra outside vertex beyond one per clique. At most one K5 clique has two outside vertices; all others have one.
- If x∈H, the twelve K5 cliques have at most fourteen outside-H vertices available, so there are at most two extra outside vertices. The only possibilities are one K5 clique with three shell/pivot vertices, or two K5 cliques each with two shell/pivot vertices, or a subcase where the extras occur in the gadget cliques. No K5 clique can have four or more outside vertices.
- A K5 clique with two shell vertices requires their pair to be an edge of M. A K5 clique with three shell vertices requires a triangle in M. The pivot p cannot co-occur with a shell vertex in such a clique because p is target-adjacent to every shell vertex.
- Among the ten isolated K5 components, at most two fail to have exactly one outside-H vertex. Therefore at least eight yield independent 4-sets in H. If x∉H, at least nine do.

This exhausts the outside-support multiplicity patterns relevant to the witness floor. It does not classify every isomorphism type of M[B] in Case II, and no such classification is needed for the 285-edge capacity theorem: that theorem is uniform over all M.

## 5. Cross-branch firewall

The E407 Q32 and E408 Q33 284-edge/excess-four statements are not used. The only core excess identity here is Σ_H(d_H-12)=6. The stronger support floor v≥33/35/37 follows from the twelve-clique witness extraction and the 285-edge capacity theorem in CORE285_CAPACITY_THEOREM.md, irrespective of which of Case I or Case II holds.

Remaining open question: combine the labelled shell-hit constraints and the surviving core support profiles with all seven outer K12 near-Latin blocks to obtain a contradiction or a smaller certified terminal.
