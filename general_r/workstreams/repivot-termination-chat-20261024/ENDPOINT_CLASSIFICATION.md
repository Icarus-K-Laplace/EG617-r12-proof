# Endpoint Classification

All statements are conditional on hypotheses A+B and `r>=12` unless stated otherwise.

Audited caps:

- `alpha(F)<=4`, `omega(F)<=r-1`;
- every legal core H has `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`.

Do not use an independent-4 contradiction unless all four vertices lie in H.

---

## 1. Degree endpoint collapse

`K_r>=8` gives `q<=3r-1`. Since every regular repivot of missing degree d satisfies

`q_y>=d(r+1-d)`,

all medium degrees are impossible:

> **`d in {0,1,2,3,r-2,r-1,r}`.**

---

## 2. Shell-incidence kernel

For `s in A`,

`t_s=d_M(s)+g_s=e_F(s,H)`,

and

> `sum_A t_s<=6r-2`.

For a regular owner with missing set S, `|S|=d`,

`sigma_s=t_s-(r+1-d)-m_S(s)>=0`,

`sum_(s in S)t_s=d(r+1-d)+a+b`.

Consequences:

- d1 missing partners lie in at most5 shell vertices/classes;
- all d2 missing-set endpoints lie in at most6 shell vertices, hence at most15 pair classes.

Thus shell-side low-endpoint type count is absolute-constant in r.

---

## 3. d0

d0 is neutral: same core, q and tau. Quotient it.

**Status:** `PROVED_SYMBOLIC`.

---

## 4. d1

There are at most5 shell singleton classes. For `S={s}`, `D={u}`,

> `q-q_y=kappa'_s-kappa_u`.

In the neutral-free plateau slice, the new eta-coordinate population is distributed among these five classes. If one class has N1 flat owners and allowance c, then under the inherited core cap `K<=2r-2`,

> **`(N1-1)c<=3r-2`.**

If c=0, row closure gives `N1<=3`.

Hence every linear d1 plateau concentration has O(1) allowance.

**Status:** shell/exchange `PROVED_CONDITIONAL`; scale-transfer `PROVED_CONDITIONAL`; final bounded-allowance d1 rigidity `OPEN`.

---

## 5. d2 shell universe

Every d2 missing pair belongs to one of at most15 shell pair classes.

For a fixed class `S={u,v}`, put

`w_x=kappa_x+e_F(x,S)`, `mu(D)=1-e_H(D)`.

Every owner satisfies

> `ell=q-q_y=a-[w(D)+mu(D)]>=0`.

Let `s=|S intersect X|`.

- `s=0`: fixed-width, at most3 owners in the clean b=0 plateau and only O(1) strict types when b=1;
- `s=1`: at most6 q-flat owners;
- `s=2`: unique scalable equal-q regime.

So only a fully decorated shell pair `S subset X` can scale.

---

## 6. d2 repeated branch

For exact class multiplicity m and neutral population zeta,

> `zeta(new)=m-1`,
>
> `m_reverse=zeta+1`.

At `Phi_3=(q,tau,zeta)` maximality, `m<=zeta+1`.

The flat equality branch `m=zeta+1` is the Balanced Two-Chamber terminal

> `H <--> H-D+S`,

with no longer correction cycle.

**Status:** `PROVED_SYMBOLIC` / `PROVED_CONDITIONAL`.

---

## 7. d2 distinct fully-decorated branch

Work in the genuine neutral-free `Phi_3`-flat slice `zeta=0`.

For two same-class supports `D_i,D_j`, repivot through `D_i` gives exact new missing degree

> **`2-|D_i intersect D_j|`.**

Thus support overlap is literally a d1 correction transition.

### Fourth coordinate

Define

`eta(p)=#{regular d1 owners x on the same (q,tau,zeta) plateau as p}`.

Then

> **`Phi_4=(q,tau,zeta,eta)`**

is bounded. If `G_S` is the support-intersection graph, then at `Phi_4` maximality

> **`Delta(G_S)<=eta`.**

Hence a class of N supports contains a disjoint subfamily of size at least

> **`ceil(N/(eta+1))`.**

### Low allowances

- `a=0`: at most3 distinct flat supports;
- `a=1`: at most9 distinct flat supports;
- `a>=2`: every disjoint subfamily of size nu satisfies the weighted matching bound
  > `nu(a-1)<=W<=4r+9-a`.

### First scalable layer a=2

At a=2:

- zero-weight support vertices number at most3;
- the zero-free `(1,1)` target-support graph has maximum degree3;
- every unbounded family contains an unbounded disjoint clean subsystem;
- every linear-size family contains a linear-size one.

A clean block is a target K2 whose two endpoints both have common-S weight1.

Repivot through one clean block preserves every other disjoint clean block as a clean d2 block of allowance2. Thus the scalable a=2 terminal contains the repivot-closed

> **Clean Pair-Exchange Design:** clean K2 blocks, each inter-block target graph a matching of size0,1,or2, plus at most O(1) zero-containing special blocks.

**Status:** `PROVED_CONDITIONAL`; Clean Pair Nonextension is `OPEN`.

---

## 8. d3

Equality B-floor gives `q<=3r-2` and `a+B<=4`; declared low-charge Bridge-B assets eliminate the sector.

> **No d3 terminal remains.**

**Status:** `PROVED_CONDITIONAL`.

---

## 9. High endpoint

All regular owners with `d>=r-2` number at most3.

Writing `r-d in {0,1,2}`, their interaction is a bounded-complement kernel with at most9 shell interaction vertices and at most8 core owner-incidence signatures.

**Status:** `PROVED_CONDITIONAL`.

---

## 10. Canonical surviving terminal families

Only four structural packages remain:

1. bounded-allowance d1 singleton-exchange systems in at most5 shell classes;
2. the Balanced Two-Chamber repeated d2 terminal;
3. the Clean Pair-Exchange distinct d2 terminal beginning at allowance2, with higher allowance controlled by eta/matching compression;
4. at most3 high-endpoint owners.

No surviving endpoint has an r-growing number of shell-support types.

The unique currently visible r-growing **local design object** is the clean allowance-2 pair system.