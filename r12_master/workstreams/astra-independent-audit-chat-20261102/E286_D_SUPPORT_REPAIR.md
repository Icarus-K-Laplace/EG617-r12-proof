# E286 D-support zero-completer repair

Audit snapshot: Astra integration commit `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.

This note expands the missing case in the D-support elimination. It is an analytic derivation from the scalar blockers in E286 Section 3; it does not change the frozen theorem source.

## Setup

The D support is
[
P=z_{01},quad A=z_{02},quad B=z_{03},quad C=z_{12},quad D=z_{13},
]
with (K_0,K_1) of size 10 and (K_2,K_3) of size 11. The total excess is (T=8).

Each mixed point (A,B,C,D) cannot complete its K11, so its missing set in that K11 is nonempty. Formula (5) gives a charge of at least 5 to a mixed point when there is an additional point completing its K10. The only question is what happens if neither of the two mixed points incident with a K10 completes it.

## Lemma: each K10 has a mixed completer

Consider (K_0), and suppose neither (A) nor (B) completes (K_0). Let (A_0,A_2,A_3subseteq K_0) be the missing sets of (P,A,B), respectively. Let (B_0subseteq K_1), (B_2subseteq K_2), (B_3subseteq K_3) be their opposite missing sets, with sizes (a_i,b_i).

### Case 1: P misses both K10s

Then (a_0,b_0>0), and all three scalar blockers apply. The only shared charged clique is (K_0). For (xin K_0) missing the subset (Ssubseteq{P,A,B}), its internal 9 neighbors, its adjacencies to the other (3-|S|) points, and the forced opposite missing sets give
[
d(x)ge 9+(3-|S|)+sum_{iin S}b_i
=12+sum_{iin S}(b_i-1).
]
Since every (b_ige1), this excess dominates the sum of the (K_0)-terms in the three scalar blockers, namely (sum_{iin S}max(0,b_i-3)). The other charged sets are disjoint: (B_0,B_2,B_3) lie in (K_1,K_2,K_3), and (P,A,B) are distinct points. Therefore
[
Tge f_{10,10}(a_0,b_0)+f_{10,11}(a_2,b_2)+f_{10,11}(a_3,b_3)
ge2+4+4=10,
]
contradiction.

### Case 2: P completes K1 but misses K0

The two mixed blockers for (A,B) still add to at least 8. Their only overlap is in (K_0): if (xin A_2cap A_3), then
[
d(x)ge9+b_2+b_3,
quad
epsilon(x)gemax(0,b_2+b_3-3)
gemax(0,b_2-3)+max(0,b_3-3).
]
For vertices in only one missing set the corresponding single-point bound applies. Thus
[
Tge f_{10,11}(a_2,b_2)+f_{10,11}(a_3,b_3)ge8.
]
If (Tle8), equality is forced. Each blocker has its unique minimum at ((a_i,b_i)=(2,3)), with all four units concentrated on its point (A) or (B); all clique vertices have zero excess, as does P.

Because P completes (K_1), it has at least (10+(10-a_0)) neighbors in (K_1cup K_0). Its zero excess implies (12ge20-a_0), hence (a_0ge8).

Every vertex of (A_2cap A_0) has at least (9+3+1=13) neighbors (internal (K_0), forced (B_2), and B), or at least (9+3+3) if it also lies in (A_3). This contradicts zero excess. Thus (A_2cap A_0=arnothing); similarly (A_3cap A_0=arnothing). Since (|K_0setminus A_0|le2) and (|A_2|=|A_3|=2), it follows that
[
A_2=A_3=K_0setminus A_0.
]
A vertex in this common 2-set is adjacent to P and forced to all of (B_2cup B_3), so its degree is at least (9+1+3+3=16), again a contradiction.

### Case 3: P completes K0

Then P is precisely the additional K10-completing vertex needed for formula (5) for both A and B. Each mixed blocker costs at least 5. Their charges add even if their missing sets overlap in K0: for (xin A_2cap A_3),
[
d(x)ge9+1+b_2+b_3,
quad
epsilon(x)gemax(0,b_2+b_3-2)
gemax(0,b_2-2)+max(0,b_3-2).
]
For a vertex in only one missing set the analogous one-arm bound applies. The opposite K11 charges and point charges are disjoint. Hence (Tge5+5=10), contradiction.

All cases contradict (Tle8). Therefore at least one of A,B completes K0. By symmetry at least one of C,D completes K1.

## Completion of D elimination

Let (c_iin{1,2}) count the mixed points completing (K_i), for (i=0,1). The lemma proves (c_ige1).

- If (c_i=2), the two points complete the same K10 and are nonadjacent (otherwise they and the K10 form K12). Their common neighborhood has size at least 10, so the common-neighbor bound gives combined excess at least 7.
- If (c_i=1), the other mixed point has the completing point as the additional vertex in formula (5), and costs at least 5.

If both (c_0=c_1=1), the two 5-unit charges add; if they share a K11 leaf, use the shared-leaf inequality. Thus (Tge10). If one side has two completers, the other side contributes at least 5 or 7, so (Tge12).

Every case contradicts (T=8). This closes D.


## Audit disposition update (2026-11-03): optional alternative, not required repair

A later re-derivation found that the frozen E286 Section9 already obtains formula (5) for each noncompleting mixed point from its pointwise D-support inequality. The pointwise inequality sums all incidence contributions at each clique vertex, including zero-missing-set cases, so it does not require the separate assertion that every K10 has a mixed completer. This file proves a stronger statement but is redundant for closing D. Do not treat it as a missing premise or require its integration into the frozen source. See `THEOREM_SOURCE_CROSSWALK_20261103.md`.
