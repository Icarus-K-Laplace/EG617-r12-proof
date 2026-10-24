# General-r 5r+1 All-Large-r Anchor Extraction

Status: **PROVED_RELATIVE_TO_LIU_REN_WANG_2025**; a purely classical Andrásfai–Erdős–Sós fallback gives the weaker threshold `r>=71`.

Conditional inputs:

- the contextual `5r+1` terminal contract;
- the contextual full-color cap

  `e(F) <= U_(5,r)=(5r^2+7r+18)/2`;

- `alpha(F)<=5`, `omega(F)<=r-1`;
- `delta(F) in {r,r+1}`.

## 1. Degree-r+1 branch

If `delta(F)=r+1`, choose a degree-(r+1) vertex a.

If no independent triple `{a,u,v}` has

`d_F(u),d_F(v)<=r+2`,

then the at-most-(r+2) vertices in the `4r-1` non-neighbours of a form a clique, hence there are at most `r-1` of them. Therefore at least `3r` non-neighbours have excess at least2 above `r+1`.

But

`2e(F)-(r+1)(5r+1)<=r+17`,

while `3r` vertices of excess at least2 require at least `6r` excess. Contradiction for every `r>=5`.

Hence the `delta=r+1` branch contains an independent triple of degrees

> **`(r+1,<=r+2,<=r+2)`.**

## 2. Constant-defect reduction in the degree-r branch

Assume `delta(F)=r` and choose a degree-r vertex a. Let

`Z=V(F)\N_F[a]`,

so `|Z|=4r`.

Assume no independent triple `{a,u,v}` satisfies

`d_F(u),d_F(v)<=r+1`.

Define

`L={z in Z:d_F(z)<=r+1}`

and `H=Z\L`.

Then L is a clique. Since `omega(F)<=r-1`, write

`|L|=r-1-s`,

with `s>=0`. Hence

`|H|=3r+1+s`.

The contextual cap gives total excess over r

`K_r(F)=2e(F)-r(5r+1)<=6r+18`.

Every h in H has excess at least2, so

`6r+2+2s<=K_r(F)<=6r+18`,

and therefore

> **`0<=s<=8`.**

For h in H define

`lambda_h=d_F(h)-(r+2)>=0`.

After charging the baseline2 to H,

> **`sum_(h in H) lambda_h <=16-2s`.**

## 3. Delete only lambda>=3 exceptions

Let

`E={h in H:lambda_h>=3}`

and `t=|E|`. Then

> **`t<=5`.**

Put

`Z'=Z\E`,

so `|Z'|=4r-t`.

Every z in Z' has target degree at most `r+4`.

Let

`J'=bar(F[Z'])`.

Since a is target-nonadjacent to all of Z and `alpha(F)<=5`, the full complement `bar(F[Z])` is K5-free; hence J' is K5-free.

Also

> **`delta(J')>=3r-t-5`.**

## 4. 2025 degree-sensitive AES sharpening

Liu–Ren–Wang prove the following strengthening of the Andrásfai–Erdős–Sós theorem for K5-free graphs:

if G has order n, minimum degree delta and maximum degree Delta, then G is 4-partite whenever

`delta > min{ (4/5)n-Delta/10, n-(Delta+1)/3 }`.

The maximum, over all possible Delta, of the right-hand minimum occurs where the two expressions are equal. Solving gives

`Delta=(6n-10)/7`

and common value

> **`(5n+1)/7`.**

Therefore the following Delta-free corollary is immediate:

> **Every K5-free graph G with `delta(G)>(5|G|+1)/7` is 4-partite.**

Apply this to J'. We need

`3r-t-5 > [5(4r-t)+1]/7`,

which is equivalent to

> **`r>2t+36`.**

Since `t<=5`, every

> **`r>=47`**

forces J' to be 4-partite.

For comparison, the classical AES threshold `8|J'|/11` gives `r>=71`.

## 5. Capacity immediately kills t<=3

Every part of a 4-partition of J' is a clique in F, hence has size at most `r-1`.

If `t<=3`, four parts cover at most `4r-4` vertices, but

`|Z'|=4r-t>=4r-3`.

Contradiction.

Only `t=4,5` remain.

## 6. Endpoint t=4

Now `|Z'|=4r-4`, so all four parts have size exactly `r-1`.

The complete 4-partite cross-degree is `3r-3`, whereas

`delta(J')>=3r-9`.

Thus each J'-vertex misses at most6 possible cross-edges.

Fix e in E. The other three exceptional vertices consume at least9 lambda-units, so

`lambda_e<=7`,

hence

`d_F(e)<=r+9`.

Therefore e has at least

`3r-13`

J-neighbours in Z'. Let their intersections with the four parts be `N_1,...,N_4`.

No `N_i` is empty, because otherwise e is target-adjacent to an entire target `K_(r-1)`, producing a forbidden target `K_r`.

For `r>=29`, the total lower bound `sum|N_i|>=3r-13`, together with the fact that each previously chosen J'-vertex forbids at most6 candidates in each later part, gives a greedy K4 transversal through `N_1,...,N_4`.

Together with e this is a K5 in `bar(F[Z])`, contradiction.

Thus t=4 is impossible throughout the relevant range `r>=47`.

## 7. Endpoint t=5

Five exceptional vertices consume at least15 defect units, so the budget `16-2s` forces

> **`s=0`.**

Each exceptional e then satisfies

`lambda_e<=4`,

hence

`d_F(e)<=r+6`.

Since `|Z'|=4r-5`, the four part sizes must be

> **`(r-2,r-1,r-1,r-1)`.**

Call the unique small part `P_0`.

Now

`delta(J')>=3r-10`,

so each J'-vertex misses at most7 possible cross-edges.

Each exceptional e has at least

`3r-11`

J-neighbours in Z'.

If e has at least one J-neighbour in every part, then for `r>=32` a greedy transversal produces a K4 in J' all adjacent to e, yielding a forbidden K5 in `bar(F[Z])`.

Therefore every exceptional e has no J-neighbour in one part.

It cannot be one of the three `(r-1)`-parts, because then e is target-adjacent to a target `K_(r-1)` and forms K_r. Hence every exceptional e has no J-neighbour in the same small part `P_0`.

Equivalently, every exceptional vertex is target-adjacent to all of the target clique `P_0` of size `r-2`.

If two exceptional vertices were target-adjacent, together with `P_0` they would form a target K_r. Thus the five exceptional vertices are pairwise target-nonadjacent.

The original anchor a is target-nonadjacent to all of Z, hence to all five exceptional vertices. Therefore

`{a} union E`

is an independent6-set, contradicting `alpha(F)<=5`.

Thus t=5 is impossible.

## 8. Final theorem

> **5r+1 All-Large-r Direct Anchor Extraction Theorem.**
>
> Under the contextual terminal contract, for every `r>=47`, every `5r+1` terminal contains a direct near-anchor independent triple.
>
> - if `delta(F)=r`, there is an independent triple of degrees `(r,<=r+1,<=r+1)`;
> - if `delta(F)=r+1`, there is an independent triple of degrees `(r+1,<=r+2,<=r+2)`.

Thus the structural extraction problem inside the `5r+1` terminal is closed for all `r>=47` relative to Liu–Ren–Wang 2025.

Using only the classical Andrásfai–Erdős–Sós theorem, the same proof gives `r>=71`.

## 9. Logical boundary

This theorem does not yet prove Erdős Problem 617 for all large r. It still needs:

1. an upstream theorem forcing every hypothetical counterexample into the contextual `4r+1 / 5r+1` alternatives;
2. a downstream theorem converting the extracted near-anchor triple into contradiction.

The contextual `4r+1` branch is already impossible for `r>=5`. Hence, after upstream extraction, the only large-r downstream obstruction is the uniform near-anchor incompatibility theorem.