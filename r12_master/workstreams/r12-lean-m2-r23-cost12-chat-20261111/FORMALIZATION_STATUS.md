# Verified Case I and balanced exterior — full R23 and GATE47 remain open

Subsequent checkpoint14e5b5c / CI43679609897: full build, exact statements and
all169 axiom reports PASS. r23_121_completion_or_missing_exterior now derives
actual one-edge completion to Case I from the original121-edge assumptions
whenever the exterior is complete. The remaining alternative retains exactly
one missing edge in balanced9+9 parts. The singleton completion preserves
triangle-freeness and alpha<=11 and has exactly122 edges. Compatible missing
endpoints have a verified no-common-neighbor graph lemma; incompatible
endpoints have a verified full adjacency/type equivalence. Their exact
exceptional fiber sizes and the final Case IV assembly are current candidates.
The older checkpoint and its independent ZIP below remain valid historical evidence.

Latest verified code: c252a45b185c07387e71b3416cde37f46b95b3f1.
Linux CI 43618192344, job 132517777312 (2026-11-15 Asia/Shanghai).
Focused compile, full lake build, exact statements, all159 transitive axiom
reports, nine fixed dependencies and source/config SHA256 checks PASS.
Only propext, Classical.choice, Quot.sound. All local source hashes match CI.
The original LEVEL1 mathematical source files remain byte-identical.
Full evidence: CI_STATUS.json; logs/linux-43618192344-full.txt.

r23_122_case_I proves frozen M2a / Case I from exactly these hypotheses:
card V=23, triangle-free, CoreIndependenceBound11, e(G)=122.
The result is an actual-vertex type map with adjacency iff C5 type adjacency
and all five fiber sizes, in cyclic order: 10,A,1,1,B, with A+B=11 and
1<=A,B<=10. Thus the 122-edge branch is classified, not merely represented
by example graphs or a compatible type pattern.

r23_exists_balanced_exterior excludes K8,10 from the original e>=121 contract.
r23_exact_neighbor_ledger proves the precise121/122 ledger and singleton iff.
All labels refer to the SAME C5 support as that ledger.

Open: the121-edge singleton completion, compatible missing-edge completion,
and incompatible missing-edge whole-graph classification. Cost-6 for every
independent set, sharp R335/R336, GATE47 and MainTheorem are NOT proved.
No source scan or finite diagnostic search is used as a substitute for Lean.
