# Independent four-set of degree-12 vertices

Status: **PROVED**.

Assume |V(H)|=47, e(H)=284, delta(H)>=12 and alpha(H)<=4. Put epsilon(v)=d_H(v)-12. Then
\[
\sum_v\epsilon(v)=2\cdot284-12\cdot47=4.
\]
Consequently at most four vertices have positive excess, so at least 43 vertices have degree exactly 12. The induced graph on these regular vertices has maximum degree at most 12. A greedy independent-set algorithm removes at most 13 vertices at each selection, so it selects at least
\[
\left\lceil\frac{43}{13}\right\rceil=4
\]
pairwise nonadjacent degree-12 vertices. This gives the required independent four-set I.

For a second, independent arithmetic check, the previous Turán proof is also valid. If Q is the set of q positive-excess vertices, q=1,2,3,4, and S=V(H)\\Q had no independent four-set, the complement of H[S] would be K4-free. Turán's theorem gives
\[
e(H[S])\ge p_3(47-q)=\sum_{j=1}^3\binom{s_j}{2},
\]
where (s_1,s_2,s_3) is the balanced tripartition. Using
\[
e(H)=e(H[S])+\sum_{v\in Q}d(v)-e(H[Q])
\]
gives the independently checked lower bounds 346,342,338,333 for q=1,2,3,4, each greater than 284. Thus the lemma does not depend on a questionable greedy estimate; both proofs establish it.