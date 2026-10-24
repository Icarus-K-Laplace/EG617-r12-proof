# General-r Contextual 5r+1 Terminal Structure

Status: **PROVED_SYMBOLIC** under the original balanced-colouring context and target residual `alpha<=5`. External input: Brouwer exact Turan stability.

## 1. Other-color edge floor

Let R be a set of `5r+1` vertices in the original balanced r-colouring and let F be the target-color graph on R. Assume

`alpha(F)<=5`.

For every other color C_j:

- `alpha(C_j)<=r` by the Problem-617 condition;
- `omega(C_j)<=5`, since a color-j K6 would be an independent6 in F.

The ordinary alpha<=r minimum is

`p_r(5r+1)=10r+5`.

We claim

> **`e(C_j)>=10r+9`.**

If instead `e(C_j)<=p_r(5r+1)+3`, then `J=bar(C_j)` is `K_(r+1)`-free with at least

`ex(5r+1,K_(r+1))-3`

edges.

Brouwer exact stability applies because

`floor((5r+1)/r)=5`,

so the r-partite threshold is exactly `ex-3`. Hence J is r-partite. One part has size at least6, contradicting `alpha(J)=omega(C_j)<=5`.

Therefore `e(C_j)>=10r+9`.

## 2. Contextual target cap

The non-target colors partition the complement of F, so

`e(F)<=C(5r+1,2)-(r-1)(10r+9)`.

Simplification gives

> **`e(F)<=(5r^2+7r+18)/2`.**

For r=12 this is411.

## 3. Minimum-degree collapse

Suppose the extraction theorem supplies

`delta(F)>=r`.

If `delta(F)>=r+2`, then

`e(F)>=ceil((5r+1)(r+2)/2)`.

The raw difference between this lower bound and the contextual upper bound is

`[(5r+1)(r+2) -(5r^2+7r+18)]/2`
`=(4r-16)/2`
`=2r-8`.

This is positive for every `r>=5`.

Therefore:

> **For every r>=5, any contextual 5r+1 residual with delta>=r must have**
>
> **`delta(F) in {r,r+1}`.**

This exactly parameterizes the r=12 T61 two-row minimum-degree interface `h=12 or13`.

## 4. Direct near-anchor forcing in the high row

Assume

`delta(F)=r+1`.

Define total excess over the minimum degree:

`K^(5)=sum_v(d_F(v)-(r+1))`.

The contextual cap gives

`K^(5)=2e(F)-(r+1)(5r+1)`
`    <=r+17`.

For `r>=5`, this is less than `5r+1`, so a degree-(r+1) vertex exists.

Suppose there is no independent triple with degrees

`(r+1, <=r+2, <=r+2)`.

Fix a degree-(r+1) vertex a. Its open antineighbourhood has

`(5r+1)-1-(r+1)=4r-1`

vertices.

The vertices in this antineighbourhood having excess at most1 must form a target clique: two nonadjacent such vertices together with a would give the forbidden triple. Since the target clique number is at most `r-1` in the extracted terminal, at most `r-1` such low-excess vertices exist.

Hence at least

`(4r-1)-(r-1)=3r`

vertices have excess at least2. Therefore

`K^(5)>=6r`.

But

`r+17<6r`

for every `r>=4`. Contradiction.

Thus:

> **High-row direct near-anchor theorem.** For every `r>=5`, a contextual `5r+1` terminal with `delta=r+1` contains an independent triple of degrees
>
> **`(r+1, <=r+2, <=r+2)`.**

## 5. r=12 interpretation

For r=12 the contextual cap is411. The front-end anchor ledger further sharpens the embedded T61 budget to408, but the present theorem already explains structurally why the only possible minimum degrees are12 and13.

In the h13 branch it also forces an independent triple

`(13,<=14,<=14)`

before any shell classification.

This may provide a shorter replacement interface for some of the fixed-r T61 high-row analysis.

## 6. Remaining branch

The minimum-degree-r branch is not closed by the crude contextual excess estimate:

`2e(F)-r(5r+1)<=6r+18`,

while the same one-anchor argument would need a strict bound below approximately `6r+2`.

Thus the general 5r+1 programme has now reduced to:

1. exploit the direct near-anchor triple in the `delta=r+1` branch;
2. gain at least17 units (or use a different structural argument) in the `delta=r` branch.
