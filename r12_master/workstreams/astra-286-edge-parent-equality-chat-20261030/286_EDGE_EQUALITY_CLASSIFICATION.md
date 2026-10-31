# The 286-edge boundary: exhaustive structural elimination

Date: 2026-10-31. Status: **PROVED** (analytic proof; finite checks are supplementary).

## Theorem E286

There is no simple graph H with

    |H|=47, e(H)=286, delta(H)>=12, alpha(H)<=4, omega(H)<=11.

No hereditary density cap or color decomposition is required by this abstract theorem. Together with the previously established minimum-degree gate and low-edge floor, it implies

    J in R(4,47) => e(J)>=287.                       [PROVED]

The old284/285 proofs are not rerun. The new parameter throughout is epsilon(v)=d(v)-12>=0 and T=sum epsilon=8.

## 1. The valid common-neighbor bound at T=8

The 25-point non-bipartite triangle-free bound is 145. For completeness, take a shortest odd cycle of length 2k+1, k>=2. It is chordless; every outside vertex meets at most k cycle vertices, and Mantel bounds the edges on the remaining 24-2k vertices. The total is at most (2k+1)+k(24-2k)+(24-2k)^2/4=145+2k-k^2<=145. A 25-set of independence at most 2 would therefore span at least 155 edges: its complement cannot be bipartite, since two cliques of order at most 11 cannot cover 25 vertices. On the other hand it spans at most (25*12+8)/2=154 edges. Thus no such 25-set exists.

For a nonedge uv the common antineighborhood has size21+c(u,v)-epsilon(u)-epsilon(v), and independence number at most2. Consequently

    c(u,v)<=3+epsilon(u)+epsilon(v)<=11.              (1)

The upper bound9 is NOT used. Two exterior vertices completing the same K10 must be nonadjacent (otherwise K12), and (1) then forces their combined excess to be at least7. Two nonadjacent vertices completing K9 similarly require combined excess at least6. These are the replacements for the old completion-capacity lemma.

## 2. Exact support classification

At most8 vertices have positive excess. If the other47-q degree12 vertices had independence number at most3, their internal edges plus edges incident with the q exceptional vertices would give

    e(H)>=p3(47-q)+12q+8-binom(q,2), 1<=q<=8.

Each bound exceeds286 (the minimum is310). Thus choose an independent degree12 four-set I={s0,s1,s2,s3}. Private neighbors of each seed form a clique with that seed. Write these four cliques K_i, and let Z contain vertices with at least two seed-neighbors.

The48 seed incidences cover43 vertices, giving surplus5. If h=|Z| and d_i is the number of Z-neighbors of s_i, then |K_i|=13-d_i<=11, sum d_i=h+5 and3<=h<=5. Every z-support has size at least2.

Up to relabeling, all possibilities are:

|h|clique sizes|support multisets|
|---:|---|---|
|3|11,11,11,11|{0123,01,23}; {01,023,123}|
|4|10,11,11,11|{01,01,023,23}; {01,012,03,23}; {01,02,03,123}|
|5|9,11,11,11|{01,01,02,03,23}|
|5|10,10,11,11|P={01,02,02,13,13}; D={01,02,03,12,13}; B={01,01,02,13,23}; C={01,01,01,23,23}|

In the h5,3322 rows, labels0,1 are the K10s. There are ten support orbits in total. All are eliminated below.

## 3. Blocker and scalar lemmas

If z has seed-support exactly ij, let A=K_i minus N(z), B=K_j minus N(z), a=|A|, b=|B|. Every A-B pair is a target edge; otherwise its two nonadjacent endpoints, z, and the other two seeds give an independent5-set.

For positive a,b define:

    f11=max(0,10-a-b)+a max(0,b-2)+b max(0,a-2)>=6;
    f10,11=max(0,9-a-b)+a max(0,b-3)+b max(0,a-2)>=4;
    f9,11=max(0,8-a-b)+a max(0,b-4)+b max(0,a-2)>=2;
    f10,10=max(0,8-a-b)+a max(0,b-3)+b max(0,a-3)>=2.

Each bounds the excess on the disjoint sets A,B,{z}, using internal clique degree, forced cross edges, and z's neighbors in its two cliques. The last three minima are unique at(2,3),(2,4),(3,3), respectively, and all their excess at equality lies on z. Splitting at the thresholds in the positive parts proves these inequalities; the verifier independently enumerates their full finite domains.

If f11<=8, min(a,b)<=2; if a=2 then b<=4. When a<=b and a<=2, the excess on z and the SMALL-missing-side clique alone is at least

    max(0,10-a-b)+a max(0,b-2)>=6.                   (2)

For a=1 it is at least7; for a=2,b>=2 it is at least6. The remaining a=2,b=1 case has concentrated charge7 as well, so a=2 always gives at least6 even when this side is not the smaller one. This concentrated charge is useful even when the two-clique blockers overlap elsewhere.

For three star pairs on K10 and three different K11s, the simultaneous center charge is a(b-1), giving

    max(0,9-a-b)+a(b-1)+b max(0,a-2)>=6.             (3)

For two mixed pairs on K9, when two other points complete that K9, the corresponding bound is

    max(0,8-a-b)+a(b-1)+b max(0,a-2)>=5.             (4)

For a mixed K10/K11 pair with one additional vertex complete to its K10, or the usual diamond accounting, the bound is

    max(0,9-a-b)+a max(0,b-2)+b max(0,a-2)>=5.       (5)

For (3),(4), when b=1 the minima are6,5; when a=1 the bounds are at least7,6; on a,b>=2 they are at least7,6. For (5), a=1 or b=1 gives at least6; on a,b>=2 the expression increases in either variable and equals5 at(2,2). The four other scalar minima follow by the same elementary threshold split, with both variables below their respective thresholds or one/both above them.

### Shared-leaf accounting

If a K11 meets two pair points whose opposite missing sets lie in DIFFERENT cliques and have sizes a,b>=0, then at a vertex missing one or both points the internal10 neighbors plus those two point adjacencies give baseline12. Forced neighbors in different opposite cliques are disjoint. Therefore its excess is at least the sum of the corresponding max(0,a-2),max(0,b-2) contributions. Algebraically

    max(0,(a-1)+(b-1))>=max(0,a-2)+max(0,b-2).

The same statement applies to any subset of the two missing incidences. This permits simultaneous f11 and mixed charges sharing a leaf clique; it does not add the same vertex's full excess twice.

## 4. A triple on three K11s costs at least3 locally

Suppose z has support on three K11s and total excess on z and those three cliques is at most2. Its three nonempty missing sets have sizes a<=b<=c<=10 and total at least33-d(z)>=19. Hence b>=5 and b+c>=13.

Every vertex of those cliques has at most4 neighbors outside its own clique, since its excess is at most2. Pick x in the smallest missing set. After removing its neighbors from the other two missing sets, both remain nonempty, and their sizes sum to at least b+c-4>=9. They must be complete to each other, since otherwise x and a nonadjacent pair extend with z and the fourth seed to an independent5-set. One remaining part has size at least5, forcing a vertex of the other part to have at least5 external neighbors, contradiction. The local excess is therefore at least3.

## 5. Eliminate h=3

For {0123,01,23}, the two K11 pair blockers occupy disjoint clique pairs and distinct points, costing at least12.

For {01,023,123}, orient the01 missing sets so the smaller one is in K0. Formula(2) charges at least6 to its pair point and K0. The triple123 and K1,K2,K3 are disjoint from those charged vertices and cost at least3 by Section4. Thus T>=9>8. The other orientation uses triple023 instead.

## 6. Eliminate h=4

For {01,01,023,23}, the K11 pair23 costs6. If either01 point misses both supported cliques, its disjoint mixed blocker costs4. Otherwise both complete K0, costing at least7 on those two points by(1). Either way the total exceeds8.

For {01,012,03,23}, the pair01 must complete K0, since otherwise its cost4 is disjoint from pair23's cost6. If03 also completes K0, the two completing points cost7, disjoint from pair23. Otherwise03 has positive missing sets. Its K0 missing vertices have an additional neighbor at the completing01 point, so(5) applies. Shared-leaf accounting on K3 makes this cost5 additive to pair23's cost6. Contradiction.

For the star {01,02,03,123}, formula(3) is additive at K0 because the leaf cliques are distinct. At most one pair point can have positive K0 missing set. If one does, it costs6 and the other two completing points cost7 on disjoint vertices. If none does, all three complete K0 and are pairwise nonadjacent; each pair has combined excess at least7, so their total excess is at least11. Contradiction in either case.

## 7. The small-budget double-pair lemma

Consider two points supported on the same9/11 or10/10 clique pair, with total excess on the two cliques and the two points at most2. No point can miss both cliques. Indeed, its scalar charge would equal2 at the unique minimum, putting all excess on that point and zero on both cliques and its companion. The companion then cannot miss both cliques and must complete at least one. A missing vertex of the first point in that completed clique has internal neighbors plus its forced opposite missing set plus the completing companion:8+4+1=13 for9/11, or9+3+1=13 for10/10. This contradicts its zero excess.

Thus in9/11 both points complete the K9. In10/10 each completes one K10, cannot complete both (degree at least20), and they complete opposite K10s: two completions of the same K10 would cost at least7, exceeding the local budget2.

## 8. Eliminate h=5 with sizes9,11,11,11

Supports are {01,01,02,03,23}. The K11 pair23 costs6, leaving at most2 on K0,K1 and the doubled01 points. Section7 makes both01 points complete K0.

For02 and03, simultaneous center accounting on K0 now has internal8 neighbors plus the two completing points, and the remaining two point adjacencies, for baseline12. Shared-leaf accounting on K2,K3 combines their charges with the23 blocker. If either point has a positive K0 missing set, (4) costs5 in addition to f11>=6, impossible. Thus all four star points complete K9.

Pair23's charge leaves at most2 excess units on those four points. Every pair of them must be adjacent by(1), since a nonadjacent pair sharing nine neighbors requires excess at least6. They and K9 form K13, contradiction.

## 9. Eliminate P and D

In P, if both points of one doubled mixed pair complete its K10, their excess is at least7; the disjoint other pair costs at least4 if either point misses both cliques, or at least7 if both complete its K10. Thus each doubled pair contains a noncompleting point. Selecting one per pair costs4+4=8 on disjoint sets. Equality forces missing sizes(2,3), excess4 at each selected point and zero at every clique vertex and companion. A companion cannot miss both cliques, so completes its K10; then the selected point's missing K10 vertices have degree at least9+3+1=13, contradiction.

In D, the distinct support pairs give the pointwise accounting

    epsilon(v)>=sum_(incident missing e)max(0,a_opposite,e-2).

At a K10, internal degree 9 plus three supported point adjacencies gives baseline 12. A missing incidence replaces that point by a_opposite forced neighbors, giving increment a_opposite-1. There is only one potentially negative increment, from its K10 neighbor, because a point cannot complete a K11. For any subset of at most three increments with at most one negative term, max(0,sum(a-1))>=sum max(0,a-2): every positive right-hand term has one spare unit to absorb the possible -1. At a K11 there are only two increments, and the shared-leaf inequality applies. Thus the displayed inequality includes all zero-missing-set cases. Every mixed point not complete to its K10 contributes at least5 by(5).

If one K10 has two completing mixed points, these cost7 on their two points. The other K10 either has a noncompleting mixed point (additional cost5 via the pointwise accounting) or two completing points (additional cost7). Both exceed8. Otherwise at most one mixed point per K10 is completing, leaving at least two noncompleting mixed points and total charge at least10. D is impossible.

## 10. Eliminate B={01,01,02,13,23}

Pair23 costs6. The doubled10/10 pair01 therefore has local budget at most2. Section7 makes its points complete opposite K10s. Consider mixed point02. If it misses K0, its K0 missing vertices have the extra neighbor at the01 point completing K0. Shared-leaf accounting on K2 combines (5) with f11 for23, giving at least5+6=11. Otherwise02 completes K0; together with its01 completer it costs7 on two points, disjoint from23's six-unit charge. Contradiction.

## 11. Two points on the same K11/K11 pair are impossible at T<=8

Let their missing sets in X,Y be A,B and A',B', with sizes a,b,a',b'. All are positive. Each f11<=8, so each point has a missing set of size at most2. A point with a size-two missing set on one side has missing size at most4 on the other.

If the small missing sides are necessarily opposite, (2) costs at least6 on z+X and at least6 on z'+Y, disjoint. Otherwise relabel X so a,a'<=2 and order a<=a'.

- a=a'=2: the first point plus X costs at least6 by(2); the second point has epsilon>=10-2-b'>=4 since b'<=4. Total at least10.
- a=1,a'=2, A disjoint A': the vertex of A is adjacent to z' and to every vertex of B. Its excess is at least b-1. Together with epsilon(z)>=max(0,9-b), this costs at least8; epsilon(z')>=4 is additional.
- a=1,a'=2, A subset A': let x be the shared vertex and y the other vertex of A'. The union B union B' forces epsilon(x)>=max(0,b-2); together with z this costs at least7. Vertex y sees z and B', so epsilon(y)>=b'-1; together with z' this costs at least7. These four charged vertices are distinct.
- a=a'=1, A and A' distinct: each missing vertex sees the other point and its own opposite missing set. Each vertex/point pair costs at least8, for total at least16.
- a=a'=1, A=A'={x}: the two points cannot be adjacent, because they share ten neighbors in X, which would make K12. Put B0=|B union B'|. Their common neighborhood has at least21-B0 vertices, so(1) forces epsilon(z)+epsilon(z')>=18-B0. The vertex x has excess at least max(0,B0-2). Total at least16.

All cases exceed8. The full intersection-parameter enumeration independently gives the stronger lower bound14, but that numerical result is not needed by this analytic proof.

## 12. Eliminate C and conclude

C={01,01,01,23,23} contains two points on the same K11 pair23 and is excluded by Section11. Every support orbit has now been eliminated. The five abstract286-edge hypotheses are inconsistent.

For R(4,47), the accepted previous workstream proves e>=286 and the generic gate e<=286=>delta>=12. The only new equality case has just been excluded, so the strict floor is287. This is a new boundary theorem, not an extrapolation of the old9-common-neighbor bound.
