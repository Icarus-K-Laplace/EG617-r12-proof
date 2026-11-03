# Global counterexample attack: K145 -> T61 -> terminal split

Date: 2026-11-03  
Audited theorem source: integration commit `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.  
Audit branch: `workstream/r12-astra-independent-audit-20261102`; source files are read-only.

## Verdict

**NO GLOBAL COUNTEREXAMPLE OR LOAD-BEARING INTERFACE GAP FOUND in this attack.**

The audit attempted to break the proof at the transitions between:
1. the original 12-coloring and the least-edge color graph;
2. the color graph and the contextual hereditary class;
3. maximal K12 packing and the residual graph contract;
4. the residual recurrence and its unique T61 survivor;
5. the T61 minimum-degree split and the h12/h13 terminal theorems.

The exact quantifiers and inherited hypotheses match at each transition. This is an analytic interface audit plus an independent recurrence transcription; it is not an exhaustive search over all 61-vertex graphs, a clean-checkout run of the complete root verifier, Lean certification, or external human review.

## 1. Original coloring -> hereditary caps

Assume every 13-set of K145 contains all 12 colors. For every color c and every vertex subset U, the complement of the c-color graph on U is K13-free. Turan therefore gives at least
[
p_{12}(|U|)=\binom{|U|}{2}-t_{12}(|U|)
]
edges of color c on U. Summing the other eleven color lower bounds gives the target-color cap
[
e(G[U])\le D(|U|)=\binom{|U|}{2}-11p_{12}(|U|).
]
This is hereditary on every induced subset; no balancing assumption on the color-class sizes is inserted.

For a least-edge color graph G:
- (e(G)\le \binom{145}{2}/12=870);
- (alpha(G)\le12), since an independent 13-set misses this color;
- (omega(G)\le12), since a monochromatic K13 misses the other colors;
- every induced subset obeys D.

If (delta(G)\ge12), then the average-degree bound forces G to be 12-regular. Brooks applies componentwise: (Delta=12), and no component is K13 because (omega(G)\le12). Thus (chi(G)\le12), so one vertex color class has size at least (lceil145/12ceil=13), contradicting (alpha(G)\le12). Therefore a minimum-degree vertex has (d\le11).

## 2. Contextual R(4,49) exclusion: no generic transfer

The recurrence class is contextual: its graphs are induced subgraphs of this same G, have (omega\le11), and inherit every D-cap. The proof does **not** assume or claim that the generic uncolored R(4,49) problem is solved.

Suppose a 49-set induces F with (alpha(F)\le4), (omega(F)\le11), and all caps.

- A vertex of degree at most11 leaves at least37 nonneighbors. That 37-set has (alpha\le3) (an independent 4-set plus the vertex would give 5) and is a forbidden R(3,37).
- If a vertex has degree12, its 36-point nonneighborhood H is in R(3,36), so (e(H)\ge234). The 12-neighborhood is not a clique K12; choose a missing pair a,b. If its two H-rows had union at most12, at least24 H-vertices would be anticomplete to a,b; that 24-set would have (alpha\le2), contradicting R(2,24). Thus the row union is at least13 and
  [
  e(F[H\cup\{a,b\}])\ge234+13=247>D(38)=241.
  ]
  Hence degree12 is impossible.
- Therefore (delta(F)\ge13) and (e(F)\ge\lceil49\cdot13/2\rceil=319).

For each of the other eleven color graphs C on the same 49-set, (alpha(C)\le12) by the original all-colors condition. Also (omega(C)\le4): a C-clique of size5 is an independent 5-set in F. Its complement L is K13-free and not 12-partite, since a 12-partition would partition C into twelve cliques of size at most4 and cover at most48 vertices. Kang–Pikhurko at (49,12) gives (e(L)\le1097), hence (e(C)\ge79). The eleven other colors consume at least869 edges, so (e(F)\le1176-869=307<319), contradiction.

This proves only the contextual R(4,49) exclusion needed by the original coloring proof. It does not prove a generic R(4,49) theorem.

## 3. Maximal K12 packing -> exact residual contract

Let v be a minimum-degree vertex of G, (A=N(v)), (|A|=d\le11), and (U=V(G)\setminus N[v]). Pack a maximal family of j disjoint target-color K12 blocks in G[U].

The D(13)=67 cap implies that any vertex outside a target K12 has at most one target-color neighbor in it: two would give68 target edges on13 vertices. Therefore:
- cross edges between distinct packed blocks form a matching;
- a residual vertex has at most one neighbor in each block;
- if j were at least12, choose independent representatives greedily from twelve blocks and add v, obtaining an independent13-set;
- if the residual R had an independent set of size12-j, every block would retain at least j points avoiding it; choose j pairwise nonadjacent representatives and add v, again obtaining an independent13-set.

Thus (j\le11), (omega(R)\le11) by maximality, and (alpha(R)\le11-j). All induced D-caps are inherited.

The exact edge ledger was rederived. With
[
\sigma=870-e(G),\quad z=\binom d2-e(G[A]),\quad
g=\sum_{a\in A}(d_G(a)-d),
]
and x,y the block-block and block-residual edge counts, respectively, the degree sum on A gives (e(A,U)=2z+g). Hence
[
e(R)=870-\binom{d+1}{2}-66j-(\sigma+z+g+x+y).
]
All five defect terms are nonnegative. No initial neighborhood clique assumption is used.

## 4. Independent recurrence transcription and all outer stops

The recurrence was reimplemented from the mathematical rules, rather than importing either frozen recurrence module. The implementation uses:
- (p_a(n)), the Turan-complement lower bound from (alpha\le a);
- the hereditary cap D(n);
- the pair-row bound (eta=\max(0,m-N_{a-2}));
- the triangle-row bound (gamma=\max(0,m-N_{a-3}));
- the proved matching guarantee for missing graphs;
- the exhaustive triangle-free / triangle-containing split;
- deletion averaging and the licensed lower-order seeds.

The independently computed maxima are
[
N_0=0,\ N_1=11,\ N_2=23,\ N_3=36,\ N_4=48.
]
The two terminal row bounds at (a,n)=(5,61) are:
- h=12: core term B(4,48)=308, (eta=12), matching number at least2, q-floor20, giving (e(R)\ge406);
- h=13: core term B(4,47)=284, (eta=11), matching number at least3, q-floor22, giving (e(R)\ge397);
- h=14: handshake already gives (e(R)\ge427).

The full transcription computed all 1,752 ((a,n)) entries and all144 ((d,j)) outer stops. Exactly one stop survives:
[
(d,j,a,n)=(11,6,5,61),\qquad397\le e(R)\le408.
]
This matches the frozen frontend replay and the separately recorded independent replay. It is a finite recurrence computation; correctness of the recurrence rules is justified analytically in RECURRENCE_PROOF.md.

## 5. T61 -> only the h12 or h13 terminal

For the unique residual F, (alpha(F)\le5), (omega(F)\le11), all D-caps, and (397\le E=e(F)\le408).

- If (delta(F)\le11), a vertex and 49 of its nonneighbors give a contextual R(4,49), already excluded.
- If (delta(F)\ge14), handshake gives (E\ge\lceil61\cdot14/2\rceil=427), impossible.

Thus (delta(F)\in\{12,13\}), with no missing degree case.

### h12

A degree-12 pivot gives a 48-core in R(4,48). The independent 48-core theorem gives (e(C)\ge310); the 12-shell charge satisfies (q\ge20). The exact identity is
[
E=\binom{13}{2}+q+e(C)=78+q+e(C),
]
so (E\ge408). At E=408 equality forces q=20 and one of the five (K_{2,r}) shell families, r=6,...,10. Repivoting at a leaf inserts the two hubs into another genuine R(4,48) core. Each inserted hub has degree at most (10+1=11), contradicting the independently proved 48-core minimum degree12. Therefore the h12 branch is empty for E≤408.

### h13

A regular pivot exists: otherwise all61 degrees would be at least14, already excluded. For every regular pivot p, the 47-core is in R(4,47), so (e(C_p)\ge287), and
[
E=\binom{14}{2}+q_p+e(C_p)=91+q_p+e(C_p).
]
Thus every pivot satisfies (q_p\le E-378), pointwise:
- E=407 gives every (q_p\le29), hence (Q\le29), while COVER proves (Q\ge30);
- E=408 gives every (q_p\le30), hence (Q\le30), while COVER proves (Q\ge31).

The maximum Q is taken only after the pointwise upper bound is established. No quantifier reversal is present. The COVER Q29/Q30 statements are used under the exact same-parent 61-point contract.

Both h12 and h13 branches are impossible, contradicting the original coloring.

## 6. Dependency and status findings

| Interface | Verdict | Reason |
|---|---|---|
| Coloring -> D-caps | NO GAP | Turan lower bound for each color on every induced subset |
| Brooks -> d≤11 | NO GAP | 12-regular and no K13 component |
| Contextual R(4,49) | NO GAP | Original full-color context is retained; no generic theorem is imported |
| K12 packing -> residual alpha/omega | NO GAP | D13 cap gives one-neighbor property; greedy transversal is valid |
| Edge ledger | NO GAP | (e(A,U)=2z+g) and all remaining terms are nonnegative |
| Recurrence -> unique T61 | NO GAP FOUND | Independent transcription: 1,752 nodes, 144 stops, one survivor |
| T61 -> h12/h13 | NO GAP | Degree and energy cases are exhaustive |
| h12/h13 quantifiers | NO GAP | All regular pivots bounded before taking Q; repivoted cores are in the stated hereditary class |

## 7. What this audit does not certify

- No exhaustive search over all 61-vertex graphs was performed or claimed.
- The complete root verifier was not freshly executed from a clean checkout in this audit session. Its scope must not be overstated: a hash/DAG/replay verifier is not a formal proof checker.
- The fixed theorem remains an informal mathematical proof supported by finite computation and an AI-assisted audit, not Lean/Coq kernel certification.
- External human combinatorics review and journal review remain outstanding.
- The generic uncolored high-energy R(4,49) layers E333–E340 and the general-r conjecture remain outside this fixed-r12 dependency chain.

**Final disposition:** no global counterexample or fatal interface gap was found in the pinned K145 -> T61 -> terminal chain. The result is a strong independent audit conclusion, not a claim of infallibility or formal proof-assistant certification.
