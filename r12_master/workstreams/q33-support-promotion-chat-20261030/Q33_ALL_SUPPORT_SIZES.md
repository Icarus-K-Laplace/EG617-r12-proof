# Q33 component-only U/W support screen — KP-refined

Status: COMPUTATION_CERTIFIED for the finite necessary-profile relaxation, not a graph-level UNSAT certificate.

Choose seven guaranteed isolated-K5 component witnesses from each exact-129 color, so h=0. The KP Type-I gadget consists of two special K5s and one exceptional vertex. Each K5 has at most four core vertices by alpha(H)<=4, and the exceptional vertex contributes at most one. Thus the gadget core has size7..9. With seven selected component K4s, the three remaining component core sizes satisfy 10<=sum(c_i)<=12. This supersedes the earlier 9..12 shell-only profile.

Per-color option counts are distinct aggregate (X_U,X_W) pairs. Final DP-state counts are aggregate cost pairs after all exact colors and both reserve budgets, not labelled graph configurations.

## m=8

|v|B_U|B_W|options|DP states|result|
|---:|---:|---:|---:|---:|---|
|31|-61|84|18|0|EXCLUDED|
|32|-45|75|27|0|EXCLUDED|
|33|-28|67|31|0|EXCLUDED|
|34|-10|60|39|0|EXCLUDED|
|35|9|54|48|0|EXCLUDED|
|36|28|45|50|0|EXCLUDED|
|37|45|37|50|0|EXCLUDED|
|38|63|30|50|0|EXCLUDED|
|39|82|24|50|27|PROFILE_FEASIBLE|
|40|101|18|48|90|PROFILE_FEASIBLE|
|41|121|13|39|202|PROFILE_FEASIBLE|
|42|142|9|31|298|PROFILE_FEASIBLE|
|43|164|6|27|255|PROFILE_FEASIBLE|
|44|186|3|18|150|PROFILE_FEASIBLE|
|45|209|1|10|68|PROFILE_FEASIBLE|
|46|233|0|4|32|PROFILE_FEASIBLE|
|47|254|0|3|17|PROFILE_FEASIBLE|

## m=9

|v|B_U|B_W|options|DP states|result|
|---:|---:|---:|---:|---:|---|
|32|-59|78|27|0|EXCLUDED|
|33|-40|69|31|0|EXCLUDED|
|34|-20|61|39|0|EXCLUDED|
|35|1|54|48|0|EXCLUDED|
|36|22|45|50|0|EXCLUDED|
|37|42|37|50|0|EXCLUDED|
|38|63|30|50|0|EXCLUDED|
|39|85|24|50|0|EXCLUDED|
|40|107|18|48|27|PROFILE_FEASIBLE|
|41|130|13|39|160|PROFILE_FEASIBLE|
|42|154|9|31|310|PROFILE_FEASIBLE|
|43|179|6|27|270|PROFILE_FEASIBLE|
|44|204|3|18|163|PROFILE_FEASIBLE|
|45|230|1|10|76|PROFILE_FEASIBLE|
|46|257|0|4|36|PROFILE_FEASIBLE|
|47|281|0|3|19|PROFILE_FEASIBLE|

## m=10

|v|B_U|B_W|options|DP states|result|
|---:|---:|---:|---:|---:|---|
|34|-30|62|39|0|EXCLUDED|
|35|-7|54|48|0|EXCLUDED|
|36|16|45|50|0|EXCLUDED|
|37|39|37|50|0|EXCLUDED|
|38|63|30|50|0|EXCLUDED|
|39|88|24|50|0|EXCLUDED|
|40|113|18|48|0|EXCLUDED|
|41|139|13|39|120|PROFILE_FEASIBLE|
|42|166|9|31|319|PROFILE_FEASIBLE|
|43|194|6|27|283|PROFILE_FEASIBLE|
|44|222|3|18|170|PROFILE_FEASIBLE|
|45|251|1|10|82|PROFILE_FEASIBLE|
|46|281|0|4|40|PROFILE_FEASIBLE|
|47|308|0|3|21|PROFILE_FEASIBLE|

## Exact frontier

- m=8: excluded v=31..38; first aggregate survivor v=39.
- m=9: excluded v=32..39; first aggregate survivor v=40.
- m=10: excluded v=34..40; first aggregate survivor v=41.

The support floors remain v>=31,32,34. The KP refinement reduces per-color option sets but does not change the exclusion frontier.

## First-survivor W structure

At (m,v)=(8,39), minimum per-color W cost is3 and total W budget24, forcing H[W]=4K2; each exact-color W-edge set is a 3-edge matching.
At (m,v)=(9,40), minimum per-color W cost is2 and total W budget18, forcing H[W]=3K2 union K1; each exact-color W-edge set is a 2-edge matching.
At (m,v)=(10,41), minimum total W cost is10 against budget13, leaving at most3 units of W slack.

This screen omits labelled incidence, gadget-shell labels, and the full vertex degree/excess ledger. PROFILE_FEASIBLE is not a graph realization. Q33 remains OPEN / NOT_CERTIFIED.
