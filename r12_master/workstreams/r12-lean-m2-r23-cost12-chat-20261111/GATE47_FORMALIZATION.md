# GATE47 — LEAN VERIFIED

Frozen source: low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md, Theorem M and M6,
immutable commit c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2.
Exact build evidence: CI_STATUS.json and its complete logs/linux-<run>-full.txt.
Full source signatures: DECLARATION_STATEMENTS.md; elaborated types and every
transitive axiom are printed by the compiled audit modules.

```lean
theorem gate47_verified : Gate47Statement
```

The unchanged baseline definition expands to:
```lean
def Gate47Statement : Prop :=
  ∀ G : SimpleGraph (Fin 47), CoreAdmissible 4 G → G.edgeFinset.card ≤ 286 →
    ∀ v : Fin 47, 12 ≤ G.degree v
```

CoreAdmissible 4 means alpha<=4, omega<=11 and e(G[U])<=D(|U|)
for EVERY finite vertex subset U. No condition is omitted. Fin47 supplies exactly
47 vertices; all counting helpers work on arbitrary finite vertex types.

The proof selects an actual minimum-degree vertex. The existing R337 argument
gives degree>=10. In the degree10 case, its actual36-point nonneighborhood is
in R(3,36); e(C)>=234 and the exact shell degree/edge ledger give e(G)>=289.
No assumption that the shell is a clique is made.

In the degree11 case, e(C)>=210. The full clique bound supplies two distinct
nonadjacent shell vertices x,y. Their common nonneighbors inside C have at
most23 vertices, by inherited R(2,24) impossibility; hence the actual row union
has at least12 vertices. Each actual row size dominates its missing-shell degree.
The two-vertex incidence bound d_M(x)+d_M(y)<=e(M)+1 yields
sum(rows)>=e(M)+11. Since e(S)+e(M)=55, the exact disjoint edge ledger gives
e(G)>=210+11+55+11=287. Both cases contradict the supplied286-edge ceiling.

| Frozen M6 step | Certified theorem |
|---|---|
| Actual shell and exterior ledger | core_shell_edge_degree_ledger |
| d=10 exclusion | core_R447_min_degree_ten_edges_ge_289 |
| Inheritance for common nonneighbors | core_admissible_common_nonNeighbors |
| At most23 common nonneighbors | core_R4_common_nonneighbors_card_le_23 |
| Row union>=12 | core_R4_row_union_ge_twelve |
| Two-vertex missing-edge incidence | core_two_degrees_le_edges_add_one |
| Each row dominates missing degree | core_shell_row_missing_degree_le |
| Sum of rows>=missing edges+11 | core_missing_edge_row_sum |
| d=11 exclusion | core_R447_min_degree_eleven_edges_ge_287 |
| Exact original gate | gate47_verified |

Helper premises are explicit and proved in the parent; none is a hidden terminal
assumption. The row-sum formulation is algebraically the frozen z+sum(g)>=11.
Only the three standard logical axioms occur, as listed in LEAN_AXIOM_AUDIT.md.
Finite diagnostic attacks are separate from the Lean proof and are never imported.

This is not a MainTheorem proving original K145. Parent construction and the
286-edge input are not established by GATE47 itself. No E286 work was performed.
