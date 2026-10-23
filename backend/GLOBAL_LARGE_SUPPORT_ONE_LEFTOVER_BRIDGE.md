# Global Large-Support One-Leftover Bridge

Status: **PROVED_ANALYTIC**.

This theorem closes an important gap in the forcing-to-master-contract programme.  It shows that a fully-decorated large-support family which is only one owner short of the maximal K4,9 equality state does not create a new high-dimensional shell regime: the unique leftover shell vertex has combined missing-degree/decoration at most two and therefore returns to the low-support / one-spoke part of the global support architecture.

Dependencies:

- the shell identity `q=e(M)+G_A`;
- `GLOBAL_COMMON_S_OWNER_CLIQUE_THEOREM.md`;
- the definition of a common-S regular owner family;
- the legal high-right ceiling `q<=38`.

No E-layer label and no solver are used.

---

## 1. Setup

Let `p` be a pivot whose shell `A` has size 13.  Let `M` be the shell missing graph and let `g_v>=0` be the shell decoration, with

`G_A=sum_(v in A) g_v`.

Let `Y` be a common-S family of regular shell vertices with

- common missing set `S`;
- `d=|S| in {4,9}`;
- every point of S globally decorated, so `g_s>=1` for every `s in S`;
- owner count

  `N=12-d`.

Thus the family is exactly one owner short of the maximum possible count `13-d`.

Let `x` be the unique shell vertex outside `S union Y`:

`A = S disjoint_union Y disjoint_union {x}`.

Assume `q<=38`.

---

## 2. All missing edges incident with owners are forced

For every owner `y in Y`, its shell missing set is exactly S.  Hence:

- y is missing from every point of S;
- y is target-adjacent to every other owner;
- y is target-adjacent to x.

Therefore the missing edges incident with Y are exactly the `dN` edges between Y and S.

Every remaining shell missing edge lies either

- inside S, or
- between x and S.

Put

`R_M = e_M(S) + e_M(x,S)`.

Then

> `e(M)=dN+R_M`.                                      (L1)

Moreover

> `d_M(x)=e_M(x,S)<=R_M`.                              (L2)

---

## 3. Decoration baseline

Because S is fully decorated,

`G_S>=d`.

Write the decoration above this forced baseline as

`R_G = (G_S-d)+G_Y+g_x >=0`.

Then

> `G_A=d+R_G`,                                         (L3)

and in particular

> `g_x<=R_G`.                                          (L4)

---

## 4. Exact slack identity

Since `N=12-d`,

`dN+d = d(12-d)+d = d(13-d)`.

For `d in {4,9}`,

`d(13-d)=36`.

Using `q=e(M)+G_A` together with (L1) and (L3),

`q = dN+R_M+d+R_G`
`  = 36+R_M+R_G`.

Thus we have the exact identity

> **`R_M+R_G=q-36`.**                                  (L5)

In particular, because `q<=38`,

> `R_M+R_G<=2`.                                        (L6)

Combining (L2), (L4), and (L6) gives the main conclusion

> **`d_M(x)+g_x <= q-36 <=2`.**                        (L7)

This is an exact structural consequence, not an averaging estimate.

---

## 5. Sharp q36/q37/q38 forms

The theorem immediately gives:

### q=36

`R_M=R_G=0`.

Hence

- `d_M(x)=0`;
- `g_x=0`;
- S has no internal missing edge;
- every point of S has decoration exactly one;
- every owner has zero decoration.

Thus the one-leftover escape is completely rigid at q36.

### q=37

`R_M+R_G=1`, so

> `d_M(x)+g_x<=1`.

The leftover is either regular of missing degree at most one or decorated with no more than one unit of total local defect.

### q=38

`R_M+R_G=2`, so

> `d_M(x)+g_x<=2`.

The leftover can carry only a d0/d1/d2 regular row, or a decorated degree-zero/one analogue.  No genuinely large-support geometry remains at x.

---

## 6. Bridge to the global support architecture

This proves the promised bridge:

> **One-Leftover Decorated-Escape Bridge.**
>
> A fully-decorated d4/d9 common-S family at q<=38 with owner count `12-d` automatically produces a unique leftover shell vertex whose combined shell missing degree and decoration is at most two.

Consequently the near-maximal large-support escape does not require an independent K4,9-style case tree.

- If `g_x=0`, x is a regular low-support shell vertex with `d_M(x)<=2`; it feeds the d0/d1/d2 low-support/repivot machinery.
- If `g_x>0`, then `d_M(x)<=1`; it feeds the decorated one-spoke / low-defect compatibility machinery.

Thus the large-support regime descends back into the low-support or shell-poor regimes already present in the Global Support-Compatibility programme.

---

## 7. Relation to maximal-owner K4,9

`GLOBAL_LARGE_SUPPORT_DECORATED_ESCAPE_THEOREM.md` showed that the maximal fully-decorated owner count

`N=13-d`

produces the K4,9 equality geometry at the zero-extra-missing plateau.

The present theorem identifies the immediately adjacent layer `N=12-d`:

> maximal owner count -> K4,9 equality geometry;
>
> one fewer owner -> one leftover vertex with total local defect at most two.

This is the desired equality-descent mechanism.  The large-support escape cannot drift arbitrarily far from the already-understood equality family without generating a low-support witness.

---

## 8. Parameterized form

The proof only uses

- shell size h=13;
- support size d satisfying `d(h-d)=36`;
- one leftover vertex, `N=h-d-1`;
- full decoration on S;
- the q ceiling.

In an analogous pivot system with shell size h and baseline `Q0=d(h-d)`, the same calculation gives

`q = Q0 + R_M+R_G`

and hence for a one-leftover fully-decorated escape

> `d_M(x)+g_x <= q-Q0`.

Thus the theorem is not intrinsically tied to the E338--E340 labels and is portable to higher-r reductions once the corresponding shell baseline is known.