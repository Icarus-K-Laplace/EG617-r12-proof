# Outer-ray invariant behind the fixed-r recurrence

Status: `PROVED_SYMBOLIC` under the explicit anchor/block-extraction hypotheses below.

## Setup

Let `G` be the least-color graph of a hypothetical r-color counterexample on `r^2+1` vertices, so

`e(G)<=E0:=r(r^2+1)/2`.

Choose a **minimum-degree** anchor `x` with

`d_G(x)=d<=r-1`.

Put the anchor defect

`s:=r-d`.

The minimum-degree pivot identity gives

`e(G)=C(d+1,2)+q+e(G-N[x])`, with `q>=0`.

Consequently the initial non-neighborhood residual has edge budget

`e(G-N[x])<=E0-C(d+1,2)`.

Suppose we then extract `j` vertex-disjoint target-color `K_r` blocks from the current residual. Removing one such block deletes at least its `C(r,2)` internal edges, so after `j` blocks the remaining induced residual `R_j` obeys

`e(R_j)<=B_r(d,j):=E0-C(d+1,2)-j C(r,2)`.

Because each extracted `K_r` reduces the independence cap by one,

`alpha(R_j)<=a:=r-1-j`.

Its order is

`n:=|R_j|=r^2-d-jr`.

## Theorem 1: affine outer-ray invariant

With `a=r-1-j` and `s=r-d`,

> `n=ar+s`.

Equivalently,

> `Theta:=n-r a=s=r-d`.

Thus a legal block extraction

`(n,a) -> (n-r,a-1)`

preserves `Theta` exactly.

### Proof

Substitute `d=r-s` and `j=r-1-a`:

`n=r^2-(r-s)-(r-1-a)r=ar+s`.

Nothing else is used.

### Interpretation

The r=12 outer stopping table is not fundamentally a two-dimensional cloud of `(n,a)` states. It is a union of affine rays indexed by the single anchor-defect parameter `s`.

In particular the critical ray is `s=1`, i.e. `d=r-1`.

Status: `PROVED_SYMBOLIC`, independent of r.

## Corollary 2: 4r+1 and 5r+1 are consecutive critical-ray stops

On `s=1`:

- `a=5` gives `n=5r+1`;
- `a=4` gives `n=4r+1`.

Equivalently:

- after `j=r-6` blocks one reaches the `5r+1` residual;
- after `j=r-5` blocks one reaches the `4r+1` residual.

Hence the r=12 values 61 and 49 are forced by the same all-r affine geometry; they are not numerical coincidences of the 1752-node certificate.

Status: `PROVED_SYMBOLIC`.

## Theorem 3: exact critical-ray edge slack

On `s=1` (so `d=r-1`) the residual budget is

`B_r(r-1,r-1-a)= r((a+1)r-a+1)/2`.

The generic Turan lower floor for a graph on `ar+1` vertices with independence number at most `a` is

`p_a(ar+1)=a C(r,2)+r`.

Therefore

> `B_r(r-1,r-1-a)-p_a(ar+1)=C(r,2)`

for every admissible `a`.

### Proof

Direct substitution gives

`B_r = r((a+1)r-a+1)/2`

and

`p_a(ar+1)=ar(r-1)/2+r`.

Subtracting leaves `r(r-1)/2`.

Status: `PROVED_SYMBOLIC`, independent of r.

## Corollary 4: exact top budget of a 5r+1 terminal

For `a=5`,

`p_5(5r+1)=5 C(r,2)+r`.

Adding the invariant slack `C(r,2)` gives

> `e(R)<=3r^2-2r`

on the critical `5r+1` ray.

At `r=12` this is 408, exactly the top budget in the certified T61 terminal.

Similarly the `4r+1` critical-ray budget is

`B_4= (5r^2-3r)/2`.

At `r=12` this is 342, exactly the outer stopping-table budget at `(d,j,a,n)=(11,7,4,49)`.

Status: `PROVED_SYMBOLIC`.

## What this replaces, and what it does not

This invariant replaces the *outer-coordinate bookkeeping* of the fixed-r recurrence. It does **not** yet prove that every noncritical ray `s>=2` dies, nor that the `s=1` ray must pass through `a=5` and then extract to `a=4`.

The remaining recurrence-elimination problem can now be stated cleanly:

> **Ray elimination target.** Prove analytically that all `s>=2` rays are incompatible with the hereditary least-color cap before they can become terminals, while the critical `s=1` ray either extracts from `5r+1` to `4r+1` or satisfies a bounded symbolic `5r+1` terminal contract.

This is the correct general-r substitute for saying “parameterize 1752 nodes.”