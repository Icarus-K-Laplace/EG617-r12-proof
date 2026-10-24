# General-r 5r+1 All-Large-r Anchor Extraction

Status: **PROVED_RELATIVE_TO_CLASSICAL_ANDRASFAI_ERDOS_SOS**, conditional on the contextual 5r+1 terminal contract and contextual full-color cap already proved in this workstream.

## 1. Terminal setup

Let `F` be a contextual target-color residual on

`n=5r+1`

vertices arising from the original balanced `r`-coloring. Assume

- `alpha(F)<=5`;
- `omega(F)<=r-1`;
- the contextual full-color cap

  `e(F) <= U_(5,r)=(5r^2+7r+18)/2`;

- `delta(F) in {r,r+1}`.

The cap gives the total excess over degree r

`K_r(F)=sum_v(d_F(v)-r)=2e(F)-r(5r+1) <= 6r+18`.

We prove that for every `r>=210`, F contains a direct near-anchor independent triple.

---

## 2. The delta=r+1 branch

Assume `delta(F)=r+1` and choose a degree-(r+1) vertex a.

If there is no independent triple

`{a,u,v}`

with

`d_F(u),d_F(v)<=r+2`,

then among the `4r-1` non-neighbours of a, the vertices of degree at most `r+2` form a clique. Since `omega(F)<=r-1`, there are at most `r-1` such vertices. Hence at least

`(4r-1)-(r-1)=3r`

non-neighbours have degree at least `r+3`, i.e. excess at least2 over the minimum degree `r+1`.

But the total excess over `r+1` is

`2e(F)-(r+1)(5r+1) <= r+17`.

For every `r>=5`, `6r>r+17`, contradiction.

Therefore for every `r>=5`, the delta=r+1 branch contains an independent triple of degree pattern

> **`(r+1, <=r+2, <=r+2)`.**

---

## 3. Constant-defect reduction in the delta=r branch

Assume now `delta(F)=r` and choose a degree-r vertex a. Put

`Z=V(F)\N_F[a]`,

so `|Z|=4r`.

Suppose there is no independent triple

`{a,u,v}`

with

`d_F(u),d_F(v)<=r+1`.

Let

`L={z in Z : d_F(z)<=r+1}`

and `H=Z\L`.

Then L is a clique: otherwise two nonadjacent points of L together with a form the forbidden independent triple. Since `omega(F)<=r-1`, write

`|L|=r-1-s`,

with `s>=0`. Hence

`|H|=3r+1+s`.

Every point of H has degree at least `r+2`, so

`K_r(F)>=2|H|=6r+2+2s`.

Together with `K_r(F)<=6r+18`, this yields

> **`0<=s<=8`.**

Moreover, after charging the baseline excess2 to each H-vertex, all remaining excess in the whole graph is at most

`16-2s`.

Therefore every h in H satisfies

`d_F(h)-r <= 2+(16-2s) <=18`,

while every l in L has `d_F(l)<=r+1`. Consequently

> **every z in Z satisfies `d_F(z)<=r+18`.**

---

## 4. Complement minimum degree

Let

`J=bar(F[Z])`.

Because a is nonadjacent in F to every point of Z, an independent5-set in F[Z] together with a would give an independent6-set in F, contradicting `alpha(F)<=5`. Thus

> **J is K5-free.**

For every z in Z,

`d_J(z)=4r-1-d_(F[Z])(z)`

and `d_(F[Z])(z)<=d_F(z)<=r+18`. Hence

> **`delta(J)>=3r-19`.**

---

## 5. Apply Andrasfai-Erdos-Sos

The classical Andrasfai-Erdos-Sos theorem states that every K_(ell+1)-free graph G on n vertices satisfying

`delta(G) > ((3ell-4)/(3ell-1)) n`

is ell-partite.

Take `ell=4` and `n=4r`. Then the threshold is

`(8/11)4r=32r/11`.

For

`r>=210`,

we have

`3r-19 > 32r/11`.

Therefore J is 4-partite.

Each part of a 4-partition of J is an independent set in J, hence a clique in F[Z]. Since `omega(F)<=r-1`, each part has size at most `r-1`. Four parts therefore cover at most

`4(r-1)=4r-4`

vertices, contradicting `|Z|=4r`.

Thus the assumption of no near-anchor triple is impossible.

Hence for every `r>=210`, the delta=r branch contains an independent triple of degree pattern

> **`(r, <=r+1, <=r+1)`.**

---

## 6. Combined theorem

> **5r+1 All-Large-r Direct Anchor Extraction Theorem.**
>
> Under the contextual terminal contract above, for every `r>=210`, every 5r+1 terminal contains a direct near-anchor independent triple. More precisely:
>
> - if `delta(F)=r`, there is an independent triple of degrees `(r,<=r+1,<=r+1)`;
> - if `delta(F)=r+1`, there is an independent triple of degrees `(r+1,<=r+2,<=r+2)`.

This closes the structural extraction problem inside the 5r+1 terminal for all sufficiently large r. The remaining obligation is no longer a growing terminal case tree: it is a uniform near-anchor excess / incompatibility theorem.

## 7. Logical boundary

This theorem does **not** by itself prove Erdős Problem 617 for all large r. It still depends on:

1. an upstream theorem forcing every hypothetical counterexample into the contextual 4r+1 or 5r+1 alternatives;
2. the contextual full-color cap for the 5r+1 terminal;
3. the inherited clique bound `omega(F)<=r-1`;
4. a downstream theorem turning the extracted near-anchor triple into contradiction.

The 4r+1 alternative is already impossible for r>=5 by the contextual cap theorem in this workstream. Hence, once the upstream extraction theorem is available, the only large-r downstream gap is the uniform near-anchor contradiction.