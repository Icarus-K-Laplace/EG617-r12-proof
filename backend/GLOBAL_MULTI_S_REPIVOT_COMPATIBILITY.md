# Global Multi-S Repivot-Compatibility Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- exact regular-pivot exchange formula from `HIGH_LAYER_V3_JOINT_CANONICAL.md`;
- exact decoration transport;
- all-pivot core minimum-degree baseline;
- lexicographic maximality of `(q,tau)`.

Purpose: remove the common-missing-set hypothesis from the global charging step. This is the correct framework for a genuine multi-view system in which different regular owners may have different missing sets.

## 1. General setup

Let p be a lexicographically maximal `(q,tau)` pivot.

Let A be its shell, H its core, and let the core minimum-degree baseline be `h-1`, where `h=|A|`.

Take any family Y of regular shell vertices. For each `y in Y`, write

- `S_y=N_M(y)`;
- `d_y=|S_y|`;
- `D_y=N_H(y)`, so `|D_y|=d_y`;
- `T_y=A\(S_y union {y})`;
- `B_y=e_M(T_y)+G_(T_y)`;
- `kappa_v=d_H(v)-(h-1)`;
- `mu_y=C(d_y,2)-e_H(D_y)`.

Define the row allowance

`a_y=q-d_y(h-d_y)-B_y`.                                     (MS1)

The exact exchange formula gives

`q_y=d_y(h-d_y)+B_y+kappa(D_y)+mu_y+e_F(S_y,D_y)`.           (MS2)

Hence

> `q-q_y=a_y-kappa(D_y)-mu_y-e_F(S_y,D_y)`.                 (MS3)

No common-S hypothesis is used.

## 2. Exact multi-S gain/loss identity

For a core vertex v define its support-incidence multiplicity

`lambda_v=#{y in Y:v in D_y}`.

Put

`Phi_multi`
` =sum_v lambda_v kappa_v`
`  +sum_y mu_y`
`  +sum_y e_F(S_y,D_y)`.                                    (MS4)

Summing (MS3) over Y gives the exact identity

> **Multi-S support-gain identity**
>
> `sum_y(q-q_y)=sum_y a_y-Phi_multi`.                        (MS5)

Since p has maximum q, every summand on the left is nonnegative. Therefore

> `Phi_multi<=sum_y a_y`.                                    (MS6)

This is the exact global accounting law for a multi-view support system.

## 3. Support incidence still forces global decoration

Fix `v in H`.

Its old core degree is

`(h-1)+kappa_v`.

For every owner y with `v in D_y`, the shell vertex y is a target neighbour of v. These `lambda_v` shell neighbours are distinct and lie outside H.

Therefore

`d_F(v)>=(h-1)+kappa_v+lambda_v`.

With `g_v=d_F(v)-h`,

> `g_v>=kappa_v+lambda_v-1`.                                (MS7)

Thus every core vertex satisfying

`kappa_v+lambda_v>=2`

is globally decorated.

This requires no relation between the missing sets `S_y`.

## 4. Multi-S repetition-to-loss theorem

Let

`X_forced={v in H:kappa_v+lambda_v>=2}`

and define the number of forced-decorated support incidences

`J=sum_(v in X_forced) lambda_v`.                            (MS8)

For each row put

`s_y=|S_y intersect X|`,

`c_y=d_y-s_y`.                                               (MS9)

If y is a q-plateau row (`q_y=q`), exact tau transport and lexicographic maximality give

`|D_y intersect X|<=s_y`.                                   (MS10)

In particular the number of incidences of D_y lying on `X_forced` is at most `s_y`.

A strict row can contain at most `d_y=s_y+c_y` such incidences.

Hence, if L is the set of strict rows,

> `J<=sum_y s_y + sum_(y in L)c_y`.                          (MS11)

Put

`R=max(0,J-sum_y s_y)`.                                     (MS12)

Order the nonnegative capacities `c_y` decreasingly:

`c_(1)>=c_(2)>=...`.

Define

`ell*(R)=min{ell:sum_(i=1)^ell c_(i)>=R}`,                   (MS13)

with `ell*(0)=0`.

Then (MS11) implies

> `|L|>=ell*(R)`.                                             (MS14)

Every strict q-loss is an integer at least1. Combining (MS5) and (MS14) yields

> **Multi-S repetition-charging inequality**
>
> `Phi_multi+ell*(R)<=sum_y a_y`.                            (MS15)

If (MS15) fails, some legal repivot has `q_y>q`.

This is a fully multi-S improving-repivot criterion.

## 5. Same-support repetition gives a direct loss penalty

Let D be one fixed support used by a class of m owners

`Y_D={y:D_y=D}`,

with `m>=2` and `|D|=d`.

Every point of D has support multiplicity at least2, hence is globally decorated by (MS7).

For an owner `y in Y_D`, if

`s_y=|S_y intersect X|<d`,                                  (MS16)

then a q-plateau repivot would replace fewer than d decorated missing-set vertices by all d decorated vertices of D. Exact tau transport would give `tau_y>tau_p`, contradicting lexicographic maximality.

Therefore every owner satisfying (MS16) has

> `q_y<=q-1`.                                                 (MS17)

If `m_0` owners in the repeated class satisfy (MS16), then

> `sum_(y in Y_D)(q-q_y)>=m_0`.                              (MS18)

Thus support repetition itself creates a deterministic strict-loss penalty even when the owners have different missing sets.

## 6. Local geometry forced by one strict repeated owner

For `y in Y_D`, (MS3) reads

`q-q_y=a_y-[kappa(D)+mu(D)+e_F(S_y,D)]`.                     (MS19)

If y satisfies (MS16), then (MS17) implies

> `kappa(D)+mu(D)+e_F(S_y,D)<=a_y-1`.                        (MS20)

In particular

> `kappa(D)+mu(D)<=a_y-1`.                                   (MS21)

This converts a global repeated-support event into a fixed local structural defect bound on D.

## 7. E334 q32/d3 corollary

Now specialize only the numerical exchange baseline, without assuming a common S.

In the source-reported E334 surviving channel,

- `q=32`;
- the relevant rows have `d_y=3`;
- `h=13`.

Therefore

`d_y(h-d_y)=3*10=30`,

and

`a_y=2-B_y<=2`.                                              (MS22)

Let D be any repeated three-point support.

If at least one owner of D has a missing triple which is not fully decorated, then (MS21) gives

> `kappa(D)+mu(D)<=1`.                                       (MS23)

Hence D is forced into one of only two internal-defect regimes:

1. `mu(D)=0` and `kappa(D)<=1`: a target K3 with at most one unit of core excess on the support;
2. `mu(D)=1` and `kappa(D)=0`: a two-edge triple with zero core excess.

No support with two or three internal target nonedges can repeat through a non-fully-decorated owner in this q32 channel.

Therefore every repeated support in the d3 system satisfies the dichotomy:

> **near-K3 regime:** D obeys (MS23); or
>
> **fully-decorated-missing regime:** every owner using D has `|S_y intersect X|=3`.   (MS24)

This is a finite structural split, not an eleven-view enumeration.

## 8. Coupling with the dense-block theorem

The same repeated support D is subject to `GLOBAL_REPEATED_SUPPORT_DENSE_BLOCK_THEOREM.md` independently of the missing sets.

For d=3, any repeated support has multiplicity

> `m<=8`.                                                     (MS25)

If D lies in the near-K3 regime, then `mu(D)<=1`, so the repeated-support block

`{p} union Y_D union D`

is a near-clique whose complement consists only of

- the three pivot--D nonedges;
- at most one internal D nonedge.

Thus high multiplicity forces a hereditary near-extremal dense block with at most four missing edges.

This is precisely an equality-rigidity object suitable for the final bridge.

## 9. What remains for the E334 eleven-view system

This theorem deliberately does not assume that the source-reported eleven views share one missing triple.

The unresolved translation is now smaller:

1. either the eleven-view system contains a high-multiplicity repeated core support, in which case Sections5--8 apply;
2. or its supports are mostly distinct, in which case one needs a multi-S extraction theorem controlling pairwise support intersections/cross-density;
3. any repeated class not entering the near-K3 regime must lie entirely in the fully-decorated-missing regime (MS24), which is itself a strong decoration-concentration condition.

Thus the multi-view bridge is reduced to **distinct-support extraction versus fully-decorated missing-set saturation**.

## 10. Relation to the front end

The proof of (MS5)--(MS15) uses only

- exact per-pivot gain/loss identities;
- incidence-induced decoration;
- exact lexicographic transport.

This is the same abstract mechanism sought for Q32/Q33 front-end correction compatibility. A front-end theorem would require identifying the corresponding labelled correction weight replacing `kappa(D)+mu+e(S,D)`, but the charging architecture itself is already multi-pivot and does not depend on common S.

## 11. Parameterized nature

Everything through Section6 is symbolic in

- h;
- the row sizes `d_y`;
- row allowances `a_y`;
- missing-set decoration counts `s_y`.

The r=12 numbers enter only in the E334 corollary. Therefore the multi-S charging theorem is a reusable candidate for higher-r pivot systems.