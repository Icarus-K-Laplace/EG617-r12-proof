# Exact 5r+1 terminal and its design-like irreducible form

Status: `PROVED_SYMBOLIC` for the reductions in this file.

Assume `r>=17` and the canonical greedy extraction of `ANCHOR_NORMALIZATION_AND_GREEDY_EXTRACTION.md` reaches its first `K_r`-free state at `a=5`.

Define `T=T_r`.

## Base terminal contract

`T` satisfies

- `|T|=5r+1`;
- **`alpha(T)=5`**;
- `omega(T)<=r-1`;
- every induced subgraph inherits the least-color cap;
- `e(T)<=3r^2-2r`;
- `T` contains no target-color `K_r`.

The equality `alpha(T)=5` is automatic from the alpha-saturation theorem in `RECURRENCE_REPLACEMENT_POTENTIALS.md`: a canonical `R_a` cannot have alpha below a without violating its edge budget.

This is an exact symbolic contract, not an analogy.

## Residual-or-rigid refinement

If `T` contains an induced `F` on `4r+1` vertices with `alpha(F)<=4`, then `omega(F)<=r-1` and the hereditary cap are automatic. `RESIDUAL_BRANCH_CLOSURE.md` then gives Branch A.

Therefore an **irreducible** 5r+1 terminal (one from which Branch A cannot already be extracted) has the following equivalent design condition.

### Independent-5 hypergraph

Let

`I_5(T) := { S subset V(T) : |S|=5 and S is independent in T }`.

Let `tau(I_5(T))` be its vertex-transversal number.

Then irreducibility is equivalent to

> `tau(I_5(T))>=r+1`.

### Proof of equivalence

If `tau(I_5(T))<=r`, extend a transversal to an `r`-vertex set `Z`. Then `T-Z` has exactly `4r+1` vertices and contains no independent 5-set, hence `alpha(T-Z)<=4`; this is Branch A.

Conversely, if an induced `4r+1` graph `F=T-Z` has `alpha(F)<=4`, then its deleted `r`-set `Z` meets every independent 5-set of `T`. Thus `tau(I_5(T))<=r`.

Status: `PROVED_SYMBOLIC`.

This gives a literal block-design object: the independent 5-sets form a 5-uniform hypergraph whose transversal number exceeds `r`.

## Minimum degree in an irreducible terminal

Every irreducible `T_r` satisfies

> `delta(T)>=r`.

### Proof

If `d_T(v)<=r-1`, then

`A=T-N_T[v]`

has at least

`5r-d_T(v)>=4r+1`

vertices. Because `alpha(T)=5`, `alpha(A)<=4`: an independent 5-set in `A` together with `v` would be independent of size 6 in `T`.

Choose any `4r+1` vertices of `A`. The induced graph has alpha at most 4 and hence gives Branch A, contradiction.

Status: `PROVED_SYMBOLIC` conditional only on residual-branch closure.

## Exact degree-r witness property

Suppose an irreducible terminal contains a vertex `v` with

`d_T(v)=r`.

Then

`A_v:=T-N_T[v]`

has exactly `4r` vertices and `alpha(A_v)<=4`.

For **every** neighbor `y in N_T(v)`, there exists an independent 4-set

`I_y subset A_v`

such that `y` has no neighbors in `I_y`.

### Proof

Otherwise, for some neighbor `y`, the induced graph on

`A_v union {y}`

would have `4r+1` vertices and no independent 5-set: any independent 5-set would have to contain `y` plus an independent 4-set in `A_v` entirely nonadjacent to `y`. Therefore `alpha(A_v union {y})<=4`, giving Branch A.

Status: `PROVED_SYMBOLIC`.

This is a concrete block-incidence requirement on every degree-r row, not an affine-plane heuristic.

## Complement formulation

Let `L=bar T`. Then an irreducible terminal satisfies

- `|L|=5r+1`;
- `omega(L)=5`;
- `alpha(L)<=r-1`;
- every `n`-vertex induced subgraph has at least `(r-1)p_r(n)` edges;
- the family of `K_5` vertex sets in `L` has transversal number at least `r+1`;
- `Delta(L)<=4r` because `delta(T)>=r`.

Thus the `5r+1` terminal is a dense hereditary-cap graph whose `K_5` blocks resist every `r`-vertex hitting set. This is the exact finite-geometric / block-design interface to be studied next if the terminal survives.

## Status relative to the desired dichotomy

If the remaining `a>=6` stopping obstruction is eliminated, the front-end theorem becomes:

> every hypothetical counterexample with `r>=17` produces either
> (A) the fully certified `4r+1 -> 3r-1` residual-core contract, or
> (B) an irreducible `5r+1` terminal satisfying all conditions above.

The terminal is therefore now mathematically defined with O(1) symbolic conditions; what remains open is whether it exists and, before that, whether a canonical greedy process can stop above `a=5`.