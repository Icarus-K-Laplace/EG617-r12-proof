# Z=4 two-aligned-column pattern-10 exclusion

Date: 2026-10-30  
Status: PROVED for the exact matching pattern stated below; this is not a universal 4+6 or m=10 closure.

## 1. Contract and scope

Work in the 4+6 K4-e subcase with Z=4:
- the four small blocks are A,B,C,D;
- AB is the unique heavy small-side pair;
- the six outer blocks are E_1,...,E_6;
- the outer heavy graph is a perfect matching M on the six columns;
- all 24 small-to-outer pairs have exactly five edges;
- all small-side base matchings and all outer-side base matchings have been aligned to identity;
- every outer block vertex has degree exactly 12;
- the small-side residual clique-fiber sizes are n=(3,2,2,0), in arbitrary label order.

Let p_{ij} be the base perfect matching from small row i to outer column j and let e_{ij}=(a_{ij},b_{ij}) be its unique extra edge. Let e_AB=(a,b) be the unique extra edge on the heavy pair AB, and let tau_AB=(a b) be the transposition swapping its two endpoint labels.

The theorem below excludes exactly this proposed terminal pattern:
- there are two aligned columns J_0, |J_0|=2, where p_Aj=p_Bj=p_Cj=p_Dj=P;
- there are four nonaligned columns J_1, |J_1|=4, where p_Aj=P tau and p_Bj=p_Cj=p_Dj=P;
- tau is a transposition.

It does not claim that every possible two-aligned-column grid has this pattern.

## 1a. Z=4 degree saturation (derived, not assumed)

In this K4-e subcase, the ten pivot blocks contribute exactly

    180 base matching edges + 1 small-side heavy edge
    + 3 outer heavy edges + 24 cross-heavy edges = 208 edges.

Also e(R)=3+Z=7. Since e(H)=285, the residual-to-block edge count is exactly 70, its minimum possible value 10*|R|. Thus Y=0: every residual vertex has exactly one neighbor in each pivot block. For an outer block E_j, the degree sum is therefore

    36 (nine base matchings) + 7 (residual incidences)
    + 5 (four cross-heavy edges plus its one outer-heavy edge) = 48.

Every vertex has degree at least 12, so all four vertices of every outer block have degree exactly 12. This justifies the exact outer degree equation used in Section 6.

## 2. The outer light cut is connected

The outer light graph is K6-M, where M is a perfect matching. The bipartite cut between J_0 and J_1 is K_{2,4} with the crossing edges of M deleted.

Each vertex of J_0 has at most one deleted cut edge, so it has at least three neighbors in J_1. Each vertex of J_1 has at most one deleted cut edge, so it has at least one neighbor in J_0. Moreover the two J_0 vertices have at least two common neighbors in J_1. Hence the cut graph is connected.

Also, at most two edges of the three-edge matching M can meet J_0. Therefore at least one edge of M has both endpoints in J_1.

## 3. Row-A 4,5,5 switches synchronize both endpoints

For each light cut edge j-l, the triangle (A,E_j,E_l) has pair sizes 5,5,4. Since p_Aj and p_Al are P and P tau, the 4,5,5 switch theorem applies.

In the column-direction form, if p_j=P and p_l=P tau, then for some source label s_{jl},

    e_Aj = (tau(s_{jl}), P(s_{jl})),
    e_Al = (s_{jl}, P(s_{jl})).

In particular, the target endpoint b_Aj=b_Al is the same on the two ends of every light cut edge. Since the cut graph is connected, there is one common target label t such that

    b_Aj=t for every j=1,...,6.

Put s=P^{-1}(t). The same switch equations now give the exact source endpoints:

    a_Aj = tau(s) for j in J_0,
    a_Aj = s      for j in J_1.

Thus the six A-row extra-edge source endpoints consist of exactly two copies of tau(s) and four copies of s. No other source label occurs in row A.

## 4. The A-vertex degree contract forces tau away from tau_AB

For a small-side label x, let n_x be its residual fiber size and let c_A(x) be the number of the six cross-extra edges in row A whose source endpoint is x. Every A_x vertex has:
- nine base-matching neighbors in the other pivot blocks;
- n_x residual neighbors;
- c_A(x) cross-extra neighbors;
- one additional AB neighbor exactly when x=a.

Since delta(H)>=12,

    c_A(x) + 1_{x=a} >= 3 - n_x.

For n=(3,2,2,0), write r for the size-3 label, u,v for the two size-2 labels, and z for the empty-fiber label. The positive requirements are:
- if a is r or z: all three labels u,v,z still require positive c_A;
- if a=u: the two labels v,z require positive c_A;
- if a=v: the two labels u,z require positive c_A.

But c_A is supported on only the two labels {s,tau(s)}. Therefore a must be one of u,v, and

    {s,tau(s)} = {z, the size-2 label different from a}.

In particular a is not in the support of tau. Since tau_AB=(a b) contains a in its support, we obtain

    tau != tau_AB.

This is the key use of the exact small-side vertex-degree contract. It prevents the exceptional transposition case of the corrected 5,5,5 theorem.

## 5. The corrected 5,5,5 theorem fixes the B-row target

Fix any nonaligned column j in J_1. In this column,

    p_Aj=P tau,   p_Bj=P.

The triangle (A,B,E_j) has five edges on each of its three block pairs. Normalize the A-E_j matching to identity. Its relative matching is tau, and the normalized A-E_j extra edge is

    e_Aj' = (s,tau(s)).

Because tau != tau_AB, the corrected 5,5,5 classification has exactly the non-special transposition branch: it forces

    e_Bj' = (s,s).

Undoing the target normalization gives

    e_Aj = (s,P(s)),
    e_Bj = (s,P tau(s)).

The two light small-side pairs AC and AD, by the 4,5,5 switch theorem, give

    e_Cj = (s,P tau(s)),
    e_Dj = (s,P tau(s)).

Consequently the four extra-edge target endpoints in every nonaligned column have multiplicity pattern

    P tau(s)  (three times),   P(s)  (once).

## 6. Outer degree vector and matching contradiction

Let m_t be the size of the outer residual fiber G_t. Let alpha_j be the endpoint label in E_j of its unique internal heavy-pair extra edge. Since every outer vertex has degree exactly 12,

    c_j(t) = 3 - m_t - 1_{t=alpha_j},

where c_j(t) counts the four small-to-outer extra edges ending at label t in column j.

For the outer profile (3,2,2,0), a target-endpoint multiplicity pattern 3+1 is possible only as follows:
- the triple target label is the unique empty outer fiber;
- the singleton target label is one of the two size-2 outer fibers;
- alpha_j is the other size-2 outer label.

The labels P tau(s) and P(s) are fixed across all four nonaligned columns, so alpha_j is the same fixed outer label for every j in J_1.

But Section 2 proves that at least one outer heavy pair has both endpoints in J_1. Its two extra-edge endpoints would then have equal labels alpha_j=alpha_l. This is impossible because the heavy-pair extra edge is off the identity base matching.

Contradiction.

## 7. Conclusion and firewall

The exact two-aligned-column pattern-10 terminal is PROVED IMPOSSIBLE.

This proof uses:
- the unchanged 4,5,5 switch theorem;
- the corrected 5,5,5 theorem, specifically its non-special transposition branch;
- the exact small- and outer-block vertex-degree equations;
- the perfect-matching structure of the Z=4 outer heavy graph.

It does not exclude other two-aligned patterns, mixtures of singleton/2+2 column partitions, other residual profiles, or any other 4+6 branch. Full-support m=10 Q32 remains OPEN / NOT_CERTIFIED.
