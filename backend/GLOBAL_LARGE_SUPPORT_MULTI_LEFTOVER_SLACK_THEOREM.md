# Global Large-Support Multi-Leftover Slack Theorem

Status: **PROVED_ANALYTIC**.

This theorem extends `GLOBAL_LARGE_SUPPORT_ONE_LEFTOVER_BRIDGE.md` from one leftover shell vertex to an arbitrary leftover set.  It converts the entire fully-decorated large-support branch into a quantitative local-defect extraction problem.

Dependencies:

- exact shell identity `q=e(M)+G_A`;
- common-S owner definition;
- full decoration of S;
- shell size 13;
- no E-layer label and no solver.

---

## 1. Setup

Let A be the 13-point shell of a maximum-q pivot.  Let Y be a common-S regular owner family with

- common missing set `S`, `|S|=d`;
- every vertex of S globally decorated;
- owner count `N`;
- leftover set

  `L=A\(S union Y)`, `|L|=r>=1`.

Thus

> `N=13-d-r`.                                             (1)

Every owner y has shell missing set exactly S, so y is target-adjacent to every other owner and to every leftover vertex.

Consequently all shell missing edges consist of

1. the forced `dN` owner--S edges;
2. missing edges inside S;
3. missing edges between S and L;
4. missing edges inside L.

Write

`R_M=e_M(S)+e_M(S,L)+e_M(L)`.                             (2)

Because S is fully decorated, write the decoration above its forced d-unit baseline as

`R_G=(G_S-d)+G_Y+G_L>=0`.                                 (3)

Put

`R=R_M+R_G`.                                               (4)

---

## 2. Exact total-slack identity

The shell identity gives

`q=e(M)+G_A`
` =dN+R_M+d+R_G`
` =d(13-d-r)+d+R`.

Hence

> `q=d(14-d-r)+R`.                                        (5)

For the high-right large-support values `d in {4,9}`,

`d(13-d)=36`.

Therefore (5) becomes

> **`R=q-36+d(r-1)`.**                                    (6)

For r=1 this reduces exactly to the one-leftover identity `R=q-36`.

---

## 3. Total local defect of the leftover set

For each leftover vertex x define its local shell defect

`lambda_x=d_M(x)+g_x`.                                    (7)

Since no owner is missing from x, the missing neighbours of x lie only in `S union L`.

Summing over all leftovers,

`sum_(x in L) d_M(x)=e_M(S,L)+2e_M(L)`.                   (8)

Thus

`Lambda:=sum_(x in L) lambda_x`
` =e_M(S,L)+2e_M(L)+G_L`.                                 (9)

Comparing (9) with R gives

`Lambda`
`=R + e_M(L) - e_M(S) -(G_S-d)-G_Y`
`<=R+e_M(L)`
`<=R+binom(r,2)`.                                         (10)

Combining (6) and (10):

> **`Lambda <= q-36+d(r-1)+binom(r,2)`.**                 (11)

Therefore at least one leftover satisfies

> **`min_x lambda_x <= floor((q-36+d(r-1)+binom(r,2))/r)`.**  (12)

This is the multi-leftover defect-extraction bound.

---

## 4. Equivalent threshold form

If every leftover had local defect at least t, then `Lambda>=rt`.  Hence (11) gives the necessary condition

> `rt <= q-36+d(r-1)+binom(r,2)`.                          (13)

Equivalently, if

> `rt > q-36+d(r-1)+binom(r,2)`,                           (14)

then some leftover has `lambda_x<=t-1`.

Thus any desired low-defect threshold can be tested by one scalar inequality; no large-support shell enumeration is needed.

---

# 5. d=4 consequences at q<=38

Take d=4.

Then

`R=q-36+4(r-1)`

and

`min lambda_x <= floor((q-36+4(r-1)+binom(r,2))/r)`.       (15)

### Two leftovers

For r=2,

> `Lambda<=q-31`,                                         (16)

so

- q=36: `min lambda<=2`;
- q=37: `min lambda<=3`;
- q=38: `min lambda<=3`.

Hence:

> **the fully-decorated d4/q36/two-leftover state automatically descends to the local-defect-at-most-two interface.**

This extends the old one-leftover descent by one complete owner layer at q36.

### Exact q37 equality residual

At d=4, r=2, q=37 we have `R=5` and `Lambda<=6`.

Suppose neither leftover has defect at most2.  Then both have defect at least3, so `Lambda>=6`.  Thus equality holds throughout (10):

- `lambda_x=lambda_y=3`;
- `e_M(L)=1`, so the two leftovers are shell-missing adjacent;
- `e_M(S)=0`;
- `G_S=d`, i.e. every point of S has exactly the forced one unit of decoration;
- `G_Y=0`.

Therefore the only q37/two-leftover state which fails to produce a local-defect-at-most-two witness is the rigid equality geometry

> **two mutually missing leftovers, each of total local defect exactly3, with no internal missing edge in S, no owner decoration, and no decoration excess on S.**

This is a finite equality interface, not an arbitrary large-support family.

### q38

At q=38,r=2, `Lambda<=7`.  Hence at least one leftover has defect at most3.  Thus even the worst two-leftover q38 escape has descended from d4 to a d<=3 local defect object.

---

# 6. d=9 consequences

For d=9,

`R=q-36+9(r-1)`.                                           (17)

The fully-decorated owner bound already gives `N<=3`, so an actually repeated owner family has only:

- N=3, r=1: covered by the one-leftover theorem;
- N=2, r=2: the only genuine repeated multi-leftover case.

For r=2,

`Lambda<=q-26`,                                            (18)

so at q=36,37,38 one obtains a leftover of defect at most5,5,6 respectively.

This is not yet a low-support closure, but it reduces the entire repeated fully-decorated d9 multi-leftover branch to a two-vertex defect system.  No higher-dimensional leftover geometry remains.

---

# 7. Strengthened forcing-to-master coverage

Combine this theorem with `GLOBAL_FORCING_TO_MASTER_ALLOWANCE_COVERAGE.md`.

The previously open fully-decorated large-support bridge now sharpens as follows.

## d=4

- maximum fully-decorated owner count (`r=1`): local defect <=2;
- one fewer owner (`r=2`):
  - q36: local defect <=2;
  - q37/q38: local defect <=3, with q37 failure of <=2 forced into one exact equality geometry;
- r>=3: controlled by the scalar defect-extraction inequality (12).

## d=9

- r=1: local defect <=2;
- the only repeated multi-leftover layer is r=2 and is reduced to a two-leftover defect system by (18).

Thus Bridge C is no longer an arbitrary fully-decorated support problem.  It is a finite local-defect/equality descent problem parameterized only by `(d,r,q)`.

---

# 8. General parameterization

For a shell of size h and fully-decorated common missing set S of size d, with N owners and r=h-d-N leftovers, the same proof gives

`q=dN+d+R`

and

`sum_(x in L)(d_M(x)+g_x)<=R+binom(r,2)`.

Hence the multi-leftover defect-extraction method is portable to larger-r pivot systems once the shell size and q ceiling are known.