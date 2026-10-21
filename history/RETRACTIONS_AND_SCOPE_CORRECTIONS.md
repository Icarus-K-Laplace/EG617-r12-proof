# Retractions and scope corrections

This file exists to prevent old exploratory claims from silently re-entering the final manuscript.

## RETRACTED: exact E325 bridge requirement

Old architecture tried to prove an exact 49-point residual with `e(F)=325`.

Current architecture only needs a legitimate induced `F in R(4,49)`; the backend handles edge layers. Exact E325 is not a required front-end target.

## RETRACTED: anchor algebraic 66 means a K12

For a degree-11 anchor,

`e(G[N[v]]) = 66-z`,

not automatically 66. The old inference that the anchor contribution creates a genuine K12 without proving `z=0` was invalid.

Current status: `z=0` has now been separately proved inside T61; the historical shortcut remains retracted because its reasoning was wrong.

## RETRACTED: full `(5,7,8,8)` profile closed

The original singleton-triangle argument requires explicit cross-row singleton adjacency hypotheses. It proves a labelled branch, not the entire sorted profile.

Later scalar lemmas remove additional k=0/k=1 cases, but the full profile and T61-to-S30 coverage remain open.

## RETRACTED: eight-block high-cross branch remains open

Once eight genuine K12 blocks exist, matching-transversal rigidity plus equality rotation removes the alpha>=5 branch analytically and yields a legal 49-point residual.

What remains open is forcing/extracting the needed block/residual structure, not the conditional eight-block theorem.

## SCOPE CORRECTION: q29 good repivot

Correct theorem:

`q=29` plus inherited `delta(H)>=12`

`=> exists degree-13 pivot y with q_y>=30`.

The existence theorem does not require `e(H)=211`.

CORE211 enters only when applying the theorem to a fixed edge layer such as E331, where it provides the upper bound on every new pivot.

## SCOPE CORRECTION: S31

Correct theorem applies to the explicit 61-point parent:

`e=406, delta>=13, alpha<=5, omega<=11`, plus the audited hereditary density assumptions.

Conclusion: a degree-13 pivot with `q<=30` exists.

It does not prove that every T61 object has E406/delta13, does not construct a new K12, and does not by itself imply outer descent.

## SCOPE CORRECTION: S27

Retain only the certified scope supplied by the audit: the relevant 47-core with `e=288` and minimum degree11 is impossible.

A parent statement `q=27` may imply the edge count in one fixed edge layer but does not automatically imply the required minimum-degree hypothesis.

## SCOPE CORRECTION: historical E405 q30-LIFT

This is a valid template under its stronger 47-point/EDGE13 parent contract. It cannot be transferred verbatim to E332 q30+211, whose shell/core contract is weaker/different.

## RETRACTED: solver UNSAT as proof

Any historical solver-only infeasibility claim without a small independently checkable certificate is discovery evidence only. Final status must be analytic PROVED or COMPUTATION_CERTIFIED under the repository policy.

## Current safety rule

When two integration documents disagree, the result with the strongest explicit assumptions/provenance wins, not the chronologically latest CLOSED label.