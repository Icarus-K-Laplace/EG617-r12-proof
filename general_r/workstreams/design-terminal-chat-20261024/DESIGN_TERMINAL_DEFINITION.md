# Precise general `(5r+1)` terminal definition

Status: **PROVED_SYMBOLIC as a conditional object; forcing into the object is OPEN**.

The definition is intentionally embedding-aware. A naked graph on `5r+1` vertices is not enough: the r=12 terminal carried an anchor and a maximal block packing, and the multicolor completion is essential.

## 1. Ambient contract

Let `r>=6`. Suppose an `r`-edge-coloring of `K_(r^2+1)` is a hypothetical counterexample: every `(r+1)`-set sees every color. Fix a least-edge target color graph `G`.

Then every color graph has independence number at most `r`; the target has clique number at most `r`; and

`e(G)<=M_r:=r(r^2+1)/2`.

## 2. Anchored terminal witness `T_r`

A **front-compatible anchored terminal witness** consists of:

1. a target vertex `v` with `d_G(v)=r-1`;
2. `A=N_G(v)` and `U=V(G)\N_G[v]`;
3. an inclusion-maximal packing `Q_1,...,Q_(r-6)` of disjoint target `K_r` blocks inside `U`;
4. the induced remainder
   `R=G[U \ (Q_1 union ... union Q_(r-6))]`.

Then, exactly,

> `|R| = r^2-(r-1)-(r-6)r = 5r+1`.

The greedy representative argument gives

> `alpha(R)<=5`,

and maximality gives

> `omega(R)<=r-1`.

Every induced subset of `R` inherits the multicolor density cap

`e_target(X)<=D_r(|X|):=C(|X|,2)-(r-1)p_r(|X|)`.

These are symbolic consequences of the witness, not conjectural design properties.

## 3. Exact anchor ledger

Put

- `sigma=M_r-e(G)>=0`;
- `z=C(r-1,2)-e_G(A)>=0`;
- `g=sum_(a in A)(d_G(a)-(r-1))>=0`;
- `x` = target edges between the packed `K_r` blocks;
- `y` = target edges from those blocks to `R`.

The general anchor decomposition gives

> `e(R)+sigma+z+g+x+y = 3r^2-2r`.  (T-LEDGER)

At `r=12` this right-hand side is `408`.

This is the correct symbolic replacement for the r=12 outer ledger.

## 4. Contextual no-extraction strengthening `T_r^*`

Assume additionally that the fixed ambient target graph contains no legal `(4r+1)` residual with `alpha<=4`, `omega<=r-1`, and the inherited density caps.

Then:

### Exact independence

If `alpha(R)<=4`, any `4r+1` vertices of `R` would already form such a residual. Hence

> `alpha(R)=5`.

### Minimum degree

If `u in R` had `d_R(u)<=r-1`, then its nonneighbourhood in `R` would have size at least

`(5r+1)-1-(r-1)=4r+1`.

That nonneighbourhood has independence number at most 4, because an independent 5-set there together with `u` would be an independent 6-set in `R`. It inherits the clique and density caps, contradicting no-extraction. Therefore

> `delta(R)>=r`.

Status: **PROVED_SYMBOLIC**.

## 5. What is deliberately NOT in the definition

The following r=12 properties are not promoted:

- `delta(R)<=r+1`;
- a two-row `delta in {r,r+1}` terminal;
- `z=0` or `N[v]=K_r`;
- outer charge `sigma+z+g+x+y<=r-1`;
- fixed q-windows such as q30/q31;
- five-template, common-`K_(r-1)`, or shell-correction patterns from the E397--E408 closure.

Those require additional equality/small-slack input and are not consequences of the general anchored stop.

## 6. Terminal theorem still sought

The desired callable interface is

> `failure of legal (4r+1) extraction => anchored T_r^*`,

followed by

> `T_r^* => contradiction`.

The first implication is **OPEN**. This workstream focuses on the second.
