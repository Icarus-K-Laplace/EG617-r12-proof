# Degree-capacity mechanism

## D1. Six-unit global budget — PROVED

For epsilon(v)=d_H(v)-12, sum epsilon=570-564=6. At most six vertices have positive excess, every degree is at most18, and the proof of U1 finds an independent four-set consisting entirely of degree12 vertices.

Its48 neighbor incidences cover43 vertices. The overlap surplus is exactly5. The private-neighbor sets are cliques by alpha(H)<=4. The clique cap11 then leaves at most five multiple-neighbor vertices. This is the structural mechanism, rather than a scalar edge-count contradiction.

## D2. Common-antineighborhood capacity — PROVED relative to second Turan

No25-set can have independence number at most2: its target edge requirement is155 while its global degree capacity is at most153. Thus every nonedge uv obeys

    codegree(u,v)<=3+epsilon(u)+epsilon(v).

Two external vertices cannot both complete a K10. This rules out the dangerous zero-missing-set alternatives in the private-clique argument. A vertex MAY complete a K10 or K9 individually; pretending every missing set is nonempty would be an illegal strengthening. The proof explicitly keeps these alternatives.

## D3. The final75-edge completion ledger — PROVED

In U1 let X count target edges between distinct K_i, E=e_H(Z), and epsilon_Z=sum_(z in Z)epsilon(z). Let B=e_H(Z,H minus Z). Then

    B+2E=60+epsilon_Z,
    200+X+B+E=285,
    X=25+E-epsilon_Z.

Ten edges of B are the fixed distinguished-vertex supports. Every remaining edge avoids those four distinguished vertices. Therefore75 edges must be selected from:

-541 pairs between distinct private groups of orders9,9,10,10;
-190 pairs between the38 private vertices and Z;
-10 pairs within Z.

For a private vertex in a10-clique, its variable degree is3+epsilon(v); in an11-clique it is2+epsilon(v). For z in Z its variable degree is10+epsilon(z). The excesses are nonnegative and sum6. The two support templates D and P have the same scalar ledger; their actual adjacency constraints differ.

## D4. Parent outside-edge ledger — PROVED_CONDITIONAL on genuine T61

Let a=e_F(A) and b=e_F(A,H). Then a+b=110 after removing the13 target p-A edges. Summing d_F(a)>=13 over the13 shell vertices gives2a+b>=156, so a>=46.

On the14-set O, each non-target color has at least two edges by alpha(C)<=12. Consequently13+a<=91-22=69, so a<=56. Thus46<=a<=56 and54<=b<=64. These bounds follow directly from the original color and degree conditions; no local candidate-derived cut is promoted to an unconditional assertion.

## D5. Mixed pair capacity - PROVED

A pair-supported point z on a K10 and K11, missing a>=1 and b>=1 vertices respectively, forces the complete a-by-b cross graph. Its own excess and the excesses of those missing vertices sum to at least

    max(0,9-a-b)+a max(0,b-3)+b max(0,a-2)>=4.

The P template has two disjoint mixed-clique pairs, each with two supported points. At most one point in either pair can complete its K10, by U3. Thus the global excess is at least8, impossible.

## D6. Simultaneous diamond incidence capacity - PROVED

In D, different support edges join different clique pairs. For v in K_i the forced cross edges attached to its missing support points therefore do not overlap. Its internal clique degree plus its support degree is12. With a_{j,e} the missing count in the opposite clique,

    epsilon(v)>=max(0,sum_{e missing v}(a_{j,e}-1))
              >=sum_{e missing v}max(0,a_{j,e}-2).

The second inequality retains all zero counts: a K10 has at most one neighboring K10 support; a K11 has only two incident supports. At most one negative term can coexist with a positive term. The exact reasoning is in step8 of the theorem.

Each mixed support point missing both cliques contributes, after summing this pointwise accounting,

    max(0,9-a-b)+a max(0,b-2)+b max(0,a-2)>=5.

Of four mixed points at least two miss both cliques, because at most one exterior point completes each K10. Thus the global excess is at least10, impossible.

## Universal closure - PROVED

The actual available excess is six. P requires eight and D requires ten. The structural reduction is exhaustive, so the core contract is inconsistent. These inequalities use only the true CORE assumptions and the independently named common-neighbor lemma; there is no omega(H)<=5 assumption or source-color placement cut.
