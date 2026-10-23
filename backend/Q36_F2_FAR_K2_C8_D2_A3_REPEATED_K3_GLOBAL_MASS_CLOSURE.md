# q36 f=2 far-target-K2 — global closure of the A3 repeated-K3 sector

Status: `PROVED` under `Q36_F2_FAR_K2_C8_D2_A3_MULTIPLICITY_REDUCTION.md`, `Q36_F2_FAR_K2_D2_GLOBAL_REDUCTION.md`, the f=2 master ledger, CORE211, common-S row closure, and `alpha(H)<=3`.

This supersedes the Type-P/Type-Q terminal analysis: no multiplicity-three target-K3 support can occur at all.

## 1. Global w-mass is exactly 37

We are in the far-target-K2 branch with c=8, one d2 row and seven d3 rows in one active missing-set class of allowance A=3.

Let

`S=F union {x}`

where F is the far target-K2 and x is the active decorated shell vertex.

For every core vertex v define

`w_v=kappa_v+e_F(v,S)`.

CORE211 gives

`sum_(v in H) kappa_v = 2`.                                 (1)

Because a d2 row exists, the exact d2 formula forces `a_F=0`. Hence each far regular shell vertex is target-nonadjacent to all eight low-clique vertices and all three decorated shell vertices, while adjacent to the other far vertex. Its shell missing degree is therefore11. Being regular, its core row size is also11.

For the active vertex x, all seven d3 owners miss x, both far vertices miss x, and its missing degree inside X is `nu_x`. Thus

`d_M(x)=9+nu_x`.

The c=8 allowance identity is

`A=nu_x+g_x-1`.

With A=3,

`nu_x+g_x=4`.

The core row size of x is `d_M(x)+g_x`, hence exactly13.

Therefore the total S-to-core incidence is

`e_F(S,H)=11+11+13=35`.                                    (2)

Combining (1)--(2),

> `sum_(v in H) w_v = 37`.                                  (3)

## 2. A repeated K3 forces a disjoint K3 support

Assume D is a multiplicity-three target-K3 support.

Lexicographic q36 maximality gives repeated-support defect

`defect(D)=sum_(d in D) w_d <=2`.                           (4)

The valid A3 multiplicity reduction proves that at least two of the four external owner incidences belong to support classes disjoint from D, and every support disjoint from D is itself a target K3.

Choose one such support E.

Joint row closure from D gives

`e_H(D,E)<=defect(D)<=2`.                                   (5)

Hence the bipartite target-nonedge graph B between D and E is obtained from K3,3 by deleting at most two edges. It still has a perfect matching, so by Konig

> `tau(B)=3`.                                                (6)

## 3. The pure d2 block

Let D0 be the unique d2 support.

The global far-K2 d2 reduction gives:

- D0 is a pure target K2 of globally regular core vertices;
- D0 is disjoint from every d3 support;
- D0 is target-anticomplete to the entire d3-support union U;
- its common missing set is F and its common-S allowance is zero.

In particular D0 is disjoint and target-anticomplete to D and E.   (7)

## 4. Every other core vertex has w>=2

Take

`v in H \ (D0 union D union E)`.

There are two cases.

### Case A: N(v) covers every D--E target nonedge

Then `N_H(v) intersect (D union E)` is a vertex cover of B. By (6),

`e_H(v,D)+e_H(v,E)>=3`.

Common-S row closure against D and E gives

`e_H(v,D)<=w_v`,
`e_H(v,E)<=w_v`.

Since the two nonnegative integer terms sum to at least3, one of them is at least2. Thus

`w_v>=2`.                                                    (8)

### Case B: N(v) does not cover B

Choose a target-nonedge `de` of B with

`vd, ve` both target nonedges.

If v failed to be adjacent to one vertex `u in D0`, then by (7)

`{d,e,v,u}`

would be an independent4-set in H, contradicting `alpha(H)<=3`.

Therefore v is adjacent to both vertices of D0:

`e_H(v,D0)=2`.

Zero-allowance row closure for the pure d2 support D0 gives

`2 <= kappa_v+e_F(v,F) <= w_v`.

Hence again

`w_v>=2`.                                                    (9)

Thus every vertex outside `D0 union D union E` has w-mass at least2.

## 5. Global contradiction

The three sets are disjoint and have sizes

`|D0|=2`, `|D|=3`, `|E|=3`.

Therefore there are

`35-2-3-3=27`

core vertices covered by Section4. Consequently

`sum_(v in H) w_v >= 27*2 =54`,

contradicting the exact global total (3):

`sum_H w_v=37`.

## 6. Conclusion

No multiplicity-three target-K3 support D can exist in the c=8, one-d2, A=3 far-K2 branch.

Therefore the entire repeated-K3 terminal — including all Type-P, Type-Q, single-class and multiclass geometries — is EMPTY.

Combined with `Q36_F2_FAR_K2_C8_D2_A3_ONEEDGE_FULL_CLOSURE.md`, every multiplicity-three support is now eliminated under the correct far-K2 contract.