# Proof dependency map — independent audit

## Status vocabulary

- VERIFIED: the statement and its stated hypotheses have been re-derived in this audit.
- VERIFIED_WITH_LIMITATIONS: mathematically sound, but a separate requested computational check was not run or the publication text still needs an explicit presentation detail.
- OPEN_GAP: a material implication has not been justified.
- DISPROVED: a counterexample to the stated lemma or proof step was found.

## Main theorem dependency DAG

    Input contract:
      |V(H)|=3r-1, alpha(H)<=3, omega(H)<=r-1, delta(H)>=r
      + three pairwise nonadjacent degree-r anchors
            |
            v
    [1] Excess identity and parity -------------------------- VERIFIED
        K=sum_v(d(v)-r)=2e-r(3r-1), K even
            |
            v
    Assume K<=6; all vertex excesses are nonnegative
            |
            v
    [2] Anchor partition and connector incidence ----------- VERIFIED
        every non-anchor meets an anchor
        Xi union {ai} clique
        c+t=4, sum d_i=c-2, q_i=d_j+d_k
            |
            v
    Four mutually exclusive geometries:
        c=2, (0,0,0)
        c=3, (0,0,1)
        c=4, (0,0,2)
        c=4, (0,1,1)
            |
            +------------------+-------------------+------------------+
            |                  |                   |                  |
            v                  v                   v                  v
    [3] Rectangle lemma   [4] Common-          [5] Same-missing-  [6] R-threshold
        forced complete       nonneighbour          anchor             inequalities
        bipartite support     set is clique         disjointness        VERIFIED
        VERIFIED              VERIFIED               VERIFIED
            |                  |                   |                  |
            +------------------+-------------------+------------------+
                               |
                               v
    [7] Rectangle charge R_pq and additivity ---------------- VERIFIED
        R_pq lower-bounds vertex excess on support
        disjoint opposite blocks -> pointwise additivity
        adjacent same-group overlap -> use max(R1,R2), not sum
                               |
                +--------------+-----------------+------------------+
                |              |                 |                  |
                v              v                 v                  v
           c=2 branch      c=3 branch       c=4 (0,0,2)       c=4 (0,1,1)
                |              |                 |                  |
                v              v                 v                  v
    [8] Empty-Part       [9] Focus/nonfocus  [10] f=0,1,2      [11] s=0,1,2
        Self-Consistency      split + r=12,13      focus count         focus-owner
        Lemma VERIFIED        equality audit       VERIFIED            classification
                |              |                 |                  VERIFIED
                v              v                 v                  |
    [12] Degree-two       [13] Boundary        [14] Two-focus       [15] Two-slot
          transversal          equality              overlap              overlap
          cover + size         patterns              equality              equality
          count VERIFIED       VERIFIED              VERIFIED              VERIFIED
                |              |                 |                  |
                +--------------+-----------------+------------------+
                               |
                               v
    [16] All four geometries contradict K<=6 ---------------- VERIFIED
                               |
                               v
    Conclusion K>=8 for every r>=12 ------------------------ INDEPENDENTLY VERIFIED

## Lemma ledger

| ID | Claim | Status | Notes |
|---|---|---|---|
| L1 | K=sum_v e(v)=2e(H)-r(3r-1), and K is even | VERIFIED | No external theorem |
| L2 | Every non-anchor meets an anchor | VERIFIED | Otherwise independent 4-set |
| L3 | Xi union {ai} is a clique | VERIFIED | Otherwise two Xi vertices and the other two anchors are independent |
| L4 | c+t=4 | VERIFIED | Anchor-incidence count |
| L5 | sum d_i=c-2 and q_i=d_j+d_k | VERIFIED | Exact anchor degree equations |
| L6 | Pair-connector nonneighbour rectangle is complete | VERIFIED | Independent 4-set contradiction |
| L7 | R_pq is a lower bound on exclusive vertex excess | VERIFIED | Sum the endpoint excess inequalities |
| L8 | Rectangle charge additivity | VERIFIED | Explicit vertexwise inequality in LEMMA_VERIFICATION.md |
| L9 | Common-nonneighbour set of a nonedge is a clique | VERIFIED | Otherwise independent 4-set |
| L10 | Same-missing-anchor nonneighbour supports are disjoint for nonadjacent connectors | VERIFIED | Otherwise connector pair + missed anchor + common nonneighbour independent |
| L11 | Eight R-threshold inequalities and zero-charge conditions | VERIFIED | Algebraic case split; finite cross-check in ARITHMETIC_AUDIT.py |
| L12 | Empty-Part Self-Consistency Lemma | VERIFIED | Full derivation in LEMMA_VERIFICATION.md |
| L13 | Degree-two transversal-cover lemma | VERIFIED | Proof expanded in LEMMA_VERIFICATION.md |
| L14 | c=2 size contradiction | VERIFIED | Missing r<=K+5 derivation supplied |
| L15 | c=3, r>=14 mixed branch | VERIFIED | k+R22>=r-7+gamma>=7 |
| L16 | c=3, r=13 equality | VERIFIED | Unique (k,gamma,a,b,n2)=(6,0,2,2,0) |
| L17 | c=3, r=12 equality | VERIFIED | 19 local signatures enumerated; all have a saturated rectangle vertex or the one-neighbour exceptional argument |
| L18 | c=4,(0,0,2), focus count f<=2 | VERIFIED | Common-nonneighbour clique / forbidden clique |
| L19 | c=4,(0,0,2), f=0,1 | VERIFIED | Additivity plus local costs |
| L20 | c=4,(0,0,2), f=2,r>=13 | VERIFIED | K>=r-6+max(k1,k2)>=7 |
| L21 | c=4,(0,0,2), f=2,r=12 | VERIFIED | Only identical (1,8) or (8,1) supports survive arithmetic; each contradicts independence/clique capacity |
| L22 | c=4,(0,1,1), focus-slot collision | VERIFIED | Same focus-owner pair creates forbidden clique or oversized clique M |
| L23 | c=4,(0,1,1), s=0,1 | VERIFIED | Additive local bounds |
| L24 | c=4,(0,1,1), s=2 owner patterns | VERIFIED | Four patterns exhaustive; three are over budget |
| L25 | c=4,(0,1,1), overlap equality | VERIFIED | Same (1,8)/(8,1) support analysis as L21 |
| L26 | Local connector/focus skeleton relaxation for r=12,13,14,15 | VERIFIED_WITH_LIMITATIONS | All labelled c=3/c=4 connector graphs and allowed focus owners enumerated; relaxed survivors match the analytic boundary cases. Not a full graph search |
| L27 | External graph/SAT counterexample search | VERIFIED_WITH_LIMITATIONS | Not run; no SAT/ILP backend installed. Not used as proof evidence |


| L28 | Finite support for \(K\le16\) | VERIFIED | Positive excess support has size at most \(K\); anchors are exact |
| L29 | \(c=2\), \(K=8\), \(r\ge13\) | PROVED_ANALYTIC | Empty-part self-consistency, transversal-cover size count, and \(r=13\) connector contradiction |
| L30 | \(c=3\), mixed focus, \(r=14\), \(K=8\) | PROVED_ANALYTIC | Exact 23-profile list eliminated by common-nonneighbour clique and saturation |
| L31 | \(c=4,(0,0,2)\), \(f=2\), \(r=13\), \(K=8\) | PROVED_ANALYTIC | One-sided local profile plus opposite-long-block external-incidence deficit |
| L32 | \(c=4,(0,1,1)\), \(s=2\), \(r=14\), \(K=8\) | PROVED_ANALYTIC | The size-12 block requires 24 external incidences; equality supplies at most 22 |
| L33 | \(K=8\Rightarrow r\le13\) | PROVED_ANALYTIC | Exhausts the four anchor geometries and their focus-owner cases for \(r\ge14\) |
| L34 | Full \(K=8\) equality classification for \(r=12,13\) | OPEN_GAP | Remaining necessary strata listed in EQUALITY_K8_CLASSIFICATION.md; no graph realization claimed |
| L35 | K8_LOCAL_PROFILE_AUDIT.py | VERIFIED_WITH_LIMITATIONS | Exact local integer/rectangle profiles only; not a full graph search |


## External results

No external graph theorem is used in the Exact Three-Anchor Excess proof. The only ingredients are the stated graph hypotheses, degree counting, independent-set/clique contradictions, and integer inequalities.
