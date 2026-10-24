# General-r `(k,s)` contextual-cap plane for anchor/block residuals

Status: **PROVED_RELATIVE_TO_BROUWER SECOND-TURAN** in the stated near-anchor range `1<=s<k`.

This file gives a symbolic replacement for a substantial part of the outer contextual recurrence.

## 1. Reparameterize the anchor/block state

Let G be the least target color in a hypothetical balanced r-coloring of `K_(r^2+1)`.

Choose a minimum-degree anchor v of target degree d and, inside its target nonneighbourhood, an inclusion-maximal packing of j genuine target K_r blocks.

Set

> `s=r-d`,
>
> `k=r-1-j`.

Then the residual R has order

`|R|=r^2-d-jr`

`=r^2-(r-s)-(r-1-k)r`

> **`=kr+s`.**

The standard greedy representative argument gives

> **`alpha(R)<=k`.**

Maximality of the K_r packing gives

> **`omega(R)<=r-1`.**

Thus every outer recurrence state may be viewed as a point `(k,s)` rather than as the raw pair `(d,j)`.

The two r=12 historical stops become

- `(k,s)=(4,1)` -> `4r+1`;
- `(k,s)=(5,1)` -> `5r+1`.

## 2. Contextual lower bound for every non-target color

Assume

`1<=s<k`.

On the same residual vertex set, each non-target color C satisfies

- `alpha(C)<=r` by the balanced condition;
- `omega(C)<=k`, because a C-clique of size `k+1` would be a target-independent `(k+1)`-set.

The residual order is

`n=kr+s>kr`.

If `bar(C)` were r-partite, its r independent parts would be C-cliques of size at most k, covering at most kr vertices, contradiction. Hence `bar(C)` is a non-r-partite K_(r+1)-free graph.

Brouwer's exact second-Turan theorem therefore gives

`e(C)>=p_r(n)+floor(n/r)-1`.

Since `n=kr+s` with `s<r` and here `s<k<=r-1`,

`floor(n/r)=k`.

Also

`p_r(kr+s)=r*C(k,2)+ks`.

Therefore every non-target color has at least

> **`r*C(k,2)+ks+k-1`**

edges on R.

## 3. Exact contextual target cap

The r colors partition all `C(n,2)` pairs. Thus the target residual obeys

> **`e(R)<=U_(k,s)(r)`**, where
>
> `U_(k,s)(r)=C(kr+s,2)`
>
> ` -(r-1)[r*C(k,2)+ks+k-1]`.

Expanded,

`U_(k,s)(r)`

`=[k^2 r + k r^2 -4kr +2ks +2k +2r +s^2-s-2]/2`.

## 4. Exact gap above the target alpha-floor

Since `alpha(R)<=k` and `n=kr+s` with `s<k`, the ordinary target floor is

`p_k(n)=k*C(r,2)+rs`.

Subtracting gives the exact contextual slack

> **`Delta_(k,s)(r)=U_(k,s)(r)-p_k(kr+s)`**
>
> `= r[C(k-1,2)-s] + k(s+1)+C(s,2)-1.`

This number is the entire edge room available between the target independence floor and the full-color compatibility cap.

In particular, if

`s>C(k-1,2)`,

the coefficient of r is negative. Therefore for every fixed `(k,s)` in this range, all sufficiently large r have

`Delta_(k,s)(r)<0`,

so the residual is impossible before any shell/core analysis.

This is a symbolic asymptotic pruning rule for the contextual recurrence.

## 5. Add a minimum-degree `r+1` contract

If an outer recurrence theorem additionally proves

`delta(R)>=r+1`,

then

`e(R)>=(kr+s)(r+1)/2`.

Subtracting the contextual upper cap gives

> **`Gamma_(k,s)(r)`**
>
> `=(kr+s)(r+1)/2-U_(k,s)(r)`
>
> `=[r(-k^2+5k+s-2)-2ks-2k-s^2+2s+2]/2`.

Whenever `Gamma_(k,s)(r)>0`, that `(k,s)` residual is impossible.

## 6. Why 4r+1 dies and 5r+1 survives

Take `s=1`.

### k=4

`Gamma_(4,1)(r)=(3r-13)/2`.

Hence for every `r>=5`, a contextual `(4r+1)` residual with minimum degree at least `r+1` is impossible.

### k=5

`Gamma_(5,1)(r)=-(r+17)/2`.

Thus the same minimum-degree contract does not contradict the contextual cap at `5r+1`.

This explains structurally why the historical r=12 `49/61` dichotomy has the roles it does:

- `49=4r+1` lies on the automatically forbidden side of the contextual cap;
- `61=5r+1` is the first genuine terminal not killed by the same degree lower bound.

## 7. Research consequence

The general front recurrence should be organized on the `(k,s)` plane.

The proof obligations become:

1. force `(k,s)` into a bounded region using the exact contextual slack `Delta_(k,s)`;
2. derive minimum-degree information and apply `Gamma_(k,s)`;
3. reserve explicit terminal analysis only for the small surviving cells, beginning with `(5,1)`.

This is a direct symbolic alternative to replaying the fixed-r 1752-node recurrence state by state.
