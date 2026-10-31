# Triple antineighborhood interface at the 286-edge boundary

Date: 2026-10-31. Status: **all triple cells excluded for the two boundary parents**; no universal exclusion of these cells at other charges is asserted.

Choose any regular pivot p. Among its 47 non-neighbors there exist nonadjacent u,v with d_F(u),d_F(v)<=14. Otherwise those low-degree points form a clique of size at most 11 and at least 36 other points have degree >=15. Their excess over 13 is at least 72, exceeding the full excess 21 or 23.

The independent triple T={p,u,v} has common antineighborhood W contained in H. Its independence number is at most 2. The closed-neighborhood union has size at most 3+13+14+14=44, so |W|>=17. The accepted R(2,24)=empty seed, inherited by subsets of W, gives |W|<=23. This upper bound is not derived from elementary pair counting alone.

We reuse the previously audited 23-point classification without recomputing it:

- Cell A: e(F[W])=132 and all eleven non-target colors are near-perfect matchings on W.
- Cell B: e(F[W])=131 and complement(F[W]) is the single-edge subdivision of K11,11. Its subdivision point w has target degree 20 inside W.

For E408, Delta(F)<=19 immediately excludes Cell B for every charge. For E407, Delta(F)<=20 forces d_F(w)=20 and no target neighbors outside W. Its parent excess is 7, leaving total excess 14 on the other 60 points.

If this E407 parent also has the q30 boundary core, then W subset H implies d_H(w)=20 and epsilon_H(w)=8. Since sum epsilon_H=8, every other core point has degree 12. Thus the 14-defect parent extension and the core excess ledger are compatible arithmetically but impossible structurally by E286. This is the required connection between the two ledgers; no false arithmetic contradiction is claimed.

At (E,q)=(407,30),(408,31), Cell A and every |W|=17..22 case likewise sit inside the impossible 286-edge H. They are all excluded by the same containing-core theorem. There is no need to classify each smaller W or to assume that W always has size 23. Outside these boundary charges, this file leaves Cell A and the smaller sizes open; source-dependent E407 Cell B arguments are separate.

Dependencies: the accepted R(2,24) seed and audited 23-point classification are used only to describe the triple interface. The boundary parent exclusion itself uses neither: its proof is already complete from E286 and the accepted R(4,47) gate.
