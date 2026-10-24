# General-r Common-S Equality B-Floor

Status: **PROVED_SYMBOLIC**, conditional on the symbolic common-S contract and, for the equality consequence, hereditary-cap equality at order `4r+1`.

## 1. Regular clique extraction from a common-S family

Let a legal pivot p have shell A of size `r+1`. Let a common-S regular-owner family have missing set S of size d, owners Y, and leftover

`L=A\(S union Y)`.

Recall

`B=e_M(L)+G_L`,

where `G_L=sum_(v in L) g_v` and `g_v=d_F(v)-(r+1)>=0`.

The set

`C0={p} union Y union L={p} union (A\S)`

has size

`r+2-d`.

Every owner is regular and target-adjacent to every point of `A\S`. The pivot p is regular and target-adjacent to the whole shell.

Inside L, delete every decorated vertex (`g_v>0`). There are at most `G_L` such vertices. Then choose one endpoint of every missing edge of `M[L]`; this deletes at most `e_M(L)` additional vertices and removes every remaining target nonedge inside L.

The surviving vertices of C0 therefore form a target clique consisting entirely of target-degree-`r+1` vertices. Its size is at least

> **`r+2-d-B`.**

This extraction uses only the definition of B and the common-S owner contract.

## 2. Equality B-floor

Assume additionally that the target residual F on `4r+1` vertices saturates the hereditary cap:

`e(F)=D_r(4r+1)`.

By `GENERAL_R_MULTICOLOR_EQUALITY_CLIQUE_OBSTRUCTION.md`, every target clique consisting of target-degree-`r+1` vertices has size at most

`floor((r-1)/2)`.

Hence every common-S family at hereditary equality satisfies

> **`B >= r+2-d-floor((r-1)/2)`.**

This is an exact multicolor compatibility lower bound on the shell residual B.

## 3. d3 top-q exclusion

Assume the strengthened near-anchor envelope

`q<=3r-1`

and a d3 common-S family (`d=3`). The exact q decomposition is

`q=3(r-2)+a+B`.

Suppose `q=3r-1`. Then

`a+B=5`,

so in particular `B<=5`.

At the strengthened ceiling equality, the symbolic backend identity and the `K_r>=8` core floor force the residual edge count to attain `D_r(4r+1)`. Therefore the equality B-floor applies:

`B >= r-1-floor((r-1)/2)`.

For every `r>=12`, this lower bound is at least6. Contradiction.

Therefore:

> **For every r>=12, every d3 common-S family satisfies `q<=3r-2`.**

Consequently

`3(r-2)+a+B <=3r-2`,

so

> **`a+B<=4`, and in particular `a<=4`.**

Thus the entire d3 top-q / allowance-five frontier disappears, not merely the specific `b=1,a=5` cell.

## 4. Entire d3 sector disappears at hereditary equality

There is a stronger consequence at the maximum residual edge layer itself.

Assume

`e(F)=D_r(4r+1)`

and the strengthened near-anchor core floor `K_r>=8`, hence `q<=3r-1`.

For any d3 common-S family, the equality B-floor gives

`B >= r-1-floor((r-1)/2)`.

For every `r>=12`, the right side is at least6. Since `a>=0`,

`q=3(r-2)+a+B >=3r-6+6=3r`,

contradicting `q<=3r-1`.

Therefore:

> **Maximum-edge d3 exclusion.** For every `r>=12`, under the residual-core contract and the general near-anchor theorem, a hereditary-cap equality residual `e(F)=D_r(4r+1)` contains no regular shell vertex of missing degree3.

A single regular d3 vertex would itself define a one-owner common-S family, so no multiplicity assumption is involved.

This is strictly stronger than excluding the allowance-five boundary. It removes the whole d3 sector from the maximum residual edge layer.

## 5. d2 side consequence

For d=2, `B=0` already creates the target clique

`{p} union (A\S)`

of size r, contradicting the inherited clique cap `omega(F)<=r-1`. Hence every d2 common-S family has

> **`B>=1`.**

Under `q<=3r-1`, this improves the crude allowance ceiling from `a<=r+1` to

> **`a<=r`.**

At hereditary equality the stronger B-floor gives

`B>=r-floor((r-1)/2)`.

This may be useful for later d2 positive-loss equality analysis.

## 6. Strategic consequence

Conditional on the general exact/near-anchor theorem, the scalable d3 common-S sector is confined to `a<=4` in every residual and disappears entirely at the maximum hereditary edge layer. Therefore no d3 higher-slack hierarchy survives asymptotically.
