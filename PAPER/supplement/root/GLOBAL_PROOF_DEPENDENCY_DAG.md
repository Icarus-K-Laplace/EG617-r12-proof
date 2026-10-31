# Acyclic root dependency graph

The exact machine-readable adjacency list is PROOF_DAG.json (node -> prerequisites). The verifier checks every referenced node exists and performs a depth-first cycle check. Result:25 nodes, ACYCLIC. The principal paths are:

    original coloring + Turan -> hereditary caps
    caps + lower-order proof -> source gate
    source gate + abstract low285 + abstract286 -> R447 floor287
    lower-order + AES -> CORE211
    lower-order + q20 classification + CORE211 -> R448 floor310 -> h12 empty
    lower-order -> general COVER Q29
    general COVER Q29 + CORE211 -> full E407/E408 COVER
    COVER + R447 floor287 -> every h13 E<=408 empty

    original coloring + lower-order + second Turan -> contextual49 empty
    caps + Brooks -> exact d/j extraction
    contextual49 + lower floors47/48 + proved recurrence -> unique61 stop
    unique61 stop + h12/h13 closure + other-degree exclusions -> K145 contradiction

Logical ordering differs from file chronology: CORE211 is proved directly by LOWER+AES, even though its text also appears in COVER Section8. The48-point theorem therefore does NOT depend on COVER's terminal conclusion. COVER's class is an arbitrary graph contract; it does NOT need the frontend to construct F before its universal theorem can be proved. Conversely the recurrence uses weaker numerical47/48 seeds whose proofs precede it. These distinctions prevent the apparent frontend/backend circle.

The second Turan contextual49 proof uses none of the47/48 or T61 terminal results. Generic R449 emptiness, E333--340 shell classifications, old Q32/Q33 parent gates, general-r finite tails and zero-cycle assertions are absent from all final paths.

External nodes: Turan (including Mantel), Brooks, AES, second Turan. Their exact statements, specialization and primary references are in K145_TO_T61_FRONTEND_AUDIT.md. The bipartite matching-cover lemma is proved there by alternating paths, so no additional untraced external node is required.

Finite evidence: the complete integer recurrence is newly reconstructed in INDEPENDENT_VERIFIER.py; lower-order type/family verification is frozen/low/INDEPENDENT_VERIFIER.py; the authenticated full COVER enumerator and prior result are frozen/cover/INDEPENDENT_VERIFIER.py and VERIFICATION_RESULT.json. Only retained-state checks are repeated here. Equality support completeness is rechecked as a tiny orbit quotient and independently proved in the frozen equality theorem.

Each root promotion must preserve the graph-contract and contextual qualifiers in GLOBAL_THEOREM_LEDGER.md. A file's location or a source status label is not a DAG edge.
