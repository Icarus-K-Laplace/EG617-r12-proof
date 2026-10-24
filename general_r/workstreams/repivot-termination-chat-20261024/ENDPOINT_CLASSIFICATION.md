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

## 3. High Endpoint Three-Owner Theorem

### Theorem

Let `Y_hi` be the set of **all** regular shell vertices with missing degree

`d_y>=r-2`.

Then for every `r>=12`,

> **`|Y_hi|<=3`.**

This is a global high-endpoint bound across all missing sets; no common-S assumption is used.

### Proof

Assume four distinct high owners `y_1,y_2,y_3,y_4` exist, and write `Z={y_1,y_2,y_3,y_4}`.

#### Step 1: Z contains a target edge

If the four vertices were pairwise target-nonadjacent, the symbolic zero-gap theorem would give

`D_{y_i} intersect D_{y_j}=empty`

for every `i!=j`.

Since every `|D_{y_i}|=d_{y_i}>=r-2`, the core H would contain at least

`4(r-2)`

vertices. But

`|H|=3r-1`

and

`4(r-2)>3r-1`

for every `r>=8`.

Therefore `F[Z]` contains at least one target edge. Equivalently,

`e_M(Z)<=C(4,2)-1=5`.                                      (3.1)

#### Step 2: four high owners already force many shell missing edges

Sum their missing degrees in the shell missing graph M:

`sum_{y in Z} d_y >=4(r-2)`.

The number of **distinct** missing edges incident with Z is

`sum_{y in Z} d_y - e_M(Z)`,

because an internal missing edge of Z is counted twice in the degree sum and must be corrected once.

Using (3.1),

`e(M)>=4(r-2)-5=4r-13`.                                    (3.2)

Since

`q=e(M)+G_A>=e(M)`,

we obtain

`q>=4r-13`.                                                  (3.3)

But hypothesis B gives

`q<=3r-1`.

For every `r>=13`,

`4r-13>3r-1`,

contradiction.

Thus only the boundary value `r=12` remains.

#### Step 3: the r=12 equality boundary is impossible

At `r=12`, (3.3) gives

`q>=35`,

while the strengthened ceiling gives `q<=35`. Hence equality holds throughout:

- `q=35`;
- `e(M)=35`;
- `G_A=0`, so every shell vertex is regular;
- every selected high owner has `d_y=10`;
- `e_M(Z)=5`, so `F[Z]` has exactly one target edge;
- every missing edge of M is incident with Z.

Therefore the nine vertices of `A\Z` contain no shell missing edge. Consequently

`B_0={p} union (A\Z)`

is a target clique of size 10, and every vertex of `B_0` has target degree exactly `r+1=13`.

Moreover `q=35` together with `K>=8` and the residual edge cap forces equality in both:

`E=D_12(49)=340`, `K=8`.

Hence the multicolor equality regular-clique obstruction applies and says every regular target clique has size at most

`floor((r-1)/2)=5`.

This contradicts `|B_0|=10`.

Therefore four high owners are impossible also for r=12.

Thus

> **`|Y_hi|<=3` for every `r>=12`.** QED.

**Status:** `PROVED_CONDITIONAL`.

---

## 4. High Endpoint Bounded-Complement Reduction Theorem

For a high owner define

`s_y=r-d_y`.

Since `d_y in {r-2,r-1,r}`,

`s_y in {2,1,0}`.

The shell target-neighbour set of y is

`T_y=A\(S_y union {y})`

and has exactly

`|T_y|=s_y<=2`.

By the Three-Owner Theorem there are at most three high owners. Hence the entire high endpoint has the following r-independent encoding.

### Shell kernel

Let

`K_A=Y_hi union (union_{y in Y_hi} T_y)`.

Then

> **`|K_A|<=3+3*2=9`.**

Every target edge from a high owner to the shell is incident with this at-most-nine-point kernel. Outside it, every shell vertex is target-nonadjacent to every high owner.

### Core incidence kernel

For each `v in H`, define

`I(v)={y in Y_hi : v in D_y}`.

Because `|Y_hi|<=3`, there are at most

> **`2^3=8`**

possible owner-incidence signatures.

The zero-gap theorem further forbids any signature containing a target-nonadjacent pair of owners, so only clique signatures of the at-most-three-vertex owner graph actually survive.

### Finite high-endpoint skeleton

Thus every high endpoint is encoded by:

1. at most three owners;
2. one complement parameter `s_y in {0,1,2}` per owner;
3. a target graph on at most three owners;
4. shell neighbour sets `T_y` of size at most two inside a kernel of size at most nine;
5. at most eight core incidence-signature multiplicities;
6. the transported excess/decoration integers attached to these fixed classes.

The number of combinatorial skeleton types is independent of r. Only the integer multiplicities/excess values vary with r.

> **High Endpoint Reduction Theorem.** Under A+B, every `d>=r-2` local state is equivalent, for repivot-compatibility purposes, to one of finitely many bounded-complement skeletons with at most three owners and `s in {0,1,2}`.

**Status:** `PROVED_CONDITIONAL`.

This achieves the desired fixed-width high-endpoint reduction. The remaining task is to prove improvement/contradiction for each bounded skeleton family without expanding them into an r-dependent case tree.

---

## 5. Exact d2 common-S charge identity

Let a common-S d2 family have

- `S={s_1,s_2}`;
- `b=e_M(S) in {0,1}`;
- owner set Y of size N;
- leftover `L=A\(S union Y)` of size `l=r-1-N`;
- total common-S core charge `W=sum_{v in H}(kappa_v+e_F(v,S))`;
- allowance `a=b+sigma_{s_1}+sigma_{s_2}`.

The exact common-S ledger gives

`W=K+2N+G_S+2b+m_ST`.

Also

`sum_{s in S} sigma_s=m_ST+G_S-2l`,

so

`G_S+m_ST=a-b+2l`.

Substitution and `l=r-1-N` yield cancellation of N:

> **`W=K+2r-2+a+b`.**                                    (5.1)

This is exact and independent of owner multiplicity.

For a d2 exact one-loss common-hub system with three distinct support classes, the pre-existing charge barrier gives

`W>=|H|-1=3r-2`.

Combining with (5.1):

> **`K+a+b>=r`.**                                           (5.2)

Thus every three-class d2 terminal must carry linearly large total core excess/allowance. In particular, any d2 regime with `K+a+b<=r-1` has at most two nontrivial common-hub support classes.

The previously known concentrated state `K=8,a=3,b=1` gives

`W=2r+10`,

and (5.2) immediately yields `r<=12`; this explains its exact small-r cutoff.

**Status:** `PROVED_SYMBOLIC` for (5.1), `PROVED_CONDITIONAL` for the three-class consequence (uses the existing one-loss pattern theorem and charge barrier).

---

## 6. Surviving endpoint families

After the results above:

- `d=3` common-S: **closed**;
- `d=2`: scalable; three-class one-loss terminals must satisfy `K+a+b>=r`; global plateau equality/positive-loss closure remains open;
- `d=1,0`: not yet frozen in this workstream;
- `d>=r-2`: **reduced to a finite bounded-complement skeleton with at most three total owners**.

No medium degree survives.