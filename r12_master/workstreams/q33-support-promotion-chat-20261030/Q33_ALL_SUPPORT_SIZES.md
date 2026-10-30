# Q33 all support sizes — source-correct component-only screen

Status: **COMPUTATION_CERTIFIED** for the exact finite necessary-profile screen under the registered source contract. It is not a graph realization or a full Q33 UNSAT certificate.

The canonical support family chooses seven isolated-K5 component witnesses from each exact-129 color. The nonempty gadget-shell lemma forces the three unselected component core sizes to sum to 9..12, so the gadget core size is 7..10. Thus h=0 by construction and the csum=8 profiles are excluded.

Per-color option count is the number of distinct aggregate (X_U,X_W) pairs. Final DP-state count is the number of aggregate cost pairs surviving after all m exact colors and both reserve budgets. These are cost states, not graph configurations.

## m=8

| v | B_U | B_W | per-color options | final DP states | result |
|---:|---:|---:|---:|---:|---|
|31|-61|84|26|0|EXCLUDED|
|32|-45|75|41|0|EXCLUDED|
|33|-28|67|47|0|EXCLUDED|
|34|-10|60|58|0|EXCLUDED|
|35|9|54|69|0|EXCLUDED|
|36|28|45|69|0|EXCLUDED|
|37|45|37|67|0|EXCLUDED|
|38|63|30|67|0|EXCLUDED|
|39|82|24|69|27|PROFILE_FEASIBLE|
|40|101|18|69|90|PROFILE_FEASIBLE|
|41|121|13|58|204|PROFILE_FEASIBLE|
|42|142|9|47|390|PROFILE_FEASIBLE|
|43|164|6|41|315|PROFILE_FEASIBLE|
|44|186|3|26|172|PROFILE_FEASIBLE|
|45|209|1|17|83|PROFILE_FEASIBLE|
|46|233|0|7|42|PROFILE_FEASIBLE|
|47|254|0|5|39|PROFILE_FEASIBLE|

## m=9

| v | B_U | B_W | per-color options | final DP states | result |
|---:|---:|---:|---:|---:|---|
|32|-59|78|41|0|EXCLUDED|
|33|-40|69|47|0|EXCLUDED|
|34|-20|61|58|0|EXCLUDED|
|35|1|54|69|0|EXCLUDED|
|36|22|45|69|0|EXCLUDED|
|37|42|37|67|0|EXCLUDED|
|38|63|30|67|0|EXCLUDED|
|39|85|24|69|0|EXCLUDED|
|40|107|18|69|27|PROFILE_FEASIBLE|
|41|130|13|58|160|PROFILE_FEASIBLE|
|42|154|9|47|380|PROFILE_FEASIBLE|
|43|179|6|41|315|PROFILE_FEASIBLE|
|44|204|3|26|172|PROFILE_FEASIBLE|
|45|230|1|17|83|PROFILE_FEASIBLE|
|46|257|0|7|42|PROFILE_FEASIBLE|
|47|281|0|5|39|PROFILE_FEASIBLE|

## m=10

| v | B_U | B_W | per-color options | final DP states | result |
|---:|---:|---:|---:|---:|---|
|34|-30|62|58|0|EXCLUDED|
|35|-7|54|69|0|EXCLUDED|
|36|16|45|69|0|EXCLUDED|
|37|39|37|67|0|EXCLUDED|
|38|63|30|67|0|EXCLUDED|
|39|88|24|69|0|EXCLUDED|
|40|113|18|69|0|EXCLUDED|
|41|139|13|58|120|PROFILE_FEASIBLE|
|42|166|9|47|370|PROFILE_FEASIBLE|
|43|194|6|41|315|PROFILE_FEASIBLE|
|44|222|3|26|172|PROFILE_FEASIBLE|
|45|251|1|17|83|PROFILE_FEASIBLE|
|46|281|0|7|42|PROFILE_FEASIBLE|
|47|308|0|5|39|PROFILE_FEASIBLE|

## Exact result

- m=8: excluded v=31..38; first aggregate survivor v=39.
- m=9: excluded v=32..39; first aggregate survivor v=40.
- m=10: excluded v=34..40; first aggregate survivor v=41.

The support lower bounds are v>=31,32,34, respectively. The m=8 lower bound uses the registered near-Turán/linear-block packing lemma at v=30; the m=9,10 lower bounds follow from 42m>t4(v) at v=31,33.

## First-survivor W structure

At m=8,v=39, each exact color has minimum W-cost3 and the W budget is24=8*3. Thus all eight exact colors attain the minimum and \(\overline{H[W]}=K_{2,2,2,2}\), so H[W]=4K2. Each exact-color W-edge set is a 3-edge matching.

At m=9,v=40, each exact color has minimum W-cost2 and the W budget is18=9*2. Thus \(\overline{H[W]}=K_{2,2,2,1}\), so H[W]=3K2 plus an isolated vertex. Each exact-color W-edge set is a 2-edge matching.

At m=10,v=41, the per-color minimum W-cost is1 and the W budget is13, leaving at most3 units of aggregate W slack.

A PROFILE_FEASIBLE entry means only that this aggregate necessary relaxation has a cost-pair survivor. It does not produce a labelled graph or certify that any actual Q33 completion exists.
