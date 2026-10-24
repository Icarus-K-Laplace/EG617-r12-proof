# Adversarial audit
Overall status: PARTIAL.

## First unsupported implication
"Canonical greedy extraction terminates" => "its first K_r-free stop has a<=5".
The first statement is proved; the second is OPEN. This is the first missing implication on the chosen extraction route, before near-anchor or design-terminal exclusions.

## Symbolic scalar survivor, not a graph
For a=6 and r>=7 choose
x_0=r-1, x_1=5+(8r+12), x_2=...=x_(r-1)=5.
Then all second-Turan scalar floors hold, their sum is 14r+6, and
p_6(6r+1)+x_0<=B_6 because binom(r,2)>=r-1.
Also x_0 is below the contextual target cap. This proves feasibility of precisely this scalar ledger, NOT every graph-level constraint.
It neither assigns edges nor certifies critical cores, minimum degrees, or simultaneous colour compatibility.

## Real single-colour sharpness witness
H_(6,r), r>=62, has 6r+1 vertices, alpha=r, omega=6, e=15r+11, maximum degree 10.
It satisfies every inherited single-colour D_r cap.
Its precise construction and proof are in THEOREM section 5.
Thus a proposed increase of the NON-TARGET floor using only alpha<=r, omega<=6 and the hereditary caps is false.
All r-1 non-target colours cannot simply be assigned this same graph: they must be edge-disjoint and leave a compatible target graph. That simultaneous question remains OPEN.

## Quantifier and predecessor checks
Fixed-a results with thresholds depending on a do not yield a theorem simultaneously for 6<=a<=r-1.
At a=r-1 there may be zero deleted blocks, so the predecessor label lemma is inapplicable.
Neither finding refutes the source's fixed-a theorem, whose eventual range does have a predecessor.

## Accounting checks
The exact residual count always subtracts cross edges.
Induced normalization uses averaging, not equality of residual edges and an outer budget.
The scalar target floor is not a target graph construction.
A (4r+1) density contradiction needs its minimum-degree input.
No solver status is used.

## New extraction scope check
Minimal induced-rank selection is well-founded on finite integers. It cannot inherit the old canonical B_a edge budget merely from the starting state. THEOREM section 7 intentionally uses only full-colour contextual caps.
No r-clique packing, predecessor, or design completion is required for this reduction.
The H_(a,r) obstruction is a non-target graph, so it does not refute the new target minimum-degree statement.
