# COVER: FORMALIZATION_GAP

frozen/COVER.md proves only the h13 E407/E408 COVER under the full61-vertex
contract: minimum degree13, alpha<=5, omega<=11 and every D cap.
It explicitly does not prove h12 or the original EG617 root.

Section 2 now has the embedded R336 exclusion, the minimum-degree-eleven
theorem for actual pivot cores, the degree-eleven clique, and EDGE12
(Linux run 45659098716).

Section 3 has the exact vertex exchange, equal exchanged sizes, and the signed
charge balance for actual regular pivots (Linux run 45661580041, commit
`6b5e8a249b6320110e11eaa4910d5bfd2b36275e`). In the notation of the frozen
source, `cover_repivot_INS11` retains the removed-row term b and proves
11d + b + 2m ≤ t(S) + 2 choose(d,2). Its minimum-degree bound is derived on
the new core. The balance theorem uses degree sums; cancellation of equal
exchange sizes explains the equivalent signed excess formula for either beta.
The beta=12 applications still need degree witnesses. The charge lower bounds
and Q27/Q28/Q29/Q30 terminal classifications remain open.
The source's Section8 uses AES with a strict threshold; that theorem cannot
be introduced as an axiom. Both old and new core minimum-degree conditions
must be proved when licensing beta12 repivots, including the K4 degree2 branch.
Family I/II completeness and terminal exclusions remain open.
