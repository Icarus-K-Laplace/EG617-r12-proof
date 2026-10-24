# General-r Cell B High-Layer 22-Defect Ledger

Status: **PROVED_SYMBOLIC** conditional on the Cell B normal form and the contextual `5r+1` cap.

## 1. Setup

Let F be a contextual target terminal on `5r+1` vertices with

`delta(F)=r+1`

and suppose a direct near-anchor triple has common target anti-neighbourhood W in Cell B of the `|W|=2r-1` normal form.

Thus the non-target union on W is

`S(K_(r-1,r-1))`.

Let A,B be the two `(r-1)`-vertex sides and w the subdivision vertex.

Put

`O=V(F)\W`,

so

`|O|=3r+2`.

## 2. Exact target degrees inside W

In the target complement of the subdivided complete bipartite graph:

- every vertex of `A union B` has target degree exactly `r-1` inside W;
- w is target-adjacent to all W vertices except the two endpoints of the subdivided edge, hence

  `d_(F[W])(w)=2r-4`.

Also

`e_F(W)=r^2-r-1`.

## 3. External target incidences

Because the full terminal has minimum degree `r+1`, every side vertex s in `A union B` has at least two target neighbours in O.

Write

> **`d_F(s,O)=2+a_s`, with `a_s>=0`.**

Write

> **`x_w=d_F(w,O)>=0`.**

For every outside vertex `o in O`, define its high-layer excess

> **`kappa_o=d_F(o)-(r+1)>=0`.**

## 4. Total high-layer excess cap

The contextual cap is

`e(F)<=U_(5,r)=(5r^2+7r+18)/2`.

Therefore the total excess above minimum degree `r+1` satisfies

`K^(5)_(r+1)=2e(F)-(r+1)(5r+1)`

`<= [5r^2+7r+18] - [5r^2+6r+1]`

`=r+17`.

## 5. The unavoidable subdivision excess

Inside W alone, the subdivision vertex w already has degree

`2r-4`.

Relative to the terminal minimum `r+1`, this contributes the unavoidable excess

> **`r-5`.**

Every side vertex has internal degree `r-1`; after its two mandatory outside neighbours it reaches exactly `r+1`, with only `a_s` contributing excess.

Thus the full excess decomposes exactly as

`K^(5)_(r+1)`

`=(r-5) + x_w + sum_(s in A union B) a_s + sum_(o in O) kappa_o`.

Combining with the cap `K^(5)_(r+1)<=r+17` gives the constant ledger

> **`x_w + sum_s a_s + sum_o kappa_o <=22`.**

This bound is independent of r.

## 6. Consequences

The single 22-unit budget simultaneously controls three kinds of extension defect:

1. subdivision extension:

   `x_w<=22`;

2. side over-incidence:

   `sum_s a_s<=22`;

3. outside degree excess:

   `sum_o kappa_o<=22`.

Hence all but at most22 vertices of O have exact target degree `r+1`.

Likewise, all but at most22 side vertices have exactly two target neighbours in O, unless fewer vertices carry larger multiplicity.

## 7. Combine with the Cell B color-certificate bound

The Latin / rainbow extension reduction implies a separate pointwise fact for every outside vertex o:

> **`d_F(o,W)<=3`.**

Indeed, in every ordinary non-target color o must either use the unique w-edge as a one-edge certificate or use both endpoints of a factor edge; the exceptional color also requires one certificate. Across all colors this forces at least `2r-4` of the `2r-1` W-edges at o to be non-target.

Therefore every high-layer Cell B extension satisfies simultaneously

- `d_F(o,W)<=3` for every o in O;
- total outside degree excess at most22;
- total side over-incidence at most22;
- subdivision outside degree at most22.

## 8. Strategic consequence

The high Cell B nonextension problem is not an asymptotically growing graph problem.

After the canonical W design is fixed, every deviation from the baseline extension pattern is contained in a **22-unit defect ledger**.

This is suitable for either:

- a finite symbolic classification of defect placements; or
- a uniform switching/repivot argument showing that any nonzero defect creates an illegal color-independent set or target clique.

For r=12 this interfaces directly with the surviving T61 `h=13` branch.