# Endpoint Classification

All statements are conditional on hypotheses A+B and `r>=12` unless stated otherwise.

## 1. Endpoint collapse

The strengthened ceiling is `q<=3r-1`. Every regular repivot of missing degree `d` has

`q_y>=d(r+1-d)`.

For `4<=d<=r-3`,

`d(r+1-d)>=4(r-3)>3r-1`

for every `r>=12`. Therefore

`d in {0,1,2,3,r-2,r-1,r}`.

The scalable low endpoint is `d<=3`; the high endpoint is `d>=r-2`.

---

## 2. d3 common-S endpoint closes completely

For a d3 common-S family,

`q=3(r-2)+a+B`.

The already-proved equality B-floor shows that `q=3r-1` is impossible: equality at the global charge ceiling forces hereditary edge equality, whereas the regular-clique extraction gives a lower bound `B>=6` for `r>=12`, contradicting `a+B=5`.

Hence

`q<=3r-2`,

so

`a+B<=4`, in particular `a<=4`.

The existing symbolic Bridge-B low-charge machinery absorbs the complete `b=2` sector and the `b=1,a<=4` sector. Therefore no d3 common-S boundary remains.

**Status:** `PROVED_CONDITIONAL` (uses A+B, equality B-floor, and the pre-existing low-charge absorption assets).

---

## 3. High Endpoint Absolute Owner Bound

### Theorem

Let `Y` be the set of all regular shell vertices with missing degree

`d_y>=r-2`.

Then

> **`|Y|<=7`.**

This is a bound on the total high-endpoint population, not merely on a single common-S class.

### Proof

Let `G=F[Y]` be the target graph induced by the high owners.

For `y in Y`, the number of target neighbours of `y` inside the whole shell is

`r-d_y<=2`.

Therefore

`Delta(G)<=2`.                                                    (3.1)

If four vertices `y_1,...,y_4` were pairwise target-nonadjacent, the symbolic zero-gap theorem would give

`D_{y_i} intersect D_{y_j}=empty`

for every `i != j`. Since `|D_{y_i}|=d_{y_i}>=r-2`, the core would contain at least

`4(r-2)`

vertices. But `|H|=3r-1`, and

`4(r-2)>3r-1`

for `r>=8`. Hence

`alpha(G)<=3`.                                                     (3.2)

Because a graph of maximum degree two is 3-colourable,

`alpha(G)>=ceil(|Y|/3)`,

so initially `|Y|<=9`.

We sharpen this.

If no high owner has `d=r-2`, then every high owner has target shell degree at most one, so `Delta(G)<=1`. Hence

`alpha(G)>=ceil(|Y|/2)`.

Together with (3.2), this gives `|Y|<=6`.

It remains to assume that some `y` has `d_y=r-2`.

For this one owner, take the singleton common-S representation. Its shell target-neighbour set

`T_y=A\(S_y union {y})`

has size two. The allowance identity gives

`q=3(r-2)+a_y+B_y`,

with

`a_y=e_M(S_y)+sum_{s in S_y} sigma_s >= e_M(S_y)`.

Since `q<=3r-1`,

`a_y+B_y<=5`,

and hence

> `e_M(S_y)<=5`.                                                   (3.3)

Let

`Z_y=Y\({y} union N_G(y))`.

Every vertex of `Z_y` is target-nonadjacent to `y`, hence lies in `S_y`. Put `k=|Z_y|`. By `Delta(G)<=2`,

`k>=|Y|-3`.

Also `Delta(G[Z_y])<=2`, so

`e_F(Z_y)<=k`.

Thus

`e_M(Z_y)=C(k,2)-e_F(Z_y)>=C(k,2)-k=k(k-3)/2`.

Together with `Z_y subset S_y` and (3.3),

`k(k-3)/2<=5`.

Therefore `k<=5`, and hence `|Y|<=8`.

Suppose for contradiction `|Y|=8`. Then for every `d=r-2` vertex y used above all inequalities are tight:

- `d_G(y)=2`;
- `k=5`;
- `e_F(Z_y)=5`;
- `G[Z_y]` has five vertices, five edges and maximum degree two.

Therefore `G[Z_y]=C_5`. Since every vertex of this C5 already has degree two, the C5 is a connected component of G. The remaining three vertices form another component. Because `alpha(C5)=2` and `alpha(G)<=3`, the remaining component must have independence number one, hence it is `K_3`.

So

`G=C_5 disjoint_union K_3`.

Every vertex of G now has G-degree two. A high owner has at most two target neighbours in the entire shell, therefore every vertex of G must actually have shell target degree exactly two, i.e. every high owner has `d=r-2`.

Pick a vertex z of the C5. Its five non-neighbours in G consist of

- the two C5 vertices at distance two from z, which are adjacent to each other; and
- all three vertices of the K3.

Thus `Z_z` induces exactly `K_2 disjoint_union K_3`, with four target edges. Hence

`e_M(Z_z)=C(5,2)-4=6`.

But `Z_z subset S_z` and (3.3) applied to z gives `e_M(S_z)<=5`, contradiction.

Therefore `|Y|<=7`. QED.

**Status:** `PROVED_CONDITIONAL`.

---

## 4. High Endpoint Fixed-Width Incidence Kernel

### Theorem

Let `Y` be as above. Then the complete incidence of high owners with the shell and with their core support sets admits an r-independent bounded skeleton:

1. `|Y|<=7`;
2. each shell target-neighbour complement `T_y` has `|T_y|=r-d_y<=2`;
3. the union
   `K_A=Y union (union_{y in Y} T_y)`
   has size at most 21;
4. every high-owner target edge to the shell is incident with `K_A`;
5. the core owner-incidence signatures use at most 17 classes.

### Proof of the signature bound

For `v in H`, define

`I(v)={y in Y : v in D_y}`.

If x and y are target-nonadjacent high owners, the zero-gap theorem gives

`D_x intersect D_y=empty`.

Therefore two vertices can occur together in `I(v)` only if they are adjacent in G. Hence every `I(v)` is a clique of G.

Now `|V(G)|<=7` and `Delta(G)<=2`. The nonempty cliques of G consist only of

- singleton vertices: at most 7;
- edges: at most 7;
- triangles: at most `floor(7/3)=2`, because in a maximum-degree-two graph every triangle is a connected component.

Thus there are at most

`7+7+2=16`

nonempty incidence signatures, and at most 17 after adding the empty signature.

This proves a fixed-width interaction kernel. The multiplicities of the signature classes may depend on r; the *number and combinatorial types* of classes do not.

**Status:** `PROVED_CONDITIONAL`.

### Consequence

High-endpoint multi-pivot compatibility can be written as a finite-dimensional integer system indexed by

- a graph G on at most seven vertices with `Delta(G)<=2` and `alpha(G)<=3`;
- shell complements `T_y` of size at most two;
- at most seventeen core incidence-signature multiplicities.

Therefore the high endpoint cannot generate an r-growing case tree. What remains is to eliminate the finite family of kernel types analytically or by an O(1)-sized certificate enumeration.

---

## 5. Surviving endpoint families

After the results above:

- `d=3` common-S: **closed**;
- `d=2`: scalable and still open in general plateau equality/positive-loss form;
- `d=1,0`: not yet frozen in this workstream;
- `d>=r-2`: reduced to a fixed-width kernel with at most seven owners.

No medium degree survives.