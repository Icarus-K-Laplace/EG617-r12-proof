# E408 Q32 full support — two-block transversal blocker for the 2+8 cell

Date: 2026-10-28  
Status: **PROVED local structural theorem; no global Q32 closure claimed.**

## 1. Contract

Consider the disconnected m=10 light-block cell with components 2+8. Let A,B be the two small pivot blocks and D any outer block. Then:
- A and B are independent 4-sets joined by exactly a perfect matching;
- each of A-D and B-D has exactly five H-edges, hence a perfect matching plus one extra edge;
- every r in R has a unique neighbor f(r) in each of A and B, and after aligning A-B the two maps coincide;
- `Delta(H[R])<=2`;
- every q in D has `d_H(q)=12`, hence `e_Q(q)+d_R(q)=3`, where e_Q counts Q-Q incidences beyond the nine mandatory base neighbors;
- the 4,5,5 switch lemma says the two A/B neighbor-label sets of q have nonempty intersection.

Write `F_h=f^{-1}(h)`, `n_h=|F_h|`, and `S_A(q)=N(q) cap A`, `S_B(q)=N(q) cap B`, `I(q)=S_A(q) cap S_B(q)`.

## 2. Singleton-track blocker

**Lemma 2.1.** If `I(q)={h}`, then q is adjacent to every vertex of `F_h`. Consequently
`d_R(q)>=n_h`, `k(q)<=e_Q(q)<=3-n_h`,
where k(q) is the number of the two mandatory extra edges from D to A,B incident with q.

**Proof.** Suppose r in F_h is nonadjacent to q. Since `e_Q(q)+d_R(q)=3`, q has at most three R-neighbors, so at least four vertices of R are nonneighbors of q. Among these, choose s distinct from r and nonadjacent to r: this is possible because r has at most two R-neighbors. Since F_h is a clique, s lies in F_k for k != h.

Let a,b be the two labels other than h,k. Each of S_A(q), S_B(q) contains h and has size at most two. Since their intersection is exactly {h}, one can choose distinct labels a' and b' from {a,b} with a' not in S_A(q) and b' not in S_B(q); otherwise both sets would contain the same second label and I(q) would have size two.

Then q,r,s,A_{a'},B_{b'} are pairwise nonadjacent: r,s are nonadjacent by choice; their unique neighbors in A,B have labels h,k; A_{a'} and B_{b'} avoid both labels; q avoids them by construction; and A_{a'},B_{b'} are nonadjacent because the A-B edges are exactly the identity matching and a' != b'. This is an independent 5-set, contradiction. QED.

## 3. Double-track blocker

**Lemma 3.1.** If `I(q)={h,j}`, then q is incident with both extra A-D and B-D edges, so `k(q)=2` and `d_R(q)<=1`. Further, if both fibers are nonempty, then `n_h+n_j<=3`.

**Proof.** Since q is adjacent to two labels in each of A and B, it must receive the extra edge in each five-edge pair, so k(q)=2. Thus e_Q(q)>=2 and d_R(q)<=1.

If r in F_h and s in F_j are nonadjacent and both miss q, choose the two remaining labels a,b outside {h,j}. The vertices q,r,s,A_a,B_b are an independent 5-set, because q is adjacent in A and B only to labels h,j, and A_a,B_b are distinct labels across the A-B matching. Hence every nonedge between F_h and F_j must be covered by N_R(q), a set of size at most one.

If N_R(q) is empty, all cross-pairs between F_h and F_j are edges. If its unique vertex lies in F_h, every cross-pair not involving that vertex must be an edge; similarly if it lies in F_j. If the unique neighbor lies outside both fibers, all cross-pairs must be edges. In every case, when both fibers are nonempty, some vertex has at least `n_h+n_j-1` neighbors in H[R]. Since `Delta(H[R])<=2`, this gives `n_h+n_j<=3`. QED.

If one fiber is empty, the same numerical inequality is automatic because every nonempty fiber has size at most three.

## 4. Block and endpoint-load consequences

Each outer block has exactly two extra edges to A,B, so `sum_{q in D} k(q)=2`. Thus:
- if a double-track vertex occurs, it consumes both extra A/B edges in that block; all other vertices of D have k=0;
- its two track-fiber sizes sum to at most three;
- every singleton-track vertex of label h has k(q)<=3-n_h.

For each small block A or B, let e_i(h) count its extra-edge endpoints at label h. The eight outer blocks contribute eight such endpoints, while the minimum-degree floor gives `e_i(h)>=3-n_h`. Therefore
`sum_h e_i(h)=8`, `e_i(h)=3-n_h+u_i(h)`, `u_i(h)>=0`, `sum_hu_i(h)=3`.
Hence `e_i(h)<=6-n_h`.

In a synchronized switch block, the two extra edges share one endpoint label s on the small side, so each such block contributes one unit to e_A(s) and e_B(s). The number of switch blocks with extra endpoint label s is consequently at most `6-n_s`.

## 5. Scope

This is a source-correct local refinement for the 2+8 cell. It uses only the true 4,5,5 matching-switch lemma, the aligned zero-slack maps, `alpha(H)<=4`, `Delta(H[R])<=2`, and the pointwise degree ledger. It does not invoke retracted KP degree-nine or exceptional-injectivity claims. The 2+8 cell remains OPEN.
