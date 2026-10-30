# Source contract audit

Status: **PARENT APPLICATION NOT CERTIFIED. Four of five U6 core conditions are source-mapped; the minimum-degree condition remains conditional.**

## 1. Target/non-target distinction and parent mapping

Let F be the actual 61-point T61 target residual, p a target-degree-13 pivot, A=N_F(p), and H=F[V(F) minus N_F[p]]. The parent files front_end/FRONTEND_BRIDGE_THEOREM.md F7-F8 and front_end/T61_H13_FULL_COLOR_DEGREE_AND_ANTINEIGHBORHOOD.md retain alpha(F)<=5, omega(F)<=11, delta(F)=13 and e(F)=408.

The parent edge identity is e(F)=91+q+e(H). For Q32, q=32 and e(F)=408, hence |H|=47 and e(H)=285. Since p is anticomplete to H, alpha(H)<=4. Since H is induced in F, omega(H)<=11.

The Q32 terminal's frozen contract also states delta(H)>=12, but that statement is imported through E406_CORE_MINDEG_288.md and the lower-order R(3,35) seed; it is not a self-contained consequence of e(H)=285. The current proof-body gap is recorded in Q32_PARENT_CONTRACT_MAPPING.md.

A non-target clique of order6 would be target-independent of order6. Therefore omega(C)<=5 on this same 61-point residual. This is not an assertion that every arbitrary 61-point induced subcoloring of a balanced graph has omega(C)<=5.

## 2. Exact-129 classification — PROVED CONDITIONAL on Kang–Pikhurko

Primary source: M. Kang and O. Pikhurko, Maximum K_(r+1)-free graphs which are not r-partite, Mathematychnі Studii 24 (2005), 12-20. Theorem 1 gives the extremal size; Theorem 4 gives the equality construction.

For a non-target C, its complement G is K13-free. It cannot be 12-partite: its parts would be C-cliques of size at most5 and could cover at most60 vertices. At equality, Theorem 4 supplies an added point x and twelve old independent parts of G, whose sizes sum to60. Each is a C-clique of size at most5; therefore all sizes are5. This directly excludes both size-six profiles and the 12-partite case under the genuine T61 coupling.

In C the ten ordinary parts are isolated K5 components. The two special K5s Ns,Nt and x form an 11-point gadget. Choose y in Nt and a nonempty proper A0 subset Ns, with a=|A0| in {1,2,3,4}. The variable degrees are d(y)=4+a and d(x)=9-a; all other gadget vertices have degree5 and ordinary vertices degree4. There is no universal degree-nine exceptional point.

## 3. Every exceptional position and outside profile

Put O={p} union A, |O|=14. Every K5 factor meets O because its H intersection is target-independent and alpha(H)<=4.

- x in O: factor outside counts are (2,1^11), in 12 labelled positions; H part sizes are 4^11,3.
- x in H: either (2,2,1^10), in 66 labelled positions, or (3,1^11), in 12 labelled positions. The H part sizes are respectively 4^10,3,3,{x}, or 4^11,2,{x}.

The total 90 aggregate assignments preserve the identities of both special factors; no isolated or special double/triple placement is removed. Aggregate counts do not specify which of y,A0,x is inside a part and do not certify a colored completion. All four source parameters remain legal.

U6 has no source-position premise, so none of these placements is lost if and when the parent core contract is certified.

## 4. Counts and exact parent variables

All colors partition 1830 edges. Since e(F)=408, the non-target total is1422=11*129+3. Consequently m=8,9,10 with nonexact counts respectively (130,130,130), (130,131), (132). This is a source-count identity, not a proof that a Q32 core exists.

In the full extension, pH has no target edge and pA is entirely target. There are 123 target edges outside the core; after the 13 pivot-star edges, 110 target edges remain on A or A-H. A core theorem is not a 61-point colored witness or a 145-point balanced-coloring counterexample.

## 5. Minimum-degree dependency and promotion status

The parent implication delta(H)>=12 is not certified by the present audit. E406_CORE_MINDEG_288.md derives it using CORE211. INTEGRATED1_CORE211_AUDIT.md recovers the 210-edge Andrásfai–Erdős–Sós contradiction and equality degree multisets, but explicitly says the prior 23-neighbourhood / cap-two exclusion used to establish delta(J)>=12 for J in R(3,35) still needs a standalone proof/certificate or exact bibliographic dependency.

ASSUMPTION_LEDGER.md labels this lower-order seed PROVED, while the integration audit labels its source recovery PARTIAL_STANDALONE_RECOVERY. V9 lists the seed as retained input, not as a theorem newly proved by V9. This evidence conflict is not resolved here.

Accordingly U6 remains a proved conditional graph theorem; its application to all genuine E408/Q32 parents is NOT_CERTIFIED until the A4 dependency is recovered and independently checked. No root promotion is issued.
