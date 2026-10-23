# Global Large-Support Decorated-Escape Theorem

Status: **PROVED_ANALYTIC** after the 2026-10-23 scope correction recorded below.

Dependencies:

- `GLOBAL_SUBCRITICAL_ALLOWANCE_DECOMPOSITION.md`;
- `GLOBAL_BLOCK_TRANSVERSAL_THEOREM.md`;
- `GLOBAL_COMMON_S_OWNER_CLIQUE_THEOREM.md`;
- exact shell identity `q=e(M)+G_A`;
- the inherited shell floor `e(M)>=22` in the legal r=12 49-point backend.

Purpose: reorganize the large-support q36--q38 analysis around one structural dichotomy and state the fully-decorated branch with the correct q-budget.

## Scope correction

An earlier version incorrectly described the maximal shell-complement owner count `N=13-d` as a possible **fully-decorated** K4,9 equality state.  This is incompatible with the exact shell identity: `N=13-d` already contributes `d(13-d)=36` missing edges, while full decoration of S contributes at least d further units, so `q>=36+d>38` for `d in {4,9}`.

Therefore K4,9 is **not** a fully-decorated escape.  It belongs to the non-fully-decorated / plateau side of the large-support analysis.  The corrected fully-decorated owner bound is strictly smaller and is proved below.

---

## 1. General high-right setup

Let p be a maximum-q pivot in the r=12 49-point backend.

Let Y be a common-S owner family with support/missing size

`d in {4,9}`.

Assume

`q<=38`.

For a common-S row the base exchange term is

`d(13-d)=36`

for both d=4 and d=9.

The common row allowance is

`a=q-36-B`,

with `B>=0`.  Therefore

> `a<=2<d-1`.                                               (L1)

Let

`s=|S intersect X|`

be the number of globally decorated vertices in the common missing set.

---

## 2. Non-fully-decorated regime

Assume

`s<d`.                                                       (L2)

Then `GLOBAL_SUBCRITICAL_ALLOWANCE_DECOMPOSITION.md` applies.

Hence:

1. plateau owner rows are singleton support classes and there are at most3 of them;
2. every strict-loss support is disjoint from every distinct support class;
3. two distinct strict supports have at most `a-1<=1` target cross-edge.

Thus the strict layer is a family of pairwise-disjoint d-blocks with cross allowance at most1.

Suppose four distinct strict support classes existed.  Choose one point uniformly from each block.  Since each block pair has at most one target cross-edge, the expected number of target edges in the four-point transversal is at most

`6/d^2 <= 6/16 <1`.

But every four-point transversal lies in H with `alpha(H)<=3`, so it must contain at least one target edge.  Contradiction.

Therefore

> **number of distinct strict support classes <=3**,          (L3)

and every non-fully-decorated d4/d9 common-S family has at most six distinct support classes after adjoining the at-most-three plateau singletons.

This is the bounded-block branch of the theorem.

---

## 3. Fully-decorated regime: corrected owner bound

Now assume

`s=d`.                                                       (L4)

Then every point of S has decoration at least one, so

`G_A>=d`.                                                    (L5)

Every common-S owner is missing from every point of S, and owners are distinct from S.  Therefore the shell missing graph contains all `dN` owner--S edges:

`e(M)>=dN`.                                                  (L6)

Using the exact identity `q=e(M)+G_A`, (L5)--(L6) give

> **`q>=dN+d`.**                                            (L7)

Hence

> **`N <= floor((q-d)/d)`.**                                (L8)

At `q<=38` this yields the sharp uniform high-right bounds

- `d=4`: `N<=8`;
- `d=9`: `N<=3`.

Thus a fully-decorated d4/d9 system can **never** attain the shell-complement maximum `13-d` under the q36--q38 ceiling.

In particular, the K4,9 shell cannot be interpreted as a fully-decorated equality state.

---

## 4. Maximum possible fully-decorated state

The corrected bounds in Section3 are exactly one below the shell-complement maxima:

- d4: maximum fully-decorated `N=8=12-d`;
- d9: maximum fully-decorated `N=3=12-d`.

Therefore the maximal possible fully-decorated state has exactly one leftover shell vertex.

`GLOBAL_LARGE_SUPPORT_ONE_LEFTOVER_BRIDGE.md` proves that in this state, if x is the unique vertex outside `S union Y`, then

> **`d_M(x)+g_x <= q-36 <=2`.**                              (L9)

Consequently the maximal fully-decorated large-support state automatically descends to the low-support / decorated one-spoke interface.  It is not a new plateau family.

At q=36 the descent is exact:

- x is regular;
- `d_M(x)=0`;
- S has no internal missing edge;
- every point of S has decoration exactly one;
- all other shell decoration vanishes.

At q=37/38 the unique leftover carries at most one/two units of combined missing-degree plus decoration.

---

## 5. Correct role of K4,9

The already-proved q36--q38 K4,9 closure remains valid, but its conceptual role is different from the one stated in the earlier version of this file.

K4,9 is a **non-fully-decorated large-support plateau/equality geometry**.  In either orientation of the bipartition, the relevant common missing side does not carry one positive decoration unit on every one of its vertices under q<=38.

Therefore K4,9 belongs on the `s<d` side of the global dichotomy, together with the subcritical plateau/strict-block machinery.  Its separate closure should be presented as an equality-case exclusion inside that branch, not as the endpoint of the fully-decorated escape.

---

## 6. d=10 low-q analogue

The same q-budget logic applies to d=10 rows at q<=33.

The base term is

`10*(13-10)=30`,

so `a<=3<d-1=9` and the non-fully-decorated branch is subcritical.

If S is fully decorated, then `G_A>=10`, while N owners contribute `10N` shell missing edges.  Hence

`q>=10N+10`.

At q<=33,

> `N<=2`.                                                    (L10)

This is stronger than the shell-complement bound `N<=3` and again shows that full decoration automatically suppresses owner multiplicity.

---

## 7. Unified corrected statement

> **Large-Support Decorated-Escape Theorem.**
>
> Let a common-S large-support family lie below the first overlap threshold.  Then:
>
> 1. if `s<d`, its support system is a bounded union of plateau singletons and pairwise-disjoint low-cross strict blocks;
> 2. if `s=d`, the exact shell q-budget gives `q>=dN+d`, sharply reducing owner multiplicity.
>
> For d4/d9 at q<=38, the fully-decorated branch has `N<=12-d`; at equality there is exactly one leftover shell vertex and it has combined missing-degree/decoration at most two.

Thus both sides of the dichotomy feed back into the Global Support-Compatibility architecture: the first through subcritical support packing, the second through low-support/one-spoke descent.

---

## 8. Remaining large-support bridge

After the corrected theorem, the genuinely open large-support task is smaller than previously stated.

- Non-fully-decorated systems are already in the subcritical bounded-block regime; the remaining work is equality compatibility of the few repeated strict/plateau blocks.
- Maximum-owner fully-decorated systems descend by the one-leftover theorem to local defect at most two.
- Fully-decorated systems with fewer owners have at least two leftover shell vertices; the remaining bridge is to turn their total q-slack into a low-defect leftover or a dense-decoration contradiction.

No independent 'fully-decorated K4,9' family remains.

---

## 9. Parameterization

The corrected owner inequality is symbolic.  In a shell of size h, if a common missing set S of size d is fully decorated and has N owners, then

`q >= dN+d`.

It therefore applies verbatim to analogous higher-r pivot reductions.  The subcritical decomposition likewise depends only on the allowance threshold and the residual-core independence bound.