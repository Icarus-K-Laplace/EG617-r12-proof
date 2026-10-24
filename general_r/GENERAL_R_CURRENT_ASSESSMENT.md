# General-r Current Assessment

Status: **OPEN**, but the architecture has changed materially after the contextual full-color cap and the `5r+1` all-large-r anchor extraction theorem.

## 1. New contextual cap principle

For a target residual on `kr+1` vertices arising inside the original balanced `r`-coloring, assume

`alpha(F)<=k`.

For every non-target color `C_j` on the same vertex set,

- `alpha(C_j)<=r` by the balanced-coloring condition;
- `omega(C_j)<=k`, because a `(k+1)`-clique in `C_j` would be a target-independent `(k+1)`-set.

Using the exact Brouwer/Kang-Pikhurko second-Turan layer gives

`e(C_j)>=p_r(kr+1)+(k-1)`.

Therefore the target color satisfies the contextual cap

> **`e(F)<=U_(k,r)`**, where
>
> `U_(k,r)=[k r^2+(k^2-4k+2)r+4k-2]/2`.

This is strictly stronger than the old one-color hereditary cap because it remembers that all `r` colors must coexist on the same residual.

## 2. The 4r+1 branch is dead

For `k=4`,

`U_(4,r)=2r^2+r+7`.

If a contextual `4r+1` residual has the front-end minimum-degree contract

`delta(F)>=r+1`,

then

`e(F)>=(4r+1)(r+1)/2`.

The lower bound exceeds `U_(4,r)` by

`(3r-13)/2`.

Hence:

> **For every `r>=5`, the contextual `4r+1` branch is impossible as soon as `delta(F)>=r+1` is available.**

Thus the old plan “extract 4r+1 residual, then run the 3r-1 backend” is no longer the preferred all-large-r route. In the original-coloring context, the 4r+1 residual should be killed immediately by full-color density compatibility.

At `r=12`, the existing front-end theorem already proves every genuine contextual `R(4,49)` residual has `delta>=13`; therefore the contextual `R(4,49)` branch is empty outright.

## 3. Why 5r+1 is the first genuine terminal

For `k=5`,

`U_(5,r)=(5r^2+7r+18)/2`.

If `delta(F)>=r+2`, then the degree lower bound exceeds this cap for every `r>=5`.

Hence any surviving contextual `5r+1` terminal with the natural lower minimum-degree source is forced into exactly the two layers

> **`delta(F) in {r,r+1}`.**

This explains the r=12 T61 `h=12/13` split as the specialization of a general full-color stability phenomenon rather than a fixed-r accident.

## 4. 5r+1 anchor extraction is closed for r>=71

The file

`GENERAL_R_5R1_ALL_LARGE_R_ANCHOR_EXTRACTION.md`

proves, relative only to the classical Andrasfai-Erdos-Sos theorem and the contextual terminal contract:

> **For every `r>=71`, every contextual `5r+1` terminal contains a direct near-anchor independent triple.**

More precisely:

- if `delta(F)=r`, there is an independent triple of degree pattern

  `(r, <=r+1, <=r+1)`;

- if `delta(F)=r+1`, there is an independent triple of degree pattern

  `(r+1, <=r+2, <=r+2)`.

The difficult `delta=r` branch is reduced by a constant-defect ledger. Under the negation of the triple, a degree-r anchor has a non-neighbourhood split

`L union H`,

with

`|L|=r-1-s`, `0<=s<=8`,

and only `16-2s` excess units remain after charging baseline excess2 to H. Deleting vertices whose extra defect is at least3 removes at most5 points. AES then forces the complement of the remaining graph to be 4-partite for `r>=71`; the endpoint cases `t=4,5` are killed by clique-capacity and greedy K4-transversal arguments.

Therefore the `5r+1` terminal no longer has a growing structural case tree for all large r.

## 5. The new large-r logical DAG

The preferred all-large-r architecture is now

`hypothetical counterexample`

`-> contextual extraction theorem`

`-> either 4r+1 or 5r+1`

`-> 4r+1 dies immediately by contextual cap`

`-> 5r+1 has delta in {r,r+1}`

`-> for r>=71, direct near-anchor triple`

`-> uniform near-anchor incompatibility theorem`

`-> contradiction`.

Thus the two load-bearing missing results are now much cleaner:

1. **upstream contextual extraction:** force the `4r+1 / 5r+1` dichotomy for all sufficiently large r;
2. **downstream near-anchor incompatibility:** turn the extracted low-excess independent triple in the `5r+1` terminal into a contradiction.

The old symbolic d2/d3 support machinery remains valuable for fixed r and for equality diagnostics, but it is no longer the highest-leverage route to an all-large-r theorem.

## 6. Existing symbolic backend assets remain valid

Conditional on a legal `4r+1` backend view, the following are still proved symbolically:

- `e(F)=C(r+2,2)+q+e(H)`;
- `K_r(H)=2(E-q-(2r^2+r+1))`;
- exact regular-repivot identity;
- row closure;
- allowance localization;
- zero-signature/sunflower decomposition;
- repeated-support strict loss;
- exact Bridge B transported-excess identity.

These assets should now be treated primarily as fixed-r / finite-tail machinery, or as a fallback if the contextual extraction theorem outputs a weaker terminal contract than desired.

## 7. Multicolor near-extremal owner capacity

A second new consequence of full-color stability is a slope-1/2 owner bound near contextual extremality.

If the residual contextual edge deficit is epsilon, a clique of target-degree-`r+1` vertices has size at most

`[r-1+2epsilon+epsilon sqrt(4epsilon+1)]/2`.

Hence any common-S owner family satisfies

> **`N <= [r-3+2epsilon+epsilon sqrt(4epsilon+1)]/2`.**

For fixed epsilon this is

`N<=r/2+O_epsilon(1)`,

improving the old hereditary sunflower capacities of slope1.

This creates a genuine slope contradiction whenever shell forcing can produce a common-S class larger than `(1/2+o(1))r`.

## 8. Current status of the old near-anchor/core theorem

For a `3r-1` backend core, the direct forcing lemma still gives an independent triple `(r,<=r+1,<=r+1)` under the residual-core contract. The old desired statement

`independent low-excess triple => K_r>=8`

remains open in general.

However, for the new all-large-r route the more relevant theorem is now the analogous **5r+1 terminal near-anchor incompatibility theorem**. It may be stronger and easier to formulate directly in the original residual rather than passing through a `3r-1` core.

## 9. r=12 implication

For the fixed r=12 project, the contextual 4r+1 cap combines with the already-proved front-end `delta(F)>=13` to show:

> **no genuine contextual `R(4,49)` residual exists in the original balanced K145 coloring.**

Therefore the contextual recurrence may treat the no-49-extraction condition as a theorem rather than a temporary assumption, and the only original front-end obstruction is the embedded T61 branch.

This does not by itself close T61 or the full r=12 proof; it simplifies the front-end dependency DAG.

## 10. Highest-leverage theorem now

The highest-leverage general theorem is no longer a full residual-core extraction into the old backend. It is:

> **Contextual 4r+1 / 5r+1 Extraction Theorem.** For all sufficiently large r, every hypothetical balanced r-coloring of `K_(r^2+1)` in its least-edge color contains either
>
> - a contextual `4r+1` residual with minimum degree at least `r+1`, or
> - a contextual `5r+1` terminal with minimum degree at least r and the inherited full-color completion constraints.

Once this is proved:

- the `4r+1` branch is impossible for all `r>=5`;
- the `5r+1` terminal is forced into `delta in {r,r+1}`;
- for `r>=71`, it automatically contains a direct near-anchor triple;
- only one uniform near-anchor incompatibility theorem remains downstream.

This is currently the shortest plausible path to an all-sufficiently-large-r theorem.