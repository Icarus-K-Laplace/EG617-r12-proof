# Upstream promotion audit: original Q32 to Astra 3+7 normal form

Date: 2026-10-30  
Status: PROVED_CONDITIONAL for the 3+7 component split; NOT a universal m=10 promotion.

## 1. Exact Astra theorem contract

The Astra structural theorem excludes every graph H satisfying these five properties:

1. Vertex partition: three independent 4-sets S_1,S_2,S_3, seven independent 4-sets D_1,...,D_7, and a residual set R of order seven.
2. Pair edges: after common labels, each small-small pair is an identity perfect matching; every small-outer pair is a perfect matching plus exactly one extra edge; every outer-outer pair contains the same four identity-matching edges, with any additional edges off that matching.
3. Residual structure: Delta(H[R])<=2, 3<=e(H[R])<=7, and there are two labelled partitions of R into four clique fibers F_s and G_g; empty fibers are allowed.
4. Residual incidence: each r in F_s is adjacent to exactly the three small vertices of label s; each r in G_g is adjacent to all seven vertices of outer track g; its number of additional outer incidences is exactly 2-d_R(r).
5. Degree and Ramsey bounds: every outer vertex has degree 12, every small vertex has degree at least 12, alpha(H)<=4, and omega(H)<=11.

The graph theorem itself does not assume the eleven source-colored graphs or a solver result. Its application to Q32 depends on proving all five properties for the actual candidate.

## 2. Promotion chain inside the 3+7 split

Assume the ten-block light graph L is disconnected and its two component sizes are 3+7.

- The component reduction forces the three-block component to be a light triangle, with zero residual-incidence slack on each of its three blocks.
- Every small-to-outer pair is cross-component heavy with exactly one extra unit, hence exactly five edges. The small-small pairs have exactly four edges and are perfect matchings. The 4,5,5 switch theorem and the small-component constraints give the aligned/synchronized-switch local structure.
- On the seven-block component, the ledger gives internal weighted-heavy degree at most two, total internal heavy weight 3+Z<=7, and light minimum degree at least four.
- The outer light-holonomy theorem aligns all four matching tracks across the seven outer blocks. The light graph is connected, so relabelling the four vertices in each outer block makes every light matching the identity. Every heavy pair has a common light neighbor; the two-light matching-composition theorem then forces the same identity matching in every heavy pair. Thus the 28 outer vertices contain four aligned K7 tracks.
- The three zero-slack small blocks give unique-neighbor maps from R into each small block. The zero-slack map-alignment theorem makes the three maps agree. The independent-set incidence cover lemma makes each fiber a clique, yielding F_s and exactly three small neighbors per residual vertex.
- The four K7 tracks give the outer map G_g. Since the residual degree equation is d_R(r)+b_r=2 and all small-block residual incidences are already exactly one, the remaining b_r=2-d_R(r) incidences are precisely additional outer incidences.
- For an outer block D, its internal heavy degree t_D and residual slack y_D satisfy t_D+y_D=2. Its four base outer-track neighbors, residual neighbors, and the three small-extra incidences give d_H(q)=12. The small blocks inherit d_H(q)>=12 from the 47-core contract. The parent maximality gate gives omega(H)<=11; alpha(H)<=4 is part of the Q32 core contract.

Therefore all five Astra properties follow once, and only once in this argument, the original candidate is already in the 3+7 light-component split.

## 3. The missing universal implication

The original Q32 source contract does not imply that L has component sizes 3+7. The proved disconnected reduction allows exactly 1+9, 2+8, 3+7, 4+6, 5+5. It also leaves L connected.

No theorem in the audited source set eliminates 1+9, 2+8, 4+6, 5+5, or connected L. Hence original Q32 candidate => Astra five properties is NOT proved without a separate case split. The valid implication is:

    original Q32 candidate + (L has 3+7 components)
       => Astra five properties
       => contradiction.

The Astra theorem must not be used to eliminate the other component profiles or connected L.

## 4. Astra proof and replay evidence

Actual branch: workstream/r12-astra-independent-structural-attack-20261029  
Actual branch head: 99f60126fdd9c72c450475e7fd75c6c499d69df7  
Key structural commits: d1f05a51c5f7c09e3c3e0a50db07fecdc0321739 and 99f60126fdd9c72c450475e7fd75c6c499d69df7.

The branch's residual catalog records 18 path/cycle types: 14 are excluded by the nonempty-fiber theorem; the remaining four are handled by the empty-fiber analyses. The recorded verifier log reports the 3,456 normalized 4,5,5 inputs with 156 accepted patterns, 42,336 three-small matching representations, the two-triangle replay, the C3+2P2 and C3+P4 replays, and the z=4 empty-fiber replay. These are local finite replays; they are not a full Q32 SAT/UNSAT proof.

## 5. Source-occupancy promotion firewall

The exact Type-I source audit gives three aggregate profiles:
- x_C in O: (2,1^11);
- x_C in H, two-double: (2,2,1^10);
- x_C in H, triple: (3,1^11).

The 90-row labelled factor-occupancy catalog in M10_SOURCE_OCCUPANCY_90.csv is source-complete at this aggregate level. It includes a double-outside isolated K5, two isolated double-outside K5s, an isolated triple-outside K5, and the distinct N_s/N_t special-factor placements.

The isolated-triple occupancy is not excluded by the generic source factorization. It can be excluded only after importing a target-part pointwise degree floor in a specific aligned cell. Therefore the Astra five-property promotion must be justified from the 3+7 graph contracts, not by silently discarding source occupancy modes.

## 6. Conclusion

Astra is a valid conditional structural contradiction for the 3+7 split. It is not an upstream theorem that all original Q32 candidates satisfy the 3+7 contract. The 1+9, 2+8, 4+6, 5+5, connected-light-graph, and endpoint-labelled Type-I source-placement branches remain OPEN. No root Q32 closure is claimed.


## 7. Parent clique-cap provenance for the 4+6 K4-e, Z=4 proof

The K12 contradictions in M10_K4E_Z4_GLOBAL_GRID_CLOSURE.md use omega(H)<=11. This is an inherited parent condition, not a consequence of |H|=47, e(H)=285, alpha(H)<=4, and delta(H)>=12 alone.

The registered T61 residual has omega<=11 in the root promotion audit (workstream/r12-twochat-e408-global-20261026, R12_ROOT_CLOSURE_PROMOTION_AUDIT.md, Section 2). The Q32 core H is an induced 47-vertex subset of that 61-point residual. Therefore omega(H)<=omega(T61)<=11. This dependency is stated explicitly in the new theorem and is used only to rule out a K12 after all ten pivot matching tracks align.

No Q32 parent closure or EG617 root promotion is inferred.
