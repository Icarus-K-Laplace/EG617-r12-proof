# Global Fully-Decorated Multi-Leftover Descent Theorem

Status: **PROVED_ANALYTIC**.

This theorem extends `GLOBAL_LARGE_SUPPORT_ONE_LEFTOVER_BRIDGE.md` from one leftover shell vertex to an arbitrary leftover set.  Its purpose is to turn the remaining fully-decorated large-support escape into a quantitative low-defect extraction problem rather than a new shell case tree.

Dependencies:

- exact shell identity `q=e(M)+G_A`;
- common-S owner definition;
- full decoration of the common missing set.

No r=12 hereditary cap or solver is used in the derivation.

---

## 1. Setup

Let a pivot shell A have size 13.

Let Y be a common-S family of regular owners with

`|S|=d`,
`|Y|=N`,

and suppose every point of S is globally decorated:

`g_s>=1` for all `s in S`.

Let

`T=A\(S union Y)`,
`t=|T|=13-d-N`.

Assume `t>=1`.

Because every owner has missing set exactly S:

- every Y--S pair is a shell missing edge;
- every Y--Y pair is a target edge;
- every Y--T pair is a target edge.

Hence all shell missing edges outside the forced `Y x S` block lie inside `S union T`.

Write

`m_SS=e_M(S)`,
`m_ST=e_M(S,T)`,
`m_TT=e_M(T)`.

Let

`R_G=(G_S-d)+G_Y+G_T >=0`.

---

## 2. Exact global slack

The shell missing-edge count is

`e(M)=dN+m_SS+m_ST+m_TT`.

The shell decoration is

`G_A=d+R_G`.

Therefore

`q=dN+d + m_SS+m_ST+m_TT+R_G`.

Since `N=13-d-t`,

`dN+d=d(14-d-t)`.

Define

> `R := q-d(14-d-t)`.                                      (M1)

Then the preceding identity gives the exact nonnegative decomposition

> `R=m_SS+m_ST+m_TT+R_G`.                                  (M2)

Thus R is precisely the slack remaining after the forced owner--S missing block and the forced one-unit decoration on every point of S.

---

## 3. Total local defect of the leftover set

For `x in T`, x is target-adjacent to every owner in Y.  Hence all shell missing neighbours of x lie in `S union T`.

Summing shell missing degrees over T gives

`sum_(x in T) d_M(x)=m_ST+2m_TT`.                           (M3)

Therefore the total combined missing/decoration defect on T is

`L_T := sum_(x in T)(d_M(x)+g_x)`
`     =m_ST+2m_TT+G_T`.                                    (M4)

Using (M2),

`2R-L_T`
` =2m_SS+m_ST`
`  +2(G_S-d)+2G_Y+G_T`
` >=0`.

Hence

> **`L_T<=2R`.**                                           (M5)

This is the multi-leftover descent inequality.

---

## 4. Low-defect extraction

By averaging (M5), some leftover vertex x satisfies

> **`d_M(x)+g_x <= floor(2R/t)`.**                          (M6)

Equivalently,

> **`d_M(x)+g_x <= floor( 2[q-d(14-d-t)]/t )`.**            (M7)

Thus every fully-decorated common-S family with at least one leftover shell vertex produces a quantitatively controlled low-defect leftover.

This conclusion is independent of support geometry in the core.

---

## 5. One-leftover sharpening

When `t=1`, there are no T--T missing edges.  Equation (M4) becomes

`L_T=m_ST+G_T`.

Comparing directly with (M2) gives

`L_T<=R`,

so

> `d_M(x)+g_x<=R`.                                         (M8)

For `d in {4,9}` one has `d(13-d)=36`; at the maximum possible fully-decorated owner count `N=12-d`,

`R=q-36`,

recovering the sharper theorem

> `d_M(x)+g_x<=q-36<=2`.

---

## 6. q36 d4 illustration

Take `d=4` and `q=36`.

Then

`R=36-4(10-t)=4t-4`.

For `t>=2`, (M6) gives

`d_M(x)+g_x <= floor(8-8/t)`.

In particular:

- `t=2`: some leftover has combined defect at most4;
- `t=3`: some leftover has combined defect at most5;
- `t>=4`: some leftover has combined defect at most6.

Thus even several owners below the fully-decorated maximum, the system must expose a bounded-defect shell vertex rather than an unconstrained new large-support state.

The t=1 case is much sharper and gives defect zero at q36.

---

## 7. Threshold form

For any target integer k, if

`2R < t(k+1)`,

then (M6) yields a leftover vertex with

`d_M(x)+g_x<=k`.

Hence the theorem can be used as an extraction criterion:

> enough owner multiplicity / small enough q-slack forces the fully-decorated escape to descend into a prescribed low-defect regime.

This is the desired forcing-to-master-contract mechanism.

---

## 8. Parameterization beyond r=12

For a shell of arbitrary size h, the same proof gives

`N=h-d-t`,

forced baseline

`dN+d=d(h-d-t+1)`,

and

`R=q-d(h-d-t+1)`.

Then

`sum_(x in T)(d_M(x)+g_x)<=2R`.

Thus multi-leftover descent is a general feature of fully-decorated common-support systems, not an r=12-specific coincidence.