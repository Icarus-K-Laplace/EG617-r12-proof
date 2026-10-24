# General-r 5r+1 All-Large-r Anchor Extraction

Status: **PROVED_RELATIVE_TO_CLASSICAL_ANDRASFAI_ERDOS_SOS**, conditional on the contextual `5r+1` terminal contract and the contextual full-color cap already proved in this workstream.

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

We prove that for every `r>=71`, F contains a direct near-anchor independent triple.

---

## 2. The delta=r+1 branch

Assume `delta(F)=r+1` and choose a degree-(r+1) vertex a.

If there is no independent triple `{a,u,v}` with

`d_F(u),d_F(v)<=r+2`,

then among the `4r-1` non-neighbours of a, the vertices of degree at most `r+2` form a clique. Since `omega(F)<=r-1`, there are at most `r-1` such vertices. Hence at least `3r` non-neighbours have degree at least `r+3`, i.e. excess at least2 over the minimum degree `r+1`.

But the total excess over `r+1` is

`2e(F)-(r+1)(5r+1) <= r+17`.

For every `r>=5`, `6r>r+17`, contradiction.

Therefore for every `r>=5`, the `delta=r+1` branch contains an independent triple of degree pattern

> **`(r+1, <=r+2, <=r+2)`.**

---

## 3. Constant-defect reduction in the delta=r branch

Assume now `delta(F)=r` and choose a degree-r vertex a. Put

`Z=V(F)\N_F[a]`,

so `|Z|=4r`.

Suppose there is no independent triple `{a,u,v}` with

`d_F(u),d_F(v)<=r+1`.

Let

`L={z in Z : d_F(z)<=r+1}`

and `H=Z\L`.

Then L is a clique. Since `omega(F)<=r-1`, write

`|L|=r-1-s`,

with `s>=0`. Hence

`|H|=3r+1+s`.

Every point of H has degree at least `r+2`, so

`K_r(F)>=2|H|=6r+2+2s`.

Together with `K_r(F)<=6r+18`, this yields

> **`0<=s<=8`.**

Define for h in H

`lambda_h=d_F(h)-(r+2)>=0`.

After charging the baseline excess2 to every H-vertex, the remaining excess ledger gives

> **`sum_(h in H) lambda_h <=16-2s`.**

This is the constant-defect core of the proof.

---

## 4. Delete only high lambda-exceptions

Let

`E={h in H : lambda_h>=3}`

and put `t=|E|`. Since each point of E consumes at least3 units of the at-most16 defect budget,

> **`t<=5`.**

Set

`Z'=Z\E`,

so `|Z'|=4r-t`.

Every point of `Z'` has target degree at most `r+4`:

- points of L have degree at most `r+1`;
- points of `H\E` have `lambda_h<=2`, hence degree at most `r+4`.

Let

`J'=bar(F[Z'])`.

Because a is target-nonadjacent to all of Z and `alpha(F)<=5`, the full complement `bar(F[Z])` is K5-free; therefore J' is K5-free.

For every z in Z',

`d_(J')(z)>=|Z'|-1-d_F(z)`

and hence

> **`delta(J')>=3r-t-5`.**

---

## 5. AES forces J' to be 4-partite for r>=71

The classical Andrasfai-Erdos-Sos theorem states that a K_(ell+1)-free graph G on n vertices with

`delta(G) > ((3ell-4)/(3ell-1)) n`

is ell-partite.

Take `ell=4`. For J' the condition is

`3r-t-5 > (8/11)(4r-t)`.

This is equivalent to

> **`r>3t+55`.**

Since `t<=5`, every `r>=71` satisfies the condition. Thus for `r>=71`, J' is 4-partite.

Each part of a 4-partition of J' is a clique in F and therefore has size at most `r-1`.

If `t<=3`, four parts can cover at most `4r-4` vertices, while

`|Z'|=4r-t>=4r-3`,

impossible.

Thus only `t=4` and `t=5` require analysis.

---

## 6. The t=4 endpoint is impossible

If `t=4`, then `|Z'|=4r-4`. Since J' is 4-partite and every part has size at most `r-1`, all four parts have size exactly `r-1`.

Also every vertex of J' has at most6 missing cross-edges, because the complete 4-partite graph on four `(r-1)`-parts has cross-degree `3r-3`, whereas

`delta(J')>=3r-9`.

Fix an exceptional vertex e in E. The other three exceptional vertices consume at least9 lambda-units, so

`lambda_e<=16-9=7`.

Hence

`d_F(e)<=r+9`.

Therefore e has at least

`(4r-4)-(r+9)=3r-13`

J-neighbours in Z'. Let their intersections with the four parts be `N_1,...,N_4`.

No `N_i` is empty: otherwise e is target-adjacent to an entire `(r-1)`-clique, creating a target `K_r`, contrary to `omega(F)<=r-1`.

Order the four sizes increasingly. For `r>=29`, the total lower bound `sum|N_i|>=3r-13` implies

- the second size is at least7;
- the third size is at least13;
- the fourth size is at least19.

Since every chosen J'-vertex forbids at most6 vertices in each later part, a greedy choice produces one point from each `N_i` spanning a `K_4` in J'. Together with e this gives a `K_5` in `bar(F[Z])`, contradiction.

Thus `t=4` is impossible for the range `r>=71` relevant here.

---

## 7. The t=5 endpoint is impossible

Assume `t=5`. Since five exceptional vertices already consume at least15 units while the defect budget is at most `16-2s`, necessarily

> **`s=0`.**

Moreover each exceptional vertex satisfies `lambda_e<=4`, because the other four consume at least12 units. Thus

> **`d_F(e)<=r+6` for every e in E.**

Now `|Z'|=4r-5`. Four parts of size at most `r-1` covering Z' must have sizes

> **`(r-2,r-1,r-1,r-1)`.**

Call the unique small part `P_0`.

The minimum-degree bound gives

`delta(J')>=3r-10`.

Hence every J'-vertex misses at most7 possible cross-edges.

Fix e in E. Since `d_F(e)<=r+6`, e has at least

`(4r-5)-(r+6)=3r-11`

J-neighbours in Z'.

If e has a J-neighbour in every one of the four parts, then for `r>=32` the same greedy transversal argument (now allowing at most7 forbidden vertices per previous choice) produces a `K_4` in J' all adjacent to e, giving a forbidden K5 in `bar(F[Z])`.

Therefore every e in E has no J-neighbour in at least one part.

It cannot miss all J-neighbours in any of the three `(r-1)`-parts, because then e is target-adjacent to an entire target `K_(r-1)`, again producing a target `K_r`.

Thus for every e in E the unique part with no J-neighbour is `P_0`. Equivalently,

> **every exceptional vertex is target-adjacent to every vertex of the target clique P_0 of size r-2.**

If two exceptional vertices e,f were target-adjacent, then

`P_0 union {e,f}`

would be a target `K_r`, impossible. Therefore the five exceptional vertices form a target-independent set.

But the original degree-r anchor a is target-nonadjacent to all of Z, hence to all five exceptional vertices. Thus

`{a} union E`

is an independent6-set, contradicting `alpha(F)<=5`.

Therefore `t=5` is impossible.

---

## 8. Combined theorem with threshold 71

We have eliminated every no-near-anchor configuration in the `delta=r` branch for `r>=71`. Therefore:

> **5r+1 All-Large-r Direct Anchor Extraction Theorem.**
>
> Under the contextual terminal contract above, for every `r>=71`, every `5r+1` terminal contains a direct near-anchor independent triple. More precisely:
>
> - if `delta(F)=r`, there is an independent triple of degrees `(r,<=r+1,<=r+1)`;
> - if `delta(F)=r+1`, there is an independent triple of degrees `(r+1,<=r+2,<=r+2)`.

Thus the structural extraction problem inside the `5r+1` terminal is completely closed for all `r>=71`.

The remaining large-r downstream obligation is a uniform near-anchor excess / incompatibility theorem, not a growing terminal case tree.

## 9. Logical boundary

This theorem does **not** by itself prove Erdős Problem 617 for all large r. It still depends on:

1. an upstream theorem forcing every hypothetical counterexample into the contextual `4r+1` or `5r+1` alternatives;
2. the contextual full-color cap for the `5r+1` terminal;
3. the inherited clique bound `omega(F)<=r-1`;
4. a downstream theorem turning the extracted near-anchor triple into contradiction.

The `4r+1` alternative is already impossible for `r>=5` by the contextual cap theorem in this workstream. Hence, once the upstream extraction theorem is available, the only large-r downstream gap is the uniform near-anchor contradiction.