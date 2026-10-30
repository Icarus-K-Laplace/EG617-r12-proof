# Q33 all support sizes — source-correct component-only screen

Status: **COMPUTATION_CERTIFIED** for the exact finite necessary-profile screen under the registered source contract. It is not a graph realization or a full Q33 UNSAT certificate.

The canonical support family chooses seven isolated-K5 component witnesses from each of the \(m\) exact-129 colors. Thus \(h=0\) by construction. The earlier all-h table is retained only as a broader diagnostic relaxation; it is not the canonical screen because a source-guaranteed component-only choice is available.

The per-color option count is the number of distinct aggregate \((X_U,X_W)\) pairs. The final DP-state count is the number of aggregate cost pairs surviving after all \(m\) exact colors and both reserve budgets. These are cost states, not graph configurations.

## m=8

| v | B_U | B_W | per-color options | final DP states | result |
|---:|---:|---:|---:|---:|---|
|31|-61|84|35|0|EXCLUDED|
|32|-45|75|56|0|EXCLUDED|
|33|-28|67|61|0|EXCLUDED|
|34|-10|60|75|0|EXCLUDED|
|35|9|54|85|0|EXCLUDED|
|36|28|45|84|0|EXCLUDED|
|37|45|37|78|0|EXCLUDED|
|38|63|30|78|0|EXCLUDED|
|39|82|24|84|27|PROFILE_FEASIBLE|
|40|101|18|85|90|PROFILE_FEASIBLE|
|41|121|13|75|204|PROFILE_FEASIBLE|
|42|142|9|61|390|PROFILE_FEASIBLE|
|43|164|6|56|315|PROFILE_FEASIBLE|
|44|186|3|35|172|PROFILE_FEASIBLE|
|45|209|1|21|83|PROFILE_FEASIBLE|
|46|233|0|10|42|PROFILE_FEASIBLE|
|47|254|0|8|39|PROFILE_FEASIBLE|

## m=9

| v | B_U | B_W | per-color options | final DP states | result |
|---:|---:|---:|---:|---:|---|
|32|-59|78|56|0|EXCLUDED|
|33|-40|69|61|0|EXCLUDED|
|34|-20|61|75|0|EXCLUDED|
|35|1|54|85|0|EXCLUDED|
|36|22|45|84|0|EXCLUDED|
|37|42|37|78|0|EXCLUDED|
|38|63|30|78|0|EXCLUDED|
|39|85|24|84|0|EXCLUDED|
|40|107|18|85|27|PROFILE_FEASIBLE|
|41|130|13|75|160|PROFILE_FEASIBLE|
|42|154|9|61|380|PROFILE_FEASIBLE|
|43|179|6|56|315|PROFILE_FEASIBLE|
|44|204|3|35|172|PROFILE_FEASIBLE|
|45|230|1|21|83|PROFILE_FEASIBLE|
|46|257|0|10|42|PROFILE_FEASIBLE|
|47|281|0|8|39|PROFILE_FEASIBLE|

## m=10

| v | B_U | B_W | per-color options | final DP states | result |
|---:|---:|---:|---:|---:|---|
|34|-30|62|75|0|EXCLUDED|
|35|-7|54|85|0|EXCLUDED|
|36|16|45|84|0|EXCLUDED|
|37|39|37|78|0|EXCLUDED|
|38|63|30|78|0|EXCLUDED|
|39|88|24|84|0|EXCLUDED|
|40|113|18|85|0|EXCLUDED|
|41|139|13|75|120|PROFILE_FEASIBLE|
|42|166|9|61|370|PROFILE_FEASIBLE|
|43|194|6|56|315|PROFILE_FEASIBLE|
|44|222|3|35|172|PROFILE_FEASIBLE|
|45|251|1|21|83|PROFILE_FEASIBLE|
|46|281|0|10|42|PROFILE_FEASIBLE|
|47|308|0|8|39|PROFILE_FEASIBLE|

## Exact result

- \(m=8\): excluded \(v=31,\ldots,38\); first aggregate survivor \(v=39\).
- \(m=9\): excluded \(v=32,\ldots,39\); first aggregate survivor \(v=40\).
- \(m=10\): excluded \(v=34,\ldots,40\); first aggregate survivor \(v=41\).

The support lower bounds are \(v\ge31,32,34\), respectively. The \(m=8\) lower bound uses the registered near-Turán/linear-block packing lemma at \(v=30\); the \(m=9,10\) lower bounds follow from \(42m>t_4(v)\) at \(v=31,33\).

A PROFILE_FEASIBLE entry means only that this aggregate necessary relaxation has a cost-pair survivor. It does not produce a labelled graph and does not certify that any actual Q33 completion exists.
