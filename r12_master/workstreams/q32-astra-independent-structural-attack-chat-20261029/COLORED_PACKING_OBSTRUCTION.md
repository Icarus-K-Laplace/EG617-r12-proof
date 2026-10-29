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

A surviving3+7 completion must have one of those four types AND at least one of F,G must have an empty fiber. This does not assert that any of these four types is realizable. Other light-component splits and m=8,9 are not classified here.

verify_residual_types.py independently enumerates component multisets and computes independence and clique-cover numbers by direct subset search on the resulting7-vertex graph. Its finite classification is supplemental to the analytic theorem.

