# R12 E407 / E408 global compatibility audit

## Shared shell/core identity

For a T61 residual F with a degree-13 pivot, shell A of size13, core H of size47, q=e(M)+G_A:

e(F)=91+q+e(H).

For E407, q=32 and e(H)=284 in the Q32 cell.
For E408, q=33 and e(H)=284 in the Q33 cell.
The core excess at e(H)=284 and delta(H)>=12 is 2*284-47*12=4.

## E407

Repository-proved relative to extremal inputs:
- At a sharp |W|=23 Cell-B near-anchor, the subdivision vertex w has target degree20 and no target neighbours outside W.
- The 11 non-target colors have edge-count multiset 129^7,130^4.
- Four 130-edge colors create disjoint isolated K4 components through w.
- Independent 4-sets in the outside set force four disjoint target 3-neighbourhoods to partition B union {x} or A union {y}.
- Each saturated 3-neighbourhood must meet both A and B, contradiction.

This eliminates that sharp Cell-B completion only.

Still OPEN:
- V12 reports five rho=0 Q32 templates sharing a regular K11.
- No verified theorem currently shows those five templates cannot coexist with one and the same legal 284-edge core.
- V12 package replay remains pending; retain SOURCE_REPORTED label.

## E408

Repository-proved relative to the outer embedding ledger:
- Seven target K12 blocks are pairwise target-anticomplete and anticomplete to R, |R|=61, e(R)=408.
- Every color has exactly870 edges globally.
- For each non-target color C, P_C+R_C+s_C=62 and sum_C s_C=3.
- At least eight colors have e_C(R)=129.
- For every exact129 color, each block has e_C(B_i,R)>=62, so R_C>=7 and P_C<=55.
- The Q33/d3 branch has beta+X+G_B=3, conditional on the retained V11 core interface.

These are simultaneous necessary conditions, not an exclusion.

Still OPEN:
- joint incidence/color-factor compatibility across all seven blocks and the same 284-edge core;
- classification of all equality states of the aggregate budget;
- independent replay of the retained-seed V11/V12 package claims.

## Non-transfer warning

E407 Cell-B exclusion does not imply the V12 Q32 templates are Cell-B. E408's Q32/Q33 equality system does not inherit E407's local contradiction. No aggregate sum identity forces each local defect to vanish.

## Cross-cutting shell/core witness-capacity constraint (new, proved)

The independent workstream now proves the lemma in R12_SHELL_CORE_WITNESS_LEMMA.md.

For any T61 shell row a, if t_a=|N_F(a) intersect H|<=7, then H\N_H(a) has an independent 4-set. The proof uses the inherited edge cap D(n) and Brouwer's second-Turan lower bound for n=40,...,47; the lower bounds exceed D(n) in every case. Separately, the contextual no-R(4,49) condition implies that at least eight shell vertices are good, since two bad shell vertices cannot be target-adjacent.

For E408 Q33/d3, beta+X+G_B=3 gives G_B<=3, while k_b=d_M(b)<=3. Hence every b in B has t_b=k_b+g_b<=6 and is good. Choose an independent 4-set Q_b in H anticomplete to b. For every a in S with ab in M, Q_b must meet N_H(a), or else Q_b union {a,b} would be an independent 6-set. The exact Q33 budget forces at least five such B-vertices to have k_b>=2, so at least five independent-4 witnesses each hit at least two S-rows.

This creates a concrete witness-capacity subproblem for the 284-edge core. It does not prove that the witness sets coincide or that their incidence patterns are impossible; Q33 remains OPEN.
