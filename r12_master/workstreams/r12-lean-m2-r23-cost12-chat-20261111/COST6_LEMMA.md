# Cost-6 — FORMALIZATION GAP

Target, unchanged: for every classified 23-vertex graph W with alpha<=11 and every
independent I, there exists a 12-set T with e(W[T])+|T intersect I|<=6.
Paper mapping: frozen low M3.

There is no Lean theorem proving this assertion in this workstream. In particular,
no terminal Cost-6 hypothesis has been packaged as its proof.

The independent diagnostic program attacks all independent sets, not merely a
chosen witness or maximal set. Across the 61 blow-up/deletion representatives,
49 satisfy alpha<=11, and 271235 independent sets in those 49 were tested.
The stated 12-set choices have minimum cost at most 6 in every tested case.
Twelve representatives are excluded by the original alpha condition, not discarded
to manufacture success. The maximum minimum cost observed is 6.

This evidence is not imported into Lean and does not establish graph classification,
class-symmetry reduction, or a kernel-checked Cost-6 theorem. Those remain necessary.
