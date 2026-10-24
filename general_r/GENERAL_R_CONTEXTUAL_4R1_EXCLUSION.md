# General-r Contextual 4r+1 Exclusion

Status: **PROVED_SYMBOLIC**, conditional only on the residual being an induced subset of the original balanced r-colouring, `alpha(F)<=4`, and `delta(F)>=r+1`. External input: Brouwer exact Turan stability.

This theorem is stronger than the one-color hereditary cap and bypasses the backend completely on the 4r+1 branch.

## 1. Other colors satisfy a two-sided Ramsey constraint

Let R be a set of `4r+1` vertices in the original balanced r-colouring, and fix one target color with graph F on R.

Assume

`alpha(F)<=4`.

For every other color j, let C_j be its graph on the same R.

The original Problem-617 condition implies

`alpha(C_j)<=r`:

otherwise an independent `(r+1)`-set in color j would be an `(r+1)`-set missing color j.

Also

`omega(C_j)<=4`:

a color-j K5 would have no target-color edges among its five vertices, giving an independent5 in F.

Hence every non-target color satisfies

> **`alpha(C_j)<=r` and `omega(C_j)<=4`.**

## 2. Minimum edge theorem on 4r+1 vertices

The ordinary alpha<=r edge floor is

`p_r(4r+1)=6r+4`.

We prove the stronger contextual floor

> **`e(C_j)>=6r+7`.**

Suppose instead

`e(C_j)<=p_r(4r+1)+2`.

Then `J=bar(C_j)` is `K_(r+1)`-free and has at least

`ex(4r+1,K_(r+1))-2`

edges.

Brouwer's exact Turan stability theorem states that if `n>=2r+1` and a `K_(r+1)`-free graph has at least

`ex(n,K_(r+1))-floor(n/r)+2`

edges, then it is r-partite.

Here `floor((4r+1)/r)=4`, so the threshold is exactly `ex-2`. Therefore J is r-partite.

But every r-partition of `4r+1` vertices has a part of size at least5. That part is independent in J, hence a clique of size at least5 in C_j, contradicting `omega(C_j)<=4`.

Thus `e(C_j)>=6r+7`.

## 3. Strengthened contextual target cap

The r color classes partition all pairs of R. Therefore

`e(F) = C(4r+1,2)-sum_(j!=target)e(C_j)`
`     <= C(4r+1,2)-(r-1)(6r+7)`.

Exact simplification gives

> **`e(F)<=2r^2+r+7`.**

Compare this with the ordinary one-color hereditary cap

`D_r(4r+1)=2r^2+4r+4`.

The full-color context improves the cap by exactly

> **`3(r-1)`.**

This gain is invisible if the residual is treated as a generic one-color Ramsey graph.

## 4. Minimum-degree contradiction

Assume additionally

`delta(F)>=r+1`.

Then

`e(F)>=ceil((4r+1)(r+1)/2)`.

Ignoring the harmless ceiling, the lower minus the contextual upper bound is

`[(4r+1)(r+1)]/2 -(2r^2+r+7)`
`=(3r-13)/2`.

This is positive for every `r>=5`.

Hence:

> **Contextual 4r+1 Exclusion Theorem.**
>
> For every `r>=5`, no induced target residual on `4r+1` vertices arising from the original balanced r-colouring can simultaneously satisfy
>
> `alpha(F)<=4` and `delta(F)>=r+1`.

No residual-core theorem, repivot identity, anchor theorem, or support classification is needed.

## 5. r=12 corollary

In the main r=12 front-end, `FRONTEND_BRIDGE_THEOREM.md`, F5 proves that every contextual induced `R(4,49)` produced from the original least-edge color satisfies

`delta(F)>=13`.

The present theorem gives, directly,

`e(F)<=2*12^2+12+7=307`,

while minimum degree13 gives

`e(F)>=ceil(49*13/2)=319`.

Contradiction.

Therefore:

> **The fixed original least-edge graph G contains no contextual induced `R(4,49)`.**

Thus the temporary no-extraction hypothesis C0/F7 in the r=12 front-end can be replaced by a proved multicolor theorem. The F7 recurrence consequently forces every hypothetical r=12 counterexample directly into the embedded T61 terminal.

This does not by itself prove T61 empty.

## 6. General-r architectural consequence

The general front theorem should no longer aim to feed the 4r+1 branch into the backend.

Instead the target becomes:

`counterexample`
` -> contextual 4r+1 residual with delta>=r+1` **(immediate contradiction)**
` OR`
` -> controlled 5r+1 design-like terminal.`

Therefore the only genuinely surviving front branch for sufficiently large r is the 5r+1 terminal.

This substantially lowers the strategic importance of generalizing the 4r+1 backend anchor/support machinery as a route to the full conjecture, although that machinery remains valuable as an independent structural theorem family.
