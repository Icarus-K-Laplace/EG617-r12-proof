# Universal Q32 core nonexistence theorem

Date: 2026-10-30.

**Status: PROVED, using the published second-Turan theorem.** No simple graph satisfies |H|=47, e(H)=285, delta(H)>=12, alpha(H)<=4 and omega(H)<=11. Consequently no full-support Q32 configuration with this core contract exists, simultaneously for m=8,9,10. This does not settle other EG617 branches. Steps1–6 reduce a putative core to two templates; steps7–8 exclude both analytically.

## U1. Two-template core theorem — PROVED relative to the published second-Turan theorem

Let H be a simple graph with

    |H|=47, e(H)=285, delta(H)>=12, alpha(H)<=4, omega(H)<=11.

Write epsilon(v)=d_H(v)-12. Then sum epsilon=6. There is a partition

    V(H)=K1 dot-union K2 dot-union K3 dot-union K4 dot-union Z

with these properties:

1. Each K_i induces a clique; their orders are10,10,11,11. The set Z has five vertices.
2. There are distinguished vertices s_i in K_i with d_H(s_i)=12. The four s_i are independent. A vertex of K_i other than s_i is adjacent to exactly s_i among these four vertices.
3. Every z in Z is adjacent to exactly two distinguished vertices. Up to relabeling the two10-cliques, the two11-cliques, and Z, the five neighbor-label pairs are exactly one of

       D: 12,13,14,23,24;
       P: 12,13,13,24,24.

   Repeated pairs mean distinct vertices of Z, not multiple graph edges.
4. The clique edges and the ten distinguished-vertex/Z edges fix exactly210 target edges. Exactly75 further edges occur among the remaining38 clique vertices and Z, with no additional edge incident with any s_i. The degree and independence conditions above still apply to those75 edges.

This intermediate conclusion uses no exact color, no pivot-neighborhood placement, no m-specific hypothesis, and no sibling theorem. It therefore applies simultaneously to every m=8,9,10 configuration under the stated core contract. The final two steps below exclude both completion families.

## Proof, step1: an independent four-set of degree12 vertices

Let q be the number of vertices with positive epsilon. Then1<=q<=6. If the other47-q vertices had independence number at most3, Turan's theorem in the complement would give at least p3(47-q) internal edges, where p_r(n) is the sum of binomial(part-size,2) over the balanced r-part partition of n. Edges incident with the q exceptional-degree vertices number at least12q+6-binomial(q,2). Thus

    e(H)>=p3(47-q)+12q+6-binomial(q,2).

For q=1,...,6 these lower bounds are348,344,340,335,329,323, all greater than285. Hence there is an independent set I={s1,s2,s3,s4} of degree12 vertices.

Every vertex outside I has a neighbor in I, or alpha(H)>=5. The four degrees sum to48, covering43 outside vertices. Put Z={v outside I: |N(v) intersect I|>=2}, h=|Z|, and let P_i consist of the outside vertices with unique neighbor s_i in I. The set P_i is a clique: two nonadjacent points of P_i, together with I minus {s_i}, would be independent of size5. Consequently K_i={s_i} union P_i is a clique.

Let d_i=|N(s_i) intersect Z|. Then

    |K_i|=13-d_i,   sum_i d_i=h+5,   d_i>=2.

The last inequality uses omega(H)<=11. Each z contributes at least one to the overlap surplus5, so h<=5; the sum equation gives h>=3. There are only these size patterns:

| h | d_i, sorted | clique orders |
|---:|---|---|
|3|2,2,2,2|11,11,11,11|
|4|3,2,2,2|10,11,11,11|
|5|4,2,2,2|9,11,11,11|
|5|3,3,2,2|10,10,11,11|

All subsequent arguments apply to this actual partition, without choosing matchings in the color graphs.

## Step2: a uniform common-neighbor bound

**Lemma U2 — PROVED relative to [Kang-Pikhurko Theorem1](https://opikhurko.warwick.ac.uk/E/KangPikhurko05ms.pdf) at n=25,r=2.** Its hypotheses n>=r+3 and 2<=r<=(n-1)/2 hold. Every nonedge uv of H satisfies

    |N(u) intersect N(v)| <= 3+epsilon(u)+epsilon(v).        (1)

Indeed, any25-vertex induced subgraph W of H has at most(25*12+6)/2=153 edges. If alpha(H[W])<=2, its complement is triangle-free. That complement cannot be bipartite, since two H-cliques of orders at most11 cannot cover25 vertices. The sharp non-bipartite triangle-free bound gives at most

    floor(25^2/4)-floor(25/2)+1=145

complement edges, hence at least300-145=155 target edges, contradiction. Thus H has no25-set with independence number at most2.

For a nonedge uv, its common antineighborhood has independence number at most2. Its order is21+|N(u) intersect N(v)|-epsilon(u)-epsilon(v), so it is at most24, proving (1).

**Corollary U3 — PROVED.** At most one vertex outside a given K10 can be complete to that K10. Two such vertices would either be adjacent, giving K12, or nonadjacent, giving ten common neighbors, whereas (1) permits at most3+sum epsilon<=9.

We will also use that nonadjacent degree12 vertices have at most three common neighbors.

## Step3: a pair supported on two K11s spends all excess

**Lemma U4 — PROVED.** Suppose z in Z has I-neighbor set {s_i,s_j}, with |K_i|=|K_j|=11. Then epsilon(z)=6, every other vertex has epsilon zero, and z has exactly nine neighbors in each of these two cliques and no other neighbors.

Let A=K_i minus N(z), B=K_j minus N(z), a=|A|, b=|B|. Both are nonempty, since z cannot complete a K11. Each is disjoint from its distinguished vertex. Every A-B pair is an H-edge: otherwise z, a nonadjacent pair from A,B, and the two other distinguished vertices form an independent5-set.

For u in A, d(u)>=10+b, so epsilon(u)>=max(0,b-2); similarly epsilon(v)>=max(0,a-2) on B. Also d(z)>=22-a-b. These disjoint sets give

    6 >= epsilon(z)+sum_A epsilon+sum_B epsilon
      >= max(0,10-a-b)+a max(0,b-2)+b max(0,a-2).           (2)

The right side is at least6, with equality only at a=b=2. For a=1 it is at least7, and likewise for b=1. If a,b>=2 with one equal to2, equality6 occurs only when both equal2; if both are at least3, the expression is at least10. These statements can also be checked over the complete finite range1<=a,b<=10. Therefore a=b=2, epsilon(z)>=6, and the total budget forces the claimed equality structure.

## Step4: exclude h=3

Here all four K_i have size11 and every distinguished vertex meets two Z vertices. The three Z supports have total size8. Their only possibilities, up to relabeling, are:

- one support1234 and two disjoint pairs12,34;
- supports12,134,234.

In the first case each pair point spends all six excess units by U4, impossible.

In the second case call the pair point z and the triple points u=134 and v=234. U4 puts all excess on z and gives two nonneighbors A in K1 and two B in K2, with A complete to B. Choose a in A. Since a has degree12, its ten internal K1 neighbors and the two vertices of B are all its neighbors. In particular it has no neighbor in Z, K3, or K4. Replace s1 by a to get another independent four-set of degree12 vertices I'. Both original K3,K4 are still private cliques of size11 relative to I'. The vertex u now has support34 relative to I', since it misses a and s2. Applying U4 to u forces epsilon(u)=6, contradicting epsilon(u)=0. Thus h=3 is impossible.

## Step5: exclude h=4

There is one K10, call it K0, and three K11s. The four Z supports are one triple and three pairs.

First suppose a pair joins two K11 labels. Its point uses all excess by U4. Every remaining pair point has degree12, as do all clique vertices. Another pair joining K11s is impossible. A remaining pair must therefore join K0 to a K11. If it misses a>=1 vertices of K0 and b>=1 vertices of the K11, the complete bipartite blocker and degree12 at its endpoints give b<=3 and a<=2. Its own degree would be at least21-a-b>=16, impossible. So both remaining pair points are complete to K0, contradicting U3.

Hence all three pairs join the K10 label0 to a K11 label. Counting the four support degrees forces exactly the star pairs01,02,03 and complementary triple123.

Call the three pair points z_i. Put A_i=K0 minus N(z_i), B_i=K_i minus N(z_i), with a_i>=0 and b_i>=1. Each A_i-B_i graph is complete by the same independent5 blocker. For u in K0, edges to the three z_i plus the forced cross-clique edges give

    epsilon(u) >= sum_{i:u in A_i}(b_i-1).

The right side is nonnegative, and the three leaf cliques are disjoint. In K_i, vertices of B_i have epsilon at least max(0,a_i-2). Also epsilon(z_i)>=max(0,9-a_i-b_i). Therefore

    6 >= sum_i [max(0,9-a_i-b_i)+a_i(b_i-1)
                              +b_i max(0,a_i-2)].         (3)

Whenever a_i>=1, its summand is at least6. To check analytically: if b_i=1 it is max(0,8-a_i)+max(0,a_i-2)>=6; if a_i=1,b_i>=2 it is max(0,8-b_i)+b_i-1>=7; if a_i,b_i>=2 the minimum is at least7. Thus at most one a_i is positive. At least two z_i are complete to K0, contradicting U3. This excludes h=4.

## Step6: classify h=5

Every support has size2, so regard the five supports as a loopless multigraph on the four distinguished labels. Its degrees are either4,2,2,2 or3,3,2,2.

For degrees4,2,2,2, there is one K9 and three K11s. Exactly one of the five support edges joins two K11 labels, since four edges meet the degree4 label. Its point z spends all excess by U4. Every other pair point w has degree12 and joins K9 to K11. If w missed at least one point in both cliques, the complete bipartite blocker and zero excess at all clique vertices would give at most two missing points in K9 and at most four in K11. Then d(w)>=20-2-4=14, contradiction. Thus all four remaining points complete the K9. Any two of them must be adjacent by (1), since both have degree12 and share nine neighbors. They and K9 form a clique larger than11. This degree pattern is impossible.

Now the clique orders are10,10,11,11, with the first two distinguished labels of support-degree3. Suppose a support edge joins the two K11 labels. Its point spends all excess by U4; a second such support edge is impossible. Each of the other four pair points has degree12 and meets at least one K10 label. It must complete a K10: if it misses points in both of its cliques, the zero-excess complete-bipartite bounds give degree at least14 for a10/10 pair or at least16 for a10/11 pair. But U3 permits at most one completing point per K10, only two in total, whereas four are required. Contradiction.

There is therefore no support edge34. Degree counting forces exactly one edge12 and four edges between {1,2} and {3,4}. The latter form a2-by-2 nonnegative integer matrix with every row and column sum2. Up to relabeling, its only possibilities are all entries1, or diagonal entries2 and off-diagonal entries0. These give D and P in U1.

Finally, the four clique edge counts sum to200 and the five support pairs contribute ten additional edges. All distinguished vertices already have degree12, so all remaining285-210=75 edges avoid them. This completes the universal reduction.

## Step7: exclude the double template P

**Lemma U5 — PROVED.** Let z be supported on a K10 and a K11, and suppose it is not complete to either. Write A=K10 minus N(z), B=K11 minus N(z), a=|A|>=1 and b=|B|>=1. Then the total excess on the disjoint sets A, B, {z} is at least4.

The independent5 blocker again makes A complete to B. A vertex of A has nine internal neighbors and b neighbors in B; a vertex of B has ten internal neighbors and a neighbors in A; z has at least21-a-b neighbors. Therefore

    epsilon(z)+sum_A epsilon+sum_B epsilon
      >= max(0,9-a-b)+a max(0,b-3)+b max(0,a-2) >=4.      (4)

Here is an analytic proof of the last inequality. For a=1 the expression is max(0,8-b)+max(0,b-3)>=5. For a=2 it is max(0,7-b)+2 max(0,b-3)>=4, with equality at b=3. For a>=3 and b=1 it is at least6; for a>=3 and b=2 it is at least6. On the remaining domain a,b>=3 it is nondecreasing in each variable and its value at (3,3) is6. This covers all positive integer a,b.

In P there are two points supported on K1,K3 and two supported on K2,K4. In either pair, U3 allows at most one point complete to the K10. Neither point can complete the K11. Choose one point not complete to the K10 from each pair. Applying (4) to these two points uses disjoint cliques and distinct points, so the global excess is at least4+4=8. This contradicts sum epsilon=6. Template P is impossible.

## Step8: exclude the diamond template D

This step accounts for every forced edge only once. The five support pairs 12,13,14,23,24 are distinct. For a support edge e=ij with point z_e, write

    A_{i,e}=K_i minus N(z_e),   a_{i,e}=|A_{i,e}|.

The sets may be empty for a K10. For each e the independent5 blocker forces every edge between A_{i,e} and A_{j,e}. Fix v in K_i. Let M(v) be the incident support edges e for which v belongs to A_{i,e}. The forced cross edges for different incident e go to different cliques, hence are disjoint. With d_i the support degree of label i, the identity |K_i|-1+d_i=12 gives

    epsilon(v) >= max(0, sum_{e in M(v)} (a_{j,e}-1)).     (5)

We claim this implies

    epsilon(v) >= sum_{e in M(v)} max(0,a_{j,e}-2).        (6)

For i=1 or2, at most one summand in (5) can be negative: only the other K10 can have a zero missing set, and there is just one support edge12. For i=3 or4 there are only two incident support edges; if both summands are negative the right side of (6) is zero, and otherwise there is at most one negative summand. All negative summands equal -1. For nonnegative integers x_l, max(0,sum x_l-1)>=sum max(0,x_l-1). This proves (6), including empty missing sets and complete K10 attachments.

Summing (6) over the four cliques counts the forced incidence contributions as

    sum_{v outside Z} epsilon(v)
      >= sum_{e=ij} [a_{i,e} max(0,a_{j,e}-2)
                    +a_{j,e} max(0,a_{i,e}-2)].           (7)

There are four mixed K10/K11 support edges. At most two of their points can be complete to their K10, by U3 applied separately to K1 and K2. Thus at least two mixed support edges have both missing sets nonempty. For each such edge, its summand in (7), together with the excess of its distinct point z_e, is at least

    max(0,9-a-b)+a max(0,b-2)+b max(0,a-2) >=5.           (8)

To prove (8), if a=1 or b=1 the expression is at least6. On a,b>=2 it is nondecreasing in each argument, with minimum5 at (2,2). In fact increasing a by1 changes it by at least2b-3>=1, and similarly for b. All omitted terms in (7) and all other vertex excesses are nonnegative. Therefore sum epsilon>=5+5=10, contradicting6. Template D is impossible.

## U6. Universal nonexistence — PROVED

Steps1–6 show that every graph under the five stated core hypotheses has template D or P. Steps7–8 exclude both. No graph under that contract exists. Every genuine full-support Q32 configuration for m=8,9,10 has such a core, so none exists.

This is an analytic proof. The verifier rechecks the finite arithmetic, support classification and the local accounting inequality, and independently rejects the recorded search candidates; no failed random search, SAT solver, sibling closure, exact-color partition, or placement restriction is used to prove nonexistence. Source profiles and exceptional-point placements cannot escape the theorem, because it excludes their common target-core projection before any colored extension is imposed. Importing the conclusion into a different parent branch still requires verifying that parent's five core hypotheses; this document does not assert closure of Q33, E407 or EG617(r=12) as a whole.
