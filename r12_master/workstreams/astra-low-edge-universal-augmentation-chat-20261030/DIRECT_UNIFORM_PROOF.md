# Direct proof with total excess at most six

Date: 2026-10-30. Status: **PROVED**. This proof uses neither augmentation nor an exact-edge nonexistence theorem.

Assume the five low-edge hypotheses and put epsilon(v)=d(v)-12>=0, T=sum epsilon<=6. Let p_r(n) be the sum of binomial(part size,2) for the balanced r-part partition of n; Turan in the complement gives e(G)>=p_r(n) when alpha(G)<=r.

## 1. A degree12 independent four-set, including T=0

Let q be the number of positive excesses. Then 0<=q<=T<=6. If the other47-q vertices contain no independent four-set, they span at least p3(47-q) edges. The edges incident with the q exceptional vertices number at least12q+T-binom(q,2). Hence

    e(H)>=p3(47-q)+12q+T-binom(q,2)
         >=p3(47-q)+12q-binom(q,2).

For q=0,...,6 the last bounds are345,342,338,334,329,323,317, all greater than285. Therefore there are four independent degree12 vertices I={s1,s2,s3,s4}. In particular the regular case T=0 is included.

Every outside vertex meets I. The 48 incidences cover43 vertices, leaving exactly five surplus incidences. Let Z contain vertices with at least two I-neighbors, and P_i those with unique I-neighbor s_i. If two members of P_i were nonadjacent, they together with the other three seeds would be independent. Thus K_i=P_i union {s_i} is a clique.

With h=|Z| and d_i=|N(s_i) intersect Z|,

    |K_i|=13-d_i<=11, sum_i d_i=h+5, 3<=h<=5.

The only clique sizes are 11^4 (h=3), 10,11,11,11 (h=4), and 9,11,11,11 or10,10,11,11 (h=5).

## 2. Shared tools and the six-unit equality trigger

The independently proved common-neighbor lemma C2 gives c(u,v)<=3+epsilon(u)+epsilon(v) for nonedges; C3 allows at most one exterior vertex complete to a given K10.

For a point z with support exactly {s_i,s_j}, put A=K_i minus N(z) and B=K_j minus N(z). Every A-B pair is an edge: otherwise its nonadjacent endpoints, z, and the two other seeds form an independent five-set. This blocker is used only for support of size exactly two.

If both cliques have size11, a=|A| and b=|B| are positive and at most10. Disjoint excess accounting gives

    T>=max(0,10-a-b)+a max(0,b-2)+b max(0,a-2)>=6.

For a=1 or b=1 the expression is at least7; on a,b>=2 its unique minimum6 is at (2,2) (increasing either variable increases the expression). Consequently the EXISTENCE of such a pair forces T=6, a=b=2, epsilon(z)=6 and every other excess zero. The point z has nine neighbors in each clique and no other neighbors. For T<6 such a pair is already impossible. This single equality trigger replaces every use of exact e=285 in the structural reduction.

## 3. Excluding h=3

Each label occurs twice among three supports. Their only possibilities up to relabeling are {1234,12,34} and {12,134,234}. The first has two K11/K11 pair points, each requiring all excess on itself, impossible.

In the second, the pair point z=12 triggers equality. Its two missing vertices A in K1 are complete to its two missing vertices B in K2. A chosen a in A has its ten internal K1 neighbors and the two B-neighbors as its whole degree12 neighborhood. Replace seed s1 by a. The new seeds are still independent and degree12; K3,K4 remain private K11s and cannot enlarge because of the clique cap. The old point with support134 now has support34, so the equality trigger requires six excess units on this different point, contradiction.

## 4. Excluding h=4

There is one K10, K0, and three K11s. Supports consist of one triple and three pairs. If any pair joins two K11s, its point consumes all excess. The other two pair points have degree12 and cannot join two K11s. A K10/K11 pair point missing a>=1,b>=1 vertices forces the blocker. Zero excess on clique vertices gives a<=2,b<=3, but its own degree is at least21-a-b>=16, contradiction. Thus both other pair points complete K0, forbidden by C3.

Otherwise all three pairs meet label0. Support-degree counting forces exactly01,02,03, with complementary triple123. For these pair points z_i write a_i=|K0 minus N(z_i)|>=0 and b_i=|Ki minus N(z_i)|>=1. At v in K0, the three support adjacencies and the disjoint forced edges into the three leaf cliques give

    epsilon(v)>=sum_(i:v missing z_i)(b_i-1).

Adding the disjoint leaf and point contributions yields

    T>=sum_i [max(0,9-a_i-b_i)+a_i(b_i-1)+b_i max(0,a_i-2)].

For a,b>=1 the bracket is at least6: b=1 gives max(0,8-a)+max(0,a-2)>=6; a=1,b>=2 gives at least7; a,b>=2 gives at least7. Since T<=6, at most one a_i is positive. At least two points complete K0, contradiction. Empty missing sets have not been excluded by assumption.

## 5. Reducing h=5 to P or D

All five supports are pairs. Their multigraph degrees are4222 or3322.

In4222 the cliques have sizes9,11,11,11. Exactly one pair joins two K11 labels and triggers the six-unit equality. Each of the other four pair points joins K9 to K11 and has degree12. If it misses positive sets in both, zero-excess endpoint degrees bound those sizes by2 and4, giving its degree at least20-2-4=14. Therefore all four complete K9. Any two must be adjacent: otherwise their common neighborhood has size at least9, while both excesses are zero and C2 permits only3. Together with K9 they form K13, contradiction.

In3322 label K1,K2 by the two K10s and K3,K4 by K11s. A pair34 would trigger equality; each of the other four degree12 pair points would then have to complete a K10. If both missing sets were positive, the blocker gives degree at least14 for10/10 or16 for10/11. C3 permits only two completing points in total, contradiction.

Thus no34 pair exists. There is exactly one12 pair; the four mixed pairs form a 2-by-2 nonnegative integer matrix with row/column sums2. Up to relabeling the possibilities are

    P:12,13,13,24,24;
    D:12,13,14,23,24.

## 6. Excluding P by disjoint mixed blockers

A K10/K11 pair point missing a>=1,b>=1 vertices forces excess at least

    max(0,9-a-b)+a max(0,b-3)+b max(0,a-2)>=4

on itself and those two missing sets. For a=1 the bound is at least5; for a=2 it is at least4; for a>=3, b=1 or2 gives at least6; on a,b>=3 it is increasing and is6 at (3,3).

In each doubled mixed pair, C3 lets at most one of its points complete the K10, and neither can complete K11. Choose a noncompleting point from each doubled pair. The two charged clique pairs and points are disjoint. Thus T>=8>6, contradiction.

## 7. Excluding D with simultaneous incidence accounting

For each support edge e=ij let A_{i,e}=K_i minus N(z_e), a_{i,e}=|A_{i,e}|. At v in K_i, let M(v) be the incident e with v in A_{i,e}. Distinct incident support edges go to distinct opposite cliques, so the forced blocker neighborhoods do not overlap. Since |K_i|-1+d_i=12,

    epsilon(v)>=max(0,sum_(e in M(v))(a_{j,e}-1))
              >=sum_(e in M(v))max(0,a_{j,e}-2).

For K10 there is at most one negative summand, from the sole other K10 support; K11 has only two summands, and if both are negative the claimed right side is zero. Otherwise use max(0,sum x-1)>=sum max(0,x-1) for nonnegative integer x. This covers all complete K10 attachments.

Summing over the cliques and then over distinct mixed support points counts each excess once via the pointwise inequality. Each mixed point with positive missing sets contributes at least

    max(0,9-a-b)+a max(0,b-2)+b max(0,a-2)>=5.

If a=1 or b=1 this is at least6; on a,b>=2 it increases in either argument and is5 at (2,2). Of four mixed points, at most one per K10 can complete it, so at least two have positive missing sets. Their pointwise contributions are additive even if they share a leaf clique, because their forced neighbors are in distinct opposite cliques. Thus T>=10>6, contradiction.

All support possibilities are excluded under T<=6. This proves the low-edge theorem directly. No source partition, witness-support cardinality, hereditary cap or exact edge count was added to the five assumptions.
