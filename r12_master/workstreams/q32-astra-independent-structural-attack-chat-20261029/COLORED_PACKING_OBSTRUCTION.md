# Colored packing and the nonempty-fiber obstruction

Date: 2026-10-29
Status: PROVED_CONDITIONAL on the source local 3+7 normal form described below.

## 1. Outside-edge packing

NEAR_TURAN_STABILITY_THEOREM.md proves the universal57-edge reserve and its eleven-color contradiction627>626 for a (12,12,12,11) target partition. It counts actual edges, each in exactly one color, not component multiplicities.

The single-color bound57 is sharp. sharp_typeI_single_color.json gives an explicit source-correct129-edge graph with alpha=12, omega=5, independent tracks of sizes11,12,12,12, and exactly57 outside edges. Thus a hypothetical58-edge per-color strengthening is false even in the correct Type-I family.

## 2. Stronger 3+7 theorem: both fiber partitions cannot be nonempty

Use the registered m=10 disconnected3+7 normal form:
- three small pivot blocks form four target triangles, one per small label;
- seven outer blocks contain four target K7 tracks;
- residual R has7 vertices and partitions into four clique fibers F_s of the small map and four clique fibers G_g of the outer map;
- every residual point is joined to the three small vertices in its F-label and the seven outer vertices in its G-label;
- every outer vertex q has d_R(q)+e_Q(q)=3;
- for each outer block D, exactly three extra small-to-outer edges give sum_q k(q)=3, with k(q)<=e_Q(q);
- sum_D y_D=8-2z, 0<=z<=4, and sum_(q in D)d_R(q)=7+y_D;
- the source local 4,5,5 classification says each block has either three aligned small-to-outer base matchings, or a synchronized transposition switch. In the aligned case with all common intersections singleton, the common labels are a permutation. In the switch case a label is duplicated, another omitted, and the two duplicated-label vertices receive respectively two and one extra edges;
- the singleton-track blocker forces q with common label s to meet all F_s; a two-label common intersection forces d_R(q)=0.
These are the local statements in V47_ZERO_SLACK_MAP_ALIGNMENT_AND_TRANSVERSAL_BLOCKER.md and the outer holonomy / residual-track results. They are named hypotheses, not a claim to have replayed their entire upstream chain.

**Claim.** If all four F_s and all four G_g are nonempty, the core contains a target K12 (indeed a K13 in one profile). Therefore no genuine T61 completion has both partitions nonempty.

### Step1: no double-label outer vertex

Every q meets its nonempty G_g, hence d_R(q)>=1. The double-label conclusion d_R(q)=0 is impossible. All common intersections are therefore singleton.

### Step2: the two unordered partitions coincide

For each block D, put eta_D=sum_q |F_(s(q)) minus G_(g(q))|.
The neighborhood union bound gives y_D>=eta_D.
If the unordered partitions differ, eta_D>=1 for every block:
- for an aligned permutation, eta_D=0 would inject four nonempty F-fibers into the four distinct G-fibers and hence make the partitions identical;
- for a switch, the same nonempty F-fiber cannot lie in two disjoint G-fibers.
For z>=1 this implies y>=7, contradicting y=8-2z<=6.
For z=0, e(H[R])=3 and the two four-clique partitions of7 vertices must both be the three edges and singleton of 3K2+K1.
Thus in every case F=G as unordered partitions. Relabel them equally.

Since Delta(H[R])<=2, fiber sizes are at most3. The only nonempty profiles are (3,2,1,1) and (2,2,2,1).

### Step3: a size-three fiber gives K13 directly

Let F_h=G_h have size3. Every outer vertex in outer track h is adjacent to G_h. Its common label s must be h: if s differs, the disjoint nonempty F_s would force d_R(q)>=4, exceeding d_R(q)<=3.
Consequently all seven vertices of outer track h meet all three small vertices of label h. Together with F_h, they form a target clique of size7+3+3=13.

This argument does not assume that the remaining singleton labels align.

### Step4: the (2,2,2,1) profile forces full alignment

First exclude a switch. Its vertex receiving two extra edges has d_R<=1. Its outer fiber and common fiber must therefore both be the unique singleton fiber; hence the duplicated common label is that singleton. The other duplicated-label vertex receives one extra edge and lies in a different, size-two outer fiber. It must meet that size-two fiber and the disjoint singleton, forcing d_R>=3 while k>=1 forces d_R<=2. Contradiction.

Thus the common labels in each block form a permutation. For a nonidentity permutation, the sum eta_D is at least3: the least expensive moved pair consists of the singleton and a two-point fiber. But
7+eta_D <= sum_q d_R(q) <= sum_q (3-k(q)) =12-3=9,
so eta_D<=2. Contradiction.
Hence every common label equals its outer label.

The three small vertices, seven outer vertices, and two residual vertices in any size-two fiber form a target K12. QED.

The genuine parent omega(F)<=11 excludes both outcomes. This is a complete conditional contradiction, not just a new necessary inequality.

## 3. Consequence for the18 registered residual types

A graph of maximum degree2 is a disjoint union of paths and cycles. If R cannot be covered by three cliques, any partition of R into at most four clique fibers uses four nonempty fibers. Both F and G must then be nonempty, and Section2 excludes the cell.

Under |R|=7, Delta(R)<=2, alpha(R)<=4, clique-cover number<=4, and 3<=e(R)<=7, there are18 unlabeled path/cycle types. Four have clique-cover number3:
- C3 + P2 + P2, z=2;
- C3 + P4, z=3;
- C3 + C3 + P1, z=3;
- C3 + C4, z=4.

The other14 types have clique-cover number4 and are excluded by Section2. This includes the two alpha=3 odd-cycle types C5+P2 and C7, not only the alpha=4 rows.

At this stage a surviving3+7 completion must have one of those four types AND at least one of F,G must have an empty fiber. Section4 below now excludes the fourth type. This does not assert that any remaining type is realizable. Other light-component splits and m=8,9 are not classified here.

verify_residual_types.py independently enumerates component multisets and computes independence and clique-cover numbers by direct subset search on the resulting7-vertex graph. Its finite classification is supplemental to the analytic theorem.

## 4. New theorem: the z=4 empty-fiber cell is impossible

Date: 2026-10-30. Status: PROVED_CONDITIONAL on the registered3+7 normal form, alpha(H)<=4, delta(H)>=12, and the genuine parent omega(H)<=11. The proof is analytic; the finite replay below is supplementary.

**Theorem.** No graph in that normal form has z=4 and residual R=C3+C4. Together with Section2, this excludes every z=4 residual type in the registered m=10 disconnected3+7 cell. It does not exclude other light-component splits or m=8,9.

### Exact zero-slack bookkeeping

Write the three small independent4-blocks as S1,S2,S3, with the same-label edges giving four triangles. Write the seven outer independent4-blocks as D1,...,D7, with same-label edges giving four K7 tracks. F_s and G_g are the two residual clique partitions. Each residual vertex already has ten pivot neighbors, three small and seven outer. In C3+C4 it also has two residual neighbors. The residual equation d_R(r)+b_r=2 therefore gives b_r=0. Every outer vertex q_g has exactly G_g as its residual neighborhood; likewise small vertex s has exactly F_s.

For each small-to-outer pair there is a unique base perfect matching and one extra edge. Let e_D(s) count the three extras ending at small label s, aggregated over the three small blocks, and E_s=sum_D e_D(s). Thus sum_s e_D(s)=3 and sum_s E_s=21.

A small vertex has base degree9 plus |F_s| residual neighbors. Minimum degree12 implies, on summing over the three small blocks,

    E_s >= 3(3-|F_s|).                                      (4.1)

For an outer block D, its four vertices have total residual degree7 and total excess-pivot degree5, since d_R(q)+e_Q(q)=3. Three of these excess incidences go to the small blocks. Hence exactly two go to other outer blocks. Every heavy outer pair uses at least one such incidence at each endpoint. Therefore

    each outer block has at most two heavy outer neighbors. (4.2)

An outer pair that is not heavy consists precisely of the four same-label edges; call it light. No assumption on the arrangement or weights of the heavy pairs is needed beyond (4.2).

### Local facts and an empty-column observation

For a given outer vertex q, intersect its three small-block neighbor-label sets; call the intersection I(q). The registered4,5,5 classification and blocker give:

1. The three base matchings are all the same permutation, or two agree and the third differs by one transposition.
2. In the aligned case I(q) is its base singleton, except that all three extras can meet the same q from the same second label, making I(q) a doubleton.
3. In a switch every I(q) is a singleton. One label s is duplicated and another omitted; all three extras have small label s.
4. Every I(q) is nonempty. If I(q)={s}, then F_s is a subset of G_g. A doubleton is possible only when G_g is empty.

There is one useful direct strengthening. If an empty-residual q has doubleton I(q)={a,s}, then F_a union F_s is a clique. Otherwise choose nonadjacent residual vertices r in F_a and r' in F_s. Together with q and two small vertices of the other two labels in distinct small blocks they form an independent5-set. This contradicts alpha(H)<=4.

The clique partitions of C3+C4 into at most four classes are elementary: two have three nonempty classes, consisting of the triangle and one of the two perfect matchings of the4-cycle; each has one empty class. The other ten are obtained by splitting exactly one class of one of those partitions into two nonempty cliques. In a four-nonempty partition there is exactly one pair of classes whose union is a clique.

### Unequal empty/nonempty statuses are impossible

Suppose F has one empty class and G has none. A doubleton is impossible. An aligned singleton permutation would place every F class inside a distinct G class; since both partitions cover the same seven vertices, all four containments would be equalities, contrary to their empty-class counts. A switch duplicates a label s, so F_s is contained in two disjoint G classes and must be empty. Thus all three extras in EVERY outer block have that empty small label. A nonempty size-two F class receives no extras, contradicting (4.1).

Suppose F has no empty class and G has one. At the empty G column a singleton is impossible, so every outer block is aligned with a doubleton {a,s} there. All three extras have label s. The preceding observation says F_a union F_s is a clique; hence a,s are the unique mergeable pair of F classes. Consequently the other two F classes receive no extras from ANY outer block. At least one of these two has size at most2, contradicting (4.1). This covers all ten nonempty F partitions, whether or not G is their coarsening.

The case where both partitions are nonempty is already excluded by Section2.

### Both empty partitions must coincide

Each has sizes (0,3,2,2). If they differ as unordered partitions, their4-cycle edge pairings differ, so no size-two F class is contained in any G class.

For an aligned block with only singleton intersections, the containments force equality of the partitions, impossible. In a switch the duplicated label must be the empty F class; of the two remaining nonempty common labels at least one is a4-cycle edge, which cannot be contained in its G class. In an aligned block with a doubleton {a,s} at the empty G column, the clique-union observation forces at least one of F_a,F_s to be empty: no two nonempty classes of a (0,3,2,2) partition have clique union. Among the remaining singleton intersections at least one size-two F class still occurs, again impossible.

Thus F=G after relabeling. Set F_0=G_0=empty, F_1=G_1=C3, and F_2=G_2,F_3=G_3 equal to the two cycle edges. Equation (4.1) gives

    E_0>=9, E_2>=3, E_3>=3.                                (4.3)

### Special blocks and their light neighbors

In the triangle outer column q_1, residual degree3 forces k(q_1)=0. Its common label is therefore the common base label of all three matchings, and can only be0 or1.

Call D special when that common label is0. Its full local form is forced:

    all three base matchings: tau=(0 1), fixing2,3;
    all three extras: small label0 to outer column0.       (4.4)

To see this, a switch duplicates the empty label0, hence its transposition involves0; the three base matchings would then disagree on the image of0, contrary to their common image q_1. So the matchings are aligned. The singleton containments at columns2,3 force their labels to be2,3. Column0 then has base label1, which cannot be its singleton common label since G_0 is empty. It must be a doubleton, requiring exactly the three extras in (4.4).

**Light-neighbor lemma.** Any outer block E light-adjacent to a special D is either special, or has

    all three base matchings: identity;
    all three extras: small label1 to outer column0.       (4.5)

Proof. Apply the4,5,5 classification to each triple S_j,D,E, using the identity matching between D and E. The fixed D extra (small0,outer0), relative to its tau base, permits either the same tau base at E, or the unique transposition alternative: identity base and extra (small1,outer0). These are statements for each j separately. At E's triangle column, k=0 again, so the three base labels there must coincide. Hence the three choices are either all tau or all identity. The former is (4.4); the latter forces all three extras as in (4.5). QED.

### Terminal contradiction

Let a be the number of special blocks. In each of the other 7-a blocks, the triangle-column vertex meets the three small vertices of label1. Together with those three vertices and the residual triangle, these vertices form a clique of size

    (7-a)+3+3=13-a.

The genuine parent clique cap11 forces a>=2.

Call a block other if it is neither (4.4) nor (4.5). All extras at labels2 and3 must occur in other blocks. Their total required count is at least6 by (4.3), and each block has only three extras. Thus the number b of other blocks is at least2.

By the light-neighbor lemma every special-other pair is heavy. Equation (4.2) implies a<=2 and b<=2. Therefore a=b=2. The two other blocks have exactly six extras altogether, all consumed by the required labels2 and3, and contribute nothing to E_0. Each special block contributes three to E_0; every remaining block has form (4.5), contributing zero. Thus

    E_0=6<9,

contradicting (4.3). This completes the proof.

### Verification and precise scope

verify_z4_empty_fibers.py checks the local ingredients by direct independent-set search, without an external solver. It enumerates all3456 normalized4,5,5 triples and verifies the exact156 accepted patterns. It then enumerates all42336 three-small-block matching/extra configurations and all44 ordered F,G pairs with an empty class; every admitted23-vertex graph is checked for independent5-sets. Assertions check the case reductions, the forced special form, and the light-neighbor lemma on every raw accepted configuration before deduplication. z4_local_profiles.json records the158 distinct necessary summaries with representatives. They are not full Q32 assignments.

Completeness of this local replay: labels of the fixed residual graph may be named0,...,6 without loss; all its four-clique partitions are enumerated. Sorting each unordered partition removes only independent small/outer label permutations. Those label choices are restored by all24 base permutations. The4,5,5 classification supplies exactly the aligned and synchronized-switch possibilities, including every minority small block and both transposition orientations. The graph construction includes all edges of the selected23-vertex induced local graph. It deliberately omits the other six outer blocks, the14 outside vertices, and the eleven other colors. Thus acceptance is only a necessary local condition, never a global realization certificate. The analytic degree/clique argument above supplies the global contradiction within the stated normal form.

After Section4 the remaining3+7 residual types are C3+2P2 (z=2), C3+P4 (z=3), and2C3+P1 (z=3), with at least one empty fiber. Section5 below further excludes2C3+P1. Full Q32 and the original EG617 problem remain OPEN / NOT_CERTIFIED.

## 5. New theorem: the z=3 two-triangle cell is impossible

Date: 2026-10-30. Status: PROVED_CONDITIONAL on the same registered3+7 normal form and genuine parent clique cap. No full-color solver is used.

**Theorem.** There is no graph in that normal form with R=2C3+K1, z=3, alpha(H)<=4, and omega(H)<=11. This includes every empty/nonempty status of the two residual fiber partitions. Combined with Sections2 and4, sixteen of the eighteen residual types are excluded.

Write R=T1 disjoint-union T2 disjoint-union {r}, with T1,T2 triangles. The residual equation b_v=2-d_R(v) gives b_v=0 on both triangles and b_r=2. Therefore only r can have any additional outer neighbor beyond its full G-track. Small-block residual neighborhoods remain exactly their F-fibers. For an outer block D let y_D count additional residual incidences and t_D count outer-to-outer extra-edge incidences. The source ledger gives

    t_D+y_D=2,   sum_D y_D=2.                              (5.1)

Every vertex in a G-track occupied by a full residual triangle has residual degree3. The exact outer-vertex degree equation then gives k=0 and no additional residual or outer-extra incidence at that vertex. Its common small label is thus the same base-matching label in all three small blocks.

### 5.1 All unequal empty-class statuses force K13

There is exactly one unordered three-class clique partition of R: T1,T2,{r}. Thus an empty-fiber partition is this partition plus an empty class. Each four-nonempty partition splits one of the triangles into a pair and singleton, leaving the other triangle and {r} intact. There are six such partitions.

If both F and G have four nonempty classes, Section2 applies.

Suppose F has four nonempty classes and G has an empty class. Let T be the triangle left unsplit by F; it is also a full G class. Every outer vertex in its G-track has residual degree3 and hence a singleton common label. Because no triangle vertex has an additional neighbor, the only nonempty F class contained in its residual neighborhood T is F_s=T itself. Thus all seven vertices in that track meet the three small vertices of label s. These vertices and T form a K13.

Suppose F has an empty class and G has four nonempty classes. Let T1 be the triangle split by G and T2 the unsplit triangle. No outer vertex can have F-label T1 as its singleton common label: it would need all three vertices of T1, but no G class contains T1 and none of those three vertices has an additional neighbor. Since all G classes are nonempty, a doubleton is impossible. Thus each outer block is a switch, and its omitted common label must be T1. The T2 label consequently occurs, and the only outer vertex that can carry it is the vertex in the full T2 G-track. Again that entire K7 track meets the same small triangle, giving K13 with T2.

Hence only the case where both partitions have an empty class remains. They necessarily coincide. Label them

    F0=G0=empty, F1=G1=T1, F2=G2=T2, F3=G3={r}.            (5.2)

### 5.2 Two diversion classes

For i=1,2, the vertex in column i of any outer block has residual degree3 and k=0. Its singleton common label can only be i or0. Let A_i be the set of outer blocks whose column-i common label is0, and let a_i=|A_i|.

The two sets A1,A2 are disjoint: their triangle columns have no small-extra incidences, so their common labels are base-matching labels; a bijection cannot assign small label0 to both columns.

In the other 7-a_i blocks, column i meets all three small vertices of label i. Together with T_i these vertices form a clique of size13-a_i. The parent cap11 therefore forces

    a_1>=2,   a_2>=2.                                    (5.3)

**Opposite-diversion lemma.** Every pair D in A1, E in A2 is heavy.

Proof. In each small-block-to-D base matching, the inverse labels at outer columns1,2 are respectively0,2. In each small-block-to-E matching they are respectively1,0. These two permutations are neither equal nor related by one transposition: the change at column1 would require swapping small labels0 and1, which cannot also change label2 at column2 into0. If D-E were light, its matching would be the global outer identity, and the4,5,5 classification on S_j,D,E would allow only equal matchings or a single-transposition difference. Contradiction. QED.

Every block in A1 thus has at least a_2 heavy outer neighbors, and conversely. Each heavy neighbor costs at least one incidence in (5.1), where t_D<=2. From (5.3),

    a_1=a_2=2, and y_D=0 for all D in A1 union A2.         (5.4)

All four blocks have used their entire heavy-incidence budget on the opposite diversion class. Each of the remaining three outer blocks must therefore be light-adjacent to all four.

### 5.3 Exact special forms at the four zero-slack blocks

For D in A_i, y_D=0 makes every residual neighborhood exactly its G class. A switch would duplicate an F class, which under zero slack must be the empty class0. Its transposition would then involve0, making the three base matchings disagree on the image of0. This is incompatible with the column-i common base label0. Thus D is aligned.

Its other triangle column has its own label. Its singleton column must have label3: the other possible contained F class is empty, and label0 is already used at column i. Therefore all three base matchings are tau_i=(0 i). At column0 the base label is i, whose nonempty F-fiber cannot be a singleton common label there. The only possible doubleton is {i,0}, since a triangle has no complete join to {r} or the other triangle. Hence

    S_i: all three bases tau_i; all three extras (small0, outer0).  (5.5)

### 5.4 The remaining three blocks are impossible

Fix any remaining block E. It lies in neither diversion class, so at each triangle column i its common base label is i. It is light-adjacent to an S_i block for both i=1 and i=2.

Apply the4,5,5 classification to the triple consisting of a small block S_j, a fixed outer block D_i of form (5.5), and E. Relative to (5.5), a light neighbor has either the same tau_i base, or the identity base with extra (small i,outer0). The first option would put base label0 at column i of E, contrary to that column's common base label i. Thus every small-block-to-E matching is identity and every one of its three extras is (small i,outer0).

For i=1 these extras must all have small label1; for i=2 they must all have small label2. An extra edge cannot have both small labels. Contradiction. This completes the proof.

This argument permits both additional incidences of r throughout. It does not assume the z4 zero-slack condition globally: zero slack at the four diversion blocks is deduced in (5.4). It does not require choosing a particular weighted-heavy-graph isomorphism type.

### 5.5 Independent finite replay and remaining interface

verify_z3_two_triangles.py considers all42336 aligned/switch matching representations, all13 ordered partition pairs with at least one empty class, and all ways the isolated residual vertex can have zero, one, or two additional neighbors in the selected outer block. The six triangle vertices have no such choice because their budgets are zero. Each admitted23-vertex local graph is checked directly for independent5-sets and the outer-vertex degree cap. Sorting partitions removes only label names, restored by the complete permutation loop. The local assignments and counts are in z3_two_triangles_verification.json.

The replay admits564 raw local configurations:534 for the equal empty partitions and30 for unequal empty/nonempty statuses. Every unequal-status configuration has the forced full-triangle common label used in Section5.1. In the equal-partition case it checks every opposite-diversion pair for light incompatibility and every remaining candidate against both fixed special forms. These are local necessary-condition checks, not full Q32 SAT assignments or a full-model UNSAT proof certificate. The analytic proof above supplies the global contradiction under the named normal-form premises.

The remaining registered3+7 residual types are now only C3+2P2,z2 and C3+P4,z3, with at least one empty class. For C3+P4 the two additional incidences belong to the two path endpoints; for C3+2P2 four incidences belong to the four edge endpoints. Those positive budgets remain to be analyzed. Other m10 light-component splits and m8,m9 remain outside this theorem.

