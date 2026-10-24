# General-r least-color minimum-degree seed and exact extension budget

Status: **PROVED_RELATIVE_TO_BROUWER SECOND-TURAN**.

This is an upstream theorem in the original `K_(r^2+1)` coloring, independent of the later `4r+1 / 5r+1` residual contracts.

## 1. Least-color setup

Let G be a least-edge color in a hypothetical balanced r-coloring of `K_(r^2+1)` avoiding the desired `(r+1)`-set omission.

Then

- `|V(G)|=r^2+1`;
- `e(G)<=r(r^2+1)/2` by averaging over the r colors;
- `alpha(G)<=r`;
- `omega(G)<=r`.

Let v be a minimum-degree vertex and put

`d=d_G(v)`.

Write

`A=N_G(v)`, `|A|=d`,

`B=V(G)\(A union {v})`, `|B|=r^2-d`.

Because v is target-nonadjacent to every vertex of B, an independent r-set in G[B] together with v would give an independent `(r+1)`-set. Therefore

> **`alpha(G[B])<=r-1`.**

Also `omega(G[B])<=r` is inherited.

## 2. Constrained lower bound inside B

Let H=G[B]. Its complement J is K_r-free because `alpha(H)<=r-1`.

If `d<r`, then

`|B|=r^2-d > r(r-1)`.

If J were `(r-1)`-partite, each part would be an independent set in J, hence a clique in H. Since `omega(H)<=r`, each part would have size at most r, and `(r-1)` parts could cover at most `r(r-1)` vertices, contradiction.

Hence J is a non-`(r-1)`-partite K_r-free graph.

Brouwer's exact second-Turan theorem gives

`e(J)<=t_(r-1)(|B|)-floor(|B|/(r-1))+1`.

Taking complements,

> **`e(H)>=p_(r-1)(|B|)+floor(|B|/(r-1))-1`.**

This is the correct constrained lower bound; the ordinary `p_(r-1)` floor is unattainable because of the simultaneous clique cap.

## 3. Degrees 0 and 1 are impossible

The total target edge count satisfies

`e(G)>=d+e(H)`.

### d=0

Now `|B|=r^2`. The constrained lower bound gives

`e(H)>=p_(r-1)(r^2)+r`.

A direct evaluation shows

`p_(r-1)(r^2)+r = r(r^2+1)/2 + (r+1)`.

Thus the lower bound exceeds the least-color averaging upper bound by `r+1`, contradiction.

### d=1

Now `|B|=r^2-1=(r-1)(r+1)`. The constrained lower bound is

`e(H)>=p_(r-1)(r^2-1)+r`.

Adding the single edge incident with v gives

`1+e(H) >= r(r^2+1)/2 +1`,

again one edge above the allowed least-color budget.

Therefore

> **`delta(G)>=2`.**

This holds for every r in the range where the balanced counterexample contract and Brouwer theorem apply (in particular all r>3 relevant to Problem 617).

## 4. Exact extension budget for 2<=d<=r-1

For `2<=d<=r-1`, divide

`r^2-d=(r-1)r+(r-d)`.

Hence

`floor((r^2-d)/(r-1))=r`,

and the constrained floor is

`e(H)>=p_(r-1)(r^2-d)+(r-1)`.

Let

`xi_B = e(H)-[p_(r-1)(r^2-d)+(r-1)] >=0`

be the excess above this second-Turan floor.

The total edge decomposition is

`e(G)=d+e(A)+e(A,B)+e(H)`.

Subtracting from the least-color upper bound gives exactly

> **`e(A)+e(A,B)+xi_B <= (d-1)(r-1)`.**

Thus after fixing the minimum degree d, every deviation from the constrained second-Turan core B, together with all target edges inside A and from A into B, lives inside a linear defect budget `(d-1)(r-1)`.

## 5. Interpretation for the general contextual recurrence

The symbolic front recurrence should not treat the `r^2-d` non-neighbourhood as an arbitrary lower-order state.

It is already forced into a near-second-Turan regime with only

`(d-1)(r-1)`

total extension budget.

For small d this is extremely rigid. The next front-end objective is to classify/repivot these bounded-defect extensions or prove that each forces the minimum degree upward. This provides a direct symbolic replacement candidate for the low-degree portion of the r=12 1752-node contextual recurrence.
