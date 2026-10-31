# Theorem ledger with exact domains

Status vocabulary: PROVED means an analytic proof with traced hypotheses is supplied; COMPUTATION_CERTIFIED means only finite execution; PROVED_CONDITIONAL would mean an unclosed premise; OPEN means no proof here. An ordinary graph-contract hypothesis is part of a theorem statement, not an unresolved premise. No proof-assistant certification is claimed.

|Node|Statement / quantifier|Evidence|Status|
|---|---|---|---|
|CAP|Every induced set in every color graph of the assumed original coloring obeys D|Frontend Section1, Turan|PROVED|
|LOWER|R224 empty; R223>=131; delta R335>=12; delta R336>=13; R337 empty|frozen/low minimum-degree and capacity proofs, L|PROVED|
|CORE211|Every R335 has e>=211|LOWER + strict AES threshold22>175/8|PROVED|
|LOW285|No47 graph with e<=285,delta>=12,alpha<=4,omega<=11|frozen direct uniform proof, L|PROVED|
|EX286|Same contract at e=286 impossible|frozen equality proof, X|PROVED|
|GATE47|Every R447 with e<=286 has delta>=12|frozen self-contained gate, L|PROVED|
|FLOOR47|Every R447 has e>=287|GATE47 + LOW285 + EX286|PROVED|
|Q32|Exact e285 abstract theorem,T6|separate frozen Q32 audit; implied independently by LOW285|PROVED; not needed separately|
|Q33|Exact e284 abstract theorem,T4|separate frozen Q33 audit; implied independently by LOW285|PROVED; not needed separately|
|CTX49|No induced R449 in a balanced original coloring|Frontend Section2, second Turan|PROVED, contextual domain only|
|D48|Every R448 has delta>=12|new h12 proof Section1|PROVED|
|Q20|12-shell necessary conditions force q>=20 and exactly five equality families|new h12 proof Section2|PROVED|
|FLOOR48|Every R448 has e>=310|D48, CORE211,Q20, inserted-center argument|PROVED|
|C29|Every61 graph with delta13,alpha5,omega11,caps has max regular q>=29|frozen COVER Sections1--7, C, energy independence audited|PROVED|
|C407/C408|Same contract and E407 gives Q>=30; E408 gives Q>=31|full frozen COVER, C|PROVED|
|H12|Every61 graph with delta12,alpha5,omega11,caps,E<=408 is impossible|new h12 proof Sections3--5|PROVED|
|H13LOW|Same61 contract with delta13,E<=406 impossible|C29,FLOOR47|PROVED|
|H13TOP|Same61 contract at E407/E408 impossible|two final h13 certificates|PROVED|
|STOP|Every hypothetical original coloring has a residual61 graph with397<=E<=408|frontend analytic rules plus all144 stops|PROVED|
|REPLAY|Three recurrences agree at1,752 nodes; retained COVER checks pass|INDEPENDENT_VERIFIER.py and JSON output|COMPUTATION_CERTIFIED|
|K145|No12-coloring of K145 has every13-set containing all12 colors|FINAL_GLOBAL_PROOF.md|PROVED|
|GEN49|Abstract uncolored high-energy R449 obstruction|No contextual-to-generic transfer authorized|OPEN, outside final dependency path|

L=783c72090205d4bd1a6eefce1dec09e15f78e319, X=c3d07b2ca5912b1b0c1c6998303c19c3c2911340, C=531e41c79e08dd2bb3892ca9ba8a491a56678565. Prior frontend F=b0459807acd4b7e386148056ddf77d7998918893. SOURCE_MANIFEST.json fixes individual file/blob provenance, and SHA256SUMS.txt covers this entire local package.

No load-bearing node remains PROVED_CONDITIONAL. Repository promotion has a separate operational state and does not change these mathematical domains.
