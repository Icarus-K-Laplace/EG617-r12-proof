# Uniform common-neighborhood capacity

Date: 2026-10-30. Status: **PROVED**.

Assume H is simple, |H|=47, e(H)<=285, delta(H)>=12, alpha(H)<=4 and omega(H)<=11. Define epsilon(v)=d_H(v)-12 and T=sum epsilon=2e(H)-564. Thus 0<=T<=6.

## C1. No 25-set has independence number at most two

For any 25-set W,

    2e(H[W]) <= sum_(w in W) d_H(w)
              =300+sum_(w in W)epsilon(w) <=300+T<=306.

Thus e(H[W])<=153. No excess is charged twice: the middle sum includes each vertex of W once; the first inequality counts internal edges twice and boundary edges once.

If alpha(H[W])<=2, L=complement(H[W]) is triangle-free. It is not bipartite: a bipartition of L would partition W into two H-cliques, each of order at most11, so |W|<=22. There may be H-edges between the two parts. The stronger assertion that H[W] is a disjoint union of two cliques is unnecessary and generally false.

[Kang-Pikhurko 2005, Theorem1](https://opikhurko.warwick.ac.uk/E/KangPikhurko05ms.pdf) applies with n=25,r=2: n>=r+3 and 2<=r<=(n-1)/2. It gives

    e(L)<=floor(25^2/4)-floor(25/2)+1=156-12+1=145.

Hence e(H[W])>=binom(25,2)-145=155, contradicting153.

An elementary independent check of the same bound is available. A shortest odd cycle of a non-bipartite triangle-free n-vertex graph has length 2k+1>=5 and is chordless. An outside vertex meets at most k cycle vertices. Mantel on the outside gives

    B(n,k)=2k+1+k(n-2k-1)+floor((n-2k-1)^2/4).

For n=25, k=2,...,12, these bounds are 145,142,137,130,121,110,97,82,65,46,25. Thus their maximum is145. This provides the needed upper bound without invoking the general second-Turan theorem. The verifier recomputes the whole table. Mantel follows by summing d(x)+d(y)<=n over edges and applying Cauchy.

## C2. Every nonedge has small common neighborhood

Let uv be a nonedge and c=|N(u) intersect N(v)|. Its common antineighborhood, excluding u,v, has size

    47-2-[d(u)+d(v)-c]=21+c-epsilon(u)-epsilon(v).

If c>=4+epsilon(u)+epsilon(v), that set contains a 25-subset W. An independent triple in W, together with u,v, would violate alpha(H)<=4. Hence alpha(H[W])<=2, contradicting C1. Therefore

    c<=3+epsilon(u)+epsilon(v)<=3+T<=9.

## C3. Complete attachments to K10

At most one vertex outside any K10 can be adjacent to all ten clique vertices. Two such vertices, if adjacent, produce K12; if nonadjacent, have ten common neighbors, contrary to C2. Individual complete attachments to K10 or K9 are legal and must not be discarded. An outside vertex cannot complete K11 because omega(H)<=11.

Dependencies: only the five displayed core assumptions, elementary counting and the 25-point triangle-free bound proved above. No color, source profile, hereditary density cap, pivot placement or sibling theorem is used.
