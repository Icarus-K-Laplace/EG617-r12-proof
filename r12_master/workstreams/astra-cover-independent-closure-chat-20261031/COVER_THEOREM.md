# Independent COVER theorem and E407/E408 h13 elimination

Date: 2026-10-31. Status: **PROVED under the explicit hereditary T61 contract below**, using the accepted prior lower-order proof and the standard Andrasfai--Erdos--Sos theorem. No historical COVER, V7--V12 classification output, MS-29 assertion, or zero-correction-cycle inference is an input.

## 0. Statement, conventions, and dependencies

Let F be a simple graph with 61 vertices, delta(F)=13, alpha(F)<=5, omega(F)<=11, and

    e(F[U]) <= D(|U|) for EVERY U subset V(F),
    D(n)=binom(n,2)-11 p12(n),
    p12(12a+b)=12 binom(a,2)+ab, 0<=b<12.

Let E=e(F) be 407 or 408. A regular vertex means exactly degree 13 in F. For a regular pivot p let A=N_F(p), C=F-N_F[p], M=complement(F[A]), g_a=d_F(a)-13, t_a=|N_F(a) intersect V(C)|, z=e(M), G=sum_A g_a, and q_p=z+G. Put Q=max q_p over ALL regular vertices. These are the original charge definitions.

**COVER.** If E=407 then Q>=30. If E=408 then Q>=31.

The accepted 287-edge theorem gives Q<=29 and Q<=30, respectively. Consequently both full h13 energy layers are empty under the stated contract. This is not a conclusion about h12 or the entire EG617 root.

The only prior research input used below is the explicitly proved lower-order chain M1--M5 in `MINIMUM_DEGREE_GATE_SELF_CONTAINED.md`, low-edge commit `783c72090205d4bd1a6eefce1dec09e15f78e319`:

1. R(2,24) is empty; every R(2,23) has at least131 edges.
2. Every R(3,35) has minimum degree at least12.
3. Every R(3,36) has minimum degree at least13 and at least234 edges; R(3,37) is empty.

Here R(a,n) includes alpha<=a, omega<=11 and all D caps. The earlier source supplies a complete cap-based proof of these assertions, including the formerly missing 23-point argument; its statements and proof were read, rather than inferred from a status label. They do not depend on COVER or any h13 energy closure. The earlier 284/285/286 obstruction proofs are not rerun. Section 8 uses the standard AES theorem only at n=35, forbidden K4, minimum degree22; its exact strict threshold and primary source are recorded below.

The finite classification in Section 6 is newly reconstructed. The independent verifier enumerates row multiplicities and decorations from scratch, and does not read the exploratory generator or historical outputs. All graph-to-state reductions are proved here.

## 1. Parent inheritance and exact identities

The 47-core C has alpha<=4: an independent five-set there extends with p. It inherits omega<=11 and all D caps. Decorations are nonnegative. For a in A,

    t_a=d_M(a)+g_a,
    e_F(A,C)=2z+G,
    E=91+q_p+e(C).

The induced 14-set N[p] has 91-z edges, so z>=22 from D(14)=69. Also alpha(M)<=10, since a target K11 in A extends with p to K12. For every S subset A,

    q_p=t(S)-e_M(S)+e_M(A\S)+G_(A\S).             (1)

There are regular vertices: this is included in delta(F)=13, and also follows from the average degree being below14 if only delta>=13 is assumed. No exceptional regular pivot is discarded.

## 2. Global degree-11 core interface and deficient clique

There is no induced H in R(3,36) inside F. Otherwise the prior lower-order theorem and D(36)=234 force H to be 13-regular. Every outside vertex has at most3 neighbors in H by D(37)=237. If the outside25-set contained an independent triple, at least27 H-vertices would avoid it and would contain an independent triple by R(2,24) emptiness. This gives an independent six-set in F. Thus that outside25-set has alpha<=2, again contradicting R(2,24).

It follows that EVERY actual 47-core C has delta(C)>=11: a vertex of core degree at most10 leaves an induced R(3,36) in its non-neighborhood. This statement has no core edge-count assumption.

For any such C, its degree-11 vertices form a clique. Indeed, if two of them x,y were nonadjacent, y lies in the 35-point non-neighborhood of x, a member of R(3,35). Its degree there is at most11, contradicting the prior minimum-degree12 theorem.

For a missing-shell edge ab, the C-vertices outside N_C(a) union N_C(b) have alpha<=3, and cannot contain36 vertices by the embedded exclusion. Therefore

    |N_C(a) union N_C(b)|>=12, hence t_a+t_b>=12. (EDGE12)

A missing triangle has row union at least24, by R(2,24) emptiness. A missing K4 has row union at least36, since its uncovered core is a clique of size at most11. In particular

    t(T)>=24 for every M-triangle T,
    t(S)>=36 for every M-K4 S.                    (2)

For q<=28, M is K4-free, since (1),(2) would give q>=36-6=30.

## 3. Exact repivot and inserted-degree inequalities

Let y be a regular shell vertex. Write d=d_M(y), S=N_M(y), D_y=N_C(y); both sets have size d. The new core is (C minus D_y) union S. Put

    rho=e_M(A\S)+G_(A\S), m=e_M(S),
    h_beta=sum_(x in D_y)(d_C(x)-beta),
    kappa=binom(d,2)-e_C(D_y), b=e_F(S,D_y).

Direct edge partition, with no inequality, gives

    q_y=d(beta+1-d)+rho+h_beta+kappa+b.            (3)

The sum of new-core degree excess over beta on inserted vertices S is

    eta_beta=q_p-d(beta+1-d)-rho-m-b.             (4)

Thus when both cores have minimum degree at least beta, h_beta and eta_beta are nonnegative. In particular, at beta=11 this is valid for EVERY regular repivot, and (4) implies the useful shell-only condition

    t(S)-2e_M(S)>=d(12-d).                       (INS11)

The exact signed identity is

    q_y-q_p=h_beta-eta_beta+kappa-m.

A closed walk gives only sum(h_beta+kappa)=sum(eta_beta+m). No summand is set to zero from a closed walk. Below zero corrections arise only from a specified maximum charge and a matching lower bound in (3). At beta=12 the minimum-degree hypothesis is separately licensed at each use.

## 4. Matching and triangle-free reductions

Every 13-point M with z>=22 and alpha(M)<=10 has a 3-matching. To prove this, suppose its matching number is2 (number <=1 gives only a star or a triangle and at most12 edges). Let S be the four endpoints of a maximum matching and I the remaining independent9-set. The bipartite cross graph has matching number at most2, hence a vertex cover of at most2 by Konig's theorem. A cover using one point of S and one of I supports at most12 cross edges; one using two points of I supports at most8. Even adding all six edges on S gives fewer than22. Therefore the cross cover consists of two points of S. There are at least16 cross edges, so two disjoint cross edges exist on those two cover points. The other two S-points cannot be adjacent, as that would make a 3-matching. They and I are consequently independent11, a contradiction.

Suppose now M is triangle-free and q<=28. A 4-matching, EDGE12 and Mantel would give q>=48-16=32 on its eight endpoints. Thus its matching number is exactly3.

Such M must be bipartite. A shortest odd cycle has length5 or7; longer ones have a 4-matching. A C7 has neither an exterior edge nor an exterior attachment: either would combine with a perfect matching of the appropriate cycle remainder to give four disjoint edges. It then has only7 edges. For a C5, the outside8-set has matching number at most1. If it has no edge, at most16 attachments give z<=21. If it has one edge ab, no outside vertex other than a,b can meet the cycle, giving z<=5+1+4=10. If it has at least two edges, its nontrivial part is a star or a triangle; cycle attachments can occur only at the intersection of all outside-edge endpoint sets. There are at most7 outside edges and at most2 attachments, giving z<=14. Each bound contradicts z>=22.

Konig gives a size-three cover X and an independent ten-set Y. X can be chosen independent; in fact any such cover is independent here. If e_M(X)=1, triangle-freeness gives at most20 cross edges, so z<=21. If e_M(X)=2, z>=22 forces all ten Y-vertices onto the unique nonadjacent pair of X, making Y plus the third hub independent11. Three edges on X would be a triangle. Hence M has bipartition X3,Y10 with no other edges.

## 5. Every q<=28 triangle channel is impossible

Fix an M-triangle T and let B=A\T. Write u=e_M(B). Equation (1) gives

    u+G_B=q+3-t(T)<=q-21<=7.                     (5)

For an edge ab in B, K4-freeness bounds each endpoint's T-degree by2, and d_B(a)+d_B(b)<=u+1. Thus

    t_a+t_b<=5+u+G_B<=12.

EDGE12 forces equality. In particular q=28, u+G_B=7, t(T)=24, both endpoints have T-degree2, every B-edge meets {a,b}, and all B-decoration is on {a,b}. These conclusions apply to EVERY B-edge. Therefore the nontrivial part of M[B] is a star or a triangle. A triangle has u=3 and forces G_B=0 (intersect its three endpoint pairs), incompatible with u+G_B=7.

If B has a single edge ab, their two T-neighborhoods overlap at a hub w. The two triangles and t(T)=24, t_a+t_b=12 force t_w=12, and the other hub weights to be t_b,t_a. Both are at most9 because each endpoint has internal degree3 and the decorations sum6. The other eight B-points are regular and can meet only w by EDGE12. Thus z<=3+1+4+8=16, impossible.

If the star has k>=2 edges and center a, all B-decoration is at a, namely7-k. Its leaves are regular of weight3 and its center has weight9. Each leaf and a have distinct two-element T-neighborhoods. Their common hub has weight12; the other hub weights are3 and9. There cannot be two different common hubs of weight12 since t(T)=24 and the third hub has positive degree. Thus every leaf has missing neighborhood consisting of the weight12 hub, the weight9 hub and the weight9 center. This neighborhood spans two M-edges. INS11 would require 30-2*2>=3*(12-3)=27, whereas its left side is26. Contradiction. This exhausts u>0.

It remains that B is independent. Its T-incidence count is z-3>=19 and at most20, so all ten B-points have T-degree2, or nine have degree2 and one degree1. Here G=q-z<=6. Every hub must meet a regular degree-two B-point. To prove this, suppose hub i does not. A possible regular degree-one neighbor would see hub weight at most3+G<=9, violating EDGE12. All remaining possible neighbors are decorated. For a decorated neighbor b, the number c_i of hub i's B-neighbors is at most G_B-g_b+1, whence

    t_i+t_b <= (2+c_i+g_i)+(2+g_b)
              <=5+G_B+g_i<=5+G<=11,

again impossible. A hub with no B-neighbor makes an independent11-set, so the claim follows.

Consequently each hub has weight at least10. Their total is q+3-G_B<=31. If it is30, all weights are10; if31 they are11,10,10. (For q<=26 the total is already too small.) A regular degree-two B-point has two adjacent hubs as its missing neighborhood, whose weight sum is at most21. INS11 requires that sum minus2 to be at least20. Contradiction.

Thus no q<=28 triangle shell exists. In the triangle-free channel a 3-matching gives q>=36-9=27. We have proved, without invoking maximum charge,

    EVERY regular pivot has q>=27.              (6)

## 6. Complete new bipartite classification at q27 and q28

Use X={0,1,2}, Y of size10 from Section4. Write x_i=t_i. A Y-point is encoded by (B,g), with B subset X its missing neighbors and g>=0. Its weight is |B|+g. Completeness is exact: every graph in the reduced channel is uniquely such a list, up to permutations within Y and relabeling X.

The verifier enumerates all 19,448 nonnegative eight-tuples (n_B) summing to10. It checks z=sum n_B|B| in [22,q] and Hall's seven inequalities on X. It then distributes exactly G=q-z decoration units among the three hubs and the ten low vertices, sorting decorations within each identical B type to avoid only genuine symmetries. It enforces EDGE12 and INS11 at every regular vertex. These conditions are NECESSARY for every legal parent; no parent realization is assumed. Every possible decoration allocation occurs in this enumeration.

The resulting states, modulo S3 on X, are exactly:

|q|hub weights|Y rows|parameters|
|---|---|---|---|
|27|(9,9,9)|k copies (X,0), 10-k copies (empty,0)|k=8,9|
|28|(9,9,10)|k copies (X,0), 10-k copies (empty,0)|k=8,9; call these B1|
|28|(9,9,9)|k copies (X,0), one (two-hub subset,1), 9-k copies (empty,0)|k=7,8|
|28|(9,9,9)|k-1 copies (X,0), one (X,1), 10-k copies (empty,0)|k=8,9|
|28|(9,9,9)|k copies (X,0), one (empty,1), 9-k copies (empty,0)|k=8,9|

There are two states at q27 and eight at q28. Hubs' decorations are determined, not free: g_i=x_i-d_M(i). `INDEPENDENT_VERIFIER.py` reconstructs these states independently of `explore_bipartite.py`, asserts exact set equality (any extra or omitted case fails), rebuilds all ten graphs, and checks all 8,192 subset identities for each. Its executed output is `VERIFICATION_RESULT.json`. The exploratory enumeration used a different order (hub weights first, then individual row types), finding the same canonical classes.

## 7. Exclude Q<=28, including B1 without the old 289-core classification

### 7.1 A repeated deficient-row contradiction

At Q=27 choose any pivot; Section6 gives the q27 state. Every active regular low y has d=3, rho=0. Formula (3) at beta11 and maximality force q_y=27 and h_11=kappa=b=0. Its row D_y is a triangle of degree-11 core vertices and is anticomplete to the three hubs X.

At Q=28, consider one of the six non-B1 q28 states. There is exactly one low decoration, so for every active regular full row y, rho=1. Again maximality in (3) forces h_11=kappa=b=0. There are at least seven such full rows.

In either situation all these rows coincide. If x lay in D_z minus D_y, it is degree11 in C and, by Section2, adjacent to all three vertices of D_y. It is anticomplete to X from b_z=0. In the core after repivoting at y, its degree would therefore be 11-3=8, contradicting the global minimum degree11. This proves row coincidence directly, with no cycle or unproved compatibility assertion.

But K={p} union Y is a target K11, disjoint from their common triangle D. The induced K union D has at least55+3+3a edges, where a>=7 is the number of full regular rows. This is at least79>D(14)=69. Thus Q27 and all six non-B1 q28 states are impossible.

### 7.2 The two B1 states

Suppose Q=28 and choose a B1 pivot. K={p} union Y is now a K11 of regular vertices. Every v in K has exactly three neighbors T_v outside K. For inactive lows T_v=X=T_p. For active lows, (3) gives

    q_v=27+h_11+kappa+b<=28.

If kappa=1, then h_11=0, and all three row points have degree11 in C; the deficient-clique lemma would force kappa=0. Thus every T_v is a triangle. Also q_v is27 or28. Its missing shell is bipartite between T_v and K minus {v}; the latter ten points are ALL regular. The Section6 classification, applied with this specified cover, allows only the q27 states or B1 states (the other six require a decorated low).

In each of these views, every other K-point is adjacent to all or none of T_v. Hence two triples T_v,T_w are equal or disjoint. The multiplicity c of every distinct triple is exactly2 or3, since the complete bipartite shell has k=9 or8 active lows and c=11-k. Partitioning eleven K-points therefore gives at least four distinct triples.

For any outside row point x in a triple of multiplicity c, its hub weight in its corresponding shell is

    t_x=d_F(x)-c-2.

At least two of the three hub weights are9. Call those points base points; their degrees are d_F(x)=c+11. If p belongs to a different row class, its core degree at x is

    d_(C_p)(x)=d_F(x)-c-e_F(x,T_p)=11-e_F(x,T_p).

The global core minimum degree11 forces e_F(x,T_p)=0 and d_(C_p)(x)=11. Fix one row class for p and choose base points x,y in two other distinct row classes. They are nonadjacent by the same formula, but both have degree11 in C_p. This contradicts the deficient-clique lemma.

Therefore B1 is impossible as well. We have independently proved

    Q>=29.                                      (7)

This replaces the historical Q27 and Q28 survivor geometry, including its separate 289-edge K10/K11 classification.

## 8. The <=288 core gate and EDGE13, with exact provenance

The prior lower-order chain gives minimum degree12 for H in R(3,35), so e(H)>=210. Equality would make its complement 22-regular, K4-free, on35 vertices. AES Theorem1.1 at forbidden clique order4 says minimum degree greater than5n/8 makes such a graph 3-partite. Here 22>175/8 strictly. One part has at least12 vertices, a target K12, contradiction. Hence

    H in R(3,35) => e(H)>=211.                   (8)

Primary source: B. Andrasfai, P. Erdos and V. T. Sos, *On the connection between chromatic number, maximal clique and minimal degree of a graph*, Discrete Mathematics8 (1974),205--218, Theorem1.1, p.207, DOI10.1016/0012-365X(74)90133-2. The original paper was inspected at https://real.mtak.hu/110445/1/1974-18.pdf. No stronger equality classification is assumed.

Let C be an actual47-core with e(C)<=288. Section2 gives delta(C)>=11. If x has degree11, its 35-point antineighborhood H has at least211 edges and minimum degree12. Its11-shell is not complete, since otherwise x extends it to K12. A missing edge uv in that shell has H-row union at least12 by R(2,24) emptiness. Its shell charge q11 is at least11. Thus e(C)>=66+211+11=288. At equality, the two rows are disjoint with union U of size12, and W=H minus U is an R(2,23), so e(W)>=131. The degree sum on U gives e(H[U])>=131-211+144=64. Then U union {u,v} has at least64+12=76>D(14)=69 edges. Contradiction. Therefore

    e(C)<=288 => delta(C)>=12.                  (9)

For a missing edge ab of the original13-shell, its uncovered core has alpha<=3. If its row union has size at most12, extend that union to X of size12. The complement C-X is R(3,35) and has at least211 edges. But (9) gives

    e(C-X)<=288-12*12+binom(12,2)=210,

a contradiction. Hence every such shell has

    t_a+t_b>=13.                               (EDGE13)

## 9. Uniform promotion when q<=29 and the core has <=288 edges

Suppose q<=29 and e(C)<=288. Then G<=7, EDGE13 holds and C has minimum degree12. We prove that some regular shell vertex has missing degree3..10. Suppose not, and put X={a:t_a>=11}. By (1), three such points would give q>=33-3=30; hence |X|<=2. Also M is K4-free by (2).

Every regular vertex outside X has missing degree0,1 or2. It cannot have an M-edge to another point outside X, by EDGE13. Thus all edges outside X have decorated endpoints.

- If X is empty, all edges lie on at most7 decorated points, giving at most16 edges by Turan's K4-free bound, below22.
- If X={x} with t_x=11, a regular outside point could only meet x and so would have weight1, violating EDGE13. All edges lie on x plus decorated points; a regular x cannot have degree11 there, and a decorated x leaves at most6 other decorated points. The edge count is again below22.
- If X={x} with t_x>=12, the other12-set must contain a triangle or a 2-matching: otherwise a graph of matching number at most1 is a star or triangle plus isolates, giving independent11 unless it is a triangle. A triangle with x yields q>=12+24-5=31 by K4-freeness. A 2-matching with x yields q>=12+26-8=30, since a K4-free five-set has at most8 edges.
- If |X|=2, the other11-set must contain an edge uv. The four points have total weight at least22+13=35 and at most5 edges, giving q>=30.

Each case is impossible. For the resulting regular middle-degree y, (3) at beta12 gives q_y>=d(13-d)>=30. No assumption that neighboring charges are at least the old charge is used.

Together with (7), this already proves E407 COVER: if Q<=29 then Q=29, e(C)=407-91-29=287, and this promotion contradicts maximality. It also reduces E408 with Q<=30 to Q=30: Q29 has e(C)=288 and promotes.

## 10. Complete q30 maximum-shell classification for E408

Assume E=408 and Q=30; choose a maximizing pivot. Its core has287 edges, so (9) and EDGE13 apply. Any repivot with q_y>=29 also has core size at most288 and inherits minimum degree12.

If a regular shell vertex has missing degree4..9, (3) gives q_y>=36, impossible. If it has degree3 or10, (3) forces q_y=30, rho=h_12=kappa=b=0. Formula (4), now licensed on the new core, forces m=0.

For d=3, S is M-independent, the other10-set is independent and regular, and q=t(S)=30. Each inserted vertex has new-core degree t_s+2>=12, so all three weights are10. EDGE13 forces every nonisolated low point to meet all three hubs. Thus

    Family I: M=K_(3,k) plus (10-k) isolates,
              k=8,9,10; hub weights10 and decorations10-k;
              all ten low points regular.                (I)

For d=10, S10 and the other3-set are M-independent, with the other3 regular; t(S)=30. EDGE13 against y of weight10 gives every S-weight at least3, so all are3. Any active point on the three-side then has degree10 by EDGE13. Since z>=22 all three are active, giving the k10 case of (I).

Now suppose no regular missing degree3..10 occurs. First M is K4-free. Otherwise a K4 has weight sum36 and all nine outside points are independent and regular by (1). Each K4 weight is at most12 by its three-point complements and (2). At least one outside point y has missing degree2, since z>=22. Its neighbors are adjacent in M, and (3) gives q_y>=53-t(S)>=29. Thus its new core has minimum degree12. Each of the two inserted vertices has degree t_s minus a nonnegative correction, so each weight is at least12. The other pair in the K4 then has weight sum at most12, violating EDGE13. Contradiction.

Put X={a:t_a>=11}; now |X|<=3. As in Section9 all edges outside X have decorated endpoints.

- X empty: at most8 decorated points support all edges, and the K4-free bound is21<22.
- |X|=1, weight11: regular outside points have no incident edge; a regular hub cannot attain degree11, and a decorated hub leaves at most7 other decorated points. Again at most21 edges.
- |X|=1, weight>=12: the other12-set contains a triangle or2-matching. A triangle gives q>=31. A2-matching gives q>=30 with equality forcing hub weight12, its four endpoints' total weight26, and eight induced edges on these five points. All other eight vertices are independent and regular. They can only meet the unique weight>=11 point, so add at most8 edges. Then z<=16<22.
- |X|=3: (1) forces three weight11 points forming a triangle, and ten independent regular outside points. An active outside point must have degree2 (degree1 fails EDGE13); its two hub weights22 give q_y>=30+22-(22-1)=31. Contradiction.
- |X|=2: the other11-set contains an edge uv. Equation (1) forces equality: both hub weights11, t_u+t_v=13, the four-set spans five M-edges, and the other nine points are independent and regular. Each active outside point must meet both hubs, so z=5+2k>=22 forces k=9. Each hub has weight11 and at least9 outside neighbors, so its induced four-set degree is2. Therefore the missing edge of this K4-minus-edge is exactly between the two hubs. They are regular of degree11; u,v have internal missing degree3 and decorations summing7. Neither decoration is zero, since regular degree3 was excluded in this channel.

The last case is precisely

    Family II: M=K_(2,11) plus one edge uv in its11-side;
               the two hubs regular of weight11;
               nine ordinary lows regular of weight2;
               u,v decorated positively, g_u+g_v=7.       (II)

This proves completeness of (I),(II) without importing the old q30 classification.

## 11. Eliminate Family I by a global excess count

K={p} union the ten lows is a regular target K11. For v in K let T_v be its three outside neighbors. Inactive lows are true twins of p. Active lows repivot with equality in (3), so their rows are triangles, their charges are30, and their new cores have minimum degree12.

At every v in K the missing shell is bipartite between K minus {v} and T_v. Its q30 classification therefore must again be Family I, since Family II contains triangles in M. Consequently all distinct T_v are disjoint target triangles, with multiplicities c_i=11-k_i in {1,2,3} summing to11. Write their number r. Each vertex x in a multiplicity-c triangle has degree c+12 (its hub weight is10). In a core at a different row class its degree is12-e_F(x,T_v)>=12, so distinct triangles are target-anticomplete.

Thus r<=5 by alpha(F)<=5, while c_i<=3 implies r>=4. The row triangles contribute exactly3(11-r) excess above degree13. The remaining 50-3r vertices have total excess

    23-3(11-r).

If r=5 there are35 remainder vertices and only5 excess units. Each remainder vertex must complete some row triangle, otherwise it and one avoiding point from each of the five triangles give independent6. But it has no neighbors in K; its degree in each q30 core is d_F(v)-e_F(v,T_i)>=12, so completing a triangle forces d_F(v)>=15, or excess at least2. This needs70 units, contradiction.

If r=4 there are38 remainder vertices and only2 excess units, hence at least36 are regular. Each regular remainder vertex meets a row triangle in at most1 point by the same core inequality. Any two nonadjacent regular remainder vertices together avoid a point in each of the four triangles, producing independent6. They must therefore form a clique of size at least36, contradicting omega(F)<=11.

Family I is impossible. The same arithmetic also excludes it at E407 if needed.

## 12. Eliminate Family II and finish COVER

Let K consist of p and the nine ordinary lows, a regular target K10. All its points are adjacent to the two decorated points u,v, which are target-nonadjacent. Each v_i in K has exactly two further neighbors T_i.

For an ordinary low y, d=2, its missing neighbors are the two hubs of weight11, and rho=8. Formula (3) yields q_y=30+h_12+kappa+b. Maximality forces equality, so T_y is an edge, q_y=30, and its new core has minimum degree12. The same holds at p.

The q30 classification applies at every v_i. Family I is already impossible, so every such shell is Family II. The globally decorated u,v must be the two exceptional lows in each view, since these are that family's only decorated vertices. The other nine K-points are adjacent to both u,v, and hence are ordinary lows. Thus T_i is precisely the regular hub pair in this view. Each x in T_i has degree13, is adjacent to v_i alone in K, and is nonadjacent to u,v.

The ten pairs T_i are disjoint. If i!=j and x in T_i, then in the q30 core at v_j,

    d_core(x)=13-1-e_F(x,T_j)>=12.

Thus distinct pairs are anticomplete. Choosing one point from each gives independent10, contradiction.

Hence Q=30 is impossible for E408. Together with Sections7--9 this proves E408 Q>=31, and E407 Q>=30 was already established in Section9. This completes the independent COVER theorem.

## 13. Final use of the accepted 287-edge theorem

Every regular-pivot core is genuinely R(4,47), by Section1. The earlier low-edge gate is used only at its licensed edge range; one does NOT assert delta(C)>=12 for every core solely from its order. Combining accepted low-edge floor286, its e<=286 minimum-degree gate, and the abstract286 exclusion at `c3d07b2ca5912b1b0c1c6998303c19c3c2911340` gives e(C)>=287.

Thus E407 has q_p<=29 for every regular pivot, contradicting COVER Q>=30. E408 has q_p<=30, contradicting COVER Q>=31. All low and high charge values are covered. The theorem uses only the displayed graph contract, so the original full-color T61 parent is included; no extra color factorization assumption is needed. Historical V11/V12 and support-union dependencies are absent from this closure. Other EG617 root obligations remain separate.
