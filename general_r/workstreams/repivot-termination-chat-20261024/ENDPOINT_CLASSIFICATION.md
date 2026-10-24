# Endpoint Classification

All statements are conditional on hypotheses A+B and `r>=12` unless stated otherwise.

## 1. Degree endpoint collapse

`K_r>=8` gives `q<=3r-1`. Every regular repivot with missing degree d satisfies

`q_y>=d(r+1-d)`.

For `4<=d<=r-3`,

`d(r+1-d)>=4(r-3)>3r-1`,

so no such degree occurs. Hence

> `d in {0,1,2,3,r-2,r-1,r}`.

---

## 2. Global shell-incidence budget

For `s in A`, define

`t_s=d_M(s)+g_s=e_F(s,H)`.

Then

> `sum_A t_s=2e(M)+G_A=2q-G_A<=6r-2`.                       (2.1)

For any regular owner y with missing set `S_y`, `|S_y|=d`, put `b_y=e_M(S_y)`. Singleton transport gives, pointwise for `s in S_y`,

> `sigma_s=t_s-(r+1-d)-m_{S_y}(s)>=0`,                       (2.2)

and after summing,

> `sum_{s in S_y}t_s=d(r+1-d)+a_y+b_y`.                     (2.3)

This budget controls all low endpoints simultaneously.

---

## 3. d0 — neutral

If d=0, then `S=D=empty`; the repivot preserves H, q and tau. It is only a pivot relabelling and is contracted.

**Status:** `PROVED_SYMBOLIC`.

---

## 4. d1 — at most five shell classes

For d=1, (2.2) gives `t_s>=r` for the unique missing partner. By (2.1), all d1 missing partners lie in a fixed set of at most five shell vertices.

For `S={s}`, `D={u}`, the exact loss is

> `q-q_y=kappa'_s-kappa_u`.

Thus d1 is a one-point excess exchange inside at most five shell classes.

**Status:** shell reduction and exchange identity `PROVED_CONDITIONAL`; final q/tau-flat rigidity `OPEN`.

---

## 5. d2 — six-point support universe

For `S={u,v}`, put `b=e_M(S)`. Equation (2.2) gives

` t_u,t_v>=r-1+b `.

Let `U_2` be the union of all d2 shell missing sets. Then by (2.1)

> **`|U_2|<=6`.**                                            (5.1)

Therefore every d2 shell missing set is one of at most

> **`C(6,2)=15`**                                            (5.2)

pair classes, independent of r.

If `h_u=t_u-(r-1)`, then a fixed shell class `{u,v}` has exact allowance

> `a_{uv}=h_u+h_v-b_{uv}`.                                  (5.3)

If `m=|U_2|`,

`sum_{u in U_2}h_u<=(6-m)r+m-2`.

In particular, if `m=6`, then `sum h_u<=4`, and the total number of d2 owners is at most two.

Thus no d2 shell-support case count grows with r.

**Status:** `PROVED_CONDITIONAL`.

---

## 6. Fixed-class d2 plateau classification

Fix one of the at-most-fifteen d2 shell classes `S={u,v}` and let Y be all owners in that class. For core vertices put

`w_x=kappa_x+e_F(x,S)`,

and for a 2-support D put

`mu(D)=1-e_H(D)`.

Every owner y has exact integer loss

> `ell_y=q-q_y=a-[w(D_y)+mu(D_y)]>=0`.                       (6.1)

Let `lambda_x` be the number of owners whose support contains x. Support incidence gives

`g_x>=w_x+lambda_x-1`,

so

> `lambda_x>=2 or w_x>=1  => x in X`.                        (6.2)

Let `s=|S intersect X|`. A q-flat row satisfies

`|D_y intersect X|<=s`.

### s=0

Common-S transport forces `sigma_u=sigma_v=0`, hence `a=b`.

Every endpoint of a q-flat support has `lambda=1`, `w=0`; q-flat supports are disjoint.

- if `b=0`, then `a=0`, so every owner is q-flat, every support is a target edge, distinct supports have no target cross-edges, and `alpha(H)<=3` gives
  > `|Y|<=3`;
- if `b=1`, at most one q-flat owner exists. Every strict row has loss one and a target-edge, zero-w support; distinct strict support classes have no target cross-edges, so there are at most three distinct strict support classes.

### s=1

A q-flat support cannot repeat: repetition would decorate both of its endpoints, contradicting `|D_y intersect X|<=1`.

The graph of q-flat supports is a disjoint union of stars and isolated edges. A repeated star center is decorated; its leaves have w=0. Row closure makes the center plus its leaves independent, so `alpha(H)<=3` permits at most two edges per star. Choosing one zero-w endpoint from each component and using row closure shows there are at most three components.

Therefore

> **a fixed d2 class with `|S intersect X|=1` has at most six q-flat owners.**   (6.3)

### s=2

Tau imposes no cardinality restriction on a 2-support. Repeated q-flat supports can survive.

Hence:

> **The only d2 shell class in which the number of q-flat owners can scale with r is the fully decorated regime `S subset X`.**   (6.4)

This is the unique scalable equal-q d2 endpoint.

**Status:** `PROVED_CONDITIONAL`.

---

## 7. Exact d2 charge identity

For every d2 common-S system, with `b=e_M(S)`, allowance a and total core charge

`W=sum_{x in H}(kappa_x+e_F(x,S))`,

one has

> `W=K+2r-2+a+b`.                                           (7.1)

If an exact-one-loss common-hub subsystem has three distinct core support classes, the existing pattern charge barrier gives

`W>=3r-2`, hence

> `K+a+b>=r`.                                                (7.2)

Thus any difficult three-class one-loss terminal lies in a linearly-high scalar regime.

**Status:** (7.1) `PROVED_SYMBOLIC`; (7.2) `PROVED_CONDITIONAL`.

---

## 8. d3 — eliminated

The equality B-floor excludes `q=3r-1` for d3. Therefore every d3 view has `q<=3r-2`, so `a+B<=4`. The declared low-charge Bridge-B assets absorb the remaining d3 sector.

> **No d3 terminal remains.**

**Status:** `PROVED_CONDITIONAL`.

---

## 9. High endpoint — at most three owners

Let `Y_hi` be all regular shell vertices with `d>=r-2`.

If four existed, zero-gap/core packing forces at least one target edge among them, so their incident shell missing edges number at least

`4(r-2)-5=4r-13`.

For `r>=13`, this exceeds `q<=3r-1`. At `r=12`, equality forces `q=35`, `G_A=0`, hereditary equality and a 10-vertex regular target clique, contradicting the multicolor equality regular-clique obstruction.

Therefore

> **`|Y_hi|<=3` for every `r>=12`.**                          (9.1)

Writing `s_y=r-d_y in {0,1,2}`, all high-owner shell interaction lies in an at-most-nine-point kernel and core owner-incidence uses at most eight signatures.

Thus the high endpoint is an r-independent bounded-complement skeleton.

**Status:** `PROVED_CONDITIONAL`.

---

## 10. Low-owner clique

Any two regular owners with `d<=3` are target-adjacent: otherwise zero-gap requires `S_x union S_y=A`, while the union has size at most six and `|A|=r+1>=13`.

Hence all regular low-endpoint owners together with p form a target clique. From `omega(F)<=r-1`, there are at most `r-2` such owners.

**Status:** `PROVED_SYMBOLIC`.

---

## 11. Canonical surviving endpoint families

After all reductions:

- d0: quotient-neutral;
- d1: at most five shell classes; q/tau-flat one-point core exchange remains;
- d2: at most six shell support vertices / fifteen shell classes;
  - non-fully-decorated fixed classes have only O(1) q-flat skeletons;
  - the **only scalable q-flat class** has a fully decorated shell pair `S subset X`;
  - core-support multiplicity / transported loss inside that regime remains open;
- d3: eliminated;
- high endpoint: at most three owners in a finite bounded-complement skeleton.

No endpoint has an r-growing number of shell-support types. The unique scalable equal-q mechanism is now **fully decorated fixed-class d2 core-support multiplicity**.