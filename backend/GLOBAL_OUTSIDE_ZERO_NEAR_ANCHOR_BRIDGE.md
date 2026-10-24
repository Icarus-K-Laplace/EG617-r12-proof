# Global Outside-Zero to Near-Anchor Bridge

Status: **PROVED_ANALYTIC** under the common-S row-closure and all-pivot minimum-degree contract.

This theorem converts a zero common-S charge witness into an exact minimum-degree anchor after owner repivot.  Combined with the independent-triple h<=3 theorem, it removes a large part of the remaining d2/d3 shallow-loss bridge.

---

## 1. Setup

Use a common-S regular owner system in one 35-point core H.

Let

- S be the common shell missing set;
- y be an owner with support D_y;
- `w_v=kappa_v+e_F(v,S)` be the common-S core charge;
- `sigma_s` be the transport slack on s in S;
- a be the exact ambient allowance.

Recall

`a=e_M(S)+sum_(s in S)sigma_s`.

Assume there exists a core vertex

`z notin D_y`

with

> **`w_z=0`.**                                             (OZ1)

---

## 2. A zero-charge witness remains an exact degree-12 vertex

Since both terms in `w_z=kappa_z+e_F(z,S)` are nonnegative, (OZ1) gives

- `kappa_z=0`;
- `e_F(z,S)=0`.

Thus z has degree12 in the old core and is target-nonadjacent to every point of S.

Row closure for y gives

`e_H(z,D_y)<=w_z=0`,

so

`e_H(z,D_y)=0`.

After repivoting y, z remains in the core, loses no old-core neighbour and gains no neighbour from S. Therefore

> **`d_(H_y)(z)=12`.**                                    (OZ2)

So every zero common-S charge witness outside the active support becomes a transported degree-12 anchor.

---

## 3. Missing edge in S creates an independent near-anchor triple

Let `u,v in S` form a target missing edge, i.e. `uv in M[S]`.

Because z is anticomplete to S, the three vertices

`{u,v,z}`

are pairwise target-nonadjacent in H_y.

The anchor-transport identity gives

`d_(H_y)(u)-12 <= sigma_u`,

`d_(H_y)(v)-12 <= sigma_v`.

Together with (OZ2), the total degree excess of this independent triple is at most

`sigma_u+sigma_v`
`<=sum_(s in S)sigma_s`
`=a-e_M(S)`.                                               (OZ3)

Therefore if

> **`a-e_M(S)<=3`,**                                      (OZ4)

then H_y contains an independent triple of total excess at most3.

Apply `GLOBAL_INDEPENDENT_TRIPLE_H3_THEOREM.md`:

`K(H_y)>=8`,

hence

> **`q_y<=E-305`.**                                      (OZ5)

This proves the bridge.

---

## 4. Uniform theorem

> **Outside-Zero Near-Anchor Theorem.**
>
> In a common-S d2/d3 owner system, suppose an owner y has a zero-charge core vertex z outside D_y.  If M[S] contains a target missing edge and
>
> `a-e_M(S)<=3`,
>
> then the owner-repivot core H_y lies in the strengthened near-anchor branch and satisfies
>
> `q_y<=E-305`.

No support-multiplicity classification is used.

---

## 5. d2 consequence

Let `d=2` and suppose the common pair S is internally a target nonedge, so

`e_M(S)=1`.

Then every owner with a zero-charge witness outside its support and allowance

> **`a<=4`**

satisfies `q_y<=E-305`.

Thus repeated-pair shallow-loss states through allowance four are automatically absorbed by the near-anchor envelope whenever the existing zero-concentration machinery supplies an outside zero.

---

## 6. d3 consequences

For d3, if M[S] is not empty:

- if `e_M(S)=1`, allowance `a<=4` is absorbed;
- if `e_M(S)=2`, allowance `a<=5` is absorbed;
- if `e_M(S)=3`, the separate missing-triangle theorem is stronger and absorbs `a<=6` without needing an outside-zero witness.

Hence much of the non-triangular d3 shallow-loss frontier is also reduced to the zero-concentration question.

---

## 7. Remaining structural obstruction

After this bridge, a low-support shallow-loss state can avoid the strengthened envelope only by one of the following mechanisms:

1. M[S] has no internal missing edge;
2. no zero-charge vertex is available outside the active support;
3. the positive transport slack exceeds three after subtracting `e_M(S)`.

These are charge/concentration obstructions, not new support-overlap geometries.

The natural next theorem is therefore a parameterized zero-concentration result at the relevant allowances, rather than a renewed d2/d3 multiplicity case tree.