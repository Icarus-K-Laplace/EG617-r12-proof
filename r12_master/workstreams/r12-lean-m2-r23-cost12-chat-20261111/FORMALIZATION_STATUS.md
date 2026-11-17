# R23 classification and universal Cost-6 VERIFIED

Exact verified code, CI run, dependency pins, source hashes and declaration counts:
CI_STATUS.json. Full logs and exact statements are retained locally and in GitHub.
Only propext, Classical.choice and Quot.sound occur in transitive axiom audits.
Original LEVEL1 mathematical files and the K145 statement remain byte-identical.

r23_complete_classification gives the exhaustive frozen M2 classification from
card23, triangle-free, alpha<=11 and e>=121. Its whole-graph alternatives are
C5(10,A,1,1,B), A+B=11; an actual one-edge deletion thereof; and C5(9,9,2,1,2).
Actual vertex fibers and adjacency equivalence are proved, not assumed.

r23_cost_six closes frozen M3 for EVERY independent set. It combines
case_I_cost_six, case_I_single_edge_deletion_cost_six and exceptional_cost_six.
exceptional_cost_four proves the stronger exceptional bound4. The deletion lemma
also covers the singleton edge and all alpha>11 deletions; the parent still
retains all original R23 hypotheses. No external enumeration is a Lean premise.

core_R223_complement_cost_six and
core_R335_degree_eleven_nonneighbor_cost_six certify M4's input reduction, retaining
the full CoreAdmissible alpha/omega/hereditary-D contract. They do not prove that
a degree-eleven vertex is impossible.

OPEN: actual fourteen-point cap contradiction in R335, sharp R335/R336 bounds,
GATE47 d10/d11 exclusions and the original MainTheorem. See OPEN_BLOCKERS.md.
Windows local lake build is not claimed; see logs/windows-environment-20261116.txt.
