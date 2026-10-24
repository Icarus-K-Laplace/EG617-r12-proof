# Global Large-Support Multi-Leftover Degree Descent

Status: **PROVED_ANALYTIC**.

This theorem combines the multi-leftover slack inequality with the exact regular-row exchange gap.  Its conclusion is that fully-decorated repeated d4/d9 families at q<=38 cannot create a genuinely new medium-support regime: they produce a leftover of shell missing degree at most four, except for one explicit decorated `(d_M,g)=(5,1)` equality escape in the weakest layers.

Dependencies:

- `GLOBAL_LARGE_SUPPORT_MULTI_LEFTOVER_SLACK_THEOREM.md`;
- exact regular exchange identity `q_x=d(13-d)+P_x` with `P_x>=0`;
- q ceiling `q<=38`.

---

# 1. Regular degree gap at q<=38

Let x be a regular shell vertex with shell missing degree d.
The exact exchange identity gives

`q_x=d(13-d)+P_x`, `P_x>=0`.

At a maximum-q pivot, `q_x<=q<=38`.  Hence necessarily

`d(13-d)<=38`.

But

- d=5 gives 40;
- d=6 gives 42;
- d=7 gives 42;
- d=8 gives 40.

Therefore

> **no regular shell vertex at q<=38 has missing degree 5,6,7 or8.**       (G1)

Thus a regular vertex whose local defect `lambda=d_M` is at most6 actually has

> `d_M<=4`.                                                               (G2)

For a decorated shell vertex, `g_x>=1`, so if

`lambda_x=d_M(x)+g_x<=5`,

then also

> `d_M(x)<=4`.                                                            (G3)

If `lambda_x<=6`, the only way to have `d_M(x)>4` is

> **`d_M(x)=5`, `g_x=1`.**                                                (G4)

Indeed d_M=6 would leave no positive decoration, while d_M>=7 exceeds lambda<=6.

Hence local-defect bounds five and six translate almost completely into a d<=4 descent.

---

# 2. Fully-decorated d9 repeated families

For d=9 at q<=38, full decoration gives owner count N<=3.
A repeated owner family has N>=2, so only two layers exist.

## N=3

Then r=1 leftover.  The one-leftover theorem gives

`lambda_x<=q-36<=2`.

Hence

> `d_M(x)<=2`.

## N=2

Then r=2.  The multi-leftover theorem gives

`Lambda<=q-26`,

so some leftover satisfies

- q36: `lambda<=5`;
- q37: `lambda<=5`;
- q38: `lambda<=6`.

Using (G2)--(G4):

- at q36 or q37, some leftover has `d_M<=4`;
- at q38, either some leftover has `d_M<=4`, or the extracted minimum-defect leftover is exactly

  `(d_M,g)=(5,1)`.

Therefore:

> **Every fully-decorated repeated d9 family at q<=38 descends to a d<=4 leftover, except possibly the q38 two-owner equality escape `(d_M,g)=(5,1)`.**

No d6/d7/d8 leftover can survive.

---

# 3. Fully-decorated d4 repeated families

For d=4, a repeated family has owner count N>=2, so

`r=13-4-N=9-N`,

hence `1<=r<=7`.

The multi-leftover bound is

`min lambda <= floor((q-36+4(r-1)+binom(r,2))/r)`.          (D1)

For q<=38 this gives the following worst-case bounds:

|r|owner count N=9-r|max extracted lambda at q<=38|
|---:|---:|---:|
|1|8|2|
|2|7|3|
|3|6|4|
|4|5|5|
|5|4|5|
|6|3|6|
|7|2|6|

Apply the regular-degree gap and decorated conversion above.

### N>=4 (r<=5)

The extracted leftover has `lambda<=5`.
Therefore, whether regular or decorated,

> **some leftover has `d_M<=4`.**

### N=2 or3 (r=7 or6)

The extracted leftover has `lambda<=6`.
Therefore either

- some leftover has `d_M<=4`, or
- the only possible failure is the exact decorated local state

  `(d_M,g)=(5,1)`.

Thus:

> **Every fully-decorated repeated d4 family at q<=38 descends to a d<=4 leftover, except possibly when N is 2 or3 and the extracted extremal leftover is `(d_M,g)=(5,1)`.**

At smaller q the table improves automatically; for example d4/r=2/q36 already yields d_M<=2.

---

# 4. Unified large-support descent theorem

Combining Sections2--3:

> **Large-Support Degree Descent.**
>
> In the r=12 shell at q<=38, every fully-decorated repeated common-S family with support size d=4 or9 produces a leftover shell vertex of missing degree at most4, except for one explicit equality type:
>
> `d_M=5`, `g=1`.
>
> That equality type can occur only in the weakest multi-leftover layers:
> - d9: N=2 at q38;
> - d4: N=2 or3 in the lambda<=6 layers.

Therefore the fully-decorated large-support bridge has been reduced to

1. an actual d<=4 low-/medium-support witness, already inside the global support programme; or
2. a single decorated d5/g1 equality escape.

No separate d6/d7/d8 geometry remains.

---

# 5. Consequence for the forcing-to-master bridge

The large-support part of `GLOBAL_FORCING_TO_MASTER_ALLOWANCE_COVERAGE.md` can now be sharpened:

- non-fully-decorated d4/d9: subcritical bounded-block regime;
- fully-decorated repeated d4/d9: descend to d<=4;
- unique possible obstruction to full descent: decorated `(d_M,g)=(5,1)` in the explicitly listed low-owner equality layers.

Hence Bridge C is no longer a general multi-leftover problem.  It is a single local equality problem.

The remaining global backend bridge can therefore be organized as:

- common-S extraction;
- d2/d3 higher-slack shallow-loss classification;
- one decorated d5/g1 equality closure.

---

# 6. Portability

The only q-specific input is the regular exchange gap

`d(13-d)>q`

for d=5,6,7,8.  In a larger-r pivot problem, replace 13 by the new shell size and recompute the forbidden middle-degree interval.  The combination with the multi-leftover defect inequality is otherwise unchanged.