# Original K145 to the unique T61 stop

Independent integration, 2026-10-31. The original assumption is a 12-edge-coloring of K145 in which EVERY 13-set contains all 12 colors. It does not mean equal color-class sizes. The proof below retains the original coloring wherever the contextual49 lemma is used.

## 1. Caps and least color

Let G be a least-edge color graph. Then e(G)<=870, alpha(G)<=12 and omega(G)<=12. Write p_k(n)=k binom(q,2)+qr for n=kq+r, 0<=r<k. Turan applied to the complement says that every n-set has at least p12(n) edges of EACH color. Hence every induced target graph satisfies e(U)<=D(|U|), where D(n)=binom(n,2)-11p12(n). These caps are hereditary, including at orders13,14,23,24,36,37,38 used later.

If delta(G)>=12, the edge bound forces every degree to equal12. Brooks' theorem colors G with12 vertex colors, since G has no K13 component; thus alpha(G)>=ceil(145/12)=13, a contradiction. Therefore a minimum-degree vertex v has d in {0,...,11}. This is the only use of Brooks.

## 2. Contextual R(4,49) is impossible

Here R(a,n) denotes alpha<=a, omega<=11 and all D caps. Suppose F=G[S] lies in R(4,49).

First delta(F)>=13. Degree<=11 leaves at least37 nonneighbors, a forbidden R(3,37). A degree12 vertex leaves a36-core H in R(3,36), with e(H)=234. The12-shell has a missing pair a,b because a shell K12 is forbidden. Its H-row union has size>=13: otherwise at least24 H-points avoid a,b, giving R(2,24). Thus H+a+b has at least247 edges, exceeding D(38)=241. Consequently e(F)>=319.

For each other color C on S, alpha(C)<=12 and omega(C)<=4: a C-clique of size5 would be independent in F. Therefore L=complement(C) is K13-free and is not12-partite. Indeed, a12-partition of L would partition C into12 cliques of size<=4, covering at most48 points. The second Turan theorem of Kang--Pikhurko, Theorem1, n=49,r=12, gives e(L)<=t12(49)-4+1. Equivalently e(C)>=p12(49)+3=79. Summing the other11 colors gives e(F)<=1176-11*79=307<319, a contradiction.

All hypotheses of that external theorem hold: r>=2, n>=r+3 and r<=(n-1)/2. No classification of its equality graphs is needed. This proves absence of any contextual49 object, without proving absence of every abstract uncolored R(4,49). It removes the temporary contextual premise in the old recurrence. It uses no T61 closure, COVER, 287-edge floor, or 48-point theorem.

## 3. Exhaustive extraction and exact edge ledger

Put A=N_G(v), U=V(G) minus N_G[v], so |U|=144-d. Choose an inclusion-maximal packing of j disjoint genuine target K12s in G[U]. Any vertex outside a K12 has at most one target neighbor in it: D(13)=67 and its internal66 edges leave only one edge. Edges between two blocks therefore form a matching.

There cannot be12 blocks. Greedily choose one independent representative from each of12 blocks: the k-th block loses at most k-1 points to preceding representatives, and has12 points. Adding v gives independent13. Hence 0<=j<=11.

The residual R has n=144-d-12j and omega(R)<=11 by maximality. Also alpha(R)<=11-j. Otherwise choose12-j independent residual points. Each block retains at least j points avoiding them; choose j independent representatives greedily (at stage k at most k-1 further points are excluded). Together with v this again gives independent13. This also covers j=0 and j=11. All residuals inherit the original coloring and caps.

For the exact budget write sigma=870-e(G), z=binom(d,2)-e(G[A]), g=sum_(a in A)(d_G(a)-d), x=edges between distinct packed blocks, y=edges from blocks to R. Every term is nonnegative and the disjoint edge partition gives

    e(R)=870-binom(d+1,2)-66j-(sigma+z+g+x+y).

In particular, the initial closed neighborhood is NOT assumed a clique. Its defect z is explicitly retained. The 144 pairs (d,j) above exhaust all extraction outcomes, including hypothetical pairs that cannot occur; including extra pairs cannot omit a legitimate parent.

## 4. Proof of every recurrence rule

Bounds B(a,n) concern induced subgraphs of this FIXED hypothetical G, with alpha<=a and omega<=11. Empty means impossible in that contextual class. Base maximum orders are 11,23,36,48 for a=1,2,3,4. The first three follow from the frozen lower-order proofs; the fourth from Section2. Seeds (2,23):131, (3,35):210, (3,36):234, (4,47):284, (4,48):308 are licensed by the stronger audited floors131,211,234,287,310. They contain no backend E333--340 assumption.

For a min-degree h vertex of an n-graph J, let C be its m=n-h-1 core, M the missing graph on its h-shell, g_x=d_J(x)-h>=0, t_x=d_M(x)+g_x and q=e(M)+sum g. Then

    e(J)=binom(h+1,2)+q+e(C),
    q=t(S)-e_M(S)+e_M(A minus S)+g(A minus S).

Since alpha(M)<=10, shell and closed-shell caps give

    q>=z>=max(p10(h), binom(h,2)-D(h), binom(h+1,2)-D(h+1)).

If h>=11 a missing edge exists. Its core-row union has size at least beta=max(0,m-N_(a-2)), where N is the already proved maximum order. Thus q>=beta-1. If B(a-1,m)+beta>D(m+2), the entire row is impossible.

The missing graph has a matching of size at least

    k=max(ceil((h-10)/2), 1+[h>=12]+[h>=13]).

The first bound follows because vertices unmatched by a maximum matching are independent. At h12, matching number1 would give a star (independence>=11) or triangle (only3 edges, whereas z>=11). At h13, the 3-matching proof is COVER Section4 and uses only z>=22, alpha(M)<=10. At h14, matching number<=2 gives at most four matched endpoints and an independent10-set. The cross bipartite graph has a cover of size<=2, hence at most20 cross edges; adding six endpoint edges gives26<z_floor=33. For h>=15 the first bound already gives3. This licenses every h, not only12 and13.

For any t<=k, the 2t endpoints have total weight>=t beta. Target alpha<=a bounds their M-edges by binom(2t,2)-p_a(2t). The subset identity gives q>=t beta-binom(2t,2)+p_a(2t). In the triangle-free channel, Mantel improves this to q>=t beta-t^2. In the triangle channel the three rows have union at least gamma=max(0,m-N_(a-3)), giving q>=gamma-3; that channel is impossible if B(a-1,m)+gamma>D(m+3). For a=2 a missing triangle is impossible directly. Take the MINIMUM of the two channel floors, not their maximum.

Each viable h row therefore gives max(ceil(nh/2), binom(h+1,2)+q_floor+B(a-1,m)). Minimize over all h. Finally maximize with p_a(n), the licensed seed, and the deletion bound ceil(n B(a,n-1)/(n-2)) when n>2. The deletion bound follows by summing edges over all one-vertex deletions. A value exceeding D(n), or no viable h, certifies emptiness; emptiness propagates to larger n. All recursive references have smaller a, or the same a and smaller n. There is no recursive assumption of the desired conclusion.

The bipartite matching-cover theorem used here and in COVER can be proved directly: for a maximum matching, follow alternating paths from unmatched vertices on the left. The unreached left vertices together with reached right vertices cover every edge and contain exactly one endpoint of each matching edge. Thus the minimum cover has the matching size. No extra extremal classification is hidden in this step. Turan includes Mantel as r=2.

## 5. Executed independent replay and final interface

The new third implementation agrees with both frozen implementations at ALL 1,752 nodes and at all144 outer comparisons. `FRONTEND_REPLAY.json` retains every bound and every stop, including excluded stops. The unique survivor is

    d=11, j=6, a=5, n=61, B(5,61)=397, budget=408.

Thus 397<=E<=408 and E+sigma+z+g+x+y=408. The only minimum-degree rows compatible with this budget are h12 and h13. Independently, h<=11 leaves a forbidden contextual49 core, while h>=14 forces e>=427. The terminal contract is exactly |F|=61, alpha<=5, omega<=11, all caps, E<=408, and minimum degree12 or13. It is the SAME induced graph F throughout each repivot.

The h12 theorem and all h13 closures cited in `FINAL_GLOBAL_PROOF.md` apply to this full contract. The proof does not equate the existence of some degree13 vertex with minimum degree13.

## External references inspected

- R. L. Brooks, *On colouring the nodes of a network*, Proc. Cambridge Philos. Soc.37 (1941),194--197. Original paper reprinted in Appendix A at https://www.tu-ilmenau.de/fileadmin/Bereiche/MN/komgra/BackMatterSMM.pdf . Applied only at maximum degree12 with no K13 component.
- M. Kang and O. Pikhurko, *Maximum K_(r+1)-free graphs which are not r-partite*, Matematychni Studii24 (2005),12--20, Theorem1, p13: https://opikhurko.warwick.ac.uk/E/KangPikhurko05ms.pdf . Its introduction also states the exact Turan theorem used for p_k.
- B. Andrasfai, P. Erdos and V. T. Sos, Discrete Mathematics8 (1974),205--218, Theorem1.1: https://real.mtak.hu/110445/1/1974-18.pdf . Used separately at n35, K4-free, delta22>175/8 to obtain CORE211.

Frozen prior front-end source: b0459807acd4b7e386148056ddf77d7998918893. This document supplies the independent analytic audit rather than inheriting its status labels.
